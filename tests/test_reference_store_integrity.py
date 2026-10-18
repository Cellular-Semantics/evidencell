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
