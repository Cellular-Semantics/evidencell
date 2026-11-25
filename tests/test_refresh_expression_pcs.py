"""refresh-expression: which names a stale marker PC is looked up by (review #7).

Free text in ``node_a_value`` is never resolved through synonyms or case:
``In`` is a unique synonym of Ahr on WMB, so "In layer 5 …" would write
Ahr's expression onto the PC. A curated marker's pin decides alone.
"""

from __future__ import annotations

import pytest

from evidencell import refresh_expression_pcs as rep
from evidencell.gene_identity import (
    ACCEPTED_METHODS,
    EXACT_SYMBOL,
    NO_GENE,
    NO_GENE_ID,
    PINNED_ID,
    UNIQUE_SYNONYM,
    Pin,
)


def _edge(prop: str, node_a: str) -> dict:
    return {
        "id": "e1", "taxonomy_type": "CS1",
        "property_comparisons": [
            {"property": prop, "node_a_value": node_a, "node_b_value": "not assessed"},
        ],
    }


@pytest.fixture
def fake_expression(monkeypatch):
    """``methods`` says how each name resolved; resolved names have a value."""
    methods: dict[str, str] = {}

    def fake(taxonomy_id, accession, symbols, gene_ids=None):
        ok = [s for s in symbols if methods.get(s) in ACCEPTED_METHODS]
        return (
            {s: 1.0 for s in ok},
            {s: s.upper() for s in ok},
            {s: methods[s] for s in symbols if s in methods},
        )

    monkeypatch.setattr(rep, "_load_expression", fake)
    return methods


def test_text_token_must_be_an_exact_symbol(fake_expression):
    fake_expression.update({"In": UNIQUE_SYNONYM, "Sst": EXACT_SYMBOL})
    edge = _edge("marker_somatostatin", "In layer 5 these cells express Sst")
    changes = rep.refresh_edge(edge, "T")
    assert [c["gene"] for c in changes] == ["SST"]


def test_text_token_by_synonym_alone_is_not_used(fake_expression):
    fake_expression.update({"In": UNIQUE_SYNONYM})
    assert rep.refresh_edge(_edge("marker_foo", "In layer 5"), "T") == []


def test_curated_marker_without_gene_is_not_rescued_by_text(fake_expression):
    """A NO_GENE_ID marker stays unmeasured: the words of node_a_value
    (Ncam1 here) are not tried in its place."""
    fake_expression.update({"PSA-NCAM": NO_GENE_ID, "Ncam1": EXACT_SYMBOL})
    edge = _edge("marker_PSA-NCAM", "PSA-NCAM+ by IHC (Ncam1 glycoform)")
    assert rep.refresh_edge(edge, "T", {"PSA-NCAM": NO_GENE}) == []
    assert edge["property_comparisons"][0]["node_b_value"] == "not assessed"


def test_pinned_marker_is_looked_up_by_its_pin_only():
    pc = {"property": "marker_CB", "node_a_value": "CB+ and Sst+"}
    assert rep._candidate_gene_symbols(pc, {"CB": Pin("NCBIGene:12307", "Calb1")}) == [
        ("CB", False)
    ]


def test_pinned_suffix_still_measured(fake_expression):
    fake_expression.update({"CB": PINNED_ID})
    changes = rep.refresh_edge(
        _edge("marker_CB", "CB+"), "T", {"CB": Pin("NCBIGene:12307", "Calb1")}
    )
    assert [c["gene"] for c in changes] == ["CB"]


def test_uncurated_suffix_resolves_by_name_as_elsewhere(fake_expression):
    """The suffix is a marker name, so it resolves like any unpinned name
    (here by a unique synonym); only free-text words are restricted."""
    fake_expression.update({"PV": UNIQUE_SYNONYM})
    assert [c["gene"] for c in rep.refresh_edge(_edge("marker_PV", "PV+"), "T")] == ["PV"]
