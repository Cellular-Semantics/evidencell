# Cerebellar basket cell — WMBv1 Mapping Report
*2026-02-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/cerebellum/CB_MLI_types.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | cerebellar basket cell (CL:2000027) | |
| Soma location | Cerebellar cortex, molecular layer (inner third) [MBA:1144] |  |
| NT | GABA |  |
| Markers |  |  |

---

## Cell Ontology mapping

Cerebellar basket cell is mapped to **cerebellar basket cell (CL:2000027)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:2000027 (cerebellar basket cell) is the exact CL term for this type. The cross-cutting relationship with MLI1 means the classical definition (morphology + location) and the transcriptomic definition (MLI1) do not align — the CL term captures the classical morphological type.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | MLI1 (Kozareva 2021) |  | — |  |  |

All edges: `evidencell:CrossCuttingMatch`

---

## MLI1 (Kozareva 2021) · 

**Supporting evidence:**

- Kozareva 2021 explicitly states that MLI1/MLI2 do not map to the classical basket/stellate boundary. MLI1 cells near the PC layer have basket morphology but MLI1 is not equivalent to basket cells — it also contains distally-located cells with stellate morphology. CROSS_CUTTING is the correct relationship: MLI1 draws from both classical types. [Literature] [1]
- Direct morphological characterisation of MLI1: proximal (inner ML) MLI1 cells have basket morphology, distal MLI1 cells have stellate morphology. This confirms CROSS_CUTTING — the classical basket type is a positional subset of MLI1, not a distinct transcriptomic entity. [Literature] [1]

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_basket_to_mli1 | Literature [1] | SUPPORT |
| edge_basket_to_mli1 | Literature [1] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:34616064 | [34616064](https://pubmed.ncbi.nlm.nih.gov/34616064/) | Kozareva 2021 explicitly states that MLI1/MLI2 do not map to the classical baske |
