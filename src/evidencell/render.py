"""
evidencell render.py — Fact extractor and Markdown report generator.

Two-layer pipeline:
  1. `facts`   — deterministic extraction: reads KB YAML + references.json, emits
                 report_facts.json with every claim labelled by YAML provenance.
                 No LLM, no hallucination risk.
  2. `summary` / `drilldowns` / `index`
               — direct Markdown output (programmatic mode; use gen-report orchestrator
                 for LLM-assisted synthesis with hallucination guard).

CLI usage:
  python -m evidencell.render facts      <graph_file> --node NODE_ID [--output-dir DIR]
  python -m evidencell.render summary    <graph_file> [--node NODE_ID] [--output-dir DIR]
  python -m evidencell.render drilldowns <graph_file> --node NODE_ID [--pmid PMID] [--output-dir DIR]
  python -m evidencell.render index      <region> [--output-dir DIR]
"""

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import yaml


# ── Constants ─────────────────────────────────────────────────────────────────

CONF_ORDER = {"HIGH": 0, "MODERATE": 1, "LOW": 2, "UNCERTAIN": 3, "REFUTED": 4}
CONF_BADGES = {
    "HIGH": "🟢 HIGH",
    "MODERATE": "🟡 MODERATE",
    "LOW": "🔴 LOW",
    "UNCERTAIN": "⚪ UNCERTAIN",
    "REFUTED": "⛔ REFUTED",
}
EVIDENCE_TYPE_LABELS = {
    "LITERATURE": "Literature",
    "ATLAS_METADATA": "Atlas metadata",
    "ANNOTATION_TRANSFER": "Annotation transfer",
    "SPATIAL_COLOCATION": "Spatial co-location",
    "PATCH_SEQ": "Patch-seq",
    "PROJECTION_SEQ": "Projection-seq",
    "ELECTROPHYSIOLOGY": "Electrophysiology",
    "MORPHOLOGY": "Morphology",
    "MARKER_ANALYSIS": "Marker analysis",
    "ATLAS_QUERY": "Atlas query",
    "BULK_CORRELATION": "Bulk correlation",
}
REL_LABELS = {
    "EQUIVALENT": "≡ EQUIVALENT",
    "PARTIAL_OVERLAP": "~ PARTIAL OVERLAP",
    "CROSS_CUTTING": "✕ CROSS-CUTTING",
    "TYPE_A_SPLITS": "→ TYPE_A_SPLITS",
    "TYPE_A_MERGES": "← TYPE_A_MERGES",
    "SUBSET": "⊂ SUBSET",
    "SUPERSET": "⊃ SUPERSET",
    "NO_CORRESPONDENCE": "∅ NO CORRESPONDENCE",
    "UNCERTAIN": "? UNCERTAIN",
}

DRAFT_BANNER = (
    "> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.\n"
    "> All edges require expert review before use."
)
MERFISH_LOCATION_NOTE = (
    "> **Location note.** WMBv1 location data derives from MERFISH spatial\n"
    "> registration and records **soma position** only. Axonal and dendritic\n"
    "> projection targets are not reflected in atlas cluster location fields and\n"
    "> are not used in mapping assessments."
)


# ── Data class ────────────────────────────────────────────────────────────────

@dataclass
class RefEntry:
    label: str            # "[1]" or "[A]"
    pmid: str | None
    doi: str | None
    corpus_id: str | None
    query_url: str | None
    citation_line: str    # "Author et al. Year · PMID:…"
    used_for: str         # one-line purpose


# ── Helper functions ──────────────────────────────────────────────────────────

def _ot(term: dict | None) -> str:
    """Format an OntologyTerm dict as 'label (id)'."""
    if not term:
        return ""
    label = term.get("label", "")
    tid = term.get("id", "")
    if label and tid:
        return f"{label} ({tid})"
    return label or tid


def _conf_badge(conf: str) -> str:
    return CONF_BADGES.get(conf, conf)


def _rel_badge(rel: str) -> str:
    return REL_LABELS.get(rel, rel)


def _evidence_type_label(et: str) -> str:
    return EVIDENCE_TYPE_LABELS.get(et, et)


def _ref_identifier(ref_str: str) -> tuple[str, str]:
    """Parse 'PMID:31420995' or bare PMID into ('pmid', '31420995')."""
    if ref_str.startswith("PMID:"):
        return "pmid", ref_str[5:]
    if ref_str.startswith("DOI:"):
        return "doi", ref_str[4:]
    # Bare PMID (numeric) or DOI
    if ref_str.replace(".", "").replace("/", "").replace("-", "").isdigit():
        return "pmid", ref_str
    return "doi", ref_str


def _find_corpus_by_pmid(bare_pmid: str, refs: dict) -> dict | None:
    for entry in refs.values():
        if isinstance(entry, dict) and entry.get("pmid") == bare_pmid:
            return entry
    return None


def _find_corpus_by_doi(bare_doi: str, refs: dict) -> dict | None:
    for entry in refs.values():
        if isinstance(entry, dict) and entry.get("doi") == bare_doi:
            return entry
    return None


def _coerce_authors(authors) -> list[str]:
    """Coerce a references.json `authors` field to list[str].

    Canonical shape is list[str]; defensive against the historical bug-class
    documented in planning/minirefs_author_rendering_fix.md, where the
    asta-report-ingest writer has shipped:
      - list[str]                      → returned as-is
      - list[dict] (S2 batch shape)    → extract `name` from each dict
      - "First, Second, ... et al."    → split on commas, strip et-al suffix
      - empty / None / whitespace      → []
    """
    if not authors:
        return []
    if isinstance(authors, str):
        s = authors.strip()
        if not s:
            return []
        # Drop a trailing 'et al.' / 'et al' token (with optional comma before)
        for suffix in (", et al.", ", et al", " et al.", " et al"):
            if s.endswith(suffix):
                s = s[: -len(suffix)].rstrip(",").rstrip()
                break
        return [part.strip() for part in s.split(",") if part.strip()]
    result: list[str] = []
    for a in authors:
        if isinstance(a, str):
            result.append(a)
        elif isinstance(a, dict):
            name = a.get("name", "")
            if name:
                result.append(name)
    return result


def _format_citation_line(entry: dict) -> str:
    """Format a references.json entry as 'Author et al. YYYY · PMID:…'"""
    authors = _coerce_authors(entry.get("authors"))
    year = entry.get("year", "")
    pmid = entry.get("pmid", "")
    doi = entry.get("doi", "")
    if len(authors) == 0:
        author_str = "Unknown"
    elif len(authors) == 1:
        author_str = authors[0].split()[-1]
    elif len(authors) == 2:
        author_str = f"{authors[0].split()[-1]} & {authors[1].split()[-1]}"
    else:
        author_str = f"{authors[0].split()[-1]} et al."
    parts = [f"{author_str} {year}"]
    if pmid:
        parts.append(f"PMID:{pmid}")
    elif doi:
        parts.append(f"DOI:{doi}")
    return " · ".join(parts)


# ── Run-ref → publication PMID resolver ───────────────────────────────────────
#
# Evidence types whose source is a CorrelationRun (BulkCorrelationEvidence,
# future analogues) carry `run_ref: <run_id>`. The publication PMID lives
# indirectly via:
#   evidence.run_ref            → kb/correlation_runs/{run_id}/manifest.yaml
#   manifest.dataset_ref        → kb/datasets/<file>.yaml (lookup by `id`)
#   dataset.source_pmid         → "PMID:NNNN"
#
# Resolved PMIDs feed into build_reference_index() so cited papers appear
# in the report's references table with a [n] label, and into the drilldown
# blockquote rendering so non-LITERATURE evidence narratives carry attributions.

_RUN_REF_PMID_CACHE: dict[str, str | None] = {}
# Cache (run_ref → dataset descriptor dict) so build_reference_index can pull
# authors/year/title for citation-line formatting without re-reading dataset YAMLs.
_RUN_REF_DATASET_CACHE: dict[str, dict] = {}
# Cache (run_ref → full manifest dict) so methods extraction and figure
# generation can read run-level details (script, atlas SHA, contrasts,
# code_version) without re-reading manifests.
_RUN_REF_MANIFEST_CACHE: dict[str, dict] = {}
# Cache (run_ref → run directory Path) for locating ranked output TSVs and
# scripts during figure generation.
_RUN_REF_DIR_CACHE: dict[str, Path | None] = {}


def _resolve_run_ref_to_pmid(run_ref: str) -> str | None:
    """Trace run_ref → manifest.yaml → dataset.yaml → source_pmid.

    Returns "PMID:NNNN" or None if any step fails (file missing, malformed,
    or no source_pmid). Failures are non-fatal — the evidence item still
    flows through the renderer, just without a [n] ref label.

    Side effect: populates `_RUN_REF_DATASET_CACHE[run_ref]` with the dataset
    descriptor (authors, year, title, source_pmid, etc.) when the chain
    resolves. Callers wanting the citation-formatting fields can read from
    that cache directly via `_dataset_for_run_ref()`.

    Cached for the lifetime of the module to avoid re-reading manifests
    when multiple evidence items share a run_ref.
    """
    if run_ref in _RUN_REF_PMID_CACHE:
        return _RUN_REF_PMID_CACHE[run_ref]

    from evidencell.paths import repo_root  # local to avoid import cycles
    try:
        root = repo_root()
    except RuntimeError:
        _RUN_REF_PMID_CACHE[run_ref] = None
        return None

    runs_dir = root / "kb" / "correlation_runs"
    if not runs_dir.is_dir():
        _RUN_REF_PMID_CACHE[run_ref] = None
        return None

    # Run directories are typically named with a date prefix (e.g.
    # 20260428_stephens_kiss1_wmbv1) while the manifest's `id` field carries
    # the full identifier (corr_run_20260428_stephens_kiss1_wmbv1). Try the
    # direct path first for cheapness, then scan + match by `id` if missing.
    manifest = None
    run_dir = None
    direct = runs_dir / run_ref / "manifest.yaml"
    if direct.exists():
        try:
            manifest = yaml.safe_load(direct.read_text(encoding="utf-8")) or {}
            run_dir = direct.parent
        except yaml.YAMLError:
            manifest = None
            run_dir = None
    if not manifest or manifest.get("id") != run_ref:
        manifest = None
        run_dir = None
        for run_subdir in runs_dir.iterdir():
            if not run_subdir.is_dir():
                continue
            mp = run_subdir / "manifest.yaml"
            if not mp.exists():
                continue
            try:
                m = yaml.safe_load(mp.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError:
                continue
            if m.get("id") == run_ref:
                manifest = m
                run_dir = run_subdir
                break
    if not manifest:
        _RUN_REF_PMID_CACHE[run_ref] = None
        return None
    _RUN_REF_MANIFEST_CACHE[run_ref] = manifest
    _RUN_REF_DIR_CACHE[run_ref] = run_dir

    dataset_ref = manifest.get("dataset_ref")
    if not dataset_ref:
        _RUN_REF_PMID_CACHE[run_ref] = None
        return None

    # kb/datasets/*.yaml are named by source identifier (PMID/GEO), not by
    # the dataset id field. Scan and match by id.
    datasets_dir = root / "kb" / "datasets"
    if not datasets_dir.is_dir():
        _RUN_REF_PMID_CACHE[run_ref] = None
        return None
    for yaml_path in datasets_dir.glob("*.yaml"):
        try:
            ds = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        if ds.get("id") != dataset_ref:
            continue
        pmid = ds.get("source_pmid")
        _RUN_REF_PMID_CACHE[run_ref] = pmid
        _RUN_REF_DATASET_CACHE[run_ref] = ds
        return pmid

    _RUN_REF_PMID_CACHE[run_ref] = None
    return None


def _dataset_for_run_ref(run_ref: str) -> dict | None:
    """Return the BulkDataset descriptor for a given run_ref, or None.

    Triggers `_resolve_run_ref_to_pmid` to populate the cache lazily.
    """
    if run_ref not in _RUN_REF_DATASET_CACHE:
        _resolve_run_ref_to_pmid(run_ref)
    return _RUN_REF_DATASET_CACHE.get(run_ref)


# ── AT run resolver (parallels _resolve_run_ref_to_pmid for CorrelationRun) ───

_AT_RUN_MANIFEST_CACHE: dict[str, dict] = {}
_AT_RUN_DIR_CACHE: dict[str, Path | None] = {}


def _resolve_at_run_ref(run_ref: str) -> tuple[dict | None, Path | None]:
    """Find an AnnotationTransferRun manifest by id under kb/annotation_transfer_runs/.

    Returns (manifest_dict, run_dir). Either may be None if not found.
    Caches the lookup for the lifetime of the module.

    Run directories are typically named with a date prefix (e.g.
    20260408_winterer_olm_mmc_wmbv1) while the manifest's `id` field carries
    the full identifier. Try the direct path first, then scan + match by `id`.
    """
    if run_ref in _AT_RUN_MANIFEST_CACHE or run_ref in _AT_RUN_DIR_CACHE:
        return _AT_RUN_MANIFEST_CACHE.get(run_ref), _AT_RUN_DIR_CACHE.get(run_ref)

    from evidencell.paths import repo_root
    try:
        root = repo_root()
    except RuntimeError:
        _AT_RUN_MANIFEST_CACHE[run_ref] = {}
        _AT_RUN_DIR_CACHE[run_ref] = None
        return None, None

    runs_dir = root / "kb" / "annotation_transfer_runs"
    if not runs_dir.is_dir():
        _AT_RUN_MANIFEST_CACHE[run_ref] = {}
        _AT_RUN_DIR_CACHE[run_ref] = None
        return None, None

    manifest = None
    run_dir = None
    direct = runs_dir / run_ref / "manifest.yaml"
    if direct.exists():
        try:
            manifest = yaml.safe_load(direct.read_text(encoding="utf-8")) or {}
            run_dir = direct.parent
        except yaml.YAMLError:
            manifest = None
            run_dir = None
    if not manifest or manifest.get("id") != run_ref:
        manifest = None
        run_dir = None
        for run_subdir in runs_dir.iterdir():
            if not run_subdir.is_dir():
                continue
            mp = run_subdir / "manifest.yaml"
            if not mp.exists():
                continue
            try:
                m = yaml.safe_load(mp.read_text(encoding="utf-8")) or {}
            except yaml.YAMLError:
                continue
            if m.get("id") == run_ref:
                manifest = m
                run_dir = run_subdir
                break

    if not manifest:
        _AT_RUN_MANIFEST_CACHE[run_ref] = {}
        _AT_RUN_DIR_CACHE[run_ref] = None
        return None, None

    _AT_RUN_MANIFEST_CACHE[run_ref] = manifest
    _AT_RUN_DIR_CACHE[run_ref] = run_dir
    return manifest, run_dir


def _manifest_for_run_ref(run_ref: str) -> dict | None:
    """Return the CorrelationRun manifest for a given run_ref, or None.

    Triggers `_resolve_run_ref_to_pmid` to populate the cache lazily.
    """
    if run_ref not in _RUN_REF_MANIFEST_CACHE:
        _resolve_run_ref_to_pmid(run_ref)
    return _RUN_REF_MANIFEST_CACHE.get(run_ref)


def _run_dir_for_run_ref(run_ref: str) -> Path | None:
    """Return the on-disk directory for a given run_ref, or None."""
    if run_ref not in _RUN_REF_DIR_CACHE:
        _resolve_run_ref_to_pmid(run_ref)
    return _RUN_REF_DIR_CACHE.get(run_ref)


def _top_n_hits_for_contrast(
    run_ref: str,
    contrast_id: str,
    target_accession: str | None = None,
    n: int = 10,
) -> list[dict]:
    """Read the top-N rows from a CorrelationRun's ranked TSV for a contrast.

    Returns a list of dicts (one per cluster row) with keys:
      rank, cluster_id, label, parent_supertype, mfr, top_anat,
      top_anat_n, delta, is_target.

    `is_target` is True when cluster_id == target_accession (used by the
    renderer/synthesis prompt to highlight the row in the report).

    Returns an empty list if the run dir, the ranked output, or the
    contrast can't be located. The contrast's δ column is identified by
    convention: a column matching `delta_{contrast_id_short}` or, failing
    that, the contrast id substring.

    For the existing two runs (Stephens, Knoedler), the per-contrast TSVs
    live at:
      stephens: {run_dir}/delta_rp3v_specific.tsv etc. (ranked by delta)
      knoedler: {run_dir}/ranked_contrasts/{contrast_name}.tsv

    The function tolerates both layouts.
    """
    run_dir = _run_dir_for_run_ref(run_ref)
    if run_dir is None or not run_dir.is_dir():
        return []

    # Resolve contrast → (pool_a, pool_b) via the manifest. The contrast id
    # alone isn't enough to match a TSV filename: contrast ids use `_vs_`
    # while ranked TSVs use `_minus_` or `_specific`.
    manifest = _manifest_for_run_ref(run_ref) or {}
    pool_a = pool_b = ""
    for c in manifest.get("contrasts") or []:
        if c.get("id") == contrast_id:
            pool_a = c.get("pool_a", "")
            pool_b = c.get("pool_b", "")
            break

    def _short(pool_id: str) -> str:
        # pool ids are `{dataset}_{label}` (e.g. stephens_RP3V, knoedler_POA_FR);
        # the filename uses just the label.
        return pool_id.split("_", 1)[1] if "_" in pool_id else pool_id

    a_short = _short(pool_a)
    b_short = _short(pool_b)

    # Generate candidate filename stems in priority order.
    stems: list[str] = []
    if a_short and b_short:
        stems.extend([
            f"delta_{a_short}_minus_{b_short}",
            f"{a_short}_minus_{b_short}",
        ])
    if a_short:
        stems.extend([
            f"delta_{a_short}_specific",
            f"{a_short}_specific",
        ])
    # Last-resort: substring of the raw contrast id.
    short = contrast_id.removeprefix("corr_")
    stems.append(short)

    # Search both run_dir/ and run_dir/ranked_contrasts/ in priority order.
    search_dirs: list[Path] = [run_dir]
    nested = run_dir / "ranked_contrasts"
    if nested.is_dir():
        search_dirs.append(nested)

    tsv_path: Path | None = None
    for stem in stems:
        for d in search_dirs:
            for ci in (False, True):
                p = d / f"{stem}.tsv"
                if not p.exists() and ci:
                    # Case-insensitive fallback
                    matches = [q for q in d.glob("*.tsv") if q.stem.lower() == stem.lower()]
                    if matches:
                        p = matches[0]
                if p.exists():
                    tsv_path = p
                    break
            if tsv_path:
                break
        if tsv_path:
            break
    if tsv_path is None:
        return []

    try:
        rows = []
        with tsv_path.open(encoding="utf-8") as fh:
            header = fh.readline().rstrip("\n").split("\t")
            for line in fh:
                cells = line.rstrip("\n").split("\t")
                if len(cells) != len(header):
                    continue
                rows.append(dict(zip(header, cells)))
    except OSError:
        return []

    # Identify the δ column matching this contrast. The contrast id uses `_vs_`
    # (e.g. corr_VMH_FR_vs_BNST_FR) while column names use `_minus_`
    # (e.g. delta_VMH_FR_minus_BNST_FR). Translate before matching.
    delta_col: str | None = None
    contrast_name = contrast_id.removeprefix("corr_")
    contrast_minus = contrast_name.replace("_vs_", "_minus_")
    for col in header:
        if col.startswith("delta_") and contrast_minus in col:
            delta_col = col
            break
    if delta_col is None:
        # Fallback: first delta_* column (e.g. for runs that stash a single
        # contrast per file with a less canonical naming).
        for col in header:
            if col.startswith("delta_"):
                delta_col = col
                break
    if delta_col is None:
        return []

    # Sort rows by the chosen δ column (descending), then take top N.
    def _f(row: dict, col: str) -> float:
        v = row.get(col, "")
        try:
            return float(v)
        except (TypeError, ValueError):
            return float("-inf")

    rows_sorted = sorted(rows, key=lambda r: _f(r, delta_col), reverse=True)
    out: list[dict] = []
    for rank, r in enumerate(rows_sorted[:n], start=1):
        cid = r.get("cluster_id", "")
        parent = r.get("parent_supertype", "")
        # Target match: direct (cluster→cluster) or via parent (cluster→supertype).
        is_target = bool(
            target_accession is not None
            and (cid == target_accession or parent == target_accession)
        )
        out.append({
            "rank": rank,
            "cluster_id": cid,
            "label": r.get("label", ""),
            "parent_supertype": parent,
            "mfr": r.get("mfr", ""),
            "top_anat": r.get("top_anat", ""),
            "top_anat_n": r.get("top_anat_n", ""),
            "delta": r.get(delta_col, ""),
            "is_target": is_target,
        })
    return out


# ── Methods summary (for paper-style Methods section) ─────────────────────────

def _evidencell_commit() -> str:
    """Return the current evidencell git short SHA (or empty string on failure).

    Used by the renderer to stamp the report with the codebase version that
    produced it — equivalent to a paper's "code availability" footer.
    """
    import subprocess
    from evidencell.paths import repo_root
    try:
        root = repo_root()
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=str(root), timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (RuntimeError, OSError, subprocess.TimeoutExpired):
        pass
    return ""


def extract_methods_summary(
    graph: dict,
    node_id: str,
    graph_file: Path,
) -> dict:
    """Aggregate methods/provenance data across all edges for a classical node.

    Returns a structured dict the synthesis subagent uses to build the Methods
    section narrative. Deterministic — no prose generation here.

    Keys:
      evidence_type_counts: {EVIDENCE_TYPE: count} across all edges
      bulk_correlation_runs: list of run summaries (run_ref, dataset citation,
        statistic, parameters, script provenance, contrasts cited)
      annotation_transfer_runs: list of AT method summaries
      atlas_data_sources: list of {atlas, taxonomy_id, pseudobulk_sha}
      bulk_data_sources: list of {dataset_id, source_pmid, geo_accession,
        technique, n_pools, citation}
      framework_version: evidencell git commit at extract time
      gen_timestamp: ISO 8601 of the extract call
      kb_graph_file: relative path to the KB YAML
    """
    from datetime import datetime, timezone

    edges = [e for e in graph.get("edges", []) if e.get("type_a") == node_id]

    evidence_type_counts: dict[str, int] = {}
    bulk_runs: list[dict] = []
    at_runs: list[dict] = []
    atlas_sources_seen: dict[str, dict] = {}
    bulk_dataset_sources_seen: dict[str, dict] = {}
    seen_run_refs: set[str] = set()
    seen_at_keys: set[tuple] = set()

    for edge in edges:
        for ev in edge.get("evidence", []):
            et = ev.get("evidence_type", "")
            if et:
                evidence_type_counts[et] = evidence_type_counts.get(et, 0) + 1

            run_ref = ev.get("run_ref")
            if run_ref and run_ref not in seen_run_refs:
                seen_run_refs.add(run_ref)
                manifest = _manifest_for_run_ref(run_ref) or {}
                dataset = _dataset_for_run_ref(run_ref) or {}
                method = manifest.get("method") or {}
                script = manifest.get("script") or {}
                atlas = manifest.get("atlas") or {}

                bulk_runs.append({
                    "run_ref": run_ref,
                    "dataset_ref": manifest.get("dataset_ref", ""),
                    "statistic_kind": method.get("statistic_kind", ""),
                    "parameters": method.get("parameters", ""),
                    "atlas_taxonomy_id": atlas.get("taxonomy_id", ""),
                    "atlas_pseudobulk_sha": atlas.get("sha256", ""),
                    "script_relpath": script.get("relpath", ""),
                    "script_python_version": script.get("python_version", ""),
                    "script_packages": script.get("packages", []),
                    "script_git_repo_url": script.get("git_repo_url", ""),
                    "script_git_commit": script.get("git_commit", ""),
                    "code_version": manifest.get("code_version", ""),
                    "n_contrasts": len(manifest.get("contrasts") or []),
                    "caveats": manifest.get("caveats", ""),
                })

                # Bulk data source (one per dataset across runs)
                ds_id = dataset.get("id", "")
                if ds_id and ds_id not in bulk_dataset_sources_seen:
                    bulk_dataset_sources_seen[ds_id] = {
                        "dataset_id": ds_id,
                        "source_pmid": dataset.get("source_pmid", ""),
                        "geo_accession": dataset.get("geo_accession", ""),
                        "technique": dataset.get("technique", ""),
                        "n_pools": len(dataset.get("pools") or []),
                        "n_data_files": len(dataset.get("data_files") or []),
                        "authors": dataset.get("authors") or [],
                        "year": dataset.get("year"),
                        "title": dataset.get("title", ""),
                    }

                # Atlas data source (deduped by sha)
                atlas_key = atlas.get("sha256") or atlas.get("taxonomy_id", "")
                if atlas_key and atlas_key not in atlas_sources_seen:
                    atlas_sources_seen[atlas_key] = {
                        "atlas": "WMBv1",
                        "taxonomy_id": atlas.get("taxonomy_id", ""),
                        "pseudobulk_source": atlas.get("pseudobulk_source", ""),
                        "pseudobulk_sha256": atlas.get("sha256", ""),
                    }

            if et == "ANNOTATION_TRANSFER":
                # If the evidence carries run_ref, the AnnotationTransferRun
                # manifest is the canonical provenance source. Otherwise fall
                # back to the inline fields (back-compat with evidence
                # ingested before the run schema landed).
                run_ref_at = ev.get("run_ref", "")
                if run_ref_at:
                    if run_ref_at not in seen_at_keys:
                        seen_at_keys.add(run_ref_at)
                        m, run_dir = _resolve_at_run_ref(run_ref_at)
                        if m:
                            atlas_at = m.get("atlas") or {}
                            script_at = m.get("script") or {}
                            output_at = m.get("output") or {}
                            figure_at = m.get("figure") or {}
                            at_runs.append({
                                "run_ref": run_ref_at,
                                "method": m.get("method", ""),
                                "tool_version": m.get("tool_version", ""),
                                "code_reference": m.get("code_reference", ""),
                                "source_dataset_accession": m.get("source_dataset_accession", ""),
                                "source_cluster_label": m.get("source_cluster_label", ""),
                                "source_species": m.get("source_species", ""),
                                "target_atlas": m.get("target_atlas", ""),
                                "target_taxonomy_id": m.get("target_taxonomy_id", ""),
                                "target_species": m.get("target_species", ""),
                                "bootstrap_threshold": m.get("bootstrap_threshold"),
                                "n_cells_total": m.get("n_cells_total"),
                                "n_cells_after_filter": m.get("n_cells_after_filter"),
                                "atlas_pseudobulk_sha": atlas_at.get("sha256", ""),
                                "script_relpath": script_at.get("relpath", ""),
                                "script_git_repo_url": script_at.get("git_repo_url", ""),
                                "script_git_commit": script_at.get("git_commit", ""),
                                "code_version": m.get("code_version", ""),
                                "output_relpath": output_at.get("relpath", ""),
                                "figure_relpath": figure_at.get("relpath", ""),
                                "run_dir_name": run_dir.name if run_dir else "",
                                "caveats": m.get("caveats", ""),
                            })
                else:
                    # Back-compat path: evidence has inline fields, no run_ref.
                    key = (
                        ev.get("source_dataset_accession", ""),
                        ev.get("method", ""),
                        ev.get("target_atlas", ""),
                    )
                    if key not in seen_at_keys:
                        seen_at_keys.add(key)
                        at_runs.append({
                            "method": ev.get("method", ""),
                            "tool_version": ev.get("tool_version", ""),
                            "code_reference": ev.get("code_reference", ""),
                            "source_dataset_accession": ev.get("source_dataset_accession", ""),
                            "source_species": ev.get("source_species", ""),
                            "target_atlas": ev.get("target_atlas", ""),
                            "target_species": ev.get("target_species", ""),
                            "best_f1_score": ev.get("best_f1_score"),
                            "best_mapping_level": ev.get("best_mapping_level", ""),
                            "bootstrap_threshold": ev.get("bootstrap_threshold"),
                            "n_cells_total": ev.get("n_cells_total"),
                            "n_cells_after_filter": ev.get("n_cells_after_filter"),
                        })

    # Surface CL mapping at top of methods summary so the synthesis subagent
    # can reuse it in the Discussion best-candidate block.
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    classical = nodes_by_id.get(node_id, {})
    cl = classical.get("cl_mapping") or {}
    cl_term = cl.get("cl_term") or {}
    cl_id = cl_term.get("id", "") if isinstance(cl_term, dict) else ""
    cl_mapping_summary = {
        "cl_term_id": cl_id,
        "cl_term_label": cl_term.get("label", "") if isinstance(cl_term, dict) else "",
        "cl_term_name_in_source": cl_term.get("name_in_source", "") if isinstance(cl_term, dict) else "",
        "mapping_type": cl.get("mapping_type", ""),
        "mapping_notes": cl.get("mapping_notes", ""),
        "ols_url": (
            f"https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id={cl_id}"
            if cl_id.startswith("CL:") else ""
        ),
    }

    # Render kb_graph_file as repo-relative when possible, so the report's
    # reproducibility footer carries a portable path (not someone's $HOME).
    try:
        from evidencell.paths import repo_root
        rel_graph = str(Path(graph_file).resolve().relative_to(repo_root().resolve()))
    except (ValueError, RuntimeError):
        rel_graph = str(graph_file)

    return {
        "evidence_type_counts": evidence_type_counts,
        "cl_mapping": cl_mapping_summary,
        "bulk_correlation_runs": bulk_runs,
        "annotation_transfer_runs": at_runs,
        "atlas_data_sources": list(atlas_sources_seen.values()),
        "bulk_data_sources": list(bulk_dataset_sources_seen.values()),
        "framework_version": _evidencell_commit(),
        "gen_timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "kb_graph_file": rel_graph,
    }


# ── Reference index builder ───────────────────────────────────────────────────

def build_reference_index(
    graph: dict,
    refs: dict,
    node_id: str | None = None,
) -> dict[str, RefEntry]:
    """
    Scan all evidence items for a node's edges (and node property sources) in
    document order. Assign [1]..[N] to literature/AT references, [A]..[Z] to
    AtlasQueryEvidence query_urls. Returns lookup keyed by normalized ref string.

    Only identifiers that actually appear in the graph are included — no invention.
    """
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    all_edges = graph.get("edges", [])
    edges = [e for e in all_edges if e.get("type_a") == node_id] if node_id else all_edges

    lit_n = [0]    # running counter for [1]..[N]
    qry_n = [0]    # running counter for [A]..[Z]
    index: dict[str, RefEntry] = {}

    def _add_lit(ref_str: str, used_for: str = "") -> str:
        ref_type, bare = _ref_identifier(ref_str)
        key = f"{ref_type}:{bare}"
        if key in index:
            return index[key].label
        if ref_type == "pmid":
            entry = _find_corpus_by_pmid(bare, refs)
        else:
            entry = _find_corpus_by_doi(bare, refs)
        lit_n[0] += 1
        label = f"[{lit_n[0]}]"
        if entry:
            citation_line = _format_citation_line(entry)
            pmid = entry.get("pmid")
            doi = entry.get("doi")
            corpus_id = entry.get("corpus_id")
        else:
            citation_line = ref_str
            pmid = bare if ref_type == "pmid" else None
            doi = bare if ref_type == "doi" else None
            corpus_id = None
        index[key] = RefEntry(
            label=label, pmid=pmid, doi=doi, corpus_id=corpus_id,
            query_url=None, citation_line=citation_line, used_for=used_for,
        )
        return label

    def _add_qry(query_url: str, atlas: str = "", filters: str = "") -> str:
        if query_url in index:
            return index[query_url].label
        qry_n[0] += 1
        label = f"[{chr(ord('A') + qry_n[0] - 1)}]"
        cite = f"{atlas}" if atlas else "Atlas query"
        index[query_url] = RefEntry(
            label=label, pmid=None, doi=None, corpus_id=None,
            query_url=query_url, citation_line=cite, used_for=filters,
        )
        return label

    # Scan classical node property sources (appear before edge evidence in document)
    if node_id and node_id in nodes_by_id:
        node = nodes_by_id[node_id]
        for loc in node.get("anatomical_location", []):
            for src in loc.get("sources", []):
                if src.get("ref"):
                    _add_lit(src["ref"], "soma location")
        nt = node.get("nt_type") or {}
        for src in nt.get("sources", []):
            if src.get("ref"):
                _add_lit(src["ref"], "neurotransmitter type")
        for marker in node.get("defining_markers", []):
            sym = marker.get("symbol", "")
            for src in marker.get("sources", []):
                if src.get("ref"):
                    _add_lit(src["ref"], f"{sym} marker")
        for marker in node.get("neuropeptides", []):
            sym = marker.get("symbol", "")
            for src in marker.get("sources", []):
                if src.get("ref"):
                    _add_lit(src["ref"], f"{sym} neuropeptide")

    # Scan edge evidence items
    for edge in edges:
        for ev in edge.get("evidence", []):
            et = ev.get("evidence_type", "")
            if et == "LITERATURE":
                ref = ev.get("reference", "")
                if ref:
                    _add_lit(ref, (ev.get("explanation") or "")[:80].strip())
            elif et == "ATLAS_QUERY":
                qurl = ev.get("query_url", "")
                if qurl:
                    _add_qry(
                        qurl,
                        atlas=ev.get("atlas", ""),
                        filters=ev.get("filters_applied", ""),
                    )
            else:
                # Generic path: any evidence type carrying run_ref resolves
                # to its source publication via manifest → dataset → source_pmid.
                # If references.json doesn't have an entry for the resolved
                # PMID, fall back to authors/year/title from the BulkDataset
                # descriptor itself so the citation line renders properly.
                run_ref = ev.get("run_ref", "")
                if run_ref:
                    pmid = _resolve_run_ref_to_pmid(run_ref)
                    if pmid:
                        label = _add_lit(pmid, (ev.get("explanation") or "")[:80].strip())
                        ref_type, bare = _ref_identifier(pmid)
                        key = f"{ref_type}:{bare}"
                        existing = index.get(key)
                        # If _add_lit fell back to the bare PMID (no
                        # references.json hit), patch the citation_line from
                        # the dataset descriptor.
                        if existing and existing.citation_line == pmid:
                            ds = _dataset_for_run_ref(run_ref)
                            if ds:
                                synthetic = {
                                    "authors": ds.get("authors") or [],
                                    "year": ds.get("year"),
                                    "pmid": bare,
                                    "doi": None,
                                }
                                citation_line = _format_citation_line(synthetic)
                                if citation_line and citation_line != pmid:
                                    index[key] = RefEntry(
                                        label=label, pmid=existing.pmid,
                                        doi=existing.doi, corpus_id=existing.corpus_id,
                                        query_url=existing.query_url,
                                        citation_line=citation_line,
                                        used_for=existing.used_for,
                                    )

    return index


# ── Structural helpers ────────────────────────────────────────────────────────

def _location_note(graph: dict) -> str | None:
    """
    Return the MERFISH soma-only location note if any terminal node has anatomical_location.
    """
    for node in graph.get("nodes", []):
        if node.get("is_terminal") and node.get("anatomical_location"):
            return MERFISH_LOCATION_NOTE
    return None


def _cl_introduction(cn: dict) -> list[str]:
    """
    Render the Introduction paragraph(s) describing this node's relationship
    to the Cell Ontology. Pulls from cl_term / cl_id / cl_mapping_type /
    cl_mapping_notes / proposed_cl_term on the classical_node facts dict.
    Returns an empty list if no CL information is present.
    """
    cl_term = cn.get("cl_term") or ""
    cl_id = cn.get("cl_id") or ""
    mapping_type = cn.get("cl_mapping_type") or ""
    notes = cn.get("cl_mapping_notes") or ""
    proposed = cn.get("proposed_cl_term") or {}
    name = cn.get("name") or "this cell type"

    if not cl_term and not proposed and not mapping_type:
        return []

    out: list[str] = []
    # cl_term is already formatted "label (id)" by _ot(); cl_id is exposed
    # separately for downstream consumers (e.g. NTR drafting).
    parent_str = f"**{cl_term}**" if cl_term else "—"

    if mapping_type == "EXACT":
        out.append(
            f"{name} is mapped to {parent_str} as an **exact match** in the "
            f"Cell Ontology (skos:exactMatch); the existing CL term covers this type."
        )
    elif mapping_type in ("BROAD", "RELATED"):
        out.append(
            f"{name} is a **{mapping_type.lower()} match** to {parent_str} in the "
            f"Cell Ontology — i.e. {parent_str} is the closest existing CL term "
            f"({'an ancestor' if mapping_type == 'BROAD' else 'a related concept'}) "
            f"but does not fully cover this type. A new child term is a candidate "
            f"for submission to CL."
        )
    elif cl_term or cl_id:
        out.append(
            f"{name} has a CL mapping to {parent_str} (mapping_type unspecified)."
        )
    else:
        out.append(
            f"No existing Cell Ontology term currently covers {name}. "
            f"This type is a candidate for a new CL term."
        )

    if notes:
        out.append("")
        out.append(f"*Mapping notes:* {notes}")

    if proposed:
        plabel = proposed.get("label") or ""
        pdef = (proposed.get("definition") or "").strip()
        pstatus = proposed.get("status") or "DRAFT"
        if plabel or pdef:
            out.append("")
            head = f"**Proposed CL term:** *{plabel}* ({pstatus})" if plabel else f"**Proposed CL term** ({pstatus})"
            out.append(head)
            if pdef:
                out.append("")
                out.append(f"> {pdef}")

    return out


def _candidate_verdict(edge: dict, nodes_by_id: dict) -> str:
    """
    Derive verdict from confidence + property_comparisons.
    HIGH/MODERATE → 'Best candidate'
    LOW → 'Speculative'
    UNCERTAIN with DISCORDANT marker → 'Eliminated ({marker})'
    UNCERTAIN otherwise → 'Uncertain'
    """
    conf = edge.get("confidence", "")
    if conf in ("HIGH", "MODERATE"):
        return "Best candidate"
    if conf == "LOW":
        return "Speculative"
    if conf in ("UNCERTAIN", "REFUTED"):
        for pc in edge.get("property_comparisons", []):
            if pc.get("alignment") == "DISCORDANT" and "marker" in pc.get("property", ""):
                prop = pc["property"].replace("marker_", "")
                return f"Eliminated ({prop})"
        return "Eliminated" if conf == "UNCERTAIN" else "Refuted"
    return conf


def _best_edge(edges: list[dict], node_id: str) -> dict | None:
    """Return highest-confidence edge where type_a == node_id."""
    candidates = [e for e in edges if e.get("type_a") == node_id]
    if not candidates:
        return None
    return min(candidates, key=lambda e: CONF_ORDER.get(e.get("confidence", "REFUTED"), 99))


def _group_experiments(edges: list[dict]) -> list[dict]:
    """
    Collect proposed_experiments[] across edges.
    Group by leading method keyword. Deduplicate near-identical strings.
    Returns list of {group: str, experiments: [str], edge_ids: [str]}.
    """
    METHOD_KEYS = [
        ("MapMyCells", "MapMyCells / annotation transfer"),
        ("MapMyCell", "MapMyCells / annotation transfer"),
        ("patch-seq", "Patch-seq"),
        ("Patch-seq", "Patch-seq"),
        ("MERFISH", "MERFISH / spatial transcriptomics"),
        ("scRNA-seq", "scRNA-seq / single-cell"),
        ("snRNA-seq", "scRNA-seq / single-cell"),
    ]
    groups: dict[str, dict] = {}

    for edge in edges:
        for exp in edge.get("proposed_experiments", []):
            exp_str = exp.strip() if isinstance(exp, str) else str(exp)
            group_name = "Other"
            for keyword, name in METHOD_KEYS:
                if keyword in exp_str:
                    group_name = name
                    break
            if group_name not in groups:
                groups[group_name] = {"group": group_name, "experiments": [], "edge_ids": []}
            # Deduplicate: skip if a nearly identical string already present
            already = any(
                abs(len(x) - len(exp_str)) < 20 and x[:40] == exp_str[:40]
                for x in groups[group_name]["experiments"]
            )
            if not already:
                groups[group_name]["experiments"].append(exp_str)
            eid = edge.get("id", "")
            if eid and eid not in groups[group_name]["edge_ids"]:
                groups[group_name]["edge_ids"].append(eid)

    return list(groups.values())


def _open_taxonomy_db(taxonomy_id: str) -> "object | None":
    """Open the SQLite TaxonomyDB for a taxonomy_id, or None if unavailable.

    Imported lazily to keep `render` usable in environments where the taxonomy
    DB hasn't been built yet (e.g. CI fixtures, tests). Failures degrade
    gracefully — render still emits a valid report, just without atlas-side
    enrichment (n_cells, supertype).
    """
    if not taxonomy_id:
        return None
    try:
        from evidencell.paths import taxonomy_dir
        from evidencell.taxonomy_db import TaxonomyDB
    except Exception:
        return None
    db_path = taxonomy_dir(taxonomy_id) / f"{taxonomy_id}.db"
    if not db_path.exists():
        return None
    return TaxonomyDB(db_path)


def _node_b_info(edge: dict, nodes_by_id: dict, db_cache: dict | None = None) -> dict:
    """Extract display info for the atlas (type_b) node of an edge.

    `db_cache` is a per-render mutable dict keyed by taxonomy_id; if provided,
    looks up atlas-only properties (n_cells, parent supertype) from the
    TaxonomyDB by accession. Stubs in mapping-graph YAML carry minimal data
    per the KB convention (taxonomy YAML is canonical for atlas properties),
    so this lookup is what surfaces the per-node 10x cell count and the
    nearest-supertype label in reports.
    """
    b_id = edge.get("type_b", "")
    b_node = nodes_by_id.get(b_id, {})
    accession = b_node.get("cell_set_accession", "")
    n_cells = b_node.get("n_cells")
    supertype = ""

    if db_cache is not None and accession:
        tax_id = b_node.get("taxonomy_id") or ""
        if tax_id and tax_id not in db_cache:
            db_cache[tax_id] = _open_taxonomy_db(tax_id)
        db = db_cache.get(tax_id)
        if db is not None:
            try:
                tax_node = db.get_node_by_accession(accession)
                if tax_node:
                    if n_cells is None:
                        n_cells = tax_node.get("n_cells")
                    parents = db.get_parent_hierarchy(accession)
                    supt_entry = next(
                        (p for p in parents
                         if (p.get("level") or "").upper() == "SUPERTYPE"),
                        None,
                    )
                    if supt_entry:
                        supertype = supt_entry.get("name", "")
            except Exception:
                # DB lookup is best-effort — never block report rendering
                pass

    return {
        "id": b_id,
        "name": b_node.get("name", b_id),
        "accession": accession,
        "supertype": supertype,
        "n_cells": n_cells,
        "taxonomy_level": b_node.get("taxonomy_level", ""),
    }


# ── Quotes extraction ─────────────────────────────────────────────────────────

def _collect_quotes(graph: dict, refs: dict, node_id: str) -> dict:
    """
    Collect all quotes referenced by quote_key fields in the node and its edges.
    Returns {quote_key: {text, section, claims}} — verbatim from references.json.
    Raises KeyError if a quote_key is present in YAML but absent from references.json.
    """
    quotes: dict = {}
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    node = nodes_by_id.get(node_id, {})

    def _add_quote(qk: str) -> None:
        if not qk or qk in quotes:
            return
        # Find in references.json
        corpus_id = qk.split("_")[0]
        corpus = refs.get(corpus_id, {})
        quote_obj = corpus.get("quotes", {}).get(qk)
        if quote_obj is None:
            raise KeyError(
                f"quote_key '{qk}' not found in references.json "
                f"(corpus_id='{corpus_id}'). Fix YAML or update references.json."
            )
        quotes[qk] = {
            "text": quote_obj["text"],
            "section": quote_obj.get("section", ""),
            "claims": quote_obj.get("claims", []),
        }

    # Node property sources
    for loc in node.get("anatomical_location", []):
        for src in loc.get("sources", []):
            _add_quote(src.get("quote_key", ""))
    for src in (node.get("nt_type") or {}).get("sources", []):
        _add_quote(src.get("quote_key", ""))
    for marker in node.get("defining_markers", []):
        for src in marker.get("sources", []):
            _add_quote(src.get("quote_key", ""))
    for marker in node.get("neuropeptides", []):
        for src in marker.get("sources", []):
            _add_quote(src.get("quote_key", ""))

    # Edge evidence
    for edge in graph.get("edges", []):
        if edge.get("type_a") != node_id:
            continue
        for ev in edge.get("evidence", []):
            _add_quote(ev.get("quote_key", ""))

    return quotes


# ── Facts extractor (primary output) ─────────────────────────────────────────

def extract_node_facts(
    graph: dict,
    refs: dict,
    node_id: str,
    graph_file: Path,
) -> dict:
    """
    Build report_facts dict for one classical node.
    This is the structured intermediate representation passed to the synthesis subagent.
    All fields trace directly to YAML source — no inference, no LLM.
    """
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    node = nodes_by_id.get(node_id)
    if node is None:
        raise ValueError(f"Node '{node_id}' not found in graph")
    if node.get("is_terminal"):
        raise ValueError(f"Node '{node_id}' is a terminal (atlas) node; reports are for classical nodes")

    all_edges = graph.get("edges", [])
    node_edges = sorted(
        [e for e in all_edges if e.get("type_a") == node_id],
        key=lambda e: CONF_ORDER.get(e.get("confidence", "UNCERTAIN"), 99),
    )

    # Detect draft vs canonical
    status = "draft" if "draft" in str(graph_file) else "canonical"

    # Check for MERFISH location data
    has_merfish = any(
        n.get("is_terminal") and n.get("anatomical_location")
        for n in graph.get("nodes", [])
    )

    # Build reference index
    ref_index = build_reference_index(graph, refs, node_id)
    # key → label string lookup
    ref_labels: dict[str, str] = {k: v.label for k, v in ref_index.items()}

    def _ref_label(ref_str: str) -> str:
        ref_type, bare = _ref_identifier(ref_str)
        return ref_labels.get(f"{ref_type}:{bare}", f"[?{ref_str}]")

    def _query_label(qurl: str) -> str:
        return ref_labels.get(qurl, f"[?{qurl[:20]}]")

    # Classical node properties
    cl = node.get("cl_mapping") or {}
    cl_term_str = _ot(cl.get("cl_term")) if cl else ""

    nt_obj = node.get("nt_type") or {}
    nt_sources_labels = [_ref_label(s["ref"]) for s in nt_obj.get("sources", []) if s.get("ref")]

    def _marker_refs(marker: dict) -> list[str]:
        return [_ref_label(s["ref"]) for s in marker.get("sources", []) if s.get("ref")]

    soma_locations = []
    for loc in node.get("anatomical_location", []):
        soma_locations.append({
            "id": loc.get("id", ""),
            "label": loc.get("label", ""),
            "name_in_source": loc.get("name_in_source", ""),
        })

    location_refs = [
        _ref_label(s["ref"])
        for loc in node.get("anatomical_location", [])
        for s in loc.get("sources", [])
        if s.get("ref")
    ]

    # Edges. db_cache holds opened TaxonomyDBs keyed by taxonomy_id so we
    # don't reconnect for every edge; lookups fill n_cells / supertype on
    # b_info from the canonical taxonomy reference DB.
    edge_facts = []
    db_cache: dict = {}
    for edge in node_edges:
        b_info = _node_b_info(edge, nodes_by_id, db_cache=db_cache)
        verdict = _candidate_verdict(edge, nodes_by_id)

        # Evidence items — generic extraction.
        # All EvidenceItem subclasses share evidence_type, supports, explanation
        # (the abstract parent's required fields). Subclass-specific fields
        # (snippet, run_ref, statistics, best_f1_score, ...) are preserved
        # verbatim under `fields:` so the synthesis subagent can use any of
        # them without per-type code paths in the renderer.
        ev_items = []
        _BASE_KEYS = {"evidence_type", "supports", "explanation"}
        for ev in edge.get("evidence", []):
            et = ev.get("evidence_type", "")
            item: dict = {
                "evidence_type": et,
                "supports": ev.get("supports", ""),
                "explanation": (ev.get("explanation") or "").strip(),
            }
            # Resolve a [n] ref label by the appropriate lookup for each
            # evidence type. LITERATURE has a direct `reference`; ATLAS_QUERY
            # uses `query_url` (gets a letter label); other types may carry a
            # `run_ref` that resolves through the dataset chain to a PMID.
            ref_label = ""
            if et == "LITERATURE":
                ref = ev.get("reference", "")
                if ref:
                    ref_label = _ref_label(ref)
            elif et == "ATLAS_QUERY":
                qurl = ev.get("query_url", "")
                if qurl:
                    ref_label = _query_label(qurl)
            elif ev.get("run_ref"):
                pmid = _resolve_run_ref_to_pmid(ev["run_ref"])
                if pmid:
                    ref_label = _ref_label(pmid)
            item["ref_label"] = ref_label

            # Preserve every other populated field verbatim under `fields:`.
            extras = {
                k: v for k, v in ev.items()
                if k not in _BASE_KEYS and v not in (None, "", [], {})
            }
            # For evidence items pointing at a CorrelationRun, attach the top-N
            # ranked hits for the named contrast. This lets the synthesis
            # subagent emit a "show your work" table alongside the
            # attributed-blockquote evidence narrative — addresses the
            # 2026-04-29_bulk-correlation-show-top-hits.md feedback.
            # AnnotationTransferEvidence with run_ref: pull the run-level
            # figure (e.g. F1 heatmap) from the manifest. The figure is
            # run-level (one PNG per AT run, covering all candidates) so
            # it embeds once in the report — the synthesis subagent decides
            # where (typically Results overview).
            if et == "ANNOTATION_TRANSFER" and ev.get("run_ref"):
                at_manifest, at_dir = _resolve_at_run_ref(ev["run_ref"])
                if at_manifest and at_dir:
                    fig = at_manifest.get("figure") or {}
                    fig_relpath = fig.get("relpath", "")
                    if fig_relpath:
                        # Path the report references — relative to the report
                        # dir (reports/{region}/), pointing into the run dir.
                        # We use a path of the form:
                        #   ../../kb/annotation_transfer_runs/{run_dir.name}/{fig_relpath}
                        # Two ".." steps because reports/{region}/file.md sits two
                        # levels below the repo root.
                        extras["figure_relpath"] = (
                            f"../../kb/annotation_transfer_runs/{at_dir.name}/{fig_relpath}"
                        )
                        extras["figure_caption"] = (
                            f"Annotation transfer F1 heatmap "
                            f"({at_manifest.get('source_dataset_accession', 'source')} "
                            f"→ {at_manifest.get('target_atlas', 'target')})"
                        )

            run_ref = ev.get("run_ref")
            contrast_ref = ev.get("contrast_ref")
            if run_ref and contrast_ref:
                hits = _top_n_hits_for_contrast(
                    run_ref, contrast_ref,
                    target_accession=ev.get("target_accession"),
                    n=10,
                )
                if hits:
                    extras["top_n_hits"] = hits
                    # Render the matching δ ranked-bar figure alongside the
                    # report. Filename is content-hashed; the report's
                    # reference becomes a visibly broken link if the
                    # underlying data changes (sync mechanism — see
                    # planning/paper_style_reports_review_addendum.md §4).
                    try:
                        from evidencell.figures import render_top_n_hits_figure
                        from evidencell.paths import reports_dir_for_region
                        # Region is the parent directory of the graph file
                        # (kb/draft/{region}/file.yaml or kb/mappings/{region}/file.yaml).
                        region = graph_file.parent.name if graph_file else ""
                        if region:
                            figures_dir = reports_dir_for_region(region) / "figures"
                            short_contrast = contrast_ref.removeprefix("corr_")
                            caption = (
                                f"Top {len(hits)} clusters by δ for {short_contrast} "
                                f"({ev.get('target_accession', node_id)})"
                            )
                            png_path, _ = render_top_n_hits_figure(
                                hits, figures_dir, node_id, contrast_ref,
                                caption=caption,
                                framework_version=_evidencell_commit(),
                            )
                            # Path relative to the report file (which lives
                            # in reports/{region}/).
                            extras["figure_relpath"] = f"figures/{png_path.name}"
                            extras["figure_caption"] = caption
                    except (ImportError, ValueError, OSError) as exc:
                        # Figure rendering is best-effort — never fail facts
                        # extraction over a plotting issue.
                        print(f"WARNING: figure rendering failed for {run_ref} / {contrast_ref}: {exc}", file=sys.stderr)
            if extras:
                item["fields"] = extras
            ev_items.append(item)

        edge_facts.append({
            "id": edge["id"],
            "node_b_id": b_info["id"],
            "node_b_name": b_info["name"],
            "node_b_accession": b_info["accession"],
            "supertype": b_info["supertype"],
            "n_cells": b_info["n_cells"],
            "taxonomy_level": b_info["taxonomy_level"],
            "confidence": edge.get("confidence", ""),
            "relationship": edge.get("relationship", ""),
            "verdict": verdict,
            "evidence_items": ev_items,
            "property_comparisons": edge.get("property_comparisons", []),
            "caveats": edge.get("caveats", []),
            "unresolved_questions": edge.get("unresolved_questions", []),
            "proposed_experiments": edge.get("proposed_experiments", []),
            "notes": edge.get("notes", ""),
        })

    # Quotes: collect all quote_keys referenced in node + edges
    # (may raise KeyError if quote_key absent from references.json)
    try:
        quotes = _collect_quotes(graph, refs, node_id)
    except KeyError as exc:
        print(f"WARNING: {exc}", file=sys.stderr)
        quotes = {}

    # Reference index as serialisable dict
    ref_index_serial = {
        k: {
            "label": v.label,
            "pmid": v.pmid,
            "doi": v.doi,
            "corpus_id": v.corpus_id,
            "query_url": v.query_url,
            "citation_line": v.citation_line,
            "used_for": v.used_for,
        }
        for k, v in ref_index.items()
    }

    methods_summary = extract_methods_summary(graph, node_id, graph_file)

    return {
        "graph_meta": {
            "name": graph.get("name", ""),
            "target_atlas": graph.get("target_atlas", ""),
            "brain_region": _ot(graph.get("brain_region")),
            "species": _ot(graph.get("species")),
            "status": status,
            "creation_date": str(graph.get("creation_date", "")),
            "graph_file": str(graph_file),
            "has_merfish_location": has_merfish,
        },
        "methods_summary": methods_summary,
        "reference_index": ref_index_serial,
        "classical_nodes": [{
            "id": node_id,
            "name": node.get("name", ""),
            "definition_basis": node.get("definition_basis", ""),
            "cl_term": cl_term_str,
            "cl_id": (cl.get("cl_term") or {}).get("id", "") if cl else "",
            "cl_mapping_type": cl.get("mapping_type", "") if cl else "",
            "cl_mapping_notes": (cl.get("mapping_notes") or "").strip() if cl else "",
            "proposed_cl_term": node.get("proposed_cl_term") or None,
            "nt": nt_obj.get("name_in_source", ""),
            "nt_refs": nt_sources_labels,
            "defining_markers": [
                {
                    "symbol": m.get("symbol", ""),
                    "refs": _marker_refs(m),
                }
                for m in node.get("defining_markers", [])
            ],
            "negative_markers": [m.get("symbol", "") for m in node.get("negative_markers", [])],
            "neuropeptides": [
                {
                    "symbol": m.get("symbol", ""),
                    "refs": _marker_refs(m),
                }
                for m in node.get("neuropeptides", [])
            ],
            "soma_locations": soma_locations,
            "location_refs": location_refs,
            "morphology_notes": node.get("morphology_notes", ""),
            "electrophysiology_class": node.get("electrophysiology_class", ""),
            "notes": node.get("notes", ""),
        }],
        "edges": edge_facts,
        "quotes": quotes,
    }


# ── Programmatic Markdown renderers ───────────────────────────────────────────

def render_summary(
    graph: dict,
    refs: dict,
    node_id: str,
    out_path: Path,
    graph_file: Path,
) -> None:
    """
    Write Tier 1 summary report Markdown for one classical node.
    Programmatic mode — constructs prose from YAML fields directly.
    For higher-quality synthesis, use the gen-report orchestrator workflow.
    """
    facts = extract_node_facts(graph, refs, node_id, graph_file)
    gm = facts["graph_meta"]
    cn = facts["classical_nodes"][0]
    edges = facts["edges"]
    ref_index = facts["reference_index"]

    lines: list[str] = []

    # 1. Header
    lines.append(f"# {cn['name']} — {gm['target_atlas']} Mapping Report")
    status_tag = f"*{gm['status'].capitalize()} · {gm['creation_date']} · Source: `{gm['graph_file']}`*"
    lines.append(status_tag)
    if gm["status"] == "draft":
        lines.append("")
        lines.append(DRAFT_BANNER)
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. Location note (conditional)
    loc_note = _location_note(graph)
    if loc_note:
        lines.append(loc_note)
        lines.append("")
        lines.append("---")
        lines.append("")

    # 3. Classical type table
    lines.append("## Classical type")
    lines.append("")
    markers_str = ", ".join(
        f"{m['symbol']}+"
        for m in cn["defining_markers"]
    )
    neg_str = ", ".join(f"{s}−" for s in cn["negative_markers"])
    np_str = ", ".join(m["symbol"] for m in cn["neuropeptides"])
    def _loc_label(loc: dict) -> str:
        name = loc.get("name_in_source") or loc.get("label") or loc.get("id", "")
        loc_id = loc.get("id", "")
        return f"{name} [{loc_id}]" if loc_id else name

    loc_str = "; ".join(_loc_label(loc) for loc in cn["soma_locations"])
    loc_refs = " ".join(cn["location_refs"])
    nt_refs = " ".join(cn["nt_refs"])
    # Deduplicate refs
    all_marker_refs = list(dict.fromkeys(
        ref for m in cn["defining_markers"] for ref in m["refs"]
    ))
    cl_str = cn["cl_term"] if cn["cl_term"] else "—"

    lines.append("| Property | Value | References |")
    lines.append("|---|---|---|")
    lines.append(f"| CL term | {cl_str} | |")
    lines.append(f"| Soma location | {loc_str} | {loc_refs} |")
    lines.append(f"| NT | {cn['nt']} | {nt_refs} |")
    lines.append(f"| Markers | {markers_str} | {' '.join(all_marker_refs)} |")
    if neg_str:
        lines.append(f"| Negative | {neg_str} | |")
    if np_str:
        np_refs = " ".join(dict.fromkeys(
            ref for m in cn["neuropeptides"] for ref in m["refs"]
        ))
        lines.append(f"| Neuropeptides | {np_str} | {np_refs} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 4. Cell Ontology mapping (closes Introduction; placed AFTER classical
    #    type description so the reader has the biology in mind first).
    intro_lines = _cl_introduction(cn)
    if intro_lines:
        lines.append("## Cell Ontology mapping")
        lines.append("")
        lines.extend(intro_lines)
        lines.append("")
        lines.append("---")
        lines.append("")

    # 5. Mapping candidates table
    lines.append("## Mapping candidates")
    lines.append("")
    lines.append("| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |")
    lines.append("|---|---|---|---|---|---|")
    rank = 0
    for edge in edges:
        conf = edge["confidence"]
        if conf in ("HIGH", "MODERATE", "LOW"):
            rank += 1
            rank_str = str(rank)
        else:
            rank_str = "—"
        name = edge["node_b_name"]
        acc = edge.get("node_b_accession", "")
        cluster_label = f"{name} [{acc}]" if acc else name
        n_cells = f"{edge['n_cells']:,}" if edge["n_cells"] is not None else "—"
        badge = _conf_badge(conf)
        verdict = edge["verdict"]
        lines.append(f"| {rank_str} | {cluster_label} | {edge['supertype']} | {n_cells} | {badge} | {verdict} |")
    lines.append("")

    if edges:
        rel = edges[0]["relationship"]
        lines.append(f"All edges: `{rel}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 5. Candidate paragraphs
    uncertain_edges = [e for e in edges if e["confidence"] in ("UNCERTAIN", "REFUTED")]
    confident_edges = [e for e in edges if e["confidence"] not in ("UNCERTAIN", "REFUTED")]

    for edge in confident_edges:
        conf = edge["confidence"]
        name = edge["node_b_name"]
        n = edge["n_cells"]
        badge = _conf_badge(conf)
        lines.append(f"## {name} · {badge}")
        lines.append("")

        # One-line node summary: accession · 10x cell count · supertype
        acc = edge.get("node_b_accession") or ""
        supt = edge.get("supertype") or ""
        summary_parts: list[str] = []
        if acc:
            summary_parts.append(f"`{acc}`")
        if n is not None:
            summary_parts.append(f"{n:,} cells (10x)")
        if supt:
            summary_parts.append(f"supertype: {supt}")
        if summary_parts:
            lines.append("*" + " · ".join(summary_parts) + "*")
            lines.append("")

        support_items = [ev for ev in edge["evidence_items"] if ev["supports"] in ("SUPPORT", "PARTIAL")]
        refute_items = [ev for ev in edge["evidence_items"] if ev["supports"] == "REFUTE"]

        if support_items:
            lines.append("**Supporting evidence:**")
            lines.append("")
            for ev in support_items:
                ref_lbl = ev.get("ref_label", "")
                et_lbl = _evidence_type_label(ev["evidence_type"])
                expl = ev.get("explanation", "")
                filt = ev.get("filters_applied", "")
                detail = filt if filt else expl
                lines.append(f"- {detail} [{et_lbl}]{' ' + ref_lbl if ref_lbl else ''}")
            lines.append("")

        concerns = []
        for ev in refute_items:
            ref_lbl = ev.get("ref_label", "")
            expl = ev.get("explanation", "")
            concerns.append(f"- {expl} [{_evidence_type_label(ev['evidence_type'])}]{' ' + ref_lbl if ref_lbl else ''}")
        for pc in edge["property_comparisons"]:
            if pc.get("alignment") in ("DISCORDANT", "APPROXIMATE"):
                note = pc.get("notes", "")
                prop = pc["property"]
                a_val = pc.get("node_a_value", "")
                b_val = pc.get("node_b_value", "")
                aln = pc["alignment"]
                concerns.append(f"- **{prop}** ({aln}): A={a_val} / B={b_val}. {note}")
        for cav in edge["caveats"]:
            desc = cav.get("description", "").strip()
            concerns.append(f"- {desc}")

        if concerns:
            lines.append("**Concerns:**")
            lines.append("")
            lines.extend(concerns)
            lines.append("")

        # Upgrade path
        upgrade_parts = []
        for q in edge.get("unresolved_questions", []):
            upgrade_parts.append(f"- *Unresolved:* {q}")
        for exp in edge.get("proposed_experiments", []):
            upgrade_parts.append(f"- *Proposed:* {exp}")
        if upgrade_parts:
            lines.append("**What would upgrade confidence:**")
            lines.append("")
            lines.extend(upgrade_parts)
            lines.append("")

        lines.append("---")
        lines.append("")

    # Eliminated / uncertain block
    if uncertain_edges:
        lines.append("## Eliminated candidates")
        lines.append("")
        # Check for shared disqualifier
        common_discordant = None
        for edge in uncertain_edges:
            for pc in edge.get("property_comparisons", []):
                if pc.get("alignment") == "DISCORDANT" and "marker" in pc.get("property", ""):
                    if common_discordant is None:
                        common_discordant = pc["property"]
                    elif common_discordant != pc["property"]:
                        common_discordant = None
                        break
        if common_discordant:
            prop = common_discordant.replace("marker_", "")
            lines.append(f"**Primary reason:** Shared disqualifying signal: {prop} is DISCORDANT across all UNCERTAIN edges.")
            lines.append("")
        for edge in uncertain_edges:
            name = edge["node_b_name"]
            n = f"{edge['n_cells']:,}" if edge["n_cells"] is not None else "?"
            refutes = [
                ev for ev in edge["evidence_items"] if ev["supports"] == "REFUTE"
            ]
            lines.append(f"**{name}** ({n} cells)")
            for ev in refutes:
                ref_lbl = ev.get("ref_label", "")
                expl = ev.get("explanation", "")
                lines.append(f"- {expl} {ref_lbl}".strip())
            for pc in edge.get("property_comparisons", []):
                if pc.get("alignment") == "DISCORDANT":
                    note = pc.get("notes", "")
                    lines.append(f"- {pc['property']}: {note}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # 6. Proposed experiments
    all_node_edges_raw = [e_raw for e_raw in graph.get("edges", []) if e_raw.get("type_a") == node_id]
    exp_groups = _group_experiments(all_node_edges_raw)
    if exp_groups:
        lines.append("## Proposed experiments")
        lines.append("")
        for i, grp in enumerate(exp_groups, 1):
            lines.append(f"### {i} — {grp['group']}")
            lines.append("")
            for exp in grp["experiments"]:
                lines.append(f"- {exp}")
            lines.append(f"*Resolves: {', '.join(grp['edge_ids'])}*")
            lines.append("")
        lines.append("---")
        lines.append("")

    # 7. Open questions
    all_questions = []
    seen_q: set = set()
    for edge in edges:
        for q in edge.get("unresolved_questions", []):
            q_str = q.strip() if isinstance(q, str) else str(q)
            if q_str not in seen_q:
                seen_q.add(q_str)
                all_questions.append(q_str)
    if all_questions:
        lines.append("## Open questions")
        lines.append("")
        for i, q in enumerate(all_questions, 1):
            lines.append(f"{i}. {q}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # 8. Evidence base table
    lines.append("## Evidence base")
    lines.append("")
    lines.append("| Edge | Evidence types | Supports |")
    lines.append("|---|---|---|")
    for edge in edges:
        eid = edge["id"]
        for ev in edge["evidence_items"]:
            et_lbl = _evidence_type_label(ev["evidence_type"])
            ref_lbl = ev.get("ref_label", "")
            supports = ev.get("supports", "")
            lines.append(f"| {eid} | {et_lbl}{' ' + ref_lbl if ref_lbl else ''} | {supports} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 9. References
    lines.append("## References")
    lines.append("")
    lines.append("| # | Citation | PMID | Used for |")
    lines.append("|---|---|---|---|")

    # Sort: numbered first, then lettered
    lit_entries = [(k, v) for k, v in ref_index.items() if not v["label"].startswith("[A") and not v["label"][1].isalpha()]
    query_entries = [(k, v) for k, v in ref_index.items() if v["query_url"]]
    lit_entries.sort(key=lambda x: int(x[1]["label"][1:-1]) if x[1]["label"][1:-1].isdigit() else 99)

    for k, v in lit_entries:
        pmid = v.get("pmid", "")
        cite = v.get("citation_line", "")
        used = v.get("used_for", "")
        pmid_str = f"[{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)" if pmid else "—"
        lines.append(f"| {v['label']} | {cite} | {pmid_str} | {used} |")
    for k, v in query_entries:
        qurl = v.get("query_url", "")
        cite = v.get("citation_line", "")
        filters = v.get("used_for", "")
        url_str = f"[view]({qurl})" if qurl else "—"
        lines.append(f"| {v['label']} | {cite} | — | {filters} · {url_str} |")

    lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {out_path}")


def render_drilldown(
    graph: dict,
    refs: dict,
    node_id: str,
    pmid_or_corpus: str,
    out_path: Path,
    graph_file: Path,
    summary_path: Path | None = None,
) -> None:
    """
    Write Tier 2 drill-down for one paper.
    All quotes come verbatim from references.json — raises KeyError if quote_key missing.
    """
    nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
    node_edges = [e for e in graph.get("edges", []) if e.get("type_a") == node_id]

    # Resolve corpus entry
    bare_pmid = pmid_or_corpus.removeprefix("PMID:")
    corpus_entry = _find_corpus_by_pmid(bare_pmid, refs) or refs.get(pmid_or_corpus)
    if corpus_entry is None:
        raise ValueError(f"PMID/corpus_id '{pmid_or_corpus}' not found in references.json")

    corpus_id = corpus_entry["corpus_id"]
    authors = _coerce_authors(corpus_entry.get("authors"))
    year = corpus_entry.get("year", "")
    pmid = corpus_entry.get("pmid", "")
    doi = corpus_entry.get("doi", "")
    title = corpus_entry.get("title", "")
    quotes = corpus_entry.get("quotes", {})

    # Author string for filename
    if authors:
        first_author_last = authors[0].split()[-1]
    else:
        first_author_last = "Unknown"

    cite_line = _format_citation_line(corpus_entry)
    back_link = f"[← Back to summary report]({summary_path.name})" if summary_path else ""

    lines: list[str] = []
    lines.append(f"# Evidence Drill-down: {first_author_last} et al. {year}")

    # Find edges citing this paper in edge evidence items.
    # LITERATURE evidence has the cite directly in `reference`. Other evidence
    # types (BULK_CORRELATION, ...) cite via run_ref → manifest → dataset →
    # source_pmid; resolve and match.
    citing_edges = []
    for edge in node_edges:
        for ev in edge.get("evidence", []):
            ref = ev.get("reference", "")
            ref_type, bare = _ref_identifier(ref) if ref else ("", "")
            if bare and (bare == pmid or bare == doi or bare == corpus_id):
                citing_edges.append(edge)
                break
            run_ref = ev.get("run_ref", "")
            if run_ref:
                resolved = _resolve_run_ref_to_pmid(run_ref)
                if resolved:
                    _, resolved_bare = _ref_identifier(resolved)
                    if resolved_bare == pmid:
                        citing_edges.append(edge)
                        break

    # Also scan node marker sources — papers cited there provide classical-type
    # evidence that informs all edges, even if not listed per-edge.
    node = nodes_by_id.get(node_id, {})
    node_marker_refs: list[dict] = []
    for field in ("defining_markers", "negative_markers"):
        for m in node.get(field, []):
            for src in m.get("sources", []):
                ref = src.get("ref", "")
                _, bare = _ref_identifier(ref) if ref else ("", "")
                if bare == pmid or bare == doi or bare == corpus_id:
                    node_marker_refs.append(
                        {"symbol": m.get("symbol", ""), "quote_key": src.get("quote_key", "")}
                    )
    for np in node.get("neuropeptides", []):
        if isinstance(np, dict):
            for src in np.get("sources", []):
                ref = src.get("ref", "")
                _, bare = _ref_identifier(ref) if ref else ("", "")
                if bare == pmid or bare == doi or bare == corpus_id:
                    node_marker_refs.append(
                        {"symbol": np.get("symbol", ""), "quote_key": src.get("quote_key", "")}
                    )

    # If paper only cited in node markers, it applies to all edges for this node
    paper_in_node_markers = bool(node_marker_refs)
    if not citing_edges and paper_in_node_markers:
        citing_edges = list(node_edges)

    edge_desc = "; ".join(
        f"{e.get('type_a', '')} → {nodes_by_id.get(e.get('type_b', ''), {}).get('name', e.get('type_b', ''))}"
        for e in citing_edges
    )
    if citing_edges:
        lines.append(f"*Supporting: {edge_desc}*")
    if back_link:
        lines.append(f"*{back_link}*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 2. Citation + why
    lines.append(f"**{cite_line}**")
    lines.append("")
    if title:
        lines.append(f"*{title}*")
        lines.append("")

    # Explanation from first citing evidence item
    for edge in citing_edges:
        for ev in edge.get("evidence", []):
            expl = (ev.get("explanation") or "").strip()
            if expl and ev.get("evidence_type") == "LITERATURE":
                lines.append("**Why this paper matters for the mapping.**")
                lines.append(expl)
                lines.append("")
                break

    lines.append("---")
    lines.append("")

    # 3. Per-property evidence sections from quotes
    if quotes:
        lines.append("## Evidence from this paper")
        lines.append("")
        first_author_str = authors[0].split()[-1] if authors else "Unknown"
        for qk, qobj in quotes.items():
            text = qobj["text"]
            section = qobj.get("section", "")
            claims = qobj.get("claims", [])
            lines.append(f"### {section or qk}")
            lines.append("")
            lines.append(f"> {text}")
            # Attribution line: visible miniref + hidden quote_key for hook validation
            lines.append(
                f"> — {first_author_str} et al. {year}, {section} "
                f"<!-- quote_key: {qk} -->"
            )
            lines.append("")
            if claims:
                lines.append(f"*Claims: {', '.join(claims)}*")
                lines.append("")

    # 4. Summary scorecard
    # Build from node marker sources citing this paper (have quote_key + symbol);
    # cross-reference alignment from edge property_comparisons where property contains symbol.
    lines.append("## Evidence summary")
    lines.append("")
    lines.append("| Property | Claims | Best alignment | Quote key |")
    lines.append("|---|---|---|---|")
    seen_qk: set[str] = set()
    for mr in node_marker_refs:
        symbol = mr["symbol"]
        qk = mr.get("quote_key", "")
        if qk in seen_qk:
            continue
        seen_qk.add(qk)
        # Find best alignment from edge property_comparisons for this marker
        best_aln = "—"
        for edge in node_edges:
            for pc in edge.get("property_comparisons", []):
                prop = pc.get("property", "")
                if symbol.lower() in prop.lower():
                    best_aln = pc.get("alignment", "—")
                    break
        qobj = quotes.get(qk, {})
        claims = ", ".join(qobj.get("claims", [])) or "—"
        lines.append(f"| {symbol} | {claims} | {best_aln} | {qk} |")
    # Fallback: edge evidence items that directly cite this paper
    if not node_marker_refs:
        for edge in citing_edges:
            for pc in edge.get("property_comparisons", []):
                for ev in edge.get("evidence", []):
                    ref = ev.get("reference", "")
                    _, bare = _ref_identifier(ref) if ref else ("", "")
                    if bare == pmid or bare == doi or bare == corpus_id:
                        prop = pc.get("property", "")
                        b_val = pc.get("node_b_value", "")
                        aln = pc.get("alignment", "")
                        lines.append(f"| {prop} | {b_val} | {aln} | — |")
                        break

    lines.append("")
    lines.append("---")
    lines.append("")

    # 5. Critical gap
    open_qs = []
    for edge in citing_edges:
        for q in edge.get("unresolved_questions", []):
            q_str = q.strip() if isinstance(q, str) else str(q)
            if q_str not in open_qs:
                open_qs.append(q_str)
    if open_qs:
        lines.append("## Critical gap")
        lines.append("")
        for q in open_qs:
            lines.append(f"- {q}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # 6. Footer
    source_methods = list({
        qobj.get("source_method", "") for qobj in quotes.values()
        if qobj.get("source_method")
    })
    statuses = list({
        qobj.get("status", "") for qobj in quotes.values() if qobj.get("status")
    })
    lines.append(f"*Drill-down generated from: references.json (corpus_id: {corpus_id})*")
    if source_methods:
        lines.append(f"*Quotes: source_method={', '.join(source_methods)}, status={', '.join(statuses)}*")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {out_path}")


def render_index(region: str, kb_root: Path, out_path: Path) -> None:
    """
    Scan all *.yaml in kb/{draft|mappings}/{region}/.
    For each non-terminal node: name, cl_mapping, best edge (highest confidence),
    edge count by tier. Write sorted index table.
    """
    # Find region directory (draft takes precedence for display)
    region_dirs = []
    for base in (kb_root / "draft", kb_root / "mappings"):
        rdir = base / region
        if rdir.is_dir():
            region_dirs.append((rdir, "draft" if "draft" in str(base) else "canonical"))

    if not region_dirs:
        raise FileNotFoundError(f"Region '{region}' not found under {kb_root}")

    rows = []
    for rdir, status in region_dirs:
        for yaml_file in sorted(rdir.glob("*.yaml")):
            graph = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
            if not graph:
                continue
            nodes_by_id = {n["id"]: n for n in graph.get("nodes", [])}
            all_edges = graph.get("edges", [])
            for node in graph.get("nodes", []):
                if node.get("is_terminal"):
                    continue
                node_id = node["id"]
                node_edges = [e for e in all_edges if e.get("type_a") == node_id]
                best = _best_edge(all_edges, node_id)
                best_conf = best["confidence"] if best else "—"
                best_b = nodes_by_id.get(best["type_b"], {}).get("name", best["type_b"]) if best else "—"

                tier_counts = {c: 0 for c in ("HIGH", "MODERATE", "LOW", "UNCERTAIN")}
                for e in node_edges:
                    c = e.get("confidence", "")
                    if c in tier_counts:
                        tier_counts[c] += 1

                cl = node.get("cl_mapping") or {}
                cl_str = _ot(cl.get("cl_term")) if cl else "—"

                tier_summary = ", ".join(
                    f"{v} {k}" for k, v in tier_counts.items() if v > 0
                )
                breakdown = f"{len(node_edges)} ({tier_summary})"

                rows.append({
                    "name": node.get("name", node_id),
                    "cl_term": cl_str,
                    "best_atlas_hit": best_b,
                    "best_conf": best_conf,
                    "candidates": breakdown,
                    "report_link": f"{node_id}_summary.md",
                    "conf_order": CONF_ORDER.get(best_conf, 99),
                })

    rows.sort(key=lambda r: (r["conf_order"], r["name"]))

    today = date.today().isoformat()
    n_types = len(rows)
    statuses = "/".join(dict.fromkeys(s for _, s in region_dirs))

    header_lines = [
        f"# {region.capitalize()} Cell Type Mapping Index",
        f"*{n_types} classical types · {today} · {statuses}*",
        "",
    ]

    table_lines = [
        "| Classical type | CL term | Best atlas hit | Best confidence | Candidates | Link |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        badge = _conf_badge(row["best_conf"])
        table_lines.append(
            f"| {row['name']} | {row['cl_term']} | {row['best_atlas_hit']} | "
            f"{badge} | {row['candidates']} | [report]({row['report_link']}) |"
        )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(header_lines + table_lines + [""]), encoding="utf-8")
    print(f"Written: {out_path}")


# ── CLI entry point ───────────────────────────────────────────────────────────

def _load_graph_and_refs(graph_file: Path) -> tuple[dict, dict]:
    from evidencell.paths import refs_path_for_graph

    graph = yaml.safe_load(graph_file.read_text(encoding="utf-8"))
    if not graph:
        raise ValueError(f"Empty or invalid YAML: {graph_file}")
    refs_file = refs_path_for_graph(graph_file)
    if refs_file.exists():
        refs = json.loads(refs_file.read_text(encoding="utf-8"))
    else:
        print(f"WARNING: references.json not found at {refs_file}; quotes will be unavailable", file=sys.stderr)
        refs = {}
    return graph, refs


def _classical_nodes(graph: dict) -> list[dict]:
    return [n for n in graph.get("nodes", []) if not n.get("is_terminal")]


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="python -m evidencell.render",
        description="evidencell report generator",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # facts
    p_facts = sub.add_parser("facts", help="Extract structured facts JSON for synthesis subagent")
    p_facts.add_argument("graph_file", type=Path)
    p_facts.add_argument("--node", required=True, help="Classical node id")
    p_facts.add_argument("--output-dir", type=Path, default=None)

    # summary
    p_sum = sub.add_parser("summary", help="Generate Markdown summary report (programmatic mode)")
    p_sum.add_argument("graph_file", type=Path)
    p_sum.add_argument("--node", default=None, help="Classical node id (default: all)")
    p_sum.add_argument("--output-dir", type=Path, default=None)
    p_sum.add_argument("--drilldowns", action="store_true", help="Also generate drill-downs")

    # drilldowns
    p_dd = sub.add_parser("drilldowns", help="Generate Markdown drill-down reports")
    p_dd.add_argument("graph_file", type=Path)
    p_dd.add_argument("--node", required=True, help="Classical node id")
    p_dd.add_argument("--pmid", default=None, help="Specific PMID (default: all cited papers)")
    p_dd.add_argument("--output-dir", type=Path, default=None)

    # index
    p_idx = sub.add_parser("index", help="Generate region index")
    p_idx.add_argument("region", help="Region name (e.g. hippocampus)")
    p_idx.add_argument("--output-dir", type=Path, default=None)

    args = parser.parse_args()

    if args.cmd == "facts":
        from evidencell.paths import reports_dir_for_region, region_from_graph
        graph_file = args.graph_file.resolve()
        graph, refs = _load_graph_and_refs(graph_file)
        facts = extract_node_facts(graph, refs, args.node, graph_file)
        out_dir = args.output_dir or reports_dir_for_region(region_from_graph(graph_file))
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{args.node}_facts.json"
        out_path.write_text(json.dumps(facts, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Written: {out_path}")

    elif args.cmd == "summary":
        from evidencell.paths import reports_dir_for_region, region_from_graph
        graph_file = args.graph_file.resolve()
        graph, refs = _load_graph_and_refs(graph_file)
        out_dir = args.output_dir or reports_dir_for_region(region_from_graph(graph_file))
        nodes = _classical_nodes(graph)
        if args.node:
            node_ids = [args.node]
        else:
            node_ids = [n["id"] for n in nodes]
        for nid in node_ids:
            out_path = out_dir / f"{nid}_summary.md"
            render_summary(graph, refs, nid, out_path, graph_file)
            if args.drilldowns:
                # Generate all drill-downs for this node
                from evidencell.paths import refs_path_for_graph as _rfg
                refs_file = _rfg(graph_file)
                if refs_file.exists():
                    _gen_all_drilldowns(graph, refs, nid, out_dir, graph_file)

    elif args.cmd == "drilldowns":
        from evidencell.paths import reports_dir_for_region, region_from_graph
        graph_file = args.graph_file.resolve()
        graph, refs = _load_graph_and_refs(graph_file)
        out_dir = args.output_dir or reports_dir_for_region(region_from_graph(graph_file))
        if args.pmid:
            _gen_single_drilldown(graph, refs, args.node, args.pmid, out_dir, graph_file)
        else:
            _gen_all_drilldowns(graph, refs, args.node, out_dir, graph_file)

    elif args.cmd == "index":
        # Find kb root relative to cwd
        kb_root = Path.cwd() / "kb"
        out_dir = args.output_dir
        if out_dir is None:
            from evidencell.paths import reports_dir_for_region
            out_dir = reports_dir_for_region(args.region)
        out_path = out_dir / "index.md"
        render_index(args.region, kb_root, out_path)


def _gen_single_drilldown(
    graph: dict, refs: dict, node_id: str, pmid: str, out_dir: Path, graph_file: Path
) -> None:
    bare_pmid = pmid.removeprefix("PMID:")
    corpus_entry = _find_corpus_by_pmid(bare_pmid, refs) or refs.get(pmid)
    if corpus_entry is None:
        print(f"WARNING: PMID '{pmid}' not found in references.json; skipping", file=sys.stderr)
        return
    authors = _coerce_authors(corpus_entry.get("authors"))
    year = corpus_entry.get("year", "")
    first_author_last = authors[0].split()[-1] if authors else "Unknown"
    filename = f"{node_id}_drilldown_{first_author_last}{year}.md"
    out_path = out_dir / filename
    summary_path = out_dir / f"{node_id}_summary.md"
    render_drilldown(graph, refs, node_id, pmid, out_path, graph_file, summary_path)


def _gen_all_drilldowns(
    graph: dict, refs: dict, node_id: str, out_dir: Path, graph_file: Path
) -> None:
    """Generate drill-downs for all papers cited in the node's edges."""
    node_edges = [e for e in graph.get("edges", []) if e.get("type_a") == node_id]
    seen_pmids: set = set()
    for edge in node_edges:
        for ev in edge.get("evidence", []):
            ref = ev.get("reference", "")
            if ref and ev.get("evidence_type") == "LITERATURE":
                _, bare = _ref_identifier(ref)
                if bare not in seen_pmids:
                    seen_pmids.add(bare)
                    _gen_single_drilldown(graph, refs, node_id, ref, out_dir, graph_file)


if __name__ == "__main__":
    main()
