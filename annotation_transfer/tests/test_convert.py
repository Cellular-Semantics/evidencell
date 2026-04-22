"""Tests for h5ad → MapMyCells conversion."""

from __future__ import annotations


import anndata as ad
import numpy as np
import pytest
import scipy.sparse as sp

from annotation_transfer.convert import (
    ConversionError,
    prepare_for_mapmycells,
    save_source_labels,
    load_source_labels,
)


def _make_adata(
    n_cells: int = 50,
    n_genes: int = 20,
    *,
    sparse: bool = True,
    cluster_col: str | None = "cluster",
    cluster_values: list[str] | None = None,
    put_counts_in_raw: bool = False,
) -> ad.AnnData:
    """Create a synthetic AnnData for testing."""
    rng = np.random.default_rng(42)
    counts = rng.poisson(5, size=(n_cells, n_genes)).astype(np.float32)

    if sparse:
        X = sp.csr_matrix(counts)
    else:
        X = counts

    obs_names = [f"cell_{i}" for i in range(n_cells)]
    var_names = [f"Gene{i}" for i in range(n_genes)]

    adata = ad.AnnData(X=X)
    adata.obs_names = obs_names
    adata.var_names = var_names

    if cluster_col and cluster_values:
        adata.obs[cluster_col] = rng.choice(cluster_values, size=n_cells)

    if put_counts_in_raw:
        adata.raw = adata.copy()
        # Overwrite X with normalised (non-integer) data
        adata.X = sp.csr_matrix(counts / counts.sum(axis=1, keepdims=True))

    return adata


class TestPrepareForMapmycells:
    def test_basic_conversion(self, tmp_path):
        adata = _make_adata()
        out = tmp_path / "out.h5ad"

        labels = prepare_for_mapmycells(adata, out)

        result = ad.read_h5ad(out)
        assert result.n_obs == 50
        assert result.n_vars == 20
        assert sp.issparse(result.X)
        assert sp.isspmatrix_csr(result.X)
        assert list(result.obs.columns) == ["cell_id"]
        assert list(result.var.columns) == ["gene_id"]
        assert result.raw is None
        # No labels when no cluster_col
        assert labels == {}

    def test_dense_input_converted_to_sparse(self, tmp_path):
        adata = _make_adata(sparse=False)
        out = tmp_path / "out.h5ad"

        prepare_for_mapmycells(adata, out)

        result = ad.read_h5ad(out)
        assert sp.isspmatrix_csr(result.X)

    def test_integer_counts_preserved(self, tmp_path):
        adata = _make_adata()
        out = tmp_path / "out.h5ad"

        prepare_for_mapmycells(adata, out)

        result = ad.read_h5ad(out)
        X = result.X.toarray()
        assert np.allclose(X, np.round(X))
        assert X.min() >= 0

    def test_slice_by_cluster(self, tmp_path):
        adata = _make_adata(cluster_col="cluster", cluster_values=["A", "B", "C"])
        n_a = (adata.obs["cluster"] == "A").sum()
        out = tmp_path / "out.h5ad"

        labels = prepare_for_mapmycells(
            adata, out, cluster_col="cluster", cluster_value="A"
        )

        result = ad.read_h5ad(out)
        assert result.n_obs == n_a
        assert all(v == "A" for v in labels.values())

    def test_source_labels_from_label_col(self, tmp_path):
        adata = _make_adata(cluster_col="cluster", cluster_values=["X", "Y"])
        adata.obs["subtype"] = "sub_" + adata.obs["cluster"]
        out = tmp_path / "out.h5ad"

        labels = prepare_for_mapmycells(adata, out, label_col="subtype")

        assert all(v.startswith("sub_") for v in labels.values())

    def test_raw_counts_used_when_x_is_normalised(self, tmp_path):
        adata = _make_adata(put_counts_in_raw=True)
        out = tmp_path / "out.h5ad"

        prepare_for_mapmycells(adata, out)

        result = ad.read_h5ad(out)
        X = result.X.toarray()
        assert np.allclose(X, np.round(X)), "Should use raw integer counts, not normalised"

    def test_rejects_non_integer_counts(self, tmp_path):
        adata = _make_adata()
        # Replace with normalised data, no raw
        adata.X = sp.csr_matrix(adata.X.toarray() / 10.0 + 0.1)
        out = tmp_path / "out.h5ad"

        with pytest.raises(ConversionError, match="integer counts"):
            prepare_for_mapmycells(adata, out)

    def test_rejects_negative_values(self, tmp_path):
        adata = _make_adata()
        arr = adata.X.toarray()
        arr[0, 0] = -5.0
        adata.X = sp.csr_matrix(arr)
        out = tmp_path / "out.h5ad"

        with pytest.raises(ConversionError, match="negative"):
            prepare_for_mapmycells(adata, out)

    def test_missing_cluster_col_raises(self, tmp_path):
        adata = _make_adata(cluster_col=None)
        out = tmp_path / "out.h5ad"

        with pytest.raises(ConversionError, match="not found"):
            prepare_for_mapmycells(adata, out, cluster_col="nonexistent", cluster_value="X")

    def test_empty_slice_raises(self, tmp_path):
        adata = _make_adata(cluster_col="cluster", cluster_values=["A"])
        out = tmp_path / "out.h5ad"

        with pytest.raises(ConversionError, match="No cells"):
            prepare_for_mapmycells(adata, out, cluster_col="cluster", cluster_value="MISSING")

    def test_does_not_modify_input(self, tmp_path):
        adata = _make_adata(cluster_col="cluster", cluster_values=["A", "B"])
        original_shape = adata.shape
        original_cols = list(adata.obs.columns)
        out = tmp_path / "out.h5ad"

        prepare_for_mapmycells(adata, out, cluster_col="cluster", cluster_value="A")

        assert adata.shape == original_shape
        assert list(adata.obs.columns) == original_cols


class TestSourceLabelsIO:
    def test_roundtrip(self, tmp_path):
        labels = {"cell_0": "TypeA", "cell_1": "TypeB", "cell_2": "TypeA"}
        path = tmp_path / "labels.json"

        save_source_labels(labels, path)
        loaded = load_source_labels(path)

        assert loaded == labels
