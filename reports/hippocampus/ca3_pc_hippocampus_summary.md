# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA3 stratum pyramidale [UBERON:0014550] | [1] [2] |
| NT | glutamatergic | [3] |
| Markers |  |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0078 CA3 Glut_4 [CS20230722_SUPT_0078] |  | — | 🟡 MODERATE | Best candidate |

All edges: `TYPE_A_SPLITS`

---

## 0078 CA3 Glut_4 · 🟡 MODERATE

**Supporting evidence:**

- SUPT_0078 (0078 CA3 Glut_4) is the WMBv1 supertype with the strongest annotation transfer support for CA3 pyramidal cells (see ANNOTATION_TRANSFER evidence below). It belongs to subclass CS20230722_SUBC_017 (017 CA3 Glut), the dedicated CA3 glutamatergic subclass. SUPT_0078 MERFISH anatomy is entirely CA3: pyramidal layer (1467 cells), stratum oriens (1381), stratum radiatum (945), stratum lucidum (868), and stratum lacunosum-moleculare (437). Defining markers: Homer3, Cldn22. SUBC_017 contains five supertypes (SUPT_0075-0079); the classical CA3 pyramidal cell type spans this entire range. The previous primary candidate SUPT_0075 received only 16.8% of Yao 2021 CA3 cells (F1=0.288); SUPT_0078 received 63.0% (F1=0.773), indicating it is the dominant CA3 PC supertype in the atlas. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) mouse hippocampus SSv4 scRNA-seq CA3 subclass label onto WMBv1 (CCN20230722). Of 322 CA3 cells, 203 (63.0%) map to SUPT_0078 at the supertype level. F1 score = 0.773 (group_purity=0.630, target_purity=1.0). Target_purity=1.0 confirms SUPT_0078 receives only CA3 cells in this dataset. The remaining cells distribute across SUPT_0075 (16.8%), SUPT_0077 (11.5%), SUPT_0076 (6.5%), and SUPT_0079 (1.6%), consistent with TYPE_A_SPLITS: the classical CA3 pyramidal cell spans all SUBC_017 supertypes, with SUPT_0078 as the dominant correspondence. [Annotation transfer]

**Concerns:**

- WMBv1 SUBC_017 (CA3 Glut) contains five supertypes: SUPT_0075-0079. Annotation transfer (Yao 2021) confirms SUPT_0078 as the primary CA3 PC correspondence (63.0% of CA3 cells, F1=0.773). The previous claim that SUPT_0078-0079 represent mossy cell populations is not supported — SUPT_0078 anatomy is exclusively CA3 pyramidal/oriens/radiatum/lucidum/SLM strata with no hilar representation. Sublayer correspondence of SUPT_0075-0077 (CA3 Glut_1-3) to CA3a/b/c remains unresolved; those supertypes collectively received 34.8% of Yao 2021 CA3 cells.

**What would upgrade confidence:**

- *Unresolved:* Do SUPT_0075, 0076, 0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to other organisational principles (e.g. proximal vs. distal mossy fiber input zone)?

- *Proposed:* Run annotation transfer from a CA3 sublayer-resolved dataset to map CA3a/b/c correspondence among SUBT_0075-0077 and clarify the role of SUPT_0078 vs 0075-0077 in the sublayer organisation.


---

## Proposed experiments

### 1 — Other

- Run annotation transfer from a CA3 sublayer-resolved dataset to map CA3a/b/c correspondence among SUBT_0075-0077 and clarify the role of SUPT_0078 vs 0075-0077 in the sublayer organisation.
*Resolves: edge_ca3_pc_hippocampus_to_supt_0078*

---

## Open questions

1. Do SUPT_0075, 0076, 0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to other organisational principles (e.g. proximal vs. distal mossy fiber input zone)?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ca3_pc_hippocampus_to_supt_0078 | Atlas metadata | SUPPORT |
| edge_ca3_pc_hippocampus_to_supt_0078 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | soma location |
| [2] | Wheeler et al. 2015 · PMID:26402459 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | soma location |
| [3] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
