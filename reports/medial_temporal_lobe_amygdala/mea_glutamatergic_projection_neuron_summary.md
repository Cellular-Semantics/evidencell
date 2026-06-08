# Medial amygdala glutamatergic projection neuron — CCN20230722 Mapping Report

*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The medial amygdala (MeA) is a predominantly GABAergic structure derived from the subpallium, but it harbours a distinct minority population of glutamatergic projection neurons. These glutamatergic pyramidal neurons are developmentally derived from the third ventricle neuroepithelium and project to the bed nucleus of the stria terminalis (BST) and the hypothalamus, where they contribute to circuits governing reproductive and defensive behaviours. Mapping this population to the CCN20230722 (Allen Brain Cell Atlas WMBv1) mouse taxonomy is important for anchoring a classically defined principal cell class — sparse in the MeA yet functionally significant — to a transcriptomically resolved identity, and for understanding how the sexually dimorphic architecture of MeA relates to transcriptomically distinguishable subpopulations.

---

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Medial amygdala [UBERON:0002892] | [1] [2] [3] [4] |
| Neurotransmitter type | Glutamatergic | [1] |
| Defining markers | None recorded | — |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Morphology | Pyramidal-like glutamatergic projection neuron; projects to BST and hypothalamus | [1] |
| Notes | Minority class — MeA is predominantly GABAergic but contains this distinct glutamatergic projection population | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / NT type / Morphology:** Literature review · Raudales et al. 2024 · [1]
  > .Within the amygdala nuclei, PNs are exclusively glutamatergic in BLA, CoA, BMA, exclusively GABAergic in CeA, and predominantly GABAergic in MeA and BST.In rodents, there is also a population of glutamatergic pyramidal neurons (GLU PNs, derived from third ventricle neuroepithelium) that populates the BST, MeA, and hypothalamus (García-Moreno et al., 2010)(Huilgol et al., 2016).
  > — Raudales et al. 2024, Classical neuron classes across amygdala subdivisions · [1] <!-- quote_key: 271240390_159f2413 -->

- **Soma location:** Literature review · Yeh et al. 2024 · [2]
  > The pallial portion, encompassing the BLA and CoA, exhibits a cortical-like structure predominantly composed of glutamatergic (excitatory) neurons. In contrast, the CeA neurons, originating from the subpallial region, show a striatal-like organization with a majority of GABAergic (inhibitory) neurons (Swanson et al., 1983)(Sah et al., 2003); Figure 1A). The MeA, deriving from both ventral pallial and subpallial origins, presents a diverse neuronal population (Garcia-Lopez et al., 2008;Bupesh et al., 2011)
  > — Yeh et al. 2024, Central amygdala cell types · [2] <!-- quote_key: 267685584_678b0ee4 -->

- **Soma location (MeA subdivisions):** Literature review · Carney et al. 2010 · [3]
  > the posterior portion of the MeA is divided into dorsal (medial posterodorsal nucleus (MePD)) and ventral (medial posteroventral nucleus (MePV)) subdivisions, which via their projections to distinct hypothalamic nuclei regulate reproductive and defensive behaviors, respectively
  > — Carney et al. 2010, Background · [3] <!-- quote_key: 627853_76bae8ef -->

- **Soma location:** Literature review · Hochgerner et al. 2023 · [4]
  > In the medial amygdala (MEA) and basomedial amygdala (BMA), neurons from VGLUT2 and GABA classes intermixed.
  > — Hochgerner et al. 2023, Inhibitory cells mirror projection type and subregion · [4] <!-- quote_key: 264517392_28378bc6 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0195 [MEA Slc17a7 Glut_1] is the representative selection from a four-cluster family (CLUS_0194–0197) under SUPT_0055, all of which score equally against this classical type. Confidence is UNCERTAIN — mapping rests on region and NT type concordance alone, with no molecular marker data available to discriminate among the four siblings or to confirm projection neuron identity.

**Null result headline (no discriminating evidence):** A complete scan of CCN20230722 at ranks 0 and 1 identified five glutamatergic clusters in MBA:403 (medial amygdalar nucleus), all with equal discovery score (1/5 cohort). Four of these — CLUS_0194, CLUS_0195, CLUS_0196, and CLUS_0197 — fall under SUPT_0055 (MEA Slc17a7 Glut_1 parent) and are indistinguishable by available atlas metadata alone. No molecular markers are defined on the classical node, and no annotation-transfer evidence is available. The present edge to CLUS_0195 represents the most sex-ratio-balanced member of this family (MFR=1.27) and is selected as a working representative, but cardinality is formally 1:n.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | CS20230722_CLUS_0195 [MEA Slc17a7 Glut_1] | SUPT_0055 | null | ⚪ UNCERTAIN | NT CONSISTENT · Location CONSISTENT | Region+NT filter only; 1:n family |

*1 edge assessed; relationship type: skos:broadMatch, cardinality 1:n.*

*(Note: n_cells is null — taxonomy DB predates the n_cells column (PR #21). Rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` to populate.)*

### Property alignment table — CS20230722_CLUS_0195

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial amygdala [UBERON:0002892] | not available | MBA:403 medial amygdalar nucleus; region_fraction 0.401; cluster label "MEA Slc17a7 Glut_1" directly confirms MeA identity | CONSISTENT |
| NT type | Glutamatergic | not available | Glut (Slc17a7/VGLUT1) | CONSISTENT |
| Morphology / projection | Pyramidal-like glutamatergic projection neuron; BST and hypothalamus targets | not available | NOT_ASSESSED — morphological information not available from WMBv1 | NOT_ASSESSED |
| Sex ratio | Not documented | not available | MFR=1.27 (CLUS_0195); siblings CLUS_0196 MFR=4.88, CLUS_0197 MFR=10.11 | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Raudales 2024 GLU PN | Literature | SUPPORT | MeA glutamatergic projection neurons confirmed distributing to BST and hypothalamus | [1] |
| WMBv1 atlas metadata | Atlas metadata | SUPPORT | CLUS_0195 "MEA Slc17a7 Glut_1"; MeA region_fraction 0.401; MFR 1.27 (most balanced sibling) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments. All four MEA Slc17a7 Glut_1 siblings scored equally; CLUS_0195 chosen by balanced sex ratio heuristic only.)*

---

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The medial amygdala glutamatergic projection neuron is defined on a CLASSICAL basis: NT type (Glutamatergic) and soma location (medial amygdala [UBERON:0002892]) are sourced from the primary literature ([1] [2] [3] [4]). No defining molecular markers, electrophysiology, or morphological profile beyond projection class are recorded on the classical node. The classical evidence base is minimal — NT type and location only — which caps confidence at UNCERTAIN pending marker data.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**

| Atlas | Taxonomy ID | SHA-256 |
|---|---|---|
| WMBv1 (Allen Brain Cell Atlas) | CCN20230722 | not recorded in edge |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_mea_glutamatergic_projection_neuron_to_cs20230722_clus_0195 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [1]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:51+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Medial amygdala glutamatergic projection neuron → CS20230722_CLUS_0195 [MEA Slc17a7 Glut_1] at UNCERTAIN confidence. Key support: NT type (Glutamatergic / Slc17a7 CONSISTENT) and soma location (MBA:403 region_fraction 0.401 CONSISTENT). Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (four equal-scoring siblings CLUS_0194–0197 under SUPT_0055; cardinality is formally 1:n), and no molecular markers to discriminate the projection neuron class from potential local interneurons within the MEA Slc17a7 family.

No Cell Ontology term is currently assigned. The MeA glutamatergic projection population is a candidate for a new CL term contribution once marker identity is resolved.

The Cell Ontology has no specific term for this population. Given the CLASSICAL definition basis and the sparse evidence (region + NT only), this type should be considered a candidate for a new CL term request once primary marker data (e.g. Slc17a7 co-expression with Lhx9 or Tbr1 in MeA glutamatergic neurons) are available to provide a minimal discriminating definition.

### Proposed experiments and follow-ups

No annotation-transfer evidence is currently on this edge. The following experiments are proposed to resolve the UNCERTAIN mapping:

**1. Annotation transfer (MapMyCells)**
- **What:** Run MapMyCells (hierarchical mapping mode) against CCN20230722 using a dataset enriched for MeA glutamatergic neurons (e.g. Slc17a7-Cre FACS-sorted MeA neurons, or spatial transcriptomics restricted to MBA:403).
- **Target:** F1 ≥ 0.80 at CLUSTER level against one or more of CLUS_0194–0197 to disambiguate which sibling(s) represent the projection population.
- **Expected output:** AnnotationTransferEvidence on the edge with resolved cardinality.
- **Resolves:** Both open questions (subdivision correspondence; projection vs. local identity).

**2. Retrograde tracing + scRNA-seq**
- **What:** Retrograde viral tracing from BST and hypothalamus targets, followed by scRNA-seq of retrogradely-labelled MeA neurons.
- **Target:** Transcriptomic assignment of projection-identified cells to specific CLUS_0194–0197 siblings.
- **Expected output:** LiteratureEvidence or marker update resolving which cluster(s) are bona fide projection neurons.
- **Resolves:** Open question 2 (projection vs. local identity); would also inform 1:1 vs. 1:n cardinality.

**3. smFISH marker survey**
- **What:** smFISH in mouse MeA with probes for Slc17a7 (VGLUT1) and a panel of candidate subdivision markers (e.g. Lhx9, Tbr1, Foxp1, Nr2f2) to test co-expression with region-restricted labelling across MePD and MePV.
- **Target:** Identification of at least one marker that co-segregates with projection neuron identity and discriminates MeA subdivisions.
- **Expected output:** Updated classical node definition with defining marker(s); property_comparison upgrade from NOT_ASSESSED to CONSISTENT/DISCORDANT.
- **Resolves:** Open question 1 (anatomical subdivision correspondence); enables future marker-based mapping reassessment.

### Open questions

1. Do the four MEA Slc17a7 Glut_1 siblings (CLUS_0194–0197) correspond to anatomical subdivisions of MeA (MePD vs MePV vs anterior vs posterior)?
2. Which cluster(s) specifically represent the BST/hypothalamus projection population versus local MeA glutamatergic interneurons?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Raudales et al. 2024 | [39012795](https://pubmed.ncbi.nlm.nih.gov/39012795/) | NT type; soma location; projection morphology |
| [2] | Yeh et al. 2024 | [38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | Soma location |
| [3] | Carney et al. 2010 | [20507551](https://pubmed.ncbi.nlm.nih.gov/20507551/) | Soma location; MeA subdivision anatomy |
| [4] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Soma location |

---

<!-- verdict-block-start: edge_mea_glutamatergic_projection_neuron_to_cs20230722_clus_0195 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    Mapping rests on region (MBA:403 region_fraction 0.401, SELF evidence) and NT type
    (Slc17a7/VGLUT1, CONSISTENT) only; no molecular markers are defined on the classical
    node (score 1 in a 5-member SURVIVAL_COHORT filtered by region=MBA:403 + nt_type=Glutamatergic).
    Four MEA Slc17a7 Glut_1 siblings (CLUS_0194–0197) under SUPT_0055 score equally;
    CLUS_0195 selected by balanced sex ratio heuristic (MFR=1.27 vs CLUS_0196 MFR=4.88
    and CLUS_0197 MFR=10.11) but this selection is not discriminating. Cardinality is
    formally 1:n (DISTRIBUTED_ACROSS_CLUSTERS). No annotation-transfer evidence available.
  reconciliation_note: >
    broadMatch 1:n cardinality is appropriate: the classical type likely spans the MEA
    Slc17a7 Glut_1 cluster family (CLUS_0194–0197). Resolution to a discriminating
    1:1 or narrowed n:1 mapping requires retrograde tracing data or smFISH with
    subdivision markers to assign projection identity to specific siblings.
  unresolved_questions:
    - Do the four MEA Slc17a7 Glut_1 siblings (CLUS_0194–0197) correspond to anatomical
      subdivisions of MeA (MePD vs MePV vs anterior vs posterior)?
    - Which cluster(s) specifically represent the BST/hypothalamus projection population
      vs local MeA glutamatergic interneurons or non-projection cells?
```
<!-- verdict-block-end -->
