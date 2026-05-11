"""Tests for the AT F1 attribution audit + correction + hook check."""

from __future__ import annotations

import json

import pytest
import yaml

from evidencell.at_f1_attribution import (
    AttributionFinding,
    apply_corrections,
    find_mismatches,
    target_level_from_accession,
)
from evidencell.validate import check_at_f1_attribution


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
                "type_a": "lit_thing",
                "type_b": "atlas_thing",
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
            "id": "edge_ok", "type_a": "lit", "type_b": "atlas",
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


# ── apply_corrections ──────────────────────────────────────────────


def test_apply_corrections_surgical_edit_preserves_unrelated_content(
    graph_with_mismatched_evidence, tmp_path, monkeypatch
):
    """Correction modifies only the two target fields; the rest of the
    file (comments, formatting, other keys) is preserved byte-for-byte."""
    import evidencell.paths as paths_mod
    import evidencell.at_f1_attribution as f1_mod
    monkeypatch.setattr(paths_mod, "repo_root", lambda: graph_with_mismatched_evidence)
    monkeypatch.setattr(f1_mod, "repo_root", lambda: graph_with_mismatched_evidence)

    yaml_path = graph_with_mismatched_evidence / "kb" / "graphs" / "test_region" / "test.yaml"

    # Replace the simple safe_dump output with a file that has a
    # leading comment and explicit block-scalar explanation we want
    # preserved verbatim.
    yaml_path.write_text(
        "# This is a test graph file.\n"
        "# Edits to data should preserve commentary.\n"
        "\n"
        "nodes:\n"
        "  - id: lit_thing\n"
        "    definition_basis: ARTIFICIAL\n"
        "\n"
        "  - id: atlas_thing\n"
        "    definition_basis: ATLAS_TRANSCRIPTOMIC\n"
        "    taxonomy_id: CCN20230722\n"
        "    cell_set_accession: CS20230722_CLUS_0769\n"
        "\n"
        "edges:\n"
        "  - id: edge_mismatch\n"
        "    type_a: lit_thing\n"
        "    type_b: atlas_thing\n"
        "    relationship: EQUIVALENT\n"
        "    evidence:\n"
        "      - evidence_type: ANNOTATION_TRANSFER\n"
        "        explanation: >\n"
        "          A folded-block explanation that should\n"
        "          remain a folded block after correction.\n"
        "        run_ref: fake_run\n"
        "        source_cluster_label: fake_source\n"
        "        best_f1_score: 0.67\n"
        '        best_mapping_level: "SUPERTYPE"\n'
    )

    findings = find_mismatches(
        graphs_root=graph_with_mismatched_evidence / "kb" / "graphs"
    )
    assert len(findings) == 1
    log_path = tmp_path / "corrections_log.json"
    actions = apply_corrections(findings, log_path=log_path)
    assert len(actions) == 1

    after = yaml_path.read_text()

    # Preserved verbatim
    assert "# This is a test graph file." in after
    assert "# Edits to data should preserve commentary." in after
    assert "explanation: >" in after
    assert "A folded-block explanation that should" in after
    assert "remain a folded block after correction." in after

    # Surgically updated
    assert "best_f1_score: 0.67" not in after
    assert "best_mapping_level: \"SUPERTYPE\"" not in after
    assert 'best_mapping_level: "CLUSTER"' in after

    # Audit log captured the change with old + new values
    log = json.loads(log_path.read_text())
    assert len(log) == 1
    assert log[0]["old_f1"] == 0.67
    assert log[0]["old_mapping_level"] == "SUPERTYPE"
    assert log[0]["new_mapping_level"] == "CLUSTER"


# ── check_at_f1_attribution (pre-edit hook check) ──────────────────


def test_hook_check_rejects_mismatch():
    """The hook check returns an error string for an AT evidence whose
    level disagrees with the target accession's level."""
    doc = {
        "nodes": [{"id": "atlas", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                   "cell_set_accession": "CS20230722_CLUS_0769"}],
        "edges": [{
            "id": "edge_bad", "type_a": "lit", "type_b": "atlas",
            "evidence": [{
                "evidence_type": "ANNOTATION_TRANSFER",
                "best_f1_score": 0.67,
                "best_mapping_level": "SUPERTYPE",
            }],
        }],
    }
    errors = check_at_f1_attribution(doc)
    assert len(errors) == 1
    assert "edge_bad" in errors[0]
    assert "SUPERTYPE" in errors[0]
    assert "CLUSTER" in errors[0]


def test_hook_check_passes_when_levels_agree():
    doc = {
        "nodes": [{"id": "atlas", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                   "cell_set_accession": "CS20230722_SUPT_0216"}],
        "edges": [{
            "id": "edge_ok", "type_a": "lit", "type_b": "atlas",
            "evidence": [{
                "evidence_type": "ANNOTATION_TRANSFER",
                "best_f1_score": 0.67,
                "best_mapping_level": "SUPERTYPE",
            }],
        }],
    }
    assert check_at_f1_attribution(doc) == []


def test_hook_check_ignores_evidence_without_mapping_level():
    """An AT evidence item with no best_mapping_level recorded is
    passed through (the field is optional in the schema; this check
    fires only on a declared-and-wrong value)."""
    doc = {
        "nodes": [{"id": "atlas", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                   "cell_set_accession": "CS20230722_CLUS_0769"}],
        "edges": [{
            "id": "edge_no_level", "type_a": "lit", "type_b": "atlas",
            "evidence": [{
                "evidence_type": "ANNOTATION_TRANSFER",
                "best_f1_score": 0.5,
            }],
        }],
    }
    assert check_at_f1_attribution(doc) == []


def test_hook_check_ignores_non_at_evidence():
    """The check applies only to ANNOTATION_TRANSFER evidence type."""
    doc = {
        "nodes": [{"id": "atlas", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                   "cell_set_accession": "CS20230722_CLUS_0769"}],
        "edges": [{
            "id": "edge_lit", "type_a": "lit", "type_b": "atlas",
            "evidence": [{
                "evidence_type": "LITERATURE",
                "best_f1_score": 0.99,
                "best_mapping_level": "SUBCLASS",
            }],
        }],
    }
    assert check_at_f1_attribution(doc) == []
