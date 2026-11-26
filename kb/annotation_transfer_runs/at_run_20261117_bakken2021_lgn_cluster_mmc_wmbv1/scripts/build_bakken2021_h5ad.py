"""Build a MapMyCells-ready h5ad + source-label JSONs from the mouse subset of
Bakken et al. 2021 (GEO:GSE182211) SMART-seq v4 dLGN / LP / LGv single cells.

Inputs (GEO suppl, re-downloadable):
  GSE182211_mouse_LGN_2021_exon-matrix.csv.gz    genes x cells, exon read counts
  GSE182211_mouse_LGN_2021_intron-matrix.csv.gz  genes x cells, intron read counts
  GSE182211_mouse_LGN_2021_metadata.csv.gz       per-cell metadata (cluster_label, dissection_roi, ...)

Steps:
  1. counts = exon + intron reads per gene (the paper's quantification: "sum of
     intronic and exonic reads per gene"); raw integer read counts, not UMIs
  2. drop the 73 cells with cluster_label == "Low Quality" -> 2,114 cells
  3. remap gene symbols -> Ensembl IDs with conf/gene_mapping_CCN20230722.tsv
     (WMBv1 precomputed stats are keyed by Ensembl ID); unmapped and
     duplicate-Ensembl symbols are dropped (first symbol kept)
  4. write CSR integer-count h5ad (obs index = sample_name, var index = Ensembl ID)
  5. write three label JSONs (cell id -> label), one per AT run record:
       labels_cluster.json   cluster_label (published clusters; all 2,114 cells)
       labels_coreshell.json LGd cluster only, split by dissection_roi:
                             "LGd core" / "LGd shell" (derived scheme)
       labels_dlgnin.json    all 2,114 cells; the three dLGN GABAergic clusters
                             (Chrna1, Chrna2, Chrna3) pooled as one label, every
                             other cell "other (non-dLGN-IN)" (derived scheme;
                             labels chosen not to collide with labels_cluster)

Usage (from the clone root):
  annotation_transfer/.venv/bin/python -I kb/annotation_transfer_runs/\
at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1/scripts/build_bakken2021_h5ad.py \
    annotation_transfer/data/bakken2021_lgn \
    conf/gene_mapping_CCN20230722.tsv \
    kb/annotation_transfer_runs/at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp

PREFIX = "GSE182211_mouse_LGN_2021_"
ROI_LABEL = {"dLGN - Core": "LGd core", "dLGN - Shell": "LGd shell"}
DLGN_IN = ("Chrna1", "Chrna2", "Chrna3")
DLGN_IN_LABEL = "dLGN GABA (Chrna1-3)"
OTHER_LABEL = "other (non-dLGN-IN)"


def main(data_dir: Path, gene_map_tsv: Path, out_dir: Path) -> None:
    meta = pd.read_csv(data_dir / f"{PREFIX}metadata.csv.gz").set_index("sample_name")
    exon = pd.read_csv(data_dir / f"{PREFIX}exon-matrix.csv.gz", index_col=0)
    intron = pd.read_csv(data_dir / f"{PREFIX}intron-matrix.csv.gz", index_col=0)
    print(f"exon {exon.shape}, intron {intron.shape}, metadata {meta.shape}")
    assert exon.index.equals(intron.index) and exon.columns.equals(intron.columns)
    counts = (exon + intron).T  # cells x genes
    del exon, intron

    keep = meta.index[meta["cluster_label"] != "Low Quality"]
    assert set(keep) <= set(counts.index), "metadata cells missing from matrix"
    counts = counts.loc[keep]
    meta = meta.loc[keep]
    print(f"after Low Quality filter: {len(keep)} cells")

    gmap = pd.read_csv(gene_map_tsv, sep="\t")
    sym2ens = dict(zip(gmap["symbol"], gmap["ensembl_id"]))
    ens = pd.Series([sym2ens.get(s) for s in counts.columns], index=counts.columns)
    mapped = ens.dropna()
    mapped = mapped[~mapped.duplicated(keep="first")]
    print(f"genes: {counts.shape[1]} symbols, {len(mapped)} mapped to unique Ensembl IDs")
    counts = counts[mapped.index]

    X = sp.csr_matrix(counts.to_numpy(dtype=np.float32))
    assert np.allclose(X.data, np.round(X.data)), "expected integer read counts"
    adata = ad.AnnData(
        X=X,
        obs=pd.DataFrame(index=counts.index.astype(str)),
        var=pd.DataFrame(index=pd.Index(mapped.values, name="gene_id")),
    )
    h5ad_path = data_dir / "bakken2021_lgn_mouse_mmc.h5ad"
    adata.write_h5ad(h5ad_path)
    print(f"wrote {h5ad_path} {adata.shape}")

    out_dir.mkdir(parents=True, exist_ok=True)
    cluster = {str(k): str(v) for k, v in meta["cluster_label"].items()}
    lgd = meta[meta["cluster_label"] == "LGd"]
    coreshell = {str(k): ROI_LABEL[v] for k, v in lgd["dissection_roi"].items() if v in ROI_LABEL}
    dlgnin = {k: (DLGN_IN_LABEL if v in DLGN_IN else OTHER_LABEL) for k, v in cluster.items()}
    for name, labels in (
        ("labels_cluster.json", cluster),
        ("labels_coreshell.json", coreshell),
        ("labels_dlgnin.json", dlgnin),
    ):
        (out_dir / name).write_text(json.dumps(labels, indent=0, sort_keys=True) + "\n")
        print(f"wrote {out_dir / name}: {pd.Series(labels).value_counts().to_dict()}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
