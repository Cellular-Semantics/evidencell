"""Tests for corpus-ID → PMID/DOI resolution (`just fetch-reference`).

Offline layers are tested against tmp_path fixtures. Anything that touches the
network is marked `integration` so the default suite stays hermetic — the
keyless Semantic Scholar pool returns 429 under normal load and must never be
able to fail CI.
"""

import json

import pytest

from evidencell.fetch import (
    SOURCE_CATALOGUE,
    SOURCE_REFERENCES,
    Resolution,
    resolve_corpus_ids,
    verify_pmid,
)


def _repo(tmp_path, *, refs=None, catalogue=None):
    (tmp_path / "schema").mkdir(exist_ok=True)
    if refs is not None:
        d = tmp_path / "references" / "hippocampus"
        d.mkdir(parents=True, exist_ok=True)
        (d / "references.json").write_text(json.dumps(refs), encoding="utf-8")
    if catalogue is not None:
        d = tmp_path / "research" / "hippocampus" / "run"
        d.mkdir(parents=True, exist_ok=True)
        (d / "paper_catalogue.json").write_text(json.dumps(catalogue), encoding="utf-8")
    return tmp_path


SIK = {
    "10664418": {
        "corpus_id": "10664418",
        "title": "Hippocampal CA1 interneurons: an in vivo intracellular labeling study",
        "pmid": "7472426",
        "doi": "",
        "year": 1995,
    }
}

CATALOGUE = {
    "result": [
        {
            "title": "Hippocampal CA1 interneurons",
            "year": 1995,
            "externalIds": {"CorpusId": 10664418, "PubMed": "7472426"},
        }
    ]
}


# ── layer 1: validated reference store ────────────────────────────────────────

def test_resolves_from_references_store(tmp_path):
    root = _repo(tmp_path, refs=SIK)
    out = resolve_corpus_ids(["10664418"], root=root, allow_network=False)
    assert out["10664418"].pmid == "7472426"
    assert out["10664418"].source == SOURCE_REFERENCES


def test_accepts_prefixed_corpus_id(tmp_path):
    root = _repo(tmp_path, refs=SIK)
    out = resolve_corpus_ids(["CorpusId:10664418"], root=root, allow_network=False)
    assert out["10664418"].pmid == "7472426"


def test_meta_block_is_not_treated_as_a_paper(tmp_path):
    """references.json carries a `_meta` bookkeeping key alongside papers."""
    refs = dict(SIK)
    refs["_meta"] = {"region": "hippocampus", "last_updated": "2026-04-29"}
    root = _repo(tmp_path, refs=refs)
    out = resolve_corpus_ids(["_meta"], root=root, allow_network=False)
    assert out == {}


# ── layer 2: cached catalogues ────────────────────────────────────────────────

def test_resolves_from_catalogue_when_store_lacks_it(tmp_path):
    root = _repo(tmp_path, catalogue=CATALOGUE)
    out = resolve_corpus_ids(["10664418"], root=root, allow_network=False)
    assert out["10664418"].pmid == "7472426"
    assert out["10664418"].source == SOURCE_CATALOGUE


def test_references_store_wins_over_catalogue(tmp_path):
    """The validated store is authoritative; a raw catalogue is not."""
    stale = {"result": [{"externalIds": {"CorpusId": 10664418, "PubMed": "99999999"}}]}
    root = _repo(tmp_path, refs=SIK, catalogue=stale)
    out = resolve_corpus_ids(["10664418"], root=root, allow_network=False)
    assert out["10664418"].pmid == "7472426"
    assert out["10664418"].source == SOURCE_REFERENCES


# ── misses ────────────────────────────────────────────────────────────────────

def test_unknown_corpus_id_is_absent_not_empty(tmp_path):
    """A miss must be distinguishable from 'resolved to nothing'."""
    root = _repo(tmp_path, refs=SIK)
    out = resolve_corpus_ids(["404404"], root=root, allow_network=False)
    assert "404404" not in out


def test_offline_never_calls_network(tmp_path, monkeypatch):
    from evidencell import fetch

    def _boom(*a, **k):
        raise AssertionError("network called despite allow_network=False")

    monkeypatch.setattr(fetch, "_from_api", _boom)
    root = _repo(tmp_path, refs=SIK)
    assert resolve_corpus_ids(["404404"], root=root, allow_network=False) == {}


def test_api_failure_yields_miss_not_false_negative(tmp_path, monkeypatch):
    """A 429 means 'unknown', never 'this paper does not exist'."""
    from evidencell import fetch

    monkeypatch.setattr(fetch, "_from_api", lambda ids, **k: {})
    root = _repo(tmp_path, refs=SIK)
    out = resolve_corpus_ids(["404404"], root=root, allow_network=True)
    assert "404404" not in out


def test_resolution_resolved_property():
    assert not Resolution(corpus_id="1").resolved
    assert Resolution(corpus_id="1", pmid="7472426").resolved
    assert Resolution(corpus_id="1", doi="10.1/x").resolved


# ── network-dependent ─────────────────────────────────────────────────────────

def _epmc(pmid):
    """Call verify_pmid, skipping the test if Europe PMC is unreachable.

    An unreachable service must never be reported as a verdict about a PMID —
    that is the same confusion this module exists to prevent.
    """
    try:
        return verify_pmid(pmid)
    except OSError as exc:
        pytest.skip(f"Europe PMC unreachable: {exc}")


@pytest.mark.integration
def test_verify_pmid_rejects_a_fabricated_id():
    """PMID:29412992 is cited on five DG nodes and does not exist."""
    assert _epmc("29412992") is None


@pytest.mark.integration
def test_verify_pmid_accepts_a_real_id():
    rec = _epmc("7472426")
    assert rec is not None
    assert "interneuron" in rec.title.lower()
