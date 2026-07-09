# hippocampal Cajal-Retzius cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Introduction

Cajal-Retzius cells are early-generated, reelin-secreting neurons that orchestrate cortical and hippocampal circuit development; an adult-persisting, reelin-positive, glutamatergic subpopulation occupies CA1 stratum lacunosum-moleculare and the outer molecular layer of the dentate gyrus, where it forms direct monosynaptic connections onto interneurons and pyramidal cells via AMPA- and NMDA-type glutamate receptors [1]. Unlike the canonical trisynaptic loop, a subset of these cells projects local axons that cross the hippocampal fissure between SLM and OML, defining a non-classical intrahippocampal glutamatergic connection [2]. Establishing a transcriptomic mapping for this population is the bridge between this classical, optogenetics- and tract-tracing-derived definition and the WMBv1 cluster space; it also has direct relevance for assigning glutamatergic identity to the reelin-positive cells that classical and recent immuno-anatomical work [3,4] has reported in adult hippocampus alongside their GABAergic counterparts.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum lacunosum-moleculare (UBERON:0014557); outer molecular layer of dentate gyrus (UBERON:0001885) | [1], [2], [3] |
| NT type | glutamatergic | [1], [3], [4] |
| Defining markers | Reln | [1], [4] |
| Notes | A substantial fraction of hippocampal CR cells are GABAergic; only the glutamatergic (reelin+/calretinin+/VGluT3+) subpopulation is captured here. Three axonal subtypes (layer-restricted local, cross-fissure local, long-range) likely warrant separate sub-nodes. CR cells are more abundant in adult rat than previously assumed. | [1], [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** optogenetic stimulation of CR cells with EPSC recordings from SLM targets (Quattrocolo & Maccaferri 2014) · mouse · [1]
  > Light delivered to stratum lacunosum-moleculare triggered EPSCs both on local interneurons and on pyramidal cells.
  > — Quattrocolo & Maccaferri 2014, Specialized Glutamatergic Populations · [1] <!-- quote_key: 7165380_5e53cfc0 -->
- **Soma location:** anatomical tracing of CR cell axons across the hippocampal fissure (Anstotz et al. 2015) · [2]
  > our discovery of local-projecting CR cells (whose axons crosses the hippocampal fissure and travel from the SLM to OML or vice versa) is the first evidence of an intrinsic glutamatergic hippocampal connection that does not flow according to the classical direction of the trisynaptic circuit
  > — Anstotz et al. 2015, Specialized Glutamatergic Populations · [2] <!-- quote_key: 2565845_8c6a8b64 -->
- **Soma location:** comparative characterisation of adult hippocampal CR populations (Wheeler et al. 2015) · [3]
  > in CA1, Cajal-Retzius cells, which were recently characterized as glutamatergic and more abundant than previously assumed in adult rats
  > — Wheeler et al. 2015, Specialized Glutamatergic Populations · [3] <!-- quote_key: 631148_85ae9bb1 -->
- **NT type:** functional and pharmacological characterisation, AMPA/NMDA-mediated EPSCs (Quattrocolo & Maccaferri 2014) · [1]
  > Both connections showed physiological and pharmacological properties indicating the involvement of AMPA- and NMDA-type glutamate receptors.
  > — Quattrocolo & Maccaferri 2014, Specialized Glutamatergic Populations · [1] <!-- quote_key: 7165380_5e53cfc0 -->
- **NT type:** reelin-positive cell phenotyping across cortex and hippocampus (Yu et al. 2014) · [4]
  > A large number of Cajal-Retzius cells are GABAergic neurons, while others are glutamatergic.
  > — Yu et al. 2014, Specialized Glutamatergic Populations · [4] <!-- quote_key: 7981953_ebaa6eee -->
- **Defining marker Reln:** reelin-positive cell identification in adult dentate gyrus and molecular layer (Yu et al. 2014) · [4]
  > Reelin-positive mossy cells in the dentate hilus were predominantly glutamatergic, but in the molecular layer of the dentate gyrus, reelin-positive cells that were GABAergic and glutamatergic showed a spatiotemporal pattern.
  > — Yu et al. 2014, Specialized Glutamatergic Populations · [4] <!-- quote_key: 7981953_7f1ea74e -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: Cajal-Retzius cell [[CL:0000695](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000695)] (BROAD).

---

## Results

Atlas-side reelin expression and soma-region painting converge on the WMBv1 supertype 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] as the hippocampal Cajal-Retzius cell mapping, with child cluster 0497 HPF CR Glut_1 [CS20230722_CLUS_0497] carrying the bulk of the supertype's cells (2498 of 3116) and the highest-percentile Reln signal in the cohort (see property comparison tables). The other eight candidates emerged from cohort-scoring on hippocampal-region and glutamatergic NT alone; they comprise CA3 and dentate-gyrus principal-neuron supertypes and one presubicular L2 IT cluster, none of which show Reln at the level seen on the CR supertype, and are eliminated on cell-class grounds (see candidates audit table below).

### 0135 HPF CR Glut_1 (supertype) · 🟡 MODERATE

**Property alignment (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | CA1 SLM [UBERON:0014557]; DG OML [UBERON:0001885] | Hippocampal formation; Dentate gyrus, molecular layer (count_100um=2410 of 2967 hippocampal); region_fraction_100um=0.670 | Dentate gyrus, molecular layer (CLUS_0497); region_fraction_100um=0.694 | CONSISTENT |
| NT type | glutamatergic | not asserted at supertype level | Glut (CLUS_0497) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Reln expression | defining marker | mean 12.43; cohort percentile 0.990; child-coverage 1.000 | mean 12.42; cohort percentile 0.987 (CLUS_0497) | CONSISTENT |
| Sex ratio | not documented | not available | not available (sex MFR not in edge) | NOT_ASSESSED |

*(1 of 1 child cluster (CLUS_0497) shows Reln concordant with the classical type at high cohort percentile; the supertype's child-coverage is 1.000 indicating uniform Reln signal across the parent.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + region painting | Atlas metadata | PARTIAL | Reln=12.43 (cohort_pct 0.99); region_fraction_100um=0.670 | atlas-internal |

**Supporting evidence.**

- The supertype's painted soma distribution localises overwhelmingly to dentate gyrus, molecular layer (the DG portion of the classical type's soma description); the strict region_fraction is 0.542 and the 100µm-proximity fraction is 0.670, consistent with cells lying within and immediately adjacent to the targeted region set.
- Reln is the classical type's primary defining marker. The supertype's precomputed Reln mean (12.43) is the highest in the hippocampal-glutamatergic candidate cohort (cohort percentile 0.990) and child-coverage is 1.000, indicating the marker is robust across all child clusters of the supertype.
- The atlas team's own naming convention ("HPF CR Glut_1") encodes a hippocampal Cajal-Retzius glutamatergic identity, providing concordant nomenclature with the classical type.

**Marker evidence provenance.**

- **Reln** is supported on the classical node by Quattrocolo & Maccaferri 2014 [1] (functional optogenetic characterisation of reelin-secreting CR cells in SLM) and Yu et al. 2014 [4] (anatomical phenotyping of reelin-positive cells in adult hippocampus). Both are transcript-and-protein-level references for a reelin-defined population. The atlas-side precomputed mean (12.43) at cohort percentile 0.990 cross-validates the classical defining marker at transcript level on the same supertype the atlas team labels HPF CR Glut_1.

**Concerns.**

- Cell Ontology mapping is BROAD: CL:0000695 covers the general (cortical + hippocampal, embryonic + adult) Cajal-Retzius cell class. The classical type here is narrower — the adult-persisting, hippocampal, glutamatergic, reelin+/calretinin+/VGluT3+ subpopulation. A more specific CL term is currently unavailable, and the mapping should be read as a class-level alignment rather than a 1:1 identity.
- NT type at the supertype level is not asserted in atlas metadata (NOT_ASSESSED at supertype rank); glutamatergic NT identity is confirmed only at child-cluster level (CLUS_0497 is annotated Glut). Supertype-level NT inheritance from the named "Glut_1" suffix is a naming convention rather than an asserted property.
- The classical-side notes flag heterogeneity within hippocampal CR cells (substantial GABAergic fraction; three axonal subtypes — layer-restricted local, cross-fissure local, long-range); these subdivisions are not resolved at WMBv1 supertype granularity, and the supertype-level mapping pools them with the single transcriptomically-defined CR cluster.
- The 100µm-proximity region_fraction of 0.670 means roughly a third of the supertype's cells lie outside the targeted hippocampal-region set even at the proximity-tolerant level; some scatter into adjacent registration regions is present but does not displace the dominant DG-molecular-layer signal.

**What would upgrade confidence.**

- AnnotationTransferEvidence from a hippocampal scRNA-seq dataset with curator-labelled Cajal-Retzius cells (e.g. a Reln-Cre or Calb2-marked CR cohort) mapping onto CCN20230722; an F1 ≥ 0.80 at supertype level would lift this mapping from MODERATE to HIGH.
- BulkCorrelationEvidence from a sorted reelin+/calretinin+ CR preparation against CCN20230722 pseudobulks would corroborate the marker-driven assignment with a transcriptome-wide signal.
- A targeted literature scan for primary Calb2 and Slc17a8 (VGluT3) marker citations on morphologically-confirmed hippocampal CR cells would strengthen the multi-marker basis of the classical node beyond Reln alone.
- Resolution of the three axonal subtypes (layer-restricted local, cross-fissure local, long-range) against the supertype's child clusters would clarify whether the supertype maps 1:1 or 1:n to the classical type's sub-structure.

### 0497 HPF CR Glut_1 (cluster) · 🟡 MODERATE

**Property alignment (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | CA1 SLM [UBERON:0014557]; DG OML [UBERON:0001885] | Hippocampal formation; Dentate gyrus, molecular layer (SUPT_0135); region_fraction_100um=0.670 | Hippocampal formation; Dentate gyrus, molecular layer (CLUS_0497, count_100um=2358 of 2880 hippocampal); region_fraction_100um=0.694 | CONSISTENT |
| NT type | glutamatergic | not asserted (SUPT_0135) | Glut (CLUS_0497) | CONSISTENT |
| Reln expression | defining marker | mean 12.43; cohort percentile 0.990 (SUPT_0135) | mean 12.42; cohort percentile 0.987 (CLUS_0497) | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + region painting | Atlas metadata | PARTIAL | Reln=12.42 (cohort_pct 0.99); region_fraction_100um=0.694 | atlas-internal |

**Supporting evidence.**

- Cluster 0497 is the single child of supertype 0135 carrying the supertype's signal (2498 of 3116 supertype cells); its painted soma distribution centres on the dentate gyrus molecular layer (count_100um=2358 of 2880 hippocampal-formation cells), matching one of the two classical soma locations (OML).
- Cluster-level Reln expression (12.42, cohort percentile 0.987) is virtually identical to the parent supertype's mean and is the highest cluster-level Reln value in the rank-0 cohort, consistent with the classical type's defining marker.
- NT annotation at cluster level is Glut, confirming the glutamatergic identity that is only nominal at supertype rank.

**Concerns.**

- The classical soma definition includes two compartments — CA1 SLM and DG OML — but the cluster's painted distribution concentrates on DG molecular layer. CA1-SLM-resident CR cells described in [1] may map to a separate hippocampal-CR cluster not present at the cluster-level discovery, or may distribute thinly across the same supertype below the proximity-painting resolution.
- Cluster cell count (n=2498) is the dominant child of SUPT_0135, but a curator should verify whether sibling clusters (not surfaced in the top-K) correspond to a distinguishable CA1-SLM CR subtype.
- Sex ratio is not assessed in the edge YAML; classical literature does not document a sex bias for CR cells, but per-cluster sex MFR has not been pulled into property comparison.

**What would upgrade confidence.**

- AnnotationTransferEvidence from a Cajal-Retzius-targeted scRNA-seq cohort (Reln driver, Calb2 driver, or post-hoc reelin immunostaining on sequenced cells) with F1 ≥ 0.80 at cluster level would establish a 1:1 mapping.
- A targeted query for sibling clusters within SUPT_0135 carrying the CA1 stratum lacunosum-moleculare painted signal would test whether the classical type's CA1 component is captured by a distinct cluster.
- Cross-check of multi-marker concordance (Calb2, Slc17a8/VGluT3) at cluster level against the classical multi-marker definition would consolidate the cluster-level call.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] | — | 3116 | 🟡 MODERATE | Reln=12.43 (cohort_pct 0.99); DG molecular layer painted | Primary (supertype) |
| 0497 HPF CR Glut_1 [CS20230722_CLUS_0497] | 0135 HPF CR Glut_1 | 2498 | 🟡 MODERATE | Reln=12.42 (cohort_pct 0.99); DG molecular layer painted | Primary (cluster within supertype) |
| 0079 CA3 Glut_5 [CS20230722_SUPT_0079] | — | 318 | 🔴 LOW | CA3 / DG polymorph soma; Reln=0.16 | Eliminated (CA3 pyramidal cell class) |
| 0294 CA1-ProS Glut_6 [CS20230722_CLUS_0294] | 0074 CA1-ProS Glut_6 | 802 | 🔴 LOW | Prosubiculum painted; Reln=3.28 (cohort_pct 0.79) | Eliminated (prosubicular pyramidal, wrong cell class) |
| 0316 CA3 Glut_5 [CS20230722_CLUS_0316] | 0079 CA3 Glut_5 | 202 | 🔴 LOW | CA3 stratum radiatum painted; Reln=0.11 | Eliminated (CA3 pyramidal, Reln near-absent) |
| 0317 CA3 Glut_5 [CS20230722_CLUS_0317] | 0079 CA3 Glut_5 | 116 | 🔴 LOW | DG polymorph layer painted; Reln=0.21 | Eliminated (DG hilar / CA3 lineage, Reln low) |
| 0323 L2 IT PPP-APr Glut_2 [CS20230722_CLUS_0323] | 0081 L2 IT PPP-APr Glut_2 | 951 | 🔴 LOW | Presubiculum L2 IT; Reln=0.20 | Eliminated (presubicular L2 IT, wrong subclass) |
| 0137 DG Glut_2 [CS20230722_SUPT_0137] | — | 74950 | 🔴 LOW | DG granule cell layer (n=74950); Reln=0.22 | Eliminated (DG granule cells, wrong cell class) |
| 0138 DG Glut_3 [CS20230722_SUPT_0138] | — | 964 | 🔴 LOW | DG granule cell layer; Reln=0.61 | Eliminated (DG granule lineage, wrong cell class) |
| 0139 DG Glut_4 [CS20230722_SUPT_0139] | — | 5166 | 🔴 LOW | DG polymorph layer; Reln=0.27 | Eliminated (DG mossy-cell-region, wrong cell class) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** hippocampal Cajal-Retzius cell is defined by the reelin-positive (Reln) defining marker, glutamatergic NT type, and soma locations in CA1 stratum lacunosum-moleculare and the outer molecular layer of the dentate gyrus, with the `definition_basis` value `CLASSICAL_MULTIMODAL` — the classical evidentiary base combines optogenetic functional characterisation [1], anatomical reconstruction of cross-fissure local-projecting axons [2], adult-rat density assessment [3], and reelin-positive cell phenotyping [4].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:391 + MBA:726, NT type = glutamatergic, defining marker = Reln). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Evidence base across candidates.**

| Candidate | Evidence types | Headline |
|---|---|---|
| CS20230722_SUPT_0135 | ATLAS_METADATA | Reln=12.43 (pct 0.99); region_fraction_100um=0.670 |
| CS20230722_CLUS_0497 | ATLAS_METADATA | Reln=12.42 (pct 0.99); region_fraction_100um=0.694 |
| CS20230722_CLUS_0294 | ATLAS_METADATA | Reln=3.28 (pct 0.79); region_fraction_100um=0.582 |
| CS20230722_CLUS_0316 | ATLAS_METADATA | Reln=0.11 (pct 0.14); region_fraction_100um=0.646 |
| CS20230722_CLUS_0317 | ATLAS_METADATA | Reln=0.21 (pct 0.29); region_fraction_100um=0.997 |
| CS20230722_CLUS_0323 | ATLAS_METADATA | Reln=0.20 (pct 0.25); region_fraction_100um=0.504 |
| CS20230722_SUPT_0079 | ATLAS_METADATA | Reln=0.16 (pct 0.16); region_fraction_100um=0.953 |
| CS20230722_SUPT_0137 | ATLAS_METADATA | Reln=0.22 (pct 0.28); region_fraction_100um=0.996 |
| CS20230722_SUPT_0138 | ATLAS_METADATA | Reln=0.61 (pct 0.53); region_fraction_100um=0.995 |
| CS20230722_SUPT_0139 | ATLAS_METADATA | Reln=0.27 (pct 0.33); region_fraction_100um=0.853 |

</details>

---

## Discussion

### Best candidate + caveats

The primary mapping is to supertype 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] (broader, supertype-level placement) with cluster 0497 HPF CR Glut_1 [CS20230722_CLUS_0497] as the dominant child carrying the supertype's reelin signal. The Cell Ontology mapping is BROAD: CL:0000695 (Cajal-Retzius cell) covers the general class — cortical and hippocampal, embryonic and adult, glutamatergic and GABAergic combined — whereas the classical node targets the narrower adult-persisting, hippocampal, glutamatergic, reelin+/calretinin+/VGluT3+ subpopulation. The mapping is therefore confidently anchored on cell class but requires a more specific Cell Ontology term to capture the adult hippocampal glutamatergic CR subset.

The supportable evidence base is currently atlas-internal (precomputed Reln expression and region painting); no annotation transfer, bulk correlation, or extracted literature evidence is attached to the edges yet, which holds the confidence at MODERATE rather than HIGH. The classical node also flags substantial within-CR heterogeneity (a GABAergic fraction excluded from this glutamatergic node; three axonal subtypes) that the supertype-level mapping necessarily pools.

### Open questions and recommended next steps

- Retrieve and run annotation transfer from a hippocampal scRNA-seq cohort with curator-labelled Cajal-Retzius cells (e.g. driver-targeted Reln+, Calb2+, or Slc17a8+ CR populations) against CCN20230722; F1 ≥ 0.80 at SUPT_0135 would lift the mapping to HIGH.
- Resolve the CA1-SLM vs DG-OML soma compartments against the supertype's child clusters: cluster 0497 painted distribution centres on DG molecular layer; the CA1-SLM component of the classical type's soma definition may map to a distinct sibling cluster not currently in the top-K candidate set.
- Curate primary citations for Calb2 and Slc17a8 (VGluT3) on morphologically-confirmed hippocampal CR cells to broaden the marker basis beyond Reln.
- Consider whether the three axonal subtypes (layer-restricted local, cross-fissure local, long-range) reported in [2] and related anatomy literature warrant subdivision of the classical node, with each sub-node tested against the supertype's child-cluster structure.
- File a Cell Ontology term-request for an adult hippocampal glutamatergic Cajal-Retzius cell narrower than CL:0000695 once the supporting evidence base matures.

---

## References

[1] Quattrocolo & Maccaferri 2014 · PMID:25253849
[2] Anstotz et al. 2015 · PMID:26582498
[3] Wheeler et al. 2015 · PMID:26402459
[4] Yu et al. 2014 · PMID:25206826

---

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0135 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0135
  confidence: MODERATE
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  rationale: "[tier:STRONGEST] Atlas supertype 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] aligns with the classical hippocampal Cajal-Retzius cell on its primary defining marker (Reln mean 12.43, cohort percentile 0.990, child-coverage 1.000) and on painted soma distribution centred on dentate gyrus molecular layer (region_fraction_100um=0.670). The supertype name itself encodes a hippocampal CR glutamatergic identity matching the classical type. Confidence held at MODERATE because the evidence base is atlas-internal only; no cluster annotation transfer or targeted transcriptomic profiling evidence has been attached. The two named soma compartments of the classical type (CA1 SLM, DG OML) are pooled at supertype rank, and the classical-side within-type heterogeneity (three axonal subtypes; cross-fissure local projection) is not resolved at supertype granularity. Best child cluster CLUS_0497 holds the bulk of supertype cells (2498/3116) and carries the same Reln signal."
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: "Classical type pools three axonal subtypes (layer-restricted local, cross-fissure local, long-range); supertype-level mapping does not resolve these subdivisions."
    - caveat_type: SINGLE_STUDY
      description: "Reln is the single defining marker on the classical node; multi-marker concordance (Calb2, VGluT3) is not yet evidenced at transcript level on the atlas side."
    - caveat_type: AMBIGUOUS_MAPPING
      description: "Cell Ontology mapping CL:0000695 is BROAD; covers cortical+hippocampal, embryonic+adult, glutamatergic+GABAergic CR cells. A more specific term for the adult hippocampal glutamatergic subpopulation is currently unavailable."
  proposed_experiments:
    - "Annotation transfer from a hippocampal Cajal-Retzius-targeted transcriptomic cohort (Reln, Calb2, or Slc17a8 driver) against CCN20230722; target F1 >= 0.80 at supertype rank."
    - "Bulk-correlation analysis of sorted reelin+/calretinin+ adult hippocampal CR preparations against CCN20230722 pseudobulks."
    - "Targeted literature retrieval for primary Calb2 and Slc17a8 (VGluT3) citations on morphology-confirmed hippocampal CR cells to broaden the multi-marker classical definition."
  unresolved_questions:
    - "Do the three axonal subtypes of hippocampal CR cells correspond to distinguishable child clusters within SUPT_0135?"
    - "Does a separate child cluster within SUPT_0135 carry the CA1 stratum lacunosum-moleculare painted signal complementing the DG molecular layer dominance of CLUS_0497?"
  reconciliation_note: "Paired with cluster-level edge edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0497 (best-child within this supertype) which carries the cluster-level closeMatch."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0497 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0497
  confidence: MODERATE
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  rationale: "[tier:NEXT] Cluster 0497 HPF CR Glut_1 [CS20230722_CLUS_0497] is the dominant child of supertype SUPT_0135 (2498 of 3116 cells) and carries the highest cluster-level Reln signal in the hippocampal-glutamatergic rank-0 cohort (mean 12.42, cohort percentile 0.987). Painted soma distribution centres on dentate gyrus molecular layer (region_fraction_100um=0.694), aligning with the OML compartment of the classical soma description. NT annotation at cluster level is Glut, confirming glutamatergic identity. Confidence held at MODERATE because the evidence base is atlas-internal only; the CA1 stratum lacunosum-moleculare component of the classical soma definition is not reflected in the cluster's painted distribution and may map to a sibling cluster not surfaced in the candidate set."
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: "Classical soma definition includes both CA1 SLM and DG OML; cluster painted distribution centres on DG molecular layer with the CA1-SLM component not captured at this cluster's resolution."
    - caveat_type: SINGLE_STUDY
      description: "Reln is the only marker evidenced at transcript level on the cluster; multi-marker concordance (Calb2, VGluT3) is not yet attached."
  proposed_experiments:
    - "Annotation transfer from a hippocampal CR-targeted transcriptomic cohort against CCN20230722; F1 >= 0.80 at cluster rank would establish 1:1 mapping."
    - "Sibling-cluster query within SUPT_0135 for child clusters carrying CA1 stratum lacunosum-moleculare painted signal."
  unresolved_questions:
    - "Is the CA1-SLM CR population captured by a distinct sibling cluster within SUPT_0135 not currently in the top-K candidate set?"
    - "Do the multi-marker classical defining set (Reln + Calb2 + VGluT3) align quantitatively at cluster level?"
  reconciliation_note: "Paired with supertype-level edge edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0135 (parent supertype) which carries the broadMatch."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0294 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0294
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Cluster 0294 is a CA1-ProS pyramidal-class glutamatergic cluster with painted soma in prosubiculum / subiculum, not in CA1 SLM or DG OML; Reln expression (3.28, cohort percentile 0.791) is the second-highest in the rank-0 cohort but well below the dedicated CR cluster (CLUS_0497, mean 12.42), consistent with a different cell class that incidentally expresses Reln at moderate level. Cell class is wrong for hippocampal Cajal-Retzius cell."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in prosubiculum / subiculum, not in classical CR soma compartments (CA1 SLM, DG OML)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0316 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0316
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Cluster 0316 is a CA3 pyramidal-class cluster with painted soma in field CA3 stratum radiatum; Reln expression is near-absent (0.11, cohort percentile 0.138). Cell class is wrong for hippocampal Cajal-Retzius cell, and the defining marker is not present at meaningful level."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in CA3 stratum radiatum, not in classical CR soma compartments."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln near-absent (mean 0.11, cohort percentile 0.138)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0317 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0317
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Cluster 0317 (CA3 Glut_5) has painted soma in dentate gyrus polymorph layer (hilar region) consistent with a hilar / CA3 lineage cell, not Cajal-Retzius. Reln expression is low (0.21, cohort percentile 0.289). Cell class is wrong."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in DG polymorph layer (hilus), not in classical CR soma compartments (CA1 SLM, DG OML)."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln low (mean 0.21, cohort percentile 0.289)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0323 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_CLUS_0323
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Cluster 0323 is an L2 IT presubicular / area prostriata cluster (subclass L2 IT PPP-APr), painted predominantly in presubiculum; this is a cortical-type intratelencephalic projecting neuron class, not Cajal-Retzius. Reln low (0.20, cohort percentile 0.253)."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in presubiculum, not in classical CR soma compartments."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln low (mean 0.20, cohort percentile 0.253)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0079 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0079
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Supertype 0079 CA3 Glut_5 is a CA3-lineage glutamatergic supertype with child clusters in CA3 stratum radiatum and DG polymorph layer; Reln near-absent (0.16, cohort percentile 0.155). Cell class is wrong for hippocampal Cajal-Retzius cell."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in CA3 / DG polymorph layer, not in classical CR soma compartments."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln near-absent (mean 0.16, cohort percentile 0.155)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0137 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0137
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Supertype 0137 DG Glut_2 is the dentate gyrus granule cell supertype (n=74950, painted in dentate gyrus granule cell layer); this is the principal excitatory neuron class of the dentate gyrus, not Cajal-Retzius. Reln low (0.22, cohort percentile 0.282)."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in DG granule cell layer, not in OML or SLM."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln low (mean 0.22, cohort percentile 0.282)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0138 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0138
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Supertype 0138 DG Glut_3 is a dentate gyrus granule-lineage supertype painted in DG granule cell layer; cell class is wrong for hippocampal Cajal-Retzius cell. Reln modest (0.61, cohort percentile 0.534) but well below the dedicated CR supertype."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in DG granule cell layer."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln modest (mean 0.61) but well below the dedicated CR supertype (12.43)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0139 -->
```yaml
verdict:
  edge_id: edge_hpc_cajal_retzius_cell_to_CS20230722_SUPT_0139
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "n:1"
  rationale: "[tier:CUT] Supertype 0139 DG Glut_4 is a dentate gyrus polymorph-layer supertype (likely mossy-cell lineage) painted in DG polymorph layer; cell class is wrong for hippocampal Cajal-Retzius cell. Reln low (0.27, cohort percentile 0.330)."
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: "Painted soma in DG polymorph layer (hilus), not in OML or SLM."
    - caveat_type: MARKER_NOT_SPECIFIC
      description: "Reln low (mean 0.27, cohort percentile 0.330)."
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->
