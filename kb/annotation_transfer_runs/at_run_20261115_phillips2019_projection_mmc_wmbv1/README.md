# AT Run: Phillips 2019 thalamic projection neurons → WMBv1 (CCN20230722)

Status: outputs complete, manifest written, run registered (`index.yaml`).
`at_results.yaml` / `at_results_best.yaml` generated with `at_metrics migrate`.
Not yet attached to any KB node (pending F1 gate review).

## Purpose

Link WMBv1 thalamic clusters to cortical **projection target**. Phillips et al.
2019 (PMID:31527803) retrogradely labelled thalamic neurons from five cortical
areas, microdissected the labelled complex and sequenced single sorted cells.
Each cell's projection system is set by anatomy, not by transcriptome.

## Data source

- GEO:GSE133912: `GSE133912_thal_singlecell_counts.csv.gz` (cells x gene
  symbols, UMI), `GSE133912_thal_singlecell_metadata.csv.gz`
- Authors' analysis code: https://github.com/aschulmann/ThalamoSeq
  (`thal_singlecell.Rmd`). Its object names suggest the dissected complexes:
  VAL (motor), VBPO (somatosensory), LGLP (visual), MGB (auditory) and MD
  (prefrontal).
- The nuclei dissected per system are **not recorded** in the metadata or in
  Supp. Table 3, which gives injection coordinates only. The composition above
  is inferred, and it is incomplete for Visual: about 20% of Visual cells map
  to LD-dominant WMB supertype 0658 / cluster 2655.

## Two label schemes, one mapping

| Run | Labels | File |
|---|---|---|
| this run | `Projection` (5 systems) | `labels_projection.json` |
| `at_run_20261115_phillips2019_syscluster_mmc_wmbv1` | `cluster` (17 per-system clusters, Fig. 6) | `../at_run_20261115_phillips2019_syscluster_mmc_wmbv1/labels_syscluster.json` |

Both score the same `mmc_results.csv`.

## Reproduction (from the clone root)

```bash
# 1. fetch GEO files
D=annotation_transfer/inputs/datasets/phillips2019_thalamus; mkdir -p $D
for f in GSE133912_thal_singlecell_counts.csv.gz GSE133912_thal_singlecell_metadata.csv.gz; do
  curl -sSL -o $D/$f https://ftp.ncbi.nlm.nih.gov/geo/series/GSE133nnn/GSE133912/suppl/$f; done

# 2. build h5ad (drop 20 is_ODC cells, symbols -> Ensembl) + label JSONs
R=kb/annotation_transfer_runs/at_run_20261115_phillips2019_projection_mmc_wmbv1
annotation_transfer/.venv/bin/python -I $R/scripts/build_phillips2019_h5ad.py \
  $D conf/gene_mapping_CCN20230722.tsv $R
mv $R/labels_syscluster.json kb/annotation_transfer_runs/at_run_20261115_phillips2019_syscluster_mmc_wmbv1/

# 3. preflight + local MapMyCells (cell_type_mapper 1.7.5; `uv sync --extra mapper`
#    in annotation_transfer/, plus `uv pip install setuptools` on Python 3.13)
just at-preflight ../$D/phillips2019_thalamus_mmc.h5ad
cd annotation_transfer && uv run --no-sync annotation-transfer map-local \
  inputs/datasets/phillips2019_thalamus/phillips2019_thalamus_mmc.h5ad \
  ../conf/mapmycells/CCN20230722/precomputed_stats_ABC_revision_230821.h5 \
  ../conf/mapmycells/CCN20230722/mouse_markers_230821.json \
  inputs/datasets/phillips2019_thalamus/mmc/mmc_extended.json \
  --csv inputs/datasets/phillips2019_thalamus/mmc/mmc_results.csv && cd ..
cp $D/mmc/mmc_results.csv $R/

# 4. score (bootstrap threshold 0.8), both schemes
S=kb/annotation_transfer_runs/at_run_20261115_phillips2019_syscluster_mmc_wmbv1
just at-score ../$R/mmc_results.csv ../$R/labels_projection.json ../$R/f1_matrix.csv
just at-score ../$R/mmc_results.csv ../$S/labels_syscluster.json ../$S/f1_matrix.csv

# 5. per-label distribution with WMBv1 MERFISH nucleus annotation
.venv/bin/python -I $R/scripts/summarise_label_distribution.py \
  $R/mmc_results.csv $R/labels_projection.json $R/label_distribution.tsv --top 6
.venv/bin/python -I $R/scripts/summarise_label_distribution.py \
  $R/mmc_results.csv $S/labels_syscluster.json $S/label_distribution.tsv --top 4
```

## Source-label purity

- Projection labels are pure by anatomy but mixed by nucleus (each complex
  spans 2+ nuclei) and by profile. F1 peaks at supertype (0.42–0.62) and falls
  at cluster. Read `label_distribution.tsv`.
- Per-system clusters are pure (one projection × one transcriptomic cluster).
  F1 mostly rises with resolution (Vis_1 0.12 → 0.69 → 0.77).
