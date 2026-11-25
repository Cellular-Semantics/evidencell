# AT Run: Bakken 2021 mouse dLGN / LP / LGv (SMART-seq v4) → WMBv1 (CCN20230722)

Status: outputs complete, manifests written, runs registered (`index.yaml`).
`at_results.yaml` / `at_results_best.yaml` generated with `at_metrics migrate`.
Declared as `at_source_sets` on `dlgn_relay_neuron` and
`dlgn_gabaergic_interneuron`. Neither node has mapping edges yet; pending F1 gate review.

## Purpose

Bakken et al. 2021 (PMID:34473054) give an independent, Allen-curated
transcriptomic label set for mouse dLGN. It is the only dataset in the KB
that reaches the dLGN local interneuron. For the relay neuron it is a second
source alongside Phillips 2019 (`at_run_20261115_phillips2019_*`).

## Data source

- GEO:GSE182211, mouse files only (macaque and human out of scope):
  `GSE182211_mouse_LGN_2021_exon-matrix.csv.gz`,
  `GSE182211_mouse_LGN_2021_intron-matrix.csv.gz` (genes × cells, raw read
  counts) and `GSE182211_mouse_LGN_2021_metadata.csv.gz`.
- 2,187 cells: SMART-seq v4, tdTomato+ FACS from Cre;Ai14 mice, adult males,
  dissections dLGN-core (1,244), dLGN-shell (570), LP (187), LGv (186).
- Counts used: exon + intron reads, the paper's own quantification.
- Not in WMBv1 training. WMBv1 is 10x only (10xv2, 10xv3, Multiome).

## Three label schemes, one mapping

| Run | Labels | File | Declared on node |
|---|---|---|---|
| this run | published `cluster_label` (15 clusters) | `labels_cluster.json` | `dlgn_relay_neuron` ← `LGd` |
| `at_run_20261117_bakken2021_lgn_dlgnin_mmc_wmbv1` | Chrna1+2+3 pooled vs other | `../at_run_20261117_bakken2021_lgn_dlgnin_mmc_wmbv1/labels_dlgnin.json` | `dlgn_gabaergic_interneuron` ← `dLGN GABA (Chrna1-3)` |
| `at_run_20261117_bakken2021_lgn_coreshell_mmc_wmbv1` | LGd split by dissection ROI | `../at_run_20261117_bakken2021_lgn_coreshell_mmc_wmbv1/labels_coreshell.json` | none (analysis only) |

All three score this record's `mmc_results.csv`.

## Reproduction (from the clone root)

```bash
# 1. fetch GEO files (gitignored location)
D=annotation_transfer/data/bakken2021_lgn; mkdir -p $D
for f in exon-matrix.csv.gz intron-matrix.csv.gz metadata.csv.gz readme.txt; do
  curl -sSL -o $D/GSE182211_mouse_LGN_2021_$f \
    https://ftp.ncbi.nlm.nih.gov/geo/series/GSE182nnn/GSE182211/suppl/GSE182211_mouse_LGN_2021_$f; done

# 2. build h5ad (exon+intron, drop Low Quality, symbols -> Ensembl) + 3 label JSONs
R=kb/annotation_transfer_runs/at_run_20261117_bakken2021_lgn_cluster_mmc_wmbv1
S=kb/annotation_transfer_runs/at_run_20261117_bakken2021_lgn_coreshell_mmc_wmbv1
P=kb/annotation_transfer_runs/at_run_20261117_bakken2021_lgn_dlgnin_mmc_wmbv1
(cd annotation_transfer && uv sync --extra mapper && uv pip install setuptools)
annotation_transfer/.venv/bin/python -I $R/scripts/build_bakken2021_h5ad.py \
  $D conf/gene_mapping_CCN20230722.tsv $R
mv $R/labels_coreshell.json $S/; mv $R/labels_dlgnin.json $P/

# 3. preflight + local MapMyCells (cell_type_mapper 1.7.5)
just at-preflight ../$D/bakken2021_lgn_mouse_mmc.h5ad
cd annotation_transfer && uv run --no-sync annotation-transfer map-local \
  data/bakken2021_lgn/bakken2021_lgn_mouse_mmc.h5ad \
  ../conf/mapmycells/CCN20230722/precomputed_stats_ABC_revision_230821.h5 \
  ../conf/mapmycells/CCN20230722/mouse_markers_230821.json \
  data/bakken2021_lgn/mmc/mmc_extended.json \
  --csv data/bakken2021_lgn/mmc/mmc_results.csv && cd ..
cp $D/mmc/mmc_results.csv $R/

# 4. score (bootstrap threshold 0.8), all three schemes
just at-score ../$R/mmc_results.csv ../$R/labels_cluster.json ../$R/f1_matrix.csv
just at-score ../$R/mmc_results.csv ../$S/labels_coreshell.json ../$S/f1_matrix.csv
just at-score ../$R/mmc_results.csv ../$P/labels_dlgnin.json ../$P/f1_matrix.csv

# 5. per-label distribution with WMBv1 MERFISH nucleus annotation
for X in "$R labels_cluster" "$S labels_coreshell" "$P labels_dlgnin"; do set -- $X
  .venv/bin/python -I $R/scripts/summarise_label_distribution.py \
    $R/mmc_results.csv $1/$2.json $1/label_distribution.tsv --top 4; done

# 6. schema-compliant result sets + registry
uv run python -m evidencell.at_metrics migrate-all
just register-at-run
```

`scripts/summarise_label_distribution.py` is vendored unchanged from
`at_run_20261115_phillips2019_projection_mmc_wmbv1/scripts/`.

## Headline results (bootstrap ≥ 0.8)

| Source label | Best WMB target | Level | F1 | Purity | Cells |
|---|---|---|---|---|---|
| LGd | 2650 TH Prkcd Grin2c Glut_2 | cluster | 0.998 | 1.00 | 961/1012 |
| dLGN GABA (Chrna1-3) | 213 SCsg Gabrr2 Gaba | subclass | 0.999 | 0.998 | 452/452 |
| dLGN GABA (Chrna1-3) | 0872 SCsg Gabrr2 Gaba_1 | supertype | 0.998 | 0.998 | 443/452 |
| GABA1 (RT) | 093 RT-ZI Gnb3 Gaba / 0435 | subclass/supertype | 1.00 | 1.00 | 54/54 |
| LP | 0659 TH Prkcd Grin2c Glut_6 | supertype | 0.74 | 0.99 | 99/193 |
| LGd core / LGd shell | 2650 (both) | cluster | n/a | — | 97.2% / 99.7% of label |

See the manifests' `caveats` for how to read these numbers.
