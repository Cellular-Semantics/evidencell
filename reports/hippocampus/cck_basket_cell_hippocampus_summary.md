# Cholecystokinin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Cholecystokinin (CCK)-positive basket cells are a major class of perisomatic-targeting GABAergic interneurons of the hippocampus, distinguished from parvalbumin (Pvalb)-expressing basket cells by their expression of CCK and the type-1 cannabinoid receptor (Cnr1/CB1R), and by their distinct morphological, biochemical and electrophysiological features [3] [5]. Cnr1+ CCK basket cells form the structural substrate for cannabinoid modulation of hippocampal inhibition, with axon terminals that surround the somata and proximal dendrites of pyramidal neurons [5]. Mapping these cells onto the Whole Mouse Brain v1 atlas requires reconciling a CGE-derived transcriptomic identity (Sncg / Vip subclasses) with a strong marker signature (Cck, Cnr1, Vglut3) and an explicit exclusion of Pvalb.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1] [2] [3] [4] |
| NT type | GABAergic | [3] |
| Defining markers | Cck, Cnr1, Vglut3 | Cck: [5] [2] [4] [6] [7]; Cnr1: [5] |
| Negative markers | Pvalb | [5] |
| Neuropeptides | Cck | [5] |
| CL term | basket cell [CL:0000118] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Defining markers (Cck, Cnr1):** immunohistochemistry + electron microscopy in rat hippocampus · [5]
  > To understand the functional significance and mechanisms of action in the CNS of endogenous and exogenous cannabinoids, it is crucial to identify the neural elements that serve as the structural substrate of these actions. We used a recently developed antibody against the CB1 cannabinoid receptor to study this question in hippocampal networks. Interneurons with features typical of basket cells showed a selective, intense staining for CB1 in all hippocampal subfields and layers. Most of them (85.6%) contained cholecystokinin (CCK), which corresponded to 96.9% of all CCK-positive interneurons, whereas only 4.6% of the parvalbumin (PV)- containing basket cells expressed CB1.
  > — Katona et al. 1999, Classical Functional and Morphological Interneuron Types · [5] <!-- quote_key: 480205_62cd73ae -->
- **Negative marker (Pvalb):** immunohistochemistry · [1]
  > Most CB + 1 terminals surrounding the somata and proximal dendrites of pyramidal neurons were cholecystokinin + (CCK) GABAergic interneurons (basket cells) and, to a lower extent, calbindin D-28k + GABAergic interneurons (Katona et al., 1999) (Marsicano et al., 1999)(Tsou et al., 1999). However, parvalbumin + GABAergic interneuron terminals localized in pyramidal cell layers were negative for CB 1 (Katona et al., 1999)(Marsicano et al., 1999)
  > — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_418c51dd -->
- **Defining marker (Cck) and NT type:** intersectional genetic labelling across forebrain · [3]
  > Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus. As CCK- and PV-GABA neurons differ in an array of morphological, biochemical and electrophysiological features, it has been proposed that they form distinct inhibitory ensembles which differentially contribute to network oscillations and behavior.
  > — Whissell et al. 2015, Classification Schemes and Methodological Approaches · [3] <!-- quote_key: 16859318_009e9f36 -->
- **Defining marker (Cck):** cluster-targeted re-analysis · [7]
  > We focused on cholecystokinin (CCK)-containing(+) GABAergic interneurons because their morphological and molecular features are thought to form a quasi-continuum from axon- to dendrite-targeting interneurons
  > — Fuzik et al. 2015, Results · [7] <!-- quote_key: 7738817_f3d2a066 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD).

---

## Results

Annotation transfer of Harris 2018 CA1 inhibitory-neuron cluster labels onto WMBv1, combined with cluster-level Cck/Cnr1/Vglut3 expression, places the hippocampal CCK basket cell most cleanly at supertype 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] (F1=0.77 to the Harris Cck.Cxcl14.Vip class; see Figure 1 and Table 1). At cluster resolution the strongest expression match is 0681 Sncg Gaba_5 [CS20230722_CLUS_0681], which carries the highest combined Cck / Cnr1 / Vglut3 profile in the hippocampal GABAergic cohort but carries a Pvalb-positive signal that is inconsistent with the classical type and sits under a different supertype than the AT-supported one.

![Filtered AT figure for Cholecystokinin-positive basket cell](figures/f1_for_cck_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the single Harris 2018 source group relevant to the hippocampal CCK basket cell (Cck.Cxcl14.Vip; n=72 source cells). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. With a single pooled source, Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. Scatter at cluster level across multiple 0187 Sncg Gaba_3 children (0672–0677) is consistent with sub-cluster heterogeneity within the CCK-positive Sncg supertype rather than a single best cluster pick.*

The Harris 2018 Cck.Cxcl14.Vip class collapses cleanly onto the Sncg subclass at the supertype level (F1=0.77, Coverage=0.95) and fragments across at least five Sncg Gaba_3 children at the cluster level (top child 0672 Sncg Gaba_3 F1=0.46), indicating that the Harris CCK-expressing CA1 cohort distributes within supertype 0187 rather than concentrating on one cluster.

### Property alignment + Evidence support — 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype (CS20230722_SUPT_0187) | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Isocortex [MBA:315] 1191; Hippocampal formation [MBA:1089] 348; Olfactory areas [MBA:698] 284 | not assessed | NOT_ASSESSED (region_evidence: DESCENDANT_ONLY) |
| NT type | GABAergic | not asserted | not assessed | NOT_ASSESSED |
| Cck expression | defining marker | mean 10.58; cohort_pct 0.903; child-coverage 1.000 | not assessed | CONSISTENT |
| Cnr1 expression | defining marker | mean 11.67; cohort_pct 0.839; child-coverage 1.000 | not assessed | CONSISTENT |
| Vglut3 expression | defining marker | mean 0.05; cohort_pct 0.419 | not assessed | DISCORDANT |
| Pvalb expression | ABSENT (negative marker) | mean 0.37; cohort_pct 0.452 | not assessed | DISCORDANT |
| Cck (neuropeptide) | classical neuropeptide | mean 10.58; cohort_pct 0.903 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Child-cluster breakdown not assessed at supertype edge; the cluster-level annotation transfer in Figure 1 shows the Harris CCK source distributed across five Sncg Gaba_3 children — see proposed experiments.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Harris 2018 Cck.Cxcl14.Vip cluster annotation transfer | Annotation transfer | PARTIAL | F1=0.77 at supertype | atlas-internal |

### 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] · 🟡 MODERATE

**Supporting evidence:**
- Annotation transfer of the Harris 2018 CA1 Cck.Cxcl14.Vip class (n=72 source cells) onto WMBv1 lands on supertype 0187 Sncg Gaba_3 at F1=0.77 with Coverage=0.95 and Purity=0.64; the higher-level class (06 CTX-CGE GABA) and subclass (047 Sncg Gaba) signals are consistent with the CGE origin of CCK basket cells.
- Supertype-level expression on 0187 shows Cck (10.58) and Cnr1 (11.67) at cohort percentiles 0.90 and 0.84 respectively — the two highest CCK / CB1R combined values in the hippocampal GABAergic cohort, with 100% child-cluster coverage for both markers.

**Marker evidence provenance:**
- **Cck**: protein-level (immunohistochemistry [5]) and transcript-level (intersectional genetic targeting [3], cluster-targeted re-analysis [7]); cell-type specificity is well established — Katona et al. confirmed CB1+ basket-cell morphology and 85.6% CCK co-expression on identified hippocampal interneurons [5].
- **Cnr1**: protein-level immunohistochemistry on CB1-positive basket cells co-stained for CCK [5]; transcript-level confirmation would strengthen this further.
- **Vglut3**: listed as a defining marker on the classical node without an explicit primary citation in `sources[]`; the supertype shows mean Vglut3 = 0.05 (below MIN_DETECTABLE), discordant with the classical assertion. The marker provenance gap and the negative supertype-level value should both be resolved.
- **Pvalb (negative marker)**: established as absent on Cnr1+ basket cell terminals by immunohistochemistry [5] [1]; supertype 0187 shows Pvalb = 0.37 at cohort percentile 0.45, which is in tension with the classical exclusion.

**Concerns:**
- Pvalb at mean 0.37 on the supertype (cohort_pct 0.45) is above MIN_DETECTABLE and discordant with the classical negative-marker call; this may reflect Pvalb expression in a minority of the supertype's children rather than the CCK-basket-cell-like child specifically. The atlas annotation/expression check is not triggered (Pvalb is not a listed marker on 0187) but the value is non-trivial.
- Vglut3 supertype mean (0.05) is discordant with the classical defining-marker assertion; the Harris-targeted child clusters (0672–0677) need direct expression inspection to determine whether Vglut3 is concentrated in a subset of children invisible at the supertype mean.
- Location alignment is NOT_ASSESSED because the supertype's region evidence is `DESCENDANT_ONLY` — the spatial signal is rescued from rank-0 children rather than carried at supertype rank. Hippocampal formation appears in 0187's top-3 anatomical bins (count_100um=348) but Isocortex (1191) and Olfactory areas (284) dominate, so the supertype is not hippocampus-specific.
- Annotation transfer evidence is from a single source dataset (Harris 2018, mouse CA1 inhibitory neurons, GEO:GSE99888); the Cck.Cxcl14.Vip label is a transcriptomic class, not a morphologically confirmed CCK basket cell cohort.

**What would upgrade confidence:**
- Patch-seq or Cnr1-Cre+ cluster annotation transfer targeted at morphologically confirmed CCK basket cells onto WMBv1, with F1 ≥ 0.80 at the supertype level; expected output: AnnotationTransferEvidence with morphology-confirmed source labels.
- Targeted literature trawl for primary Vglut3 expression evidence in CCK basket cells (a defining marker on the classical node currently lacks a primary citation).
- Cluster-level Pvalb expression breakdown across the five Sncg Gaba_3 children to test whether the supertype's non-zero Pvalb is concentrated outside the CCK-basket-cell-like child.

### Property alignment + Evidence support — 0681 Sncg Gaba_5 [CS20230722_CLUS_0681] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster (CS20230722_CLUS_0681) | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | not available | Hippocampal formation [MBA:1089] 158; Field CA1 [MBA:382] 81; Field CA1, stratum oriens [MBA:399] 68 | APPROXIMATE |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Cck expression | defining marker | not available | mean 11.12; cohort_pct 0.956 | CONSISTENT |
| Cnr1 expression | defining marker | not available | mean 12.71; cohort_pct 0.985 | CONSISTENT |
| Vglut3 expression | defining marker | not available | mean 3.29; cohort_pct 0.985 | CONSISTENT |
| Pvalb expression | ABSENT (negative marker) | not available | mean 1.05; cohort_pct 0.779 | DISCORDANT |
| Cck (neuropeptide) | classical neuropeptide | not available | mean 11.12; atlas category: NEUROPEPTIDE | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Single cluster, no supertype-level concordance inventory; 0681's parent is 0189 Sncg Gaba_5 — a different supertype than the AT-supported 0187 Sncg Gaba_3.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | region_fraction_100um=0.310 | atlas-internal |

### 0681 Sncg Gaba_5 [CS20230722_CLUS_0681] · 🟡 MODERATE

**Supporting evidence:**
- 0681 carries the strongest combined positive-marker profile of any candidate in the hippocampal GABAergic cohort: Cck mean=11.12 (cohort_pct 0.956), Cnr1 mean=12.71 (cohort_pct 0.985), Vglut3 mean=3.29 (cohort_pct 0.985). Atlas metadata records Cck as a `NEUROPEPTIDE` category marker on this cluster, consistent with the classical neuropeptide assertion.
- Cluster top anatomical bins include Field CA1 [MBA:382] (count_100um=81) and Field CA1, stratum oriens [MBA:399] (count_100um=68), with hippocampal formation as the dominant rank-1 anat label (count_100um=158); `region_fraction_100um`: 0.31 places 0681 in the boundary band for the queried CA1 pyramidal layer.
- Stage A scored 0681 at the top of its 50-member hippocampal GABAergic cohort (score 7 vs next-best 6), driven by three rank-2 marker tiers (Cck cohort_pct 0.956, Cnr1 0.985, Vglut3 0.985).

**Marker evidence provenance:**
- **Cck, Cnr1**: as for 0187 — protein and transcript evidence well established.
- **Vglut3**: 0681's value is substantially higher than 0187's (3.29 vs 0.05), suggesting Vglut3 is a child-cluster-specific signal not visible at the parent supertype mean. This is consistent with the HIDDEN-1:1 signal seen on the related Vip Gaba_7 supertype (Vglut3 child-coverage 0.333 on SUPT_0179). The primary-citation gap on the classical-node Vglut3 marker still applies.
- **Pvalb (negative marker)**: 0681 shows Pvalb = 1.05 (cohort_pct 0.78), well above MIN_DETECTABLE and the highest among CCK/Cnr1-high candidates considered. This is the principal counter-signal against a clean CCK basket cell mapping.

**Concerns:**
- Pvalb = 1.05 at cohort percentile 0.78 is a substantive contradiction of the classical negative marker. The literature establishes Pvalb-absence as a defining negative on CB1+ CCK basket cells with high (96%) selectivity at the protein level [5], so this is a non-trivial counter-signal at this cluster. No documented Pvalb-positive subpopulation of hippocampal CCK basket cells has been gathered in the available references — a targeted literature trawl is recommended (recorded in open questions).
- 0681 sits under supertype 0189 Sncg Gaba_5, NOT under the AT-supported supertype 0187 Sncg Gaba_3. The Harris 2018 annotation transfer of Cck.Cxcl14.Vip lands at 0187 / Sncg Gaba_3 (F1=0.77), not at 0189 / Sncg Gaba_5 (Sncg Gaba_5 does not appear in the Harris top hits at supertype level). The strong marker dominance of 0681 is therefore not corroborated by direct cluster annotation transfer evidence.
- Location alignment is APPROXIMATE — `region_fraction_100um: 0.31` places 0681 at the CA1 boundary band rather than centred in CA1 pyramidal layer; strict `region_fraction: 0.064` indicates only a small minority of cells fall strictly inside the queried region.

**What would upgrade confidence:**
- A morphology-confirmed CCK basket cell cluster annotation transfer (Cnr1-Cre+ or post-hoc CCK immunostaining on the sequenced cells) onto WMBv1 reporting F1 to both 0187 Sncg Gaba_3 and 0189 Sncg Gaba_5 — would resolve whether the Pvalb-low Harris cohort (mapping to 0187) and the Pvalb-positive marker-dominant 0189 Sncg Gaba_5 / 0681 cluster correspond to the same or different morphological types.
- Primary literature on Pvalb co-expression in CCK basket cells (or its absence): expected output: LiteratureEvidence on the classical node.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] | (supertype) | 7737 | 🟡 MODERATE | Harris CCK class AT F1=0.77 to supertype | Primary |
| 0681 Sncg Gaba_5 [CS20230722_CLUS_0681] | 0189 Sncg Gaba_5 | 291 | 🟡 MODERATE | Top Cck/Cnr1/Vglut3 expression in cohort | Secondary |
| 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | (supertype) | 1083 | 🔴 LOW | Cck and Vglut3 below cohort median | Eliminated (markers below cohort median) |
| 0651 Vip Gaba_7 [CS20230722_CLUS_0651] | 0179 Vip Gaba_7 | 170 | 🔴 LOW | Cck cohort_pct 0.29; Cnr1 0.79; Pvalb absent | Eliminated (Cck below cohort median) |
| 0655 Vip Gaba_9 [CS20230722_CLUS_0655] | 0181 Vip Gaba_9 | 653 | 🔴 LOW | Cck cohort_pct 0.13; Cnr1 0.52 | Eliminated (Cck below cohort median) |
| 0705 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0705] | 0198 RHP-COA Ndnf Gaba_6 | 61 | 🔴 LOW | Cck cohort_pct 0.25; Cnr1 0.43 | Eliminated (RHP-COA off-target subclass) |
| 0637 Vip Gaba_4 [CS20230722_CLUS_0637] | 0176 Vip Gaba_4 | 338 | 🔴 LOW | Location DISCORDANT (Isocortex + Cortical subplate dominant) | Eliminated (non-hippocampal location) |
| 0196 RHP-COA Ndnf Gaba_4 [CS20230722_SUPT_0196] | (supertype) | 167 | 🔴 LOW | Vglut3 cohort_pct 0.97 but RHP-COA off-target | Eliminated (RHP-COA off-target subclass) |
| 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | (supertype) | 725 | 🔴 LOW | Cck cohort_pct 0.10; Sst subclass | Eliminated (wrong subclass; Pvalb positive) |
| 0189 Sncg Gaba_5 [CS20230722_SUPT_0189] | (supertype) | 1065 | 🔴 LOW | High Cck/Cnr1 but Pvalb positive at supertype | Eliminated (Pvalb positive; superseded by child CLUS_0681) |
| 0198 RHP-COA Ndnf Gaba_6 [CS20230722_SUPT_0198] | (supertype) | 272 | 🔴 LOW | Cck and Cnr1 cohort_pct 0.32 / 0.42 | Eliminated (RHP-COA off-target subclass) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Cholecystokinin-positive basket cell node is defined as a GABAergic [3], perisomatic-targeting hippocampal interneuron of the CA1 pyramidal layer [UBERON:0014548] [1] [2] [3] [4], expressing Cck [5] [2] [4] [6] [7], Cnr1 [5], and Vglut3 as defining markers, with Cck as its principal neuropeptide [5] and Pvalb explicitly absent [5]. `definition_basis: CLASSICAL_MULTIMODAL`.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Cck.Cxcl14.Vip) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| Script (external) | ../at_run_20260506_harris_chamberland_mmc_wmbv1/README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Caveats | This run record scores Harris 2018's published Class labels against WMBv1. Companion run `at_run_20260512_chamberland_subfamily_mmc_wmbv1` scores the same underlying cluster-annotation-transfer output under Chamberland 2024 in-silico gene-pair subfamily labels. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:26+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0187 | ANNOTATION_TRANSFER | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0681 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0651 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0655 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0705 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0637 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0196 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0189 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0198 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Cholecystokinin-positive basket cell → 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] at MODERATE confidence. Key support: cluster annotation transfer of the Harris 2018 CCK-expressing CA1 inhibitory class to the Sncg subclass (F1=0.77 at supertype); supertype-level Cck and Cnr1 expression at cohort percentiles 0.90 and 0.84. Key caveats: AMBIGUOUS_MAPPING (Pvalb above MIN_DETECTABLE at supertype, Vglut3 below MIN_DETECTABLE); SINGLE_STUDY (one cluster annotation transfer source dataset).

The Cell Ontology has no specific term for this population; basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] is the closest ancestor. CL:0000118 covers perisomatic morphology but does not capture CCK/CB1R marker identity or regular-spiking firing pattern. No CCK-specific basket cell term in CL.

### Proposed experiments and follow-ups

A cluster annotation transfer run already exists (Harris 2018 Cck.Cxcl14.Vip → WMBv1; F1=0.77 at supertype 0187). This resolves the Harris-class → supertype mapping but does **not** anchor the assignment to morphologically confirmed CCK basket cells, leaves Pvalb co-expression unresolved, and does not corroborate the marker-dominant 0681 Sncg Gaba_5 cluster (which sits under a different supertype than the AT-supported one).

- **What:** cluster annotation transfer of a Cnr1-Cre+ or post-hoc CCK-immunostained CA1 basket cell dataset onto WMBv1.
  **Target:** F1 ≥ 0.80 at SUPERTYPE level; resolution to a single best child cluster at CLUSTER level.
  **Expected output:** AnnotationTransferEvidence with morphology-confirmed source labels.
  **Resolves:** whether the Harris-supported 0187 Sncg Gaba_3 mapping holds when the source labels are morphology-confirmed CCK basket cells; whether 0681 Sncg Gaba_5 (under 0189) represents a related but distinct CCK-expressing transcriptomic identity.

- **What:** child-cluster expression breakdown of Pvalb and Vglut3 across the five Sncg Gaba_3 children that received Harris Cck.Cxcl14.Vip transfer (CLUS_0672, 0673, 0676, 0677, 0674).
  **Target:** identify whether one child (analogous to the OLM-style supertype-with-best-child pattern) shows Pvalb below MIN_DETECTABLE and Vglut3 at or above the supertype mean.
  **Expected output:** PropertyComparison entries on a new child-cluster edge.
  **Resolves:** the Pvalb supertype-mean tension and the Vglut3 supertype-mean discordance; would also clarify whether the cluster-level scatter in Figure 1 is true sub-supertype heterogeneity or transfer noise.

- **What:** targeted literature trawl for primary Vglut3 expression in CCK basket cells and for documented Pvalb co-expression heterogeneity within CCK basket cells.
  **Target:** primary studies (not reviews) testing Vglut3 on morphologically confirmed CCK basket cells; primary studies reporting Pvalb co-expression in any CCK basket cell subpopulation.
  **Expected output:** LiteratureEvidence with PropertySource on the classical node.
  **Resolves:** the primary-citation gap on Vglut3 as a defining marker; whether the 0681 Pvalb signal corresponds to a documented biological subpopulation.

### Open questions

1. Does the Harris-supported supertype 0187 Sncg Gaba_3 and the marker-dominant 0681 Sncg Gaba_5 cluster correspond to distinct CCK-expressing transcriptomic identities, or to one continuum partitioned differently by the two evidence streams?
2. Is the supertype-level Pvalb signal at 0187 (mean 0.37) concentrated outside the Harris-targeted children, or distributed across them?
3. What is the primary evidence base for Vglut3 as a defining marker of hippocampal CCK basket cells?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703) | soma location |
| [2] | Fasano et al. 2017 | [28559797](https://pubmed.ncbi.nlm.nih.gov/28559797) | soma location |
| [3] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554) | soma location, NT, Cck marker |
| [4] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048) | soma location |
| [5] | Katona et al. 1999 | [10341254](https://pubmed.ncbi.nlm.nih.gov/10341254) | Cck, Cnr1 markers; Pvalb negative |
| [6] | Huang et al. 2014 | [24533597](https://pubmed.ncbi.nlm.nih.gov/24533597) | Cck marker |
| [7] | Fuzik et al. 2015 | [26689544](https://pubmed.ncbi.nlm.nih.gov/26689544) | Cck marker |

---

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0187 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Cluster annotation transfer of the Harris 2018
    CA1 Cck.Cxcl14.Vip class (run_ref at_run_20260512_harris_class_mmc_wmbv1)
    lands on CS20230722_SUPT_0187 at F1=0.77 (Coverage=0.95, Purity=0.64)
    with cluster-level scatter across five Sncg Gaba_3 children; supertype
    Cck (10.58) and Cnr1 (11.67) at cohort_pct 0.90 / 0.84 anchor the
    marker side. 4 of 6 property comparisons CONSISTENT; Vglut3 DISCORDANT
    at supertype mean (0.05) but child-cluster-localised on related Vip
    supertypes (HIDDEN-1:1 signal); Pvalb DISCORDANT at supertype mean (0.37).
  reconciliation_note: >
    Paired with the marker-dominant child-cluster candidate
    edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0681, which sits
    under a different supertype (0189 Sncg Gaba_5); the two survivors
    encode the AT-supported supertype reading and the expression-led
    cluster reading respectively, pending a curator-confirmed cluster
    annotation transfer source to discriminate.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Pvalb mean (0.37, cohort_pct 0.45) above MIN_DETECTABLE at
        CS20230722_SUPT_0187 is in tension with the classical
        negative-marker assertion; Vglut3 supertype mean (0.05) is
        discordant with the classical defining-marker assertion.
        Child-cluster breakdown not assessed at this edge.
    - caveat_type: SINGLE_STUDY
      description: >
        Cluster annotation transfer evidence rests on one source dataset
        (GEO:GSE99888, Harris 2018) targeting a transcriptomic Class
        label rather than curator-confirmed CCK basket cells.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        The Harris Cck.Cxcl14.Vip cohort fragments across multiple
        0187 Sncg Gaba_3 children at cluster resolution; the supertype
        is the supportable rank for this mapping (F1=0.77 at supertype
        vs F1=0.21 at subclass).
  proposed_experiments:
    - >
      Curator-confirmed CCK basket cell cluster annotation transfer onto
      WMBv1 with F1 >= 0.80 at SUPERTYPE level; expected output
      AnnotationTransferEvidence with source labels validated against
      classical CCK basket cell defining criteria.
    - >
      Child-cluster Pvalb and Vglut3 expression breakdown across the
      Sncg Gaba_3 children of CS20230722_SUPT_0187.
    - >
      Targeted literature trawl for primary Vglut3 expression in
      curator-confirmed CCK basket cells.
  unresolved_questions:
    - >
      Does CS20230722_SUPT_0187 (Harris-supported) and
      CS20230722_CLUS_0681 (marker-dominant, under SUPT_0189) correspond
      to distinct CCK-expressing transcriptomic identities or to one
      continuum partitioned differently by the two evidence streams?
    - >
      Trawl literature for Pvalb heterogeneity within the CCK basket
      cell type; the atlas-side non-zero supertype mean may be a real
      subpopulation signal not yet captured in the synthesised evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0681 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.5
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0681 carries the strongest combined
    Cck (11.12, cohort_pct 0.96), Cnr1 (12.71, cohort_pct 0.99) and
    Vglut3 (3.29, cohort_pct 0.99) profile in the hippocampal GABAergic
    cohort (50 members; Stage A score 7 vs next-best 6), with
    region_fraction_100um 0.31 placing it at the CA1 boundary band;
    Cck is recorded as a NEUROPEPTIDE atlas category marker.
    5 of 6 property comparisons CONSISTENT; Pvalb (1.05, cohort_pct 0.78)
    DISCORDANT with the classical negative-marker assertion.
  reconciliation_note: >
    Sits under CS20230722_SUPT_0189 (Sncg Gaba_5), not under the
    Harris-AT-supported CS20230722_SUPT_0187 (Sncg Gaba_3); paired with
    edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0187 in this
    report, pending a curator-confirmed cluster annotation transfer
    source to discriminate the two supertype-level placements.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Pvalb mean (1.05, cohort_pct 0.78) at CS20230722_CLUS_0681 is a
        substantive contradiction of the classical Pvalb-absent negative
        marker; no documented Pvalb-positive CCK basket cell subpopulation
        has been gathered in the available references.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        The companion supertype-level edge to CS20230722_SUPT_0187 is the
        cluster annotation transfer survivor; CS20230722_CLUS_0681 sits
        under CS20230722_SUPT_0189, not CS20230722_SUPT_0187. The marker
        dominance of CS20230722_CLUS_0681 lacks direct cluster annotation
        transfer support on this edge.
  proposed_experiments:
    - >
      Curator-confirmed CA1 CCK basket cell cluster annotation transfer
      reporting F1 to both CS20230722_SUPT_0187 and CS20230722_SUPT_0189
      to resolve whether the two supertype-level placements correspond to
      distinct transcriptomic identities.
  unresolved_questions:
    - >
      Is the Pvalb signal at CS20230722_CLUS_0681 (1.05) a documented
      biological co-expression in a CCK basket cell subpopulation or a
      cluster-level artefact?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0179 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0179 (Vip Gaba_7) shows Cck mean (1.36)
    at cohort_pct 0.07 and Vglut3 child-coverage 0.33, well below cohort
    medians; superseded by the Harris-AT-supported CS20230722_SUPT_0187
    placement.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Vip Gaba subclass identity is unexpected for CCK basket cells;
        the cluster annotation transfer does not support this supertype.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0651 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0651 (Vip Gaba_7) Cck mean (1.59) at
    cohort_pct 0.29 is below the cohort median for the defining marker;
    Pvalb is appropriately absent but the Cck signal does not support a
    primary CCK basket cell mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0655 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0655 (Vip Gaba_9) Cck mean (1.34) at
    cohort_pct 0.13 and Cnr1 cohort_pct 0.52 are below cohort medians
    for the CCK basket cell defining markers.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0705 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0705 (RHP-COA Ndnf Gaba_6) Cck (1.55,
    cohort_pct 0.25) and Cnr1 (8.28, cohort_pct 0.43) are below cohort
    medians; RHP-COA subclass identity is off-target for hippocampal
    CCK basket cells.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_CLUS_0637 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_CLUS_0637 (Vip Gaba_4) location DISCORDANT
    with Isocortex and Cortical subplate dominating its anatomical
    bins; region_fraction_100um 0.077 places it outside the CA1
    pyramidal layer target.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Isocortex (count_100um 1191) and Cortical subplate (count_100um 62)
        dominate the anatomical bins for CS20230722_CLUS_0637; only a
        small minority of cells fall in or near the CA1 pyramidal layer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0196 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0196 (RHP-COA Ndnf Gaba_4) RHP-COA
    subclass identity is off-target for hippocampal CCK basket cells;
    Vglut3 high (cohort_pct 0.97) but Pvalb (0.48) above MIN_DETECTABLE.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0219 (Sst Gaba_6) wrong subclass — Sst
    rather than CGE-derived Sncg/Vip; Cck (1.48, cohort_pct 0.10) and
    Cnr1 (3.04, cohort_pct 0.13) below cohort medians; Pvalb (1.68,
    cohort_pct 0.84) DISCORDANT with classical negative marker.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0189 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUPT_0189 (Sncg Gaba_5) carries high Cck
    (11.25, cohort_pct 0.94) and Cnr1 (12.48, cohort_pct 0.94) at the
    supertype but Pvalb (0.61, cohort_pct 0.68) above MIN_DETECTABLE;
    superseded in this report by its child CS20230722_CLUS_0681 (the
    marker-dominant secondary survivor) and not supported by the
    Harris cluster annotation transfer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0198 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0198 (RHP-COA Ndnf Gaba_6) RHP-COA
    subclass identity is off-target for hippocampal CCK basket cells;
    Cck (1.88, cohort_pct 0.32) and Cnr1 (9.11, cohort_pct 0.42) below
    cohort medians; Pvalb (0.23) above MIN_DETECTABLE.
```
<!-- verdict-block-end -->
