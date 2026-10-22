"""Pool-candidate discovery for Phase 3 report-time synthesis.

The Phase 3 ``gen-report`` orchestrator includes a deterministic
pre-pass that surfaces candidate source-group pools for the synthesis
subagent to judge. A *pool candidate* is a pair (or set) of source
groups whose annotation-transfer F1/P/R rows are similar enough across
their shared atlas targets that the synthesis agent should consider
the "no transcriptomic distinction" call (#61, Winterer Sst-OLM /
Htr3a-OLM is the canonical worked example).

This module is the surfacing layer — it computes pairwise similarity
across edges in a KB graph and emits a JSON list of candidate pairs.
The agent's job is to *judge* whether to pool (and write the
indistinguishability call into ``rationale`` /
``reconciliation_note`` / a lit-to-lit ``skos:closeMatch`` edge per
the synthesis-prompt instructions). Surfacing is mechanical;
judgement is agentic.

**Algorithm.** For each pair of distinct lit_types that share at
least one atlas target:

1. Walk each lit_type's edges and collect their AT-evidence
   ``metrics_by_level`` entries. Key each entry by
   ``(taxonomy_level, target_accession)``.
2. For each shared (level, target) cell, compute the absolute
   differences in F1, precision, recall between the two source
   groups.
3. The pair is a candidate if **all** shared cells are within
   ``f1_tolerance`` AND ``pr_tolerance`` (defaults 0.05).
4. The candidate also notes which property panels have been assessed
   on each source group's edges to the shared targets, so the
   synthesis agent knows whether this is a Case A (multi-modal
   indistinguishability → write lit-to-lit closeMatch) or Case B
   (AT-only indistinguishability → annotate only).

The pre-pass surfaces *all* such pairs and trusts the agent to judge
biological significance — see ``workflows/gen-report.md`` Step 2b for
the agent contract.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml


DEFAULT_F1_TOLERANCE = 0.05
DEFAULT_PR_TOLERANCE = 0.05


# Property panels we track to give the synthesis agent enough signal
# to call Case A vs Case B. These are the canonical
# ``property_comparisons[*].property`` prefixes we expect on the
# classical / atlas edges; extend as new panel kinds are introduced.
_PANEL_PROPERTY_PREFIXES = {
    "markers": ("marker_",),
    "anat": ("location", "anatomical_location", "anat_"),
    "nt": ("nt_type", "neurotransmitter"),
    "ephys": ("electrophysiology", "ephys_", "firing_"),
    "morphology": ("morphology", "morpho_"),
    "dev": ("developmental", "dev_marker", "lineage"),
}


def _classify_panel(property_name: str) -> str | None:
    """Bucket a ``property_comparisons[*].property`` name into one of
    the panel families, or None if it doesn't match a known panel.
    Unknown property names are ignored — they don't count toward
    indistinguishability assessment.
    """
    prop = (property_name or "").lower()
    for panel, prefixes in _PANEL_PROPERTY_PREFIXES.items():
        for pfx in prefixes:
            if prop == pfx or prop.startswith(pfx):
                return panel
    return None


def _panel_signal_for_edges(edges: list[dict]) -> tuple[set[str], set[str]]:
    """Return (panels_assessed, panels_distinguishing) across a set of
    edges.

    ``panels_assessed``: panels with at least one non-NOT_ASSESSED
    PropertyComparison anywhere in the edges.
    ``panels_distinguishing``: panels where at least one
    PropertyComparison is DISCORDANT (the property differs between
    lit_type and taxonomy_type — i.e. it could in principle distinguish
    different source groups).
    """
    assessed: set[str] = set()
    distinguishing: set[str] = set()
    for edge in edges:
        for pc in edge.get("property_comparisons") or []:
            if not isinstance(pc, dict):
                continue
            panel = _classify_panel(pc.get("property", ""))
            if panel is None:
                continue
            alignment = (pc.get("alignment") or "").upper()
            if alignment and alignment != "NOT_ASSESSED":
                assessed.add(panel)
            if alignment == "DISCORDANT":
                distinguishing.add(panel)
    return assessed, distinguishing


def _at_metrics_index(
    edge: dict,
) -> dict[tuple[str, str], dict[str, float]]:
    """Index an edge's ANNOTATION_TRANSFER evidence by
    ``(taxonomy_level, best_target_accession)`` → {f1, coverage,
    purity, source}. Multiple metrics_by_level rows can share a key
    (one edge per AT evidence item); keep the highest-F1 row.

    ``source`` is ``(run_ref, source_cluster_label)`` -- the identity of the
    measurement, needed to tell independent agreement from one number copied
    onto several edges.
    """
    out: dict[tuple[str, str], dict[str, float]] = {}
    for ev in edge.get("evidence") or []:
        if not isinstance(ev, dict):
            continue
        if ev.get("evidence_type") != "ANNOTATION_TRANSFER":
            continue
        for m in ev.get("metrics_by_level") or []:
            if not isinstance(m, dict):
                continue
            level = (m.get("taxonomy_level") or "").upper()
            acc = m.get("best_target_accession")
            f1 = m.get("f1_score")
            if not (level and acc) or f1 is None:
                continue
            row = {
                "f1": float(f1),
                "coverage": float(m.get("coverage") or 0.0),
                "purity": float(m.get("purity") or 0.0),
                # Provenance of the measurement, so two lit_types scored from
                # the *same* source group can be told apart from two scored
                # independently. See _independent_sources.
                "source": (ev.get("run_ref"), ev.get("source_cluster_label")),
            }
            key = (level, acc)
            existing = out.get(key)
            if existing is None or row["f1"] > existing["f1"]:
                out[key] = row
    return out


def _independent_sources(row_a: dict, row_b: dict) -> bool:
    """True if two metrics rows are separate measurements.

    When two lit_types' AT evidence comes from the same
    ``(run_ref, source_cluster_label)``, their metrics are *one* measurement
    reported against both -- not two observations that happen to agree. Such a
    row cannot be evidence that the two types are indistinguishable, because
    the source group never distinguished them in the first place.

    This is not hypothetical. Six Yao 2021 subclass labels are each cited by
    several hippocampal lit_types, and the F1 values are identical to sixteen
    decimal places: ``Sst`` appears on six morphologically distinct
    interneuron types at CLASS 0.4133738601823709 / SUBCLASS
    0.9833024118738404. ``Sst`` is a subclass sitting one level above all six,
    so the transfer could not discriminate between them even in principle.
    Counting that as convergence evidence manufactures pool candidates out of
    label resolution.

    Both halves of the identity must be known before anything is suppressed.
    A run normally scores many source groups, so a shared ``run_ref`` alone
    says nothing -- two lit_types in one run are usually scored from different
    groups. And a missing ``run_ref`` or label is a provenance gap, reported by
    the ``run_ref`` QC check; suppressing on it here would hide one problem
    behind another.
    """
    src_a = row_a.get("source")
    src_b = row_b.get("source")
    if not (src_a and src_b):
        return True
    run_a, label_a = src_a
    run_b, label_b = src_b
    if not (run_a and run_b and label_a and label_b):
        return True
    return (run_a, label_a) != (run_b, label_b)


def _all_within(values: list[tuple[float, float]], tol: float) -> bool:
    """True iff |a - b| <= tol for every (a, b) pair in ``values``."""
    return all(abs(a - b) <= tol + 1e-9 for a, b in values)


def find_pool_candidates(
    graph: dict,
    *,
    f1_tolerance: float = DEFAULT_F1_TOLERANCE,
    pr_tolerance: float = DEFAULT_PR_TOLERANCE,
) -> list[dict]:
    """Return a list of pool-candidate dicts for the given KB graph.

    Each candidate names a pair of distinct lit_types whose AT-evidence
    metrics_by_level rows are within tolerance across all the shared
    atlas targets they map to, plus a property-panel signal so the
    synthesis agent can decide between Case A (write lit-to-lit
    closeMatch) and Case B (annotate only).
    """
    edges = [e for e in (graph.get("edges") or []) if isinstance(e, dict)]
    edges_by_lit: dict[str, list[dict]] = defaultdict(list)
    for edge in edges:
        lit = edge.get("lit_type")
        if not lit:
            continue
        edges_by_lit[lit].append(edge)

    # Pre-compute AT-metrics indices once per edge.
    metrics_by_edge_id: dict[str, dict] = {
        edge["id"]: _at_metrics_index(edge)
        for edge in edges
        if edge.get("id")
    }

    lit_types = sorted(edges_by_lit)
    out: list[dict] = []
    seen_pairs: set[tuple[str, str]] = set()
    # (lit_a, lit_b, n_dropped, n_remaining) for pairs whose shared targets were
    # scored from the same source group. Reported, never dropped silently.
    suppressed: list[tuple[str, str, int, int]] = []

    for i, lit_a in enumerate(lit_types):
        for lit_b in lit_types[i + 1:]:
            pair = (lit_a, lit_b)
            if pair in seen_pairs:
                continue
            seen_pairs.add(pair)

            # Collect AT metrics from each lit_type's edges into a
            # single merged index per lit_type. If two edges of the
            # same lit_type touch the same (level, target), keep the
            # higher-F1 row.
            metrics_a: dict[tuple[str, str], dict[str, float]] = {}
            for edge in edges_by_lit[lit_a]:
                for key, row in metrics_by_edge_id.get(edge.get("id") or "", {}).items():
                    cur = metrics_a.get(key)
                    if cur is None or row["f1"] > cur["f1"]:
                        metrics_a[key] = row
            metrics_b: dict[tuple[str, str], dict[str, float]] = {}
            for edge in edges_by_lit[lit_b]:
                for key, row in metrics_by_edge_id.get(edge.get("id") or "", {}).items():
                    cur = metrics_b.get(key)
                    if cur is None or row["f1"] > cur["f1"]:
                        metrics_b[key] = row

            overlap = sorted(set(metrics_a) & set(metrics_b))
            shared = [
                k for k in overlap
                if _independent_sources(metrics_a[k], metrics_b[k])
            ]
            if len(shared) < len(overlap):
                suppressed.append(
                    (lit_a, lit_b, len(overlap) - len(shared), len(shared))
                )
            if not shared:
                continue

            f1_pairs = [
                (metrics_a[k]["f1"], metrics_b[k]["f1"]) for k in shared
            ]
            gp_pairs = [
                (metrics_a[k]["coverage"], metrics_b[k]["coverage"])
                for k in shared
            ]
            tp_pairs = [
                (metrics_a[k]["purity"], metrics_b[k]["purity"])
                for k in shared
            ]
            if not _all_within(f1_pairs, f1_tolerance):
                continue
            if not _all_within(gp_pairs, pr_tolerance):
                continue
            if not _all_within(tp_pairs, pr_tolerance):
                continue

            # All shared rows within tolerance → candidate pair.
            assessed_a, dist_a = _panel_signal_for_edges(edges_by_lit[lit_a])
            assessed_b, dist_b = _panel_signal_for_edges(edges_by_lit[lit_b])
            panels_assessed = sorted(assessed_a & assessed_b)
            # A panel is "distinguishing" between the source groups
            # only if BOTH have data and at least one shows DISCORDANT
            # alignment — proxy for: the panel can in principle split
            # the two groups. Better signal would be a direct cross-
            # comparison, but the existing schema doesn't carry that.
            panels_distinguishing = sorted(dist_a | dist_b)
            panels_not_distinguishing = sorted(
                set(panels_assessed) - set(panels_distinguishing)
            )

            out.append(
                {
                    "source_groups": [lit_a, lit_b],
                    "shared_targets": [
                        {
                            "taxonomy_level": level,
                            "target_accession": acc,
                            "f1_a": round(metrics_a[(level, acc)]["f1"], 4),
                            "f1_b": round(metrics_b[(level, acc)]["f1"], 4),
                            "coverage_a": round(
                                metrics_a[(level, acc)]["coverage"], 4
                            ),
                            "coverage_b": round(
                                metrics_b[(level, acc)]["coverage"], 4
                            ),
                            "purity_a": round(
                                metrics_a[(level, acc)]["purity"], 4
                            ),
                            "purity_b": round(
                                metrics_b[(level, acc)]["purity"], 4
                            ),
                        }
                        for (level, acc) in shared
                    ],
                    "panels_assessed": panels_assessed,
                    "panels_distinguishing": panels_distinguishing,
                    "panels_not_distinguishing": panels_not_distinguishing,
                    "f1_tolerance": f1_tolerance,
                    "pr_tolerance": pr_tolerance,
                }
            )

    if suppressed:
        total = sum(n for _, _, n, _ in suppressed)
        print(
            f"  pool-candidates: ignored {total} shared target(s) across "
            f"{len(suppressed)} pair(s) whose AT metrics come from the same "
            "source group -- one measurement reported against both types, not "
            "independent agreement (see _independent_sources):",
            file=sys.stderr,
        )
        for lit_a, lit_b, dropped, kept in suppressed:
            print(
                f"    {lit_a} / {lit_b}: {dropped} ignored, {kept} independent "
                "target(s) remain",
                file=sys.stderr,
            )
    return out


def find_pool_candidates_for_node(
    graph: dict,
    node_id: str,
    *,
    f1_tolerance: float = DEFAULT_F1_TOLERANCE,
    pr_tolerance: float = DEFAULT_PR_TOLERANCE,
) -> list[dict]:
    """Subset of ``find_pool_candidates`` involving ``node_id`` as one
    of the two source groups. Use this from the per-node gen-report
    pre-pass."""
    all_candidates = find_pool_candidates(
        graph, f1_tolerance=f1_tolerance, pr_tolerance=pr_tolerance
    )
    return [c for c in all_candidates if node_id in c["source_groups"]]


def load_region_graph(graph_file: Path) -> dict:
    """Merge every KB graph YAML in ``graph_file``'s directory into one graph.

    Pool detection compares lit_types pairwise, so it must see the whole
    region. A per-file view was adequate while one file held many lit_types;
    once each file holds a single component it yields one lit_type, zero
    pairs, and would silently return no candidates.

    Edges are de-duplicated by id. Falls back to the single file if it is not
    inside a region directory.
    """
    graph_file = Path(graph_file)
    region_dir = graph_file.parent
    if not region_dir.is_dir():
        return yaml.safe_load(graph_file.read_text(encoding="utf-8")) or {}

    edges: list[dict] = []
    seen: set[str] = set()
    for path in sorted(region_dir.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        for edge in data.get("edges") or []:
            if not isinstance(edge, dict):
                continue
            edge_id = edge.get("id")
            if edge_id:
                if edge_id in seen:
                    continue
                seen.add(edge_id)
            edges.append(edge)
    return {"edges": edges}


# ─── CLI ─────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m evidencell.pool_candidates",
        description=(
            "Surface candidate source-group pools from a KB graph "
            "(Phase 3 gen-report pre-pass). Emits JSON on stdout."
        ),
    )
    parser.add_argument(
        "graph_file", type=Path, help="Path to KB graph YAML."
    )
    parser.add_argument(
        "--node",
        default=None,
        help=(
            "Restrict to candidates involving this lit_type. Omit to "
            "list all pairs in the graph."
        ),
    )
    parser.add_argument(
        "--f1-tolerance",
        type=float,
        default=DEFAULT_F1_TOLERANCE,
        help=f"Max absolute F1 difference. Default {DEFAULT_F1_TOLERANCE}.",
    )
    parser.add_argument(
        "--pr-tolerance",
        type=float,
        default=DEFAULT_PR_TOLERANCE,
        help=(
            f"Max absolute precision/recall difference. "
            f"Default {DEFAULT_PR_TOLERANCE}."
        ),
    )
    parser.add_argument(
        "--this-file-only",
        action="store_true",
        help=(
            "Restrict to edges in GRAPH_FILE instead of the whole region. "
            "Pool detection is cross-file by default."
        ),
    )
    args = parser.parse_args(argv)

    if args.this_file_only:
        graph = yaml.safe_load(args.graph_file.read_text(encoding="utf-8"))
    else:
        graph = load_region_graph(args.graph_file)
    if args.node:
        candidates = find_pool_candidates_for_node(
            graph,
            args.node,
            f1_tolerance=args.f1_tolerance,
            pr_tolerance=args.pr_tolerance,
        )
    else:
        candidates = find_pool_candidates(
            graph,
            f1_tolerance=args.f1_tolerance,
            pr_tolerance=args.pr_tolerance,
        )
    json.dump(candidates, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
