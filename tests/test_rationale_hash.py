"""Phase 3: rationale-currency hash."""

from __future__ import annotations

import copy

from evidencell._rationale_hash import (
    compute_hash,
    is_stale,
    canonical_payload,
)


def _sample_edge() -> dict:
    return {
        "id": "edge_olm_to_supt_0216",
        "lit_type": "olm_cell_ca1",
        "taxonomy_type": "CS20230722_SUPT_0216",
        "relationship": "skos:closeMatch",
        "mapping_cardinality": "1:1",
        "mapping_justification": "semapv:CompositeMatching",
        "evidence": [
            {
                "evidence_type": "ANNOTATION_TRANSFER",
                "method": "MapMyCells",
                "metrics_by_level": [
                    {
                        "taxonomy_level": "SUPERTYPE",
                        "best_target_accession": "CS20230722_SUPT_0216",
                        "f1_score": 0.488,
                    }
                ],
            }
        ],
        "property_comparisons": [
            {"property": "marker_Sst", "alignment": "CONSISTENT"},
            {"property": "marker_Chrna2", "alignment": "CONSISTENT"},
        ],
    }


def _sample_lit_node() -> dict:
    return {
        "id": "olm_cell_ca1",
        "definition_basis": "CLASSICAL_MULTIMODAL",
        "defining_markers": [{"symbol": "Sst"}, {"symbol": "Chrna2"}],
    }


def _sample_tax_node() -> dict:
    return {
        "id": "CS20230722_SUPT_0216",
        "definition_basis": "ATLAS_TRANSCRIPTOMIC",
        "taxonomy_id": "CCN20230722",
        "cell_set_accession": "CS20230722_SUPT_0216",
    }


def test_hash_is_stable_format():
    h = compute_hash(_sample_edge(), _sample_lit_node(), _sample_tax_node())
    assert len(h) == 8
    assert all(c in "0123456789abcdef" for c in h)


def test_hash_stable_under_key_reordering():
    """Reordering dict keys at any level must not change the hash."""
    edge = _sample_edge()
    h1 = compute_hash(edge, _sample_lit_node(), _sample_tax_node())

    # Build the same edge with keys inserted in a different order.
    reordered = {}
    for k in reversed(list(edge.keys())):
        if isinstance(edge[k], list):
            reordered[k] = [
                {kk: vv for kk, vv in reversed(item.items())}
                if isinstance(item, dict)
                else item
                for item in edge[k]
            ]
        else:
            reordered[k] = edge[k]
    h2 = compute_hash(reordered, _sample_lit_node(), _sample_tax_node())
    assert h1 == h2


def test_hash_excludes_rationale_suite():
    """Changes to rationale, confidence, confidence_score,
    rationale_generated_at, rationale_source_hash, report_path must
    NOT change the hash — they're outputs of the report-time agent
    and must not feed back into the input hash."""
    base = _sample_edge()
    h_base = compute_hash(base, _sample_lit_node(), _sample_tax_node())

    edge_with_outputs = copy.deepcopy(base)
    edge_with_outputs["rationale"] = "some prose"
    edge_with_outputs["confidence"] = "MODERATE"
    edge_with_outputs["confidence_score"] = 0.65
    edge_with_outputs["rationale_generated_at"] = "2026-05-13T12:00:00Z"
    edge_with_outputs["rationale_source_hash"] = "deadbeef"
    edge_with_outputs["report_path"] = "reports/x/y.md"
    h_with = compute_hash(
        edge_with_outputs, _sample_lit_node(), _sample_tax_node()
    )
    assert h_base == h_with


def test_hash_changes_on_marker_edit():
    """Editing a defining_marker on the lit node should invalidate
    the rationale (Q9: hash inputs include endpoint nodes)."""
    h_base = compute_hash(_sample_edge(), _sample_lit_node(), _sample_tax_node())

    lit_node_changed = _sample_lit_node()
    lit_node_changed["defining_markers"] = [{"symbol": "Sst"}]  # dropped Chrna2
    h_changed = compute_hash(
        _sample_edge(), lit_node_changed, _sample_tax_node()
    )
    assert h_base != h_changed


def test_hash_unaffected_by_relationship_edit():
    """``relationship`` is a Phase-3 report-time output (filter+synth
    merge), so it's excluded from the hash domain. A curator
    re-predicating an edge does not invalidate the rationale-currency
    hash; staleness is keyed off upstream-evidence drift, not the
    agent's own outputs."""
    h_base = compute_hash(_sample_edge(), _sample_lit_node(), _sample_tax_node())

    edge_changed = _sample_edge()
    edge_changed["relationship"] = "skos:exactMatch"
    h_changed = compute_hash(
        edge_changed, _sample_lit_node(), _sample_tax_node()
    )
    assert h_base == h_changed


def test_is_stale_no_stored_hash():
    edge = _sample_edge()
    assert is_stale(edge, _sample_lit_node(), _sample_tax_node())


def test_is_stale_matching_stored_hash():
    edge = _sample_edge()
    edge["rationale_source_hash"] = compute_hash(
        edge, _sample_lit_node(), _sample_tax_node()
    )
    assert not is_stale(edge, _sample_lit_node(), _sample_tax_node())


def test_is_stale_after_marker_drift():
    """The canonical use case: rationale was written, then a curator
    edited the lit node's markers. Hash should now flag stale."""
    edge = _sample_edge()
    lit_node = _sample_lit_node()
    edge["rationale_source_hash"] = compute_hash(
        edge, lit_node, _sample_tax_node()
    )
    assert not is_stale(edge, lit_node, _sample_tax_node())

    lit_node["defining_markers"].append({"symbol": "Reln"})
    assert is_stale(edge, lit_node, _sample_tax_node())


def test_canonical_payload_handles_missing_endpoints():
    """When an endpoint node isn't in the local graph (e.g. lit-to-lit
    edge spanning two graphs), the hash still produces a stable value
    that distinguishes absent endpoints from present-but-empty ones."""
    payload = canonical_payload(_sample_edge(), None, None)
    assert payload["lit_node"] == {"_absent": True}
    assert payload["taxonomy_node"] == {"_absent": True}
