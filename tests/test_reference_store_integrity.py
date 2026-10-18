"""Tests for reference-store integrity: quote-key hashing and append-only writes.

The reference store is the file every other provenance check resolves against,
and until now it was the only one with no write guard. These two checks are what
make `references.write_quote_to_refs()` the mandatory path rather than a
convention.
"""

import json

from evidencell.references import compute_quote_key, write_quote_to_refs
from evidencell.validate import check_quote_key_integrity, check_store_append_only


def _store(**quotes):
    return {
        "_meta": {"region": "hippocampus"},
        "11290620": {
            "corpus_id": "11290620",
            "title": "Hilar mossy cells of the dentate gyrus",
            "pmid": "23420672",
            "doi": "10.3389/fncir.2012.00106",
            "year": 2012,
            "quotes": dict(quotes),
        },
    }


def _quote(text):
    return compute_quote_key("11290620", text), {"text": text, "section": "Results"}


# ── quote-key integrity ───────────────────────────────────────────────────────

def test_key_derived_from_text_passes():
    k, q = _quote("A cell body in the hilus, defined as zone 4 of Amaral (1978).")
    assert check_quote_key_integrity(_store(**{k: q})) == []


def test_text_altered_after_key_minted_is_caught():
    """The exact defect found in the hippocampus store."""
    k, q = _quote("original verbatim text")
    q["text"] = "original verbatim text, with an edit appended"
    errors = check_quote_key_integrity(_store(**{k: q}))
    assert len(errors) == 1
    assert "does not match its text" in errors[0]


def test_hand_authored_key_is_caught():
    _, q = _quote("some verbatim text")
    errors = check_quote_key_integrity(_store(**{"11290620_deadbeef": q}))
    assert len(errors) == 1
    assert "11290620_deadbeef" in errors[0]


def test_key_copied_from_another_quote_is_caught():
    k1, q1 = _quote("first passage")
    _, q2 = _quote("second passage")
    errors = check_quote_key_integrity(_store(**{k1: q1, "11290620_aaaaaaaa": q2}))
    assert len(errors) == 1


def test_quote_without_text_is_caught():
    errors = check_quote_key_integrity(_store(**{"11290620_aaaaaaaa": {"section": "x"}}))
    assert len(errors) == 1
    assert "no text" in errors[0]


def test_meta_block_is_skipped():
    assert check_quote_key_integrity({"_meta": {"region": "x"}}) == []


def test_whitespace_normalisation_is_respected():
    """Keys hash normalised text, so reflowing whitespace must not break them."""
    text = "a passage that was wrapped"
    k = compute_quote_key("11290620", text)
    reflowed = "A  passage   that\nwas   wrapped"
    assert check_quote_key_integrity(_store(**{k: {"text": reflowed}})) == []


# ── append-only ───────────────────────────────────────────────────────────────

def test_adding_a_quote_is_allowed():
    k1, q1 = _quote("first")
    old = _store(**{k1: q1})
    k2, q2 = _quote("second")
    new = _store(**{k1: q1, k2: q2})
    assert check_store_append_only(old, new) == []


def test_adding_a_paper_is_allowed():
    old = _store()
    new = _store()
    new["999"] = {"corpus_id": "999", "title": "New paper", "quotes": {}}
    assert check_store_append_only(old, new) == []


def test_removing_a_quote_is_blocked():
    k1, q1 = _quote("first")
    errors = check_store_append_only(_store(**{k1: q1}), _store())
    assert len(errors) == 1
    assert "would be removed" in errors[0]


def test_removing_a_paper_is_blocked():
    errors = check_store_append_only(_store(), {"_meta": {}})
    assert len(errors) == 1
    assert "11290620" in errors[0]


def test_clobbering_the_whole_store_is_blocked():
    errors = check_store_append_only(_store(), {"totally": "corrupt"})
    assert errors


def test_changing_identity_is_blocked():
    old = _store()
    new = _store()
    new["11290620"]["pmid"] = "99999999"
    errors = check_store_append_only(old, new)
    assert len(errors) == 1
    assert "identity field 'pmid'" in errors[0]


def test_each_identity_field_is_guarded():
    for fld, bad in [("doi", "10.0/x"), ("title", "Different"), ("year", 1999)]:
        new = _store()
        new["11290620"][fld] = bad
        assert check_store_append_only(_store(), new), f"{fld} not guarded"


def test_filling_a_previously_empty_identity_field_is_allowed():
    """Backfilling a missing pmid is an improvement, not a rewrite."""
    old = _store()
    old["11290620"]["pmid"] = ""
    new = _store()
    new["11290620"]["pmid"] = "23420672"
    assert check_store_append_only(old, new) == []


# ── the real writer satisfies both contracts ──────────────────────────────────

def test_write_quote_to_refs_produces_integrity_clean_output(tmp_path):
    from evidencell.references import load_store
    p = tmp_path / "references.json"
    write_quote_to_refs(p, "11290620", "A verbatim passage.", "Results",
                        "ASTA_SNIPPET", "test_run", paper_meta={"title": "T"})
    assert check_quote_key_integrity(load_store(p)) == []


def test_write_quote_to_refs_is_append_only(tmp_path):
    p = tmp_path / "references.json"
    from evidencell.references import load_store
    write_quote_to_refs(p, "11290620", "First passage.", "Results",
                        "ASTA_SNIPPET", "run1", paper_meta={"title": "T"})
    before = load_store(p)
    write_quote_to_refs(p, "11290620", "Second passage, later deepsearch.", "Methods",
                        "ASTA_SNIPPET", "run2")
    after = load_store(p)
    assert check_store_append_only(before, after) == []
    assert len(after["11290620"]["quotes"]) == 2


def test_re_adding_the_same_quote_changes_nothing(tmp_path):
    p = tmp_path / "references.json"
    args = (p, "11290620", "A verbatim passage.", "Results", "ASTA_SNIPPET")
    from evidencell.references import load_store
    write_quote_to_refs(*args, "run1", paper_meta={"title": "T"})
    before = load_store(p)
    write_quote_to_refs(*args, "run2")
    after = load_store(p)
    assert before["11290620"]["quotes"] == after["11290620"]["quotes"]


# ── split layout: papers/ + quotes/ ───────────────────────────────────────────

def _split_region(tmp_path, corpus_id="11290620"):
    """Build a region in the split layout; returns the region dir."""
    d = tmp_path / "references" / "hippocampus"
    (d / "papers").mkdir(parents=True)
    (d / "quotes").mkdir(parents=True)
    (d / "papers" / f"{corpus_id}.json").write_text(json.dumps(
        {"corpus_id": corpus_id, "title": "T", "pmid": "23420672"}))
    k, q = _quote("A verbatim passage.")
    (d / "quotes" / f"{corpus_id}.json").write_text(json.dumps({k: q}))
    return d


def test_load_store_reads_split_layout(tmp_path):
    from evidencell.references import load_store
    d = _split_region(tmp_path)
    store = load_store(d)
    assert store["11290620"]["pmid"] == "23420672"
    assert len(store["11290620"]["quotes"]) == 1


def test_load_store_reads_legacy_layout(tmp_path):
    """Dual-layout reading must stay covered while the shim exists."""
    from evidencell.references import load_store
    d = tmp_path / "references" / "hippocampus"
    d.mkdir(parents=True)
    k, q = _quote("legacy passage")
    (d / "references.json").write_text(json.dumps(_store(**{k: q})))
    store = load_store(d / "references.json")
    assert store["11290620"]["pmid"] == "23420672"


def test_store_exists_true_for_both_layouts(tmp_path):
    from evidencell.references import store_exists
    split = _split_region(tmp_path)
    assert store_exists(split)
    legacy = tmp_path / "references" / "dg"
    legacy.mkdir(parents=True)
    (legacy / "references.json").write_text("{}")
    assert store_exists(legacy / "references.json")


def test_store_exists_false_when_absent(tmp_path):
    """A bare Path.exists() here would silently disable every provenance check."""
    from evidencell.references import store_exists
    assert not store_exists(tmp_path / "references" / "nope")


def test_save_paper_refuses_to_overwrite(tmp_path):
    import pytest
    from evidencell.references import save_paper
    d = _split_region(tmp_path)
    with pytest.raises(FileExistsError):
        save_paper(d, "11290620", {"corpus_id": "11290620", "title": "Different"})


def test_append_quote_is_idempotent(tmp_path):
    from evidencell.references import append_quote
    d = _split_region(tmp_path)
    k, q = _quote("A second passage.")
    assert append_quote(d, "11290620", k, q) is True
    assert append_quote(d, "11290620", k, dict(q, text="hijacked")) is False
    stored = json.loads((d / "quotes" / "11290620.json").read_text())
    assert stored[k]["text"] == "A second passage."


def test_writer_routes_to_split_and_never_recreates_the_monolith(tmp_path):
    from evidencell.references import load_store, write_quote_to_refs
    d = _split_region(tmp_path)
    key = write_quote_to_refs(d / "references.json", "11290620",
                              "Routed passage.", "Results", "ASTA_SNIPPET", "run")
    assert not (d / "references.json").exists()
    assert key in load_store(d)["11290620"]["quotes"]


def test_writer_creates_a_new_paper_in_split_layout(tmp_path):
    from evidencell.references import load_store, write_quote_to_refs
    d = _split_region(tmp_path)
    write_quote_to_refs(d / "references.json", "999", "New paper passage.",
                        "Results", "ASTA_SNIPPET", "run",
                        paper_meta={"title": "New", "pmid": "1"})
    assert (d / "papers" / "999.json").exists()
    assert load_store(d)["999"]["title"] == "New"


def test_split_store_stays_integrity_clean_through_the_writer(tmp_path):
    from evidencell.references import load_store, write_quote_to_refs
    d = _split_region(tmp_path)
    for i in range(3):
        write_quote_to_refs(d / "references.json", "11290620", f"Passage {i}.",
                            "Results", "ASTA_SNIPPET", f"run{i}")
    assert check_quote_key_integrity(load_store(d)) == []


# ── migration ─────────────────────────────────────────────────────────────────

def test_migration_round_trips_exactly(tmp_path):
    from evidencell.migrate_refs import migrate_region
    from evidencell.references import load_store
    d = tmp_path / "references" / "hippocampus"
    d.mkdir(parents=True)
    k1, q1 = _quote("first")
    k2, q2 = _quote("second")
    legacy = _store(**{k1: q1, k2: q2})
    refs_path = d / "references.json"
    refs_path.write_text(json.dumps(legacy))

    before = load_store(refs_path)
    r = migrate_region(refs_path)
    assert r.papers == 1 and r.quotes == 2
    assert not refs_path.exists()
    assert load_store(d) == before


def test_migration_is_idempotent(tmp_path):
    from evidencell.migrate_refs import migrate_region
    d = _split_region(tmp_path)
    r = migrate_region(d / "references.json")
    assert r.skipped == "already split"


# ── review findings: migration safety ─────────────────────────────────────────

def _legacy(tmp_path, payload):
    d = tmp_path / "references" / "r"
    d.mkdir(parents=True)
    (d / "references.json").write_text(json.dumps(payload))
    return d


def test_failed_round_trip_writes_nothing(tmp_path, monkeypatch):
    """A split that would not round-trip must not be left shadowing the monolith.

    Writing first and asserting afterwards leaves a proven-wrong split store on
    disk; is_split_layout() flips True and every later read silently prefers the
    bad copy over the intact references.json.
    """
    import evidencell.migrate_refs as m
    d = _legacy(tmp_path, {"_meta": {"region": "r"}, "111": {"corpus_id": "111"}})
    monkeypatch.setattr(m, "load_store", lambda p: {"deliberately": "different"})
    try:
        m.migrate_region(d / "references.json")
    except AssertionError:
        pass
    assert (d / "references.json").exists(), "monolith must survive"
    assert not (d / "papers").exists(), "nothing may be written on failure"


def test_entry_without_quotes_key_migrates(tmp_path):
    """No 'quotes' key is semantically identical to an empty one."""
    from evidencell.migrate_refs import migrate_region
    from evidencell.references import load_store
    d = _legacy(tmp_path, {"_meta": {"region": "r"},
                           "111": {"corpus_id": "111", "title": "No quotes key"}})
    r = migrate_region(d / "references.json")
    assert r.papers == 1
    assert load_store(d)["111"]["quotes"] == {}


def test_empty_monolith_is_not_deleted(tmp_path):
    """Otherwise verification is tautological and the region loses its store."""
    from evidencell.migrate_refs import migrate_region
    d = _legacy(tmp_path, {"_meta": {"region": "r"}})
    r = migrate_region(d / "references.json")
    assert "no paper entries" in r.skipped
    assert (d / "references.json").exists()


# ── review findings: store resolution ─────────────────────────────────────────

def test_monolith_beside_papers_is_rejected_not_ignored(tmp_path):
    """Silently preferring the split would discard whatever the monolith holds."""
    import pytest
    from evidencell.references import ShadowedStoreError, load_store
    d = tmp_path / "references" / "r"
    (d / "papers").mkdir(parents=True)
    (d / "papers" / "1.json").write_text('{"corpus_id": "1"}')
    (d / "references.json").write_text('{"2": {"corpus_id": "2"}}')
    with pytest.raises(ShadowedStoreError):
        load_store(d)


def test_new_region_is_born_split(tmp_path):
    """A storeless region must not mint a fresh monolith post-migration."""
    from evidencell.references import write_quote_to_refs
    d = tmp_path / "references" / "BG"
    write_quote_to_refs(d / "references.json", "123", "A passage.", "Results",
                        "ASTA_SNIPPET", "run", paper_meta={"title": "T"})
    assert (d / "papers" / "123.json").exists()
    assert not (d / "references.json").exists()


def test_resolver_finds_stores_recursively(tmp_path):
    """Discovery narrowed from rglob to iterdir would silently drop nested stores."""
    from evidencell.fetch import _from_references
    d = tmp_path / "references" / "group" / "r"
    (d / "papers").mkdir(parents=True)
    (d / "papers" / "77.json").write_text(json.dumps(
        {"corpus_id": "77", "pmid": "123", "doi": ""}))
    assert "77" in _from_references(tmp_path)


# ── schema conformance (schema/references.yaml) ───────────────────────────────

def _paper(**over):
    base = {"corpus_id": "11290620", "title": "T", "year": 2012,
            "authors": ["A. Author"], "author_keys": ["Author, 2012"],
            "resolution_confidence": "HIGH"}
    base.update(over)
    return {"_meta": {"region": "r"}, "11290620": {**base, "quotes": {}}}


def test_valid_paper_passes_schema():
    from evidencell.validate import check_store_records
    assert check_store_records(_paper()) == []


def test_missing_required_paper_field_is_caught():
    from evidencell.validate import check_store_records
    s = _paper()
    del s["11290620"]["title"]
    errors = check_store_records(s)
    assert any("title" in e for e in errors)


def test_unmodelled_paper_field_is_caught():
    """The 'banana' case — a brand-new record of arbitrary shape."""
    from evidencell.validate import check_store_records
    s = _paper(banana=True)
    assert any("banana" in e for e in check_store_records(s))


def test_authors_must_be_strings_not_objects():
    """dentate_gyrus stored {'name': ...} objects; every other region stored names."""
    from evidencell.validate import check_store_records
    s = _paper(authors=[{"name": "A. Author"}])
    assert any("authors" in e for e in check_store_records(s))


def test_top_level_pmcid_is_rejected():
    """PubMedCentral belongs in externalIds; a parallel field duplicates it."""
    from evidencell.validate import check_store_records
    assert any("pmcid" in e for e in check_store_records(_paper(pmcid="123")))


def test_bad_resolution_confidence_is_caught():
    from evidencell.validate import check_store_records
    assert check_store_records(_paper(resolution_confidence="SORT_OF"))


def test_quote_without_text_fails_schema():
    from evidencell.validate import check_store_records
    s = _paper()
    s["11290620"]["quotes"] = {"11290620_abcd1234": {"section": "Results"}}
    assert any("text" in e for e in check_store_records(s))


# ── source_method vocabulary ──────────────────────────────────────────────────

def _with_quote(**q):
    s = _paper()
    s["11290620"]["quotes"] = {"11290620_abcd1234": {"text": "t", **q}}
    return s


def test_canonical_source_methods_pass():
    from evidencell.validate import SOURCE_METHODS, check_source_methods
    for m in SOURCE_METHODS:
        assert check_source_methods(_with_quote(source_method=m)) == []


def test_experimental_method_in_source_method_is_flagged():
    from evidencell.validate import check_source_methods
    errors = check_source_methods(
        _with_quote(source_method="patch-clamp (rat hippocampal slice)"))
    assert len(errors) == 1
    assert "not a retrieval method" in errors[0]


def test_absent_source_method_is_not_flagged():
    from evidencell.validate import check_source_methods
    assert check_source_methods(_with_quote()) == []


# ── source_document linkage ───────────────────────────────────────────────────

def test_asta_report_quote_without_source_document_is_flagged():
    from evidencell.validate import check_source_documents
    errors = check_source_documents(_with_quote(source_method="asta_report"), set())
    assert len(errors) == 1
    assert "unrecorded" in errors[0]


def test_asta_report_quote_with_known_source_passes():
    from evidencell.validate import check_source_documents
    s = _with_quote(source_method="asta_report", source_document="a_report")
    assert check_source_documents(s, {"a_report"}) == []


def test_source_document_pointing_at_nothing_is_flagged():
    from evidencell.validate import check_source_documents
    s = _with_quote(source_method="asta_report", source_document="ghost")
    assert any("no record" in e for e in check_source_documents(s, {"a_report"}))


def test_non_asta_quote_needs_no_source_document():
    """Full-text quotes come from the paper itself; the paper is the source."""
    from evidencell.validate import check_source_documents
    s = _with_quote(source_method="europepmc_fulltext")
    assert check_source_documents(s, set()) == []


# ── normalisation ─────────────────────────────────────────────────────────────

def test_normalise_converts_author_objects_losslessly():
    from evidencell.migrate_refs import normalise_paper
    out, changes = normalise_paper({"authors": [{"name": "A. Author"}, "B. Other"]})
    assert out["authors"] == ["A. Author", "B. Other"]
    assert any("authors" in c for c in changes)


def test_normalise_folds_pmcid_into_external_ids():
    from evidencell.migrate_refs import normalise_paper
    out, _ = normalise_paper({"pmcid": "5266860", "externalIds": {"DOI": "10.1/x"}})
    assert "pmcid" not in out
    assert out["externalIds"]["PubMedCentral"] == "5266860"


def test_normalise_drops_redundant_pmcid_without_overwriting():
    from evidencell.migrate_refs import normalise_paper
    out, _ = normalise_paper(
        {"pmcid": "5266860", "externalIds": {"PubMedCentral": "5266860"}})
    assert "pmcid" not in out
    assert out["externalIds"]["PubMedCentral"] == "5266860"


def test_normalise_is_idempotent():
    from evidencell.migrate_refs import normalise_paper
    once, _ = normalise_paper({"authors": [{"name": "A"}], "pmcid": "1"})
    twice, changes = normalise_paper(once)
    assert twice == once
    assert changes == []
