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

from evidencell.paths import taxonomy_dir, taxonomy_yaml_path
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
    """
    path = taxonomy_yaml_path(taxonomy_id, level)
    if not path.exists():
        raise FileNotFoundError(f"Taxonomy file not found: {path}")
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def save_taxonomy_level(taxonomy_id: str, level: str, data: dict[str, Any]) -> Path:
    """Write a TaxonomyNodeList dict back to YAML."""
    path = taxonomy_yaml_path(taxonomy_id, level)
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


# ── CLI ──────────────────────────────────────────────────────────────────────

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


if __name__ == "__main__":
    main()
