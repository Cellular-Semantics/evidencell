# Dentate gyrus granule cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | dentate gyrus granule cell layer [UBERON:0001885] | [1] [2] [3] [4] |
| NT | glutamatergic | [5] [6] [7] |
| Markers | Prox1+, C1ql2+ | [8] [9] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0137 DG Glut_2 [CS20230722_SUPT_0137] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0137 DG Glut_2 · 🟡 MODERATE

**Supporting evidence:**

- MapMyCells local annotation transfer of Hochgerner 2018 (GSE95315) mouse hippocampus scRNA-seq Granule-mature and Granule-immature labels onto WMBv1 (CCN20230722). Both mature and immature granule cell populations map primarily to SUPT_0137 (0137 DG Glut_2) at the supertype level. F1 scores of 0.584 (Granule-mature, 433/609 cells) and 0.601 (Granule-immature, 437/581 cells) indicate robust but partial overlap; a minority of granule cells map to adjacent DG Glut supertypes (SUPT_0136, SUPT_0138) and to CA3/CA2 clusters, suggesting either genuine DG transcriptomic heterogeneity or minor contamination. At subclass level, group_purity for DG Glut subclass (037) is 0.988 (Granule-mature) and 0.888 (Granule-immature), confirming DG Glut as the dominant classification. [Annotation transfer]
- SUPT_0137 has 7199 cells in Dentate gyrus, granule cell layer (MBA:632), 6636 in molecular layer, and 3067 in polymorph layer — consistent with DG granule cell soma location. Defining markers Dsp, Kcnh3, Syndig1 have not been compared against classical granule cell transcriptomics (require precomputed expression cross-check). [Atlas metadata]

**Concerns:**

- DG Glut subclass (SUBC_037) in WMBv1 contains at least four supertypes (SUPT_0136-0139). Hochgerner Granule-mature and Granule-immature both map predominantly to SUPT_0137 (F1 ~0.59-0.60), suggesting SUPT_0137 is the dominant mature granule cell supertype. However, adult-born immature granule cells may also map to SUPT_0141 (DG-PIR Ex IMN_2; F1=0.146 for Granule-immature). The classical DG granule cell type as described here spans both mature and immature populations.
- Annotation transfer from rat (Hochgerner 2018) to mouse WMBv1 atlas; species-level differences in granule cell transcriptomics are unquantified.

**What would upgrade confidence:**

- *Unresolved:* Do SUPT_0136, SUPT_0137, SUPT_0138 correspond to functionally distinct granule cell populations (e.g. adult-born vs. developmentally-born, or dorsal vs. ventral DG)?

- *Unresolved:* Are Prox1 and C1ql2 expressed in SUPT_0137 cells? Requires add-expression from precomputed stats to resolve.

- *Proposed:* Run add-expression for Prox1 and C1ql2 on SUPT_0136-0139 to assess granule cell marker expression across the DG Glut supertypes.

- *Proposed:* Perform annotation transfer from a mouse granule cell dataset (e.g. Artimovich 2020 or Shin 2015) to cross-validate the SUPT_0137 mapping in the same species as WMBv1.


---

## Proposed experiments

### 1 — Other

- Run add-expression for Prox1 and C1ql2 on SUPT_0136-0139 to assess granule cell marker expression across the DG Glut supertypes.
- Perform annotation transfer from a mouse granule cell dataset (e.g. Artimovich 2020 or Shin 2015) to cross-validate the SUPT_0137 mapping in the same species as WMBv1.
*Resolves: edge_dg_granule_cell_hippocampus_to_supt_0137*

---

## Open questions

1. Do SUPT_0136, SUPT_0137, SUPT_0138 correspond to functionally distinct granule cell populations (e.g. adult-born vs. developmentally-born, or dorsal vs. ventral DG)?
2. Are Prox1 and C1ql2 expressed in SUPT_0137 cells? Requires add-expression from precomputed stats to resolve.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_dg_granule_cell_hippocampus_to_supt_0137 | Annotation transfer | SUPPORT |
| edge_dg_granule_cell_hippocampus_to_supt_0137 | Atlas metadata | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Munster-Wandowski et al. 2013 · PMID:24319410 | [24319410](https://pubmed.ncbi.nlm.nih.gov/24319410/) | soma location |
| [2] | Hagihara et al. 2011 · PMID:21927594 | [21927594](https://pubmed.ncbi.nlm.nih.gov/21927594/) | soma location |
| [3] | Yau et al. 2015 · PMID:26380120 | [26380120](https://pubmed.ncbi.nlm.nih.gov/26380120/) | soma location |
| [4] | https://doi.org/10.1038/s41598-017-11268-z | — | soma location |
| [5] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | neurotransmitter type |
| [6] | Zander et al. 2010 · PMID:20519538 | [20519538](https://pubmed.ncbi.nlm.nih.gov/20519538/) | neurotransmitter type |
| [7] | Pedroni et al. 2014 · PMID:24592213 | [24592213](https://pubmed.ncbi.nlm.nih.gov/24592213/) | neurotransmitter type |
| [8] | Sarvari et al. 2016 · PMID:27375434 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434/) | Prox1 marker |
| [9] | D et al. 2018 · PMID:29674952 | [29674952](https://pubmed.ncbi.nlm.nih.gov/29674952/) | C1ql2 marker |
