"""
Correlate bulk RNA-seq Kiss1 RP3V/ARC pools (Stephens et al. 2024, PMID 37934722,
Reproduction supp table 3) against WMBv1 cluster pseudobulks.

Output: ranked tables of clusters by Spearman correlation against each bulk pool,
plus a short text summary of top hits and the rank of expected matches.
"""

import json
import sys
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).parent
H5_PATH = "/Users/do12/Documents/GitHub/evidencell/scratch/olm-at/precomputed_stats_ABC_revision_230821.h5"
BULK_CSV = ROOT / "bulk_supp_table.csv"
TAX_DB = "/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/taxonomy/CCN20230722/CCN20230722.db"


def load_bulk():
    df = pd.read_csv(BULK_CSV)
    df.columns = [c.strip() for c in df.columns]
    df = df.rename(columns={"Esemble Gene ID": "ensembl_id", "ARC Log2>7": "ARC", "Gene Name": "gene_name"})
    df = df.drop_duplicates(subset="ensembl_id", keep="first")
    return df.set_index("ensembl_id")


def load_atlas():
    with h5py.File(H5_PATH, "r") as f:
        s = f["sum"][()]
        n = f["n_cells"][()].astype(np.float64)
        col_names = json.loads(f["col_names"][()])
        c2r = json.loads(f["cluster_to_row"][()])
    mean = s / n[:, None]
    mean_log = np.log1p(mean)
    return mean_log, col_names, c2r


def correlate_all(atlas_mean, atlas_genes_idx, bulk_vec, cluster_ids, atlas_genes_subset_idx_in_atlas):
    rho_list = []
    p_list = []
    sub = atlas_mean[:, atlas_genes_subset_idx_in_atlas]
    for i, cid in enumerate(cluster_ids):
        rho, p = spearmanr(sub[i], bulk_vec)
        rho_list.append(rho)
        p_list.append(p)
    return np.array(rho_list), np.array(p_list)


def cluster_metadata(cluster_ids):
    import sqlite3
    con = sqlite3.connect(TAX_DB)
    q = """
        SELECT n.short_form, n.label, n.parent_id, n.male_female_ratio,
               (SELECT a.anat_label FROM anat a
                  WHERE a.node_id = n.node_id
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
    print("Loading bulk supp table…", file=sys.stderr)
    bulk = load_bulk()
    print(f"  bulk genes: {len(bulk)}", file=sys.stderr)

    print("Loading atlas HDF5…", file=sys.stderr)
    atlas_mean, atlas_genes, c2r = load_atlas()
    print(f"  atlas: {atlas_mean.shape[0]} clusters × {atlas_mean.shape[1]} genes", file=sys.stderr)

    cluster_ids = [None] * len(c2r)
    for cid, row in c2r.items():
        cluster_ids[row] = cid
    assert all(c is not None for c in cluster_ids)

    atlas_idx_by_gene = {g: i for i, g in enumerate(atlas_genes)}
    shared = [g for g in bulk.index if g in atlas_idx_by_gene]
    print(f"  shared genes: {len(shared)} (of {len(bulk)} bulk; {len(atlas_genes)} atlas)", file=sys.stderr)

    bulk_sub = bulk.loc[shared]
    atlas_subset_idx = np.array([atlas_idx_by_gene[g] for g in shared])

    rp3v_vec = bulk_sub["RP3V"].to_numpy()
    arc_vec = bulk_sub["ARC"].to_numpy()

    print("Correlating clusters vs RP3V…", file=sys.stderr)
    rho_rp3v, p_rp3v = correlate_all(atlas_mean, atlas_genes, rp3v_vec, cluster_ids, atlas_subset_idx)
    print("Correlating clusters vs ARC…", file=sys.stderr)
    rho_arc, p_arc = correlate_all(atlas_mean, atlas_genes, arc_vec, cluster_ids, atlas_subset_idx)

    df = pd.DataFrame({
        "cluster_id": cluster_ids,
        "rho_rp3v": rho_rp3v,
        "rho_arc": rho_arc,
        "delta_rp3v_minus_arc": rho_rp3v - rho_arc,
    })
    meta = cluster_metadata(cluster_ids)
    df = df.merge(meta, on="cluster_id", how="left")

    df["delta_arc_minus_rp3v"] = df["rho_arc"] - df["rho_rp3v"]
    df.sort_values("rho_rp3v", ascending=False).to_csv(ROOT / "correlations_rp3v.tsv", sep="\t", index=False)
    df.sort_values("rho_arc", ascending=False).to_csv(ROOT / "correlations_arc.tsv", sep="\t", index=False)
    df.sort_values("delta_rp3v_minus_arc", ascending=False).to_csv(ROOT / "delta_rp3v_specific.tsv", sep="\t", index=False)
    df.sort_values("delta_arc_minus_rp3v", ascending=False).to_csv(ROOT / "delta_arc_specific.tsv", sep="\t", index=False)

    expected = ["CS20230722_CLUS_1915", "CS20230722_CLUS_1916", "CS20230722_CLUS_1917",
                "CS20230722_CLUS_1918", "CS20230722_CLUS_1919"]
    print("\n=== TOP 20 by RP3V correlation ===", file=sys.stderr)
    print(df.sort_values("rho_rp3v", ascending=False).head(20).to_string(index=False), file=sys.stderr)
    print("\n=== TOP 20 by ARC correlation ===", file=sys.stderr)
    print(df.sort_values("rho_arc", ascending=False).head(20).to_string(index=False), file=sys.stderr)
    print("\n=== TOP 20 by RP3V - ARC delta (RP3V-specific) ===", file=sys.stderr)
    print(df.sort_values("delta_rp3v_minus_arc", ascending=False).head(20).to_string(index=False), file=sys.stderr)
    print("\n=== TOP 20 by ARC - RP3V delta (ARC-specific) ===", file=sys.stderr)
    print(df.sort_values("delta_arc_minus_rp3v", ascending=False).head(20).to_string(index=False), file=sys.stderr)

    print("\n=== Rank of expected AVPV/PeN Kiss1 candidates ===", file=sys.stderr)
    df_rp3v_sorted = df.sort_values("rho_rp3v", ascending=False).reset_index(drop=True)
    for cid in expected:
        rank = df_rp3v_sorted.index[df_rp3v_sorted["cluster_id"] == cid]
        if len(rank) > 0:
            r = rank[0]
            row = df_rp3v_sorted.iloc[r]
            print(f"  {cid}: rank {r+1}/{len(df_rp3v_sorted)}  rho_rp3v={row['rho_rp3v']:.4f}  rho_arc={row['rho_arc']:.4f}  delta={row['delta_rp3v_minus_arc']:.4f}", file=sys.stderr)


if __name__ == "__main__":
    main()
