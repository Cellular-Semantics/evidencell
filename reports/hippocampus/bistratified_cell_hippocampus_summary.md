# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | bistratified cell (CL:0004247) | |
| Soma location | CA1 stratum pyramidale [UBERON:0005401]; CA1 stratum oriens [UBERON:0005383]; CA1 stratum radiatum [UBERON:0005402] | [1] [2] [3] [1] [2] [3] [1] [2] [3] |
| NT | GABAergic | [4] |
| Markers | Pvalb+, Sst+, Tac1+ | [5] [6] [7] [8] [9] |
| Neuropeptides | Sst | [9] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## 0216 Sst Gaba_3 · 🔴 LOW

**Supporting evidence:**

- Sst subclass and GABA NT type are consistent with bistratified cell co-expression of Pvalb and Sst. CA1 stratum oriens (818 cells) and prosubiculum (259 cells) and posterior amygdala (780 cells) present. Defining markers include Reln (consistent with bistratified cells, which are Reln+) and Sp9 (not a canonical bistratified marker). Tac1 among DEFINING_SCOPED markers is directly consistent with bistratified cell identity (Chamberland et al. 2024 used Sst;;Tac1 intersection to target bistratified cells, PMID:38640347). Partial overlap declared because this supertype also contains OLM cells (olm_cell_ca1 mapping, see separate edge) and HS cells — these classical types are not separable at supertype level. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. SUPT_0216 (Sst Gaba_3) receives only 6/66 Pvalb cells (F1=0.053, target_purity=0.036). The Pvalb population maps predominantly to Pvalb chandelier (SUPT_0204, F1=0.612) and Pvalb Gaba_2 (SUPT_0206, F1=0.324) supertypes. SUPT_0216 is a Sst supertype; Sst SSv4 cells map to SUPT_0216 with F1=0.488 (83/273 cells). PARTIAL: the weak Pvalb→SUPT_0216 signal reflects possible Sst co-expression in a bistratified cell subpopulation, consistent with the known transcriptomic plasticity of bistratified cells (some express both Pvalb and Sst). The Sst SSv4 Gaba population partially supports this target, but SUPT_0219 (Sst Gaba_6, F1=0.759) is the dominant Sst target. This edge should be interpreted with LOW confidence. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]

**Concerns:**

- **location_CA1_stratum_pyramidale** (APPROXIMATE): A=CA1 stratum pyramidale (UBERON:0005401) — soma / B=CA1 stratum oriens (MBA:399, 818 cells) — no pyramidal layer listed. Dominant hippocampal signal in CA1 SO, not pyramidale. Bistratified cell soma classically in/near stratum pyramidale.
- **marker_Pvalb** (DISCORDANT): A=Pvalb — defining marker (co-expressed with Sst) / B=Sst subclass, not Pvalb; Pvalb not in supertype markers; precomputed stats mean: 1.48. Bistratified cells co-express Pvalb and Sst (PMID:37467748). The Sst subclass placement is consistent with the Sst component but the Pvalb component is not captured. High transcriptomic similarity within Sst subclass may place bistratified closer to OLM cells than PV basket cells at transcriptomic level.

- Sst Gaba_3 supertype contains at least three classical hippocampal types: OLM cells (Sst+/Chrna2+), bistratified cells (Sst+/Pvalb+/Tac1+), and HS cells (Sst+, long-range projecting). These are not separable at supertype level. This edge and the olm_cell_ca1 edge to the same supertype reflect this overlap explicitly.
- Pvalb co-expression (defining for bistratified) is not captured at the supertype level — Sst subclass placement may under-represent the PV component of bistratified cell identity.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | Atlas metadata | PARTIAL |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland & Topolnik 2012 · PMID:23162426 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | soma location |
| [2] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [3] | Perez et al. 2020 · PMID:33404500 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [4] | Dannenberg et al. 2017 · PMID:29321728 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | neurotransmitter type |
| [5] | Ekins et al. 2020 · PMID:33150866 | [33150866](https://pubmed.ncbi.nlm.nih.gov/33150866/) | Pvalb marker |
| [6] | Chamberland et al. 2023 · PMID:37162922 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Pvalb marker |
| [7] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Pvalb marker |
| [8] | Que et al. 2021 · PMID:33398060 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker |
| [9] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker |
