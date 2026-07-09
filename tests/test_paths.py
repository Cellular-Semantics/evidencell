"""Unit tests for src/evidencell/paths.py"""

from pathlib import Path

import pytest

from evidencell.paths import (
    find_node_file,
    region_from_graph,
    refs_path_for_graph,
    refs_path_for_region,
    repo_root,
    reports_dir_for_region,
    research_dir_for_region,
)


def test_repo_root_finds_schema():
    """repo_root() returns a directory containing schema/."""
    root = repo_root()
    assert (root / "schema").is_dir()


def test_region_from_graph_hippocampus():
    root = repo_root()
    gf = root / "kb" / "graphs" / "hippocampus" / "test.yaml"
    assert region_from_graph(gf) == "hippocampus"


def test_region_from_graph_BG():
    root = repo_root()
    gf = root / "kb" / "graphs" / "BG" / "test.yaml"
    assert region_from_graph(gf) == "BG"


def test_region_from_graph_cerebellum():
    root = repo_root()
    gf = root / "kb" / "graphs" / "cerebellum" / "CB_MLI_types.yaml"
    assert region_from_graph(gf) == "cerebellum"


def test_region_from_graph_invalid():
    with pytest.raises(ValueError, match="Cannot extract region"):
        region_from_graph(Path("/tmp/not_a_kb/file.yaml"))


def test_refs_path_for_graph():
    root = repo_root()
    gf = root / "kb" / "graphs" / "hippocampus" / "test.yaml"
    expected = root / "references" / "hippocampus" / "references.json"
    assert refs_path_for_graph(gf) == expected


def test_refs_path_for_region():
    root = repo_root()
    assert refs_path_for_region("hippocampus") == root / "references" / "hippocampus" / "references.json"


def test_reports_dir_for_region():
    root = repo_root()
    assert reports_dir_for_region("BG") == root / "reports" / "BG"


def test_research_dir_for_region():
    root = repo_root()
    assert research_dir_for_region("cerebellum") == root / "research" / "cerebellum"


def test_find_node_file_known_node():
    """find_node_file returns a YAML path containing the requested node."""
    # olm_cell_ca1 lives in hippocampus_GABAergic_interneurons.yaml after the
    # 2026-06-10 olm_hippocampus → olm_cell_ca1 merge (PR #114, GH #116).
    path = find_node_file("olm_cell_ca1")
    assert path.exists()
    assert path.suffix == ".yaml"
    import yaml
    data = yaml.safe_load(path.read_text())
    node_ids = [n.get("id") for n in data.get("nodes", []) if isinstance(n, dict)]
    assert "olm_cell_ca1" in node_ids


def test_find_node_file_missing_node():
    """find_node_file raises FileNotFoundError for unknown node_id."""
    with pytest.raises(FileNotFoundError, match="not found in any KB YAML"):
        find_node_file("this_node_does_not_exist_xyz")
