"""Tests for F1 matrix computation."""

from __future__ import annotations

import pandas as pd
import pytest

from annotation_transfer.score import compute_f1_matrix, best_mappings


def _make_mmc_df(
    n_cells: int = 100,
    source_groups: dict[str, int] | None = None,
    target_cluster: str = "5188 CBX MLI Megf11 Gaba_1",
    target_supertype: str = "1149 CBX MLI Megf11 Gaba_1",
    target_subclass: str = "311 CBX MLI Megf11 Gaba",
    target_class: str = "28 CB GABA",
    bootstrap: float = 0.95,
) -> tuple[pd.DataFrame, dict[str, str]]:
    """Create a synthetic MapMyCells output DataFrame and source labels.

    By default creates a clean 1:1 mapping scenario.
    """
    if source_groups is None:
        source_groups = {"TypeA": n_cells}

    rows = []
    labels = {}
    cell_idx = 0

    for group, count in source_groups.items():
        for _ in range(count):
            cid = f"cell_{cell_idx}"
            rows.append({
                "cell_id": cid,
                "class_name": target_class,
                "class_bootstrapping_probability": bootstrap,
                "subclass_name": target_subclass,
                "subclass_bootstrapping_probability": bootstrap,
                "supertype_name": target_supertype,
                "supertype_bootstrapping_probability": bootstrap,
                "cluster_name": target_cluster,
                "cluster_alias": 4167,
                "cluster_bootstrapping_probability": bootstrap,
            })
            labels[cid] = group
            cell_idx += 1

    return pd.DataFrame(rows), labels


class TestComputeF1Matrix:
    def test_perfect_mapping(self):
        """All cells from one source group map to one target → F1 = 1.0."""
        df, labels = _make_mmc_df(n_cells=100)

        result = compute_f1_matrix(df, labels)

        assert not result.empty
        # At every level, group_purity and target_purity should be 1.0
        for _, row in result.iterrows():
            assert row["group_purity"] == pytest.approx(1.0)
            assert row["target_purity"] == pytest.approx(1.0)
            assert row["f1"] == pytest.approx(1.0)

    def test_two_groups_one_target(self):
        """Two source groups mapping to the same target: precision < 1.0."""
        df, labels = _make_mmc_df(source_groups={"TypeA": 60, "TypeB": 40})

        result = compute_f1_matrix(df, labels)

        cluster_rows = result[result["level"] == "cluster"]
        assert len(cluster_rows) == 2

        type_a = cluster_rows[cluster_rows["source_label"] == "TypeA"]
        assert type_a["group_purity"].values[0] == pytest.approx(1.0)
        assert type_a["target_purity"].values[0] == pytest.approx(0.6)

        type_b = cluster_rows[cluster_rows["source_label"] == "TypeB"]
        assert type_b["group_purity"].values[0] == pytest.approx(1.0)
        assert type_b["target_purity"].values[0] == pytest.approx(0.4)

    def test_two_groups_two_targets(self):
        """Two groups mapping to different targets → each has F1 = 1.0."""
        df1, labels1 = _make_mmc_df(
            source_groups={"TypeA": 50},
            target_cluster="ClusterA",
            target_supertype="SupertypeA",
            target_subclass="SubclassA",
            target_class="ClassA",
        )
        df2, labels2 = _make_mmc_df(
            source_groups={"TypeB": 50},
            target_cluster="ClusterB",
            target_supertype="SupertypeB",
            target_subclass="SubclassB",
            target_class="ClassB",
        )
        # Avoid cell_id collisions between the two groups
        df2["cell_id"] = [f"cellB_{i}" for i in range(50)]
        labels2 = {f"cellB_{i}": "TypeB" for i in range(50)}

        df = pd.concat([df1, df2], ignore_index=True)
        labels = {**labels1, **labels2}

        result = compute_f1_matrix(df, labels)

        cluster_rows = result[result["level"] == "cluster"]
        assert len(cluster_rows) == 2
        assert list(cluster_rows["f1"]) == pytest.approx([1.0, 1.0])

    def test_bootstrap_filtering(self):
        """Cells below threshold are excluded."""
        df, labels = _make_mmc_df(n_cells=100, bootstrap=0.5)

        result = compute_f1_matrix(df, labels, threshold=0.8)

        # All cells have bootstrap 0.5, below 0.8 threshold → empty
        assert result.empty

    def test_mixed_bootstrap(self):
        """Only high-bootstrap cells are counted."""
        df, labels = _make_mmc_df(n_cells=100, bootstrap=0.95)
        # Add 20 low-bootstrap cells
        low_df, low_labels = _make_mmc_df(
            source_groups={"TypeA": 20}, bootstrap=0.5
        )
        # Rename cell IDs to avoid collision
        low_df["cell_id"] = [f"low_cell_{i}" for i in range(20)]
        low_labels = {f"low_cell_{i}": "TypeA" for i in range(20)}

        combined_df = pd.concat([df, low_df], ignore_index=True)
        combined_labels = {**labels, **low_labels}

        result = compute_f1_matrix(combined_df, combined_labels, threshold=0.8)

        # Only 100 high-bootstrap cells should be counted, not the 20 low ones
        cluster_rows = result[result["level"] == "cluster"]
        assert cluster_rows["n_cells"].sum() == 100

    def test_specific_levels(self):
        """Can compute for a subset of levels."""
        df, labels = _make_mmc_df(n_cells=50)

        result = compute_f1_matrix(df, labels, levels=["cluster", "supertype"])

        assert set(result["level"]) == {"cluster", "supertype"}

    def test_empty_labels(self):
        """No matching labels → empty result."""
        df, _ = _make_mmc_df(n_cells=50)

        result = compute_f1_matrix(df, {})

        assert result.empty

    def test_from_csv(self, tmp_path):
        """Can read from a CSV file path."""
        df, labels = _make_mmc_df(n_cells=30)
        csv_path = tmp_path / "mmc_output.csv"
        df.to_csv(csv_path, index=False)

        result = compute_f1_matrix(csv_path, labels)

        assert not result.empty
        assert len(result[result["level"] == "cluster"]) == 1


class TestBestMappings:
    def test_picks_best_per_level(self):
        """Returns one row per (source_label, level)."""
        df, labels = _make_mmc_df(source_groups={"TypeA": 70, "TypeB": 30})

        f1_df = compute_f1_matrix(df, labels)
        best = best_mappings(f1_df)

        # 2 source labels × 4 levels = 8 rows
        assert len(best) == 8
        assert set(best["source_label"]) == {"TypeA", "TypeB"}
        assert set(best.columns) == {
            "source_label", "level", "best_target",
            "group_purity", "target_purity", "f1", "n_cells", "median_boot",
        }

    def test_empty_input(self):
        best = best_mappings(pd.DataFrame())
        assert best.empty

    def test_sorted_by_level(self):
        df, labels = _make_mmc_df(n_cells=50)

        f1_df = compute_f1_matrix(df, labels)
        best = best_mappings(f1_df)

        levels = list(best["level"])
        assert levels == ["class", "subclass", "supertype", "cluster"]
