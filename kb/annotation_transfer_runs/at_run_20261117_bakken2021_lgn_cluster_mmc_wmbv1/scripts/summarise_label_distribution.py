"""Per-source-label distribution of mapped cells over WMBv1 nodes, annotated
with each WMBv1 node's dominant MERFISH thalamic nucleus.

Complements the F1 matrix: for anatomy-defined labels (a projection system =
a nucleus complex retrogradely labelled from one cortical area) the useful
read-out is "which WMB clusters do these cells land in, and where do those
clusters sit", not a single best F1 target.

Cells are counted at a level only if that level's bootstrapping probability
is >= THRESHOLD (same rule as `annotation-transfer score`, default 0.8).
Dominant nucleus = the thalamic nucleus-level MBA term (list below) with the
highest cell_ratio in the taxonomy DB `anat` table for that node.

Usage (from the clone root):
  .venv/bin/python -I <this script> MMC_CSV LABELS_JSON OUT_TSV [--threshold 0.8] [--top 6]
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

import pandas as pd

DB = Path("kb/taxonomy/CCN20230722/CCN20230722.db")

# Nucleus-level MBA terms within / adjacent to dorsal thalamus.
NUCLEI = {
    "MBA:170": "LGd", "MBA:218": "LP", "MBA:1020": "PO", "MBA:629": "VAL",
    "MBA:685": "VM", "MBA:733": "VPM", "MBA:718": "VPL", "MBA:741": "VPMpc",
    "MBA:1072": "MGd", "MBA:1079": "MGv", "MBA:1088": "MGm", "MBA:362": "MD",
    "MBA:255": "AV", "MBA:64": "AD", "MBA:127": "AM", "MBA:155": "LD",
    "MBA:149": "PVT", "MBA:181": "RE", "MBA:189": "RH", "MBA:599": "CM",
    "MBA:575": "CL", "MBA:907": "PCN", "MBA:930": "PF", "MBA:366": "SMT",
    "MBA:262": "RT", "MBA:178": "LGv", "MBA:27": "IGL", "MBA:1113": "IAD",
    "MBA:609": "SPA", "MBA:325": "SGN", "MBA:560581563": "PIL", "MBA:59": "IMD",
    "MBA:15": "PT", "MBA:563807435": "PoT",
}
LEVELS = ("class", "subclass", "supertype", "cluster")


def dominant_nucleus(con: sqlite3.Connection, accession: str) -> str:
    q = ",".join("?" * len(NUCLEI))
    rows = con.execute(
        f"SELECT anat_id, MAX(cell_ratio) FROM anat WHERE node_id=? AND anat_id IN ({q}) "
        "GROUP BY anat_id ORDER BY 2 DESC LIMIT 2",
        (accession, *NUCLEI),
    ).fetchall()
    return "; ".join(f"{NUCLEI[a]} {r:.2f}" for a, r in rows) or "-"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mmc_csv")
    ap.add_argument("labels_json")
    ap.add_argument("out_tsv")
    ap.add_argument("--threshold", type=float, default=0.8)
    ap.add_argument("--top", type=int, default=6)
    a = ap.parse_args()

    mmc = pd.read_csv(a.mmc_csv, comment="#").set_index("cell_id")
    labels = pd.Series(json.loads(Path(a.labels_json).read_text()))
    mmc = mmc.loc[mmc.index.intersection(labels.index)]
    mmc["source_label"] = labels.loc[mmc.index]
    con = sqlite3.connect(DB)

    out = []
    for lvl in ("supertype", "cluster"):
        ok = mmc[mmc[f"{lvl}_bootstrapping_probability"] >= a.threshold]
        target_tot = ok[f"{lvl}_label"].value_counts()
        for lab, grp in ok.groupby("source_label"):
            n_lab = int((labels == lab).sum())
            vc = grp[[f"{lvl}_label", f"{lvl}_name"]].value_counts().head(a.top)
            for (acc, name), n in vc.items():
                out.append({
                    "source_label": lab, "level": lvl, "target_accession": acc,
                    "target_name": name, "n_cells": int(n),
                    "frac_of_label": round(n / n_lab, 3),
                    "purity_in_dataset": round(n / target_tot[acc], 3),
                    "dominant_merfish_nucleus": dominant_nucleus(con, acc),
                })
    df = pd.DataFrame(out)
    df.to_csv(a.out_tsv, sep="\t", index=False)
    with pd.option_context("display.width", 250, "display.max_rows", 500, "display.max_colwidth", 40):
        print(df.to_string(index=False))


if __name__ == "__main__":
    main()
