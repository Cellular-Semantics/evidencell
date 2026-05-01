# Hippocampo-septal (HS) cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | sst chodl GABAergic interneuron (CL:4023121) | |
| Soma location | CA1 stratum oriens [UBERON:0005383] | [1] [2] [3] [4] |
| NT | GABAergic |  |
| Markers | Sst+ | [1] [5] [6] |
| Neuropeptides | Sst |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## 0216 Sst Gaba_3 · 🔴 LOW

**Supporting evidence:**

- Sst Gaba_3 supertype is MGE-derived Sst+ GABA interneuron in hippocampal stratum oriens (CA1 SO: 818 cells, largest single location). HS cell is Sst+ GABAergic with soma in CA1 stratum oriens — both properties match. However, the supertype also captures OLM cells and potentially bistratified cells; the HS-specific feature (long-range projection to medial septum) is not resolvable from atlas metadata. The Reln defining marker of SUPT_0216 is inconsistent with HS cell identity (Reln is an OLM marker). This is a shared supertype with OLM and other SO interneurons, not an HS-specific target. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. Sst cells map strongly to SUBC_053 (F1=0.983) at SUBCLASS level. At SUPERTYPE level, SUPT_0216 (Sst Gaba_3) receives 83/273 Sst cells (F1=0.488, target_purity=1.0). PARTIAL: hippocampo-septal cells are Sst+ long-range projection neurons; the Sst SSv4 label is mixed and cannot discriminate this cell type. SUPT_0219 (Sst Gaba_6) is the dominant Sst supertype target (F1=0.759) and may be a better correspondent for some Sst subtypes. Yao 2021 SSv4 'Sst' subclass (n=273 HIP cells) encompasses multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, oriens-oriens, and others); subtype resolution requires a dataset with morphologically identified Sst-IN labels. [Annotation transfer]

**Concerns:**

- **marker_Reln** (DISCORDANT): A=not listed — not a HS defining marker / B=Reln — DEFINING marker of SUPT_0216; precomputed stats mean: 7.9. Reln is a known OLM marker (Chrna2::Reln coexpression confirmed). Its presence as a defining marker of this supertype is consistent with OLM but not expected for HS cells. May indicate SUPT_0216 predominantly captures OLM-like cells.

- SUPT_0216 (Sst Gaba_3) is a shared supertype: MapMyCells annotation transfer of OLM interneurons (GSE124847) maps 43/46 OLM cells to this supertype with F1=0.67. Bistratified cells (Pvalb/Sst/Tac1+) may also contribute. HS-specific long-range projection identity cannot be verified from atlas metadata.
- The Reln defining marker of SUPT_0216 is an OLM marker, not an HS marker. This may indicate the supertype predominantly captures OLM rather than HS cells.

**What would upgrade confidence:**

- *Unresolved:* Does SUPT_0216 contain any long-range projecting Sst+ neurons or is it exclusively local-circuit (OLM)?
- *Unresolved:* Is there a more appropriate HS candidate outside the Sst Gaba_3 supertype (e.g. Chodl+ class)?

---

## Open questions

1. Does SUPT_0216 contain any long-range projecting Sst+ neurons or is it exclusively local-circuit (OLM)?
2. Is there a more appropriate HS candidate outside the Sst Gaba_3 supertype (e.g. Chodl+ class)?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | Atlas metadata | PARTIAL |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.1101/598599 | — | soma location |
| [2] | Müller & Remy 2017 · PMID:29250747 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | soma location |
| [3] | Perez et al. 2020 · PMID:33404500 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [4] | Oren et al. 2009 · PMID:19176803 | [19176803](https://pubmed.ncbi.nlm.nih.gov/19176803/) | soma location |
| [5] | Takács et al. 2024 · PMID:38470935 | [38470935](https://pubmed.ncbi.nlm.nih.gov/38470935/) | Sst marker |
| [6] | Katona et al. 2017 · PMID:27997999 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | Sst marker |
