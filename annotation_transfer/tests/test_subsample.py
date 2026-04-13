"""Tests for the subsampling module."""

import numpy as np
import pandas as pd
import pytest
import anndata as ad
import scipy.sparse as sp

from annotation_transfer.subsample import subsample_adata, SubsampleError


def _make_adata(n_cells: int, n_genes: int = 50, labels: list[str] | None = None) -> ad.AnnData:
    """Create a test AnnData with optional cluster labels."""
    rng = np.random.default_rng(42)
    X = sp.random(n_cells, n_genes, density=0.1, format="csr", random_state=42)
    X.data = np.round(X.data * 100).astype(np.float32)
    adata = ad.AnnData(X=X)
    adata.obs_names = [f"cell_{i}" for i in range(n_cells)]
    adata.var_names = [f"gene_{i}" for i in range(n_genes)]
    if labels is not None:
        adata.obs["cluster"] = labels
    return adata


def test_noop_under_limit():
    adata = _make_adata(100)
    result = subsample_adata(adata, max_cells=200)
    assert result.n_obs == 100


def test_random_subsample():
    adata = _make_adata(1000)
    result = subsample_adata(adata, max_cells=100)
    assert result.n_obs == 100
    # All cell names should be from the original
    assert set(result.obs_names).issubset(set(adata.obs_names))


def test_stratified_subsample_preserves_proportions():
    # 800 type A, 200 type B → subsample to 100 should give ~80 A, ~20 B
    labels = ["A"] * 800 + ["B"] * 200
    adata = _make_adata(1000, labels=labels)
    result = subsample_adata(adata, max_cells=100, stratify_col="cluster")

    assert result.n_obs == 100
    counts = result.obs["cluster"].value_counts()
    assert counts["A"] >= 70  # roughly proportional
    assert counts["B"] >= 10
    assert counts["A"] + counts["B"] == 100


def test_stratified_guarantees_all_labels():
    # 990 type A, 5 type B, 5 type C → subsample to 50
    labels = ["A"] * 990 + ["B"] * 5 + ["C"] * 5
    adata = _make_adata(1000, labels=labels)
    result = subsample_adata(adata, max_cells=50, stratify_col="cluster")

    assert result.n_obs == 50
    present_labels = set(result.obs["cluster"].unique())
    assert "A" in present_labels
    assert "B" in present_labels
    assert "C" in present_labels


def test_missing_column_raises():
    adata = _make_adata(100)
    with pytest.raises(SubsampleError, match="not found in obs"):
        subsample_adata(adata, max_cells=50, stratify_col="nonexistent")


def test_reproducible_with_seed():
    labels = ["A"] * 500 + ["B"] * 500
    adata = _make_adata(1000, labels=labels)
    r1 = subsample_adata(adata, max_cells=100, stratify_col="cluster", seed=42)
    r2 = subsample_adata(adata, max_cells=100, stratify_col="cluster", seed=42)
    assert list(r1.obs_names) == list(r2.obs_names)


def test_different_seeds_differ():
    labels = ["A"] * 500 + ["B"] * 500
    adata = _make_adata(1000, labels=labels)
    r1 = subsample_adata(adata, max_cells=100, stratify_col="cluster", seed=42)
    r2 = subsample_adata(adata, max_cells=100, stratify_col="cluster", seed=99)
    assert list(r1.obs_names) != list(r2.obs_names)
