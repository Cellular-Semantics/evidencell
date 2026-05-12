# Yao 2021 SSv4 — re-aggregate AT by Yao **cluster** label

## Goal

Replace / supplement `at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1`
(currently aggregated by Yao **subclass** label) with a sibling run
aggregating by Yao **cluster** label (e.g. `82_Sst`, `98_Sst`,
`362_DG`, …).

## Why

The Yao SSv4 `Sst` subclass label is a biologically mixed bag
containing OLM, bistratified, hippocampo-septal, oriens-oriens,
R-LM, P-LM, and LTH cells. The audit's `at_f1_monotonicity`
diagnostic tags it `falls_with_resolution`: F1 collapses from 0.98
at subclass → 0.23 at cluster, because the source population
fragments. Aggregating per Yao cluster (the level *below* subclass)
gives clean per-Sst-subtype mapping targets — analogous to what
Que 2021 patch-seq cluster labels deliver for BC / BIC / AAC.

See [`planning/at_blind_region_drop_findings_2026-05-12.md`](../at_blind_region_drop_findings_2026-05-12.md)
§§ d, f for the worked motivation.

## Scope

1. Read per-cell Yao SSv4 cluster labels from
   `inputs/datasets/GSE185862_yao2021/metadata_ssv4.csv.gz`
   (column `cluster_label`, e.g. `82_Sst`).
2. Bridge cell IDs: MapMyCells `mmc_output.csv` uses `SM-GE664_…`
   prefixes; Yao metadata uses `US-…` IDs. The two are not directly
   joinable. Likely path: re-extract from the source h5ad with both
   ID schemes, or find an existing crosswalk in the Allen download
   bundle.
3. Compute F1 per `(Yao cluster_label, WMBv1 level, WMBv1 target)`.
4. Write
   `kb/annotation_transfer_runs/at_run_<date>_yao2021_hpf_ssv4_yaoclust_mmc_wmbv1/`
   with manifest + `f1_scores_yao_cluster.csv`.
5. Register in `kb/annotation_transfer_runs/index.yaml`.
6. Write per-Yao-cluster AT-evidence blocks onto the classical
   GABAergic / glutamatergic edges they support.

## Expected outcome (hypothesis)

F1 *rises* with finer aggregation for Sst-subtype-pure Yao
clusters — mirroring Que 2021's BIC pattern. Each Yao cluster
should target a single WMBv1 supertype or cluster cleanly. This
should:

- Convert several Yao Sst subclass-level edges from
  `falls_with_resolution` to `rises_with_resolution` in the audit
  diagnostic.
- Concretely tie classical types (OLM, bistratified, HS, etc.) to
  *named* Yao clusters rather than the Sst-as-a-whole subclass.

## Where the deferred work was paused

The bridge from MMC cell IDs to Yao cluster labels is the blocker.
`inputs/datasets/GSE185862_yao2021/` contains `metadata_ssv4.csv.gz`
(per-cell cluster_label, but using `US-…` sample IDs) and
`hpf_ssv4_mmc.labels.json` (per-cell **subclass** labels keyed by
`SM-GE664_…` IDs). The crosswalk between the two ID schemes lives
in the original Allen h5ad (not in this repo). Pulling the h5ad +
re-extracting both schemes is the first step.

## Tags

`#annotation-transfer` `#yao2021` `#hippocampus` `#deferred-from-phase2-c2`
