# Dentate Gyrus Neuroblast (Type-3 Progenitor) — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**DRAFT WARNING:** Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.

---

## Classical type

**CL term:** dentate gyrus neuroblast (CL:9900001) · EXACT

**Morphology note.** Migratory precursor cells residing in the SGZ; they migrate only a few micrometres toward the inner granule cell layer. At the type-2b stage they co-express Nestin and DCX; at the type-3 stage they are DCX+ only. They are proliferative (Ki67+) and represent the last mitotic stage before postmitotic differentiation.

**Developmental note.** The developmental sequence distinguishes type-2a (Nestin+/Sox2+), type-2b (Nestin+/DCX+), and type-3 (DCX+) stages. A transcription factor cascade (Pax6 → Ngn2 → Tbr2 → NeuroD → Tbr1) marks stage transitions [2].

---

## Classical type properties

| Property | Value | References |
|----------|-------|------------|
| Soma location | Dentate Gyrus Subgranular Zone [UBERON:0009952] | [1], [2] |
| Neurotransmitter | Glutamatergic (committed but not yet functional) | — |
| Defining markers | DCX (doublecortin), Ki67 (Mki67), PSA-NCAM, Nestin | [3] (DCX, Nestin), [4] (DCX, Ki67) |
| Negative markers | NeuN, Calbindin, GFAP | — |
| Neuropeptides | None recorded | — |
| CL term | dentate gyrus neuroblast (CL:9900001) · EXACT | — |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|------|--------------|-----------|-------|------------|----------------------|---------|
| 1 | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] | DG-PIR Ex IMN_1 (CS20230722_SUPT_0140) | n/a | 🔴 LOW | Eomes/Tbr2 TF CONSISTENT · DCX APPROXIMATE | Speculative |

**Total:** 1 edge · relationship type: PARTIAL_OVERLAP

---

## 0511 DG-PIR Ex IMN_1 · 🔴 LOW

### Supporting evidence

- **Atlas curator annotation "early neuroblast."** Cluster 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] carries an explicit curator label of "early neuroblast", providing direct human-curated alignment with the classical neuroblast cell type.
- **Eomes (Tbr2) transcription factor signature.** The cluster's defining TF markers include Eomes (= Tbr2), Neurod1, Sox6, Meis1/2, and Igfbpl1. Tbr2 is the canonical intermediate progenitor cell marker in the adult SGZ and is specifically localized to transit-amplifying cells in adult hippocampal neurogenesis [2]. Its presence is the strongest molecular link between this cluster and the classical type-2b neuroblast stage.
- **Glutamatergic neurotransmitter identity.** The cluster shows Slc17a6 MERFISH score 6.02, confirming a glutamatergic identity. The classical type is defined as glutamatergic (committed but not yet functional), making this CONSISTENT.
- **MERFISH spatial validation.** MERFISH expression of Eomes and Igfbpl1 is validated at the DG-STR boundary, consistent with the SGZ position defined for the classical type [UBERON:0009952].
- **CL:9900001 mapping on parent supertype.** The cluster is the sole member of supertype CS20230722_SUPT_0140 (DG-PIR Ex IMN_1), which carries a BROAD mapping to CL:9900001 (dentate gyrus neuroblast). This is PARTIAL support — the BROAD designation means the supertype encompasses the concept without guaranteeing cluster-level identity.

### Concerns

- **DCX protein-level marker absent from defining markers (APPROXIMATE).** DCX is the canonical neuroblast marker at the protein level [3][4], but it does not appear in the cluster's defining markers list. This is likely a protein-transcriptome gap: Dcx mRNA may be broadly expressed across the DG-PIR Ex IMN subclass and thus filtered out during cluster-level differential expression selection, rather than reflecting true biological absence. Nonetheless, direct confirmation of Dcx transcript expression in cluster 0511 cells is lacking.
- **Ki67 absent from defining markers (APPROXIMATE).** Ki67/Mki67 is a defining marker of proliferating neuroblasts [4], but is absent from cluster 0511's defining markers. This is partly expected given the known under-capture of rapidly cycling cells in snRNA-seq; a small cluster size is consistent with a rare proliferative population. However, the absence means proliferative status cannot be confirmed from atlas metadata alone.
- **Nestin absent from defining markers (APPROXIMATE).** Nestin expression at the type-2b stage [3] is absent from the cluster's RNA-level markers. This is partially consistent with the biology — Nestin/Nes is downregulated at the type-3 stage — and the Eomes+ TF signature suggests type-2b enrichment, where Nestin would be expected to decrease.
- **PSA-NCAM not assessable (NOT_ASSESSED).** PSA-NCAM is a post-translational glycan epitope intrinsically undetectable by RNA-seq. No transcript-level correlate is available. This property gap is methodologically unavoidable and cannot be resolved from atlas data.
- **Location APPROXIMATE — CCF registration artefact.** CCF broad annotation shows NA:0.75, CTXsp:0.12. The NA (not assigned) fraction reflects a known registration artefact at the sparse SGZ margin rather than genuine extrahippocampal localisation. MERFISH label "DG STR" places cells at the DG-STR boundary, consistent with the SGZ. *(adjacent region — could reflect registration boundary error; weak counter-evidence)*
- **Gad2 signal of uncertain origin.** A Gad2 nt_marker signal (score 3.24) is noted in cluster 0511. Its origin is unresolved: it could represent ambient RNA contamination, a minor contaminating GABAergic subpopulation, or evidence of transient GABAergic signalling in type-2b progenitors. *(note: transient GABAergic signalling in immature granule neurons is reported in the literature, but its relevance to the type-2b stage specifically is not confirmed by the facts in this file.)*
- **Type-2b vs type-3 stage ambiguity.** The classical dg_neuroblast node spans type-2b (Nestin+/DCX+/Eomes+) and type-3 (DCX+/Eomes-low) sub-stages. Cluster 0511 is enriched for type-2b (Eomes+ dominant); correspondence with the type-3 sub-stage is unconfirmed. Cluster 0512 is noted as a secondary candidate for the type-3 transition, but is not evaluated in this report.
- **Methodological gap: protein IHC vs scRNA-seq defining markers.** Classical neuroblast markers (DCX, Ki67, PSA-NCAM, Nestin) are defined by protein IHC. Atlas defining markers are derived from RNA-level differential expression. Protein abundance does not track mRNA linearly for structural proteins, and broadly expressed stage markers are filtered during cluster-level marker selection. APPROXIMATE alignments across multiple markers reflect this systematic methodological gap rather than biological discordance per se.

### What would upgrade confidence

- **Targeted Dcx transcript query** (ExpressionEvidence / atlas feature matrix query): retrieve Dcx expression values in cluster 0511 cells from the full atlas feature matrix. If Dcx is expressed at a level below the differential expression cutoff but above background, this would resolve the DCX APPROXIMATE alignment toward CONSISTENT.
- **Triple-label smFISH** (LiteratureEvidence or in-house ExperimentalEvidence): combine Dcx, Eomes, and Sox6 transcripts with Ki67 IHC in adult mouse DG to directly test co-localisation of the cluster 0511 signature with classical DCX+/Ki67+ neuroblasts in the SGZ.
- **Protein-sorted snRNA-seq + AnnotationTransferEvidence**: DCX-GFP sorted cells from adult DG followed by snRNA-seq and MapMyCells projection onto CCN202307220. This would assign protein-defined neuroblasts to specific atlas clusters with a quantitative F1 score. A target of F1 ≥ 0.80 at the cluster level would upgrade confidence to MODERATE. Expected output: AnnotationTransferEvidence on edge `edge_dg_neuroblast_to_CS20230722_CLUS_0511`. Resolves open questions 1 and 3.
- **Classical node split** (schema-level): splitting the dg_neuroblast node into separate type-2b and type-3 nodes (addressing open question 3) would allow cluster-level correspondence to be evaluated independently for each sub-stage, reducing ambiguity arising from the current broad node definition.

---

## Proposed experiments

No annotation transfer experiments have been completed for this edge. All proposed experiments are genuinely outstanding.

### smFISH multiplex (Dcx / Eomes / Sox6 / Ki67)

- **What:** Triple-label smFISH for Dcx, Eomes, Sox6 transcripts combined with Ki67 protein IHC in adult mouse DG sections.
- **Target:** Co-localisation frequency — if ≥ 80% of DCX+/Ki67+ cells in the SGZ also express Eomes and Sox6 transcripts, that constitutes strong support for the cluster 0511 alignment.
- **Expected output:** LiteratureEvidence or ExperimentalEvidence item on `edge_dg_neuroblast_to_CS20230722_CLUS_0511`.
- **Resolves:** Open question 1 (Dcx transcript in cluster 0511); open question 3 (type-2b vs type-3 sub-stage distribution).

### Protein-sorted snRNA-seq with MapMyCells annotation transfer

- **What:** FACS-isolate DCX-GFP+ cells from adult mouse DG; perform snRNA-seq; project onto Allen Brain Cell Atlas CCN202307220 using MapMyCells.
- **Target:** F1 ≥ 0.80 at CLUSTER level mapping DCX-GFP+ cells to cluster 0511 and/or 0512.
- **Expected output:** AnnotationTransferEvidence on `edge_dg_neuroblast_to_CS20230722_CLUS_0511`; would also assess whether a second edge to cluster 0512 is warranted for the type-3 sub-stage.
- **Resolves:** Open questions 1, 2, and 3.

### Atlas feature matrix Dcx expression query

- **What:** Targeted query of Dcx transcript expression across all cells in cluster 0511 from the full Allen Brain Cell Atlas feature matrix (not the condensed defining_markers list).
- **Target:** Determine mean Dcx expression and fraction of cells with detectable Dcx counts in cluster 0511 vs flanking clusters.
- **Expected output:** ExpressionEvidence item; would upgrade the marker_DCX property comparison from APPROXIMATE toward CONSISTENT or DISCORDANT.
- **Resolves:** Open question 1.

---

## Open questions

1. Does Dcx transcript appear in cluster 0511 cells at a level below the differential expression threshold for defining_marker selection? A targeted Dcx expression query on the full atlas feature matrix would resolve this.
2. Is the Gad2 nt_marker signal (score 3.24) in cluster 0511 ambient RNA, a minor contaminating GABAergic population, or evidence of transient GABAergic signalling in type-2b progenitors?
3. Should the dg_neuroblast classical node be split into separate type-2b and type-3 nodes to match atlas resolution (cluster 0511 for type-2b; cluster 0512 for type-3)?

---

## Evidence base

| Edge ID | Evidence type | Evidence source | Supports |
|---------|--------------|-----------------|----------|
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | ATLAS_METADATA | Atlas curator annotation "early neuroblast"; TF markers Eomes/Neurod1/Sox6; Slc17a6 MERFISH score 6.02 | SUPPORT |
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | ATLAS_METADATA | CL:9900001 BROAD on parent supertype CS20230722_SUPT_0140; Eomes/Tbr2 TF signature | PARTIAL |

**Note:** All evidence for this edge is atlas-metadata derived. No LiteratureEvidence, AnnotationTransferEvidence, or ExperimentalEvidence items are currently recorded.

---

## References

| # | Citation | PMID | Used for |
|---|----------|------|----------|
| [1] | Velusamy 2017 | [28168008](https://pubmed.ncbi.nlm.nih.gov/28168008/) | Soma location (SGZ) |
| [2] | Hodge 2008 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Soma location; Tbr2 intermediate progenitor TF; TF cascade Pax6 → Ngn2 → Tbr2 → NeuroD → Tbr1 |
| [3] | Micheli 2025 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | DCX marker; Nestin marker; type-2a/2b/3 stage definitions |
| [4] | Stepień 2021 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX marker; Ki67 marker; PSA-NCAM; NeuN immature neuron marker |
