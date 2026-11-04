"""Tests for the reviewer render (quote dereferencing)."""

import json
import pathlib
import tempfile

from evidencell.render_review import render_file, render_node


def _store(tmp_path, region="testregion"):
    """Minimal split reference store: papers/ + quotes/."""
    d = tmp_path / "references" / region
    (d / "papers").mkdir(parents=True)
    (d / "quotes").mkdir(parents=True)
    (d / "papers" / "123.json").write_text(json.dumps({
        "corpus_id": "123", "author_keys": ["Doe et al., 2020"],
        "title": "A paper", "year": 2020, "authors": ["Jane Doe"],
        "pmid": "11111111", "doi": "10.1/abc",
    }))
    (d / "quotes" / "123.json").write_text(json.dumps({
        "123_aaaaaaaa": {"text": "Cells are Th positive.",
                         "source_method": "ASTA_REPORT", "status": "pending"},
    }))
    return d


NODE = {
    "id": "n1", "name": "Test neuron", "definition_basis": "CLASSICAL_NEUROCHEMICAL",
    "species": None,
    "notes": "A caveat worth reading.",
    "defining_markers": [
        {"name_in_source": "Th", "sources": [
            {"ref": "PMID:11111111", "method": "IHC", "scope": "mouse",
             "quote_key": "123_aaaaaaaa"}]},
    ],
}


def test_quote_text_is_inlined():
    from evidencell.references import load_papers, load_quotes
    with tempfile.TemporaryDirectory() as td:
        d = _store(pathlib.Path(td))
        out = render_node(NODE, load_quotes(d), load_papers(d))
    assert "Cells are Th positive." in out
    assert "Doe et al., 2020" in out
    assert "PMID:11111111" in out


def test_notes_are_rendered():
    """notes is the field `render summary` omits; it is why this exists."""
    out = render_node(NODE, {}, {})
    assert "A caveat worth reading." in out


def test_blockquotes_carry_the_hook_annotation():
    """Output must stay valid if written under reports/, where the pre-edit
    hook rejects a blockquote with no `<!-- quote_key: X -->` annotation."""
    from evidencell.references import load_papers, load_quotes
    with tempfile.TemporaryDirectory() as td:
        d = _store(pathlib.Path(td))
        out = render_node(NODE, load_quotes(d), load_papers(d))
    for i, line in enumerate(out.splitlines()):
        if line.strip().startswith(">") and "mapping_notes" not in line:
            prior = "\n".join(out.splitlines()[max(0, i - 3):i])
            assert "<!-- quote_key:" in prior or "CL:" in prior, line


def test_missing_quote_key_is_loud_not_silent():
    """A key absent from the store must be visible, never rendered as blank."""
    out = render_node(NODE, {}, {})
    assert "NOT FOUND" in out
    assert "123_aaaaaaaa" in out


def test_render_file_warns_when_store_absent(tmp_path, monkeypatch, capsys):
    import evidencell.render_review as rr
    g = tmp_path / "kb" / "graphs" / "r" / "n1.yaml"
    g.parent.mkdir(parents=True)
    g.write_text("nodes:\n  - id: n1\n    name: N\nedges: []\n")
    monkeypatch.setattr(rr, "refs_dir_for_graph", lambda p: tmp_path / "nope")
    rr.render_file(g)
    assert "no reference store" in capsys.readouterr().err


def test_edges_are_flagged_as_not_rendered(tmp_path, monkeypatch):
    import evidencell.render_review as rr
    g = tmp_path / "n1.yaml"
    g.write_text(
        "nodes:\n  - id: n1\n    name: N\n"
        "edges:\n  - id: e1\n    lit_type: n1\n    taxonomy_type: t1\n"
    )
    monkeypatch.setattr(rr, "refs_dir_for_graph", lambda p: tmp_path / "nope")
    monkeypatch.setattr(rr, "store_exists", lambda p: True)
    monkeypatch.setattr(rr, "load_quotes", lambda p: {})
    monkeypatch.setattr(rr, "load_papers", lambda p: {})
    assert "not" in render_file(g).lower() and "gen-report" in render_file(g)
