# CA1 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

CA1 pyramidal cells are the dominant glutamatergic projection population of Ammon's
horn area CA1, with somata in the pyramidal layer of CA1 [UBERON:0014548] and a major
axonal output via the subiculum to entorhinal cortex. They constitute one of the
classical principal-cell populations of the hippocampal formation [UBERON:0002421] —
together with CA2/CA3 pyramidal cells, mossy cells, and granule cells — and
collectively these glutamatergic principal cells dominate hippocampal cytoarchitecture.

> Glutamatergic neurons dominate the hippocampal architecture, accounting for over
> 90% of all hippocampal neurons, with pyramidal layers being densely packed with
> these excitatory cells (Mancini et al., 2022).
> — Mancini et al. 2022, Classical Hippocampal Circuit Organization · [5] <!-- quote_key: 252086716_9d46d627 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1], [2], [3], [4], [5] |
| Neurotransmitter | glutamatergic | [4] |
| Defining markers | Wfs1 | [6], [7], [8], [9], [10] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomical and molecular characterisation of CA1
  pyramidal cells in mouse · [1], [2], [3], [4], [5]
  > we used next-generation RNA sequencing (RNA-seq) to produce a quantitative,
  > whole genome characterization of gene expression for the major excitatory
  > neuronal classes of the hippocampus; namely, granule cells and mossy cells of
  > the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
  > — Cembrowski et al. 2016, abstract · [1] <!-- quote_key: 4875295_4a456257 -->

  > The Cornu Ammonis‐1 (CA1) subfield and subiculum (SUB) serve as major output
  > structures of the hippocampal formation
  > — Müller & Remy 2017, abstract · [2] <!-- quote_key: 2171766_537d45ba -->

- **Neurotransmitter:** glutamatergic identity established across the major
  hippocampal pyramidal populations · [4]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic
  > pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic
  > granule cells in the DG (Figure 1). They generally have excitatory effects on
  > the neurons to which they send axon terminals including other glutamatergic
  > and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine
  > (DA)], cholinergic, and histaminergic (HA) cells.
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [4] <!-- quote_key: 2281033_5b9805ff -->

- **Wfs1 marker:** wolframin is a CA1-enriched membrane protein used as a
  CA1 / deep-sublayer pyramidal cell marker · [6], [7], [8], [9], [10]
  > Virtually all projection neurons across hippocampal subfields contain subunits
  > from the AMPA/kainate, kainate, and NMDA receptor families, with these
  > receptors being broadly colocalized in hippocampal neurons and even at
  > individual dendritic spines (Siegel et al., 1995).
  > — Siegel et al. 1995, Synaptic Properties and Neurotransmitter Systems · [6] <!-- quote_key: 5468451_9958f302 -->

  > Neuroplastin-65 positive glutamatergic neurons: These include granule neurons
  > of the dentate gyrus, pyramidal neurons of CA1, CA2-3, subiculum, and specific
  > layers of entorhinal cortex (Herrera-Molina et al., 2017)(Langnaese et al.,
  > 1997). Neuroplastin-65 is abundant at membranes of cell bodies, dendrites, and
  > in punctate structures within the neuropil, and plays important roles in
  > regulating excitatory synapse number and function (Herrera-Molina et al.,
  > 2017)(Herrera-Molina et al., 2014).
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [8] <!-- quote_key: 3288675_d83802d0 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD).

**Proposed CL term:** *CA1 pyramidal cell* (SUBMITTED). Candidate-definition prose: A hippocampal pyramidal neuron with soma located in the pyramidal layer of hippocampal area CA1 (UBERON:0014548) (Cembrowski et al., 2016; Müller & Remy, 2017), forming the dominant excitatory projection population of the CA1 subfield. As the primary output cell of Ammon's horn, it projects via the subiculum to entorhinal cortex and is capable of glutamate secretion as a neurotransmitter (Dale et al., 2015). In mouse, it is distinguished from CA2 and CA3 pyramidal neurons by soma position within the CA1 stratum pyramidale and by expression of wolframin (Wfs1), an endoplasmic reticulum-resident membrane protein enriched in deep-sublayer CA1 cells (Cembrowski et al., 2016).

---

## Results

Marker (Wfs1) concordance, region alignment, and annotation transfer of Yao et al.
CA1-ProS labels support mapping the CA1 pyramidal cell to the dedicated CA1-ProS
glutamatergic supertype 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]
(F1=0.79 at supertype level; see figure and property comparison table). Within that
supertype, 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] is the AT-leading and
region-best child cluster; the broader CA1 pyramidal population scatters across
all four CA1-ProS Glut supertypes (SUPT_0069 through SUPT_0072) and across multiple
clusters within them, consistent with the well-documented sublayer (deep vs.
superficial) and proximo-distal heterogeneity of CA1.

**Annotation-transfer overview figure (Yao 2021 hippocampal formation → WMBv1)**

![Filtered AT figure for CA1 pyramidal cell](figures/f1_for_ca1_pc_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GSE185862) CA1-ProS source group
(n=1590 cells reaching the class level after filtering). Coverage = fraction of
source-group cells landing on the target; Purity = fraction of this target's
cells coming from the source group. With a single source group in the figure,
Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a
level indicates a clean mapping at that resolution; the subclass-level value
(016 CA1-ProS Glut, F1=0.99) shows the CA1-ProS branch is essentially
encapsulated by one WMBv1 subclass, while the cluster-level drop (0262 CA1-ProS
Glut_1, F1=0.44) reflects distribution of CA1-ProS cells across several CA1-ProS
clusters.*

The cluster-level scatter is the expected fingerprint of CA1 sublayer
heterogeneity rather than a mapping failure; resolving sublayer correspondence
across SUPT_0069 – SUPT_0072 requires a sublayer-resolved source dataset (see
Discussion).

### 0069 CA1-ProS Glut_1 · 🟡 MODERATE

**Property alignment (Table 1):**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Field CA1, pyramidal layer [MBA:407] (27305 of 28476 cells within 100µm) | Field CA1, pyramidal layer [MBA:407] (CLUS_0262: 19403 of 19886 cells within 100µm) | CONSISTENT |
| NT type | glutamatergic | not asserted | Glut (CLUS_0262) | NOT_ASSESSED (supertype); CONSISTENT (cluster) |
| Wfs1 expression | defining marker | mean 3.97 (cohort percentile 0.83; child-cluster coverage 1.00) | mean 7.68 (cohort percentile 0.98) on CLUS_0262 | CONSISTENT |

*(All 5 child clusters of SUPT_0069 show Wfs1 expression above the cohort median
(child-cluster coverage 1.00); CLUS_0262 leads with Wfs1=7.68 (cohort percentile
0.98) and the highest in-region cell count of any CA1-ProS cluster.)*

**Evidence support (Table 2):**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + region painting (SUPT_0069) | Atlas metadata | SUPPORT | Wfs1=3.97; 27305 cells in CA1 pyramidal layer | atlas-internal |
| Annotation transfer (Yao 2021 → WMBv1) | Annotation transfer | SUPPORT | F1=0.79 (supertype); F1=0.99 (subclass 016 CA1-ProS Glut) | atlas-internal |

**Supporting evidence**

- 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] is the highest-scoring WMBv1
  supertype in the CA1-pyramidal-layer × glutamatergic cohort (Stage A
  cohort-rank 1 of 29; tied score with SUPT_0072, SUPT_0073, SUPT_0074 at the
  supertype level, but SUPT_0069 carries the largest CA1-pyramidal-layer cell
  count and the highest annotation-transfer coverage from CA1-ProS source
  labels). Region alignment is strong: `region_fraction_100um: 0.959` against
  MBA:407 (Field CA1, pyramidal layer).

- Annotation transfer from Yao 2021 (GSE185862) hippocampal formation labels
  onto CCN20230722 places 0.99 of the CA1-ProS source-cell coverage onto the
  016 CA1-ProS Glut subclass (F1=0.99 at subclass level; n=1574 cells), and
  0.65 of that coverage onto SUPT_0069 specifically (F1=0.79). Purity at the
  supertype is 1.0 — every SUPT_0069 target cell that received a label in this
  annotation transfer run came from CA1-ProS. The remainder of the CA1-ProS
  coverage distributes across SUPT_0070, SUPT_0071, SUPT_0072, and SUPT_0073,
  all within the same subclass.

- Wfs1 expression is consistent at the supertype mean and present across all
  child clusters (child-cluster coverage 1.000). In the classical literature
  Wfs1 marks deep-sublayer CA1 pyramidal cells; the elevated cohort percentile
  on CLUS_0262 (0.98) and CLUS_0263 (0.99) is the expected fingerprint of the
  deep-CA1 children of this supertype.

**Concerns**

- The classical CA1 pyramidal cell type encompasses *at least four* WMBv1
  supertypes (SUPT_0069 through SUPT_0072) within subclass 016 CA1-ProS Glut.
  SUPT_0069 is the primary correspondence by annotation-transfer coverage and
  Wfs1 percentile, but a complete mapping of the classical population requires
  sibling edges to SUPT_0070, SUPT_0071, and SUPT_0072 (and possibly SUPT_0073,
  SUPT_0074), which the wider CA1 PC population also touches. The relationship
  is therefore one classical type → many atlas supertypes.

- No CA1-specific Cell Ontology term currently exists; CL:1001571 (hippocampal
  pyramidal neuron) is the closest ancestor and covers CA1, CA2, and CA3
  pyramidal populations together.

**What would upgrade confidence:**

- Annotation transfer using a sublayer-resolved CA1 pyramidal cell source dataset
  (Cembrowski 2016 deep vs. superficial CA1 PC labels, or Zeisel 2018 dorsal CA1
  pyramidal cell labels) onto WMBv1, with a per-supertype coverage breakdown
  across SUPT_0069 – SUPT_0072. Expected evidence type: AnnotationTransferEvidence
  with sublayer-resolved source labels; threshold F1 ≥ 0.80 at supertype level
  for the leading sublayer mapping.

### 0262 CA1-ProS Glut_1 · 🟡 MODERATE

**Property alignment (Table 1):**

| Property | Classical | Supertype (SUPT_0069) | Best cluster (CLUS_0262) | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | 27305 of 28476 cells within 100µm of MBA:407 | 19403 of 19886 cells within 100µm of MBA:407 | CONSISTENT |
| NT type | glutamatergic | not asserted | Glut | CONSISTENT |
| Wfs1 expression | defining marker | mean 3.97 (cohort percentile 0.83) on SUPT_0069 | mean 7.68 (cohort percentile 0.98) on CLUS_0262 | CONSISTENT |

*(Of the 5 SUPT_0069 child clusters, CLUS_0262 leads in both Wfs1 expression
(7.68, cohort percentile 0.98) and CA1-pyramidal-layer cell count (19403 within
100µm). CLUS_0263 is the immediate runner-up (Wfs1=7.75, percentile 0.99; 5398
cells in MBA:407). Cluster-level Yao-CA1-ProS annotation transfer places
CLUS_0262 as the best-cluster target at F1=0.44 (purity 1.0; coverage 0.28).)*

**Evidence support (Table 2):**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + region painting (CLUS_0262) | Atlas metadata | PARTIAL | Wfs1=7.68; 19403 cells in CA1 pyramidal layer | atlas-internal |

**Supporting evidence**

- CLUS_0262 is the leading cluster in its 50-member CA1-pyramidal-layer ×
  glutamatergic cohort (Stage A cohort-rank 1 of 50). Region alignment is
  excellent (`region_fraction_100um: 0.975`); the strict in-region fraction
  (`region_fraction: 0.468`) reflects boundary scatter at the pyramidal-layer
  border rather than off-target placement.

- Wfs1 expression is at the cohort 98th percentile, matching the classical
  "deep-sublayer CA1" expression signature.

- This cluster is the leading cluster within SUPT_0069 from the Yao 2021
  CA1-ProS source group (F1=0.44, purity 1.0, coverage 0.28; the four other
  SUPT_0069 children and other CA1-ProS supertypes absorb the remaining
  coverage).

**Concerns**

- The cluster-level F1 (0.44) is well below the supertype-level F1 (0.79),
  indicating that CA1-ProS source cells distribute across multiple CA1-ProS Glut
  clusters rather than collapsing cleanly onto CLUS_0262. CLUS_0263 carries
  even higher Wfs1 expression (7.75 vs. 7.68); CLUS_0262 leads by sheer cell
  count and slight annotation-transfer advantage, not by an unambiguous marker
  signature.

- No sublayer-resolved source dataset has yet been mapped onto WMBv1, so the
  question of whether CLUS_0262 corresponds to deep-CA1, superficial-CA1, or
  some other sublayer / proximo-distal axis remains unresolved.

**What would upgrade confidence:**

- A sublayer-resolved CA1 PC annotation transfer (Cembrowski 2016 or Zeisel
  2018) onto WMBv1 to resolve which of SUPT_0069's child clusters
  (CLUS_0261 – CLUS_0266) corresponds to which CA1 sublayer / proximo-distal
  position. Expected evidence type: AnnotationTransferEvidence with sublayer
  labels; threshold F1 ≥ 0.80 at cluster level for the leading sublayer.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 target | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]` (curator-built edge) | — | 19061 | 🟡 MODERATE | CA1-ProS AT F1=0.79; Wfs1 percentile 0.83 | Primary |
| `0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262]` | 0069 CA1-ProS Glut_1 | 12018 | 🟡 MODERATE | Wfs1=7.68 (cohort percentile 0.98); leading SUPT_0069 child by region + AT | Secondary (best child within SUPT_0069) |
| `0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]` (fresh-emit edge) | — | 19061 | ⚪ UNCERTAIN | Duplicate of curator-built edge (same accession) | Eliminated (duplicate edge ID on same accession; curator-built edge prevails) |
| `0263 CA1-ProS Glut_1 [CS20230722_CLUS_0263]` | 0069 CA1-ProS Glut_1 | 4105 | 🔴 LOW | Wfs1=7.75; in CA1 pyramidal layer | Supports broader mapping (sibling within SUPT_0069) |
| `0072 CA1-ProS Glut_4 [CS20230722_SUPT_0072]` | — | 3493 | 🔴 LOW | Wfs1=4.78; 0.88 in CA1 pyramidal layer | Supports broader mapping (sibling supertype within CA1-ProS subclass) |
| `0070 CA1-ProS Glut_2 [CS20230722_SUPT_0070]` | — | 4609 | 🔴 LOW | Wfs1=3.84; soma in CA1 stratum oriens | Supports broader mapping (sibling supertype, stratum oriens children) |
| `0073 CA1-ProS Glut_5 [CS20230722_SUPT_0073]` | — | 898 | 🔴 LOW | Wfs1=2.41; soma in CA1 stratum oriens | Supports broader mapping (sibling supertype, lower Wfs1) |
| `0074 CA1-ProS Glut_6 [CS20230722_SUPT_0074]` | — | 1921 | 🔴 LOW | Wfs1=6.79 but only 0.41 in CA1 pyramidal layer | Eliminated (predominantly prosubicular, not CA1 pyramidal layer) |
| `0293 CA1-ProS Glut_6 [CS20230722_CLUS_0293]` | 0074 CA1-ProS Glut_6 | 983 | 🔴 LOW | Wfs1=6.75; only 0.50 in CA1 pyramidal layer | Eliminated (predominantly prosubicular) |
| `0261 CA1-ProS Glut_1 [CS20230722_CLUS_0261]` | 0069 CA1-ProS Glut_1 | 215 | 🔴 LOW | Wfs1=4.29; 0.71 in CA1, soma in stratum oriens | Eliminated (stratum oriens, not pyramidal layer; smallest sibling) |
| `0266 CA1-ProS Glut_1 [CS20230722_CLUS_0266]` | 0069 CA1-ProS Glut_1 | 130 | 🔴 LOW | Wfs1=2.69 (cohort percentile 0.53); soma in stratum oriens | Eliminated (low Wfs1; stratum oriens) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The CA1 pyramidal cell node is defined under
`CLASSICAL_MULTIMODAL`: glutamatergic neurotransmitter identity [4], soma in
pyramidal layer of CA1 [UBERON:0014548] [1], [2], [3], [4], [5], and Wfs1 as a
defining marker [6], [7], [8], [9], [10].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match against MBA:407 Field CA1 pyramidal layer,
glutamatergic NT filter, and Wfs1 expression). Full scoring rules:
`workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
each candidate cluster / supertype (taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (CA1-ProS) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells (default parameters) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. Authored-prose evidence narratives are validated
against their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the Discussion
section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:48+00:00 from
[kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ca1_pc_hippocampus_to_supt_0069 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0262 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0263 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0293 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0261 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0266 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0069 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0074 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0073 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0072 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0070 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** CA1 pyramidal cell → 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069]
at MODERATE confidence. Key support: annotation transfer of Yao 2021 (GSE185862)
CA1-ProS source labels (F1=0.79 at supertype, F1=0.99 at the parent CA1-ProS Glut
subclass) and consistent Wfs1 expression on all SUPT_0069 children. Key caveats:
AMBIGUOUS_MAPPING (the classical CA1 PC type spans SUPT_0069 – SUPT_0072 within
subclass 016 CA1-ProS Glut, with SUPT_0069 as the primary correspondence); the
best-child cluster within SUPT_0069 is CLUS_0262 by joint region + AT + Wfs1
criteria, but no sublayer-resolved source data have yet been transferred to resolve
which of CLUS_0261 – CLUS_0266 corresponds to which CA1 sublayer. The Cell
Ontology has no specific term for CA1 pyramidal cells; hippocampal pyramidal neuron
[[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)]
is the closest ancestor (BROAD). CA1 pyramidal cells are a subpopulation of
hippocampal pyramidal neurons; CL:1001571 covers all hippocampal pyramidal neurons
and is therefore a BROAD match. No CA1-specific CL term currently exists.

### Proposed experiments and follow-ups

- **What:** Annotation transfer of a sublayer-resolved CA1 PC source dataset
  (Cembrowski 2016 deep vs. superficial CA1 PCs, or Zeisel 2018 dorsal CA1 PC
  labels) onto WMBv1 CCN20230722, with per-supertype and per-cluster coverage
  reporting across SUPT_0069 – SUPT_0074.
  **Target:** F1 ≥ 0.80 at SUPERTYPE level for the leading sublayer; F1 ≥ 0.70 at
  CLUSTER level for the leading cluster within that supertype.
  **Expected output:** AnnotationTransferEvidence with sublayer source labels on
  the SUPT_0069 / CLUS_0262 edges (and sibling edges as appropriate).
  **Resolves:** open questions 1 and 2 below; what was already done — Yao 2021
  CA1-ProS subclass-level annotation transfer (this report) — confirmed the
  CA1-ProS branch encapsulation at the subclass level (F1=0.99) and identified
  SUPT_0069 + CLUS_0262 as the leading targets, but the Yao 2021 source labels
  are not sublayer-resolved and so cannot answer the deep / superficial question.

### Open questions

1. Which of SUPT_0069 – SUPT_0072 correspond to deep vs. superficial CA1
   pyramidal cell sublayers? Wfs1 marks deep-layer CA1 PCs in the classical
   literature; checking which supertype carries the highest Wfs1 percentile in
   the atlas (the current data place this on SUPT_0069 / CLUS_0262 / CLUS_0263)
   suggests SUPT_0069 represents the deep-layer population, but this needs
   direct confirmation via sublayer-resolved annotation transfer.
2. Which of the SUPT_0069 child clusters (CLUS_0261, CLUS_0262, CLUS_0263,
   CLUS_0266) correspond to deep vs. superficial CA1, and which capture the
   proximo-distal axis? CLUS_0262 leads on combined region + annotation-transfer
   + Wfs1 evidence, but CLUS_0263 carries higher Wfs1 expression; CLUS_0261 and
   CLUS_0266 are stratum-oriens-leaning and likely represent a non-pyramidal-
   layer subpopulation.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915) | soma location |
| [2] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747) | soma location |
| [3] | https://doi.org/10.1038/s41598-017-11268-z | — | soma location |
| [4] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726) | soma location |
| [5] | Mancini et al. 2022 | [37011759](https://pubmed.ncbi.nlm.nih.gov/37011759) | soma location |
| [6] | Siegel et al. 1995 | [7722624](https://pubmed.ncbi.nlm.nih.gov/7722624) | Wfs1 marker |
| [7] | Yeung et al. 2020 | [32009891](https://pubmed.ncbi.nlm.nih.gov/32009891) | Wfs1 marker |
| [8] | Herrera-Molina et al. 2017 | [28779130](https://pubmed.ncbi.nlm.nih.gov/28779130) | Wfs1 marker |
| [9] | Langnaese et al. 1997 | [8995369](https://pubmed.ncbi.nlm.nih.gov/8995369) | Wfs1 marker |
| [10] | Herrera-Molina et al. 2014 | [24554721](https://pubmed.ncbi.nlm.nih.gov/24554721) | Wfs1 marker |

---

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_supt_0069 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.7
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer of Yao 2021 (GSE185862) CA1-ProS
    source labels onto WMBv1 places F1=0.99 at the 016 CA1-ProS Glut subclass
    and F1=0.79 at CS20230722_SUPT_0069 (run_ref
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1); 1 of 1 markers CONSISTENT
    (Wfs1 mean 3.97, cohort percentile 0.83, child-cluster coverage 1.00);
    region_fraction_100um 0.959 against MBA:407 Field CA1 pyramidal layer.
    The classical CA1 PC population spans CS20230722_SUPT_0069 through
    CS20230722_SUPT_0072 within subclass 016 CA1-ProS Glut, so the mapping
    is one classical type to many atlas supertypes (broad, 1:n).
  reconciliation_note: >
    Paired with the best-child cluster edge to CS20230722_CLUS_0262
    (closeMatch, 1:1) - CLUS_0262 leads SUPT_0069 children on combined
    region + annotation transfer + Wfs1 cohort percentile; see report.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical CA1 pyramidal cell spans at least four WMBv1 supertypes
        (CS20230722_SUPT_0069 through CS20230722_SUPT_0072) within subclass
        016 CA1-ProS Glut; SUPT_0069 is the primary correspondence by
        annotation-transfer coverage and Wfs1 cohort percentile (0.83), but
        a complete mapping requires sibling edges to SUPT_0070, SUPT_0071,
        and SUPT_0072.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        CA1-ProS source coverage distributes across multiple SUPT_0069 child
        clusters (CLUS_0261, CLUS_0262, CLUS_0263, CLUS_0266) and across
        sibling supertypes; cluster-level F1 falls to 0.44 on the leading
        child (CS20230722_CLUS_0262).
  proposed_experiments:
    - >
      Annotation transfer of a sublayer-resolved CA1 pyramidal source dataset
      (Cembrowski 2016 or Zeisel 2018 deep vs. superficial CA1 PC labels) onto
      WMBv1 CCN20230722, with per-supertype coverage breakdown across
      CS20230722_SUPT_0069 through CS20230722_SUPT_0072; target F1 >= 0.80 at
      the supertype level for the leading sublayer.
  unresolved_questions:
    - Which of CS20230722_SUPT_0069 through CS20230722_SUPT_0072 corresponds
      to deep vs. superficial CA1 pyramidal cell sublayers?
    - Which of the SUPT_0069 child clusters (CS20230722_CLUS_0261,
      CS20230722_CLUS_0262, CS20230722_CLUS_0263, CS20230722_CLUS_0266)
      captures the deep-CA1, superficial-CA1, and proximo-distal axes?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0262 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0262 is the leading child cluster within
    CS20230722_SUPT_0069 on joint criteria: region_fraction_100um 0.975
    against MBA:407, Wfs1 mean 7.68 (cohort percentile 0.98), and the
    highest coverage among SUPT_0069 children in the Yao 2021 CA1-ProS
    annotation transfer (run_ref
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1; F1=0.44 cluster-level,
    purity 1.00, coverage 0.28). 1 of 1 markers CONSISTENT.
  reconciliation_note: >
    Paired with the parent supertype edge to CS20230722_SUPT_0069
    (broadMatch, 1:n); CLUS_0262 is the best-child within SUPT_0069 but the
    cluster-level F1 of 0.44 reflects distribution of CA1-ProS source cells
    across multiple SUPT_0069 children - the supertype level is the
    cleaner anchor.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Yao 2021 CA1-ProS source cells distribute across CS20230722_CLUS_0262
        and sibling clusters within SUPT_0069 (cluster-level F1=0.44, coverage
        0.28); CS20230722_CLUS_0263 carries even higher Wfs1 (mean 7.75,
        cohort percentile 0.99), and the cluster wins by region cell count
        plus marginal annotation-transfer advantage rather than by an
        unambiguous marker signature.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Cluster-level annotation-transfer F1 (0.44) is well below
        supertype-level F1 (0.79 on CS20230722_SUPT_0069); the cleanest
        mapping resolution for the classical CA1 pyramidal cell is the
        supertype, with the cluster-level call held provisionally pending
        sublayer-resolved annotation transfer.
  proposed_experiments:
    - >
      Sublayer-resolved annotation transfer (Cembrowski 2016 deep vs.
      superficial CA1 PC labels) onto WMBv1 CCN20230722; target F1 >= 0.70
      at cluster level for the leading sublayer within CS20230722_SUPT_0069.
  unresolved_questions:
    - Does CS20230722_CLUS_0262 correspond to deep-layer CA1, superficial-layer
      CA1, or a proximo-distal subpopulation?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0263 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.4
  rationale: >
    [tier:WEAKEST] Sibling cluster within CS20230722_SUPT_0069 (Wfs1 mean
    7.75, cohort percentile 0.99; region_fraction_100um 0.973 against
    MBA:407). Supports the broader CA1 pyramidal cell to SUPT_0069 mapping
    but trails CS20230722_CLUS_0262 on annotation-transfer coverage and
    in-region cell count. Held as a supporting sibling, not the primary
    cluster-level call.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Wfs1 expression on CS20230722_CLUS_0263 (7.75) is marginally above
        CS20230722_CLUS_0262 (7.68), but CLUS_0263 carries fewer cells in
        MBA:407 (5398 vs. 19403); both clusters absorb CA1-ProS source
        coverage within SUPT_0069.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0293 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0293 sits predominantly in prosubiculum
    (region_fraction_100um 0.500; strict region_fraction 0.110 against
    MBA:407 Field CA1 pyramidal layer); only half of its cells fall within
    100 microns of the CA1 pyramidal layer. Wfs1 expression is high
    (mean 6.75, cohort percentile 0.95) but the location is off-target for
    a classical CA1 pyramidal cell.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Predominantly prosubicular cluster; only 110 of 1000 cells fall
        strictly within MBA:407 (Field CA1, pyramidal layer).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0261 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0261 is a small sibling within
    CS20230722_SUPT_0069 (215 cells) with soma painting predominantly in
    CA1 stratum oriens, not the pyramidal layer
    (region_fraction_100um 0.707, strict region_fraction 0.178 against
    MBA:407). Wfs1 expression is modest (mean 4.29, cohort percentile
    0.79). Likely represents a stratum-oriens subpopulation rather than a
    classical CA1 pyramidal cell.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma painting in Field CA1 stratum oriens (MBA:399) rather
        than Field CA1 pyramidal layer (MBA:407).
    - caveat_type: LOW_CELL_COUNT
      description: >
        Only 215 cells in this cluster - at the threshold for robust
        cluster-level analysis.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0266 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0266 carries low Wfs1 (mean 2.69, cohort
    percentile 0.53 - at the cohort median, not elevated) and soma
    painting predominantly in CA1 stratum oriens
    (region_fraction_100um 0.584; strict region_fraction 0.032 against
    MBA:407). Does not match the classical CA1 pyramidal cell signature.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma painting in Field CA1 stratum oriens (MBA:399);
        only 32 of 1000 cells fall strictly within MBA:407.
    - caveat_type: LOW_CELL_COUNT
      description: >
        Only 130 cells in this cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0069 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.3
  rationale: >
    [tier:CUT] Duplicate edge ID targeting CS20230722_SUPT_0069 - the
    curator-built edge (edge_ca1_pc_hippocampus_to_supt_0069) carries
    substantive annotation-transfer evidence and a populated property-
    comparison set against the same accession; this fresh-emit edge
    carries only a Stage A discovery_score and a stub property
    comparison. Held as a duplicate pending curator removal.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Duplicate edge on the same taxonomy_type accession
        (CS20230722_SUPT_0069) as edge_ca1_pc_hippocampus_to_supt_0069;
        the curator-built edge is the authoritative mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0074 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0074 sits predominantly in prosubiculum
    (region_fraction_100um 0.409; strict region_fraction 0.090 against
    MBA:407); Wfs1 is high (mean 6.79, cohort percentile 0.97) but the
    cells are not in the CA1 pyramidal layer. Represents a CA1-ProS Glut
    sibling supertype anchored on the prosubicular side rather than the
    classical CA1 PC population.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma location in Prosubiculum (MBA:484682470) rather than
        Field CA1 pyramidal layer (MBA:407).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0073 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:WEAKEST] CS20230722_SUPT_0073 is a CA1-ProS Glut sibling
    supertype with predominant soma painting in CA1 stratum oriens
    (region_fraction_100um 0.545; strict region_fraction 0.102 against
    MBA:407) and low Wfs1 (mean 2.41, cohort percentile 0.52). Supports
    the broader classical CA1 PC to subclass 016 CA1-ProS Glut mapping
    only at the subclass level; not a primary supertype-level call.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma location in Field CA1 stratum oriens (MBA:399), not
        the pyramidal layer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0072 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.4
  rationale: >
    [tier:WEAKEST] CS20230722_SUPT_0072 is a CA1-ProS Glut sibling
    supertype with strong region alignment (region_fraction_100um 0.877;
    strict region_fraction 0.299 against MBA:407) and elevated Wfs1
    (mean 4.78, cohort percentile 0.90). Supports the broader CA1
    pyramidal cell to subclass 016 CA1-ProS Glut mapping (1:n) but is
    not the primary supertype-level call (SUPT_0069 leads on
    annotation-transfer coverage).
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Sibling CA1-ProS Glut supertype that absorbs a fraction of the
        CA1-ProS annotation-transfer coverage not captured by
        CS20230722_SUPT_0069.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0070 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:WEAKEST] CS20230722_SUPT_0070 is a CA1-ProS Glut sibling
    supertype with predominant soma in CA1 stratum oriens
    (region_fraction_100um 0.684; strict region_fraction 0.186 against
    MBA:407) and modest Wfs1 (mean 3.84, cohort percentile 0.79).
    Absorbs roughly a fifth of CA1-ProS annotation-transfer coverage in
    the Yao 2021 run (run_ref at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1);
    supports the broader 1:n mapping at subclass level.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma location in Field CA1 stratum oriens (MBA:399)
        rather than the pyramidal layer; likely a stratum-oriens-leaning
        CA1-ProS Glut population.
```
<!-- verdict-block-end -->
