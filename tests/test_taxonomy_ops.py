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
    add_expression,
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
                "precomputed_expression": {
                    "source": "old_stats.h5",
                    "level": "cluster",
                    "genes": [
                        {"symbol": "Pvalb", "ensembl_id": "ENSMUSG00000005716", "mean_expression": 5.0},
                    ],
                },
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

    def test_expression_in_enrichment(self):
        assert "precomputed_expression" in ENRICHMENT_FIELDS


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
                "precomputed_expression": {"source": "old.h5", "genes": []},
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
        assert merged[0]["precomputed_expression"]["source"] == "old.h5"
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
                "precomputed_expression": {"source": "old"},
            },
        ]
        new = [
            {
                "cell_set_accession": "ACC_1",
                "precomputed_expression": {"source": "new"},
            },
        ]
        merged, _ = _merge_nodes(old, new, ENRICHMENT_FIELDS)
        # New already has the field → preserved as-is (not replaced from old)
        assert merged[0]["precomputed_expression"]["source"] == "new"


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
            assert data2["nodes"][1]["precomputed_expression"]["source"] == "old_stats.h5"


class TestAddExpression:
    def test_add_expression_basic(self, tmp_taxonomy: Path, gene_mapping_tsv: Path):
        """Test add-expression with mock HDF5 data."""
        import numpy as np

        gene_mapping = load_gene_mapping(gene_mapping_tsv)

        # Mock the HDF5 loading
        col_names = ["ENSMUSG00000004366", "ENSMUSG00000026787", "ENSMUSG00000005716"]
        cluster_to_row = {"CLUS_001": 0, "CLUS_002": 1}
        sum_matrix = np.array([
            [3.5, 1.2, 0.1],  # CLUS_001: Sst=3.5, Gad1=1.2, Pvalb=0.1
            [0.3, 0.8, 8.7],  # CLUS_002: Sst=0.3, Gad1=0.8, Pvalb=8.7
        ])

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names, cluster_to_row, sum_matrix)

            result = add_expression(
                taxonomy_id="TEST001",
                stats_path="fake.h5",
                genes=["Sst", "Pvalb"],
                gene_mapping=gene_mapping,
                level="cluster",
            )

        assert result["updated"] == 2
        assert result["genes_found"] == 2
        assert result["genes_missing"] == []

        # Verify written data
        with (tmp_taxonomy / "cluster.yaml").open() as fh:
            data = yaml.safe_load(fh)

        node1 = data["nodes"][0]
        assert "precomputed_expression" in node1
        expr = node1["precomputed_expression"]
        assert expr["source"] == "fake.h5"
        assert len(expr["genes"]) == 2
        sst = next(g for g in expr["genes"] if g["symbol"] == "Sst")
        assert sst["mean_expression"] == 3.5
        assert sst["ensembl_id"] == "ENSMUSG00000004366"

    def test_add_expression_filters_accessions(self, tmp_taxonomy: Path, gene_mapping_tsv: Path):
        """Only update specified accessions."""
        import numpy as np

        gene_mapping = load_gene_mapping(gene_mapping_tsv)
        col_names = ["ENSMUSG00000004366"]
        cluster_to_row = {"CLUS_001": 0, "CLUS_002": 1}
        sum_matrix = np.array([[3.5], [0.3]])

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names, cluster_to_row, sum_matrix)

            result = add_expression(
                taxonomy_id="TEST001",
                stats_path="fake.h5",
                genes=["Sst"],
                gene_mapping=gene_mapping,
                level="cluster",
                accessions=["CLUS_001"],
            )

        assert result["updated"] == 1
        assert result["skipped"] == 1

    def test_missing_genes_reported(self, tmp_taxonomy: Path, gene_mapping_tsv: Path):
        """Genes not in mapping are reported as missing."""
        import numpy as np

        gene_mapping = load_gene_mapping(gene_mapping_tsv)
        col_names = ["ENSMUSG00000004366"]
        cluster_to_row = {"CLUS_001": 0}
        sum_matrix = np.array([[3.5]])

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names, cluster_to_row, sum_matrix)

            result = add_expression(
                taxonomy_id="TEST001",
                stats_path="fake.h5",
                genes=["Sst", "FakeGene"],
                gene_mapping=gene_mapping,
                level="cluster",
            )

        assert "FakeGene" in result["genes_missing"]

    def test_add_expression_merges_sequential_calls(self, tmp_taxonomy: Path, gene_mapping_tsv: Path):
        """Two sequential calls with disjoint gene sets leave both sets in YAML (issue #40)."""
        import numpy as np

        gene_mapping = load_gene_mapping(gene_mapping_tsv)

        # First call: Sst + Gad1
        col_names_1 = ["ENSMUSG00000004366", "ENSMUSG00000026787"]  # Sst, Gad1
        cluster_to_row = {"CLUS_001": 0, "CLUS_002": 1}
        sum_matrix_1 = np.array([[3.5, 1.2], [0.3, 0.8]])

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names_1, cluster_to_row, sum_matrix_1)
            add_expression(
                taxonomy_id="TEST001",
                stats_path="fake1.h5",
                genes=["Sst", "Gad1"],
                gene_mapping=gene_mapping,
                level="cluster",
            )

        # Second call: Cck only (disjoint)
        col_names_2 = ["ENSMUSG00000032532"]  # Cck
        sum_matrix_2 = np.array([[5.1], [2.3]])

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names_2, cluster_to_row, sum_matrix_2)
            add_expression(
                taxonomy_id="TEST001",
                stats_path="fake2.h5",
                genes=["Cck"],
                gene_mapping=gene_mapping,
                level="cluster",
            )

        with (tmp_taxonomy / "cluster.yaml").open() as fh:
            data = yaml.safe_load(fh)

        node1 = data["nodes"][0]
        symbols = {g["symbol"] for g in node1["precomputed_expression"]["genes"]}
        assert "Sst" in symbols, "Sst from first call was dropped"
        assert "Gad1" in symbols, "Gad1 from first call was dropped"
        assert "Cck" in symbols, "Cck from second call is missing"
        assert len(symbols) == 3

    def test_add_expression_updates_existing_gene(self, tmp_taxonomy: Path, gene_mapping_tsv: Path):
        """Re-pushing a gene with a new value replaces it rather than duplicating."""
        import numpy as np

        gene_mapping = load_gene_mapping(gene_mapping_tsv)
        col_names = ["ENSMUSG00000004366"]  # Sst
        cluster_to_row = {"CLUS_001": 0, "CLUS_002": 1}

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names, cluster_to_row, np.array([[3.5], [0.3]]))
            add_expression(
                taxonomy_id="TEST001", stats_path="fake.h5",
                genes=["Sst"], gene_mapping=gene_mapping, level="cluster",
            )

        with (
            patch("evidencell.taxonomy_ops.taxonomy_yaml_path") as mock_path,
            patch("evidencell.taxonomy_ops.load_stats_h5") as mock_h5,
        ):
            mock_path.return_value = tmp_taxonomy / "cluster.yaml"
            mock_h5.return_value = (col_names, cluster_to_row, np.array([[9.9], [0.1]]))
            add_expression(
                taxonomy_id="TEST001", stats_path="fake.h5",
                genes=["Sst"], gene_mapping=gene_mapping, level="cluster",
            )

        with (tmp_taxonomy / "cluster.yaml").open() as fh:
            data = yaml.safe_load(fh)

        node1 = data["nodes"][0]
        genes = node1["precomputed_expression"]["genes"]
        sst_entries = [g for g in genes if g["symbol"] == "Sst"]
        assert len(sst_entries) == 1, "Sst should not be duplicated"
        assert sst_entries[0]["mean_expression"] == 9.9


class TestReingest:
    def test_reingest_preserves_enrichment(self, tmp_taxonomy: Path, tmp_path: Path):
        """Re-ingest preserves precomputed_expression from old data."""
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
                # No precomputed_expression in new source
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
        assert nodes_by_acc["CLUS_002"]["precomputed_expression"]["source"] == "old_stats.h5"
        assert "precomputed_expression" not in nodes_by_acc["CLUS_001"]
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
        assert "add-expression" in result.stdout
        assert "reingest" in result.stdout

    def test_add_expression_help(self):
        import subprocess
        result = subprocess.run(
            ["uv", "run", "python", "-m", "evidencell.taxonomy_ops", "add-expression", "--help"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "gene_mapping" in result.stdout
