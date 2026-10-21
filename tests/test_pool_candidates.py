"""Phase 3: pool-candidate discovery pre-pass."""

from __future__ import annotations

from evidencell.pool_candidates import (
    find_pool_candidates,
    find_pool_candidates_for_node,
    _classify_panel,
)


def _at_evidence(target_acc: str, level: str, f1: float, gp: float = None, tp: float = None) -> dict:
    """Helper: build a single ANNOTATION_TRANSFER evidence dict."""
    if gp is None:
        gp = f1
    if tp is None:
        tp = f1
    return {
        "evidence_type": "ANNOTATION_TRANSFER",
        "run_ref": "at_run_test",
        "metrics_by_level": [
            {
                "taxonomy_level": level,
                "best_target_accession": target_acc,
                "f1_score": f1,
                "coverage": gp,
                "purity": tp,
            }
        ],
    }


def test_classify_panel_known_prefixes():
    assert _classify_panel("marker_Sst") == "markers"
    assert _classify_panel("location") == "anat"
    assert _classify_panel("anatomical_location") == "anat"
    assert _classify_panel("nt_type") == "nt"
    assert _classify_panel("electrophysiology") == "ephys"
    assert _classify_panel("morphology") == "morphology"


def test_classify_panel_unknown_returns_none():
    assert _classify_panel("random_property") is None
    assert _classify_panel("") is None
    assert _classify_panel(None) is None


def test_no_candidates_when_targets_disjoint():
    """Two lit_types that don't share any atlas target → no candidates."""
    graph = {
        "edges": [
            {
                "id": "e1",
                "lit_type": "lit_A",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.9)],
            },
            {
                "id": "e2",
                "lit_type": "lit_B",
                "taxonomy_type": "CS_CLUS_999",
                "evidence": [_at_evidence("CS_CLUS_999", "CLUSTER", 0.9)],
            },
        ]
    }
    assert find_pool_candidates(graph) == []


def test_candidate_when_shared_target_within_tolerance():
    """Two lit_types mapping to the same target with F1 within 5% → pool candidate."""
    graph = {
        "edges": [
            {
                "id": "e1",
                "lit_type": "lit_A",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.67)],
            },
            {
                "id": "e2",
                "lit_type": "lit_B",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.69)],
            },
        ]
    }
    candidates = find_pool_candidates(graph)
    assert len(candidates) == 1
    c = candidates[0]
    assert sorted(c["source_groups"]) == ["lit_A", "lit_B"]
    assert len(c["shared_targets"]) == 1


def test_no_candidate_when_f1_outside_tolerance():
    """F1 gap > 5% disqualifies the pair (default tolerance)."""
    graph = {
        "edges": [
            {
                "id": "e1",
                "lit_type": "lit_A",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.6)],
            },
            {
                "id": "e2",
                "lit_type": "lit_B",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.9)],
            },
        ]
    }
    assert find_pool_candidates(graph) == []


def test_all_shared_targets_must_be_within_tolerance():
    """Any single shared target with F1 outside tolerance disqualifies."""
    graph = {
        "edges": [
            {
                "id": "e1",
                "lit_type": "lit_A",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [
                    _at_evidence("CS_CLUS_001", "CLUSTER", 0.67),
                    _at_evidence("CS_CLUS_002", "CLUSTER", 0.5),
                ],
            },
            {
                "id": "e2",
                "lit_type": "lit_B",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [
                    _at_evidence("CS_CLUS_001", "CLUSTER", 0.69),
                    _at_evidence("CS_CLUS_002", "CLUSTER", 0.85),  # +35%
                ],
            },
        ]
    }
    assert find_pool_candidates(graph) == []


def test_panels_assessed_picked_up_from_property_comparisons():
    """The synthesis agent needs to know which panels have been
    assessed on each source group's edges, so it can call Case A vs
    Case B. We populate `panels_assessed` from non-NOT_ASSESSED
    PropertyComparisons."""
    graph = {
        "edges": [
            {
                "id": "e1",
                "lit_type": "lit_A",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.67)],
                "property_comparisons": [
                    {"property": "marker_Sst", "alignment": "CONSISTENT"},
                    {"property": "electrophysiology", "alignment": "CONSISTENT"},
                ],
            },
            {
                "id": "e2",
                "lit_type": "lit_B",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.69)],
                "property_comparisons": [
                    {"property": "marker_Sst", "alignment": "CONSISTENT"},
                    {"property": "electrophysiology", "alignment": "CONSISTENT"},
                ],
            },
        ]
    }
    candidates = find_pool_candidates(graph)
    assert len(candidates) == 1
    assessed = set(candidates[0]["panels_assessed"])
    # Both edges assess markers + ephys.
    assert "markers" in assessed
    assert "ephys" in assessed


def test_find_for_node_filters_to_relevant_candidates():
    """The per-node variant returns only candidates involving the
    given lit_type."""
    graph = {
        "edges": [
            {
                "id": "e1",
                "lit_type": "lit_A",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.67)],
            },
            {
                "id": "e2",
                "lit_type": "lit_B",
                "taxonomy_type": "CS_CLUS_001",
                "evidence": [_at_evidence("CS_CLUS_001", "CLUSTER", 0.69)],
            },
            {
                "id": "e3",
                "lit_type": "lit_C",
                "taxonomy_type": "CS_CLUS_002",
                "evidence": [_at_evidence("CS_CLUS_002", "CLUSTER", 0.5)],
            },
        ]
    }
    a_candidates = find_pool_candidates_for_node(graph, "lit_A")
    assert len(a_candidates) == 1
    assert "lit_A" in a_candidates[0]["source_groups"]

    # C is in no candidate.
    c_candidates = find_pool_candidates_for_node(graph, "lit_C")
    assert c_candidates == []


# ── Region scoping ────────────────────────────────────────────────────────────

def test_load_region_graph_merges_sibling_files(tmp_path):
    """Pool detection is pairwise across lit_types, so it must see the region.

    Once each file holds one component, a per-file view yields one lit_type,
    zero pairs, and silently returns no candidates.
    """
    import yaml as _yaml

    from evidencell.pool_candidates import load_region_graph

    (tmp_path / "a.yaml").write_text(
        _yaml.safe_dump({"edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "x"}]})
    )
    (tmp_path / "b.yaml").write_text(
        _yaml.safe_dump({"edges": [{"id": "e2", "lit_type": "b", "taxonomy_type": "y"}]})
    )
    merged = load_region_graph(tmp_path / "a.yaml")
    assert sorted(e["id"] for e in merged["edges"]) == ["e1", "e2"]


def test_load_region_graph_dedupes_shared_edge_ids(tmp_path):
    import yaml as _yaml

    from evidencell.pool_candidates import load_region_graph

    edge = {"id": "e1", "lit_type": "a", "taxonomy_type": "x"}
    (tmp_path / "a.yaml").write_text(_yaml.safe_dump({"edges": [edge]}))
    (tmp_path / "b.yaml").write_text(_yaml.safe_dump({"edges": [edge]}))
    assert len(load_region_graph(tmp_path / "a.yaml")["edges"]) == 1


def test_load_region_graph_tolerates_unparseable_sibling(tmp_path):
    import yaml as _yaml

    from evidencell.pool_candidates import load_region_graph

    (tmp_path / "a.yaml").write_text(
        _yaml.safe_dump({"edges": [{"id": "e1", "lit_type": "a", "taxonomy_type": "x"}]})
    )
    (tmp_path / "broken.yaml").write_text("{[not valid yaml", encoding="utf-8")
    assert [e["id"] for e in load_region_graph(tmp_path / "a.yaml")["edges"]] == ["e1"]
