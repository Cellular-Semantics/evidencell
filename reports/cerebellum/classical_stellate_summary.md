# Cerebellar stellate cell — WMBv1 Mapping Report
*2026-02-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/cerebellum/CB_MLI_types.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | cerebellar stellate cell (CL:0010010) | |
| Soma location | Cerebellar cortex, molecular layer (outer third) [MBA:1144] |  |
| NT | GABA |  |
| Markers |  |  |

---

## Cell Ontology mapping

Cerebellar stellate cell is mapped to **cerebellar stellate cell (CL:0010010)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:0010010 (cerebellar stellate cell) is the exact CL term for this type. Kozareva 2021 shows that distal MLI1 and distal MLI2 both have stellate morphology, so both transcriptomic types partially correspond to the classical stellate definition. The CL term captures the morphological type without implying transcriptomic uniformity.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | MLI1 (Kozareva 2021) |  | — |  |  |
| — | MLI2 (Kozareva 2021) |  | — |  |  |

All edges: `evidencell:PartialOverlapMatch`

---

## MLI1 (Kozareva 2021) · 

**Supporting evidence:**

- Distal MLI1 cells have stellate morphology, meaning classical stellate cells (defined by outer ML location + star-shaped morphology) partially overlap with MLI1. However, distal MLI2 cells also have stellate morphology, so stellate → PARTIAL_OVERLAP with both MLI1 and MLI2. [Literature] [1]

**Concerns:**

- The fraction of classical stellate cells in MLI1 vs MLI2 is not precisely quantified by Kozareva 2021 — the split is described qualitatively as location-dependent. Quantitative spatial analysis needed.

---

## MLI2 (Kozareva 2021) · 

**Supporting evidence:**

- Distal MLI2 cells have stellate morphology, confirming partial overlap with the classical stellate type. MLI2 near the PC layer has a distinct morphology (not basket). Together with edge_stellate_to_mli1, this means the classical stellate type is distributed across both MLI1 and MLI2 transcriptomic types. [Literature] [1]

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_stellate_to_mli1 | Literature [1] | SUPPORT |
| edge_stellate_to_mli2 | Literature [1] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:34616064 | [34616064](https://pubmed.ncbi.nlm.nih.gov/34616064/) | Distal MLI1 cells have stellate morphology, meaning classical stellate cells (de |
