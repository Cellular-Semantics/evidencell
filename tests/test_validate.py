"""Unit tests for evidencell.validate structural checks and edit simulation."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from evidencell.validate import (
    PLACEHOLDER_SNIPPETS,
    linkml_validate,
    simulate_edit,
    structural_checks,
)


# ── Helpers ────────────────────────────────────────────────────────────────────

def _node(id: str, is_terminal: bool = False, cell_set_accession: str | None = None) -> dict:
    n = {"id": id, "name": f"Name for {id}"}
    if is_terminal:
        n["is_terminal"] = True
    if cell_set_accession:
        n["cell_set_accession"] = cell_set_accession
    return n


def _edge(id: str, type_a: str, type_b: str, evidence: list | None = None) -> dict:
    return {
        "id": id,
        "type_a": type_a,
        "type_b": type_b,
        "evidence": evidence if evidence is not None else [{"snippet": "Real verbatim text."}],
    }


def _lit_evidence(snippet: str) -> dict:
    return {"corpus_id": "12345", "snippet": snippet}


# ── structural_checks: clean graph ────────────────────────────────────────────

def test_clean_graph_returns_no_errors():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B")],
    }
    assert structural_checks(doc) == []


def test_empty_nodes_and_edges():
    assert structural_checks({"nodes": [], "edges": []}) == []


def test_no_nodes_or_edges_key():
    assert structural_checks({}) == []


# ── Duplicate node IDs ────────────────────────────────────────────────────────

def test_duplicate_node_id():
    doc = {
        "nodes": [_node("A"), _node("A")],
        "edges": [],
    }
    errors = structural_checks(doc)
    assert len(errors) == 1
    assert "Duplicate node id" in errors[0]
    assert "'A'" in errors[0]


# ── Edge endpoint references ──────────────────────────────────────────────────

def test_edge_type_a_missing_node():
    doc = {
        "nodes": [_node("B")],
        "edges": [_edge("e1", "NONEXISTENT", "B")],
    }
    errors = structural_checks(doc)
    assert any("type_a" in e and "NONEXISTENT" in e for e in errors)


def test_edge_type_b_missing_node():
    doc = {
        "nodes": [_node("A")],
        "edges": [_edge("e1", "A", "NONEXISTENT")],
    }
    errors = structural_checks(doc)
    assert any("type_b" in e and "NONEXISTENT" in e for e in errors)


def test_edge_both_endpoints_valid():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B")],
    }
    assert structural_checks(doc) == []


# ── Evidence list ─────────────────────────────────────────────────────────────

def test_edge_missing_evidence_key():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [{"id": "e1", "type_a": "A", "type_b": "B"}],
    }
    errors = structural_checks(doc)
    assert any("evidence" in e for e in errors)


def test_edge_empty_evidence_list():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [{"id": "e1", "type_a": "A", "type_b": "B", "evidence": []}],
    }
    errors = structural_checks(doc)
    assert any("non-empty list" in e for e in errors)


def test_edge_null_evidence():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [{"id": "e1", "type_a": "A", "type_b": "B", "evidence": None}],
    }
    errors = structural_checks(doc)
    assert any("non-empty list" in e for e in errors)


# ── Snippet quality ───────────────────────────────────────────────────────────

def test_empty_snippet_blocked():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=[_lit_evidence("")])],
    }
    errors = structural_checks(doc)
    assert any("empty" in e and "snippet" in e for e in errors)


def test_whitespace_only_snippet_blocked():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=[_lit_evidence("   ")])],
    }
    errors = structural_checks(doc)
    assert any("empty" in e and "snippet" in e for e in errors)


# PLACEHOLDER_SNIPPETS currently blocks: TODO, ADD SNIPPET, PLACEHOLDER, TBD, ..., FIXME
# Strings NOT yet blocked (known gaps — add to PLACEHOLDER_SNIPPETS if they appear in practice):
#   "WIP", "STUB", "XXX", "CITATION_NEEDED", "N/A", "FILL IN"
# Rationale: keep the set tight to avoid false positives; expand on regression.
@pytest.mark.parametrize("placeholder", list(PLACEHOLDER_SNIPPETS))
def test_placeholder_snippets_blocked(placeholder: str):
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=[_lit_evidence(placeholder)])],
    }
    errors = structural_checks(doc)
    assert any("placeholder" in e.lower() for e in errors)


def test_todo_prefix_blocked():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=[_lit_evidence("TODO: add snippet")])],
    }
    errors = structural_checks(doc)
    assert any("placeholder" in e.lower() for e in errors)


def test_real_snippet_allowed():
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=[_lit_evidence(
            "These cells express parvalbumin and are located in layer IV."
        )])],
    }
    assert structural_checks(doc) == []


def test_non_literature_evidence_no_snippet_ok():
    """Evidence items without a snippet field (e.g. ExpressionEvidence) should not error."""
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=[
            {"marker_gene": "PVALB", "expression_pattern": "HIGH"}
        ])],
    }
    assert structural_checks(doc) == []


# ── Terminal node accession ───────────────────────────────────────────────────

def test_terminal_node_without_accession_errors():
    doc = {
        "nodes": [_node("A", is_terminal=True)],
        "edges": [],
    }
    errors = structural_checks(doc)
    assert any("cell_set_accession" in e for e in errors)


def test_terminal_node_with_accession_ok():
    doc = {
        "nodes": [_node("A", is_terminal=True, cell_set_accession="CS20221014_001")],
        "edges": [],
    }
    assert structural_checks(doc) == []


def test_non_terminal_node_without_accession_ok():
    doc = {
        "nodes": [_node("A", is_terminal=False)],
        "edges": [],
    }
    assert structural_checks(doc) == []


# ── simulate_edit ─────────────────────────────────────────────────────────────

def test_simulate_write(tmp_path: Path):
    f = tmp_path / "test.yaml"
    result = simulate_edit("Write", {"file_path": str(f), "content": "hello: world"}, f)
    assert result == "hello: world"


def test_simulate_edit_replaces_string(tmp_path: Path):
    f = tmp_path / "test.yaml"
    f.write_text("hello: world")
    result = simulate_edit(
        "Edit",
        {"file_path": str(f), "old_string": "world", "new_string": "earth"},
        f,
    )
    assert result == "hello: earth"


def test_simulate_edit_replace_all(tmp_path: Path):
    f = tmp_path / "test.yaml"
    f.write_text("a: 1\na: 2")
    result = simulate_edit(
        "Edit",
        {"file_path": str(f), "old_string": "a:", "new_string": "b:", "replace_all": True},
        f,
    )
    assert result == "b: 1\nb: 2"


def test_simulate_multiedit(tmp_path: Path):
    f = tmp_path / "test.yaml"
    f.write_text("hello: world\nfoo: bar")
    result = simulate_edit(
        "MultiEdit",
        {
            "file_path": str(f),
            "edits": [
                {"old_string": "world", "new_string": "earth"},
                {"old_string": "bar", "new_string": "baz"},
            ],
        },
        f,
    )
    assert result == "hello: earth\nfoo: baz"


def test_simulate_write_on_nonexistent_file(tmp_path: Path):
    f = tmp_path / "new.yaml"
    result = simulate_edit("Write", {"file_path": str(f), "content": "id: x"}, f)
    assert result == "id: x"


# ── Edge cases: node with no id, non-dict evidence ────────────────────────────

def test_node_without_id_field_ignored():
    """Nodes missing the 'id' key should be silently skipped (no crash, no error)."""
    doc = {
        "nodes": [{"name": "Unnamed node"}],  # no 'id' key
        "edges": [],
    }
    assert structural_checks(doc) == []


def test_non_dict_evidence_item_ignored():
    """A non-dict evidence item (e.g. a bare string) must not crash structural_checks."""
    doc = {
        "nodes": [_node("A"), _node("B")],
        "edges": [_edge("e1", "A", "B", evidence=["bare string evidence"])],
    }
    # Should pass — non-dict items are skipped, and the list is non-empty
    assert structural_checks(doc) == []


# ── linkml_validate ────────────────────────────────────────────────────────────


def test_linkml_validate_skips_when_schema_missing(tmp_path: Path):
    """When schema file does not exist, validation is skipped and passes."""
    missing_schema = tmp_path / "nonexistent_schema.yaml"
    ok, msg = linkml_validate("id: x", missing_schema)
    assert ok is True
    assert "schema not found" in msg.lower() or "skipped" in msg.lower()


def test_linkml_validate_returns_true_on_success(tmp_path: Path):
    schema = tmp_path / "schema.yaml"
    schema.write_text("id: fake")  # exists but won't be called — we mock subprocess
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "Validation passed"
    mock_result.stderr = ""
    with patch("evidencell.validate.subprocess.run", return_value=mock_result):
        ok, output = linkml_validate("nodes: []", schema)
    assert ok is True
    assert "Validation passed" in output


def test_linkml_validate_returns_false_on_failure(tmp_path: Path):
    schema = tmp_path / "schema.yaml"
    schema.write_text("id: fake")
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = ""
    mock_result.stderr = "ERROR: missing required field 'id'"
    with patch("evidencell.validate.subprocess.run", return_value=mock_result):
        ok, output = linkml_validate("bad: yaml", schema)
    assert ok is False
    assert "missing required field" in output
