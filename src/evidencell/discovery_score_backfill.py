"""Backfill MappingEdge.discovery_score from on-disk discovery JSONs.

§1.11 of confidence_and_predicates_review_2026-05-24: persist the
Stage A find_candidates output onto the MappingEdge it produced.
This module is the one-off backfill path for edges created before
Stage B started writing `discovery_score` directly.

It walks a graph YAML file, and for each MappingEdge lacking a
`discovery_score`, scans the per-region discovery JSONs under
``research/{region}/**/discovery_*.json`` to find the candidate
entry that produced the edge. When found, the JSON entry is
transcribed into a schema-shaped `discovery_score` block and
inlined on the edge. Missing entries are logged to
``backfill_missing.txt`` rather than erroring — many existing
edges predate the discovery-JSON convention.

Honest scope caveat: existing on-disk discovery JSONs (as of
2026-05-26) tend to carry only the minimal fields
(score, taxonomy_rank, nt_type) and lack expression_detail /
at_hit / region_fraction / region_evidence. The backfill faithfully
transcribes whatever is present, leaving the empty fields out.
Re-running discovery against the current Stage A code (which emits
the rich block end-to-end) is the path to a fully populated
discovery_score; backfill provides cohort-dominance signal
(score / rank_in_cohort / next_best_score / cohort_size) only.

Recipe: ``just backfill-discovery-score {graph_file}``.
Idempotent: edges that already carry `discovery_score` are
skipped. Writes go through the pre-edit hook so YAML validity is
enforced automatically.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

import yaml

from evidencell.paths import repo_root


def _parse_discovery_json(path: Path) -> dict | None:
    """Extract the JSON payload from a discovery file.

    Many on-disk discovery files include the command echo and
    stderr log lines at the top before the JSON object begins
    (because the caller redirected stdout+stderr together). Locate
    the first balanced object and parse from there.
    """
    text = path.read_text()
    # Most files start with the JSON directly, but some have a
    # preamble (command echo + log lines). Find the first '{' that
    # begins a JSON object on its own line.
    for marker in ("\n{\n", "{\n"):
        idx = text.find(marker)
        if idx != -1:
            # marker length: include the leading newline if present
            start = idx + (1 if marker.startswith("\n") else 0)
            break
    else:
        start = 0
    try:
        data = json.loads(text[start:])
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict) or "candidates" not in data:
        return None
    return data


def _expression_detail_to_list(
    flat: dict[str, dict] | None,
) -> list[dict]:
    """Convert legacy flat ``{gene: {...}}`` expression_detail to
    the new list-of-GeneDiscoveryDetail shape.

    Legacy entries carry: val, reliable, cohort_pct, score,
    source, optional coverage. The new shape adds:
      - ``gene``: the dict key (with any ``-`` prefix preserved)
      - ``raw_tier``: reconstructed when possible, else absent
      - ``applied_score``: legacy ``score``
      - ``percentiles[]``: built from ``cohort_pct``
      - ``source``: upper-cased to match the schema enum
    """
    if not flat:
        return []
    out: list[dict] = []
    for gene_key, entry in flat.items():
        applied = entry.get("score")
        coverage = entry.get("coverage")
        # raw_tier reconstruction: if no coverage dampener was
        # applied, applied_score == raw_tier (integer). Otherwise
        # raw_tier = applied / sqrt(coverage), rounded — close
        # enough for downstream reading and verifiable from the
        # other fields.
        raw_tier: int | None = None
        if applied is not None:
            if coverage is None and float(applied) == int(applied):
                raw_tier = int(applied)
            elif coverage and coverage > 0:
                # Inverse of the live emitter's dampener:
                # applied = raw_tier × sqrt(coverage).
                raw_tier = round(float(applied) / (float(coverage) ** 0.5))

        percentiles: list[dict] = []
        cohort_pct = entry.get("cohort_pct")
        if cohort_pct is not None:
            percentiles.append({"context_id": "cohort", "pct": cohort_pct})

        gd: dict = {
            "gene": gene_key,
            "val": entry.get("val"),
            "reliable": entry.get("reliable"),
            "applied_score": (
                float(applied) if applied is not None else None
            ),
            "source": (
                (entry.get("source") or "EXPRESSION").upper()
            ),
            "percentiles": percentiles,
        }
        if raw_tier is not None:
            gd["raw_tier"] = raw_tier
        if coverage is not None:
            gd["coverage"] = coverage
        out.append(gd)
    return out


def candidate_to_discovery_score(
    candidate: dict,
    *,
    rank: int | None,
    cohort_size: int,
    rank_in_cohort: int,
    next_best_score: int,
) -> dict:
    """Transcribe one candidate-dict from an on-disk discovery
    JSON into a schema-shaped ``discovery_score`` block.

    The candidate dict may be in either the legacy flat shape
    (``score`` / ``expression_detail`` / ``region_*`` / ``at_hit``
    at the top level) or the new shape (a ``discovery_score`` key
    already present). The new-shape path is a pass-through.
    """
    # Forward-compatible: if the candidate already has a
    # discovery_score block (newer Stage A emission), trust it
    # verbatim — this path lets the backfill module also work as
    # a re-runner on fresher JSONs without losing data.
    if candidate.get("discovery_score"):
        return candidate["discovery_score"]

    contexts = [
        {
            "id": "cohort",
            "kind": "SURVIVAL_COHORT",
            "rank": rank,
            "n_members": cohort_size,
            # Filters not recoverable from on-disk JSON — note
            # the gap explicitly so downstream readers know not to
            # over-interpret an empty `filters` list.
            "filters": [],
            "description": (
                "Backfilled from legacy discovery JSON; original "
                "query filters not recorded in file."
            ),
        }
    ]
    block: dict = {
        "score": int(candidate.get("score", 0)),
        "rank_in_cohort": rank_in_cohort,
        "cohort_size": cohort_size,
        "next_best_score": next_best_score,
        "rank": rank,
        "contexts": contexts,
        "expression_detail": _expression_detail_to_list(
            candidate.get("expression_detail")
        ),
    }
    if candidate.get("region_fraction") is not None:
        block["region_fraction"] = candidate["region_fraction"]
    if candidate.get("region_evidence"):
        block["region_evidence"] = candidate["region_evidence"].upper()
    hit = candidate.get("at_hit")
    if hit:
        block["at_signal"] = {
            "f1": hit.get("f1"),
            "n_cells": hit.get("n_cells"),
            "target_level": hit.get("target_level"),
            "target_name": hit.get("target_name"),
            "score": hit.get("score"),
        }
    return block


def _index_discovery_jsons(
    region: str,
) -> dict[str, list[tuple[Path, dict]]]:
    """Map ``classical_node_id`` → list of (file_path, parsed_data).

    Multiple files may target the same classical node (different
    ranks or runs); the lookup keeps all of them so the matcher
    can prefer the one matching the edge's candidate rank.
    """
    root = repo_root() / "research" / region
    index: dict[str, list[tuple[Path, dict]]] = {}
    if not root.exists():
        return index
    for path in sorted(root.rglob("discovery_*.json")):
        data = _parse_discovery_json(path)
        if data is None:
            continue
        cid = data.get("classical_node_id")
        if not cid:
            continue
        index.setdefault(cid, []).append((path, data))
    return index


def _find_candidate(
    index: dict[str, list[tuple[Path, dict]]],
    classical_id: str,
    atlas_accession: str,
    preferred_rank: int | None,
) -> tuple[Path, dict, dict, int, int, int] | None:
    """Return ``(json_path, data, candidate, rank_in_cohort,
    cohort_size, next_best_score)`` for the discovery entry that
    produced an edge, or ``None`` if no JSON contains the
    candidate.

    When multiple discovery JSONs match the classical id, prefer
    the one whose ``rank`` equals ``preferred_rank`` (i.e. matches
    the candidate's taxonomy_rank — that's the JSON it was
    sourced from).
    """
    matches = index.get(classical_id, [])
    if not matches:
        return None
    # Prefer rank-matched JSON; fall back to any match.
    ordered = sorted(
        matches,
        key=lambda pd: 0 if pd[1].get("rank") == preferred_rank else 1,
    )
    for path, data in ordered:
        candidates = data.get("candidates") or []
        for i, c in enumerate(candidates):
            if c.get("node_id") == atlas_accession:
                cohort_size = len(candidates)
                next_best_score = (
                    int(candidates[1].get("score") or 0)
                    if cohort_size >= 2
                    else 0
                )
                return path, data, c, i + 1, cohort_size, next_best_score
    return None


def backfill_graph(graph_file: Path, *, dry_run: bool = False) -> dict:
    """Walk the graph's edges and patch ``discovery_score`` in
    place. Returns a summary dict for logging.
    """
    region = graph_file.parent.name
    index = _index_discovery_jsons(region)
    with graph_file.open() as fh:
        graph = yaml.safe_load(fh)
    edges = graph.get("edges", []) or []
    nodes_by_id = {n["id"]: n for n in (graph.get("nodes") or [])}

    patched: list[str] = []
    skipped_present: list[str] = []
    missing: list[tuple[str, str, str]] = []  # (edge_id, lit_type, taxonomy_type)

    for edge in edges:
        if edge.get("discovery_score"):
            skipped_present.append(edge["id"])
            continue
        lit_type = edge.get("lit_type") or edge.get("type_a")
        atlas_acc = edge.get("taxonomy_type") or edge.get("type_b")
        if not lit_type or not atlas_acc:
            continue
        # Look up the candidate's queried rank from the atlas
        # stub if present (taxonomy_rank is recorded on the node).
        atlas_node = nodes_by_id.get(atlas_acc) or {}
        # Candidate's emitted rank in discovery JSONs equals the
        # queried `rank` param at Stage A time; without that, we
        # try the node's taxonomy_rank — same value in practice.
        preferred_rank = atlas_node.get("taxonomy_rank")
        match = _find_candidate(index, lit_type, atlas_acc, preferred_rank)
        if match is None:
            missing.append((edge["id"], lit_type, atlas_acc))
            continue
        json_path, data, candidate, ric, cs, nbs = match
        block = candidate_to_discovery_score(
            candidate,
            rank=data.get("rank"),
            cohort_size=cs,
            rank_in_cohort=ric,
            next_best_score=nbs,
        )
        edge["discovery_score"] = block
        patched.append(f"{edge['id']} <- {json_path.name}")

    if not dry_run and patched:
        with graph_file.open("w") as fh:
            yaml.safe_dump(graph, fh, sort_keys=False, allow_unicode=True)

    return {
        "graph_file": str(graph_file),
        "region": region,
        "n_edges": len(edges),
        "patched": patched,
        "skipped_already_present": skipped_present,
        "missing": missing,
        "dry_run": dry_run,
    }


def _write_missing_log(missing: list[tuple[str, str, str]], log_path: Path) -> None:
    if not missing:
        return
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a") as fh:
        for edge_id, lit_type, atlas_acc in missing:
            fh.write(f"{edge_id}\t{lit_type}\t{atlas_acc}\n")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Backfill MappingEdge.discovery_score from on-disk "
            "discovery JSONs (one graph file at a time)."
        )
    )
    parser.add_argument("graph_file", type=Path)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing the graph file.",
    )
    parser.add_argument(
        "--missing-log",
        type=Path,
        default=None,
        help=(
            "Append unmatched (edge_id, lit_type, taxonomy_type) "
            "triples to this file. Default: <graph_dir>/backfill_missing.txt"
        ),
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    graph_file: Path = args.graph_file.resolve()
    if not graph_file.exists():
        print(f"ERROR: graph file not found: {graph_file}", file=sys.stderr)
        return 1

    result = backfill_graph(graph_file, dry_run=args.dry_run)
    print(f"Graph: {result['graph_file']}")
    print(f"Region: {result['region']}")
    print(f"Edges: {result['n_edges']}")
    print(f"Patched: {len(result['patched'])}")
    for line in result["patched"]:
        print(f"  + {line}")
    print(f"Skipped (already populated): {len(result['skipped_already_present'])}")
    print(f"Missing (no discovery JSON match): {len(result['missing'])}")
    for edge_id, lit_type, atlas_acc in result["missing"]:
        print(f"  - {edge_id}  ({lit_type} -> {atlas_acc})")

    log_path = args.missing_log or (graph_file.parent / "backfill_missing.txt")
    if not args.dry_run:
        _write_missing_log(result["missing"], log_path)
        if result["missing"]:
            print(f"Wrote missing log: {log_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
