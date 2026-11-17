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


def _log2cpm_adata(n_cells: int = 20, n_genes: int = 30) -> ad.AnnData:
    """Synthetic AnnData whose X is a well-formed log2(CPM+1) matrix."""
    rng = np.random.default_rng(7)
    counts = rng.poisson(5, size=(n_cells, n_genes)).astype(float) + 1.0
    cpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
    adata = ad.AnnData(X=sp.csr_matrix(np.log2(cpm + 1.0)))
    adata.obs_names = [f"cell_{i}" for i in range(n_cells)]
    adata.var_names = [f"Gene{i}" for i in range(n_genes)]
    return adata


class TestNormalizationModes:
    def test_unknown_normalization_rejected(self, tmp_path):
        with pytest.raises(ConversionError, match="Unknown normalization"):
            prepare_for_mapmycells(
                _make_adata(), tmp_path / "out.h5ad", normalization="cpm"
            )

    def test_raw_mode_still_rejects_non_integer(self, tmp_path):
        with pytest.raises(ConversionError, match="integer counts"):
            prepare_for_mapmycells(_log2cpm_adata(), tmp_path / "out.h5ad")

    def test_log2cpm_mode_accepts_non_integer(self, tmp_path):
        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(
            _log2cpm_adata(), out, normalization="log2CPM"
        )
        written = ad.read_h5ad(out)
        assert written.n_obs == 20
        assert not np.allclose(
            written.X.toarray(), np.round(written.X.toarray())
        )

    def test_log2cpm_mode_rejects_linear_values(self, tmp_path):
        """Linear TPM passed as log2CPM — the mistake the max check catches."""
        rng = np.random.default_rng(3)
        counts = rng.poisson(5, size=(10, 20)).astype(float) + 1.0
        tpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
        adata = ad.AnnData(X=sp.csr_matrix(tpm))
        adata.obs_names = [f"c{i}" for i in range(10)]
        adata.var_names = [f"G{i}" for i in range(20)]
        with pytest.raises(ConversionError, match="above the"):
            prepare_for_mapmycells(
                adata, tmp_path / "out.h5ad", normalization="log2CPM"
            )

    def test_log2cpm_mode_rejects_negative(self, tmp_path):
        adata = _log2cpm_adata()
        dense = adata.X.toarray()
        dense[0, 0] = -1.0
        adata.X = sp.csr_matrix(dense)
        with pytest.raises(ConversionError, match="negative"):
            prepare_for_mapmycells(
                adata, tmp_path / "out.h5ad", normalization="log2CPM"
            )

    def test_log2cpm_mode_warns_on_wrong_log_base(self, tmp_path):
        """ln(TPM+1) mis-declared as log2(TPM+1): no error upstream, so the
        de-logged library-size check is the only thing that notices."""
        rng = np.random.default_rng(11)
        counts = rng.poisson(5, size=(20, 30)).astype(float) + 1.0
        tpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
        adata = ad.AnnData(X=sp.csr_matrix(np.log(tpm + 1.0)))
        adata.obs_names = [f"c{i}" for i in range(20)]
        adata.var_names = [f"G{i}" for i in range(30)]
        with pytest.warns(UserWarning, match="log base"):
            prepare_for_mapmycells(
                adata, tmp_path / "out.h5ad", normalization="log2CPM"
            )

    def test_log2cpm_mode_ignores_adata_raw(self, tmp_path):
        """In log2CPM mode X is the matrix to map; adata.raw must not be
        substituted (it would swap the normalised matrix for counts)."""
        adata = _log2cpm_adata()
        raw_copy = adata.copy()
        raw_copy.X = sp.csr_matrix(
            np.ones(adata.shape, dtype=float) * 3.0
        )
        adata.raw = raw_copy
        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(adata, out, normalization="log2CPM")
        written = ad.read_h5ad(out).X.toarray()
        assert not np.allclose(written, 3.0)


class TestToLog2Cpm:
    def test_tpm_roundtrip(self):
        from annotation_transfer.convert import to_log2cpm

        rng = np.random.default_rng(5)
        counts = rng.poisson(5, size=(10, 20)).astype(float) + 1.0
        tpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
        adata = ad.AnnData(X=sp.csr_matrix(tpm))
        adata.var_names = [f"G{i}" for i in range(20)]

        out = to_log2cpm(adata, input_scale="tpm")
        np.testing.assert_allclose(
            out.X.toarray(), np.log2(tpm + 1.0), rtol=1e-6
        )

    def test_ln1p_input_matches_direct_log2(self):
        """The ln → log2 conversion that is easy to get wrong by hand."""
        from annotation_transfer.convert import to_log2cpm

        rng = np.random.default_rng(6)
        counts = rng.poisson(5, size=(10, 20)).astype(float) + 1.0
        tpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
        adata = ad.AnnData(X=sp.csr_matrix(np.log(tpm + 1.0)))
        adata.var_names = [f"G{i}" for i in range(20)]

        out = to_log2cpm(adata, input_scale="ln1p")
        np.testing.assert_allclose(
            out.X.toarray(), np.log2(tpm + 1.0), rtol=1e-5
        )

    def test_output_passes_log2cpm_validation(self, tmp_path):
        from annotation_transfer.convert import to_log2cpm

        rng = np.random.default_rng(8)
        counts = rng.poisson(5, size=(15, 25)).astype(float) + 1.0
        tpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
        adata = ad.AnnData(X=sp.csr_matrix(tpm))
        adata.obs_names = [f"c{i}" for i in range(15)]
        adata.var_names = [f"G{i}" for i in range(25)]

        out = to_log2cpm(adata, input_scale="tpm")
        prepare_for_mapmycells(
            out, tmp_path / "out.h5ad", normalization="log2CPM"
        )

    def test_gene_length_correction_rescales_to_1e6(self):
        from annotation_transfer.convert import to_log2cpm

        rng = np.random.default_rng(9)
        counts = rng.poisson(5, size=(8, 10)).astype(float) + 1.0
        tpm = counts / counts.sum(axis=1, keepdims=True) * 1e6
        adata = ad.AnnData(X=sp.csr_matrix(tpm))
        adata.obs_names = [f"c{i}" for i in range(8)]
        adata.var_names = [f"G{i}" for i in range(10)]
        lengths = {f"G{i}": 500.0 * (i + 1) for i in range(10)}

        out = to_log2cpm(adata, input_scale="tpm", gene_lengths=lengths)
        delogged = np.expm1(out.X.toarray() * np.log(2))
        np.testing.assert_allclose(delogged.sum(axis=1), 1e6, rtol=1e-4)
        # Long genes gain relative weight once length normalisation is undone.
        assert out.X.toarray()[:, -1].mean() > np.log2(tpm + 1.0)[:, -1].mean()

    def test_unknown_input_scale_rejected(self):
        from annotation_transfer.convert import to_log2cpm

        with pytest.raises(ConversionError, match="Unknown input_scale"):
            to_log2cpm(_log2cpm_adata(), input_scale="rpkm")
