# AT Run: Kapustina 2024 anterior thalamic nuclei → WMBv1 (CCN20230722)

Status: outputs complete, manifest written, run registered (`index.yaml`).
`at_results.yaml` / `at_results_best.yaml` generated with `at_metrics migrate`.
`at_source_sets` declared on `anterior_thalamic_nucleus_excitatory_neuron`
(label `ATN`); no mapping edges exist yet, so no evidence attached.
F1 gate review pending.

## Purpose

Kapustina et al. 2024 (*Cell Rep* 43:113842, PMID:38427564,
doi:10.1016/j.celrep.2024.113842) report three discrete excitatory clusters in
the mouse ATN, corresponding to AD, AV and AM. This run maps their scRNA-seq
cells onto WMBv1.

## Data source

- GEO:GSE227627 `GSE227627_merged_counts.txt.gz`: genes × wells UMI counts,
  Ensembl IDs (NCBIM37).
- GEO:GSE227627 `GSE227627_metadata.txt.gz`: per-well identifier, barcode,
  animalId and source.
- **No per-cell cluster / nucleus labels are deposited.** The only annotation
  is the ATN dissection. Control wells (ERCC, qRNA, blank) are flagged in
  `source`.
- Out of scope: the Visium objects in the same series, and the Xenium
  companion GEO:GSE255953.

## Two label schemes, one mapping

| Run | Labels | File |
|---|---|---|
| this run | `ATN` (all 912 QC-passed cells) | `labels_atn.json` |
| `at_run_20261117_kapustina2024_atn_derivedk3_mmc_wmbv1` | `derived_k3_{0,1,2}`: re-derived unsupervised groups of 878 neurons (not the authors' labels) | `../at_run_20261117_kapustina2024_atn_derivedk3_mmc_wmbv1/labels_derivedk3.json` |

Both score the same `mmc_results.csv`.

## Reproduction (from the clone root)

```bash
# 1. fetch GEO files
D=annotation_transfer/inputs/datasets/kapustina2024_atn; mkdir -p $D
for f in GSE227627_merged_counts.txt.gz GSE227627_metadata.txt.gz; do
  curl -sSL -o $D/$f https://ftp.ncbi.nlm.nih.gov/geo/series/GSE227nnn/GSE227627/suppl/$f; done

# 2. build h5ad (ATN wells, >= 1,000 genes, Ensembl IDs in WMBv1 stats) + ATN label JSON
R=kb/annotation_transfer_runs/at_run_20261117_kapustina2024_atn_mmc_wmbv1
annotation_transfer/.venv/bin/python -I $R/scripts/build_kapustina2024_h5ad.py \
  $D conf/mapmycells/CCN20230722/precomputed_stats_ABC_revision_230821.h5 $R

# 3. preflight + local MapMyCells (cell_type_mapper 1.7.5)
just at-preflight ../$D/kapustina2024_atn_mmc.h5ad
cd annotation_transfer && uv run --no-sync annotation-transfer map-local \
  inputs/datasets/kapustina2024_atn/kapustina2024_atn_mmc.h5ad \
  ../conf/mapmycells/CCN20230722/precomputed_stats_ABC_revision_230821.h5 \
  ../conf/mapmycells/CCN20230722/mouse_markers_230821.json \
  inputs/datasets/kapustina2024_atn/mmc/mmc_extended.json \
  --csv inputs/datasets/kapustina2024_atn/mmc/mmc_results.csv && cd ..
cp $D/mmc/mmc_results.csv $R/

# 4. derived 3-group labels (companion run)
S=kb/annotation_transfer_runs/at_run_20261117_kapustina2024_atn_derivedk3_mmc_wmbv1
annotation_transfer/.venv/bin/python -I $S/scripts/derive_k3_labels.py \
  $D/kapustina2024_atn_mmc.h5ad $D/GSE227627_merged_counts.txt.gz $S

# 5. score (bootstrap threshold 0.8), both schemes
just at-score ../$R/mmc_results.csv ../$R/labels_atn.json ../$R/f1_matrix.csv
just at-score ../$R/mmc_results.csv ../$S/labels_derivedk3.json ../$S/f1_matrix.csv

# 6. per-label distribution with WMBv1 MERFISH nucleus annotation
.venv/bin/python -I $R/scripts/summarise_label_distribution.py \
  $R/mmc_results.csv $R/labels_atn.json $R/label_distribution.tsv --top 12
.venv/bin/python -I $R/scripts/summarise_label_distribution.py \
  $R/mmc_results.csv $S/labels_derivedk3.json $S/label_distribution.tsv --top 5

# 7. at_results YAML + index
just migrate-at-metrics && just register-at-run
```

## Results summary

| Level | Best target | Coverage | Purity | F1 |
|---|---|---|---|---|
| class | 18 TH Glut | 0.96 | 1.0* | 0.98 |
| subclass | 148 AV Col27a1 Glut | 0.51 | 1.0* | 0.68 |
| supertype | 0642 AV Col27a1 Glut_1 | 0.51 | 1.0* | 0.68 |
| cluster | 2615 AV Col27a1 Glut_1 | 0.29 | 1.0* | 0.46 |

\* Purity is 1.0 by construction in a single-label run.

Supertype split: 0642 AV 48%, 0662 (AM-dominant) 22%, 0652 CM-IAD-CL-PCN 8%,
0641 AD 4%, 0658 (LD) 3%. The rest is minor. See `label_distribution.tsv`.

## Source-label purity

`ATN` is pure by dissection but mixed by nucleus. F1 falls with resolution
by design, so read the distribution, not the best-F1 target.
