"""Prepare Li et al. 2020 TRN snRNA-seq (GEO:GSE145273) for MapMyCells → WMBv1.

Inputs (fetched by fetch_inputs.sh into annotation_transfer/inputs/datasets/li2020_trn/):
  GSE145273_TPM.TRN.tsv.gz   genes x 1687 nuclei. Despite the "TPM" filename the
                             values are natural-log ln(TPM+1): the paper reports
                             "log(TPM+1)" and a median of 3909 detected genes at
                             >= 1.1, which this file reproduces exactly.
  conf/gene_mapping_CCN20230722.tsv  WMBv1 ensembl_id <-> symbol (GEO is keyed by
                             symbol; local MapMyCells needs WMBv1's Ensembl IDs).
  scp344_type.tsv            SCP344 "Type" annotation (author-deposited; TRN Gad2+
                             Pvalb+ nuclei: Spp1+, DP, DN, Ecel1+), cell ids
                             prefixed "TRN_" relative to GEO column names, saved
                             exactly as the SCP344 API returns it.

Outputs (in OUT_DIR):
  li2020_trn_pvalb_ln1ptpm.h5ad  670 cells x WMBv1-mapped genes, X = ln(TPM+1)
                                 exactly as deposited (CSR float32, obs cell_id,
                                 var indexed by Ensembl ID, column symbol).
                                 Symbols absent from the WMBv1 gene mapping are
                                 dropped; a duplicate Ensembl ID keeps its first
                                 symbol (same rule as the Harris 2018 run).
                                 Not mapped directly: `just at-normalize ...
                                 --input-scale ln1p --gene-lengths ...` turns it
                                 into log2(CPM+1) (see ../README.md).
  labels_trn_pvalb.json          cell_id -> "TRN Pvalb+" (plain run, parent node)
  labels_spp1_ecel1_type.json    cell_id -> SCP344 Type (relabel run)

Usage passes the repo root as a fifth argument (for conf/gene_mapping_*.tsv).

SCP344 name/annotation offset. In the SCP344 cluster data the NAME column is
shifted one row against the Type annotation (and the biSNE coordinates): the
first NAME is "TRN_X" (an R row-names header artefact) and each real cell's Type
sits on the row above it. Paired as returned, Type agrees with the paper's own
definition (binarised Spp1/Ecel1 on/off, ln(TPM+1) > 1.1; Li 2020 Ext. Data
Fig. 3c-d) for only 34% of cells, i.e. chance. Shifted by one row, it agrees
for 99.9%. This script applies the shift and asserts the agreement, so a
re-fetch with a corrected SCP344 upload fails loudly instead of silently
mislabelling. After the shift, "TRN_X" has no Type and no GEO column and is
dropped, and the last row's Type has no cell: 670 labelled cells.

Usage:
  uv run --project annotation_transfer python -I \
    research/thalamus/annotation_transfer/li2020_trn/scripts/prepare_li2020_trn.py \
    annotation_transfer/inputs/datasets/li2020_trn \
    research/thalamus/annotation_transfer/li2020_trn/scp344_type.tsv \
    annotation_transfer/inputs/datasets/li2020_trn \
    research/thalamus/annotation_transfer/li2020_trn \
    .
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp


def main(geo_dir: Path, scp_tsv: Path, h5ad_dir: Path, labels_dir: Path, root: Path) -> None:
    ln_tpm = pd.read_csv(geo_dir / "GSE145273_TPM.TRN.tsv.gz", sep="\t", index_col=0)
    types = pd.read_csv(scp_tsv, sep="\t")
    types["cell_id"] = types["NAME"].str.removeprefix("TRN_")
    types["Type"] = types["Type"].shift(1)  # see "SCP344 name/annotation offset"
    types = types.dropna(subset=["Type"])

    keep = types[types["cell_id"].isin(ln_tpm.columns)]
    dropped = sorted(set(types["NAME"]) - set("TRN_" + keep["cell_id"]))
    print(f"SCP344 cells: {len(types)}; matched to GEO: {len(keep)}; dropped: {dropped}")

    sub = ln_tpm[keep["cell_id"].tolist()]

    spp1, ecel1 = sub.loc["Spp1"].to_numpy() > 1.1, sub.loc["Ecel1"].to_numpy() > 1.1
    call = np.select([spp1 & ~ecel1, ecel1 & ~spp1, spp1 & ecel1], ["Spp1+", "Ecel1+", "DP"], "DN")
    agree = float((call == keep["Type"].to_numpy()).mean())
    print(f"Type vs binarised Spp1/Ecel1 (ln(TPM+1) > 1.1) agreement: {agree:.3f}")
    assert agree > 0.95, "SCP344 Type no longer lines up with GEO expression; recheck the offset"

    gm = pd.read_csv(root / "conf/gene_mapping_CCN20230722.tsv", sep="\t")
    sym2ens = dict(zip(gm["symbol"], gm["ensembl_id"]))
    ens = sub.index.map(lambda g: sym2ens.get(g, ""))
    mapped = (ens != "") & ~pd.Series(ens).duplicated().to_numpy()
    print(f"genes: {len(sub)}; unmapped to WMBv1 Ensembl: {(ens == '').sum()}; kept: {mapped.sum()}")
    symbols = sub.index[mapped]
    sub = sub[mapped]
    sub.index = ens[mapped]
    ln1p_tpm = sub.to_numpy(dtype=np.float32).T  # cells x genes

    a = ad.AnnData(
        X=sp.csr_matrix(ln1p_tpm),
        obs=pd.DataFrame({"cell_id": keep["cell_id"].to_numpy()}, index=keep["cell_id"].to_numpy()),
        var=pd.DataFrame({"symbol": symbols.to_numpy()}, index=pd.Index(sub.index.to_numpy(), name="ensembl_id")),
    )
    h5ad_dir.mkdir(parents=True, exist_ok=True)
    out = h5ad_dir / "li2020_trn_pvalb_ln1ptpm.h5ad"
    a.write_h5ad(out, compression="gzip")
    print(f"wrote {out} shape={a.shape} max={ln1p_tpm.max():.2f}")

    labels_dir.mkdir(parents=True, exist_ok=True)
    plain = {c: "TRN Pvalb+" for c in keep["cell_id"]}
    relabel = dict(zip(keep["cell_id"], keep["Type"]))
    (labels_dir / "labels_trn_pvalb.json").write_text(json.dumps(plain, indent=0))
    (labels_dir / "labels_spp1_ecel1_type.json").write_text(json.dumps(relabel, indent=0))
    print("relabel counts:", pd.Series(relabel).value_counts().to_dict())


if __name__ == "__main__":
    main(*(Path(p) for p in sys.argv[1:6]))
