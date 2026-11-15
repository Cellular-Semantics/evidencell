"""Tests for evidencell.taxonomy_ops — taxonomy update operations."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from evidencell.taxonomy_ops import (
    ENRICHMENT_FIELDS,
    INGEST_FIELDS,
    _index_nodes,
    _merge_nodes,
    collect_kb_marker_union,
    load_gene_mapping,
    load_taxonomy_level,
    reingest,
    save_taxonomy_level,
)


# ── Fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture
def tmp_taxonomy(tmp_path: Path) -> Path:
    """Create a minimal taxonomy directory with one level file."""
    tax_dir = tmp_path / "kb" / "taxonomy" / "TEST001"
    tax_dir.mkdir(parents=True)

    cluster_data = {
        "taxonomy_id": "TEST001",
        "taxonomy_level": "CLUSTER",
        "taxonomy_rank": 0,
        "nodes": [
            {
                "id": "TEST:CLUS_001",
                "name": "Cluster 1",
                "cell_set_accession": "CLUS_001",
                "taxonomy_id": "TEST001",
                "taxonomy_level": "CLUSTER",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "is_terminal": True,
                "markers": [
                    {"symbol": "Sst", "category": "DEFINING"},
                    {"symbol": "Gad1", "category": "DEFINING"},
                ],
            },
            {
                "id": "TEST:CLUS_002",
                "name": "Cluster 2",
                "cell_set_accession": "CLUS_002",
                "taxonomy_id": "TEST001",
                "taxonomy_level": "CLUSTER",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "is_terminal": True,
                "markers": [
                    {"symbol": "Pvalb", "category": "DEFINING"},
                ],
                # Pre-existing enrichment
                "electrophysiology": {"firing_pattern": "fast-spiking"},
            },
        ],
    }

    with (tax_dir / "cluster.yaml").open("w") as fh:
        yaml.dump(cluster_data, fh, allow_unicode=True, sort_keys=False)

    meta = {
        "taxonomy_id": "TEST001",
        "taxonomy_name": "Test Taxonomy",
        "species_id": "NCBITaxon:10090",
        "species_label": "Mus musculus",
        "ingest_date": "2026-04-23",
        "level_counts": {"cluster": 2},
        "mapmycells": {
            "at_taxonomy_id": "TEST001",
            "stats_s3_url": "https://example.com/stats.h5",
        },
    }
    with (tax_dir / "taxonomy_meta.yaml").open("w") as fh:
        yaml.dump(meta, fh, allow_unicode=True, sort_keys=False)

    return tax_dir


@pytest.fixture
def gene_mapping_tsv(tmp_path: Path) -> Path:
    """Create a minimal gene mapping TSV."""
    p = tmp_path / "gene_mapping.tsv"
    p.write_text(textwrap.dedent("""\
        ensembl_id\tsymbol
        ENSMUSG00000004366\tSst
        ENSMUSG00000026787\tGad1
        ENSMUSG00000005716\tPvalb
        ENSMUSG00000032532\tCck
    """))
    return p


# ── Unit tests ────────────────────────────────────────────────────────────────

class TestFieldOwnership:
    def test_no_overlap(self):
        """Ingest and enrichment fields must not overlap."""
        assert INGEST_FIELDS & ENRICHMENT_FIELDS == frozenset()

    def test_id_in_ingest(self):
        assert "id" in INGEST_FIELDS
        assert "name" in INGEST_FIELDS

    def test_expression_not_stored_in_yaml(self):
        """#189: expression lives in the DB cache, not YAML — not an enrichment."""
        assert "precomputed_expression" not in ENRICHMENT_FIELDS
        assert "electrophysiology" in ENRICHMENT_FIELDS


class TestIndexNodes:
    def test_index_by_accession(self):
        nodes = [
            {"id": "A:1", "cell_set_accession": "ACC_1", "name": "n1"},
            {"id": "A:2", "cell_set_accession": "ACC_2", "name": "n2"},
        ]
        idx = _index_nodes(nodes)
        assert "ACC_1" in idx
        assert idx["ACC_1"]["name"] == "n1"

    def test_fallback_to_id(self):
        nodes = [{"id": "A:1", "name": "n1"}]
        idx = _index_nodes(nodes)
        assert "A:1" in idx


class TestMergeNodes:
    def test_preserve_enrichment(self):
        old = [
            {
                "cell_set_accession": "ACC_1",
                "name": "Old Name",
                "markers": [{"symbol": "X"}],
                "electrophysiology": {"firing_pattern": "old"},
            },
        ]
        new = [
            {
                "cell_set_accession": "ACC_1",
                "name": "New Name",
                "markers": [{"symbol": "Y"}],
            },
        ]
        merged, stats = _merge_nodes(old, new, ENRICHMENT_FIELDS)
        assert len(merged) == 1
        assert merged[0]["name"] == "New Name"
        assert merged[0]["markers"] == [{"symbol": "Y"}]
        assert merged[0]["electrophysiology"]["firing_pattern"] == "old"
        assert stats["updated"] == 1

    def test_new_node_added(self):
        old = [{"cell_set_accession": "ACC_1", "name": "N1"}]
        new = [
            {"cell_set_accession": "ACC_1", "name": "N1"},
            {"cell_set_accession": "ACC_2", "name": "N2"},
        ]
        merged, stats = _merge_nodes(old, new, ENRICHMENT_FIELDS)
        assert len(merged) == 2
        assert stats["added"] == 1

    def test_removed_node_flagged(self):
        old = [
            {"cell_set_accession": "ACC_1", "name": "N1"},
            {"cell_set_accession": "ACC_OLD", "name": "Gone"},
        ]
        new = [{"cell_set_accession": "ACC_1", "name": "N1"}]
        merged, stats = _merge_nodes(old, new, ENRICHMENT_FIELDS)
        assert len(merged) == 2
        assert stats["removed_flagged"] == 1
        flagged = [n for n in merged if n.get("_reingest_status")]
        assert len(flagged) == 1
        assert flagged[0]["cell_set_accession"] == "ACC_OLD"

    def test_enrichment_not_overwritten_by_new(self):
        """If new also has the enrichment field, new wins (it's fresher)."""
        old = [
            {
                "cell_set_accession": "ACC_1",
                "electrophysiology": {"firing_pattern": "old"},
            },
        ]
        new = [
            {
                "cell_set_accession": "ACC_1",
                "electrophysiology": {"firing_pattern": "new"},
            },
        ]
        merged, _ = _merge_nodes(old, new, ENRICHMENT_FIELDS)
        # New already has the field → preserved as-is (not replaced from old)
        assert merged[0]["electrophysiology"]["firing_pattern"] == "new"


class TestLoadGeneMapping:
    def test_load(self, gene_mapping_tsv: Path):
        mapping = load_gene_mapping(gene_mapping_tsv)
        assert mapping["Sst"] == "ENSMUSG00000004366"
        assert mapping["Pvalb"] == "ENSMUSG00000005716"
        assert len(mapping) == 4


class TestYamlIO:
    def test_load_save_roundtrip(self, tmp_taxonomy: Path):
        with patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path:
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"

            data = load_taxonomy_level("TEST001", "cluster")
            assert data["taxonomy_id"] == "TEST001"
            assert len(data["nodes"]) == 2

            # Modify and save
            data["nodes"][0]["name"] = "Modified"
            save_taxonomy_level("TEST001", "cluster", data)

            # Reload and verify
            data2 = load_taxonomy_level("TEST001", "cluster")
            assert data2["nodes"][0]["name"] == "Modified"
            # Other data preserved
            assert data2["nodes"][1]["electrophysiology"]["firing_pattern"] == "fast-spiking"


class TestReingest:
    def test_reingest_preserves_enrichment(self, tmp_taxonomy: Path, tmp_path: Path):
        """Re-ingest preserves enrichment fields from old data."""
        # Create a "new source" JSON that the ingest functions will process
        # We'll mock the ingest to write known data to the temp dir
        new_nodes = [
            {
                "id": "TEST:CLUS_001",
                "name": "Cluster 1 Updated",
                "cell_set_accession": "CLUS_001",
                "taxonomy_id": "TEST001",
                "taxonomy_level": "CLUSTER",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "is_terminal": True,
                "markers": [{"symbol": "Sst", "category": "DEFINING"}],
            },
            {
                "id": "TEST:CLUS_002",
                "name": "Cluster 2 Updated",
                "cell_set_accession": "CLUS_002",
                "taxonomy_id": "TEST001",
                "taxonomy_level": "CLUSTER",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "is_terminal": True,
                "markers": [{"symbol": "Pvalb", "category": "DEFINING"}],
                # No electrophysiology in new source
            },
            {
                "id": "TEST:CLUS_003",
                "name": "Cluster 3 New",
                "cell_set_accession": "CLUS_003",
                "taxonomy_id": "TEST001",
                "taxonomy_level": "CLUSTER",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "is_terminal": True,
            },
        ]

        new_data = {
            "taxonomy_id": "TEST001",
            "taxonomy_level": "CLUSTER",
            "taxonomy_rank": 0,
            "nodes": new_nodes,
        }

        new_meta = {
            "taxonomy_id": "TEST001",
            "taxonomy_name": "Test Taxonomy v2",
            "ingest_date": "2026-04-24",
        }

        # Mock the ingest function to write our test data to tmp
        def fake_ingest(source, taxonomy_id, output_dir):
            out = Path(output_dir)
            with (out / "cluster.yaml").open("w") as fh:
                yaml.dump(new_data, fh, sort_keys=False)
            with (out / "taxonomy_meta.yaml").open("w") as fh:
                yaml.dump(new_meta, fh, sort_keys=False)
            return {"cluster": 3}

        source_json = tmp_path / "source.json"
        source_json.write_text(json.dumps({"not": "cas_format"}))

        with (
            patch("evidencell.taxonomy_ops.taxonomy_dir") as mock_dir,
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_ypath,
            patch("evidencell.taxonomy_ops.ingest_to_yaml", side_effect=fake_ingest),
            patch("evidencell.taxonomy_ops._is_cas_format", return_value=False),
        ):
            mock_dir.return_value = tmp_taxonomy
            mock_ypath.side_effect = lambda tid, level: tmp_taxonomy / f"{level}.yaml"

            result = reingest(
                taxonomy_id="TEST001",
                source_json=source_json,
            )

        assert result["nodes_updated"] == 2  # CLUS_001 and CLUS_002
        assert result["nodes_added"] == 1  # CLUS_003
        assert result["nodes_removed_flagged"] == 0

        # Verify enrichment preserved
        with (tmp_taxonomy / "cluster.yaml").open() as fh:
            data = yaml.safe_load(fh)

        nodes_by_acc = {n["cell_set_accession"]: n for n in data["nodes"]}
        assert nodes_by_acc["CLUS_002"]["name"] == "Cluster 2 Updated"
        assert nodes_by_acc["CLUS_002"]["electrophysiology"]["firing_pattern"] == "fast-spiking"
        assert "electrophysiology" not in nodes_by_acc["CLUS_001"]
        assert "CLUS_003" in nodes_by_acc

        # Verify meta preserved mapmycells
        with (tmp_taxonomy / "taxonomy_meta.yaml").open() as fh:
            meta = yaml.safe_load(fh)
        assert meta["mapmycells"]["at_taxonomy_id"] == "TEST001"
        assert meta["taxonomy_name"] == "Test Taxonomy v2"

    def test_reingest_dry_run(self, tmp_taxonomy: Path, tmp_path: Path):
        """Dry run reports changes without writing."""
        new_data = {
            "taxonomy_id": "TEST001",
            "taxonomy_level": "CLUSTER",
            "nodes": [
                {
                    "cell_set_accession": "CLUS_001",
                    "name": "Updated",
                    "taxonomy_level": "CLUSTER",
                },
            ],
        }

        def fake_ingest(source, taxonomy_id, output_dir):
            out = Path(output_dir)
            with (out / "cluster.yaml").open("w") as fh:
                yaml.dump(new_data, fh, sort_keys=False)
            return {"cluster": 1}

        source_json = tmp_path / "source.json"
        source_json.write_text(json.dumps({"not": "cas"}))

        # Read original state
        with (tmp_taxonomy / "cluster.yaml").open() as fh:
            original = fh.read()

        with (
            patch("evidencell.taxonomy_ops.taxonomy_dir") as mock_dir,
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_ypath,
            patch("evidencell.taxonomy_ops.ingest_to_yaml", side_effect=fake_ingest),
            patch("evidencell.taxonomy_ops._is_cas_format", return_value=False),
        ):
            mock_dir.return_value = tmp_taxonomy
            mock_ypath.side_effect = lambda tid, level: tmp_taxonomy / f"{level}.yaml"

            result = reingest(
                taxonomy_id="TEST001",
                source_json=source_json,
                dry_run=True,
            )

        assert result["dry_run"] is True
        # File should be unchanged
        with (tmp_taxonomy / "cluster.yaml").open() as fh:
            assert fh.read() == original


class TestCLI:
    def test_help(self):
        """CLI --help should work."""
        import subprocess
        result = subprocess.run(
            ["uv", "run", "python", "-m", "evidencell.taxonomy_ops", "--help"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "warm-expression-cache" in result.stdout
        assert "reingest" in result.stdout
        assert "add-expression" not in result.stdout


# ── KB marker union (drives warm-expression-cache) ──────────────────────────


def _make_kb_graphs(tmp_path: Path) -> Path:
    """Create a synthetic kb/graphs/ tree with one classical and one atlas node."""
    g_dir = tmp_path / "kb" / "graphs" / "test_region"
    g_dir.mkdir(parents=True)

    graph_yaml = {
        "nodes": [
            {
                "id": "lit_alpha",
                "name": "Alpha cell",
                "definition_basis": "ARTIFICIAL",
                "defining_markers": [{"symbol": "Sst"}, {"symbol": "Calb1"}],
                "neuropeptides": [{"symbol": "Npy"}],
                "negative_markers": [{"symbol": "Pvalb"}],
            },
            {
                "id": "lit_beta",
                "name": "Beta cell",
                "definition_basis": "ARTIFICIAL",
                "defining_markers": [{"symbol": "Sst"}, {"symbol": "Vip"}],
                "neuropeptides": [],
                "negative_markers": [],
            },
            {
                "id": "atlas_node",
                "name": "Atlas cluster",
                "definition_basis": "ATLAS_TRANSCRIPTOMIC",
                "defining_markers": [{"symbol": "Foo"}],  # must be ignored
                "neuropeptides": [{"symbol": "Bar"}],     # must be ignored
            },
        ]
    }
    (g_dir / "test.yaml").write_text(yaml.safe_dump(graph_yaml))
    return tmp_path


def test_collect_kb_marker_union_unions_lit_node_markers(tmp_path, monkeypatch):
    """The union covers defining + neuropeptides + negative across all
    non-atlas nodes; atlas-node markers are excluded."""
    import evidencell.paths as paths_mod
    _make_kb_graphs(tmp_path)
    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)

    union = collect_kb_marker_union()
    assert union == {"Sst", "Calb1", "Npy", "Pvalb", "Vip"}
    assert "Foo" not in union  # atlas-node markers excluded
    assert "Bar" not in union


def test_collect_kb_marker_union_handles_no_kb_dir(tmp_path, monkeypatch):
    """No kb/graphs directory → empty set, no error."""
    import evidencell.paths as paths_mod
    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)
    assert collect_kb_marker_union() == set()


def test_collect_kb_marker_union_skips_unparseable(tmp_path, monkeypatch):
    """Unparseable YAML files are logged and skipped, not fatal."""
    import evidencell.paths as paths_mod
    g_dir = tmp_path / "kb" / "graphs" / "broken"
    g_dir.mkdir(parents=True)
    (g_dir / "bad.yaml").write_text("this: is: not: valid: yaml: at: all:[")
    (g_dir / "good.yaml").write_text(yaml.safe_dump({
        "nodes": [{
            "id": "x",
            "definition_basis": "ARTIFICIAL",
            "defining_markers": [{"symbol": "Sst"}],
        }]
    }))
    monkeypatch.setattr(paths_mod, "repo_root", lambda: tmp_path)
    union = collect_kb_marker_union()
    assert "Sst" in union


class TestWarmExpressionCacheCLI:
    def test_help(self):
        import subprocess
        result = subprocess.run(
            ["uv", "run", "python", "-m", "evidencell.taxonomy_ops",
             "warm-expression-cache", "--help"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "taxonomy_id" in result.stdout
