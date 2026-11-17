"""Tests for evidencell.schema_slice and the ingest-question annotations it reads."""

from __future__ import annotations

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from evidencell.paths import repo_root
from evidencell.schema_slice import PHASES, phase_slots, render_slice


@pytest.fixture(scope="module")
def sv() -> SchemaView:
    return SchemaView(str(repo_root() / "schema/celltype_mapping.yaml"))


def _annotated(sv: SchemaView):
    for cls in sv.all_classes():
        for s in sv.class_induced_slots(cls):
            ann = s.annotations or {}
            if "ingest_question" in ann or "ingest_phase" in ann:
                yield cls, s.name, ann


def test_every_question_has_a_valid_phase_and_vice_versa(sv):
    # A question without a phase is never rendered; a phase without a question
    # renders an empty prompt. Either is a silent gap in agent guidance.
    seen = list(_annotated(sv))
    assert seen
    for cls, slot, ann in seen:
        assert "ingest_question" in ann, f"{cls}.{slot}: ingest_phase without question"
        assert "ingest_phase" in ann, f"{cls}.{slot}: ingest_question without phase"
        assert ann["ingest_phase"].value in PHASES, f"{cls}.{slot}: unknown phase"


@pytest.mark.parametrize("phase", PHASES)
def test_slice_lists_every_slot_of_its_phase(sv, phase):
    out = render_slice(phase)
    slots = phase_slots(sv, "CellTypeNode", phase)
    assert slots
    for s in slots:
        assert f"### `{s.name}`" in out


def test_phases_partition_the_questions(sv):
    identity = {s.name for s in phase_slots(sv, "CellTypeNode", "identity")}
    properties = {s.name for s in phase_slots(sv, "CellTypeNode", "properties")}
    assert not identity & properties
    assert {"name", "definition_basis", "species"} <= identity
    assert {"defining_markers", "anatomical_location", "notes"} <= properties


def test_unannotated_slots_are_left_out():
    out = render_slice("properties")
    assert "`precomputed_expression`" not in out
    assert "`cell_set_accession`" not in out


def test_enum_values_are_rendered():
    out = render_slice("identity")
    assert "`CLASSICAL_ANATOMICAL`" in out
    assert "`PRIOR_TRANSCRIPTOMIC`" in out


def test_nested_class_shapes_and_their_questions_are_rendered():
    out = render_slice("properties")
    assert "### MarkerSource" in out
    assert "### PropertySource" in out
    # marker_type is a properties-phase question on a nested class
    marker = out.split("### MarkerSource", 1)[1]
    assert "`marker_type`" in marker
    assert "**Question:**" in marker
    assert "`NOT_STATED`" in marker


def test_identity_slice_does_not_carry_property_questions():
    out = render_slice("identity")
    assert "### `defining_markers`" not in out
    assert "How was the marker detected" not in out


def test_unknown_phase_is_rejected():
    with pytest.raises(ValueError, match="phase must be one of"):
        render_slice("everything")
