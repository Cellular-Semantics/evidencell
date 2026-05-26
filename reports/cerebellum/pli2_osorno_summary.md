# PLI2 (Osorno 2022 / Globular) — WMBv1 Mapping Report
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
| — | 5177 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5177] |  | 535 |  |  |

All edges: `skos:closeMatch`

---

## 5177 CB PLI Gly-Gaba_1 · 

*`CS20230722_CLUS_5177` · 535 cells (10x)*

**Supporting evidence:**

- MapMyCells transfer of PLI2 (Globular) cells to WMBv1 shows strongest mapping to cluster 5177 with good precision (83%) but limited recall (93% at cluster level, but only 30% at subclass and 38% at supertype), indicating PLI2 cells distribute across multiple clusters. NT prediction (GABA-Glyc) is consistent with co-transmitting Globular cells. [Annotation transfer]

**Concerns:**

- PLI2 (Globular) cells distribute across multiple WMBv1 clusters within the CB PLI Gly-Gaba subclass (subclass-level purity only 30%), suggesting either transcriptomic heterogeneity within the Globular type or that the classical morphological Globular definition encompasses multiple transcriptomic subtypes.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Do the PLI2 cells mapping to clusters other than 5177 represent a distinct Globular subtype, or is this noise in the annotation transfer?

- *Proposed:* Re-analyse PLI2 cells from SCP795 at higher resolution to determine if the cluster-level heterogeneity reflects a biologically meaningful split.


---

## Proposed experiments

### 1 — Other

- Re-analyse PLI2 cells from SCP795 at higher resolution to determine if the cluster-level heterogeneity reflects a biologically meaningful split.
*Resolves: edge_pli2_to_wmb5177*

---

## Open questions

1. Do the PLI2 cells mapping to clusters other than 5177 represent a distinct Globular subtype, or is this noise in the annotation transfer?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_pli2_to_wmb5177 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
