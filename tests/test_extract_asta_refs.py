"""Unit tests for evidencell.extract_asta_refs and evidencell.show_node."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from evidencell.extract_asta_refs import parse_snippet_response
from evidencell.show_node import node_context


# ── Fixtures ──────────────────────────────────────────────────────────────────

def _make_response(papers: list[dict]) -> dict:
    """Wrap paper dicts in the standard Semantic Scholar snippet_search shape."""
    return {"data": papers}


def _paper(corpus_id: int, title: str, snippets: list[dict]) -> dict:
    return {"corpusId": corpus_id, "title": title, "snippets": snippets}


def _snippet(text: str, section_title: str = "") -> dict:
    snip: dict = {"text": text, "snippetKind": "passage"}
    if section_title:
        snip["section"] = {"title": section_title}
    return snip


# ── parse_snippet_response: basic cases ───────────────────────────────────────

def test_empty_response():
    result = parse_snippet_response({})
    assert result["total_snippets"] == 0
    assert result["candidate_refs"] == []
    assert result["source_papers"] == []


def test_empty_data_list():
    result = parse_snippet_response({"data": []})
    assert result["total_snippets"] == 0
    assert result["source_papers"] == []


def test_single_paper_with_snippets():
    data = _make_response([
        _paper(111, "Cerebellar interneuron study",
               [_snippet("Candelabrum cells are located in the Purkinje layer."),
                _snippet("These cells express GABA.")])
    ])
    result = parse_snippet_response(data)
    assert result["total_snippets"] == 2
    assert len(result["source_papers"]) == 1
    assert result["source_papers"][0]["corpus_id"] == "111"
    assert result["source_papers"][0]["snippet_count"] == 2


def test_section_titles_captured():
    data = _make_response([
        _paper(222, "MLI paper", [
            _snippet("Results text.", section_title="Results"),
            _snippet("Methods text.", section_title="Methods"),
        ])
    ])
    result = parse_snippet_response(data)
    sections = result["source_papers"][0]["sections_seen"]
    assert "Results" in sections
    assert "Methods" in sections


def test_section_unknown_when_absent():
    data = _make_response([_paper(333, "No section", [_snippet("Some text.")])])
    result = parse_snippet_response(data)
    assert result["source_papers"][0]["sections_seen"] == ["unknown"]


def test_multiple_papers():
    data = _make_response([
        _paper(10, "Paper A", [_snippet("text A")]),
        _paper(20, "Paper B", [_snippet("text B"), _snippet("text B2")]),
    ])
    result = parse_snippet_response(data)
    assert result["total_snippets"] == 3
    assert len(result["source_papers"]) == 2
    ids = {p["corpus_id"] for p in result["source_papers"]}
    assert ids == {"10", "20"}


# ── gap_papers ────────────────────────────────────────────────────────────────

def test_gap_papers_identified():
    data = _make_response([_paper(10, "Paper A", [_snippet("text")])])
    result = parse_snippet_response(data, queried_ids=["10", "99", "100"])
    assert "99" in result["gap_papers"]
    assert "100" in result["gap_papers"]
    assert "10" not in result["gap_papers"]


def test_no_queried_ids_no_gaps():
    data = _make_response([_paper(10, "Paper A", [_snippet("text")])])
    result = parse_snippet_response(data, queried_ids=None)
    assert result["gap_papers"] == []


def test_all_queried_are_gaps():
    result = parse_snippet_response({"data": []}, queried_ids=["55", "66"])
    assert set(result["gap_papers"]) == {"55", "66"}


# ── candidate_refs ────────────────────────────────────────────────────────────

def test_source_paper_appears_in_candidates():
    data = _make_response([_paper(42, "Some paper", [_snippet("text")])])
    result = parse_snippet_response(data)
    cids = [c["corpus_id"] for c in result["candidate_refs"]]
    assert "42" in cids


def test_nested_corpus_id_in_snippet_captured():
    """Corpus IDs embedded inside snippet dicts (e.g. cited papers) are extracted."""
    snippet_with_ref = {
        "text": "See [1]",
        "references": [{"corpusId": 999, "title": "Cited paper"}],
    }
    data = _make_response([_paper(1, "Source", [snippet_with_ref])])
    result = parse_snippet_response(data)
    cids = [c["corpus_id"] for c in result["candidate_refs"]]
    assert "999" in cids
    assert "1" in cids


def test_deduplication_of_candidates():
    """Same corpus ID appearing in multiple papers is deduplicated."""
    data = _make_response([
        _paper(1, "Paper 1", [{"text": "t", "references": [{"corpusId": 50}]}]),
        _paper(2, "Paper 2", [{"text": "t", "references": [{"corpusId": 50}]}]),
    ])
    result = parse_snippet_response(data)
    cids = [c["corpus_id"] for c in result["candidate_refs"]]
    assert cids.count("50") == 1


# ── CLI (main) ────────────────────────────────────────────────────────────────

def test_cli_parses_valid_json():
    payload = json.dumps(_make_response([_paper(77, "Test", [_snippet("hi")])]))
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.extract_asta_refs", "--pretty"],
        input=payload, capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 0
    out = json.loads(result.stdout)
    assert out["total_snippets"] == 1
    assert "77" in [c["corpus_id"] for c in out["candidate_refs"]]


def test_cli_handles_empty_input():
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.extract_asta_refs"],
        input="", capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 1
    out = json.loads(result.stdout)
    assert "error" in out


def test_cli_handles_bad_json():
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.extract_asta_refs"],
        input="{not valid json", capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 1
    out = json.loads(result.stdout)
    assert "error" in out


def test_cli_queried_ids_flag():
    payload = json.dumps(_make_response([_paper(10, "Paper", [_snippet("t")])]))
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.extract_asta_refs",
         "--queried-ids", "10,99", "--pretty"],
        input=payload, capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 0
    out = json.loads(result.stdout)
    assert "99" in out["gap_papers"]
    assert "10" not in out["gap_papers"]


# ── show_node ─────────────────────────────────────────────────────────────────

@pytest.fixture
def kb_file(tmp_path: Path) -> Path:
    doc = {
        "nodes": [
            {
                "id": "test_node",
                "name": "Test Neuron",
                "defining_markers": [{"symbol": "PVALB"}, {"symbol": "SST"}],
                "anatomical_location": [{"label": "Cerebellar cortex"}],
                "nt_type": {"name_in_source": "GABA"},
            }
        ]
    }
    f = tmp_path / "test.yaml"
    f.write_text(yaml.dump(doc))
    return f


def test_node_context_basic(kb_file: Path):
    ctx = node_context(kb_file, "test_node")
    assert "test_node" in ctx
    assert "Test Neuron" in ctx
    assert "PVALB" in ctx
    assert "SST" in ctx
    assert "Cerebellar cortex" in ctx
    assert "GABA" in ctx


def test_node_context_missing_markers(tmp_path: Path):
    doc = {"nodes": [{"id": "bare", "name": "Bare Node"}]}
    f = tmp_path / "bare.yaml"
    f.write_text(yaml.dump(doc))
    ctx = node_context(f, "bare")
    assert "not yet characterised" in ctx
    assert "unknown" in ctx


def test_node_context_missing_node(kb_file: Path):
    with pytest.raises(ValueError, match="not found"):
        node_context(kb_file, "nonexistent_id")


def test_show_node_cli(kb_file: Path):
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.show_node", str(kb_file), "test_node"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 0
    assert "Test Neuron" in result.stdout
    assert "PVALB" in result.stdout


def test_show_node_cli_missing_node(kb_file: Path):
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.show_node", str(kb_file), "bad_id"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 1


def test_show_node_cli_wrong_args():
    result = subprocess.run(
        [sys.executable, "-m", "evidencell.show_node"],
        capture_output=True, text=True,
        cwd=Path(__file__).parent.parent,
    )
    assert result.returncode == 1
