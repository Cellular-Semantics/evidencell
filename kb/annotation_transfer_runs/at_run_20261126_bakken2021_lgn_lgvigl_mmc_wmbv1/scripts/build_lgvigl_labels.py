"""Derive the pooled LGv/IGL GABAergic label scheme for Bakken 2021 mouse cells.

Reads the published-label JSON of
at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1 (GEO `cluster_label`, "Low
Quality" already dropped) and writes {cell: label} with the five GABAergic
clusters the authors place outside dLGN, in IGL / LGv (Bakken et al. 2021,
Figure 4C; GABA2-6) pooled as "LGv/IGL GABA (GABA2-6)". Every other cell is
"other (non-LGv/IGL GABA)". The pool is chosen from the paper's own anatomical
assignment only; no WMBv1 mapping output is read.

Usage:
    python -I build_lgvigl_labels.py LABELS_CLUSTER_JSON OUT_JSON
"""

import json
import sys

POOL = {"GABA2", "GABA3", "GABA4", "GABA5", "GABA6"}
IN_LABEL = "LGv/IGL GABA (GABA2-6)"
OUT_LABEL = "other (non-LGv/IGL GABA)"


def main(src: str, dst: str) -> None:
    with open(src) as fh:
        published = json.load(fh)
    derived = {cell: IN_LABEL if lab in POOL else OUT_LABEL for cell, lab in published.items()}
    with open(dst, "w") as fh:
        json.dump(derived, fh, indent=0)
        fh.write("\n")
    n_in = sum(v == IN_LABEL for v in derived.values())
    print(f"{IN_LABEL}: {n_in}; {OUT_LABEL}: {len(derived) - n_in}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
