"""Refresh atlas-side expression on marker-family PropertyComparisons.

Many ``MappingEdge.property_comparisons[*]`` entries carry stale claims
like ``node_b_value: "not resolvable from atlas metadata"`` for markers
that DO have ``precomputed_expression`` values on the atlas node — the
claim was written before the precomputed-stats panel was loaded for
that taxonomy / gene. This module sweeps the KB and updates such PCs
with the current ``mean_expression`` value from the appropriate
taxonomy file (``cluster.yaml`` / ``supertype.yaml`` / ``subclass.yaml``
/ ``class.yaml``).

Scope (conservative — minimises curator surprise):

- Only ``marker_*`` / ``neuropeptide_*`` / ``tf_*`` / ``np_*`` /
  ``negative_marker_*`` PCs are considered.
- Only PCs whose current ``node_b_value`` matches a "no data" pattern
  (``not resolvable``, ``not available``, ``not assessed``, empty,
  ``-``, ``n/a``) get rewritten.
- Curator-set values (anything not matching the stale patterns) are
  left untouched.
- Alignments stay as-is — the human / agent who wrote the original
  alignment may have had grounds beyond expression. Surfacing the
  expression value lets a downstream consumer (gen-report agent) call
  out a likely re-assessment.

CLI::

    just refresh-expression GRAPH_FILE [--dry-run] [--all]

Without ``--all``, only ``GRAPH_FILE`` is processed; with ``--all``,
every YAML under ``kb/graphs/**`` is processed.

Protein → gene aliases (``mGluR1`` → ``Grm1`` etc.) are mapped via
``_PROTEIN_TO_GENE_ALIASES``. Extend as new aliases come up; the
fallback is the property suffix taken literally.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

# Protein → gene alias map lives in :mod:`marker_aliases`. Import the
# canonical mapping so the two refreshers (this module and
# stage_b_emit) stay in sync.
from .marker_aliases import PROTEIN_TO_GENE_ALIASES as _PROTEIN_TO_GENE_ALIASES
from .paths import repo_root


# Atlas accession prefix → taxonomy YAML filename
_ACCESSION_PREFIX_TO_YAML = {
    "CLAS_": "class.yaml",
    "SUBC_": "subclass.yaml",
    "SUPT_": "supertype.yaml",
    "CLUS_": "cluster.yaml",
}


_STALE_PATTERN = re.compile(
    r"not\s+(?:resolvable|available|assessed)|\bn/a\b|^\s*[-]\s*$|^\s*$",
    re.IGNORECASE,
)
_GENE_TOKEN_PATTERN = re.compile(r"\b([A-Z][a-zA-Z0-9-]+\d*)\b")


def _looks_stale(node_b_value: str) -> bool:
    if not node_b_value:
        return True
    return bool(_STALE_PATTERN.search(node_b_value))


def _candidate_gene_symbols(pc: dict) -> list[str]:
    """Return candidate gene symbols to look up in
    ``precomputed_expression`` for this PC, ordered by likelihood.

    Sources, in order:
    1. PC's ``property`` suffix (e.g. ``marker_Grm1`` → ``Grm1``).
    2. Protein-alias mapped from the suffix (``marker_mGluR1`` →
       ``Grm1``).
    3. Tokens extracted from ``node_a_value`` matching a mouse-gene
       capitalisation pattern.
    """
    out: list[str] = []
    seen: set[str] = set()

    def push(sym: str) -> None:
        if sym and sym not in seen:
            out.append(sym)
            seen.add(sym)

    prop = pc.get("property") or ""
    suffix = re.sub(
        r"^(marker_|neuropeptide_|tf_|np_|negative_marker_)",
        "",
        prop,
    )
    if suffix:
        push(suffix)
        if suffix in _PROTEIN_TO_GENE_ALIASES:
            push(_PROTEIN_TO_GENE_ALIASES[suffix])

    node_a = pc.get("node_a_value") or ""
    if isinstance(node_a, str):
        for m in _GENE_TOKEN_PATTERN.finditer(node_a):
            tok = m.group(1)
            push(tok)
            if tok in _PROTEIN_TO_GENE_ALIASES:
                push(_PROTEIN_TO_GENE_ALIASES[tok])
    return out


def _resolve_taxonomy_path(taxonomy_id: str, accession: str) -> Path | None:
    """Map a taxonomy accession to the appropriate ``{level}.yaml``
    file under ``kb/taxonomy/{taxonomy_id}/``. Returns None when the
    accession's level can't be inferred or the file is missing.
    """
    for prefix, fname in _ACCESSION_PREFIX_TO_YAML.items():
        if prefix in accession:
            p = repo_root() / "kb" / "taxonomy" / taxonomy_id / fname
            return p if p.exists() else None
    return None


def _load_precomputed_expression(
    taxonomy_yaml_path: Path, accession: str
) -> dict[str, float] | None:
    """Load ``{gene_symbol: mean_expression}`` for a single
    atlas-taxonomy node.

    Routes through the taxonomy SQLite DB's ``node_expression`` table
    (millisecond lookup) rather than re-parsing the level YAML file
    (~minutes for cluster.yaml.gz). The ``taxonomy_yaml_path``
    argument is retained in the signature for backwards-compat but
    used only to derive the taxonomy_id.

    Returns ``{symbol: mean_expression}``, or None if the DB doesn't
    exist / has no rows for this node.
    """
    from evidencell.paths import taxonomy_db_path
    from evidencell.taxonomy_db import TaxonomyDB

    # Path shape: kb/taxonomy/{taxonomy_id}/{level}.yaml(.gz).
    # Extract the taxonomy_id from the parent dir name.
    taxonomy_id = taxonomy_yaml_path.parent.name
    db_path = taxonomy_db_path(taxonomy_id)
    if not db_path.exists():
        return None
    db = TaxonomyDB(db_path)
    expr = db.get_node_expression(accession)
    return expr or None


def _format_expression_value(gene: str, mean: float) -> str:
    return f"{gene} mean_expression={mean:.2f}"


def refresh_edge(
    edge: dict,
    expr_cache: dict[tuple[str, str], dict[str, float] | None],
    taxonomy_id: str,
) -> list[dict[str, Any]]:
    """Inspect each marker-family PC on this edge; for any with a
    stale ``node_b_value``, look up the atlas-side expression and
    rewrite ``node_b_value`` if a gene match is found. Returns a list
    of change records (one per updated PC) for the audit log.
    """
    changes: list[dict[str, Any]] = []
    taxonomy_type = edge.get("taxonomy_type")
    if not taxonomy_type:
        return changes

    expr_key = (taxonomy_id, taxonomy_type)
    if expr_key not in expr_cache:
        path = _resolve_taxonomy_path(taxonomy_id, taxonomy_type)
        if path is None:
            expr_cache[expr_key] = None
        else:
            expr_cache[expr_key] = _load_precomputed_expression(
                path, taxonomy_type
            )
    expr = expr_cache[expr_key]
    if not expr:
        return changes

    for pc in edge.get("property_comparisons") or []:
        if not isinstance(pc, dict):
            continue
        prop = (pc.get("property") or "").lower()
        marker_family = (
            "marker_",
            "neuropeptide_",
            "tf_",
            "np_",
            "negative_marker_",
        )
        if not any(prop.startswith(p) for p in marker_family):
            continue
        old_b = pc.get("node_b_value") or ""
        if not _looks_stale(old_b):
            continue
        candidates = _candidate_gene_symbols(pc)
        for sym in candidates:
            if sym in expr:
                new_b = _format_expression_value(sym, expr[sym])
                pc["node_b_value"] = new_b
                changes.append(
                    {
                        "edge_id": edge.get("id"),
                        "property": pc.get("property"),
                        "gene": sym,
                        "mean_expression": expr[sym],
                        "old_node_b_value": old_b,
                        "new_node_b_value": new_b,
                    }
                )
                break  # first matching candidate wins
    return changes


def refresh_graph(
    path: Path,
    *,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Refresh expression PCs in a single KB graph file."""
    yaml_rt = YAML(typ="rt")
    yaml_rt.preserve_quotes = True
    yaml_rt.width = 4096
    yaml_rt.indent(mapping=2, sequence=4, offset=2)
    doc = yaml_rt.load(path)
    if doc is None:
        return {"file": str(path), "edges_seen": 0, "pcs_updated": 0,
                "changes": []}

    expr_cache: dict[tuple[str, str], dict[str, float] | None] = {}
    all_changes: list[dict[str, Any]] = []
    edges_seen = 0
    # The taxonomy_id lives on the atlas-side taxonomy node referenced
    # by `taxonomy_type`. Most graphs target one taxonomy; resolve per-edge.
    nodes_by_id: dict[str, dict] = {}
    for n in doc.get("nodes") or []:
        if isinstance(n, dict) and n.get("id"):
            nodes_by_id[n["id"]] = n

    for edge in doc.get("edges") or []:
        if not isinstance(edge, dict):
            continue
        edges_seen += 1
        # Look up taxonomy_id from the atlas-side node stub.
        tax_node = nodes_by_id.get(edge.get("taxonomy_type") or "")
        if not isinstance(tax_node, dict):
            continue
        taxonomy_id = tax_node.get("taxonomy_id")
        if not taxonomy_id:
            continue
        changes = refresh_edge(edge, expr_cache, taxonomy_id)
        all_changes.extend(changes)

    if all_changes and not dry_run:
        with path.open("w", encoding="utf-8") as fh:
            yaml_rt.dump(doc, fh)

    return {
        "file": str(path),
        "edges_seen": edges_seen,
        "pcs_updated": len(all_changes),
        "changes": all_changes,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.refresh_expression_pcs",
        description=(
            "Refresh atlas-side expression on marker-family "
            "property_comparisons. Looks up mean_expression in the "
            "appropriate kb/taxonomy/{id}/{level}.yaml and rewrites "
            "stale 'not resolvable from atlas metadata' node_b_values."
        ),
    )
    parser.add_argument(
        "graph_file",
        type=Path,
        nargs="?",
        default=None,
        help="Single KB graph YAML to refresh; omit + use --all to sweep.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process every YAML under kb/graphs/**.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change; do not edit YAML.",
    )
    args = parser.parse_args(argv)

    if not args.graph_file and not args.all:
        parser.error("Provide GRAPH_FILE or --all.")
    if args.graph_file and args.all:
        parser.error("Use one of GRAPH_FILE or --all, not both.")

    if args.all:
        paths = sorted((repo_root() / "kb" / "graphs").rglob("*.yaml"))
    else:
        paths = [args.graph_file]

    grand_total_updates = 0
    grand_changes: list[dict[str, Any]] = []
    for path in paths:
        result = refresh_graph(path, dry_run=args.dry_run)
        if result["pcs_updated"]:
            print(f"{path}: {result['pcs_updated']} PC(s) updated")
            for c in result["changes"]:
                print(
                    f"  - {c['edge_id']} :: {c['property']} "
                    f"→ {c['new_node_b_value']}"
                )
        grand_total_updates += result["pcs_updated"]
        grand_changes.extend(result["changes"])
    print()
    print(f"GRAND TOTAL: {grand_total_updates} PC(s) updated"
          f"{' (dry-run)' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
