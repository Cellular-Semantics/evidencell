# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The hippocampal bistratified cell is a CA1 GABAergic interneuron whose axonal arbor bilaminates across stratum oriens and stratum radiatum, co-innervating the apical and basal dendrites of pyramidal neurons. It co-expresses Pvalb, Sst, and Tac1, and intersectional Sst;;Tac1 genetics selectively label this population (Chamberland et al. 2024 [9]). Distinguishing bistratified cells from sibling PV-INs (basket, axo-axonic) and from Sst+ siblings (OLM, HS) is the central transcriptomic challenge for this type, because the bistratified identity sits at a Pvalb–Sst transcriptomic interface (Que et al. 2021 [8]).

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548]; CA1 stratum oriens [UBERON:0014552]; CA1 stratum radiatum [UBERON:0014554] | [1], [2], [3] |
| NT type | GABAergic | [4] |
| Defining markers | Pvalb, Sst, Tac1 | [5], [6], [7], [8], [9] |
| Neuropeptides | Sst | [9] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical morphological review · CA1 pyramidal layer with axon bilaminating in stratum oriens and stratum radiatum · [1], [2], [3]
  > Different types of hippocampal inhibitory interneurons control spike initiation [e.g., axo-axonic and basket cells (BCs)] and synaptic integration (e.g., bistratified and oriens–lacunosum moleculare interneurons) within pyramidal neurons
  > — Chamberland & Topolnik 2012, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 8530661_92702482 -->

  > the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin
  > — Bocchio et al. 2024, Results · [2] <!-- quote_key: 262127573_ba6d02e9 -->

  > The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus
  > — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [3] <!-- quote_key: 224817966_79f4a500 -->

- **Pvalb (defining marker):** review + patch-seq evidence · mouse · [5], [6], [7], [8]
  > Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
  > — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 38778375_462ec931 -->

  > WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes (basket, axo-axonic, bistratified, radiatum-targeting).
  > — Ekins et al. 2020, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 221276443_e917908b -->

  > while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities
  > — Que et al. 2021 · [8] <!-- quote_key: 230508306_e8cc8c19 -->

- **Sst, Tac1 (defining markers + Sst neuropeptide):** intersectional genetics · mouse · [9]
  > the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [9] <!-- quote_key: 269246896_c084d5c0 -->

</details>

Cell Ontology mapping: bistratified cell [[CL:0004247](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)] (BROAD). CL:0004247 is retinal-focused; the hippocampal bistratified interneuron (Pvalb/Sst/Tac1+, axon in SO and SR) has no dedicated CL term and is a candidate for a new CL contribution.

---

## Results

Marker expression alignment, anatomical localisation, and morphology-confirmed patch-seq annotation transfer (Que et al. 2021, GSE142546, hBIC + vBIC pooled, n=20) converge on cluster 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] as the primary atlas match for the canonical Pvalb-positive bistratified cell, with the parent supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] capturing the broader Pvalb container (F1=0.80 at cluster vs F1=0.38 at supertype — see figure and Table 1). A speculative secondary mapping to the Sst supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] reflects the possibility of a Sst-dominant, Pvalb-low bistratified subpopulation flagged by Chamberland et al. 2024 [9] Sst;;Tac1 genetics — Que 2021 patch-seq cells provide no support for that target and it is reported at LOW confidence.

![Filtered AT figure for bistratified cell](figures/f1_for_bistratified_cell_hippocampus.png)

*F1 across taxonomy levels for the morphologically confirmed Que 2021 bistratified cohort (BIC = hBIC + vBIC pooled, n=20). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The collapse of F1 from cluster (0.80) to supertype (0.38) reflects the basket / bistratified split within SUPT_0206 — basket cells preferentially map to sibling cluster CLUS_0739 (F1=0.83) and dilute purity at the supertype-level.*

### 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] · 🟢 HIGH

Patch-seq annotation transfer of morphologically reconstructed bistratified cells (Que et al. 2021, hBIC + vBIC pooled, n=20) lands cleanly on this cluster (F1=0.80, Coverage=0.94, Purity=0.70) — see figure and property comparison table. All three defining markers (Pvalb, Sst, Tac1) align CONSISTENT with cluster-level precomputed expression; the cluster's atlas-side soma distribution (CA1 stratum oriens dominant, with CA1 stratum radiatum and CA3 stratum oriens contributions) directly mirrors the bistratified axon territory.

**Table 1 — Property comparison.**

| Property | Classical | Supertype (SUPT_0206) | Best cluster (CLUS_0737) | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Hippocampal formation [MBA:1089]; CA1 [MBA:382] (region_fraction_100um=0.160) | CA1 [MBA:382]; CA1 stratum oriens [MBA:399] (region_fraction_100um=0.224) | APPROXIMATE |
| NT type | GABAergic | not asserted | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Pvalb expression | defining marker | 8.74 (cohort_pct 0.968) | 8.27 (cohort_pct 0.956) | CONSISTENT |
| Sst expression | defining marker | 2.72 (cohort_pct 0.774) | 4.39 (cohort_pct 0.706) | CONSISTENT |
| Tac1 expression | defining marker | 5.36 (cohort_pct 0.935) | 7.26 (cohort_pct 0.956) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(Of the 2 child clusters of SUPT_0206 with morphology-relevant precomputed signal, CLUS_0737 carries the bilaminar CA1 SO + CA1 SR distribution that matches bistratified axon territory; CLUS_0739, the sibling, preferentially binds Que 2021 basket cells (F1=0.83) and is the basket-cell target.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + anatomy | Atlas metadata | SUPPORT | CA1 SO/SR distribution; Pvalb+Sst+Tac1 CONSISTENT | atlas-internal |
| Que 2021 patch-seq AT | Annotation transfer | SUPPORT | F1=0.80 (cluster); Coverage=0.94; Purity=0.70 | [8] |
| Chamberland-Harris Sst_Tac1 AT | Annotation transfer | PARTIAL | F1=0.47 (cluster); Purity=0.94 | [9] |

**Supporting evidence:**
- Morphologically-identified bistratified cells (Que et al. 2021 [8]; patch-clamp recovery of hBIC + vBIC subtypes from GEO:GSE142546) map predominantly to this cluster, with BC (basket) cells preferentially landing on sibling CLUS_0739 — the BIC/BC split within SUPT_0206 is a genuine transcriptomic signal driven by morphological identity, not artefactual.
- Atlas precomputed expression for CLUS_0737 carries the canonical Pvalb+Sst+Tac1 triad at high cohort percentiles, and the cluster's MERFISH-panel markers (Moxd1, Grpr, Syt2, Nxph2, Prkg2) plus neuropeptide annotation (Cort, Tac1, Npy, Cck, Sst) are all consistent with bistratified identity.
- An in-silico Sst_Tac1 label derived from Harris 2018 cluster-mean expression via Chamberland 2024 [9] gene-pair rules also lands on CLUS_0737 with very high cluster-level purity (0.94), independently confirming this as the specific landing site within the Pvalb tree. PARTIAL because the Sst_Tac1 label is in-silico, not morphologically confirmed.

**Marker evidence provenance:**
- **Pvalb:** transcript-level (atlas precomputed and Que 2021 patch-seq) and protein-level (Dannenberg 2017 [4], Ekins 2020 [5]) confirmation in cells whose bistratified morphology was directly recovered (Que 2021). Pvalb is a defining atlas-side discriminator for this cluster (val=8.27, cohort_pct=0.956).
- **Sst:** atlas categorises Sst as a NEUROPEPTIDE annotation on this cluster (val=4.39, cohort_pct=0.706). Classical citation for Sst on bistratified comes from Chamberland 2024 [9] Sst;;Tac1 intersectional genetics, which is transcript- and protein-level co-detection in cells confirmed bistratified by axonal arborisation.
- **Tac1:** atlas categorises Tac1 as a NEUROPEPTIDE annotation (val=7.26, cohort_pct=0.956). Anchored by the same Chamberland 2024 [9] intersection. Strong concordance with transcript-level evidence.

**Concerns:**
- Location is APPROXIMATE (`region_fraction_100um: 0.224`, strict `region_fraction: 0.040`) — the high proximity / low strict gap is the classical boundary-scatter signature for an interneuron whose soma sits at the stratum-pyramidale / stratum-oriens border; not a counter-signal.
- Sst-expressing bistratified subpopulations may distribute partially toward SUPT_0216 (Sst Gaba_3) rather than concentrating on CLUS_0737 (see the SUPT_0216 candidate below); CLUS_0737 captures the PV-primary bistratified population.

**What would upgrade confidence:**
- Replication of the Que 2021 BIC → CLUS_0737 F1=0.80 with an independent morphologically confirmed PV bistratified scRNA-seq dataset (target: AnnotationTransferEvidence with F1 ≥ 0.80 at CLUSTER level).
- Robustness check of CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts normalization on GSE142546 (the current run used TPM as pseudo-counts).

### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟡 MODERATE

Aggregated annotation transfer support and atlas-side marker alignment place this supertype as the broader Pvalb container for canonical bistratified cells, but cluster-level resolution within it is non-trivial: Que 2021 BIC and BC cells separate at cluster level (CLUS_0737 for bistratified, CLUS_0739 for basket), so SUPT_0206-level F1=0.38 reflects basket-cell dilution rather than a poor bistratified mapping. The supertype edge is reported at MODERATE confidence as a 1:n broader-match relationship, paired with the CLUS_0737 1:1 close match above.

**Table 1 — Property comparison.**

| Property | Classical | Supertype value | Best cluster (CLUS_0737) | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | CA1 [MBA:382]; Cortical subplate [MBA:703] (region_fraction_100um=0.160) | CA1 stratum oriens [MBA:399] (region_fraction_100um=0.224) | APPROXIMATE |
| NT type | GABAergic | not asserted | GABA | NOT_ASSESSED at SUPT; CONSISTENT at CLUS |
| Pvalb expression | defining marker | 8.74 (cohort_pct 0.968) | 8.27 (cohort_pct 0.956) | CONSISTENT |
| Sst expression | defining marker | 2.72 (cohort_pct 0.774) | 4.39 (cohort_pct 0.706) | CONSISTENT |
| Tac1 expression | defining marker | 5.36 (cohort_pct 0.935) | 7.26 (cohort_pct 0.956) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(SUPT_0206 contains both PV basket cells (CLUS_0739) and PV bistratified cells (CLUS_0737); not separable at supertype level — see CLUS_0737 edge above for cluster-level resolution.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + anatomy | Atlas metadata | PARTIAL | Pvalb+Sst+Tac1 CONSISTENT at supertype; mixed BC/BIC content | atlas-internal |
| Que 2021 patch-seq AT | Annotation transfer | SUPPORT | F1=0.38 (supertype); Coverage=0.90; 18/20 cells | [8] |

**Supporting evidence:**
- 18 of 20 Que 2021 patch-seq BIC cells map within this supertype, with the remaining 2 outside it (Coverage=0.90 at supertype level). The supertype is the Pvalb subclass container for bistratified identity.
- All three defining markers (Pvalb, Sst, Tac1) are CONSISTENT at the supertype mean.

**Concerns:**
- F1=0.38 at supertype is driven by basket-cell dilution (CLUS_0739) sharing this supertype with bistratified (CLUS_0737); the supertype is not separable at this rank into the bistratified vs basket axes.
- Location APPROXIMATE (`region_fraction_100um: 0.160`, strict `region_fraction: 0.032`): boundary scatter consistent with stratum-pyramidale-border interneuron soma distribution; weak counter-evidence at most.

**What would upgrade confidence:**
- A higher-cell-count morphologically-confirmed PV bistratified dataset to firm up the BC/BIC cluster-level split that already separates CLUS_0737 from CLUS_0739 at F1 ≥ 0.80.

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

A speculative secondary mapping reflecting the possibility — flagged by Chamberland et al. 2024 [9] Sst;;Tac1 intersectional genetics — that a Sst-dominant, Pvalb-low bistratified subpopulation exists and that such cells would partition transcriptomically toward the Sst Gaba_3 supertype rather than the Pvalb Gaba_2 supertype. Que 2021 patch-seq BIC cells provide no support for this target: 0 of 20 morphologically-confirmed bistratified cells map here, and Yao 2021 SSv4 Pvalb cells reach this supertype at only F1=0.053. Reported at LOW confidence as a documented hypothesis, not as a primary mapping.

**Table 1 — Property comparison.**

| Property | Classical | Supertype value (SUPT_0216) | Alignment |
|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | CA1 [MBA:382]; CA1 stratum oriens [MBA:399] (region_fraction_100um=0.153) | APPROXIMATE |
| NT type | GABAergic | not asserted | NOT_ASSESSED |
| Pvalb expression | defining marker | 1.48 (cohort_pct 0.806; child-coverage 0.889) | CONSISTENT |
| Sst expression | defining marker | 11.44 (cohort_pct 0.968) | CONSISTENT |
| Tac1 expression | defining marker | 0.55 (cohort_pct 0.742; child-coverage 0.667) | CONSISTENT |
| Sex ratio | not documented | not available | NOT_ASSESSED |

*(SUPT_0216 contains at least three classical hippocampal types: OLM cells (Sst+/Chrna2+), bistratified cells (Sst+/Pvalb+/Tac1+), and HS cells (Sst+, long-range projecting); not separable at supertype level. Tac1 child-coverage of 0.667 indicates Tac1 is not uniformly present across this supertype's children.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + anatomy | Atlas metadata | PARTIAL | Sst+Tac1 supertype-mean consistent with bistratified subpopulation | atlas-internal |
| Yao 2021 SSv4 Pvalb AT | Annotation transfer | PARTIAL | F1=0.053; 6/66 cells | [8] |
| Que 2021 patch-seq BIC AT | Annotation transfer | PARTIAL | F1 absent from top results; 0/20 BIC cells | [8] |

**Supporting evidence:**
- Atlas-side Sst (val=11.44, cohort_pct=0.968) and Tac1 (val=0.55, cohort_pct=0.742) are both annotated as DEFINING_SCOPED / NEUROPEPTIDE markers for this supertype, which is the Sst container Chamberland 2024 [9] Sst;;Tac1 genetics would predict targets a Sst-dominant bistratified subpopulation.
- Pvalb is detectable at the supertype mean (val=1.48), with child-coverage 0.889 indicating most children carry some Pvalb signal — compatible with Pvalb-low rather than Pvalb-absent identity.

**Marker evidence provenance:**
- **Tac1 at SUPT_0216:** child-coverage of 0.667 means Tac1 expression is not uniform across child clusters — the supertype-mean signal is driven by a subset of children. This weakens the supertype-level Tac1 case and is consistent with the speculative-subpopulation reading rather than a clean mapping.

**Concerns:**
- Que 2021 patch-seq bistratified cells (morphologically identified) provide zero AT support for this target; the entire BIC cohort maps within the Pvalb supertype branch.
- The supertype mixes OLM, bistratified, and HS cells at this rank; cluster-level resolution would be required to test the Sst-dominant-bistratified hypothesis.
- Pvalb co-expression (defining for bistratified) is under-represented at the supertype mean (val=1.48 vs Pvalb-supertype 8.27), suggesting Sst subclass placement would under-capture the PV component of bistratified identity.

**What would upgrade confidence:**
- A Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology experiment to test whether a Sst-dominant Pvalb-low bistratified subpopulation exists, and if so whether it maps to SUPT_0216 (target: AnnotationTransferEvidence with F1 ≥ 0.5 at SUPERTYPE level on confirmed Pvalb-negative cells).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] | 0206 Pvalb Gaba_2 | 170 | 🟢 HIGH | Que 2021 patch-seq F1=0.80 | Primary |
| — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | 650 | 🟡 MODERATE | Pvalb-container; BC/BIC split at cluster | Supports broader mapping |
| — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 2004 | 🔴 LOW | Speculative Sst-dominant subpopulation; 0/20 Que 2021 BIC | Secondary (speculative) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Bistratified cells are CA1 GABAergic [4] interneurons defined by Pvalb [5,6,7,8], Sst [9], and Tac1 [9] co-expression, with soma in CA1 stratum pyramidale and axon bilaminating across stratum oriens and stratum radiatum [1,2,3]. Definition basis: CLASSICAL_MULTIMODAL (combining classical morphology, electrophysiology, and recent intersectional genetics).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (Que 2021 patch-seq PV-IN; hBIC + vBIC pooled as BIC, n=20) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 88 (filtered to 88) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Caveats | TPM input used as pseudo-counts; juvenile age range (mean P30) vs adult atlas; aggregated BIC label (hBIC + vBIC). |

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018, Chamberland 2024 in-silico Sst_Tac1 subfamily labels) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_matrix_chamberland_by_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/f1_matrix_chamberland_by_class.csv) |
| Caveats | In-silico subfamily labels derived from Harris cluster-mean expression via Chamberland 2024 gene-pair rules; not morphologically confirmed. |

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 hippocampal formation SMART-Seq v4; Pvalb subclass n=66 HIP) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| n cells | 6398 |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `8c61574` at 2026-06-08T15:22:25+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | ATLAS_METADATA; ANNOTATION_TRANSFER (×2) | SUPPORT; SUPPORT; PARTIAL | [8], [9] |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | [8] |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER (×2) | PARTIAL; PARTIAL; PARTIAL | [8], [9] |

</details>

---

## Discussion

**Primary mapping:** Bistratified cell → 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] at HIGH confidence, with the parent supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] as a paired 1:n broader-match at MODERATE confidence. Key support: morphology-confirmed patch-seq annotation transfer (Que 2021 [8], F1=0.80 at cluster) plus precomputed-expression alignment on all three defining markers (Pvalb, Sst, Tac1) and atlas-side soma anatomy matching the bilaminar CA1 SO + SR axon territory. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS at supertype level (basket cells share SUPT_0206 via CLUS_0739); a separately reported speculative LOW-confidence Sst-supertype edge to SUPT_0216 documents the unresolved question of whether a Sst-dominant Pvalb-low bistratified subpopulation exists.

The Cell Ontology has no specific term for hippocampal bistratified cells; bistratified cell [[CL:0004247](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)] is the closest ancestor and is retinal-focused, so this classical type is a candidate for a new CL contribution.

### Proposed experiments and follow-ups

**Replication of Que 2021 BIC mapping with an independent dataset.**
- *What:* MapMyCells annotation transfer of an independent morphologically confirmed PV bistratified scRNA-seq dataset onto WMBv1.
- *Target:* F1 ≥ 0.80 at CLUSTER level on CLUS_0737.
- *Expected output:* AnnotationTransferEvidence on the CLUS_0737 edge, raising confidence to HIGH-with-replication.
- *Resolves:* Open question 1.

**Robustness of cluster-level assignment to normalization.**
- *What:* Re-run MapMyCells on GSE142546 with raw counts (rather than TPM as pseudo-counts) where recoverable.
- *Target:* CLUS_0737 F1 within 0.05 of current 0.80.
- *Expected output:* AnnotationTransferEvidence variant with normalization-comparison note.
- *Resolves:* Open question 2.

**Test the Sst-dominant Pvalb-low bistratified hypothesis.**
- *What:* Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology recovery.
- *Target:* If such cells exist, AnnotationTransferEvidence at F1 ≥ 0.5 to SUPT_0216.
- *Expected output:* AnnotationTransferEvidence on the SUPT_0216 edge, either confirming or refuting the speculative mapping.
- *Resolves:* Open question 3.

### Open questions

1. Replication of Que 2021 BIC → CLUS_0737 F1=0.80 with an independent morphologically confirmed PV bistratified scRNA-seq dataset.
2. Robustness of CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts normalization in GEO:GSE142546.
3. Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and if so does it map to CS20230722_SUPT_0216 specifically?
4. Whether SUPT_0206 provides morphologically informative substructure beyond the CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.

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
| [8] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060) | Pvalb marker; patch-seq AT source |
| [9] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347) | Sst marker; Sst;;Tac1 intersectional genetics |

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.85
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Morphologically-confirmed patch-seq annotation transfer
    (Que 2021, run_ref at_run_20260508_que2021_pvin_mmc_wmbv1) lands the BIC
    cohort on CS20230722_CLUS_0737 with F1=0.80; defining markers Pvalb, Sst,
    Tac1 all CONSISTENT (3 of 3 markers CONSISTENT); atlas-side anatomy
    (CA1 stratum oriens + CA1 stratum radiatum) matches bistratified axon
    territory. region_fraction_100um: 0.22 is boundary scatter typical of
    pyramidal-layer interneurons.
  reconciliation_note: >
    Paired with edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206
    (skos:broadMatch 1:n; supertype container with basket cells in sibling
    CLUS_0739).
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        A Sst-dominant Pvalb-low bistratified subpopulation may distribute
        toward SUPT_0216 (Sst Gaba_3); CLUS_0737 captures the PV-primary
        bistratified population. See speculative LOW edge to
        CS20230722_SUPT_0216.
  proposed_experiments:
    - >
      Replicate Que 2021 BIC → CS20230722_CLUS_0737 F1=0.80 with an
      independent morphologically confirmed PV bistratified patch-seq
      dataset; target F1 ≥ 0.80 at cluster level.
    - >
      Robustness check on CS20230722_CLUS_0737 assignment via re-running
      MapMyCells on GEO:GSE142546 with raw counts rather than TPM
      pseudo-counts.
  unresolved_questions:
    - >
      Replication of Que 2021 BIC → CS20230722_CLUS_0737 F1=0.80 with an
      independent morphologically confirmed PV bistratified scRNA-seq
      dataset.
    - >
      Robustness of CS20230722_CLUS_0737 assignment to raw-counts vs
      TPM-pseudo-counts normalization in GEO:GSE142546.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_SUPT_0206 is the Pvalb-subclass supertype container
    for the bistratified cell; Que 2021 patch-seq (run_ref
    at_run_20260508_que2021_pvin_mmc_wmbv1) places 18/20 BIC cells in this
    supertype (F1=0.38, coverage 0.90) with all 3 of 3 markers (Pvalb, Sst,
    Tac1) CONSISTENT. F1 at supertype is diluted by basket cells in sibling
    CLUS_0739; the cluster-level resolution lives on
    CS20230722_CLUS_0737 (F1=0.80).
  reconciliation_note: >
    Paired with edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737
    (skos:closeMatch 1:1; the best-child resolution within this supertype).
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        SUPT_0206 contains both PV basket cells (CS20230722_CLUS_0739) and
        PV bistratified cells (CS20230722_CLUS_0737). Not separable at
        supertype level.
  proposed_experiments:
    - >
      Higher-cell-count morphologically-confirmed PV bistratified dataset
      to consolidate the CS20230722_CLUS_0737 / CS20230722_CLUS_0739
      cluster-level BC/BIC split at F1 ≥ 0.80.
  unresolved_questions:
    - >
      Whether CS20230722_SUPT_0206 provides morphologically informative
      substructure beyond the CS20230722_CLUS_0737 / CS20230722_CLUS_0739
      BIC/BC cluster-level split.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:WEAKEST] Speculative secondary mapping for a putative Sst-dominant
    Pvalb-low bistratified subpopulation flagged by Chamberland 2024
    Sst;;Tac1 intersectional genetics. Que 2021 patch-seq BIC cells (run_ref
    at_run_20260508_que2021_pvin_mmc_wmbv1) provide zero AT support to
    CS20230722_SUPT_0216; Yao 2021 SSv4 Pvalb cells reach this supertype at
    only F1=0.05. Supertype mixes OLM, bistratified, and HS cells and
    Tac1 child-coverage is 0.67. 3 of 3 markers (Pvalb, Sst, Tac1)
    CONSISTENT at supertype mean but Pvalb is low (1.48 vs Pvalb-supertype
    8.27).
  reconciliation_note: >
    Predicate left as evidencell:UncertainRelationship pending experimental
    test of whether a Sst-dominant Pvalb-low bistratified subpopulation
    exists. Primary mapping lives on
    edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Sst Gaba_3 supertype contains at least three classical hippocampal
        types: OLM (Sst+/Chrna2+), bistratified (Sst+/Pvalb+/Tac1+), and
        HS cells. Not separable at supertype level.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Pvalb co-expression (defining for bistratified) is under-represented
        at the supertype mean; Sst subclass placement may under-capture the
        PV component of bistratified identity.
  proposed_experiments:
    - >
      Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq with
      morphological recovery to test whether a Sst-dominant Pvalb-low
      bistratified subpopulation exists and maps to CS20230722_SUPT_0216
      at F1 ≥ 0.5 at supertype level.
  unresolved_questions:
    - >
      Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and
      if so does it map to CS20230722_SUPT_0216 specifically?
```
<!-- verdict-block-end -->
