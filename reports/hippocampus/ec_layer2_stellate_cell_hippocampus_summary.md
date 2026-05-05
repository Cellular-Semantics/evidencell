# entorhinal cortex layer II stellate cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | glutamatergic neuron (CL:0000679) | |
| Soma location | entorhinal cortex layer II [UBERON:0001905] | [1][2][3][4][5][6][7] |
| NT | glutamatergic | [4] |
| Defining markers | Reln (reelin) | [1] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] | L2/3 IT PIR-ENTl Glut | — | 🟡 MODERATE | Reln CONSISTENT · F1=0.964 | Best candidate |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP (the classical EC layer II stellate cell is specifically Reln+; SUPT_0042 may include a minor piriform cortex component sharing transcriptomic similarity).

---

## 3. Candidate paragraphs

## 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0042 belongs to subclass SUBC_009 L2/3 IT PIR-ENTl Glut, a glutamatergic subclass grouping lateral entorhinal cortex and piriform cortex layer II/III intratelencephalic (IT) neurons. The classical EC layer II stellate cell is glutamatergic [4], consistent with this subclass identity.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq data onto WMBv1 (CCN20230722): of 180 Yao 2021 'L2 IT ENTl' subclass cells (representing lateral entorhinal cortex layer II IT neurons — the population containing reelin-positive stellate cells as the dominant excitatory type), 172 (95.6%) map to SUPT_0042 at the supertype level. F1 = 0.964, group_purity = 0.956, target_purity = 0.972. This is an exceptionally high F1, indicating SUPT_0042 is a highly specific and sensitive match for lateral EC layer II cells. This is the strongest quantitative evidence for this mapping.

- **Marker Reln — CONSISTENT.** Reln is listed as the defining identity marker of EC layer II stellate cells [1]. Precomputed expression stats (precomputed_stats.h5, supertype level) confirm Reln mean expression = 8.17 in SUPT_0042. Although Reln does not appear among the defining discriminating markers listed for SUPT_0042 in the atlas (Igfn1, Endou, Bcl11b, Boc), the high precomputed Reln expression confirms that stellate cell-level Reln expression is present in this supertype, consistent with stellate cell identity.

- **Location — APPROXIMATE.** The 'PIR-ENTl' subclass designation reflects a shared transcriptomic signature between lateral entorhinal cortex and piriform cortex. EC layer II stellate cells reside specifically in the entorhinal cortex [UBERON:0001905]; piriform cortex layer II neurons share a similar molecular profile but are a distinct population. *(note: piriform cortex and lateral entorhinal cortex are anatomically adjacent — the piriform-entorhinal border is not sharply delineated — which may explain the shared transcriptomic cluster identity; this adjacency makes the location APPROXIMATE rather than DISCORDANT.)*

**Marker evidence provenance**

- **Reln** [1]: Naumann et al. 2015 established that Reln-positive cells in EC layer II have the electrophysiological properties of stellate cells and project to the dentate gyrus, distinguishing them from Calb1-positive pyramidal cells that project to CA1. Cell-type identity in this study was established by electrophysiological characterisation combined with projection tracing (retrograde labelling), providing strong specificity for the stellate cell identity. The evidence is transcript- and protein-level (immunofluorescence). The Reln mean expression of 8.17 in SUPT_0042 from precomputed stats is consistent with the high Reln expression expected for this population. No significant discrepancy exists between the literature and atlas values for Reln. *(Recommendation: Running add-expression for Reln and Calb1 across all SUBC_009 supertypes at the atlas level would directly confirm the stellate/pyramidal marker distinction within the PIR-ENTl subclass.)*

**Concerns**

- **Location APPROXIMATE — piriform cortex component.** The SUBC_009 (L2/3 IT PIR-ENTl Glut) subclass spans both lateral entorhinal cortex and piriform cortex. Any piriform cortex component within SUPT_0042 would represent a different biological population sharing a transcriptomic signature with EC layer II stellate cells rather than being true stellate cells. *(note: lateral entorhinal cortex and piriform cortex are adjacent regions and the PIR-ENTl designation likely reflects transcriptomic clustering rather than equal spatial representation — this is weak counter-evidence, consistent with an adjacent-region boundary effect.)*

- **PARTIAL_OVERLAP caveat — minor non-stellate fraction.** The Yao 2021 'L2 IT ENTl' subclass may include a small fraction of non-stellate (Reln-negative) neurons in lateral EC layer II. Given the extremely high purity (F1=0.964), this contamination is minimal and does not substantially affect the mapping confidence.

**What would upgrade confidence**

- **Reln and Calb1 expression atlas check:** Running add-expression for Reln and Calb1 on CCN20230722 SUBC_009 supertypes would confirm that SUPT_0042 is Reln-high/Calb1-low (stellate) and SUPT_0052 is Reln-low/Calb1-high (pyramidal), directly resolving the stellate/pyramidal distinction at the atlas level (Open question 1). This can be done without new experiments.

- **MERFISH spatial validation:** Checking WMBv1 MERFISH soma assignments for SUPT_0042 cells to quantify the entorhinal vs. piriform cortex spatial distribution would resolve whether the 'PIR' component is a substantial contaminant or a minor transcriptomic artefact (Open question 2).

---

## 4. Proposed experiments

### 1 — Atlas expression query (add-expression)

**What:** Run add-expression for Reln and Calb1 on CCN20230722 precomputed stats across all SUBC_009 (L2/3 IT PIR-ENTl Glut) supertypes.

**Target:** Confirm Reln mean expression significantly higher in SUPT_0042 than in SUPT_0052; Calb1 mean expression significantly higher in SUPT_0052 than in SUPT_0042.

**Expected output:** PrecomputedExpression entries on atlas nodes confirming the molecular distinction between stellate and pyramidal EC layer II supertypes.

**Resolves:** Open question 1 (stellate vs. pyramidal molecular distinction at atlas level).

### 2 — MERFISH / spatial transcriptomics

**What:** Check WMBv1 MERFISH soma assignments for SUPT_0042 cells to quantify entorhinal cortex vs. piriform cortex spatial distribution.

**Target:** Determine whether the majority of SUPT_0042 cells are spatially assigned to lateral entorhinal cortex or piriform cortex in the MERFISH dataset.

**Expected output:** Atlas metadata evidence (ATLAS_METADATA) clarifying whether PARTIAL_OVERLAP should be upgraded to CONSISTENT if the piriform component is negligible.

**Resolves:** Open question 2 (piriform vs. entorhinal spatial contribution to SUPT_0042).

---

## 5. Open questions

1. Does Reln expression in SUPT_0042 match the level expected for stellate cells, and does Calb1 expression distinguish SUPT_0042 (Reln+, stellate) from SUPT_0052 (Calb1+, pyramidal) at the atlas level? Running add-expression for Reln and Calb1 across SUBC_009 supertypes would resolve this.

2. Does SUPT_0042 include a substantial piriform cortex component in the WMBv1 MERFISH data, or does the 'PIR-ENTl' designation primarily reflect transcriptomic similarity rather than equal spatial representation? Checking MERFISH soma assignments for SUPT_0042 would resolve this.

---

## 6. Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ec_layer2_stellate_cell_hippocampus_to_supt_0042 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.964; group_purity=0.956; target_purity=0.972; 95.6% of L2 IT ENTl cells map to SUPT_0042 |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Naumann et al. 2015 · PMID:26223342 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342/) | Soma location; Reln marker |
| [2] | Unknown 2016 · PMID:26711115 | [26711115](https://pubmed.ncbi.nlm.nih.gov/26711115/) | Soma location |
| [3] | Unknown 2010 · PMID:20512133 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133/) | Soma location |
| [4] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | Soma location; NT type |
| [5] | Unknown 2023 · PMID:37219048 | [37219048](https://pubmed.ncbi.nlm.nih.gov/37219048/) | Soma location |
| [6] | Unknown 2018 · PMID:29665671 | [29665671](https://pubmed.ncbi.nlm.nih.gov/29665671/) | Soma location |
| [7] | Unknown 2018 · PMID:30209250 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250/) | Soma location |
