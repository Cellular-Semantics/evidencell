# Oriens-Lacunosum Moleculare (O-LM) cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0005383]; CA1 stratum lacunosum-moleculare [UBERON:0005403] | [1] [2] [3] [4] [5] [6] [7] [1] [2] [3] [4] [5] [6] [7] |
| NT | GABAergic | [4] |
| Markers | Sst+, Chrna2+, Reln+ | [4] [8] [5] [6] |
| Negative | Pvalb− | |
| Neuropeptides | Sst, Npy, Pnoc | [4] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0216 Sst Gaba_3 · 🟡 MODERATE

**Supporting evidence:**

- Sst subclass and GABA NT type are fully consistent with OLM cell identity. CA1 stratum oriens (818 cells) is the primary OLM soma location. Defining markers include Reln (OLM cells express Reelin per Winterer 2019 PMID:31420995) and Sp9. Neuropeptide-related markers not resolved at supertype level but Sst subclass is the primary OLM subclass from MapMyCells results on GSE124847 (43/46 OLM cells mapped to this supertype, F1=0.67). PARTIAL_OVERLAP declared because the supertype also contains bistratified cells (Sst/Pvalb/Tac1) and HS cells (long-range Sst) that are not separable here. [Atlas metadata]
- Precomputed stats cross-check: Sst=11.44, Reln=7.90, Chrna2=1.53 (low but present), Pvalb=1.48 (absent). All 3 neuropeptides confirmed (Sst=11.44, Npy=5.07, Pnoc=3.69). Multiple independent marker confirmations. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. At SUBCLASS level, Sst cells map strongly to SUBC_053 (Sst Gaba, F1=0.983). At SUPERTYPE level, the Sst population splits between SUPT_0219 (Sst Gaba_6, F1=0.759, 161 cells) and SUPT_0216 (Sst Gaba_3, F1=0.488, 83 cells). SUPT_0216 receives 83/273 Sst cells with target_purity=1.0. PARTIAL: the Sst label is a mixed population; OLM cells mapping to SUPT_0216 cannot be discriminated from other Sst types mapping to the same supertype. The SUPT_0219 (Sst Gaba_6) being the dominant Sst hit raises uncertainty about whether OLM cells preferentially occupy SUPT_0216 or SUPT_0219. Yao 2021 SSv4 'Sst' subclass (n=273 HIP cells) encompasses multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, oriens-oriens, and others); subtype resolution requires a dataset with morphologically identified Sst-IN labels. [Annotation transfer]

**Concerns:**

- **marker_Chrna2** (APPROXIMATE): A=Chrna2 — defining marker / B=not in supertype defining_markers; scattered expression in Sst Gaba_3 per ABC Atlas; precomputed stats mean: 1.53. ABC Atlas HPF/GABA/Chrna2 filter retains Sst Gaba_3 (unlike Sst Gaba_6). Chrna2 expression is present but scattered across clusters within this supertype — consistent with partial OLM cell representation.

- Sst Gaba_3 supertype contains at least three classical hippocampal cell types: OLM cells, bistratified cells, and HS cells. These are not separable at supertype level. This supertype-level edge reflects the best available resolution from atlas metadata alone. Cluster-level resolution of OLM cells within this supertype requires MapMyCells annotation transfer or Chrna2-Cre targeting.
- Prosubiculum (259 cells) and posterior amygdala (780 cells) are prominent in this supertype; classical OLM characterisation is primarily in CA1. The non-hippocampal cells in this supertype likely include non-OLM Sst interneurons.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | Atlas metadata | PARTIAL |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | Atlas metadata | SUPPORT |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Friend et al. 2019 · PMID:30987110 | [30987110](https://pubmed.ncbi.nlm.nih.gov/30987110/) | soma location |
| [2] | Tecuatl et al. 2020 · PMID:33361464 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | soma location |
| [3] | Bezaire et al. 2016 · PMID:28009257 | [28009257](https://pubmed.ncbi.nlm.nih.gov/28009257/) | soma location |
| [4] | Winterer et al. 2019 · PMID:31420995 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | soma location |
| [5] | Leão et al. 2012 · PMID:23042082 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | soma location |
| [6] | Nichol et al. 2018 · PMID:29487503 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | soma location |
| [7] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | soma location |
| [8] | Chamberland et al. 2023 · PMID:37162922 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Sst marker |
