"""Taxonomy update operations.

Managed field-level updates to taxonomy reference YAML files.
Each operation declares which fields it owns and only touches those.

Operations:
  reingest               — re-ingest from source, preserving enrichment fields
  warm-expression-cache  — pre-load the KB marker union into the taxonomy DB's
                           expression cache (optional; the cache fills on use)

Atlas expression is not stored in taxonomy YAML (#189): it is read on demand
from the MapMyCells stats HDF5 and cached in the taxonomy SQLite DB — see
``evidencell.expression_cache``.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

import yaml

from evidencell.paths import (
    at_run_index_path,
    at_runs_dir,
    open_taxonomy_yaml,
    taxonomy_dir,
    taxonomy_yaml_path,
)
from evidencell.expression_cache import load_gene_mapping  # noqa: F401  (re-export)
from evidencell.taxonomy_db import ingest_to_yaml, ingest_cas_to_yaml, _is_cas_format

log = logging.getLogger(__name__)

# ── Field ownership ──────────────────────────────────────────────────────────

# Fields written by standard ingest (flush-and-replace).
# reingest() replaces these from the new source.
INGEST_FIELDS: frozenset[str] = frozenset({
    "id",
    "name",
    "cell_set_accession",
    "taxonomy_id",
    "taxonomy_level",
    "taxonomy_rank",
    "definition_basis",
    "is_terminal",
    "parent_hierarchy",
    "nt_type",
    "markers",
    "cl_mapping",
    "anatomical_location",
    "neighborhood",
    "male_female_ratio",
    "n_cells",
    "species",
    "cell_set_designation",
    "rationale_dois",
    "ccf_distribution",
})

# Fields written by enrichment operations (preserved across re-ingest).
# Expression is not one of them: it lives in the taxonomy DB's on-demand
# cache, not in YAML (#189), so re-ingest cannot lose it.
ENRICHMENT_FIELDS: frozenset[str] = frozenset({
    "electrophysiology",
    "morphology",
    "defining_markers",
    "negative_markers",
    "neuropeptides",
    "definition_references",
})


# ── YAML I/O ─────────────────────────────────────────────────────────────────

def load_taxonomy_level(taxonomy_id: str, level: str) -> dict[str, Any]:
    """Load a TaxonomyNodeList YAML file and return the raw dict.

    Returns dict with keys: taxonomy_id, taxonomy_level, taxonomy_rank, nodes.
    Handles both `.yaml` and `.yaml.gz` paths via the shared helper.
    """
    path = taxonomy_yaml_path(taxonomy_id, level)
    if not path.exists():
        raise FileNotFoundError(f"Taxonomy file not found: {path}")
    with open_taxonomy_yaml(path) as fh:
        return yaml.safe_load(fh) or {}


def save_taxonomy_level(taxonomy_id: str, level: str, data: dict[str, Any]) -> Path:
    """Write a TaxonomyNodeList dict back to YAML.

    Preserves on-disk compression: if the existing file at the resolved
    path is `.yaml.gz`, the rewrite stays gzipped; otherwise plain
    `.yaml`. (`taxonomy_yaml_path` returns the `.gz` variant when it
    exists, so existing-gzipped-stays-gzipped is automatic.)
    """
    import gzip
    path = taxonomy_yaml_path(taxonomy_id, level)
    if str(path).endswith(".gz"):
        with gzip.open(path, "wt", encoding="utf-8") as fh:
            yaml.dump(data, fh, allow_unicode=True, sort_keys=False, default_flow_style=False)
    else:
        with path.open("w", encoding="utf-8") as fh:
            yaml.dump(data, fh, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return path


def _index_nodes(nodes: list[dict]) -> dict[str, dict]:
    """Build accession → node dict for fast lookup."""
    idx: dict[str, dict] = {}
    for n in nodes:
        acc = n.get("cell_set_accession") or n.get("id", "")
        if acc:
            idx[acc] = n
    return idx


# ── gene mapping ──────────────────────────────────────────────────────────────

def generate_gene_mapping_tsv(
    stats_path: str | Path,
    output_path: str | Path,
) -> Path:
    """Generate a gene mapping TSV from HDF5 col_names using mygene.

    Requires: pip install mygene
    Queries the MyGene.info API to resolve Ensembl IDs → gene symbols.
    Writes a TSV with columns: ensembl_id, symbol.
    """
    import h5py

    f = h5py.File(str(stats_path), "r")
    col_names = json.loads(f["col_names"][()].decode())
    f.close()

    try:
        import mygene  # type: ignore[import-untyped]
    except ImportError:
        raise ImportError(
            "mygene required for gene mapping generation. "
            "Install with: uv add mygene"
        )

    mg = mygene.MyGeneInfo()
    results = mg.querymany(
        col_names,
        scopes="ensembl.gene",
        fields="symbol",
        species="mouse",
        returnall=True,
    )

    out = Path(output_path)
    n_mapped = 0
    with out.open("w", encoding="utf-8") as fh:
        fh.write("ensembl_id\tsymbol\n")
        for hit in results["out"]:
            if "symbol" in hit and "query" in hit:
                fh.write(f"{hit['query']}\t{hit['symbol']}\n")
                n_mapped += 1

    log.info("Wrote %d/%d gene mappings to %s", n_mapped, len(col_names), out)
    return out


# ── reingest ──────────────────────────────────────────────────────────────────

def reingest(
    taxonomy_id: str,
    source_json: str | Path,
    preserve_fields: frozenset[str] | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Re-ingest taxonomy from source JSON, preserving enrichment fields.

    1. Runs standard ingest to a temp location.
    2. Loads old (enriched) and new (fresh) YAML per level.
    3. For each node matched by accession:
       - Ingest-owned fields: take from new.
       - Preserved fields: keep from old.
    4. Nodes in new but not old: add as-is.
    5. Nodes in old but not new: flagged for review (kept with warning).

    Parameters
    ----------
    taxonomy_id : str
        Target taxonomy.
    source_json : str | Path
        Path to new source JSON (WMBv1 or CAS format).
    preserve_fields : frozenset[str] | None
        Fields to preserve from old data. Defaults to ENRICHMENT_FIELDS.
    dry_run : bool
        If True, report changes without writing.

    Returns
    -------
    dict with keys: levels_processed, nodes_updated, nodes_added,
    nodes_removed (flagged), fields_preserved.
    """
    import tempfile

    if preserve_fields is None:
        preserve_fields = ENRICHMENT_FIELDS

    source_json = Path(source_json)
    tax_dir = taxonomy_dir(taxonomy_id)

    # Step 1: Ingest to temp directory
    with tempfile.TemporaryDirectory(prefix="reingest_") as tmp:
        tmp_dir = Path(tmp)

        # Detect format and run standard ingest
        with source_json.open(encoding="utf-8") as fh:
            data = json.load(fh)

        if _is_cas_format(data):
            ingest_cas_to_yaml(source_json, taxonomy_id, tmp_dir)
        else:
            ingest_to_yaml(source_json, taxonomy_id, tmp_dir)

        # Step 2: Merge per level
        result: dict[str, Any] = {
            "levels_processed": [],
            "nodes_updated": 0,
            "nodes_added": 0,
            "nodes_removed_flagged": 0,
            "fields_preserved": sorted(preserve_fields),
            "dry_run": dry_run,
        }

        for new_yaml in tmp_dir.glob("*.yaml"):
            if new_yaml.name == "taxonomy_meta.yaml":
                if not dry_run:
                    # Update metadata (ingest-owned)
                    _merge_meta(tax_dir / "taxonomy_meta.yaml", new_yaml)
                continue

            level_name = new_yaml.stem  # e.g. "cluster", "supertype"
            old_yaml = tax_dir / new_yaml.name

            new_data = yaml.safe_load(new_yaml.read_text(encoding="utf-8")) or {}
            new_nodes = new_data.get("nodes", [])

            if old_yaml.exists():
                old_data = yaml.safe_load(old_yaml.read_text(encoding="utf-8")) or {}
                old_nodes = old_data.get("nodes", [])
            else:
                old_data = {}
                old_nodes = []

            merged, stats = _merge_nodes(old_nodes, new_nodes, preserve_fields)
            result["levels_processed"].append(level_name)
            result["nodes_updated"] += stats["updated"]
            result["nodes_added"] += stats["added"]
            result["nodes_removed_flagged"] += stats["removed_flagged"]

            if not dry_run:
                # Write merged data
                out_data = {
                    k: v for k, v in new_data.items() if k != "nodes"
                }
                out_data["nodes"] = merged
                save_taxonomy_level(taxonomy_id, level_name, out_data)

            log.info(
                "reingest %s/%s: %d updated, %d added, %d flagged",
                taxonomy_id, level_name,
                stats["updated"], stats["added"], stats["removed_flagged"],
            )

    return result


def _merge_nodes(
    old_nodes: list[dict],
    new_nodes: list[dict],
    preserve_fields: frozenset[str],
) -> tuple[list[dict], dict[str, int]]:
    """Merge old and new node lists, preserving enrichment fields.

    Returns (merged_nodes, stats).
    """
    old_idx = _index_nodes(old_nodes)
    new_idx = _index_nodes(new_nodes)

    stats = {"updated": 0, "added": 0, "removed_flagged": 0}
    merged: list[dict] = []

    # Process all new nodes (preserving new ordering)
    for node in new_nodes:
        acc = node.get("cell_set_accession") or node.get("id", "")
        old_node = old_idx.get(acc)

        if old_node is not None:
            # Merge: take ingest fields from new, preserve enrichment from old
            for field in preserve_fields:
                if field in old_node and field not in node:
                    node[field] = old_node[field]
            stats["updated"] += 1
        else:
            stats["added"] += 1

        merged.append(node)

    # Flag nodes in old but not in new
    new_accs = set(new_idx.keys())
    for acc, old_node in old_idx.items():
        if acc not in new_accs:
            # Keep with a warning marker
            old_node["_reingest_status"] = "REMOVED_IN_NEW_SOURCE"
            merged.append(old_node)
            stats["removed_flagged"] += 1
            log.warning("Node %s in old but not new — flagged for review", acc)

    return merged, stats


def _merge_meta(old_path: Path, new_path: Path) -> None:
    """Merge taxonomy metadata: take new ingest fields, preserve custom additions."""
    if old_path.exists():
        old = yaml.safe_load(old_path.read_text(encoding="utf-8")) or {}
    else:
        old = {}

    new = yaml.safe_load(new_path.read_text(encoding="utf-8")) or {}

    # Preserve mapmycells config from old (set by at-download-taxonomy)
    if "mapmycells" in old and "mapmycells" not in new:
        new["mapmycells"] = old["mapmycells"]

    with old_path.open("w", encoding="utf-8") as fh:
        yaml.dump(new, fh, allow_unicode=True, sort_keys=False)


# ── AT run registry ──────────────────────────────────────────────────────────

def build_at_index() -> dict[str, Any]:
    """Build (or rebuild) the AT run registry index from manifest files.

    Scans ``kb/annotation_transfer_runs/*/manifest.yaml``, reads each manifest,
    and writes ``kb/annotation_transfer_runs/index.yaml`` with one entry per run
    keyed by the run ``id`` declared in the manifest.

    Returns a summary dict with ``indexed`` (int) and ``skipped`` (list of paths).
    """
    runs_dir = at_runs_dir()
    index_path = at_run_index_path()

    indexed: dict[str, dict[str, str]] = {}
    skipped: list[str] = []

    for manifest in sorted(runs_dir.glob("*/manifest.yaml")):
        try:
            data = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            skipped.append(f"{manifest}: {exc}")
            continue

        run_id = data.get("id")
        if not run_id:
            skipped.append(f"{manifest}: missing 'id' field")
            continue

        # Relative path from repo root for portability
        try:
            rel = manifest.relative_to(runs_dir.parent.parent)
        except ValueError:
            rel = manifest

        indexed[run_id] = {
            "id": run_id,
            "target_taxonomy_id": data.get("target_taxonomy_id", ""),
            "source_dataset_accession": data.get("source_dataset_accession", ""),
            "manifest_path": str(rel),
        }

    header = (
        "# Auto-generated by `just register-at-run`. Do not edit manually.\n"
        "# Regenerate after adding a new AT run: just register-at-run\n"
    )
    # Emit as list (LinkML AnnotationTransferIndex / AnnotationTransferRunSummary)
    index_doc = {"runs": [indexed[k] for k in sorted(indexed)]}
    with index_path.open("w", encoding="utf-8") as fh:
        fh.write(header)
        yaml.dump(index_doc, fh, allow_unicode=True, sort_keys=False)

    log.info("build-at-index: indexed %d runs, skipped %d", len(indexed), len(skipped))
    return {"indexed": len(indexed), "run_ids": sorted(indexed), "skipped": skipped}


def at_back_index() -> dict[str, list[str]]:
    """Return a mapping from AT run_id → list of KB YAML file paths that cite it.

    Generated on demand by scanning all KB YAML files for ``run_ref`` fields.
    """
    from evidencell.paths import repo_root

    root = repo_root()
    back: dict[str, list[str]] = {}

    for kb_yaml in sorted((root / "kb").rglob("*.yaml")):
        try:
            doc = yaml.safe_load(kb_yaml.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        run_refs = _collect_run_refs(doc)
        for ref in run_refs:
            back.setdefault(ref, []).append(str(kb_yaml.relative_to(root)))

    return back


def _collect_run_refs(obj: object, result: list[str] | None = None) -> list[str]:
    """Recursively collect all ``run_ref`` string values from a nested dict/list."""
    if result is None:
        result = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "run_ref" and isinstance(v, str) and v:
                result.append(v)
            else:
                _collect_run_refs(v, result)
    elif isinstance(obj, list):
        for item in obj:
            _collect_run_refs(item, result)
    return result


# ── CLI ──────────────────────────────────────────────────────────────────────

def collect_kb_marker_union() -> set[str]:
    """Scan kb/graphs/**/*.yaml for non-atlas nodes and return the union of
    all marker gene symbols mentioned across them.

    Drives ``warm_expression_cache``. The set covers every gene any
    classical/literature node carries on its `defining_markers`,
    `neuropeptides`, or `negative_markers` fields.

    Atlas nodes (`definition_basis: ATLAS_TRANSCRIPTOMIC`) are skipped —
    their markers come from the taxonomy ingest itself, not from the KB
    side. Files that fail to parse are logged and skipped.
    """
    from evidencell.paths import repo_root

    root = repo_root()
    graphs_dir = root / "kb" / "graphs"
    if not graphs_dir.exists():
        return set()

    out: set[str] = set()
    for yaml_path in sorted(graphs_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:  # noqa: BLE001
            log.warning("Failed to parse %s: %s — skipping", yaml_path, exc)
            continue
        nodes = doc.get("nodes") or []
        for nd in nodes:
            if not isinstance(nd, dict):
                continue
            if nd.get("definition_basis") == "ATLAS_TRANSCRIPTOMIC":
                continue
            for field in ("defining_markers", "neuropeptides", "negative_markers"):
                for m in nd.get(field) or []:
                    sym = m.get("symbol") if isinstance(m, dict) else m
                    if sym:
                        out.add(sym)
    return out


def warm_expression_cache(taxonomy_id: str) -> dict[str, Any]:
    """Pre-load the KB marker union into the taxonomy DB's expression cache.

    Optional: the cache fills on first use by find-candidates / emit-stage-b
    / refresh-*. Warming once avoids per-gene loads spread across those runs
    and surfaces every not-measured gene up front.
    """
    from evidencell.taxonomy_db import TaxonomyDB, require_taxonomy_db

    genes = sorted(collect_kb_marker_union())
    db = TaxonomyDB(require_taxonomy_db(taxonomy_id))
    lookup = db.expression(genes, accessions=[])
    return {
        "taxonomy_id": taxonomy_id,
        "n_genes": len(genes),
        "n_measured": len(genes) - len(lookup.not_measured),
        "not_measured": dict(sorted(lookup.not_measured.items())),
        "source_file": lookup.source_file,
    }


def main() -> None:
    """CLI entry point for taxonomy update operations."""
    import argparse
    import sys

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    parser = argparse.ArgumentParser(
        prog="python -m evidencell.taxonomy_ops",
        description="Taxonomy update operations",
    )
    sub = parser.add_subparsers(dest="command")

    # reingest
    p_re = sub.add_parser(
        "reingest",
        help="Re-ingest taxonomy preserving enrichment fields",
    )
    p_re.add_argument("taxonomy_id", help="Target taxonomy ID")
    p_re.add_argument("source_json", help="Path to new source JSON")
    p_re.add_argument(
        "--preserve", nargs="*",
        help="Additional fields to preserve (added to defaults)",
    )
    p_re.add_argument(
        "--dry-run", action="store_true",
        help="Report changes without writing",
    )

    # generate-gene-mapping
    p_gm = sub.add_parser(
        "generate-gene-mapping",
        help="Generate gene mapping TSV from HDF5 via mygene",
    )
    p_gm.add_argument("stats_h5", help="Path to precomputed_stats HDF5")
    p_gm.add_argument("output", help="Output TSV path")

    # build-at-index
    sub.add_parser(
        "build-at-index",
        help="Build/rebuild kb/annotation_transfer_runs/index.yaml from manifest files",
    )

    # warm-expression-cache: pre-load the KB marker union into the DB cache
    p_warm = sub.add_parser(
        "warm-expression-cache",
        help="Pre-load expression for every KB-mentioned marker into the taxonomy DB cache",
    )
    p_warm.add_argument("taxonomy_id", help="Target taxonomy ID")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "reingest":
        preserve = ENRICHMENT_FIELDS
        if args.preserve:
            preserve = preserve | frozenset(args.preserve)

        result = reingest(
            taxonomy_id=args.taxonomy_id,
            source_json=args.source_json,
            preserve_fields=preserve,
            dry_run=args.dry_run,
        )
        print(json.dumps(result, indent=2))

    elif args.command == "generate-gene-mapping":
        out = generate_gene_mapping_tsv(args.stats_h5, args.output)
        print(f"Gene mapping written to {out}")

    elif args.command == "build-at-index":
        result = build_at_index()
        print(json.dumps(result, indent=2))

    elif args.command == "warm-expression-cache":
        from evidencell.expression_cache import ExpressionUnavailable

        try:
            result = warm_expression_cache(args.taxonomy_id)
        except ExpressionUnavailable as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            sys.exit(1)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
