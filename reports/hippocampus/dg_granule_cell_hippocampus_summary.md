# Dentate gyrus granule cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus granule cell layer [UBERON:0001885] | [1][2][3][4] |
| NT | Glutamatergic | [5][6][7] |
| Defining markers | Prox1, C1ql2 | Prox1: [8]; C1ql2: [9] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0137 DG Glut_2 [CS20230722_SUPT_0137] | DG Glut | 7199 (DG granule cell layer, MBA:632) | 🟡 MODERATE | Location CONSISTENT · NT CONSISTENT · Prox1 mean=8.59, C1ql2 mean=5.77 | Best candidate |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP.

---

## 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0137 belongs to subclass CS20230722_SUBC_037 (037 DG Glut), the dedicated dentate gyrus glutamatergic subclass in WMBv1. The classical DG granule cell is glutamatergic [5][6][7], and SUBC_037 is exclusively glutamatergic.

- **Soma location — CONSISTENT.** SUPT_0137 has 7199 cells in Dentate gyrus, granule cell layer (MBA:632), consistent with the classical DG granule cell soma location [UBERON:0001885] [1][2][3][4]. The molecular layer (6636 cells) and polymorph layer (3067 cells) likely reflect dendritic processes of granule cells extending into the molecular layer, or immature granule cells with broader distribution. A small representation in Field CA3, pyramidal layer (MBA:495; 1529 cells) may represent adult-born granule cells in transit or MERFISH registration overlap at CA3c.

- **Marker Prox1 — CONSISTENT.** Prox1 is listed as a defining marker of the DG granule cell [8]. Although Prox1 does not appear among SUPT_0137's atlas defining markers (Dsp, Kcnh3, Syndig1), precomputed expression stats (precomputed_stats.h5, supertype level) confirm Prox1 mean expression = 8.59 in SUPT_0137. This quantitative value is consistent with Prox1 marking granule cells in this supertype.

- **Marker C1ql2 — CONSISTENT.** C1ql2 is listed as a defining marker of the DG granule cell [9]. Precomputed expression stats confirm C1ql2 mean expression = 5.77 in SUPT_0137, consistent with C1ql2 marking this supertype.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Hochgerner 2018 (GEO:GSE95315) mouse hippocampus scRNA-seq Granule-mature and Granule-immature labels onto WMBv1 (CCN20230722). Both mature and immature granule cell populations map primarily to SUPT_0137 at the supertype level: F1 = 0.584 (Granule-mature, 433/609 cells) and F1 = 0.601 (Granule-immature, 437/581 cells). At subclass level, coverage for DG Glut subclass (037) is 0.988 (Granule-mature) and 0.888 (Granule-immature), confirming DG Glut as the dominant classification.

**Marker evidence provenance**

- **Prox1** [8]: Evidence is from Sarvari et al. 2016 [8], which documents expression of metabotropic glutamate receptors and vesicular glutamate transporters in hippocampal subfields. Cell-type specificity for Prox1 as a granule cell marker is based on regional assignment to the DG. Prox1 is a well-established homeodomain transcription factor specifically expressed in DG granule cells and is the gold-standard molecular marker for this cell type in the published literature *(note: the broad Prox1–DG granule cell association is from training knowledge; the specific reference [8] addresses synaptic glutamate receptors rather than Prox1 directly; a targeted cite-traverse for "Prox1 dentate gyrus granule cell mouse" would confirm the primary citation)*. Precomputed atlas stats confirm Prox1 mean = 8.59 in SUPT_0137 — consistent with this marker identifying the granule cell population.

- **C1ql2** [9]: Evidence is from D et al. 2018 [9], which reports that "the expression of Sema5B and C1ql2 is restricted to dentate granule cells within the hippocampus." This is a direct statement of cell-type specificity within the hippocampus at transcript level. Cell-type specificity: the study restricts C1ql2 expression to dentate granule cells within the hippocampus, providing strong specificity evidence. Precomputed atlas stats confirm C1ql2 mean = 5.77 in SUPT_0137. No discrepancy between sources.

**Concerns**

- **PARTIAL_OVERLAP — heterogeneous supertype.** DG Glut subclass (SUBC_037) in WMBv1 contains at least four supertypes (SUPT_0136–0139). Hochgerner Granule-mature and Granule-immature both map predominantly to SUPT_0137 (F1 ~0.59–0.60), but a substantial minority of cells distribute to adjacent supertypes. The F1 scores of ~0.58–0.60 reflect genuine heterogeneity rather than a clean one-to-one mapping.

- **Species caveat.** The Hochgerner 2018 dataset is rat; annotation transfer is to the mouse WMBv1 atlas. Species-level differences in granule cell transcriptomics are unquantified; cross-species transfer adds uncertainty.

- **Immature granule cell coverage.** Adult-born immature granule cells may also map to SUPT_0141 (DG-PIR Ex IMN_2; F1=0.146 for Granule-immature from Hochgerner 2018). The classical DG granule cell type as described here spans both mature and immature populations, but SUPT_0137 may preferentially capture mature cells.

**What would upgrade confidence**

- **Add-expression for Prox1 and C1ql2 on DG Glut supertypes** (SUPT_0136–0139): confirm that Prox1 and C1ql2 are specifically elevated in SUPT_0137 vs adjacent DG Glut supertypes; expected output: precomputed expression entries formalising the granule cell marker profile at the atlas level. Resolves open question 2.

- **Annotation transfer from a mouse granule cell dataset** (AnnotationTransferEvidence): run MapMyCells using a mouse-specific granule cell dataset (e.g. Artimovich 2020 or Shin 2015) to cross-validate the SUPT_0137 mapping in the same species as WMBv1 and remove the species extrapolation concern. Expected F1 ≥ 0.70 at SUPERTYPE level. Resolves cross-species uncertainty.

- **Additional supertype edges (SUPT_0136, 0138, 0139):** Adding MappingEdge entries for the remaining DG Glut supertypes would accurately represent the full classical DG granule cell population and resolve whether SUPT_0136–0139 correspond to functionally distinct sub-populations. Resolves open question 1.

---

## Proposed experiments

*Note on existing AT evidence:* The Hochgerner 2018 (GEO:GSE95315) annotation transfer establishes SUPT_0137 as the dominant DG Glut supertype at subclass level (coverage ≥ 0.88). A refined round using a mouse-specific granule cell dataset would remove the species extrapolation concern and strengthen the mapping.

### Add-expression (Prox1 and C1ql2 on DG Glut supertypes)

- **What:** Run `just add-expression` for Prox1 and C1ql2 on SUPT_0136–0139 using CCN20230722 precomputed stats HDF5.
- **Target:** Confirm Prox1 mean ≥ 5.0 and C1ql2 mean ≥ 3.0 specifically in SUPT_0137; low expression in flanking supertypes.
- **Expected output:** Precomputed expression blocks on atlas nodes; LiteratureEvidence or ATLAS_METADATA cross-check entries.
- **Resolves:** Open question 2 (are Prox1 and C1ql2 expressed specifically in SUPT_0137?).

### Annotation transfer (mouse granule cell dataset)

- **What:** MapMyCells local annotation transfer to WMBv1 (CCN20230722) using a mouse-specific granule cell dataset (e.g. Artimovich 2020 or Shin 2015).
- **Target:** F1 ≥ 0.70 at SUPERTYPE level for SUPT_0137.
- **Expected output:** AnnotationTransferEvidence entry on edge_dg_granule_cell_hippocampus_to_supt_0137.
- **Resolves:** Cross-species uncertainty introduced by rat-to-mouse Hochgerner 2018 transfer.

---

## Open questions

1. Do SUPT_0136, SUPT_0137, SUPT_0138 correspond to functionally distinct granule cell populations (e.g. adult-born vs. developmentally-born granule cells, or dorsal vs. ventral DG)?

2. Are Prox1 and C1ql2 specifically elevated in SUPT_0137 cells vs. adjacent DG Glut supertypes? This requires add-expression from precomputed stats to resolve.

---

## Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_granule_cell_hippocampus_to_supt_0137 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE95315) | SUPPORT — F1=0.584 (Granule-mature) / F1=0.601 (Granule-immature); subclass coverage ≥ 0.88; SUPT_0137 is dominant DG Glut supertype |
| edge_dg_granule_cell_hippocampus_to_supt_0137 | ATLAS_METADATA | SUPPORT — 7199 cells in DG granule cell layer (MBA:632); Prox1 mean=8.59, C1ql2 mean=5.77 in SUPT_0137 |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Munster-Wandowski et al. 2013 · PMID:24319410 | [24319410](https://pubmed.ncbi.nlm.nih.gov/24319410/) | Soma location |
| [2] | Hagihara et al. 2011 · PMID:21927594 | [21927594](https://pubmed.ncbi.nlm.nih.gov/21927594/) | Soma location |
| [3] | Yau et al. 2015 · PMID:26380120 | [26380120](https://pubmed.ncbi.nlm.nih.gov/26380120/) | Soma location |
| [4] | doi:https://doi.org/10.1038/s41598-017-11268-z | — | Soma location |
| [5] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Neurotransmitter type |
| [6] | Zander et al. 2010 · PMID:20519538 | [20519538](https://pubmed.ncbi.nlm.nih.gov/20519538/) | Neurotransmitter type |
| [7] | Pedroni et al. 2014 · PMID:24592213 | [24592213](https://pubmed.ncbi.nlm.nih.gov/24592213/) | Neurotransmitter type |
| [8] | Sarvari et al. 2016 · PMID:27375434 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434/) | Prox1 marker |
| [9] | D et al. 2018 · PMID:29674952 | [29674952](https://pubmed.ncbi.nlm.nih.gov/29674952/) | C1ql2 marker |
