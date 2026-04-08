"""Tier 2: Synthetic format zoo — test convert.py against varied h5ad layouts and 10x mtx bundles.

Each test creates a small synthetic dataset in a specific format variant,
runs prepare_for_mapmycells, and asserts the output is valid MapMyCells-ready h5ad.
"""

from __future__ import annotations

import gzip
from pathlib import Path

import anndata as ad
import numpy as np
import scipy.sparse as sp
import scipy.io as sio

from annotation_transfer.convert import prepare_for_mapmycells, ConversionError


def _assert_valid_mmc_h5ad(path: Path, expected_n_cells: int | None = None):
    """Assert that an h5ad file is valid MapMyCells input."""
    a = ad.read_h5ad(path)

    # Sparse CSR integer counts
    assert sp.issparse(a.X), "X must be sparse"
    assert sp.isspmatrix_csr(a.X), "X must be CSR"
    sample = a.X[:min(10, a.n_obs), :].toarray()
    assert np.allclose(sample, np.round(sample)), "X must be integer counts"
    assert sample.min() >= 0, "X must be non-negative"

    # Minimal obs/var
    assert "cell_id" in a.obs.columns
    assert "gene_id" in a.var.columns
    assert a.raw is None

    if expected_n_cells is not None:
        assert a.n_obs == expected_n_cells


def _make_counts(n_cells: int = 30, n_genes: int = 15, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.poisson(3, size=(n_cells, n_genes)).astype(np.float32)


# --- Format variants ---


class TestH5adCountsInX:
    """Happy path: counts already in X."""

    def test_sparse_csr(self, tmp_path):
        counts = _make_counts()
        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.obs["cluster"] = "TypeA"

        out = tmp_path / "out.h5ad"
        labels = prepare_for_mapmycells(a, out, label_col="cluster")

        _assert_valid_mmc_h5ad(out, expected_n_cells=30)
        assert all(v == "TypeA" for v in labels.values())

    def test_sparse_csc(self, tmp_path):
        """CSC input should be converted to CSR."""
        counts = _make_counts()
        a = ad.AnnData(X=sp.csc_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]

        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(a, out)

        _assert_valid_mmc_h5ad(out)

    def test_dense(self, tmp_path):
        """Dense numpy array input."""
        counts = _make_counts()
        a = ad.AnnData(X=counts)
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]

        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(a, out)

        _assert_valid_mmc_h5ad(out)


class TestH5adCountsInRaw:
    """Counts in raw.X, normalised data in X."""

    def test_normalised_x_raw_counts(self, tmp_path):
        counts = _make_counts()
        normed = counts / counts.sum(axis=1, keepdims=True)

        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.raw = a.copy()
        a.X = sp.csr_matrix(normed)

        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(a, out)

        _assert_valid_mmc_h5ad(out)

    def test_log_transformed_x(self, tmp_path):
        """log1p-transformed X with raw counts in raw."""
        counts = _make_counts()
        log_x = np.log1p(counts)

        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.raw = a.copy()
        a.X = sp.csr_matrix(log_x)

        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(a, out)

        _assert_valid_mmc_h5ad(out)


class TestNonStandardObsColumns:
    """Datasets with different annotation column names."""

    def test_celltype_column(self, tmp_path):
        counts = _make_counts()
        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.obs["celltype"] = np.random.choice(["Neuron", "Glia"], size=a.n_obs)

        out = tmp_path / "out.h5ad"
        labels = prepare_for_mapmycells(a, out, label_col="celltype")

        _assert_valid_mmc_h5ad(out)
        assert set(labels.values()) <= {"Neuron", "Glia"}

    def test_multiple_granularities(self, tmp_path):
        """obs has both coarse and fine annotations."""
        counts = _make_counts()
        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.obs["broad_type"] = "GABAergic"
        a.obs["subclass"] = np.random.choice(["Sst", "Pvalb", "Vip"], size=a.n_obs)
        a.obs["cluster_id"] = np.random.choice(["C1", "C2", "C3", "C4"], size=a.n_obs)

        out = tmp_path / "out.h5ad"
        # Use the fine-grained column
        labels = prepare_for_mapmycells(a, out, label_col="cluster_id")

        _assert_valid_mmc_h5ad(out)
        assert set(labels.values()) <= {"C1", "C2", "C3", "C4"}

    def test_slice_then_label(self, tmp_path):
        """Slice by one column, label by another."""
        counts = _make_counts(n_cells=60)
        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.obs["major_class"] = np.random.choice(["GABA", "Glut"], size=a.n_obs)
        a.obs["subtype"] = np.random.choice(["Sub1", "Sub2", "Sub3"], size=a.n_obs)

        n_gaba = (a.obs["major_class"] == "GABA").sum()
        out = tmp_path / "out.h5ad"
        labels = prepare_for_mapmycells(
            a, out,
            cluster_col="major_class", cluster_value="GABA",
            label_col="subtype",
        )

        _assert_valid_mmc_h5ad(out, expected_n_cells=n_gaba)
        assert set(labels.values()) <= {"Sub1", "Sub2", "Sub3"}


class TestExtraMetadata:
    """h5ad with extra obs/var columns, obsm, uns that should be stripped."""

    def test_extra_obs_var_stripped(self, tmp_path):
        counts = _make_counts()
        a = ad.AnnData(X=sp.csr_matrix(counts))
        a.obs_names = [f"c{i}" for i in range(a.n_obs)]
        a.var_names = [f"Gene{i}" for i in range(a.n_vars)]
        a.obs["nCount_RNA"] = 1000
        a.obs["nFeature_RNA"] = 500
        a.obs["percent_mt"] = 0.02
        a.var["highly_variable"] = True
        a.var["means"] = 5.0
        a.uns["neighbors"] = {"foo": "bar"}

        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(a, out)

        result = ad.read_h5ad(out)
        assert list(result.obs.columns) == ["cell_id"]
        assert list(result.var.columns) == ["gene_id"]
        assert len(result.uns) == 0


class TestMtxBundleLoading:
    """Test loading 10x mtx bundles into AnnData then converting.

    This tests the load path that the agentic skill would use,
    not convert.py directly (which takes AnnData).
    """

    def _write_mtx_bundle(self, tmp_path: Path, n_cells: int = 20, n_genes: int = 10):
        """Write a minimal 10x-style mtx bundle."""
        rng = np.random.default_rng(42)
        counts = sp.random(n_cells, n_genes, density=0.3, format="coo",
                           dtype=np.float64, random_state=rng)
        counts.data = np.round(counts.data * 10).astype(np.float64)

        sio.mmwrite(str(tmp_path / "matrix.mtx"), counts)

        barcodes = tmp_path / "barcodes.tsv"
        barcodes.write_text("\n".join(f"BARCODE{i}-1" for i in range(n_cells)) + "\n")

        features = tmp_path / "features.tsv"
        features.write_text(
            "\n".join(f"ENSG{i:05d}\tGene{i}\tGene Expression" for i in range(n_genes)) + "\n"
        )

        return n_cells, n_genes

    def _write_mtx_bundle_gzipped(self, tmp_path: Path, n_cells: int = 20, n_genes: int = 10):
        """Write a gzipped 10x-style mtx bundle.

        10x format stores matrix as (genes x cells), so we transpose.
        """
        rng = np.random.default_rng(42)
        # Generate as (cells x genes), then transpose for 10x convention
        counts = sp.random(n_cells, n_genes, density=0.3, format="coo",
                           dtype=np.float64, random_state=rng)
        counts.data = np.round(counts.data * 10).astype(np.float64)
        counts_t = counts.T.tocoo()  # (genes x cells) for 10x format

        import io
        buf = io.BytesIO()
        sio.mmwrite(buf, counts_t)
        with gzip.open(tmp_path / "matrix.mtx.gz", "wb") as f:
            f.write(buf.getvalue())

        with gzip.open(tmp_path / "barcodes.tsv.gz", "wt") as f:
            f.write("\n".join(f"BARCODE{i}-1" for i in range(n_cells)) + "\n")

        with gzip.open(tmp_path / "features.tsv.gz", "wt") as f:
            f.write(
                "\n".join(f"ENSG{i:05d}\tGene{i}\tGene Expression" for i in range(n_genes)) + "\n"
            )

    def test_load_gzipped_mtx(self, tmp_path):
        self._write_mtx_bundle_gzipped(tmp_path, n_cells=20, n_genes=10)

        import scanpy as sc
        adata = sc.read_10x_mtx(tmp_path, var_names="gene_symbols")

        out = tmp_path / "out.h5ad"
        prepare_for_mapmycells(adata, out)

        _assert_valid_mmc_h5ad(out, expected_n_cells=20)
