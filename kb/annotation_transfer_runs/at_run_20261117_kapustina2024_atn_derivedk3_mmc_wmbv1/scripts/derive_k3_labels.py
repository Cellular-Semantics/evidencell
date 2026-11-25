"""Derive neutral 3-group labels for the Kapustina 2024 ATN query cells.

GEO:GSE227627 deposits no per-cell cluster labels, so the authors' three
excitatory clusters (AD / AV / AM) cannot be scored directly. This script
re-derives an unsupervised 3-group partition of the excitatory neurons,
WITHOUT reference to WMBv1 (no mapping output is read), and names the groups
neutrally (derived_k3_0/1/2). The groups are NOT asserted to be AD/AV/AM.

Steps (deterministic: fixed seeds):
  1. read the MapMyCells query h5ad (912 cells, Ensembl IDs) and attach
     symbols from GSE227627_merged_counts.txt.gz
  2. stage 1: normalise (1e4) + log1p, 2,000 HVG (seurat), PCA 30, KMeans
     k=6 on PCs 1-20 (seed 0). Keep the three large groups; drop the
     oligodendrocyte-contaminated group (Plp1/Mbp high) and the two tiny
     low-Snap25 groups (non-neuronal / low quality)
  3. stage 2 on the kept neurons: drop technical genes (mt-, Gm*, Rp[sl]*,
     *Rik, Malat1, Meg3, Snhg*, Kcnq1ot1, unnamed AC/AL/CT contigs, Hba/Hbb),
     normalise + log1p, 1,500 HVG (seurat, batch_key=animalId), regress out
     total UMI, scale (max 10), PCA 30, KMeans k=3 on PCs 1-15 (seed 0,
     n_init 30)
  4. write labels_derivedk3.json (cell id -> derived_k3_{0,1,2}) and
     derived_k3_markers.tsv (top Wilcoxon markers per group)

Usage (from the clone root):
  annotation_transfer/.venv/bin/python -I <this script> QUERY_H5AD COUNTS_TXT_GZ RUN_DIR
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import scanpy as sc
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

TECH = r"^(mt-|Gm\d|Rp[sl]\d|.*Rik$|Malat1|Meg3|Snhg|Kcnq1ot1|AC\d|AL\d|CT\d|Hba|Hbb)"


def main(query_h5ad: Path, counts_gz: Path, run_dir: Path) -> None:
    a = sc.read_h5ad(query_h5ad)
    sym = pd.read_csv(counts_gz, sep="\t", usecols=["gene_id", "gene_name"]).set_index("gene_id")["gene_name"]
    a.var["symbol"] = sym.reindex(a.var_names).astype(str).to_numpy()
    a.var_names = pd.Index(a.var["symbol"]).astype(str)
    a.var_names_make_unique()
    counts = a.X.copy()

    # stage 1: separate neurons from contaminated / low-quality cells
    sc.pp.normalize_total(a, target_sum=1e4)
    sc.pp.log1p(a)
    sc.pp.highly_variable_genes(a, n_top_genes=2000, flavor="seurat")
    sc.pp.pca(a, n_comps=30, mask_var="highly_variable")
    k6 = KMeans(6, n_init=20, random_state=0).fit_predict(a.obsm["X_pca"][:, :20])
    a.obs["k6"] = k6.astype(str)
    expr = pd.DataFrame(a[:, ["Snap25", "Plp1"]].X.toarray(), index=a.obs_names, columns=["Snap25", "Plp1"])
    g = expr.groupby(a.obs["k6"]).mean().assign(n=a.obs["k6"].value_counts())
    print("stage 1 groups:\n", g.round(2))
    neuronal = g.index[(g["Snap25"] > 2) & (g["Plp1"] < 1)]
    keep = a.obs["k6"].isin(neuronal).to_numpy()
    print(f"neurons kept: {keep.sum()} of {a.n_obs}")

    # stage 2: neuronal sub-structure
    n = a[keep].copy()
    n.X = counts[keep]
    n = n[:, ~n.var_names.str.match(TECH)].copy()
    sc.pp.normalize_total(n, target_sum=1e4)
    sc.pp.log1p(n)
    n.obs["umi"] = np.asarray(counts[keep].sum(axis=1)).ravel()
    sc.pp.highly_variable_genes(n, n_top_genes=1500, flavor="seurat", batch_key="animalId")
    raw_log = n.copy()
    sc.pp.regress_out(n, ["umi"])
    sc.pp.scale(n, max_value=10)
    sc.pp.pca(n, n_comps=30, mask_var="highly_variable")
    P = n.obsm["X_pca"][:, :15]
    lab = KMeans(3, n_init=30, random_state=0).fit_predict(P)
    print(f"k=3 silhouette {silhouette_score(P, lab):.3f}; sizes {pd.Series(lab).value_counts().to_dict()}")

    labels = {c: f"derived_k3_{l}" for c, l in zip(n.obs_names, lab)}
    (run_dir / "labels_derivedk3.json").write_text(json.dumps(labels, indent=0, sort_keys=True) + "\n")

    raw_log.obs["grp"] = pd.Categorical([labels[c] for c in raw_log.obs_names])
    sc.tl.rank_genes_groups(raw_log, "grp", method="wilcoxon")
    rows = []
    for grp in sorted(raw_log.obs["grp"].cat.categories):
        df = sc.get.rank_genes_groups_df(raw_log, grp).head(25)
        rows += [{"group": grp, "rank": i + 1, "gene": r.names, "log2fc": round(r.logfoldchanges, 2),
                  "pval_adj": f"{r.pvals_adj:.2e}"} for i, r in enumerate(df.itertuples())]
    pd.DataFrame(rows).to_csv(run_dir / "derived_k3_markers.tsv", sep="\t", index=False)
    print(f"wrote labels_derivedk3.json ({len(labels)} cells) and derived_k3_markers.tsv")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
