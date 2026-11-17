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


# ─── query normalisation plumbing ─────────────────────────────────────


def _save_spec(tmp_path, **overrides):
    from annotation_transfer.taxonomies import save_taxonomy

    spec = _spec(**overrides)
    save_taxonomy(spec, taxonomy_dir=tmp_path)
    return spec


def test_run_mapmycells_passes_normalization_to_cli(tmp_path, monkeypatch):
    """The flag must reach --type_assignment.normalization; a mismatch
    between the declared and actual scale does not raise, it silently
    degrades every call."""
    from annotation_transfer import mapper_local

    captured: dict = {}

    class _Result:
        returncode = 0
        stdout = ""
        stderr = ""

    def fake_run(cmd, **kwargs):
        captured["cmd"] = cmd
        return _Result()

    monkeypatch.setattr(mapper_local.subprocess, "run", fake_run)
    mapper_local.run_mapmycells(
        tmp_path / "q.h5ad",
        tmp_path / "stats.h5",
        tmp_path / "markers.json",
        tmp_path / "out.json",
        normalization="log2CPM",
    )
    cmd = captured["cmd"]
    idx = cmd.index("--type_assignment.normalization")
    assert cmd[idx + 1] == "log2CPM"


def test_run_mapmycells_defaults_to_raw(tmp_path, monkeypatch):
    from annotation_transfer import mapper_local

    captured: dict = {}

    class _Result:
        returncode = 0
        stdout = ""
        stderr = ""

    monkeypatch.setattr(
        mapper_local.subprocess, "run",
        lambda cmd, **kw: (captured.update(cmd=cmd), _Result())[1],
    )
    mapper_local.run_mapmycells(
        tmp_path / "q.h5ad",
        tmp_path / "stats.h5",
        tmp_path / "markers.json",
        tmp_path / "out.json",
    )
    cmd = captured["cmd"]
    assert cmd[cmd.index("--type_assignment.normalization") + 1] == "raw"


def test_run_mapmycells_rejects_unknown_normalization(tmp_path):
    from annotation_transfer.mapper_local import (
        MapperError as LocalMapperError,
    )
    from annotation_transfer.mapper_local import run_mapmycells

    with pytest.raises(LocalMapperError, match="Unknown normalization"):
        run_mapmycells(
            tmp_path / "q.h5ad",
            tmp_path / "stats.h5",
            tmp_path / "markers.json",
            tmp_path / "out.json",
            normalization="cpm",
        )


def test_run_mapping_refuses_non_raw_on_web_backend(tmp_path):
    """The web API exposes no normalisation parameter and treats every
    upload as counts — refuse rather than mis-map silently."""
    from annotation_transfer.mapper import run_mapping

    _save_spec(tmp_path, id="TESTWEB", preferred_backend="web")
    with pytest.raises(MapperError, match="not available on the"):
        run_mapping(
            tmp_path / "q.h5ad",
            "TESTWEB",
            tmp_path / "out",
            backend=MappingBackend.WEB,
            normalization="log2CPM",
            taxonomy_dir=tmp_path,
        )


def test_run_mapping_rejects_unknown_normalization(tmp_path):
    from annotation_transfer.mapper import run_mapping

    _save_spec(tmp_path, id="TESTNORM")
    with pytest.raises(MapperError, match="Unknown normalization"):
        run_mapping(
            tmp_path / "q.h5ad",
            "TESTNORM",
            tmp_path / "out",
            normalization="tpm",
            taxonomy_dir=tmp_path,
        )


def test_run_mapping_local_threads_normalization(tmp_path, monkeypatch):
    from annotation_transfer import mapper as mapper_mod

    stats = tmp_path / "stats.h5"
    markers = tmp_path / "markers.json"
    stats.write_text("")
    markers.write_text("{}")
    _save_spec(
        tmp_path,
        id="TESTLOCAL",
        web_ref_id=None,
        preferred_backend="local",
        local_stats_path=str(stats),
        local_markers_path=str(markers),
    )

    captured: dict = {}

    def fake_run_mapmycells(*args, **kwargs):
        captured.update(kwargs)
        return kwargs.get("output_csv")

    monkeypatch.setattr(
        "annotation_transfer.mapper_local.run_mapmycells", fake_run_mapmycells
    )
    monkeypatch.setattr(mapper_mod, "_count_cells", lambda p: 42)

    result = mapper_mod.run_mapping(
        tmp_path / "q.h5ad",
        "TESTLOCAL",
        tmp_path / "out",
        normalization="log2CPM",
        taxonomy_dir=tmp_path,
    )
    assert captured["normalization"] == "log2CPM"
    assert result.normalization == "log2CPM"


# ─── normalisation as a backend constraint (#208 follow-up) ───────────


def test_log2cpm_prefers_local_even_when_web_available(tmp_path):
    """log2CPM can only be mapped locally, so `auto` must not hand it to
    the web backend when the local files are sitting right there."""
    from annotation_transfer.mapper import MappingBackend, resolve_backend
    from annotation_transfer.taxonomies import TaxonomySpec

    stats = tmp_path / "stats.h5"
    markers = tmp_path / "markers.json"
    stats.touch()
    markers.touch()
    tax = TaxonomySpec(
        id="CCN20230722",
        name="Whole Mouse Brain",
        species="mouse",
        web_ref_id="WMB-10Xv3",
        local_stats_path=stats,
        local_markers_path=markers,
        preferred_backend="web",
    )
    assert resolve_backend(
        tax, tmp_path / "q.h5ad", None, normalization="log2CPM"
    ) == MappingBackend.LOCAL
    # raw is unaffected — the web preference still wins.
    assert resolve_backend(
        tax, tmp_path / "q.h5ad", None, normalization="raw"
    ) == MappingBackend.WEB
    # An explicit --backend web is still honoured (and refused later by
    # run_mapping with a diagnostic).
    assert resolve_backend(
        tax, tmp_path / "q.h5ad", MappingBackend.WEB, normalization="log2CPM"
    ) == MappingBackend.WEB


def test_log2cpm_without_local_files_falls_through_to_web(tmp_path):
    """No local files → WEB, so run_mapping raises the refusal that tells
    the user to download them."""
    from annotation_transfer.mapper import MappingBackend, resolve_backend
    from annotation_transfer.taxonomies import TaxonomySpec

    tax = TaxonomySpec(
        id="CCN20230722",
        name="Whole Mouse Brain",
        species="mouse",
        web_ref_id="WMB-10Xv3",
        preferred_backend="auto",
    )
    assert resolve_backend(
        tax, tmp_path / "q.h5ad", None, normalization="log2CPM"
    ) == MappingBackend.WEB
