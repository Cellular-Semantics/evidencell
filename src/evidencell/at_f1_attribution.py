"""AT F1 attribution audit + correction.

Each ``AnnotationTransferEvidence`` item on a ``MappingEdge`` should
report an F1 score that corresponds to the edge's target at the
target's level. When ``best_mapping_level`` disagrees with the
target's accession-derived level, the recorded F1 is the wrong number
for the edge — it reflects MapMyCells output at a different
granularity than the edge claims to be about.

This module:

  * Walks ``kb/graphs/**/*.yaml`` and flags every AT-evidence item with
    level mismatch.
  * For each mismatch, tries to look up the *correct* F1 for the
    target at the target's level by opening the source AT run's
    ``f1_matrix.csv``. Falls back to ``None`` when the source label
    is a curator aggregation that doesn't match a single matrix row.
  * In ``--apply`` mode, rewrites the affected evidence items in
    place, prepending a flag to ``explanation`` so the change is
    traceable.

Detection logic is also imported by ``.claude/hooks/validate_mapping_hook.py``
to prevent new misattributions at write time.
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

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
    """One problematic AT-evidence record."""
    graph_file: Path
    edge_id: str
    type_a: str
    target_accession: str
    target_level: str
    best_mapping_level: str
    recorded_f1: float | None
    run_ref: str | None
    source_cluster_label: str | None
    # Path within edge YAML (evidence index) for the auto-fix step.
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
    ``best_mapping_level`` disagrees with the target accession's level.

    Items with no ``best_mapping_level`` or no target-level inference
    are skipped (they need their own remediation; this function focuses
    on the unambiguous mismatch case).
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
            target_node = nodes_by_id.get(edge.get("type_b") or "", {})
            target_acc = (
                target_node.get("cell_set_accession")
                or edge.get("type_b")
                or ""
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
                    type_a=edge.get("type_a") or "",
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
    """Look up the actual F1 for this (source_label, target_accession,
    target_level) in the source AT run's ``f1_matrix.csv``.

    Returns ``(f1, status)``. ``f1`` is ``None`` when the lookup can't
    produce a single defensible value; ``status`` is a short string
    explaining why (``"resolved"``, ``"absent_from_matrix"``,
    ``"source_label_not_in_matrix"``, ``"run_dir_missing"``,
    ``"no_f1_matrix"``).

    A target absent from the matrix at the requested level means
    MapMyCells assigned zero cells to it — F1 is effectively 0.0.
    """
    if not run_ref or not source_cluster_label:
        return None, "missing_fields"
    runs_root = runs_root or (repo_root() / "kb" / "annotation_transfer_runs")

    # Run directories don't always share their `id` field; the canonical
    # mapping lives in ``kb/annotation_transfer_runs/index.yaml``. Try
    # the index first, then fall back to the run_ref as a literal
    # directory name (with and without an ``at_run_`` prefix).
    run_dir = _resolve_run_dir(runs_root, run_ref)
    if not run_dir or not run_dir.exists():
        return None, "run_dir_missing"

    # Find the f1_matrix.csv — naming varies across runs.
    candidates = sorted(run_dir.glob("f1_matrix*.csv"))
    if not candidates:
        return None, "no_f1_matrix"

    # Resolve target_accession → target_name via the taxonomy DB so we
    # can match the f1_matrix.csv's ``target_name`` column.
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
        # Was the source_label in this matrix at all?
        if source_cluster_label not in source_seen:
            return None, "source_label_not_in_matrix"
        # Source present but target+level isn't → MapMyCells assigned
        # zero cells to this specific target at this level. F1 = 0.0.
        return 0.0, "absent_from_matrix_zero_f1"

    if len(found_rows) > 1:
        return None, "multiple_rows_match"

    try:
        return float(found_rows[0]["f1"]), "resolved"
    except (KeyError, TypeError, ValueError):
        return None, "f1_unparseable"


def _resolve_run_dir(runs_root: Path, run_ref: str) -> Path | None:
    """Resolve a ``run_ref`` (the canonical id used on edges) to the
    actual directory on disk. Tries the registry index first, then
    falls back to literal directory-name matching with and without the
    ``at_run_`` prefix that some runs carry."""
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
    # Fallback: literal dir name, with and without ``at_run_`` prefix.
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


def apply_corrections(
    findings: list[AttributionFinding],
    runs_root: Path | None = None,
    taxonomy_id: str = "CCN20230722",
    log_path: Path | None = None,
) -> list[dict]:
    """Surgically rewrite each affected YAML in place: change only the
    two fields that carry the misattribution (``best_f1_score`` and
    ``best_mapping_level``). Preserves every other byte — comments,
    indentation, block scalar styles, explicit ``null`` tokens — by
    doing targeted text substitutions rather than YAML load+dump.

    Records the full correction history (old values, new values,
    lookup status, target accession) to a sidecar JSON log at
    ``research/validation/methods_audits/at_f1_attribution/log.json``
    so the trail is auditable without polluting curator-authored
    explanations.

    Returns one dict per finding with the action taken
    (``"rewrote"``, ``"set_null"``, ``"skipped"`` + reason).
    """
    import json
    import re
    from datetime import datetime, timezone

    actions: list[dict] = []
    by_file: dict[Path, list[AttributionFinding]] = {}
    for f in findings:
        by_file.setdefault(f.graph_file, []).append(f)

    # Compile patterns once. The targets are:
    #   <indent>best_f1_score: <value>
    #   <indent>best_mapping_level: "<LEVEL>"  (also unquoted)
    # We search per-finding in the file text, anchored by the edge_id
    # and the AT-evidence item's source_cluster_label so we don't
    # accidentally touch a sibling evidence record.
    re_f1 = re.compile(r"^(\s*)best_f1_score:\s.*$", re.MULTILINE)
    re_bml = re.compile(r"^(\s*)best_mapping_level:\s.*$", re.MULTILINE)

    for path, file_findings in by_file.items():
        text = path.read_text(encoding="utf-8")

        for fnd in file_findings:
            new_f1, status = lookup_correct_f1(
                run_ref=fnd.run_ref or "",
                source_cluster_label=fnd.source_cluster_label or "",
                target_accession=fnd.target_accession,
                target_level=fnd.target_level,
                runs_root=runs_root,
                taxonomy_id=taxonomy_id,
            )
            old_f1 = fnd.recorded_f1

            # Locate the edge block by id. Capture from `id: <edge_id>`
            # to next `- id:` at the same indentation level or EOF.
            edge_marker = f"- id: {fnd.edge_id}\n"
            edge_start = text.find(edge_marker)
            if edge_start < 0:
                actions.append({"edge_id": fnd.edge_id, "action": "skipped",
                                "reason": "edge_marker_not_found"})
                continue
            # Find next `  - id:` at same indent (edge-level) — that's
            # the start of the next edge. End of file otherwise.
            # Edge id lines start with two spaces then "- id:" in this
            # codebase's convention.
            next_edge = text.find("\n  - id: ", edge_start + 1)
            edge_end = next_edge if next_edge > 0 else len(text)
            edge_block = text[edge_start:edge_end]

            # Within the edge block, locate the AT evidence we want.
            # Anchor on source_cluster_label + best_f1_score combination
            # if source_cluster_label exists; otherwise just match the
            # first ANNOTATION_TRANSFER evidence in the edge.
            evidence_marker = "- evidence_type: ANNOTATION_TRANSFER"
            ev_starts = [
                m.start() for m in re.finditer(
                    re.escape(evidence_marker), edge_block
                )
            ]
            if not ev_starts:
                actions.append({"edge_id": fnd.edge_id, "action": "skipped",
                                "reason": "evidence_marker_not_found"})
                continue
            # Pick the evidence block that contains the matching
            # source_cluster_label (or fall back to evidence_index).
            chosen = None
            for ev_start in ev_starts:
                # End of this evidence block: next evidence marker or
                # end of edge_block.
                ev_end = edge_block.find(
                    "- evidence_type:", ev_start + 1
                )
                if ev_end < 0:
                    ev_end = len(edge_block)
                ev_block = edge_block[ev_start:ev_end]
                if fnd.source_cluster_label and (
                    f"source_cluster_label: {fnd.source_cluster_label!r}"
                    in ev_block
                    or f'source_cluster_label: "{fnd.source_cluster_label}"'
                    in ev_block
                    or f"source_cluster_label: {fnd.source_cluster_label}"
                    in ev_block
                ):
                    chosen = (ev_start, ev_end)
                    break
            if chosen is None:
                # Fall back to evidence_index relative to all evidence
                # items in this edge (not just AT-type) — risky but
                # better than nothing.
                if fnd.evidence_index < len(ev_starts):
                    ev_start = ev_starts[fnd.evidence_index]
                    ev_end = (
                        edge_block.find("- evidence_type:", ev_start + 1)
                        or len(edge_block)
                    )
                    if ev_end < 0:
                        ev_end = len(edge_block)
                    chosen = (ev_start, ev_end)
            if chosen is None:
                actions.append({"edge_id": fnd.edge_id, "action": "skipped",
                                "reason": "evidence_block_unresolvable"})
                continue

            ev_start, ev_end = chosen
            ev_text = edge_block[ev_start:ev_end]

            # Surgical replacements within ev_text only.
            new_f1_str = "" if new_f1 is None else f" {new_f1}"
            new_ev_text, n1 = re_f1.subn(
                lambda m: f"{m.group(1)}best_f1_score:{new_f1_str}",
                ev_text, count=1,
            )
            new_ev_text, n2 = re_bml.subn(
                lambda m: f"{m.group(1)}best_mapping_level: "
                          f'"{fnd.target_level}"',
                new_ev_text, count=1,
            )
            if n1 == 0 or n2 == 0:
                actions.append({"edge_id": fnd.edge_id, "action": "skipped",
                                "reason": f"field_not_found (f1={n1}, bml={n2})"})
                continue

            new_edge_block = (
                edge_block[:ev_start] + new_ev_text + edge_block[ev_end:]
            )
            text = text[:edge_start] + new_edge_block + text[edge_end:]

            actions.append({
                "timestamp": datetime.now(tz=timezone.utc).isoformat(),
                "edge_id": fnd.edge_id,
                "graph_file": str(fnd.graph_file.relative_to(repo_root())),
                "target_accession": fnd.target_accession,
                "source_cluster_label": fnd.source_cluster_label,
                "run_ref": fnd.run_ref,
                "old_f1": old_f1,
                "new_f1": new_f1,
                "old_mapping_level": fnd.best_mapping_level,
                "new_mapping_level": fnd.target_level,
                "action": "rewrote" if new_f1 is not None else "set_null",
                "lookup_status": status,
            })

        path.write_text(text, encoding="utf-8")

    # Sidecar log so the corrections are auditable without bloating
    # the curator-authored explanation fields.
    log_path = log_path or (
        repo_root() / "research" / "validation" / "methods_audits"
        / "at_f1_attribution" / "log.json"
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    if log_path.exists():
        try:
            existing = json.loads(log_path.read_text(encoding="utf-8"))
        except Exception:
            existing = []
    existing.extend(actions)
    log_path.write_text(json.dumps(existing, indent=2, default=str))

    return actions


def main() -> int:
    """CLI: ``python -m evidencell.at_f1_attribution [--apply]``."""
    import argparse
    import json

    p = argparse.ArgumentParser(
        prog="python -m evidencell.at_f1_attribution",
        description="Audit and (with --apply) correct AT evidence whose "
                    "best_mapping_level disagrees with the edge target's level.",
    )
    p.add_argument("--apply", action="store_true",
                   help="Rewrite the affected YAML files in place.")
    p.add_argument("--taxonomy", default="CCN20230722")
    args = p.parse_args()

    findings = find_mismatches()
    print(f"Found {len(findings)} AT-evidence items with level mismatch:")
    print()
    for f in findings:
        rel = str(f.graph_file.relative_to(repo_root()))
        print(
            f"  {rel}:{f.edge_id}\n"
            f"    target={f.target_accession} (level={f.target_level})\n"
            f"    best_mapping_level={f.best_mapping_level} "
            f"recorded_f1={f.recorded_f1}\n"
            f"    run_ref={f.run_ref}  source_label={f.source_cluster_label!r}"
        )

    if not args.apply:
        print()
        print("(Dry-run. Re-run with --apply to rewrite YAML files.)")
        return 0

    print()
    print("Applying corrections…")
    actions = apply_corrections(findings, taxonomy_id=args.taxonomy)
    print(json.dumps(actions, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
