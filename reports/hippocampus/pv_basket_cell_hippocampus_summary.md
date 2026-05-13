# Parvalbumin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Parvalbumin-positive (PV+) basket cells are fast-spiking GABAergic interneurons of the hippocampal formation whose axons innervate the somata and proximal axons of pyramidal cells, providing the perisomatic inhibition that paces network oscillations [1][2]. Mapping this classical type to a Whole Mouse Brain v1 (WMBv1) transcriptomic cluster matters because PV+ interneurons in the hippocampus comprise several morphological subtypes (basket, axo-axonic, bistratified) with high transcriptomic similarity, and establishing which atlas type contains the basket population — versus chandelier or bistratified cells — is a prerequisite for any downstream PV-IN circuit work.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548]; pyramidal layer of CA3 [UBERON:0014550]; dentate gyrus granule cell layer [UBERON:0005381] | [1][2][3][4] |
| Neurotransmitter | GABAergic | [5] |
| Defining markers | Pvalb [1][6][7][8]; Gad1; Gad2 | [1][6][7][8] |
| Negative markers | Cnr1 | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |
| CL term | basket cell [CL:0000118] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / morphology:** classical anatomical and electrophysiological description (rat hippocampus, biocytin fills + immunohistochemistry) · [2]
  > Fast spiking interneurons in the CA1 area of the dorsal hippocampus were recorded from and filled with biocytin in anesthetized rats. The full extent of their dendrites and axonal arborizations as well as their calcium binding protein content were examined. Based on the spatial extent of axon collaterals, local circuit cells (basket and O- LM neurons) and long-range cells (bistratified, trilaminar, and backprojection neurons) could be distinguished. Basket cells were immunoreactive for parvalbumin and their axon collaterals were confined to the pyramidal layer. A single basket cell contacted more than 1500 pyramidal neurons and 60 other parvalbumin-positive interneurons. Commissural stimulation directly discharged basket cells, followed by an early and late IPSPs, indicating interneuronal inhibition of basket cells. The dendrites of another local circuit neuron (O-LM) were confined to stratum oriens and it had a small but high-density axonal terminal field in stratum lacunosum-moleculare. The fastest firing cell of all interneurons was a calbindin-immunoreactive bistratified neuron with axonal targets in stratum oriens and radiatum. Two neurons with their cell bodies in the alveus innervated the CA3 region (backprojection cells), in addition to rich axon collaterals in the CA1 region. The trilaminar interneuron had axon collaterals in strata radiatum, oriens and pyramidale with its dendrites confined to stratum oriens. Commissural stimulation evoked an early EPSP-IPSP-late depolarizing potential sequence in this cell. All interneurons formed symmetric synapses with their targets at the electron microscopic level. These findings indicate that interneurons with distinct axonal targets have differential functions in shaping the physiological patterns of the CA1 network.
  > — Sik et al. 1995, Anatomical Location and Morphology · [2] <!-- quote_key: 10664418_9acd7ec1 -->
- **Anatomical distribution / Pvalb marker:** rat hippocampus immunolocalisation · [1]
  > Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)
  > — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->
- **GABAergic identity / PV–CCK relationship:** intersectional genetic mapping of CCK- and PV-GABA cells across forebrain · [5]
  > Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus. As CCK- and PV-GABA neurons differ in an array of morphological, biochemical and electrophysiological features, it has been proposed that they form distinct inhibitory ensembles which differentially contribute to network oscillations and behavior. However, the relationship and balance between CCK- and PV-GABA neurons in the inhibitory networks of the brain is currently unclear as the distribution of these cells has never been compared on a large scale. Here, we systemically investigated the distribution of CCK- and PV-GABA cells across a wide number of discrete forebrain regions using an intersectional genetic approach. Our analysis revealed several novel trends in the distribution of these cells. While PV-GABA cells were more abundant overall, CCK-GABA cells outnumbered PV-GABA cells in several subregions of the hippocampus, medial prefrontal cortex and ventrolateral temporal cortex. Interestingly, CCK-GABA cells were relatively more abundant in secondary/ association areas of the cortex (V2, S2, M2, and AudD/AudV) than they were in corresponding primary areas (V1, S1, M1, and Aud1). The reverse trend was observed for PV-GABA cells. Our findings suggest that the balance between CCK- and PV-GABA cells in a given cortical region is related to the type of processing that area performs; inhibitory networks in the secondary cortex tend to favor the inclusion of CCK-GABA cells more than networks in the primary cortex. The intersectional genetic labeling approach employed in the current study expands upon the ability to study molecularly defined subsets of GABAergic neurons. This technique can be applied to the investigation of neuropathologies which involve disruptions to the GABAergic system, including schizophrenia, stress, maternal immune activation and autism.
  > — Whissell et al. 2015, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 16859318_009e9f36 -->
- **Pvalb perisomatic-interneuron framing:** [8]
  > the majority of interneurons in these regions express either the neuropeptide cholecystokinin or the calcium binding protein parvalbumin
  > — Contreras et al. 2019, SOMA AND AXON TARGETING INTERNEURONS · [8] <!-- quote_key: 195584607_37a80af5 -->
- **Representativeness of PV basket within hippocampal IN repertoire:** [4]
  > the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin
  > — Bocchio et al. 2024, Results · [4] <!-- quote_key: 262127573_ba6d02e9 -->

</details>

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD). CL:0000118 covers perisomatic-targeting GABAergic interneurons but does not capture PV-specific identity; no hippocampus-specific PV basket cell term exists in CL.

---

## Results

Two candidate atlas entries were assessed (supertype SUPT_0206 and its child cluster CLUS_0739), both at HIGH confidence with PARTIAL_OVERLAP relationship: SUPT_0206 contains the PV+ Gaba_2 population and CLUS_0739 is the basket-preferring cluster within that supertype, distinct from the bistratified-preferring CLUS_0737.

**Annotation-transfer overview (node-scoped, filtered).**

![Filtered AT figure (Que 2021 PV basket cells, BC source group)](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/figures/f1_for_pv_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the BC (basket cell) source group relevant to the PV basket cell mapping. The BC row aggregates Que et al. 2021 patch-seq morphology-confirmed hippocampal basket cells (horizontal + vertical BC, n=62) — morphology was verified by patch-clamp + biocytin fill, so this row is the strongest single AT signal for the basket subtype. F1 ≥ 0.5 at a level indicates a clean mapping; SUPT_0206 (Pvalb Gaba_2) reaches F1=0.785 and CLUS_0739 reaches F1=0.827.*

![Filtered AT figure (Yao 2021 Pvalb subclass)](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_pv_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 SSv4 Pvalb subclass source group (n=66 hippocampal Pvalb cells). The SSv4 Pvalb label aggregates basket, axo-axonic and bistratified PV cells, so the signal splits between Pvalb chandelier (SUPT_0204, F1=0.612) and Pvalb Gaba_2 (SUPT_0206, F1=0.324) — chandelier dominance reflects population composition of the source label, not contradictory evidence against PV-basket → SUPT_0206. The Que 2021 morphology-confirmed BC run resolves this ambiguity.*

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | — (supertype) | 2860 | 🟢 HIGH | Pvalb CONSISTENT · location APPROXIMATE | Best candidate |
| 2 | 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] | 0206 Pvalb Gaba_2 | 490 | 🟢 HIGH | Pvalb CONSISTENT · Cck DISCORDANT | Best candidate (child cluster) |

Total: 2 edges; relationship type PARTIAL_OVERLAP on both.

#### Property alignment — primary candidate SUPT_0206 (0206 Pvalb Gaba_2)

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA (CLUS_0739) | CONSISTENT |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | CA1 stratum oriens (818 cells); CA1 pyramidal layer not listed | CA1 pyramidal layer (26 cells); CA1 SO (124 cells) (CLUS_0739) | APPROXIMATE |
| Pvalb expression | defining marker | Pvalb subclass; precomputed mean 8.74 | Pvalb in MERFISH markers; precomputed mean 10.63 (CLUS_0739) | CONSISTENT |
| Gad1 expression | defining marker | not in supertype defining_markers; precomputed mean 10.34 | precomputed mean 10.52 (CLUS_0739) | APPROXIMATE |
| Gad2 expression | defining marker | not in supertype defining_markers; precomputed mean 9.28 | precomputed mean 8.43 (CLUS_0739) | APPROXIMATE |
| Cnr1 (negative) | absent | not in supertype markers; precomputed mean 1.93 | not in cluster markers; precomputed mean 1.68 (CLUS_0739) | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas supertype metadata (SUPT_0206) | Atlas metadata | PARTIAL | Pvalb subclass; CA1 SO (818) + CA3 SO (152) + piriform (959 cells) | atlas-internal |
| Atlas precomputed expression (SUPT_0206) | Atlas metadata | SUPPORT | Pvalb=8.74; Gad1=10.34; Gad2=9.28; Cnr1=1.93 | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 | Annotation transfer | PARTIAL | SUPT_0206 F1=0.324 (12 cells); SUPT_0204 chandelier F1=0.612 | atlas-internal |
| Que 2021 patch-seq BC → WMBv1 | Annotation transfer | SUPPORT | SUPT_0206 F1=0.785 (53/62 cells, group_purity=0.898) | atlas-internal |

*(2 of the SUPT_0206 child clusters carry PV basket vs. PV bistratified signal: CLUS_0739 is the BC-preferring cluster (Que 2021 F1=0.827) and CLUS_0737 is the BIC-preferring cluster; the remainder of SUPT_0206 children are not separately assessed. Best match: CLUS_0739.)*

#### Property alignment — secondary candidate CLUS_0739 (0739 Pvalb Gaba_2)

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | CA1 SO dominant | CA1 pyramidal layer (26 cells); CA1 SO (124 cells); CA3 SO (80); CA1 SR (45) | APPROXIMATE |
| Pvalb expression | defining marker | precomputed mean 8.74 | Pvalb in MERFISH markers; precomputed mean 10.63 | CONSISTENT |
| Gad1 expression | defining marker | precomputed mean 10.34 | precomputed mean 10.52 | APPROXIMATE |
| Gad2 expression | defining marker | precomputed mean 9.28 | precomputed mean 8.43 | APPROXIMATE |
| Cnr1 (negative) | absent | precomputed mean 1.93 | precomputed mean 1.68 | CONSISTENT |
| Cck (neuropeptide) | not expected (Cnr1-negative PV cells) | not assessed at supertype | Cck score 7.6; precomputed mean 7.56 | DISCORDANT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas cluster metadata (CLUS_0739) | Atlas metadata | PARTIAL | CA1 SO (124) + CA3 SO (80) + CA1 PYR (26); Pvalb MERFISH; Cck neuropeptide score 7.6 | atlas-internal |
| Atlas precomputed expression (CLUS_0739) | Atlas metadata | SUPPORT | Pvalb=10.63; Gad1=10.52; Gad2=8.43; Cnr1=1.68 | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 | Annotation transfer | PARTIAL | CLUS_0739 F1=0.179 (5 cells); CLUS_0732 chandelier F1=0.622 | atlas-internal |
| Que 2021 patch-seq BC → WMBv1 | Annotation transfer | SUPPORT | CLUS_0739 F1=0.827 (31 cells, target_purity=0.861) | atlas-internal |

*(Within SUPT_0206, the Que 2021 morphology-confirmed BC cells preferentially map to CLUS_0739 while morphology-confirmed BIC cells map to CLUS_0737 — a genuine BC/BIC cluster-level separation. Best match for PV basket: CLUS_0739.)*

### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟢 HIGH

**Supporting evidence**
- Pvalb subclass identity and GABA neurotransmitter type are consistent with PV basket cell identity; CA1 stratum oriens (818 cells) and CA3 stratum oriens (152 cells) are appropriate perisomatic interneuron locations.
- Precomputed expression cross-check: all 3 defining markers confirmed (Pvalb=8.74, Gad1=10.34, Gad2=9.28) and negative marker Cnr1 absent (1.93).
- Que 2021 morphology-confirmed PV basket cells (n=62, hBC + vBC aggregated) map to SUPT_0206 with F1=0.785, group_purity=0.898 (53/62 cells). Second independent AT run — convergence from morphologically labelled patch-seq cells justifies HIGH confidence.
- Yao 2021 SSv4 Pvalb subclass (n=66 HIP cells) splits between PV chandelier (SUPT_0204, F1=0.612) and PV basket/bistratified (SUPT_0206, F1=0.324); SUPT_0206 hits have target_purity=0.800. The split reflects the mixed-population SSv4 label rather than a transcriptomic conflict.

**Marker evidence provenance**
- **Pvalb (defining):** transcript- and protein-level evidence with multiple primary citations [1][6][7][8]; rat IHC [1] plus morphologically reconstructed/patch-seq mouse studies. Atlas precomputed mean 8.74 at supertype and 10.63 at CLUS_0739 strongly support presence. No discrepancy.
- **Gad1, Gad2 (defining):** no specific citations attached on the classical node; supported indirectly by the GABAergic NT assignment [5]. Atlas precomputed means (10.34 / 9.28 at supertype) are high and consistent. Listing a primary citation establishing Gad1/Gad2 in PV basket cells specifically would strengthen the evidence chain.
- **Cnr1 (negative):** no specific citation attached on the classical node. Atlas precomputed mean 1.93 (supertype) confirms low/absent expression; the literature framing relies on the established Cnr1-positive identity of CCK basket cells as the contrasting class [5][8].

**Concerns**
- Soma location APPROXIMATE: classical CA1 stratum pyramidale, atlas dominant CA1 stratum oriens *(adjacent region — could reflect registration boundary error; weak counter-evidence)*. SO and SP are immediately adjacent and PV basket cell somata at the SP/SO border are well documented.
- Supertype is not hippocampus-specific: includes 959 piriform area cells alongside CA1 SO (818) and CA3 SO (152). The mapping is PARTIAL_OVERLAP rather than EXACT.
- DISTRIBUTED_ACROSS_CLUSTERS caveat: PV+ morphological subtypes (basket, axo-axonic, bistratified) share high transcriptomic similarity and are not cleanly separated at supertype level. The supertype contains multiple classical PV subtypes including the chandelier-leaning fraction.
- Yao 2021 SSv4 'Pvalb' label is a mixed PV population; chandelier/AAC cells likely dominate the SSv4 mapping (PARTIAL). Morphology-resolved data (Que 2021) is needed to confirm — and does so.

**What would upgrade confidence**
- A within-supertype refinement using Que 2021 BC vs BIC vs AAC cell labels mapped at cluster level (already partially achieved — see CLUS_0739 below) to formally separate the PV basket fraction from PV bistratified and axo-axonic fractions.
- Targeted literature search for primary citations establishing Gad1 / Gad2 / Cnr1 in morphology-confirmed hippocampal PV basket cells (currently unsourced on the classical node).

### 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] · 🟢 HIGH

**Supporting evidence**
- Hippocampal enrichment: CA1 SO (124 cells), CA3 SO (80 cells), CA1 pyramidal layer (26 cells), CA1 SR (45 cells). GABA NT consistent.
- Precomputed expression: Pvalb=10.63 (strongest among SUPT_0206 child clusters), Gad1=10.52, Gad2=8.43, Cnr1=1.68 (absent).
- Que 2021 patch-seq BC (morphologically confirmed basket cells, n=62) — CLUS_0739 is the top cluster hit: F1=0.827, group_purity=0.795 (31 cells map here), target_purity=0.861. Bistratified cells (BIC) preferentially map to CLUS_0737 instead, demonstrating a genuine within-supertype BC/BIC transcriptomic distinction at cluster level from morphologically labelled cells.

**Marker evidence provenance**
- **Pvalb (defining):** atlas MERFISH markers list Pvalb and precomputed mean is 10.63; concordant with classical literature [1][6][7][8].
- **Cck (neuropeptide — discordant atlas signal):** Cck is *not* a classical marker for PV basket cells (which are Cnr1-negative and distinct from CCK basket cells per Whissell et al. [5] and Contreras et al. [8]), yet CLUS_0739 carries a Cck neuropeptide expression score of 7.6 and precomputed mean 7.56. Flag for investigation: this may reflect cluster boundaries that do not align cleanly to classical types, or genuine Cck transcript co-expression in a subset of PV basket cells at a level below the threshold for the classical Cnr1/CB1R-positive CCK basket identity.

**Concerns**
- Cck DISCORDANT: high Cck neuropeptide expression at this cluster is unexpected for PV basket cells. May indicate mixed cluster content or low-level Cck transcript co-expression in PV cells. The classical PV-vs-CCK perisomatic dichotomy [5][8] is at the protein/CB1R level and does not strictly rule out Cck transcript in PV cells, but the magnitude here warrants follow-up.
- Soma location APPROXIMATE: classical CA1 SP vs cluster signal mostly in CA1 SO with only 26 CA1 SP cells *(adjacent region — could reflect registration boundary error; weak counter-evidence)*.
- DISTRIBUTED_ACROSS_CLUSTERS caveat: PV+ hippocampal interneurons (basket, axo-axonic, bistratified) have high transcriptomic similarity [6]; CLUS_0739 is BC-enriched but likely contains residual non-basket PV cells.
- Yao 2021 SSv4 Pvalb → CLUS_0739 F1=0.179 is low (PARTIAL); this is consistent with the SSv4 Pvalb label being mixed and chandelier-dominated (CLUS_0732 F1=0.622) rather than counter-evidence.

**What would upgrade confidence**
- A Cre-driver-targeted single-cell dataset of morphology-confirmed PV basket cells (separating BC from AAC and BIC in vivo) mapped at F1 ≥ 0.85 at CLUSTER level — partially achieved by Que 2021 (F1=0.827); a larger morphology-confirmed cohort or a complementary technique (e.g. retro-PV-Cre + scRNA-seq) would push the result over the F1 ≥ 0.85 line.
- Resolution of the Cck discrepancy: protein-level validation (Cck IHC in CLUS_0739-mapped Pvalb cells) or co-expression analysis from the underlying 10x dataset.
- Targeted literature search for Cnr1-negative status of hippocampal PV basket cells (primary citation, not review).

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The PV basket cell is defined here on a CLASSICAL_MULTIMODAL basis — converging immunohistochemistry, single-cell morphology + electrophysiology, and intersectional genetic mapping. Defining markers Pvalb [1][6][7][8], Gad1, Gad2; negative marker Cnr1; soma in pyramidal layers of CA1 [UBERON:0014548], CA3 [UBERON:0014550], and dentate gyrus granule cell layer [UBERON:0005381] [1][2][3][4]; GABAergic neurotransmission [5].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer — Yao 2021 SSv4 (GSE185862).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 (GSE185862) mouse hippocampal formation SMART-Seq v4 cell type labels — Pvalb subclass used here) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Annotation transfer — Que 2021 patch-seq (GSE142546).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (Que 2021 patch-seq PV interneuron morphological types: hBC, vBC, hBIC, vBIC, AAC; aggregated to BC, BIC, AAC for F1 scoring) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). Gene symbols remapped to Ensembl IDs (19788/35825 mapped). Input TPM treated as pseudo-counts. |
| Tool version | cell_type_mapper v1.7.1 |
| n cells | 88 (filtered to 88) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Caveats | Patch-seq dataset with morphologically confirmed PV subtypes. TPM input used as pseudo-counts. Age range P10–P77 (mean P30) vs adult WMBv1; Que et al. found high transcriptomic similarity of morphological types across ages. AAC n=6 is insufficient for reliable F1 (treated as uninformative). Key finding: BC and BIC cells separate cleanly within SUPT_0206 (Pvalb Gaba_2) at cluster level — BC to CLUS_0739 (F1=0.827), BIC to CLUS_0737 (F1=0.800). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `bb9feaf` at 2026-05-13T10:38:59+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL ×2, SUPPORT ×2 | atlas-internal |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL ×2, SUPPORT ×2 | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Parvalbumin-positive basket cell → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] at HIGH confidence, with the basket-preferring child cluster 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] at HIGH confidence within that supertype. Key support: convergent annotation transfer from morphologically labelled patch-seq PV basket cells (Que 2021, BC F1=0.785 at supertype, 0.827 at cluster) plus quantitative atlas precomputed expression (Pvalb high, Cnr1 absent). Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (PV basket / axo-axonic / bistratified share the Pvalb Gaba subclass with high transcriptomic similarity per [6]) and MARKER_NOT_SPECIFIC (Cnr1 negative status not directly verifiable from atlas metadata; unexpected high Cck neuropeptide score at CLUS_0739).

The Cell Ontology has no specific term for hippocampal PV basket cells; basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] is the closest ancestor (BROAD). CL:0000118 covers perisomatic-targeting GABAergic interneurons but does not capture PV-specific identity. No hippocampus-specific PV basket cell term exists in CL — this is a candidate for a CL new-term request.

### Proposed experiments and follow-ups

The two AT runs already substantially address the standard "run MapMyCells from a hippocampal PV-IN dataset" experiment. What was done:
- **Yao 2021 SSv4 Pvalb subclass → WMBv1 (GSE185862, n=66 HIP cells):** subclass-level mapping; results PARTIAL because the SSv4 label aggregates basket + axo-axonic + bistratified cells.
- **Que 2021 patch-seq morphology-confirmed BC / BIC / AAC → WMBv1 (GSE142546, n=88 cells):** morphology-resolved labels; BC to SUPT_0206 F1=0.785 and CLUS_0739 F1=0.827; BC vs BIC cluster-level separation confirmed (BIC → CLUS_0737).

Refinements that would still add value:
- **What:** Larger morphology-confirmed PV-IN cohort (Cre-driver or retro-tagged) mapped at cluster level. **Target:** F1 ≥ 0.85 at CLUSTER, n ≥ 200 BC cells. **Expected output:** AnnotationTransferEvidence with tighter group_purity and target_purity bounds. **Resolves:** DISTRIBUTED_ACROSS_CLUSTERS caveat for the BC fraction specifically.
- **What:** Cck transcript and protein co-expression analysis in CLUS_0739-mapped PV cells (re-analysis of underlying 10x dataset; or Cck IHC in Pvalb-Cre × reporter sections). **Target:** quantify fraction of PV+ CLUS_0739-mapped cells with detectable Cck and CB1R/Cnr1. **Expected output:** MarkerAnalysisEvidence + LiteratureEvidence (if existing primary literature is found). **Resolves:** Cck DISCORDANT property comparison at CLUS_0739.
- **What:** Targeted cite-traverse for primary citations supporting Gad1 / Gad2 expression and Cnr1 negativity in morphology-confirmed hippocampal PV basket cells (currently unsourced on the classical node). **Expected output:** additional LiteratureEvidence entries; updated `defining_markers[*].refs` and negative-marker citations.

### Open questions

1. To what extent does the Pvalb Gaba subclass (SUBC_052) and supertype SUPT_0206 cleanly separate PV basket from PV axo-axonic and PV bistratified at single-cell resolution in the WMBv1 10x data? Que 2021 evidence supports cluster-level separation of BC vs BIC within SUPT_0206 (CLUS_0739 vs CLUS_0737); AAC was underpowered (n=6).
2. What is the biological basis for the high Cck neuropeptide score at CLUS_0739 (precomputed mean 7.56) given that PV basket cells are classically Cnr1/CB1R-negative and distinct from CCK basket cells? Mixed cluster content vs low-level Cck transcript co-expression in PV cells.
3. Is the piriform area component of SUPT_0206 (959 cells) transcriptomically distinguishable from the hippocampal CA1 SO + CA3 SO component, or does Pvalb Gaba_2 represent a genuinely shared cortical-hippocampal PV cell state?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703) | soma location; Pvalb marker |
| [2] | Sik et al. 1995 | [7472426](https://pubmed.ncbi.nlm.nih.gov/7472426) | soma location; morphology |
| [3] | Müller & Remy 2014 | [25324774](https://pubmed.ncbi.nlm.nih.gov/25324774) | soma location |
| [4] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | soma location; classical type representativeness |
| [5] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554) | neurotransmitter type; PV/CCK distinction |
| [6] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060) | Pvalb marker; PV subtype transcriptomic similarity |
| [7] | Perrenoud et al. 2022 | [35802727](https://pubmed.ncbi.nlm.nih.gov/35802727) | Pvalb marker |
| [8] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048) | Pvalb marker; perisomatic interneuron framing |
