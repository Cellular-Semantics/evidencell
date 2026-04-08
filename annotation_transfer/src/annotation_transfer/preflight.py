"""Resource estimation and human gate for large datasets.

Reads dataset dimensions from file metadata without loading the full matrix,
estimates memory requirements, and checks against available RAM.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import h5py
import psutil


@dataclass
class PreflightReport:
    """Result of a resource estimation check."""

    file_path: Path
    n_cells: int
    n_genes: int
    est_memory_gb: float
    available_memory_gb: float
    fits: bool

    def summary(self) -> str:
        status = "OK" if self.fits else "WARNING — may exceed available RAM"
        return (
            f"Preflight: {self.file_path.name}\n"
            f"  Cells:     {self.n_cells:,}\n"
            f"  Genes:     {self.n_genes:,}\n"
            f"  Est. mem:  {self.est_memory_gb:.1f} GB\n"
            f"  Available: {self.available_memory_gb:.1f} GB\n"
            f"  Status:    {status}"
        )


# Sparse CSR: ~12 bytes per nonzero (8 data + 4 index).
# Typical scRNA-seq sparsity: ~90-95% zeros → ~5-10% nonzero.
# We use 10% fill as a conservative estimate for memory.
_SPARSE_FILL_FRACTION = 0.10
_BYTES_PER_NNZ = 12
_SAFETY_FACTOR = 1.5  # headroom for pandas/anndata overhead during load


def _estimate_sparse_memory_gb(n_cells: int, n_genes: int) -> float:
    """Estimate memory for a sparse CSR matrix."""
    nnz_est = n_cells * n_genes * _SPARSE_FILL_FRACTION
    raw_bytes = nnz_est * _BYTES_PER_NNZ
    return (raw_bytes * _SAFETY_FACTOR) / (1024**3)


def _get_available_memory_gb() -> float:
    """Return available system memory in GB."""
    return psutil.virtual_memory().available / (1024**3)


def check_h5ad(file_path: Path) -> PreflightReport:
    """Read h5ad shape from HDF5 metadata without loading X."""
    with h5py.File(file_path, "r") as f:
        if "X" in f:
            x = f["X"]
            if "shape" in x.attrs:
                shape = tuple(x.attrs["shape"])
            elif isinstance(x, h5py.Dataset):
                shape = x.shape
            else:
                # Sparse group — shape is stored in attrs
                shape = tuple(x.attrs.get("shape", (0, 0)))
        elif "raw" in f and "X" in f["raw"]:
            x = f["raw"]["X"]
            if "shape" in x.attrs:
                shape = tuple(x.attrs["shape"])
            elif isinstance(x, h5py.Dataset):
                shape = x.shape
            else:
                shape = tuple(x.attrs.get("shape", (0, 0)))
        else:
            shape = (0, 0)

    n_cells, n_genes = int(shape[0]), int(shape[1])
    est_gb = _estimate_sparse_memory_gb(n_cells, n_genes)
    avail_gb = _get_available_memory_gb()

    return PreflightReport(
        file_path=file_path,
        n_cells=n_cells,
        n_genes=n_genes,
        est_memory_gb=est_gb,
        available_memory_gb=avail_gb,
        fits=est_gb < avail_gb,
    )


def check_mtx_bundle(mtx_dir: Path) -> PreflightReport:
    """Estimate dimensions from a 10x mtx bundle directory.

    Expects: matrix.mtx or matrix.mtx.gz, barcodes.tsv(.gz), features.tsv(.gz).
    """
    n_cells = 0
    n_genes = 0

    for pattern in ["barcodes.tsv", "barcodes.tsv.gz"]:
        p = mtx_dir / pattern
        if p.exists():
            if pattern.endswith(".gz"):
                import gzip

                with gzip.open(p, "rt") as fh:
                    n_cells = sum(1 for _ in fh)
            else:
                with open(p) as fh:
                    n_cells = sum(1 for _ in fh)
            break

    for pattern in ["features.tsv", "features.tsv.gz", "genes.tsv", "genes.tsv.gz"]:
        p = mtx_dir / pattern
        if p.exists():
            if pattern.endswith(".gz"):
                import gzip

                with gzip.open(p, "rt") as fh:
                    n_genes = sum(1 for _ in fh)
            else:
                with open(p) as fh:
                    n_genes = sum(1 for _ in fh)
            break

    est_gb = _estimate_sparse_memory_gb(n_cells, n_genes)
    avail_gb = _get_available_memory_gb()

    return PreflightReport(
        file_path=mtx_dir,
        n_cells=n_cells,
        n_genes=n_genes,
        est_memory_gb=est_gb,
        available_memory_gb=avail_gb,
        fits=est_gb < avail_gb,
    )


def check_file_size_heuristic(file_path: Path, expansion_factor: float = 10.0) -> PreflightReport:
    """Fallback for unknown formats: estimate from file size.

    Used for RDS, loom, or other formats where we can't cheaply read dimensions.
    """
    file_size_gb = file_path.stat().st_size / (1024**3)
    est_gb = file_size_gb * expansion_factor
    avail_gb = _get_available_memory_gb()

    return PreflightReport(
        file_path=file_path,
        n_cells=0,  # unknown
        n_genes=0,  # unknown
        est_memory_gb=est_gb,
        available_memory_gb=avail_gb,
        fits=est_gb < avail_gb,
    )


def check_resources(file_path: Path) -> PreflightReport:
    """Auto-detect format and run appropriate preflight check."""
    path = Path(file_path)

    if path.suffix in (".h5ad", ".h5"):
        return check_h5ad(path)

    # mtx bundle: a directory containing matrix.mtx[.gz]
    if path.is_dir():
        mtx_candidates = list(path.glob("matrix.mtx*"))
        if mtx_candidates:
            return check_mtx_bundle(path)

    # RDS, loom, or anything else: file size heuristic
    if path.suffix.lower() in (".rds", ".robj"):
        return check_file_size_heuristic(path, expansion_factor=10.0)
    if path.suffix.lower() == ".loom":
        return check_file_size_heuristic(path, expansion_factor=3.0)

    return check_file_size_heuristic(path, expansion_factor=5.0)


def preflight_gate(file_path: Path, auto_approve: bool = False) -> PreflightReport:
    """Run preflight check and halt for confirmation if dataset is too large.

    In CLI/interactive mode, prints the report and asks for confirmation.
    When auto_approve=True, prints the report but proceeds regardless.
    """
    report = check_resources(file_path)
    print(report.summary())

    if not report.fits and not auto_approve:
        print(
            "\nDataset may not fit in available memory. "
            "Loading could cause swapping or an OOM kill."
        )
        try:
            answer = input("Proceed anyway? [y/N] ").strip().lower()
        except EOFError:
            answer = "n"
        if answer not in ("y", "yes"):
            print("Aborted by user.")
            sys.exit(1)

    return report
