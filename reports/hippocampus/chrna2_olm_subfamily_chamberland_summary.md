# Chrna2-IN (Chrna2-OLM, Chamberland 2024) — WMBv1 Mapping Report
*2026-05-12 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0005371] | [1] |
| NT | GABAergic | [1] |
| Markers | Sst+, Chrna2+ | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0771 Sst Gaba_3 [CS20230722_CLUS_0771] | 0216 Sst Gaba_3 | 394 |  |  |

All edges: `skos:closeMatch`

---

## 0771 Sst Gaba_3 · 

*`CS20230722_CLUS_0771` · 394 cells (10x) · supertype: 0216 Sst Gaba_3*

**Supporting evidence:**

- Chamberland Chrna2-IN cells (Harris 2018 cells satisfying the per-cluster Sst+/Chrna2+ rule, n=153) concentrate in CLUS_0771 Sst Gaba_3 (F1=0.65, recall 0.81, precision 0.54). At supertype the population scatters into SUPT_0216 Sst Gaba_3 with high recall (0.95) but low precision (0.20), consistent with multiple Sst types being grouped at this supertype. Cluster-level resolution is the right summary — F1 rises with finer aggregation (rises_with_resolution monotonicity). [Annotation transfer]

**Concerns:**

- **marker_Chrna2** (APPROXIMATE): A=Chrna2 — defining marker / B=scattered Chrna2 in Sst Gaba_3 cluster. Chrna2 expression is sparse but enriched in CLUS_0771 relative to siblings.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: F1=0.649 ≤ 0.75 → closeMatch. Curator review recommended.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_chrna2_olm_to_CS20230722_CLUS_0771 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | soma location |
