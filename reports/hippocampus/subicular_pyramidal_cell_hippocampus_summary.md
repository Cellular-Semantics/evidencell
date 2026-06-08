# subicular pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

Subicular pyramidal cells are the principal glutamatergic projection neurons of the subiculum, the main output structure of the hippocampal formation. They convey hippocampal output to entorhinal cortex and provide excitatory feedback to CA1, with three electrophysiologically distinct firing classes (regular-firing, weak-burst, strong-burst) described in the classical literature.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | subiculum [UBERON:0002191] | [1], [2], [3], [4] |
| NT type | glutamatergic | [5] |
| Defining markers | Np65 | [6] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location** (subiculum [UBERON:0002191]): classical anatomical assignment from multiple lines of evidence:
  > These subicular glutamatergic pyramidal neurons then transmit information to the deep layers (layers V and VI) of entorhinal cortex in a spatially structured manner (MacDougall et al., 2013)(Guinet et al., 2026).
  > — Unknown et al. 2026, Subicular Glutamatergic Neurons · [1] <!-- quote_key: 285611647_ae8e7717 -->

  > accumulating evidence supports the existence of a significant backprojection pathway comprised of both excitatory and inhibitory elements from the subiculum to CA1
  > — Unknown et al. 2016, abstract · [2] <!-- quote_key: 6552145_472efe77 -->

  > Hippocampome.org uses axonal and dendritic morphology as a foundational approach to classify neurons in the rodent hippocampal formation, including dentate gyrus, Cornu Ammonis, subiculum, and entorhinal cortex
  > — Unknown et al. 2025, abstract · [3] <!-- quote_key: 284374132_0534d2cf -->

  > The Cornu Ammonis‐1 (CA1) subfield and subiculum (SUB) serve as major output structures of the hippocampal formation
  > — Unknown et al. 2013, abstract · [4] <!-- quote_key: 2171766_537d45ba -->

  > The subiculum functions as one of the major output structures of the hippocampal formation alongside CA1, playing an integral role in hippocampal-cortical information processing (MacDougall et al., 2013). CA1 pyramidal cells project through a topographically organized projection to the subiculum, and the majority of subicular cells conserve their topographic input along the transverse axis from CA1 (MacDougall et al., 2013).
  > — Unknown et al. 2013, Subicular Glutamatergic Neurons · [4] <!-- quote_key: 2171766_2eaf3e02 -->

  > The subiculum also provides feedback connections to earlier stages of the hippocampal circuit, with anatomical and electrophysiological evidence showing that subicular neurons provide excitatory synaptic input back to CA1 pyramidal cells (Xu et al., 2016).
  > — Unknown et al. 2016, Subicular Glutamatergic Neurons · [2] <!-- quote_key: 6552145_e1cd39ad -->

- **NT type** (glutamatergic):
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG
  > — Dale et al. 2015, Anatomy of the Hippocampus · [5] <!-- quote_key: 2281033_8482ea88 -->

- **Np65 (defining marker)**:
  > the highest level of Np expression being located on the dendrites of granule cells and subicular pyramidal neurons
  > — I et al. 2019, abstract · [6] <!-- quote_key: 54102201_823cc8cc -->

</details>

Cell Ontology mapping: pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] (BROAD).

---

## Results

Annotation transfer from Yao 2021 (GSE185862) SMART-Seq v4 hippocampal subicular cells onto WMBv1, combined with atlas spatial registration, supports a supertype-level mapping to 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] as the primary intratelencephalic (IT) subicular type (AT F1=0.798 at supertype rank; n=471 source cells from the Yao 2021 SUB-ProS subclass). The classical subicular pyramidal cell does not collapse to a single WMBv1 supertype: the source-paper IT subicular cells distribute across three SUB-ProS supertypes (SUPT_0096/0097/0098 together account for 99.1% of SUB-ProS cells), and two additional projection-defined SUB supertypes (0121 CT SUB Glut_2, 0128 NP SUB Glut_2) lie within the subiculum on atlas spatial data and are plausible homologues of the WB / SB firing classes.

![Annotation transfer F1 across taxonomy levels for SUB-ProS source cells onto WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Yao 2021 SUB-ProS subclass source group (n=471) mapped onto WMBv1 (CCN20230722) by local MapMyCells. Nodes are coloured by F1 with **Purity** (Pur) = fraction of target cells from this source group and **Coverage** (Cov) = fraction of source cells landing on this target. F1 ≥ 0.5 at a level indicates a clean mapping. SUB-ProS cells resolve cleanly at supertype level on SUPT_0096 (F1=0.798; Cov=0.665; Pur=1.00), with the remaining SUB-ProS cells distributed across SUPT_0097 and SUPT_0098.*

### 0096 SUB-ProS Glut_1 · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype 0096 | Alignment |
|---|---|---|---|
| Soma location | subiculum [UBERON:0002191] | Subiculum [MBA:502] count_100um=3972; Prosubiculum [MBA:484682470] count_100um=2725; Hippocampal formation [MBA:1089] count_100um=4094 | CONSISTENT |
| NT type | glutamatergic | not asserted | NOT_ASSESSED |
| Np65 expression | defining marker | Np65: 8.60; cohort_pct 0.243; child-coverage 1.000 | APPROXIMATE |

*(Child-cluster breakdown not assessed at this report time — see proposed experiments.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yao 2021 SSv4 AT (`at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1`) | Annotation transfer | SUPPORT | F1=0.798 (supertype); Cov=0.665; Pur=1.00 | atlas-internal |
| Atlas precomputed expression / spatial | Atlas metadata | SUPPORT | Np65 mean 8.60; region_fraction_100um=0.966 | atlas-internal |

**Supporting evidence**

- Annotation transfer from Yao 2021 (GSE185862) SMART-Seq v4 hippocampal data, mapped onto WMBv1 by local MapMyCells, places 66.5% of Yao 2021 SUB-ProS subclass cells (n=313 of 471) on supertype 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096], with F1=0.798 at supertype level and target purity 1.00 (every cell mapped to SUPT_0096 originates from the Yao 2021 subicular source). This is direct transcriptomic evidence connecting a subiculum-targeted source cohort to the WMBv1 supertype.
- Atlas spatial registration places SUPT_0096 cleanly within the subiculum: of the cells in this supertype, near-100µm proximity to Subiculum [MBA:502] is 0.966 and strict in-region fraction is 0.767, with the dominant painted regions being Subiculum [MBA:502], Prosubiculum [MBA:484682470], and the parent Hippocampal formation [MBA:1089].
- Np65, the classical defining marker for subicular pyramidal cells (I et al. 2019 [6]), is expressed on this supertype (mean 8.60), although it is not specific to SUPT_0096 across the subiculum-glutamatergic cohort (cohort percentile 0.243).

**Marker evidence provenance**

- **Np65 (Nptn).** Evidence is from a single primary report at protein level (I et al. 2019, immunohistochemistry on rat hippocampus, dendrites of granule cells and subicular pyramidal neurons [6]). The atlas precomputed mean (8.60) confirms transcript-level presence on SUPT_0096 with child-coverage 1.00, but Np65 is not a unique discriminator — it is expressed across the subiculum-glutamatergic cohort with this supertype near the lower quartile (cohort percentile 0.243). The defining-marker status rests on a single primary citation; targeted lit review for additional subicular-pyramidal markers (e.g. Fn1, Ntng2, Nts subicular sub-class markers) would strengthen the mapping.

**Concerns**

- The classical subicular pyramidal cell type does not have a 1:1 WMBv1 supertype: the AT evidence shows the Yao 2021 SUB-ProS subclass also distributes 14.6% onto SUPT_0097 (F1=0.253) and 18.0% onto SUPT_0098 (F1=0.305). Together these three supertypes account for 99.1% of SUB-ProS cells — the classical type encompasses the IT subicular fan, not a single supertype. This edge captures the most abundant component (AMBIGUOUS_MAPPING caveat).
- NT type is not asserted on the atlas supertype metadata, so the glutamatergic identity cannot be confirmed from precomputed stats at supertype level; cluster-level Glut annotations on the SUB-ProS cluster children (e.g. CLUS_0277, CLUS_0282, CLUS_0283, CLUS_0294) confirm the glutamatergic identity by inheritance, but the supertype-level field is empty.
- Three electrophysiologically distinct subicular pyramidal subtypes (RF, WB, SB) are described in the classical literature, but the published electrophysiology has not been cross-walked onto the SUB-ProS / CT SUB / NP SUB supertype split. Whether the AT-secondary supertypes (SUPT_0097, SUPT_0098) and the projection-defined SUB supertypes (SUPT_0121, SUPT_0128) correspond to WB and SB firing types is unresolved.

**What would upgrade confidence**

- Patch-seq from electrophysiologically classified subicular pyramidal cells (RF / WB / SB) mapped via MapMyCells to WMBv1; targets at F1 ≥ 0.80 at supertype level for each firing class would resolve the SUPT_0096–SUPT_0098 / CT SUB / NP SUB assignment.
- Adding edges for SUPT_0097 and SUPT_0098 (the two other SUB-ProS supertypes that absorb the AT-mapped IT subicular cells) would complete the IT side of the mapping.
- Targeted literature trawl for subicular pyramidal marker panels beyond Np65 (e.g. Fn1, Ntng2, Calb1, Nts in subicular cell-type studies) to convert a single-marker defining set into a multi-marker panel.

### 0128 NP SUB Glut_2 · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype 0128 | Alignment |
|---|---|---|---|
| Soma location | subiculum [UBERON:0002191] | Subiculum [MBA:502] count_100um=3118; Prosubiculum [MBA:484682470] count_100um=1429; Hippocampal formation [MBA:1089] count_100um=3417 | CONSISTENT |
| NT type | glutamatergic | not asserted | NOT_ASSESSED |
| Np65 expression | defining marker | Np65: 9.63; cohort_pct 0.786; child-coverage 1.000 | CONSISTENT |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression / spatial | Atlas metadata | PARTIAL | Np65 mean 9.63 (cohort_pct 0.786); region_fraction_100um=0.900 | atlas-internal |

**Supporting evidence**

- Atlas spatial registration places 0128 NP SUB Glut_2 [CS20230722_SUPT_0128] cleanly within the subiculum: near-100µm proximity to Subiculum [MBA:502] is 0.900 and strict in-region fraction is 0.674, with dominant painted regions Subiculum [MBA:502], Prosubiculum [MBA:484682470], and Hippocampal formation [MBA:1089].
- Np65 expression is high on this supertype (mean 9.63, cohort percentile 0.786 — top quartile of the subiculum-glutamatergic cohort), consistent with the classical Np65-defining subicular pyramidal cell.
- This supertype is part of the WMBv1 "NP SUB" group — near-projecting subicular cells — which is a projection-defined subicular population candidate for one of the firing-class subtypes (plausibly the strong-burst SB class, which has been described as a distinct near-projecting subicular population in the classical literature).

**Concerns**

- No annotation transfer evidence on this edge: the Yao 2021 SUB-ProS subclass source maps predominantly onto the SUB-ProS supertypes (SUPT_0096–0098), not onto NP SUB. The Yao 2021 source labels include "NP SUB" as a separate subclass (see methods), but no AT result for that source label has been written onto this edge. The mapping to subicular pyramidal cells is therefore presumptive at this stage, resting on spatial registration and marker expression rather than direct transcriptomic anchoring of NP-SUB-labelled source cells.
- NT type is not asserted at supertype level (NOT_ASSESSED).
- The relationship of NP SUB to the classical subicular pyramidal firing classes (RF / WB / SB) is unresolved.

**What would upgrade confidence**

- Annotation transfer from a source dataset carrying explicit "NP SUB" labels (Yao 2021 has this subclass available; the present AT run aggregated source labels but the NP SUB subclass should be examined separately) onto SUPT_0128, with F1 ≥ 0.6 at supertype level.
- Patch-seq from near-projecting subicular pyramidal cells (axonal labelling + sequencing) mapped to WMBv1.

### 0121 CT SUB Glut_2 · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype 0121 | Alignment |
|---|---|---|---|
| Soma location | subiculum [UBERON:0002191] | Subiculum [MBA:502] count_100um=928; Prosubiculum [MBA:484682470] count_100um=633; Hippocampal formation [MBA:1089] count_100um=1425 | CONSISTENT |
| NT type | glutamatergic | not asserted | NOT_ASSESSED |
| Np65 expression | defining marker | Np65: 9.57; cohort_pct 0.743; child-coverage 1.000 | CONSISTENT |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression / spatial | Atlas metadata | PARTIAL | Np65 mean 9.57 (cohort_pct 0.743); region_fraction_100um=0.590 | atlas-internal |

**Supporting evidence**

- Atlas spatial registration places 0121 CT SUB Glut_2 [CS20230722_SUPT_0121] in the subiculum with near-100µm proximity 0.590 and strict in-region fraction 0.464 (a weaker, but still SELF, region signal than SUPT_0096 or SUPT_0128).
- Np65 mean (9.57; cohort percentile 0.743) is among the top quartile of the subiculum-glutamatergic cohort, consistent with the classical Np65-defining subicular pyramidal cell.
- WMBv1 labels this supertype as "CT SUB" — cortico-thalamic projecting subicular cells — a projection-defined subicular population that is a candidate for one of the classical firing-class subtypes (plausibly the regular-firing RF class or the weak-burst WB class given their cortico-thalamic projection patterns described in the classical literature).

**Concerns**

- No annotation transfer evidence on this edge. Source-paper cohort-based confirmation of the CT SUB ↔ subicular pyramidal cell identity is absent in the present run.
- Strict in-region fraction (0.464) is lower than SUPT_0096 (0.767) and SUPT_0128 (0.674) — `region_fraction_100um: 0.590` indicates some boundary scatter into Prosubiculum and the broader Hippocampal formation, consistent with the CT SUB cells sitting at the subiculum / prosubiculum boundary rather than centred in MBA:502.
- NT type NOT_ASSESSED at supertype level.

**What would upgrade confidence**

- Annotation transfer from a source dataset carrying explicit "CT SUB" or retrograde-labelled cortico-thalamic projecting subicular cells, with F1 ≥ 0.6 at supertype level.
- Patch-seq from electrophysiologically classified cortico-thalamic subicular cells mapped to WMBv1.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] | — | 3490 | 🟡 MODERATE | Yao 2021 AT F1=0.798; in subiculum | Primary |
| 0128 NP SUB Glut_2 [CS20230722_SUPT_0128] | — | 2445 | 🟡 MODERATE | Np65 high; in subiculum; projection-defined SUB subtype | Secondary |
| 0121 CT SUB Glut_2 [CS20230722_SUPT_0121] | — | 2367 | 🟡 MODERATE | Np65 high; in subiculum; projection-defined SUB subtype | Secondary |
| 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] (legacy/duplicate edge id) | — | 3490 | ⚪ UNCERTAIN | Duplicate edge — see primary | Eliminated (duplicate edge id) |
| 0256 ENTmv-PA-COAp Glut_2 [CS20230722_CLUS_0256] | 0067 ENTmv-PA-COAp Glut_2 | 334 | 🔴 LOW | Outside subiculum — entorhinal / PA / COAp | Eliminated (wrong region) |
| 0277 CA1-ProS Glut_2 [CS20230722_CLUS_0277] | 0070 CA1-ProS Glut_2 | 283 | 🔴 LOW | CA1-prosubiculum cells, not subiculum | Eliminated (CA1, not subiculum) |
| 0282 CA1-ProS Glut_2 [CS20230722_CLUS_0282] | 0071 CA1-ProS Glut_3 | 251 | 🔴 LOW | CA1-prosubiculum cells, not subiculum | Eliminated (CA1, not subiculum) |
| 0283 CA1-ProS Glut_3 [CS20230722_CLUS_0283] | 0071 CA1-ProS Glut_3 | 102 | 🔴 LOW | CA1-prosubiculum cells, not subiculum | Eliminated (CA1, not subiculum) |
| 0294 CA1-ProS Glut_6 [CS20230722_CLUS_0294] | 0074 CA1-ProS Glut_6 | 802 | 🔴 LOW | CA1-prosubiculum cells, not subiculum | Eliminated (CA1, not subiculum) |
| 1181 COP NN_1 [CS20230722_SUPT_1181] | — | 16063 | 🔴 REFUTED | Isocortex / fibre tracts, not subiculum | Eliminated (wrong region — isocortex) |
| 0172 OB-STR-CTX Inh IMN_7 [CS20230722_SUPT_0172] | — | 32 | 🔴 REFUTED | OB-STR-CTX inhibitory immature; wrong subclass | Eliminated (wrong subclass — inhibitory) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The subicular pyramidal cell is defined as the principal glutamatergic projection neuron of the subiculum [UBERON:0002191], with Np65 as a defining dendritic marker (I et al. 2019 [6]). Classical references support soma location in the subiculum [1, 2, 3, 4] and glutamatergic identity [5]. `definition_basis: CLASSICAL_MULTIMODAL` — anatomical, electrophysiological, and connectional criteria define the type; three electrophysiological subtypes (RF, WB, SB) are described in the classical literature.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:502 Subiculum, NT type glutamatergic, defining marker Np65). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 (GSE185862) mouse hippocampal formation SMART-Seq v4 cell type labels) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:53+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_subicular_pyramidal_cell_hippocampus_to_supt_0096 | ANNOTATION_TRANSFER; ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0096 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0128 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0121 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0256 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0277 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0282 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0283 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0294 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_1181 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0172 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** subicular pyramidal cell → 0096 SUB-ProS Glut_1 [CS20230722_SUPT_0096] at MODERATE confidence. Key support: annotation transfer from Yao 2021 SUB-ProS source cells (F1=0.798 at supertype rank) and atlas spatial registration (in subiculum, region_fraction_100um=0.966). Key caveats: AMBIGUOUS_MAPPING — the classical type also encompasses SUPT_0097 / SUPT_0098 (other SUB-ProS supertypes) and plausibly the projection-defined SUPT_0121 (CT SUB) and SUPT_0128 (NP SUB).

The Cell Ontology has no specific term for this population; pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] is the closest ancestor. Subicular pyramidal cells are the primary glutamatergic output neurons of the subiculum. Three electrophysiologically distinct subtypes (RF, WB, SB) have been described (Guinet et al., 2026). No subiculum-specific CL term exists; CL:0000598 (pyramidal neuron) is used as BROAD mapping.

### Proposed experiments and follow-ups

Annotation transfer from the Yao 2021 SUB-ProS subclass has already been completed for SUPT_0096 (F1=0.798). The remaining experiments are:

- **What:** annotation transfer of remaining SUB-ProS source cells onto SUPT_0097 and SUPT_0098. **Target:** F1 reported at supertype rank for each subtarget. **Expected output:** AnnotationTransferEvidence on new edges to SUPT_0097 and SUPT_0098. **Resolves:** completes the IT subicular side of the mapping; addresses caveat AMBIGUOUS_MAPPING.
- **What:** annotation transfer from source labels carrying explicit "CT SUB" and "NP SUB" subclasses (Yao 2021 includes both as separate subclass labels). **Target:** F1 ≥ 0.6 at supertype level for SUPT_0121 and SUPT_0128. **Expected output:** AnnotationTransferEvidence on the SUPT_0121 and SUPT_0128 edges. **Resolves:** whether the projection-defined SUB supertypes are direct homologues of the classical firing-class subtypes.
- **What:** patch-seq from electrophysiologically classified subicular pyramidal cells (RF / WB / SB firing classes), mapped via MapMyCells to WMBv1. **Target:** F1 ≥ 0.80 at supertype level for each firing class. **Expected output:** AnnotationTransferEvidence linking firing class → WMBv1 supertype. **Resolves:** Open question 1 (which firing class corresponds to which supertype).
- **What:** targeted literature trawl for a multi-marker subicular pyramidal panel beyond Np65. **Target:** identify ≥ 2 additional primary-citation markers with transcript-level data. **Expected output:** LiteratureEvidence on the classical node and additional `property_comparisons` rows on existing edges. **Resolves:** weak marker provenance for the classical type.

### Open questions

1. Which of the three electrophysiological subtypes of subicular pyramidal cells (regular-firing RF, weak-burst WB, strong-burst SB) correspond to SUPT_0096, SUPT_0097, SUPT_0098, SUPT_0121 (CT SUB), and SUPT_0128 (NP SUB)? F1 scores per electrophysiologically classified source cohort would resolve this.
2. The graph contains two edges targeting CS20230722_SUPT_0096 with different edge ids (one carrying the AT + caveat record, one a stub fresh-emit edge); curator removal of the duplicate is needed.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2026 · PMID:41693678 | [41693678](https://pubmed.ncbi.nlm.nih.gov/41693678) | soma location |
| [2] | Unknown 2016 · PMID:27150503 | [27150503](https://pubmed.ncbi.nlm.nih.gov/27150503) | soma location |
| [3] | Unknown 2025 · PMID:41509312 | [41509312](https://pubmed.ncbi.nlm.nih.gov/41509312) | soma location |
| [4] | Unknown 2013 · PMID:24303119 | [24303119](https://pubmed.ncbi.nlm.nih.gov/24303119) | soma location |
| [5] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726) | neurotransmitter type |
| [6] | I et al. 2019 · PMID:30488668 | [30488668](https://pubmed.ncbi.nlm.nih.gov/30488668) | Np65 marker |

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_supt_0096 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer from Yao 2021 SUB-ProS source cells
    onto WMBv1 (run_ref at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) places
    66.5% of n=471 source cells on CS20230722_SUPT_0096 with F1=0.80 at
    supertype rank (target purity 1.00); atlas spatial registration places
    SUPT_0096 in MBA:502 with region_fraction_100um: 0.97. Np65 is expressed
    on the supertype (mean 8.60, cohort percentile 0.243; not specific
    within the subiculum-glutamatergic cohort). The classical subicular
    pyramidal type encompasses three IT SUB-ProS supertypes
    (SUPT_0096/0097/0098) plus projection-defined CT SUB and NP SUB
    populations — broadMatch + 1:n captures the IT-primary supertype.
  reconciliation_note: >
    Two edges in the graph target CS20230722_SUPT_0096
    (edge_subicular_pyramidal_cell_hippocampus_to_supt_0096 carrying the
    AT evidence + AMBIGUOUS_MAPPING caveat; edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0096
    a fresh-emit stub with only ATLAS_METADATA). This verdict is on the
    substantive edge; the duplicate fresh-emit edge should be removed.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical subicular pyramidal cells encompass three SUB-ProS
        supertypes (SUPT_0096/0097/0098 together absorb 99.1% of Yao 2021
        SUB-ProS source cells) plus the projection-defined CT SUB
        (SUPT_0121) and NP SUB (SUPT_0128) supertypes. This edge targets
        SUPT_0096 as the IT-primary; full coverage requires edges to
        SUPT_0097 and SUPT_0098.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        The single defining marker Np65 (mean 8.60, cohort percentile 0.243)
        is expressed across the subiculum-glutamatergic cohort and does
        not uniquely identify SUPT_0096.
  proposed_experiments:
    - Annotation transfer of Yao 2021 SUB-ProS source cells onto
      CS20230722_SUPT_0097 and CS20230722_SUPT_0098 to complete the IT
      subicular mapping (F1 reported at supertype rank).
    - Targeted transcriptomic profiling of RF / WB / SB firing-class subicular pyramidal cells
      mapped to WMBv1 by MapMyCells at F1 >= 0.80 at supertype rank to
      resolve the firing-class to supertype assignment.
    - Targeted literature trawl for additional primary-citation
      transcript-level subicular pyramidal markers beyond Np65.
  unresolved_questions:
    - Which firing-class subtypes (RF / WB / SB) correspond to which
      SUB-ProS / CT SUB / NP SUB supertypes (SUPT_0096, 0097, 0098, 0121,
      0128)?
    - Curator removal of duplicate edge edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0096
      — legacy/fresh-emit ID collision on taxonomy_type CS20230722_SUPT_0096.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0096 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Duplicate edge id targeting CS20230722_SUPT_0096; the
    substantive edge with annotation-transfer evidence is
    edge_subicular_pyramidal_cell_hippocampus_to_supt_0096. This stub
    carries only ATLAS_METADATA and should be removed by curator
    (legacy/fresh-emit ID collision).
  caveats:
    - caveat_type: OTHER
      description: >
        Duplicate edge targeting the same taxonomy_type
        (CS20230722_SUPT_0096) as a substantive AT-bearing edge; flagged
        for curator removal.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0128 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.5
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Atlas spatial registration places CS20230722_SUPT_0128 in
    MBA:502 with region_fraction_100um: 0.90; Np65 mean 9.63 (cohort
    percentile 0.786) is in the top quartile of the
    subiculum-glutamatergic cohort. NP SUB is a projection-defined
    subicular subpopulation that is a candidate for one of the classical
    firing-class subtypes (plausibly SB). No annotation transfer evidence
    on this edge yet — the call rests on spatial + marker convergence.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        No annotation transfer evidence on this edge; mapping rests on
        atlas spatial registration and Np65 expression alone (no
        independent transcriptomic anchor from a source cohort).
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Relationship of NP SUB to the classical RF / WB / SB firing-class
        subtypes is unresolved.
  proposed_experiments:
    - Annotation transfer from Yao 2021 source labels carrying the "NP
      SUB" subclass onto CS20230722_SUPT_0128 (F1 >= 0.6 at supertype
      rank).
    - Targeted transcriptomic profiling of near-projecting subicular cells (with axonal
      labelling) mapped to WMBv1 to confirm the NP SUB identity.
  unresolved_questions:
    - Does CS20230722_SUPT_0128 correspond to one of the classical
      subicular pyramidal firing-class subtypes (RF / WB / SB)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0121 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.45
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Atlas spatial registration places CS20230722_SUPT_0121 in
    MBA:502 with region_fraction_100um: 0.59 (some boundary scatter into
    Prosubiculum); Np65 mean 9.57 (cohort percentile 0.743) is in the top
    quartile of the subiculum-glutamatergic cohort. CT SUB is a
    projection-defined cortico-thalamic subicular subpopulation that is
    a candidate for one of the classical firing-class subtypes. No
    annotation transfer evidence on this edge yet.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        No annotation transfer evidence on this edge; mapping rests on
        atlas spatial registration and Np65 expression alone.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Relationship of CT SUB to the classical RF / WB / SB firing-class
        subtypes is unresolved.
  proposed_experiments:
    - Annotation transfer from Yao 2021 source labels carrying the "CT
      SUB" subclass onto CS20230722_SUPT_0121 (F1 >= 0.6 at supertype
      rank).
    - Targeted transcriptomic profiling of electrophysiologically classified cortico-thalamic
      subicular cells mapped to WMBv1.
  unresolved_questions:
    - Does CS20230722_SUPT_0121 correspond to one of the classical
      subicular pyramidal firing-class subtypes (RF / WB / SB)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0256 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0256 is an ENTmv-PA-COAp glutamatergic
    cluster whose dominant painted regions are entorhinal area, piriform-
    amygdalar, and cortical amygdalar — outside the subiculum. Region
    fraction is high only because the cluster spills into hippocampal
    formation parents; strict in-region fraction at MBA:502 is 0.49 and
    the dominant region is not subiculum. Not the classical subicular
    pyramidal cell.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant painted region is entorhinal / piriform-amygdalar, not
        subiculum.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0277 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0277 is a CA1-prosubiculum glutamatergic
    cluster; dominant painted regions are Field CA1 [MBA:382] and
    Prosubiculum [MBA:484682470], not subiculum proper. CA1 pyramidal
    cells project to subiculum but are not subicular pyramidal cells.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Cluster is CA1-ProS (CA1 pyramidal / prosubiculum), not subiculum
        proper.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0282 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0282 is a CA1-prosubiculum glutamatergic
    cluster; dominant painted regions are Prosubiculum [MBA:484682470]
    and Field CA1 (parent: Hippocampal formation [MBA:1089]) — not
    subiculum proper. Strict in-region fraction at MBA:502 is 0.17.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Cluster is CA1-ProS, not subiculum proper.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0283 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0283 is a CA1-prosubiculum glutamatergic
    cluster; dominant painted regions are Prosubiculum [MBA:484682470]
    and subiculum boundary, with strict in-region fraction at MBA:502
    only 0.17. CA1-ProS cluster, not subiculum proper.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Cluster is CA1-ProS, not subiculum proper.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0294 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0294 is a CA1-prosubiculum glutamatergic
    cluster; dominant painted regions are Prosubiculum [MBA:484682470]
    and Field CA1 (parent: Hippocampal formation [MBA:1089]). CA1-ProS,
    not subiculum proper.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Cluster is CA1-ProS, not subiculum proper.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_1181 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:NoCorrespondence
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] CS20230722_SUPT_1181 (COP NN_1) dominant painted regions
    are Isocortex [MBA:315], lateral forebrain bundle system, and corpus
    callosum — not subiculum (region_fraction_100um: 0.02; strict
    region_fraction: 0.01). High Np65 expression (mean 10.37) is not
    specific to subicular pyramidal identity; this supertype is in
    cortex / fibre tracts.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant painted regions are isocortex, lateral forebrain bundle
        system, and corpus callosum — not subiculum.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_subicular_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0172 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  relationship: evidencell:NoCorrespondence
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] CS20230722_SUPT_0172 (OB-STR-CTX Inh IMN_7) is labelled as
    an inhibitory immature neuron supertype whose dominant painted
    regions are lateral forebrain bundle system, corpus callosum, and
    cerebrum-related — not subiculum (region_fraction_100um: 0.08).
    Wrong subclass (inhibitory) and wrong region.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant painted regions are lateral forebrain bundle / corpus
        callosum / cerebrum-related — not subiculum; cells labelled
        inhibitory immature, inconsistent with classical glutamatergic
        identity.
```
<!-- verdict-block-end -->
