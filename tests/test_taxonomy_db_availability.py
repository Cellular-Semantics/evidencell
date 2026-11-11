"""A missing taxonomy DB fails closed; only read-only paths honour the opt-out."""

import sqlite3

import pytest

from evidencell import paths, taxonomy_db
from evidencell.taxonomy_db import (
    ALLOW_MISSING_DB_ENV,
    TaxonomyDB,
    TaxonomyDBUnavailable,
    require_taxonomy_db,
    taxonomy_db_or_none,
)


@pytest.fixture
def db_path(tmp_path, monkeypatch):
    path = tmp_path / "T1.db"
    monkeypatch.setattr(paths, "taxonomy_db_path", lambda tid: path)
    monkeypatch.delenv(ALLOW_MISSING_DB_ENV, raising=False)
    monkeypatch.setattr(taxonomy_db, "_MISSING_WARNED", set())
    return path


def _build(path):
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE nodes (node_id TEXT)")
    con.commit()
    con.close()


def test_missing_db_raises_with_build_command(db_path):
    with pytest.raises(TaxonomyDBUnavailable, match="just build-taxonomy-db T1") as exc:
        require_taxonomy_db("T1")
    assert "does not exist" in str(exc.value)
    assert ALLOW_MISSING_DB_ENV in str(exc.value)


def test_empty_db_file_raises(db_path):
    """A 0-byte file left by an earlier sqlite3.connect() passes exists()."""
    db_path.touch()
    with pytest.raises(TaxonomyDBUnavailable, match="empty"):
        require_taxonomy_db("T1")


def test_usable_db_returns_path(db_path):
    _build(db_path)
    assert require_taxonomy_db("T1") == db_path
    assert taxonomy_db_or_none("T1") == db_path


def test_or_none_raises_without_opt_out(db_path):
    with pytest.raises(TaxonomyDBUnavailable):
        taxonomy_db_or_none("T1")


def test_or_none_opt_out_warns_once(db_path, monkeypatch, capsys):
    monkeypatch.setenv(ALLOW_MISSING_DB_ENV, "1")
    assert taxonomy_db_or_none("T1") is None
    assert taxonomy_db_or_none("T1") is None
    err = capsys.readouterr().err
    assert err.count("WITHOUT atlas-side fields for T1") == 1


def test_opt_out_requires_exactly_1(db_path, monkeypatch):
    monkeypatch.setenv(ALLOW_MISSING_DB_ENV, "true")
    with pytest.raises(TaxonomyDBUnavailable):
        taxonomy_db_or_none("T1")


def test_query_connection_never_creates_a_db(db_path):
    with pytest.raises(sqlite3.OperationalError):
        TaxonomyDB(db_path).get_node_by_accession("X")
    assert not db_path.exists()


def test_freshness_reports_empty_db_as_stale(db_path, tmp_path):
    db_path.touch()
    stale, reasons = taxonomy_db._freshness_at(db_path, tmp_path)
    assert stale and "not found or empty" in reasons[0]


def test_load_expression_data_raises(db_path):
    with pytest.raises(TaxonomyDBUnavailable):
        taxonomy_db.load_expression_data("T1", "cluster")


def test_kb_writer_ignores_opt_out(db_path, monkeypatch):
    """emit-stage-b writes edges; an atlas-less edge must never be emitted."""
    from evidencell.stage_b_emit import _load_atlas_node

    monkeypatch.setenv(ALLOW_MISSING_DB_ENV, "1")
    with pytest.raises(TaxonomyDBUnavailable):
        _load_atlas_node("T1", "CS_1", 0)


def test_render_raises_without_opt_out(db_path):
    from evidencell.render import _open_taxonomy_db

    with pytest.raises(TaxonomyDBUnavailable):
        _open_taxonomy_db("T1")


def test_render_opt_out_leaves_atlas_fields_blank(db_path, monkeypatch):
    from evidencell.render import _node_b_info

    monkeypatch.setenv(ALLOW_MISSING_DB_ENV, "1")
    nodes = {"CS_1": {"id": "CS_1", "taxonomy_id": "T1", "cell_set_accession": "CS_1"}}
    cache: dict = {}
    info = _node_b_info({"taxonomy_type": "CS_1"}, nodes, db_cache=cache)
    assert (info["n_cells"], info["supertype"], info["taxonomy_level"]) == (None, "", "")
    # extract_node_facts reports the taxonomies cached as None.
    assert cache == {"T1": None}
