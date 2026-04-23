# Dentate Gyrus Neuroblast (Type-3 Progenitor) — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus neuroblast (CL:9900001) — EXACT | — |
| Soma location | Dentate gyrus subgranular zone [UBERON:0009952] | [1][2] |
| Neurotransmitter | Glutamatergic (committed but not yet functional) | — |
| Defining markers | DCX, Ki67, PSA-NCAM, Nestin | [3][4], [4], —, [3] |
| Negative markers | NeuN, Calbindin, GFAP | — |
| Neuropeptides | None documented | — |

**Morphology and developmental context.** Neuroblasts are migratory precursor cells residing in the subgranular zone [UBERON:0009952]; they migrate only a few micrometres toward the inner granule cell layer. The classical node spans two sub-stages: type-2b (Nestin+/DCX+/Eomes+) and type-3 (DCX+/Eomes-low). A transcription factor cascade (Pax6 > Ngn2 > Tbr2 > NeuroD > Tbr1) marks stage transitions [2]. Neuroblasts are the last proliferative stage before postmitotic differentiation. Electrophysiologically they receive depolarising GABAergic (not glutamatergic) synaptic input and are characterised by high input resistance and small capacitance; glutamatergic output is synaptically silent at this stage *(note: mouse patch-clamp data, Tozuka et al. 2005; Esposito et al. 2005; Ge et al. 2006 — not represented in reference_index)*.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] | DG-PIR Ex IMN_1 (CS20230722_SUPT_0140) | — | 🔴 LOW | NT consistent; soma location approximate (SGZ boundary); DCX/Ki67/Nestin not in cluster defining_markers | Speculative |

**Total:** 1 edge · relationship type: PARTIAL_OVERLAP

---

## 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] · 🔴 LOW

### Supporting evidence

- Atlas curator annotation labels this cluster as "early neuroblast", directly aligned with the classical type name. *(Atlas metadata; PARTIAL_OVERLAP relationship)*
- Transcription factor markers include Eomes (= Tbr2), Neurod1, Sox6, Meis1/2, and Igfbpl1. Tbr2/Eomes is the canonical intermediate progenitor cell (IPC) TF and is specifically localised to intermediate-stage progenitors in the adult SGZ [2].
- The parent supertype CS20230722_SUPT_0140 carries a BROAD CL:9900001 (dentate gyrus neuroblast) mapping, providing a hierarchy-level anchor for this cluster.
- Neurotransmitter identity is CONSISTENT: Slc17a6 MERFISH score 6.02 confirms glutamatergic specification, matching the classical node's committed-but-not-yet-functional glutamatergic designation.
- MERFISH independently validates Eomes and Igfbpl1 expression at the DG-STR boundary, corresponding to the SGZ, consistent with the soma location Dentate gyrus subgranular zone [UBERON:0009952] [1][2].

### Concerns

- **Soma location is APPROXIMATE.** CCF annotation shows NA:0.75 and CTXsp:0.12. MERFISH places cells at the DG-STR (SGZ) boundary, which is broadly consistent, but the high NA fraction is a known registration artefact at the sparse SGZ margin. *(adjacent region — could reflect registration boundary error; weak counter-evidence)*
- **DCX (defining neuroblast marker) is absent from cluster defining_markers.** This is an APPROXIMATE alignment: Dcx mRNA may be broadly expressed across the DG-PIR Ex IMN subclass and not rank as a cluster-distinguishing marker in differential expression analysis. Protein–transcriptome gap for structural proteins is a recognised methodological caveat.
- **Ki67 (proliferation marker) is absent from cluster defining_markers.** Also APPROXIMATE: snRNA-seq systematically under-captures rapidly cycling cells. The small cluster size (n=92) is itself consistent with a rare proliferative population.
- **Nestin is absent from cluster defining_markers.** APPROXIMATE, and partly consistent: Nestin/Nes is downregulated at the type-3 stage; its absence may reflect type-2b-to-type-3 transition rather than a true mismatch given the dominant Eomes+ signature.
- **PSA-NCAM cannot be assessed.** PSA-NCAM is a post-translational glycan epitope, intrinsically undetectable by RNA-seq. No transcript-level correlate is available. Alignment is NOT_ASSESSED.
- **Weak Gad2 signal** (nt_marker score 3.24) is unexplained: could be ambient RNA, minor GABAergic contamination, or transient GABAergic signalling in type-2b progenitors — which would be biologically relevant given the known depolarising GABA responses at this stage.
- **Stage ambiguity.** The classical dg_neuroblast node spans both type-2b (Eomes+) and type-3 (Eomes-low) sub-stages. Cluster 0511 is enriched for type-2b markers (Eomes dominant). Full correspondence with the type-3 sub-stage is unconfirmed; cluster 0512 is noted as a secondary candidate for the type-3 transition.

### What would upgrade confidence

- Triple-label smFISH combining Dcx, Eomes, and Sox6 transcripts with Ki67 IHC in adult mouse DG to directly test co-localisation of the cluster 0511 TF signature with classical DCX+/Ki67+ neuroblasts in the SGZ — this would confirm or refute the protein–transcriptome gap explanation.
- DCX-GFP sorted cells from adult DG followed by snRNA-seq and MapMyCells projection onto CCN202307220, to assign protein-defined neuroblasts to specific atlas clusters and establish whether cluster 0511 (and/or 0512) captures both sub-stages.
- A targeted Dcx expression query on the full atlas feature matrix to determine whether Dcx transcript is present in cluster 0511 cells below the differential expression threshold.
- Clarification of the Gad2 signal source (ambient RNA profiling or doublet detection).

---

## Eliminated candidates

No edges were classified as UNCERTAIN for this mapping graph.

---

## Proposed experiments

### smFISH multiplex panel

- **What:** Triple-label smFISH (Dcx / Eomes / Sox6 transcripts) combined with Ki67 IHC
- **Target:** Co-localisation rate ≥ 70% of DCX+/Ki67+ neuroblasts in the SGZ carrying the Eomes+/Sox6+ TF signature
- **Expected output:** Protein-to-transcript co-expression evidence added to KB, resolving APPROXIMATE alignments for DCX and Ki67 markers
- **Resolves:** DCX and Ki67 APPROXIMATE alignment for edge `edge_dg_neuroblast_to_CS20230722_CLUS_0511`; question of whether cluster 0511 corresponds to type-2b, type-3, or both sub-stages

### Sorted-cell snRNA-seq with MapMyCells projection

- **What:** DCX-GFP FACS sorting from adult mouse DG → snRNA-seq → MapMyCells projection onto CCN202307220
- **Target:** ≥ 80% of protein-defined (DCX+) neuroblasts mapping to cluster 0511 and/or 0512
- **Expected output:** Independent protein-anchored cluster assignment, upgrading confidence from LOW to MODERATE or HIGH
- **Resolves:** Stage ambiguity between type-2b (cluster 0511) and type-3 (cluster 0512); overall confidence for edge `edge_dg_neuroblast_to_CS20230722_CLUS_0511`

### Atlas feature-matrix query (computational)

- **What:** Targeted Dcx expression query on full CCN202307220 feature matrix
- **Target:** Determine whether Dcx transcript is expressed in cluster 0511 cells at sub-threshold levels (e.g. detected in > 20% of cells but below marker selection cutoff)
- **Expected output:** Clarification of APPROXIMATE marker alignment; no new experimental data required
- **Resolves:** Open question 1 (Dcx transcript level in cluster 0511)

---

## Open questions

1. Does Dcx transcript appear in cluster 0511 cells at a level below the differential expression threshold for defining_marker selection? A targeted Dcx expression query on the full atlas feature matrix would resolve this.
2. Is the Gad2 nt_marker signal (score 3.24) in cluster 0511 ambient RNA, a minor contaminating GABAergic population, or evidence of transient GABAergic signalling in type-2b progenitors?
3. Should the dg_neuroblast classical node be split into separate type-2b and type-3 nodes to match atlas resolution (cluster 0511 for type-2b; cluster 0512 for type-3)?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | ATLAS_METADATA (curator annotation "early neuroblast"; Eomes/Neurod1/Sox6 TF markers; CL:9900001 BROAD on supertype) | SUPPORT |
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | ATLAS_METADATA (supertype CL:9900001 BROAD mapping; Eomes/Tbr2 type-2b IPC signature) | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Velusamy 2017 · PMID:28168008 | [28168008](https://pubmed.ncbi.nlm.nih.gov/28168008/) | Soma location (SGZ) |
| [2] | Hodge 2008 · PMID:18385329 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Soma location; Tbr2/Eomes TF cascade in adult SGZ neurogenesis |
| [3] | Micheli 2025 · PMID:40519263 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | DCX marker; Nestin marker; type-2b/type-3 stage definition |
| [4] | Stepień 2021 · PMID:37082558 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX marker; Ki67 marker |

---

### Verbatim source quotes

> "In the hippocampal SGZ, proliferating NSCs develop into intermediate progenitors, which generate neuroblasts or immature neurons. These newly generated immature neurons migrate into the inner granule cell layer (GCL) and differentiate into new granule neurons of the hippocampus (Ming et al., 2005)"
> — Velusamy et al. 2017, Olfactory Bulb Immature Neurons · [1] <!-- quote_key: 13752593_f176b6ad -->

> "Neurogenesis in the adult hippocampus is a highly regulated process that originates from multipotent progenitors in the subgranular zone (SGZ). Currently, little is known about molecular mechanisms that regulate proliferation and differentiation in the SGZ. To study the role of transcription factors (TFs), we focused on Tbr2 (T-box brain gene 2), which has been implicated previously in developmental glutamatergic neurogenesis. In adult mouse hippocampus, Tbr2 protein and Tbr2-GFP (green fluorescent protein) transgene expression were specifically localized to intermediate-stage progenitor cells (IPCs), a type of transit amplifying cells. The Tbr2+ IPCs were highly responsive to neurogenic stimuli, more than doubling after voluntary wheel running. Notably, the Tbr2+ IPCs formed cellular clusters, the average size of which (Tbr2+ cells per cluster) likewise more than doubled in runners. Conversely, Tbr2+ IPCs were selectively depleted by antimitotic drugs, known to suppress neurogenesis. After cessation of antimitotic treatment, recovery of neurogenesis was paralleled by recovery of Tbr2+ IPCs, including a transient rebound above baseline numbers. Finally, Tbr2 was examined in the context of additional TFs that, together, define a TF cascade in embryonic neocortical neurogenesis (Pax6 → Ngn2 → Tbr2 → NeuroD → Tbr1). Remarkably, the same TF cascade was found to be linked to stages of neuronal lineage progression in adult SGZ. These results suggest that Tbr2+ IPCs play a major role in the regulation of adult hippocampal neurogenesis, and that a similar transcriptional program controls neurogenesis in adult SGZ as in embryonic cerebral cortex."
> — Hodge et al. 2008, Dentate Gyrus Immature Neurons · [2] <!-- quote_key: 15727849_56e1c8ef -->

> "Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004)."
> — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [3] <!-- quote_key: 279046466_998847af -->

> "Three types of proliferatively active cells have been identified in the granular layer of the dentate gyrus (DG) of the hippocampus: type I cells -radial glial-like stem cells expressing glial fibrillary acidic protein (GFAP) and Sox2; type II cells -non-sessile cells expressing nestin, also referred to as transiently activated progenitor cells, neuroblasts expressing doublecortin (DCX); and Ki67 proteins and immature neurons expressing the DCX protein, PSA-NCAM, a marker of migrating neurons (polysialylated neuronal cell adhesion molecules) and neuron-specific protein (NeuN) (Attardo et al., 2009)(Gault et al., 2021). On the other hand, three types of cells were distinguished in the subventricular zone (SVZ): B1-type astrocytic stem cells, GFAP-positive, C-type progenitor cells expressing the Mash1 protein, and neuroblasts expressing the DCX protein (Okano et al., 2008)."
> — Stepień et al. 2021, Dentate Gyrus Immature Neurons · [4] <!-- quote_key: 245432259_44d5c91b -->
