"""Tests for the taxonomy registry."""

import pytest

from annotation_transfer.taxonomies import (
    TaxonomySpec,
    get_taxonomy,
    list_taxonomies,
    save_taxonomy,
    TaxonomyError,
)


def test_get_builtin_taxonomy():
    spec = get_taxonomy("CCN20230722")
    assert spec.id == "CCN20230722"
    assert spec.species == "mouse"
    assert spec.web_ref_id == "10xGene"
    assert "HierarchicalAlgorithmRun" in spec.algorithms


def test_get_unknown_taxonomy():
    with pytest.raises(TaxonomyError, match="Unknown taxonomy"):
        get_taxonomy("NONEXISTENT")


def test_list_taxonomies():
    specs = list_taxonomies()
    ids = {s.id for s in specs}
    assert "CCN20230722" in ids
    assert "CCN202210140" in ids
    assert "CCN20230505" in ids
    assert "CCN20250428" in ids


def test_save_and_load(tmp_path):
    spec = TaxonomySpec(
        id="TEST001",
        name="Test Taxonomy",
        species="mouse",
        web_ref_id="test_ref",
        preferred_backend="web",
    )
    path = save_taxonomy(spec, taxonomy_dir=tmp_path)
    assert path.exists()

    loaded = get_taxonomy("TEST001", taxonomy_dir=tmp_path)
    assert loaded.id == "TEST001"
    assert loaded.preferred_backend == "web"
    assert loaded.web_ref_id == "test_ref"


def test_persisted_overrides_builtin(tmp_path):
    """A persisted spec should take precedence over built-in."""
    spec = get_taxonomy("CCN20230722")
    spec.preferred_backend = "local"
    save_taxonomy(spec, taxonomy_dir=tmp_path)

    loaded = get_taxonomy("CCN20230722", taxonomy_dir=tmp_path)
    assert loaded.preferred_backend == "local"


def test_all_builtins_have_web_ref_id():
    for spec in list_taxonomies():
        assert spec.web_ref_id is not None, f"{spec.id} missing web_ref_id"
