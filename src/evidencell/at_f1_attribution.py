"""AT F1 attribution: informational report on level annotations.

This module's role was substantially revised after a destructive
auto-correction pass (commit 46db139, reverted in 369dd4b) demonstrated
that **rewriting curator-recorded F1 values without verifiable matrix
provenance is not a safe automation**. The module is now a *report*
only: it surfaces the cases where an AT evidence's
``best_mapping_level`` differs from the target accession's level, so a
curator (or downstream audit) can interpret the F1 correctly.

A ``best_mapping_level`` that differs from the edge's target level is
**not an error per se** — it's the curator's honest annotation that
the F1 was computed at a different (typically coarser) taxonomy
level. The :func:`evidencell.validate.check_at_f1_attribution` pre-edit
hook merely requires the field to be set; it does not enforce
equality. Downstream consumers (audits, scorers) are responsible for
routing test cases via ``best_mapping_level``.

See also:

* ``src/evidencell/validation/at_blind.py`` — audit driver that
  consumes ``best_mapping_level`` to route test cases to the correct
  rank.
* ``research/validation/methods_audits/at_blind/`` — findings.
* ``workflows/annotation-transfer.md`` § Step 4 — curation rule
  (always record ``best_mapping_level``).
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from evidencell import _mapping_compat
from evidencell.paths import repo_root

# Accession-prefix → taxonomy-level (UPPERCASE — same convention as
# the ``best_mapping_level`` enum values in MappingEvidence schema).
_PREFIX_TO_LEVEL = {
    "_CLUS_": "CLUSTER",
    "_SUPT_": "SUPERTYPE",
    "_SUBC_": "SUBCLASS",
    "_CLAS_": "CLASS",
}


def target_level_from_accession(accession: str) -> str | None:
    """Return the taxonomy-level token implied by a WMBv1-style accession
    prefix (``CLUSTER`` for ``CS20230722_CLUS_0769`` etc.). Returns
    None when the accession matches no known prefix."""
    if not accession:
        return None
    for pfx, lvl in _PREFIX_TO_LEVEL.items():
        if pfx in accession:
            return lvl
    return None


@dataclass
class AttributionFinding:
    """One AT-evidence record whose ``best_mapping_level`` differs from
    the edge target's accession-derived level. Informational — these
    are legitimate cases that downstream consumers route via
    ``best_mapping_level``."""
    graph_file: Path
    edge_id: str
    type_a: str
    target_accession: str
    target_level: str
    best_mapping_level: str
    recorded_f1: float | None
    run_ref: str | None
    source_cluster_label: str | None
    evidence_index: int

    def as_dict(self) -> dict:
        return {
            "graph_file": str(self.graph_file),
            "edge_id": self.edge_id,
            "type_a": self.type_a,
            "target_accession": self.target_accession,
            "target_level": self.target_level,
            "best_mapping_level": self.best_mapping_level,
            "recorded_f1": self.recorded_f1,
            "run_ref": self.run_ref,
            "source_cluster_label": self.source_cluster_label,
        }


def find_mismatches(graphs_root: Path | None = None) -> list[AttributionFinding]:
    """Walk every KB graph YAML and return all AT-evidence items whose
    ``best_mapping_level`` differs from the target accession's level.

    Reminder: these are NOT errors. The curator honestly recorded that
    the F1 was computed at a different level than the edge's target.
    Downstream audits should use ``best_mapping_level`` to route the
    test case, not treat the F1 as oracle for the edge's level.

    The report is useful for surfacing curation patterns (e.g. how
    often supertype-level AT evidence is attached to cluster edges,
    informing whether the schema should support multi-level AT
    evidence directly).
    """
    root = graphs_root or (repo_root() / "kb" / "graphs")
    findings: list[AttributionFinding] = []
    for path in sorted(root.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        nodes_by_id = {
            n["id"]: n for n in (doc.get("nodes") or []) if n.get("id")
        }
        for edge in doc.get("edges") or []:
            type_b = _mapping_compat.taxonomy_type(edge) or ""
            target_node = nodes_by_id.get(type_b, {})
            target_acc = (
                target_node.get("cell_set_accession")
                or type_b
            )
            target_level = target_level_from_accession(target_acc)
            if not target_level:
                continue
            for i, ev in enumerate(edge.get("evidence") or []):
                if not isinstance(ev, dict):
                    continue
                if ev.get("evidence_type") != "ANNOTATION_TRANSFER":
                    continue
                bml = ev.get("best_mapping_level")
                if not bml:
                    continue
                if bml.upper() == target_level.upper():
                    continue
                findings.append(AttributionFinding(
                    graph_file=path,
                    edge_id=edge.get("id") or "<unnamed>",
                    type_a=_mapping_compat.lit_type(edge) or "",
                    target_accession=target_acc,
                    target_level=target_level,
                    best_mapping_level=bml,
                    recorded_f1=ev.get("best_f1_score"),
                    run_ref=ev.get("run_ref"),
                    source_cluster_label=ev.get("source_cluster_label"),
                    evidence_index=i,
                ))
    return findings


def lookup_correct_f1(
    run_ref: str,
    source_cluster_label: str,
    target_accession: str,
    target_level: str,
    runs_root: Path | None = None,
    taxonomy_id: str = "CCN20230722",
) -> tuple[float | None, str]:
    """Look up the actual F1 for ``(source_label, target_accession,
    target_level)`` in the source AT run's ``f1_matrix*.csv``. Used by
    audits for read-only verification; never used to mutate KB data.

    Returns ``(f1, status)``. See module docstring for the rationale
    behind read-only usage.
    """
    if not run_ref or not source_cluster_label:
        return None, "missing_fields"
    runs_root = runs_root or (repo_root() / "kb" / "annotation_transfer_runs")
    run_dir = _resolve_run_dir(runs_root, run_ref)
    if not run_dir or not run_dir.exists():
        return None, "run_dir_missing"
    candidates = sorted(run_dir.glob("f1_matrix*.csv"))
    if not candidates:
        return None, "no_f1_matrix"
    target_label = _label_for_accession(target_accession, taxonomy_id)
    if not target_label:
        return None, "target_label_unresolvable"
    level = target_level.lower()
    found_rows: list[dict] = []
    source_seen: set[str] = set()
    for f1_csv in candidates:
        with f1_csv.open(encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                source_seen.add(row.get("source_label", ""))
                if (
                    row.get("source_label") == source_cluster_label
                    and (row.get("level") or "").lower() == level
                    and row.get("target_name") == target_label
                ):
                    found_rows.append(row)
        if found_rows:
            break
    if not found_rows:
        if source_cluster_label not in source_seen:
            return None, "source_label_not_in_matrix"
        return 0.0, "absent_from_matrix_zero_f1"
    if len(found_rows) > 1:
        return None, "multiple_rows_match"
    try:
        return float(found_rows[0]["f1"]), "resolved"
    except (KeyError, TypeError, ValueError):
        return None, "f1_unparseable"


def _resolve_run_dir(runs_root: Path, run_ref: str) -> Path | None:
    """Resolve a ``run_ref`` (the canonical id used on edges) to the
    actual directory on disk via the registry index, with literal-name
    fallback."""
    index_path = runs_root / "index.yaml"
    if index_path.exists():
        try:
            index = yaml.safe_load(index_path.read_text(encoding="utf-8")) or {}
        except Exception:
            index = {}
        for entry in index.get("runs") or []:
            if entry.get("id") == run_ref:
                manifest_rel = entry.get("manifest_path")
                if manifest_rel:
                    manifest_path = repo_root() / manifest_rel
                    return manifest_path.parent
    candidates = [
        runs_root / run_ref,
        runs_root / run_ref.removeprefix("at_run_"),
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def _label_for_accession(accession: str, taxonomy_id: str) -> str | None:
    """Query the taxonomy DB for a node's ``label``. Returns None if
    the DB or node isn't available."""
    from evidencell.paths import taxonomy_db_path
    db_path = taxonomy_db_path(taxonomy_id)
    if not db_path.exists():
        return None
    import sqlite3
    with sqlite3.connect(db_path) as con:
        row = con.execute(
            "SELECT label FROM nodes WHERE node_id = ?", (accession,)
        ).fetchone()
    return row[0] if row else None


def main() -> int:
    """CLI: ``python -m evidencell.at_f1_attribution`` — print a report
    of all level-attribution divergences (no mutation)."""
    import argparse
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.at_f1_attribution",
        description="Report AT evidence whose best_mapping_level differs "
                    "from the target accession's level. Informational "
                    "only — no KB mutation.",
    )
    parser.parse_args()
    findings = find_mismatches()
    print(
        f"Found {len(findings)} AT-evidence items where best_mapping_level "
        f"differs from the target accession's level."
    )
    print(
        "(These are not errors. The curator's annotation says the F1 "
        "was computed at a different level than the edge target. "
        "Audits should route via best_mapping_level.)\n"
    )
    for f in findings:
        rel = str(f.graph_file.relative_to(repo_root()))
        print(
            f"  {rel}:{f.edge_id}\n"
            f"    target={f.target_accession} (target_level={f.target_level})\n"
            f"    best_mapping_level={f.best_mapping_level} "
            f"recorded_f1={f.recorded_f1}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
