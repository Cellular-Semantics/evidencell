"""Unit tests for src/evidencell/references.py"""

import json
import pytest

from evidencell.references import compute_quote_key, write_quote_to_refs


# ── compute_quote_key ────────────────────────────────────────────────────────

def test_compute_quote_key_format():
    key = compute_quote_key("12345", "Some quote text")
    assert key.startswith("12345_")
    assert len(key) == len("12345_") + 8


def test_compute_quote_key_deterministic():
    key1 = compute_quote_key("99", "Exactly the same text")
    key2 = compute_quote_key("99", "Exactly the same text")
    assert key1 == key2


def test_compute_quote_key_normalises_case():
    key_lower = compute_quote_key("1", "some text here")
    key_upper = compute_quote_key("1", "SOME TEXT HERE")
    key_mixed = compute_quote_key("1", "Some Text Here")
    assert key_lower == key_upper == key_mixed


def test_compute_quote_key_normalises_whitespace():
    key_single = compute_quote_key("1", "word another")
    key_multi = compute_quote_key("1", "word  another")
    key_tab = compute_quote_key("1", "word\tanother")
    key_newline = compute_quote_key("1", "word\nanother")
    assert key_single == key_multi == key_tab == key_newline


def test_compute_quote_key_different_texts_differ():
    key1 = compute_quote_key("1", "first quote")
    key2 = compute_quote_key("1", "second quote")
    assert key1 != key2


def test_compute_quote_key_different_corpus_ids_differ():
    key1 = compute_quote_key("111", "same text")
    key2 = compute_quote_key("222", "same text")
    assert key1 != key2


def test_compute_quote_key_known_value():
    # Regression: matches the normalisation documented in asta-report-ingest.md
    # and used in extract_asta_report.py tests
    import hashlib
    text = "Some interneurons of the hippocampus"
    normalised = " ".join(text.lower().split())
    expected_hash = hashlib.sha256(normalised.encode()).hexdigest()[:8]
    expected_key = f"1015389_{expected_hash}"
    assert compute_quote_key("1015389", text) == expected_key


# ── write_quote_to_refs ──────────────────────────────────────────────────────

@pytest.fixture
def tmp_refs(tmp_path):
    """Return a path to a temporary references.json (does not exist yet)."""
    return tmp_path / "references.json"


@pytest.fixture
def existing_refs(tmp_path):
    """Return a path to a references.json with one existing paper + quote."""
    refs = {
        "_meta": {"region": "test", "last_updated": "", "last_updated_by": ""},
        "42": {
            "corpus_id": "42",
            "author_keys": ["Smith et al., 2020"],
            "title": "Existing paper",
            "year": 2020,
            "authors": ["Alice Smith"],
            "pmid": "12345678",
            "doi": "10.1234/existing",
            "resolution_confidence": "HIGH",
            "quotes": {
                "42_abc12345": {
                    "text": "existing quote text",
                    "section": "Results",
                    "claims": [],
                    "source_method": "asta_report",
                    "status": "validated",
                    "added_by": "prior_run",
                }
            },
        },
    }
    p = tmp_path / "references.json"
    p.write_text(json.dumps(refs, indent=2))
    return p


def test_write_quote_creates_file(tmp_refs):
    key = write_quote_to_refs(
        refs_path=tmp_refs,
        corpus_id="100",
        quote_text="A new quote from the paper.",
        section="Results",
        source_method="asta_snippet",
        added_by="test_run",
    )
    assert tmp_refs.exists()
    data = json.loads(tmp_refs.read_text())
    assert "100" in data
    assert key in data["100"]["quotes"]
    assert data["100"]["quotes"][key]["text"] == "A new quote from the paper."


def test_write_quote_returns_correct_key(tmp_refs):
    key = write_quote_to_refs(
        refs_path=tmp_refs,
        corpus_id="200",
        quote_text="Quote for key check.",
        section="Methods",
        source_method="europepmc_fulltext",
        added_by="test_run",
    )
    assert key == compute_quote_key("200", "Quote for key check.")


def test_write_quote_idempotent(tmp_refs):
    kwargs = dict(
        refs_path=tmp_refs,
        corpus_id="300",
        quote_text="Same quote written twice.",
        section="Discussion",
        source_method="asta_snippet",
        added_by="test_run",
    )
    key1 = write_quote_to_refs(**kwargs)
    key2 = write_quote_to_refs(**kwargs)
    assert key1 == key2
    data = json.loads(tmp_refs.read_text())
    assert len(data["300"]["quotes"]) == 1


def test_write_quote_preserves_existing_paper(existing_refs):
    write_quote_to_refs(
        refs_path=existing_refs,
        corpus_id="42",
        quote_text="New quote for existing paper.",
        section="Introduction",
        source_method="asta_snippet",
        added_by="test_run",
    )
    data = json.loads(existing_refs.read_text())
    # Existing quote still present
    assert "42_abc12345" in data["42"]["quotes"]
    # New quote also added
    new_key = compute_quote_key("42", "New quote for existing paper.")
    assert new_key in data["42"]["quotes"]


def test_write_quote_preserves_existing_entries(existing_refs):
    write_quote_to_refs(
        refs_path=existing_refs,
        corpus_id="99",
        quote_text="New paper entry.",
        section="Results",
        source_method="asta_snippet",
        added_by="test_run",
    )
    data = json.loads(existing_refs.read_text())
    # Original paper still present
    assert "42" in data
    assert data["42"]["title"] == "Existing paper"


def test_write_quote_uses_paper_meta(tmp_refs):
    meta = {
        "title": "A Great Paper",
        "year": 2023,
        "authors": [{"name": "Jane Doe"}, {"name": "Bob Lee"}],
        "externalIds": {"PubMed": "99887766", "DOI": "10.9999/great"},
    }
    write_quote_to_refs(
        refs_path=tmp_refs,
        corpus_id="500",
        quote_text="Quote with metadata.",
        section="Results",
        source_method="europepmc_fulltext",
        added_by="test_run",
        paper_meta=meta,
    )
    data = json.loads(tmp_refs.read_text())
    entry = data["500"]
    assert entry["title"] == "A Great Paper"
    assert entry["year"] == 2023
    assert entry["pmid"] == "99887766"
    assert entry["doi"] == "10.9999/great"
    assert "Doe et al., 2023" in entry["author_keys"]


def test_write_quote_status_pending(tmp_refs):
    key = write_quote_to_refs(
        refs_path=tmp_refs,
        corpus_id="600",
        quote_text="Status check quote.",
        section="Results",
        source_method="asta_snippet",
        added_by="test_run",
    )
    data = json.loads(tmp_refs.read_text())
    assert data["600"]["quotes"][key]["status"] == "pending"


def test_write_quote_meta_updated(tmp_refs):
    write_quote_to_refs(
        refs_path=tmp_refs,
        corpus_id="700",
        quote_text="Meta update check.",
        section="Results",
        source_method="asta_snippet",
        added_by="my_extraction_run",
    )
    data = json.loads(tmp_refs.read_text())
    assert data["_meta"]["last_updated_by"] == "my_extraction_run"
    assert data["_meta"]["last_updated"] != ""
