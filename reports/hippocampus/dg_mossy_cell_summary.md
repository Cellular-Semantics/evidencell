# hilar mossy cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

## Introduction

Hilar mossy cells are large glutamatergic principal neurons of the dentate gyrus hilus, distinguished by complex proximal-dendritic thorny excrescences that receive granule-cell mossy-fibre input and by long-range commissural and associational axons that re-enter the dentate inner molecular layer. They are the major non-granule excitatory cell type of the dentate gyrus and a defining component of dentate microcircuit organisation; an accurate transcriptomic correspondence in the Whole Mouse Brain v1 (WMBv1) taxonomy is a prerequisite for connecting decades of dentate-circuit physiology to the atlas-level cell-type framework.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | dentate hilus (polymorph layer of dentate gyrus) [UBERON:0001885]; with axonal projections into dentate gyrus inner molecular layer [UBERON:0022347] and (dorsal mossy cells only) middle molecular layer [UBERON:0022346] | [1][2][3] |
| Neurotransmitter | glutamatergic | [4][1] |
| Defining markers | Slc17a7 (vGLUT1); Drd2; Calcrl (Crlr); Reln | [5][1][6][7] |
| Negative markers | Gad1 | — |

Note: dorsal and ventral mossy cells differ in axonal projection (dorsal: IML + MML; ventral: IML only); within-type heterogeneity may warrant separate atlas correspondences once mapping is performed.

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / morphology:** classical description of hilar position, thorny excrescences, and commissural/associational axon · [1][2][3]
  > Hilar mossy cells (MCs) are large glutamatergic neurons that innervate both GCs and inhibitory GABAergic neurons within the DG (Scharfman, 2016)(Scharfman et al., 2013). MCs make up the majority of hilar neurons, and are known for their complex spines called thorny excrescences (Scharfman, 2016)(Scharfman et al., 2013). They have dendrites mainly in the hilus and their axon projects to locations within the DG. Near the cell body the axon makes collaterals that terminate mainly in the hilus. Distal to the cell body the axon terminates at many septotemporal levels. There is also a commissural projection that terminates in the contralateral DG (Scharfman et al., 2013)
  > — Botterill et al. 2021, Mossy Cells: Specialized Glutamatergic Neurons · [1] <!-- quote_key: 231953329_132cf2e1 -->

  > mossy cells (MC) are a large subset of neurons that together with granule cells (GC) and GABAergic interneurons constitute the major cell types of the DG. MCs were first described by Lorente de Nó (1934) as non-principal cells of the hilar region of the hippocampus (Lorente de Nó, 1934). Years later, Amaral's landmark paper of Golgi-stained rat tissue reported these cells as the most impressive and frequently observed neurons in the hilus (Amaral, 1978). The most characteristic feature is the encrustation of the proximal dendrites with thorny excrescences resembling moss, a trait that led him to give the name of mossy cells. These excrescences receive excitatory synapses from mossy fiber terminals of GCs in the DG (Amaral, 1978)H E Scharfman, 1995a). MCs are glutamatergic, shown by immunohistochemical analyses, and confirmed by electrophysiological recordings of individual cells displaying an excitatory postsynaptic action (Buckmaster et al., 1996;Scharfman, 1995b;Scharfman & Schwartzkroin, 1988;Scharfman, 2016). Their axons project to the inner molecular layer of the DG
  > — Fredes & Shigemoto 2021, Mossy Cells: Specialized Glutamatergic Neurons · [2] <!-- quote_key: 235678538_35b7c784 -->

  > Hilar mossy cells are the prominent glutamatergic cell type in the dentate hilus of the dentate gyrus (DG)
  > — Sun et al. 2017, Mossy Cells: Specialized Glutamatergic Neurons · [3] <!-- quote_key: 3583187_ea3794f5 -->

  > while ~25% of the MC axon is located in the hilus, over 60% of the axon was distal from the cell body and located in the molecular layer (ML). The majority of the MC axon projected to the inner molecular layer (IML)
  > — Botterill et al. 2021, Mossy Cells: Specialized Glutamatergic Neurons · [1] <!-- quote_key: 231953329_6269a191 -->

  > long‐range axons of ventral MCs terminated in the IML, consistent with the literature
  > — Botterill et al. 2021, Mossy Cells: Specialized Glutamatergic Neurons · [1] <!-- quote_key: 231953329_54cbe1b7 -->

- **Neurotransmitter (glutamatergic):** immunohistochemical and electrophysiological confirmation in hilar neurons with thorny excrescences · [4][1]
  > Currently mossy cells can be easily distinguished from GABAergic neurons in the hilus because mossy cells are glutamatergic
  > — Scharfman & Myers 2013, Mossy Cells: Specialized Glutamatergic Neurons · [4] <!-- quote_key: 11290620_c6e60ece -->

  > Two studies provided evidence that mossy cells were glutamatergic, one anatomical and the second physiological. The first anatomical demonstration of glutamate immunoreactivity was made in Golgi-impregnated mossy cells (Soriano et al., 1994). The physiological study used hippocampal slices to impale mossy cells-which were confirmed to be regular-spiking, hilar, and had thorny excrescences-and simultaneously recorded from neurons in the granule cell layer until a monosynaptic connection was identified. That study showed for the first time that mossy cells produced unitary EPSPs in granule cells, supporting the hypothesis that mossy cells were glutamatergic (Scharfman, 1995).
  > — Scharfman & Myers 2013, Mossy Cells: Specialized Glutamatergic Neurons · [4] <!-- quote_key: 11290620_a475a601 -->

- **Slc17a7 (vGLUT1):** vGLUT1 is the principal vesicular glutamate transporter in hippocampal glutamatergic terminals · [5]
  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [5] <!-- quote_key: 14854554_ed1bdc00 -->

- **Drd2 / Calcrl as mossy-cell markers:** Drd2-Cre and Crlr-Cre (Calcrl) drivers selectively label hilar mossy cells, including their IML and MML axonal arbors · [1][6]
  > dorsal MC axons are an exception to this rule. We used two mouse lines that allow for Cre‐dependent viral labeling of MCs and their axons: dopamine receptor D2 (Drd2‐Cre) and calcitonin receptor‐like receptor (Crlr‐Cre). A single viral injection into the dorsal DG to label dorsal MCs resulted in labeling of MC axons in both the IML and middle molecular layer (MML)
  > — Botterill et al. 2021, Mossy Cells: Specialized Glutamatergic Neurons · [1] <!-- quote_key: 231953329_ceaf8acb -->

  > glutamatergic neurons represented 45.1% of all D1 or D2 cells in vHipp, in stark contrast to more dorsal parts of hippocampus where -barring D2-positive hilar mossy cells -D1 or D2 cells are almost exclusively interneurons (Gangarossa et al., 2012) (Puighermanal et al., 2015)(Puighermanal et al., 2016) . While GABAergic clusters readily mapped to canonical neuropeptide-defined interneuron cell types 40 , glutamatergic pyramidal neuron classification was not as clear-cut: we hypothesize that pyramidal neuron clusters might generally correspond to projection-specific vCA1/vSub populations.
  > — Godino et al. 2023, Specialized Glutamatergic Populations · [6] <!-- quote_key: 260336826_494cac70 -->

- **Reln:** reelin-positive hilar mossy cells are predominantly glutamatergic (in contrast to GABAergic reelin+ cells in the molecular layer) · [7]
  > Results of the present study showed that reelin-positive cells that were GABAergic or glutamatergic increased in density with increasing age. Moreover, these cells were both GABAergic and glutamatergic. Reelin-positive mossy cells in the dentate hilus were predominantly glutamatergic, but in the molecular layer of the dentate gyrus, reelin-positive cells that were GABAergic and glutamatergic showed a spatiotemporal pattern.
  > — Yu et al. 2014, Specialized Glutamatergic Populations · [7] <!-- quote_key: 7981953_7f1ea74e -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term. Children of CL:4023062 (dentate gyrus neuron) include granule cell (CL:2000089), basket cell (CL:2000087), kisspeptin neuron (CL:4023124) and stellate cell (CL:2000090); none captures the hilar mossy cell.

---

## Results

No WMBv1 candidate atlas clusters have yet been emitted for this classical node — the graph carries the classical-type ingest only, and no MappingEdge entries are present. Atlas candidate generation and per-candidate property comparison remain to be run before a transcriptomic correspondence can be reported.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The hilar mossy cell node is defined on a CLASSICAL_MULTIMODAL basis from anatomical, morphological, electrophysiological, and marker literature: hilar soma in the dentate polymorph layer with associational/commissural projections into the dentate inner molecular layer (dorsal mossy cells additionally projecting to the middle molecular layer) [1][2][3]; glutamatergic neurotransmitter phenotype confirmed by glutamate immunoreactivity and by monosynaptic EPSPs onto granule cells [4][1]; defining markers Slc17a7 (vGLUT1) [5], Drd2 and Calcrl (Crlr) (transgene-driver–validated labelling of hilar mossy cells and their IML/MML axons) [1][6], and Reln (reelin-positive hilar cells are predominantly glutamatergic) [7]; Gad1 as a negative marker distinguishing mossy cells from hilar GABAergic interneurons [4].

**Atlas mapping query.** Not yet performed — no candidate atlas clusters have been retrieved from the WMBv1 (CCN20230722) taxonomy for this node.

**Property alignment.** Not yet performed — no `property_comparisons` are present in the graph.

</details>

---

## Discussion

This report stage establishes the curated classical definition of the hilar mossy cell from the dentate-circuit literature and identifies an open Cell Ontology gap (no existing CL term captures hilar mossy cell despite the availability of sibling dentate-gyrus neuron terms). The next workflow stage is candidate retrieval from the WMBv1 taxonomy followed by property comparison; the dorsal/ventral projection-target dichotomy is a likely source of within-type transcriptomic heterogeneity to watch for in atlas candidates, since dorsal mossy cells (IML + MML projections) and ventral mossy cells (IML only) may resolve as distinct atlas clusters.

---

## References

- [1] Botterill et al. 2021 · PMID:33600026 · doi:10.1002/hipo.23314
- [2] Fredes & Shigemoto 2021 · PMID:34214666 · doi:10.1016/j.nlm.2021.107486
- [3] Sun et al. 2017 · PMID:28451637 · doi:10.1523/ENEURO.0097-17.2017
- [4] Scharfman & Myers 2013 · PMID:23420672 · doi:10.3389/fncir.2012.00106
- [5] Sarvari et al. 2016 · PMID:27375434 · doi:10.3389/fncel.2016.00149
- [6] Godino et al. 2023 · PMID:37546856 · doi:10.1101/2023.07.25.550554
- [7] Yu et al. 2014 · PMID:25206826 · doi:10.4103/1673-5374.128243
