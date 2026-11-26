"""Build h5ad files from Gao et al. 2023 PVT snRNA-seq (GEO:GSE208707).

Inputs (GEO suppl, re-downloadable; see fetch_inputs.sh):
  GSE208707_allnuclei_matrix.mtx.gz    genes x nuclei integer UMI counts (33,502 x 20,503)
  GSE208707_allnuclei_genes.tsv.gz     gene symbol (both columns; no Ensembl IDs)
  GSE208707_allnuclei_barcodes.tsv.gz  nucleus ids ("<Sex>_<sample>_<barcode>")
  GSE208707_allnuclei_metadata.csv.gz  Seurat meta.data. The only cell-type
                                       annotation is `cluster.ids`, the paper's
                                       PHASE-1 clusters (all cell types; "Neurons (1)"
                                       ... "Neurons (8)"). The phase-2 neuron clusters
                                       and phase-3 PVT1-5 are NOT deposited.

Steps:
  1. keep nuclei whose cluster.ids starts with "Neurons" (10,410) and that have
     > MIN_GENES detected genes, the paper's phase-2 filter (Methods,
     "Clustering analysis") -> 10,307
  2. write gao2023_neurons_symbols.h5ad: all genes, symbols, obs = metadata.
     Input to derive_gao2023_labels.py
  3. map symbols to WMBv1 Ensembl IDs by exact match to the stats symbol
     (kb/taxonomy/CCN20230722/CCN20230722.db `genes.stats_symbol`), keeping
     symbols that match exactly one Ensembl ID; write gao2023_pvt_mmc.h5ad
     (CSR integer counts, var = Ensembl ID) for MapMyCells

Usage (from the clone root):
  annotation_transfer/.venv/bin/python -I <this script> DATA_DIR TAXONOMY_DB
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.io
import scipy.sparse as sp

MIN_GENES = 1000


def main(data_dir: Path, db: Path) -> None:
    X = scipy.io.mmread(data_dir / "GSE208707_allnuclei_matrix.mtx.gz").tocsc()
    genes = pd.read_csv(data_dir / "GSE208707_allnuclei_genes.tsv.gz", sep="\t", header=None)[0]
    bcs = pd.read_csv(data_dir / "GSE208707_allnuclei_barcodes.tsv.gz", sep="\t", header=None)[0]
    meta = pd.read_csv(data_dir / "GSE208707_allnuclei_metadata.csv.gz", index_col=0)
    assert X.shape == (len(genes), len(bcs)), (X.shape, len(genes), len(bcs))
    assert list(meta.index) == list(bcs), "metadata rows not in barcode order"
    print(f"matrix {X.shape} (genes x nuclei)")

    X = sp.csr_matrix(X.T)  # nuclei x genes
    assert np.allclose(X.data, np.round(X.data)), "expected integer UMI counts"
    ngenes = np.asarray((X > 0).sum(axis=1)).ravel()
    is_neuron = meta["cluster.ids"].str.startswith("Neurons").to_numpy()
    keep = is_neuron & (ngenes > MIN_GENES)
    print(f"neuronal (phase-1) nuclei: {is_neuron.sum()}; with > {MIN_GENES} genes: {keep.sum()}")

    obs = meta.loc[keep, ["orig.ident", "sample", "Sex", "nCount_RNA", "nFeature_RNA",
                          "percent.mt", "cluster.ids"]].copy()
    obs.columns = ["orig_ident", "sample", "sex", "n_counts", "n_genes", "percent_mt", "phase1_cluster"]
    obs["sample"] = obs["sample"].astype(str)
    obs.index.name = "cell_id"
    Xk = X[keep].astype(np.float32)

    sym = ad.AnnData(X=Xk, obs=obs, var=pd.DataFrame(index=pd.Index(genes.astype(str), name="symbol")))
    sym.var_names_make_unique()
    p = data_dir / "gao2023_neurons_symbols.h5ad"
    sym.write_h5ad(p)
    print(f"wrote {p} {sym.shape}")

    con = sqlite3.connect(db)
    gm = pd.read_sql("SELECT ensembl_id, stats_symbol FROM genes", con)
    n_per_sym = gm.groupby("stats_symbol")["ensembl_id"].transform("size")
    gm = gm[n_per_sym == 1].set_index("stats_symbol")["ensembl_id"]
    ens = genes.map(gm)
    ok = ens.notna().to_numpy() & ~genes.duplicated(keep=False).to_numpy()
    print(f"genes: {len(genes)} symbols, {ok.sum()} map to exactly one WMBv1 Ensembl ID")

    mmc = ad.AnnData(
        X=Xk[:, ok],
        obs=obs[["sample", "sex"]].copy(),
        var=pd.DataFrame(index=pd.Index(ens[ok].to_numpy(), name="gene_id")),
    )
    assert mmc.var_names.is_unique
    p = data_dir / "gao2023_pvt_mmc.h5ad"
    mmc.write_h5ad(p)
    print(f"wrote {p} {mmc.shape}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
