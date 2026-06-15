"""Refresh stale ``property_comparisons`` + ``discovery_score`` on
existing edges using current Stage A scoring + Stage B emission rules.

Narrow scope: this tool exists to fix edges authored by the pre-2026-05
LLM Step 3 mapping subagent (which decided per-marker alignment by
checking whether the gene appeared in the atlas's ``defining_markers``
JSON list rather than by consulting ``precomputed_expression``
quantitatively). The current mechanical Stage B emitter
(``stage_b_emit``) does this correctly; this module backfills its
output onto edges that predate it.

Matches existing edges by ``(lit_type, taxonomy_type)`` biological
identity, NOT by ``edge.id``. So legacy lowercase-accession edges
(e.g. ``edge_olm_to_wmb_clus_0769``) are picked up just as well as
edges using the current emitter's ID format.

Refreshes exactly two fields per matched edge:
- ``edge.property_comparisons``
- ``edge.discovery_score``

Leaves byte-identical:
- ``evidence[]`` (including any AT evidence with rich
  ``source_groups[*].rationale``)
- Rationale-suite (``confidence``, ``confidence_score``, ``rationale``,
  ``relationship``, ``mapping_cardinality``, ``mapping_justification``,
  ``caveats``, ``proposed_experiments``, ``unresolved_questions``,
  ``report_path``, ``rationale_generated_at``,
  ``rationale_source_hash``, ``reconciliation_note``)
- ``curator``, ``reviewed_by``
- ``id``, ``lit_type``, ``taxonomy_type``

CLI::

    just refresh-property-comparisons GRAPH NODE TAXONOMY RANK [--dry-run]

Closes #103.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

from evidencell.stage_b_emit import emit_stage_b


def _yaml_rt() -> YAML:
    """Match the rt config used elsewhere in evidencell so quote-style
    is preserved across the file (avoids the underscore-float coercion
    bug on quote_keys)."""
    y = YAML(typ="rt")
    y.preserve_quotes = True
    y.width = 4096
    y.indent(mapping=2, sequence=4, offset=2)
    return y


def refresh_property_comparisons(
    graph_file: Path,
    classical_node_id: str,
    taxonomy_id: str,
    rank: int,
    *,
    top_k: int = 30,
    discovery_json_path: Path | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Refresh ``property_comparisons`` + ``discovery_score`` on
    existing edges for ``classical_node_id`` in ``graph_file``.

    Parameters
    ----------
    graph_file : Path
        KB graph YAML (e.g. ``kb/graphs/hippocampus/hippocampus_OLM.yaml``).
    classical_node_id : str
        ID of the classical node whose edges should be refreshed.
    taxonomy_id : str
        Target taxonomy (e.g. ``CCN20230722``).
    rank : int
        Taxonomy rank to score against (0 = cluster, 1 = supertype).
    top_k : int
        Number of fresh candidates to surface from Stage A. Default 30
        is generously large to cover most legacy-edge taxonomy_types.
        Edges whose ``taxonomy_type`` doesn't appear in the fresh top-K
        are skipped (left untouched) and reported in the summary.
    discovery_json_path : Path | None
        Override the canonical discovery JSON path. ``None`` = let
        ``emit_stage_b`` resolve it.
    dry_run : bool
        If True, do not write back to ``graph_file``. Useful for a
        preview of what would change.

    Returns
    -------
    dict
        Summary with: graph, classical_node_id, edges_refreshed,
        edges_skipped_taxtype_not_in_topk, fresh_candidates_with_no_edge,
        refreshed_details (list of {edge_id, taxonomy_type}),
        skipped_details (same shape), unmatched_candidates (list of
        taxonomy_type strings).
    """
    graph_file = Path(graph_file).resolve()

    # Build the fresh edges in-memory (no write-back from emit_stage_b).
    fresh_edges = emit_stage_b(
        classical_node_file=graph_file,
        classical_node_id=classical_node_id,
        taxonomy_id=taxonomy_id,
        rank=rank,
        top_k=top_k,
        discovery_json_path=discovery_json_path,
        write=False,
    )
    fresh_by_tax: dict[str, dict] = {
        e["taxonomy_type"]: e for e in fresh_edges if e.get("taxonomy_type")
    }

    # Load the on-disk graph via ruamel round-trip so comments + quotes
    # survive the refresh.
    yaml_rt = _yaml_rt()
    with graph_file.open(encoding="utf-8") as fh:
        graph = yaml_rt.load(fh)

    refreshed: list[dict[str, str]] = []
    skipped_no_topk: list[dict[str, str]] = []
    matched_tax_types: set[str] = set()

    for edge in graph.get("edges") or []:
        if not isinstance(edge, dict):
            continue
        if edge.get("lit_type") != classical_node_id:
            continue
        tax = edge.get("taxonomy_type")
        if not tax:
            continue
        fresh = fresh_by_tax.get(tax)
        if fresh is None:
            skipped_no_topk.append({
                "edge_id": edge.get("id"),
                "taxonomy_type": tax,
            })
            continue
        # Surgical field replacement: only the two analysis-owned
        # blocks. Everything else on the edge survives byte-identical
        # because ruamel round-trip preserves the rest of the YAML
        # structure.
        edge["property_comparisons"] = fresh.get("property_comparisons")
        edge["discovery_score"] = fresh.get("discovery_score")
        refreshed.append({
            "edge_id": edge.get("id"),
            "taxonomy_type": tax,
        })
        matched_tax_types.add(tax)

    unmatched_candidates = [
        tax for tax in fresh_by_tax
        if tax not in matched_tax_types
    ]

    if not dry_run and refreshed:
        with graph_file.open("w", encoding="utf-8") as fh:
            yaml_rt.dump(graph, fh)

    return {
        "graph": str(graph_file),
        "classical_node_id": classical_node_id,
        "taxonomy_id": taxonomy_id,
        "rank": rank,
        "top_k": top_k,
        "dry_run": dry_run,
        "edges_refreshed": len(refreshed),
        "edges_skipped_taxtype_not_in_topk": len(skipped_no_topk),
        "fresh_candidates_with_no_existing_edge": len(unmatched_candidates),
        "refreshed_details": refreshed,
        "skipped_details": skipped_no_topk,
        "unmatched_candidates": unmatched_candidates,
    }


# ─── CLI ────────────────────────────────────────────────────────────────────


def _cli() -> int:
    p = argparse.ArgumentParser(
        prog="python -m evidencell.refresh_property_comparisons",
        description=(
            "Refresh property_comparisons + discovery_score on existing "
            "edges for a classical node, using current Stage A + Stage B "
            "rules. Leaves evidence[], rationale-suite, caveats, "
            "proposed_experiments, curator/reviewer fields byte-identical."
        ),
    )
    p.add_argument("graph_file", type=Path)
    p.add_argument("classical_node_id")
    p.add_argument("taxonomy_id")
    p.add_argument("rank", type=int)
    p.add_argument(
        "--top-k", type=int, default=30,
        help="Number of fresh Stage A candidates to surface "
             "(default 30; raise if some existing edges' taxonomy_types "
             "are missed).",
    )
    p.add_argument(
        "--discovery-json", type=Path, default=None,
        help="Override the canonical discovery JSON path.",
    )
    p.add_argument(
        "--dry-run", action="store_true",
        help="Compute the refresh but do not write the graph back; "
             "print the summary.",
    )
    args = p.parse_args()
    summary = refresh_property_comparisons(
        graph_file=args.graph_file,
        classical_node_id=args.classical_node_id,
        taxonomy_id=args.taxonomy_id,
        rank=args.rank,
        top_k=args.top_k,
        discovery_json_path=args.discovery_json,
        dry_run=args.dry_run,
    )
    json.dump(summary, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
