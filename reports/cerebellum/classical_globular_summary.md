# Globular cell — WMBv1 Mapping Report
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
| CL term | Purkinje layer interneuron (CL:4072102) | |
| Soma location | Cerebellar cortex, Purkinje layer [MBA:1145] |  |
| NT | GABA-Glyc |  |
| Markers |  |  |

---

## Cell Ontology mapping

Globular cell is a **broad match** to **Purkinje layer interneuron (CL:4072102)** in the Cell Ontology — i.e. **Purkinje layer interneuron (CL:4072102)** is the closest existing CL term (an ancestor) but does not fully cover this type. A new child term is a candidate for submission to CL.

*Mapping notes:* No specific CL term yet for Globular cell. CL:4072102 (Purkinje layer interneuron) is the appropriate broad ancestor — this is also the direct parent of CL:4042030 (candelabrum cell) and CL:0011006 (Lugaro cell). A new term for Globular cell would be placed as a sibling of candelabrum cell within this parent.

**Proposed CL term** (DRAFT)

> A GABAergic/glycinergic interneuron of the cerebellar cortex Purkinje layer with a globular soma morphology, distinct from Lugaro and Candelabrum cells. Reference transcriptomic data for this type can be found in WMBv1 in cell set CS20230722_CLUS_5177 (best mapping) and neighbouring PLI clusters.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | PLI2 (Osorno 2022 / Globular) |  | — |  |  |

All edges: `skos:exactMatch`

---

## PLI2 (Osorno 2022 / Globular) · 

**Supporting evidence:**

- Osorno 2022 defines PLI2 as globular cells based on soma morphology, providing the primary classical-to-T-type correspondence. [Literature] [1]

**What would upgrade confidence:**

- *Unresolved:* The Globular cell type has limited prior classical characterisation compared to Lugaro and Candelabrum. The PLI2 definition is largely Osorno 2022's own contribution — prior classical literature may not have this type explicitly named.


---

## Open questions

1. The Globular cell type has limited prior classical characterisation compared to Lugaro and Candelabrum. The PLI2 definition is largely Osorno 2022's own contribution — prior classical literature may not have this type explicitly named.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_globular_to_pli2 | Literature [1] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:35578131 | [35578131](https://pubmed.ncbi.nlm.nih.gov/35578131/) | Osorno 2022 defines PLI2 as globular cells based on soma morphology, providing t |
