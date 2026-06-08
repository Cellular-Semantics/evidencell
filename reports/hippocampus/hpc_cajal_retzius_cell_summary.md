# hippocampal Cajal-Retzius cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Introduction

Cajal-Retzius (CR) cells are an early-born reelin-secreting population that orchestrates cortical and hippocampal lamination during development; in the adult hippocampus a glutamatergic subpopulation persists in CA1 stratum lacunosum-moleculare and the outer molecular layer of the dentate gyrus, where it provides AMPA/NMDA-receptor-mediated excitation onto local interneurons and pyramidal cells [1]. Recent work has shown these adult CR cells are more abundant in rat than previously recognised and include local intra-hippocampal axonal projections that cross the hippocampal fissure — a non-canonical glutamatergic connectivity not predicted by the classical trisynaptic circuit [1][2][3].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum lacunosum moleculare [UBERON:0014557]; dentate gyrus of hippocampal formation [UBERON:0001885] (outer molecular layer) | [1][2][3] |
| NT | glutamatergic | [1][4][3] |
| Markers | Reln | [1][4] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** optogenetic activation of CR cells in CA1 stratum lacunosum-moleculare (Quattrocolo & Maccaferri 2014) · [1]
  > Cajal-Retzius cells orchestrate the development of cortical circuits by secreting the glycoprotein reelin. However, their computational functions are still unknown. In fact, the nature of their postsynaptic targets, major neurotransmitter released, as well as the class of postsynaptic receptors activated by their firing remain unclear. Here, we have addressed these questions by activating Cajal-Retzius cells optogenetically in mouse hippocampal slices. Light delivered to stratum lacunosum-moleculare triggered EPSCs both on local interneurons and on pyramidal cells.
  > — Quattrocolo et al. 2014, Specialized Glutamatergic Populations · [1] <!-- quote_key: 7165380_5e53cfc0 -->

- **Soma location / morphology:** description of local-projecting CR cells whose axons cross the hippocampal fissure between SLM and OML (Anstotz et al. 2015) · [2]
  > our discovery of local-projecting CR cells (whose axons crosses the hippocampal fissure and travel from the SLM to OML or vice versa) is the first evidence of an intrinsic glutamatergic hippocampal connection that does not flow according to the classical direction of the trisynaptic circuit (Andersen et al., 1966). In fact, this type of nonclassical intrahippocampal connectivity has been described only for GABAergic (Sik et al., 1994)(Ceranik et al., 1997)), but never for glutamatergic connections
  > — Anstotz et al. 2015, Specialized Glutamatergic Populations · [2] <!-- quote_key: 2565845_8c6a8b64 -->

- **Soma location / NT type:** characterisation of CA1 CR cells as glutamatergic and more abundant in adult rat (Wheeler et al. 2015) · [3]
  > in CA1, Cajal-Retzius cells, which were recently characterized as glutamatergic and more abundant than previously assumed in adult rats (Quattrocolo et al., 2014)
  > — Wheeler et al. 2015, Specialized Glutamatergic Populations · [3] <!-- quote_key: 631148_85ae9bb1 -->

- **NT type / heterogeneity:** review noting both GABAergic and glutamatergic CR cell populations (Yu et al. 2014) · [4]
  > A large number of Cajal-Retzius cells are GABAergic neurons, while others are glutamatergic. Both GABAergic Cajal-Retzius cells and glutamatergic Cajal-Retzius cells interact with each other to regulate neural migration and the formation of the neural network in the cortex and hippocampus. For instance, glutamate is released from glutamatergic Cajal-Retzius cells and facilitates the migration of GABAergic Cajal-Retzius cells and interneurons, which in turn releases GABA and facilitates the migration of glutamatergic neuroblasts (Myakhar et al., 2011)(Hsiao, 1998)(Tomidokoro et al., 2000)(Wang et al., 2012)(Manent et al., 2006)
  > — Yu et al. 2014, Specialized Glutamatergic Populations · [4] <!-- quote_key: 7981953_ebaa6eee -->

- **Markers (Reln):** reelin-positive cells include a glutamatergic subpopulation distributed across hippocampal layers (Yu et al. 2014) · [4]
  > Results of the present study showed that reelin-positive cells that were GABAergic or glutamatergic increased in density with increasing age. Moreover, these cells were both GABAergic and glutamatergic. Reelin-positive mossy cells in the dentate hilus were predominantly glutamatergic, but in the molecular layer of the dentate gyrus, reelin-positive cells that were GABAergic and glutamatergic showed a spatiotemporal pattern.
  > — Yu et al. 2014, Specialized Glutamatergic Populations · [4] <!-- quote_key: 7981953_7f1ea74e -->

</details>

Cell Ontology mapping: Cajal-Retzius cell [[CL:0000695](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000695)] (BROAD).

---

## Results

No atlas candidate edges have been generated for this classical node in the source graph. Candidate discovery against WMBv1 (CCN20230722) has not yet been run for hippocampal Cajal-Retzius cells, so no per-candidate property alignment, annotation transfer, or verdict assessment is available in this report.

*(note: this node is a classical-type stub awaiting Stage A/B candidate emission against the WMBv1 taxonomy; no mapping conclusions can be drawn at this time.)*

---

## Discussion

**Primary mapping:** None — no candidate atlas edges are present in the source graph for hippocampal Cajal-Retzius cell. The Cell Ontology has no specific term for the adult hippocampal glutamatergic Cajal-Retzius subpopulation; Cajal-Retzius cell [[CL:0000695](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000695)] is the closest ancestor. CL:0000695 = Cajal-Retzius cell describes the general CR cell class across cortex and hippocampus; the proposed type is the specifically hippocampal, adult-persisting, glutamatergic subpopulation (reelin+/calretinin+/VGluT3+). The CL definition includes hippocampal SLM and OML localisation.

### Open questions

1. The classical node carries documented heterogeneity that should shape future candidate emission: a substantial fraction of hippocampal CR cells are GABAergic; only the glutamatergic (reelin+/calretinin+/VGluT3+) subpopulation is captured here. Three axonal subtypes (layer-restricted local, cross-fissure local, long-range) likely warrant separate sub-nodes.
2. CR cells are more abundant in adult rat than previously assumed (Quattrocolo et al., 2014) — atlas-side cell counts in WMBv1 SLM/OML clusters should be cross-checked against this expectation when candidates are emitted.
3. Run candidate emission against WMBv1 at ranks 0 (cluster) and 1 (supertype) restricted to hippocampal formation [UBERON:0002421], filtered for glutamatergic NT and Reln expression, to populate the candidate set for this node.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Quattrocolo & Maccaferri 2014 | [25253849](https://pubmed.ncbi.nlm.nih.gov/25253849) | soma location |
| [2] | Anstotz et al. 2015 | [26582498](https://pubmed.ncbi.nlm.nih.gov/26582498) | soma location |
| [3] | Wheeler et al. 2015 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459) | soma location |
| [4] | Yu et al. 2014 | [25206826](https://pubmed.ncbi.nlm.nih.gov/25206826) | neurotransmitter type |

---

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:23+00:00 from [kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml](kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml).*
