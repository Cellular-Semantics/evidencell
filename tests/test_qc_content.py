"""Tests for the content QC sweep (`just qc-content`).

Each test builds a miniature repo tree in tmp_path so the sweep runs against
known content rather than the live KB.
"""

import json

import yaml

from evidencell.qc_content import (
    ERROR,
    Finding,
    _fingerprint,
    load_baseline,
    prune_baseline,
    run_sweep,
    stale_baseline_entries,
    sweep_kb_file,
    write_baseline,
)
from evidencell.validate import _collect_flat_refs, check_flat_ref_pmids

# ── fixtures ──────────────────────────────────────────────────────────────────

def _split(region_dir, store):
    """Write a store in the split layout from a legacy-shaped dict."""
    (region_dir / "papers").mkdir(parents=True, exist_ok=True)
    (region_dir / "quotes").mkdir(parents=True, exist_ok=True)
    for cid, entry in store.items():
        if cid == "_meta":
            (region_dir / "_meta.json").write_text(json.dumps(entry))
            continue
        if not isinstance(entry, dict):
            continue
        paper = {k: v for k, v in entry.items() if k != "quotes"}
        paper.setdefault("corpus_id", cid)
        (region_dir / "papers" / f"{cid}.json").write_text(json.dumps(paper))
        (region_dir / "quotes" / f"{cid}.json").write_text(
            json.dumps(entry.get("quotes") or {}))


def _mini_repo(tmp_path, *, region="hippocampus", refs=None, graph=None, report=None):
    """Build a minimal repo tree; returns the root path."""
    (tmp_path / "schema").mkdir(exist_ok=True)  # repo_root() marker
    gdir = tmp_path / "kb" / "graphs" / region
    gdir.mkdir(parents=True, exist_ok=True)
    if graph is not None:
        (gdir / "graph.yaml").write_text(yaml.safe_dump(graph), encoding="utf-8")
    if refs is not None:
        rdir = tmp_path / "references" / region
        rdir.mkdir(parents=True, exist_ok=True)
        _split(rdir, refs)
    if report is not None:
        pdir = tmp_path / "reports" / region
        pdir.mkdir(parents=True, exist_ok=True)
        (pdir / "r.md").write_text(report, encoding="utf-8")
    return tmp_path


REFS_OK = {"smith2020": {"pmid": "12345678", "quotes": {"smith2020_q1": "..."}}}


# ── flat citation lists (#81 / #133) ──────────────────────────────────────────

def test_collect_flat_refs_finds_definition_references():
    doc = {"nodes": [{"definition_references": ["PMID:1", "PMID:2"]}]}
    assert _collect_flat_refs(doc) == [
        ("definition_references", "PMID:1"),
        ("definition_references", "PMID:2"),
    ]


def test_collect_flat_refs_recurses_into_nested_structures():
    doc = {"a": {"b": [{"xrefs": ["PMID:9"]}]}}
    assert ("xrefs", "PMID:9") in _collect_flat_refs(doc)


def test_flat_check_flags_unresolvable_pmid(tmp_path):
    _split(tmp_path, REFS_OK)
    refs = tmp_path
    doc = {"nodes": [{"definition_references": ["PMID:99999999"]}]}
    errors = check_flat_ref_pmids(doc, refs)
    assert len(errors) == 1
    assert "99999999" in errors[0]


def test_flat_check_accepts_resolvable_pmid(tmp_path):
    _split(tmp_path, REFS_OK)
    refs = tmp_path
    doc = {"nodes": [{"definition_references": ["PMID:12345678"]}]}
    assert check_flat_ref_pmids(doc, refs) == []


def test_flat_check_ignores_ccn_accessions_in_xrefs(tmp_path):
    """xrefs legitimately holds CCN accessions — they must not be flagged."""
    _split(tmp_path, REFS_OK)
    refs = tmp_path
    doc = {"nodes": [{"proposed_cl_term": {"xrefs": ["CS20230722_SUPT_0069"]}}]}
    assert check_flat_ref_pmids(doc, refs) == []


def test_flat_check_skips_when_no_refs_store(tmp_path):
    doc = {"nodes": [{"definition_references": ["PMID:99999999"]}]}
    assert check_flat_ref_pmids(doc, tmp_path / "absent.json") == []


# ── sweep-level behaviour ─────────────────────────────────────────────────────

def test_sweep_flags_hallucinated_definition_reference(tmp_path):
    root = _mini_repo(
        tmp_path,
        refs=REFS_OK,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]},
    )
    findings = sweep_kb_file(root / "kb/graphs/hippocampus/graph.yaml", root)
    flat = [f for f in findings if f.check == "flat_citation"]
    assert len(flat) == 1
    # Must be an ERROR, not a WARN — a *new* hallucinated citation has to fail
    # CI, and the baseline file is what absorbs the pre-existing backlog.
    assert flat[0].severity == ERROR


def test_sweep_flags_region_with_no_references_store(tmp_path):
    """A region with no references.json makes every provenance check vacuous."""
    root = _mini_repo(
        tmp_path,
        refs=None,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:12345678"]}]},
    )
    findings = sweep_kb_file(root / "kb/graphs/hippocampus/graph.yaml", root)
    assert [f for f in findings if f.check == "no_refs_store" and f.severity == ERROR]


def test_sweep_quiet_for_unbacked_graph_with_no_citations(tmp_path):
    """No reference store is fine when the graph cites nothing yet."""
    root = _mini_repo(tmp_path, refs=None, graph={"nodes": [{"id": "n1"}]})
    findings = sweep_kb_file(root / "kb/graphs/hippocampus/graph.yaml", root)
    assert [f for f in findings if f.check == "no_refs_store"] == []


def test_sweep_reports_yaml_parse_errors(tmp_path):
    root = _mini_repo(tmp_path, refs=REFS_OK, graph={"nodes": []})
    bad = root / "kb/graphs/hippocampus/graph.yaml"
    bad.write_text("nodes:\n  - a: 1\n   - b: 2\n", encoding="utf-8")
    findings = sweep_kb_file(bad, root)
    assert any(f.check == "yaml-parse" and f.severity == ERROR for f in findings)


def test_sweep_counts_files(tmp_path):
    root = _mini_repo(
        tmp_path, refs=REFS_OK, graph={"nodes": []}, report="# r\n\ntext\n"
    )
    result = run_sweep(root)
    assert result.kb_files == 1
    assert result.report_files == 1


def test_sweep_flags_unannotated_blockquote(tmp_path):
    root = _mini_repo(
        tmp_path, refs=REFS_OK, graph={"nodes": []},
        report="# Report\n\n> an unattributed claim\n",
    )
    result = run_sweep(root)
    assert any(f.check == "markdown" for f in result.findings)


# ── baseline ──────────────────────────────────────────────────────────────────

def test_baseline_roundtrip_absorbs_known_findings(tmp_path):
    root = _mini_repo(
        tmp_path,
        refs=REFS_OK,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]},
    )
    result = run_sweep(root)
    assert result.errors

    bl = tmp_path / "baseline.json"
    n = write_baseline(bl, result)
    assert n == len({_fingerprint(f) for f in result.findings})

    accepted = load_baseline(bl)
    new = [f for f in result.errors if _fingerprint(f) not in accepted]
    assert new == [], "every pre-existing finding should be absorbed"


def test_baseline_does_not_absorb_a_new_finding(tmp_path):
    root = _mini_repo(
        tmp_path,
        refs=REFS_OK,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]},
    )
    bl = tmp_path / "baseline.json"
    write_baseline(bl, run_sweep(root))

    # A second hallucinated PMID appears later.
    (root / "kb/graphs/hippocampus/graph.yaml").write_text(
        yaml.safe_dump({"nodes": [{"id": "n1", "definition_references": [
            "PMID:99999999", "PMID:77777777",
        ]}]}),
        encoding="utf-8",
    )
    accepted = load_baseline(bl)
    new = [f for f in run_sweep(root).errors if _fingerprint(f) not in accepted]
    assert len(new) == 1
    assert "77777777" in new[0].message


def test_stale_entries_detected_when_content_is_fixed(tmp_path):
    """A fixed finding leaves a baseline entry that would re-accept a regression."""
    root = _mini_repo(
        tmp_path,
        refs=REFS_OK,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]},
    )
    bl = tmp_path / "baseline.json"
    write_baseline(bl, run_sweep(root))

    # Content fixed: the bad citation is replaced with a resolvable one.
    (root / "kb/graphs/hippocampus/graph.yaml").write_text(
        yaml.safe_dump({"nodes": [{"id": "n1", "definition_references": ["PMID:12345678"]}]}),
        encoding="utf-8",
    )
    stale = stale_baseline_entries(bl, run_sweep(root))
    assert len(stale) == 1
    assert "99999999" in next(iter(stale))


def test_pruning_closes_the_regression_hole(tmp_path):
    root = _mini_repo(
        tmp_path,
        refs=REFS_OK,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]},
    )
    bl = tmp_path / "baseline.json"
    write_baseline(bl, run_sweep(root))
    good = {"nodes": [{"id": "n1", "definition_references": ["PMID:12345678"]}]}
    gpath = root / "kb/graphs/hippocampus/graph.yaml"
    gpath.write_text(yaml.safe_dump(good), encoding="utf-8")

    stale = stale_baseline_entries(bl, run_sweep(root))
    prune_baseline(bl, sorted(load_baseline(bl) - stale))

    # The bad citation comes back; the pruned baseline must not absorb it.
    gpath.write_text(
        yaml.safe_dump({"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]}),
        encoding="utf-8",
    )
    accepted = load_baseline(bl)
    new = [f for f in run_sweep(root).errors if _fingerprint(f) not in accepted]
    assert len(new) == 1
    assert "99999999" in new[0].message


def test_prune_never_accepts_anything_new(tmp_path):
    """Pruning may only remove entries, never add them."""
    root = _mini_repo(
        tmp_path,
        refs=REFS_OK,
        graph={"nodes": [{"id": "n1", "definition_references": ["PMID:99999999"]}]},
    )
    bl = tmp_path / "baseline.json"
    write_baseline(bl, run_sweep(root))
    before = load_baseline(bl)
    prune_baseline(bl, sorted(before - stale_baseline_entries(bl, run_sweep(root))))
    assert load_baseline(bl) <= before


def test_load_baseline_missing_file_is_empty(tmp_path):
    assert load_baseline(tmp_path / "nope.json") == set()


def test_fingerprint_is_stable_and_distinct():
    a = Finding("f.yaml", ERROR, "flat_citation", "msg")
    b = Finding("f.yaml", ERROR, "flat_citation", "msg")
    c = Finding("f.yaml", ERROR, "flat_citation", "other")
    assert _fingerprint(a) == _fingerprint(b)
    assert _fingerprint(a) != _fingerprint(c)


# ── fingerprint stability ─────────────────────────────────────────────────────

def test_fingerprint_survives_a_message_rewording():
    """The whole point: improving wording must not look like a new finding.

    Fingerprinting on the rendered message caused three spurious re-baselines
    while the compat shim was removed. Each needed a manual 1-new/1-stale
    check; skipping that check once would absorb a real regression.
    """
    before = Finding("kb/x.yaml", ERROR, "flat_citation",
                     "definition_references: 'PMID:123' not found in references.json. Fix it.")
    after = Finding("kb/x.yaml", ERROR, "flat_citation",
                    "definition_references: 'PMID:123' is absent from the hippocampus "
                    "reference store. Either ingest the paper or remove the citation.")
    assert _fingerprint(before) == _fingerprint(after)


def test_fingerprint_still_separates_different_subjects():
    a = Finding("kb/x.yaml", ERROR, "flat_citation", "'PMID:111' not found.")
    b = Finding("kb/x.yaml", ERROR, "flat_citation", "'PMID:222' not found.")
    assert _fingerprint(a) != _fingerprint(b)


def test_fingerprint_still_separates_files_and_checks():
    a = Finding("kb/x.yaml", ERROR, "flat_citation", "'PMID:111' not found.")
    assert _fingerprint(a) != _fingerprint(Finding("kb/y.yaml", ERROR, "flat_citation",
                                                   "'PMID:111' not found."))
    assert _fingerprint(a) != _fingerprint(Finding("kb/x.yaml", ERROR, "ref_pmid",
                                                   "'PMID:111' not found."))


def test_every_emitted_check_has_a_subject_rule():
    """A new check without a rule silently falls back to the full message and
    reintroduces the churn. Fail here instead, where the fix is one line."""
    from evidencell.qc_content import _SUBJECT_PATTERNS, _SUBJECTLESS_CHECKS, run_sweep
    emitted = {f.check for f in run_sweep().findings}
    missing = emitted - set(_SUBJECT_PATTERNS) - _SUBJECTLESS_CHECKS
    assert not missing, f"checks with no subject rule: {sorted(missing)}"


# ── gaps are not backlog ──────────────────────────────────────────────────────

def _store_with_asta_quote(tmp_path, *, source_document=None):
    import json as _json
    d = tmp_path / "references" / "hippocampus"
    (d / "papers").mkdir(parents=True)
    (d / "quotes").mkdir(parents=True)
    (d / "papers" / "11.json").write_text(_json.dumps(
        {"corpus_id": "11", "title": "T", "year": 2020, "authors": ["A"],
         "author_keys": ["A, 2020"], "resolution_confidence": "HIGH"}))
    q = {"text": "t", "source_method": "asta_report"}
    if source_document:
        q["source_document"] = source_document
    (d / "quotes" / "11.json").write_text(_json.dumps({"11_aaaaaaaa": q}))
    (tmp_path / "schema").mkdir(exist_ok=True)
    return d


def test_missing_source_document_is_a_gap_not_a_failure(tmp_path):
    """Those ASTA PDFs were never committed; no change here can fix it."""
    from evidencell.qc_content import GAP, sweep_reference_store
    d = _store_with_asta_quote(tmp_path)
    f = [x for x in sweep_reference_store(d, tmp_path) if x.check == "source_document"]
    assert len(f) == 1
    assert f[0].severity == GAP


def test_dangling_source_document_is_an_error(tmp_path):
    """Pointing at a record that does not exist is fixable — a broken
    reference, not a missing one."""
    from evidencell.qc_content import ERROR, sweep_reference_store
    d = _store_with_asta_quote(tmp_path, source_document="ghost")
    f = [x for x in sweep_reference_store(d, tmp_path) if x.check == "source_document"]
    assert len(f) == 1
    assert f[0].severity == ERROR


def test_gaps_are_collapsed_per_paper_not_per_quote(tmp_path):
    """241 per-quote findings filled three quarters of the baseline."""
    import json as _json
    from evidencell.qc_content import sweep_reference_store
    d = _store_with_asta_quote(tmp_path)
    (d / "quotes" / "11.json").write_text(_json.dumps({
        f"11_{i:08x}": {"text": f"t{i}", "source_method": "asta_report"}
        for i in range(5)}))
    f = [x for x in sweep_reference_store(d, tmp_path) if x.check == "source_document"]
    assert len(f) == 1, "five affected quotes on one paper is one finding"
    assert "5 asta_report quote(s)" in f[0].message


def test_gaps_are_excluded_from_the_baseline(tmp_path):
    """Mixing them is what made '0 new / 0 stale' stop meaning anything."""
    from evidencell.qc_content import GAP, load_baseline, run_sweep, write_baseline
    _store_with_asta_quote(tmp_path)
    result = run_sweep(tmp_path)
    assert any(f.severity == GAP for f in result.findings)
    bl = tmp_path / "baseline.json"
    write_baseline(bl, result)
    accepted = load_baseline(bl)
    gaps = {_fingerprint(f) for f in result.findings if f.severity == GAP}
    assert not (accepted & gaps), "a gap must never enter the baseline"


def test_gaps_do_not_fail_the_sweep(tmp_path):
    from evidencell.qc_content import GAP, run_sweep
    _store_with_asta_quote(tmp_path)
    result = run_sweep(tmp_path)
    assert result.gaps
    assert all(f.severity == GAP for f in result.gaps)
    assert not [f for f in result.errors if f.check == "source_document"]


# ── coverage reporting: silence must be visible ───────────────────────────────

def test_sweep_reports_regions_with_no_reference_store(tmp_path):
    """Those files' provenance checks return [] — the sweep must say so.

    The pre-edit hook already reports this per file. Without the same report
    here, the corpus-wide sweep (the one CI runs) could pass with checks inert
    across the whole repository and say nothing.
    """
    root = _mini_repo(tmp_path, refs=None, graph={"nodes": [{"id": "n1"}]})
    result = run_sweep(root)
    assert any("no reference store" in u for u in result.unavailable)
    assert any("1 file(s) unchecked" in u for u in result.unavailable)


def test_sweep_reports_missing_term_index(tmp_path):
    """The CURIE check has never fired in this repo; make that visible."""
    root = _mini_repo(tmp_path, refs=REFS_OK, graph={"nodes": []},
                      report="# r\n\ntext\n")
    result = run_sweep(root)
    assert any("term_index.json" in u for u in result.unavailable)


def test_sweep_reports_nothing_when_all_stores_are_present(tmp_path):
    root = _mini_repo(tmp_path, refs=REFS_OK, graph={"nodes": []})
    (root / "references" / "hippocampus" / "term_index.json").write_text("{}")
    result = run_sweep(root)
    assert result.unavailable == []


def test_coverage_gap_is_not_a_finding(tmp_path):
    """Coverage is about what ran, not about the content. It must not be
    baselined, counted as an error, or make the sweep fail."""
    root = _mini_repo(tmp_path, refs=None, graph={"nodes": [{"id": "n1"}]})
    result = run_sweep(root)
    assert result.unavailable
    assert not [f for f in result.findings if "unchecked" in f.message]
