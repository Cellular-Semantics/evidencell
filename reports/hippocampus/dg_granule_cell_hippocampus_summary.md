# Dentate gyrus granule cell — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus granule cell layer [UBERON:0001885] | [1][2][3][4][5] |
| NT type | Glutamatergic | [6][7][8] |
| Defining markers | Prox1, C1ql2 | [9] (Prox1); C1ql2 unsourced |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0137 DG Glut_2 | — | — | 🟡 MODERATE | Glutamatergic; DG granule cell layer location; strong AT F1 (supertype 0.584–0.601; subclass 0.703) | Best candidate |

1 edge total. Relationship type: PARTIAL_OVERLAP.

---

## 0137 DG Glut_2 · 🟡 MODERATE

**Supporting evidence**

- Annotation transfer (MapMyCells local, CCN20230722) of Hochgerner 2018 (GEO:GSE95315) Granule-mature and Granule-immature populations maps both to SUPT_0137 as the primary supertype. Granule-mature: F1=0.584 at supertype level (433/609 cells; group_purity=0.711, target_purity=0.495). Granule-immature: F1=0.601 at supertype level (437/581 cells). Both populations confirm DG Glut subclass (037) with subclass-level group_purity of 0.988 (Granule-mature) and 0.888 (Granule-immature).
- At subclass level, DG Glut (037) achieves F1=0.703 across 716 cells, confirming the DG Glut subclass as the dominant classification for both granule cell populations.
- Atlas metadata: SUPT_0137 has 7,199 cells in Dentate gyrus, granule cell layer (MBA:632), consistent with the classical granule cell soma location. Additional cells in molecular layer (6,636) and polymorph layer (3,067) are consistent with dendritic processes extending into the molecular layer.
- Glutamatergic NT type is CONSISTENT between the classical node and SUPT_0137 (SUBC_037 DG Glut).

**Marker evidence provenance**

- Prox1 (sourced [9]): Protein-level immunostaining study (Sarvari et al. 2016); confirmed as a canonical DG granule cell transcription factor. Prox1 is not listed among SUPT_0137 defining markers (Dsp, Kcnh3, Syndig1); expression may be present but not rank-selected as a defining marker. NOT_ASSESSED — requires precomputed expression cross-check via `add-expression`.
- C1ql2 (unsourced): No reference in facts.reference_index. This marker is flagged as unsourced; targeted cite-traverse is recommended to establish the evidentiary basis before treating it as a defining criterion.

**Concerns**

- SUPT_0137 supertype-level F1 scores (0.584–0.601) indicate only partial overlap: a minority of Hochgerner granule cells map to adjacent DG Glut supertypes (SUPT_0136, SUPT_0138) and to CA3/CA2 clusters. This may reflect genuine DG transcriptomic heterogeneity (e.g. dorsal vs. ventral DG positions) or minor contamination in the source dataset.
- The 1,529 cells of SUPT_0137 assigned to Field CA3 pyramidal layer (MBA:495) are unexpected for a granule cell supertype. These may represent adult-born granule cells in transit, MERFISH registration overlap at CA3c, or mossy fiber terminals.
- The DG Glut subclass (SUBC_037) contains at least four supertypes (SUPT_0136–0139); this edge targets SUPT_0137 as the dominant mature granule cell supertype, but the full classical DG granule cell type may span multiple supertypes — particularly for adult-born immature granule cells that may also map to SUPT_0141 (DG-PIR Ex IMN_2; F1=0.146 for Granule-immature).
- Annotation transfer was performed from rat (Hochgerner 2018) to mouse WMBv1 atlas. Species-level transcriptomic differences in granule cells are unquantified and may affect mapping accuracy.

**What would upgrade confidence**

- Run `add-expression` for Prox1 and C1ql2 on SUPT_0136–0139: if either marker shows differential expression within DG Glut supertypes, this would support or refine the SUPT_0137 assignment.
- Perform annotation transfer from a mouse granule cell dataset (e.g. Artimovich 2020 or Shin 2015) to cross-validate the SUPT_0137 mapping in the same species as WMBv1.

---

## Proposed experiments

**Precomputed expression query**
- What: Run `add-expression` for Prox1 and C1ql2 on SUPT_0136–0139.
- Target: Detect differential expression at supertype level; confirm Prox1 presence in SUPT_0137 cells.
- Expected output: Expression evidence supporting or refuting SUPT_0137 as the dominant Prox1+ granule cell supertype.
- Resolves: marker_Prox1 and marker_C1ql2 NOT_ASSESSED comparisons; ambiguous DG Glut supertype boundaries.

**Cross-species annotation transfer**
- What: MapMyCells annotation transfer using a mouse DG granule cell dataset.
- Target: F1 >= 0.70 at supertype level for SUPT_0137.
- Expected output: AnnotationTransferEvidence in the same species as WMBv1, removing the rat-to-mouse extrapolation caveat.
- Resolves: CROSS_SPECIES_EXTRAPOLATION caveat; confidence upgrade from MODERATE to HIGH if F1 threshold is met.

---

## Open questions

1. Do SUPT_0136, SUPT_0137, and SUPT_0138 correspond to functionally distinct granule cell populations (e.g. adult-born vs. developmentally-born, or dorsal vs. ventral DG)?
2. Are Prox1 and C1ql2 expressed in SUPT_0137 cells? Requires `add-expression` from precomputed stats to resolve.

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_granule_cell_hippocampus_to_supt_0137 | ANNOTATION_TRANSFER (GSE95315, Granule-mature + Granule-immature; F1=0.584/0.601 supertype, 0.703 subclass) | SUPPORT |
| edge_dg_granule_cell_hippocampus_to_supt_0137 | ATLAS_METADATA (7,199 cells in DG granule cell layer MBA:632; consistent location) | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Munster-Wandowski et al. 2013 | [PMID:24319410](https://pubmed.ncbi.nlm.nih.gov/24319410/) | Soma location |
| [2] | Hagihara et al. 2011 | [PMID:21927594](https://pubmed.ncbi.nlm.nih.gov/21927594/) | Soma location |
| [3] | CorpusId:18555666 | — | Soma location |
| [4] | Yau et al. 2015 | [PMID:26380120](https://pubmed.ncbi.nlm.nih.gov/26380120/) | Soma location |
| [5] | DOI:10.1038/s41598-017-11268-z | — | Soma location |
| [6] | Cembrowski et al. 2016 | [PMID:27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Neurotransmitter type |
| [7] | Zander et al. 2010 | [PMID:20519538](https://pubmed.ncbi.nlm.nih.gov/20519538/) | Neurotransmitter type |
| [8] | Pedroni et al. 2014 | [PMID:24592213](https://pubmed.ncbi.nlm.nih.gov/24592213/) | Neurotransmitter type |
| [9] | Sarvari et al. 2016 | [PMID:27375434](https://pubmed.ncbi.nlm.nih.gov/27375434/) | Prox1 marker |
