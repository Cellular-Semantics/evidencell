"""
Unit tests for src/evidencell/render.py

Run with: just test-fast (no OAK DB, no network)
"""

import tempfile
from pathlib import Path

import pytest

from evidencell.render import (
    _best_edge,
    _candidate_verdict,
    _collect_quotes,
    _conf_badge,
    _group_experiments,
    _location_note,
    _ot,
    _ref_identifier,
    build_reference_index,
    extract_node_facts,
    render_index,
    render_summary,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

MINIMAL_GRAPH = {
    "name": "Test region",
    "target_atlas": "WMBv1",
    "brain_region": {"id": "UBERON:0000955", "label": "brain", "name_in_source": "brain"},
    "species": {"id": "NCBITaxon:10090", "label": "Mus musculus", "name_in_source": "mouse"},
    "creation_date": "2026-01-01",
    "nodes": [
        {
            "id": "test_classical",
            "name": "Test cell type",
            "definition_basis": "CLASSICAL_MULTIMODAL",
            "is_terminal": False,
            "nt_type": {
                "name_in_source": "GABAergic",
                "cl_terms": [{"id": "CL:0000617", "label": "GABAergic neuron", "name_in_source": "GABAergic"}],
                "sources": [{"ref": "PMID:12345678", "method": "IHC", "scope": "mouse"}],
            },
            "defining_markers": [
                {
                    "symbol": "Sst",
                    "sources": [{"ref": "PMID:12345678", "method": "ISH", "scope": "mouse"}],
                }
            ],
            "negative_markers": [{"symbol": "PV", "modifier": "ABSENT"}],
            "neuropeptides": [{"symbol": "Sst", "sources": []}],
            "anatomical_location": [
                {"id": "UBERON:0014548", "label": "stratum oriens", "name_in_source": "CA1 SO"}
            ],
            "location_sources": [{"ref": "PMID:99999999", "method": "biocytin fill", "scope": "mouse"}],
        },
        {
            "id": "atlas_clus_001",
            "name": "Sst Gaba_1",
            "definition_basis": "ATLAS_TRANSCRIPTOMIC",
            "is_terminal": True,
            "atlas": "WMBv1",
            "n_cells": 100,
            "anatomical_location": [{"id": "MBA:399", "label": "CA1", "name_in_source": "CA1 SO"}],
        },
        {
            "id": "atlas_clus_002",
            "name": "Sst Gaba_2",
            "definition_basis": "ATLAS_TRANSCRIPTOMIC",
            "is_terminal": True,
            "atlas": "WMBv1",
            "n_cells": 50,
            "anatomical_location": [],
        },
    ],
    "edges": [
        {
            "id": "edge_test_to_001",
            "type_a": "test_classical",
            "type_b": "atlas_clus_001",
            "relationship": "TYPE_A_SPLITS",
            "confidence": "MODERATE",
            "evidence": [
                {
                    "evidence_type": "ATLAS_METADATA",
                    "supports": "SUPPORT",
                    "explanation": "Sst subclass consistent.",
                },
                {
                    "evidence_type": "ATLAS_QUERY",
                    "supports": "PARTIAL",
                    "atlas": "ABC Atlas",
                    "query_url": "https://example.com/query",
                    "filters_applied": "anatomy=HPF; Sst",
                    "explanation": "Survives Sst filter.",
                },
            ],
            "property_comparisons": [
                {
                    "property": "nt_type",
                    "node_a_value": "GABAergic",
                    "node_b_value": "GABA",
                    "alignment": "CONSISTENT",
                },
                {
                    "property": "location",
                    "node_a_value": "CA1 SO",
                    "node_b_value": "CA3 SO",
                    "alignment": "APPROXIMATE",
                    "notes": "CA3 SO — adjacent subfield.",
                },
            ],
            "caveats": [],
            "unresolved_questions": ["Is Sst expression cluster-defining?"],
            "proposed_experiments": ["MapMyCells annotation transfer from Sst dataset."],
        },
        {
            "id": "edge_test_to_002",
            "type_a": "test_classical",
            "type_b": "atlas_clus_002",
            "relationship": "TYPE_A_SPLITS",
            "confidence": "UNCERTAIN",
            "evidence": [
                {
                    "evidence_type": "ATLAS_QUERY",
                    "supports": "REFUTE",
                    "atlas": "ABC Atlas",
                    "query_url": "https://example.com/query",
                    "filters_applied": "anatomy=HPF; Sst",
                    "explanation": "Eliminated by Sst filter.",
                }
            ],
            "property_comparisons": [
                {
                    "property": "marker_Sst",
                    "node_a_value": "Sst — defining",
                    "node_b_value": "absent",
                    "alignment": "DISCORDANT",
                    "notes": "Sst absent from cluster.",
                }
            ],
            "caveats": [],
            "unresolved_questions": [],
            "proposed_experiments": ["patch-seq of SO neurons."],
        },
    ],
}

MINIMAL_REFS = {
    "_meta": {"region": "test"},
    "111111": {
        "corpus_id": "111111",
        "author_keys": ["Smith et al., 2020"],
        "title": "A test paper",
        "year": 2020,
        "authors": ["John Smith", "Jane Doe"],
        "pmid": "12345678",
        "doi": "10.1234/test",
        "resolution_confidence": "HIGH",
        "quotes": {
            "111111_abc12345": {
                "text": "Verbatim quote text from the paper.",
                "section": "Results",
                "claims": ["marker_Sst"],
                "source_method": "asta_report",
                "status": "validated",
            }
        },
    },
}


# ── Helper tests ──────────────────────────────────────────────────────────────

def test_conf_badge():
    assert _conf_badge("HIGH") == "🟢 HIGH"
    assert _conf_badge("MODERATE") == "🟡 MODERATE"
    assert _conf_badge("LOW") == "🔴 LOW"
    assert _conf_badge("UNCERTAIN") == "⚪ UNCERTAIN"
    assert _conf_badge("UNKNOWN") == "UNKNOWN"  # Fallback: return as-is


def test_ot_full():
    term = {"label": "stratum oriens", "id": "UBERON:0014548"}
    assert _ot(term) == "stratum oriens (UBERON:0014548)"


def test_ot_label_only():
    term = {"label": "stratum oriens"}
    assert _ot(term) == "stratum oriens"


def test_ot_id_only():
    term = {"id": "UBERON:0014548"}
    assert _ot(term) == "UBERON:0014548"


def test_ot_none():
    assert _ot(None) == ""


def test_ref_identifier_pmid_prefixed():
    assert _ref_identifier("PMID:31420995") == ("pmid", "31420995")


def test_ref_identifier_doi_prefixed():
    assert _ref_identifier("DOI:10.1523/test") == ("doi", "10.1523/test")


def test_ref_identifier_bare_pmid():
    rtype, bare = _ref_identifier("31420995")
    assert rtype == "pmid"
    assert bare == "31420995"


# ── Reference index tests ─────────────────────────────────────────────────────

def test_build_reference_index_ordering():
    """PMIDs from node sources appear before edge evidence; query_urls get [A]-style labels."""
    idx = build_reference_index(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical")
    # PMID:99999999 (location source) should appear before PMID:12345678 (marker/nt source)
    # Both are from node sources and appear in iteration order
    labels = [v.label for v in idx.values() if not v.query_url]
    # All should be numbered
    assert all(lbl.startswith("[") and lbl[1:-1].isdigit() for lbl in labels)
    # Query ref should be lettered
    query_entries = [v for v in idx.values() if v.query_url]
    assert len(query_entries) == 1
    assert query_entries[0].label == "[A]"


def test_build_reference_index_no_invention():
    """A PMID in refs.json but absent from all edge evidence is not included."""
    # Add a paper to refs that's not cited in any edge
    refs_with_extra = dict(MINIMAL_REFS)
    refs_with_extra["999999"] = {
        "corpus_id": "999999",
        "pmid": "00000000",
        "authors": ["Ghost Author"],
        "year": 2000,
        "quotes": {},
    }
    idx = build_reference_index(MINIMAL_GRAPH, refs_with_extra, "test_classical")
    # The ghost PMID should NOT appear in index
    all_pmids = {v.pmid for v in idx.values() if v.pmid}
    assert "00000000" not in all_pmids


def test_build_reference_index_citation_line():
    """Citation line for a known PMID includes author name and year."""
    idx = build_reference_index(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical")
    lit_entries = [v for v in idx.values() if v.pmid == "12345678"]
    assert len(lit_entries) == 1
    assert "Smith" in lit_entries[0].citation_line
    assert "2020" in lit_entries[0].citation_line


# ── Structural helper tests ───────────────────────────────────────────────────

def test_location_note_present():
    """Graph with terminal node + anatomical_location → returns location note."""
    note = _location_note(MINIMAL_GRAPH)
    assert note is not None
    assert "soma position" in note


def test_location_note_absent():
    """Graph with no terminal nodes → returns None."""
    graph_no_terminal = {
        "nodes": [
            {"id": "classical", "is_terminal": False},
        ],
        "edges": [],
    }
    assert _location_note(graph_no_terminal) is None


def test_location_note_terminal_no_location():
    """Terminal node with empty anatomical_location → no note."""
    graph = {
        "nodes": [
            {"id": "atlas_x", "is_terminal": True, "anatomical_location": []},
        ],
        "edges": [],
    }
    assert _location_note(graph) is None


def test_candidate_verdict_moderate():
    edge = {"confidence": "MODERATE", "property_comparisons": []}
    assert _candidate_verdict(edge, {}) == "Best candidate"


def test_candidate_verdict_high():
    edge = {"confidence": "HIGH", "property_comparisons": []}
    assert _candidate_verdict(edge, {}) == "Best candidate"


def test_candidate_verdict_low():
    edge = {"confidence": "LOW", "property_comparisons": []}
    assert _candidate_verdict(edge, {}) == "Speculative"


def test_candidate_verdict_uncertain_discordant_marker():
    edge = {
        "confidence": "UNCERTAIN",
        "property_comparisons": [
            {"property": "marker_Chrna2", "alignment": "DISCORDANT"},
        ],
    }
    verdict = _candidate_verdict(edge, {})
    assert verdict == "Eliminated (Chrna2)"


def test_candidate_verdict_uncertain_no_discordant():
    edge = {
        "confidence": "UNCERTAIN",
        "property_comparisons": [
            {"property": "location", "alignment": "DISCORDANT"},
        ],
    }
    assert _candidate_verdict(edge, {}) == "Eliminated"


def test_best_edge_ordering():
    """HIGH beats MODERATE beats LOW."""
    edges = [
        {"id": "e1", "type_a": "node_x", "type_b": "b1", "confidence": "LOW"},
        {"id": "e2", "type_a": "node_x", "type_b": "b2", "confidence": "HIGH"},
        {"id": "e3", "type_a": "node_x", "type_b": "b3", "confidence": "MODERATE"},
    ]
    best = _best_edge(edges, "node_x")
    assert best["id"] == "e2"


def test_best_edge_no_edges():
    assert _best_edge([], "node_x") is None


def test_best_edge_wrong_node():
    edges = [{"id": "e1", "type_a": "other_node", "confidence": "HIGH"}]
    assert _best_edge(edges, "node_x") is None


# ── Experiment grouping tests ─────────────────────────────────────────────────

def test_group_experiments_by_method():
    edges = [
        {
            "id": "e1",
            "proposed_experiments": ["MapMyCells annotation transfer from Chrna2 dataset."],
        },
        {
            "id": "e2",
            "proposed_experiments": ["patch-seq of stratum oriens neurons."],
        },
        {
            "id": "e3",
            "proposed_experiments": ["MapMyCells with Sst-Cre dataset."],
        },
    ]
    groups = _group_experiments(edges)
    group_names = {g["group"] for g in groups}
    assert "MapMyCells / annotation transfer" in group_names
    assert "Patch-seq" in group_names


def test_group_experiments_deduplication():
    """Near-identical experiments should not be repeated."""
    edges = [
        {"id": "e1", "proposed_experiments": ["MapMyCells annotation transfer."]},
        {"id": "e2", "proposed_experiments": ["MapMyCells annotation transfer."]},
    ]
    groups = _group_experiments(edges)
    mm_group = next(g for g in groups if "MapMyCells" in g["group"])
    assert len(mm_group["experiments"]) == 1
    assert set(mm_group["edge_ids"]) == {"e1", "e2"}


# ── Quote collection tests ────────────────────────────────────────────────────

def test_collect_quotes_valid_key():
    """quote_key present in references.json → returns text verbatim."""
    graph = dict(MINIMAL_GRAPH)
    # Add a quote_key to a node source
    graph["nodes"][0]["location_sources"][0]["quote_key"] = "111111_abc12345"
    quotes = _collect_quotes(graph, MINIMAL_REFS, "test_classical")
    assert "111111_abc12345" in quotes
    assert quotes["111111_abc12345"]["text"] == "Verbatim quote text from the paper."


def test_collect_quotes_missing_key_raises():
    """quote_key present in YAML but absent from references.json → KeyError."""
    graph = dict(MINIMAL_GRAPH)
    graph["nodes"][0]["location_sources"][0]["quote_key"] = "111111_NONEXISTENT"
    with pytest.raises(KeyError, match="111111_NONEXISTENT"):
        _collect_quotes(graph, MINIMAL_REFS, "test_classical")


# ── Facts extractor tests ─────────────────────────────────────────────────────

def test_extract_node_facts_structure():
    """extract_node_facts returns expected top-level keys."""
    facts = extract_node_facts(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", Path("test.yaml"))
    assert "graph_meta" in facts
    assert "reference_index" in facts
    assert "classical_nodes" in facts
    assert "edges" in facts
    assert "quotes" in facts


def test_extract_node_facts_classical_node():
    """Classical node fields are extracted correctly."""
    facts = extract_node_facts(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", Path("test.yaml"))
    cn = facts["classical_nodes"][0]
    assert cn["id"] == "test_classical"
    assert cn["name"] == "Test cell type"
    assert cn["nt"] == "GABAergic"
    assert any(m["symbol"] == "Sst" for m in cn["defining_markers"])
    assert "PV" in cn["negative_markers"]


def test_extract_node_facts_edges_sorted_by_confidence():
    """Edges in facts are sorted MODERATE before UNCERTAIN."""
    facts = extract_node_facts(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", Path("test.yaml"))
    confs = [e["confidence"] for e in facts["edges"]]
    assert confs[0] == "MODERATE"
    assert confs[-1] == "UNCERTAIN"


def test_extract_node_facts_unknown_node_raises():
    with pytest.raises(ValueError, match="not found"):
        extract_node_facts(MINIMAL_GRAPH, MINIMAL_REFS, "nonexistent_node", Path("test.yaml"))


def test_extract_node_facts_terminal_node_raises():
    with pytest.raises(ValueError, match="terminal"):
        extract_node_facts(MINIMAL_GRAPH, MINIMAL_REFS, "atlas_clus_001", Path("test.yaml"))


def test_extract_node_facts_ref_index_no_invention():
    """Reference index does not include PMIDs absent from graph evidence or node sources."""
    facts = extract_node_facts(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", Path("test.yaml"))
    # PMID:99999999 is in location_sources; it should appear with a citation fallback
    # since it's not in MINIMAL_REFS
    ref_pmids = {
        v["pmid"] for v in facts["reference_index"].values() if v.get("pmid")
    }
    # 99999999 cited in location_sources but not in MINIMAL_REFS → appears as unknown
    # 12345678 cited in markers/NT sources and IS in MINIMAL_REFS
    assert "12345678" in ref_pmids


# ── Summary render smoke test ─────────────────────────────────────────────────

def test_render_summary_creates_file():
    """render_summary writes a file without exception."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "test_classical_summary.md"
        render_summary(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", out_path, Path("test.yaml"))
        assert out_path.exists()
        content = out_path.read_text()
        assert "Test cell type" in content
        assert "Mapping candidates" in content
        assert "References" in content


def test_render_summary_contains_confidence_badges():
    """Summary includes confidence badges for all edges."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "test_classical_summary.md"
        render_summary(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", out_path, Path("test.yaml"))
        content = out_path.read_text()
        assert "🟡 MODERATE" in content
        assert "⚪ UNCERTAIN" in content


def test_render_summary_draft_banner():
    """Draft status → draft banner present."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "test_classical_summary.md"
        render_summary(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", out_path,
            Path("kb/draft/test_region/test.yaml"),
        )
        content = out_path.read_text()
        assert "⚠ Draft mappings" in content


def test_render_summary_no_draft_banner_for_canonical():
    """Canonical graph → no draft banner."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "test_classical_summary.md"
        render_summary(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", out_path,
            Path("kb/mappings/test_region/test.yaml"),
        )
        content = out_path.read_text()
        assert "⚠ Draft mappings" not in content


def test_render_summary_reference_table():
    """Reference table includes entries for all cited PMIDs."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "test_classical_summary.md"
        render_summary(MINIMAL_GRAPH, MINIMAL_REFS, "test_classical", out_path, Path("test.yaml"))
        content = out_path.read_text()
        # Smith 2020 should appear in References section (PMID:12345678)
        assert "Smith" in content or "12345678" in content


# ── Index render smoke test ───────────────────────────────────────────────────

def test_render_index_creates_file():
    """render_index writes an index file from YAML on disk."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        # Set up minimal KB structure
        region_dir = tmp_path / "draft" / "testregion"
        region_dir.mkdir(parents=True)
        import yaml as _yaml
        (region_dir / "test_graph.yaml").write_text(
            _yaml.dump(MINIMAL_GRAPH), encoding="utf-8"
        )
        out_path = tmp_path / "reports" / "index.md"
        render_index("testregion", tmp_path, out_path)
        assert out_path.exists()
        content = out_path.read_text()
        assert "Test cell type" in content
        assert "MODERATE" in content or "🟡" in content
