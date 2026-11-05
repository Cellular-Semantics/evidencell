"""Tests for the in-memory kb/graphs index."""

import os

import pytest
import yaml

from evidencell import kb_index, paths
from evidencell.kb_index import KbIndexError, get_index
from evidencell.paths import find_node_file


@pytest.fixture(autouse=True)
def _fresh_index():
    kb_index.clear_cache()
    yield
    kb_index.clear_cache()


def _repo(tmp_path, monkeypatch):
    (tmp_path / "schema").mkdir()
    monkeypatch.setattr(paths, "repo_root", lambda: tmp_path)
    return tmp_path / "kb" / "graphs"


def _write(kb_dir, name, nodes, edges=()):
    path = kb_dir / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump({"nodes": nodes, "edges": list(edges)}), encoding="utf-8")
    return path


LIT = {"id": "olm", "definition_basis": "CLASSICAL_MULTIMODAL"}
ATLAS = {"id": "supt_1", "definition_basis": "ATLAS_TRANSCRIPTOMIC",
         "taxonomy_id": "T1", "cell_set_accession": "CS_1"}
EDGE = {"id": "edge_olm_to_supt_1", "lit_type": "olm", "taxonomy_type": "supt_1"}


def test_records_carry_provenance_for_nodes_and_edges(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    f = _write(kb / "hippocampus", "olm.yaml", [LIT, ATLAS], [EDGE])
    idx = get_index()

    [lit] = idx.nodes["olm"]
    assert (lit.source_file, lit.is_stub, lit.node["definition_basis"]) == (
        f, False, "CLASSICAL_MULTIMODAL")
    [stub] = idx.nodes["supt_1"]
    assert stub.is_stub and stub.source_file == f
    [edge] = idx.edges["edge_olm_to_supt_1"]
    assert edge.source_file == f and edge.edge["taxonomy_type"] == "supt_1"


def test_derived_maps(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    a = _write(kb / "hippocampus", "olm.yaml", [LIT, ATLAS], [EDGE])
    b = _write(kb / "cerebellum", "pc.yaml",
               [{"id": "pc", "definition_basis": "CLASSICAL_MULTIMODAL"}, ATLAS])
    idx = get_index()

    assert idx.by_lit == {"olm": ["edge_olm_to_supt_1"]}
    # Regions list canonical nodes only; a stub is not a member of its holder's region.
    assert idx.by_region == {"hippocampus": ["olm"], "cerebellum": ["pc"]}
    assert [r.source_file for r in idx.stubs_by_accession["CS_1"]] == [b, a]
    assert idx.files == (b, a)


def test_canonical_records_precede_stubs(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r", "aaa.yaml", [{**LIT, "reference_stub": "LIT_TYPE"}])
    canonical = _write(kb / "r", "zzz.yaml", [LIT])
    assert [r.source_file for r in get_index().nodes["olm"]][0] == canonical


def test_unparseable_file_fails_closed(tmp_path, monkeypatch):
    """An index built only from the files that parsed would answer as if complete."""
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r", "good.yaml", [LIT])
    bad = kb / "r" / "bad.yaml"
    bad.write_text("nodes: [unclosed\n", encoding="utf-8")
    with pytest.raises(KbIndexError, match="bad.yaml"):
        get_index()
    with pytest.raises(KbIndexError):
        find_node_file("olm")


@pytest.mark.parametrize("content", ["", "- a list\n", "just a string\n"])
def test_non_mapping_file_fails_closed(tmp_path, monkeypatch, content):
    kb = _repo(tmp_path, monkeypatch)
    (kb / "r").mkdir(parents=True)
    (kb / "r" / "odd.yaml").write_text(content, encoding="utf-8")
    with pytest.raises(KbIndexError, match="odd.yaml"):
        get_index()


def test_malformed_entries_are_skipped(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r", "a.yaml", [LIT, "not a dict", {"name": "no id"}], ["nope", {"lit_type": "olm"}])
    idx = get_index()
    assert set(idx.nodes) == {"olm"} and idx.edges == {} and idx.by_lit == {}


def test_cached_until_a_file_changes(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    f = _write(kb / "r", "a.yaml", [LIT])
    first = get_index()
    assert get_index() is first

    f.write_text(yaml.safe_dump({"nodes": [{**LIT, "id": "renamed"}], "edges": []}),
                 encoding="utf-8")
    st = f.stat()
    os.utime(f, ns=(st.st_atime_ns, st.st_mtime_ns + 1_000_000))
    rebuilt = get_index()
    assert rebuilt is not first and set(rebuilt.nodes) == {"renamed"}


def test_adding_a_file_rebuilds(tmp_path, monkeypatch):
    kb = _repo(tmp_path, monkeypatch)
    _write(kb / "r", "a.yaml", [LIT])
    first = get_index()
    _write(kb / "r", "b.yaml", [{**LIT, "id": "other"}])
    assert get_index() is not first and set(get_index().nodes) == {"olm", "other"}


def test_missing_kb_dir_is_an_empty_index(tmp_path, monkeypatch):
    _repo(tmp_path, monkeypatch)
    idx = get_index()
    assert idx.nodes == {} and idx.files == ()


def test_real_kb_indexes_every_file():
    """The live KB must build cleanly, with every edge endpoint resolvable.

    Not "every lit_type is canonical": atlas-to-atlas AT edges (e.g.
    hippocampus/wmb_to_ctx_annotation_transfer.yaml) put an atlas stub in the
    lit_type slot.
    """
    idx = get_index()
    assert idx.files
    for records in idx.edges.values():
        for r in records:
            for end in ("lit_type", "taxonomy_type"):
                assert r.edge.get(end) in idx.nodes, (r.edge["id"], end)
