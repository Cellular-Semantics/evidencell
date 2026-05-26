# Trilaminar cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic |  |
| Markers | Pvalb+, M2R+ |  |
| Negative | Sst− | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] |  | 2,860 |  |  |

All edges: `skos:closeMatch`

---

## 0206 Pvalb Gaba_2 · 

*`CS20230722_SUPT_0206` · 2,860 cells (10x)*

**Supporting evidence:**

- Pvalb Gaba_2 supertype is enriched in CA1 stratum oriens (493 cells) and CA3 stratum oriens (152 cells), consistent with the trilaminar cell soma location in stratum oriens. Pvalb subclass is consistent with the PV+/Sst- marker profile of the trilaminar cell. However, the trilaminar cell is defined by long-range projection to subiculum and medial septum and a unique burst-firing pattern — properties that cannot be assessed from atlas metadata alone. SUPT_0206 likely contains multiple PV+ interneuron types including PV basket cells, making overlap partial. [Atlas metadata]
- Precomputed stats cross-check: defining markers confirmed (Pvalb=8.74, Chrm2/M2R=4.52), but negative marker Sst expressed at 2.72. Low-level Sst in a Pvalb supertype is not unexpected (some Pvalb interneurons co-express Sst at low levels) but weakens the negative marker constraint. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Pvalb subclass (n=66 HIP cells) onto WMBv1. SUPT_0206 (Pvalb Gaba_2) receives 12/66 Pvalb cells (F1=0.324, purity=0.800). Trilaminar cells are reported to be PV+ in some studies; the Pvalb population partially supporting SUPT_0206 is consistent with this, though the chandelier/AAC supertypes receive stronger hits. PARTIAL: the SSv4 Pvalb label is a mixed population and trilaminar cell identity cannot be confirmed from this AT alone. Yao 2021 SSv4 'Pvalb' subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells; subtype resolution requires a morphologically identified PV-IN dataset. [Annotation transfer]

**Concerns:**

- SUPT_0206 (Pvalb Gaba_2) is the same supertype assigned to PV basket cells. The trilaminar cell and PV basket cell share Pvalb expression and stratum oriens soma location; this supertype likely contains both types (and possibly axo-axonic cells). No transcriptomic features distinguishing trilaminar cells from other PV+ interneurons are available in the atlas metadata.
- The key discriminating marker M2R (Chrm2) is not represented in SUPT_0206 defining markers. Long-range projection identity cannot be assessed from metadata.
- Trilaminar cell is well-documented by Katona et al. 2017 (Somogyi lab) but transcriptomic identity has not been independently confirmed.
- Negative marker Sst shows low expression (2.72) in SUPT_0206. Classical trilaminar cells are defined as Sst-negative, but low-level Sst co-expression in Pvalb types is known. Does not disqualify the mapping but reduces confidence in Sst as a discriminating marker.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: F1=0.119 ≤ 0.75, existing caveats → closeMatch. Curator review recommended.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | Atlas metadata | PARTIAL |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | Atlas metadata | PARTIAL |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Katona et al. 2017 · PMID:27997999 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | soma location |
