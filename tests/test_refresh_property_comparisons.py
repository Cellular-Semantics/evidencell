"""Tests for ``refresh_property_comparisons`` — targeted refresh of
stale Stage B output on legacy edges, with byte-identity preservation
of everything else on the edge. Closes #103.

The critical regression-locking property is the second test
(``test_refresh_preserves_evidence_and_rationale_suite_byte_identical``):
when the tool runs, it MUST NOT mutate ``evidence[]``, the
rationale-suite fields (``confidence``, ``rationale``, etc.),
``caveats[]``, ``proposed_experiments[]``,
``unresolved_questions[]``, ``curator``, or ``reviewed_by`` — even
for AT evidence with rich ``source_groups[*].rationale`` populated.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
from ruamel.yaml import YAML

from evidencell.refresh_property_comparisons import refresh_property_comparisons


REPO_ROOT = Path(__file__).resolve().parent.parent
OLM_GRAPH = REPO_ROOT / "kb" / "graphs" / "hippocampus" / "hippocampus_OLM.yaml"
OLM_DISCOVERY_RANK0 = (
    REPO_ROOT
    / "research"
    / "hippocampus"
    / "map_olm_20260603"
    / "discovery_candidates_rank0.json"
)


# Curator-set rationale-suite + caveats + AT evidence with rich
# source_groups rationale. These are the fields the refresh tool
# must NOT touch.
_CURATOR_RATIONALE = "MODERATE confidence; OLM cells map to Sst Gaba_3 supertype."
_CURATOR_CAVEAT = "AT cells scatter across siblings within Sst Gaba_3."
_CURATOR_RECONCILIATION = "broadMatch + 1:n encoding chosen at supertype rather than cluster."
_CURATOR_AT_SOURCE_GROUP_RATIONALE = (
    "Sst-OLM and Htr3a-OLM map indistinguishably under run_ref X; "
    "pooled at the source-curation step."
)
_LITERATURE_EVIDENCE_QUOTE = "OLMs express somatostatin (Sst)."


def _yaml_rt() -> YAML:
    y = YAML(typ="rt")
    y.preserve_quotes = True
    y.width = 4096
    y.indent(mapping=2, sequence=4, offset=2)
    return y


def _build_decorated_olm_graph(tmp_path: Path) -> Path:
    """Build a tmp OLM graph carrying ONE injected edge for CLUS_0768
    (which IS in the OLM rank-0 discovery fixture's top-K) with rich
    curator content. The injected edge is the test subject.

    The real OLM graph's existing curator edges target 0727/0785/
    0769/0788/0789 — none in the fresh top-K — so they're not refresh
    candidates here. We inject CLUS_0768 to give the refresh tool
    something to match against, then check that:
    1. Its stale property_comparisons (sentinel) get replaced.
    2. Its evidence + rationale-suite + caveats etc. survive untouched.

    Stages the graph under ``kb/graphs/hippocampus/_tmp_test_*.yaml``
    because gen-facts / find-candidates require the path to live
    under ``kb/graphs/{region}/`` (paths.region_from_graph constraint).
    """
    yaml_rt = _yaml_rt()
    with OLM_GRAPH.open(encoding="utf-8") as fh:
        graph = yaml_rt.load(fh)

    # Inject a fresh-style edge for CLUS_0768 (which IS in the
    # discovery fixture's top-K). This is the edge whose
    # property_comparisons + discovery_score will be refreshed; its
    # other fields must survive verbatim.
    target_acc = "CS20230722_CLUS_0768"
    target_edge = {
        "id": "edge_olm_to_wmb_clus_0768_test",
        "lit_type": "olm_hippocampus",
        "taxonomy_type": target_acc,
        "relationship": "evidencell:UncertainRelationship",
    }
    graph.setdefault("edges", []).insert(0, target_edge)

    # Stamp curator content. Order matters: replace whole fields not
    # individual nested entries, so the test fixture is reproducible.
    target_edge["confidence"] = "MODERATE"
    target_edge["confidence_score"] = 0.65
    target_edge["rationale"] = _CURATOR_RATIONALE
    target_edge["relationship"] = "skos:closeMatch"
    target_edge["mapping_cardinality"] = "1:1"
    target_edge["mapping_justification"] = "semapv:CompositeMatching"
    target_edge["reconciliation_note"] = _CURATOR_RECONCILIATION
    target_edge["caveats"] = [
        {
            "caveat_type": "DISTRIBUTED_ACROSS_CLUSTERS",
            "description": _CURATOR_CAVEAT,
        }
    ]
    target_edge["proposed_experiments"] = [
        "Re-map with Chrna2-Cre line to test cluster resolution."
    ]
    target_edge["unresolved_questions"] = [
        "Why does AT scatter across Sst Gaba_3 children?"
    ]
    target_edge["curator"] = "test-curator"
    target_edge["reviewed_by"] = "test-reviewer"

    # Build a fresh evidence list: a curator-authored LITERATURE item +
    # an AT item with rich source_groups[*].rationale. Both should
    # survive the refresh byte-identical.
    target_edge["evidence"] = [
        {
            "evidence_type": "LITERATURE",
            "supports": "SUPPORT",
            "explanation": "Curator-added Winterer 2019 quote",
            "reference": "PMID:31420995",
            "snippet": _LITERATURE_EVIDENCE_QUOTE,
        },
        {
            "evidence_type": "ANNOTATION_TRANSFER",
            "supports": "PARTIAL",
            "explanation": "MapMyCells annotation transfer of OLM cohort.",
            "run_ref": "at_run_test",
            "source_cluster_label": "Sst-OLM + Htr3a-OLM (combined)",
            "source_groups": [
                {
                    "label": "OLM-pooled",
                    "members": ["Sst-OLM", "Htr3a-OLM"],
                    "rationale": _CURATOR_AT_SOURCE_GROUP_RATIONALE,
                }
            ],
            "metrics_by_level": [
                {
                    "taxonomy_level": "SUPERTYPE",
                    "best_target_accession": "CS20230722_SUPT_0216",
                    "f1_score": 0.97,
                }
            ],
        },
    ]

    # Stamp a sentinel into existing property_comparisons so we can
    # detect whether they were overwritten.
    target_edge["property_comparisons"] = [
        {
            "property": "marker_mGluR1",
            "node_a_value": "mGluR1 — defining marker",
            "node_b_value": "stale value",
            "alignment": "NOT_ASSESSED",
            "notes": "STALE_SENTINEL_PC",
        }
    ]
    target_edge["discovery_score"] = {"score": -999, "stale": True}

    # Stage the graph inside kb/graphs/{region}/ because gen-facts +
    # find-candidates require that path layout
    # (paths.region_from_graph constraint). Use a non-conflicting
    # filename that won't clash with real KB graphs.
    region_dir = REPO_ROOT / "kb" / "graphs" / "hippocampus"
    staged_path = region_dir / f"_tmp_test_refresh_pc_{tmp_path.name}.yaml"
    with staged_path.open("w", encoding="utf-8") as fh:
        yaml_rt.dump(graph, fh)
    return staged_path


@pytest.mark.skipif(
    not OLM_DISCOVERY_RANK0.exists(),
    reason="OLM rank-0 discovery JSON fixture missing (run `just find-candidates` first)",
)
def test_refresh_replaces_stale_property_comparisons_only(tmp_path):
    """After refresh, the sentinel ``STALE_SENTINEL_PC`` in the
    decorated edge's property_comparisons is gone — the field was
    replaced by fresh Stage B output."""
    staged_path = _build_decorated_olm_graph(tmp_path)
    try:
        summary = refresh_property_comparisons(
            graph_file=staged_path,
            classical_node_id="olm_hippocampus",
            taxonomy_id="CCN20230722",
            rank=0,
            top_k=10,
            discovery_json_path=OLM_DISCOVERY_RANK0,
        )
        assert summary["edges_refreshed"] >= 1
        # Reload and check the sentinel is gone.
        yaml_rt = _yaml_rt()
        with staged_path.open(encoding="utf-8") as fh:
            after = yaml_rt.load(fh)
        target = next(
            e for e in after["edges"]
            if e.get("id") == "edge_olm_to_wmb_clus_0768_test"
        )
        pcs = target.get("property_comparisons") or []
        # Sentinel string MUST be gone from any pc's notes.
        for pc in pcs:
            assert (pc.get("notes") or "") != "STALE_SENTINEL_PC", \
                f"Stale sentinel survived: {pc}"
        # Fresh discovery_score must have replaced the {-999, stale} stub.
        ds = target.get("discovery_score") or {}
        assert ds.get("score") != -999, \
            f"Stale discovery_score survived: {ds}"
        # Should now have multiple marker_-prefixed PCs (Sst, Chrna2, mGluR1, …).
        marker_pcs = [
            pc for pc in pcs
            if (pc.get("property") or "").startswith("marker_")
        ]
        assert len(marker_pcs) >= 3, \
            f"Expected multiple marker rows post-refresh, got {len(marker_pcs)}"
    finally:
        if staged_path.exists():
            staged_path.unlink()


@pytest.mark.skipif(
    not OLM_DISCOVERY_RANK0.exists(),
    reason="OLM rank-0 discovery JSON fixture missing (run `just find-candidates` first)",
)
def test_refresh_preserves_evidence_and_rationale_suite_byte_identical(tmp_path):
    """Regression-locking test: refresh MUST NOT mutate any of:
    - evidence[] (including AT source_groups[*].rationale)
    - rationale-suite (confidence, rationale, etc.)
    - caveats[], proposed_experiments[], unresolved_questions[]
    - curator, reviewed_by

    If a future change to the refresh tool's scope creep accidentally
    touches these, this test fails loudly.
    """
    staged_path = _build_decorated_olm_graph(tmp_path)
    try:
        yaml_rt = _yaml_rt()
        with staged_path.open(encoding="utf-8") as fh:
            before = yaml_rt.load(fh)
        before_target = next(
            e for e in before["edges"]
            if e.get("id") == "edge_olm_to_wmb_clus_0768_test"
        )
        # Deep-copy each preservation-target field BEFORE refresh.
        before_snapshot = {
            "evidence": copy.deepcopy(before_target.get("evidence")),
            "confidence": before_target.get("confidence"),
            "confidence_score": before_target.get("confidence_score"),
            "rationale": before_target.get("rationale"),
            "relationship": before_target.get("relationship"),
            "mapping_cardinality": before_target.get("mapping_cardinality"),
            "mapping_justification": before_target.get("mapping_justification"),
            "reconciliation_note": before_target.get("reconciliation_note"),
            "caveats": copy.deepcopy(before_target.get("caveats")),
            "proposed_experiments": copy.deepcopy(
                before_target.get("proposed_experiments")
            ),
            "unresolved_questions": copy.deepcopy(
                before_target.get("unresolved_questions")
            ),
            "curator": before_target.get("curator"),
            "reviewed_by": before_target.get("reviewed_by"),
            "id": before_target.get("id"),
            "lit_type": before_target.get("lit_type"),
            "taxonomy_type": before_target.get("taxonomy_type"),
        }

        refresh_property_comparisons(
            graph_file=staged_path,
            classical_node_id="olm_hippocampus",
            taxonomy_id="CCN20230722",
            rank=0,
            top_k=10,
            discovery_json_path=OLM_DISCOVERY_RANK0,
        )

        with staged_path.open(encoding="utf-8") as fh:
            after = yaml_rt.load(fh)
        after_target = next(
            e for e in after["edges"]
            if e.get("id") == "edge_olm_to_wmb_clus_0768_test"
        )
        for key, before_val in before_snapshot.items():
            after_val = after_target.get(key)
            # Coerce ruamel CommentedMap / CommentedSeq → plain
            # dict/list for equality comparison (ruamel objects don't
            # always compare equal across reads).
            import json
            assert json.dumps(after_val, default=str, sort_keys=True) == \
                json.dumps(before_val, default=str, sort_keys=True), \
                f"Field {key!r} was mutated by refresh.\n  before: {before_val!r}\n  after:  {after_val!r}"

        # Specifically: AT evidence's source_groups[*].rationale is the
        # most-at-risk piece. Spot-check it explicitly.
        at_items = [
            ev for ev in after_target.get("evidence") or []
            if ev.get("evidence_type") == "ANNOTATION_TRANSFER"
        ]
        assert len(at_items) == 1, \
            f"Expected 1 AT evidence item; found {len(at_items)}"
        sgs = at_items[0].get("source_groups") or []
        assert len(sgs) == 1
        assert sgs[0].get("rationale") == _CURATOR_AT_SOURCE_GROUP_RATIONALE, \
            "AT source_groups rationale was mutated by refresh"

        # And: LITERATURE evidence item (curator-added) must survive
        # verbatim.
        lit_items = [
            ev for ev in after_target.get("evidence") or []
            if ev.get("evidence_type") == "LITERATURE"
        ]
        assert len(lit_items) == 1
        assert lit_items[0].get("snippet") == _LITERATURE_EVIDENCE_QUOTE
    finally:
        if staged_path.exists():
            staged_path.unlink()


@pytest.mark.skipif(
    not OLM_DISCOVERY_RANK0.exists(),
    reason="OLM rank-0 discovery JSON fixture missing",
)
def test_refresh_dry_run_does_not_mutate_disk(tmp_path):
    """With dry_run=True, the graph file on disk is not modified even
    when matched edges would otherwise be refreshed."""
    staged_path = _build_decorated_olm_graph(tmp_path)
    try:
        before_bytes = staged_path.read_bytes()
        summary = refresh_property_comparisons(
            graph_file=staged_path,
            classical_node_id="olm_hippocampus",
            taxonomy_id="CCN20230722",
            rank=0,
            top_k=10,
            discovery_json_path=OLM_DISCOVERY_RANK0,
            dry_run=True,
        )
        assert summary["dry_run"] is True
        assert summary["edges_refreshed"] >= 1
        # Disk untouched.
        assert staged_path.read_bytes() == before_bytes
    finally:
        if staged_path.exists():
            staged_path.unlink()


@pytest.mark.skipif(
    not OLM_DISCOVERY_RANK0.exists(),
    reason="OLM rank-0 discovery JSON fixture missing",
)
def test_refresh_matches_by_biological_identity_not_edge_id(tmp_path):
    """Legacy lowercase-accession edges with ad-hoc IDs (e.g.
    ``edge_olm_to_wmb_clus_0769``) must be matched and refreshed
    despite NOT matching the current emitter's ID format. The match
    key is (lit_type, taxonomy_type), not edge.id."""
    yaml_rt = _yaml_rt()
    # Construct a minimal graph with two edges: one with the legacy
    # ID format, one with the fresh ID format. Both target CLUS_0768.
    # The legacy one targets the SAME taxonomy_type, so refresh
    # should hit BOTH (they're "duplicates" by biological identity).
    region_dir = REPO_ROOT / "kb" / "graphs" / "hippocampus"
    staged_path = region_dir / f"_tmp_test_id_match_{tmp_path.name}.yaml"

    # Copy the real OLM graph and inject a legacy-style edge.
    with OLM_GRAPH.open(encoding="utf-8") as fh:
        graph = yaml_rt.load(fh)
    legacy_edge = {
        "id": "edge_olm_to_wmb_clus_0768_legacy",
        "lit_type": "olm_hippocampus",
        "taxonomy_type": "CS20230722_CLUS_0768",
        "relationship": "evidencell:UncertainRelationship",
        "property_comparisons": [
            {
                "property": "marker_Sst",
                "alignment": "NOT_ASSESSED",
                "notes": "LEGACY_STALE_SENTINEL",
            }
        ],
        "evidence": [],
    }
    graph.setdefault("edges", []).insert(0, legacy_edge)
    with staged_path.open("w", encoding="utf-8") as fh:
        yaml_rt.dump(graph, fh)

    try:
        refresh_property_comparisons(
            graph_file=staged_path,
            classical_node_id="olm_hippocampus",
            taxonomy_id="CCN20230722",
            rank=0,
            top_k=10,
            discovery_json_path=OLM_DISCOVERY_RANK0,
        )
        with staged_path.open(encoding="utf-8") as fh:
            after = yaml_rt.load(fh)
        # The legacy edge MUST have been refreshed despite its
        # non-canonical ID. Look it up by ID.
        legacy_after = next(
            e for e in after["edges"]
            if e.get("id") == "edge_olm_to_wmb_clus_0768_legacy"
        )
        pcs = legacy_after.get("property_comparisons") or []
        # Sentinel string MUST be gone (replaced by fresh Stage B output).
        for pc in pcs:
            assert (pc.get("notes") or "") != "LEGACY_STALE_SENTINEL", \
                f"Stale sentinel survived on legacy-ID edge: {pc}"
        assert any(
            (pc.get("property") or "").startswith("marker_")
            for pc in pcs
        ), "Legacy edge's pcs not refreshed (no marker rows after)"
    finally:
        if staged_path.exists():
            staged_path.unlink()
