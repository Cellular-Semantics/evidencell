"""Tests for preflight resource estimation."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import anndata as ad
import numpy as np
import scipy.sparse as sp

from annotation_transfer.preflight import (
    PreflightReport,
    check_h5ad,
    check_mtx_bundle,
    check_resources,
    _estimate_sparse_memory_gb,
)


def _make_tiny_h5ad(path: Path, n_cells: int = 50, n_genes: int = 100) -> Path:
    """Create a minimal h5ad for preflight testing."""
    X = sp.random(n_cells, n_genes, density=0.1, format="csr", dtype=np.float32)
    adata = ad.AnnData(X=X)
    adata.obs_names = [f"cell_{i}" for i in range(n_cells)]
    adata.var_names = [f"gene_{i}" for i in range(n_genes)]
    adata.write_h5ad(path, compression="gzip")
    return path


def test_estimate_sparse_memory_positive():
    gb = _estimate_sparse_memory_gb(100_000, 30_000)
    assert gb > 0


def test_check_h5ad_reads_shape(tmp_path):
    h5ad_path = tmp_path / "test.h5ad"
    _make_tiny_h5ad(h5ad_path, n_cells=50, n_genes=100)

    report = check_h5ad(h5ad_path)
    assert report.n_cells == 50
    assert report.n_genes == 100
    assert report.est_memory_gb > 0
    assert report.available_memory_gb > 0
    # Tiny dataset should always fit
    assert report.fits is True


def test_check_h5ad_with_raw(tmp_path):
    """h5ad where counts are in raw.X."""
    h5ad_path = tmp_path / "test_raw.h5ad"
    X = sp.random(30, 80, density=0.1, format="csr", dtype=np.float32)
    adata = ad.AnnData(X=X.copy())
    adata.raw = adata.copy()
    # Overwrite X with normalised (different shape shouldn't happen, but raw is the fallback)
    adata.write_h5ad(h5ad_path)

    report = check_h5ad(h5ad_path)
    assert report.n_cells == 30
    assert report.n_genes == 80


def test_check_mtx_bundle(tmp_path):
    """Estimate from a 10x mtx-style directory."""
    # Create minimal barcodes and features files
    barcodes = tmp_path / "barcodes.tsv"
    barcodes.write_text("\n".join(f"BARCODE{i}" for i in range(200)) + "\n")

    features = tmp_path / "features.tsv"
    features.write_text("\n".join(f"GENE{i}\tGENE{i}\tGene Expression" for i in range(500)) + "\n")

    # Need a matrix.mtx marker file for auto-detection
    (tmp_path / "matrix.mtx").write_text("%%MatrixMarket\n")

    report = check_mtx_bundle(tmp_path)
    assert report.n_cells == 200
    assert report.n_genes == 500


def test_check_resources_auto_detects_h5ad(tmp_path):
    h5ad_path = tmp_path / "auto.h5ad"
    _make_tiny_h5ad(h5ad_path, n_cells=20, n_genes=40)

    report = check_resources(h5ad_path)
    assert report.n_cells == 20
    assert report.n_genes == 40


def test_check_resources_auto_detects_mtx_dir(tmp_path):
    (tmp_path / "barcodes.tsv").write_text("A\nB\nC\n")
    (tmp_path / "features.tsv").write_text("G1\nG2\n")
    (tmp_path / "matrix.mtx").write_text("%%MatrixMarket\n")

    report = check_resources(tmp_path)
    assert report.n_cells == 3
    assert report.n_genes == 2


def test_check_resources_rds_fallback(tmp_path):
    rds = tmp_path / "data.rds"
    rds.write_bytes(b"\x00" * 1024 * 1024)  # 1 MB fake file

    report = check_resources(rds)
    # File size heuristic with 10x expansion
    assert report.n_cells == 0  # unknown for RDS
    assert report.est_memory_gb > 0


def test_report_fits_flag():
    report = PreflightReport(
        file_path=Path("test.h5ad"),
        n_cells=100,
        n_genes=100,
        est_memory_gb=0.001,
        available_memory_gb=16.0,
        fits=True,
    )
    assert "OK" in report.summary()

    report_bad = PreflightReport(
        file_path=Path("big.h5ad"),
        n_cells=1_000_000,
        n_genes=50_000,
        est_memory_gb=20.0,
        available_memory_gb=8.0,
        fits=False,
    )
    assert "WARNING" in report_bad.summary()
