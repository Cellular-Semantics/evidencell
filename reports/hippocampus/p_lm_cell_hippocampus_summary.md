# Pyramidale-lacunosum moleculare (P-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | stratum pyramidale [UBERON:0014548] |  |
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

- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. SUPT_0219 (Sst Gaba_6) is the dominant supertype target for Sst HIP cells (F1=0.759, 161/273 cells). P-LM cells are Sst+ interneurons in stratum lacunosum-moleculare; SUPT_0219 being the dominant Sst target is consistent with this assignment, but subtype resolution requires a P-LM-specific dataset. Yao 2021 SSv4 'Sst' subclass (n=273 HIP cells) encompasses multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, oriens-oriens, and others); subtype resolution requires a dataset with morphologically identified Sst-IN labels. [Annotation transfer]

**Concerns:**

- **location_stratum_pyramidale** (DISCORDANT): A=stratum pyramidale (SOMA) / B=CA3 pyramidal layer (261 cells); no CA1 pyramidal layer. P-LM cell described in CA1; SUPT_0219 has no CA1 representation in atlas metadata. CA3 pyramidal layer cells present but classical type not documented in CA3.

- SUPT_0219 is a CA3-enriched supertype with no CA1 representation. The P-LM cell is a CA1 type described in stratum pyramidale. This is the primary source of uncertainty. A CA1-enriched Sst supertype (e.g., SUPT_0216) may be a better match, but the soma in stratum pyramidale (not oriens) motivated this distinct candidate.
- P-LM cell described in a single study (Oliva et al. 2000, PMID:10818134). Not transcriptomically characterised. May be the same transcriptomic type as R-LM cells; the two types were described together in one study and may not be separable.
- R-LM and P-LM were identified in the same study and differ only in soma laminar position (stratum oriens vs stratum pyramidale). Whether they constitute distinct transcriptomic types or a single type with variable soma location is unknown.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | Atlas metadata | WEAK |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Oliva et al. 2000 · PMID:10777798 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst marker |
