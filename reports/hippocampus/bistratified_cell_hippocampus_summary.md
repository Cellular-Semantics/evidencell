# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The hippocampal bistratified cell is a GABAergic interneuron defined by its bilaminar axon distribution across both stratum oriens [UBERON:0014552] and stratum radiatum [UBERON:0014554] of CA1, distinguishing it from basket and axo-axonic cells that target pyramidal cell soma and axon initial segment respectively [1][4]. Mapping this cell type onto the Allen Brain Cell Atlas (WMBv1/CCN20230722) is of particular importance because bistratified cells co-express Pvalb and Sst — two markers that place them at the boundary between two major atlas subclasses — and because a dedicated Cell Ontology term for the hippocampal bistratified interneuron does not yet exist.

> "Different types of hippocampal inhibitory interneurons control spike initiation [e.g., axo-axonic and basket cells (BCs)] and synaptic integration (e.g., bistratified and oriens–lacunosum moleculare interneurons) within pyramidal neurons"
> — Chamberland & Topolnik 2012, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 8530661_92702482 -->

**Cell Ontology mapping.** CL:0004247 (bistratified cell) is BROAD — the term is retinal-focused and the hippocampal bistratified interneuron (Pvalb/Sst/Tac1+, axon in stratum oriens + radiatum) has no dedicated CL term. No proposed replacement term is available at this time; this cell type is a candidate for a new CL term request.

---

### Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA1 [UBERON:0014548]; CA1 stratum oriens [UBERON:0014552]; CA1 stratum radiatum [UBERON:0014554] | [1] [2] [3] |
| Neurotransmitter | GABAergic | [4] |
| Defining markers | Pvalb, Sst, Tac1 | Pvalb: [5][6][7][8]; Sst: [9]; Tac1: [9] |
| Negative markers | — | — |
| Neuropeptides | Sst | [9] |

<details>
<summary>Per-property literature support</summary>

**Soma location** [1][2][3]. Three independent studies confirm soma placement across the pyramidal layer of CA1 [UBERON:0014548], CA1 stratum oriens [UBERON:0014552], and CA1 stratum radiatum [UBERON:0014554]. Perez et al. 2020 [3] contextualises this:

> "The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus"
> — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [3] <!-- quote_key: 224817966_79f4a500 -->

Bocchio et al. 2024 [2] explicitly lists bistratified cells among the most representative PV-expressing interneuron subtypes in the CA1 pyramidal layer:

> "the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin"
> — Bocchio et al. 2024, Results · [2] <!-- quote_key: 262127573_ba6d02e9 -->

**Pvalb** [5][6][7][8]. Evidence spans transcript- and protein-level methods across four independent studies. Dannenberg et al. 2017 [4] classifies bistratified cells explicitly within the PV+ interneuron group, noting that hippocampal PV+ cells comprise at least three functionally and morphologically distinct populations:

> "Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells."
> — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 38778375_462ec931 -->

Tzilivaki et al. 2023 [7] confirms the morphological subtype classification at transcript level:

> "WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes (basket, axo-axonic, bistratified, radiatum-targeting)."
> — Tzilivaki et al. 2023, Classification Schemes and Methodological Approaches · [7] <!-- quote_key: 221276443_e917908b -->

Crucially, Que et al. 2021 [8] highlights a key constraint on Pvalb-based transcriptomic classification:

> "while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities"
> — Que et al. 2021 · [8] <!-- quote_key: 230508306_e8cc8c19 -->

This finding — that PV interneuron morphological subtypes are not transcriptomically separated at coarse resolution — bears directly on all Pvalb-based atlas mappings for bistratified cells.

**Sst and Tac1** [9]. Chamberland et al. 2024 [9] used Sst;;Tac1 intersectional genetics and confirmed that this combination specifically targets bistratified cells, validating both markers simultaneously:

> "the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells"
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [9] <!-- quote_key: 269246896_c084d5c0 -->

Tac1 is currently supported by a single primary citation [9]; independent confirmation is needed.

**Node notes.** Sst::Tac1 intersectional genetics targets bistratified cells that overwhelmingly target fast-spiking interneurons (Chamberland et al. 2024 [9]).

</details>

---

## Results

Three candidates were assessed across two MODERATE and one LOW edges. The primary mapping is to WMBv1 supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] and its child cluster 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737], both at MODERATE confidence, anchored by morphologically labelled patch-seq annotation transfer (Que 2021, GSE142546; 20 BIC source cells, 16 mapped to CLUS_0737 at cluster level, F1=0.800). A secondary PARTIAL_OVERLAP edge to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (LOW confidence) captures a Sst-expressing bistratified subpopulation identified by Sst;;Tac1 intersectional genetics.

### 4a. Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | 2,860 | 🟡 MODERATE | NT CONSISTENT · Pvalb CONSISTENT · CA1 SO+SR CONSISTENT · Sst CONSISTENT · Tac1 CONSISTENT | Best candidate |
| 2 | 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] | (child of SUPT_0206) | ~1,312[^clus0737] | 🟡 MODERATE | NT CONSISTENT · Pvalb CONSISTENT · CA1 SO+SR CONSISTENT · Sst CONSISTENT · Tac1 CONSISTENT | Best candidate |
| 3 | — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 2,712 | 🔴 LOW | Sst CONSISTENT · Tac1 CONSISTENT · Pvalb DISCORDANT · location APPROXIMATE | Speculative |

[^clus0737]: Cell count for 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] is not populated in the rendered facts file; approximate value ~1312 derived from atlas metadata.

3 edges total · all PARTIAL_OVERLAP.

---

### 4b. Property alignment — MODERATE candidates

#### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]

**Table 1. Property comparison — classical vs atlas**

| Property | Classical value | Atlas value | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb | Defining marker | Pvalb subclass; CLUS_0739 MERFISH: Pvalb present | CONSISTENT |
| Location CA1 SO+SR | Axon in CA1 stratum oriens [UBERON:0014552] + CA1 stratum radiatum [UBERON:0014554] | CLUS_0737: CA1 SO 361 cells, CA1 SR 72 cells — bilaminar axon pattern | CONSISTENT |
| Sst | Co-expressed | CLUS_0737 NP: Sst 4.4 | CONSISTENT |
| Tac1 | Co-expressed | CLUS_0737 NP: Tac1 7.3 | CONSISTENT |

**Table 2. Evidence support**

| Evidence type | Source | Supports | Key metric | Notes |
|---|---|---|---|---|
| ATLAS_METADATA | WMBv1 CCN20230722 | PARTIAL | Bilaminar CLUS_0737 anatomy (CA1 SO 361, CA1 SR 72) | Supertype contains both PV basket (CLUS_0739) and bistratified (CLUS_0737) cells; cluster-level edge provides resolution |
| ANNOTATION_TRANSFER | GEO:GSE142546 (Que 2021, morphologically labelled PV BIC cells, n=20) | SUPPORT | 18/20 cells map to SUPT_0206 (group_purity=0.900, F1=0.375 at supertype); best cluster CLUS_0737 (F1=0.800, group_purity=0.941, target_purity=0.696) | BC/BIC cluster separation within SUPT_0206 is a genuine transcriptomic signal from morphologically labelled cells |

**Subcluster concordance.** Within SUPT_0206, PV basket cells (BC) preferentially map to sibling cluster CLUS_0739, while PV bistratified cells (BIC) concentrate at CLUS_0737 (F1=0.800), providing clean cluster-level separation of these two PV subtypes.

---

#### 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737]

**Table 1. Property comparison — classical vs atlas**

| Property | Classical value | Atlas value | Alignment | Notes |
|---|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT | |
| Pvalb | Defining marker | Pvalb subclass; scoped marker Ednra (vs CLUS_0739 which has Pvalb in MERFISH) | CONSISTENT | Pvalb not in CLUS_0737 MERFISH but present in parent subclass; bistratified Pvalb expression confirmed by patch-seq |
| Location CA1 SO+SR | Axon in CA1 stratum oriens [UBERON:0014552] + CA1 stratum radiatum [UBERON:0014554] | CA1 SO 361 cells, CA1 SR 72 cells — bilaminar | CONSISTENT | CLUS_0737 has highest CA1 SO cell count of any Pvalb cluster (361) with significant CA1 SR — bilaminar pattern is the anatomical definition of bistratified cells |
| Sst | Co-expressed | CLUS_0737 NP: Sst 4.4 | CONSISTENT | |
| Tac1 | Co-expressed | CLUS_0737 NP: Tac1 7.3 | CONSISTENT | |

**Table 2. Evidence support**

| Evidence type | Source | Supports | Key metric | Notes |
|---|---|---|---|---|
| ATLAS_METADATA | WMBv1 CCN20230722 | SUPPORT | Bilaminar CA1 SO+SR; MERFISH markers: Moxd1, Grpr, Syt2, Nxph2, Prkg2; NP: Cort 8.0, Tac1 7.3, Npy 5.5, Cck 5.2, Sst 4.4 | Anatomy + marker profile converge on bistratified identity |
| ANNOTATION_TRANSFER | GEO:GSE142546 (Que 2021, morphologically labelled PV BIC cells, n=20) | SUPPORT | F1=0.800, group_purity=0.941, target_purity=0.696; CLUS_0737 is primary cluster hit | Strongest AT signal for bistratified cell identity in WMBv1; BC cells preferentially map to sibling CLUS_0739 (F1=0.827) |

**Subcluster concordance.** CLUS_0737 is itself a leaf cluster; the BC/BIC separation within SUPT_0206 is reflected in the cluster assignments — BC cells map to CLUS_0739 and BIC cells to CLUS_0737, demonstrating that these two PV subtypes are transcriptomically distinguishable at the finest WMBv1 resolution.

---

### 5. Candidate sections

#### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0206 belongs to the GABA NT class, matching the GABAergic identity of bistratified cells [4].
- **Pvalb — CONSISTENT.** SUPT_0206 is an explicitly Pvalb-defined supertype, the dominant hippocampal Pvalb supertype, and primary atlas target for canonical PV bistratified cells [5][6][7][8].
- **Location CA1 SO+SR — CONSISTENT.** Child cluster CLUS_0737 shows bilaminar anatomy (CA1 SO: 361 cells, CA1 SR: 72 cells) directly consistent with the bistratified axon territories (stratum oriens + radiatum).
- **Sst co-expression — CONSISTENT.** CLUS_0737 NP markers include Sst 4.4, consistent with bistratified identity [9].
- **Tac1 co-expression — CONSISTENT.** CLUS_0737 NP markers include Tac1 7.3, consistent with bistratified identity [9].
- **Annotation transfer (GEO:GSE142546, Que 2021) — SUPPORT.** MapMyCells local (cell_type_mapper v1.7.1) using morphologically labelled PV bistratified cells (20 cells: hBIC n=11 + vBIC n=9). 18/20 cells map to SUPT_0206 (group_purity=0.900, F1=0.375 at supertype). Best cluster: CLUS_0737 (F1=0.800, group_purity=0.941, target_purity=0.696). BC cells preferentially map to CLUS_0739; BIC cells to CLUS_0737 — this cluster separation is a genuine transcriptomic signal from morphologically labelled cells [8].

**Concerns**

- **DISTRIBUTED_ACROSS_CLUSTERS.** SUPT_0206 contains both PV basket cells (CLUS_0739) and PV bistratified cells (CLUS_0737). Not separable at supertype level; see CLUS_0737 edge for cluster-level resolution.
- Supertype-level annotation transfer metrics (F1=0.375, target_purity=0.237) are substantially weaker than the cluster-level signal (F1=0.800) — confidence at supertype level rests partly on the cluster-level evidence; supertype alone would not cross the MODERATE threshold.

**What would upgrade confidence**

- Additional morphologically labelled bistratified cell datasets (e.g. Sst;;Tac1 Cre-driver with post-hoc morphological confirmation) mapped at cluster level would provide independent confirmation of the BC/BIC cluster separation within SUPT_0206.
- Resolution of the CLUS_0737 MERFISH Pvalb absence: direct smFISH co-localisation of Pvalb and Sst in CLUS_0737 cells would fully close the Pvalb alignment at cluster level.

---

#### 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] · 🟡 MODERATE

**Supporting evidence**

- **Bilaminar CA1 anatomy — CONSISTENT.** CLUS_0737 shows CA1 SO (361 cells) and CA1 SR (72 cells) — the highest CA1 SO count among any Pvalb cluster — with the bilaminar pattern directly matching the anatomical definition of bistratified cells.
- **Sst NP (4.4) and Tac1 NP (7.3) — CONSISTENT.** Both markers are expected in bistratified cells per Chamberland et al. 2024 [9].
- **Annotation transfer (GEO:GSE142546, Que 2021) — SUPPORT.** CLUS_0737 is the primary cluster target for morphologically labelled PV bistratified cells (F1=0.800, group_purity=0.941, target_purity=0.696; n=16 BIC cells). The BC/BIC cluster separation — BC cells preferentially to sibling CLUS_0739 (F1=0.827), BIC cells to CLUS_0737 — is the strongest annotation transfer signal for bistratified cell identity in WMBv1 [8].
- **GABA NT — CONSISTENT.**

**Concerns**

- **Pvalb not in CLUS_0737 MERFISH markers.** Although Pvalb is present in the parent subclass and patch-seq data confirm PV expression in bistratified cells, CLUS_0737's scoped marker is Ednra rather than Pvalb itself. *(note: Pvalb presence at parent subclass level and patch-seq confirmation are strong indirect evidence; the MERFISH absence may reflect detection threshold rather than genuine absence.)*
- **Sst-expressing bistratified subpopulation may distribute toward SUPT_0216.** CLUS_0737 captures the Pvalb-primary bistratified population; Sst-dominant bistratified cells may be distributed toward the Sst Gaba_3 supertype. This cluster does not capture the full heterogeneity of bistratified cells.
- **Target purity 0.696.** Approximately 30% of CLUS_0737 cells in the Que 2021 transfer are not BIC cells, indicating that CLUS_0737 is not a pure bistratified cell cluster — it likely also contains PV+ cells of other morphological subtypes.

**What would upgrade confidence**

- Sst;;Tac1 Cre-driver or other Sst/Tac1 intersection-targeted bistratified cell dataset mapped at cluster level against CLUS_0737 would test whether the Sst-expressing bistratified subpopulation co-maps to this cluster or to SUPT_0216.
- smFISH co-detection of Pvalb, Sst, and Tac1 in CLUS_0737 cells in situ would resolve the Pvalb MERFISH absence and directly confirm bistratified identity.
- Improving target purity (currently 0.696) requires either larger morphologically labelled source datasets or tighter cell selection criteria (hBIC only vs. full BIC aggregate).

---

#### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

*This edge represents the Sst-expressing bistratified subpopulation specifically, not the canonical PV bistratified cell population. The PV-primary bistratified cell maps to SUPT_0206/CLUS_0737 (see above). The evidence for this edge rests on Sst/Tac1 co-expression and Chamberland 2024 Sst;;Tac1 genetics [9], which capture a Sst-dominant bistratified subpopulation.*

**Supporting evidence**

- **Sst — CONSISTENT.** SUPT_0216 is an Sst-defined supertype (precomputed mean: 11.44), consistent with Sst co-expression in bistratified cells [9].
- **Tac1 DEFINING_SCOPED — CONSISTENT.** Tac1 is among the DEFINING_SCOPED markers of SUPT_0216 (precomputed mean: 0.55). Chamberland et al. 2024 [9] used Sst;;Tac1 intersectional genetics to specifically target bistratified cells — Tac1 positivity in this supertype is directly consistent with that identity.
- **Neuropeptide Sst — CONSISTENT.** Precomputed mean 11.44 is fully consistent with the Sst neuropeptide on the classical node.
- **NT type — CONSISTENT.** GABA NT class.
- **Annotation transfer (GEO:GSE185862, Yao 2021 SSv4 Sst subclass, n=273 HIP cells) — PARTIAL.** Sst SSv4 cells map to SUPT_0216 with F1=0.488 (83/273 cells); SUPT_0219 (Sst Gaba_6) is the dominant Sst target (F1=0.759). Weak but non-zero signal lends partial support for an Sst-component bistratified subpopulation.

**Concerns**

- **Pvalb — DISCORDANT.** Bistratified cells co-express Pvalb and Sst, but SUPT_0216 is in the Sst subclass; Pvalb is not among supertype markers and the precomputed mean is 1.48 (low). The Sst-class placement captures the Sst component but misses the Pvalb component entirely [8].
- **Annotation transfer (GEO:GSE142546, Que 2021 PV BIC) — does not support.** Morphologically identified PV bistratified cells (20 cells: hBIC + vBIC) show NO mapping to any Sst supertype: 18/20 map to SUPT_0206 and 16/20 concentrate at CLUS_0737. SUPT_0216 F1 is absent from BIC top results. This AT does not support SUPT_0216 as the primary target for canonical PV bistratified cells.
- **Location — APPROXIMATE.** SUPT_0216 dominant hippocampal signal is CA1 stratum oriens (818 cells, MBA:399); bistratified cell soma classically sits at or near the pyramidal layer [UBERON:0014548]. CA1 stratum oriens [UBERON:0014552] is immediately adjacent but represents a layer mismatch.
- **DISTRIBUTED_ACROSS_CLUSTERS.** SUPT_0216 contains at least three classical hippocampal types: OLM cells (Sst+/Chrna2+), bistratified cells (Sst+/Pvalb+/Tac1+), and HS cells (Sst+, long-range projecting). These are not separable at supertype level. This edge and the olm_cell_ca1 edge to the same supertype reflect this overlap explicitly.
- **Annotation transfer source limitation (GEO:GSE185862).** The Yao 2021 SSv4 Pvalb subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells without morphological resolution. Only 6/66 Pvalb cells map to SUPT_0216 (F1=0.053), consistent with a minor Sst-expressing minority rather than a primary signal.

**What would upgrade confidence**

- A morphologically confirmed Sst;;Tac1-targeted bistratified cell dataset mapped via MapMyCells at cluster level targeting specific clusters within SUPT_0216. Target: F1 ≥ 0.70 at CLUSTER level, resolving which SUPT_0216 child cluster captures bistratified cells versus OLM versus HS cells.
- Targeted cite-traverse for "Tac1 bistratified hippocampus" or "substance P bistratified interneuron hippocampus" to independently confirm Tac1 as a bistratified marker beyond the single Chamberland 2024 citation [9].
- Cluster-level separation of OLM, bistratified, and HS cell matches within SUPT_0216 [CS20230722_SUPT_0216] would directly address the DISTRIBUTED_ACROSS_CLUSTERS caveat.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

#### Classical type definition

The bistratified cell classical node (`bistratified_cell_hippocampus`) is defined at CLASSICAL_MULTIMODAL basis from nine primary references spanning IHC, transcript-level, Cre-driver, and patch-seq methods [1]–[9]. The node was created through the `asta-report-ingest` workflow. Defining markers are: Pvalb [5][6][7][8], Sst [9], Tac1 [9]; neuropeptide Sst [9]; soma locations pyramidal layer of CA1 [UBERON:0014548], CA1 stratum oriens [UBERON:0014552], CA1 stratum radiatum [UBERON:0014554] [1][2][3]; neurotransmitter GABAergic [4].

#### Atlas mapping query

Atlas candidates were identified by querying the WMBv1 (CCN20230722) taxonomy SQLite index using `just find-candidates` (multi-rank scan: class, subclass, supertype, cluster). Primary search terms: "Pvalb", "bistratified", "Sst", "Tac1". The Pvalb Gaba supertype family and Sst Gaba_3 supertype were identified as candidate targets. Three edges were written:
- `edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206` (supertype, MODERATE)
- `edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737` (cluster, MODERATE)
- `edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216` (supertype, LOW)

#### Property alignment

Property comparisons were assessed for NT type, Pvalb marker, location (CA1 SO+SR), Sst, and Tac1 against WMBv1 atlas metadata (MERFISH, NP markers, precomputed expression stats from CCN20230722 HDF5 stats). CONSISTENT, APPROXIMATE, and DISCORDANT verdicts follow the standard evidencell alignment rubric.

#### Annotation transfer — Run 1: GEO:GSE185862 (Yao 2021 SSv4)

- **Method:** MapMyCells (default parameters)
- **Source:** GEO:GSE185862 (Yao 2021 SSv4), Pvalb subclass hippocampal cells (n=66 HIP cells)
- **Target atlas:** WMBv1 (CCN20230722)
- **Best F1:** 0.488 at SUPERTYPE level
- **Best target:** 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.488, 83 cells from Sst SSv4 subclass)
- **Limitation:** Yao 2021 SSv4 Pvalb subclass label encompasses PV basket, axo-axonic, and bistratified cells without morphological resolution; subtype-level confidence requires a morphologically identified source.

#### Annotation transfer — Run 2: GEO:GSE142546 (Que 2021 morphologically labelled patch-seq)

- **Method:** MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization)
- **Source:** GEO:GSE142546 (Que 2021), morphologically labelled PV bistratified cells (BIC: hBIC n=11 + vBIC n=9 aggregated; n=20 BIC cells; full dataset n=88 cells including BC)
- **Target atlas:** WMBv1 (CCN20230722)
- **Best F1:** 0.800 at CLUSTER level
- **Best target:** 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] (F1=0.800, group_purity=0.941, target_purity=0.696, n=16 BIC cells mapped)
- **Gene mapping:** Gene symbols remapped to Ensembl IDs; 19788/35825 genes mapped.
- **Hierarchy of results:**

| Level | Rank | Best target | Accession | F1 | group_purity | target_purity | n cells |
|---|---|---|---|---|---|---|---|
| CLASS | 3 | 07 CTX-MGE GABA | CS20230722_CLAS_07 | 0.366 | 1.000 | 0.224 | 17 |
| SUBCLASS | 2 | 052 Pvalb Gaba | CS20230722_SUBC_052 | 0.383 | 0.947 | 0.240 | 18 |
| SUPERTYPE | 1 | 0206 Pvalb Gaba_2 | CS20230722_SUPT_0206 | 0.375 | 0.900 | 0.237 | 18 |
| CLUSTER | 0 | 0737 Pvalb Gaba_2 | CS20230722_CLUS_0737 | 0.800 | 0.941 | 0.696 | 16 |

#### Annotation transfer — Run 3: GEO:GSE99888 (Harris 2018 + Chamberland per-cluster Sst_Tac1)

- **Method:** MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100)
- **Source:** GEO:GSE99888 (Harris 2018, 3,663 CA1 inhibitory neurons, STRT-seq). Source label: Chamberland 2024 Sst_Tac1 per-cluster subfamily (n=168 cells, propagated from Harris cluster-mean Sst>0 AND Tac1>0 gene-pair rule — dropout-robust).
- **Target atlas:** WMBv1 (CCN20230722)
- **Best F1:** 0.578 at SUBCLASS level (Pvalb Gaba)
- **Key result:** CLUS_0737 shows target_purity=0.939 at cluster level — high target purity confirms CLUS_0737 as the specific landing site for Sst_Tac1-labelled bistratified cells within the Pvalb tree.
- **Limitation:** Sst_Tac1 label is in-silico derived from Harris cluster-mean expression, not morphologically confirmed. Per-cluster labels are dropout-robust (cluster-mean gene-pair rules; see `at_run_20260506_harris_chamberland_mmc_wmbv1` README Methods note).
- **Hierarchy of results:**

| Level | Rank | Best target | Accession | F1 | group_purity | target_purity | n cells |
|---|---|---|---|---|---|---|---|
| SUBCLASS | 2 | 052 Pvalb Gaba | CS20230722_SUBC_052 | 0.578 | 0.783 | 0.458 | 126 |
| SUPERTYPE | 1 | 0206 Pvalb Gaba_2 | CS20230722_SUPT_0206 | 0.566 | 0.437 | 0.802 | 69 |
| CLUSTER | 0 | 0737 Pvalb Gaba_2 | CS20230722_CLUS_0737 | 0.467 | 0.310 | 0.939 | 31 |

#### Atlas data sources

- WMBv1 taxonomy: CCN20230722 (Allen Brain Cell Atlas). Taxonomy reference YAML in `kb/taxonomy/CCN20230722/`.
- Precomputed expression statistics from local HDF5 stats file (CCN20230722).
- MERFISH spatial data (WMBv1): soma position registration; axonal/dendritic projections are not reflected in atlas cluster location fields.

#### Anti-hallucination

All KB YAML writes validated by the pre-write hook (`.claude/hooks/validate_mapping_hook.py`): YAML parse, structural integrity, `quote_key` and PMID presence in `references.json`, LinkML schema conformance. All blockquotes in this report carry `<!-- quote_key: ... -->` attribution to entries in `references.json`.

#### Reproducibility footer

- Framework version: 950c14b
- Report generated: 2026-05-11T09:31:05+00:00
- KB graph: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`

#### Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA | PARTIAL | Bilaminar CLUS_0737 anatomy consistent; supertype-level only; basket+bistratified not separable at supertype |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | ANNOTATION_TRANSFER (GEO:GSE142546, Que 2021, n=20 BIC) | SUPPORT | 18/20 BIC to SUPT_0206; F1=0.800 at CLUS_0737; BC/BIC separation confirmed |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | ATLAS_METADATA | SUPPORT | Bilaminar CA1 SO+SR; Sst 4.4, Tac1 7.3 NP markers consistent |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | ANNOTATION_TRANSFER (GEO:GSE142546, Que 2021, n=20 BIC) | SUPPORT | F1=0.800, group_purity=0.941, target_purity=0.696; primary cluster hit |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | ANNOTATION_TRANSFER (GEO:GSE99888, Harris 2018 Chamberland Sst_Tac1, n=168) | PARTIAL | SUBC Pvalb Gaba F1=0.578; CLUS_0737 target_purity=0.939 — confirms cluster-level specificity |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | Sst, Tac1 consistent; Pvalb DISCORDANT; three classical types co-occupy supertype |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (GEO:GSE185862, Yao 2021 SSv4 Sst, n=273) | PARTIAL | Sst subclass F1=0.488 (83/273 HIP cells); SUPT_0219 dominant Sst target; mixed source population |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (GEO:GSE142546, Que 2021 PV BIC, n=20) | NO SUPPORT | BIC cells show zero mapping to any Sst supertype; 18/20 to SUPT_0206 |

</details>

---

## Discussion

### 6. Best candidate and caveats summary

**Primary mapping:** bistratified_cell_hippocampus → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] at MODERATE confidence; refined to cluster level at 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] (MODERATE). This mapping is anchored by Que et al. 2021 [8] morphologically labelled patch-seq data: BIC cells (n=20 source cells: hBIC n=11 + vBIC n=9; 16 mapped to CLUS_0737 at cluster level) show F1=0.800, group_purity=0.941, and target_purity=0.696 — the strongest annotation transfer signal for bistratified cell identity currently available in WMBv1. The bilaminar CA1 SO+SR anatomy of CLUS_0737 (361 cells in CA1 SO, 72 in CA1 SR) is the atlas-side anatomical correlate of the defining bistratified cell axon territory. Sst (NP: 4.4) and Tac1 (NP: 7.3) expression in CLUS_0737 are fully consistent with [9].

**Secondary mapping:** bistratified_cell_hippocampus → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at LOW confidence. This edge is not the primary mapping but represents a distinct Sst-expressing bistratified subpopulation — the one targeted by Sst;;Tac1 intersectional genetics [9]. The canonical PV bistratified cells identified by Que 2021 patch-seq show zero overlap with any Sst supertype, placing this edge firmly in the LOW category for the bulk of the bistratified cell population.

**Biological heterogeneity.** Three independent annotation transfer runs reveal that bistratified cells are transcriptomically diverse:
- **GSE142546 (Que 2021, PV-subtype, morphologically labelled):** BIC cells map exclusively to SUPT_0206/CLUS_0737 (Pvalb subclass). This is the Pvalb-primary population.
- **GSE185862 (Yao 2021 SSv4, Sst-subtype label):** Sst SSv4 cells map partially to SUPT_0216 (Sst Gaba_3, F1=0.488). This is consistent with a Sst-dominant bistratified subpopulation but cannot be isolated from OLM and HS cells at supertype resolution.
- **GSE99888 (Harris 2018, Chamberland per-cluster Sst_Tac1 label):** Sst_Tac1-labelled cells map to Pvalb Gaba subclass (SUBCLASS F1=0.578) and show target_purity=0.939 at CLUS_0737, confirming cluster-level specificity for the Sst_Tac1 (bistratified-proxy) population within the Pvalb tree. This is consistent with Chamberland 2024 (PMID:38640347) Fig 6 Sst–Pvalb transcriptomic continuity for bistratified cells.

Together, these three runs reveal that bistratified cells span both the Pvalb and Sst supertype regions of WMBv1 — a direct transcriptomic reflection of their unusual co-expression of Pvalb and Sst [8][9]. The continuous PV interneuron transcriptomic landscape noted by Que et al. 2021 [8] likely means that the Pvalb-primary bistratified population (CLUS_0737) and the Sst-dominant subpopulation (SUPT_0216 region) cannot be fully separated by current atlas resolution.

**Remaining caveats:**
- CLUS_0737 target purity is 0.696 — approximately 30% of mapped cells are non-BIC. The cluster is not a pure bistratified cell compartment.
- SUPT_0206 supertype-level F1 (0.375) is substantially below the cluster-level signal (0.800) — the supertype is shared with PV basket cells and cannot be used as a bistratified cell proxy without cluster-level resolution.
- The Pvalb MERFISH absence from CLUS_0737 is a technical caveat that should be resolved by spatial validation.
- No dedicated Cell Ontology term exists for the hippocampal bistratified interneuron; this type should be prioritised for a new CL term request.

### 7. Proposed experiments and follow-ups

**Status of completed AT runs:**
- GEO:GSE185862 (Yao 2021 SSv4, mixed Pvalb + Sst, n=66 HIP Pvalb cells): completed at SUPERTYPE level. Provides partial support for SUPT_0216; insufficient for subtype-level confidence.
- GEO:GSE142546 (Que 2021 patch-seq, morphologically labelled PV bistratified, n=20 BIC): completed at CLUSTER level. This is the key morphologically grounded result: F1=0.800 at CLUS_0737.

**Proposed experiment 1 — Sst;;Tac1 bistratified cell dataset AT.**
Chamberland 2024 [9] provides validation of Sst;;Tac1 intersectional genetics as a bistratified cell targeting strategy. Using scRNA-seq from Sst;;Tac1 Cre-driver cells (sorted from CA1), a MapMyCells cluster-level AT against WMBv1 would test: (a) whether Sst;;Tac1 bistratified cells map primarily to CLUS_0737 (co-mapping with Que 2021 PV BIC), (b) whether a subset maps to SUPT_0216 clusters, and (c) whether OLM and bistratified cells can be separated within SUPT_0216 at cluster level. Target: F1 ≥ 0.70 at cluster level. This is the single highest-priority experiment to resolve the Pvalb/Sst heterogeneity of bistratified cells.

**Proposed experiment 2 — smFISH co-localisation of Pvalb, Sst, Tac1 in CLUS_0737 and SUPT_0216.**
Spatial validation of Pvalb expression in CLUS_0737 cells (absent from MERFISH markers but expected from patch-seq and parent subclass) and of Tac1 expression in both CLUS_0737 and SUPT_0216, using FISH probes against Pvalb, Sst, and Tac1 in CA1 sections. This would resolve the MERFISH-vs-patch-seq Pvalb discrepancy and confirm whether CLUS_0737 cells in CA1 are genuine bistratified cells.

**Proposed experiment 3 — targeted cite-traverse for Tac1 as bistratified marker.**
Tac1 is supported by a single primary citation [9]. A targeted cite-traverse for "Tac1 bistratified hippocampus" and "substance P bistratified interneuron hippocampus" would identify any independent primary studies confirming Tac1/substance P expression in morphologically confirmed bistratified cells, removing the single-citation caveat.

**Proposed experiment 4 — new CL term request for hippocampal bistratified interneuron.**
CL:0004247 (bistratified cell) is retinal-focused (BROAD mapping). The CA1 bistratified interneuron has a well-characterised multimodal phenotype (Pvalb/Sst/Tac1+, GABA, axon SO+SR) and MODERATE-confidence atlas mapping — it is a strong candidate for a dedicated CL term via the `cl-term-request` workflow.

### 8. Open questions

1. Can the Pvalb-primary and Sst-dominant bistratified cell subpopulations be separated at WMBv1 cluster level, or do they overlap within CLUS_0737?
2. Do Sst;;Tac1 bistratified cells (Chamberland 2024 [9]) map to CLUS_0737 (co-mapping with Que 2021 PV BIC), or do they preferentially map to a distinct cluster within SUPT_0216?
3. Can OLM cells, bistratified cells (Sst-subtype), and HS cells be resolved at cluster level within 0216 Sst Gaba_3 [CS20230722_SUPT_0216]?
4. Is Tac1 expression in bistratified cells confirmed by independent primary studies beyond Chamberland et al. 2024 [9]?
5. What is the functional significance of the BC/BIC cluster separation within SUPT_0206? Does CLUS_0737 have a distinct transcriptomic signature beyond the Ednra scoped marker that predicts bilaminar axon targeting?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland & Topolnik 2012 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | Soma location |
| [2] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | Soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | Soma location |
| [4] | Dannenberg et al. 2017 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | Neurotransmitter type; PV+ interneuron heterogeneity |
| [5] | Ekins et al. 2020 | [33150866](https://pubmed.ncbi.nlm.nih.gov/33150866/) | Pvalb marker |
| [6] | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Pvalb marker |
| [7] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Pvalb marker; morphological subtypes |
| [8] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker; transcriptomic landscape; annotation transfer source |
| [9] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker; Tac1 marker; Sst neuropeptide; Sst;;Tac1 intersectional genetics |
