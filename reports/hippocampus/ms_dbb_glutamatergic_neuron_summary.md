# medial septal / diagonal band of Broca glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Introduction

Medial septal / diagonal band of Broca (MS-DBB) glutamatergic neurons are a minority projection population of the basal forebrain septal complex — roughly a quarter of the septohippocampal projection — defined by vesicular glutamate transporter expression and an absence of cholinergic and GABAergic markers, with a striking electrophysiological diversity that includes a unique cluster-firing subgroup not seen in other septal cell classes [1]. Their somata sit outside the hippocampal formation proper; the relevance of the type to hippocampal taxonomies lies in their dense, layer-specific axonal projection onto stratum oriens interneurons, where they contribute to hippocampal theta pacing [1][2].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | medial septum / diagonal band of Broca (extrahippocampal soma; UBERON term hippocampal formation [UBERON:0002421] used as nearest umbrella term); synaptic target on interneurons in hippocampus stratum oriens near alveus [UBERON:0005371] | [1] |
| NT | glutamatergic | [1] |
| Defining markers | Slc17a7 (VGluT1), Slc17a6 (VGluT2) | [1], [2] |
| Negative markers | Chat, Gad1 | [1] |
| Electrophysiology | Four VGluT2+ subgroups: fast-spiking, cluster-firing, burst-firing, slow-firing; cluster firing is unique to the glutamatergic population (not GABAergic) | [1], [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Markers + NT identity + negative markers:** review (Müller & Remy 2017) summarising Sotty et al. 2003 single-cell RT-PCR results · [1]
  > Glutamatergic neurons account for approximately 23% of the projections from the medial septum to the hippocampus (Colom et al. 2005). They are characterized by the expression of VGluT1 and/or VGluT2 and by the lack of expression of either ChAT or GAD (Sotty et al. 2003). Electrophysiologically, medial septal glutamatergic neurons form a highly diverse group (Huh et al. 2010; Sotty et al. 2003). The VGluT2 expressing medial septal neurons can be separated into four groups. The first and largest group is formed by the fast spiking neurons, showing only little action potential accommodation and sometimes spontaneous action potential firing (Huh et al. 2010). Remarkably, some of the fast-spiking glutamatergic neurons show a pronounced sag in response to a hyperpolarizing current injection. Similar intrinsic properties can be observed in GABAergic medial septal neurons (Huh et al. 2010). The second group of VGluT2-positive medial septal neurons exhibit a quite specific firing pattern. These neurons fire clusters of action potentials, which cannot be observed in other cell types of the medial septum. In these neurons, subthreshold intrinsic membrane oscillations, only a small or no sag and strong action potential accommodation is seen. The third group is formed by burst firing glutamatergic neurons, exhibiting a small or no sag (Huh et al. 2010). The neurons of the fourth group are slow firing. Following somatic current injection, they discharge at low rates with accommodating action potentials
  > — Müller & Remy 2017, Electrophysiological Properties and Firing Patterns · [1] <!-- quote_key: 21358766_0c242fdc -->
- **Soma + projection target:** review (Müller & Remy 2017) summarising hippocampal-targeting septal anatomy · [1]
  > Glutamatergic medial septal neurons mainly project to hippocampal interneurons (see Fig. 1) with their somata located in stratum oriens near the alveus. In vivo, the activity of glutamatergic medial septal neurons increases before the mouse initiates locomotion and is higher during running, when compared to resting phases.
  > — Müller & Remy 2017, Electrophysiological Properties and Firing Patterns · [1] <!-- quote_key: 21358766_01840c4a -->
- **Slc17a6 marker + theta-pacing context:** review (Senova et al. 2020) on basal forebrain circuitry · [2]
  > Medial septal glutamatergic neurons expressing type 2 vesicular glutamate transporters (VGluT2) are likely involved in hippocampal theta generation. 132,135,140 They display a heterogeneous firing pattern, including fast, slow, burs, and clusterfiring (8-14 Hz, half of glutamatergic neurons) properties in slice. 135,137 Glutamatergic neurons also have intrinsic firing properties that may play an important role in pacing the hippocampus in vivo: they can discharge in recurrent clusters of action potentials, interspersed with intrinsically generated subthreshold membrane potential oscillations. 135
  > — Senova et al. 2020, Electrophysiological Properties and Firing Patterns · [2] <!-- quote_key: 212418354_02349d4e -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term. *(note: CL:0000679 "glutamatergic neuron" is too broad to capture the septal projection identity, the cluster-firing electrophysiology, or the stratum oriens interneuron projection target.)*

---

## Results

No candidate WMBv1 atlas edges have been emitted for this classical node. The graph currently carries the classical type definition (markers, negative markers, electrophysiology, projection target) but no mapping edges, so no per-candidate paragraphs, property comparison tables, or candidate audit tables are rendered.

The biological barrier to mapping is that the somata of this type sit in the medial septum / diagonal band of Broca — an extrahippocampal region — and the graph is curated to the hippocampal formation. The hippocampus-side anatomy on this node refers to the axonal projection target (stratum oriens of the hippocampus near the alveus), not the soma. Because the WMBv1 taxonomy stores soma-position location data and the hippocampal candidate cohort is queried on hippocampal anat terms, no candidate atlas clusters were assembled for this node in this graph. A targeted query against septal complex atlas cohorts is the appropriate next step *(note: this graph was curated for hippocampal types; the MS-DBB glutamatergic candidate set belongs to a septal-complex assessment that has not yet been run)*.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node draws on a CLASSICAL_MULTIMODAL definition basis combining electrophysiology, marker expression, and projection anatomy. VGluT1 (Slc17a7) and VGluT2 (Slc17a6) are the defining transcript-level identity markers; Chat and Gad1 are the defining negatives that distinguish the type from the cholinergic and GABAergic septal populations [1], [2]. The neurotransmitter assignment is glutamatergic [1], and the soma is recorded as extrahippocampal with a synaptic target in stratum oriens near the alveus [1].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:23+00:00 from [kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml](kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** none. No atlas candidate edges have been emitted against the MS-DBB glutamatergic node in this graph. The classical type is well-characterised at the marker, negative-marker, and electrophysiological level by review literature [1], [2], but the soma location (medial septum / diagonal band of Broca) falls outside the curated hippocampal target region; the hippocampus-side anatomy on the node reflects the axonal projection target only. A candidate cohort against the WMBv1 basal forebrain / septal complex partition has not been run.

No Cell Ontology term currently covers this type. CL:0000679 (glutamatergic neuron) is the closest ancestor but is too broad to capture the septal-projection identity or the cluster-firing electrophysiology; this node is a candidate for a new CL term contribution.

### Proposed experiments and follow-ups

- **What:** generate WMBv1 candidate edges for MS-DBB glutamatergic neurons by querying the taxonomy at ranks 0 and 1 against atlas regions corresponding to the medial septal nucleus and diagonal band of Broca (rather than against hippocampal formation).
  - **Target:** at least one candidate cluster with Slc17a6 / Slc17a7 expression CONSISTENT, Chat absent, Gad1 absent, and soma localisation in the septal complex.
  - **Expected output:** new MappingEdges against the septal complex partition of WMBv1; PropertyComparison entries for each of the four defining markers and two negative markers; downstream cluster-level electrophysiology comparison against the four-subgroup profile reported by [1].
  - **Resolves:** the absence of any atlas candidate set for this node.

- **What:** patch-seq or Cre-driver-targeted (Vglut2-Cre / Slc17a6-Cre) annotation transfer of MS-DBB glutamatergic neurons onto WMBv1.
  - **Target:** F1 ≥ 0.75 at SUPERTYPE level on the candidate septal-complex supertype, with cluster-level coverage that recapitulates the four electrophysiological subgroups described by Huh et al. 2010 and summarised in [1].
  - **Expected output:** AnnotationTransferEvidence on the new MappingEdges, enabling a supertype-level closeMatch or broadMatch verdict and a child-cluster discussion of the cluster-firing subgroup specifically.
  - **Resolves:** open questions 1 and 2 below.

- **What:** draft a new CL term request for "medial septal / diagonal band of Broca glutamatergic projection neuron" defined by Slc17a6/Slc17a7 expression, Chat and Gad1 absence, soma in the medial septum / diagonal band of Broca, and axonal projection onto hippocampal stratum oriens interneurons.
  - **Target:** definition + parent term (CL:0000679 glutamatergic neuron) + projection relation onto a hippocampal-interneuron CL term, following `docs/LLM_prompt_guidelines_for_CL_definitions.md`.
  - **Expected output:** issue-ready markdown for CL new term request via `workflows/cl-term-request.md`.
  - **Resolves:** open question 3.

### Open questions

1. Which WMBv1 cluster(s) and supertype(s) in the basal forebrain / septal complex partition correspond to the VGluT2+ glutamatergic population described by [1]?
2. Does the cluster-firing electrophysiological subgroup [1], [2] correspond to a distinct WMBv1 child cluster, or does it represent an electrophysiologically-defined subpopulation within a transcriptomically homogeneous supertype?
3. Should a new CL term be created for this type, and what should its parent and projection relations be?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | soma location, markers, negatives, NT, electrophysiology |
| [2] | Senova et al. 2020 | [32132227](https://pubmed.ncbi.nlm.nih.gov/32132227/) | Slc17a6 marker, theta-pacing electrophysiology context |
