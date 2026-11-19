"""Tests for evidencell.schema_subset and the ingest_phase annotations."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from evidencell.paths import repo_root
from evidencell.schema_subset import OMIT, PHASES, render_subset

SCHEMA = repo_root() / "schema/celltype_mapping.yaml"


@pytest.fixture(scope="module")
def subset_path(tmp_path_factory) -> Path:
    path = tmp_path_factory.mktemp("subset") / "subset.yaml"
    path.write_text(render_subset())
    return path


@pytest.fixture(scope="module")
def subset(subset_path) -> SchemaView:
    return SchemaView(str(subset_path))


def test_subset_is_self_contained(subset):
    known = set(subset.all_classes()) | set(subset.all_enums()) | set(subset.all_types())
    for cls in subset.all_classes():
        for slot in subset.class_induced_slots(cls):
            refs = [slot.range] + [b.range for b in slot.bindings or []]
            for ref in refs:
                assert ref in known, f"{cls}.{slot.name} -> {ref} missing from subset"


def test_subset_carries_binding_enums_and_drops_omitted_slots(subset):
    # Binding ranges are never a slot's declared range; a walk over ranges
    # alone misses them, and an agent then cannot see which ontology applies.
    assert {"AnatomyTerm", "CLClassTerm", "NCBITaxonClassTerm"} <= set(subset.all_enums())
    for cls, slots in OMIT.items():
        assert not slots & set(subset.class_slots(cls))
    assert "MappingEdge" not in subset.all_classes()


def _kb_instances():
    """(path, target_class, instance) for every node the KB holds.

    Node-only files validate whole. Files with edges or AT datasets validate
    node by node, since the subset omits those graph slots.
    """
    for path in sorted((repo_root() / "kb/graphs").rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        if doc.get("edges") == []:
            doc.pop("edges")
        if any(doc.get(slot) for slot in OMIT["CellTypeMappingGraph"]):
            for node in doc.get("nodes") or []:
                yield path, "CellTypeNode", node
        else:
            yield path, "CellTypeMappingGraph", doc


def test_every_kb_node_validates_against_subset(subset_path):
    # The completeness check: anything the subset lacks that a real node uses
    # fails here, so an agent is never handed a subset the KB contradicts.
    validator = Validator(str(subset_path),
                          validation_plugins=[JsonschemaValidationPlugin(closed=True)])
    failures = {}
    count = 0
    for path, target, instance in _kb_instances():
        count += 1
        msgs = [r.message for r in validator.validate(instance, target_class=target).results]
        if msgs:
            failures.setdefault(str(path.relative_to(repo_root())), msgs[:2])
    assert count > 100
    assert not failures, failures


def test_subset_validator_rejects_bad_node(subset_path):
    # Guards against a validator that passes everything (no plugins, wrong class).
    validator = Validator(str(subset_path),
                          validation_plugins=[JsonschemaValidationPlugin(closed=True)])
    bad = {"id": "x", "name": "x", "definition_basis": "NOT_A_BASIS"}
    assert validator.validate(bad, target_class="CellTypeNode").results


def test_ingest_phase_tags():
    sv = SchemaView(str(SCHEMA))
    tagged: dict[str, list[str]] = {}
    for cls in sv.all_classes():
        for slot in sv.class_induced_slots(cls):
            ann = slot.annotations or {}
            if "ingest_phase" in ann:
                assert cls == "CellTypeNode", f"{cls}.{slot.name}: phases tag node slots only"
                tagged.setdefault(str(ann["ingest_phase"].value), []).append(slot.name)
    assert set(tagged) == set(PHASES)
    assert tagged["classification"] == ["cl_mapping"]
    assert {"name", "synonyms", "definition_basis", "species"} == set(tagged["identity"])


def test_schema_names_no_tools():
    # Which lookup tool to use belongs to the workflow, not the schema.
    text = SCHEMA.read_text()
    found = re.findall(r"OLS4|NodeNormalization|mcp__|[Ll]ook up via", text)
    assert not found, found
