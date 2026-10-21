"""Tests for canonical node resolution in paths.find_node_file."""

import pytest
import yaml

from evidencell import paths
from evidencell.paths import AmbiguousNodeError, find_node_file


@pytest.fixture(autouse=True)
def _fresh_index():
    paths._NODE_INDEX = None
    yield
    paths._NODE_INDEX = None


def _write(kb_dir, name, nodes):
    path = kb_dir / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"nodes": nodes, "edges": []}), encoding="utf-8")
    return path


def _repo(tmp_path, monkeypatch):
    (tmp_path / "schema").mkdir()
    monkeypatch.setattr(paths, "repo_root", lambda: tmp_path)
    return tmp_path / "kb" / "graphs"


def test_resolves_single_definition(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    target = _write(kb / "r", "a.yaml", [{"id": "a", "definition_basis": "CLASSICAL_MULTIMODAL"}])
    assert find_node_file("a") == target


def test_stub_does_not_shadow_canonical_definition(tmp_path, monkeypatch):
    """The highest-risk post-split failure.

    find_node_file returns the first match over sorted(rglob), so a stub in an
    alphabetically earlier file could shadow the real definition -- and
    render.extract_node_facts would then render a full report from a stub.
    """
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r", "aaa_stub_holder.yaml",
           [{"id": "node_x", "definition_basis": "ATLAS_TRANSCRIPTOMIC"}])
    canonical = _write(kb / "r", "zzz_canonical.yaml",
                       [{"id": "node_x", "definition_basis": "CLASSICAL_MULTIMODAL"}])
    assert find_node_file("node_x") == canonical


def test_duplicate_canonical_definitions_raise(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r1", "a.yaml", [{"id": "dup", "definition_basis": "CLASSICAL_MULTIMODAL"}])
    _write(kb / "r2", "b.yaml", [{"id": "dup", "definition_basis": "CLASSICAL_MULTIMODAL"}])
    with pytest.raises(AmbiguousNodeError) as excinfo:
        find_node_file("dup")
    assert "dup" in str(excinfo.value)
    assert "r1/a.yaml" in str(excinfo.value)
    assert "r2/b.yaml" in str(excinfo.value)


def test_atlas_only_node_resolves_to_a_stub(tmp_path, monkeypatch):
    """Atlas ids exist only as stubs; several copies is duplication, not ambiguity."""
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r", "a.yaml", [{"id": "s", "definition_basis": "ATLAS_TRANSCRIPTOMIC"}])
    _write(kb / "r", "b.yaml", [{"id": "s", "definition_basis": "ATLAS_TRANSCRIPTOMIC"}])
    assert find_node_file("s").name == "a.yaml"


def test_missing_node_raises_file_not_found(tmp_path, monkeypatch):
    _repo(tmp_path, monkeypatch)
    with pytest.raises(FileNotFoundError):
        find_node_file("absent")


def test_index_invalidates_when_a_file_changes(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    path = _write(kb / "r", "a.yaml", [{"id": "a", "definition_basis": "CLASSICAL_MULTIMODAL"}])
    assert find_node_file("a") == path
    path.write_text(
        yaml.safe_dump({"nodes": [{"id": "renamed", "definition_basis": "CLASSICAL_MULTIMODAL"}],
                        "edges": []}),
        encoding="utf-8",
    )
    import os
    st = path.stat()
    os.utime(path, ns=(st.st_atime_ns, st.st_mtime_ns + 1_000_000))
    assert find_node_file("renamed") == path
    with pytest.raises(FileNotFoundError):
        find_node_file("a")
