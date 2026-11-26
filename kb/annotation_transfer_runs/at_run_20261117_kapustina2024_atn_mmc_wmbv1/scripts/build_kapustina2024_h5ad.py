"""Build a MapMyCells-ready h5ad + the "ATN" source-label JSON from Kapustina
et al. 2024 (GEO:GSE227627) anterior thalamic nuclei single-cell RNA-seq.

Inputs (GEO suppl, re-downloadable):
  GSE227627_merged_counts.txt.gz  genes x wells UMI counts (gene_id = Ensembl,
                                  NCBIM37; gene_name = symbol; 92 ERCC rows)
  GSE227627_metadata.txt.gz       per-well metadata: identifier, well, barcode,
                                  animalId, source (+165 blank trailing rows)

GEO deposits NO cluster / cell-type / nucleus label per cell. The only
per-cell annotation is `source`: "Mark_Anterior Thalamus_<date>_<n>" for
manually picked cells from 3 animals, or ERCC / qRNA / blank control wells.

Steps:
  1. keep wells whose source contains "Anterior Thalamus" (1,216 of 1,344);
     drop ERCC / qRNA / blank control wells
  2. QC: keep cells with >= MIN_GENES detected genes (912 of 1,216)
  3. genes: drop ERCC rows; keep GEO Ensembl IDs that occur in the WMBv1
     precomputed stats (col_names); write CSR integer-count h5ad
  4. write labels_atn.json: every retained cell -> "ATN" (the GEO tissue
     annotation "tissue: Anterior thalamic nuclei"; no further partition)

Usage (from the clone root):
  annotation_transfer/.venv/bin/python -I <this script> DATA_DIR STATS_H5 RUN_DIR
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import anndata as ad
import h5py
import numpy as np
import pandas as pd
import scipy.sparse as sp

MIN_GENES = 1000


def main(data_dir: Path, stats_h5: Path, run_dir: Path) -> None:
    meta = pd.read_csv(data_dir / "GSE227627_metadata.txt.gz", sep="\t")
    meta = meta.dropna(subset=["identifier"]).set_index("identifier")
    counts = pd.read_csv(data_dir / "GSE227627_merged_counts.txt.gz", sep="\t")
    counts = counts[~counts["gene_id"].str.startswith("ERCC")]
    gene_ids = counts["gene_id"].to_numpy()
    X = counts.drop(columns=["gene_id", "gene_name"])
    print(f"counts {X.shape} (genes x wells), metadata {meta.shape}")

    src = meta["source"].reindex(X.columns)
    cells = X.columns[src.str.contains("Anterior Thalamus", na=False)]
    X = X[cells]
    ngenes = (X > 0).sum(axis=0)
    cells = ngenes.index[ngenes >= MIN_GENES]
    X = X[cells]
    print(f"ATN wells: {len(ngenes)}; after >= {MIN_GENES} genes: {len(cells)}")

    with h5py.File(stats_h5) as h:
        ref = set(json.loads(h["col_names"][()].decode()))
    keep = np.array([g in ref for g in gene_ids])
    print(f"genes: {len(gene_ids)} non-ERCC, {keep.sum()} present in WMBv1 stats")

    M = sp.csr_matrix(X.to_numpy(dtype=np.float32).T[:, keep])
    assert np.allclose(M.data, np.round(M.data)), "expected integer UMI counts"
    obs = meta.loc[cells, ["animalId", "source"]].copy()
    obs["animalId"] = obs["animalId"].astype(int).astype(str)
    adata = ad.AnnData(
        X=M,
        obs=obs.set_axis(pd.Index(cells.astype(str), name="cell_id")),
        var=pd.DataFrame(index=pd.Index(gene_ids[keep], name="gene_id")),
    )
    h5ad_path = data_dir / "kapustina2024_atn_mmc.h5ad"
    adata.write_h5ad(h5ad_path)
    print(f"wrote {h5ad_path} {adata.shape}")

    labels = {c: "ATN" for c in adata.obs_names}
    (run_dir / "labels_atn.json").write_text(json.dumps(labels, indent=0, sort_keys=True) + "\n")
    print(f"wrote {run_dir / 'labels_atn.json'}: {len(labels)} cells")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
