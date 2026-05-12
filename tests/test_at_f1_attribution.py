"""Tests for the AT F1 attribution audit + correction + hook check."""

from __future__ import annotations


import pytest
import yaml

from evidencell.at_f1_attribution import (
    AttributionFinding,
    find_mismatches,
    target_level_from_accession,
)


# ── target_level_from_accession ────────────────────────────────────


def test_target_level_from_accession_known_prefixes():
    assert target_level_from_accession("CS20230722_CLUS_0769") == "CLUSTER"
    assert target_level_from_accession("CS20230722_SUPT_0216") == "SUPERTYPE"
    assert target_level_from_accession("CS20230722_SUBC_053") == "SUBCLASS"
    assert target_level_from_accession("CS20230722_CLAS_07") == "CLASS"


def test_target_level_from_accession_unknown():
    assert target_level_from_accession("foo") is None
    assert target_level_from_accession("") is None
    assert target_level_from_accession("CS_other_format") is None


# ── find_mismatches ────────────────────────────────────────────────


@pytest.fixture
def graph_with_mismatched_evidence(tmp_path):
    """Build a minimal kb/graphs/ tree with one edge whose AT evidence
    has best_mapping_level disagreeing with the target's level."""
    g = tmp_path / "kb" / "graphs" / "test_region"
    g.mkdir(parents=True)
    doc = {
        "nodes": [
            {
                "id": "lit_thing", "definition_basis": "ARTIFICIAL",
                "anatomical_location": [],
            },
            {
                "id": "atlas_thing", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "taxonomy_id": "CCN20230722",
                "cell_set_accession": "CS20230722_CLUS_0769",
            },
        ],
        "edges": [
            {
                "id": "edge_mismatch",
                "lit_type": "lit_thing",
                "taxonomy_type": "atlas_thing",
                "relationship": "EQUIVALENT",
                "evidence": [{
                    "evidence_type": "ANNOTATION_TRANSFER",
                    "best_f1_score": 0.67,
                    "best_mapping_level": "SUPERTYPE",  # mismatch — target is CLUSTER
                    "explanation": "block",
                    "run_ref": "fake_run",
                    "source_cluster_label": "fake_source",
                }],
            },
        ],
    }
    (g / "test.yaml").write_text(yaml.safe_dump(doc))
    return tmp_path


def test_find_mismatches_picks_up_level_disagreement(graph_with_mismatched_evidence):
    """The mismatch in the fixture (SUPERTYPE F1 on a CLUSTER edge) is
    reported, with correct field extraction."""
    graphs_root = graph_with_mismatched_evidence / "kb" / "graphs"
    findings = find_mismatches(graphs_root=graphs_root)
    assert len(findings) == 1
    f = findings[0]
    assert isinstance(f, AttributionFinding)
    assert f.edge_id == "edge_mismatch"
    assert f.target_accession == "CS20230722_CLUS_0769"
    assert f.target_level == "CLUSTER"
    assert f.best_mapping_level == "SUPERTYPE"
    assert f.recorded_f1 == 0.67


def test_find_mismatches_passes_through_when_levels_agree(tmp_path):
    """An edge whose AT evidence reports a level matching the target's
    accession-derived level is NOT flagged."""
    g = tmp_path / "kb" / "graphs" / "test_region"
    g.mkdir(parents=True)
    doc = {
        "nodes": [
            {"id": "lit", "definition_basis": "ARTIFICIAL"},
            {"id": "atlas", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
             "cell_set_accession": "CS20230722_SUPT_0216",
             "taxonomy_id": "CCN20230722"},
        ],
        "edges": [{
            "id": "edge_ok", "lit_type": "lit", "taxonomy_type": "atlas",
            "evidence": [{
                "evidence_type": "ANNOTATION_TRANSFER",
                "best_f1_score": 0.5,
                "best_mapping_level": "SUPERTYPE",
            }],
        }],
    }
    (g / "test.yaml").write_text(yaml.safe_dump(doc))
    findings = find_mismatches(graphs_root=g)
    assert findings == []


# NOTE: apply_corrections and check_at_f1_attribution were removed
# after they were found to enforce a convention that doesn't match how
# AT evidence is actually authored (the bml field records the level
# the F1 was computed at, which can legitimately differ from the edge
# target's level). The module is now informational-only via
# find_mismatches() and lookup_correct_f1().
