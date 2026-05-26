# PLI3 (Osorno 2022 / Lugaro) — WMBv1 Mapping Report
*2026-02-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/cerebellum/CB_PLI_types.yaml`*

---

> **Location note.** WMBv1 location data derives from MERFISH spatial
> registration and records **soma position** only. Axonal and dendritic
> projection targets are not reflected in atlas cluster location fields and
> are not used in mapping assessments.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location |  |  |
| NT | GABA-Glyc |  |
| Markers |  |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | CB PLI Gly-Gaba_2 (supertype 1145) [CS20230722_SUPT_1145] |  | 254 |  |  |

All edges: `skos:exactMatch`

---

## CB PLI Gly-Gaba_2 (supertype 1145) · 

*`CS20230722_SUPT_1145` · 254 cells (10x)*

**Supporting evidence:**

- MapMyCells annotation transfer of PLI3 (Lugaro) cells to WMBv1 shows clean mapping at supertype level (1145 CB PLI Gly-Gaba_2): coverage=0.94, purity=0.98, F1=0.96. Cluster-level mapping is less clean (coverage only 49% to cluster 5180), indicating PLI3 cells distribute across the 2-3 clusters within supertype 1145. NT prediction (GABA-Glyc) is consistent with Lugaro co-transmission. [Annotation transfer]

**Concerns:**

- Clean mapping is at supertype level (1145), not cluster level. Individual WMBv1 clusters 5180-5182 within this supertype each receive only a fraction of PLI3 cells. The biological basis for this intra-supertype heterogeneity is not yet characterised.

**What would upgrade confidence:**

- *Proposed:* Sub-cluster analysis of supertype 1145 with additional markers (particularly MERFISH-compatible probes) to determine if the intra-supertype variation corresponds to identifiable biological differences in Lugaro cells.


---

## Proposed experiments

### 1 — MERFISH / spatial transcriptomics

- Sub-cluster analysis of supertype 1145 with additional markers (particularly MERFISH-compatible probes) to determine if the intra-supertype variation corresponds to identifiable biological differences in Lugaro cells.
*Resolves: edge_pli3_to_wmb1145*

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_pli3_to_wmb1145 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
