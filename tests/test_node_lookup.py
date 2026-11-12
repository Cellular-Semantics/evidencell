"""Tests for node_lookup.get_node: one lookup over kb/graphs and kb/taxonomy."""

import pytest
import yaml

from evidencell import kb_index, paths
from evidencell.node_lookup import NodeNotFoundError, get_node
from evidencell.paths import AmbiguousNodeError
from evidencell.taxonomy_db import (
    TaxonomyDB,
    TaxonomyDBUnavailable,
    UnknownTaxonomyError,
    taxonomy_accessions,
)


@pytest.fixture(autouse=True)
def _fresh_index():
    kb_index.clear_cache()
    yield
    kb_index.clear_cache()


@pytest.fixture
def repo(tmp_path, monkeypatch):
    (tmp_path / "schema").mkdir()
    monkeypatch.setattr(paths, "repo_root", lambda: tmp_path)
    return tmp_path


def _write(path, doc):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(doc), encoding="utf-8")
    return path


def _taxonomy(repo, taxonomy_id="T1", accessions=("CS_1", "CS_2"), build_db=True):
    tax_dir = repo / "kb" / "taxonomy" / taxonomy_id
    _write(tax_dir / "cluster.yaml", {
        "taxonomy_id": taxonomy_id, "taxonomy_level": "CLUSTER", "taxonomy_rank": 0,
        "nodes": [{
            "id": f"X:{a}", "name": f"label {a}", "cell_set_accession": a,
            "taxonomy_id": taxonomy_id, "taxonomy_level": "CLUSTER",
            "definition_basis": "ATLAS_TRANSCRIPTOMIC",
        } for a in accessions],
    })
    if build_db:
        TaxonomyDB(tax_dir / f"{taxonomy_id}.db").build_from_yaml(tax_dir)
    return tax_dir


LIT = {"id": "olm", "name": "OLM", "definition_basis": "CLASSICAL_MULTIMODAL"}


def _stub(accession, taxonomy_id="T1"):
    return {"id": accession, "name": accession, "definition_basis": "ATLAS_TRANSCRIPTOMIC",
            "taxonomy_id": taxonomy_id, "cell_set_accession": accession}


def _graph(repo, name, nodes, edges=()):
    return _write(repo / "kb" / "graphs" / "r" / name, {"nodes": nodes, "edges": list(edges)})


def test_lit_node(repo):
    f = _graph(repo, "olm.yaml", [LIT])
    view = get_node("olm")
    assert (view.kind, view.source_file, view.taxonomy_id) == ("lit", f, None)
    assert view.data["name"] == "OLM"


def test_lit_data_is_read_only(repo):
    _graph(repo, "olm.yaml", [LIT])
    with pytest.raises(TypeError):
        get_node("olm").data["name"] = "x"  # type: ignore[index]


def test_atlas_stub_resolves_through_the_db_with_every_stub_file(repo):
    _taxonomy(repo)
    a = _graph(repo, "a.yaml", [LIT, _stub("CS_1")])
    b = _graph(repo, "b.yaml", [dict(LIT, id="pv"), _stub("CS_1")])
    view = get_node("CS_1")
    assert (view.kind, view.taxonomy_id, view.source_file) == ("atlas", "T1", None)
    assert view.data["label"] == "label CS_1"  # the DB row, not the stub
    assert set(view.stub_files) == {a, b}


def test_accession_the_kb_never_references(repo):
    _taxonomy(repo)
    view = get_node("CS_2")
    assert (view.kind, view.taxonomy_id, view.stub_files) == ("atlas", "T1", ())


def test_unknown_id_raises(repo):
    _taxonomy(repo)
    with pytest.raises(NodeNotFoundError):
        get_node("nope")


def test_ambiguous_canonical_definition_raises(repo):
    _graph(repo, "a.yaml", [LIT])
    _graph(repo, "b.yaml", [LIT])
    with pytest.raises(AmbiguousNodeError):
        get_node("olm")


def test_lit_stub_without_definition_raises(repo):
    _graph(repo, "a.yaml", [dict(LIT, reference_stub="LIT_TYPE")])
    with pytest.raises(NodeNotFoundError, match="lit reference stub"):
        get_node("olm")


def test_stub_for_taxonomy_without_store_raises(repo):
    """CS20250428_GROUP_0016 today: HMBA BG is referenced but not ingested."""
    _graph(repo, "a.yaml", [LIT, _stub("CS_1", taxonomy_id="HMBA")])
    with pytest.raises(UnknownTaxonomyError, match="HMBA"):
        get_node("CS_1")


def test_missing_db_fails_closed(repo):
    _taxonomy(repo, build_db=False)
    _graph(repo, "a.yaml", [LIT, _stub("CS_1")])
    with pytest.raises(TaxonomyDBUnavailable, match="build-taxonomy-db T1"):
        get_node("CS_1")


def test_accession_in_yaml_but_not_db_reads_as_stale(repo):
    tax_dir = _taxonomy(repo)
    _taxonomy(repo, accessions=("CS_1", "CS_2", "CS_3"), build_db=False)
    assert "CS_3" in taxonomy_accessions(tax_dir)
    with pytest.raises(NodeNotFoundError, match="stale"):
        get_node("CS_3")


def test_stubs_disagreeing_on_taxonomy_raise(repo):
    _taxonomy(repo)
    _graph(repo, "a.yaml", [LIT, _stub("CS_1")])
    _graph(repo, "b.yaml", [dict(LIT, id="pv"), _stub("CS_1", taxonomy_id="T2")])
    with pytest.raises(NodeNotFoundError, match="do not agree"):
        get_node("CS_1")


def test_taxonomy_accessions_cache_follows_the_files(repo):
    import os

    tax_dir = _taxonomy(repo, build_db=False)
    assert taxonomy_accessions(tax_dir) == {"CS_1", "CS_2"}
    level = tax_dir / "cluster.yaml"
    _taxonomy(repo, accessions=("CS_9",), build_db=False)
    st = level.stat()
    os.utime(level, ns=(st.st_atime_ns, st.st_mtime_ns + 1_000_000))
    assert taxonomy_accessions(tax_dir) == {"CS_9"}


def test_taxonomy_accessions_missing_store(repo):
    with pytest.raises(UnknownTaxonomyError):
        taxonomy_accessions(repo / "kb" / "taxonomy" / "NOPE")
