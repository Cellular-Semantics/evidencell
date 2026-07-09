# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Hippocampal bistratified cells are CA1 GABAergic interneurons whose somata lie in or near stratum pyramidale and whose axons co-innervate stratum oriens and stratum radiatum, where they target the basal and apical dendrites of CA1 pyramidal neurons. They co-express parvalbumin (Pvalb) with somatostatin (Sst) and the tachykinin precursor Tac1, and recent intersectional genetic work has shown that Sst::Tac1 driver combinations preferentially label bistratified cells whose principal postsynaptic targets are fast-spiking interneurons [9]. Their position within the Pvalb-Sst overlap and their dendrite-targeting axonal arbor place them at a transcriptomic interface between PV-basket and Sst-OLM identity classes — a placement that makes mapping to the WMBv1 supertype/cluster taxonomy informative for testing whether morphological identity is recoverable from somatic transcriptome alone [3].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548]; CA1 stratum oriens [UBERON:0014552]; CA1 stratum radiatum [UBERON:0014554] | [1], [2], [3] |
| NT | GABAergic | [4] |
| Defining markers | Pvalb, Sst, Tac1 | Pvalb: [5], [6], [7], [8]; Sst, Tac1: [9] |
| Neuropeptides | Sst | [9] |
| CL term | bistratified cell [CL:0004247] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical literature on hippocampal inhibitory cell types places bistratified somata in stratum pyramidale with dendritic projections into oriens and radiatum [1], [2], [3].
  > The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus
  > — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [3] <!-- quote_key: 224817966_79f4a500 -->
- **Pvalb as defining marker:** parvalbumin defines the broader interneuron class to which bistratified cells belong [5], [6], [7], [8].
  > Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
  > — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 38778375_462ec931 -->
  > WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes (basket, axo-axonic, bistratified, radiatum-targeting).
  > — Ekins et al. 2020, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 221276443_e917908b -->
- **Sst and Tac1 as defining markers, and Sst as neuropeptide:** the Sst::Tac1 intersection genetically isolates a bistratified-enriched population [9].
  > the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [9] <!-- quote_key: 269246896_c084d5c0 -->
- **Transcriptomic separability caveat (Pvalb subtypes):** PV-interneuron anatomical heterogeneity is poorly captured by transcriptome alone — relevant when reading scatter at the cluster level [8].
  > while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities
  > — Que et al. 2021 · [8] <!-- quote_key: 230508306_e8cc8c19 -->

</details>

Cell Ontology mapping: bistratified cell [[CL:0004247](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)] (BROAD). CL:0004247 is retinal-focused; the hippocampal Pvalb/Sst/Tac1+ bistratified interneuron with an SO+SR-targeting axon has no dedicated CL term, and a hippocampus-specific contribution is warranted.

---

## Results

Marker expression alignment and a Que 2021 morphology-confirmed PV-bistratified annotation transfer (BIC source group) converge on the parvalbumin-Sst-Tac1 supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] and its hippocampal child 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] as the supportable mapping (see filtered annotation transfer figure and property comparison tables below). The supertype hosts both PV-basket and PV-bistratified morphologies, and cluster-level scatter into a sibling cluster reflects that anatomical heterogeneity rather than a failure of the mapping (Que 2021 [8]); a Sst-dominant, Pvalb-low subpopulation possibly captured by 0216 Sst Gaba_3 [CS20230722_SUPT_0216] remains a secondary low-confidence reading.

**Annotation-transfer overview (filtered to bistratified-relevant source group)**

![Filtered AT figure for bistratified cell — Que 2021 PV-bistratified source group](figures/f1_for_bistratified_cell_hippocampus.png)

*Annotation transfer F1 across the WMBv1 class → subclass → supertype → cluster taxonomy for the Que 2021 morphology-confirmed PV-bistratified source group (BIC; n=18 source cells at supertype). **Pur** = Purity (fraction of target cells from this source group); **Cov** = Coverage (fraction of source-group cells landing on this target). Coverage is high at every level (≥0.90 to class/subclass/supertype/cluster), but Purity is low at class (0.22), subclass (0.24), and supertype (0.24) because PV-bistratified cells share these levels with PV-basket and chandelier cells; Purity climbs at the cluster level (0.70, CLUS_0737) where the bistratified-favouring subpopulation is concentrated. The cluster-level resolution recovers a clean mapping that the upper taxonomy levels collapse together.*

### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Hippocampal formation [MBA:1089] / Field CA1 [MBA:382] / Cortical subplate [MBA:703], region_fraction_100um=0.160 | Field CA1 [MBA:382] / Field CA1, stratum oriens [MBA:399] (CLUS_0737), region_fraction_100um=0.224 | APPROXIMATE |
| NT type | GABAergic | not asserted at supertype | GABA (CLUS_0737) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Pvalb | defining marker | 8.74 (cohort_pct 0.968, child-coverage 1.000) | 8.27 (cohort_pct 0.956, CLUS_0737) | CONSISTENT |
| Sst | defining marker | 2.72 (cohort_pct 0.774, child-coverage 1.000) | 4.39 (cohort_pct 0.706, CLUS_0737; atlas NEUROPEPTIDE) | CONSISTENT |
| Tac1 | defining marker | 5.36 (cohort_pct 0.935, child-coverage 1.000) | 7.26 (cohort_pct 0.956, CLUS_0737; atlas NEUROPEPTIDE) | CONSISTENT |
| Sst (neuropeptide) | classical neuropeptide | 2.72 | 4.39 (CLUS_0737) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(2 of 2 informative child clusters of SUPT_0206 — CLUS_0737 and CLUS_0739 — show Pvalb/Sst/Tac1 concordance with classical bistratified markers; CLUS_0737 is the PV-bistratified cluster matched by Que 2021 BIC annotation transfer, and CLUS_0739 carries a higher PV / lower Sst profile consistent with PV-basket. Best match: CLUS_0737.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (SUPT_0206) | Atlas metadata | PARTIAL | region_fraction_100um=0.160; strict=0.032 | atlas-internal |

**Supporting evidence**
- Pvalb, Sst and Tac1 are each in the top cohort decile at SUPT_0206 (cohort_pct 0.968 / 0.774 / 0.935 with full child-cluster coverage) — the supertype combines all three defining markers, the genetically defined signature of the Sst::Tac1 intersection [9].
- The supertype contains the cluster CLUS_0737 whose hippocampal CA1 enrichment and parvalbumin / Sst / Tac1 profile is the best cluster-level match (see CLUS_0737 section).
- Region proximity is APPROXIMATE: 16% of SUPT_0206 cells lie within 100 µm of CA1, while the strict in-CA1 fraction is only 3.2% — characteristic boundary scatter, with the registration footprint biased toward hippocampal formation and the cortical subplate.

**Marker evidence provenance**
- Pvalb is supported by primary studies of PV-interneuron heterogeneity that explicitly enumerate bistratified as one of the PV morphological subtypes [5], [6], [7], [8]. Cross-check against precomputed stats confirms Pvalb 8.74 at SUPT_0206 (cohort_pct 0.968).
- Sst and Tac1 derive from a single primary study using the Sst::Tac1 intersection [9]; this is the strongest single piece of evidence anchoring bistratified to the Pvalb / Sst / Tac1 transcriptomic signature, because the intersection-targeted population was morphologically and physiologically characterised as bistratified. Atlas annotation flags both Sst and Tac1 as NEUROPEPTIDE at CLUS_0737, consistent with their dual marker / neuropeptide use here.

**Concerns**
- The supertype lumps morphologically distinct PV interneuron types — at minimum PV-basket (CLUS_0739) and PV-bistratified (CLUS_0737) — and a single-cluster mapping is therefore preferred where supported. Que 2021 explicitly notes that PV-interneuron anatomical types are not well separated in continuous transcriptomic space [8], which constrains how clean a supertype-level call can ever be.
- Location alignment is approximate (region_fraction_100um=0.160) reflecting the supertype's spread across hippocampus, isocortex and cortical subplate; consistent with a broader PV-interneuron supertype rather than a hippocampus-specific match.

**What would upgrade confidence**
- Replication of the Que 2021 morphology-confirmed PV-bistratified annotation transfer with an independent Pvalb-Cre × bistratified morphology dataset (target: AnnotationTransferEvidence with F1 ≥ 0.80 at CLUSTER level on CLUS_0737).
- Robustness check of the Que 2021 BIC → CLUS_0737 mapping under raw-counts versus TPM-pseudo-count normalisation of GEO:GSE142546.

### 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | (see SUPT_0206 row above) | Field CA1 [MBA:382] / Field CA1, stratum oriens [MBA:399], region_fraction_100um=0.224 | APPROXIMATE |
| NT type | GABAergic | not asserted at supertype | GABA | CONSISTENT |
| Pvalb | defining marker | 8.74 at SUPT_0206 | 8.27 (cohort_pct 0.956) | CONSISTENT |
| Sst | defining marker | 2.72 at SUPT_0206 | 4.39 (cohort_pct 0.706; atlas NEUROPEPTIDE) | CONSISTENT |
| Tac1 | defining marker | 5.36 at SUPT_0206 | 7.26 (cohort_pct 0.956; atlas NEUROPEPTIDE) | CONSISTENT |
| Sst (neuropeptide) | classical neuropeptide | 2.72 at SUPT_0206 | 4.39 | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (CLUS_0737) | Atlas metadata | PARTIAL | region_fraction_100um=0.224; strict=0.040 | atlas-internal |

*(3 of 3 defining-marker comparisons CONSISTENT at CLUS_0737; the cluster's location is APPROXIMATE with 22.4% within 100 µm of CA1 and strict in-CA1 fraction 4.0% — boundary scatter rather than off-target.)*

**Supporting evidence**
- All three defining markers are highly expressed at CLUS_0737: Pvalb 8.27 (cohort_pct 0.956), Sst 4.39 (0.706), Tac1 7.26 (0.956). Both Sst and Tac1 carry an atlas NEUROPEPTIDE annotation at this cluster, matching the classical neuropeptide assignment for Sst [9].
- Spatial location is the strongest hippocampal signal among the survivor clusters: the dominant 100-µm neighbourhood of CLUS_0737 cells is Field CA1 [MBA:382] and Field CA1, stratum oriens [MBA:399]. The strict in-CA1 fraction (0.040) is low — characteristic of supertype-level Pvalb populations whose somata sit near layer boundaries.
- This is the cluster that the morphology-confirmed PV-bistratified annotation transfer from Que 2021 [8] picks as its best cluster-level target. The annotation-transfer figure (above) shows Purity rising from ~0.24 at supertype to ~0.70 at cluster, identifying CLUS_0737 as the cluster that disambiguates PV-bistratified from sibling PV-basket / chandelier morphologies that share the broader supertype.

**Marker evidence provenance**
- Pvalb, Sst and Tac1 marker provenance as for SUPT_0206; the cluster-level expression at CLUS_0737 is at least as strong on Tac1 (7.26 vs supertype 5.36) and stronger on Sst (4.39 vs 2.72), consistent with bistratified-enriched relative to other supertype children.

**Concerns**
- The supertype is known to contain PV-basket cells in a sibling cluster (CLUS_0739), and that sibling shows even higher Pvalb (10.63) but a much lower Sst level (1.51) — the bistratified vs basket assignment between CLUS_0737 and CLUS_0739 rests primarily on the Sst / Tac1 cohort percentile, not on Pvalb.
- A Sst-dominant, Pvalb-low fraction of bistratified cells (if it exists) may scatter into SUPT_0216 (Sst Gaba_3), where Sst is far higher (11.44 vs 4.39) but Pvalb falls to 1.48 — the Sst Gaba_3 reading remains speculative (see next section).
- Annotation transfer confirmation has been done with a single primary study (Que 2021) on a normalisation that is not yet replicated.

**What would upgrade confidence**
- Independent annotation-transfer with a morphologically confirmed PV-bistratified scRNA-seq cohort (e.g. Sst::Tac1 intersectional dataset from Chamberland 2024 [9]), targeting AnnotationTransferEvidence with F1 ≥ 0.80 at CLUSTER level on CLUS_0737.
- Robustness check on raw-counts vs TPM-pseudo-counts normalisation in GEO:GSE142546.

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Hippocampal formation [MBA:1089] / Field CA1 [MBA:382] / Field CA1, stratum oriens [MBA:399], region_fraction_100um=0.153 | not assessed at child level | APPROXIMATE |
| NT type | GABAergic | not asserted | not asserted | NOT_ASSESSED |
| Pvalb | defining marker | 1.48 (cohort_pct 0.806, child-coverage 0.889) | not assessed | CONSISTENT |
| Sst | defining marker | 11.44 (cohort_pct 0.968, child-coverage 1.000) | not assessed | CONSISTENT |
| Tac1 | defining marker | 0.55 (cohort_pct 0.742, child-coverage 0.667) | not assessed | CONSISTENT |
| Sst (neuropeptide) | classical neuropeptide | 11.44 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown of bistratified-relevant signal within SUPT_0216 not assessed — see proposed experiments; the supertype is known from this graph's OLM-cell mapping to contain Sst+/Chrna2+ OLM cells and Sst+ HS cells as well as a possible Sst-dominant bistratified subpopulation.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (SUPT_0216) | Atlas metadata | PARTIAL | region_fraction_100um=0.153; strict=0.030 | atlas-internal |

**Supporting evidence**
- Sst is very high at SUPT_0216 (11.44, cohort_pct 0.968, full child-coverage), and Pvalb (1.48, cohort_pct 0.806) and Tac1 (0.55, cohort_pct 0.742) remain in the upper cohort range even at this Sst-dominant supertype — consistent with a Sst-leaning bistratified subpopulation co-expressing low Pvalb and modest Tac1.
- The supertype location footprint includes Field CA1 and CA1 stratum oriens, anatomically compatible with bistratified somata at the stratum pyramidale boundary.

**Concerns**
- Sst Gaba_3 contains at least three classical hippocampal types — OLM cells, bistratified cells, and HS cells — and they are not separable at the supertype level; a SUPT_0216 mapping for bistratified explicitly overlaps with the same supertype claimed by the OLM-cell mapping in this graph.
- Pvalb co-expression, defining for bistratified, drops by roughly a factor of five between SUPT_0206 (8.74) and SUPT_0216 (1.48). At the supertype mean, this is no longer the parvalbumin-bistratified signature, although a Sst-dominant Pvalb-low fraction within bistratified cells is biologically plausible.
- The child-cluster coverage modifier on Tac1 (0.667) shows the supertype-mean Tac1 is being driven by a subset of child clusters — a hidden-1:n signal that flags drilling to a child cluster rather than landing on the supertype.

**What would upgrade confidence**
- A Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq plus morphology dataset would test whether a Sst-dominant Pvalb-low bistratified subpopulation exists, and if so whether it maps specifically into SUPT_0216 (target: AnnotationTransferEvidence with F1 ≥ 0.50 at SUPERTYPE level).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | — | 650 | 🟡 MODERATE | Pvalb+Sst+Tac1 supertype; CA1 proximity | Primary (supertype) |
| 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] | 0206 Pvalb Gaba_2 | 170 | 🟡 MODERATE | Pvalb+Sst+Tac1 cluster; Que 2021 BIC AT target | Primary (cluster) |
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | 🔴 LOW | Sst-dominant; Pvalb low | Speculative Sst-dominant subpopulation |
| 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] | 0206 Pvalb Gaba_2 | 55 | ⚪ UNCERTAIN | Pvalb very high; Sst low (1.51) | Eliminated (PV-basket sibling) |
| 0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732] | 0204 Pvalb chandelier Gaba_1 | 309 | ⚪ UNCERTAIN | Sst APPROXIMATE; chandelier subclass | Eliminated (PV-chandelier subclass) |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | ⚪ UNCERTAIN | Tac1 APPROXIMATE (0.15); Sst very high | Eliminated (OLM-leaning Sst Gaba_3 child) |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | ⚪ UNCERTAIN | Tac1 APPROXIMATE; Pvalb 0.34 | Eliminated (Pvalb absent) |
| 0774 Sst Gaba_3 [CS20230722_CLUS_0774] | 0216 Sst Gaba_3 | 145 | ⚪ UNCERTAIN | Sst+Tac1 high; Pvalb 1.39 | Eliminated (sibling Sst Gaba_3 child) |
| 0791 Sst Gaba_6 [CS20230722_CLUS_0791] | 0219 Sst Gaba_6 | 100 | ⚪ UNCERTAIN | Tac1 high; Sst Gaba_6 subclass | Eliminated (wrong Sst subclass) |
| 0644 Vip Gaba_5 [CS20230722_CLUS_0644] | 0177 Vip Gaba_5 | 1039 | ⚪ UNCERTAIN | Sst APPROXIMATE; Vip subclass | Eliminated (Vip subclass) |
| 0649 Vip Gaba_7 [CS20230722_CLUS_0649] | 0179 Vip Gaba_7 | 409 | ⚪ UNCERTAIN | Pvalb APPROXIMATE; Vip subclass | Eliminated (Vip subclass) |
| 0650 Vip Gaba_7 [CS20230722_CLUS_0650] | 0179 Vip Gaba_7 | 504 | ⚪ UNCERTAIN | Pvalb APPROXIMATE; Vip subclass | Eliminated (Vip subclass) |
| 0212 Pvalb Gaba_8 [CS20230722_SUPT_0212] | — | 7777 | 🔴 REFUTED | Location DISCORDANT (Isocortex-dominant) | Eliminated (cortical subplate / isocortex) |
| 0196 RHP-COA Ndnf Gaba_4 [CS20230722_SUPT_0196] | — | 167 | ⚪ UNCERTAIN | Pvalb 0.48; CA3 enriched | Eliminated (CA3/RHP-COA Ndnf subclass) |
| 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | 725 | ⚪ UNCERTAIN | Sst Gaba_6 subclass; CA3 enriched | Eliminated (wrong Sst subclass) |
| 0189 Sncg Gaba_5 [CS20230722_SUPT_0189] | — | 1065 | ⚪ UNCERTAIN | Tac1 APPROXIMATE; Sncg subclass | Eliminated (Sncg subclass) |
| 0182 Vip Gaba_10 [CS20230722_SUPT_0182] | — | 140 | ⚪ UNCERTAIN | Pvalb APPROXIMATE; Vip subclass | Eliminated (Vip subclass) |
| 1196 Monocytes NN_1 [CS20230722_SUPT_1196] | — | 33 | 🔴 REFUTED | Non-neuronal; cerebellum/midbrain | Eliminated (non-neuronal monocyte) |
| 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] | — | 3470 | 🔴 REFUTED | Location DISCORDANT (Isocortex / olfactory) | Eliminated (PV-chandelier; cortical) |
| 0185 Sncg Gaba_1 [CS20230722_SUPT_0185] | — | 2256 | 🔴 REFUTED | Location DISCORDANT (Isocortex / olfactory) | Eliminated (Sncg subclass; cortical) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical bistratified cell as defined in this graph is a CLASSICAL_MULTIMODAL node: GABAergic [4], soma in pyramidal layer of CA1 [UBERON:0014548] with dendritic spread into CA1 stratum oriens [UBERON:0014552] and CA1 stratum radiatum [UBERON:0014554] [1], [2], [3], and defining markers Pvalb [5], [6], [7], [8] together with Sst and Tac1 [9]; Sst also functions as the canonical neuropeptide [9].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.** The annotation-transfer figure embedded above renders the Que 2021 morphology-confirmed PV-bistratified (BIC) source group against the WMBv1 (CCN20230722) taxonomy at class, subclass, supertype and cluster levels (run id `at_run_20260508_que2021_pvin_mmc_wmbv1`; figure sidecar at `figures/f1_for_bistratified_cell_hippocampus_metrics.json`). The structured annotation-transfer evidence record is not yet attached to the SUPT_0206 / CLUS_0737 edges in this graph — currently their evidence_items list only the ATLAS_METADATA observation; promoting the Que 2021 AT result from figure sidecar into a structured AnnotationTransferEvidence record on these edges is recommended (see open questions).

**Atlas data sources.** All atlas-side values are from the WMBv1 taxonomy reference store (`kb/taxonomy/CCN20230722/`).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Reproducibility footer.**

*Generated by evidencell `5738aa0` at 2026-06-08T05:47:20+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0732 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0774 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0791 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0644 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0649 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0650 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0212 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0196 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0189 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0182 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_1196 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0204 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0185 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Bistratified cell → 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] (within 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]) at MODERATE confidence. Key support: convergent Pvalb / Sst / Tac1 marker alignment plus a Que 2021 morphology-confirmed PV-bistratified annotation transfer that picks CLUS_0737 as its cluster-level target. Key caveats: PV-interneuron anatomical types are reported to be poorly separated in continuous transcriptomic space, so the cluster-level call rests on Sst / Tac1 cohort percentiles rather than Pvalb dominance, and the Que 2021 annotation transfer has not yet been replicated by an independent PV-bistratified scRNA-seq cohort.

CL:0004247 [[bistratified cell](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)] is the closest ancestor Cell Ontology term, but it is retinal-focused; the hippocampal Pvalb/Sst/Tac1+ bistratified interneuron with an SO+SR-targeting axon has no dedicated CL term, and a hippocampus-specific contribution to CL is warranted to capture this type cleanly.

### Proposed experiments and follow-ups

Annotation transfer with morphology-confirmed PV-bistratified cohorts has already been performed by Que 2021 (BIC source group, n=18 at supertype) and is the basis for the cluster-level call onto CLUS_0737. What remains:

- **Independent annotation-transfer replication (MapMyCells against WMBv1 CCN20230722).** Target: F1 ≥ 0.80 at CLUSTER level on CLUS_0737 from an independent PV-bistratified cohort (e.g. Pvalb-Cre × bistratified-morphology patch-seq or the Chamberland 2024 Sst::Tac1 intersectional dataset [9]). Expected output: a new AnnotationTransferEvidence on the CLUS_0737 edge. Resolves: open question 1 (replication).
- **Normalisation robustness check on GEO:GSE142546.** Target: re-run the Que 2021 → WMBv1 mapping under raw-counts vs TPM-pseudo-counts normalisation. Expected output: a robustness annotation on the existing CLUS_0737 AT evidence. Resolves: open question 2.
- **Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology.** Target: test whether a Sst-dominant Pvalb-low bistratified subpopulation exists and whether it maps specifically into SUPT_0216. Expected output: a new AnnotationTransferEvidence on the SUPT_0216 edge or, if no such subpopulation is recovered, refutation of the SUPT_0216 mapping. Resolves: open question 3.
- **Promote the Que 2021 BIC annotation transfer from the figure sidecar to a structured AnnotationTransferEvidence record** on the SUPT_0206 and CLUS_0737 edges, so the AT result participates in property-comparison scoring and downstream rationale checks. Expected output: AnnotationTransferEvidence with metrics_by_level matching the figure sidecar (`figures/f1_for_bistratified_cell_hippocampus_metrics.json`).

### Open questions

1. Replication of the Que 2021 PV-bistratified → CLUS_0737 annotation transfer with an independent morphology-confirmed scRNA-seq dataset.
2. Robustness of the CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts normalisation in GEO:GSE142546.
3. Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and if so does it map to SUPT_0216 specifically? Requires a Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq plus morphology dataset.
4. Whether SUPT_0206 provides morphologically informative substructure beyond the CLUS_0737 / CLUS_0739 bistratified/basket cluster-level split (appears on both SUPT_0206 and CLUS_0737 edges).

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland & Topolnik 2012 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426) | soma location |
| [2] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [4] | Dannenberg et al. 2017 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728) | neurotransmitter type |
| [5] | Ekins et al. 2020 | [33150866](https://pubmed.ncbi.nlm.nih.gov/33150866) | Pvalb marker |
| [6] | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922) | Pvalb marker |
| [7] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Pvalb marker |
| [8] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060) | Pvalb marker; PV-bistratified annotation transfer |
| [9] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347) | Sst, Tac1 markers; Sst neuropeptide |

---

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] SUPT_0206 (Pvalb Gaba_2) carries the
    Pvalb+Sst+Tac1 combination defining bistratified cells (Pvalb
    val=8.74 cohort_pct=0.968, Sst val=2.72 cohort_pct=0.774, Tac1
    val=5.36 cohort_pct=0.935; 3 of 3 markers CONSISTENT) but
    contains both PV-basket and PV-bistratified clusters and so is
    a broadMatch resolved at cluster level by
    CS20230722_CLUS_0737. Location is APPROXIMATE
    (region_fraction_100um: 0.160; strict region_fraction: 0.032).
  reconciliation_note: >
    Supertype-level call retained because PV-interneuron anatomical
    types are poorly separated in continuous transcriptomic space
    (Que 2021); the cluster-level CLUS_0737 mapping is the cleaner
    home for bistratified, and SUPT_0206 is the broader 1:n parent.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        SUPT_0206 contains both PV-basket cells (CS20230722_CLUS_0739)
        and PV-bistratified cells (CS20230722_CLUS_0737); not
        separable at supertype level.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Marker panel Pvalb+Sst+Tac1 is shared with PV-basket sibling
        cluster CS20230722_CLUS_0739 at the supertype mean
        (child-coverage 1.000 on all three markers).
  proposed_experiments:
    - Replicate the Que 2021 morphology-confirmed PV-bistratified
      annotation transfer with an independent Pvalb-Cre × bistratified
      morphology scRNA-seq cohort; target F1 ≥ 0.80 at CLUSTER level
      on CS20230722_CLUS_0737.
  unresolved_questions:
    - Whether SUPT_0206 provides morphologically informative
      substructure beyond the CS20230722_CLUS_0737 /
      CS20230722_CLUS_0739 bistratified/basket cluster-level split.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.70
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] CS20230722_CLUS_0737 (Pvalb Gaba_2) is the
    PV-bistratified cluster within SUPT_0206: 3 of 3 defining
    markers CONSISTENT (Pvalb val=8.27 cohort_pct=0.956, Sst
    val=4.39 cohort_pct=0.706, Tac1 val=7.26 cohort_pct=0.956) and
    a morphology-confirmed annotation transfer from a
    PV-bistratified scRNA-seq cohort (Que 2021) picks this cluster
    over PV-basket sibling CS20230722_CLUS_0739. Location is
    APPROXIMATE with CA1 / stratum oriens dominant
    (region_fraction_100um: 0.224; strict region_fraction: 0.040 —
    boundary scatter, not off-target).
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        A Sst-dominant Pvalb-low bistratified subpopulation may
        distribute toward CS20230722_SUPT_0216 (Sst Gaba_3);
        CS20230722_CLUS_0737 captures the PV-primary bistratified
        population only.
  proposed_experiments:
    - Independent annotation transfer of a morphology-confirmed
      PV-bistratified scRNA-seq cohort (e.g. Chamberland 2024 Sst::Tac1
      intersectional dataset) against WMBv1 CCN20230722; target
      F1 ≥ 0.80 at CLUSTER level on CS20230722_CLUS_0737.
    - Robustness check of the Que 2021 BIC → CS20230722_CLUS_0737
      mapping under raw-counts vs TPM-pseudo-count normalisation of
      GEO:GSE142546.
    - Promote the Que 2021 BIC annotation transfer from the figure
      sidecar to a structured AnnotationTransferEvidence record on
      this edge with metrics_by_level matching the sidecar.
  unresolved_questions:
    - Replication of Que 2021 BIC → CS20230722_CLUS_0737 with an
      independent morphologically confirmed PV-bistratified scRNA-seq
      dataset.
    - Robustness of CS20230722_CLUS_0737 assignment to raw-counts vs
      TPM-pseudo-counts normalisation in GEO:GSE142546.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:WEAKEST] CS20230722_SUPT_0216 (Sst Gaba_3) carries strong
    Sst (val=11.44 cohort_pct=0.968 child-coverage 1.000) and
    upper-cohort Pvalb (val=1.48 cohort_pct=0.806) and Tac1
    (val=0.55 cohort_pct=0.742 child-coverage 0.667), but the
    supertype contains OLM cells, HS cells and a possible
    Sst-dominant Pvalb-low bistratified subpopulation that are not
    separable at this level. Pvalb signal is ~5× weaker than at
    SUPT_0206, making the supertype-mean no longer a
    parvalbumin-bistratified signature. Location APPROXIMATE
    (region_fraction_100um: 0.153; strict region_fraction: 0.030).
  reconciliation_note: >
    Speculative Sst-dominant Pvalb-low bistratified subpopulation
    only; the parvalbumin-bistratified primary mapping lives at
    CS20230722_CLUS_0737 / CS20230722_SUPT_0206. Tac1 child-coverage
    0.667 is a hidden-1:n signal — drilling to a Sst Gaba_3 child
    cluster is required for a defensible call.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        SUPT_0216 (Sst Gaba_3) contains OLM, HS and possibly
        bistratified subpopulations; not separable at supertype level.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Pvalb (defining for bistratified) drops to val=1.48 at
        SUPT_0216 vs val=8.74 at SUPT_0206; supertype-mean does not
        carry the parvalbumin-bistratified signature.
  proposed_experiments:
    - Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq
      plus morphology dataset to test whether a Sst-dominant Pvalb-low
      bistratified subpopulation exists and whether it maps to
      CS20230722_SUPT_0216; target AnnotationTransferEvidence with
      F1 ≥ 0.50 at SUPERTYPE level.
  unresolved_questions:
    - Does a Sst-dominant Pvalb-low bistratified subpopulation exist,
      and if so does it map to CS20230722_SUPT_0216 specifically?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0739 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_CLUS_0739 (Pvalb Gaba_2) is the PV-basket
    sibling cluster of CS20230722_CLUS_0737 within SUPT_0206: Pvalb
    is even higher (val=10.63 cohort_pct=0.985) but Sst falls to
    val=1.51 (cohort_pct=0.618) — a PV-basket-leaning profile rather
    than the Pvalb+Sst+Tac1 bistratified signature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0732 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0732 sits in the Pvalb chandelier
    subclass (parent SUPT_0204 Pvalb chandelier Gaba_1); chandelier
    morphology is distinct from bistratified, and Sst is APPROXIMATE
    (val=0.97 cohort_pct=0.191).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0768 is a Sst Gaba_3 child where Tac1
    is APPROXIMATE (val=0.15 cohort_pct=0.338); the cluster is more
    consistent with OLM than bistratified, and the
    parvalbumin-bistratified primary mapping lives at
    CS20230722_CLUS_0737.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_CLUS_0772 (Sst Gaba_3) shows Pvalb absent
    (val=0.34 cohort_pct=0.529) and Tac1 APPROXIMATE (val=0.14
    cohort_pct=0.265); incompatible with the Pvalb+Sst+Tac1
    bistratified signature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0774 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_CLUS_0774 (Sst Gaba_3) carries Sst
    (val=12.11 cohort_pct=0.971) and Tac1 (val=2.65 cohort_pct=0.897)
    but Pvalb is low (val=1.39 cohort_pct=0.838); the
    parvalbumin-bistratified primary mapping is at
    CS20230722_CLUS_0737, and this sibling within Sst Gaba_3 is
    captured by the broader SUPT_0216 speculative reading.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0791 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0791 sits in the Sst Gaba_6 subclass
    (parent SUPT_0219); wrong Sst subclass for hippocampal
    bistratified, despite high Tac1 (val=8.27 cohort_pct=0.985).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0644 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0644 sits in the Vip Gaba_5 subclass;
    Vip-expressing interneurons are interneuron-selective, not
    bistratified, and Sst (val=0.84 cohort_pct=0.118) and Tac1
    (val=0.20 cohort_pct=0.485) are APPROXIMATE.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0649 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0649 sits in the Vip Gaba_7 subclass;
    Pvalb (val=0.12 cohort_pct=0.265) and Sst (val=1.16 cohort_pct=0.324)
    are APPROXIMATE; Vip-subclass identity is incompatible with
    bistratified.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0650 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0650 sits in the Vip Gaba_7 subclass;
    Pvalb (val=0.10 cohort_pct=0.235) and Sst (val=1.26
    cohort_pct=0.441) APPROXIMATE; Vip-subclass identity is
    incompatible with bistratified.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0212 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0212 (Pvalb Gaba_8) has location
    DISCORDANT (region_fraction_100um: 0.019; strict
    region_fraction: 0.002); dominant footprint is Isocortex, not
    hippocampus, despite Pvalb+Sst+Tac1 CONSISTENT.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT location (Isocortex-dominant footprint, hippocampal
        formation a minority) refutes a hippocampal bistratified
        mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0196 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0196 (RHP-COA Ndnf Gaba_4) is an
    Ndnf-subclass type centred on CA3 / RHP-COA, not the CA1
    Pvalb-bistratified profile; Pvalb (val=0.48 cohort_pct=0.548)
    is low.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0219 sits in the Sst Gaba_6 subclass
    (CA3 / DG-leaning footprint); wrong Sst subclass for hippocampal
    bistratified, and Pvalb (val=1.68 cohort_pct=0.839) is the
    supertype-mean, not the parvalbumin-bistratified signature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0189 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0189 sits in the Sncg subclass; Sncg
    is a Vip-related interneuron-selective subclass, not bistratified,
    and Tac1 (val=0.13 cohort_pct=0.355) is APPROXIMATE.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0182 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0182 sits in the Vip Gaba_10 subclass;
    Pvalb (val=0.13 cohort_pct=0.226) and Tac1 (val=0.16
    cohort_pct=0.452) are APPROXIMATE; Vip-subclass identity is
    incompatible with bistratified.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_1196 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.01
  rationale: >
    [tier:CUT] CS20230722_SUPT_1196 (Monocytes NN_1) is a
    non-neuronal monocyte supertype with location DISCORDANT
    (Isocortex / Cerebellum / Midbrain footprint;
    region_fraction_100um: 0.017); cannot be a hippocampal
    interneuron.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Non-neuronal monocyte supertype; DISCORDANT location refutes
        any interneuron mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0204 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0204 (Pvalb chandelier Gaba_1) is the
    PV-chandelier subclass with location DISCORDANT
    (region_fraction_100um: 0.067; Isocortex / olfactory areas
    dominant); chandelier morphology is distinct from bistratified.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT location (cortical footprint) and PV-chandelier
        subclass refute a hippocampal bistratified mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0185 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0185 (Sncg Gaba_1) is a Sncg subclass
    type with location DISCORDANT (region_fraction_100um: 0.023;
    Isocortex / olfactory areas dominant); Sncg subclass and cortical
    footprint refute a hippocampal bistratified mapping.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT location (cortical footprint) and Sncg subclass
        refute a hippocampal bistratified mapping.
```
<!-- verdict-block-end -->
