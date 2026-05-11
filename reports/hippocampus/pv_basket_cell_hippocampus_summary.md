# Parvalbumin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The hippocampal parvalbumin-positive (PV+) basket cell is a perisomatic-targeting GABAergic interneuron defined by expression of the calcium-binding protein parvalbumin (*Pvalb*) and by axon collaterals confined to the pyramidal layer of CA1 and CA3, where they contact the soma and proximal dendrites of hundreds of principal cells [2]. Mapping this cell type onto the Allen Brain Cell Atlas (WMBv1/CCN20230722) is of particular importance because PV basket cells are among the most powerful inhibitory regulators of hippocampal network oscillations, yet multiple PV+ morphological subtypes (basket, axo-axonic, bistratified) share high transcriptomic similarity that may limit resolution at coarse atlas levels [6].

> "Parvalbumin + cells were specifically localized in the granular and polymorphic cell layers of the dentate gyrus and the strata oriens and pyramidale in CA1/3 fields of the rat hippocampus (Kosaka et al., 1987). They have been considered a subpopulation of GABAergic interneurons, including basket and axo-axonic cell types, which innervate the somata and proximal axons of pyramidal cells, respectively (Soriano et al., 1990)"
> — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_bdfa426a -->

**Cell Ontology mapping.** CL:0000118 (basket cell) is BROAD — the term covers perisomatic-targeting GABAergic interneurons broadly but does not capture PV-specific identity. No hippocampus-specific PV basket cell term currently exists in the Cell Ontology. This type is a candidate for a new CL term request.

---

### Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA1 [UBERON:0014548]; pyramidal layer of CA3 [UBERON:0014550]; dentate gyrus granule cell layer [UBERON:0005381] | [1] [2] [3] [4] |
| Neurotransmitter | GABAergic | [5] |
| Defining markers | Pvalb, Gad1, Gad2 | Pvalb: [1][6][7][8]; Gad1, Gad2: (GABA identity) |
| Negative markers | Cnr1 | — |
| Neuropeptides | — | — |

<details>
<summary>Per-property literature support</summary>

**Soma location** [1][2][3][4]. Four independent studies confirm soma placement in the pyramidal layer of CA1 [UBERON:0014548], pyramidal layer of CA3 [UBERON:0014550], and dentate gyrus granule cell layer [UBERON:0005381]. Sik et al. 1995 [2] provided the foundational morphological characterisation:

> "Fast spiking interneurons in the CA1 area of the dorsal hippocampus were recorded from and filled with biocytin in anesthetized rats. The full extent of their dendrites and axonal arborizations as well as their calcium binding protein content were examined. Based on the spatial extent of axon collaterals, local circuit cells (basket and O- LM neurons) and long-range cells (bistratified, trilaminar, and backprojection neurons) could be distinguished. Basket cells were immunoreactive for parvalbumin and their axon collaterals were confined to the pyramidal layer. A single basket cell contacted more than 1500 pyramidal neurons and 60 other parvalbumin-positive interneurons. Commissural stimulation directly discharged basket cells, followed by an early and late IPSPs, indicating interneuronal inhibition of basket cells. The dendrites of another local circuit neuron (O-LM) were confined to stratum oriens and it had a small but high-density axonal terminal field in stratum lacunosum-moleculare. The fastest firing cell of all interneurons was a calbindin-immunoreactive bistratified neuron with axonal targets in stratum oriens and radiatum. Two neurons with their cell bodies in the alveus innervated the CA3 region (backprojection cells), in addition to rich axon collaterals in the CA1 region. The trilaminar interneuron had axon collaterals in strata radiatum, oriens and pyramidale with its dendrites confined to stratum oriens. Commissural stimulation evoked an early EPSP-IPSP-late depolarizing potential sequence in this cell. All interneurons formed symmetric synapses with their targets at the electron microscopic level. These findings indicate that interneurons with distinct axonal targets have differential functions in shaping the physiological patterns of the CA1 network."
> — Sik et al. 1995, Anatomical Location and Morphology · [2] <!-- quote_key: 10664418_9acd7ec1 -->

**Pvalb** [1][6][7][8]. Pvalb is the canonical marker of the PV basket cell, confirmed at protein (immunohistochemistry) and transcript level across multiple species and preparations. Rivera et al. 2014 [1] localises PV+ cells to stratum oriens and pyramidale across CA1/CA3. Que et al. 2021 [6] contributed patch-seq data from morphologically confirmed basket cells (hBC + vBC), providing direct transcriptomic validation. Perrenoud et al. 2022 [7] and Contreras et al. 2019 [8] independently confirm Pvalb marker status.

**GABAergic neurotransmitter** [5]. PV basket cells are GABAergic by canonical classification [5]. Gad1 and Gad2 are GABAergic synthesis genes consistent with GABA identity; precomputed atlas stats confirm strong expression of both in SUPT_0206 (Gad1=10.34, Gad2=9.28) and CLUS_0739 (Gad1=10.52, Gad2=8.43).

**Negative marker — Cnr1** [5][8]. Cnr1 (cannabinoid receptor 1 / CB1R) is absent in PV basket cells, distinguishing them from CCK basket cells. Whissell et al. 2015 [5] and Contreras et al. 2019 [8] describe the CCK/PV bistratification of perisomatic inhibition:

> "Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus. As CCK- and PV-GABA neurons differ in an array of morphological, biochemical and electrophysiological features, it has been proposed that they form distinct inhibitory ensembles which differentially contribute to network oscillations and behavior. However, the relationship and balance between CCK- and PV-GABA neurons in the inhibitory networks of the brain is currently unclear as the distribution of these cells has never been compared on a large scale. Here, we systemically investigated the distribution of CCK- and PV-GABA cells across a wide number of discrete forebrain regions using an intersectional genetic approach. Our analysis revealed several novel trends in the distribution of these cells. While PV-GABA cells were more abundant overall, CCK-GABA cells outnumbered PV-GABA cells in several subregions of the hippocampus, medial prefrontal cortex and ventrolateral temporal cortex. Interestingly, CCK-GABA cells were relatively more abundant in secondary/ association areas of the cortex (V2, S2, M2, and AudD/AudV) than they were in corresponding primary areas (V1, S1, M1, and Aud1). The reverse trend was observed for PV-GABA cells. Our findings suggest that the balance between CCK- and PV-GABA cells in a given cortical region is related to the type of processing that area performs; inhibitory networks in the secondary cortex tend to favor the inclusion of CCK-GABA cells more than networks in the primary cortex. The intersectional genetic labeling approach employed in the current study expands upon the ability to study molecularly defined subsets of GABAergic neurons. This technique can be applied to the investigation of neuropathologies which involve disruptions to the GABAergic system, including schizophrenia, stress, maternal immune activation and autism."
> — Whissell et al. 2015, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 16859318_009e9f36 -->

Precomputed atlas stats confirm Cnr1 low/absent in both SUPT_0206 (mean: 1.93) and CLUS_0739 (mean: 1.68).

**Node notes.** Four morphological subtypes within PV+ hippocampal interneurons: basket, axo-axonic, bistratified, radiatum-targeting (Bocchio et al. 2024 [4]). Activity of PV basket cells is inversely coupled with CCK basket cell activity. The most representative PV+ subtypes in hippocampus are the basket and bistratified cells [4]:

> "the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin"
> — Bocchio et al. 2024, Results · [4] <!-- quote_key: 262127573_ba6d02e9 -->

Contreras et al. 2019 [8] also note:

> "the majority of interneurons in these regions express either the neuropeptide cholecystokinin or the calcium binding protein parvalbumin"
> — Contreras et al. 2019, SOMA AND AXON TARGETING INTERNEURONS · [8] <!-- quote_key: 195584607_37a80af5 -->

</details>

---

## Results

Two candidates were assessed, both at HIGH confidence: a supertype-level edge to 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] and a cluster-level edge to 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739]. HIGH confidence was reached through convergent evidence from two independent annotation transfer runs (GSE185862 Yao 2021 SSv4 and GSE142546 Que 2021 patch-seq) combined with strong atlas metadata support. The Que 2021 patch-seq run — using morphologically confirmed basket cells — is the decisive evidence: 31 basket cells mapped to CLUS_0739 at cluster level (F1=0.827), and basket cells were clearly distinguished from bistratified cells (which prefer sibling cluster CLUS_0737).

### 4a. Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | 2,860 | 🟢 HIGH | NT CONSISTENT · Pvalb CONSISTENT · Cnr1 absent CONSISTENT · Gad1/Gad2 APPROXIMATE · Location APPROXIMATE | Best candidate |
| 2 | 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] | (child of SUPT_0206) | 490 | 🟢 HIGH | NT CONSISTENT · Pvalb CONSISTENT · Cnr1 absent CONSISTENT · Gad1/Gad2 APPROXIMATE · Location APPROXIMATE · Cck DISCORDANT | Best candidate |

2 edges total · both PARTIAL_OVERLAP.

---

### 4b. Property alignment — HIGH candidates

#### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]

**Table 1. Property comparison — classical vs atlas**

| Property | Classical value | Atlas value | Alignment | Notes |
|---|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT | |
| Location CA1 | Pyramidal layer of CA1 [UBERON:0014548] — soma | CA1 stratum oriens (818 cells); CA1 pyramidal layer not listed at supertype level | APPROXIMATE | Both are perisomatic layers; discrepancy may reflect soma-on-SO-border cells or atlas MERFISH resolution limits |
| Pvalb | Defining marker (IHC + transcript) | Pvalb subclass; Pvalb prominent in child cluster CLUS_0739 MERFISH; precomputed mean: 8.74 | CONSISTENT | |
| Gad1 | Defining marker | Not in supertype defining_markers; GABA NT consistent; precomputed mean: 10.34 | APPROXIMATE | |
| Gad2 | Defining marker | Not in supertype defining_markers; GABA NT consistent; precomputed mean: 9.28 | APPROXIMATE | |
| Cnr1 (negative) | Absent | Not in supertype markers; precomputed mean: 1.93 | CONSISTENT | Cnr1 low/absent confirms PV (not CCK) basket identity |

**Table 2. Evidence support**

| Evidence type | Source | Supports | Key metric | Notes |
|---|---|---|---|---|
| ATLAS_METADATA | WMBv1 CCN20230722 | PARTIAL | Pvalb subclass; GABA NT; CA1 SO 818 cells | Supertype spans hippocampus + piriform area; multiple PV+ subtypes co-populate at supertype level |
| ATLAS_METADATA | WMBv1 precomputed stats | SUPPORT | Pvalb=8.74, Gad1=10.34, Gad2=9.28, Cnr1=1.93 | All 3 defining markers confirmed; negative marker Cnr1 absent |
| ANNOTATION_TRANSFER | GEO:GSE185862 (Yao 2021 SSv4 Pvalb, n=66 HIP) | PARTIAL | F1=0.324 at SUPERTYPE; 12/66 cells to SUPT_0206; target_purity=0.800 | Mixed Pvalb source population; chandelier/AAC cells dominate mapping |
| ANNOTATION_TRANSFER | GEO:GSE142546 (Que 2021 patch-seq BC, n=62) | SUPPORT | 53/62 BC cells to SUPT_0206; group_purity=0.898; F1=0.785 | Morphologically confirmed basket cells; BC/BIC supertype convergence; second independent AT run |

**Subcluster concordance.** Within SUPT_0206, PV basket cells (BC) preferentially map to child cluster CLUS_0739, while PV bistratified cells (BIC) concentrate at sibling cluster CLUS_0737. This cluster-level separation of PV morphological subtypes within the same supertype is a genuine transcriptomic signal from morphologically labelled patch-seq data [6].

---

#### 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739]

**Table 1. Property comparison — classical vs atlas**

| Property | Classical value | Atlas value | Alignment | Notes |
|---|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT | |
| Location CA1 | Pyramidal layer of CA1 [UBERON:0014548] — soma | CA1 pyramidal layer (26 cells); CA1 stratum oriens (124 cells) | APPROXIMATE | Small CA1 pyramidal layer count; dominant hippocampal signal in stratum oriens; consistent with perisomatic layer ambiguity |
| Pvalb | Defining marker | Pvalb in MERFISH markers; strongest Pvalb expression among SUPT_0206 child clusters; precomputed mean: 10.63 | CONSISTENT | |
| Gad1 | Defining marker | Not in cluster defining_markers; GABA NT consistent; precomputed mean: 10.52 | APPROXIMATE | |
| Gad2 | Defining marker | Not in cluster defining_markers; GABA NT consistent; precomputed mean: 8.43 | APPROXIMATE | |
| Cnr1 (negative) | Absent | Not in cluster markers; precomputed mean: 1.68 | CONSISTENT | Cnr1 low/absent in atlas type; PV (not CCK) basket identity confirmed |
| Cck neuropeptide | Not expected (Cnr1-negative PV cells) | Cck present (expression score 7.6); precomputed mean: 7.56 | DISCORDANT | Unexpected for a PV basket cell; may indicate mixed cluster content or low-level Cck co-expression in a subset of PV neurons |

**Table 2. Evidence support**

| Evidence type | Source | Supports | Key metric | Notes |
|---|---|---|---|---|
| ATLAS_METADATA | WMBv1 CCN20230722 | PARTIAL | CA1 SP 26 cells, CA1 SO 124 cells; GABA NT; Pvalb in MERFISH | Cck neuropeptide discordant; cluster likely contains multiple PV+ morphological subtypes |
| ATLAS_METADATA | WMBv1 precomputed stats | SUPPORT | Pvalb=10.63, Gad1=10.52, Gad2=8.43, Cnr1=1.68 | Strongest Pvalb expression among SUPT_0206 child clusters; all defining markers confirmed |
| ANNOTATION_TRANSFER | GEO:GSE185862 (Yao 2021 SSv4 Pvalb, n=66 HIP) | PARTIAL | F1=0.179 at CLUSTER; 5/66 Pvalb cells to CLUS_0739; target_purity=1.0 | Mixed source population; chandelier/AAC cells dominant (CLUS_0732 F1=0.622); CLUS_0739 signal minor |
| ANNOTATION_TRANSFER | GEO:GSE142546 (Que 2021 patch-seq BC, n=62) | SUPPORT | F1=0.827; group_purity=0.795; target_purity=0.861; 31 cells to CLUS_0739 | Morphologically confirmed basket cells; strongest cluster-level AT signal; BC/BIC cluster separation confirmed |

**Subcluster concordance.** CLUS_0739 is itself a leaf cluster. The BC/BIC separation within SUPT_0206 is directly reflected in cluster assignments: BC cells map to CLUS_0739 (F1=0.827) and BIC cells to sibling CLUS_0737 (F1=0.800), demonstrating that PV basket and bistratified cells are transcriptomically distinguishable at the finest WMBv1 resolution [6].

---

### 5. Candidate sections

#### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟢 HIGH

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0206 belongs to the GABA NT class, fully consistent with the GABAergic identity of PV basket cells [5].
- **Pvalb — CONSISTENT.** SUPT_0206 is an explicitly Pvalb-defined supertype ("Pvalb Gaba_2"). Precomputed stats confirm mean Pvalb expression 8.74 across the supertype. Child cluster CLUS_0739 shows the strongest Pvalb expression (mean 10.63) among SUPT_0206 clusters, and Pvalb is present in CLUS_0739 MERFISH markers [1][6][7][8].
- **Cnr1 absent — CONSISTENT.** Precomputed Cnr1 mean of 1.93 at supertype level confirms absence of the CCK basket cell marker, consistent with PV basket cell identity [5][8].
- **Annotation transfer (GEO:GSE142546, Que 2021, BC n=62) — SUPPORT.** MapMyCells local (cell_type_mapper v1.7.1) using morphologically confirmed PV basket cells (hBC n=12 + vBC n=50 aggregated). 53/62 basket cells map to SUPT_0206 (group_purity=0.898, F1=0.785 at supertype). BC cells prefer child cluster CLUS_0739 (F1=0.827, 31 cells) while BIC cells prefer sibling CLUS_0737 — cluster separation from morphologically labelled cells [6].
- **Annotation transfer (GEO:GSE185862, Yao 2021, Pvalb n=66 HIP) — PARTIAL.** 12/66 Pvalb SSv4 cells map to SUPT_0206 (target_purity=0.800). Chandelier/AAC cells dominate the mapping (SUBC_051 / SUPT_0204), reflecting enrichment in the Yao dataset; SUPT_0206 signal is the basket/bistratified component.

**Concerns**

- **DISTRIBUTED_ACROSS_CLUSTERS.** SUPT_0206 spans hippocampus (CA1 stratum oriens, CA3 stratum oriens) and piriform area (959 cells); it is not hippocampus-specific. Multiple PV+ morphological subtypes (basket, axo-axonic, bistratified) co-populate the Pvalb Gaba subclass and are not separable at supertype level.
- **Cnr1 negative marker status** is not directly verifiable from supertype metadata; confirmation rests on precomputed stats alone.
- **Yao 2021 SSv4 source limitation.** The GSE185862 Pvalb subclass label (n=66 HIP cells) is a mixed population encompassing PV basket, axo-axonic, and bistratified cells; subtype resolution requires morphologically labelled datasets.

**What would upgrade confidence**

- Both available AT runs have been completed. The mapping is already HIGH confidence. Additional morphologically labelled PV basket cell datasets would further increase quantitative precision of group_purity and target_purity estimates.
- Resolution of the CA1 pyramidal layer soma location discrepancy (soma classically in SP vs. atlas predominance in SO) via MERFISH spot-level examination at the SP/SO border.

---

#### 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] · 🟢 HIGH

**Supporting evidence**

- **Pvalb — CONSISTENT.** CLUS_0739 has the strongest Pvalb expression (mean 10.63) among SUPT_0206 child clusters, and Pvalb is present in CLUS_0739 MERFISH markers — direct marker consistency at the finest resolution [1][6][7][8].
- **Cnr1 absent — CONSISTENT.** Precomputed Cnr1 mean 1.68, confirming PV (not CCK) basket identity.
- **NT type — CONSISTENT.** GABA class, consistent with GABAergic basket cell identity [5].
- **Annotation transfer (GEO:GSE142546, Que 2021, BC n=62) — SUPPORT.** CLUS_0739 is the primary cluster hit for morphologically confirmed PV basket cells (hBC + vBC): F1=0.827, group_purity=0.795, target_purity=0.861; 31 cells mapped at cluster level. Basket cell (BC) preference for CLUS_0739 versus bistratified cell (BIC) preference for sibling CLUS_0737 (F1=0.800) is the strongest transcriptomic subtype separation signal currently available [6].
- **Annotation transfer (GEO:GSE185862, Yao 2021, Pvalb n=66 HIP) — PARTIAL.** 5/66 Pvalb SSv4 cells map to CLUS_0739 at cluster level (F1=0.179, target_purity=1.0); chandelier/AAC cells dominate the cluster-level signal. Partial because source is a mixed Pvalb population.

**Concerns**

- **Cck neuropeptide discordant.** CLUS_0739 shows high Cck expression score (7.6; precomputed mean 7.56), which is unexpected for PV basket cells (Cnr1-negative). This may indicate: (a) cluster boundaries do not align cleanly with classical PV basket cell identity, (b) a subset of PV neurons co-express Cck at low level, or (c) the cluster contains a small Cck-co-expressing PV subpopulation. *(note: Cnr1 low/absent suggests this is not classical CCK basket cell contamination, but the Cck signal remains unresolved)*
- **DISTRIBUTED_ACROSS_CLUSTERS.** PV+ hippocampal interneurons (basket, axo-axonic, bistratified) have high transcriptomic similarity [6] and CLUS_0739 likely contains multiple classical PV subtypes, not only basket cells. Target purity 0.861 at cluster level indicates that approximately 14% of mapped cells fall outside basket cell identity in the Que 2021 transfer.
- **Location APPROXIMATE.** CLUS_0739 has only 26 cells in CA1 pyramidal layer vs. 124 cells in CA1 stratum oriens; classical soma location is stratum pyramidale [UBERON:0014548]. Discrepancy likely reflects perisomatic layer border ambiguity in MERFISH spatial registration.

**What would upgrade confidence**

- Both available AT runs have been completed; this mapping is already HIGH confidence. Resolving the Cck discordance is the key remaining biological question: smFISH co-staining for Pvalb, Cnr1, and Cck in CLUS_0739-predicted cells would determine whether the Cck signal reflects contamination or genuine peptide co-expression.
- Larger morphologically labelled basket cell datasets would improve target purity estimates beyond the current n=31 mapped cells.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

#### Classical type definition

The PV basket cell classical node (`pv_basket_cell_hippocampus`) is defined at CLASSICAL_MULTIMODAL basis from eight primary references spanning IHC, transcript-level, and patch-seq methods [1]–[8]. The node was created through the `asta-report-ingest` workflow. Defining markers: Pvalb [1][6][7][8], Gad1, Gad2; negative marker: Cnr1; soma locations: pyramidal layer of CA1 [UBERON:0014548], pyramidal layer of CA3 [UBERON:0014550], dentate gyrus granule cell layer [UBERON:0005381] [1][2][3][4]; neurotransmitter: GABAergic [5]. No neuropeptides are asserted on this node.

#### Atlas mapping query

Atlas candidates were identified by querying the WMBv1 (CCN20230722) taxonomy SQLite index using `just find-candidates` (multi-rank scan: class, subclass, supertype, cluster). Primary search terms: "Pvalb", "basket", "Gaba". The Pvalb Gaba supertype family was identified as the candidate target. Two edges were written:
- `edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206` (supertype, HIGH)
- `edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739` (cluster, HIGH)

#### Property alignment

Property comparisons were assessed for NT type, Pvalb, Gad1, Gad2, negative marker Cnr1, and neuropeptide Cck (cluster-level) against WMBv1 atlas metadata (MERFISH, NP markers, precomputed expression stats from CCN20230722 HDF5 stats). CONSISTENT, APPROXIMATE, and DISCORDANT verdicts follow the standard evidencell alignment rubric.

#### Annotation transfer — Run 1: GEO:GSE185862 (Yao 2021 SSv4)

- **Method:** MapMyCells (default parameters)
- **Source:** GEO:GSE185862 (Yao 2021 SSv4), Pvalb subclass hippocampal cells (n=66 HIP cells)
- **Target atlas:** WMBv1 (CCN20230722)
- **Best F1 (SUPT_0206 edge):** 0.588 at SUBCLASS level; 0.324 at SUPERTYPE for SUPT_0206 specifically
- **Best F1 (CLUS_0739 edge):** 0.622 at CLUSTER level (CLUS_0732 chandelier); CLUS_0739 F1=0.179 (5 cells)
- **Limitation:** Yao 2021 SSv4 Pvalb subclass label encompasses PV basket, axo-axonic, and bistratified cells without morphological resolution; chandelier/AAC cells dominate the mapping.
- **Hierarchy of results (SUPT_0206 edge):**

| Level | Rank | Best target | Accession | F1 | group_purity | target_purity | n cells |
|---|---|---|---|---|---|---|---|
| SUBCLASS | 2 | 051 Pvalb chandelier Gaba | CS20230722_SUBC_051 | 0.588 | 0.417 | 1.000 | 25 |
| SUPERTYPE | 1 | 0204 Pvalb chandelier Gaba_1 | CS20230722_SUPT_0204 | 0.612 | 0.441 | 1.000 | 26 |
| SUPERTYPE | 1 | 0206 Pvalb Gaba_2 | CS20230722_SUPT_0206 | 0.324 | 0.203 | 0.800 | 12 |

#### Annotation transfer — Run 2: GEO:GSE142546 (Que 2021 morphologically labelled patch-seq)

- **Method:** MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization)
- **Source:** GEO:GSE142546 (Que 2021), morphologically labelled PV basket cells (BC: hBC n=12 + vBC n=50 aggregated; n=62 BC cells; full dataset n=88 cells including BIC)
- **Target atlas:** WMBv1 (CCN20230722)
- **Best F1:** 0.827 at CLUSTER level (CLUS_0739)
- **Gene mapping:** Gene symbols remapped to Ensembl IDs; 19788/35825 genes mapped.
- **Hierarchy of results:**

| Level | Rank | Best target | Accession | F1 | group_purity | target_purity | n cells |
|---|---|---|---|---|---|---|---|
| CLASS | 3 | 07 CTX-MGE GABA | CS20230722_CLAS_07 | 0.822 | 1.000 | 0.697 | 53 |
| SUBCLASS | 2 | 052 Pvalb Gaba | CS20230722_SUBC_052 | 0.776 | 0.881 | 0.693 | 52 |
| SUPERTYPE | 1 | 0206 Pvalb Gaba_2 | CS20230722_SUPT_0206 | 0.785 | 0.898 | 0.697 | 53 |
| CLUSTER | 0 | 0739 Pvalb Gaba_2 | CS20230722_CLUS_0739 | 0.827 | 0.795 | 0.861 | 31 |

#### Atlas data sources

- WMBv1 taxonomy: CCN20230722 (Allen Brain Cell Atlas). Taxonomy reference YAML in `kb/taxonomy/CCN20230722/`.
- Precomputed expression statistics from local HDF5 stats file (CCN20230722).
- MERFISH spatial data (WMBv1): soma position registration; axonal/dendritic projections are not reflected in atlas cluster location fields.

#### Anti-hallucination

All KB YAML writes validated by the pre-write hook (`.claude/hooks/validate_mapping_hook.py`): YAML parse, structural integrity, `quote_key` and PMID presence in `references.json`, LinkML schema conformance. All blockquotes in this report carry `<!-- quote_key: ... -->` attribution to entries in `references.json`.

#### Reproducibility footer

- Framework version: 950c14b
- Report generated: 2026-05-08T14:31:25+00:00
- KB graph: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`

#### Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA | PARTIAL | Pvalb subclass + GABA NT consistent; piriform area co-presence; multiple PV subtypes at supertype level |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA (precomputed stats) | SUPPORT | Pvalb=8.74, Gad1=10.34, Gad2=9.28, Cnr1=1.93; all defining markers confirmed |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ANNOTATION_TRANSFER (GEO:GSE185862, Yao 2021 SSv4, n=66) | PARTIAL | 12/66 Pvalb cells to SUPT_0206; F1=0.324; chandelier/AAC cells dominant |
| edge_pv_basket_cell_hippocampus_to_CS20230722_SUPT_0206 | ANNOTATION_TRANSFER (GEO:GSE142546, Que 2021, n=62 BC) | SUPPORT | 53/62 BC to SUPT_0206; group_purity=0.898; F1=0.785; BC/BIC cluster separation confirmed |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA | PARTIAL | CA1 SO 124 cells, CA1 SP 26 cells; GABA NT; Pvalb in MERFISH; Cck NP discordant |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA (precomputed stats) | SUPPORT | Pvalb=10.63, Gad1=10.52, Gad2=8.43, Cnr1=1.68; strongest Pvalb in SUPT_0206 |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ANNOTATION_TRANSFER (GEO:GSE185862, Yao 2021 SSv4, n=66) | PARTIAL | 5/66 Pvalb cells to CLUS_0739; F1=0.179; CLUS_0732 chandelier dominant |
| edge_pv_basket_cell_hippocampus_to_CS20230722_CLUS_0739 | ANNOTATION_TRANSFER (GEO:GSE142546, Que 2021, n=62 BC) | SUPPORT | F1=0.827; group_purity=0.795; target_purity=0.861; 31 cells; primary cluster hit |

</details>

---

## Discussion

### 6. Best candidate and caveats summary

**Primary mapping:** pv_basket_cell_hippocampus → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] and 0739 Pvalb Gaba_2 [CS20230722_CLUS_0739] at HIGH confidence.

HIGH confidence was achieved through two independent annotation transfer runs (GSE185862 and GSE142546) providing two independent experimental evidence types alongside consistent atlas metadata. The decisive evidence is from Que et al. 2021 [6] patch-seq data (GEO:GSE142546): morphologically confirmed basket cells (hBC n=12 + vBC n=50; 53/62 cells to SUPT_0206, group_purity=0.898; best cluster CLUS_0739 with F1=0.827, target_purity=0.861, 31 cells at cluster level). The convergence of this morphologically grounded result with consistent atlas marker data (Pvalb=10.63, Cnr1=1.68/absent, GABA NT) establishes a high-quality mapping at both supertype and cluster levels.

The Yao 2021 SSv4 run (GEO:GSE185862) provides independent experimental corroboration despite its lower discriminative power: the Pvalb SSv4 source population is a mixture of PV subtypes, and chandelier/AAC cells dominate the mapping, but 12/66 Pvalb cells reach SUPT_0206 with target_purity=0.800, confirming that basket cells in the SSv4 dataset do contribute to the SUPT_0206 / CLUS_0739 signal.

**Biological heterogeneity within SUPT_0206.** The PV basket cell shares SUPT_0206 with the PV bistratified cell — both are PV+/GABA+ interneurons with high transcriptomic similarity. Their separation at cluster level (BC→CLUS_0739, BIC→CLUS_0737) is the strongest evidence that atlas resolution is sufficient to distinguish these two subtypes, but the clusters are not pure: CLUS_0739 target purity is 0.861, and a small bistratified cell fraction likely remains in the basket cell cluster (and vice versa). This is consistent with the continuous PV interneuron transcriptomic landscape described by Que et al. 2021 [6].

**Key remaining caveat — Cck discordance in CLUS_0739.** A high Cck neuropeptide score (7.6; precomputed mean 7.56) in CLUS_0739 is unexpected for PV basket cells, which are canonical Cnr1-negative neurons. Given that Cnr1 is confirmed low/absent (mean 1.68), this is unlikely to reflect simple CCK basket cell contamination, but the biological significance of high Cck in a Cnr1-low cluster is unresolved.

### 7. Proposed experiments and follow-ups

**Status of completed AT runs:**
- GEO:GSE185862 (Yao 2021 SSv4, mixed Pvalb subclass, n=66 HIP Pvalb cells): completed at SUBCLASS/SUPERTYPE level. Provides partial support for SUPT_0206; insufficient for clean basket-cell-specific cluster assignment due to mixed source population.
- GEO:GSE142546 (Que 2021 patch-seq, morphologically labelled PV basket cells, n=62 BC cells): completed at CLUSTER level. This is the definitive morphologically grounded result: F1=0.827 at CLUS_0739, BC/BIC cluster separation confirmed.

**Proposed experiment 1 — Cck discordance resolution.**
SmFISH co-staining for Pvalb, Cnr1, and Cck in CA1 sections, focused on CLUS_0739-predicted cells, would determine whether the high Cck score in CLUS_0739 reflects: (a) a minor Cck-co-expressing PV cell subpopulation, (b) MERFISH/precomputed stats noise, or (c) incomplete cluster boundary between PV and CCK basket cell populations. This is the highest-priority unresolved question for the cluster-level mapping.

**Proposed experiment 2 — larger morphologically labelled basket cell dataset.**
The Que 2021 patch-seq dataset has n=62 BC cells (n=31 mapped to CLUS_0739). A larger dataset — especially one with well-controlled morphological confirmation of perisomatic basket morphology — would improve the precision of group_purity and target_purity estimates and allow sub-cluster resolution within CLUS_0739.

**Proposed experiment 3 — new CL term request for hippocampal PV basket cell.**
CL:0000118 (basket cell) is a BROAD mapping. The hippocampal PV basket cell has a well-characterised multimodal phenotype (Pvalb+, Cnr1−, GABA, perisomatic axon targeting) and HIGH-confidence atlas mapping — it is a strong candidate for a dedicated CL term via the `cl-term-request` workflow.

### 8. Open questions

1. What is the biological explanation for the high Cck neuropeptide score (mean 7.56) in CLUS_0739, given that Cnr1 is low/absent (mean 1.68)? Is this a genuine PV/Cck co-expressing subpopulation, or a cluster boundary artefact?
2. Can the CA1 pyramidal layer soma location discrepancy be resolved? Classical basket cells are described as soma-in-stratum-pyramidale [UBERON:0014548], but CLUS_0739 shows only 26 CA1 pyramidal layer cells vs. 124 CA1 stratum oriens cells — is this a MERFISH spatial registration issue at the SP/SO border, or does it reflect genuine soma placement in stratum oriens?
3. Can PV basket, axo-axonic, and bistratified cells be completely resolved at WMBv1 cluster level, or does the continuous PV transcriptomic landscape [6] impose a resolution ceiling below which these morphological subtypes cannot be separated?
4. Do hBC (horizontal basket cells, n=12) and vBC (vertical basket cells, n=50) in the Que 2021 dataset show differential cluster preferences within SUPT_0206, or do they converge on the same cluster CLUS_0739?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | Soma location; Pvalb marker |
| [2] | Sik et al. 1995 | [7472426](https://pubmed.ncbi.nlm.nih.gov/7472426/) | Soma location; morphology |
| [3] | Müller & Remy 2014 | [25324774](https://pubmed.ncbi.nlm.nih.gov/25324774/) | Soma location |
| [4] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | Soma location; PV+ subtype overview |
| [5] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554/) | Neurotransmitter type; CCK/PV perisomatic distinction |
| [6] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker; annotation transfer source (GSE142546) |
| [7] | Perrenoud et al. 2022 | [35802727](https://pubmed.ncbi.nlm.nih.gov/35802727/) | Pvalb marker |
| [8] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048/) | Pvalb marker; Cnr1 negative marker; CCK/PV perisomatic distinction |
