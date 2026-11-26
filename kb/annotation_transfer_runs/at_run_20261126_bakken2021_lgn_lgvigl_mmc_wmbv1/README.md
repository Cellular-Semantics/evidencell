# AT Run: Bakken 2021 mouse LGv/IGL GABAergic clusters (GABA2-6 pooled) → WMBv1 (CCN20230722)

Status: scored, manifest written, run registered (`index.yaml`). Declared as
the `at_source_sets` entry of `lgv_igl_gabaergic_neuron` (SUBSET). No mapping
edges yet; F1 gate review pending.

Shares `mmc_results.csv` with
`../at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1/` (the published-label
run). No new MapMyCells run. That run's README has the full recipe (GEO fetch,
h5ad build, mapping).

## Why this pool

Bakken et al. 2021 place their mouse GABA2-6 clusters outside dLGN, in IGL and
LGv (Figure 4C; text: "the mouse GABA2-6 types are not found in dLGN but are
located only in the adjacent thalamic nuclei; IGL, LGv, and LP"). The pool
follows that assignment. No WMBv1 output was used to choose it. The
label → paper-type key and the cluster × dissection table are in
`planning/content-notes/thalamus_bakken2021_labels.md`.

## Reproduction (from the clone root)

```bash
R=kb/annotation_transfer_runs/at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1
L=kb/annotation_transfer_runs/at_run_20261126_bakken2021_lgn_lgvigl_mmc_wmbv1
.venv/bin/python -I $L/scripts/build_lgvigl_labels.py $R/labels_cluster.json $L/labels_lgvigl.json
just at-score ../$R/mmc_results.csv ../$L/labels_lgvigl.json ../$L/f1_matrix.csv
.venv/bin/python -I $L/scripts/summarise_label_distribution.py \
  $R/mmc_results.csv $L/labels_lgvigl.json $L/label_distribution.tsv --top 4
uv run python -m evidencell.at_metrics migrate $L
just register-at-run
```

`scripts/summarise_label_distribution.py` is vendored unchanged from
`../at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1/scripts/`.

## Results (bootstrap ≥ 0.8)

| Source label | Level | Best WMB target | Coverage | Purity | F1 | Cells |
|---|---|---|---|---|---|---|
| LGv/IGL GABA (GABA2-6) | class | 12 HY GABA | 0.47 | 0.72 | 0.57 | 137 |
| | class | 20 MB GABA | 0.49 | 0.24 | 0.33 | 145 |
| | subclass | 203 LGv-SPFp-SPFm Nkx2-2 Tcf7l2 Gaba | 0.49 | 1.00 | 0.66 | 143 |
| | subclass | 109 LGv-ZI Otx2 Gaba | 0.31 | 1.00 | 0.47 | 90 |
| | subclass | 101 ZI Pax6 Gaba | 0.16 | 1.00 | 0.27 | 46 |
| | supertype | 0840 LGv-SPFp-SPFm Nkx2-2 Tcf7l2 Gaba_7 | 0.15 | 1.00 | 0.25 | 41 |

The pool splits across three WMB subclasses, each pure within this dataset.
See `manifest.yaml` caveats.
