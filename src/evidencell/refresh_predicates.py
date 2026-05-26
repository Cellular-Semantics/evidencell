"""Migrate deprecated `evidencell:PartialOverlapMatch` edges to the
2026-05-26 predicate rubric.

The 2026-05-24 review (`planning/confidence_and_predicates_review_2026-05-24.md`)
deprecated `evidencell:PartialOverlapMatch`. Edges using it must be
re-predicated to one of `skos:exactMatch` / `skos:closeMatch` /
`skos:broadMatch` / `skos:narrowMatch` / `evidencell:CrossCuttingMatch` /
`evidencell:UncertainRelationship`.

This module reads each MappingEdge's existing AT evidence,
property_comparisons, caveats, and `mapping_cardinality`, then applies
a minimal rubric to pick a new `relationship` + `mapping_cardinality`.
It does NOT re-run discovery and does NOT change which atlas type an
edge points at — only the predicate.

Rubric applied:

1. If `mapping_cardinality` is `1:n` → `skos:broadMatch` + `1:n`.
2. If `mapping_cardinality` is `n:1` → `skos:narrowMatch` + `n:1`.
3. Else (1:1 candidate) — examine AT + contradictions:
   - AT F1 > 0.75 at the edge's working rank AND no contradictions
     (no DISCORDANT property_comparison, no caveats) →
     `skos:exactMatch` + `1:1`.
   - Otherwise → `skos:closeMatch` + `1:1`.
4. If no AT evidence and no usable property_comparisons →
   `evidencell:UncertainRelationship`.

Each migrated edge gets a `caveat` entry of type
`AUTO_REPREDICATED_2026_05_26` documenting the rule that fired so
curators can spot-check the migration.

Run via `just refresh-predicates [--dry-run] [--files PATTERN]`.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

from .paths import repo_root


_DEPRECATED = "evidencell:PartialOverlapMatch"
_F1_GATE = 0.75


def _yaml() -> YAML:
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.width = 4096
    return yaml


def _safe_cardinality(value: str) -> DoubleQuotedScalarString:
    """Force-quote so `1:1` / `n:1` survive YAML 1.1 sexagesimal parsing."""
    return DoubleQuotedScalarString(value)


@dataclass
class MigrationOutcome:
    edge_id: str
    file: Path
    old_predicate: str
    new_predicate: str
    new_cardinality: str | None
    rule: str


def _best_at_f1(evidence_items: Iterable[dict], target_accession: str) -> float | None:
    """Return the F1 score at the rank matching the edge's taxonomy_type
    accession, or the best available F1 across ranks if no exact match.
    """
    best_at_target = None
    best_any = None
    for item in evidence_items or []:
        if not isinstance(item, dict):
            continue
        if item.get("evidence_type") != "ANNOTATION_TRANSFER":
            continue
        for level in item.get("metrics_by_level") or []:
            if not isinstance(level, dict):
                continue
            f1 = level.get("f1_score")
            if not isinstance(f1, (int, float)):
                continue
            if level.get("best_target_accession") == target_accession:
                if best_at_target is None or f1 > best_at_target:
                    best_at_target = float(f1)
            if best_any is None or f1 > best_any:
                best_any = float(f1)
    return best_at_target if best_at_target is not None else best_any


def _has_discordant(property_comparisons: Iterable[dict]) -> bool:
    for pc in property_comparisons or []:
        if isinstance(pc, dict) and pc.get("alignment") == "DISCORDANT":
            return True
    return False


def _has_caveats(caveats: Iterable[dict]) -> bool:
    return any(isinstance(c, dict) for c in (caveats or []))


def _classify(edge: dict) -> tuple[str, str | None, str]:
    """Apply the rubric. Returns (predicate, cardinality, rule)."""
    cardinality = edge.get("mapping_cardinality")
    if cardinality == "1:n":
        return ("skos:broadMatch", "1:n", "rule-1: cardinality 1:n → broadMatch")
    if cardinality == "n:1":
        return ("skos:narrowMatch", "n:1", "rule-2: cardinality n:1 → narrowMatch")

    evidence = edge.get("evidence") or []
    target_accession = edge.get("taxonomy_type", "")
    f1 = _best_at_f1(evidence, target_accession)
    discordant = _has_discordant(edge.get("property_comparisons") or [])
    caveated = _has_caveats(edge.get("caveats") or [])
    has_at = any(
        isinstance(item, dict) and item.get("evidence_type") == "ANNOTATION_TRANSFER"
        for item in evidence
    )

    if not has_at and not edge.get("property_comparisons"):
        return (
            "evidencell:UncertainRelationship",
            None,
            "rule-4: no AT and no property_comparisons → UncertainRelationship",
        )

    if f1 is not None and f1 > _F1_GATE and not discordant and not caveated:
        return (
            "skos:exactMatch",
            "1:1",
            f"rule-3a: F1={f1:.3f} > {_F1_GATE}, no DISCORDANT, no caveats → exactMatch",
        )

    reasons = []
    if f1 is None:
        reasons.append("no AT F1")
    elif f1 <= _F1_GATE:
        reasons.append(f"F1={f1:.3f} ≤ {_F1_GATE}")
    if discordant:
        reasons.append("DISCORDANT comparison(s)")
    if caveated:
        reasons.append("existing caveats")
    return (
        "skos:closeMatch",
        "1:1",
        "rule-3b: " + ", ".join(reasons) + " → closeMatch",
    )


def _migrate_edge(edge: dict) -> MigrationOutcome | None:
    if edge.get("relationship") != _DEPRECATED:
        return None
    predicate, cardinality, rule = _classify(edge)
    outcome = MigrationOutcome(
        edge_id=edge.get("id", "<unknown>"),
        file=Path(),  # filled by caller
        old_predicate=_DEPRECATED,
        new_predicate=predicate,
        new_cardinality=cardinality,
        rule=rule,
    )

    edge["relationship"] = predicate
    if cardinality is None:
        edge.pop("mapping_cardinality", None)
    else:
        edge["mapping_cardinality"] = _safe_cardinality(cardinality)

    caveats = edge.setdefault("caveats", [])
    if not isinstance(caveats, list):
        caveats = []
        edge["caveats"] = caveats
    caveats.append(
        {
            "caveat_type": "OTHER",
            "description": (
                f"[AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated "
                f"from deprecated {_DEPRECATED} to {predicate} by "
                f"`refresh_predicates.py`. Rule: {rule}. "
                f"Curator review recommended."
            ),
        }
    )
    return outcome


def migrate_file(path: Path, *, dry_run: bool) -> list[MigrationOutcome]:
    yaml = _yaml()
    with path.open() as fh:
        data = yaml.load(fh)
    if not isinstance(data, dict):
        return []
    edges = data.get("edges") or []
    outcomes: list[MigrationOutcome] = []
    for edge in edges:
        if not isinstance(edge, dict):
            continue
        outcome = _migrate_edge(edge)
        if outcome is not None:
            outcome.file = path
            outcomes.append(outcome)
    if outcomes and not dry_run:
        with path.open("w") as fh:
            yaml.dump(data, fh)
    return outcomes


def find_candidate_files(kb_graphs_dir: Path) -> list[Path]:
    return sorted(
        p
        for p in kb_graphs_dir.rglob("*.yaml")
        if _DEPRECATED in p.read_text()
    )


def _summarise(outcomes: list[MigrationOutcome]) -> str:
    if not outcomes:
        return "No deprecated edges found."
    by_predicate: dict[str, int] = {}
    for o in outcomes:
        by_predicate[o.new_predicate] = by_predicate.get(o.new_predicate, 0) + 1
    lines = [f"Migrated {len(outcomes)} edge(s):"]
    for predicate, count in sorted(by_predicate.items(), key=lambda kv: -kv[1]):
        lines.append(f"  {count:3d} → {predicate}")
    lines.append("")
    lines.append("Per-edge:")
    for o in outcomes:
        cardinality = f" + {o.new_cardinality}" if o.new_cardinality else ""
        lines.append(
            f"  [{o.file.name}] {o.edge_id} → {o.new_predicate}{cardinality}"
        )
        lines.append(f"      {o.rule}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files.",
    )
    parser.add_argument(
        "--kb-graphs-dir",
        type=Path,
        default=None,
        help="KB graphs directory (default: <repo>/kb/graphs).",
    )
    args = parser.parse_args(argv)

    graphs_dir = args.kb_graphs_dir or (repo_root() / "kb" / "graphs")
    files = find_candidate_files(graphs_dir)
    if not files:
        print(f"No files with {_DEPRECATED} under {graphs_dir}.")
        return 0

    all_outcomes: list[MigrationOutcome] = []
    for path in files:
        outcomes = migrate_file(path, dry_run=args.dry_run)
        all_outcomes.extend(outcomes)

    if args.dry_run:
        print("[DRY RUN] No files written.")
    print(_summarise(all_outcomes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
