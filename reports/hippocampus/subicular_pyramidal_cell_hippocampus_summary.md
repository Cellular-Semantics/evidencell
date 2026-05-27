# subicular pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | subiculum [UBERON:0002191] | [1][2][3][4] |
| NT | glutamatergic | [5] |
| Defining markers | Np65 (Nptn neuroplastin-65) | [6] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] | SUB-ProS Glut | — | 🟡 MODERATE | NT CONSISTENT · Location CONSISTENT | Best candidate |

Total: 1 edge. Relationship type: TYPE_A_SPLITS (the classical subicular pyramidal cell spans multiple WMBv1 supertypes within the SUB-ProS subclass; this edge targets SUPT_0096 as the primary and most abundant supertype).

---

## 3. Candidate paragraphs

## 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0096 belongs to subclass SUBC_023 SUB-ProS Glut, the dedicated subicular/prosubicular glutamatergic subclass in WMBv1. The classical subicular pyramidal cell is defined as glutamatergic [5]; this identity is shared at both the supertype and subclass level.

- **Soma location — CONSISTENT.** WMBv1 MERFISH spatial data places SUPT_0096 cells in subicular and prosubicular layers, directly matching the classical soma location in the subiculum [UBERON:0002191] [1][2][3][4]. The subiculum is a well-delineated output structure of the hippocampal formation and the correspondence is anatomically unambiguous.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq SUB-ProS subclass labels onto WMBv1 (CCN20230722): of 471 SUB-ProS cells, 313 (66.5%) map to SUPT_0096 at the supertype level. F1 = 0.798, coverage = 0.665, purity = 1.000. The near-perfect target purity confirms that all cells assigned to SUPT_0096 originate exclusively from the subicular neuron population, with no contamination from other HPF subclasses. This is the primary quantitative evidence for this mapping. SUPT_0097 and SUPT_0098 account for a further 14.6% (F1=0.253) and 18.0% (F1=0.305) of SUB-ProS cells respectively, consistent with the TYPE_A_SPLITS relationship.

- **Marker Np65 — CONSISTENT.** Np65 (the Nptn gene product, neuroplastin-65) is listed as a defining marker of the subicular pyramidal cell [6]. Precomputed expression stats (precomputed_stats.h5, supertype level) confirm Np65 mean expression = 8.60 in SUPT_0096, placing it among the higher-expressing HPF supertypes (range approximately 2.1–9.5 across HPF supertypes). While this confirms expression, Np65 at this level is broadly distributed across hippocampal pyramidal neurons and does not discriminate among SUPT_0096, 0097, and 0098.

**Marker evidence provenance**

- **Np65 (Nptn)** [6]: The supporting citation reports the highest Np65 expression on dendrites of granule cells and subicular pyramidal neurons at the protein level (immunohistochemistry). Cell-type specificity relies on the known anatomical restriction of the subicular pyramidal neuron to the subiculum [UBERON:0002191]; the study was not specifically performed on morphology-confirmed or electrophysiology-confirmed subicular cells, but the anatomical location criterion is well established for this population. The Np65 mean expression of 8.60 in SUPT_0096 from precomputed stats is consistent with the protein-level observation. However, this value is broadly distributed across HPF supertypes and Np65 does not serve as a discriminating marker between the three IT subicular supertypes. *(Recommendation: A targeted cite-traverse for "neuroplastin-65 subiculum pyramidal" may reveal whether Np65 expression is differentially regulated across RF, WB, and SB subicular subtypes.)*

**Concerns**

- **TYPE_A_SPLITS — incomplete representation.** The classical subicular pyramidal cell population encompasses the full range of IT projection neurons in the subiculum, which WMBv1 resolves into three SUB-ProS supertypes (SUPT_0096, 0097, 0098). The current mapping has a single edge to SUPT_0096 (the dominant target at F1=0.798), but SUPT_0097 (F1=0.253) and SUPT_0098 (F1=0.305) together account for approximately one-third of subicular cells. A complete mapping requires edges to these additional supertypes.

- **CT SUB and NP SUB supertypes not covered.** WMBv1 also includes CT SUB supertypes (SUPT_0120–0121) and NP SUB supertypes (SUPT_0127–0128) representing corticothalamic and near-projection subicular neurons respectively. Whether these correspond to the weak-burst (WB) or strong-burst (SB) electrophysiological subtypes of classical subicular pyramidal cells, or represent functionally distinct populations, is currently unresolved.

**What would upgrade confidence**

- **Complete TYPE_A_SPLITS mapping:** Adding MappingEdge entries to SUPT_0097 (F1=0.253) and SUPT_0098 (F1=0.305) would accurately represent the full IT subicular pyramidal cell population. This requires only curation effort (no new experiments).

- **Electrophysiological annotation transfer:** Running MapMyCells annotation transfer from a dataset with electrophysiologically characterised subicular pyramidal cells (regular-firing RF, weak-burst WB, strong-burst SB subtypes) onto WMBv1 at CLUSTER level would resolve which supertypes correspond to which firing types. Target: F1 ≥ 0.80 at CLUSTER level. Expected output: AnnotationTransferEvidence entries per supertype resolving Open question 1.

---

## 4. Proposed experiments

### 1 — Curation (complete TYPE_A_SPLITS edges)

**What:** Add MappingEdge entries to SUPT_0097 and SUPT_0098.

**Target:** F1 scores from existing Yao 2021 annotation transfer (SUPT_0097 F1=0.253, SUPT_0098 F1=0.305) already available; no new experiment required.

**Expected output:** Two additional MappingEdge YAML entries completing the TYPE_A_SPLITS subicular mapping.

**Resolves:** Incomplete TYPE_A_SPLITS representation; provides full coverage of IT subicular pyramidal neuron supertypes.

### 2 — MapMyCells / Annotation transfer (electrophysiological subtype correspondence)

**What:** MapMyCells annotation transfer of a dataset containing electrophysiologically characterised subicular pyramidal cells (RF, WB, SB subtypes) onto WMBv1 (CCN20230722).

**Target:** F1 ≥ 0.80 at CLUSTER level for each electrophysiological subtype.

**Expected output:** AnnotationTransferEvidence entries linking RF, WB, and SB firing subtypes to specific SUPT_0096, 0097, or 0098.

**Resolves:** Open question 1 (firing subtype–supertype correspondence).

---

## 5. Open questions

1. Which of the three electrophysiological subtypes of subicular pyramidal cells (regular-firing RF, weak-burst WB, strong-burst SB) correspond to SUPT_0096, 0097, and 0098? Annotation transfer from an electrophysiologically annotated subicular dataset at CLUSTER level, targeting F1 ≥ 0.80, would resolve this.

2. Do CT SUB supertypes (SUPT_0120–0121) and NP SUB supertypes (SUPT_0127–0128) correspond to functionally defined subicular projection subtypes, or are they best treated as part of the broader classical subicular pyramidal cell population?

---

## 6. Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_subicular_pyramidal_cell_hippocampus_to_supt_0096 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.798; purity=1.000; 66.5% of SUB-ProS cells map to SUPT_0096 |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2026 · PMID:41693678 | [41693678](https://pubmed.ncbi.nlm.nih.gov/41693678/) | Soma location |
| [2] | Unknown 2016 · PMID:27150503 | [27150503](https://pubmed.ncbi.nlm.nih.gov/27150503/) | Soma location |
| [3] | Unknown 2025 · PMID:41509312 | [41509312](https://pubmed.ncbi.nlm.nih.gov/41509312/) | Soma location |
| [4] | Unknown 2013 · PMID:24303119 | [24303119](https://pubmed.ncbi.nlm.nih.gov/24303119/) | Soma location |
| [5] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | NT type |
| [6] | I et al. 2019 · PMID:30488668 | [30488668](https://pubmed.ncbi.nlm.nih.gov/30488668/) | Np65 marker |
