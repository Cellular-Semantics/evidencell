"""Phase 3: rationale-writeback module — verdict block parsing,
anti-hallucination check, KB write-back."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from evidencell import _rationale_hash
from evidencell.rationale_writeback import (
    check_rationale_against_edge,
    parse_verdict_blocks,
    write_back,
)


# ─── Verdict block parsing ──────────────────────────────────────────────────


def test_parse_single_verdict_block():
    report = """# Some report

(...lots of prose...)

## References

(...)

<!-- verdict-block-start: edge_olm_to_x -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  rationale: >
    Reln (F1=0.95 in at_run_x) anchors the close match.
```
<!-- verdict-block-end -->
"""
    out = parse_verdict_blocks(report)
    assert len(out) == 1
    assert out[0]["edge_id"] == "edge_olm_to_x"
    v = out[0]["verdict"]
    assert v["confidence"] == "MODERATE"
    assert v["confidence_score"] == 0.65
    assert "Reln" in v["rationale"]


def test_parse_multiple_verdict_blocks():
    report = """
<!-- verdict-block-start: edge_one -->
```yaml
verdict:
  confidence: HIGH
  rationale: x
```
<!-- verdict-block-end -->

Some intermediate text.

<!-- verdict-block-start: edge_two -->
```yaml
verdict:
  confidence: LOW
  rationale: y
```
<!-- verdict-block-end -->
"""
    out = parse_verdict_blocks(report)
    assert [b["edge_id"] for b in out] == ["edge_one", "edge_two"]


def test_parse_skips_malformed_blocks():
    report = """
<!-- verdict-block-start: edge_bad -->
this is not a yaml fence
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_good -->
```yaml
verdict:
  confidence: MODERATE
  rationale: ok
```
<!-- verdict-block-end -->
"""
    out = parse_verdict_blocks(report)
    assert len(out) == 1
    assert out[0]["edge_id"] == "edge_good"


# ─── Anti-hallucination check ───────────────────────────────────────────────


def _edge_with_at(f1: float = 0.65, acc: str = "CS20230722_SUPT_0216") -> dict:
    return {
        "id": "edge_test",
        "lit_type": "lit_x",
        "taxonomy_type": acc,
        "evidence": [
            {
                "evidence_type": "ANNOTATION_TRANSFER",
                "run_ref": "at_run_test_run",
                "method": "MapMyCells (patch-seq input)",
                "metrics_by_level": [
                    {
                        "taxonomy_level": "SUPERTYPE",
                        "best_target_accession": acc,
                        "f1_score": f1,
                    }
                ],
            }
        ],
        "property_comparisons": [
            {"property": "marker_Sst", "alignment": "CONSISTENT"},
            {"property": "marker_Chrna2", "alignment": "CONSISTENT"},
            {"property": "marker_Pvalb", "alignment": "DISCORDANT"},
        ],
    }


def test_rationale_passes_when_claims_verifiable():
    edge = _edge_with_at(f1=0.65)
    rationale = (
        "AT (patch-seq) supports the call: F1=0.65 to "
        "CS20230722_SUPT_0216 via at_run_test_run; "
        "2 of 3 markers CONSISTENT."
    )
    errs = check_rationale_against_edge(rationale, edge)
    assert errs == []


def test_rationale_fails_on_unverifiable_f1():
    edge = _edge_with_at(f1=0.65)
    rationale = "F1=0.99 supports the call to CS20230722_SUPT_0216."
    errs = check_rationale_against_edge(rationale, edge)
    assert any("F1=0.99" in e for e in errs)


def test_rationale_fails_on_unverifiable_accession():
    edge = _edge_with_at(f1=0.65)
    rationale = "F1=0.65 to CS20230722_CLUS_9999."
    errs = check_rationale_against_edge(rationale, edge)
    assert any("CS20230722_CLUS_9999" in e for e in errs)


def test_rationale_fails_on_wrong_run_ref():
    edge = _edge_with_at()
    rationale = "F1=0.65 via at_run_not_on_this_edge."
    errs = check_rationale_against_edge(rationale, edge)
    assert any("at_run_not_on_this_edge" in e for e in errs)


def test_rationale_fails_on_wrong_marker_count():
    edge = _edge_with_at()
    rationale = "F1=0.65; 3 of 3 markers CONSISTENT."
    errs = check_rationale_against_edge(rationale, edge)
    assert any("markers CONSISTENT" in e for e in errs)


def test_rationale_fails_on_unsupported_modality_claim():
    edge = _edge_with_at()
    # Edge's method mentions 'patch-seq'; rationale claims 'morphology'.
    rationale = "F1=0.65; CS20230722_SUPT_0216 supported by morphology."
    errs = check_rationale_against_edge(rationale, edge)
    assert any("morpholog" in e.lower() for e in errs)


def test_rationale_passes_when_modality_appears_in_property_source_method():
    """PropertySource.method on a property_comparison counts toward
    the modality blob (it's where, e.g., 'immunohistochemistry' is
    typically recorded)."""
    edge = _edge_with_at()
    edge["property_comparisons"][0]["sources"] = [
        {"method": "immunohistochemistry on rat CA1"}
    ]
    rationale = "F1=0.65; marker_Sst supported by immunohistochemistry."
    errs = check_rationale_against_edge(rationale, edge)
    assert errs == []


# ─── Write-back ─────────────────────────────────────────────────────────────


@pytest.fixture
def tiny_graph_files(tmp_path: Path) -> tuple[Path, Path]:
    """Build a minimal KB graph + a report with one verdict block.
    Returns (graph_path, report_path)."""
    graph_path = tmp_path / "graph.yaml"
    graph = {
        "nodes": [
            {
                "id": "lit_x",
                "definition_basis": "CLASSICAL_MULTIMODAL",
                "defining_markers": [{"symbol": "Sst"}],
            },
            {
                "id": "CS20230722_SUPT_0216",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "taxonomy_id": "CCN20230722",
                "cell_set_accession": "CS20230722_SUPT_0216",
            },
        ],
        "edges": [
            {
                "id": "edge_test",
                "lit_type": "lit_x",
                "taxonomy_type": "CS20230722_SUPT_0216",
                "relationship": "skos:closeMatch",
                "mapping_cardinality": "1:1",
                "mapping_justification": "semapv:UnreviewedManualMapping",
                "evidence": [
                    {
                        "evidence_type": "ANNOTATION_TRANSFER",
                        "run_ref": "at_run_test",
                        "method": "MapMyCells",
                        "metrics_by_level": [
                            {
                                "taxonomy_level": "SUPERTYPE",
                                "best_target_accession": "CS20230722_SUPT_0216",
                                "f1_score": 0.65,
                            }
                        ],
                    }
                ],
                "property_comparisons": [
                    {"property": "marker_Sst", "alignment": "CONSISTENT"}
                ],
            }
        ],
    }
    graph_path.write_text(yaml.safe_dump(graph))

    report_path = tmp_path / "report.md"
    report_path.write_text(
        "# Report for lit_x\n"
        "...\n"
        "<!-- verdict-block-start: edge_test -->\n"
        "```yaml\n"
        "verdict:\n"
        "  confidence: MODERATE\n"
        "  confidence_score: 0.65\n"
        "  rationale: >\n"
        "    F1=0.65 to CS20230722_SUPT_0216 via at_run_test;\n"
        "    1 of 1 markers CONSISTENT.\n"
        "```\n"
        "<!-- verdict-block-end -->\n"
    )
    return graph_path, report_path


def test_write_back_dry_run(tiny_graph_files):
    graph_path, report_path = tiny_graph_files
    summary = write_back(report_path, graph_path, dry_run=True, verify=True)
    assert summary["parsed"] == 1
    assert summary["verified"] == 1
    assert summary["errors"] == []
    assert summary["written"] == 1  # counted; not actually persisted

    # Verify the graph YAML was not edited (dry-run).
    doc = yaml.safe_load(graph_path.read_text())
    assert "rationale" not in doc["edges"][0]


def test_write_back_persists_fields(tiny_graph_files):
    graph_path, report_path = tiny_graph_files
    summary = write_back(report_path, graph_path, verify=True)
    assert summary["errors"] == []
    assert summary["written"] == 1

    doc = yaml.safe_load(graph_path.read_text())
    edge = doc["edges"][0]
    assert edge["confidence"] == "MODERATE"
    assert edge["confidence_score"] == 0.65
    assert "F1=0.65" in edge["rationale"]
    assert "rationale_source_hash" in edge
    assert len(edge["rationale_source_hash"]) == 8
    assert "rationale_generated_at" in edge


def test_write_back_blocks_on_verification_failure(tiny_graph_files):
    graph_path, report_path = tiny_graph_files
    # Rewrite report to claim a wrong F1.
    bad_report = report_path.read_text().replace(
        "F1=0.65", "F1=0.99"
    )
    report_path.write_text(bad_report)

    summary = write_back(report_path, graph_path, verify=True)
    assert summary["errors"], "Expected verification to fail on bad F1"
    assert summary["written"] == 0
    doc = yaml.safe_load(graph_path.read_text())
    assert "rationale" not in doc["edges"][0]


def test_writeback_hash_round_trip(tiny_graph_files):
    """After write-back, the stored hash must match `is_stale=False`."""
    graph_path, report_path = tiny_graph_files
    write_back(report_path, graph_path, verify=True)

    doc = yaml.safe_load(graph_path.read_text())
    edge = doc["edges"][0]
    nodes_by_id = {n["id"]: n for n in doc["nodes"]}
    assert not _rationale_hash.is_stale(
        edge,
        nodes_by_id[edge["lit_type"]],
        nodes_by_id[edge["taxonomy_type"]],
    )


def test_writeback_lit_to_lit_edge_creation(tmp_path: Path):
    """When a verdict block carries lit_to_lit_edges, the orchestrator
    creates a new MappingEdge with skos:closeMatch."""
    graph_path = tmp_path / "graph.yaml"
    graph = {
        "nodes": [
            {"id": "lit_a", "definition_basis": "CLASSICAL_MULTIMODAL"},
            {"id": "lit_b", "definition_basis": "CLASSICAL_MULTIMODAL"},
            {
                "id": "CS_TARGET",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "taxonomy_id": "TX",
                "cell_set_accession": "CS_TARGET",
            },
        ],
        "edges": [
            {
                "id": "edge_a",
                "lit_type": "lit_a",
                "taxonomy_type": "CS_TARGET",
                "relationship": "skos:closeMatch",
                "mapping_justification": "semapv:UnreviewedManualMapping",
                "evidence": [
                    {
                        "evidence_type": "ANNOTATION_TRANSFER",
                        "run_ref": "at_run_demo",
                        "method": "MapMyCells",
                        "metrics_by_level": [
                            {
                                "taxonomy_level": "CLUSTER",
                                "best_target_accession": "CS_TARGET",
                                "f1_score": 0.67,
                            }
                        ],
                    }
                ],
            }
        ],
    }
    graph_path.write_text(yaml.safe_dump(graph))

    report = (
        "# Report\n"
        "<!-- verdict-block-start: edge_a -->\n"
        "```yaml\n"
        "verdict:\n"
        "  confidence: MODERATE\n"
        "  confidence_score: 0.6\n"
        "  rationale: 'F1=0.67 to CS_TARGET via at_run_demo.'\n"
        "  lit_to_lit_edges:\n"
        "    - lit_a: lit_a\n"
        "      lit_b: lit_b\n"
        "      mapping_justification: semapv:CompositeMatching\n"
        "```\n"
        "<!-- verdict-block-end -->\n"
    )
    report_path = tmp_path / "report.md"
    report_path.write_text(report)

    summary = write_back(report_path, graph_path, verify=True)
    assert summary["errors"] == []
    assert summary["lit_to_lit_created"] == 1

    doc = yaml.safe_load(graph_path.read_text())
    new_edges = [e for e in doc["edges"] if e["id"] != "edge_a"]
    assert len(new_edges) == 1
    new_edge = new_edges[0]
    assert new_edge["relationship"] == "skos:closeMatch"
    assert new_edge["mapping_cardinality"] == "1:1"
    assert new_edge["mapping_justification"] == "semapv:CompositeMatching"
    assert new_edge["lit_type"] == "lit_a"
    assert new_edge["taxonomy_type"] == "lit_b"
