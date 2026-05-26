# entorhinal cortex layer II calbindin-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | entorhinal cortex layer II [UBERON:0002728] | [1] [2] [3] |
| NT | glutamatergic | [4] |
| Markers | Calb1+ | [4] [5] |

---

## Cell Ontology mapping

entorhinal cortex layer II calbindin-positive pyramidal cell is a **broad match** to **pyramidal neuron (CL:0000598)** in the Cell Ontology — i.e. **pyramidal neuron (CL:0000598)** is the closest existing CL term (an ancestor) but does not fully cover this type. A new child term is a candidate for submission to CL.

*Mapping notes:* EC layer II calbindin-positive pyramidal cells originate widespread telencephalic and intrinsic projections and show strong theta modulation. Arranged in a hexagonal patch grid in medial EC. CL:0000598 (pyramidal neuron) is the best available match; no EC layer II pyramidal-specific CL term exists.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0052 L2 IT ENT-po Glut_2 [CS20230722_SUPT_0052] |  | 857 |  |  |

All edges: `skos:closeMatch`

---

## 0052 L2 IT ENT-po Glut_2 · 

*`CS20230722_SUPT_0052` · 857 cells (10x)*

**Supporting evidence:**

- Annotation transfer of Yao 2021 (GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722) via local MapMyCells. Yao 2021 'L2 IT ENTm' subclass cells (n=42), representing medial entorhinal cortex layer II IT neurons (principally calbindin-positive pyramidal cells), map to SUPT_0052 (L2 IT ENT-po Glut_2) with coverage=0.595 and F1=0.694. SUPT_0054 (L2 IT ENT-po Glut_4) accounts for a further 33.3% of L2 IT ENTm cells. Together SUPT_0052 and SUPT_0054 cover 92.8% of L2 IT ENTm cells. Note: n=42 is a small sample; results should be interpreted with appropriate caution. The 'ENT-po' designation (entorhinal postrhinal) encompasses medial EC and postrhinal cortex layer II populations. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=entorhinal cortex layer II (UBERON:0002728, compartment: SOMA) / B=SUPT_0052 in L2 IT ENT-po (entorhinal postrhinal) subclass. Medial EC layer II calbindin-positive pyramidal cells are the primary cell type in this mapping. The 'ENT-po' designation covers medial EC and postrhinal cortex; classical EC layer II pyramidal cells are restricted to medial EC.

- Small sample size (n=42 L2 IT ENTm cells) limits statistical confidence. SUPT_0052 and SUPT_0054 together cover 92.8% of L2 IT ENTm cells, suggesting the classical EC layer II pyramidal cell TYPE_A_SPLITS across these two supertypes. A second edge to SUPT_0054 (F1=0.500) would be appropriate when more data are available.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: F1=0.694 ≤ 0.75, existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Does Calb1 expression distinguish SUPT_0052 from SUPT_0042 (stellate)? Precomputed expression check for Calb1 and Reln in SUBT_011 (ENT-po) vs SUBC_009 (PIR-ENTl) supertypes would resolve the stellate/pyramidal distinction at the atlas level.

- *Proposed:* Obtain more medial EC layer II cells (larger HPF dataset with EC) to improve statistical confidence for L2 IT ENTm→SUPT_0052 mapping.


---

## Proposed experiments

### 1 — Other

- Obtain more medial EC layer II cells (larger HPF dataset with EC) to improve statistical confidence for L2 IT ENTm→SUPT_0052 mapping.
*Resolves: edge_ec_layer2_pyramidal_cell_hippocampus_to_supt_0052*

---

## Open questions

1. Does Calb1 expression distinguish SUPT_0052 from SUPT_0042 (stellate)? Precomputed expression check for Calb1 and Reln in SUBT_011 (ENT-po) vs SUBC_009 (PIR-ENTl) supertypes would resolve the stellate/pyramidal distinction at the atlas level.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ec_layer2_pyramidal_cell_hippocampus_to_supt_0052 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2019 · PMID:31680885 | [31680885](https://pubmed.ncbi.nlm.nih.gov/31680885/) | soma location |
| [2] | Unknown 2018 · PMID:30209250 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250/) | soma location |
| [3] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | soma location |
| [4] | Naumann et al. 2015 · PMID:26223342 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342/) | neurotransmitter type |
| [5] | Unknown 2010 · PMID:20512133 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133/) | Calb1 marker |
