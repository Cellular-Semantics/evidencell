"""Antibody RRID check (#244): lookup parsing, cache, soft skip."""

from __future__ import annotations

import io
import json
import urllib.error
from pathlib import Path

import pytest

from evidencell import rrid as rr
from evidencell.rrid import check_antibody_rrids


def _graph(rrid: str | None) -> dict:
    ab: dict = {"name_in_source": "TuJ1"}
    if rrid:
        ab["rrid"] = rrid
    return {"nodes": [{"id": "n1", "defining_markers": [{
        "name_in_source": "TuJ1", "symbol": "Tubb3", "ncbi_gene_id": "NCBIGene:22152",
        "sources": [{"marker_type": "PROTEIN", "antibody": ab}],
    }]}]}


@pytest.fixture
def cache(tmp_path: Path) -> Path:
    p = tmp_path / "rrid_cache.json"
    p.write_text(json.dumps({
        "RRID:AB_10711040": {"name": "Anti-NeuN antibody [1B7]"},
        "RRID:AB_999999999": {"missing": True},
    }))
    return p


def test_no_rrid_no_check(cache):
    assert check_antibody_rrids(_graph(None), cache_path=cache) == ([], [])


def test_cached_known_rrid_passes(cache):
    assert check_antibody_rrids(_graph("RRID:AB_10711040"), cache_path=cache) == ([], [])


def test_cached_missing_rrid_is_an_error(cache):
    errors, _ = check_antibody_rrids(_graph("RRID:AB_999999999"), cache_path=cache)
    assert len(errors) == 1
    assert "antibody RRID:AB_999999999 is not in the Antibody Registry" in errors[0]


def test_offline_uncached_rrid_is_reported_unchecked(cache, monkeypatch):
    def offline(*a, **kw):
        raise urllib.error.URLError("offline")

    monkeypatch.setattr(rr.urllib.request, "urlopen", offline)
    errors, unchecked = check_antibody_rrids(_graph("RRID:AB_123"), cache_path=cache)
    assert errors == []
    assert unchecked == ["RRID:AB_123: SciCrunch resolver unreachable, not cached"]


def test_lookup_parses_hit_and_404(monkeypatch):
    hit = {"hits": {"total": 1, "hits": [{"_source": {"item": {"name": "Anti-NeuN"}}}]}}

    def fake(req, timeout):
        url = req.full_url
        if "AB_1." in url:
            return io.BytesIO(json.dumps(hit).encode())
        raise urllib.error.HTTPError(url, 404, "not found", {}, None)  # type: ignore[arg-type]

    monkeypatch.setattr(rr.urllib.request, "urlopen", fake)
    assert rr.lookup_rrid("RRID:AB_1") == {"name": "Anti-NeuN"}
    assert rr.lookup_rrid("RRID:AB_2") == {"missing": True}


def test_new_lookups_are_cached(cache, monkeypatch):
    calls: list[str] = []

    def fake_lookup(r, timeout=20):
        calls.append(r)
        return {"name": "x"}

    monkeypatch.setattr(rr, "lookup_rrid", fake_lookup)
    assert check_antibody_rrids(_graph("RRID:AB_5"), cache_path=cache) == ([], [])
    assert check_antibody_rrids(_graph("RRID:AB_5"), cache_path=cache) == ([], [])
    assert calls == ["RRID:AB_5"]
    assert json.loads(cache.read_text())["RRID:AB_5"] == {"name": "x"}
