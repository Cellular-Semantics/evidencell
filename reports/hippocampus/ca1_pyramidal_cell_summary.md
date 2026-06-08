# CA1 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

## Introduction

CA1 pyramidal cells are the canonical principal excitatory output neurons of the hippocampal Ammon's horn region CA1, with cell bodies confined to the pyramidal layer of CA1 [UBERON:0014548]. They receive Schaffer collateral input from CA3 pyramidal cells onto apical dendrites in the hippocampus stratum radiatum [UBERON:0005372] and basal dendrites in the hippocampus stratum oriens [UBERON:0005371], and they project to the subiculum [UBERON:0002191] and entorhinal cortex, completing the classical trisynaptic pathway. They form the principal output of CA1, and a correct atlas-level mapping is therefore the anchor for interpreting any CA1-targeted single-cell experiment against the Whole Mouse Brain v1 (WMBv1) taxonomy.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1], [2] |
| Dendritic field | hippocampus stratum radiatum [UBERON:0005372]; hippocampus stratum oriens [UBERON:0005371] | [2] |
| Projection target | subiculum [UBERON:0002191] | [1] |
| NT | glutamatergic | [3], [4], [5] |
| Markers | Gria1, Gria2, Nptn, Slc17a7 | [2], [6], [7] |
| Negative markers | Drd1 (dorsal CA1) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (CA1 stratum pyramidale):** review · rat hippocampus · [1]
  > The hippocampal formation consists of GCs in the dentate gyrus and pyramidal cells in the CA1 and CA3 areas
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [1] <!-- quote_key: 7458943_d6507595 -->

  > The principal cells are interconnected by glutamatergic synapses, forming the "trisynaptic pathway" (Andersen et al., 1971)(Storm- Mathisen, 1977). The GCs of the dentate gyrus receive excitatory glutamatergic input from layer II pyramidal cells of the entorhinal cortex (Steward et al., 1976)) and project to CA3 pyramidal cells. From there, they project to CA1 cells, which in turn project to the subiculum and back to the entorhinal cortex (Andersen et al., 1971)(Amaral et al., 1990).
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [1] <!-- quote_key: 7458943_efa15be5 -->

- **Dendritic field (GluA1/GluA2 immunoreactivity in CA1 strata):** immunohistochemistry · rat hippocampus · [2]
  > The CA1 showed strong dense immunoreactivity within the str. oriens and str. radiatum, with relatively decreased staining within the str. pyramidale cells.
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [2] <!-- quote_key: 210181642_7ac40176 -->

- **NT type (glutamatergic):** review · rodent hippocampus · [3], [4], [5]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1).
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 2281033_5b9805ff -->

  > The hippocampus is grossly comprised of five excitatory cell populations; namely, granule and mossy cells of the dentate gyrus (DG), and pyramidal cells of CA3, CA2, and CA1.
  > — Cembrowski et al. 2016, Major Glutamatergic Cell Types in Hippocampal Subfields · [4] <!-- quote_key: 4875295_002a714a -->

  > Hippocampal neurons mainly release glutamate or gamma-aminobutyric acid (GABA) (Richmond, 2005).
  > — Wheeler et al. 2015, Specialized Glutamatergic Populations · [5] <!-- quote_key: 631148_96ad2908 -->

- **Gria1 / Gria2 (AMPA receptor subunits):** immunohistochemistry · rat hippocampus · [2]
  > GluA2 showed diffuse uniform staining within the str. radiatum and str. oriens of the CA3, with greater localization to neuronal bodies within the str. pyramidale (Figures 4Ba-f). The CA1 region exhibited similar staining patterns, localized to the cell bodies within the str. pyramidale, with diffuse staining throughout the str. oriens and str. radiatum (Figure 4A).
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [2] <!-- quote_key: 210181642_88f001b0 -->

- **Nptn (neuroplastin-65):** immunohistochemistry · human hippocampus · [6]
  > unequivocally identified hNp65-positive glutamatergic neurons are granular neurons of DG, pyramidal neurons of CA1, CA2-3, subiculum, and layers II, IV, and V of the entorhinal cortex.
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [6] <!-- quote_key: 3288675_37ad1c13 -->

  > .hNp65 is very abundant at membranes of the cell body of granular and pyramidal neurons (Fig. 1d,e), dendrites, and in punctate structures within the neuropil (Fig. 1d,e).
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [6] <!-- quote_key: 3288675_d39d0506 -->

- **Slc17a7 (VGLUT1):** review · rat hippocampus · [7]
  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [7] <!-- quote_key: 14854554_ed1bdc00 -->

</details>

Cell Ontology mapping: hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD).

## Results

No candidate atlas mapping edges have been emitted for CA1 pyramidal cell against WMBv1 (CCN20230722) in this graph; the source YAML carries the classical-type node only, with `edges: []`. Stage B candidate emission (`just emit-stage-b`) and the property-comparison + AT-evidence assembly that gen-report normally narrates have not yet been run against this node. *(note: heterogeneity flagged on the classical node — ventral CA1 D1/D2-receptor-expressing pyramidal cells and dorsal-vs-ventral projection bias — implies that any future mapping should be assessed at supertype level first and may distribute across multiple WMBv1 clusters; see Discussion.)*

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** CA1 pyramidal cell is defined here with `definition_basis = CLASSICAL_MULTIMODAL`: glutamatergic NT [3][4][5], somata in the pyramidal layer of CA1 with apical dendrites in stratum radiatum and basal dendrites in stratum oriens [1][2], subicular projection [1], and a defining marker panel of Gria1 / Gria2 [2], Nptn [6], and Slc17a7 [7]. Drd1 is recorded as a negative marker for dorsal CA1 pyramidal neurons (no verbatim quote available in the current facts file).

**Atlas mapping query.** Candidate atlas clusters would be retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`. *(note: not yet run for this node — graph edges are empty.)*

**Property alignment.** Not applicable until edges are present. Each defining property of the classical type would be compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:22+00:00 from [kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml](kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml).*

</details>

## Discussion

**Primary mapping:** none committed — no MappingEdges have been emitted for CA1 pyramidal cell in this graph, so no candidate WMBv1 cluster or supertype can be named as primary. The classical type is fully described (multimodal markers + soma + projection + NT) and is ready for Stage B candidate emission against WMBv1 (CCN20230722).

The Cell Ontology has no specific term for this population; hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] is the closest ancestor. CA1-specific term absent from CL. Same BROAD mapping to CL:1001571 as CA3.

### Proposed experiments and follow-ups

- **Emit Stage B candidates.** Run `just emit-stage-b` for `ca1_pyramidal_cell` against `CCN20230722` at ranks 0 (cluster) and 1 (supertype). Expected output: a top-K set of `MappingEdge` entries with `discovery_score`, region fractions, and per-marker tier data populated. Resolves: open question (1).
- **Annotation transfer.** Once candidate edges exist, run MapMyCells against a CA1-targeted source dataset (e.g. dorsal CA1 pyramidal scRNA-seq) targeting WMBv1, with cluster and supertype level F1 reporting. Expected output: `AnnotationTransferEvidence` entries on each edge. Target: F1 ≥ 0.80 at SUPERTYPE level. Resolves: open question (2).
- **Disambiguate ventral / dorsal CA1.** *(note: the classical node records D1/D2-receptor-expressing ventral CA1 pyramidal cells as a likely separable subpopulation; dorsal CA1 is D1R-negative.)* A targeted literature pass for projection-specific vCA1/vSubiculum pyramidal subtypes would clarify whether ventral CA1 should be split off as a distinct classical node before Stage B is run. Expected output: refined node set or an `AMBIGUITY`-tagged caveat persisted on the parent node. Resolves: open question (3).
- **Nptn marker specificity.** *(note: Nptn / hNp65 is reported as expressed in CA1, CA2-3, subiculum, and entorhinal cortex pyramidal cells [6] — it is therefore not CA1-specific.)* Treat as a hippocampal-pyramidal panel marker rather than a CA1 discriminator. Targeted literature search recommended for any CA1-restricted marker that could anchor the mapping at supertype level beyond the broad glutamatergic panel.

### Open questions

1. No candidate WMBv1 clusters or supertypes have been emitted for CA1 pyramidal cell — Stage B candidate emission has not been run against this node.
2. Annotation-transfer evidence is absent; no direct experimental anchor links the classical type to a WMBv1 cluster.
3. Ventral CA1 pyramidal cells expressing D1/D2 receptors are flagged as a likely separable subtype (45.1% of D1/D2 cells in vHipp are glutamatergic per the curator note on the classical node); the current single-node representation may need splitting into dorsal-vs-ventral or projection-specific subnodes before mapping.
4. No primary CA1-restricted defining marker is currently anchored to the node; Gria1, Gria2, Nptn, and Slc17a7 are broad glutamatergic / pan-hippocampal-pyramidal markers.

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Munster-Wandowski et al. 2013 | [24319410](https://pubmed.ncbi.nlm.nih.gov/24319410/) | soma location |
| [2] | Yeung et al. 2020 | [32009891](https://pubmed.ncbi.nlm.nih.gov/32009891/) | soma location; Gria1/Gria2 markers |
| [3] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
| [4] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | neurotransmitter type |
| [5] | Wheeler et al. 2015 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | neurotransmitter type |
| [6] | Herrera-Molina et al. 2017 | [28779130](https://pubmed.ncbi.nlm.nih.gov/28779130/) | Nptn marker |
| [7] | Sarvari et al. 2016 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434/) | Slc17a7 marker |
