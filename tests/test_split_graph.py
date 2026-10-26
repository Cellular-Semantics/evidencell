"""Tests for the connected-component KB graph splitter."""

from pathlib import Path

import pytest
import yaml
from ruamel.yaml import YAML

from evidencell.split_graph import (
    build_component_doc,
    plan_split,
    split_file,
    verify_conservation,
)


def _doc(nodes, edges, **extra):
    base = {
        "name": "test",
        "target_atlas": "WMBv1",
        "nodes": nodes,
        "edges": edges,
    }
    base.update(extra)
    return base


def _atlas(node_id):
    return {
        "id": node_id,
        "name": node_id,
        "definition_basis": "ATLAS_TRANSCRIPTOMIC",
        "taxonomy_id": "CCN20230722",
        "cell_set_accession": node_id.upper(),
    }


def _classical(node_id, basis="CLASSICAL_MULTIMODAL"):
    return {"id": node_id, "name": node_id, "definition_basis": basis}


def _edge(edge_id, a, b):
    return {"id": edge_id, "lit_type": a, "taxonomy_type": b}


def test_independent_classical_types_split():
    doc = _doc(
        [_classical("a"), _classical("b"), _atlas("x"), _atlas("y")],
        [_edge("e1", "a", "x"), _edge("e2", "b", "y")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert [c.representative for c in plan.components] == ["a", "b"]
    assert [c.node_ids for c in plan.components] == [["a"], ["b"]]


def test_lit_to_lit_edge_keeps_component_whole():
    """A classical type joined to a PRIOR_TRANSCRIPTOMIC node is one unit.

    This is the cerebellum shape: classical -> study T-type -> atlas cluster.
    Splitting per classical type would strand the middle node and break the
    in-document endpoint rule.
    """
    doc = _doc(
        [
            _classical("classical_candelabrum"),
            _classical("pli1_osorno", "PRIOR_TRANSCRIPTOMIC"),
            _atlas("wmb_cluster_5178"),
        ],
        [
            # exactMatch: Osorno asserts PLI1 *is* the candelabrum cell. Settled
            # structure, so the two stay in one file.
            _rel_edge("e1", "classical_candelabrum", "pli1_osorno", "skos:exactMatch"),
            _edge("e2", "pli1_osorno", "wmb_cluster_5178"),
        ],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert len(plan.components) == 1
    assert plan.components[0].node_ids == ["classical_candelabrum", "pli1_osorno"]
    assert plan.is_noop


def test_chain_of_three_non_atlas_nodes_stays_one_component():
    """A subdivision chain is one unit -- union-find is transitive."""
    doc = _doc(
        [_classical("a"), _classical("b"), _classical("c"), _atlas("x")],
        [
            _rel_edge("e1", "a", "b", "skos:narrowMatch"),
            _rel_edge("e2", "b", "c", "skos:narrowMatch"),
            _edge("e3", "c", "x"),
        ],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert len(plan.components) == 1
    assert plan.components[0].node_ids == ["a", "b", "c"]


def test_orphan_atlas_stub_is_reported_not_dropped_silently():
    doc = _doc(
        [_classical("a"), _atlas("x"), _atlas("unreferenced")],
        [_edge("e1", "a", "x")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert plan.orphan_atlas == ["unreferenced"]


def test_edgeless_classical_node_becomes_its_own_component():
    """Unmapped literature types are valid content and must survive.

    Every non-atlas node is placed in a component by construction, so an
    edgeless one becomes a single-node component rather than being dropped.
    """
    doc = _doc([_classical("a"), _classical("lonely")], [])
    plan = plan_split(doc, Path("t.yaml"))
    assert [c.representative for c in plan.components] == ["a", "lonely"]
    assert verify_conservation(doc, plan) == []


def test_file_with_no_components_is_a_noop():
    """A stub dump or an atlas-to-atlas crosswalk has nothing to split."""
    doc = _doc([_atlas("x"), _atlas("y")], [])
    plan = plan_split(doc, Path("t.yaml"))
    assert plan.components == []
    assert plan.is_noop
    assert plan.orphan_atlas == ["x", "y"]


def test_refuses_to_split_when_edges_would_be_lost():
    """An atlas-to-atlas crosswalk belongs to no component, so its edges have
    nowhere to go. Conservation must catch that before anything is written."""
    doc = _doc(
        [_atlas("x"), _atlas("y")],
        [_edge("e1", "x", "y")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    problems = verify_conservation(doc, plan)
    assert problems and "edges lost" in problems[0]


def test_component_doc_carries_stubs_and_header_keys():
    doc = _doc(
        [_classical("a"), _atlas("x")],
        [_edge("e1", "a", "x")],
        brain_region={"id": "UBERON:0000955", "label": "brain"},
        species={"id": "NCBITaxon:10090", "label": "Mus musculus"},
    )
    plan = plan_split(doc, Path("t.yaml"))
    out = build_component_doc(doc, plan.components[0])
    assert [n["id"] for n in out["nodes"]] == ["a", "x"]
    assert [e["id"] for e in out["edges"]] == ["e1"]
    assert out["brain_region"]["id"] == "UBERON:0000955"
    assert out["target_atlas"] == "WMBv1"


def test_every_emitted_edge_resolves_in_document():
    doc = _doc(
        [_classical("a"), _classical("b"), _atlas("x"), _atlas("y")],
        [_edge("e1", "a", "x"), _edge("e2", "b", "y")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert verify_conservation(doc, plan) == []
    for component in plan.components:
        out = build_component_doc(doc, component)
        ids = {n["id"] for n in out["nodes"]}
        for edge in out["edges"]:
            assert edge["lit_type"] in ids
            assert edge["taxonomy_type"] in ids


def test_split_preserves_comments(tmp_path):
    source = tmp_path / "src.yaml"
    source.write_text(
        "# curatorial header\n"
        "name: test\n"
        "target_atlas: WMBv1\n"
        "nodes:\n"
        "  - id: a\n"
        "    name: a\n"
        "    definition_basis: CLASSICAL_MULTIMODAL\n"
        "  - id: b\n"
        "    name: b\n"
        "    definition_basis: CLASSICAL_MULTIMODAL\n"
        "edges: []\n",
        encoding="utf-8",
    )
    split_file(source, dry_run=False, out_dir=tmp_path)
    assert "# curatorial header" in (tmp_path / "a.yaml").read_text(encoding="utf-8")
    assert "# curatorial header" in (tmp_path / "b.yaml").read_text(encoding="utf-8")


def test_split_refuses_to_overwrite(tmp_path):
    source = tmp_path / "src.yaml"
    y = YAML()
    with source.open("w", encoding="utf-8") as fh:
        y.dump(_doc([_classical("a"), _classical("b")], []), fh)
    (tmp_path / "a.yaml").write_text("pre-existing\n", encoding="utf-8")
    with pytest.raises(FileExistsError):
        split_file(source, dry_run=False, out_dir=tmp_path)
    assert (tmp_path / "a.yaml").read_text(encoding="utf-8") == "pre-existing\n"


def test_dry_run_writes_nothing(tmp_path):
    source = tmp_path / "src.yaml"
    y = YAML()
    with source.open("w", encoding="utf-8") as fh:
        y.dump(_doc([_classical("a"), _classical("b")], []), fh)
    split_file(source, dry_run=True, out_dir=tmp_path)
    assert sorted(p.name for p in tmp_path.iterdir()) == ["src.yaml"]


def test_real_cerebellum_split_conserves_content():
    """The pilot files, end to end, against real curated content."""
    for name in ("classical_candelabrum", "classical_globular", "classical_lugaro"):
        path = Path("kb/graphs/cerebellum") / f"{name}.yaml"
        if not path.exists():
            pytest.skip("cerebellum split not applied in this tree")
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        plan = plan_split(doc, path)
        assert plan.is_noop, f"{name} should already be one whole component"
        assert verify_conservation(doc, plan) == []


# ── Component naming ──────────────────────────────────────────────────────────

def _lit(node_id):
    return {"id": node_id, "name": node_id, "definition_basis": "CLASSICAL_MULTIMODAL"}


def _rel_edge(edge_id, a, b, rel):
    return {"id": edge_id, "lit_type": a, "taxonomy_type": b, "relationship": rel}


def test_component_named_after_broadest_member():
    """A general type plus its subtypes should take the general type's name.

    Alphabetical naming would call the O-LM family file
    `chrna2_olm_subfamily_chamberland.yaml`, which misrepresents it.
    """
    doc = _doc(
        [_lit("olm_cell_ca1"), _lit("chrna2_sub"), _lit("ndnf_sub")],
        [
            _rel_edge("e1", "chrna2_sub", "olm_cell_ca1", "skos:broadMatch"),
            _rel_edge("e2", "ndnf_sub", "olm_cell_ca1", "skos:broadMatch"),
        ],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert len(plan.components) == 1
    assert plan.components[0].representative == "olm_cell_ca1"


def test_narrow_match_orients_the_other_way():
    """`A --narrowMatch--> B` makes A the broader of the two."""
    doc = _doc(
        [_lit("general"), _lit("aaa_specific")],
        [_rel_edge("e1", "general", "aaa_specific", "skos:narrowMatch")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert plan.components[0].representative == "general"


def test_ambiguous_breadth_falls_back_to_alphabetical():
    """Two roots, or none, is arbitrary -- prefer stable over misleading."""
    doc = _doc(
        [_lit("bbb"), _lit("aaa")],
        [_rel_edge("e1", "aaa", "bbb", "skos:closeMatch")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert plan.components[0].representative == "aaa"


def test_breadth_edges_outside_the_component_are_ignored():
    """Only in-component breadth orders the members."""
    doc = _doc(
        [_lit("aaa"), _lit("zzz"), _atlas("x")],
        [
            _rel_edge("e1", "aaa", "zzz", "skos:broadMatch"),
            _rel_edge("e2", "aaa", "x", "skos:broadMatch"),
        ],
    )
    plan = plan_split(doc, Path("t.yaml"))
    assert plan.components[0].representative == "zzz"


# ── Co-location policy ────────────────────────────────────────────────────────

def _two_lit(rel):
    return _doc(
        [_lit("general"), _lit("other"), _atlas("x")],
        [
            _rel_edge("e1", "other", "general", rel),
            _edge("e2", "general", "x"),
        ],
    )


@pytest.mark.parametrize("rel", ["skos:broadMatch", "skos:narrowMatch", "skos:exactMatch"])
def test_settled_relations_co_locate(rel):
    """Subdivision and asserted identity are settled structure."""
    plan = plan_split(_two_lit(rel), Path("t.yaml"))
    assert len(plan.components) == 1
    assert sorted(plan.components[0].node_ids) == ["general", "other"]


@pytest.mark.parametrize("rel", [
    "skos:closeMatch",
    "evidencell:CrossCuttingMatch",
    "evidencell:UncertainRelationship",
])
def test_open_questions_do_not_co_locate(rel):
    """A hypothesis under review must not dictate file layout.

    Keying layout to a candidate makes files churn as candidates are raised and
    dropped, and co-location visually asserts the thing being questioned. This
    is also what stops an automatic Case A closeMatch from fusing two files.
    """
    plan = plan_split(_two_lit(rel), Path("t.yaml"))
    assert len(plan.components) == 2
    assert [sorted(c.node_ids) for c in plan.components] == [["general"], ["other"]]


def test_non_co_locating_edge_gets_a_thin_lit_stub():
    """The far endpoint is a placeholder, not a second copy of the record."""
    doc = _doc(
        [
            {"id": "a", "name": "A", "definition_basis": "CLASSICAL_MULTIMODAL",
             "defining_markers": [{"symbol": "Sst"}], "notes": "lots of curated content"},
            {"id": "b", "name": "B", "definition_basis": "CLASSICAL_MULTIMODAL",
             "defining_markers": [{"symbol": "Pvalb"}], "notes": "also lots"},
        ],
        [_rel_edge("e1", "a", "b", "skos:closeMatch")],
    )
    plan = plan_split(doc, Path("t.yaml"))
    by_rep = {c.representative: build_component_doc(doc, c) for c in plan.components}

    # the edge travels with its source
    assert [e["id"] for e in by_rep["a"]["edges"]] == ["e1"]
    assert by_rep["b"]["edges"] == []

    stub = [n for n in by_rep["a"]["nodes"] if n["id"] == "b"][0]
    assert stub["reference_stub"] == "LIT_TYPE"
    assert "defining_markers" not in stub, "a lit stub must not carry content"
    assert "notes" not in stub
    # and the canonical record is untouched in its own file
    canon = [n for n in by_rep["b"]["nodes"] if n["id"] == "b"][0]
    assert canon["defining_markers"] == [{"symbol": "Pvalb"}]
    assert "reference_stub" not in canon


def test_splitting_is_idempotent_over_lit_stubs():
    """Re-splitting an already-split file must not rebuild the component.

    A lit stub carries its type's real definition_basis, so without
    `reference_stub` is_stub() would read it as a member and re-absorb it.
    """
    doc = _doc(
        [_lit("a"), _lit("b")],
        [_rel_edge("e1", "a", "b", "skos:closeMatch")],
    )
    first = plan_split(doc, Path("t.yaml"))
    a_doc = build_component_doc(doc, [c for c in first.components if c.representative == "a"][0])
    again = plan_split(dict(a_doc), Path("a.yaml"))
    assert len(again.components) == 1
    assert again.components[0].node_ids == ["a"], "the lit stub was treated as a member"
