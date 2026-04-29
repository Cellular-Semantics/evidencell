# Ventral hippocampal dopamine receptor-expressing glutamatergic pyramidal neuron

*draft · 2026-04-29 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings — confidence labels reflect current evidence only and will be revised.**

---

## Classical type summary

| Field | Value | Source |
|---|---|---|
| Node ID | `hpc_glu_dopa_receptor_pyramidal_hippocampus` | — |
| CL term | pyramidal neuron (CL:0000598) | BROAD |
| Neurotransmitter | glutamatergic | [1] |
| Defining markers | Drd1 (D1 dopamine receptor), Drd2 (D2 dopamine receptor) | [1][2] |
| Soma location | ventral CA1 / ventral subiculum (UBERON:0002421) | [1] |
| Definition basis | CLASSICAL_MULTIMODAL | — |
| Species | *Mus musculus* (primary evidence) | — |

This node captures a population of glutamatergic pyramidal neurons in the ventral hippocampus (vHipp) that are molecularly distinguished by expression of dopamine receptor subtypes Drd1 and/or Drd2. The population was defined by Godino et al. using BAC transgenic Drd1/Drd2-Cre mouse lines, IHC, and single-nucleus transcriptomics [1]. A key defining feature is ventral specificity: in dorsal CA1, D1/D2 receptors are found almost exclusively on GABAergic interneurons, whereas in vCA1/vSub a substantial fraction (~45%) of D1/D2-positive cells are glutamatergic pyramidal neurons [1][2].

> "We here study dopaminoceptive neurons in mouse ventral hippocampus (vHipp), molecularly distinguished by their expression of dopamine D1 or D2 receptors"
> <!-- quote_key: 260336826_f0ffda84 -->
> *— Godino et al. 2023 · PMID:37546856*

> "In the vCA1 pyramidal cell layer, gradual enrichment of both D1 and D2 cells emerges ventral to the rhinal fissure, along with the diffuse 21 transition from vCA1 to vSub. Together, these semiquantitative observations indicate a precise topographical organization of D1 and D2 cells across vHipp subfields and layers, most notably in the DG and in the caudal-most parts of vCA1/vSub."
> <!-- quote_key: 260336826_acc436ad -->
> *— Godino et al. 2023 · PMID:37546856*

The dorsal–ventral contrast is underscored by Puighermanal et al. [2], who showed that in dorsal CA1, D1R-expressing neurons are essentially GABAergic interneurons and not pyramidal cells. The glutamatergic Drd1/Drd2 phenotype is therefore a ventral-specific property.

> "Using BAC transgenic mice expressing enhanced green fluorescent protein under the control of D1R promoter, we examined the molecular identity of D1R-containing neurons within the CA1 subfield of the dorsal hippocampus"
> <!-- quote_key: 1711204_2c89b7e1 -->
> *— Puighermanal et al. 2016 · PMID:27678395*

An unresolved curation question remains: whether this constitutes a *transcriptomically distinct cell type* or merely a functional-property annotation (Drd1/Drd2 expression) that could be attached to existing CA1 and subicular pyramidal cell nodes. Transcriptomic data in Godino et al. suggest D1/D2-positive pyramidal neuron clusters are topographically organized and "transcriptionally distinct," but within-atlas resolution of this distinction remains unclear.

> "these neurons are transcriptionally distinct and topographically organized across vHipp subfields and cell types. In the ventral subicu"
> <!-- quote_key: 260336826_67252bb8 -->
> *— Godino et al. 2023 · PMID:37546856*

---

## Mapping candidates

### 0069 CA1-ProS Glut_1 (CS20230722_SUPT_0069) — LOW

**Atlas metadata**: SUPT_0069 is a WMBv1 supertype (CCN20230722) in the CA1-ProS Glut subclass (SUBC_016). It captures the principal glutamatergic population of CA1 and ProS (prosubiculum) across both dorsal and ventral poles. Annotation transfer from Yao 2021 CA1-ProS cells (n = 1,704) to WMBv1 yields 59.3% purity and F1 = 0.744 for SUPT_0069, confirming it as the primary CA1-ProS representative in the atlas.

**Supporting evidence**: The strongest positive support comes from regional overlap — ventral CA1 / ventral subiculum pyramidal neurons fall within the anatomical territory of SUPT_0069. Neurotransmitter type is fully consistent: both the classical node and SUPT_0069 are glutamatergic. Annotation transfer from a CA1-ProS reference dataset provides independent corroboration that CA1-ProS cells in WMBv1 map predominantly to this supertype.

**Critical concern — marker discordance**: The two defining markers of this classical node are **effectively absent** in SUPT_0069 at the supertype level. Precomputed expression statistics from the WMBv1 HDF5 (supertype level) show:

- **Drd1**: mean_expression = **0.09** — effectively absent
- **Drd2**: mean_expression = **0.02** — effectively absent

Neither Drd1 nor Drd2 appears among SUPT_0069's defining markers. This is the critical discordance for this edge: the canonical molecular identity of the classical node is not detectable in the candidate atlas match at the supertype level. Two explanations remain possible: (a) Drd1/Drd2-expressing pyramidal neurons are a sparse minority within the broader SUPT_0069 population, and mean expression statistics dilute all signal; or (b) a more specific ventral-enriched cluster within CA1-ProS carries detectable Drd1/Drd2 expression that is averaged away at supertype level. Both possibilities are untested.

**Additional concern — dorsal/ventral resolution**: SUPT_0069 spans the full dorsal–ventral CA1 range. WMBv1 does not clearly separate dorsal from ventral CA1 at the supertype level without MERFISH soma location data. The dopamine receptor-expressing pyramidal neurons described by Godino et al. [1] are specifically enriched in the ventral portion. This spatial mismatch means that even if a ventral-enriched sub-cluster within SUPT_0069 existed, the current supertype-level statistics cannot confirm or exclude it.

**Property comparison**:

| Property | Classical node | SUPT_0069 | Alignment |
|---|---|---|---|
| Neurotransmitter | glutamatergic | glutamatergic (SUBC_016 CA1-ProS Glut) | CONSISTENT |
| Soma location | ventral CA1 / ventral subiculum | dorsal + ventral CA1-ProS | APPROXIMATE |
| Drd1 (defining marker) | present (defining) | mean_expression = 0.09 — absent | **DISCORDANT** |
| Drd2 (defining marker) | present (defining) | mean_expression = 0.02 — absent | **DISCORDANT** |

**Verdict**: Speculative. SUPT_0069 is the most anatomically appropriate candidate for ventral CA1 glutamatergic neurons in WMBv1, but the absence of Drd1/Drd2 expression at the supertype level means this edge is not supported by marker evidence. Annotation transfer provides weak corroborating evidence for the CA1-ProS regional assignment, but cannot substitute for marker concordance. The edge should not be used until the marker discordance is addressed.

**Upgrade criteria**: Confidence can be raised from LOW to MODERATE if:

1. Drd1 or Drd2 expression is detected at appreciable levels in a CA1-ProS sub-cluster with ventral enrichment in WMBv1 (via `just add-expression` at cluster level across SUPT_0069–0074); OR
2. A dedicated ventral hippocampus dataset with Drd1/Drd2 labelling is run through MapMyCells and maps specifically to SUPT_0069 or a closely related supertype (F1 ≥ 0.7); OR
3. The curation decision on type vs. property annotation is resolved and the node is restructured accordingly.

---

## Proposed experiments

1. **Cluster-level expression profiling**: Run `just add-expression` for Drd1 and Drd2 across the full CA1-ProS supertype range (SUPT_0069–0074) to determine whether any sub-cluster within CA1-ProS shows ventral enrichment and detectable Drd1/Drd2 expression. This is the highest-priority action for resolving the marker discordance.

2. **Ventral hippocampus annotation transfer**: Apply MapMyCells to a ventral hippocampus scRNA-seq dataset from Drd1/Drd2-Cre-labelled mice (or a dataset with high ventral CA1/vSub representation). Compute F1 scores against WMBv1 CA1-ProS supertypes and determine whether labelled pyramidal neurons preferentially assign to a specific supertype.

3. **Curation decision on node identity**: Resolve the open question of whether this node represents a distinct transcriptomic type or a functional state annotation on vCA1/vSub pyramidal cells. If the latter, the node should be deprecated and Drd1/Drd2 expression annotations added to `ca1_pc_hippocampus` and the subicular pyramidal cell node instead.

---

## Open questions

1. **Distinct type or property annotation?** The central unresolved question: are Drd1/Drd2-expressing pyramidal neurons in vCA1/vSub transcriptomically distinct enough to warrant a separate KB node, or should they be annotated as a property on existing CA1 and subicular pyramidal cell nodes? Godino et al. [1] report them as "transcriptionally distinct" but do not resolve this at the resolution of WMBv1 supertype boundaries.

2. **Which CA1-ProS supertype(s) capture the Drd1/Drd2 subpopulation?** SUPT_0069 spans dorsal and ventral CA1. Does any sub-cluster within SUPT_0069–0074 specifically enrich for ventral CA1 and carry detectable Drd1/Drd2 expression?

3. **Dorsal–ventral separation in WMBv1**: Does WMBv1 resolve a ventral-CA1-specific supertype or cluster that would be a more appropriate anchor for this node than SUPT_0069? MERFISH spatial data would be needed to assess this.

4. **D2 neurons in subiculum**: Godino et al. [1] report D2-expressing pyramidal neurons in vSub as well as vCA1. Should this node be split into separate vCA1 and vSub nodes, or retained as a single vHipp Drd1/Drd2-pyramidal population?

---

## Evidence base

Two primary sources underpin this node. Both are mouse studies.

**Godino et al. 2023** [1] is the defining study. It used BAC transgenic Drd1-Cre and Drd2-Cre mice, IHC, and single-nucleus transcriptomics to characterize dopaminoceptive neurons across ventral hippocampal subfields. Key findings: (a) ventral-specific glutamatergic identity of D1/D2 neurons contrasting with dorsal hippocampus where these receptors label interneurons; (b) precise topographic organization across vCA1/vSub layers; (c) distinct electrophysiological responses — D2 pyramidal neurons show reversible hyperpolarization to dopamine or quinpirole, whereas D1 neurons did not depolarize at tested concentrations.

**Puighermanal et al. 2016** [2] provides essential contrast: in dorsal CA1, D1R-expressing neurons are essentially GABAergic interneurons. This dorsal-vs-ventral distinction is crucial context: the glutamatergic Drd1 phenotype at this node is a genuinely ventral-hippocampus-specific property not present in the dorsal atlas reference from the same study.

Atlas-side evidence rests on WMBv1 supertype metadata, F1-based annotation transfer from CA1-ProS reference cells, and precomputed expression statistics from the CCN20230722 HDF5. No dedicated Drd1/Drd2 ventral hippocampus dataset has been run through annotation transfer for this node.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Godino A et al. "Dopaminoceptive D1 and D2 neurons in ventral hippocampus arbitrate approach and avoidance in anxiety." *bioRxiv* 2023. DOI:10.1101/2023.07.25.550554 | [37546856](https://pubmed.ncbi.nlm.nih.gov/37546856/) | Soma location; NT type; Drd1 marker; Drd2 marker |
| [2] | Puighermanal E et al. "Anatomical and molecular characterization of dopamine D1 receptor-expressing neurons of the mouse CA1 dorsal hippocampus." *Brain Struct Funct* 2016. DOI:10.1007/s00429-016-1314-x | [27678395](https://pubmed.ncbi.nlm.nih.gov/27678395/) | Drd1 marker; dorsal/ventral contrast |
