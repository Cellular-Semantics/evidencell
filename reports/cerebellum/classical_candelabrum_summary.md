# Candelabrum cell — WMBv1 Mapping Report
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
| CL term | candelabrum cell (CL:4042030) | |
| Soma location | Cerebellar cortex, Purkinje layer [MBA:1145] |  |
| NT | GABA |  |
| Markers | Nxph1+, Aldh1a3+ | [1] |
| Negative | Slc6a5− | |

---

## Cell Ontology mapping

Candelabrum cell is mapped to **candelabrum cell (CL:4042030)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:4042030 (candelabrum cell) was created based on Osorno et al. 2022 and describes exactly this type. The CL definition notes "A GABAergic interneuron located in the Purkinje layer of the cerebellar cortex... beaded axons that make local synapses contacts within the molecular layer."

**Proposed CL term:** *candelabrum cell* (ACCEPTED)

> A GABAergic interneuron of the cerebellar cortex Purkinje layer with an ascending axon collateral projecting into the molecular layer. Reference transcriptomic data for this type can be found in WMBv1 in cell set CS20230722_CLUS_5178.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | PLI1 (Osorno 2022 / Candelabrum) |  | — |  |  |

All edges: `skos:exactMatch`

---

## PLI1 (Osorno 2022 / Candelabrum) · 

**Supporting evidence:**

- Osorno 2022 establishes PLI1 = Candelabrum cell via three converging lines of evidence: (1) Oxtr-Cre×Ai14 transgenic labels cells with confirmed CC morphology (small soma ~10 μm in PCL, dendrites to pia, beaded axon in ML; Fig 1, 2-photon fill with Alexa-594). (2) snRNA-seq identifies PLI1 as Nxph1+/Aldh1a3+/Slc6a5−, distinct from PLI2 (Globular) and PLI3 (Lugaro) which both express Slc6a5. (3) smFISH on tissue (Fig 3) confirms PLI1 molecular profile co-localises with tdTomato+ CC distribution in the PCL. PLI2 and PLI3 are excluded by morphology (different soma shape/location) and by Slc6a5 expression. Additional molecular validation: Grin1/Grin2b expression in PLI1 confirmed by NMDA receptor currents in electrophysiology on Oxtr-Cre-labelled CCs (Fig 4). [Literature] [1]
- Schilling 2023 review independently confirms PLI1=CC correspondence, citing both Kozareva 2021 and Osorno 2022. Also notes CCs are "purely GABAergic (i.e., not using glycine as a (co-) transmitter)" (citing Simat 2007), and raises Nrp1 expression as an open developmental question distinguishing CC axon targeting from basket cell targeting. [Literature] [2]

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_candelabrum_to_pli1 | Literature [1] | SUPPORT |
| edge_candelabrum_to_pli1 | Literature [2] | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:35578131 | [35578131](https://pubmed.ncbi.nlm.nih.gov/35578131/) | Nxph1 marker |
| [2] | PMID:37940705 | [37940705](https://pubmed.ncbi.nlm.nih.gov/37940705/) | Schilling 2023 review independently confirms PLI1=CC correspondence, citing both |
