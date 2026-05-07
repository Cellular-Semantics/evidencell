"""Tests for kg_query module.

All tests mock the neo4j driver — no live KG required.
Marked fast (no integration tag).
"""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

# kg_query imports neo4j lazily; we patch it before importing the module under test


def _make_mock_driver(records: list[dict]):
    """Return a mock neo4j GraphDatabase.driver that yields the given records."""
    mock_result = MagicMock()
    mock_result.__iter__ = MagicMock(
        return_value=iter([_make_mock_record(r) for r in records])
    )
    mock_session = MagicMock()
    mock_session.__enter__ = MagicMock(return_value=mock_session)
    mock_session.__exit__ = MagicMock(return_value=False)
    mock_session.run = MagicMock(return_value=mock_result)
    mock_driver = MagicMock()
    mock_driver.session = MagicMock(return_value=mock_session)
    return mock_driver


def _make_mock_record(d: dict):
    """Mock a neo4j Record exposing keys() and __getitem__.

    Mirrors what `_record_to_dict` consumes. Plain (non-Node) values pass through
    `_wrap_value` unchanged, so the mock dict round-trips as-is.
    """
    rec = MagicMock()
    rec.keys = MagicMock(return_value=list(d.keys()))
    rec.__getitem__ = MagicMock(side_effect=lambda k: d[k])
    return rec


@pytest.fixture(autouse=True)
def patch_neo4j(monkeypatch):
    """Patch neo4j import so kg_query thinks the driver is available."""
    import sys
    mock_neo4j = MagicMock()
    mock_neo4j.GraphDatabase.driver = MagicMock()
    mock_neo4j.basic_auth = MagicMock(return_value=("user", "pass"))
    # _wrap_value does `from neo4j.graph import Node` to type-check values;
    # register a stub class so the import resolves without the real driver.
    mock_neo4j_graph = MagicMock()

    class _StubNode:
        pass

    mock_neo4j_graph.Node = _StubNode
    monkeypatch.setitem(sys.modules, "neo4j", mock_neo4j)
    monkeypatch.setitem(sys.modules, "neo4j.graph", mock_neo4j_graph)
    yield mock_neo4j


def test_kg_query_client_connect(patch_neo4j):
    from evidencell import kg_query

    mock_driver = _make_mock_driver([{"result": 1}])
    patch_neo4j.GraphDatabase.driver.return_value = mock_driver

    client = kg_query.KGQueryClient(endpoint="bolt://localhost:7687")
    client.connect()
    assert client._driver is not None


def test_kg_query_client_run_query(patch_neo4j):
    from evidencell import kg_query

    expected = [{"node": {"props": {"curie": "WMB:CS1"}}, "cl": None, "anat": []}]
    mock_driver = _make_mock_driver(expected)
    patch_neo4j.GraphDatabase.driver.return_value = mock_driver

    client = kg_query.KGQueryClient(endpoint="bolt://localhost:7687")
    client._driver = mock_driver
    records = client.run_query("MATCH (n) RETURN n LIMIT 1")
    assert len(records) == 1
    assert records[0] == expected[0]


def test_fetch_taxonomy_json_writes_output(tmp_path, patch_neo4j):
    from evidencell import kg_query

    rows = [
        {"node": {"labels": ["CCN20230722_supertype"], "properties": {"curie": "WMB:X1", "short_form": "X1", "label": "Type A"}}, "cl": None, "parent_curie": None, "anat": []},
    ]

    cypher_path = tmp_path / "query.cypher"
    cypher_path.write_text("MATCH (node) RETURN node", encoding="utf-8")
    output_path = tmp_path / "output.json"

    with patch.object(kg_query, "KGQueryClient") as mock_cls:
        # fetch_taxonomy_json uses the client directly (not __enter__ return value)
        mock_cls.return_value.run_query.return_value = rows
        n = kg_query.fetch_taxonomy_json(cypher_path, output_path)

    assert output_path.exists()
    loaded = json.loads(output_path.read_text())
    assert len(loaded) == len(rows)
    assert n == len(rows)


def test_fetch_taxonomy_json_atomic_write(tmp_path, patch_neo4j):
    """A RuntimeError during run_query leaves no output file."""
    from evidencell import kg_query

    cypher_path = tmp_path / "query.cypher"
    cypher_path.write_text("MATCH (n) RETURN n", encoding="utf-8")
    output_path = tmp_path / "output.json"

    with patch.object(kg_query, "KGQueryClient") as mock_cls:
        mock_cls.return_value.run_query.side_effect = RuntimeError("connection dropped")
        with pytest.raises(RuntimeError):
            kg_query.fetch_taxonomy_json(cypher_path, output_path)

    assert not output_path.exists()
    # The tmp file should have been cleaned up (rename never happened)
    assert not (tmp_path / "output.json.tmp").exists()


def test_cypher_comment_stripping(tmp_path, patch_neo4j):
    """Comments in .cypher files are stripped before sending to the driver."""
    from evidencell import kg_query

    cypher_path = tmp_path / "annotated.cypher"
    cypher_path.write_text(
        "// This is a comment\nMATCH (n) RETURN n\n// another comment\n",
        encoding="utf-8",
    )
    output_path = tmp_path / "out.json"

    with patch.object(kg_query, "KGQueryClient") as mock_cls:
        mock_cls.return_value.run_query.return_value = []
        kg_query.fetch_taxonomy_json(cypher_path, output_path)
        sent_cypher = mock_cls.return_value.run_query.call_args[0][0]

    assert "//" not in sent_cypher
    assert "MATCH (n) RETURN n" in sent_cypher
