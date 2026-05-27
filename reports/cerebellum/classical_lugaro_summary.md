# Lugaro cell — WMBv1 Mapping Report
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
| CL term | Lugaro cell (CL:0011006) | |
| Soma location | Cerebellar cortex, Purkinje layer / granule layer border [MBA:1145] |  |
| NT | GABA-Glyc |  |
| Markers |  |  |

---

## Cell Ontology mapping

Lugaro cell is mapped to **Lugaro cell (CL:0011006)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:0011006 (Lugaro cell) is the exact CL term for this type. The CL definition describes "a spindle-shaped or triangular soma, parasagittally oriented and located at the border between the granular layer and the Purkinje cell layer... capable of co-releasing GABA and glycine." This matches the classical description.

**Proposed CL term:** *Lugaro cell* (ACCEPTED)

> A cerebellar interneuron characterized by a spindle-shaped or triangular soma, parasagittally oriented and located at the border between the granular layer and the Purkinje cell layer. The Lugaro cell extends dendrites predominantly in the parasagittal plane, forming synaptic interactions with basket, stellate, and Golgi cells. Its axonal projections extend upward into the molecular layer, where they form a parasagittal plexus and emit long transverse collaterals that run parallel to the long axis of the cerebellar folia. The Lugaro cell is capable of co-releasing GABA and glycine, as evidenced by the expression of glutamate decarboxylase (GAD65/67) and the glycine transporter GlyT2.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | PLI3 (Osorno 2022 / Lugaro) |  | — |  |  |

All edges: `skos:exactMatch`

---

## PLI3 (Osorno 2022 / Lugaro) · 

**Supporting evidence:**

- Osorno 2022 directly maps PLI3 to the classical Lugaro cell type based on soma location, axon morphology, and co-transmission of GABA + glycine. The correspondence is supported by multiple independent features. [Literature] [1]

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_lugaro_to_pli3 | Literature [1] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:35578131 | [35578131](https://pubmed.ncbi.nlm.nih.gov/35578131/) | Osorno 2022 directly maps PLI3 to the classical Lugaro cell type based on soma l |
