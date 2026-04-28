# Stephens 2024 Kiss1 RP3V vs ARC → WMBv1 correlation

Run id: `corr_run_20260428_stephens_kiss1_wmbv1` ([manifest.yaml](manifest.yaml))
Dataset: `dataset_PMID_37934722` ([kb/datasets/PMID_37934722_stephens_2024.yaml](../../datasets/PMID_37934722_stephens_2024.yaml))

## Headline

Top RP3V-specific cluster across 5,322 candidates is **CLUS_1915** (parent SUPT_0486; primary soma Hypothalamus; MFR 0.02). This is the cluster the existing `avpv_kiss1_neuron` mapping was placed on — δ rank #1 confirms it.

Top ARC-specific cluster is **CLUS_2282** (parent SUPT_0556 ARH-PVp Tbx3 Glut_3; primary soma Arcuate hypothalamic nucleus; MFR 0.11). Sister cluster CLUS_2281 (same supertype) has MFR 32.33 — the female/male-biased sister-cluster pair within SUPT_0556 mirrors the SUPT_0486 pattern at AVPV. Candidate WMBv1 home for an ARC Kiss1 / KNDy classical mapping not yet in the KB.

## Method note

Raw Spearman ρ against single-cell pseudobulks is dominated by housekeeping background (top hits are non-hypothalamic at ρ ≈ 0.45–0.52). The differential δ = ρ_RP3V − ρ_ARC removes that background and is the discriminative statistic. **Paired-bulk inputs are required** — single-bulk-vs-atlas correlation is not informative without an explicit comparator.

## Reproduce

```
python kb/correlation_runs/20260428_stephens_kiss1_wmbv1/correlate.py
```

Outputs (in this directory):

- `all_correlations.tsv` — every cluster × every pool ρ + every contrast δ
- `correlations_rp3v.tsv`, `correlations_arc.tsv` — ranked by raw ρ
- `delta_rp3v_specific.tsv`, `delta_arc_specific.tsv` — ranked by δ (the discriminative metric)

Inputs are at `bulk_supp_table.csv` (in this directory) and `conf/mapmycells/CCN20230722/precomputed_stats.h5` (project-relative). Checksums in [manifest.yaml](manifest.yaml).
