# Kiss1 RP3V vs ARC bulk RNA-seq → WMBv1 cluster correlation

**Date:** 2026-04-28
**Source dataset:** [Stephens et al. 2024, *Reproduction* 167(1)](https://pubmed.ncbi.nlm.nih.gov/37934722/) — bulk RNA-seq of FACS-sorted Kiss1 neurons from rostral periventricular (RP3V) and arcuate (ARC) hypothalamic populations in adult female mice. Pools of 10–15 cells per region.
**Input:** Supplementary Table 3 (`bulk_supp_table.csv`) — log2-scale normalised expression for 4,725 genes (4,703 unique Ensembl IDs after dedup) × 2 columns (RP3V, ARC).
**Atlas substrate:** WMBv1 `precomputed_stats_ABC_revision_230821.h5` — 5,322 clusters × 32,285 Ensembl-keyed genes (10x reference).
**Genes used after intersection:** 4,536.

---

## Method

For each cluster:
- Compute mean log-expression per gene as `log1p(sum / n_cells)`
- Restrict to the 4,536 genes shared between the bulk supp table and atlas
- Compute Spearman ρ vs (a) the RP3V bulk vector, (b) the ARC bulk vector
- Record the differential `δ_RP3V = ρ_RP3V − ρ_ARC` (positive → cluster looks more like RP3V than ARC)

Spearman handles the bulk-vs-pseudobulk normalisation mismatch automatically.

## Headline finding

**Absolute ρ ranking is dominated by housekeeping background.** Top hits by raw `ρ_RP3V` and `ρ_ARC` are non-hypothalamic clusters (PRNc Otp, Vip Gaba, NTS Dbh, COP NN) at ρ ≈ 0.45–0.52 — these populations share a large common transcriptome with any pool of differentiated neurons.

**The differential `δ_RP3V` ranking is highly informative.** Every one of the top 20 RP3V-specific clusters is a hypothalamic preoptic / periventricular GABAergic population — exactly the biology Stephens et al. profile.

### Top 5 RP3V-specific (δ_RP3V_minus_arc, descending)

| Rank | Cluster | Label | Supertype | MFR | Top anatomy | δ |
|---:|---|---|---|---:|---|---:|
| 1 | **CLUS_1915** | 1915 PVpo-VMPO-MPN Hmx2 Gaba_5 | **SUPT_0486** | **0.02** | Hypothalamus | 0.0899 |
| 2 | CLUS_1527 | 1527 PVR Six3 Sox3 Gaba_8 | SUPT_0418 | 1.56 | Median preoptic nucleus | 0.0867 |
| 3 | CLUS_1904 | 1904 PVpo-VMPO-MPN Hmx2 Gaba_3 | SUPT_0484 | 1.50 | Hypothalamus | 0.0849 |
| 4 | CLUS_1939 | 1939 DMH Hmx2 Gaba_3 | SUPT_0489 | 4.56 | Dorsomedial nucleus of hypothalamus | 0.0848 |
| 5 | CLUS_1912 | 1912 PVpo-VMPO-MPN Hmx2 Gaba_5 | SUPT_0486 | 1.22 | Hypothalamus | 0.0839 |

**CLUS_1915** — the cluster the existing `avpv_kiss1_neuron` mapping was placed on — ranks **#1 of 5,322** by RP3V-specificity. MFR=0.02 (extremely female-biased) is independently consistent. Multiple sister clusters of SUPT_0486 (1912, 1913, 1914) appear in the top 20.

### Top 5 ARC-specific (δ_ARC_minus_rp3v, descending)

| Rank | Cluster | Label | Supertype | MFR | Top anatomy | δ |
|---:|---|---|---|---:|---|---:|
| 1 | **CLUS_2282** | 2282 ARH-PVp Tbx3 Glut_3 | **SUPT_0556** | **0.11** | **Arcuate hypothalamic nucleus** | 0.0105 |

The single ARC-specific top hit is in the arcuate nucleus, with female-biased MFR. Its sister cluster CLUS_2281 (same supertype SUPT_0556) has MFR=32.33 — strongly male-biased. This pair pattern (one female-biased, one male-biased child cluster of the same supertype) mirrors what we see in the AVPV Kiss1 SUPT_0486 set, suggesting SUPT_0556 may be the WMBv1 home of the ARC Kiss1 / Kiss1-Tac2 sexually dimorphic population.

## Interpretation

1. **The bulk-correlation method works for atlas mapping refinement** — but only via the differential statistic, not absolute ρ. Raw correlation against single-cell pseudobulks is dominated by shared transcriptome and is not discriminative.

2. **AVPV/PeN Kiss1 → CLUS_1915 / SUPT_0486 mapping is now strongly supported by independent quantitative evidence** beyond the atlas marker metadata. Three independent signals converge:
   - Marker expression (Kiss1=2.51, Th=6.6, Esr1=9.55) — atlas precomputed stats
   - Sex bias (MFR=0.02) — atlas metadata
   - Cross-dataset bulk transcriptome correlation (rank #1 by δ_RP3V) — *new*

3. **ARC Kiss1 mapping points at SUPT_0556 (CLUS_2282/2281)** — a candidate that was not surfaced by the existing `find-candidates` workflow because the classical ARC Kiss1 node was not part of the sexually_dimorphic pilot. This is a concrete next mapping target.

4. **Caveats.**
   - Pools of 10–15 cells produce noisy bulk vectors; ρ values in the 0.3–0.5 range are expected even for true matches and should not be interpreted on their own.
   - The "Log2>7" filter on the supp table biases the gene set toward moderately expressed genes. This is fine for cell-type discrimination but means we have no signal from low-expression but discriminative TFs.
   - The differential statistic only works when you have at least two paired bulk samples covering different cell types in similar tissue context. Single-bulk-vs-atlas correlation would not be informative without an explicit "background" comparator.

## Files

| File | Description |
|---|---|
| `bulk_supp_table.csv` | Source data (Reproduction 167(1) supp table 3) |
| `correlate.py` | One-off analysis script |
| `correlations_rp3v.tsv` | All 5,322 clusters ranked by ρ vs RP3V |
| `correlations_arc.tsv` | All 5,322 clusters ranked by ρ vs ARC |
| `delta_rp3v_specific.tsv` | All 5,322 clusters ranked by δ_RP3V (RP3V-specific signal) |
| `delta_arc_specific.tsv` | All 5,322 clusters ranked by δ_ARC (ARC-specific signal) |

## Recommended follow-ups

- **Update `avpv_kiss1_neuron` edge to MODERATE→HIGH** with `BulkCorrelationEvidence(target=CLUS_1915, source=PMID:37934722, spearman_rho=0.388, delta_vs_paired_pool=0.090, rank_by_delta=1)` once the schema supports it.
- **Add ARC Kiss1 classical node** if not already present in the KB; map to SUPT_0556 with bulk-correlation evidence pointing at CLUS_2282 (and male-biased sister CLUS_2281 separately).
- **Promote bulk-correlation to a generic skill** — see `planning/dev_requests/2026-04-28_kiss1-bulk-atlas-correlation.md`. The differential pattern (paired bulk samples → δ ranking) should be the recommended approach in the skill, not raw absolute correlation.
- **Also consider:** any classical type with a published paired bulk RNA-seq dataset (e.g. ESR1+ vs ESR1− MPOA, PR+ vs PR− VMHvl, Crh+ vs Crh− BNST) is a candidate for the same treatment.
