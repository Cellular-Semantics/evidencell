"""Convert AnnData objects to MapMyCells-ready h5ad format.

MapMyCells accepts two query normalisations, declared per run and passed
through to ``cell_type_mapper``'s ``--type_assignment.normalization``:

``raw`` (default)
    X holds raw integer counts; ``cell_type_mapper`` rescales each cell to
    CPM and applies ``log2(x+1)`` itself.
``log2CPM``
    X already holds ``log2(CPM+1)``; ``cell_type_mapper`` uses it as-is.
    For datasets published only as normalised expression (Smart-seq2 /
    RSEM TPM tables, for example), this is the only route — there are no
    counts to recover.

Either way the file must satisfy:
- obs: minimal — just cell_id
- var: minimal — just gene_id (gene symbols)
- No negative values, no raw layer, gzip compressed

See ``docs/at_data_flow.md`` § "Query normalisation" for why a log2CPM run
is recorded in the manifest and flagged downstream: TPM is gene-length
normalised while the reference taxonomy is not, which biases the
marker-wise correlation the mapper optimises.
"""

from __future__ import annotations

import json
import warnings
from pathlib import Path

import anndata as ad
import numpy as np
import scipy.sparse as sp

#: Query normalisations accepted by ``cell_type_mapper``
#: (``--type_assignment.normalization``).
NORMALIZATIONS = ("raw", "log2CPM")

#: log2(CPM+1) of a single gene carrying an entire 1e6-scaled library is
#: ~20. Anything above this means linear values were passed by mistake.
LOG2CPM_MAX_PLAUSIBLE = 21.0

#: Tolerated relative deviation of a cell's de-logged library size from
#: 1e6 before ``prepare_for_mapmycells`` warns.
LOG2CPM_LIBSIZE_TOLERANCE = 0.25

class ConversionError(Exception):
    """Raised when h5ad cannot be converted to MapMyCells format."""


def prepare_for_mapmycells(
    adata: ad.AnnData,
    output_path: Path,
    *,
    cluster_col: str | None = None,
    cluster_value: str | None = None,
    label_col: str | None = None,
    normalization: str = "raw",
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
    normalization
        Query normalisation declared for the downstream MapMyCells run,
        one of ``NORMALIZATIONS``. ``raw`` (default) requires integer
        counts in X and prefers ``adata.raw`` when present. ``log2CPM``
        takes X as-is as log2(CPM+1), skips the integer check, and never
        substitutes ``adata.raw`` (which would swap the normalised matrix
        for counts). The same value MUST be passed to the mapper — see
        ``mapper_local.run_mapmycells``.

    Returns
    -------
    dict mapping cell_id → source cluster label (for later F1 join).
    """
    if normalization not in NORMALIZATIONS:
        raise ConversionError(
            f"Unknown normalization {normalization!r}; "
            f"must be one of {', '.join(NORMALIZATIONS)}."
        )

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

    # 3. Use raw counts if available.
    #    Only under `raw`: in log2CPM mode X *is* the matrix to map, and
    #    adata.raw typically holds the counts/other scaling we are
    #    deliberately not using.
    if normalization == "raw" and a.raw is not None:
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

    # 5. Validate X against the declared normalisation
    sample = a.X[:min(100, a.n_obs), :].toarray()
    if normalization == "raw":
        _validate_raw(sample)
    else:
        _validate_log2cpm(sample, n_genes=a.n_vars)

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


# ─── X validation ─────────────────────────────────────────────────────


def _validate_raw(sample: np.ndarray) -> None:
    """Validate a sample of X under ``normalization="raw"``."""
    if not np.allclose(sample, np.round(sample)):
        raise ConversionError(
            "X does not contain integer counts. "
            "If normalised data is in X, ensure raw counts are in adata.raw. "
            "If the dataset was published without counts (Smart-seq2/RSEM "
            "TPM tables, for example), convert X to log2(CPM+1) with "
            "`annotation-transfer normalize` and re-run with "
            "--normalization log2CPM."
        )
    if sample.min() < 0:
        raise ConversionError(
            "X contains negative values — likely scaled/z-scored data. "
            "Use raw counts instead."
        )


def _validate_log2cpm(sample: np.ndarray, *, n_genes: int) -> None:
    """Validate a sample of X under ``normalization="log2CPM"``.

    The integer check does not apply, so these checks are the only guard
    against a mis-declared matrix. That matters more here than usual: a
    wrongly scaled or wrongly based matrix does not raise inside
    ``cell_type_mapper``, it silently correlates near zero against every
    reference type and collapses every cell onto one label.
    """
    if sample.min() < 0:
        raise ConversionError(
            "X contains negative values — log2CPM input must be "
            "log2(CPM+1), which is non-negative. Likely scaled/z-scored "
            "or mean-centred data."
        )

    observed_max = float(sample.max())
    if observed_max > LOG2CPM_MAX_PLAUSIBLE:
        raise ConversionError(
            f"X has max {observed_max:.1f}, above the ~{LOG2CPM_MAX_PLAUSIBLE:.0f} "
            "ceiling for log2(CPM+1) (a single gene holding the whole "
            "library). X looks like linear CPM/TPM rather than log2(CPM+1) — "
            "convert it with `annotation-transfer normalize`."
        )

    # De-log and check library size. log2(CPM+1) de-logs to values summing
    # to ~1e6 per cell. A sum far ABOVE 1e6 cannot be explained by gene
    # subsetting, so it is an error; a sum below it can, so it warns.
    libsizes = np.expm1(sample * np.log(2)).sum(axis=1)
    median_libsize = float(np.median(libsizes))
    ratio = median_libsize / 1e6
    if ratio > 1 + LOG2CPM_LIBSIZE_TOLERANCE:
        raise ConversionError(
            f"De-logged library size is {median_libsize:.3g} per cell "
            f"(expected ~1e6 for log2(CPM+1)). X is not on a CPM/TPM "
            "scale — rescale each cell to 1e6 before taking log2(x+1), "
            "e.g. with `annotation-transfer normalize`."
        )
    if ratio < 1 - LOG2CPM_LIBSIZE_TOLERANCE:
        warnings.warn(
            f"De-logged library size is {median_libsize:.3g} per cell, "
            f"below the ~1e6 expected for log2(CPM+1) across {n_genes} "
            "genes. That is expected if X holds a gene subset; if it "
            "holds all genes, check the log base — ln(x+1) or log10(x+1) "
            "mis-declared as log2(x+1) produces exactly this signature "
            "and maps badly without erroring.",
            stacklevel=3,
        )


# ─── normalisation helper ─────────────────────────────────────────────

#: Input scales accepted by :func:`to_log2cpm`.
INPUT_SCALES = ("counts", "cpm", "tpm", "ln1p", "log2_1p", "log10_1p")


def to_log2cpm(
    adata: ad.AnnData,
    *,
    input_scale: str,
    gene_lengths: dict[str, float] | None = None,
) -> ad.AnnData:
    """Return a copy of ``adata`` with X as log2(CPM+1).

    Exists so each run doesn't re-derive the transform — and, in
    particular, so the ln/log2 conversion isn't done by eye. The
    ``ln1p`` case is the one that bites: ``ln(TPM+1) / ln(2)`` is
    exactly ``log2(TPM+1)``, but only because the ``+1`` cancels under
    the base change; the same shortcut is wrong for any other offset.

    Parameters
    ----------
    adata
        Input AnnData (not modified in place).
    input_scale
        What X currently holds, one of ``INPUT_SCALES``. ``counts``,
        ``cpm`` and ``tpm`` are linear; the ``*_1p`` scales are
        offset-logs of a linear matrix in the corresponding base.
    gene_lengths
        Optional mapping of ``var_name`` → effective gene length (bp).
        When given, X is multiplied by length/1000 before rescaling,
        which approximately undoes the gene-length normalisation in a
        TPM/FPKM table. Use it for full-length (Smart-seq) data mapped
        against a UMI-based reference taxonomy, whose CPM values are
        not length normalised. Genes absent from the mapping are
        dropped, with a warning.
    """
    if input_scale not in INPUT_SCALES:
        raise ConversionError(
            f"Unknown input_scale {input_scale!r}; "
            f"must be one of {', '.join(INPUT_SCALES)}."
        )

    a = adata.copy()
    x = a.X.toarray() if sp.issparse(a.X) else np.asarray(a.X, dtype=float)
    x = x.astype(float, copy=False)

    if x.min() < 0:
        raise ConversionError(
            "X contains negative values — cannot be counts, CPM/TPM, or "
            "an offset-log of either."
        )

    # 1. De-log to linear.
    if input_scale == "ln1p":
        x = np.expm1(x)
    elif input_scale == "log2_1p":
        x = np.expm1(x * np.log(2))
    elif input_scale == "log10_1p":
        x = np.expm1(x * np.log(10))

    # 2. Optionally undo gene-length normalisation.
    if gene_lengths is not None:
        lengths = np.array(
            [gene_lengths.get(str(g), np.nan) for g in a.var_names],
            dtype=float,
        )
        keep = ~np.isnan(lengths)
        n_missing = int((~keep).sum())
        if n_missing:
            warnings.warn(
                f"{n_missing} of {a.n_vars} genes have no entry in "
                "gene_lengths and are dropped before length correction.",
                stacklevel=2,
            )
        if not keep.any():
            raise ConversionError(
                "No gene in var_names matched the gene_lengths mapping; "
                "check that the keys use the same gene identifiers."
            )
        x = x[:, keep] * (lengths[keep] / 1000.0)
        a = a[:, keep].copy()

    # 3. Rescale each cell to 1e6 (no-op, to rounding, for TPM/CPM input).
    totals = x.sum(axis=1, keepdims=True)
    if (totals == 0).any():
        raise ConversionError(
            "At least one cell has an all-zero expression vector; "
            "filter empty cells before normalising."
        )
    x = x / totals * 1e6

    # 4. log2(x+1), in place: `x` is already a fresh array from step 3,
    # and a dense query matrix is big enough that a second full copy is
    # the difference between running and an OOM kill.
    np.add(x, 1.0, out=x)
    np.log2(x, out=x)
    a.X = sp.csr_matrix(x)
    a.raw = None
    return a


def load_gene_lengths(path: Path) -> dict[str, float]:
    """Load a two-column (gene_id, length_bp) TSV/CSV for ``to_log2cpm``.

    A header row is tolerated and skipped: any first line whose second
    field is not a number.
    """
    sep = "," if Path(path).suffix.lower() == ".csv" else "\t"
    lengths: dict[str, float] = {}
    with open(path) as f:
        for line in f:
            parts = line.rstrip("\n").split(sep)
            if len(parts) < 2:
                continue
            try:
                lengths[parts[0].strip()] = float(parts[1])
            except ValueError:
                continue  # header or malformed row
    if not lengths:
        raise ConversionError(f"No (gene, length) rows parsed from {path}")
    return lengths


def save_source_labels(labels: dict[str, str], output_path: Path) -> None:
    """Write source labels to a JSON file for later F1 scoring."""
    with open(output_path, "w") as f:
        json.dump(labels, f)


def load_source_labels(path: Path) -> dict[str, str]:
    """Load source labels from a JSON file."""
    with open(path) as f:
        return json.load(f)
