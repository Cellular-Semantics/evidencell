# Ndnf::Nkx2-1-IN (Ndnf-OLM, Chamberland 2024) — WMBv1 Mapping Report
*2026-05-12 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum oriens [UBERON:0005371] | [1] |
| NT | GABAergic | [1] |
| Markers | Sst+, Ndnf+, Nkx2-1+ | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] |  | 2,712 |  |  |

All edges: `evidencell:UncertainRelationship`

---

## 0216 Sst Gaba_3 · 

*`CS20230722_SUPT_0216` · 2,712 cells (10x)*

**Supporting evidence:**

- Chamberland Ndnf::Nkx2-1-IN cells (n=19 in this Harris re-labelling) do NOT concentrate at any single WMBv1 cluster or supertype — the population is fragmented across Lamp5, Sncg, and Sst types with F1 below 0.1 everywhere. The per-cluster Ndnf threshold qualified only one Harris Class, so the source pool is small and noisy. Cannot make a confident WMBv1 assignment from this AT evidence alone. UNCERTAIN; await targeted Ndnf::Nkx2-1 patch-seq. [Annotation transfer]

**Concerns:**

- **marker_Sst** (APPROXIMATE): A=Sst — defining (subset) / B=Sst expressed in Sst Gaba_3 supertype. Mapping to SUPT_0216 is the strongest Sst-positive hit, but per-cell evidence is too sparse to be informative.
- Ndnf::Nkx2-1-IN signal fragments across multiple WMBv1 targets with F1 < 0.1 each. Mapping at any single level is uninformative. Better source-side evidence (e.g. Chamberland 2024's published per-cell Ndnf::Nkx2-1 scRNA-seq if available) needed to firm this up.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ndnf_nkx2_1_olm_to_CS20230722_SUPT_0216 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 · PMID:38640347 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | soma location |
