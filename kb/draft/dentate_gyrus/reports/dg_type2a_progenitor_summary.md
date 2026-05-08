# Dentate Gyrus Type-2a Neural Progenitor — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical Type

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus subgranular zone [UBERON:0009952] | [1] |
| Neurotransmitter | Glutamatergic (lineage committed, not yet functional) | — |
| Defining markers | Nestin, Sox2 | [1] |
| Negative markers | DCX, GFAP | — |
| CL term | dentate gyrus type-2a neural progenitor (CL:9900003) | — |

**Morphology.** The type-2a progenitor is a non-radial, horizontally oriented intermediate progenitor residing in the subgranular zone [UBERON:0009952]. It is morphologically distinct from the upstream type-1 radial glia-like stem cell, which carries a long radial process. Type-2a cells are actively proliferating (Ki67+) and do not yet express DCX, the marker that distinguishes them from the downstream type-2b stage.

**Lineage context.** The type-2a stage is the first transit-amplifying stage in the adult dentate gyrus neurogenesis lineage, arising from quiescent type-1 radial glia-like stem cells (GFAP+/Sox2+/Nestin+). The progression through this stage and onward is captured verbatim in the literature:

> Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004).
> — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [1] <!-- quote_key: 279046466_998847af -->

---

## No Atlas Cluster Mapping

**No atlas cluster mapping.** The type-2a progenitor stage is not resolved as a distinct cluster in the Allen Brain Cell Atlas CCN202307220. The earliest DG-IMN cluster already expresses Eomes/Tbr2, a type-2b marker, placing it downstream of the type-2a stage. This is a known atlas coverage gap. No mapping edge exists for this node.

---

## Atlas Coverage Gap

### Why this stage is not resolved

The Allen Brain Cell Atlas CCN202307220 dentate gyrus taxonomy does not contain a cluster that corresponds to the type-2a transit-amplifying progenitor. The earliest atlas cluster in the dentate gyrus immature neuron (DG-IMN) lineage — cluster 0511, annotated as DG-PIR Ex IMN_1 — already expresses Eomes/Tbr2. Eomes (also known as Tbr2) is a well-established marker of the type-2b stage, at which point cells have already downregulated the Sox2+/DCX− type-2a profile and begun expressing DCX alongside Nestin. *(note: the assignment of Eomes/Tbr2 expression to the type-2b rather than type-2a stage follows the classical Kempermann/Kronenberg staging scheme as summarised in [1]; this interpretation is consistent with the negative marker profile recorded in the facts file but has not been independently verified against the raw atlas cluster data within this workflow.)*

The gap is likely a consequence of cell abundance and transcriptional similarity: type-2a progenitors are rare relative to more differentiated stages, and their transcriptome may be insufficiently distinct from type-1 stem cells or type-2b progenitors to form a stable cluster boundary in a large-scale single-cell atlas. *(note: this is an interpretation based on general principles of atlas resolution; no cluster-level resolution metrics for the CCN202307220 DG taxonomy have been reviewed in this workflow.)*

The earliest atlas-resolvable stage in this lineage is the type-2b progenitor, mapped to cluster CS20230722_CLUS_0511 (see the edge `edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511`).

### What molecular data would be needed to resolve a type-2a cluster

Resolving the type-2a stage as a discrete cluster in a future atlas iteration would require:

1. **Marker-based cell enrichment.** Prospective isolation or computational enrichment of Nestin+/Sox2+/DCX−/GFAP− cells prior to sequencing would increase the representation of type-2a progenitors relative to the more abundant downstream stages that currently dominate dentate gyrus single-cell datasets.

2. **High-sensitivity transcriptomic profiling.** Because type-2a cells are defined partly by the absence of markers (DCX−, GFAP−) rather than by a unique positive signature, resolving them requires sufficient sequencing depth to distinguish low-level from absent transcripts in each cell. *(note: no quantitative sensitivity threshold is specified here; this reflects general practice in rare-cell single-cell atlas studies.)*

3. **Orthogonal spatial validation.** MERFISH or similar spatially resolved transcriptomic methods applied to the subgranular zone [UBERON:0009952] could confirm that a putative type-2a cluster occupies the expected SGZ position and lacks DCX expression in situ, distinguishing it from adjacent type-1 and type-2b populations.

4. **Lineage tracing integration.** Inducible lineage tracing (e.g., Nestin-CreERT2 combined with temporal scRNA-seq) would allow isolation of cells that have passed through the Sox2+/Nestin+ stage without yet acquiring DCX, providing a ground-truth population for supervised cluster annotation.

---

## References

[1] Micheli et al. 2025 · PMID:40519263 · DOI:10.3389/fcell.2025.1605116
