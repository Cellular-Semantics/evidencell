# AT Run: Kapustina 2024 ATN, derived 3-group labels → WMBv1 (CCN20230722)

Status: scored, manifest written, run registered. **Descriptive only.** The
labels are re-derived, not the authors' clusters, so no node declares them as
`at_source_sets`. F1 gate review pending.

Shares `mmc_results.csv` with
`../at_run_20261117_kapustina2024_atn_mmc_wmbv1/`. The full reproduction
recipe is in that run's README (steps 4–6 cover this run).

## Why derived labels

GEO:GSE227627 deposits counts and per-well metadata but no cluster
assignments. `scripts/derive_k3_labels.py` re-partitions the 878 excitatory
neurons into three groups without reading any WMBv1 output. The groups are
named neutrally because the KB's independent nucleus markers don't separate
them cleanly (see `manifest.yaml`).

## Results (supertype level, bootstrap ≥ 0.8)

| Label | n | Best supertype | Coverage | Purity | F1 |
|---|---|---|---|---|---|
| derived_k3_1 | 459 | 0642 AV Col27a1 Glut_1 | 0.91 | 0.95 | 0.93 |
| derived_k3_2 | 222 | 0662 TH Prkcd Grin2c Glut_9 (AM-dominant) | 0.81 | 0.80 | 0.80 |
| derived_k3_0 | 197 | 0652 CM-IAD-CL-PCN Sema5b Glut_4 | 0.36 | 0.82 | 0.50 |

derived_k3_0 is a mixed remainder: 0652, plus 0662, 0658 (LD), 0641 (AD) and
0670 (RE). No AD-specific group emerges. Of the 38 AD-mapping cells, 27 are in
k3_1 and 11 in k3_0. `label_distribution.tsv` gives the per-cluster detail and
`derived_k3_markers.tsv` the within-dataset markers.
