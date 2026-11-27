# AT Run: Phillips 2019 thalamocortical neurons, all projection systems pooled → WMBv1 (CCN20230722)

Status: scored, manifest written, run registered (`index.yaml`). Declared as
the `at_source_sets` entry of `thalamic_glutamatergic_projection_neuron`
(SUBSET). No mapping edges yet.

Shares `mmc_results.csv` with
`../at_run_20261115_phillips2019_projection_mmc_wmbv1/` (the published-label
run). No new MapMyCells run. That run's README has the full recipe (GEO fetch,
h5ad build, mapping).

## Why this pool

Every cell in GEO:GSE133912 was retrogradely labelled from one of five
cortical areas, then manually dissected and sorted (Phillips et al. 2019,
Methods). Every cell is therefore a thalamocortical projection neuron by
experimental design, whatever its projection system. The pool puts all 1,952
cells under one label, so the umbrella node gets one AT entry. Five per-system
SUBSET entries would each have their purity diluted by the other four systems,
which are also members of the umbrella. No WMBv1 output was used to choose
the pool.

## Reproduction (from the clone root)

```bash
R=kb/annotation_transfer_runs/at_run_20261115_phillips2019_projection_mmc_wmbv1
P=kb/annotation_transfer_runs/at_run_20261127_phillips2019_pooled_mmc_wmbv1
.venv/bin/python -I $P/scripts/build_pooled_labels.py $R/labels_projection.json $P/labels_pooled.json
just at-score ../$R/mmc_results.csv ../$P/labels_pooled.json ../$P/f1_matrix.csv
.venv/bin/python -I $P/scripts/summarise_label_distribution.py \
  $R/mmc_results.csv $P/labels_pooled.json $P/label_distribution.tsv --top 10
uv run python -m evidencell.at_metrics migrate $P
just register-at-run
```

`scripts/summarise_label_distribution.py` is vendored unchanged from
`../at_run_20261115_phillips2019_projection_mmc_wmbv1/scripts/`.

## Results (bootstrap ≥ 0.8)

| Source label | Level | Best WMB target | Coverage | Purity | F1 | Cells |
|---|---|---|---|---|---|---|
| cortex-projecting TC (all 5 systems) | class | 18 TH Glut | 0.991 | 1.00* | 0.996 | 1915 |
| | subclass | 151 TH Prkcd Grin2c Glut | 0.865 | 1.00* | 0.928 | 1573 |
| | supertype | 0659 TH Prkcd Grin2c Glut_6 | 0.220 | 1.00* | 0.360 | 350 |
| | cluster | 2663 TH Prkcd Grin2c Glut_6 | 0.120 | 1.00* | 0.214 | 145 |

\* Purity is 1.0 by construction, because one label covers the whole scored
dataset. Read coverage. The per-supertype and per-cluster spread is in
`label_distribution.tsv`. See the `manifest.yaml` caveats.
