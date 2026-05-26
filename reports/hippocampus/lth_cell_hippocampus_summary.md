# Low-threshold high-Ih (LTH) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic |  |
| Markers | Sst+ | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] |  | 1,495 |  |  |

All edges: `evidencell:UncertainRelationship`

---

## 0219 Sst Gaba_6 · 

*`CS20230722_SUPT_0219` · 1,495 cells (10x)*

**Supporting evidence:**

- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. SUPT_0219 (Sst Gaba_6) is the dominant supertype target for Sst HIP cells (F1=0.759, 161/273 cells). LTH (long-tailed horizontal) cells are CA1 interneurons; if Sst+, SUPT_0219 is the most likely atlas correspondent based on this AT. PARTIAL due to mixed Sst population in source. Yao 2021 SSv4 'Sst' subclass (n=273 HIP cells) encompasses multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, oriens-oriens, and others); subtype resolution requires a dataset with morphologically identified Sst-IN labels. [Annotation transfer]

**Concerns:**

- **location_stratum_oriens** (DISCORDANT): A=CA1 stratum oriens (SOMA) / B=CA3 stratum oriens (305 cells); no CA1 stratum oriens. LTH cell described in CA1 stratum oriens; SUPT_0219 has no CA1 SO representation.

- LTH cell is defined exclusively by physiological clustering (Hewitt et al. 2021, PMID:34250732) in a single study. No morphological reconstruction or molecular markers beyond SST-Cre labelling. Transcriptomic identity is entirely unknown; LTH may overlap with oriens-oriens cells (also SST+/Nos1+) or represent a physiological variant within an existing transcriptomic type rather than a distinct type.
- SUPT_0219 is CA3-enriched with no CA1 stratum oriens cells. LTH was characterised in CA1. Anatomical assignment is the main weakness of this edge.
- Single-study (single-lab) evidence for LTH as a distinct cell type. Classification stability across datasets has not been established.
- LTH cells may overlap with OLM cells (both SST+, CA1 SO soma) at the transcriptomic level. If so, SUPT_0216 (not SUPT_0219) would be the correct target. The assignment to SUPT_0219 is a placeholder pending molecular characterisation.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_lth_cell_hippocampus_to_CS20230722_SUPT_0219 | Atlas metadata | WEAK |
| edge_lth_cell_hippocampus_to_CS20230722_SUPT_0219 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hewitt et al. 2021 · PMID:33991454 | [33991454](https://pubmed.ncbi.nlm.nih.gov/33991454/) | soma location |
