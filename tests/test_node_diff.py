"""Tests for the structure-aware KB diff and its review render (issue #179)."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest
import yaml

from evidencell import node_diff as nd
from evidencell.render_review import compute_diff, render_diff

BASE_NODE = """\
# a comment that must not matter
nodes:
  - id: n1
    name: Test neuron
    definition_basis: CLASSICAL_NEUROCHEMICAL
    nt_type:
      name_in_source: GABAergic
    defining_markers:
      - symbol: Th
        sources:
          - ref: "PMID:11111111"
            quote_key: "123_aaaaaaaa"
          - ref: "PMID:22222222"
            quote_key: "456_bbbbbbbb"
      - symbol: Dbh
    morphology:
      description: >
        Small round soma with
        sparse dendrites.
edges: []
"""


def _diff(base: str | None, head: str | None, path="kb/graphs/r/n1.yaml"):
    return nd.diff_graphs(yaml.safe_load(base) if base else None,
                          yaml.safe_load(head) if head else None, path=path)


# ── 1, 2: noise is not change ───────────────────────────────────────────────


def test_reorder_and_comments_are_not_changes():
    head = """\
edges: []
nodes:
  - name: Test neuron
    id: n1
    morphology:
      description: Small round soma with sparse dendrites.
    defining_markers:
      - symbol: Dbh
      - sources:
          - quote_key: "456_bbbbbbbb"
            ref: "PMID:22222222"
          - ref: "PMID:11111111"
            quote_key: "123_aaaaaaaa"
        symbol: Th
    definition_basis: CLASSICAL_NEUROCHEMICAL
    nt_type: {name_in_source: GABAergic}
"""
    assert _diff(BASE_NODE, head) == []


def test_rewrap_is_not_a_change_but_a_word_edit_is_prose():
    rewrap = BASE_NODE.replace("Small round soma with\n        sparse dendrites.",
                               "Small round\n        soma with sparse dendrites.")
    assert _diff(BASE_NODE, rewrap) == []
    edit = BASE_NODE.replace("sparse dendrites", "dense dendrites")
    ch = _diff(BASE_NODE, edit)
    assert len(ch) == 1 and ch[0].kind == "prose"
    assert ch[0].path == ["morphology", "description"]


def test_empty_values_are_equivalent():
    head = BASE_NODE.replace("edges: []", "edges:\n")
    assert _diff(BASE_NODE, head) == []


# ── 3, 4: targeted changes ──────────────────────────────────────────────────


def test_added_source_is_one_source_change():
    head = BASE_NODE.replace("      - symbol: Dbh", """\
      - symbol: Dbh
        sources:
          - ref: "PMID:11111111"
            quote_key: "123_aaaaaaaa\"""")
    ch = _diff(BASE_NODE, head)
    assert len(ch) == 1
    c = ch[0]
    assert (c.kind, c.op, c.severity) == ("source", "added", "provenance")
    assert c.path[:2] == ["defining_markers", "Dbh"]


def test_nt_type_change_is_identity_and_sorted_first():
    head = BASE_NODE.replace("GABAergic", "glutamatergic").replace(
        "sparse dendrites", "dense dendrites")
    ch = nd.sort_changes(_diff(BASE_NODE, head))
    assert [c.severity for c in ch] == ["identity", "content"]
    assert ch[0].old == "GABAergic" and ch[0].new == "glutamatergic"


def test_marker_added_and_removed_are_list_items():
    head = BASE_NODE.replace("      - symbol: Dbh", "      - symbol: Npy")
    ops = sorted((c.op, c.kind, c.path[-1]) for c in _diff(BASE_NODE, head))
    assert ops == [("added", "list_item", "Npy"), ("removed", "list_item", "Dbh")]


# ── 5, 6: whole-entity changes ──────────────────────────────────────────────


def test_added_and_removed_files():
    added = _diff(None, BASE_NODE)
    assert [(c.entity, c.op, c.kind) for c in added] == [("node", "added", "entity")]
    removed = _diff(BASE_NODE, None)
    assert [(c.entity, c.op) for c in removed] == [("node", "removed")]


def test_cross_file_move_is_one_moved_record():
    moved_body = BASE_NODE.replace("sparse dendrites", "dense dendrites")
    ch = nd.diff_files([("kb/graphs/r/a.yaml", yaml.safe_load(BASE_NODE), None),
                        ("kb/graphs/r/b.yaml", None, yaml.safe_load(moved_body))])
    ent = [c for c in ch if c.kind == "entity"]
    assert len(ent) == 1 and ent[0].op == "moved"
    assert ent[0].moved_from == "kb/graphs/r/a.yaml" and ent[0].file == "kb/graphs/r/b.yaml"
    assert [c.kind for c in ch if c.kind != "entity"] == ["prose"]


def test_stub_is_its_own_entity_kind():
    head = BASE_NODE.replace("edges: []", """\
  - id: parent
    name: Parent
    definition_basis: CLASSICAL_ANATOMICAL
    reference_stub: LIT_TYPE
edges: []""")
    ch = _diff(BASE_NODE, head)
    assert [(c.entity, c.op) for c in ch] == [("stub", "added")]


# ── Git-backed end-to-end (compute_diff + render_diff) ──────────────────────

QUOTE_TEXT = "Cells in the leaflet are GABAergic and express neuropeptide Y."


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    root = tmp_path
    _git(root, "init", "-q", "-b", "main")
    _git(root, "config", "user.email", "t@example.org")
    _git(root, "config", "user.name", "t")
    g = root / "kb" / "graphs" / "r"
    g.mkdir(parents=True)
    (g / "n1.yaml").write_text(BASE_NODE)
    refs = root / "references" / "r"
    (refs / "papers").mkdir(parents=True)
    (refs / "quotes").mkdir(parents=True)
    (refs / "papers" / "123.json").write_text(json.dumps({
        "corpus_id": "123", "author_keys": ["Doe et al., 2020"], "title": "A paper",
        "year": 2020, "authors": ["Jane Doe"], "pmid": "11111111", "doi": "10.1/abc"}))
    (refs / "quotes" / "123.json").write_text(json.dumps({
        "123_aaaaaaaa": {"text": QUOTE_TEXT, "source_method": "ASTA_REPORT",
                         "status": "pending"}}))
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", "base")
    _git(root, "checkout", "-q", "-b", "feature")
    return root


def _edge_file(snippet: str) -> str:
    return f"""\
nodes:
  - id: child
    name: Child neuron
    definition_basis: CLASSICAL_NEUROCHEMICAL
    defining_markers:
      - symbol: Npy
        sources:
          - ref: "PMID:11111111"
            quote_key: "123_aaaaaaaa"
          - ref: "PMID:11111111"
            quote_key: "123_deadbeef"
          - ref: "PMID:11111111"
  - id: n1
    name: Test neuron
    definition_basis: CLASSICAL_NEUROCHEMICAL
    reference_stub: LIT_TYPE
edges:
  - id: edge_child_to_n1
    lit_type: child
    taxonomy_type: n1
    relationship: skos:broadMatch
    mapping_justification: semapv:UnreviewedManualMapping
    evidence:
      - evidence_type: LITERATURE
        supports: SUPPORT
        reference: "PMID:11111111"
        snippet: "{snippet}"
        explanation: Places the child inside the parent.
"""


def test_end_to_end_untracked_file_edge_and_warnings(repo: Path):
    # Untracked new file: must be picked up without `git add`.
    (repo / "kb/graphs/r/child.yaml").write_text(
        _edge_file("leaflet are GABAergic and express neuropeptide Y"))
    r = compute_diff("main", repo)
    assert "kb/graphs/r/child.yaml" in r.files
    msgs = [w.message for w in r.warnings]
    assert any("123_deadbeef" in m and "NOT FOUND" in m for m in msgs)
    assert any("no quote_key" in m for m in msgs)
    assert not any("snippet" in m for m in msgs), msgs  # verbatim fragment passes

    md = render_diff(r)
    edge_line = next(ln for ln in md.splitlines() if "—**skos:broadMatch**→" in ln)
    assert "`child`" in edge_line and "stub for `n1` added" in edge_line
    # Quote and snippet text only inside folds; warnings are outside any fold.
    head, _, _ = md.partition("<details>")
    assert QUOTE_TEXT not in head
    assert "NOT FOUND" in head
    assert md.count("<details>") == md.count("</details>")


def test_non_verbatim_snippet_is_flagged(repo: Path):
    (repo / "kb/graphs/r/child.yaml").write_text(_edge_file("Cells are glutamatergic."))
    r = compute_diff("main", repo)
    assert any("not a verbatim substring" in w.message for w in r.warnings)


def test_modified_node_renders_compact_change_lines(repo: Path):
    f = repo / "kb/graphs/r/n1.yaml"
    f.write_text(BASE_NODE.replace("GABAergic", "glutamatergic").replace(
        "      - symbol: Dbh", """\
      - symbol: Dbh
        sources:
          - ref: "PMID:11111111"
            quote_key: "123_aaaaaaaa\""""))
    md = render_diff(compute_diff("main", repo))
    assert "### ✏️ Test neuron · `n1`" in md
    assert "NT type › name in source: ~~`GABAergic`~~ → **`glutamatergic`**" in md
    src_line = next(ln for ln in md.splitlines() if ln.startswith("- ➕ source on"))
    assert "Defining marker › **Dbh**" in src_line and "Doe et al., 2020" in src_line
    assert QUOTE_TEXT in md  # present, but folded:
    assert md.index("<details>") < md.index(QUOTE_TEXT)
    # Unchanged parts of the node are not rendered.
    assert "Small round soma" not in md


def test_reference_store_changes(repo: Path):
    refs = repo / "references/r"
    (refs / "papers/789.json").write_text(json.dumps({
        "corpus_id": "789", "author_keys": ["Roe et al., 2021"], "title": "New paper",
        "year": 2021, "authors": ["R Roe"], "pmid": "33333333"}))
    (refs / "quotes/789.json").write_text(json.dumps({
        "789_cccccccc": {"text": "Uncited quote.", "source_method": "ASTA_REPORT"}}))
    p = json.loads((refs / "papers/123.json").read_text())
    p["pmid"] = "99999999"
    (refs / "papers/123.json").write_text(json.dumps(p))
    q = json.loads((refs / "quotes/123.json").read_text())
    q["123_aaaaaaaa"]["claims"] = ["nt_type"]
    (refs / "quotes/123.json").write_text(json.dumps(q))

    r = compute_diff("main", repo)
    assert [x["corpus_id"] for x in r.references["papers_added"]] == ["789"]
    assert r.uncited == ["789_cccccccc"]
    assert r.references["claims_edits"] == {"123": 1}
    assert any("identity field `pmid`" in w.message for w in r.warnings)
    md = render_diff(r)
    assert "Reference-store changes only" in md
    assert "Roe et al., 2021" in md


def test_budget_keeps_change_lines_and_balanced_folds(repo: Path):
    long_text = " ".join(["word"] * 400)
    q = json.loads((repo / "references/r/quotes/123.json").read_text())
    for i in range(40):
        q[f"123_{i:08x}"] = {"text": f"{long_text} {i}"}
    (repo / "references/r/quotes/123.json").write_text(json.dumps(q))
    srcs = "\n".join(f'          - ref: "PMID:11111111"\n            quote_key: "123_{i:08x}"'
                     for i in range(40))
    (repo / "kb/graphs/r/n1.yaml").write_text(BASE_NODE.replace(
        "      - symbol: Dbh", "      - symbol: Dbh\n        sources:\n" + srcs))
    r = compute_diff("main", repo)
    full = render_diff(r, budget=0)
    budget = len(full.encode()) // 3
    small = render_diff(r, budget=budget)
    assert len(small.encode()) <= budget
    assert small.count("<details>") == small.count("</details>")
    assert small.count("- ➕ source on") == full.count("- ➕ source on") == 40
    assert "omitted for size" in small


def test_json_round_trip(repo: Path):
    (repo / "kb/graphs/r/child.yaml").write_text(_edge_file("express neuropeptide Y"))
    r = compute_diff("main", repo)
    data = json.loads(json.dumps(r.to_json(), default=str))
    assert {"base", "merge_base", "files", "changes", "warnings", "references"} <= set(data)
    c = data["changes"][0]
    assert {"file", "entity", "entity_id", "op", "path", "kind", "old", "new",
            "severity"} <= set(c)


def test_restrict_to_paths(repo: Path):
    (repo / "kb/graphs/r/child.yaml").write_text(_edge_file("express neuropeptide Y"))
    (repo / "kb/graphs/r/n1.yaml").write_text(BASE_NODE.replace("Dbh", "Npy"))
    r = compute_diff("main", repo, only=["kb/graphs/r/n1.yaml"])
    assert {c.file for c in r.changes} == {"kb/graphs/r/n1.yaml"}


def test_modified_edge_heading_and_endpoint_change(repo: Path):
    f = repo / "kb/graphs/r/child.yaml"
    f.write_text(_edge_file("express neuropeptide Y"))
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "add child")
    _git(repo, "branch", "-f", "main", "HEAD")
    f.write_text(_edge_file("express neuropeptide Y").replace(
        "relationship: skos:broadMatch", "relationship: skos:exactMatch"))
    md = render_diff(compute_diff("main", repo))
    assert "### ✏️ Edge `edge_child_to_n1`" in md
    assert "Relationship: ~~`skos:broadMatch`~~ → **`skos:exactMatch`**" in md
