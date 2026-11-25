"""Refresh atlas-side expression on marker-family PropertyComparisons.

Many ``MappingEdge.property_comparisons[*]`` entries carry stale claims
like ``node_b_value: "not resolvable from atlas metadata"`` for markers
that DO have measured expression on the atlas node — the claim was
written before expression was available for that taxonomy / gene. This
module sweeps the KB and updates such PCs with the current mean
expression, read through ``TaxonomyDB.expression`` (the on-demand
accessor over the MapMyCells stats file, #189).

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

Marker names (``mGluR1``, ``PV``, ``Sst``) resolve to atlas genes in
``TaxonomyDB.expression`` through the gene identity tables (#216), pinned
by the classical marker's ``ncbi_gene_id`` where it has one. The rewritten
value names the atlas gene symbol the name resolved to.

A PC whose property names a curated marker (one with a pin, or curated as
having no single gene) is looked up by that marker only. Otherwise words
from ``node_a_value`` are tried too, but a word counts only as an exact
gene symbol: free text is not run through synonym or case-insensitive
matching (``In`` is a synonym of Ahr).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Mapping

from .gene_identity import EXACT_SYMBOL, marker_gene_ids
from .kb_io import roundtrip_yaml
from .paths import repo_root


_STALE_PATTERN = re.compile(
    r"not\s+(?:resolvable|available|assessed)|\bn/a\b|^\s*[-]\s*$|^\s*$",
    re.IGNORECASE,
)
_GENE_TOKEN_PATTERN = re.compile(r"\b([A-Z][a-zA-Z0-9-]+\d*)\b")


def _looks_stale(node_b_value: str) -> bool:
    if not node_b_value:
        return True
    return bool(_STALE_PATTERN.search(node_b_value))


def _candidate_gene_symbols(
    pc: dict, gene_ids: Mapping[str, Any] | None = None
) -> list[tuple[str, bool]]:
    """Return ``(name, from_text)`` candidates to look up atlas expression
    for this PC, ordered by likelihood.

    Sources, in order:
    1. PC's ``property`` suffix (e.g. ``marker_Grm1`` → ``Grm1``,
       ``marker_mGluR1`` → ``mGluR1``, resolved to Grm1 downstream).
       When the suffix is a curated marker (a key of ``gene_ids``), it is
       the only candidate: its pin decides, and a marker curated as having
       no single gene stays unmeasured.
    2. Tokens extracted from ``node_a_value`` matching a mouse-gene
       capitalisation pattern (``from_text``; accepted downstream only as
       an exact gene symbol).
    """
    out: list[tuple[str, bool]] = []
    seen: set[str] = set()

    def push(sym: str, from_text: bool) -> None:
        if sym and sym not in seen:
            out.append((sym, from_text))
            seen.add(sym)

    prop = pc.get("property") or ""
    suffix = re.sub(
        r"^(marker_|neuropeptide_|tf_|np_|negative_marker_)",
        "",
        prop,
    )
    if suffix:
        push(suffix, False)
        if suffix in (gene_ids or {}):
            return out

    node_a = pc.get("node_a_value") or ""
    if isinstance(node_a, str):
        for m in _GENE_TOKEN_PATTERN.finditer(node_a):
            push(m.group(1), True)
    return out


def _load_expression(
    taxonomy_id: str,
    accession: str,
    symbols: list[str],
    gene_ids: Mapping[str, Any] | None = None,
) -> tuple[dict[str, float], dict[str, str], dict[str, str]]:
    """``({name: mean_expression}, {name: atlas gene symbol},
    {name: resolution method})`` for one atlas node, through the on-demand
    accessor (uncached genes load from the stats file)."""
    from evidencell.taxonomy_db import TaxonomyDB, require_taxonomy_db

    db = TaxonomyDB(require_taxonomy_db(taxonomy_id))
    lookup = db.expression(symbols, accessions=[accession], gene_ids=gene_ids)
    return (
        lookup.for_node(accession),
        {name: sym for name in symbols if (sym := lookup.gene_symbol(name)) is not None},
        {name: m.method for name, m in lookup.genes.items()},
    )


def _format_expression_value(gene: str, mean: float) -> str:
    return f"{gene} mean_expression={mean:.2f}"


_MARKER_FAMILY = (
    "marker_",
    "neuropeptide_",
    "tf_",
    "np_",
    "negative_marker_",
)


def refresh_edge(
    edge: dict, taxonomy_id: str, gene_ids: Mapping[str, Any] | None = None
) -> list[dict[str, Any]]:
    """Inspect each marker-family PC on this edge; for any with a
    stale ``node_b_value``, look up the atlas-side expression and
    rewrite ``node_b_value`` if a gene match is found. ``gene_ids`` pins
    marker names to the classical node's curated ``ncbi_gene_id``.
    Returns a list of change records (one per updated PC) for the audit
    log.
    """
    changes: list[dict[str, Any]] = []
    taxonomy_type = edge.get("taxonomy_type")
    if not taxonomy_type:
        return changes

    stale: list[tuple[dict, list[tuple[str, bool]]]] = []
    for pc in edge.get("property_comparisons") or []:
        if not isinstance(pc, dict):
            continue
        prop = (pc.get("property") or "").lower()
        if not any(prop.startswith(p) for p in _MARKER_FAMILY):
            continue
        if not _looks_stale(pc.get("node_b_value") or ""):
            continue
        stale.append((pc, _candidate_gene_symbols(pc, gene_ids)))
    if not stale:
        return changes

    symbols = list(dict.fromkeys(sym for _, cands in stale for sym, _ in cands))
    expr, atlas_symbols, methods = _load_expression(
        taxonomy_id, taxonomy_type, symbols, gene_ids
    )
    if not expr:
        return changes

    for pc, candidates in stale:
        old_b = pc.get("node_b_value") or ""
        for sym, from_text in candidates:
            if from_text and methods.get(sym) != EXACT_SYMBOL:
                continue
            if sym in expr:
                gene = atlas_symbols.get(sym, sym)
                new_b = _format_expression_value(gene, expr[sym])
                pc["node_b_value"] = new_b
                changes.append(
                    {
                        "edge_id": edge.get("id"),
                        "property": pc.get("property"),
                        "gene": gene,
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
    yaml_rt = roundtrip_yaml()
    doc = yaml_rt.load(path)
    if doc is None:
        return {"file": str(path), "edges_seen": 0, "pcs_updated": 0,
                "changes": []}

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
        classical = nodes_by_id.get(edge.get("lit_type") or "")
        changes = refresh_edge(
            edge, taxonomy_id, marker_gene_ids(classical) if isinstance(classical, dict) else None
        )
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
            "property_comparisons. Reads mean expression through the "
            "taxonomy DB's on-demand expression cache and rewrites "
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

    from evidencell.expression_cache import ExpressionUnavailable

    try:
        if len(paths) > 1 and not args.dry_run:
            # Preflight: a dry pass loads every needed gene before the first
            # write, so a missing stats file stops the sweep with nothing
            # half-written. The real pass then reads from the cache.
            for path in paths:
                refresh_graph(path, dry_run=True)
        return _refresh_paths(paths, dry_run=args.dry_run)
    except ExpressionUnavailable as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


def _refresh_paths(paths: list[Path], *, dry_run: bool) -> int:
    grand_total_updates = 0
    grand_changes: list[dict[str, Any]] = []
    for path in paths:
        result = refresh_graph(path, dry_run=dry_run)
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
          f"{' (dry-run)' if dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
