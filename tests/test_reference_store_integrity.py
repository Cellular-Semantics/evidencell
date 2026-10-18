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
    p = tmp_path / "references.json"
    write_quote_to_refs(p, "11290620", "A verbatim passage.", "Results",
                        "ASTA_SNIPPET", "test_run", paper_meta={"title": "T"})
    assert check_quote_key_integrity(json.loads(p.read_text())) == []


def test_write_quote_to_refs_is_append_only(tmp_path):
    p = tmp_path / "references.json"
    write_quote_to_refs(p, "11290620", "First passage.", "Results",
                        "ASTA_SNIPPET", "run1", paper_meta={"title": "T"})
    before = json.loads(p.read_text())
    write_quote_to_refs(p, "11290620", "Second passage, later deepsearch.", "Methods",
                        "ASTA_SNIPPET", "run2")
    after = json.loads(p.read_text())
    assert check_store_append_only(before, after) == []
    assert len(after["11290620"]["quotes"]) == 2


def test_re_adding_the_same_quote_changes_nothing(tmp_path):
    p = tmp_path / "references.json"
    args = (p, "11290620", "A verbatim passage.", "Results", "ASTA_SNIPPET")
    write_quote_to_refs(*args, "run1", paper_meta={"title": "T"})
    before = json.loads(p.read_text())
    write_quote_to_refs(*args, "run2")
    after = json.loads(p.read_text())
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
