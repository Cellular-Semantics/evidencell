"""Subsample AnnData objects to fit within MapMyCells web API limits.

The MapMyCells web service accepts files up to 2 GB / ~150K cells.
This module provides stratified subsampling that preserves the proportion
of each source cluster label, ensuring rare cell types are represented.
"""

from __future__ import annotations

from pathlib import Path

import anndata as ad
import numpy as np


# MapMyCells web limits
DEFAULT_MAX_CELLS = 150_000
MAX_FILE_SIZE_GB = 2.0


class SubsampleError(Exception):
    """Raised when subsampling fails."""


def subsample_adata(
    adata: ad.AnnData,
    max_cells: int = DEFAULT_MAX_CELLS,
    *,
    stratify_col: str | None = None,
    seed: int = 42,
) -> ad.AnnData:
    """Subsample an AnnData to at most max_cells rows.

    Parameters
    ----------
    adata
        Input AnnData (not modified).
    max_cells
        Maximum number of cells to keep.
    stratify_col
        Column in obs for stratified sampling. Each label gets a number
        of cells proportional to its frequency in the original data,
        with a minimum of 1 cell per label. Falls back to random
        sampling if None.
    seed
        Random seed for reproducibility.

    Returns
    -------
    Subsampled AnnData (copy). If n_obs <= max_cells, returns a copy
    with no subsampling.
    """
    if adata.n_obs <= max_cells:
        return adata.copy()

    rng = np.random.default_rng(seed)

    if stratify_col is None:
        indices = rng.choice(adata.n_obs, size=max_cells, replace=False)
        indices.sort()
        return adata[indices].copy()

    if stratify_col not in adata.obs.columns:
        raise SubsampleError(
            f"Column '{stratify_col}' not found in obs. "
            f"Available: {list(adata.obs.columns)}"
        )

    labels = adata.obs[stratify_col].astype(str)
    label_counts = labels.value_counts()
    n_labels = len(label_counts)

    if n_labels > max_cells:
        raise SubsampleError(
            f"More unique labels ({n_labels}) than max_cells ({max_cells}). "
            f"Cannot guarantee ≥1 cell per label."
        )

    # Allocate proportionally, ensuring ≥1 per label
    fractions = label_counts / label_counts.sum()
    allocations = (fractions * max_cells).astype(int)
    # Ensure minimum 1 per label
    allocations = allocations.clip(lower=1)

    # If over budget due to minimums, trim from the largest groups
    while allocations.sum() > max_cells:
        largest = allocations.idxmax()
        allocations[largest] -= 1

    # If under budget, add to largest groups
    while allocations.sum() < max_cells:
        for label in label_counts.index:
            if allocations.sum() >= max_cells:
                break
            if allocations[label] < label_counts[label]:
                allocations[label] += 1

    # Sample from each group
    all_indices: list[int] = []
    for label, n_sample in allocations.items():
        group_idx = np.where(labels.values == label)[0]
        n_sample = min(n_sample, len(group_idx))
        chosen = rng.choice(group_idx, size=n_sample, replace=False)
        all_indices.extend(chosen.tolist())

    all_indices.sort()
    return adata[all_indices].copy()


def subsample_file(
    input_path: Path,
    output_path: Path,
    max_cells: int = DEFAULT_MAX_CELLS,
    *,
    stratify_col: str | None = None,
    seed: int = 42,
) -> int:
    """Subsample an h5ad file and write the result.

    Returns the number of cells in the output.
    """
    adata = ad.read_h5ad(input_path)
    sub = subsample_adata(
        adata, max_cells, stratify_col=stratify_col, seed=seed,
    )
    sub.write_h5ad(output_path, compression="gzip")
    return sub.n_obs
