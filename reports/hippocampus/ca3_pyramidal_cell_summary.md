# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

## Introduction

CA3 pyramidal cells are glutamatergic principal neurons of Ammon's horn whose somata populate the pyramidal layer of CA3 and whose apical and basal dendrites ramify through stratum radiatum and stratum oriens. They are the recipient of the dentate granule cell mossy-fibre projection and the source of the Schaffer collateral projection to CA1, making them the central relay of the canonical hippocampal trisynaptic circuit. Establishing a transcriptomic mapping for this classical type anchors the broader hippocampal glutamatergic taxonomy and provides the reference against which finer CA3 subdivisions (e.g. early-generated pioneer pyramidal neurons reported by Marissal and colleagues) can later be tested.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA3 [UBERON:0014550]; apical/basal dendrites in CA3 stratum radiatum / stratum oriens [UBERON:0005372]; Schaffer collateral projection to CA1 stratum radiatum [UBERON:0014554] | [1], [2] |
| NT | glutamatergic | [3], [4], [5] |
| Markers | Gria1, Gria2, Grm1, Slc17a7, Nptn, Gjd2 | [2], [6], [7], [3] |
| Negative markers | (none documented) | — |
| Neuropeptides | (none documented) | — |
| CL term | hippocampal pyramidal neuron [CL:1001571] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Munster-Wandowski et al. 2013 immunohistochemical survey of the hippocampal formation · [1]
  > The hippocampal formation consists of GCs in the dentate gyrus and pyramidal cells in the CA1 and CA3 areas
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [1] <!-- quote_key: 7458943_d6507595 -->

  > The principal cells are interconnected by glutamatergic synapses, forming the "trisynaptic pathway" (Andersen et al., 1971)(Storm- Mathisen, 1977). The GCs of the dentate gyrus receive excitatory glutamatergic input from layer II pyramidal cells of the entorhinal cortex (Steward et al., 1976)) and project to CA3 pyramidal cells. From there, they project to CA1 cells, which in turn project to the subiculum and back to the entorhinal cortex (Andersen et al., 1971)(Amaral et al., 1990).
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [1] <!-- quote_key: 7458943_efa15be5 -->

- **NT type:** Dale et al. 2015 review of hippocampal circuitry · [4]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [4] <!-- quote_key: 2281033_5b9805ff -->

  Cembrowski et al. 2016 transcriptomic atlas of excitatory hippocampal populations · [5]
  > The hippocampus is grossly comprised of five excitatory cell populations; namely, granule and mossy cells of the dentate gyrus (DG), and pyramidal cells of CA3, CA2, and CA1.
  > — Cembrowski et al. 2016, Major Glutamatergic Cell Types in Hippocampal Subfields · [5] <!-- quote_key: 4875295_002a714a -->

- **Gria1 / Gria2:** Yeung et al. 2020 AMPA receptor immunolocalisation in hippocampus · [2]
  > The GluA1 receptor subunit displayed diffuse staining within the str. radiatum and str. oriens, with marked immunoreactivity localized to cellular processes within the str. pyramidale of the CA3 (Figure 2). Isolated localization to pyramidal cell bodies can be seen through all three layers of the CA3, although mainly concentrated within the str. pyramidale.
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [2] <!-- quote_key: 210181642_7ac40176 -->

  > GluA2 showed diffuse uniform staining within the str. radiatum and str. oriens of the CA3, with greater localization to neuronal bodies within the str. pyramidale
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [2] <!-- quote_key: 210181642_88f001b0 -->

- **Grm1 / Slc17a7:** Sarvari et al. 2016 review of glutamatergic signalling in hippocampus · [6]
  > Metabotropic glutamate receptor 1 (mGluR1) is mainly expressed in granule cells and CA3 pyramidal neurons while mGluR5 is highly expressed in all subfields of the rat hippocampus (Fotuhi et al., 1994)
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [6] <!-- quote_key: 14854554_b6a5ffa0 -->

  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [6] <!-- quote_key: 14854554_ed1bdc00 -->

- **Nptn (neuroplastin):** Herrera-Molina et al. 2017 hNp65 expression survey · [7]
  > unequivocally identified hNp65-positive glutamatergic neurons are granular neurons of DG, pyramidal neurons of CA1, CA2-3, subiculum, and layers II, IV, and V of the entorhinal cortex.
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [7] <!-- quote_key: 3288675_37ad1c13 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD).

---

## Results

No WMBv1 (CCN20230722) candidate edges have been generated yet for CA3 pyramidal cell — the source graph (`20260427_hippocampus_glutamatergic_report_ingest.yaml`) carries the classical-type description and its literature support, but the discovery step that produces candidate atlas matches has not been run for this node. The candidates pool surfaced by the deterministic pre-pass is empty, and no annotation transfer, bulk correlation, or property-comparison evidence is available to assess. The downstream evidence-extraction and `map-cell-type` orchestrator steps are required before a survivor analysis or per-candidate paragraphs can be written.

<details>
<summary>Candidates audited (full top-K)</summary>

No candidate edges present in the graph for this node. Re-run after `map-cell-type` populates `graph.edges` with WMBv1 candidates at ranks 0 (cluster) and 1 (supertype).

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** CA3 pyramidal cell is recorded with `definition_basis: CLASSICAL_MULTIMODAL` and is defined by glutamatergic neurotransmitter identity [3] [4] [5], expression of the AMPA receptor subunits Gria1 and Gria2 [2], the metabotropic glutamate receptor Grm1 and the vesicular glutamate transporter Slc17a7 [6], the neuroplastin gene Nptn [7], and the gap-junction subunit Gjd2 [3], with somata in the pyramidal layer of CA3 [UBERON:0014550] and dendrites in CA3 stratum radiatum / stratum oriens [UBERON:0005372] [1] [2]; the Schaffer collateral axonal projection terminates in CA1 stratum radiatum [UBERON:0014554] [1]. A known ambiguity is the existence of early-generated pioneer CA3 pyramidal neurons that may form a morpho-functionally distinct subpopulation, and CA3-specific electrophysiological characterisation distinct from shared CA1/CA3 receptor descriptions is identified as a gap requiring primary verification.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`. No candidates have yet been emitted for this node.

**Property alignment.** Each defining property of the classical type is compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values come from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location. Not yet performed for this node.

</details>

---

## Discussion

CA3 pyramidal cell sits under the BROAD CL placement `hippocampal pyramidal neuron` [CL:1001571] because the Cell Ontology currently lacks a CA3-specific subfield term; the existing synonym "hippocampus (CA) pyramidal cell" covers CA1–CA3 without subfield resolution, so this report's CL line documents the placement rather than asserting subfield specificity. The classical-type description is grounded across multiple primary and review sources spanning soma localisation, dendritic and axonal architecture, neurotransmitter identity, ionotropic and metabotropic glutamate receptor expression, and shared glutamatergic-projection markers, and is sufficient to drive a forthcoming WMBv1 candidate retrieval. Two open questions warrant attention before survivor selection: (i) whether the pioneer-pyramidal-neuron subpopulation reported in CA3 should be represented as a separate classical node before mapping, and (ii) whether CA3-specific electrophysiological signatures distinct from shared CA1/CA3 receptor properties can be sourced from primary literature, since current quotes describe receptor distributions rather than CA3-distinguishing intrinsic properties. A subfield-specific Cell Ontology term for CA3 pyramidal cells would also resolve the BROAD CL placement.

---

## References

[1] Munster-Wandowski et al. 2013 · PMID:24319410 · DOI:10.3389/fncel.2013.00210
[2] Yeung et al. 2020 · PMID:32009891 · DOI:10.3389/fnins.2019.01427
[3] https://doi.org/10.3389/fnana.2012.00013
[4] Dale et al. 2015 · PMID:26346726 · DOI:10.1017/S1092852915000425
[5] Cembrowski et al. 2016 · PMID:27113915 · DOI:10.7554/eLife.14997
[6] Sarvari et al. 2016 · PMID:27375434 · DOI:10.3389/fncel.2016.00149
[7] Herrera-Molina et al. 2017 · PMID:28779130 · DOI:10.1038/s41598-017-07839-9
