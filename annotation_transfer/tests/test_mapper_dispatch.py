"""Tests for the mapper strategy dispatcher."""

import pytest
from pathlib import Path

from annotation_transfer.mapper import resolve_backend, MappingBackend, MapperError
from annotation_transfer.taxonomies import TaxonomySpec


def _spec(**overrides) -> TaxonomySpec:
    defaults = dict(
        id="TEST",
        name="Test",
        species="mouse",
        web_ref_id="test_ref",
        local_stats_path=None,
        local_markers_path=None,
        preferred_backend="auto",
    )
    defaults.update(overrides)
    return TaxonomySpec(**defaults)


def test_explicit_web():
    spec = _spec()
    assert resolve_backend(spec, Path("f.h5ad"), MappingBackend.WEB) == MappingBackend.WEB


def test_explicit_local():
    spec = _spec()
    assert resolve_backend(spec, Path("f.h5ad"), MappingBackend.LOCAL) == MappingBackend.LOCAL


def test_preferred_local_with_files():
    spec = _spec(
        preferred_backend="local",
        local_stats_path="/tmp/stats.h5",
        local_markers_path="/tmp/markers.json",
    )
    assert resolve_backend(spec, Path("f.h5ad")) == MappingBackend.LOCAL


def test_preferred_local_missing_files_falls_back():
    spec = _spec(preferred_backend="local")
    with pytest.warns(match="files not downloaded"):
        result = resolve_backend(spec, Path("f.h5ad"))
    assert result == MappingBackend.WEB


def test_preferred_web():
    spec = _spec(preferred_backend="web", web_ref_id="test")
    assert resolve_backend(spec, Path("f.h5ad")) == MappingBackend.WEB


def test_preferred_web_no_ref_falls_back():
    spec = _spec(preferred_backend="web", web_ref_id=None)
    with pytest.warns(match="no web_ref_id"):
        result = resolve_backend(spec, Path("f.h5ad"))
    assert result == MappingBackend.LOCAL


def test_auto_prefers_web():
    spec = _spec(preferred_backend="auto", web_ref_id="test")
    assert resolve_backend(spec, Path("f.h5ad")) == MappingBackend.WEB


def test_auto_local_fallback():
    spec = _spec(
        preferred_backend="auto",
        web_ref_id=None,
        local_stats_path="/tmp/stats.h5",
        local_markers_path="/tmp/markers.json",
    )
    assert resolve_backend(spec, Path("f.h5ad")) == MappingBackend.LOCAL


def test_auto_nothing_available():
    spec = _spec(preferred_backend="auto", web_ref_id=None)
    with pytest.raises(MapperError, match="neither web API nor local"):
        resolve_backend(spec, Path("f.h5ad"))
