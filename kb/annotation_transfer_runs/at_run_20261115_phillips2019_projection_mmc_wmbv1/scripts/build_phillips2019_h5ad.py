"""Build a MapMyCells-ready h5ad + source-label JSONs from Phillips et al. 2019
(GEO:GSE133912) single-cell thalamic projection-neuron data.

Inputs (GEO suppl, re-downloadable):
  GSE133912_thal_singlecell_counts.csv.gz    cells x gene-symbol UMI counts
  GSE133912_thal_singlecell_metadata.csv.gz  per-cell metadata (Projection, cluster, is_ODC, ...)

Steps:
  1. drop the 20 cells flagged is_ODC == 1 (oligodendrocyte-contaminated; the
     authors excluded them and they carry no cluster label) -> 1,952 cells
  2. remap gene symbols -> Ensembl IDs with conf/gene_mapping_CCN20230722.tsv
     (WMBv1 precomputed stats are keyed by Ensembl ID); unmapped and
     duplicate-Ensembl symbols are dropped (first symbol kept)
  3. write CSR integer-count h5ad (obs index = cell id, var index = Ensembl ID)
  4. write two label JSONs (cell id -> label):
       labels_projection.json  Projection column (Visual/Motor/Somatosensory/Auditory/Prefrontal)
       labels_syscluster.json  cluster column (per-system Seurat clusters, e.g. Vis_1)

Usage (from the clone root):
  annotation_transfer/.venv/bin/python -I kb/annotation_transfer_runs/\
at_run_20261115_phillips2019_projection_mmc_wmbv1/scripts/build_phillips2019_h5ad.py \
    annotation_transfer/inputs/datasets/phillips2019_thalamus \
    conf/gene_mapping_CCN20230722.tsv \
    kb/annotation_transfer_runs/at_run_20261115_phillips2019_projection_mmc_wmbv1
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp


def main(data_dir: Path, gene_map_tsv: Path, out_dir: Path) -> None:
    meta = pd.read_csv(data_dir / "GSE133912_thal_singlecell_metadata.csv.gz", index_col=0)
    counts = pd.read_csv(data_dir / "GSE133912_thal_singlecell_counts.csv.gz", index_col=0)
    print(f"counts {counts.shape}, metadata {meta.shape}")

    keep = meta.index[(meta["is_ODC"] == 0) & meta["cluster"].notna()]
    counts = counts.loc[keep]
    meta = meta.loc[keep]
    print(f"after is_ODC filter: {len(keep)} cells")

    gmap = pd.read_csv(gene_map_tsv, sep="\t")
    sym2ens = dict(zip(gmap["symbol"], gmap["ensembl_id"]))
    ens = pd.Series([sym2ens.get(s) for s in counts.columns], index=counts.columns)
    mapped = ens.dropna()
    mapped = mapped[~mapped.duplicated(keep="first")]
    print(f"genes: {counts.shape[1]} symbols, {len(mapped)} mapped to unique Ensembl IDs")
    counts = counts[mapped.index]

    X = sp.csr_matrix(counts.to_numpy(dtype=np.float32))
    assert np.allclose(X.data, np.round(X.data)), "expected integer UMI counts"
    adata = ad.AnnData(
        X=X,
        obs=pd.DataFrame(index=counts.index.astype(str)),
        var=pd.DataFrame(index=pd.Index(mapped.values, name="gene_id")),
    )
    h5ad_path = data_dir / "phillips2019_thalamus_mmc.h5ad"
    adata.write_h5ad(h5ad_path)
    print(f"wrote {h5ad_path} {adata.shape}")

    out_dir.mkdir(parents=True, exist_ok=True)
    for name, col in (("labels_projection.json", "Projection"), ("labels_syscluster.json", "cluster")):
        labels = {str(k): str(v) for k, v in meta[col].items()}
        (out_dir / name).write_text(json.dumps(labels, indent=0, sort_keys=True) + "\n")
        print(f"wrote {out_dir / name}: {pd.Series(labels).value_counts().to_dict()}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
