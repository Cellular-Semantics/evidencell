# Dentate Gyrus Type-2b Neural Progenitor — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

The Dentate Gyrus Type-2b Neural Progenitor is a transitional amplifying progenitor of the adult dentate gyrus neurogenesis lineage. It occupies the intermediate position between the Nestin+/Sox2+ type-2a progenitor and the DCX-high type-3 neuroblast. The canonical molecular identity is defined by co-expression of Nestin, DCX (at low levels), and the T-box transcription factor Eomes (Tbr2). Cells reside in the subgranular zone (SGZ) and have not yet achieved postmitotic status, explaining the absence of NeuN and Calbindin.

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus subgranular zone [UBERON:0009952] | [1][2] |
| Neurotransmitter | Glutamatergic (lineage committed, not yet functional) | — |
| Defining markers | Nestin, DCX (low), Eomes (Tbr2) | [1][2] |
| Negative markers | NeuN, Calbindin | — |
| Neuropeptides | None reported | — |
| CL term | dentate gyrus type-2b neural progenitor (CL:9900004) — EXACT | — |

**Morphology notes.** Transitional progenitor co-expressing Nestin and DCX at low levels. Tbr2/Eomes+ cells cluster in the SGZ and are often found in close proximity to radial processes of type-1 cells. Short tangential processes are typical of type-2 morphology. Hodge et al. 2008 [1] showed that 64% of Tbr2+ SGZ cells co-label with DCX.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] | — | — | 🟡 MODERATE | Eomes CONSISTENT · NT Glut CONSISTENT · SGZ location CONSISTENT · DCX APPROXIMATE | Best candidate |

---

## 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511]

### Supporting evidence

- Atlas curator CL mapping for cluster 0511 is BROAD to CL:9900004 (dentate gyrus type-2b neural progenitor), with the annotation "early neuroblast", placing this cluster at the type-2b/type-3 boundary [atlas metadata].
- **Eomes (Tbr2) — primary molecular anchor.** Eomes is listed as a defining marker of cluster 0511 in the atlas differential marker set. Hodge et al. 2008 [1] established Tbr2/Eomes as the canonical type-2b intermediate progenitor transcription factor by IHC, making this the strongest single-gene alignment between the classical cell type and the transcriptomic cluster.
- Hodge et al. 2008 [1] documented that 64% of Tbr2+ SGZ cells co-label with DCX at low expression, with short tangentially oriented processes characteristic of type-2 morphology. Verbatim from the paper: "The majority of Tbr2+ cells colabeled with DCX (64.4 ± 4.7%). In general, these cells had low DCX expression, with either no processes or short, tangentially oriented processes, typical of type-2 cells." (Hodge et al. 2008, Characterization of Tbr2+ cells in the SGZ [1]).
- Micheli et al. 2025 [2] (review) confirms the canonical type-2b molecular signature (Nestin+/DCX+) that cluster 0511 anchors transcriptomically via Eomes. The lineage progression described is: "Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + )" (Micheli et al. 2025, Dentate Gyrus Immature Neurons [2]).
- Additional TF markers Sox6, Neurod1, Meis1/2, and Igfbpl1 corroborate the early neurogenesis stage of cluster 0511.
- Neurotransmitter identity is CONSISTENT: cluster 0511 expresses Slc17a6 (vGLUT2; MERFISH score 6.02), consistent with glutamatergic lineage commitment of the classical type-2b progenitor.
- Negative marker consistency: NeuN and Calbindin are absent from cluster 0511 defining markers, consistent with the progenitor (premitotic) stage definition of the classical type.
- MERFISH validates Eomes and Igfbpl1 expression at the DG-STR boundary, corresponding to the SGZ *(note: DG-STR boundary in MERFISH coordinates is interpreted as the anatomical subgranular zone [UBERON:0009952])*.

### Concerns

- **DCX alignment is APPROXIMATE.** DCX protein is expressed at low levels in type-2b progenitors (classical definition), but Dcx mRNA is absent from the cluster 0511 differential defining markers. This reflects a known methodological gap: low-abundance transcripts are filtered out during cluster-level differential marker selection; protein and mRNA abundance do not track linearly for structural proteins. This is methodological, not biological, discordance.
- **Nestin alignment is NOT_ASSESSED.** Nestin/Nes mRNA is broadly expressed across progenitor populations and is likely filtered from cluster-level differential marker selection. Its absence from the atlas defining markers does not imply absence from the cells.
- **Cluster 0511 spans the type-2b/type-3 boundary.** The curator annotation "early neuroblast" and the presence of Neurod1 — a transcription factor expressed from the neuroblast stage onward — indicate that some cells within this cluster may have already progressed past the type-2b stage. The PARTIAL_OVERLAP relationship reflects that type-2b progenitors are the dominant population, but the cluster is not exclusive to this stage.
- **MERFISH registration uncertainty.** CCF broad annotation reports NA:0.75 and CTXsp:0.12 for cluster 0511. MERFISH label "DG STR" places cells at the DG-STR boundary (SGZ), but CCF soma location cannot be fully verified. The high NA fraction is a known artefact of sparse CCF coverage at the SGZ margin *(note: MERFISH label is considered the reliable anatomical assignment here)*.
- **Minor GABAergic signal.** Gad2 MERFISH score 3.24 is detectable in cluster 0511. Whether this reflects ambient RNA contamination, a minor GABAergic cell contaminant, or transient GABAergic signalling in type-2b progenitors is unresolved.

### What would upgrade confidence

- Triple-label smFISH combining Eomes, Sox6, and Nes transcripts with Tbr2 IHC to confirm co-localisation of the cluster 0511 transcriptomic signature with classical Tbr2+/Nestin+ type-2b cells in adult mouse SGZ. This would directly bridge IHC-defined protein expression and atlas-level mRNA markers.
- Tbr2-CreERT2 fate-mapping with snRNA-seq from sorted Tbr2+ cells, followed by MapMyCells projection onto CCN202307220, to assign IHC-defined type-2b cells to specific atlas clusters. This would resolve whether type-2b cells project exclusively to cluster 0511 or distribute across 0511–0513.
- Clarification of the relationship between clusters 0511, 0512, and 0513 as a putative progressive type-2b-to-type-3 transition series, which would determine whether secondary PARTIAL_OVERLAP edges are warranted for the type-2b node.

---

## Proposed experiments

### smFISH / spatial transcriptomics

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Triple-label smFISH: Eomes + Sox6 + Nes transcripts with Tbr2 IHC | Adult mouse SGZ, cluster 0511 signature | Co-localisation of mRNA markers with Tbr2+ IHC-defined type-2b cells | Bridges the protein–mRNA gap; upgrades DCX and Nestin alignment from APPROXIMATE/NOT_ASSESSED to CONSISTENT |

### Genetic fate mapping + snRNA-seq

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Tbr2-CreERT2 fate-mapping with sorted Tbr2+ snRNA-seq + MapMyCells projection | IHC-defined Tbr2+ type-2b cells in adult SGZ | Atlas cluster assignments for sorted Tbr2+ cells | Confirms whether type-2b maps exclusively to 0511 or distributes across 0511–0513; resolves cluster boundary question |

---

## Open questions

1. Do clusters 0512 and 0513 together with 0511 represent a progressive type-2b to type-3 transition series, and if so should the type-2b classical node have secondary PARTIAL_OVERLAP edges to 0512 and 0513?
2. Is the Gad2 signal (MERFISH score 3.24) in cluster 0511 ambient RNA contamination, a minor GABAergic cell contaminant, or evidence of transient GABAergic signalling in type-2b progenitors?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511 | ATLAS_METADATA, LITERATURE (experimental [1]), LITERATURE (review [2]) | SUPPORT |

---

## References

[1] Hodge 2008 · [PMID:18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) · doi:10.1523/JNEUROSCI.4280-07.2008
[2] Micheli 2025 · [PMID:40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) · doi:10.3389/fcell.2025.1605116
