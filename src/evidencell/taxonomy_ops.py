"""Taxonomy update operations.

Managed field-level updates to taxonomy reference YAML files.
Each operation declares which fields it owns and only touches those.

Operations:
  add-expression   — write PrecomputedExpression blocks from HDF5 stats
  reingest         — re-ingest from source, preserving enrichment fields
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
ENRICHMENT_FIELDS: frozenset[str] = frozenset({
    "precomputed_expression",
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


# ── add-expression ────────────────────────────────────────────────────────────

def load_stats_h5(
    stats_path: str | Path,
) -> tuple[list[str], dict[str, int], Any]:
    """Load precomputed stats HDF5 and return (col_names, cluster_to_row, sum_matrix).

    col_names: list of Ensembl gene IDs (column index for sum matrix)
    cluster_to_row: {accession: row_index}
    sum_matrix: numpy array (n_clusters, n_genes) of mean expression values
    """
    import h5py

    f = h5py.File(str(stats_path), "r")
    col_names = json.loads(f["col_names"][()].decode())
    cluster_to_row = json.loads(f["cluster_to_row"][()].decode())
    sum_matrix = f["sum"][:]
    f.close()
    return col_names, cluster_to_row, sum_matrix


def load_gene_mapping(mapping_path: str | Path) -> dict[str, str]:
    """Load symbol → Ensembl ID mapping from a TSV file.

    Expected format: two columns, header row with 'symbol' and 'ensembl_id'.
    """
    mapping: dict[str, str] = {}
    with open(mapping_path, encoding="utf-8") as fh:
        header = fh.readline().strip().split("\t")
        sym_col = header.index("symbol")
        ens_col = header.index("ensembl_id")
        for line in fh:
            parts = line.strip().split("\t")
            if len(parts) > max(sym_col, ens_col):
                mapping[parts[sym_col]] = parts[ens_col]
    return mapping


def build_gene_mapping_from_tsv(mapping_path: str | Path) -> dict[str, str]:
    """Build symbol → Ensembl ID mapping from a TSV file.

    Alias for load_gene_mapping — provided for API consistency.
    """
    return load_gene_mapping(mapping_path)


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


def add_expression(
    taxonomy_id: str,
    stats_path: str | Path,
    genes: list[str],
    gene_mapping: dict[str, str],
    level: str = "cluster",
    accessions: list[str] | None = None,
) -> dict[str, Any]:
    """Add PrecomputedExpression blocks to taxonomy nodes.

    Parameters
    ----------
    taxonomy_id : str
        Target taxonomy (e.g. CCN20230722).
    stats_path : str | Path
        Path to precomputed_stats HDF5 file.
    genes : list[str]
        Gene symbols to extract expression for.
    gene_mapping : dict[str, str]
        symbol → Ensembl ID mapping.
    level : str
        Taxonomy level to update (default: "cluster").
    accessions : list[str] | None
        Specific node accessions to update. None = all nodes at this level.

    Returns
    -------
    dict with keys: updated (int), skipped (int), genes_found (int),
    genes_missing (list[str]).
    """
    stats_path = Path(stats_path)
    source_name = stats_path.name

    # Resolve symbols → Ensembl IDs
    gene_ens: list[tuple[str, str]] = []  # (symbol, ensembl_id)
    genes_missing: list[str] = []
    for sym in genes:
        ens = gene_mapping.get(sym)
        if ens:
            gene_ens.append((sym, ens))
        else:
            genes_missing.append(sym)

    if not gene_ens:
        raise ValueError(f"No genes could be resolved. Missing: {genes_missing}")

    # Load HDF5
    col_names, cluster_to_row, sum_matrix = load_stats_h5(stats_path)
    ens_to_col: dict[str, int] = {e: i for i, e in enumerate(col_names)}

    # Filter to genes present in HDF5
    gene_cols: list[tuple[str, str, int]] = []  # (symbol, ensembl_id, col_idx)
    for sym, ens in gene_ens:
        col = ens_to_col.get(ens)
        if col is not None:
            gene_cols.append((sym, ens, col))
        else:
            genes_missing.append(sym)

    if not gene_cols:
        raise ValueError(f"No genes found in HDF5. Missing: {genes_missing}")

    # Load taxonomy level YAML
    data = load_taxonomy_level(taxonomy_id, level)
    nodes = data.get("nodes", [])

    updated = 0
    skipped = 0
    for node in nodes:
        acc = node.get("cell_set_accession", "")
        if accessions and acc not in accessions:
            skipped += 1
            continue

        row_idx = cluster_to_row.get(acc)
        if row_idx is None:
            skipped += 1
            continue

        # Build GeneExpression list
        gene_entries: list[dict[str, Any]] = []
        for sym, ens, col in gene_cols:
            val = float(sum_matrix[row_idx, col])
            gene_entries.append({
                "symbol": sym,
                "ensembl_id": ens,
                "mean_expression": round(val, 2),
            })

        # Merge with existing genes[] — update by symbol, preserve others
        existing_expr = node.get("precomputed_expression", {})
        merged: dict[str, Any] = {g["symbol"]: g for g in existing_expr.get("genes", [])}
        for entry in gene_entries:
            merged[entry["symbol"]] = entry

        node["precomputed_expression"] = {
            "source": source_name,
            "level": level,
            "genes": list(merged.values()),
        }
        updated += 1

    # Save
    save_taxonomy_level(taxonomy_id, level, data)
    log.info(
        "add-expression: updated %d nodes, skipped %d, %d/%d genes resolved",
        updated, skipped, len(gene_cols), len(genes),
    )

    return {
        "updated": updated,
        "skipped": skipped,
        "genes_found": len(gene_cols),
        "genes_missing": genes_missing,
        "output_file": str(taxonomy_yaml_path(taxonomy_id, level)),
    }


# ── add-expression for supertypes (aggregated from clusters) ─────────────────

def add_expression_supertype(
    taxonomy_id: str,
    stats_path: str | Path,
    genes: list[str],
    gene_mapping: dict[str, str],
    accessions: list[str] | None = None,
    include_child_clusters: bool = True,
) -> dict[str, Any]:
    """Add PrecomputedExpression to supertype nodes with optional child cluster breakdown.

    For supertypes, the expression is the mean across child clusters (weighted by n_cells).
    Optionally includes per-child-cluster expression in child_cluster_expression.
    """
    import h5py
    import numpy as np

    stats_path = Path(stats_path)
    source_name = stats_path.name

    # Resolve genes
    gene_ens: list[tuple[str, str]] = []
    genes_missing: list[str] = []
    for sym in genes:
        ens = gene_mapping.get(sym)
        if ens:
            gene_ens.append((sym, ens))
        else:
            genes_missing.append(sym)

    if not gene_ens:
        raise ValueError(f"No genes resolved. Missing: {genes_missing}")

    # Load HDF5
    f = h5py.File(str(stats_path), "r")
    col_names = json.loads(f["col_names"][()].decode())
    cluster_to_row = json.loads(f["cluster_to_row"][()].decode())
    sum_matrix = f["sum"][:]
    n_cells = f["n_cells"][:]
    tree = json.loads(f["taxonomy_tree"][()].decode())
    f.close()

    ens_to_col = {e: i for i, e in enumerate(col_names)}

    gene_cols: list[tuple[str, str, int]] = []
    for sym, ens in gene_ens:
        col = ens_to_col.get(ens)
        if col is not None:
            gene_cols.append((sym, ens, col))
        else:
            genes_missing.append(sym)

    if not gene_cols:
        raise ValueError(f"No genes found in HDF5. Missing: {genes_missing}")

    # Build supertype → child clusters from taxonomy_tree
    # Find the supertype level key
    hierarchy = tree.get("hierarchy", [])
    supt_key = None
    for h in hierarchy:
        if "SUPT" in h:
            supt_key = h

    if not supt_key or supt_key not in tree:
        raise ValueError(f"Supertype level not found in taxonomy_tree. Keys: {list(tree.keys())}")

    supt_to_clusters: dict[str, list[str]] = {}
    supt_data = tree[supt_key]
    for supt_acc, children in supt_data.items():
        if isinstance(children, list):
            supt_to_clusters[supt_acc] = children
        elif isinstance(children, dict):
            # May be nested further
            supt_to_clusters[supt_acc] = list(children.keys())

    # Load supertype YAML
    data = load_taxonomy_level(taxonomy_id, "supertype")
    nodes = data.get("nodes", [])

    updated = 0
    skipped = 0
    for node in nodes:
        acc = node.get("cell_set_accession", "")
        if accessions and acc not in accessions:
            skipped += 1
            continue

        child_accs = supt_to_clusters.get(acc, [])
        if not child_accs:
            skipped += 1
            continue

        # Compute weighted mean across children
        child_rows = []
        child_ncells = []
        for ca in child_accs:
            row = cluster_to_row.get(ca)
            if row is not None:
                child_rows.append(row)
                child_ncells.append(n_cells[row])

        if not child_rows:
            skipped += 1
            continue

        weights = np.array(child_ncells, dtype=float)
        total_cells = weights.sum()
        if total_cells == 0:
            skipped += 1
            continue

        # Weighted mean expression per gene
        gene_entries: list[dict[str, Any]] = []
        for sym, ens, col in gene_cols:
            vals = sum_matrix[child_rows, col]
            wmean = float(np.average(vals, weights=weights))
            gene_entries.append({
                "symbol": sym,
                "ensembl_id": ens,
                "mean_expression": round(wmean, 2),
            })

        expr_block: dict[str, Any] = {
            "source": source_name,
            "level": "supertype",
            "genes": gene_entries,
        }

        # Optional child cluster breakdown
        if include_child_clusters:
            # Merge with existing child_cluster_expression by cluster_accession
            existing_expr = node.get("precomputed_expression", {})
            existing_children: dict[str, dict[str, Any]] = {
                e["cluster_accession"]: e
                for e in existing_expr.get("child_cluster_expression", [])
            }
            for ca in child_accs:
                row = cluster_to_row.get(ca)
                if row is None:
                    continue
                new_expr: dict[str, float] = {}
                for sym, ens, col in gene_cols:
                    new_expr[sym] = round(float(sum_matrix[row, col]), 2)
                if ca in existing_children:
                    # Merge expression dicts
                    old_expr = json.loads(existing_children[ca]["expression"])
                    old_expr.update(new_expr)
                    existing_children[ca] = {
                        "cluster_accession": ca,
                        "n_cells": int(n_cells[row]),
                        "expression": json.dumps(old_expr),
                    }
                else:
                    existing_children[ca] = {
                        "cluster_accession": ca,
                        "n_cells": int(n_cells[row]),
                        "expression": json.dumps(new_expr),
                    }
            child_entries = list(existing_children.values())
            if child_entries:
                expr_block["child_cluster_expression"] = child_entries

        # Merge top-level genes[] with existing by symbol
        existing_expr = node.get("precomputed_expression", {})
        merged_genes: dict[str, Any] = {g["symbol"]: g for g in existing_expr.get("genes", [])}
        for entry in gene_entries:
            merged_genes[entry["symbol"]] = entry
        expr_block["genes"] = list(merged_genes.values())

        node["precomputed_expression"] = expr_block
        updated += 1

    save_taxonomy_level(taxonomy_id, "supertype", data)
    log.info("add-expression (supertype): updated %d, skipped %d", updated, skipped)

    return {
        "updated": updated,
        "skipped": skipped,
        "genes_found": len(gene_cols),
        "genes_missing": genes_missing,
        "output_file": str(taxonomy_yaml_path(taxonomy_id, "supertype")),
    }


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

    Phase 1 commit 10: drives the proactive enrichment step that replaces
    per-mapping Step 2b. The set covers every gene any classical/literature
    node carries on its `defining_markers`, `neuropeptides`, or
    `negative_markers` fields, so that find-candidates always sees full
    quantitative data on candidates without a manual enrichment call.

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


def enrich_for_kb_marker_union(
    taxonomy_id: str,
    stats_path: str | Path,
    gene_mapping_path: str | Path,
    levels: list[str] | None = None,
) -> dict[str, Any]:
    """Batch-enrich every taxonomy node with `precomputed_expression` for
    the union of all KB-mentioned marker genes.

    Replaces the per-mapping Step 2b enrichment in workflows/map-cell-type.md
    so that find-candidates always sees full quantitative data on candidates
    without a manual call. Should be re-run when classical nodes are added
    or their marker lists change.

    Args:
        taxonomy_id: target taxonomy (e.g. CCN20230722).
        stats_path: path to the precomputed_stats HDF5 for this taxonomy.
        gene_mapping_path: gene mapping TSV (symbol → Ensembl).
        levels: list of taxonomy levels to enrich (default: ["cluster",
            "supertype"]). The supertype level also gets the
            `child_cluster_expression` block populated by add_expression_supertype.

    Returns:
        Summary dict with `taxonomy_id`, `n_genes`, `genes_used`,
        `genes_missing` (TSV mapping had no Ensembl), and per-level update
        counts.
    """
    if levels is None:
        levels = ["cluster", "supertype"]

    genes = sorted(collect_kb_marker_union())
    if not genes:
        return {
            "taxonomy_id": taxonomy_id,
            "n_genes": 0,
            "genes_used": [],
            "genes_missing": [],
            "by_level": {},
            "note": "No KB-mentioned marker genes found",
        }

    mapping = load_gene_mapping(gene_mapping_path)

    by_level: dict[str, dict] = {}
    for level in levels:
        if level == "supertype":
            res = add_expression_supertype(
                taxonomy_id=taxonomy_id,
                stats_path=stats_path,
                genes=genes,
                gene_mapping=mapping,
                accessions=None,
            )
        else:
            res = add_expression(
                taxonomy_id=taxonomy_id,
                stats_path=stats_path,
                genes=genes,
                gene_mapping=mapping,
                level=level,
                accessions=None,
            )
        by_level[level] = res

    # Genes the mapping couldn't resolve — same across calls; pick from cluster
    # path which always runs.
    genes_missing = by_level.get("cluster", {}).get("genes_missing", [])
    genes_used = [g for g in genes if g not in genes_missing]

    return {
        "taxonomy_id": taxonomy_id,
        "n_genes": len(genes),
        "genes_used": genes_used,
        "genes_missing": genes_missing,
        "by_level": by_level,
    }


def extract_at_f1_artifact(
    run_dir: str | Path,
    classical_node_id: str,
    source_cluster_label: str,
    region: str,
    f1_floor: float = 0.2,
    target_levels: list[str] | None = None,
) -> dict[str, Any]:
    """Extract a per-(classical, taxonomy) F1 artifact from a MapMyCells run dir.

    Reads ``{run_dir}/f1_matrix.csv`` (produced by ``annotation_transfer score``)
    and ``{run_dir}/manifest.yaml``, filters rows by source_label and F1 floor,
    resolves target labels to cell_set_accessions via the taxonomy DB, and writes

      research/{region}/at/{classical_node_id}_{taxonomy_id}_f1.json

    where the taxonomy_id is read from the manifest's ``target_taxonomy_id``.

    Args:
        run_dir: Path to ``kb/annotation_transfer_runs/{run_id}/``.
        classical_node_id: Classical node ID this artifact is keyed against.
        source_cluster_label: Filter the f1_matrix to rows whose ``source_label``
            equals this. Curator-supplied; the (source_label → classical_id)
            join is implicit at Phase 1.
        region: Region name for the output path.
        f1_floor: Minimum F1 to include (default 0.2).
        target_levels: Optional list of levels to include (e.g. ["cluster",
            "supertype"]). When None, all levels in f1_matrix are included.

    Returns:
        Summary dict with ``artifact_path``, ``hits`` count, ``run_id``,
        ``taxonomy_id``, and ``unresolved`` (list of target_names that
        could not be resolved to an accession).
    """
    from evidencell.paths import repo_root, taxonomy_db_path
    from evidencell.taxonomy_db import TaxonomyDB

    run_dir = Path(run_dir)
    f1_csv = run_dir / "f1_matrix.csv"
    manifest_path = run_dir / "manifest.yaml"
    if not f1_csv.exists():
        raise FileNotFoundError(f"f1_matrix.csv not found in {run_dir}")
    if not manifest_path.exists():
        raise FileNotFoundError(f"manifest.yaml not found in {run_dir}")

    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    taxonomy_id = manifest.get("target_taxonomy_id")
    if not taxonomy_id:
        raise ValueError(
            f"manifest at {manifest_path} missing 'target_taxonomy_id'"
        )
    run_id = manifest.get("id") or run_dir.name

    # Read f1_matrix.csv with the stdlib (no pandas dep at this layer).
    import csv as _csv
    rows: list[dict[str, Any]] = []
    with f1_csv.open(encoding="utf-8") as fh:
        reader = _csv.DictReader(fh)
        for r in reader:
            try:
                f1 = float(r.get("f1") or 0.0)
            except ValueError:
                continue
            if r.get("source_label") != source_cluster_label:
                continue
            if f1 < f1_floor:
                continue
            level = r.get("level") or ""
            if target_levels and level not in target_levels:
                continue
            try:
                n_cells = int(r.get("n_cells") or 0)
            except ValueError:
                n_cells = 0
            rows.append(
                {
                    "level": level,
                    "target_name": r.get("target_name") or "",
                    "f1": f1,
                    "n_cells": n_cells,
                    # Accept both new (coverage/purity) and legacy
                    # (group_purity/target_purity) CSV column names.
                    "coverage": float(
                        r.get("coverage") or r.get("group_purity") or 0.0
                    ),
                    "purity": float(
                        r.get("purity") or r.get("target_purity") or 0.0
                    ),
                }
            )

    # Resolve target_name → cell_set_accession via taxonomy DB.
    db_path = taxonomy_db_path(taxonomy_id)
    if not db_path.exists():
        raise FileNotFoundError(
            f"Taxonomy DB not found at {db_path}. Run: just build-taxonomy-db {taxonomy_id}"
        )
    db = TaxonomyDB(db_path)

    hits: list[dict[str, Any]] = []
    unresolved: list[str] = []
    with db._connect() as con:
        for r in rows:
            cur = con.execute(
                "SELECT node_id FROM nodes "
                "WHERE label = ? AND taxonomy_level = ? LIMIT 1",
                (r["target_name"], r["level"]),
            )
            match = cur.fetchone()
            if match is None:
                unresolved.append(f"{r['level']}: {r['target_name']}")
                continue
            hits.append(
                {
                    "target_accession": match[0],
                    "target_level": r["level"],
                    "target_name": r["target_name"],
                    "f1": r["f1"],
                    "n_cells": r["n_cells"],
                    "coverage": r["coverage"],
                    "purity": r["purity"],
                }
            )

    artifact = {
        "classical_node_id": classical_node_id,
        "taxonomy_id": taxonomy_id,
        "source_run_id": run_id,
        "source_cluster_label": source_cluster_label,
        "f1_floor": f1_floor,
        "hits": hits,
    }

    out_dir = repo_root() / "research" / region / "at"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{classical_node_id}_{taxonomy_id}_f1.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(artifact, fh, indent=2)
        fh.write("\n")

    return {
        "artifact_path": str(out_path.relative_to(repo_root())),
        "taxonomy_id": taxonomy_id,
        "run_id": run_id,
        "hits": len(hits),
        "unresolved": unresolved,
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

    # add-expression
    p_add = sub.add_parser(
        "add-expression",
        help="Add PrecomputedExpression blocks from HDF5 stats",
    )
    p_add.add_argument("taxonomy_id", help="Target taxonomy ID")
    p_add.add_argument("stats_h5", help="Path to precomputed_stats HDF5")
    p_add.add_argument("gene_mapping", help="Path to gene mapping TSV (symbol → ensembl_id)")
    p_add.add_argument(
        "genes", nargs="+",
        help="Gene symbols to extract expression for",
    )
    p_add.add_argument(
        "--level", default="cluster",
        help="Taxonomy level (default: cluster)",
    )
    p_add.add_argument(
        "--accessions", nargs="*",
        help="Specific node accessions (default: all at level)",
    )
    p_add.add_argument(
        "--supertype", action="store_true",
        help="Also compute supertype-level aggregated expression",
    )

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

    # enrich-marker-union: proactively enrich taxonomy with all KB-mentioned markers
    p_emu = sub.add_parser(
        "enrich-marker-union",
        help="Batch-enrich taxonomy nodes with KB-wide marker gene union",
    )
    p_emu.add_argument("taxonomy_id", help="Target taxonomy ID")
    p_emu.add_argument("stats_h5", help="Path to precomputed_stats HDF5")
    p_emu.add_argument("gene_mapping", help="Path to gene mapping TSV")
    p_emu.add_argument(
        "--levels", nargs="*",
        help="Taxonomy levels to enrich (default: cluster supertype)",
    )

    # at-extract-f1: produce per-(classical, taxonomy) F1 artifact for find-candidates
    p_atf1 = sub.add_parser(
        "at-extract-f1",
        help="Extract F1 hits from a MapMyCells run dir into a per-classical artifact",
    )
    p_atf1.add_argument(
        "run_dir", help="Path to kb/annotation_transfer_runs/{run_id}/"
    )
    p_atf1.add_argument(
        "classical_id", help="Classical node ID this artifact is keyed against"
    )
    p_atf1.add_argument(
        "source_cluster_label",
        help="Source label in f1_matrix.csv to filter on (e.g. 'Sst-OLM')",
    )
    p_atf1.add_argument(
        "region", help="Region (used in output path: research/{region}/at/...)"
    )
    p_atf1.add_argument(
        "--floor", type=float, default=0.2,
        help="Minimum F1 to include (default 0.2)",
    )
    p_atf1.add_argument(
        "--levels", nargs="*",
        help="Restrict to these target levels (default: all in f1_matrix)",
    )

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "add-expression":
        mapping = load_gene_mapping(args.gene_mapping)
        result = add_expression(
            taxonomy_id=args.taxonomy_id,
            stats_path=args.stats_h5,
            genes=args.genes,
            gene_mapping=mapping,
            level=args.level,
            accessions=args.accessions,
        )
        if args.supertype:
            st_result = add_expression_supertype(
                taxonomy_id=args.taxonomy_id,
                stats_path=args.stats_h5,
                genes=args.genes,
                gene_mapping=mapping,
                accessions=args.accessions,
            )
            result["supertype"] = st_result

        print(json.dumps(result, indent=2))

    elif args.command == "reingest":
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

    elif args.command == "enrich-marker-union":
        result = enrich_for_kb_marker_union(
            taxonomy_id=args.taxonomy_id,
            stats_path=args.stats_h5,
            gene_mapping_path=args.gene_mapping,
            levels=args.levels,
        )
        print(json.dumps(result, indent=2))

    elif args.command == "at-extract-f1":
        result = extract_at_f1_artifact(
            run_dir=args.run_dir,
            classical_node_id=args.classical_id,
            source_cluster_label=args.source_cluster_label,
            region=args.region,
            f1_floor=args.floor,
            target_levels=args.levels,
        )
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
