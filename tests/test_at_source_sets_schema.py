"""Schema + model coverage for the `at_source_sets` node property
(issue #126): the LinkML schema declares AtSourceSet / CorrespondenceType /
CellTypeNode.at_source_sets, and the generated Pydantic models round-trip a
node carrying them.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from evidencell._models import AtSourceSet, CellTypeNode, CorrespondenceType

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "schema" / "celltype_mapping.yaml"


def test_schema_declares_at_source_sets():
    """The LinkML schema (source of truth) declares the new class, enum, and
    slot — independent of the generated Pydantic models."""
    sv = pytest.importorskip("linkml_runtime").SchemaView(str(SCHEMA))
    assert "AtSourceSet" in sv.all_classes()
    assert "CorrespondenceType" in sv.all_enums()
    corr = sv.get_enum("CorrespondenceType")
    assert set(corr.permissible_values) == {"EXACT", "PARTIAL", "SUPERSET", "SUBSET"}

    at = sv.get_class("AtSourceSet")
    attrs = at.attributes
    assert attrs["dataset_accession"].required
    assert attrs["source_label"].required
    assert attrs["correspondence"].range == "CorrespondenceType"
    assert attrs["sources"].range == "PropertySource"
    assert attrs["sources"].multivalued

    node = sv.get_class("CellTypeNode")
    slot = node.attributes["at_source_sets"]
    assert slot.range == "AtSourceSet"
    assert slot.multivalued


def test_model_round_trips_at_source_sets():
    node = CellTypeNode(
        id="amygdala_intercalated_cell",
        name="Amygdala intercalated cell",
        definition_basis="CLASSICAL_MULTIMODAL",
        at_source_sets=[
            {
                "dataset_accession": "ArrayExpress:E-MTAB-12096",
                "source_label": "GABA-3-Foxp2_Col6a1",
                "correspondence": "SUBSET",
                "sources": [
                    {"ref": "PMID:37884748", "method": "scRNA-seq cluster annotation",
                     "scope": "mouse amygdala, Hochgerner 2023",
                     "quote_key": "37884748_deadbeef"},
                ],
                "notes": "One of four Foxp2 ITC clusters.",
            },
        ],
    )
    assert len(node.at_source_sets) == 1
    entry = node.at_source_sets[0]
    assert isinstance(entry, AtSourceSet)
    assert entry.correspondence == CorrespondenceType.SUBSET
    assert entry.sources[0].quote_key == "37884748_deadbeef"

    # Round-trip through dict.
    reloaded = CellTypeNode(**node.model_dump(exclude_none=True))
    assert reloaded.at_source_sets[0].source_label == "GABA-3-Foxp2_Col6a1"


def test_correspondence_required_fields_enforced():
    with pytest.raises(Exception):
        AtSourceSet(source_label="only-label")  # missing dataset_accession
