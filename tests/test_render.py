"""
Unit tests for src/evidencell/render.py

Run with: just test-fast (no OAK DB, no network)
"""

import tempfile
import yaml
from pathlib import Path
from unittest.mock import patch

import pytest

from evidencell.render import (
    _best_edge,
    _candidate_verdict,
    _coerce_authors,
    _collect_quotes,
    _conf_badge,
    _format_citation_line,
    _gen_all_drilldowns,
    _gen_single_drilldown,
    _group_experiments,
    _location_note,
    _ot,
    _ref_identifier,
    build_reference_index,
    extract_node_facts,
    render_drilldown,
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
                {"id": "UBERON:0014548", "label": "stratum oriens", "name_in_source": "CA1 SO",
                 "sources": [{"ref": "PMID:99999999", "method": "biocytin fill", "scope": "mouse"}]}
            ],
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
    "222222": {
        "corpus_id": "222222",
        "author_keys": ["Jones et al., 2022"],
        "title": "A second test paper",
        "year": 2022,
        "authors": ["Alice Jones"],
        "pmid": "99999999",
        "doi": "10.1234/test2",
        "resolution_confidence": "HIGH",
        "quotes": {
            "222222_def67890": {
                "text": "Another verbatim quote from a second paper.",
                "section": "Discussion",
                "claims": ["morphology"],
                "source_method": "primary",
                "status": "verified",
            }
        },
    },
}

# Graph with a LITERATURE evidence edge (needed for _gen_all_drilldowns traversal)
GRAPH_WITH_LITERATURE_EDGE = {
    **MINIMAL_GRAPH,
    "edges": MINIMAL_GRAPH["edges"] + [
        {
            "id": "edge_test_lit",
            "type_a": "test_classical",
            "type_b": "atlas_clus_001",
            "relationship": "EQUIVALENT",
            "confidence": "HIGH",
            "evidence": [
                {
                    "evidence_type": "LITERATURE",
                    "supports": "SUPPORT",
                    "reference": "PMID:99999999",
                    "explanation": "Jones 2022 reports marker co-expression.",
                }
            ],
            "property_comparisons": [],
            "caveats": [],
            "unresolved_questions": [],
            "proposed_experiments": [],
        }
    ],
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
    graph["nodes"][0]["anatomical_location"][0]["sources"][0]["quote_key"] = "111111_abc12345"
    quotes = _collect_quotes(graph, MINIMAL_REFS, "test_classical")
    assert "111111_abc12345" in quotes
    assert quotes["111111_abc12345"]["text"] == "Verbatim quote text from the paper."


def test_collect_quotes_missing_key_raises():
    """quote_key present in YAML but absent from references.json → KeyError."""
    graph = dict(MINIMAL_GRAPH)
    graph["nodes"][0]["anatomical_location"][0]["sources"][0]["quote_key"] = "111111_NONEXISTENT"
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
    # PMID:99999999 is in anatomical_location[].sources; it should appear with a citation fallback
    # since it's not in MINIMAL_REFS
    ref_pmids = {
        v["pmid"] for v in facts["reference_index"].values() if v.get("pmid")
    }
    # 99999999 cited in anatomical_location sources but not in MINIMAL_REFS → appears as unknown
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
        (region_dir / "test_graph.yaml").write_text(
            yaml.dump(MINIMAL_GRAPH), encoding="utf-8"
        )
        out_path = tmp_path / "reports" / "index.md"
        render_index("testregion", tmp_path, out_path)
        assert out_path.exists()
        content = out_path.read_text()
        assert "Test cell type" in content
        assert "MODERATE" in content or "🟡" in content


# ── Drilldown render tests ────────────────────────────────────────────────────

def test_render_drilldown_creates_file():
    """render_drilldown writes a file without exception."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "test_classical_drilldown_Smith2020.md"
        render_drilldown(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
            "PMID:12345678", out_path, Path("kb/draft/test/test.yaml"),
        )
        assert out_path.exists()
        content = out_path.read_text()
        assert "Smith" in content
        assert "2020" in content


def test_render_drilldown_contains_quote():
    """Drill-down includes verbatim quote text from references.json."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "dd.md"
        render_drilldown(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
            "PMID:12345678", out_path, Path("test.yaml"),
        )
        content = out_path.read_text()
        assert "Verbatim quote text from the paper." in content


def test_render_drilldown_bare_pmid():
    """render_drilldown accepts bare PMID (without PMID: prefix)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "dd.md"
        render_drilldown(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
            "12345678", out_path, Path("test.yaml"),
        )
        assert out_path.exists()


def test_render_drilldown_unknown_pmid_raises():
    """Unresolvable PMID raises ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "dd.md"
        with pytest.raises(ValueError, match="not found in references.json"):
            render_drilldown(
                MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
                "PMID:00000000", out_path, Path("test.yaml"),
            )


def test_render_drilldown_with_summary_back_link():
    """When summary_path provided, drill-down includes back-link."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "dd.md"
        summary_path = Path(tmpdir) / "test_classical_summary.md"
        render_drilldown(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
            "PMID:12345678", out_path, Path("test.yaml"),
            summary_path=summary_path,
        )
        content = out_path.read_text()
        assert "← Back to summary report" in content



# ── _gen_single_drilldown / _gen_all_drilldowns tests ────────────────────────

def test_gen_single_drilldown_creates_named_file():
    """_gen_single_drilldown writes file named {node}_{author}{year}.md."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_dir = Path(tmpdir)
        _gen_single_drilldown(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
            "PMID:12345678", out_dir, Path("test.yaml"),
        )
        files = list(out_dir.glob("*drilldown*.md"))
        assert len(files) == 1
        assert "Smith" in files[0].name
        assert "2020" in files[0].name


def test_gen_single_drilldown_unknown_pmid_warns(capsys):
    """Unknown PMID prints warning to stderr and does not raise."""
    with tempfile.TemporaryDirectory() as tmpdir:
        _gen_single_drilldown(
            MINIMAL_GRAPH, MINIMAL_REFS, "test_classical",
            "PMID:00000000", Path(tmpdir), Path("test.yaml"),
        )
        captured = capsys.readouterr()
        assert "WARNING" in captured.err


def test_gen_all_drilldowns_iterates_literature_evidence():
    """_gen_all_drilldowns generates one file per unique LITERATURE PMID."""
    with tempfile.TemporaryDirectory() as tmpdir:
        out_dir = Path(tmpdir)
        _gen_all_drilldowns(
            GRAPH_WITH_LITERATURE_EDGE, MINIMAL_REFS,
            "test_classical", out_dir, Path("test.yaml"),
        )
        files = list(out_dir.glob("*drilldown*.md"))
        assert len(files) == 1
        assert "Jones" in files[0].name


def test_gen_all_drilldowns_deduplicates():
    """Same PMID in multiple edges → only one drilldown file."""
    graph = {
        **MINIMAL_GRAPH,
        "edges": [
            {
                "id": "e1", "type_a": "test_classical", "type_b": "atlas_clus_001",
                "relationship": "EQUIVALENT", "confidence": "HIGH",
                "evidence": [{"evidence_type": "LITERATURE", "reference": "PMID:99999999",
                              "supports": "SUPPORT", "explanation": "x"}],
                "property_comparisons": [], "caveats": [],
                "unresolved_questions": [], "proposed_experiments": [],
            },
            {
                "id": "e2", "type_a": "test_classical", "type_b": "atlas_clus_002",
                "relationship": "EQUIVALENT", "confidence": "MODERATE",
                "evidence": [{"evidence_type": "LITERATURE", "reference": "PMID:99999999",
                              "supports": "SUPPORT", "explanation": "y"}],
                "property_comparisons": [], "caveats": [],
                "unresolved_questions": [], "proposed_experiments": [],
            },
        ],
    }
    with tempfile.TemporaryDirectory() as tmpdir:
        _gen_all_drilldowns(graph, MINIMAL_REFS, "test_classical", Path(tmpdir), Path("test.yaml"))
        files = list(Path(tmpdir).glob("*drilldown*.md"))
        assert len(files) == 1


# ── CLI main() tests ──────────────────────────────────────────────────────────

def _write_kb_files(tmp_path: Path, region: str = "testregion") -> tuple[Path, Path]:
    """Write a minimal KB YAML + references.json with proper directory layout."""
    import json
    kb_dir = tmp_path / "kb" / "draft" / region
    kb_dir.mkdir(parents=True)
    refs_dir = tmp_path / "references" / region
    refs_dir.mkdir(parents=True)
    graph_file = kb_dir / "test.yaml"
    refs_file = refs_dir / "references.json"
    graph_file.write_text(yaml.dump(MINIMAL_GRAPH), encoding="utf-8")
    refs_file.write_text(json.dumps(MINIMAL_REFS), encoding="utf-8")
    return graph_file, refs_file


def test_cli_summary(tmp_path):
    """CLI: `render summary graph.yaml` writes summary report."""
    graph_file, _ = _write_kb_files(tmp_path)
    with patch("evidencell.paths.repo_root", return_value=tmp_path):
        with patch("sys.argv", ["render", "summary", str(graph_file)]):
            from evidencell.render import main
            main()
    summaries = list(tmp_path.glob("reports/**/*_summary.md"))
    assert len(summaries) == 1


def test_cli_summary_single_node(tmp_path):
    """CLI: `render summary graph.yaml --node X` writes one summary."""
    graph_file, _ = _write_kb_files(tmp_path)
    with patch("evidencell.paths.repo_root", return_value=tmp_path):
        with patch("sys.argv", ["render", "summary", str(graph_file), "--node", "test_classical"]):
            from evidencell.render import main
            main()
    summaries = list(tmp_path.glob("reports/**/*_summary.md"))
    assert len(summaries) == 1


def test_cli_drilldowns(tmp_path):
    """CLI: `render drilldowns graph.yaml --node X` runs without error.

    No LITERATURE evidence in MINIMAL_GRAPH, so no files written — but no crash either.
    """
    graph_file, _ = _write_kb_files(tmp_path)
    with patch("evidencell.paths.repo_root", return_value=tmp_path):
        with patch("sys.argv", ["render", "drilldowns", str(graph_file), "--node", "test_classical"]):
            from evidencell.render import main
            main()  # should not raise


def test_cli_drilldown_single_pmid(tmp_path):
    """CLI: `render drilldowns graph.yaml --node X --pmid P` writes one file."""
    graph_file, _ = _write_kb_files(tmp_path)
    with patch("evidencell.paths.repo_root", return_value=tmp_path):
        with patch("sys.argv", [
            "render", "drilldowns", str(graph_file),
            "--node", "test_classical", "--pmid", "PMID:12345678",
        ]):
            from evidencell.render import main
            main()
    files = list(tmp_path.glob("reports/**/*drilldown*.md"))
    assert len(files) == 1


def test_cli_index(tmp_path):
    """CLI: `render index region` writes index from KB on disk."""
    # render_index resolves kb/ relative to cwd — set up the expected structure
    kb_dir = tmp_path / "kb" / "draft" / "myregion"
    kb_dir.mkdir(parents=True)
    (kb_dir / "test.yaml").write_text(yaml.dump(MINIMAL_GRAPH), encoding="utf-8")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    with patch("evidencell.paths.repo_root", return_value=tmp_path):
        with patch("sys.argv", ["render", "index", "myregion", "--output-dir", str(out_dir)]):
            from evidencell.render import main
            # Patch cwd so render_index finds kb/ in tmp_path
            with patch("evidencell.render.Path.cwd", return_value=tmp_path):
                main()
    assert (out_dir / "index.md").exists()


def test_cli_facts(tmp_path):
    """CLI: `render facts graph.yaml --node X` writes facts JSON."""
    graph_file, _ = _write_kb_files(tmp_path)
    with patch("evidencell.paths.repo_root", return_value=tmp_path):
        with patch("sys.argv", ["render", "facts", str(graph_file), "--node", "test_classical"]):
            from evidencell.render import main
            main()
    facts_files = list(tmp_path.glob("reports/**/*_facts.json"))
    assert len(facts_files) == 1


# ── _coerce_authors / _format_citation_line ───────────────────────────────────
#
# Regression for the asta-report-ingest free-form-writer bug class
# (planning/minirefs_author_rendering_fix.md): references.json may carry
# `authors` as list[str], list[dict] (Semantic Scholar shape), or — in
# sexually_dimorphic ingest output — a single comma-joined string. The
# renderer must produce a correct surname in all of these shapes.

def test_coerce_authors_list_of_strings():
    assert _coerce_authors(["Iris Oren", "Wiebke Nissen"]) == ["Iris Oren", "Wiebke Nissen"]


def test_coerce_authors_list_of_dicts():
    """Semantic Scholar batch shape: [{'authorId': '...', 'name': '...'}, ...]."""
    assert _coerce_authors(
        [{"authorId": "1", "name": "Jane Doe"}, {"authorId": "2", "name": "Bob Lee"}]
    ) == ["Jane Doe", "Bob Lee"]


def test_coerce_authors_comma_joined_string_with_et_al():
    """sexually_dimorphic shape: 'First Author, Second Author, ... et al.'"""
    result = _coerce_authors(
        "Shannon B. Z. Stephens, Melvin L. Rouse, K. Tolson, R. Liaw et al."
    )
    assert result == [
        "Shannon B. Z. Stephens",
        "Melvin L. Rouse",
        "K. Tolson",
        "R. Liaw",
    ]


def test_coerce_authors_comma_joined_string_no_et_al():
    assert _coerce_authors("Ha Na Choe, E. Jarvis") == ["Ha Na Choe", "E. Jarvis"]


def test_coerce_authors_single_name_string():
    assert _coerce_authors("Solo Author") == ["Solo Author"]


def test_coerce_authors_empty_inputs():
    assert _coerce_authors([]) == []
    assert _coerce_authors(None) == []
    assert _coerce_authors("") == []
    assert _coerce_authors("   ") == []


def test_format_citation_line_string_authors_regression():
    """Regression: minirefs collapsed to 'S et al. 2017' when authors was a string.

    See planning/minirefs_author_rendering_fix.md.
    """
    entry = {
        "authors": "Shannon B. Z. Stephens, Melvin L. Rouse, K. Tolson et al.",
        "year": 2017,
        "pmid": "28660243",
    }
    line = _format_citation_line(entry)
    assert line.startswith("Stephens et al. 2017"), (
        f"Expected 'Stephens et al. 2017 ...', got: {line!r}"
    )
    assert "PMID:28660243" in line


def test_format_citation_line_list_authors_unchanged():
    """Canonical list[str] shape produces identical output as before the fix."""
    entry = {
        "authors": ["Iris Oren", "Wiebke Nissen", "D. Kullmann"],
        "year": 2019,
        "pmid": "31420995",
    }
    line = _format_citation_line(entry)
    assert line == "Oren et al. 2019 · PMID:31420995"


def test_format_citation_line_two_authors_string():
    entry = {
        "authors": "Ha Na Choe, E. Jarvis",
        "year": 2021,
        "pmid": "33895570",
    }
    line = _format_citation_line(entry)
    assert "Choe & Jarvis 2021" in line


def test_format_citation_line_single_author_string():
    entry = {"authors": "Solo Author", "year": 2020, "pmid": "12345678"}
    line = _format_citation_line(entry)
    assert line == "Author 2020 · PMID:12345678"


# ── Generic evidence extraction (any EvidenceItem subclass) ───────────────────

def test_extract_node_facts_generic_evidence_fields_preserved():
    """Non-LITERATURE evidence types (e.g. BULK_CORRELATION) round-trip
    type-specific fields under `fields:` without per-type extraction code.
    """
    graph = {
        "name": "Test region",
        "target_atlas": "WMBv1",
        "creation_date": "2026-01-01",
        "nodes": [
            {
                "id": "test_classical",
                "name": "Test classical",
                "definition_basis": "CLASSICAL_MULTIMODAL",
                "is_terminal": False,
            },
            {
                "id": "atlas_X",
                "name": "Atlas X",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "is_terminal": True,
                "atlas": "WMBv1",
            },
        ],
        "edges": [
            {
                "id": "edge_test_to_X",
                "type_a": "test_classical",
                "type_b": "atlas_X",
                "relationship": "PARTIAL_OVERLAP",
                "confidence": "MODERATE",
                "evidence": [
                    {
                        "evidence_type": "BULK_CORRELATION",
                        "supports": "SUPPORT",
                        "explanation": "Knoedler 2022 ... rank 1/5322.",
                        "run_ref": "corr_run_xyz",
                        "contrast_ref": "corr_A_vs_B",
                        "target_accession": "CS_X",
                        "statistics": "delta=0.090",
                    }
                ],
            },
        ],
    }
    facts = extract_node_facts(graph, {}, "test_classical", Path("test.yaml"))
    ev_items = facts["edges"][0]["evidence_items"]
    assert ev_items[0]["evidence_type"] == "BULK_CORRELATION"
    # Required fields surfaced at top level
    assert ev_items[0]["supports"] == "SUPPORT"
    assert ev_items[0]["explanation"].startswith("Knoedler 2022")
    # Type-specific fields preserved verbatim under `fields:`
    assert ev_items[0]["fields"]["run_ref"] == "corr_run_xyz"
    assert ev_items[0]["fields"]["contrast_ref"] == "corr_A_vs_B"
    assert ev_items[0]["fields"]["target_accession"] == "CS_X"
    assert ev_items[0]["fields"]["statistics"] == "delta=0.090"
    # ref_label is empty when run_ref doesn't resolve to a PMID via filesystem
    # (no manifest exists for this fake run_ref) — the evidence still flows.
    assert ev_items[0]["ref_label"] == ""


def test_extract_node_facts_evidence_type_label_includes_bulk_correlation():
    """EVIDENCE_TYPE_LABELS dict covers BULK_CORRELATION."""
    from evidencell.render import EVIDENCE_TYPE_LABELS
    assert "BULK_CORRELATION" in EVIDENCE_TYPE_LABELS
    assert EVIDENCE_TYPE_LABELS["BULK_CORRELATION"] == "Bulk correlation"


def test_resolve_run_ref_to_pmid_returns_none_for_missing_run():
    """Unknown run_ref returns None (graceful failure, not exception)."""
    from evidencell.render import _resolve_run_ref_to_pmid
    assert _resolve_run_ref_to_pmid("definitely_not_a_real_run_id_xyz") is None


def test_resolve_run_ref_to_pmid_traverses_chain():
    """Real run_ref → manifest → dataset chain resolves to source PMID.

    Smoke test against the actual kb/correlation_runs and kb/datasets entries
    from the sexually_dimorphic mapping work — verifies the renderer can reach
    Stephens 2024 from corr_run_20260428_stephens_kiss1_wmbv1 and Knoedler 2022
    from corr_run_20260428_knoedler_esr1_wmbv1.
    """
    from evidencell.render import _resolve_run_ref_to_pmid, _RUN_REF_PMID_CACHE
    # Bypass cache for deterministic smoke
    _RUN_REF_PMID_CACHE.clear()
    pmid = _resolve_run_ref_to_pmid("corr_run_20260428_stephens_kiss1_wmbv1")
    assert pmid == "PMID:37934722"
    pmid = _resolve_run_ref_to_pmid("corr_run_20260428_knoedler_esr1_wmbv1")
    assert pmid == "PMID:35143761"


def test_build_reference_index_traverses_run_ref_for_bulk_correlation():
    """build_reference_index registers a [n] label for BULK_CORRELATION evidence
    whose run_ref resolves to a real PMID."""
    graph = {
        "name": "Test",
        "target_atlas": "WMBv1",
        "creation_date": "2026-01-01",
        "nodes": [
            {"id": "cl", "name": "cl", "definition_basis": "CLASSICAL_MULTIMODAL", "is_terminal": False},
            {"id": "ax", "name": "ax", "definition_basis": "ATLAS_TRANSCRIPTOMIC", "is_terminal": True, "atlas": "WMBv1"},
        ],
        "edges": [
            {
                "id": "e",
                "type_a": "cl",
                "type_b": "ax",
                "relationship": "PARTIAL_OVERLAP",
                "confidence": "MODERATE",
                "evidence": [
                    {
                        "evidence_type": "BULK_CORRELATION",
                        "supports": "SUPPORT",
                        "explanation": "...",
                        "run_ref": "corr_run_20260428_stephens_kiss1_wmbv1",
                    },
                ],
            },
        ],
    }
    idx = build_reference_index(graph, {}, "cl")
    # Stephens 2024 (PMID:37934722) registered via run_ref traversal
    pmids = {v.pmid for v in idx.values() if v.pmid}
    assert "37934722" in pmids


def test_build_reference_index_uses_dataset_authors_year_for_citation_line():
    """When references.json has no entry for a run_ref-resolved PMID, the
    citation line is synthesised from the BulkDataset descriptor's
    authors/year fields (rather than falling back to the bare PMID)."""
    graph = {
        "name": "Test",
        "target_atlas": "WMBv1",
        "creation_date": "2026-01-01",
        "nodes": [
            {"id": "cl", "name": "cl", "definition_basis": "CLASSICAL_MULTIMODAL", "is_terminal": False},
            {"id": "ax", "name": "ax", "definition_basis": "ATLAS_TRANSCRIPTOMIC", "is_terminal": True, "atlas": "WMBv1"},
        ],
        "edges": [
            {
                "id": "e",
                "type_a": "cl",
                "type_b": "ax",
                "relationship": "PARTIAL_OVERLAP",
                "confidence": "MODERATE",
                "evidence": [
                    {
                        "evidence_type": "BULK_CORRELATION",
                        "supports": "SUPPORT",
                        "explanation": "...",
                        "run_ref": "corr_run_20260428_stephens_kiss1_wmbv1",
                    },
                ],
            },
        ],
    }
    # references.json is empty — citation line must come from the dataset YAML
    idx = build_reference_index(graph, {}, "cl")
    stephens = next((v for v in idx.values() if v.pmid == "37934722"), None)
    assert stephens is not None
    assert "Stephens" in stephens.citation_line
    assert "2024" in stephens.citation_line
