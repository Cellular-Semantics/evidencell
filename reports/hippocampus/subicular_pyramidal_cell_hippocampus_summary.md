# subicular pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | subiculum [UBERON:0002191] | [1] [2] [3] [4] [4] [4] [2] |
| NT | glutamatergic | [5] |
| Markers | Np65+ | [6] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] |  | — | 🟡 MODERATE | Best candidate |

All edges: `TYPE_A_SPLITS`

---

## 0096 SUB-ProS Glut_1 · 🟡 MODERATE

**Supporting evidence:**

- Annotation transfer of Yao 2021 (GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722) via local MapMyCells. Yao 2021 SUB-ProS subclass cells (n=471) representing IT subicular pyramidal neurons map to three SUB-ProS supertypes: SUPT_0096 (66.5%, F1=0.798), SUPT_0097 (14.6%, F1=0.253), SUPT_0098 (18.0%, F1=0.305). Together these three supertypes account for 99.1% of SUB-ProS cells. SUPT_0096 has the highest group purity (0.665) and near-perfect target purity (1.000), indicating all cells assigned to SUPT_0096 originate from subicular neurons. The TYPE_A_SPLITS relationship reflects that the classical subicular pyramidal cell encompasses all three IT subicular supertypes; this edge targets SUPT_0096 as the primary and most abundant mapping. [Annotation transfer]

**Concerns:**

- The classical subicular pyramidal cell type encompasses the full range of IT projection neurons in the subiculum. WMBv1 resolves this into three SUB-ProS supertypes (SUPT_0096-0098) plus two CT SUB supertypes (SUPT_0120-0121) and two NP SUB supertypes (SUPT_0127-0128). This edge targets SUPT_0096 as the primary IT subicular supertype. A complete mapping requires edges to SUPT_0097 and SUPT_0098 as well. CT SUB and NP SUB represent projection-defined subpopulations (corticothalamic, near-projection) that may be classical subicular pyramidal subtypes (WB and SB firing types) or may be distinct functional populations.

**What would upgrade confidence:**

- *Unresolved:* Which of the three electrophysiological subtypes of subicular pyramidal cells (regular-firing RF, weak-burst WB, strong-burst SB) correspond to SUPT_0096, 0097, 0098? F1 scores for each subtype would require datasets with electrophysiologically characterised single-cell transcriptomics.

- *Proposed:* Add edges to SUPT_0097 (F1=0.253) and SUPT_0098 (F1=0.305) to complete the subicular pyramidal cell mapping.


---

## Proposed experiments

### 1 — Other

- Add edges to SUPT_0097 (F1=0.253) and SUPT_0098 (F1=0.305) to complete the subicular pyramidal cell mapping.
*Resolves: edge_subicular_pyramidal_cell_hippocampus_to_supt_0096*

---

## Open questions

1. Which of the three electrophysiological subtypes of subicular pyramidal cells (regular-firing RF, weak-burst WB, strong-burst SB) correspond to SUPT_0096, 0097, 0098? F1 scores for each subtype would require datasets with electrophysiologically characterised single-cell transcriptomics.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_subicular_pyramidal_cell_hippocampus_to_supt_0096 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2026 · PMID:41693678 | [41693678](https://pubmed.ncbi.nlm.nih.gov/41693678/) | soma location |
| [2] | Unknown 2016 · PMID:27150503 | [27150503](https://pubmed.ncbi.nlm.nih.gov/27150503/) | soma location |
| [3] | Unknown 2025 · PMID:41509312 | [41509312](https://pubmed.ncbi.nlm.nih.gov/41509312/) | soma location |
| [4] | Unknown 2013 · PMID:24303119 | [24303119](https://pubmed.ncbi.nlm.nih.gov/24303119/) | soma location |
| [5] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
| [6] | I et al. 2019 · PMID:30488668 | [30488668](https://pubmed.ncbi.nlm.nih.gov/30488668/) | Np65 marker |
