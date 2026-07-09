"""Tests for evidencell.stage_b_emit — mechanical Stage B emitter.

Tier: fast (no external services). Uses the on-disk OLM rank-0 discovery
fixture for the end-to-end test; uses synthetic candidate dicts for the
rule-table tests.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import evidencell.stage_b_emit as sbe
from evidencell.stage_b_emit import (
    _atlas_location_summary,
    _caveats,
    _location_alignment,
    _marker_alignment,
    _resolve_symbol,
    _property_comparisons,
    emit_stage_b,
)


REPO_ROOT = Path(__file__).resolve().parent.parent
OLM_GRAPH = REPO_ROOT / "kb" / "graphs" / "hippocampus" / "hippocampus_OLM.yaml"
OLM_DISCOVERY_RANK0 = (
    REPO_ROOT
    / "research"
    / "hippocampus"
    / "map_olm_20260603"
    / "discovery_candidates_rank0.json"
)


# ── _resolve_symbol ─────────────────────────────────────────────────────────


def test_resolve_symbol_aliases():
    assert _resolve_symbol("PV") == "Pvalb"
    assert _resolve_symbol("CB") == "Calb1"
    assert _resolve_symbol("CR") == "Calb2"
    assert _resolve_symbol("NOS") == "Nos1"
    assert _resolve_symbol("VIP") == "Vip"


def test_resolve_symbol_passthrough():
    assert _resolve_symbol("Sst") == "Sst"
    assert _resolve_symbol("Chrna2") == "Chrna2"
    assert _resolve_symbol("Grm1") == "Grm1"


# ── _location_alignment tier rules ──────────────────────────────────────────


@pytest.mark.parametrize(
    "rf100,evidence,expected",
    [
        (0.82, "SELF", "CONSISTENT"),     # high proximity
        (0.50, "SELF", "CONSISTENT"),     # boundary inclusive
        (0.30, "SELF", "APPROXIMATE"),    # mid band
        (0.10, "SELF", "APPROXIMATE"),    # boundary inclusive
        (0.05, "SELF", "DISCORDANT"),     # below approximate band
        (0.00, "SELF", "DISCORDANT"),     # zero
        (None, "SELF", "NOT_ASSESSED"),
        (0.30, "DESCENDANT_ONLY", "DISCORDANT"),  # rescue → DISCORDANT
    ],
)
def test_location_alignment_tiers(rf100, evidence, expected):
    assert _location_alignment(rf100, evidence) == expected


# ── _marker_alignment rules ─────────────────────────────────────────────────


@pytest.mark.parametrize(
    "val,cohort_pct,is_negative,expected",
    [
        # positive marker: present, top of cohort → CONSISTENT
        (12.7, 0.99, False, "CONSISTENT"),
        # positive marker: present, mid-band → APPROXIMATE
        (2.5, 0.30, False, "APPROXIMATE"),
        # positive marker: present, low cohort pct → CONSISTENT (still present)
        (1.5, 0.05, False, "CONSISTENT"),
        # positive marker: absent → DISCORDANT
        (0.05, None, False, "DISCORDANT"),
        # negative marker: absent → CONSISTENT (confirms expected absence)
        (0.05, None, True, "CONSISTENT"),
        # negative marker: present → DISCORDANT (contradicts negative)
        (3.12, 0.50, True, "DISCORDANT"),
    ],
)
def test_marker_alignment(val, cohort_pct, is_negative, expected):
    assert _marker_alignment(val, cohort_pct, is_negative) == expected


# ── _caveats rules ──────────────────────────────────────────────────────────


def test_caveat_lower_bound_completeness():
    pcs = [{"property": "location", "alignment": "CONSISTENT"}]
    ds = {"region_count_completeness": "lower_bound"}
    cavs = _caveats(pcs, ds, {})
    assert any(c["caveat_type"] == "MERFISH_REGISTRATION_UNCERTAINTY" for c in cavs)


def test_caveat_discordant_property_triggers_ambiguous():
    pcs = [
        {"property": "negative_marker_PV", "alignment": "DISCORDANT"},
        {"property": "marker_Sst", "alignment": "CONSISTENT"},
    ]
    cavs = _caveats(pcs, {}, {})
    ambig = [c for c in cavs if c["caveat_type"] == "AMBIGUOUS_MAPPING"]
    assert len(ambig) == 1
    assert "negative_marker_PV" in ambig[0]["description"]


def test_caveat_at_cluster_f1_below_threshold():
    pcs: list[dict] = []
    at_signal = {"f1": 0.44, "target_level": "cluster"}
    cavs = _caveats(pcs, {}, at_signal)
    assert any(c["caveat_type"] == "DISTRIBUTED_ACROSS_CLUSTERS" for c in cavs)


def test_caveat_at_supertype_does_not_trigger_distributed():
    """Cluster-level threshold; supertype-level low F1 is structurally
    different (the source mapped to a higher rank), so don't emit."""
    pcs: list[dict] = []
    at_signal = {"f1": 0.44, "target_level": "supertype"}
    cavs = _caveats(pcs, {}, at_signal)
    assert not any(c["caveat_type"] == "DISTRIBUTED_ACROSS_CLUSTERS" for c in cavs)


def test_caveat_at_strong_f1_does_not_trigger_distributed():
    pcs: list[dict] = []
    at_signal = {"f1": 0.85, "target_level": "cluster"}
    cavs = _caveats(pcs, {}, at_signal)
    assert not any(c["caveat_type"] == "DISTRIBUTED_ACROSS_CLUSTERS" for c in cavs)


# ── _atlas_location_summary preference ──────────────────────────────────────


def test_atlas_location_summary_prefers_painted():
    atlas = {
        "anatomical_location": [
            {"id": "MBA:997", "label": "brain", "count_in_or_near_100um": 999, "cell_count_completeness": "lower_bound"},
            {"id": "MBA:399", "label": "stratum oriens", "count_in_or_near_100um": 100, "cell_count_completeness": None},
        ],
    }
    out = _atlas_location_summary(atlas, {})
    # Painted leaf wins despite lower absolute count.
    assert "MBA:399" in out
    assert "MBA:997" not in out
    assert "painted" in out


def test_atlas_location_summary_falls_back_to_lower_bound():
    atlas = {
        "anatomical_location": [
            {"id": "MBA:997", "label": "brain", "count_in_or_near_100um": 999, "cell_count_completeness": "lower_bound"},
        ],
    }
    out = _atlas_location_summary(atlas, {})
    assert "MBA:997" in out
    assert "lower_bound" in out


# ── _property_comparisons end-to-end on a synthetic candidate ───────────────


def test_property_comparisons_basic_olm_synthetic():
    classical = {
        "nt_type": {"name_in_source": "GABAergic"},
        "anatomical_location": [
            {"id": "UBERON:0005371", "label": "CA1 stratum oriens", "compartment": "SOMA"},
        ],
        "defining_markers": [{"symbol": "Sst"}, {"symbol": "Chrna2"}],
        "negative_markers": [{"symbol": "PV"}],
        "neuropeptides": [{"symbol": "Npy"}],
    }
    atlas = {
        "nt_type": {"name_in_source": "GABA"},
        "anatomical_location": [
            {"id": "MBA:399", "label": "stratum oriens",
             "count_in_or_near_100um": 250, "cell_count_completeness": None},
        ],
        "precomputed_expression": {
            "genes": [
                {"symbol": "Sst", "mean_expression": 12.7},
                {"symbol": "Chrna2", "mean_expression": 0.57},
                {"symbol": "Pvalb", "mean_expression": 3.12},
                {"symbol": "Npy", "mean_expression": 7.58},
            ],
        },
        "markers": [{"symbol": "Sst", "category": "NEUROPEPTIDE"}],
    }
    candidate = {
        "node_id": "CS20230722_CLUS_0768",
        "label": "0768 Sst Gaba_3",
        "_classical_cache": classical,
        "discovery_score": {
            "region_fraction_100um": 0.82,
            "region_fraction": 0.46,
            "region_count_completeness": None,
            "region_evidence": "SELF",
            "expression_detail": [
                {"gene": "Sst", "val": 12.7,
                 "percentiles": [{"context_id": "cohort", "pct": 0.99}]},
                {"gene": "Chrna2", "val": 0.57,
                 "percentiles": [{"context_id": "cohort", "pct": 0.95}]},
            ],
        },
    }
    pcs = _property_comparisons(
        classical_node_id="olm",
        candidate=candidate,
        atlas=atlas,
        ds=candidate["discovery_score"],
    )
    by_prop = {p["property"]: p for p in pcs}

    # nt_type CONSISTENT
    assert by_prop["nt_type"]["alignment"] == "CONSISTENT"

    # location CONSISTENT (rf100=0.82)
    assert by_prop["location"]["alignment"] == "CONSISTENT"

    # marker_Sst CONSISTENT
    assert by_prop["marker_Sst"]["alignment"] == "CONSISTENT"

    # marker_Chrna2 CONSISTENT (top-cohort presence)
    assert by_prop["marker_Chrna2"]["alignment"] == "CONSISTENT"

    # negative_marker_PV DISCORDANT (Pvalb 3.12 in atlas; alias resolved)
    assert by_prop["negative_marker_PV"]["alignment"] == "DISCORDANT"
    # node_b_value should cite the Pvalb value (alias-resolved).
    assert "3.12" in by_prop["negative_marker_PV"]["node_b_value"]

    # neuropeptide_Npy CONSISTENT
    assert by_prop["neuropeptide_Npy"]["alignment"] == "CONSISTENT"


# ── end-to-end emit against the real OLM rank-0 fixture ─────────────────────


@pytest.mark.slow
@pytest.mark.skipif(
    not OLM_DISCOVERY_RANK0.exists(),
    reason="OLM rank-0 discovery JSON fixture missing (run `just find-candidates` first)",
)
def test_emit_stage_b_olm_rank0_validates_and_produces_expected_shape(tmp_path):
    """End-to-end: emit on the OLM fixture, write to a temp graph,
    validate against the schema. Spot-check that:
    - 5 edges emitted (top-K=5).
    - Each edge has property_comparisons (>= 5), evidence (>= 1),
      typed caveats, default predicate UncertainRelationship.
    - The top candidate (CLUS_0768) emits an ANNOTATION_TRANSFER evidence
      item with run_ref + metrics_by_level populated.
    - Negative-marker alias resolution works (Pvalb DISCORDANT).
    """
    from ruamel.yaml import YAML
    yaml_rt = YAML(typ="rt")
    yaml_rt.preserve_quotes = True
    yaml_rt.width = 4096
    with OLM_GRAPH.open(encoding="utf-8") as fh:
        doc = yaml_rt.load(fh)
    doc["edges"] = []
    test_graph = tmp_path / "olm_test.yaml"
    with test_graph.open("w", encoding="utf-8") as fh:
        yaml_rt.dump(doc, fh)

    edges = emit_stage_b(
        classical_node_file=test_graph,
        classical_node_id="olm_hippocampus",
        taxonomy_id="CCN20230722",
        rank=0,
        top_k=5,
        discovery_json_path=OLM_DISCOVERY_RANK0,
        write=True,
    )

    assert len(edges) == 5
    for e in edges:
        assert e["relationship"] == "evidencell:UncertainRelationship"
        assert e["mapping_justification"] == "semapv:UnreviewedManualMapping"
        assert "confidence" not in e
        assert "rationale" not in e
        assert len(e["property_comparisons"]) >= 5
        assert len(e["evidence"]) >= 1
        # ATLAS_METADATA always present
        assert any(ev["evidence_type"] == "ATLAS_METADATA" for ev in e["evidence"])

    # Top edge (CLUS_0768) should carry AT evidence with metrics + the
    # negative-marker alias resolution should flag PV→Pvalb DISCORDANT.
    top = next(e for e in edges if e["taxonomy_type"] == "CS20230722_CLUS_0768")
    at = next(
        ev for ev in top["evidence"] if ev["evidence_type"] == "ANNOTATION_TRANSFER"
    )
    assert at["run_ref"] == "at_run_20260408_winterer_olm_mmc_wmbv1"
    assert at["metrics_by_level"]
    pv_comp = next(
        pc for pc in top["property_comparisons"] if pc["property"] == "negative_marker_PV"
    )
    assert pv_comp["alignment"] == "DISCORDANT"


# ── idempotence on re-emit ──────────────────────────────────────────────────


@pytest.mark.slow
@pytest.mark.skipif(
    not OLM_DISCOVERY_RANK0.exists(),
    reason="OLM rank-0 discovery JSON fixture missing",
)
def test_emit_stage_b_idempotent(tmp_path, capsys):
    """Calling emit_stage_b twice should not duplicate edges; the second
    call should be a no-op with a logged 'skipped' message."""
    from ruamel.yaml import YAML
    yaml_rt = YAML(typ="rt")
    yaml_rt.preserve_quotes = True
    with OLM_GRAPH.open(encoding="utf-8") as fh:
        doc = yaml_rt.load(fh)
    doc["edges"] = []
    test_graph = tmp_path / "olm_test_idem.yaml"
    with test_graph.open("w", encoding="utf-8") as fh:
        yaml_rt.dump(doc, fh)

    emit_stage_b(
        classical_node_file=test_graph,
        classical_node_id="olm_hippocampus",
        taxonomy_id="CCN20230722",
        rank=0,
        top_k=5,
        discovery_json_path=OLM_DISCOVERY_RANK0,
        write=True,
    )

    # Confirm 5 edges present after first run.
    yaml_rt2 = YAML(typ="rt")
    with test_graph.open(encoding="utf-8") as fh:
        post1 = yaml_rt2.load(fh)
    assert len(post1["edges"]) == 5

    # Second run should not add anything.
    emit_stage_b(
        classical_node_file=test_graph,
        classical_node_id="olm_hippocampus",
        taxonomy_id="CCN20230722",
        rank=0,
        top_k=5,
        discovery_json_path=OLM_DISCOVERY_RANK0,
        write=True,
    )
    with test_graph.open(encoding="utf-8") as fh:
        post2 = yaml_rt2.load(fh)
    assert len(post2["edges"]) == 5  # unchanged
    captured = capsys.readouterr()
    assert "skipped" in (captured.err or "")


# ── AT emission driven by at_source_sets (issue #126) ───────────────────────


def _patch_at(monkeypatch, *, run_map, metrics_map):
    """Patch resolve_run_for_source / compute_edge_metrics / load_run_manifest.

    ``run_map``: {(dataset, source_label): run_ref or None}.
    ``metrics_map``: {run_ref: compute_edge_metrics payload}.
    """
    def _resolve(dataset, taxonomy, source_label, **kw):
        return run_map.get((dataset, source_label))

    def _compute(*, run_ref, source_label, edge_target):
        return metrics_map[run_ref]

    monkeypatch.setattr(sbe, "resolve_run_for_source", _resolve)
    monkeypatch.setattr(sbe, "compute_edge_metrics", _compute)
    monkeypatch.setattr(sbe, "load_run_manifest", lambda r: {"target_atlas": "WMBv1"})


def _at_items(evlist):
    return [e for e in evlist if e["evidence_type"] == "ANNOTATION_TRANSFER"]


def test_at_evidence_positive_carries_correspondence(monkeypatch):
    _patch_at(
        monkeypatch,
        run_map={("GEO:GSE1", "Calb2-clus"): "at_run_x"},
        metrics_map={"at_run_x": {
            "metrics_by_level": [{"taxonomy_level": "CLUSTER", "f1_score": 0.8}],
            "best_mapping_rank": 0, "best_f1_score": 0.8,
            "supports_default": "SUPPORT", "f1_source_relpath": "at_results.yaml",
        }},
    )
    item = sbe._at_evidence(
        source_set={"dataset_accession": "GEO:GSE1", "source_label": "Calb2-clus",
                    "correspondence": "SUBSET"},
        taxonomy_id="CCN20230722",
        edge_target="CS20230722_CLUS_0768",
    )
    assert item["evidence_type"] == "ANNOTATION_TRANSFER"
    assert item["supports"] == "SUPPORT"
    assert item["correspondence"] == "SUBSET"
    assert item["source_dataset_accession"] == "GEO:GSE1"
    assert item["source_cluster_label"] == "Calb2-clus"
    assert item["run_ref"] == "at_run_x"
    assert item["metrics_by_level"]


def test_at_evidence_negative_when_source_does_not_transfer(monkeypatch):
    """Declared source resolves to a run but has no metrics reaching this
    candidate's lineage → NO_EVIDENCE (negative signal), not dropped."""
    _patch_at(
        monkeypatch,
        run_map={("GEO:GSE1", "Vip-Crh"): "at_run_x"},
        metrics_map={"at_run_x": {"metrics_by_level": [], "supports_default": "NO_EVIDENCE"}},
    )
    item = sbe._at_evidence(
        source_set={"dataset_accession": "GEO:GSE1", "source_label": "Vip-Crh"},
        taxonomy_id="CCN20230722",
        edge_target="CS20230722_CLUS_0628",
    )
    assert item is not None
    assert item["supports"] == "NO_EVIDENCE"
    assert item["run_ref"] == "at_run_x"
    assert "does not transfer" in item["explanation"]


def test_at_evidence_unresolvable_dataset(monkeypatch):
    _patch_at(monkeypatch, run_map={}, metrics_map={})
    item = sbe._at_evidence(
        source_set={"dataset_accession": "GEO:UNKNOWN", "source_label": "X"},
        taxonomy_id="CCN20230722",
        edge_target="CS20230722_CLUS_0768",
    )
    assert item["supports"] == "NO_EVIDENCE"
    assert "run_ref" not in item
    assert "could not be resolved" in item["explanation"]


def test_at_evidence_malformed_source_set(monkeypatch):
    _patch_at(monkeypatch, run_map={}, metrics_map={})
    assert sbe._at_evidence(
        source_set={"dataset_accession": "GEO:GSE1"},  # no source_label
        taxonomy_id="CCN20230722",
        edge_target="CS20230722_CLUS_0768",
    ) is None


def test_evidence_list_no_source_sets_emits_no_at(monkeypatch):
    """Full cutover: a node without at_source_sets gets no AT evidence."""
    _patch_at(monkeypatch, run_map={}, metrics_map={})
    out = sbe._evidence_list(
        atlas=None, candidate={"node_id": "CS20230722_CLUS_0768", "label": "x"},
        ds={}, at_source_sets=[], taxonomy_id="CCN20230722",
        taxonomy_type="CS20230722_CLUS_0768",
    )
    assert _at_items(out) == []
    assert any(e["evidence_type"] == "ATLAS_METADATA" for e in out)


def test_evidence_list_two_source_sets_positive_and_negative(monkeypatch):
    """Two declared sources: one transfers (SUPPORT), one doesn't
    (NO_EVIDENCE). Both surfaced as separate AT items."""
    _patch_at(
        monkeypatch,
        run_map={("GEO:GSE1", "Calb2"): "run_pos", ("GEO:GSE1", "Vip-Crh"): "run_neg"},
        metrics_map={
            "run_pos": {"metrics_by_level": [{"taxonomy_level": "CLUSTER", "f1_score": 0.8}],
                        "best_mapping_rank": 0, "best_f1_score": 0.8,
                        "supports_default": "SUPPORT", "f1_source_relpath": "at_results.yaml"},
            "run_neg": {"metrics_by_level": [], "supports_default": "NO_EVIDENCE"},
        },
    )
    out = sbe._evidence_list(
        atlas=None, candidate={"node_id": "CS20230722_CLUS_0768", "label": "x"},
        ds={},
        at_source_sets=[
            {"dataset_accession": "GEO:GSE1", "source_label": "Calb2", "correspondence": "SUBSET"},
            {"dataset_accession": "GEO:GSE1", "source_label": "Vip-Crh"},
        ],
        taxonomy_id="CCN20230722", taxonomy_type="CS20230722_CLUS_0768",
    )
    at = _at_items(out)
    assert len(at) == 2
    supports = {i["source_cluster_label"]: i["supports"] for i in at}
    assert supports == {"Calb2": "SUPPORT", "Vip-Crh": "NO_EVIDENCE"}
