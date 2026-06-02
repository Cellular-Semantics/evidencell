# BLA glutamatergic principal neuron — CCN20230722 Mapping Report

## Introduction

Glutamatergic principal neurons are the dominant cell class of the basolateral amygdala (BLA), comprising approximately 70–85% of all neurons in this region [1][3][4][5][6]. They are pyramidal-like excitatory projection neurons — cortical in character, spiny in morphology, and classified by NT type as glutamatergic — that mediate BLA output to cortical and subcortical targets.

---

## Classical node

| Field | Value |
|---|---|
| **Node ID** | `bla_glutamatergic_principal_neuron` |
| **Name** | Basolateral amygdala glutamatergic principal neuron |
| **Definition basis** | CLASSICAL |
| **CL mapping** | CL:0000598 — BROAD (auto-proposed; requires expert review) |
| **Proposed CL term** | None |
| **Neurotransmitter** | Glutamatergic [1][5][6] |
| **Defining markers** | SLC17A7 (VGluT1) [7][8][9]; CAMK2A [7][8] |
| **Negative markers** | None recorded |
| **Soma location** | UBERON:0002887 basolateral amygdala [1][2][3][4] |
| **Notes** | Heterogeneity in dendritic field extent (small vs large neurons); also referred to as pyramidal, spiny, or class I neurons. |

---

## Mapping results

### Edge: `edge_bla_glutamatergic_principal_neuron_to_cs20230722_supt_0005`

**Atlas target:** CS20230722_SUPT_0005 — "0005 IT EP-CLA Glut_3" (n = 798 cells)
**Relationship:** skos:broadMatch | **Cardinality:** 1:n

#### Evidence

| Evidence type | Direction | Summary |
|---|---|---|
| ATLAS_METADATA | SUPPORT | MERFISH (Zhuang 2023) places SUPT_0005 cells in BLA (MBA:295; 33 cells) and BLA-anterior (MBA:303; 31 cells), confirming atlas-level evidence of cells in BLA territory. Glut subclass consistent with classical BLA principal neuron. |
| ATLAS_METADATA | AGAINST | SUPT_0005 region_fraction in the BLA discovery cohort is only 0.042 (rank 1 in a cohort of 5). Three LA-BLA-BMA-PA supertypes have region_fractions 0.40–0.71 — an order of magnitude higher — and were not captured by this rank-1 discovery. SUPT_0005 represents a minor BLA component and does not cover the full BLA glutamatergic principal neuron population. |

#### Property comparisons

| Property | Classical node (A) | Atlas supertype (B) | Alignment |
|---|---|---|---|
| **NT type** | Glutamatergic | Glut (IT EP-CLA Glut subclass; IT-ET Glut class) | CONSISTENT |
| **Soma location** | UBERON:0002887 basolateral amygdala | MBA:295 BLA: 33 cells (0.08) Zhuang 2023; 3 cells (0.006) Yao 2024. Dominant regions: Cortical subplate MBA:703 (~55%), Olfactory areas MBA:698 (~39%) | APPROXIMATE |
| **SLC17A7 (VGluT1)** | Defining marker | Not in SUPT_0005 defining set (Abca8a, Npsr1, Adam33, Gpx3); expected as pan-Glut marker | NOT_ASSESSED |
| **CAMK2A** | Defining marker | Not in SUPT_0005 defining set; consistent with IT EP-CLA lineage but unconfirmable without expression data | NOT_ASSESSED |

#### Caveats

**SUPERTYPE_SCOPE_MISMATCH.** SUPT_0005 (IT EP-CLA Glut_3) is named for isocortex/endopiriform/claustrum cells. BLA represents only ~4–8% of its cells. Three LA-BLA-BMA-PA Glut supertypes (SUBT_0063/0064/0065) with region_fractions 0.40–0.71 were not captured by the rank-1 discovery run and should be assessed as the primary BLA candidates.

**MERFISH_COVERAGE_DISCREPANCY.** Two MERFISH datasets give markedly different BLA (MBA:295) cell counts for SUPT_0005: 33 cells (region_fraction 0.08) in Zhuang 2023 versus 3 cells (region_fraction 0.006) in Yao 2024. This ~13-fold discrepancy reduces confidence in the BLA assignment.

---

## Verdict

| | |
|---|---|
| **Confidence** | LOW |
| **Confidence score** | 0.25 |
| **Relationship** | skos:broadMatch |

**Rationale.** NT type is CONSISTENT (Glut). Soma location is APPROXIMATE: BLA cells are confirmed in SUPT_0005 by MERFISH, but they constitute only 4–8% of this supertype (or as few as 0.6% by the Yao 2024 dataset); the dominant transcriptomic territory is cortical subplate and olfactory areas. The MERFISH discrepancy between datasets (33 vs 3 BLA cells) further undermines confidence. Defining markers SLC17A7 and CAMK2A are NOT_ASSESSED for SUPT_0005. Three LA-BLA-BMA-PA Glut supertypes (SUBT_0063/SUBT_0064/SUBT_0065) with region_fractions 0.40–0.71 represent the likely primary transcriptomic correlates of classical BLA glutamatergic principal neurons and require direct hypothesis-mode assessment before a higher-confidence mapping can be proposed.

---

## Discussion

The rank-1 discovery output for `bla_glutamatergic_principal_neuron` returned SUPT_0005 (IT EP-CLA Glut_3) as the top-scoring candidate using a BLA region filter (MBA:295) and Glutamatergic NT type. Atlas metadata confirm that SUPT_0005 does contain BLA cells, and its Glut identity is fully consistent with the classical definition. However, the supertype name itself signals the mismatch: "IT EP-CLA" denotes an isocortex/endopiriform/claustrum lineage, and BLA territory accounts for under one-tenth of its transcriptomic footprint.

The three LA-BLA-BMA-PA supertypes that did not appear in the top-5 rank-1 cohort are distinguished by region_fractions of 0.40–0.71 within BLA-adjacent regions — values that indicate genuine anatomical specificity for the lateral/basal amygdala nuclei. These candidates were filtered out of the rank-1 discovery pass because the region query was applied strictly to MBA:295 (BLA), while LA-BLA-BMA-PA supertypes may have their highest representation assigned to adjacent region codes (e.g. MBA:303 BLA-anterior, LA, BA). A follow-up **hypothesis-mode** `map-cell-type` run targeting SUBT_0063, SUBT_0064, and SUBT_0065 directly is the recommended next step.

Additionally, obtaining precomputed expression data and querying SLC17A7 and CAMK2A across all BLA Glut supertypes would allow the marker NOT_ASSESSED gaps to be resolved, which could substantially alter the confidence level of any final mapping edge.

The broadMatch relationship to SUPT_0005 is retained as a valid partial observation — SUPT_0005 likely captures a genuine EP/claustrum-homologous subpopulation within the BLA — but it is not a satisfactory representation of the full glutamatergic principal neuron class.

---

## References

| Label | Citation | PMID | DOI | Used for |
|---|---|---|---|---|
| [1] | Veinante et al. 2013 | 25408902 | 10.1186/2049-9256-1-9 | Soma location |
| [2] | Raudales et al. 2024 | 39012795 | 10.7554/eLife.93481 | Soma location |
| [3] | Nolan et al. 2020 | 33015518 | 10.1177/2470547020944553 | Soma location |
| [4] | Zhu et al. 2025 | 40352758 | 10.3389/fncir.2025.1575232 | Soma location |
| [5] | Ignacio et al. 2014 | 25309888 | 10.3389/fped.2014.00103 | Neurotransmitter type |
| [6] | Polepalli et al. 2020 | 32802405 | 10.1038/s41539-020-0071-z | Neurotransmitter type |
| [7] | Hájos 2021 | 34177472 | 10.3389/fncir.2021.687257 | SLC17A7 marker |
| [8] | Wilson et al. 2015 | 26844236 | 10.1016/j.ynstr.2015.06.001 | SLC17A7 marker |
| [9] | Fernández et al. 2025 | 40867603 | 10.3390/biom15081160 | SLC17A7 marker |

Atlas metadata source: PMID:37915112 (Zhuang 2023 MERFISH; Yao 2024)
