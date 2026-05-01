# CA1 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | [1] [2] [3] [4] [5] |
| NT | glutamatergic | [4] |
| Markers | Wfs1+ | [6] [7] [8] [9] [10] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] |  | — | 🟡 MODERATE | Best candidate |

All edges: `TYPE_A_SPLITS`

---

## 0069 CA1-ProS Glut_1 · 🟡 MODERATE

**Supporting evidence:**

- SUPT_0069 (0069 CA1-ProS Glut_1) is the highest-scoring WMBv1 supertype candidate for CA1 pyramidal cells (discovery score 5). It belongs to subclass CS20230722_SUBC_016 (016 CA1-ProS Glut), which is the dedicated CA1/ProS glutamatergic subclass in WMBv1. SUPT_0069 has 2553 cells in Field CA1, pyramidal layer (MBA:407). The TYPE_A_SPLITS relationship is used because WMBv1 resolves at least four CA1-ProS supertypes (SUPT_0069-0072) within SUBC_016; the classical CA1 pyramidal cell encompasses all of these. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) mouse hippocampus SSv4 scRNA-seq CA1-ProS subclass label onto WMBv1 (CCN20230722). Of 1704 CA1-ProS cells, 1011 (59.3%) map to SUPT_0069 at the supertype level. F1 score = 0.745 (group_purity=0.593, target_purity=1.0). Target_purity=1.0 confirms SUPT_0069 is exclusively populated by CA1-ProS cells in this dataset. The remaining CA1-ProS cells distribute across SUPT_0070 (20.1%), SUPT_0072 (13.3%), SUPT_0071 (3.5%), and SUPT_0073 (2.8%), consistent with the TYPE_A_SPLITS relationship: the classical CA1 pyramidal cell encompasses all CA1-ProS Glut supertypes, with SUPT_0069 as the primary correspondence. [Annotation transfer]

**Concerns:**

- The CA1 pyramidal cell type in WMBv1 is resolved into at least four supertypes within SUBC_016 (SUPT_0069-0072). This edge targets SUPT_0069 as the primary mapping (highest discovery score; carries Fibcd1) but the full classical CA1 PC population spans all four supertypes. A complete mapping requires additional edges to SUPT_0070, 0071, and 0072.

**What would upgrade confidence:**

- *Unresolved:* Which CA1-ProS supertypes (0069-0072) correspond to deep vs. superficial CA1 pyramidal cell sublayers? Wfs1 marks deep-layer CA1 PCs in the literature; checking which supertype carries Wfs1 in the atlas would resolve the sublayer correspondence.

- *Proposed:* Run MapMyCells annotation transfer of Cembrowski 2016 or Zeisel 2018 dorsal CA1 pyramidal cell labels onto WMBv1 to resolve SUPT_0069-0072 correspondence.


---

## Proposed experiments

### 1 — MapMyCells / annotation transfer

- Run MapMyCells annotation transfer of Cembrowski 2016 or Zeisel 2018 dorsal CA1 pyramidal cell labels onto WMBv1 to resolve SUPT_0069-0072 correspondence.
*Resolves: edge_ca1_pc_hippocampus_to_supt_0069*

---

## Open questions

1. Which CA1-ProS supertypes (0069-0072) correspond to deep vs. superficial CA1 pyramidal cell sublayers? Wfs1 marks deep-layer CA1 PCs in the literature; checking which supertype carries Wfs1 in the atlas would resolve the sublayer correspondence.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ca1_pc_hippocampus_to_supt_0069 | Atlas metadata | SUPPORT |
| edge_ca1_pc_hippocampus_to_supt_0069 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | soma location |
| [2] | Müller & Remy 2017 · PMID:29250747 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | soma location |
| [3] | https://doi.org/10.1038/s41598-017-11268-z | — | soma location |
| [4] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | soma location |
| [5] | Mancini et al. 2022 · PMID:37011759 | [37011759](https://pubmed.ncbi.nlm.nih.gov/37011759/) | soma location |
| [6] | Siegel et al. 1995 · PMID:7722624 | [7722624](https://pubmed.ncbi.nlm.nih.gov/7722624/) | Wfs1 marker |
| [7] | Yeung et al. 2020 · PMID:32009891 | [32009891](https://pubmed.ncbi.nlm.nih.gov/32009891/) | Wfs1 marker |
| [8] | Herrera-Molina et al. 2017 · PMID:28779130 | [28779130](https://pubmed.ncbi.nlm.nih.gov/28779130/) | Wfs1 marker |
| [9] | Langnaese et al. 1997 · PMID:8995369 | [8995369](https://pubmed.ncbi.nlm.nih.gov/8995369/) | Wfs1 marker |
| [10] | Herrera-Molina et al. 2014 · PMID:24554721 | [24554721](https://pubmed.ncbi.nlm.nih.gov/24554721/) | Wfs1 marker |
