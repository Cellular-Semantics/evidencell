"""
Correlate Knoedler 2022 (Cell, GSE183092) TRAP-seq Esr1+ pools against
WMBv1 cluster pseudobulks. Four regions × three states × three replicates.

Pools (after replicate averaging): 12 total
  BNST_M, BNST_FR, BNST_FNR
  MeA_M,  MeA_FR,  MeA_FNR
  POA_M,  POA_FR,  POA_FNR
  VMH_M,  VMH_FR,  VMH_FNR

Differential contrasts (target classical type → expected δ):
  POA_FR  - VMH_FR   → mpoa_esr1_neuron (POA-specific Esr1+)
  POA_M   - POA_FR   → sdn_poa_calbindin_neuron proxy (male-biased POA Esr1+)
  BNST_FR - VMH_FR   → bnst_crf_neuron proxy via Esr1+ (BNST-specific)
  MeA_FR  - VMH_FR   → MeA Esr1+ (no current classical node)
  VMH_FR  - MeA_FR   → vmhvl_esr1_pr_neuron (VMHvl-specific Esr1+)
  VMH_M   - VMH_FR   → male-biased VMH Esr1+ (PR+/aggression population)
"""

import json
import sys
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).parent
DATA = ROOT / "data"
H5_PATH = "/Users/do12/Documents/GitHub/evidencell/scratch/olm-at/precomputed_stats_ABC_revision_230821.h5"
GENE_MAPPING = "/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/conf/gene_mapping_CCN20230722.tsv"
TAX_DB = "/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/taxonomy/CCN20230722/CCN20230722.db"

REGIONS = ["BNST", "MeA", "POA", "VMH"]
STATES = ["Male", "FR", "FNR"]


def load_symbol_to_ensembl():
    df = pd.read_csv(GENE_MAPPING, sep="\t")
    return dict(zip(df["symbol"], df["ensembl_id"]))


def load_knoedler(symbol_to_ens):
    pools = {}
    for region in REGIONS:
        path = DATA / f"GSE183092_{region}_Normalized_Gene_Counts.csv.gz"
        df = pd.read_csv(path)
        df.columns = [c.strip().lstrip("﻿") for c in df.columns]
        df = df.rename(columns={"Gene": "symbol"})
        df["ensembl_id"] = df["symbol"].map(symbol_to_ens)
        df = df.dropna(subset=["ensembl_id"]).drop_duplicates(subset="ensembl_id", keep="first").set_index("ensembl_id")
        for state in STATES:
            cols = [c for c in df.columns if c.startswith(f"{state} {region} Rep")]
            assert len(cols) == 3, f"{region}/{state}: expected 3 reps, got {cols}"
            pool_name = f"{region}_{state}"
            pools[pool_name] = df[cols].mean(axis=1)
    out = pd.DataFrame(pools).dropna()
    return out


def load_atlas():
    with h5py.File(H5_PATH, "r") as f:
        s = f["sum"][()]
        n = f["n_cells"][()].astype(np.float64)
        col_names = json.loads(f["col_names"][()])
        c2r = json.loads(f["cluster_to_row"][()])
    mean_log = np.log1p(s / n[:, None])
    cluster_ids = [None] * len(c2r)
    for cid, row in c2r.items():
        cluster_ids[row] = cid
    return mean_log, col_names, cluster_ids


def correlate_pool(atlas_sub, pool_log_vec):
    rho = np.empty(atlas_sub.shape[0])
    for i in range(atlas_sub.shape[0]):
        rho[i], _ = spearmanr(atlas_sub[i], pool_log_vec)
    return rho


def cluster_metadata(cluster_ids):
    import sqlite3
    con = sqlite3.connect(TAX_DB)
    q = """
        SELECT n.short_form, n.label, n.parent_id, n.male_female_ratio,
               (SELECT a.anat_label FROM anat a WHERE a.node_id = n.node_id
                  ORDER BY a.cell_count DESC LIMIT 1) AS top_anat,
               (SELECT MAX(a.cell_count) FROM anat a WHERE a.node_id = n.node_id) AS top_anat_n
          FROM nodes n
          WHERE n.short_form = ?
    """
    cur = con.cursor()
    rows = []
    for cid in cluster_ids:
        cur.execute(q, (cid,))
        r = cur.fetchone()
        if r:
            rows.append({"cluster_id": cid, "label": r[1], "parent_supertype": r[2],
                         "mfr": r[3], "top_anat": r[4] or "", "top_anat_n": r[5]})
        else:
            rows.append({"cluster_id": cid, "label": "", "parent_supertype": "",
                         "mfr": None, "top_anat": "", "top_anat_n": None})
    con.close()
    return pd.DataFrame(rows)


def main():
    print("Loading symbol → Ensembl…", file=sys.stderr)
    sym2ens = load_symbol_to_ensembl()
    print(f"  {len(sym2ens)} mappings", file=sys.stderr)

    print("Loading Knoedler pools…", file=sys.stderr)
    pools = load_knoedler(sym2ens)
    print(f"  {pools.shape[0]} genes (Ensembl-mapped, deduped) × {pools.shape[1]} pools", file=sys.stderr)
    pools_log = np.log1p(pools)

    print("Loading atlas HDF5…", file=sys.stderr)
    atlas, atlas_genes, cluster_ids = load_atlas()
    print(f"  {atlas.shape[0]} clusters × {atlas.shape[1]} genes", file=sys.stderr)

    g2i = {g: i for i, g in enumerate(atlas_genes)}
    shared = [g for g in pools_log.index if g in g2i]
    print(f"  shared genes: {len(shared)}", file=sys.stderr)

    pool_sub = pools_log.loc[shared]
    atlas_idx = np.array([g2i[g] for g in shared])
    atlas_sub = atlas[:, atlas_idx]

    rho_df = pd.DataFrame(index=cluster_ids)
    for pool in pool_sub.columns:
        print(f"Correlating clusters vs {pool}…", file=sys.stderr)
        rho_df[f"rho_{pool}"] = correlate_pool(atlas_sub, pool_sub[pool].to_numpy())

    contrasts = {
        "delta_POA_FR_minus_VMH_FR":  ("POA_FR",  "VMH_FR"),
        "delta_POA_Male_minus_POA_FR":   ("POA_Male",  "POA_FR"),
        "delta_BNST_FR_minus_VMH_FR":    ("BNST_FR",   "VMH_FR"),
        "delta_MeA_FR_minus_VMH_FR":     ("MeA_FR",    "VMH_FR"),
        "delta_VMH_FR_minus_MeA_FR":     ("VMH_FR",    "MeA_FR"),
        "delta_VMH_Male_minus_VMH_FR":   ("VMH_Male",  "VMH_FR"),
        "delta_VMH_FR_minus_BNST_FR":    ("VMH_FR",    "BNST_FR"),
        "delta_BNST_Male_minus_BNST_FR": ("BNST_Male", "BNST_FR"),
    }
    for name, (a, b) in contrasts.items():
        rho_df[name] = rho_df[f"rho_{a}"] - rho_df[f"rho_{b}"]

    rho_df = rho_df.reset_index().rename(columns={"index": "cluster_id"})
    meta = cluster_metadata(cluster_ids)
    rho_df = rho_df.merge(meta, on="cluster_id", how="left")

    rho_df.to_csv(ROOT / "all_correlations.tsv", sep="\t", index=False)

    out_dir = ROOT / "ranked_contrasts"
    out_dir.mkdir(exist_ok=True)
    for name in contrasts:
        sub = rho_df.sort_values(name, ascending=False)
        sub.to_csv(out_dir / f"{name}.tsv", sep="\t", index=False)
        print(f"\n=== TOP 10 by {name} ===", file=sys.stderr)
        cols = ["cluster_id", "label", "parent_supertype", "mfr", "top_anat", "top_anat_n", name]
        print(sub[cols].head(10).to_string(index=False), file=sys.stderr)


if __name__ == "__main__":
    main()
