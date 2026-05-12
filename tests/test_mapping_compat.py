"""Phase 2 schema-overhaul back-compat shim tests.

Exercises ``src/evidencell/_mapping_compat.py`` — the read-path shim
that lets PR1 code work against both old (``type_a`` / ``type_b`` /
``EQUIVALENT`` / ``TYPE_A_SPLITS`` / ...) and new (``lit_type`` /
``taxonomy_type`` / ``skos:exactMatch`` / ``skos:broadMatch`` /
``mapping_cardinality``) MappingEdge shapes.

When PR2 lands and the KB sweep migrates every edge to the new shape,
this file inverts its assertions: old field names + old enum values
must no longer be accepted (and the shim module is deleted). The
existence of this test file is the canary for that PR2 chore.
"""

from __future__ import annotations

import warnings

import pytest

from evidencell import _mapping_compat


@pytest.fixture(autouse=True)
def _clear_warn_cache():
    """The shim deduplicates DeprecationWarnings by message string
    across the process. Tests that assert the warning fires need a
    clean cache, otherwise an earlier test in the suite shadows them."""
    _mapping_compat._warned_field_names.clear()
    yield
    _mapping_compat._warned_field_names.clear()


# ──────────────────────────────────────────────────────────────────
# Field-name shim
# ──────────────────────────────────────────────────────────────────


def test_lit_type_prefers_new_name():
    edge = {"lit_type": "olm_cell_ca1", "type_a": "should_be_ignored"}
    assert _mapping_compat.lit_type(edge) == "olm_cell_ca1"


def test_lit_type_falls_back_to_old_name():
    edge = {"type_a": "olm_cell_ca1"}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = _mapping_compat.lit_type(edge)
    assert result == "olm_cell_ca1"
    assert any(
        issubclass(w.category, DeprecationWarning) and "type_a" in str(w.message)
        for w in caught
    )


def test_lit_type_returns_none_when_neither_present():
    edge = {"id": "e1"}
    assert _mapping_compat.lit_type(edge) is None


def test_taxonomy_type_prefers_new_name():
    edge = {"taxonomy_type": "CS20230722_SUPT_0216", "type_b": "ignored"}
    assert _mapping_compat.taxonomy_type(edge) == "CS20230722_SUPT_0216"


def test_taxonomy_type_falls_back_to_old_name():
    edge = {"type_b": "CS20230722_SUPT_0216"}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result = _mapping_compat.taxonomy_type(edge)
    assert result == "CS20230722_SUPT_0216"
    assert any(
        issubclass(w.category, DeprecationWarning) and "type_b" in str(w.message)
        for w in caught
    )


# ──────────────────────────────────────────────────────────────────
# Relationship-value shim
# ──────────────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "old_value, expected_curie, expected_cardinality",
    [
        ("EQUIVALENT",        "skos:exactMatch",                    None),
        ("PARTIAL_OVERLAP",   "evidencell:PartialOverlapMatch",     None),
        ("CROSS_CUTTING",     "evidencell:CrossCuttingMatch",       None),
        ("NO_CORRESPONDENCE", "evidencell:NoCorrespondence",        None),
        ("TYPE_A_SPLITS",     "skos:broadMatch",                    "1:n"),
        ("TYPE_A_MERGES",     "skos:narrowMatch",                   "n:1"),
        ("SUBSET",            "skos:broadMatch",                    "1:1"),
        ("SUPERSET",          "skos:narrowMatch",                   "n:1"),
        ("OVERLAPS",          "skos:closeMatch",                    None),
        ("CANDIDATE_SYNONYM", "skos:closeMatch",                    None),
    ],
)
def test_normalise_relationship_remaps_deprecated(
    old_value, expected_curie, expected_cardinality,
):
    edge = {"relationship": old_value}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rel, cardinality = _mapping_compat.normalise_relationship(edge)
    assert rel == expected_curie
    assert cardinality == expected_cardinality


def test_normalise_relationship_uncertain_blanks_out():
    edge = {"relationship": "UNCERTAIN"}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rel, cardinality = _mapping_compat.normalise_relationship(edge)
    assert rel == ""
    assert cardinality is None


def test_normalise_relationship_passes_curie_unchanged():
    edge = {
        "relationship": "skos:broadMatch",
        "mapping_cardinality": "1:n",
    }
    rel, cardinality = _mapping_compat.normalise_relationship(edge)
    assert rel == "skos:broadMatch"
    assert cardinality == "1:n"


def test_normalise_relationship_explicit_cardinality_wins_over_implied():
    # If a KB edge writes both a deprecated value AND an explicit
    # cardinality, prefer the explicit one over the value-implied one.
    edge = {"relationship": "TYPE_A_SPLITS", "mapping_cardinality": "1:1"}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rel, cardinality = _mapping_compat.normalise_relationship(edge)
    assert rel == "skos:broadMatch"
    assert cardinality == "1:1"


def test_normalise_relationship_returns_none_when_absent():
    edge = {"id": "e1"}
    rel, cardinality = _mapping_compat.normalise_relationship(edge)
    assert rel is None
    assert cardinality is None


# ──────────────────────────────────────────────────────────────────
# Display helpers
# ──────────────────────────────────────────────────────────────────


def test_display_relationship_with_cardinality():
    assert _mapping_compat.display_relationship(
        "skos:broadMatch", "1:n",
    ) == "skos:broadMatch (1:n)"


def test_display_relationship_without_cardinality():
    assert _mapping_compat.display_relationship(
        "skos:exactMatch",
    ) == "skos:exactMatch"


def test_display_relationship_handles_missing():
    assert _mapping_compat.display_relationship(None) == "(no relationship)"
    assert _mapping_compat.display_relationship("") == "(no relationship)"
