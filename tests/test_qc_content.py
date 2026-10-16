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
    run_sweep,
    sweep_kb_file,
    write_baseline,
)
from evidencell.validate import _collect_flat_refs, check_flat_ref_pmids

# ── fixtures ──────────────────────────────────────────────────────────────────

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
        (rdir / "references.json").write_text(json.dumps(refs), encoding="utf-8")
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
    refs = tmp_path / "references.json"
    refs.write_text(json.dumps(REFS_OK))
    doc = {"nodes": [{"definition_references": ["PMID:99999999"]}]}
    errors = check_flat_ref_pmids(doc, refs)
    assert len(errors) == 1
    assert "99999999" in errors[0]


def test_flat_check_accepts_resolvable_pmid(tmp_path):
    refs = tmp_path / "references.json"
    refs.write_text(json.dumps(REFS_OK))
    doc = {"nodes": [{"definition_references": ["PMID:12345678"]}]}
    assert check_flat_ref_pmids(doc, refs) == []


def test_flat_check_ignores_ccn_accessions_in_xrefs(tmp_path):
    """xrefs legitimately holds CCN accessions — they must not be flagged."""
    refs = tmp_path / "references.json"
    refs.write_text(json.dumps(REFS_OK))
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


def test_load_baseline_missing_file_is_empty(tmp_path):
    assert load_baseline(tmp_path / "nope.json") == set()


def test_fingerprint_is_stable_and_distinct():
    a = Finding("f.yaml", ERROR, "flat_citation", "msg")
    b = Finding("f.yaml", ERROR, "flat_citation", "msg")
    c = Finding("f.yaml", ERROR, "flat_citation", "other")
    assert _fingerprint(a) == _fingerprint(b)
    assert _fingerprint(a) != _fingerprint(c)
