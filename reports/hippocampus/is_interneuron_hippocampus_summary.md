# Interneuron-specific (IS) interneuron — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | VIP GABAergic interneuron (CL:4023016) | |
| Soma location | CA1 stratum oriens [UBERON:0005383]; CA1 stratum radiatum [UBERON:0005402]; CA1 stratum lacunosum-moleculare [UBERON:0005403] | [1] [1] [1] [1] [1] [1] [1] [1] [1] |
| NT | GABAergic |  |
| Markers | Calb2+, Vip+ | [2] [1] [3] [4] |
| Neuropeptides | Vip | [2] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0179 Vip Gaba_7 · 🟡 MODERATE

**Supporting evidence:**

- Vip Gaba_7 supertype has Vip as a DEFINING marker consistent with IS-2 and IS-3 subtypes (VIP+/CR+). Hippocampal anatomy present across multiple layers: CA1 SO (24), CA3 SO (25), CA1 SR (26), CA3 SR (17), CA1 SP (11), CA3 SP (23). The multi-laminar CA1 distribution matches IS cell soma locations spanning SO, SR, and SLM. However, the classical IS interneuron node covers three subtypes (IS-1: CR+/VIP-, IS-2: VIP+, IS-3: VIP+/CR+) — only IS-2 and IS-3 would map to a VIP supertype. Qrfpr, Stk32a, Igfbp4 are additional defining markers with no correspondence established in classical IS literature. [Atlas metadata]
- Precomputed stats cross-check: both defining markers strongly confirmed (Calb2=6.78, Vip=6.82). Vip neuropeptide also confirmed (6.82). [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Vip subclass (n=476 HIP cells) onto WMBv1. Vip cells map very strongly to SUBC_046 (Vip Gaba, F1=0.969) at SUBCLASS level, confirming VIP-family identity. At SUPERTYPE level, SUPT_0179 (Vip Gaba_7) receives 96/476 Vip cells (F1=0.379, target_purity=0.970), second to SUPT_0177 (Vip Gaba_5, F1=0.397, 101 cells). Vip cells are broadly distributed across 10+ Vip supertypes, reflecting the diversity of the Vip interneuron population. PARTIAL: the Vip SSv4 label cannot discriminate IS cells from VIP basket or other VIP subtypes. Yao 2021 SSv4 'Vip' subclass (n=476 HIP cells) encompasses VIP basket, IS cells, and other VIP interneuron subtypes; subtype resolution requires a dataset with morphologically identified VIP-IN labels. [Annotation transfer]

**Concerns:**

- The classical IS interneuron node is heterogeneous (IS-1/2/3 subtypes). IS-1 cells are VIP-negative (CR+ only) and would NOT map to a Vip supertype. This edge only represents IS-2 and IS-3 (VIP+) subtypes. A Calb2-expressing but Vip-negative supertype may be a better candidate for IS-1.
- VIP GABAergic interneurons in hippocampus include VIP basket cells (vip_basket_cell_hippocampus) in addition to IS cells. The supertype may encompass both perisomatic VIP basket cells and disinhibitory IS cells; the interneuron-specific targeting feature of IS cells is not resolvable from transcriptomic metadata alone.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | Atlas metadata | PARTIAL |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | Atlas metadata | SUPPORT |
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tyan et al. 2014 · PMID:24671999 | [24671999](https://pubmed.ncbi.nlm.nih.gov/24671999/) | soma location |
| [2] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Calb2 marker |
| [3] | Chamberland & Topolnik 2012 · PMID:23162426 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | Calb2 marker |
| [4] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | Vip marker |
