"""Tests for the taxonomy-indexed TOC generator."""

from __future__ import annotations

import sqlite3

import pytest
import yaml

from evidencell import toc


@pytest.fixture
def fake_taxonomy(tmp_path, monkeypatch) -> str:
    """Build a tiny taxonomy DB + meta + KB tree under tmp_path.

    Hierarchy:
        TX_CLAS_A (rank 3)
        ├── TX_SUBC_A1 (rank 2)
        │   ├── TX_SUPT_A1a (rank 1)
        │   │   └── TX_CLUS_A1a1 (rank 0)
        │   └── TX_SUPT_A1b (rank 1)
        │       └── TX_CLUS_A1b1 (rank 0)
        └── TX_SUBC_A2 (rank 2)  -- no edges; should prune
            └── TX_SUPT_A2a (rank 1)

    Edges (in kb/draft/region1/graph.yaml):
        classical_X → TX_CLUS_A1a1   HIGH
        classical_Y → TX_SUPT_A1b    LOW         (filtered out by MODERATE threshold)
        classical_Z → TX_SUBC_A1     MODERATE
    """
    repo = tmp_path / "repo"
    (repo / "schema").mkdir(parents=True)
    (repo / "kb" / "draft" / "region1").mkdir(parents=True)
    (repo / "kb" / "mappings").mkdir(parents=True)
    (repo / "reports" / "region1").mkdir(parents=True)
    (repo / "kb" / "taxonomy" / "TX").mkdir(parents=True)

    # Reports — only X has one; Y has none.
    (repo / "reports" / "region1" / "classical_X_summary.md").write_text("# X\n")
    (repo / "reports" / "region1" / "classical_Z_summary.md").write_text("# Z\n")

    # KB graph.
    graph = {
        "edges": [
            {"type_a": "classical_X", "type_b": "TX_CLUS_A1a1", "confidence": "HIGH",
             "relationship": "EQUIVALENT"},
            {"type_a": "classical_Y", "type_b": "TX_SUPT_A1b", "confidence": "LOW",
             "relationship": "PARTIAL_OVERLAP"},
            {"type_a": "classical_Z", "type_b": "TX_SUBC_A1", "confidence": "MODERATE",
             "relationship": "TYPE_A_SPLITS"},
        ]
    }
    (repo / "kb" / "draft" / "region1" / "graph.yaml").write_text(yaml.safe_dump(graph))

    # taxonomy_meta.yaml
    meta = {"taxonomy_id": "TX", "taxonomy_name": "Test Taxonomy", "species_label": "Mus musculus"}
    (repo / "kb" / "taxonomy" / "TX" / "taxonomy_meta.yaml").write_text(yaml.safe_dump(meta))

    # SQLite DB
    db = repo / "kb" / "taxonomy" / "TX" / "TX.db"
    conn = sqlite3.connect(db)
    conn.execute("""
        CREATE TABLE nodes (
          node_id TEXT PRIMARY KEY,
          short_form TEXT NOT NULL,
          label TEXT NOT NULL,
          taxonomy_id TEXT NOT NULL,
          taxonomy_level TEXT NOT NULL,
          taxonomy_rank INTEGER,
          parent_id TEXT
        )
    """)
    rows = [
        ("TX_CLAS_A",   "A",    "A class",    "TX", "class",    3, None),
        ("TX_SUBC_A1",  "A1",   "A1 subclass","TX", "subclass", 2, "TX_CLAS_A"),
        ("TX_SUBC_A2",  "A2",   "A2 subclass","TX", "subclass", 2, "TX_CLAS_A"),
        ("TX_SUPT_A1a", "A1a",  "A1a supt",   "TX", "supertype",1, "TX_SUBC_A1"),
        ("TX_SUPT_A1b", "A1b",  "A1b supt",   "TX", "supertype",1, "TX_SUBC_A1"),
        ("TX_SUPT_A2a", "A2a",  "A2a supt",   "TX", "supertype",1, "TX_SUBC_A2"),
        ("TX_CLUS_A1a1","A1a1", "A1a1 clus",  "TX", "cluster",  0, "TX_SUPT_A1a"),
        ("TX_CLUS_A1b1","A1b1", "A1b1 clus",  "TX", "cluster",  0, "TX_SUPT_A1b"),
    ]
    conn.executemany("INSERT INTO nodes VALUES (?,?,?,?,?,?,?)", rows)
    conn.commit()
    conn.close()

    monkeypatch.setattr(toc, "repo_root", lambda: repo)
    monkeypatch.setattr(toc, "taxonomy_db_path", lambda tid: repo / "kb" / "taxonomy" / tid / f"{tid}.db")
    monkeypatch.setattr(toc, "taxonomy_meta_path", lambda tid: repo / "kb" / "taxonomy" / tid / "taxonomy_meta.yaml")
    monkeypatch.setattr(toc, "reports_dir_for_region", lambda r: repo / "reports" / r)
    return "TX"


def test_full_taxonomy_with_pruning_and_threshold(fake_taxonomy):
    md = toc.generate(fake_taxonomy, min_confidence="MODERATE")
    # X should appear (HIGH on cluster); Z should appear (MODERATE on subclass).
    assert "classical_X" in md
    assert "classical_Z" in md
    # Y is LOW — pruned by MODERATE threshold.
    assert "classical_Y" not in md
    # Empty branch SUBC_A2 has no qualifying edges; should be pruned.
    assert "A2 subclass" not in md
    # Top-rank heading present.
    assert "## Class — A class" in md
    # Subclass appears as H3.
    assert "### Subclass — A1 subclass" in md
    # Cluster appears as H5 (rank 0, top rank 3 → depth 2 + 3 = 5).
    assert "##### Cluster — A1a1 clus" in md
    # Report link uses ../{region}/... convention from reports/_toc/.
    assert "(../region1/classical_X_summary.md)" in md


def test_low_threshold_includes_low(fake_taxonomy):
    md = toc.generate(fake_taxonomy, min_confidence="LOW")
    assert "classical_Y" in md
    # Y has no report file — confirm fallback rendering.
    assert "_(no report file)_" in md


def test_subtree_root(fake_taxonomy):
    md = toc.generate(fake_taxonomy, root_accession="TX_SUBC_A1", min_confidence="MODERATE")
    # Subtree root renders as H2 regardless of original rank.
    assert "## Subclass — A1 subclass" in md
    # Sibling outside subtree must not appear.
    assert "A class" not in md
    assert "A2 subclass" not in md


def test_high_threshold_prunes_to_single_branch(fake_taxonomy):
    md = toc.generate(fake_taxonomy, min_confidence="HIGH")
    # Only the HIGH X edge survives — and its full ancestor chain.
    assert "classical_X" in md
    assert "classical_Z" not in md
    assert "A1a1 clus" in md
    assert "A1b" not in md  # the LOW-confidence branch must be gone


def test_empty_taxonomy_renders_placeholder(fake_taxonomy, tmp_path):
    md = toc.generate(fake_taxonomy, min_confidence="HIGH", root_accession="TX_SUBC_A2")
    # SUBC_A2 has no edges anywhere — empty placeholder.
    assert "No mapping reports meet the confidence threshold" in md


def test_slugify_basic():
    assert toc.slugify("WMBv1 (Whole Mouse Brain v1)") == "WMBv1_Whole_Mouse_Brain_v1"
    assert toc.slugify("07 CTX-MGE GABA") == "07_CTX-MGE_GABA"
    assert toc.slugify("   ") == "untitled"


def test_default_output_path_uses_names(fake_taxonomy, monkeypatch):
    # Single taxonomy: filename uses taxonomy_name slug.
    surviving_roots, meta, root_node = toc._build_taxonomy(fake_taxonomy, None, "MODERATE")
    out = toc._default_output_path(fake_taxonomy, None, taxonomy_meta=meta, root_node=root_node)
    assert out.name == "Test_Taxonomy.md"

    # Subtree: uses node label slug.
    surviving_roots, meta, root_node = toc._build_taxonomy(
        fake_taxonomy, "TX_SUBC_A1", "MODERATE"
    )
    out = toc._default_output_path(fake_taxonomy, "TX_SUBC_A1", taxonomy_meta=meta, root_node=root_node)
    assert out.name == "Test_Taxonomy__A1_subclass.md"


def test_generate_all_combines_taxonomies_with_offset(fake_taxonomy):
    md = toc.generate_all(min_confidence="MODERATE")
    # H1 title for the combined report.
    assert md.startswith("# Taxonomy-indexed mapping reports\n")
    # Per-taxonomy H2.
    assert "\n## Test Taxonomy\n" in md
    # Top class heading is shifted from H2 to H3 by the offset.
    assert "### Class — A class" in md
    # Subclass shifted from H3 to H4.
    assert "#### Subclass — A1 subclass" in md
    # Cluster (rank 0) shifted to H6 (capped).
    assert "###### Cluster — A1a1 clus" in md


def test_relationship_appears_on_edge_lines(fake_taxonomy):
    md = toc.generate(fake_taxonomy, min_confidence="MODERATE")
    # Each surviving edge line carries its relationship + confidence.
    assert "EQUIVALENT · HIGH" in md
    assert "TYPE_A_SPLITS · MODERATE" in md


def test_glossary_lists_only_used_terms(fake_taxonomy):
    md = toc.generate(fake_taxonomy, min_confidence="MODERATE")
    assert "## Glossary" in md
    assert "### Mapping relationship" in md
    assert "### Mapping confidence" in md
    # Used terms appear.
    assert "**EQUIVALENT**" in md
    assert "**TYPE_A_SPLITS**" in md
    assert "**HIGH**" in md
    assert "**MODERATE**" in md
    # Unused terms (from the LOW-filtered Y edge or never-used enum values) absent.
    assert "**PARTIAL_OVERLAP**" not in md
    assert "**LOW**" not in md
    assert "**REFUTED**" not in md


def test_generate_all_empty(monkeypatch, tmp_path):
    """No taxonomies found → placeholder, no traceback."""
    monkeypatch.setattr(toc, "repo_root", lambda: tmp_path)
    md = toc.generate_all()
    assert "No taxonomies found" in md
