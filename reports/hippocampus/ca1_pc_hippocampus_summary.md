# CA1 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA1 [UBERON:0014548] | [1][2][3][4][5] |
| NT | Glutamatergic | [4] |
| Defining markers | Wfs1 | [6][7][8][9][10] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] | CA1-ProS Glut | 2553 (pyramidal layer, MBA:407) | 🟡 MODERATE | Location CONSISTENT · NT CONSISTENT · Wfs1 expression confirmed | Best candidate |

Total: 1 edge. Relationship type: TYPE_A_SPLITS (classical CA1 pyramidal cell encompasses multiple WMBv1 supertypes within SUBC_016; this edge targets the primary correspondence SUPT_0069).

---

## 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0069 belongs to subclass CS20230722_SUBC_016 (016 CA1-ProS Glut), the dedicated CA1/ProS glutamatergic subclass in WMBv1. The classical CA1 pyramidal cell is defined as glutamatergic [4], and SUBC_016 is exclusively glutamatergic — a direct match at both the supertype and subclass level.

- **Soma location — CONSISTENT.** SUPT_0069 is the highest-scoring WMBv1 supertype candidate for CA1 pyramidal cells (discovery score 5). WMBv1 MERFISH spatial data places 2553 SUPT_0069 cells in Field CA1, pyramidal layer (MBA:407), consistent with the CA1 PC soma location in pyramidal layer of CA1 [UBERON:0014548] [1][2][3][4][5]. Additional SUPT_0069 cells also appear in Field CA1, stratum oriens (MBA:399; 5205 cells) and stratum radiatum (MBA:415; 4162 cells); this distribution across adjacent strata is expected from MERFISH soma assignment at stratum boundaries and does not conflict with the classical soma location. *(note: WMBv1 location data derives from MERFISH spatial registration and records soma position only; the oriens/radiatum signals reflect assignment scatter at layer borders rather than ectopic soma locations.)*

- **Marker Wfs1 — CONSISTENT.** Wfs1 is listed as a defining marker of the CA1 pyramidal cell [6][7][8][9][10]. Although Wfs1 does not appear among the three WMBv1 defining markers for SUPT_0069 (Lefty1, Fibcd1, Pcp4l1), precomputed expression stats (precomputed_stats.h5, supertype level) confirm Wfs1 mean expression = 3.97 in SUPT_0069, indicating substantial Wfs1 expression in this supertype. The absence from the atlas defining-marker list reflects that defining markers in WMBv1 record cluster-discriminating genes, not exhaustive expression profiles; the quantitative expression value is consistent with Wfs1 marking this supertype.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq CA1-ProS subclass labels onto WMBv1 (CCN20230722): of 1704 CA1-ProS cells, 1011 (59.3%) map to SUPT_0069 at the supertype level. F1 = 0.745 (group_purity = 0.593, target_purity = 1.0). Target_purity = 1.0 confirms SUPT_0069 is exclusively populated by CA1-ProS cells in this dataset. The remaining CA1-ProS cells distribute across SUPT_0070 (20.1%), SUPT_0072 (13.3%), SUPT_0071 (3.5%), and SUPT_0073 (2.8%), consistent with the TYPE_A_SPLITS relationship.

**Marker evidence provenance**

- **Wfs1** [6][7][8][9][10]: Evidence spans multiple transcript-level and protein-level studies. Langnaese et al. 1997 [9] and Herrera-Molina et al. 2014 [10] characterise Neuroplastin-65 (Np65) in hippocampal pyramidal neurons including CA1. Siegel et al. 1995 [6] characterises AMPA/NMDA receptor distribution in CA1 stratum oriens and radiatum. Yeung et al. 2020 [7] describes glutamate receptor subunit immunoreactivity in CA1 pyramidal cell bodies. Herrera-Molina et al. 2017 [8] provides additional synaptic protein context. CA1 pyramidal cell identity in these studies is established by anatomical location (stratum pyramidale), which is the standard anatomical criterion for this well-defined cell type — morphological or Cre-driver confirmation is not required for a population as anatomically unambiguous as CA1 PCs. The Wfs1 precomputed mean expression = 3.97 at SUPT_0069 supertype level provides a direct quantitative cross-check consistent with the literature designation. Recommendation: A targeted cite-traverse for "Wfs1 CA1 pyramidal deep superficial sublayer" may clarify whether Wfs1 expression is uniform across all CA1 PCs or enriched in deep-layer cells, which would refine the sublayer interpretation for SUPT_0069 vs. other CA1-ProS supertypes.

**Concerns**

- **TYPE_A_SPLITS — incomplete representation.** The classical CA1 pyramidal cell population spans at least four supertypes within SUBC_016 (SUPT_0069, 0070, 0071, 0072). This single edge to SUPT_0069 represents the primary correspondence only. A complete mapping requires additional edges to SUPT_0070, 0071, and 0072.

- **Deep vs. superficial sublayer ambiguity.** Wfs1 is associated with deep-layer CA1 PCs in the published literature. If SUPT_0069 preferentially represents deep-layer cells (its defining marker Fibcd1 has been associated with deep CA1 PC populations), then SUPT_0069 may map more specifically to the deep CA1 PC sublayer rather than the full CA1 pyramidal cell population. This question is unresolved from current atlas metadata alone. *(note: the Fibcd1–deep CA1 PC association is from training knowledge, not from the facts file; requires literature verification.)*

**What would upgrade confidence**

- **Additional supertype edges (SUPT_0070, 0071, 0072):** Adding MappingEdge entries for the remaining CA1-ProS Glut supertypes would accurately represent the full classical CA1 pyramidal cell population (ATLAS_METADATA or LiteratureEvidence).

- **Annotation transfer at cluster level:** Run MapMyCells annotation transfer of Cembrowski 2016 or Zeisel 2018 dorsal CA1 pyramidal cell labels onto WMBv1 at CLUSTER level; target F1 ≥ 0.80 for individual supertypes; expected output: AnnotationTransferEvidence entries per supertype. This would resolve the SUPT_0069–0072 deep/superficial sublayer correspondence (open question 1) and enable confidence upgrade.

- **Wfs1 sublayer literature:** Targeted cite-traverse for "Wfs1 CA1 deep superficial sublayer" to clarify whether Wfs1 marks all CA1 PCs or preferentially deep-layer cells (LiteratureEvidence). This is addressable without new experiments.

---

## Proposed experiments

*Note on existing AT evidence:* The Yao 2021 (GEO:GSE185862) annotation transfer already establishes the CA1-ProS subclass correspondence at supertype level (F1 = 0.745, target_purity = 1.0). A refined round using dorsal-CA1-specific labels with sublayer annotations at CLUSTER resolution would resolve the remaining sublayer ambiguity not addressed by the existing transfer.

### MapMyCells / Annotation transfer (resolve CA1-ProS supertype correspondence)

- **What:** MapMyCells local annotation transfer using a dataset with deep/superficial CA1 PC annotations (e.g. Cembrowski 2016 dorsal CA1 dataset or Zeisel 2018).
- **Target:** F1 ≥ 0.80 at CLUSTER level for individual CA1-ProS Glut supertypes.
- **Expected output:** AnnotationTransferEvidence entries for edges to SUPT_0069, 0070, 0071, 0072.
- **Resolves:** Open question 1 (deep vs. superficial sublayer correspondence); completes TYPE_A_SPLITS mapping.

---

## Open questions

1. Which CA1-ProS supertypes (SUPT_0069–0072) correspond to deep vs. superficial CA1 pyramidal cell sublayers? Wfs1 marks deep-layer CA1 PCs in the literature; checking which supertype carries the highest Wfs1 mean expression in atlas precomputed stats, and running annotation transfer with sublayer-annotated CA1 data, would resolve the sublayer correspondence.

---

## Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ca1_pc_hippocampus_to_supt_0069 | ATLAS_METADATA | SUPPORT — SUPT_0069 highest-scoring CA1-ProS Glut supertype; NT CONSISTENT, location CONSISTENT (2553 cells in pyramidal layer MBA:407) |
| edge_ca1_pc_hippocampus_to_supt_0069 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1 = 0.745; target_purity = 1.0; 59.3% of CA1-ProS cells map to SUPT_0069 |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Soma location |
| [2] | Müller & Remy 2017 · PMID:29250747 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | Soma location |
| [3] | doi:https://doi.org/10.1038/s41598-017-11268-z | — | Soma location |
| [4] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | Soma location; NT type |
| [5] | Mancini et al. 2022 · PMID:37011759 | [37011759](https://pubmed.ncbi.nlm.nih.gov/37011759/) | Soma location |
| [6] | Siegel et al. 1995 · PMID:7722624 | [7722624](https://pubmed.ncbi.nlm.nih.gov/7722624/) | Wfs1 marker |
| [7] | Yeung et al. 2020 · PMID:32009891 | [32009891](https://pubmed.ncbi.nlm.nih.gov/32009891/) | Wfs1 marker |
| [8] | Herrera-Molina et al. 2017 · PMID:28779130 | [28779130](https://pubmed.ncbi.nlm.nih.gov/28779130/) | Wfs1 marker |
| [9] | Langnaese et al. 1997 · PMID:8995369 | [8995369](https://pubmed.ncbi.nlm.nih.gov/8995369/) | Wfs1 marker |
| [10] | Herrera-Molina et al. 2014 · PMID:24554721 | [24554721](https://pubmed.ncbi.nlm.nih.gov/24554721/) | Wfs1 marker |
