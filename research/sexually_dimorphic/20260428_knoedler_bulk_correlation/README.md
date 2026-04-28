# Knoedler 2022 Esr1+ TRAP-seq → WMBv1 cluster correlation

**Date:** 2026-04-28
**Source dataset:** [Knoedler et al. 2022, *Cell* (PMID:35143761)](https://www.cell.com/cell/fulltext/S0092-8674(21)01494-X) — TRAP-seq of Esr1+ neurons from four mouse brain regions across three sex/state categories. **GEO: GSE183092** — 4 regions (BNST, MeA, POA, VMH) × 3 states (Male, FR = female-receptive, FNR = female-non-receptive) × 3 biological replicates = 36 samples. Processed normalized gene-count CSVs available per region (DESeq2 normalised, gene symbols).
**Atlas substrate:** WMBv1 `precomputed_stats_ABC_revision_230821.h5` (10x reference) — 5,322 clusters × 32,285 Ensembl-keyed genes.
**Genes used after symbol→Ensembl mapping, dedup, and per-region intersection:** 11,997.

---

## Method

Per region, average across the 3 biological replicates within each (region × state) → 12 mean log-expression vectors (BNST_Male, BNST_FR, BNST_FNR, MeA_Male, …, VMH_FNR). For each cluster: Spearman ρ vs each pool. Differential contrasts then probe specific hypotheses:

| Contrast | Tests for |
|---|---|
| POA_FR − VMH_FR | POA-specific Esr1+ neurons (`mpoa_esr1_neuron`) |
| BNST_FR − VMH_FR | BNST-specific Esr1+ neurons (`bnst_crf_neuron` via Esr1 proxy) |
| MeA_FR − VMH_FR | MeA-specific Esr1+ neurons (no current classical node) |
| VMH_FR − MeA_FR | VMHvl-specific Esr1+ neurons (`vmhvl_esr1_pr_neuron`) |
| **VMH_FR − BNST_FR** | VMHvl-specific Esr1+ neurons (alternative; cleaner) |
| POA_Male − POA_FR | Male-biased POA Esr1+ (`sdn_poa_calbindin_neuron` proxy) |
| VMH_Male − VMH_FR | Male-biased VMH Esr1+ (PR+/aggression population) |
| BNST_Male − BNST_FR | Male-biased BNST Esr1+ |

---

## Findings

### 1. `mpoa_esr1_neuron` — multiple preoptic candidates surfaced

Top 10 by δ(POA_FR − VMH_FR) is dominated by preoptic populations, exactly as expected:

| Rank | Cluster | Supertype | Top anatomy | δ |
|---:|---|---|---|---:|
| 1 | CLUS_2085 | SUPT_0521 (AVPV-MEPO-SFO Tbr1 Glut_3) | Anteroventral periventricular nucleus | 0.0151 |
| 2 | CLUS_1528 | SUPT_0418 (PVR Six3 Sox3 Gaba_8) | choroid plexus | 0.0149 |
| 3 | CLUS_2087 | SUPT_0521 | Anteroventral periventricular nucleus | 0.0141 |
| 4 | CLUS_2082 | SUPT_0520 (AVPV-MEPO-SFO Tbr1 Glut_2) | Median preoptic nucleus | 0.0140 |
| 5 | CLUS_1877 | SUPT_0482 (PVpo-VMPO-MPN Hmx2 Gaba_1) | optic chiasm | 0.0140 |

The existing `mpoa_esr1_neuron` mapping points at SUPT_0486 (PVpo-VMPO-MPN Hmx2 Gaba_5). SUPT_0482 (also PVpo-VMPO-MPN Hmx2) appears at rank 5 — same lineage. **However, the top-ranked supertype is SUPT_0521 (AVPV-MEPO-SFO Tbr1 Glut_3, glutamatergic), not the GABAergic SUPT_0486 currently mapped.** This may indicate the classical node should be split: Knoedler's POA dissection includes both AVPV/MePO glutamatergic and PVpo-VMPO-MPN GABAergic Esr1+ populations. Worth re-examining the classical scope.

### 2. `vmhvl_esr1_pr_neuron` — SUPT_0563 confirmed as the missed co-primary target

The existing report flagged SUPT_0563 (VMH Fezf1 Glut_1) as a candidate co-primary mapping target that was not retrieved by the rank-1 DB query, with female-biased child clusters CLUS_2290 (MFR=0.08) and CLUS_2292 (MFR=0.12). The bulk correlation now provides direct support:

Top 10 by δ(VMH_FR − BNST_FR):

| Rank | Cluster | Supertype | MFR | Top anatomy | δ |
|---:|---|---|---:|---|---:|
| 1 | **CLUS_2293** | **SUPT_0563** | NaN | **Ventromedial hypothalamic nucleus** | 0.0180 |
| 2 | **CLUS_2290** | **SUPT_0563** | **0.08** | **Ventromedial hypothalamic nucleus** | 0.0159 |
| 3 | CLUS_2298 | SUPT_0565 (VMH Fezf1 Glut_3) | 1.70 | Tuberal nucleus | 0.0153 |
| 4 | **CLUS_2292** | **SUPT_0563** | **0.12** | **Ventromedial hypothalamic nucleus** | 0.0145 |
| 5 | CLUS_2313 | SUPT_0568 (VMH Nr5a1 Glut_3) | 1.94 | Ventromedial hypothalamic nucleus | 0.0143 |

**SUPT_0563 dominates the top hits with three of its child clusters (2293, 2290, 2292) in the top 4.** The female-biased CLUS_2290/2292 — flagged in the existing report as a concern — are now directly validated as VMHvl Esr1+ targets. This is concrete evidence that the existing single-supertype mapping (SUPT_0564) is incomplete and SUPT_0563 should be added as a co-primary CROSS_CUTTING target. Recommended action: edit `edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564` to be one of two co-primary edges, the other being a new `edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563`.

### 3. `bnst_crf_neuron` (via Esr1 proxy) — SUPT_0358 candidate

Top 10 by δ(BNST_FR − VMH_FR) includes multiple MEA-BST Lhx6 Nfib Gaba_2 clusters (SUPT_0358):

| Rank | Cluster | Supertype | MFR | Top anatomy | δ |
|---:|---|---|---:|---|---:|
| 4 | CLUS_1295 | SUPT_0358 | 0.82 | Medial amygdalar nucleus | 0.0161 |
| 5 | CLUS_1291 | SUPT_0358 | 1.27 | Medial amygdalar nucleus | 0.0160 |
| 9 | **CLUS_1290** | **SUPT_0358** | **2.23** | **Bed nuclei of the stria terminalis** | 0.0156 |
| 10 | CLUS_1293 | SUPT_0358 | **99.00** | Medial amygdalar nucleus | 0.0152 |

CLUS_1290 specifically maps to the BST and has the right population. CLUS_1293 carries an extreme male-biased sex ratio (MFR=99) — a candidate for the male-biased CRF subpopulation. The current `bnst_crf_neuron` edge sits at UNCERTAIN/PARTIAL_OVERLAP; this is an explicit candidate to upgrade. **Caveat: Knoedler sorted on Esr1, not Crh — this is a proxy, not direct CRF evidence.** It identifies the BST GABAergic Esr1+ supertype that *contains* the CRF+ subpopulation; co-localisation requires ISH/MERFISH confirmation.

### 4. MeA Esr1+ — no current classical node

Top 10 by δ(MeA_FR − VMH_FR):

| Rank | Cluster | Supertype | MFR | Top anatomy | δ |
|---:|---|---|---:|---|---:|
| 3 | CLUS_0197 | SUPT_0055 (MEA Slc17a7 Glut_1) | 10.11 | Medial amygdalar nucleus | 0.0519 |
| 5 | CLUS_0214 | SUPT_0057 (MEA Slc17a7 Glut_3) | 2.33 | Medial amygdalar nucleus | 0.0510 |
| 6 | CLUS_0194 | SUPT_0055 | 2.70 | Posterior amygdalar nucleus | 0.0508 |

Strong, anatomically clean signal. There is no classical `mea_esr1_neuron` node in the KB — could be added if literature support warrants. CLUS_0197 has MFR=10.11 (male-biased), consistent with the well-known male-biased MeA Esr1 population.

### 5. Methodological caveat — cross-sex δ is artefactual

The contrasts `POA_Male − POA_FR`, `VMH_Male − VMH_FR`, and `BNST_Male − BNST_FR` all return the *same* top hits — hindbrain motor cholinergic neurons (HB Calcb Chol_2/3/4/5, SUPT_1025–1029). These populations have no anatomical or functional connection to any of the input regions.

This is a TECHNICAL ARTEFACT: there is something about the male TRAP-seq samples (across all regions) that correlates more strongly with hindbrain cholinergic populations than the female samples. Possible causes include sex-chromosome gene dosage (Y-linked gene expression, X-inactivation), batch effects between male and female cohorts, or systematic differences in TRAP pull-down efficiency between sexes.

**Implication:** Cross-sex contrasts within the same region are NOT a usable form of paired-bulk differential for this method. The Stephens-style δ requires paired bulk samples that differ in **cell population** (region, marker), not in **systemic biological state** (sex, age, condition). The `sdn_poa_calbindin_neuron` male-bias question therefore cannot be answered with Knoedler's POA_Male − POA_FR contrast and needs an alternative comparator (e.g. dissection of SDN vs surrounding POA in same-sex samples).

---

## Summary mapping recommendations

| Classical node | Current mapping | Knoedler-supported update |
|---|---|---|
| `mpoa_esr1_neuron` | SUPT_0486 | Add SUPT_0521 (AVPV-MEPO-SFO Tbr1 Glut_3) and SUPT_0518/0520 as co-primary. Existing SUPT_0486 still supported (SUPT_0482 sister appears at rank 5). Consider classical node split (glutamatergic vs GABAergic). |
| `vmhvl_esr1_pr_neuron` | SUPT_0564 | **Add SUPT_0563 as co-primary CROSS_CUTTING target.** CLUS_2290 (MFR=0.08) and CLUS_2292 (MFR=0.12) are the female-biased ERα/lordosis subpopulation directly validated. |
| `bnst_crf_neuron` | UNCERTAIN | Upgrade with SUPT_0358 candidate (especially CLUS_1290 in BST proper, CLUS_1293 male-biased MFR=99). Note Esr1 proxy — co-localisation with Crh requires direct evidence. |
| MeA Esr1+ | not in KB | Candidate new classical node → SUPT_0055 / SUPT_0057. |
| `sdn_poa_calbindin_neuron` | UNCERTAIN | **Method does not work for cross-sex contrast.** Need alternative paired-bulk comparator. |
| `mpoa_esr1_neuron` female-vs-male | n/a | Same artefact issue — cross-sex δ unusable. |

---

## Files

| File | Description |
|---|---|
| `data/GSE183092_*_Normalized_Gene_Counts.csv.gz` | Source data (4 region CSVs from GEO) |
| `correlate.py` | One-off analysis script |
| `all_correlations.tsv` | All clusters × all 12 pool ρ values + 8 δ contrasts |
| `ranked_contrasts/delta_*.tsv` | Per-contrast ranked output (8 files) |

## Recommended next steps

1. **Update `vmhvl_esr1_pr_neuron` mapping in KB** — highest-confidence single change. Add SUPT_0563 co-primary edge.
2. **Survey ARC clusters in the Stephens ARC pool more carefully** — combine with the Stephens 2024 result; the ARC Kiss1 candidate (SUPT_0556 / CLUS_2282) was identified in that run.
3. **Investigate the male-vs-female TRAP-seq technical artefact** before committing the method to general use. Consider whether ranking by δ(within-sex) only is the correct constraint, formalising "cross-sex δ is invalid" as part of the eventual `bulk-atlas-correlate` skill spec.
4. **Hashikawa 2017 (VMHvl medial vs lateral)** — next paired-bulk dataset to ingest for cleaner VMHvl sub-mapping (Cckar+ vs Crhbp+ within the now-validated SUPT_0563/SUPT_0564 split).
