"""Convert AnnData objects to MapMyCells-ready h5ad format.

MapMyCells requires:
- X: raw integer counts in sparse CSR format
- obs: minimal — just cell_id
- var: minimal — just gene_id (gene symbols)
- No negative/scaled values, no raw layer, gzip compressed
"""

from __future__ import annotations

import json
from pathlib import Path

import anndata as ad
import numpy as np
import scipy.sparse as sp


class ConversionError(Exception):
    """Raised when h5ad cannot be converted to MapMyCells format."""


def prepare_for_mapmycells(
    adata: ad.AnnData,
    output_path: Path,
    *,
    cluster_col: str | None = None,
    cluster_value: str | None = None,
    label_col: str | None = None,
) -> dict[str, str]:
    """Sanitise an AnnData object for MapMyCells and write to disk.

    Parameters
    ----------
    adata
        Input AnnData (not modified in place).
    output_path
        Where to write the MapMyCells-ready h5ad.
    cluster_col
        If set, slice adata to rows where ``obs[cluster_col] == cluster_value``.
    cluster_value
        Value to filter on in cluster_col.
    label_col
        Column in obs to use as source cluster labels for F1 computation.
        If None, uses cluster_col. If neither is set, returns empty labels.

    Returns
    -------
    dict mapping cell_id → source cluster label (for later F1 join).
    """
    a = adata.copy()

    # 1. Optionally slice by cluster
    if cluster_col is not None and cluster_value is not None:
        if cluster_col not in a.obs.columns:
            raise ConversionError(
                f"Column '{cluster_col}' not found in obs. "
                f"Available: {list(a.obs.columns)}"
            )
        a = a[a.obs[cluster_col] == cluster_value].copy()
        if a.n_obs == 0:
            raise ConversionError(
                f"No cells match {cluster_col}=={cluster_value!r}"
            )

    # 2. Extract source labels before stripping obs
    lc = label_col or cluster_col
    source_labels: dict[str, str] = {}
    if lc and lc in a.obs.columns:
        source_labels = dict(zip(a.obs_names, a.obs[lc].astype(str)))

    # 3. Use raw counts if available
    if a.raw is not None:
        a = ad.AnnData(
            X=a.raw.X.copy(),
            obs=a.obs,
            var=a.raw.var,
            obsm=a.obsm if hasattr(a, "obsm") else None,
        )

    # 4. Ensure sparse CSR
    if not sp.issparse(a.X):
        a.X = sp.csr_matrix(a.X)
    elif not sp.isspmatrix_csr(a.X):
        a.X = a.X.tocsr()

    # 5. Validate integer counts
    sample = a.X[:min(100, a.n_obs), :].toarray()
    if not np.allclose(sample, np.round(sample)):
        raise ConversionError(
            "X does not contain integer counts. "
            "If normalised data is in X, ensure raw counts are in adata.raw."
        )
    if sample.min() < 0:
        raise ConversionError(
            "X contains negative values — likely scaled/z-scored data. "
            "Use raw counts instead."
        )

    # 6. Strip obs to cell_id, var to gene_id
    a.obs = a.obs[[]].copy()
    a.obs["cell_id"] = a.obs_names

    a.var = a.var[[]].copy()
    a.var["gene_id"] = a.var_names

    # 7. Drop raw, uns, obsp, varp to minimise file
    a.raw = None
    a.uns = {}
    if hasattr(a, "obsp"):
        a.obsp = {}
    if hasattr(a, "varp"):
        a.varp = {}

    # 8. Write
    output_path = Path(output_path)
    a.write_h5ad(output_path, compression="gzip")

    return source_labels


def save_source_labels(labels: dict[str, str], output_path: Path) -> None:
    """Write source labels to a JSON file for later F1 scoring."""
    with open(output_path, "w") as f:
        json.dump(labels, f)


def load_source_labels(path: Path) -> dict[str, str]:
    """Load source labels from a JSON file."""
    with open(path) as f:
        return json.load(f)
