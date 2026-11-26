"""Re-derive Gao et al. 2023 PVT labels for GEO:GSE208707, which deposits
only the paper's phase-1 clusters (all cell types; "Neurons (1)".."(8)").
The phase-2 neuron clusters and the phase-3 PVT1-PVT5 are not deposited.

DERIVED labels. Every name comes from the paper's own published markers
(eLife 2023;12:e81818, PMID:36867023). No WMBv1 output is read here.

Step A, PVT vs neighbouring nuclei (paper phase 2):
  all neuronal nuclei with > 1000 genes (build_gao2023_h5ad.py); Pearson-
  residual normalisation (the SCTransform model) on 3000 HVGs, PCA, Harmony
  (original "harmony1" flavour) on `sample`, kNN on the top 6 PCs (paper: 6),
  Leiden. Seurat-Louvain resolutions do not transfer, so the graph is
  deliberately over-clustered (first resolution with >= PHASE2_MIN clusters)
  and each cluster is named by the paper's identity markers (IDENTITY):
  PVT = Gck / C1ql3 / Hcn1 (Results: PVT neurons "expressed markers such as
  Gck, C1ql3, and Hcn1"); Hb Tac2, MD Adarb2, IMD Cdh24, BSTpr Gpr101
  (Figure 1-figure supplement 2c-g ISH). Score = mean over the identity's
  markers of (pct in cluster - pct in all neurons); best score if
  > MIN_IDENTITY_SCORE, else unassigned.

Step B, PVT1-PVT5 (paper phase 3):
  B1 (diagnostic only) unsupervised re-clustering of the PVT nuclei with the
  paper's 18 PCs. Reported: resolution scan, silhouette, and for each
  five-cluster solution the best one-to-one match to PVT1-5.
  B2 (labels) per-nucleus assignment from the paper's published PVT1-5
  marker sets: for each cluster, the Supplementary file 1c DEGs with
  pct.1 >= MIN_PCT1 and pct_ratio >= MIN_RATIO, top N_MARKERS by pct_ratio
  (the paper's own marker-ranking statistic). Each set is scored with
  scanpy score_genes on log-normalised counts; scores are z-scored across
  PVT nuclei and each nucleus takes the arg-max. Margin = best - second z.
  Validation, against Supplementary file 1c:
    - held-out DEGs (in no scoring set): correlation of
      log(pct in label / pct in other PVT) with the published log pct_ratio;
    - ISH markers (Esr1, Col12a1, Npffr1, Hcrtr1, Drd3) and Drd2: pct per
      label vs published pct.1 / pct.2.

Outputs (OUT_DIR):
  labels_pvt_clusters.json   PVT1..PVT5 + non-PVT neighbour labels (all neurons)
  labels_pvt_pooled.json     "PVT" + the same non-PVT labels
  labels_pvt_ap.json         paper's AP assignment: "pPVT-biased (PVT1+PVT2)",
                             "aPVT-biased (PVT3+PVT4)", "pan-PVT (PVT5)" + non-PVT
  pvt_assignment.tsv         per PVT nucleus: label, z-scores, margin
  phase2_identity.tsv, phase3_leiden_diagnostic.tsv, validation_heldout.tsv,
  marker_check.tsv, derivation_report.md

Usage (scratch env: scanpy 1.13.0, leidenalg 0.12.0, scikit-learn 1.9.1,
openpyxl, tabulate):
  python -I <this script> NEURONS_SYMBOLS_H5AD SUPP1_XLSX OUT_DIR
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import scanpy as sc
import scipy.sparse as sp
from scipy.optimize import linear_sum_assignment
from sklearn.metrics import silhouette_score

SEED = 0
PHASE2_MIN = 14
MIN_IDENTITY_SCORE = 0.1
IDENTITY = {"PVT": ["Gck", "C1ql3", "Hcn1"], "Hb": ["Tac2"], "MD": ["Adarb2"],
            "IMD": ["Cdh24"], "BSTpr": ["Gpr101"]}
MIN_PCT1, MIN_RATIO, N_MARKERS = 0.3, 1.5, 30
ISH = {"PVT1": "Esr1", "PVT2": "Col12a1", "PVT3": "Npffr1", "PVT4": "Hcrtr1", "PVT5": "Drd3"}
AP = {"PVT1": "pPVT-biased (PVT1+PVT2)", "PVT2": "pPVT-biased (PVT1+PVT2)",
      "PVT3": "aPVT-biased (PVT3+PVT4)", "PVT4": "aPVT-biased (PVT3+PVT4)",
      "PVT5": "pan-PVT (PVT5)"}


def read_supp(xlsx: Path, sheet: str) -> pd.DataFrame:
    df = pd.read_excel(xlsx, sheet_name=sheet, header=1)
    df["cluster"] = df["cluster"].astype(str)
    return df


def pct(adata: sc.AnnData, mask: np.ndarray, genes: list[str]) -> np.ndarray:
    X = sp.csr_matrix(adata[:, genes].X)
    return np.asarray((X[mask] > 0).mean(axis=0)).ravel()


def embed(adata: sc.AnnData, n_pcs: int) -> sc.AnnData:
    a = adata.copy()
    sc.experimental.pp.highly_variable_genes(a, flavor="pearson_residuals", n_top_genes=3000,
                                             batch_key="sample")
    a = a[:, a.var["highly_variable"]].copy()
    sc.experimental.pp.normalize_pearson_residuals(a)
    sc.pp.pca(a, n_comps=max(30, n_pcs), random_state=SEED)
    a.obsm["X_pca_harmony"] = sc.pp.harmony_integrate(a, "obs.sample", flavor="harmony1", out=True, rng=SEED)
    sc.pp.neighbors(a, n_pcs=n_pcs, use_rep="X_pca_harmony", random_state=SEED)
    return a


def leiden_scan(a: sc.AnnData, n_pcs: int, resolutions) -> list[tuple[float, pd.Series, float]]:
    rep = a.obsm["X_pca_harmony"][:, :n_pcs]
    out = []
    for r in resolutions:
        sc.tl.leiden(a, resolution=r, key_added="leiden", random_state=SEED,
                     flavor="igraph", n_iterations=2)
        cl = a.obs["leiden"].astype(str).copy()
        sil = (silhouette_score(rep, cl, sample_size=min(5000, a.n_obs), random_state=SEED)
               if cl.nunique() > 1 else float("nan"))
        out.append((float(r), cl, float(sil)))
    return out


def main(h5ad: Path, xlsx: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    rep: list[str] = []
    adata = sc.read_h5ad(h5ad)
    rep.append(f"Input: {adata.n_obs} neuronal nuclei (phase-1 Neurons 1-8, > 1000 genes), "
               f"{adata.n_vars} genes, {adata.obs['sample'].nunique()} samples")

    # ---------------- Step A: PVT vs neighbours
    a2 = embed(adata, n_pcs=6)
    scan2 = leiden_scan(a2, 6, np.round(np.arange(0.05, 1.51, 0.05), 2))
    r2, cl2, _ = next(s for s in scan2 if s[1].nunique() >= PHASE2_MIN)
    genes = sorted({g for gs in IDENTITY.values() for g in gs})
    allpct = pd.Series(pct(adata, np.ones(adata.n_obs, bool), genes), index=genes)
    pin = pd.DataFrame({c: pct(adata, (cl2 == c).to_numpy(), genes) for c in sorted(cl2.unique(), key=int)},
                       index=genes)
    sc2 = pd.DataFrame({k: pin.loc[gs].sub(allpct.loc[gs], axis=0).mean(axis=0) for k, gs in IDENTITY.items()})
    best2 = sc2.apply(lambda row: row.idxmax() if row.max() > MIN_IDENTITY_SCORE else "unassigned", axis=1)
    tab2 = pd.concat([sc2.round(3), pin.T.round(2)], axis=1).assign(named=best2, n=cl2.value_counts())
    tab2.to_csv(out / "phase2_identity.tsv", sep="\t")
    ident = cl2.map(best2)
    is_pvt = (ident == "PVT").to_numpy()
    nonpvt = ident.map(lambda k: f"{k} neuron (derived)" if k != "unassigned"
                       else "non-PVT neuron, unassigned (derived)")
    rep += ["\n## Step A: PVT vs neighbouring nuclei (paper phase 2; 6 PCs)",
            "Resolution scan (res, n_clusters, silhouette): "
            + str([(r, c.nunique(), round(s, 3)) for r, c, s in scan2]),
            f"Chosen resolution {r2}: {cl2.nunique()} clusters (over-clustered; named by identity markers "
            f"{json.dumps(IDENTITY)}, threshold {MIN_IDENTITY_SCORE}).",
            tab2.to_markdown(),
            f"\nPVT nuclei: {is_pvt.sum()} of {adata.n_obs} ({is_pvt.mean():.1%}); paper: 5737 of 9845 (58.3%).",
            "Identity counts: " + json.dumps(ident.value_counts().to_dict())
            + "; paper: MD 1758, IMD 609, BSTpr 879, Hb 862."]

    # ---------------- Step B: PVT1-5
    s1c = read_supp(xlsx, "Supplementary File 1c")
    sel = s1c[(s1c["pct.1"] >= MIN_PCT1) & (s1c["pct_ratio"] >= MIN_RATIO)]
    sets = {k: list(g.sort_values("pct_ratio", ascending=False)["gene"][:N_MARKERS])
            for k, g in sel.groupby("cluster")}
    pvt = adata[is_pvt].copy()
    missing = {k: [g for g in gs if g not in pvt.var_names] for k, gs in sets.items()}
    rep += ["\n## Step B: PVT1-PVT5 (paper phase 3)",
            f"Scoring sets (Supp. 1c, pct.1 >= {MIN_PCT1}, pct_ratio >= {MIN_RATIO}, top {N_MARKERS} by "
            "pct_ratio): " + json.dumps(sets), "Missing from matrix: " + json.dumps(missing)]

    lognorm = pvt.copy()
    sc.pp.normalize_total(lognorm, target_sum=1e4)
    sc.pp.log1p(lognorm)
    for k, gs in sets.items():
        sc.tl.score_genes(lognorm, [g for g in gs if g in lognorm.var_names], score_name=k, random_state=SEED)
    Z = lognorm.obs[list(sets)]
    Z = (Z - Z.mean()) / Z.std()

    # B1 diagnostic: unsupervised re-clustering, as in the paper
    a3 = embed(pvt, n_pcs=18)
    scan3 = leiden_scan(a3, 18, np.round(np.arange(0.05, 0.81, 0.025), 3))
    diag = []
    for r, cl, sil in scan3:
        if cl.nunique() == 5:
            m = Z.groupby(cl.to_numpy()).mean()
            ri, ci = linear_sum_assignment(-m.to_numpy())
            diag.append({"resolution": r, "silhouette": round(sil, 3),
                         "sizes": json.dumps(cl.value_counts().sort_index().to_dict()),
                         "best_match": json.dumps({m.index[i]: m.columns[j] for i, j in zip(ri, ci)}),
                         "mean_z_of_match": json.dumps({m.index[i]: round(float(m.iloc[i, j]), 2)
                                                        for i, j in zip(ri, ci)})})
    pd.DataFrame(diag).to_csv(out / "phase3_leiden_diagnostic.tsv", sep="\t", index=False)
    rep += ["\n### B1 diagnostic: unsupervised re-clustering (18 PCs)",
            "Resolution scan (res, n_clusters, silhouette): "
            + str([(r, c.nunique(), round(s, 3)) for r, c, s in scan3]),
            "Five-cluster solutions, matched to PVT1-5 by mean marker-set z (Hungarian):",
            pd.DataFrame(diag).to_markdown(index=False) if diag else "(no resolution gave exactly 5 clusters)"]

    # B2 assignment from published marker sets
    lab = Z.idxmax(axis=1)
    srt = np.sort(Z.to_numpy(), axis=1)
    margin = pd.Series(srt[:, -1] - srt[:, -2], index=Z.index)
    pd.concat([lab.rename("label"), Z.round(3), margin.round(3).rename("margin")], axis=1).to_csv(
        out / "pvt_assignment.tsv", sep="\t", index_label="cell_id")
    rep += ["\n### B2 assignment from the published marker sets",
            "Counts: " + json.dumps(lab.value_counts().sort_index().to_dict()),
            f"Margin (best - second z): median {margin.median():.2f}; "
            f"{(margin < 0.5).mean():.0%} of nuclei < 0.5; per label median "
            + json.dumps(margin.groupby(lab).median().round(2).to_dict())]

    # validation 1: held-out DEGs
    used = {g for gs in sets.values() for g in gs}
    rows = []
    for k in sets:
        pub = s1c[(s1c["cluster"] == k) & ~s1c["gene"].isin(used) & s1c["gene"].isin(pvt.var_names)]
        m = (lab == k).to_numpy()
        gl = list(pub["gene"])
        d1, d2 = pct(pvt, m, gl), pct(pvt, ~m, gl)
        ok = (d1 > 0) & (d2 > 0)
        rows.append({"label": k, "n_heldout_degs": len(gl),
                     "r_log_pct_ratio": round(float(np.corrcoef(np.log(d1[ok] / d2[ok]),
                                                                np.log(pub["pct_ratio"].to_numpy()[ok]))[0, 1]), 3),
                     "median_derived_minus_published_pct1": round(float(np.median(d1 - pub["pct.1"].to_numpy())), 3),
                     "frac_heldout_with_derived_ratio_gt1": round(float((d1 > d2).mean()), 3)})
    val = pd.DataFrame(rows)
    val.to_csv(out / "validation_heldout.tsv", sep="\t", index=False)
    rep += ["\nValidation on held-out Supp. 1c DEGs (not used for scoring):", val.to_markdown(index=False)]

    # validation 2: ISH markers + Drd2
    mrows = []
    for g in list(ISH.values()) + ["Drd2"]:
        for k in sets:
            m = (lab == k).to_numpy()
            pub = s1c[(s1c["cluster"] == k) & (s1c["gene"] == g)]
            mrows.append({"gene": g, "label": k, "derived_pct": round(float(pct(pvt, m, [g])[0]), 3),
                          "published_pct1": float(pub["pct.1"].iloc[0]) if len(pub) else None,
                          "published_pct2": float(pub["pct.2"].iloc[0]) if len(pub) else None,
                          "in_scoring_set": g in sets[k]})
    mc = pd.DataFrame(mrows)
    mc.to_csv(out / "marker_check.tsv", sep="\t", index=False)
    rep += ["\nISH markers (pct expressing per derived label; published pct.1/pct.2 where the gene is a "
            "Supp. 1c DEG of that cluster):",
            mc.pivot(index="gene", columns="label", values="derived_pct").to_markdown(),
            mc.dropna(subset=["published_pct1"]).to_markdown(index=False)]

    # ---------------- label files (all neurons)
    full = nonpvt.copy()
    full.loc[lab.index] = lab
    pooled = nonpvt.copy()
    pooled.loc[lab.index] = "PVT"
    ap = nonpvt.copy()
    ap.loc[lab.index] = lab.map(AP)
    for name, s in [("labels_pvt_clusters.json", full), ("labels_pvt_pooled.json", pooled),
                    ("labels_pvt_ap.json", ap)]:
        (out / name).write_text(json.dumps(s.to_dict(), indent=0, sort_keys=True) + "\n")
        rep.append(f"\nwrote {name}: " + json.dumps(s.value_counts().to_dict()))
    (out / "derivation_report.md").write_text("# Gao 2023 PVT label re-derivation (DERIVED labels)\n\n"
                                              + "\n".join(rep) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
