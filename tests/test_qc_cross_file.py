"""Tests for the corpus-wide (cross-file) qc_content checks."""

import yaml

from evidencell.qc_content import ERROR, WARN, sweep_cross_file


def _write(root, rel, doc):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(doc), encoding="utf-8")
    return path


def _classical(node_id, **extra):
    return {"id": node_id, "name": node_id,
            "definition_basis": "CLASSICAL_MULTIMODAL", **extra}


def _atlas(node_id, taxonomy_id="CCN20230722", **extra):
    return {"id": node_id, "name": node_id,
            "definition_basis": "ATLAS_TRANSCRIPTOMIC",
            "taxonomy_id": taxonomy_id, **extra}


def _checks(findings, name):
    return [f for f in findings if f.check == name]


def test_duplicate_node_id_detected_across_regions(tmp_path):
    """The duplicates that exist are cross-region.

    `_kb_nodes_for_region` is region-scoped and would never see these, which is
    why the check has to run corpus-wide.
    """
    a = _write(tmp_path, "kb/graphs/region_a/x.yaml",
               {"nodes": [_classical("dup")], "edges": []})
    b = _write(tmp_path, "kb/graphs/region_b/y.yaml",
               {"nodes": [_classical("dup")], "edges": []})
    findings = sweep_cross_file(tmp_path, [a, b])
    hits = _checks(findings, "duplicate_node_id")
    assert len(hits) == 1
    assert hits[0].severity == ERROR
    assert "dup" in hits[0].message
    assert "region_a/x.yaml" in hits[0].message
    assert "region_b/y.yaml" in hits[0].message


def test_repeated_atlas_stub_is_not_a_duplicate(tmp_path):
    """Stubs are pointers; the same accession in many files is duplication,
    not a contested definition."""
    a = _write(tmp_path, "kb/graphs/r/a.yaml", {"nodes": [_atlas("s")], "edges": []})
    b = _write(tmp_path, "kb/graphs/r/b.yaml", {"nodes": [_atlas("s")], "edges": []})
    assert _checks(sweep_cross_file(tmp_path, [a, b]), "duplicate_node_id") == []


def test_unknown_taxonomy_id_detected(tmp_path):
    """The CCN202307220 defect class: a trailing zero made 44 nodes resolve to
    no taxonomy, and every DB lookup for them failed silently."""
    (tmp_path / "kb" / "taxonomy" / "CCN20230722").mkdir(parents=True)
    path = _write(tmp_path, "kb/graphs/r/a.yaml",
                  {"nodes": [_atlas("s", taxonomy_id="CCN202307220")], "edges": []})
    hits = _checks(sweep_cross_file(tmp_path, [path]), "unknown_taxonomy_id")
    assert len(hits) == 1
    assert hits[0].severity == ERROR
    assert "CCN202307220" in hits[0].message


def test_known_taxonomy_id_is_clean(tmp_path):
    (tmp_path / "kb" / "taxonomy" / "CCN20230722").mkdir(parents=True)
    path = _write(tmp_path, "kb/graphs/r/a.yaml",
                  {"nodes": [_atlas("s")], "edges": []})
    assert _checks(sweep_cross_file(tmp_path, [path]), "unknown_taxonomy_id") == []


def test_orphan_node_is_scoped_per_file(tmp_path):
    """A node unreferenced in its own file is dropped by a component split even
    when another file's edge names it."""
    a = _write(tmp_path, "kb/graphs/r/a.yaml",
               {"nodes": [_atlas("lonely")], "edges": []})
    b = _write(tmp_path, "kb/graphs/r/b.yaml", {
        "nodes": [_classical("c"), _atlas("lonely")],
        "edges": [{"id": "e1", "lit_type": "c", "taxonomy_type": "lonely"}],
    })
    hits = _checks(sweep_cross_file(tmp_path, [a, b]), "orphan_node")
    assert len(hits) == 1
    assert hits[0].path.endswith("a.yaml")
    assert hits[0].severity == WARN
    assert "lonely" in hits[0].message


def test_referenced_node_is_not_orphan(tmp_path):
    path = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("c"), _atlas("x")],
        "edges": [{"id": "e1", "lit_type": "c", "taxonomy_type": "x"}],
    })
    assert _checks(sweep_cross_file(tmp_path, [path]), "orphan_node") == []


def test_unparseable_file_is_skipped_not_fatal(tmp_path):
    """The per-file sweep already reports parse failures; this pass must not
    crash on them."""
    bad = tmp_path / "kb/graphs/r/bad.yaml"
    bad.parent.mkdir(parents=True)
    bad.write_text("{[not valid", encoding="utf-8")
    good = _write(tmp_path, "kb/graphs/r/a.yaml",
                  {"nodes": [_classical("a")], "edges": []})
    findings = sweep_cross_file(tmp_path, [bad, good])
    assert all(f.check != "yaml-parse" for f in findings)


def test_every_new_check_has_a_fingerprint_rule():
    """A check with no _SUBJECT_PATTERNS rule falls back to the whole message,
    so rewording it reads as one finding fixed and one new finding appeared."""
    from evidencell.qc_content import _SUBJECTLESS_CHECKS, _SUBJECT_PATTERNS

    for name in ("duplicate_node_id", "unknown_taxonomy_id", "orphan_node"):
        assert name in _SUBJECT_PATTERNS or name in _SUBJECTLESS_CHECKS


def test_fingerprint_rules_actually_match_emitted_messages(tmp_path):
    """A rule that does not match its own messages is worse than no rule."""
    from evidencell.qc_content import _SUBJECTLESS_CHECKS, _subject

    (tmp_path / "kb" / "taxonomy" / "CCN20230722").mkdir(parents=True)
    a = _write(tmp_path, "kb/graphs/r1/a.yaml", {
        "nodes": [_classical("dup"), _atlas("s", taxonomy_id="BAD"), _atlas("lonely")],
        "edges": [{"id": "e1", "lit_type": "dup", "taxonomy_type": "s"}],
    })
    b = _write(tmp_path, "kb/graphs/r2/b.yaml",
               {"nodes": [_classical("dup")], "edges": []})
    findings = sweep_cross_file(tmp_path, [a, b])
    assert findings, "fixture produced no findings"
    for f in findings:
        if f.check in _SUBJECTLESS_CHECKS:
            continue
        assert _subject(f) != f.message, (
            f"check {f.check!r} has no matching subject rule: {f.message}"
        )


# ── Stub shape ────────────────────────────────────────────────────────────────

def test_fat_atlas_stub_is_flagged(tmp_path):
    """kb/taxonomy is canonical for atlas properties; a copy on a stub drifts."""
    path = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"), dict(_atlas("x"), n_cells=42, taxonomy_level="CLUSTER")],
        "edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "x"}],
    })
    hits = _checks(sweep_cross_file(tmp_path, [path]), "stub_shape")
    assert len(hits) == 1
    assert hits[0].severity == WARN
    assert "n_cells" in hits[0].message and "taxonomy_level" in hits[0].message


def test_thin_atlas_stub_is_clean(tmp_path):
    path = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"), _atlas("x")],
        "edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "x"}],
    })
    assert _checks(sweep_cross_file(tmp_path, [path]), "stub_shape") == []


def test_reference_stub_marker_is_not_a_fat_field(tmp_path):
    """The marker is identity, not content -- it must not trip the check."""
    path = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"),
                  dict(_atlas("x"), reference_stub="REFERENCE_TAXONOMY_TYPE")],
        "edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "x"}],
    })
    assert _checks(sweep_cross_file(tmp_path, [path]), "stub_shape") == []


def test_lit_nodes_are_not_subject_to_stub_shape(tmp_path):
    """Only atlas stubs are pointers; a literature node carries its content."""
    path = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [dict(_classical("a"), n_cells=42, notes="lots of curation")],
        "edges": [],
    })
    assert _checks(sweep_cross_file(tmp_path, [path]), "stub_shape") == []
# ── Lit reference stubs ───────────────────────────────────────────────────────

def _lit_stub(node_id):
    return {"id": node_id, "name": node_id,
            "definition_basis": "CLASSICAL_MULTIMODAL", "reference_stub": "LIT_TYPE"}


def test_dangling_lit_stub_detected(tmp_path):
    """Nothing in the in-document endpoint rule checks a stub resolves."""
    path = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"), _lit_stub("ghost")],
        "edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "ghost",
                   "relationship": "skos:closeMatch"}],
    })
    hits = _checks(sweep_cross_file(tmp_path, [path]), "dangling_endpoint")
    assert len(hits) == 1
    assert hits[0].severity == ERROR
    assert "ghost" in hits[0].message


def test_resolved_lit_stub_is_clean(tmp_path):
    a = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"), _lit_stub("b")],
        "edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "b",
                   "relationship": "skos:closeMatch"}],
    })
    b = _write(tmp_path, "kb/graphs/r/b.yaml", {
        "nodes": [_classical("b")],
        "edges": [{"id": "e2", "lit_type": "b", "taxonomy_type": "b",
                   "relationship": "skos:closeMatch"}],
    })
    out = sweep_cross_file(tmp_path, [a, b])
    assert _checks(out, "dangling_endpoint") == []


def test_lit_stub_is_not_a_duplicate_definition(tmp_path):
    """Bucketing by definition_basis alone counts a lit stub as canonical, so
    every cross-file reference would report as a duplicate."""
    a = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"), _lit_stub("b")],
        "edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "b",
                   "relationship": "skos:closeMatch"}],
    })
    b = _write(tmp_path, "kb/graphs/r/b.yaml", {"nodes": [_classical("b")], "edges": []})
    assert _checks(sweep_cross_file(tmp_path, [a, b]), "duplicate_node_id") == []


def test_lit_stub_is_not_reported_as_an_orphan(tmp_path):
    """dangling_endpoint owns stubs; reporting them here too double-counts."""
    a = _write(tmp_path, "kb/graphs/r/a.yaml", {
        "nodes": [_classical("a"), _lit_stub("b")], "edges": [],
    })
    hits = _checks(sweep_cross_file(tmp_path, [a]), "orphan_node")
    assert [h for h in hits if "'b'" in h.message] == []
