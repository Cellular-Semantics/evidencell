"""Prepare Li et al. 2020 TRN snRNA-seq (GEO:GSE145273) for MapMyCells → WMBv1.

Inputs (fetched by fetch_inputs.sh into annotation_transfer/inputs/datasets/li2020_trn/):
  GSE145273_TPM.TRN.tsv.gz   genes x 1687 nuclei. Despite the "TPM" filename the
                             values are natural-log ln(TPM+1): the paper reports
                             "log(TPM+1)" and a median of 3909 detected genes at
                             >= 1.1, which this file reproduces exactly.
  scp344_type.tsv            SCP344 "Type" annotation (author-deposited; 671 TRN
                             Gad2+ Pvalb+ nuclei: Spp1+, DP, DN, Ecel1+), cell ids
                             prefixed "TRN_" relative to GEO column names.

Outputs (in OUT_DIR):
  li2020_trn_pvalb_log2tpm.h5ad  670 cells x 23420 genes, X = log2(TPM+1), CSR
                                 float32, obs cell_id, var gene_id. For MapMyCells
                                 with type_assignment.normalization = log2CPM.
  labels_trn_pvalb.json          cell_id -> "TRN Pvalb+" (plain run, parent node)
  labels_spp1_ecel1_type.json    cell_id -> SCP344 Type (relabel run)

One SCP344 cell ("TRN_X") has no matching GEO column and is dropped (670/671).

Usage:
  uv run --project annotation_transfer python -I \
    research/thalamus/annotation_transfer/li2020_trn/scripts/prepare_li2020_trn.py \
    annotation_transfer/inputs/datasets/li2020_trn \
    research/thalamus/annotation_transfer/li2020_trn/scp344_type.tsv \
    annotation_transfer/inputs/datasets/li2020_trn \
    research/thalamus/annotation_transfer/li2020_trn
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp


def main(geo_dir: Path, scp_tsv: Path, h5ad_dir: Path, labels_dir: Path) -> None:
    ln_tpm = pd.read_csv(geo_dir / "GSE145273_TPM.TRN.tsv.gz", sep="\t", index_col=0)
    types = pd.read_csv(scp_tsv, sep="\t")
    types["cell_id"] = types["NAME"].str.removeprefix("TRN_")

    keep = types[types["cell_id"].isin(ln_tpm.columns)]
    dropped = sorted(set(types["NAME"]) - set("TRN_" + keep["cell_id"]))
    print(f"SCP344 cells: {len(types)}; matched to GEO: {len(keep)}; dropped: {dropped}")

    sub = ln_tpm[keep["cell_id"].tolist()]
    tpm = np.expm1(sub.to_numpy(dtype=np.float64))
    log2_tpm = np.log2(tpm + 1.0).T.astype(np.float32)  # cells x genes

    a = ad.AnnData(
        X=sp.csr_matrix(log2_tpm),
        obs=pd.DataFrame({"cell_id": keep["cell_id"].to_numpy()}, index=keep["cell_id"].to_numpy()),
        var=pd.DataFrame({"gene_id": sub.index.to_numpy()}, index=sub.index.to_numpy()),
    )
    h5ad_dir.mkdir(parents=True, exist_ok=True)
    out = h5ad_dir / "li2020_trn_pvalb_log2tpm.h5ad"
    a.write_h5ad(out, compression="gzip")
    print(f"wrote {out} shape={a.shape} max={log2_tpm.max():.2f}")

    labels_dir.mkdir(parents=True, exist_ok=True)
    plain = {c: "TRN Pvalb+" for c in keep["cell_id"]}
    relabel = dict(zip(keep["cell_id"], keep["Type"]))
    (labels_dir / "labels_trn_pvalb.json").write_text(json.dumps(plain, indent=0))
    (labels_dir / "labels_spp1_ecel1_type.json").write_text(json.dumps(relabel, indent=0))
    print("relabel counts:", pd.Series(relabel).value_counts().to_dict())


if __name__ == "__main__":
    main(*(Path(p) for p in sys.argv[1:5]))
