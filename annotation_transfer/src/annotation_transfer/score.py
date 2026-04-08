"""Compute F1 matrix from MapMyCells output + source cluster labels.

The core logic follows the analysis in the MLI-PLI annotation notebooks
(build_all_combined pattern): for each taxonomy level, compute
group_purity (precision) and target_purity (recall), then F1 as the
harmonic mean.

MapMyCells CSV columns (expected):
    cell_id,
    class_name, class_bootstrapping_probability,
    subclass_name, subclass_bootstrapping_probability,
    supertype_name, supertype_bootstrapping_probability,
    cluster_name, cluster_alias, cluster_bootstrapping_probability
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

# MapMyCells CSV column mapping: level → (name_col, prob_col)
LEVEL_COLUMNS: dict[str, tuple[str, str]] = {
    "class": ("class_name", "class_bootstrapping_probability"),
    "subclass": ("subclass_name", "subclass_bootstrapping_probability"),
    "supertype": ("supertype_name", "supertype_bootstrapping_probability"),
    "cluster": ("cluster_name", "cluster_bootstrapping_probability"),
}

DEFAULT_LEVELS = ["class", "subclass", "supertype", "cluster"]


def _build_level_stats(
    df: pd.DataFrame,
    level: str,
    name_col: str,
    prob_col: str,
    threshold: float,
) -> pd.DataFrame:
    """Compute per-(source_label, target) statistics for one taxonomy level.

    Filters by bootstrap > threshold, groups by (source_label, target_name),
    computes n_cells, group_purity, target_purity, and bootstrap stats.
    """
    dfl = df[df[prob_col] > threshold].copy()
    if dfl.empty:
        return pd.DataFrame()

    g = (
        dfl.groupby(["source_label", name_col])
        .agg(
            n_cells=("cell_id", "count"),
            mean_boot=(prob_col, "mean"),
            median_boot=(prob_col, "median"),
        )
        .reset_index()
        .rename(columns={name_col: "target_name"})
    )
    g["level"] = level
    g["group_purity"] = g["n_cells"] / g.groupby("source_label")["n_cells"].transform("sum")
    g["target_purity"] = g["n_cells"] / g.groupby("target_name")["n_cells"].transform("sum")

    return g


def _build_cluster_with_hierarchy_gate(
    df: pd.DataFrame,
    threshold: float,
) -> pd.DataFrame:
    """Cluster-level stats with hierarchy gate: all levels must pass threshold.

    This is stricter than per-level gating — a cell only counts at cluster level
    if its bootstrap score exceeds the threshold at every level in the hierarchy.
    """
    gate_cols = [col for _, (_, col) in LEVEL_COLUMNS.items()]
    mask = pd.Series(True, index=df.index)
    for col in gate_cols:
        if col in df.columns:
            mask &= df[col] > threshold

    dfl = df[mask].copy()
    if dfl.empty:
        return pd.DataFrame()

    name_col = "cluster_name"
    prob_col = "cluster_bootstrapping_probability"

    g = (
        dfl.groupby(["source_label", name_col])
        .agg(
            n_cells=("cell_id", "count"),
            mean_boot=(prob_col, "mean"),
            median_boot=(prob_col, "median"),
        )
        .reset_index()
        .rename(columns={name_col: "target_name"})
    )
    g["level"] = "cluster"
    g["group_purity"] = g["n_cells"] / g.groupby("source_label")["n_cells"].transform("sum")
    g["target_purity"] = g["n_cells"] / g.groupby("target_name")["n_cells"].transform("sum")

    return g


def compute_f1_matrix(
    mmc_csv: Path | pd.DataFrame,
    source_labels: dict[str, str],
    *,
    threshold: float = 0.8,
    levels: list[str] | None = None,
) -> pd.DataFrame:
    """Compute F1 scores from MapMyCells output and source cluster labels.

    Parameters
    ----------
    mmc_csv
        Path to MapMyCells output CSV, or a pre-loaded DataFrame.
    source_labels
        Mapping of cell_id → source cluster label.
    threshold
        Bootstrap probability threshold (default 0.8).
    levels
        Which taxonomy levels to compute. Default: all four.

    Returns
    -------
    DataFrame with columns: source_label, level, target_name, n_cells,
    group_purity, target_purity, f1, mean_boot, median_boot.
    """
    if levels is None:
        levels = DEFAULT_LEVELS

    if isinstance(mmc_csv, pd.DataFrame):
        df = mmc_csv.copy()
    else:
        df = pd.read_csv(mmc_csv)

    # Join source labels
    df["source_label"] = df["cell_id"].map(source_labels)
    df = df.dropna(subset=["source_label"])

    if df.empty:
        return pd.DataFrame(
            columns=[
                "source_label", "level", "target_name", "n_cells",
                "group_purity", "target_purity", "f1", "mean_boot", "median_boot",
            ]
        )

    frames: list[pd.DataFrame] = []

    # Non-cluster levels: per-level bootstrap gate
    for level in levels:
        if level == "cluster":
            continue
        if level not in LEVEL_COLUMNS:
            continue
        name_col, prob_col = LEVEL_COLUMNS[level]
        if name_col not in df.columns:
            continue
        stats = _build_level_stats(df, level, name_col, prob_col, threshold)
        if not stats.empty:
            frames.append(stats)

    # Cluster level: hierarchy gate (all levels must pass)
    if "cluster" in levels and "cluster_name" in df.columns:
        cluster_stats = _build_cluster_with_hierarchy_gate(df, threshold)
        if not cluster_stats.empty:
            frames.append(cluster_stats)

    if not frames:
        return pd.DataFrame(
            columns=[
                "source_label", "level", "target_name", "n_cells",
                "group_purity", "target_purity", "f1", "mean_boot", "median_boot",
            ]
        )

    combined = pd.concat(frames, ignore_index=True)

    # F1 = harmonic mean of group_purity and target_purity
    denom = combined["group_purity"] + combined["target_purity"]
    combined["f1"] = (
        (2 * combined["group_purity"] * combined["target_purity"])
        / denom.replace(0, np.nan)
    ).fillna(0.0)

    return combined[
        [
            "source_label", "level", "target_name", "n_cells",
            "group_purity", "target_purity", "f1", "mean_boot", "median_boot",
        ]
    ]


def best_mappings(f1_df: pd.DataFrame) -> pd.DataFrame:
    """Extract the best target per (source_label, level) by highest group_purity.

    Returns
    -------
    DataFrame with columns: source_label, level, best_target,
    group_purity, target_purity, f1, n_cells, median_boot.
    """
    if f1_df.empty:
        return pd.DataFrame(
            columns=[
                "source_label", "level", "best_target",
                "group_purity", "target_purity", "f1", "n_cells", "median_boot",
            ]
        )

    idx = f1_df.groupby(["level", "source_label"])["group_purity"].idxmax()
    best = (
        f1_df.loc[
            idx,
            [
                "source_label", "level", "target_name", "n_cells",
                "group_purity", "target_purity", "f1", "median_boot",
            ],
        ]
        .rename(columns={"target_name": "best_target"})
        .reset_index(drop=True)
    )

    # Sort by source_label then level order
    level_order = pd.CategoricalDtype(DEFAULT_LEVELS, ordered=True)
    best["level"] = best["level"].astype(level_order)
    best = best.sort_values(["source_label", "level"]).reset_index(drop=True)

    return best
