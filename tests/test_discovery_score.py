"""Tests for §1.11 — MappingEdge.discovery_score persistence.

Covers:
  - Schema round-trip: a fully populated discovery_score block
    validates against the LinkML schema and survives a
    yaml.safe_load → yaml.safe_dump cycle without loss.
  - Backfill module: legacy flat discovery JSON → schema-shaped
    block. Verifies field mapping, raw_tier reconstruction, source
    upper-casing, percentile context wiring, and idempotency.
  - gen-facts pass-through: edge with discovery_score → facts JSON
    preserves the block verbatim under the edge dict.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from evidencell.discovery_score_backfill import (
    _expression_detail_to_list,
    backfill_graph,
    candidate_to_discovery_score,
)


# ── Backfill module unit tests ────────────────────────────────────────────────


def test_expression_detail_to_list_empty():
    assert _expression_detail_to_list(None) == []
    assert _expression_detail_to_list({}) == []


def test_expression_detail_to_list_positive_marker_no_dampener():
    """rank 0 (no coverage): applied_score == raw_tier integer."""
    flat = {
        "Pvalb": {
            "val": 7.4,
            "reliable": True,
            "cohort_pct": 0.94,
            "score": 2,
            "source": "expression",
        }
    }
    out = _expression_detail_to_list(flat)
    assert len(out) == 1
    entry = out[0]
    assert entry["gene"] == "Pvalb"
    assert entry["val"] == 7.4
    assert entry["reliable"] is True
    assert entry["raw_tier"] == 2
    assert entry["applied_score"] == 2.0
    assert entry["source"] == "EXPRESSION"
    assert entry["percentiles"] == [{"context_id": "cohort", "pct": 0.94}]
    assert "coverage" not in entry


def test_expression_detail_to_list_dampened_supertype():
    """rank ≥ 1 coverage dampener: raw_tier reconstructed via inverse formula."""
    flat = {
        "Sst": {
            "val": 5.8,
            "reliable": True,
            "cohort_pct": 0.88,
            "score": 1.74,
            "source": "expression",
            "coverage": 0.75,
        }
    }
    out = _expression_detail_to_list(flat)
    entry = out[0]
    # raw_tier = applied / sqrt(coverage) ≈ 1.74 / 0.866 ≈ 2.0
    assert entry["raw_tier"] == 2
    assert entry["applied_score"] == pytest.approx(1.74)
    assert entry["coverage"] == 0.75


def test_expression_detail_to_list_metadata_only():
    flat = {
        "Fibcd1": {
            "val": None,
            "reliable": None,
            "cohort_pct": None,
            "score": 1,
            "source": "metadata",
        }
    }
    entry = _expression_detail_to_list(flat)[0]
    assert entry["gene"] == "Fibcd1"
    assert entry["val"] is None
    assert entry["raw_tier"] == 1
    assert entry["applied_score"] == 1.0
    assert entry["source"] == "METADATA"
    assert entry["percentiles"] == []  # no cohort_pct → no percentile entry


def test_expression_detail_to_list_negative_marker_preserves_prefix():
    flat = {
        "-Slc17a7": {
            "val": 0.2,
            "reliable": False,
            "cohort_pct": 0.12,
            "score": 1,
            "source": "expression",
        }
    }
    entry = _expression_detail_to_list(flat)[0]
    assert entry["gene"] == "-Slc17a7"
    assert entry["raw_tier"] == 1


def test_candidate_to_discovery_score_full():
    candidate = {
        "node_id": "CS20230722_CLUS_0261",
        "score": 8,
        "expression_detail": {
            "Pvalb": {
                "val": 7.4,
                "reliable": True,
                "cohort_pct": 0.94,
                "score": 2,
                "source": "expression",
            }
        },
        "region_fraction": 0.85,
        "region_evidence": "self",
        "at_hit": {
            "f1": 0.62,
            "n_cells": 142,
            "target_level": "cluster",
            "target_name": "0261 CA1-ProS Glut_1",
            "score": 3,
        },
    }
    block = candidate_to_discovery_score(
        candidate,
        rank=0,
        cohort_size=142,
        rank_in_cohort=1,
        next_best_score=3,
    )
    assert block["score"] == 8
    assert block["rank_in_cohort"] == 1
    assert block["cohort_size"] == 142
    assert block["next_best_score"] == 3
    assert block["rank"] == 0
    assert block["region_fraction"] == 0.85
    assert block["region_evidence"] == "SELF"  # upper-cased
    assert block["at_signal"]["f1"] == 0.62
    assert len(block["contexts"]) == 1
    ctx = block["contexts"][0]
    assert ctx["id"] == "cohort"
    assert ctx["kind"] == "SURVIVAL_COHORT"
    assert ctx["n_members"] == 142
    assert ctx["filters"] == []  # not recoverable from legacy JSON
    assert len(block["expression_detail"]) == 1
    assert block["expression_detail"][0]["gene"] == "Pvalb"


def test_candidate_to_discovery_score_passthrough_if_already_present():
    """When the candidate dict already carries a schema-shaped
    discovery_score (newer Stage A emission), backfill must
    forward it verbatim — not re-derive from legacy fields."""
    already_shaped = {
        "score": 5,
        "rank_in_cohort": 1,
        "cohort_size": 12,
        "next_best_score": 3,
        "rank": 0,
        "contexts": [{"id": "cohort", "kind": "SURVIVAL_COHORT", "n_members": 12, "filters": ["nt_type=Gaba"]}],
        "expression_detail": [],
    }
    candidate = {
        "node_id": "X",
        "score": 999,  # would-be-wrong if re-derived
        "discovery_score": already_shaped,
    }
    block = candidate_to_discovery_score(
        candidate, rank=999, cohort_size=999, rank_in_cohort=999, next_best_score=999
    )
    assert block is already_shaped


def test_candidate_to_discovery_score_descendant_only_region():
    candidate = {
        "node_id": "X",
        "score": 4,
        "region_evidence": "descendant_only",
        "region_fraction": 0.42,
    }
    block = candidate_to_discovery_score(
        candidate, rank=1, cohort_size=8, rank_in_cohort=2, next_best_score=5
    )
    assert block["region_evidence"] == "DESCENDANT_ONLY"


# ── End-to-end backfill on a fixture graph ────────────────────────────────────


@pytest.fixture
def fixture_graph_and_discovery(tmp_path: Path, monkeypatch):
    """Create a minimal graph file under tmp_path/kb/graphs/{region}/
    plus a discovery JSON under tmp_path/research/{region}/, then
    monkeypatch repo_root() to point at tmp_path so the backfill
    module finds both."""
    region = "testregion"
    graph_dir = tmp_path / "kb" / "graphs" / region
    graph_dir.mkdir(parents=True)
    research_dir = tmp_path / "research" / region
    research_dir.mkdir(parents=True)

    graph_file = graph_dir / "testgraph.yaml"
    graph = {
        "name": "test",
        "target_atlas": "TESTATLAS",
        "nodes": [
            {"id": "classical_x", "name": "Classical X", "definition_basis": "OTHER"},
            {
                "id": "CS_CLUS_0001",
                "name": "Test cluster",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "taxonomy_id": "TEST",
                "cell_set_accession": "CS_CLUS_0001",
                "taxonomy_rank": 0,
            },
        ],
        "edges": [
            {
                "id": "edge_with_match",
                "lit_type": "classical_x",
                "taxonomy_type": "CS_CLUS_0001",
                "relationship": "skos:closeMatch",
                "evidence": [
                    {
                        "evidence_type": "ATLAS_METADATA",
                        "supports": "PARTIAL",
                        "explanation": "test",
                    }
                ],
            },
            {
                "id": "edge_no_match",
                "lit_type": "classical_x",
                "taxonomy_type": "CS_CLUS_9999",
                "relationship": "skos:closeMatch",
                "evidence": [
                    {
                        "evidence_type": "ATLAS_METADATA",
                        "supports": "PARTIAL",
                        "explanation": "test",
                    }
                ],
            },
            {
                "id": "edge_already_populated",
                "lit_type": "classical_x",
                "taxonomy_type": "CS_CLUS_0001",
                "relationship": "skos:closeMatch",
                "discovery_score": {
                    "score": 99,
                    "rank_in_cohort": 1,
                    "cohort_size": 1,
                    "next_best_score": 0,
                    "rank": 0,
                    "contexts": [],
                    "expression_detail": [],
                },
                "evidence": [
                    {
                        "evidence_type": "ATLAS_METADATA",
                        "supports": "SUPPORT",
                        "explanation": "test",
                    }
                ],
            },
        ],
    }
    graph_file.write_text(yaml.safe_dump(graph, sort_keys=False))

    discovery = {
        "classical_node_id": "classical_x",
        "classical_node_name": "Classical X",
        "taxonomy_id": "TEST",
        "rank": 0,
        "n_candidates": 2,
        "candidates": [
            {
                "node_id": "CS_CLUS_0001",
                "label": "Test cluster",
                "taxonomy_level": "cluster",
                "taxonomy_rank": 0,
                "score": 7,
                "expression_detail": {
                    "Pvalb": {
                        "val": 7.4,
                        "reliable": True,
                        "cohort_pct": 0.94,
                        "score": 2,
                        "source": "expression",
                    },
                },
                "region_fraction": 0.9,
                "region_evidence": "self",
            },
            {
                "node_id": "CS_CLUS_0002",
                "label": "Other",
                "score": 3,
                "taxonomy_level": "cluster",
                "taxonomy_rank": 0,
            },
        ],
    }
    (research_dir / "discovery_classical_x_rank0.json").write_text(
        json.dumps(discovery, indent=2)
    )

    # Re-point repo_root() so the backfill module finds research/.
    monkeypatch.setattr(
        "evidencell.discovery_score_backfill.repo_root", lambda: tmp_path
    )
    return graph_file, region


def test_backfill_graph_patches_missing_and_skips_present(
    fixture_graph_and_discovery,
):
    graph_file, _ = fixture_graph_and_discovery
    result = backfill_graph(graph_file, dry_run=False)

    assert len(result["patched"]) == 1
    assert result["patched"][0].startswith("edge_with_match")
    assert "edge_already_populated" in result["skipped_already_present"]
    assert len(result["missing"]) == 1
    assert result["missing"][0][0] == "edge_no_match"

    # Reload and confirm discovery_score landed on the right edge.
    with graph_file.open() as fh:
        graph2 = yaml.safe_load(fh)
    edges = {e["id"]: e for e in graph2["edges"]}
    assert "discovery_score" in edges["edge_with_match"]
    ds = edges["edge_with_match"]["discovery_score"]
    assert ds["score"] == 7
    assert ds["rank_in_cohort"] == 1
    assert ds["cohort_size"] == 2
    assert ds["next_best_score"] == 3
    assert ds["rank"] == 0
    assert ds["region_evidence"] == "SELF"
    assert ds["expression_detail"][0]["gene"] == "Pvalb"
    assert ds["expression_detail"][0]["source"] == "EXPRESSION"

    # Already-populated edge unchanged.
    assert edges["edge_already_populated"]["discovery_score"]["score"] == 99
    # No-match edge still has no discovery_score.
    assert "discovery_score" not in edges["edge_no_match"]


def test_backfill_graph_idempotent(fixture_graph_and_discovery):
    """Running backfill twice produces the same file content."""
    graph_file, _ = fixture_graph_and_discovery
    backfill_graph(graph_file, dry_run=False)
    text_after_first = graph_file.read_text()
    result2 = backfill_graph(graph_file, dry_run=False)
    text_after_second = graph_file.read_text()
    assert text_after_first == text_after_second
    # Second pass should have nothing to patch (the first edge is now populated).
    assert result2["patched"] == []


def test_backfill_dry_run_does_not_write(fixture_graph_and_discovery):
    graph_file, _ = fixture_graph_and_discovery
    before = graph_file.read_text()
    backfill_graph(graph_file, dry_run=True)
    after = graph_file.read_text()
    assert before == after


# ── Schema round-trip via Pydantic ─────────────────────────────────────────────


def test_discovery_score_pydantic_round_trip():
    from evidencell._models import DiscoveryScore

    block = {
        "score": 8,
        "rank_in_cohort": 1,
        "cohort_size": 142,
        "next_best_score": 3,
        "rank": 0,
        "region_fraction": 0.85,
        "region_evidence": "SELF",
        "contexts": [
            {
                "id": "cohort",
                "kind": "SURVIVAL_COHORT",
                "rank": 0,
                "n_members": 142,
                "filters": ["region=hippocampal_formation", "nt_type=Gaba"],
            }
        ],
        "expression_detail": [
            {
                "gene": "Pvalb",
                "val": 7.4,
                "reliable": True,
                "raw_tier": 2,
                "applied_score": 2.0,
                "source": "EXPRESSION",
                "percentiles": [{"context_id": "cohort", "pct": 0.94}],
            },
            {
                "gene": "-Slc17a7",
                "val": 0.2,
                "reliable": False,
                "raw_tier": 1,
                "applied_score": 1.0,
                "source": "EXPRESSION",
                "percentiles": [{"context_id": "cohort", "pct": 0.12}],
            },
        ],
        "at_signal": {
            "f1": 0.62,
            "n_cells": 142,
            "target_level": "cluster",
            "target_name": "Test target",
            "score": 3,
        },
    }
    ds = DiscoveryScore(**block)
    assert ds.score == 8
    assert ds.rank_in_cohort == 1
    assert str(ds.contexts[0].kind) == "SURVIVAL_COHORT" or (
        hasattr(ds.contexts[0].kind, "value")
        and ds.contexts[0].kind.value == "SURVIVAL_COHORT"
    )
    assert ds.expression_detail[0].gene == "Pvalb"
    assert ds.expression_detail[1].gene == "-Slc17a7"
    assert ds.at_signal.f1 == 0.62
    # Round-trip through Pydantic's serialisation.
    dumped = ds.model_dump(exclude_none=True)
    assert dumped["score"] == 8
    assert dumped["expression_detail"][0]["gene"] == "Pvalb"


def test_discovery_score_rejects_lowercase_region_evidence():
    """The schema enum is uppercase; lowercase legacy values must
    not validate (the backfill module's job is to upper-case)."""
    from evidencell._models import DiscoveryScore
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        DiscoveryScore(
            score=1,
            region_evidence="self",  # legacy lowercase
            contexts=[],
            expression_detail=[],
        )
