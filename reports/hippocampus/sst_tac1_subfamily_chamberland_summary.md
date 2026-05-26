# Sst::Tac1-IN (bistratified-like, Chamberland 2024) — WMBv1 Mapping Report
*2026-05-12 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0005371] | [1] |
| NT | GABAergic | [1] |
| Markers | Sst+, Tac1+ | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 052 Pvalb Gaba [CS20230722_SUBC_052] |  | 44,322 |  |  |

All edges: `skos:closeMatch`

---

## 052 Pvalb Gaba · 

*`CS20230722_SUBC_052` · 44,322 cells (10x)*

**Supporting evidence:**

- Chamberland Sst::Tac1-IN cells (n=167) map dominantly to the Pvalb Gaba subclass (F1=0.58, recall 0.78) despite being Sst-expressing in source — surfaces transcriptomic Sst-Pvalb continuity for bistratified-type cells that target fast-spiking interneurons. At cluster level the population distributes across multiple Pvalb Gaba_2 clusters (CLUS_0737 highest with F1=0.47). PARTIAL_OVERLAP reflects that Sst::Tac1 by functional definition spans multiple WMBv1 Pvalb clusters, not a single one. [Annotation transfer]

**Concerns:**

- **marker_Sst** (APPROXIMATE): A=Sst — defining marker / B=Sst not in Pvalb subclass defining set; transcriptomic continuity. MapMyCells assigns Sst::Tac1 cells to Pvalb subclass despite source Sst expression — Sst-Pvalb continuity.
- **target_partner** (APPROXIMATE): A=Fast-spiking Pvalb interneurons (interneuron-selective) / B=(Pvalb cluster — postsynaptic target not directly annotated on atlas). Functional target (Pvalb-INs per Chamberland 2024) and transcriptomic placement (Pvalb cluster) are independently consistent but not strictly equivalent.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: F1=0.578 ≤ 0.75 → closeMatch. Curator review recommended.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_sst_tac1_to_CS20230722_SUBC_052 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | soma location |
