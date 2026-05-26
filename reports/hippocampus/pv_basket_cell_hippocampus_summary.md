# Parvalbumin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Parvalbumin-positive (PV+) basket cells are fast-spiking GABAergic interneurons of the hippocampal formation whose axons innervate the somata and proximal dendrites of pyramidal cells, providing the perisomatic inhibition that paces hippocampal network oscillations [1][2]. They are distributed across CA1 and CA3 stratum pyramidale as well as the dentate gyrus granule cell layer, and together with CCK basket cells form the two major perisomatic inhibitory populations of the hippocampus [5][8]. Mapping PV basket cells to the Whole Mouse Brain v1 (WMBv1) transcriptomic atlas is complicated by their high transcriptomic similarity to other PV+ hippocampal subtypes — axo-axonic and bistratified cells — which share the Pvalb Gaba subclass and can only be separated at the cluster level with morphologically confirmed data.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548]; pyramidal layer of CA3 [UBERON:0014550]; dentate gyrus granule cell layer [UBERON:0005381] | [1][2][3][4] |
| NT | GABAergic | [5] |
| Markers | Pvalb (defining); Gad1; Gad2 | Pvalb [1][6][7][8]; Gad1, Gad2 (functional GABAergic identity) |
| Negative markers | Cnr1 (absent) | — |
| CL term | basket cell [CL:0000118] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / morphology:** classical anatomical description, rat hippocampus, biocytin fills and immunohistochemistry · [2]
  > Fast spiking interneurons in the CA1 area of the dorsal hippocampus were recorded from and filled with biocytin in anesthetized rats. The full extent of their dendrites and axonal arborizations as well as their calcium binding protein content were examined. Based on the spatial extent of axon collaterals, local circuit cells (basket and O- LM neurons) and long-range cells (bistratified, trilaminar, and backprojection neurons) could be distinguished. Basket cells were immunoreactive for parvalbumin and their axon collaterals were confined to the pyramidal layer. A single basket cell contacted more than 1500 pyramidal neurons and 60 other parvalbumin-positive interneurons. Commissural stimulation directly discharged basket cells, followed by an early and late IPSPs, indicating interneuronal inhibition of basket cells. The dendrites of another local circuit neuron (O-LM) were confined to stratum oriens and it had a small but high-density axonal terminal field in stratum lacunosum-moleculare. The fastest firing cell of all interneurons was a calbindin-immunoreactive bistratified neuron with axonal targets in stratum oriens and radiatum. Two neurons with their cell bodies in the alveus innervated the CA3 region (backprojection cells), in addition to rich axon collaterals in the CA1 region. The trilaminar interneuron had axon collaterals in strata radiatum, oriens and pyramidale with its dendrites confined to stratum oriens. Commissural stimulation evoked an early EPSP-IPSP-late depolarizing potential sequence in this cell. All interneurons formed symmetric synapses with their targets at the electron microscopic level. These findings indicate that interneurons with distinct axonal targets have differential functions in shaping the physiological patterns of the CA1 network.
  > — Sik et al. 1995, Anatomical Location and Morphology · [2] <!-- quote_key: 10664418_9acd7ec1 -->

- **Pvalb marker / anatomical distribution:** rat hippocampus immunolocalisation · [1]
  > Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)
  > — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->

- **GABAergic identity / PV–CCK distinction:** intersectional genetic mapping across forebrain · [5]
  > Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus. As CCK- and PV-GABA neurons differ in an array of morphological, biochemical and electrophysiological features, it has been proposed that they form distinct inhibitory ensembles which differentially contribute to network oscillations and behavior. However, the relationship and balance between CCK- and PV-GABA neurons in the inhibitory networks of the brain is currently unclear as the distribution of these cells has never been compared on a large scale. Here, we systemically investigated the distribution of CCK- and PV-GABA cells across a wide number of discrete forebrain regions using an intersectional genetic approach. Our analysis revealed several novel trends in the distribution of these cells. While PV-GABA cells were more abundant overall, CCK-GABA cells outnumbered PV-GABA cells in several subregions of the hippocampus, medial prefrontal cortex and ventrolateral temporal cortex. Interestingly, CCK-GABA cells were relatively more abundant in secondary/ association areas of the cortex (V2, S2, M2, and AudD/AudV) than they were in corresponding primary areas (V1, S1, M1, and Aud1). The reverse trend was observed for PV-GABA cells. Our findings suggest that the balance between CCK- and PV-GABA cells in a given cortical region is related to the type of processing that area performs; inhibitory networks in the secondary cortex tend to favor the inclusion of CCK-GABA cells more than networks in the primary cortex. The intersectional genetic labeling approach employed in the current study expands upon the ability to study molecularly defined subsets of GABAergic neurons. This technique can be applied to the investigation of neuropathologies which involve disruptions to the GABAergic system, including schizophrenia, stress, maternal immune activation and autism.
  > — Whissell et al. 2015, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 16859318_009e9f36 -->

- **Perisomatic interneuron framing (PV majority):** · [8]
  > the majority of interneurons in these regions express either the neuropeptide cholecystokinin or the calcium binding protein parvalbumin
  > — Contreras et al. 2019, SOMA AND AXON TARGETING INTERNEURONS · [8] <!-- quote_key: 195584607_37a80af5 -->

- **Representativeness of PV basket within the hippocampal IN repertoire:** · [4]
  > the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin
  > — Bocchio et al. 2024, Results · [4] <!-- quote_key: 262127573_ba6d02e9 -->

</details>

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD). CL:0000118 covers perisomatic-targeting GABAergic interneurons but does not capture PV-specific identity; no hippocampus-specific PV basket cell term exists in CL.

---

## Results

Two candidate atlas entries were assessed — supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] and its child cluster 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] — both assessed at HIGH confidence with a PARTIAL_OVERLAP relationship. The primary evidence is morphologically confirmed PV basket cells from Que 2021 (GEO:GSE142546) reaching F1 = 0.785 at the supertype level and F1 = 0.827 at the cluster level.

**Annotation-transfer overview figure (run-level, filtered)**

![Filtered AT figure for Parvalbumin-positive basket cell — Que 2021 BC source group](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/figures/f1_for_pv_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the BC (basket cell) source group from Que 2021 patch-seq morphological labels (hBC n=12 + vBC n=50 aggregated, n=62 total). Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. SUPT_0206 (Pvalb Gaba_2) reaches F1 = 0.785 and CLUS_0739 reaches F1 = 0.827.*

![Filtered AT figure for Parvalbumin-positive basket cell — Yao 2021 Pvalb SSv4 source group](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_pv_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 SSv4 Pvalb subclass source group (n=66 hippocampal Pvalb cells from GEO:GSE185862). The SSv4 Pvalb label is morphologically unresolved (mixes basket, axo-axonic, and bistratified PV cells), yielding split signal across Pvalb chandelier (SUPT_0204, F1 = 0.612) and Pvalb Gaba_2 (SUPT_0206, F1 = 0.324). The chandelier dominance reflects composition of the source label; the Que 2021 morphology-confirmed BC run resolves this ambiguity.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | — (supertype) | 2860 | 🟢 HIGH | Pvalb CONSISTENT · location APPROXIMATE · Cnr1 CONSISTENT | Best candidate |
| 2 | 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] | 0206 Pvalb Gaba_2 | 490 | 🟢 HIGH | Pvalb CONSISTENT · Cnr1 CONSISTENT · Cck DISCORDANT | Best candidate (child cluster) |

Total: 2 edges; relationship type PARTIAL_OVERLAP on both.

### Property alignment — 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟢 HIGH

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA (Pvalb Gaba_2) | GABA (CLUS_0739) | CONSISTENT |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | CA1 stratum oriens (818 cells); CA1 pyramidal layer not listed | CA1 pyramidal layer (26 cells); CA1 SO (124 cells) (CLUS_0739) | APPROXIMATE |
| Pvalb expression | defining marker | Pvalb subclass; precomputed mean 8.74 | Pvalb in MERFISH markers; precomputed mean 10.63 (CLUS_0739) | CONSISTENT |
| Gad1 expression | defining marker | not in supertype defining_markers; precomputed mean 10.34 | precomputed mean 10.52 (CLUS_0739) | APPROXIMATE |
| Gad2 expression | defining marker | not in supertype defining_markers; precomputed mean 9.28 | precomputed mean 8.43 (CLUS_0739) | APPROXIMATE |
| Cnr1 (negative) | absent | not in supertype markers; precomputed mean 1.93 | not in cluster markers; precomputed mean 1.68 (CLUS_0739) | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas supertype metadata (SUPT_0206) | Atlas metadata | PARTIAL | Pvalb subclass; CA1 SO (818) + CA3 SO (152) + piriform (959 cells); multi-region | atlas-internal |
| Atlas precomputed expression (SUPT_0206) | Atlas metadata | SUPPORT | Pvalb=8.74; Gad1=10.34; Gad2=9.28; Cnr1=1.93 | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 (GEO:GSE185862) | Annotation transfer | PARTIAL | SUPT_0206 F1=0.324 (12/66 cells, target_purity=0.800); SUPT_0204 chandelier F1=0.612 dominant | atlas-internal |
| Que 2021 patch-seq BC → WMBv1 (GEO:GSE142546) | Annotation transfer | SUPPORT | SUPT_0206 F1=0.785 (53/62 cells, group_purity=0.898) | atlas-internal |

*(SUPT_0206 child clusters CLUS_0739 and CLUS_0737 carry PV basket vs PV bistratified signal respectively per the Que 2021 morphology run. Best match within this supertype: CLUS_0739.)*

### Property alignment — 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] · 🟢 HIGH

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma location | CA1 stratum pyramidale [UBERON:0014548] | CA1 SO dominant | CA1 pyramidal layer (26 cells); CA1 SO (124 cells); CA3 SO (80); CA1 SR (45) | APPROXIMATE |
| Pvalb expression | defining marker | precomputed mean 8.74 (parent) | Pvalb in MERFISH markers; precomputed mean 10.63 | CONSISTENT |
| Gad1 expression | defining marker | precomputed mean 10.34 (parent) | precomputed mean 10.52 | APPROXIMATE |
| Gad2 expression | defining marker | precomputed mean 9.28 (parent) | precomputed mean 8.43 | APPROXIMATE |
| Cnr1 (negative) | absent | precomputed mean 1.93 (parent) | precomputed mean 1.68 | CONSISTENT |
| Cck (neuropeptide) | not expected (Cnr1-negative PV cells) | not assessed at supertype | Cck expression score 7.6; precomputed mean 7.56 | DISCORDANT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas cluster metadata (CLUS_0739) | Atlas metadata | PARTIAL | CA1 SO (124) + CA3 SO (80) + CA1 PYR (26); Pvalb MERFISH; Cck NP score 7.6 | atlas-internal |
| Atlas precomputed expression (CLUS_0739) | Atlas metadata | SUPPORT | Pvalb=10.63; Gad1=10.52; Gad2=8.43; Cnr1=1.68 | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 (GEO:GSE185862) | Annotation transfer | PARTIAL | CLUS_0739 F1=0.179 (5/66 cells); CLUS_0732 chandelier F1=0.622 dominant | atlas-internal |
| Que 2021 patch-seq BC → WMBv1 (GEO:GSE142546) | Annotation transfer | SUPPORT | CLUS_0739 F1=0.827 (31/62 cells, group_purity=0.795, target_purity=0.861) | atlas-internal |

*(Within SUPT_0206, Que 2021 morphology-confirmed BC cells preferentially map to CLUS_0739 while BIC cells preferentially map to sibling CLUS_0737 — a genuine BC/BIC transcriptomic distinction at cluster level from morphologically labelled cells.)*

### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟢 HIGH

**Supporting evidence**
- Pvalb subclass identity and GABA neurotransmitter type are fully consistent with PV basket cell identity; CA1 stratum oriens (818 cells) and CA3 stratum oriens (152 cells) include appropriate perisomatic interneuron locations.
- Precomputed expression cross-check confirms all 3 defining markers (Pvalb=8.74, Gad1=10.34, Gad2=9.28) and negative marker Cnr1 absent (1.93).
- Que 2021 morphology-confirmed PV basket cells (n=62, hBC + vBC aggregated) map to SUPT_0206 with F1=0.785, group_purity=0.898 (53/62 cells). This is the stronger of the two AT runs because source cells have confirmed perisomatic basket morphology from patch-clamp + biocytin fill.
- Yao 2021 SSv4 Pvalb subclass (n=66 HIP cells) splits between PV chandelier (SUPT_0204, F1=0.612) and Pvalb Gaba_2 (SUPT_0206, F1=0.324) with SUPT_0206 target_purity=0.800; the split reflects the mixed-population SSv4 label rather than transcriptomic conflict, and is resolved by the morphology-confirmed Que 2021 run.

**Concerns**
- Soma location APPROXIMATE: classical CA1 stratum pyramidale [UBERON:0014548]; atlas dominant hippocampal CA1 signal in stratum oriens. *(note: SO and SP are immediately adjacent; PV basket cell somata at the SP/SO border are anatomically well-documented — mild counter-evidence.)*
- DISTRIBUTED_ACROSS_CLUSTERS: SUPT_0206 spans hippocampus (CA1 SO, CA3 SO) and piriform area (959 cells); multiple PV+ morphological subtypes (basket, axo-axonic, bistratified) co-populate this supertype with high transcriptomic similarity.
- Cnr1 negative-marker status not directly verifiable from atlas supertype metadata; supported by low precomputed mean (1.93) only.

**What would upgrade confidence**
- Confidence is already HIGH; the remaining gap is resolution of the Cck DISCORDANT signal at CLUS_0739 and a larger morphology-confirmed dataset to tighten BC/BIC separation statistics.

### 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] · 🟢 HIGH

**Supporting evidence**
- Hippocampal enrichment: CA1 SO (124 cells), CA3 SO (80 cells), CA1 pyramidal layer (26 cells), CA1 SR (45 cells). GABA NT consistent.
- Strongest Pvalb expression among SUPT_0206 child clusters: precomputed mean 10.63; Pvalb present in MERFISH markers. Cnr1 low/absent (1.68).
- Que 2021 patch-seq BC cells (morphologically confirmed basket, n=62) — CLUS_0739 is the top cluster hit: F1=0.827, group_purity=0.795 (31 cells), target_purity=0.861. Bistratified cells preferentially map to sibling CLUS_0737 (F1=0.800), demonstrating genuine within-supertype BC/BIC transcriptomic separation from morphologically labelled cells.
- Second independent AT run (Yao 2021) provides supporting context; the lower CLUS_0739 F1=0.179 from the SSv4 mixed-PV source label does not undermine this finding.

**Concerns**
- Cck DISCORDANT: CLUS_0739 carries Cck neuropeptide expression score 7.6 (precomputed mean 7.56), which is unexpected for PV basket cells that are classically Cnr1/CB1R-negative and distinct from CCK basket cells [5][8]. This may reflect cluster boundaries that do not align cleanly to classical types, or low-level Cck transcript co-expression in some PV neurons at levels below the threshold for CB1R-based CCK basket cell identity.
- Soma location APPROXIMATE: classical CA1 SP vs cluster signal mostly in CA1 SO (124 cells) with only 26 cells in CA1 pyramidal layer. *(adjacent region — mild counter-evidence.)*
- DISTRIBUTED_ACROSS_CLUSTERS: CLUS_0739 is BC-enriched but the PV-IN continuous transcriptomic landscape means residual non-basket PV cells are expected within this cluster [6].

**What would upgrade confidence**
- Resolution of the Cck discrepancy: protein-level validation (Cck IHC in Pvalb-Cre × reporter sections, specifically in CLUS_0739-matched cells) or re-analysis of the underlying 10x dataset.
- Larger morphology-confirmed PV basket cell cohort (n ≥ 200) to push F1 above 0.85 at cluster level with tighter purity bounds.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The PV basket cell is defined here on a CLASSICAL_MULTIMODAL basis: converging immunohistochemistry, single-cell morphology + electrophysiology, and intersectional genetic mapping. Defining markers Pvalb [1][6][7][8], Gad1, Gad2; negative marker Cnr1; soma in pyramidal layers of CA1 [UBERON:0014548], CA3 [UBERON:0014550], and dentate gyrus granule cell layer [UBERON:0005381] [1][2][3][4]; GABAergic neurotransmission [5].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster and from MERFISH spatial registration for soma location.

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4; Pvalb subclass, n=66 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |

Run 2 — Que 2021 patch-seq PV interneurons → WMBv1 (primary AT for this node):

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (Que 2021 patch-seq PV interneuron morphological types: hBC n=12, vBC n=50, hBIC n=11, vBIC n=9, AAC n=6; aggregated BC n=62, BIC n=20, AAC n=6; 88 QC-passed cells from 128 total) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). Gene symbols remapped to Ensembl IDs (19788/35825 mapped). TPM input rounded to integer pseudo-counts. F1 scored with aggregated labels (BC/BIC/AAC). |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 88 (filtered to 88) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Patch-seq dataset with morphologically confirmed PV subtypes. TPM input used as pseudo-counts (standard for patch-seq). Age range P10–P77 (mean P30) vs adult WMBv1. AAC n=6 insufficient for reliable F1 (treated as uninformative). Key finding: BC and BIC separate cleanly within SUPT_0206 at cluster level — BC to CLUS_0739 (F1=0.827), BIC to CLUS_0737 (F1=0.800). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:09+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL; SUPPORT; PARTIAL; SUPPORT | atlas-internal |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL; SUPPORT; PARTIAL; SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Parvalbumin-positive basket cell → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] at HIGH confidence, with basket-preferring child cluster 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] also at HIGH confidence within that supertype. Key support: convergent annotation transfer from morphologically labelled patch-seq PV basket cells (Que 2021, BC F1 = 0.785 at supertype, 0.827 at cluster) plus quantitative precomputed expression (Pvalb high, Cnr1 absent) and MERFISH Pvalb marker confirmation in CLUS_0739. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (PV basket / axo-axonic / bistratified share the Pvalb Gaba subclass with high transcriptomic similarity [6]) and Cck DISCORDANT at CLUS_0739 (unexpected high Cck neuropeptide score for a Cnr1-negative PV cell population [5][8]).

The Cell Ontology has no specific term for hippocampal PV basket cells; basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] is the closest ancestor (BROAD). CL:0000118 covers perisomatic-targeting GABAergic interneurons but does not capture PV-specific identity — this is a candidate for a CL new-term request.

### Proposed experiments and follow-ups

The two AT runs already substantially address the standard "map hippocampal PV cells to WMBv1" experiment. Remaining gaps:

1. **Cck co-expression resolution.** Re-analysis of the CLUS_0739 underlying 10x dataset to quantify Cck and Cnr1 transcript fraction in CLUS_0739-matched Pvalb cells; or Cck IHC in Pvalb-Cre × reporter sections. Target: establish whether Cck transcript in CLUS_0739 reflects cluster boundary ambiguity or genuine PV/CCK co-expression below the CB1R threshold. Resolves: Cck DISCORDANT property comparison.

2. **Larger morphology-confirmed PV basket cell cohort.** New patch-seq or fate-mapped + sorted PV basket cell dataset (n ≥ 200 BC cells, adult mice to match WMBv1 age). Target: F1 ≥ 0.85 at CLUSTER, tighter group_purity and target_purity bounds. Resolves: age-mismatch caveat from Que 2021 (mean P30) and DISTRIBUTED_ACROSS_CLUSTERS replication.

3. **Primary citations for Gad1 / Gad2 / Cnr1 in hippocampal PV basket cells.** Targeted literature search for cite-level support for these markers on morphologically confirmed PV basket cells specifically (currently supported by indirect functional reasoning). Resolves: unsourced marker entries on the classical node.

### Open questions

1. To what extent does SUPT_0206 cleanly separate PV basket from PV axo-axonic and PV bistratified at single-cell resolution in the WMBv1 10x data? Que 2021 evidence supports BC/BIC cluster-level separation (CLUS_0739 vs CLUS_0737) but AAC was underpowered (n=6).

2. What is the biological basis for the high Cck neuropeptide score at CLUS_0739 (precomputed mean 7.56) given that PV basket cells are classically Cnr1/CB1R-negative? Mixed cluster content vs low-level Cck transcript co-expression in PV cells?

3. Is the piriform area component of SUPT_0206 (959 cells) transcriptomically distinguishable from the hippocampal CA1 SO + CA3 SO component, or does Pvalb Gaba_2 represent a shared cortical-hippocampal PV cell state?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703) | soma location; Pvalb marker |
| [2] | Sik et al. 1995 | [7472426](https://pubmed.ncbi.nlm.nih.gov/7472426) | soma location; morphology |
| [3] | Müller & Remy 2014 | [25324774](https://pubmed.ncbi.nlm.nih.gov/25324774) | soma location |
| [4] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | soma location; PV IN repertoire |
| [5] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554) | neurotransmitter type; PV/CCK distinction |
| [6] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060) | Pvalb marker; PV subtype transcriptomic similarity |
| [7] | Perrenoud et al. 2022 | [35802727](https://pubmed.ncbi.nlm.nih.gov/35802727) | Pvalb marker |
| [8] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048) | Pvalb marker; perisomatic interneuron framing |
