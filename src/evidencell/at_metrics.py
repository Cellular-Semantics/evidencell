"""Programmatic AT metrics: migration, lookup, and edge-payload writers.

This module is the structural fix for the AT metrics divergence audit
(planning/at_metrics_divergence_audit_2026-05-14.md). It takes the LLM
out of the F1-transcription loop:

  1. ``migrate_csv``  — convert legacy ``f1_*.csv`` files in
     ``kb/annotation_transfer_runs/{run_id}/`` into schema-compliant
     ``at_results.yaml`` (an ``AnnotationTransferResultSet``).
  2. ``load_result_set`` / ``lookup_metrics`` — read the YAML and
     return F1 rows for a (run_id, source_label, target_accession).
  3. ``compute_edge_metrics``  — given (run_ref, source_label,
     edge_target), return a populated
     ``AnnotationTransferEvidence``-ready payload
     (metrics_by_level, best_mapping_rank, supports defaulted from the
     best-rank F1 against a noise floor).

Step 4 will land lookup + compute_edge_metrics; this commit lands
migration.

CSV shape notes (two variants in use across the 7 known runs):

  Shape A — "best per (source, level)":
    columns: source_label, level, best_target, n_cells, group_purity,
             target_purity, f1, median_boot
    files: ``f1_scores_best.csv``, ``f1_scores_aggregated_best.csv``
    one row per (source_label, level), describing the source's
    single best target.

  Shape B — "full matrix":
    columns: source_label, level, target_name, n_cells, group_purity,
             target_purity, f1, mean_boot, median_boot
    files: ``f1_matrix*.csv``
    many rows per (source_label, level), one per observed target.

Both map onto ``AnnotationTransferMetricRow``; Shape A simply yields
fewer rows. The migration preserves every row as-is.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from ._models import (
    AnnotationTransferLevelResult,
    AnnotationTransferMetricRow,
    AnnotationTransferResultSet,
)
from .paths import repo_root

# ─── Taxonomy ancestry lookup (lineage-aware mode) ────────────────────


def _taxonomy_db_path(taxonomy_id: str) -> Path:
    return repo_root() / "kb" / "taxonomy" / taxonomy_id / f"{taxonomy_id}.db"


def ancestor_accession_by_level(
    edge_target: str, taxonomy_id: str
) -> dict[str, str]:
    """For a node's accession, return ``{taxonomy_level: ancestor_accession}``
    walking parent_ids in the taxonomy SQLite DB. The result includes the
    node itself (at its own level) plus every ancestor up to the root.

    Levels below the node's own (e.g. CLUSTER level for an edge to a
    supertype) are absent — clusters are descendants, not ancestors.

    Used by lineage-aware `compute_edge_metrics` to fill `metrics_by_level`
    with F1 of (source, ancestor) at each rank.
    """
    import sqlite3

    db_path = _taxonomy_db_path(taxonomy_id)
    if not db_path.is_file():
        return {}
    conn = sqlite3.connect(str(db_path))
    try:
        out: dict[str, str] = {}
        # The taxonomy DB keys nodes by either `node_id` (CURIE-style)
        # or `short_form` (bare accession). Edge targets in KB graphs
        # use the bare accession (e.g. CS20230722_SUPT_0216), so try
        # short_form first.
        cur = edge_target
        seen: set[str] = set()
        while cur and cur not in seen:
            seen.add(cur)
            row = conn.execute(
                "SELECT short_form, taxonomy_level, parent_id "
                "FROM nodes WHERE short_form = ? OR node_id = ?",
                (cur, cur),
            ).fetchone()
            if not row:
                break
            sf, level, parent = row
            if level:
                out[str(level).upper()] = sf
            if not parent:
                break
            cur = parent
        return out
    finally:
        conn.close()

# ─── Level / rank conventions ─────────────────────────────────────────

_LEVEL_TO_INFIX: dict[str, str] = {
    "CLASS": "CLAS",
    "SUBCLASS": "SUBC",
    "SUPERTYPE": "SUPT",
    "CLUSTER": "CLUS",
}

_LEVEL_TO_RANK: dict[str, int] = {
    "CLASS": 3,
    "SUBCLASS": 2,
    "SUPERTYPE": 1,
    "CLUSTER": 0,
}

# Taxonomy ID → accession ID prefix. CCN20230722 (the WMBv1 internal ID)
# emits accessions of the form CS20230722_{INFIX}_{N} — the "CN" is
# dropped. Other taxonomies use their full ID as the prefix. Extend this
# map when new taxonomies are added.
_TAXONOMY_ACCESSION_PREFIX: dict[str, str] = {
    "CCN20230722": "CS20230722",
}


def _accession_prefix(taxonomy_id: str) -> str:
    return _TAXONOMY_ACCESSION_PREFIX.get(taxonomy_id, taxonomy_id)


def _normalise_level(raw: str) -> str:
    """Lowercase 'cluster' / mixed-case → canonical 'CLUSTER'."""
    s = (raw or "").strip().upper()
    if s in _LEVEL_TO_INFIX:
        return s
    raise ValueError(f"Unrecognised taxonomy level: {raw!r}")


def _derive_target_accession(
    taxonomy_id: str, level: str, target_name: str
) -> str:
    """Reconstruct ``{taxonomy_id}_{INFIX}_{NN}`` from the leading
    digits of a target_name like "0206 Pvalb Gaba_2" → "CS20230722_SUPT_0206".

    Raises ValueError when target_name doesn't start with the expected
    numeric ID — these are real curation errors and should fail loud.
    """
    infix = _LEVEL_TO_INFIX[level]
    m = re.match(r"^\s*(\d+)\s", str(target_name))
    if not m:
        raise ValueError(
            f"Cannot derive accession at level {level} from "
            f"target_name={target_name!r} (no leading numeric ID)"
        )
    digits = m.group(1)
    return f"{_accession_prefix(taxonomy_id)}_{infix}_{digits}"


# ─── Migration: CSV → at_results.yaml ─────────────────────────────────

_BEST_PREFIXES = ("f1_scores_best", "f1_scores_aggregated_best")
_MATRIX_PREFIX = "f1_matrix"


def _variant_suffix_for(csv_path: Path) -> str | None:
    """Pick the YAML basename suffix for this CSV.

    Returns the variant portion (or empty string for the canonical
    base file). E.g.:
        f1_scores_best.csv            → ""        → at_results.yaml
        f1_scores_aggregated_best.csv → ""        → at_results.yaml
        f1_matrix.csv                 → ""        → at_results.yaml
        f1_matrix_chamberland.csv     → "_chamberland"
                                                  → at_results_chamberland.yaml
        f1_matrix_chamberland_by_class.csv
                                       → "_chamberland_by_class"
                                                  → at_results_chamberland_by_class.yaml
        f1_matrix_harris_class.csv    → "_harris_class"
                                                  → at_results_harris_class.yaml

    Returns ``None`` for files that don't match either prefix (e.g.
    ``mmc_results.csv`` — raw cell-level output, not metrics).
    """
    name = csv_path.stem
    if name.startswith(_BEST_PREFIXES):
        return ""
    if name.startswith(_MATRIX_PREFIX):
        rest = name[len(_MATRIX_PREFIX) :]
        return rest  # may be "" for plain f1_matrix.csv
    return None


def _read_csv_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _row_to_metric_row(
    raw: dict[str, str], taxonomy_id: str
) -> AnnotationTransferMetricRow:
    """Convert one CSV dict-row into an AnnotationTransferMetricRow.

    Handles both Shape A (`best_target` column) and Shape B
    (`target_name` column). Floats are coerced; missing columns become
    None. The Pydantic model enforces the required-field contract.
    """
    level = _normalise_level(raw["level"])
    target_name = raw.get("target_name") or raw.get("best_target")
    if not target_name:
        raise ValueError(
            f"CSV row has neither target_name nor best_target: {raw}"
        )
    target_accession = _derive_target_accession(
        taxonomy_id, level, target_name
    )

    def _float(key: str) -> float | None:
        v = raw.get(key)
        if v is None or v == "":
            return None
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    def _int(key: str) -> int | None:
        v = raw.get(key)
        if v is None or v == "":
            return None
        try:
            return int(float(v))
        except (TypeError, ValueError):
            return None

    return AnnotationTransferMetricRow(
        source_label=raw["source_label"],
        taxonomy_level=level,
        taxonomy_rank=_LEVEL_TO_RANK[level],
        target_name=str(target_name),
        target_accession=target_accession,
        n_cells=_int("n_cells"),
        group_purity=_float("group_purity"),
        target_purity=_float("target_purity"),
        f1=_float("f1"),
        median_bootstrap=_float("median_boot"),
        mean_bootstrap=_float("mean_boot"),
    )


def migrate_csv(
    run_dir: Path,
    csv_name: str,
    taxonomy_id: str,
    *,
    generator: str = "src/evidencell/at_metrics.py::migrate_csv",
) -> tuple[Path, AnnotationTransferResultSet]:
    """Migrate one CSV in ``run_dir`` into a sibling
    ``at_results[<variant>].yaml`` file.

    Returns ``(yaml_path, result_set)``. Writes the YAML atomically
    (temp + rename). Existing YAML at the target path is overwritten;
    callers can diff externally before invoking.
    """
    csv_path = run_dir / csv_name
    if not csv_path.is_file():
        raise FileNotFoundError(csv_path)
    suffix = _variant_suffix_for(csv_path)
    if suffix is None:
        raise ValueError(
            f"CSV {csv_path.name} doesn't match the expected "
            f"f1_scores_*.csv / f1_matrix*.csv naming convention."
        )

    raw_rows = _read_csv_rows(csv_path)
    metric_rows = [_row_to_metric_row(r, taxonomy_id) for r in raw_rows]

    run_id = run_dir.name
    result_set = AnnotationTransferResultSet(
        run_id=run_id,
        taxonomy_id=taxonomy_id,
        normalisation=(suffix.lstrip("_") if suffix else None),
        source_csv_relpath=csv_path.name,
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        generator=generator,
        rows=metric_rows,
    )

    yaml_path = run_dir / f"at_results{suffix}.yaml"
    _atomic_write_yaml(yaml_path, result_set.model_dump(exclude_none=True))
    return yaml_path, result_set


def _atomic_write_yaml(path: Path, payload: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    tmp.replace(path)


def _taxonomy_id_from_manifest(run_dir: Path) -> str | None:
    manifest = run_dir / "manifest.yaml"
    if not manifest.is_file():
        return None
    try:
        doc = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return None
    return doc.get("target_taxonomy_id") or doc.get("taxonomy_id")


def migrate_run(
    run_dir: Path,
    *,
    taxonomy_id: str | None = None,
) -> list[Path]:
    """Migrate every metric-bearing CSV in ``run_dir``.

    Resolves taxonomy_id from the manifest if not supplied. Falls back
    to deriving mapping proportions from a per-cell ``mapping_result.csv``
    / ``mmc_output.csv`` (referenced by manifest ``output.relpath``)
    when no f1_*.csv exists in the run dir — Bhatt-2025 pattern. Returns
    the list of YAML paths written. Skips files that aren't metric CSVs
    (e.g. raw ``mmc_results.csv`` in the run dir).
    """
    tax_id = taxonomy_id or _taxonomy_id_from_manifest(run_dir)
    if not tax_id:
        raise ValueError(
            f"Cannot resolve taxonomy_id for {run_dir} — "
            f"pass --taxonomy or add target_taxonomy_id to manifest.yaml."
        )
    written: list[Path] = []
    for csv_path in sorted(run_dir.glob("*.csv")):
        suffix = _variant_suffix_for(csv_path)
        if suffix is None:
            continue  # not a metrics CSV
        yaml_path, _ = migrate_csv(run_dir, csv_path.name, tax_id)
        written.append(yaml_path)
    if not written:
        prop_path = migrate_proportions_from_manifest(run_dir, tax_id)
        if prop_path is not None:
            written.append(prop_path)
    return written


# ─── Proportions migration (no F1 available) ──────────────────────────


_LEVEL_COLS: list[tuple[str, str, str]] = [
    # (taxonomy_level, accession_column, name_column)
    ("CLASS",     "class_label",     "class_name"),
    ("SUBCLASS",  "subclass_label",  "subclass_name"),
    ("SUPERTYPE", "supertype_label", "supertype_name"),
    ("CLUSTER",   "cluster_label",   "cluster_name"),
]


def _read_mmc_results(path: Path) -> tuple[list[str], list[list[str]]]:
    """Parse a MapMyCells per-cell output CSV.

    Skips leading comment lines starting with ``#`` (the metadata
    header). Returns ``(header, rows)`` of column-aligned data.
    """
    header: list[str] = []
    rows: list[list[str]] = []
    with path.open("r", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        for raw in reader:
            if not raw or raw[0].startswith("#"):
                continue
            if not header:
                header = raw
                continue
            rows.append(raw)
    return header, rows


def derive_proportions_from_mmc(
    mmc_rows: list[dict[str, str]],
    *,
    source_label: str,
    taxonomy_id: str,
) -> list[AnnotationTransferMetricRow]:
    """Aggregate per-cell mapping output into per-(level, target)
    proportions.

    For each level, counts cells per target_label and emits a row with
    ``group_purity = count / total`` (precision-side mass on this
    target), ``n_cells = count``, and ``f1 / target_purity = None``
    (no source-side cluster labels = no recall side).
    """
    total = len(mmc_rows)
    if total == 0:
        return []
    out: list[AnnotationTransferMetricRow] = []
    for level, accn_col, name_col in _LEVEL_COLS:
        counts: dict[str, tuple[str, int]] = {}  # accn → (name, count)
        for r in mmc_rows:
            accn = r.get(accn_col)
            if not accn:
                continue
            name = r.get(name_col) or ""
            existing = counts.get(accn)
            if existing is None:
                counts[accn] = (name, 1)
            else:
                counts[accn] = (existing[0], existing[1] + 1)
        for accn, (name, n) in counts.items():
            out.append(
                AnnotationTransferMetricRow(
                    source_label=source_label,
                    taxonomy_level=level,
                    taxonomy_rank=_LEVEL_TO_RANK[level],
                    target_name=name,
                    target_accession=accn,
                    n_cells=n,
                    group_purity=n / total,
                    target_purity=None,
                    f1=None,
                )
            )
    return out


def migrate_proportions_from_manifest(
    run_dir: Path, taxonomy_id: str
) -> Path | None:
    """Read the manifest's ``output.relpath``, resolve relative to
    ``run_dir``, parse the per-cell MMC CSV, and write proportions
    into an ``at_results.yaml``.

    Returns the YAML path, or ``None`` if the manifest doesn't declare
    an output path or the file is missing. Source label is read from
    the manifest's ``source_cluster_label`` field.
    """
    manifest_path = run_dir / "manifest.yaml"
    if not manifest_path.is_file():
        return None
    doc = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    output = doc.get("output") or {}
    relpath = output.get("relpath")
    if not relpath:
        return None
    # Try several resolution strategies: as-given (absolute), relative
    # to run_dir, and relative to repo root. The third covers manifests
    # whose ../../.. counts are stale (e.g. after a run dir rename) or
    # written as if from a different root.
    candidates = [
        (run_dir / relpath).resolve(),
        (repo_root() / relpath.lstrip("./")).resolve()
        if not relpath.startswith("/")
        else Path(relpath),
    ]
    # Also try matching a research/ subpath of the manifest's relpath
    # against the repo root — strips any leading `../`.
    stripped = relpath
    while stripped.startswith("../"):
        stripped = stripped[3:]
    candidates.append((repo_root() / stripped).resolve())

    csv_path = next((c for c in candidates if c.is_file()), None)
    if csv_path is None:
        print(
            f"  WARNING: manifest output relpath {relpath!r} not found via any of "
            f"{[str(c) for c in candidates]}",
            file=sys.stderr,
        )
        return None

    source_label = (doc.get("source_cluster_label") or "").strip()
    if not source_label:
        print(
            f"  WARNING: manifest missing source_cluster_label; skipping {run_dir}",
            file=sys.stderr,
        )
        return None

    header, raw_rows = _read_mmc_results(csv_path)
    mmc_rows = [dict(zip(header, r)) for r in raw_rows]
    rows = derive_proportions_from_mmc(
        mmc_rows, source_label=source_label, taxonomy_id=taxonomy_id
    )
    if not rows:
        return None

    rs = AnnotationTransferResultSet(
        run_id=run_dir.name,
        taxonomy_id=taxonomy_id,
        normalisation="proportions",
        source_csv_relpath=relpath,
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        generator=(
            "src/evidencell/at_metrics.py::migrate_proportions_from_manifest"
        ),
        rows=rows,
    )
    yaml_path = run_dir / "at_results.yaml"
    _atomic_write_yaml(yaml_path, rs.model_dump(exclude_none=True))
    return yaml_path


def migrate_all(
    runs_root: Path | None = None,
) -> dict[str, list[Path]]:
    """Migrate every CSV across every run dir under
    ``kb/annotation_transfer_runs/``. Returns ``{run_id: [yaml_paths]}``.
    """
    runs_root = runs_root or (repo_root() / "kb" / "annotation_transfer_runs")
    out: dict[str, list[Path]] = {}
    for run_dir in sorted(runs_root.iterdir()):
        if not run_dir.is_dir():
            continue
        try:
            written = migrate_run(run_dir)
        except (ValueError, FileNotFoundError) as exc:
            print(f"  SKIP {run_dir.name}: {exc}", file=sys.stderr)
            continue
        out[run_dir.name] = written
    return out


# ─── Lookup + edge-payload writers ────────────────────────────────────

# F1 noise floor below which an AT evidence item should not assert
# positive support — `supports: NO_EVIDENCE` rather than PARTIAL/SUPPORT.
# The compute_edge_metrics() helper applies this when callers don't
# override. Chosen conservatively: 0.10 corresponds to roughly 10%
# F1 — well below anything we'd want to cite as positive evidence.
NOISE_FLOOR_F1: float = 0.10


def load_result_set(
    run_ref: str,
    *,
    variant: str | None = None,
    runs_root: Path | None = None,
) -> AnnotationTransferResultSet:
    """Load the at_results YAML for ``run_ref``.

    ``variant`` selects between sibling files (e.g. ``"by_class"`` for
    Chamberland's within-class-normalised result set). ``None`` loads
    the canonical ``at_results.yaml`` if present, else the *first*
    ``at_results_*.yaml`` found alphabetically (with a warning) — but
    callers should pass an explicit ``variant`` whenever a run has
    multiple files to avoid silent variant-pick.
    """
    runs_root = runs_root or (repo_root() / "kb" / "annotation_transfer_runs")
    run_dir = runs_root / run_ref
    if not run_dir.is_dir():
        raise FileNotFoundError(f"AT run dir not found: {run_dir}")

    candidates = sorted(run_dir.glob("at_results*.yaml"))
    if not candidates:
        raise FileNotFoundError(
            f"No at_results YAML in {run_dir} — run "
            f"`uv run python -m evidencell.at_metrics migrate {run_dir}` first."
        )

    if variant is None:
        canonical = run_dir / "at_results.yaml"
        chosen = canonical if canonical.is_file() else candidates[0]
        if chosen != canonical and len(candidates) > 1:
            print(
                f"WARNING: {run_dir.name} has multiple at_results files; "
                f"defaulting to {chosen.name}. Pass variant= to disambiguate.",
                file=sys.stderr,
            )
    else:
        wanted = run_dir / f"at_results_{variant}.yaml"
        if not wanted.is_file():
            raise FileNotFoundError(
                f"No at_results variant {variant!r} in {run_dir} — "
                f"available: {[p.name for p in candidates]}"
            )
        chosen = wanted

    doc = yaml.safe_load(chosen.read_text(encoding="utf-8"))
    return AnnotationTransferResultSet(**doc)


def lookup_metrics(
    result_set: AnnotationTransferResultSet,
    source_label: str,
    target_accession: str,
) -> dict[str, AnnotationTransferMetricRow]:
    """Return the metric row for each level where ``source_label`` has
    a recorded mapping to ``target_accession``.

    Keyed by ``taxonomy_level``. Empty dict if the (source, target)
    pair never appears in the set — typical when the AT run only
    persisted source-best rows (Shape A) and ``target_accession`` is
    not the source's best at any level.
    """
    out: dict[str, AnnotationTransferMetricRow] = {}
    for row in result_set.rows:
        if row.source_label == source_label and row.target_accession == target_accession:
            out[row.taxonomy_level] = row
    return out


def source_best_at_each_level(
    result_set: AnnotationTransferResultSet, source_label: str
) -> dict[str, AnnotationTransferMetricRow]:
    """Return the source's highest-F1 row at each taxonomy level.

    Useful when ``lookup_metrics(... edge_target)`` is empty — surfaces
    where the source *did* map, so the report-time agent has context
    about what the AT signal actually says.
    """
    by_level: dict[str, AnnotationTransferMetricRow] = {}
    for row in result_set.rows:
        if row.source_label != source_label:
            continue
        existing = by_level.get(row.taxonomy_level)
        if existing is None or (row.f1 or 0) > (existing.f1 or 0):
            by_level[row.taxonomy_level] = row
    return by_level


def _row_to_level_result(
    row: AnnotationTransferMetricRow,
) -> AnnotationTransferLevelResult:
    """Project a MetricRow → LevelResult (the slot type on
    AnnotationTransferEvidence.metrics_by_level).
    """
    return AnnotationTransferLevelResult(
        taxonomy_level=row.taxonomy_level,
        taxonomy_rank=row.taxonomy_rank,
        best_target_name=row.target_name or "",
        best_target_accession=row.target_accession,
        group_purity=row.group_purity,
        target_purity=row.target_purity,
        f1_score=row.f1,
        n_cells_mapped=row.n_cells,
        median_bootstrap=row.median_bootstrap,
    )


def compute_edge_metrics(
    run_ref: str,
    source_label: str,
    edge_target: str,
    *,
    variant: str | None = None,
    noise_floor: float = NOISE_FLOOR_F1,
    runs_root: Path | None = None,
    lineage_aware: bool = True,
) -> dict:
    """Build the AT-payload subset to write onto a MappingEdge's AT
    evidence item.

    Default mode is **lineage-aware**: for each taxonomy level L from
    CLASS down to ``edge_target``'s own level, look up F1 for
    ``(source, ancestor_of_edge_target_at_L)`` in the AT result set.
    A row at level L tells the reader whether the source converged
    toward the edge target's lineage at that level. Missing rows
    above ``edge_target``'s own level are themselves signal —
    the source did not reach the right lineage at L. See
    ``docs/at_data_flow.md`` § "Decision record: lineage-aware".

    Set ``lineage_aware=False`` for the strict semantic (only rows
    where ``(source, edge_target)`` matches exactly).

    Returns a dict with keys:
      ``metrics_by_level``      — list of AnnotationTransferLevelResult dicts.
                                  Under lineage-aware: one row per
                                  ancestor of ``edge_target`` that has
                                  AT data for ``source_label``. Under
                                  strict: at most one row.
      ``best_mapping_rank``     — taxonomy_rank of the row with highest F1.
      ``best_f1_score``         — best F1 across emitted rows.
      ``f1_source_relpath``     — filename of the at_results YAML used.
      ``supports_default``      — suggested ``supports``: SUPPORT if
                                  best_f1 >= 0.6, PARTIAL if >= noise_floor,
                                  NO_EVIDENCE otherwise.
      ``source_best_summary``   — dict[level → {target_accession, f1,
                                  is_edge_target_lineage}]: where the
                                  source actually went at each level, with
                                  a flag for whether the source's best at
                                  that level is in edge_target's lineage.
      ``lineage_aware``         — True / False, the mode used.

    The function is read-only — it doesn't write to the edge.
    """
    rs = load_result_set(run_ref, variant=variant, runs_root=runs_root)

    target_per_level: dict[str, str]
    if lineage_aware:
        ancestors = ancestor_accession_by_level(
            edge_target, rs.taxonomy_id
        )
        if ancestors:
            target_per_level = ancestors
        else:
            # Taxonomy DB missing — fall back to strict (lookup
            # edge_target itself at whichever level it appears).
            target_per_level = {
                row.taxonomy_level: edge_target
                for row in rs.rows
                if row.target_accession == edge_target
            }
    else:
        # Strict: only the row where target == edge_target.
        target_per_level = {
            row.taxonomy_level: edge_target
            for row in rs.rows
            if row.target_accession == edge_target
        }

    metrics_by_level: list[AnnotationTransferLevelResult] = []
    best_f1 = None
    best_rank = None
    # Emit in canonical rank order (root → leaf) for stable diffs.
    for level in ("CLASS", "SUBCLASS", "SUPERTYPE", "CLUSTER"):
        wanted_target = target_per_level.get(level)
        if not wanted_target:
            continue
        rows = lookup_metrics(rs, source_label, wanted_target)
        row = rows.get(level)
        if row is None:
            continue
        metrics_by_level.append(_row_to_level_result(row))
        f1 = row.f1 or 0
        if best_f1 is None or f1 > best_f1:
            best_f1 = f1
            best_rank = row.taxonomy_rank

    if best_f1 is None:
        supports_default = "NO_EVIDENCE"
    elif best_f1 >= 0.6:
        supports_default = "SUPPORT"
    elif best_f1 >= noise_floor:
        supports_default = "PARTIAL"
    else:
        supports_default = "NO_EVIDENCE"

    source_best = source_best_at_each_level(rs, source_label)
    lineage = (
        ancestor_accession_by_level(edge_target, rs.taxonomy_id)
        if lineage_aware
        else {}
    )
    source_best_summary = {
        lvl: {
            "target_accession": r.target_accession,
            "target_name": r.target_name,
            "f1": r.f1,
            "is_edge_target": r.target_accession == edge_target,
            "is_edge_target_lineage": (
                r.target_accession == lineage.get(lvl)
                if lineage_aware
                else (r.target_accession == edge_target)
            ),
        }
        for lvl, r in source_best.items()
    }

    return {
        "metrics_by_level": [
            m.model_dump(exclude_none=True) for m in metrics_by_level
        ],
        "best_mapping_rank": best_rank,
        "best_f1_score": best_f1,
        "f1_source_relpath": _yaml_relpath_for(rs),
        "supports_default": supports_default,
        "source_best_summary": source_best_summary,
        "lineage_aware": lineage_aware,
    }


def _yaml_relpath_for(rs: AnnotationTransferResultSet) -> str:
    """Reconstruct the at_results filename from a loaded result set."""
    if rs.normalisation:
        return f"at_results_{rs.normalisation}.yaml"
    return "at_results.yaml"


# ─── research/{region}/at/{classical}_{taxonomy}_f1.json regen ────────


def regen_at_hits_file(
    *,
    classical_node_id: str,
    region: str,
    taxonomy_id: str,
    run_ref: str,
    source_label: str,
    f1_floor: float = 0.2,
    out_path: Path | None = None,
    runs_root: Path | None = None,
) -> Path:
    """Regenerate the legacy `research/{region}/at/{classical}_{taxonomy}_f1.json`
    discovery-hint file from the canonical at_results.yaml.

    The file format (consumed by ``find_candidates`` Stage A scoring) is:
        {
          "classical_node_id": ..., "taxonomy_id": ...,
          "source_run_id": ..., "source_cluster_label": ...,
          "f1_floor": ..., "hits": [{target_accession, target_level,
                                     target_name, f1, n_cells,
                                     group_purity, target_purity}]
        }

    The regenerated file is guaranteed to match at_results.yaml row-for-row
    (filtered to F1 >= f1_floor for source_label across all levels).
    Replaces any existing file at the destination path.
    """
    import json

    rs = load_result_set(run_ref, runs_root=runs_root)
    level_to_str = {
        "CLASS": "class",
        "SUBCLASS": "subclass",
        "SUPERTYPE": "supertype",
        "CLUSTER": "cluster",
    }
    hits = []
    for row in rs.rows:
        if row.source_label != source_label:
            continue
        if (row.f1 or 0) < f1_floor:
            continue
        hits.append({
            "target_accession": row.target_accession,
            "target_level": level_to_str.get(row.taxonomy_level, row.taxonomy_level.lower()),
            "target_name": row.target_name,
            "f1": row.f1,
            "n_cells": row.n_cells,
            "group_purity": row.group_purity,
            "target_purity": row.target_purity,
        })
    payload = {
        "classical_node_id": classical_node_id,
        "taxonomy_id": taxonomy_id,
        "source_run_id": run_ref,
        "source_cluster_label": source_label,
        "f1_floor": f1_floor,
        "hits": hits,
    }
    if out_path is None:
        out_path = (
            (runs_root.parent.parent if runs_root else repo_root())
            / "research" / region / "at"
            / f"{classical_node_id}_{taxonomy_id}_f1.json"
        )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return out_path


# ─── KB sweep / refresh ───────────────────────────────────────────────


def _kb_graph_files(kb_root: Path | None = None) -> list[Path]:
    kb_root = kb_root or (repo_root() / "kb" / "graphs")
    return sorted(kb_root.rglob("*.yaml"))


def _is_at_evidence(item: dict) -> bool:
    return item.get("evidence_type") == "ANNOTATION_TRANSFER"


def _format_payload_for_diff(payload: dict) -> str:
    """One-line summary of an edge's AT-evidence-payload, for diff
    output."""
    n = len(payload.get("metrics_by_level") or [])
    bf = payload.get("best_f1_score")
    bf_s = f"{bf:.3f}" if isinstance(bf, (int, float)) else "—"
    return (
        f"metrics_levels={n} best_f1={bf_s} "
        f"supports_default={payload.get('supports_default')} "
        f"f1_source={payload.get('f1_source_relpath')}"
    )


def refresh_kb(
    *,
    dry_run: bool = True,
    only_with_run_ref: bool = True,
    kb_root: Path | None = None,
    runs_root: Path | None = None,
) -> dict:
    """Walk every MappingEdge.evidence[] AT item with a ``run_ref``,
    recompute the payload via ``compute_edge_metrics()``, and report a
    diff against what's stored.

    With ``dry_run=False`` writes the recomputed metrics_by_level back
    to the edge YAML (preserving everything else). The ``supports``
    field is **not** automatically overwritten — that's a curator
    call; we surface the suggested ``supports_default`` in the diff
    output instead.

    Returns a summary dict ``{file: [{edge_id, evidence_index, diff,
    old_supports, suggested_supports}]}``.
    """
    out: dict[str, list[dict]] = {}
    for path in _kb_graph_files(kb_root):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        rows: list[dict] = []
        changed = False
        for edge in doc.get("edges") or []:
            edge_target = edge.get("taxonomy_type") or edge.get("type_b")
            if not edge_target:
                continue
            for idx, ev in enumerate(edge.get("evidence") or []):
                if not _is_at_evidence(ev):
                    continue
                run_ref = ev.get("run_ref")
                if not run_ref:
                    if only_with_run_ref:
                        continue
                    rows.append(
                        {
                            "edge_id": edge.get("id"),
                            "evidence_index": idx,
                            "status": "skipped:no_run_ref",
                        }
                    )
                    continue
                src = ev.get("source_cluster_label")
                if not src:
                    rows.append(
                        {
                            "edge_id": edge.get("id"),
                            "evidence_index": idx,
                            "status": "skipped:no_source_label",
                        }
                    )
                    continue
                try:
                    payload = compute_edge_metrics(
                        run_ref=run_ref,
                        source_label=src,
                        edge_target=edge_target,
                        runs_root=runs_root,
                    )
                except (FileNotFoundError, ValueError) as exc:
                    rows.append(
                        {
                            "edge_id": edge.get("id"),
                            "evidence_index": idx,
                            "status": f"skipped:{type(exc).__name__}",
                            "detail": str(exc),
                        }
                    )
                    continue
                old_levels = ev.get("metrics_by_level") or []
                new_levels = payload["metrics_by_level"]
                old_supports = ev.get("supports")
                row = {
                    "edge_id": edge.get("id"),
                    "evidence_index": idx,
                    "source_label": src,
                    "edge_target": edge_target,
                    "old_n_levels": len(old_levels),
                    "new_n_levels": len(new_levels),
                    "diff": _format_payload_for_diff(payload),
                    "old_supports": old_supports,
                    "suggested_supports": payload["supports_default"],
                    "f1_source_relpath": payload["f1_source_relpath"],
                }
                rows.append(row)
                if old_levels != new_levels and not dry_run:
                    ev["metrics_by_level"] = new_levels
                    ev["f1_source_relpath"] = payload["f1_source_relpath"]
                    changed = True
        if rows:
            try:
                key = str(path.relative_to(repo_root()))
            except ValueError:
                key = str(path)
            out[key] = rows
        if changed and not dry_run:
            path.write_text(
                yaml.safe_dump(doc, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )
    return out


def print_refresh_report(summary: dict) -> None:
    for path, rows in summary.items():
        print(f"\n=== {path} ===")
        for r in rows:
            head = (
                f"  [{r.get('evidence_index')}] {r.get('edge_id')} :: "
                f"{r.get('source_label','-')} -> {r.get('edge_target','-')}"
            )
            if "status" in r:
                print(f"{head}  STATUS={r['status']}")
                if "detail" in r:
                    print(f"      {r['detail']}")
                continue
            print(f"{head}")
            print(f"      {r['diff']}")
            if r["old_supports"] != r["suggested_supports"]:
                print(
                    f"      supports: {r['old_supports']} → "
                    f"{r['suggested_supports']}  (suggested; not auto-applied)"
                )
            if r["old_n_levels"] != r["new_n_levels"]:
                print(
                    f"      metrics_by_level: {r['old_n_levels']} levels "
                    f"→ {r['new_n_levels']} levels"
                )


# ─── CLI ──────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.at_metrics",
        description=(
            "Programmatic AT metrics tooling: migrate legacy CSVs to "
            "schema-compliant at_results.yaml; (later) populate "
            "MappingEdge.evidence[].metrics_by_level by lookup."
        ),
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_migrate = sub.add_parser(
        "migrate",
        help="Convert f1_*.csv in a run dir to at_results[*].yaml",
    )
    p_migrate.add_argument(
        "run_dir", type=Path, help="kb/annotation_transfer_runs/<run_id>/"
    )
    p_migrate.add_argument(
        "--taxonomy",
        default=None,
        help="Taxonomy ID (e.g. CCN20230722); read from manifest.yaml if omitted.",
    )

    p_migrate_all = sub.add_parser(
        "migrate-all",
        help="Migrate every run dir under kb/annotation_transfer_runs/.",
    )
    p_migrate_all.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Override the runs root (default: repo's kb/annotation_transfer_runs/).",
    )

    p_refresh = sub.add_parser(
        "refresh",
        help=(
            "Recompute metrics_by_level on every AT evidence item across "
            "kb/graphs/ using compute_edge_metrics(). Dry-run by default; "
            "pass --apply to write."
        ),
    )
    p_refresh.add_argument(
        "--apply",
        action="store_true",
        help="Write recomputed metrics back to the edge YAMLs.",
    )
    p_refresh.add_argument(
        "--kb-root",
        type=Path,
        default=None,
        help="Override the KB graphs root.",
    )

    args = parser.parse_args(argv)

    if args.cmd == "migrate":
        written = migrate_run(args.run_dir, taxonomy_id=args.taxonomy)
        for p in written:
            print(f"Wrote {p}")
        return 0 if written else 1

    if args.cmd == "migrate-all":
        results = migrate_all(args.root)
        total = sum(len(v) for v in results.values())
        for run, paths in results.items():
            print(f"{run}: {len(paths)} file(s)")
            for p in paths:
                print(f"  {p}")
        print(f"--- Total: {total} at_results YAML files written")
        return 0

    if args.cmd == "refresh":
        summary = refresh_kb(dry_run=not args.apply, kb_root=args.kb_root)
        print_refresh_report(summary)
        n_files = len(summary)
        n_edges = sum(len(v) for v in summary.values())
        mode = "APPLIED" if args.apply else "DRY-RUN (use --apply to write)"
        print(f"\n--- {n_edges} AT evidence items across {n_files} files. {mode}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
