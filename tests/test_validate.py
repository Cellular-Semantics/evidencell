"""Unit tests for evidencell.validate structural checks and edit simulation."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from evidencell.validate import (
    PLACEHOLDER_SNIPPETS,
    _collect_quote_keys,
    _collect_refs,
    check_md_ids,
    check_quote_keys,
    check_ref_pmids,
    linkml_validate,
    parse_md_annotations,
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


# ── Provenance check fixtures ─────────────────────────────────────────────────


@pytest.fixture()
def refs_file(tmp_path: Path) -> Path:
    refs = {
        "201041756": {
            "corpus_id": "201041756",
            "pmid": "31420995",
            "doi": "10.1111/ejn.14606",
            "authors": ["Winterer J"],
            "year": 2019,
            "title": "OLM interneurons",
            "journal": "Eur J Neurosci",
            "quotes": {
                "201041756_aabb1234": {
                    "text": "OLM cells express Sst and Chrna2.",
                    "section": "Results 3.3",
                    "claims": ["sst_positive"],
                },
                "201041756_ccdd5678": {
                    "text": "Npy is consistently expressed.",
                    "section": "Results 3.5",
                    "claims": ["npy_positive"],
                },
            },
        },
        "987654": {
            "corpus_id": "987654",
            "pmid": "12345678",
            "doi": "10.1234/fake.2020.001",
            "quotes": {},
        },
    }
    p = tmp_path / "references.json"
    p.write_text(json.dumps(refs))
    return p


# ── _collect_quote_keys ───────────────────────────────────────────────────────


def test_collect_quote_keys_nested():
    doc = {
        "nodes": [
            {"defining_markers": [{"sources": [{"quote_key": "abc_11223344"}]}]}
        ],
        "edges": [{"evidence": [{"quote_key": "def_aabbccdd"}, {"corpus_id": "xyz"}]}],
    }
    keys = _collect_quote_keys(doc)
    assert keys == ["abc_11223344", "def_aabbccdd"]


def test_collect_quote_keys_empty():
    assert _collect_quote_keys({}) == []
    assert _collect_quote_keys({"nodes": []}) == []


# ── check_quote_keys ──────────────────────────────────────────────────────────


def test_check_quote_keys_valid(refs_file: Path):
    doc = {"nodes": [{"sources": [{"quote_key": "201041756_aabb1234"}]}]}
    assert check_quote_keys(doc, refs_file) == []


def test_check_quote_keys_missing(refs_file: Path):
    doc = {"nodes": [{"sources": [{"quote_key": "INVENTED_KEY_deadbeef"}]}]}
    errors = check_quote_keys(doc, refs_file)
    assert len(errors) == 1
    assert "INVENTED_KEY_deadbeef" in errors[0]


def test_check_quote_keys_no_refs_file(tmp_path: Path):
    """Silently skip if references.json is absent (fresh graph)."""
    doc = {"nodes": [{"sources": [{"quote_key": "anything_aaaabbbb"}]}]}
    assert check_quote_keys(doc, tmp_path / "references.json") == []


def test_check_quote_keys_reports_all_missing(refs_file: Path):
    doc = {"x": {"quote_key": "bad_00000001"}, "y": {"quote_key": "bad_00000002"}}
    errors = check_quote_keys(doc, refs_file)
    assert len(errors) == 2


# ── _collect_refs ─────────────────────────────────────────────────────────────


def test_collect_refs_basic():
    doc = {
        "defining_markers": [{"sources": [{"ref": "PMID:31420995"}]}],
        "neuropeptides": [{"sources": [{"ref": "DOI:10.1234/x"}]}],
    }
    refs = _collect_refs(doc)
    assert "PMID:31420995" in refs
    assert "DOI:10.1234/x" in refs


def test_collect_refs_ignores_non_ref_keys():
    doc = {"reference": "not a ref field", "ref": "PMID:99999999"}
    assert _collect_refs(doc) == ["PMID:99999999"]


# ── check_ref_pmids ───────────────────────────────────────────────────────────


def test_check_ref_pmids_valid_pmid(refs_file: Path):
    doc = {"sources": [{"ref": "PMID:31420995"}]}
    assert check_ref_pmids(doc, refs_file) == []


def test_check_ref_pmids_valid_doi(refs_file: Path):
    doc = {"sources": [{"ref": "DOI:10.1111/ejn.14606"}]}
    assert check_ref_pmids(doc, refs_file) == []


def test_check_ref_pmids_hallucinated_pmid(refs_file: Path):
    doc = {"sources": [{"ref": "PMID:00000001"}]}
    errors = check_ref_pmids(doc, refs_file)
    assert len(errors) == 1
    assert "PMID:00000001" in errors[0]


def test_check_ref_pmids_hallucinated_doi(refs_file: Path):
    doc = {"sources": [{"ref": "DOI:10.9999/invented.2099.0001"}]}
    assert len(check_ref_pmids(doc, refs_file)) == 1


def test_check_ref_pmids_non_pmid_ref_ignored(refs_file: Path):
    """corpus_id-style refs (no PMID:/DOI: prefix) are not checked."""
    doc = {"sources": [{"ref": "corpus:abc123"}]}
    assert check_ref_pmids(doc, refs_file) == []


def test_check_ref_pmids_no_refs_file(tmp_path: Path):
    doc = {"sources": [{"ref": "PMID:99999999"}]}
    assert check_ref_pmids(doc, tmp_path / "references.json") == []


# ── parse_md_annotations ───────────────────────────────────────────────────────


_SAMPLE_MD = """\
# OLM Interneurons

Some intro text with an ontology term: CA1 stratum oriens [UBERON:0014548].

> OLM cells express Sst and Chrna2.
> — Winterer et al. 2019, Results §3.3 · [1] <!-- quote_key: 201041756_aabb1234 -->

A bare blockquote without annotation:

> This line has no quote_key.

Cluster mapping: 0769 Sst Gaba_3 [CS20230722_CLUS_0769]

## References

1. [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) Winterer et al. 2019
"""


def test_parse_md_quote_key_extracted():
    result = parse_md_annotations(_SAMPLE_MD)
    assert "201041756_aabb1234" in result["quote_keys"]


def test_parse_md_unannotated_blockquote_flagged():
    result = parse_md_annotations(_SAMPLE_MD)
    assert any("no quote_key" in line or "This line" in line
               for line in result["unannotated_blockquotes"])


def test_parse_md_attribution_line_not_flagged():
    """The '> — Author...' attribution line must NOT appear in unannotated_blockquotes."""
    result = parse_md_annotations(_SAMPLE_MD)
    for line in result["unannotated_blockquotes"]:
        assert "Winterer" not in line


def test_parse_md_curie_ids_extracted():
    result = parse_md_annotations(_SAMPLE_MD)
    assert "UBERON:0014548" in result["curie_ids"]


def test_parse_md_accession_extracted():
    result = parse_md_annotations(_SAMPLE_MD)
    assert "CS20230722_CLUS_0769" in result["accessions"]


def test_parse_md_pmid_from_reference_table():
    result = parse_md_annotations(_SAMPLE_MD)
    assert "31420995" in result["pmids"]


def test_parse_md_empty_document():
    result = parse_md_annotations("")
    assert result["quote_keys"] == []
    assert result["unannotated_blockquotes"] == []
    assert result["curie_ids"] == []
    assert result["accessions"] == []
    assert result["pmids"] == []


# ── check_md_ids ───────────────────────────────────────────────────────────────


def test_check_md_unannotated_blockquote_is_error():
    annotations = {
        "quote_keys": [],
        "unannotated_blockquotes": ["> This line has no key."],
        "curie_ids": [],
        "accessions": [],
        "pmids": [],
    }
    errors = check_md_ids(annotations, Path("/nonexistent/references.json"))
    assert len(errors) == 1
    assert "Unannotated blockquote" in errors[0]


def test_check_md_missing_quote_key(refs_file: Path):
    annotations = {
        "quote_keys": ["INVENTED_KEY_deadbeef"],
        "unannotated_blockquotes": [],
        "curie_ids": [],
        "accessions": [],
        "pmids": [],
    }
    errors = check_md_ids(annotations, refs_file)
    assert any("INVENTED_KEY_deadbeef" in e for e in errors)


def test_check_md_valid_quote_key(refs_file: Path):
    annotations = {
        "quote_keys": ["201041756_aabb1234"],
        "unannotated_blockquotes": [],
        "curie_ids": [],
        "accessions": [],
        "pmids": [],
    }
    assert check_md_ids(annotations, refs_file) == []


def test_check_md_hallucinated_pmid(refs_file: Path):
    annotations = {
        "quote_keys": [],
        "unannotated_blockquotes": [],
        "curie_ids": [],
        "accessions": [],
        "pmids": ["00000001"],
    }
    errors = check_md_ids(annotations, refs_file)
    assert any("00000001" in e for e in errors)


def test_check_md_valid_pmid(refs_file: Path):
    annotations = {
        "quote_keys": [],
        "unannotated_blockquotes": [],
        "curie_ids": [],
        "accessions": [],
        "pmids": ["31420995"],
    }
    assert check_md_ids(annotations, refs_file) == []


def test_check_md_unknown_accession():
    annotations = {
        "quote_keys": [],
        "unannotated_blockquotes": [],
        "curie_ids": [],
        "accessions": ["CS99999999_FAKE"],
        "pmids": [],
    }
    kb_nodes = {"CS20230722_CLUS_0769": {}}
    errors = check_md_ids(annotations, Path("/nonexistent/references.json"), kb_nodes=kb_nodes)
    assert any("CS99999999_FAKE" in e for e in errors)


def test_check_md_no_caches_no_errors():
    """When refs file absent and no kb_nodes, all checks skip silently."""
    annotations = {
        "quote_keys": ["some_key_abc12345"],
        "unannotated_blockquotes": [],
        "curie_ids": ["UBERON:0014548"],
        "accessions": ["CS20230722_CLUS_0001"],
        "pmids": ["31420995"],
    }
    errors = check_md_ids(annotations, Path("/nonexistent/references.json"), kb_nodes=None)
    assert errors == []
