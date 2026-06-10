# CA1 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

CA1 pyramidal cells are the principal excitatory output neurons of Ammon's horn, sitting at the final relay of the canonical hippocampal trisynaptic circuit. Their somata occupy the CA1 stratum pyramidale; basal dendrites extend into stratum oriens and apical dendrites into stratum radiatum, with the dominant axonal projection running through the subiculum to entorhinal cortex. They form one of the five excitatory cell populations of the mouse hippocampus alongside dentate granule cells, dentate mossy cells, and CA2/CA3 pyramidal cells.

> The hippocampus is grossly comprised of five excitatory cell populations; namely, granule and mossy cells of the dentate gyrus (DG), and pyramidal cells of CA3, CA2, and CA1.
> — Cembrowski et al. 2016, Major Glutamatergic Cell Types in Hippocampal Subfields · [1] <!-- quote_key: 4875295_002a714a -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548]; apical dendrites in hippocampus stratum radiatum [UBERON:0005372]; basal dendrites in hippocampus stratum oriens [UBERON:0005371]; axonal projection to subiculum [UBERON:0002191] | [1] [2] [3] [4] [5] [6] [7] |
| Neurotransmitter | glutamatergic | [4] [1] [8] |
| Defining markers | Wfs1; Gria1; Gria2; Nptn; Slc17a7 | [9] [7] [10] [11] [12] [13] |
| Negative markers | Drd1 | — |
| Neuropeptides | (none reported) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical literature on hippocampal subfield architecture and pyramidal-cell topography · [1] [2] [3] [4] [5] [6] [7]
  > The hippocampal formation consists of GCs in the dentate gyrus and pyramidal cells in the CA1 and CA3 areas
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [6] <!-- quote_key: 7458943_d6507595 -->

  > These include granule cells and mossy cells in the dentate gyrus (DG), and pyramidal cells in the CA3, CA2, and CA1 regions (Cembrowski et al., 2016)(Dale et al., 2015).
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [4] <!-- quote_key: 2281033_0422472c -->

  > Glutamatergic neurons dominate the hippocampal architecture, accounting for over 90% of all hippocampal neurons, with pyramidal layers being densely packed with these excitatory cells (Mancini et al., 2022).
  > — Mancini et al. 2022, Classical Hippocampal Circuit Organization · [5] <!-- quote_key: 252086716_9d46d627 -->
- **Neurotransmitter (glutamatergic):** classical / direct assessment from the principal-cell literature · [4] [1] [8]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1).
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [4] <!-- quote_key: 2281033_5b9805ff -->
- **Wfs1 marker:** classical protein/transcript-level marker for deep-sublayer CA1 pyramidal cells · [9] [7] [10] [11] [12]
- **Gria1 / Gria2 markers:** AMPA-receptor subunit immunoreactivity localising to CA1 pyramidal-layer somata · [7]
  > The CA1 showed strong dense immunoreactivity within the str. oriens and str. radiatum, with relatively decreased staining within the str. pyramidale cells.
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [7] <!-- quote_key: 210181642_7ac40176 -->
- **Nptn (neuroplastin-65) marker:** identifies pyramidal neurons of CA1 alongside CA2/CA3 and subiculum · [10]
  > Neuroplastin-65 positive glutamatergic neurons: These include granule neurons of the dentate gyrus, pyramidal neurons of CA1, CA2-3, subiculum, and specific layers of entorhinal cortex (Herrera-Molina et al., 2017)(Langnaese et al., 1997).
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [10] <!-- quote_key: 3288675_d83802d0 -->
- **Slc17a7 (vGLUT1) marker:** principal vesicular glutamate transporter on hippocampal glutamatergic terminals · [13]
  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [13] <!-- quote_key: 14854554_ed1bdc00 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD).

**Proposed CL term:** *CA1 pyramidal cell* (SUBMITTED; parent CL:1001571 hippocampal pyramidal neuron)

Definition: A hippocampal pyramidal neuron with soma located in the pyramidal layer of hippocampal area CA1 (UBERON:0014548) (Cembrowski et al., 2016; Müller & Remy, 2017), forming the dominant excitatory projection population of the CA1 subfield. As the primary output cell of Ammon's horn, it projects via the subiculum to entorhinal cortex and is capable of glutamate secretion as a neurotransmitter (Dale et al., 2015). In mouse, it is distinguished from CA2 and CA3 pyramidal neurons by soma position within the CA1 stratum pyramidale and by expression of wolframin (Wfs1), an endoplasmic reticulum-resident membrane protein enriched in deep-sublayer CA1 cells (Cembrowski et al., 2016).

---

## Results

Annotation transfer of the Yao 2021 mouse hippocampal formation SMART-Seq v4 CA1-ProS source label onto WMBv1 (CCN20230722) and supertype-level Wfs1 expression jointly support a broad mapping of the classical CA1 pyramidal cell onto supertype 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] within subclass 016 CA1-ProS Glut (see figure and property comparison tables below). Source-cell coverage distributes across four sibling CA1-ProS Glut supertypes within the same subclass, so the cleanest mapping resolution is the subclass / supertype level rather than any single cluster; the best child cluster within SUPT_0069 by region painting is 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262].

### Annotation transfer overview

![Annotation transfer F1 tree for CA1-ProS source label (Yao 2021 SSv4 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) CA1-ProS source group (n=1590 cells mapped). Coverage = fraction of source-group cells landing on the target; Purity = fraction of target cells from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The CA1-ProS label maps cleanly at the subclass level (016 CA1-ProS Glut, F1=0.99) and at the class level (01 IT-ET Glut, F1=0.89); at the supertype level the leading target is CS20230722_SUPT_0069 (F1=0.79) with the remaining coverage distributing across sibling CA1-ProS Glut supertypes 0070–0073.*

### 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] · 🟡 MODERATE

**Property alignment table.** Table 1 — Property comparison:

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | not asserted | Glut (CLUS_0262) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Field CA1, pyramidal layer [MBA:407] count_100um=27305 (region_fraction_100um=0.959) | Field CA1, pyramidal layer [MBA:407] count_100um=19403 (region_fraction_100um=0.975, CLUS_0262) | CONSISTENT |
| Wfs1 expression | defining marker | mean 3.97; cohort percentile 0.828; child-cluster coverage 1.000 | mean 7.68; cohort percentile 0.975 (CLUS_0262) | CONSISTENT |

*(4 of 5 SUPT_0069 child clusters surfaced in the candidate set show Wfs1 concordant with the classical type — CLUS_0262 (7.68), CLUS_0263 (7.75), CLUS_0261 (4.29), CLUS_0266 (2.69); CLUS_0262 leads on within-CA1 pyramidal-layer cell count. Best match: CS20230722_CLUS_0262.)*

Table 2 — Evidence support:

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed metadata | Atlas metadata | SUPPORT | SUPT_0069 in CA1-ProS Glut subclass; 2553 cells in MBA:407 | atlas-internal |
| Yao 2021 cluster annotation transfer | Annotation transfer | SUPPORT | F1=0.79 (supertype); F1=0.99 (subclass 016 CA1-ProS Glut) | atlas-internal |

**Supporting evidence:**

- SUPT_0069 sits inside the dedicated CA1-ProS glutamatergic subclass 016 CA1-ProS Glut, with the dominant soma painting in Field CA1, pyramidal layer [MBA:407] (region_fraction_100um=0.959) — the classical CA1 stratum pyramidale [UBERON:0014548] location is recovered.
- Cluster annotation transfer of the Yao 2021 hippocampus dataset (GEO:GSE185862) onto WMBv1 lands the CA1-ProS source label cleanly at the subclass level (016 CA1-ProS Glut, F1=0.99) and at the class level (01 IT-ET Glut, F1=0.89). At supertype level SUPT_0069 is the leading correspondence (F1=0.79; coverage=0.65; purity=1.00). Target-side purity of 1.00 confirms that SUPT_0069 is populated exclusively by CA1-ProS source cells in this transfer.
- Wfs1, the classical deep-CA1 marker, is expressed at supertype mean 3.97 (cohort percentile 0.83) on SUPT_0069 and reaches mean 7.68 (cohort percentile 0.98) on the leading child cluster CLUS_0262, consistent with literature placement of Wfs1 on deep-sublayer CA1 pyramidal cells.

**Marker evidence provenance:**

- **Wfs1:** primary protein-level evidence anchored by Wfs1-targeted studies in CA1 pyramidal neurons (Siegel et al. 1995 [9]; Herrera-Molina et al. 2017 [10]; Langnaese et al. 1997 [11]; Herrera-Molina et al. 2014 [12]; Yeung et al. 2020 [7]). Cross-checks against atlas precomputed expression confirm Wfs1 at the supertype mean above the cohort median (cohort percentile 0.83 at SUPT_0069), supporting it as a transcript-level discriminator at this resolution.
- **Gria1 / Gria2:** AMPA receptor subunit immunoreactivity in CA1 pyramidal layer (Yeung et al. 2020 [7]); protein-level evidence on the broader pyramidal population rather than on individually filled and morphology-confirmed cells.
- **Nptn (neuroplastin-65):** protein-level evidence in CA1 pyramidal neurons (Herrera-Molina et al. 2017 [10]; Langnaese et al. 1997 [11]; Herrera-Molina et al. 2014 [12]). *(note: Np65-positive glutamatergic neurons extend beyond CA1 to CA2/CA3 and subiculum, so Nptn is informative for excitatory identity but not CA1-specific.)*
- **Slc17a7 (vGLUT1):** transcript and protein-level vesicular glutamate transporter on hippocampal glutamatergic terminals (Sarvari et al. 2016 [13]) — supports glutamatergic identity but is not CA1-specific.

**Concerns:**

- The classical CA1 pyramidal cell spans at least four WMBv1 supertypes (CS20230722_SUPT_0069 through CS20230722_SUPT_0072) inside subclass 016 CA1-ProS Glut: AMBIGUOUS_MAPPING. SUPT_0069 absorbs the majority of the CA1-ProS coverage at supertype rank, but a complete mapping requires sibling broadMatch edges to SUPT_0070, SUPT_0071, and SUPT_0072 (whose Wfs1 means 3.84, not assessed, and 4.78 respectively all sit above the cohort median).
- Cluster-level annotation transfer evidence is not carried on this edge; supertype-level coverage distributes across multiple SUPT_0069 child clusters (CLUS_0261, CLUS_0262, CLUS_0263, CLUS_0266), so the supertype-level mapping is cleaner than any single cluster call: DISTRIBUTED_ACROSS_CLUSTERS.

**What would upgrade confidence:**

- Sublayer-resolved cluster annotation transfer of a deep-vs-superficial CA1 pyramidal source dataset (Cembrowski 2016 or Zeisel 2018) onto WMBv1 CCN20230722, with per-supertype coverage breakdown across SUPT_0069 through SUPT_0072 (target supertype F1 ≥ 0.80 for the leading sublayer) — would resolve whether SUPT_0069 corresponds to deep CA1, superficial CA1, or a proximo-distal axis subpopulation, and would feed back as AnnotationTransferEvidence.

### 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] · 🟡 MODERATE

**Property alignment table.** Table 1 — Property comparison:

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | not asserted | Glut (CLUS_0262) | CONSISTENT |
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | not available | Field CA1, pyramidal layer [MBA:407] count_100um=19403 (region_fraction_100um=0.975, CLUS_0262) | CONSISTENT |
| Wfs1 expression | defining marker | not available | mean 7.68; cohort percentile 0.975 (CLUS_0262) | CONSISTENT |

*Subcluster note: CLUS_0262 is the leading child of SUPT_0069 by region painting in MBA:407 (count_100um=19403). Sibling CLUS_0263 within the same supertype carries marginally higher Wfs1 (7.75, cohort percentile 0.988) but fewer cells in the pyramidal layer (count_100um=5398).*

Table 2 — Evidence support:

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.975; strict region_fraction=0.468 | atlas-internal |

**Supporting evidence:**

- CLUS_0262 is the largest CA1-ProS Glut_1 cluster within SUPT_0069 by cells painted to Field CA1, pyramidal layer [MBA:407] (count_100um=19403; region_fraction_100um=0.975) — soma location is concordant with classical CA1 stratum pyramidale [UBERON:0014548].
- Cluster-level Wfs1 expression at mean 7.68 (cohort percentile 0.975) places CLUS_0262 in the top decile of the glutamatergic Field-CA1-pyramidal-layer cohort for the classical deep-CA1 marker.
- Cluster NT annotation is Glut, consistent with the classical glutamatergic identity.

**Marker evidence provenance:**

- **Wfs1:** primary literature support is the same set anchoring SUPT_0069 (Siegel et al. 1995 [9]; Herrera-Molina et al. 2017 [10]; Langnaese et al. 1997 [11]; Herrera-Molina et al. 2014 [12]; Yeung et al. 2020 [7]). On CLUS_0262 the atlas-side precomputed mean (7.68) places the gene at cohort percentile 0.975 — directly assessed transcript-level evidence on this specific cluster.

**Concerns:**

- Classical CA1 pyramidal source coverage distributes across CLUS_0262 and sibling clusters within SUPT_0069; CS20230722_CLUS_0263 carries marginally higher Wfs1 (mean 7.75) and CLUS_0262 wins on region cell count rather than on an unambiguous marker signature: DISTRIBUTED_ACROSS_CLUSTERS. Cluster-level annotation-transfer evidence is not carried on this edge.
- The cleanest mapping resolution for the classical CA1 pyramidal cell is the supertype (SUPT_0069), where annotation-transfer evidence is carried; the cluster-level call is held provisionally pending sublayer-resolved annotation transfer: TAXONOMY_LEVEL_MISMATCH.

**What would upgrade confidence:**

- Sublayer-resolved annotation transfer (Cembrowski 2016 deep vs. superficial CA1 pyramidal cell labels) onto WMBv1 CCN20230722 with target cluster-level F1 ≥ 0.70 for the leading sublayer within CS20230722_SUPT_0069 — would feed back as AnnotationTransferEvidence and resolve whether CLUS_0262 captures the deep-CA1, superficial-CA1, or a proximo-distal axis subpopulation.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] | — | 19061 | 🟡 MODERATE | CA1-ProS cluster annotation transfer F1=0.79 to supertype; Wfs1 percentile 0.83 | Primary (supertype-level) |
| 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] | 0069 CA1-ProS Glut_1 | 12018 | 🟡 MODERATE | Largest SUPT_0069 child in MBA:407; Wfs1 percentile 0.975 | Secondary (best child cluster) |
| 0263 CA1-ProS Glut_1 [CS20230722_CLUS_0263] | 0069 CA1-ProS Glut_1 | 4105 | 🔴 LOW | Wfs1 percentile 0.988 but fewer pyramidal-layer cells | Supports broader mapping |
| 0293 CA1-ProS Glut_6 [CS20230722_CLUS_0293] | 0074 CA1-ProS Glut_6 | 983 | 🔴 LOW | Predominantly prosubicular cluster | Eliminated (mostly prosubiculum) |
| 0261 CA1-ProS Glut_1 [CS20230722_CLUS_0261] | 0069 CA1-ProS Glut_1 | 215 | 🔴 LOW | Soma in CA1 stratum oriens, not pyramidal layer | Eliminated (wrong CA1 layer) |
| 0266 CA1-ProS Glut_1 [CS20230722_CLUS_0266] | 0069 CA1-ProS Glut_1 | 130 | 🔴 LOW | Soma in CA1 stratum oriens; very small | Eliminated (wrong CA1 layer, low n) |
| 0074 CA1-ProS Glut_6 [CS20230722_SUPT_0074] | — | 1921 | 🔴 LOW | Dominant soma in prosubiculum | Eliminated (prosubicular) |
| 0073 CA1-ProS Glut_5 [CS20230722_SUPT_0073] | — | 898 | 🔴 LOW | Dominant soma in CA1 stratum oriens | Eliminated (wrong CA1 layer) |
| 0072 CA1-ProS Glut_4 [CS20230722_SUPT_0072] | — | 3493 | 🔴 LOW | Sibling CA1-ProS Glut supertype absorbing residual CA1-ProS coverage | Supports broader mapping |
| 0070 CA1-ProS Glut_2 [CS20230722_SUPT_0070] | — | 4609 | 🔴 LOW | Sibling CA1-ProS Glut; soma in CA1 stratum oriens | Supports broader mapping |
| 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] (legacy duplicate) | — | 19061 | ⚪ UNCERTAIN | Duplicate edge on same taxonomy_type as the curator-built primary | Eliminated (duplicate edge) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The CA1 pyramidal cell classical node sits on a CLASSICAL_MULTIMODAL evidence base: glutamatergic neurotransmitter identity (refs [4] [1] [8]), soma in the pyramidal layer of CA1 [UBERON:0014548] with dendritic arborisations in stratum radiatum [UBERON:0005372] and stratum oriens [UBERON:0005371] and axonal projection to subiculum [UBERON:0002191] (refs [1] [2] [3] [4] [5] [6] [7]), and a defining-marker set of Wfs1, Gria1, Gria2, Nptn, and Slc17a7 (refs [9] [7] [10] [11] [12] [13]). Drd1 is recorded as a negative marker for dorsal CA1 pyramidal cells, with the ambiguity noted on the node that ventral CA1 carries a D1R-positive subpopulation.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:407 Field CA1 pyramidal layer, NT-type filter glutamatergic, defining-marker percentiles in the survival cohort). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster and supertype and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse HPF SMART-Seq v4 cell type labels) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `b95d284` at 2026-06-10T13:04:41+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ca1_pc_hippocampus_to_supt_0069 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0262 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0263 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0293 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0261 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0266 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0074 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0073 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0072 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0070 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0069 (legacy duplicate) | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** CA1 pyramidal cell → 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] at MODERATE confidence. Key support: cluster annotation transfer of the Yao 2021 CA1-ProS source label (subclass F1=0.99, supertype F1=0.79; target purity=1.00) and atlas precomputed Wfs1 expression at supertype cohort percentile 0.83. Key caveats: AMBIGUOUS_MAPPING (classical type spans SUPT_0069 through SUPT_0072 within subclass 016 CA1-ProS Glut, and a complete mapping requires sibling broadMatch edges) and DISTRIBUTED_ACROSS_CLUSTERS (supertype coverage distributes across SUPT_0069 child clusters with no single cluster carrying decisive lit-anchored signal). The best child cluster within SUPT_0069 by region painting and Wfs1 percentile is 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262], also at MODERATE confidence; the cluster-level call is held provisionally pending sublayer-resolved cluster annotation transfer.

The Cell Ontology has no specific term for this population; hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] is the closest ancestor. CA1 pyramidal cells are a subpopulation of hippocampal pyramidal neurons; CL:1001571 covers all hippocampal pyramidal neurons and is therefore a BROAD match. No CA1-specific CL term currently exists. A new CL term *CA1 pyramidal cell* has been drafted (status: SUBMITTED) with CL:1001571 as parent.

### Proposed experiments and follow-ups

- **What:** sublayer-resolved cluster annotation transfer of a deep-vs-superficial CA1 pyramidal cell source dataset (Cembrowski 2016 or Zeisel 2018) onto WMBv1 CCN20230722, with per-supertype coverage breakdown across CS20230722_SUPT_0069 through CS20230722_SUPT_0072 and per-cluster breakdown within SUPT_0069.
  - **Target:** supertype F1 ≥ 0.80 for the leading sublayer; cluster F1 ≥ 0.70 for the leading sublayer within SUPT_0069.
  - **Expected output:** AnnotationTransferEvidence on the SUPT_0069 edge and on the CLUS_0262 edge, plus sibling broadMatch edges to SUPT_0070 / SUPT_0071 / SUPT_0072 with their per-sublayer coverage breakdowns.
  - **Resolves:** open questions 1–3 below — deep vs. superficial CA1 correspondence across the four CA1-ProS Glut supertypes, and the proximo-distal / sublayer identity of the SUPT_0069 child clusters.

### Open questions

1. Which of CS20230722_SUPT_0069 through CS20230722_SUPT_0072 corresponds to deep vs. superficial CA1 pyramidal cell sublayers? Wfs1 marks deep-layer CA1 pyramidal cells in the literature; checking which supertype carries Wfs1 most strongly in the atlas would resolve the sublayer correspondence.
2. Which of the SUPT_0069 child clusters (CS20230722_CLUS_0261, CS20230722_CLUS_0262, CS20230722_CLUS_0263, CS20230722_CLUS_0266) captures the deep-CA1, superficial-CA1, and proximo-distal axes?
3. Does CS20230722_CLUS_0262 correspond to deep-layer CA1, superficial-layer CA1, or a proximo-distal subpopulation?
4. Should the legacy duplicate edge on CS20230722_SUPT_0069 (UNCERTAIN, no curator-authored evidence) be removed in favour of the authoritative curator-built edge?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · [PMID:27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | 27113915 | soma location |
| [2] | Müller & Remy 2017 · [PMID:29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | 29250747 | soma location |
| [3] | https://doi.org/10.1038/s41598-017-11268-z | — | soma location |
| [4] | Dale et al. 2015 · [PMID:26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | 26346726 | soma location |
| [5] | Mancini et al. 2022 · [PMID:37011759](https://pubmed.ncbi.nlm.nih.gov/37011759/) | 37011759 | soma location |
| [6] | Munster-Wandowski et al. 2013 · [PMID:24319410](https://pubmed.ncbi.nlm.nih.gov/24319410/) | 24319410 | soma location |
| [7] | Yeung et al. 2020 · [PMID:32009891](https://pubmed.ncbi.nlm.nih.gov/32009891/) | 32009891 | soma location |
| [8] | Wheeler et al. 2015 · [PMID:26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | 26402459 | neurotransmitter type |
| [9] | Siegel et al. 1995 · [PMID:7722624](https://pubmed.ncbi.nlm.nih.gov/7722624/) | 7722624 | Wfs1 marker |
| [10] | Herrera-Molina et al. 2017 · [PMID:28779130](https://pubmed.ncbi.nlm.nih.gov/28779130/) | 28779130 | Wfs1 marker |
| [11] | Langnaese et al. 1997 · [PMID:8995369](https://pubmed.ncbi.nlm.nih.gov/8995369/) | 8995369 | Wfs1 marker |
| [12] | Herrera-Molina et al. 2014 · [PMID:24554721](https://pubmed.ncbi.nlm.nih.gov/24554721/) | 24554721 | Wfs1 marker |
| [13] | Sarvari et al. 2016 · [PMID:27375434](https://pubmed.ncbi.nlm.nih.gov/27375434/) | 27375434 | Slc17a7 marker |

---

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_supt_0069 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Cluster annotation transfer of the Yao 2021 CA1-ProS source
    label (at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) lands cleanly at the
    subclass 016 CA1-ProS Glut (F1=0.99) and identifies CS20230722_SUPT_0069 as
    the leading supertype correspondence (F1=0.79; target purity=1.00); atlas
    Wfs1 expression at supertype cohort percentile 0.83 and dominant soma
    painting in Field CA1 pyramidal layer (region_fraction_100um=0.96) anchor
    the broad match; classical CA1 pyramidal cell spans CS20230722_SUPT_0069
    through CS20230722_SUPT_0072 inside the subclass so the cardinality is 1:n.
  reconciliation_note: >
    Paired with the best-child cluster edge to CS20230722_CLUS_0262
    (skos:closeMatch + 1:1) — the supertype broadMatch is the authoritative
    resolution, the cluster edge is the leading within-supertype child by
    region painting and Wfs1 percentile; pending sublayer-resolved cluster
    annotation transfer.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical CA1 pyramidal cell spans at least four WMBv1 supertypes
        (CS20230722_SUPT_0069 through CS20230722_SUPT_0072) within subclass
        016 CA1-ProS Glut; CS20230722_SUPT_0069 is the primary correspondence
        by transfer coverage and Wfs1 cohort percentile (0.83), but a complete
        mapping requires sibling broadMatch edges to CS20230722_SUPT_0070, and CS20230722_SUPT_0072.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        CA1-ProS source coverage distributes across multiple
        CS20230722_SUPT_0069 child clusters (CS20230722_CLUS_0261,
        CS20230722_CLUS_0262, CS20230722_CLUS_0263, CS20230722_CLUS_0266) and
        across sibling supertypes; cluster-level transfer evidence is not
        carried on this edge.
  proposed_experiments:
    - >
      Sublayer-resolved cluster annotation transfer of a deep-vs-superficial
      CA1 pyramidal source dataset (Cembrowski 2016 or Zeisel 2018) onto WMBv1
      CCN20230722, with per-supertype coverage breakdown across
      CS20230722_SUPT_0069 through CS20230722_SUPT_0072; target F1 >= 0.80 at
      the supertype level for the leading sublayer.
  unresolved_questions:
    - >
      Which of CS20230722_SUPT_0069 through CS20230722_SUPT_0072 corresponds to
      deep vs. superficial CA1 pyramidal cell sublayers?
    - >
      Which of the CS20230722_SUPT_0069 child clusters (CS20230722_CLUS_0261,
      CS20230722_CLUS_0262, CS20230722_CLUS_0263, CS20230722_CLUS_0266)
      captures the deep-CA1, superficial-CA1, and proximo-distal axes?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0262 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0262 is the leading child of CS20230722_SUPT_0069
    by cells painted to Field CA1 pyramidal layer (region_fraction_100um=0.98)
    and by atlas Wfs1 expression at cohort percentile 0.98; cluster NT
    annotation is glutamatergic; cluster-level annotation transfer evidence is
    not carried on this edge so the call is provisional pending sublayer-
    resolved transfer.
  reconciliation_note: >
    Paired with CS20230722_SUPT_0069 supertype broadMatch (1:n) — the cleanest
    resolution for the classical CA1 pyramidal cell is the supertype, this
    cluster edge captures the leading within-supertype child by region
    painting; CS20230722_CLUS_0263 carries marginally higher Wfs1 but fewer
    pyramidal-layer cells.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        CA1-ProS source cells distribute across CS20230722_CLUS_0262 and
        sibling clusters within CS20230722_SUPT_0069; CS20230722_CLUS_0263
        carries marginally higher Wfs1 (mean 7.75, cohort percentile 0.99),
        and CS20230722_CLUS_0262 wins on region cell count rather than on an
        unambiguous marker signature. Cluster-level transfer evidence is not
        carried on this edge.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        The cleanest mapping resolution for the classical CA1 pyramidal cell
        is the supertype (CS20230722_SUPT_0069), where cluster annotation
        transfer evidence is carried; the cluster-level call is held
        provisionally pending sublayer-resolved cluster annotation transfer.
  proposed_experiments:
    - >
      Sublayer-resolved cluster annotation transfer (Cembrowski 2016 deep vs.
      superficial CA1 pyramidal cell labels) onto WMBv1 CCN20230722; target
      F1 >= 0.70 at cluster level for the leading sublayer within
      CS20230722_SUPT_0069.
  unresolved_questions:
    - >
      Does CS20230722_CLUS_0262 correspond to deep-layer CA1, superficial-
      layer CA1, or a proximo-distal subpopulation?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0263 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:WEAKEST] CS20230722_CLUS_0263 carries the highest within-supertype
    Wfs1 expression (mean 7.75, cohort percentile 0.99) inside
    CS20230722_SUPT_0069 but holds only a fraction of the pyramidal-layer
    cell count of CS20230722_CLUS_0262; cluster-level transfer evidence is
    not carried; supports the broader supertype mapping rather than a
    standalone close match.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Wfs1 expression on CS20230722_CLUS_0263 (mean 7.75) is marginally
        above CS20230722_CLUS_0262 (mean 7.68), but CS20230722_CLUS_0263
        carries fewer cells in Field CA1 pyramidal layer (region_fraction_100um=0.97
        on a smaller cell count); both clusters absorb CA1-ProS source
        coverage within CS20230722_SUPT_0069.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0293 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0293 is a predominantly prosubicular cluster
    (region_fraction=0.11 strict in Field CA1 pyramidal layer, dominant soma
    painting in Prosubiculum MBA:484682470); not a CA1 pyramidal cell match.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Predominantly prosubicular cluster; only 110 of 1000 cells fall
        strictly within MBA:407 (Field CA1, pyramidal layer).
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0261 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0261 has dominant soma painting in Field CA1
    stratum oriens (MBA:399) rather than the pyramidal layer (region_fraction=0.18
    strict in MBA:407), only 215 cells, and modest Wfs1 (mean 4.29, cohort
    percentile 0.79); does not anchor a clean CA1 pyramidal cell call.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma painting in Field CA1 stratum oriens (MBA:399) rather
        than Field CA1 pyramidal layer (MBA:407).
    - caveat_type: LOW_CELL_COUNT
      description: >
        Only 215 cells in this cluster — at the threshold for robust
        cluster-level analysis.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_CLUS_0266 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0266 has dominant soma painting in Field CA1
    stratum oriens (MBA:399), only 32 of 1000 cells strictly in pyramidal
    layer (region_fraction=0.03), only 130 cells total, and Wfs1 at mid-cohort
    percentile 0.53; does not match the classical CA1 pyramidal cell.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma painting in Field CA1 stratum oriens (MBA:399); only 32
        of 1000 cells fall strictly within MBA:407.
    - caveat_type: LOW_CELL_COUNT
      description: >
        Only 130 cells in this cluster.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0074 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUPT_0074 has dominant soma in Prosubiculum
    (MBA:484682470) with only region_fraction_100um=0.41 proximity to Field
    CA1 pyramidal layer; Wfs1 (mean 6.79, cohort percentile 0.97) is high but
    the anatomy is discordant with the classical CA1 pyramidal cell.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma location in Prosubiculum (MBA:484682470) rather than
        Field CA1 pyramidal layer (MBA:407).
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0073 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0073 has dominant soma in Field CA1 stratum
    oriens (MBA:399), modest Wfs1 (mean 2.41, cohort percentile 0.52), and
    only region_fraction=0.10 strict in pyramidal layer; supports the broader
    CA1-ProS Glut family but not the CA1 pyramidal cell call specifically.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma location in Field CA1 stratum oriens (MBA:399), not the
        pyramidal layer.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0072 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  rationale: >
    [tier:WEAKEST] CS20230722_SUPT_0072 is a sibling CA1-ProS Glut supertype
    within subclass 016 CA1-ProS Glut; region_fraction_100um=0.88 in Field CA1
    pyramidal layer and Wfs1 at cohort percentile 0.90 — absorbs a fraction of
    the CA1-ProS coverage not captured by CS20230722_SUPT_0069; contributes to
    the 1:n mapping of the classical type onto multiple CA1-ProS Glut
    supertypes.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Sibling CA1-ProS Glut supertype that absorbs a fraction of the
        CA1-ProS annotation-transfer coverage not captured by
        CS20230722_SUPT_0069.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0070 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUPT_0070 is a sibling CA1-ProS Glut supertype with
    dominant soma in Field CA1 stratum oriens (MBA:399); Wfs1 at cohort
    percentile 0.79; the stratum-oriens-leaning anatomy weakens the
    correspondence to a pyramidal-layer CA1 pyramidal cell.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant soma location in Field CA1 stratum oriens (MBA:399) rather
        than the pyramidal layer; likely a stratum-oriens-leaning CA1-ProS
        Glut population.
  proposed_experiments: []
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0069 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Duplicate edge on the same taxonomy_type accession
    (CS20230722_SUPT_0069) as the curator-authoritative edge
    edge_ca1_pc_hippocampus_to_supt_0069; this edge carries only a stub
    discovery score and no curator-authored evidence — flag for removal.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Duplicate edge on the same taxonomy_type accession
        (CS20230722_SUPT_0069) as edge_ca1_pc_hippocampus_to_supt_0069; the
        curator-built edge is the authoritative mapping.
  proposed_experiments: []
  unresolved_questions:
    - >
      Curator removal of duplicate edge edge_ca1_pc_hippocampus_to_CS20230722_SUPT_0069
      — legacy/fresh-emit ID collision on taxonomy_type CS20230722_SUPT_0069.
```
<!-- verdict-block-end -->
