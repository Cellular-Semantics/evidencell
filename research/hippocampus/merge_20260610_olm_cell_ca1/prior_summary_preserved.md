# Oriens-Lacunosum Moleculare (O-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

Oriens-lacunosum moleculare (O-LM) cells are GABAergic interneurons whose somata
lie in CA1 stratum oriens [UBERON:0014552] and whose axons innervate the distal
apical dendrites of CA1 pyramidal cells in CA1 stratum lacunosum moleculare
[UBERON:0014557], where they gate temporoammonic input and shape dendritic
integration [1][3][5]. Identifying them in single-cell transcriptomic atlases is
biologically consequential — O-LM cells underlie input gating and feedback
inhibition in CA1, and their distinctive *Sst*+/*Reln*+/*Chrna2*+/*Pvalb*−
profile [4][6] is reported across multiple labs but is partly shared with
other CA1 stratum oriens *Sst*+ interneurons (bistratified, hippocampo-septal,
oriens-oriens, LM-projecting types), making source-label specificity a
recurring problem for annotation transfer.

### Classical type — properties

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552]; CA1 stratum lacunosum moleculare [UBERON:0014557] (dendritic tuft target) | [1][2][3][4][5][6][7] |
| NT | GABAergic | [4] |
| Defining markers | *Sst*; *Chrna2*; *Reln* | [4][5][6][8] |
| Negative markers | *Pvalb* (sparse only) | [4] |
| Neuropeptides | *Sst*; *Npy*; *Pnoc* | [4] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma / projection (CA1 stratum oriens; SLM tuft target):** review compilation · CA1 anatomy · [1]
  > Hippocampal CA1 stratum oriens interneuron subtypes include oriens lacunosum-moleculare (O-LM) interneurons, which can be identified by the expression of somatostatin and have regular-to-fast action potential spiking patterns (Oren et al., 2009)(Nicholson et al., 2014)(Huh et al., 2016). O-LM cell soma and dendrites reside in the stratum oriens and their axons project to the stratum lacunosum-moleculare layer
  > — Friend et al. 2019, Electrophysiological Properties and Function · [1] <!-- quote_key: 116862536_5f5f2ae8 -->
- **Connectivity (apical tuft of CA1 pyramidal cells):** review compilation · CA1 connectivity · [2]
  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [2] <!-- quote_key: 229694907_6865b9db -->
- **Anatomy + Sst marker (review of mouse CA1 interneuron taxonomy):** quantitative compilation · CA1 stratum oriens · [3]
  > oriens-lacunosum moleculare (O-LM) cells (these SOM+ cells project to the distal dendrites in the stratum lacunosum-moleculare though their somata are located in the stratum oriens)
  > — Bezaire et al. 2016, Molecular Markers and Gene Expression · [3] <!-- quote_key: 4776309_dd48b1ec -->
- **NT type (GABAergic identity, transcript-level):** scRNA-seq on Cre-driver-targeted OLM cells · mouse CA1 · [4]
  > Independent of the Cre line used for cell collection, we found consistent expression of GABA release‐related Gad1, Gad2 and Slc6a1 in all OLM interneurons. By contrast, glutamate release‐related vesicular glutamate transporter Slc17a7 (detected in 2/46 cells) and Slc17a6 (detected in 1/46 cells) genes were virtually not expressed across the whole population.
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d024a35 -->
- **Sst, Reln defining markers; Pvalb sparse:** scRNA-seq, Cre-driver targeted, morphology recovery · [4]
  > we found consistent expression of Sst and Reln, and sparse expression of Pvalb across both OLM neuron types
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_2d5a5fb3 -->
- **Chrna2 defining marker (OLM-specific in CA1):** review of *Chrna2* as a hippocampal OLM marker · [6]
  > The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
  > — Nichol et al. 2018, Anatomical Location and Morphology · [6] <!-- quote_key: 3591966_644f1e68 -->
- **Chrna2 detection in Cre-targeted OLM cells:** scRNA-seq, Cre-driver targeted · [4]
  > as well as expression of Chrna2, which has been used as a marker for hippocampal OLM interneurons
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_bd56f851 -->
- **Npy neuropeptide (consistent in mouse OLM, resolving older rat/mouse discrepancy):** scRNA-seq, Cre-driver targeted · [4]
  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [4] <!-- quote_key: 201041756_8d16e821 -->
- **Pnoc neuropeptide (across both Sst-Cre and Htr3a-Cre cohorts):** scRNA-seq, Cre-driver targeted · [4]
  > we detected Pnoc in both Htr3aCre‐OLM (14/23) and SstCre‐OLM (13/23)
  > — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d20426d -->
- **Sub-stratum-oriens stratification (Chrna2-INs deepest):** in-silico gene-pair subfamilies, IHC + ISH · CA1 stratum oriens depth · [7]
  > While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
  > — Chamberland et al. 2024, Results · [7] <!-- quote_key: 269246896_1b1ebab4 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Marker concordance across the *Sst*/*Chrna2*/*Reln*/*Npy*/*Pnoc*/*Pvalb*−
panel together with annotation transfer evidence from morphologically and
electrophysiologically confirmed Cre-driver-targeted O-LM cohorts (Winterer
2019; see figure and property comparison table) places the O-LM cell on the
*Sst Gaba_3* supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216], with cluster
0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the leading cluster-level candidate
within that supertype. Cluster-level scatter across multiple *Sst Gaba_3*
children — visible in the AT figure below — is consistent with reported
within-O-LM molecular heterogeneity (multiple *Pnoc* / *Chrna2*+
subpopulations) and prevents committing to a single cluster identity at
HIGH confidence.

![Filtered AT figure for O-LM cell (Winterer 2019 pool)](figures/f1_for_olm_hippocampus.png)

*F1 across taxonomy levels for the Winterer 2019 OLM cohort (Sst-Cre OLM + Htr3a-Cre OLM pooled into a single OLM group; n=46 source cells). Coverage = fraction of source-group cells landing on the target; Purity = fraction of target cells from the source group. With a single pooled source, Purity is 1.0 at every target and only Coverage discriminates. The pooled OLM cohort lands cleanly at class 07 CTX-MGE GABA and subclass 053 Sst Gaba; converges on supertype 0216 Sst Gaba_3 (F1=0.97, n=43 of 46 OLM cells) and then scatters across multiple Sst Gaba_3 child clusters, with 0768 Sst Gaba_3 as the leading cluster (F1=0.65, n=22).*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Supporting evidence:**
- Annotation transfer from Cre-driver-targeted O-LM cells with morphology recovery and post-hoc electrophysiology (Winterer 2019) converges on this supertype: 43 of 46 pooled Sst-Cre and Htr3a-Cre OLM cells map here, with the remaining three scattered singly across other supertypes (see figure caption for sidecar-grounded metrics). This is direct evidence of the classical-to-transcriptomic correspondence rather than generic *Sst* convergence.
- Independent annotation transfer of Harris 2018 CA1 inhibitory class `Sst.Pnoc.Calb1.Igfbp5` — Harris's OLM-type cluster — gives F1=0.51 against this supertype with coverage=0.97, confirming the same supertype destination from a different scRNA-seq dataset and source-label scheme.
- Sub-resolution within the supertype: Harris 2018 cells re-labelled by Chamberland's in-silico gene-pair *Chrna2*-OLM subfamily (per-cluster, dropout-robust) map to 0771 Sst Gaba_3 with F1=0.65; coverage=0.81 — *(note: CS20230722_CLUS_0771 is a child of this supertype but is not currently carried as a top-K edge in this graph; surfaced here only for the supertype-level convergence story)*.
- Marker concordance is strong: *Sst* (val=11.44; cohort percentile 0.905; child-cluster coverage 1.000), *Reln* (val=7.90; cohort percentile 0.825; child-cluster coverage 1.000; atlas DEFINING category), *Chrna2* (val=0.61; cohort percentile 0.952; child-cluster coverage 0.667), and the *Npy* / *Pnoc* neuropeptides all CONSISTENT at supertype level — see property comparison table below.

**Property comparison (Table 1).**

| Property | Classical | Supertype 0216 | Best cluster 0768 | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | Field CA1, stratum oriens [MBA:399] count_100um=1463; region_fraction_100um 0.539 | Field CA1, stratum oriens [MBA:399] count_100um=261; region_fraction_100um 0.818 | CONSISTENT |
| NT type | GABAergic | not asserted on supertype | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| *Sst* (defining) | defining marker | val=11.44; cohort_pct 0.905; child-cov 1.000 | val=12.70; cohort_pct 0.992 | CONSISTENT |
| *Chrna2* (defining) | defining marker | val=0.61; cohort_pct 0.952; child-cov 0.667 | val=0.57; cohort_pct 0.950 | CONSISTENT |
| *Reln* (defining) | defining marker | val=7.90; cohort_pct 0.825; child-cov 1.000 | val=10.65; cohort_pct 0.975 | CONSISTENT |
| *Pvalb* (negative) | absent | val=1.48; cohort_pct 0.778 | val=3.12; cohort_pct 0.866 | DISCORDANT |
| *Sst* (neuropeptide) | neuropeptide | val=11.44; cohort_pct 0.905 | val=12.70; cohort_pct 0.992 | CONSISTENT |
| *Npy* (neuropeptide) | neuropeptide | val=5.07; cohort_pct 0.794 | val=7.58; cohort_pct 0.857 | CONSISTENT |
| *Pnoc* (neuropeptide) | neuropeptide | val=3.69; cohort_pct 0.667; child-cov 0.889 | val=2.51; cohort_pct 0.479 | SUPT: CONSISTENT; CLUS: APPROXIMATE |

*(8 of 9 child clusters within Sst Gaba_3 show *Chrna2* coverage; *Sst*, *Reln*, *Npy* concordant in 100% of child clusters with measurable expression. *Pnoc* is concordant in 8 of 9 children — depleted on 0768 specifically. Best match: CS20230722_CLUS_0768.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata + GSE124847 supertype membership | Atlas metadata | PARTIAL | OLM cells map to Sst Gaba_3 supertype; supertype mixes O-LM, bistratified, HS | atlas-internal |
| Precomputed stats marker panel | Atlas metadata | SUPPORT | *Sst*=11.44, *Reln*=7.90, *Chrna2*=1.53, *Npy*=5.07, *Pnoc*=3.69, *Pvalb*=1.48 | atlas-internal |
| Yao 2021 GSE185862 SSv4 *Sst* subclass (HIP) | Annotation transfer | PARTIAL | F1=0.98 at subclass 053 Sst Gaba; supertype-level split between 0219 and 0216 | atlas-internal |
| Harris 2018 GSE99888 *Sst.Pnoc.Calb1.Igfbp5* class | Annotation transfer | SUPPORT | F1=0.51 at supertype 0216 (coverage=0.97) | atlas-internal |
| Chamberland 2024 per-cluster *Chrna2*-OLM subfamily | Annotation transfer | SUPPORT | F1=0.33 at supertype 0216; F1=0.65 at cluster 0771 (sibling child) | atlas-internal |

**Concerns:**
- *Pvalb* DISCORDANT at supertype level (cohort_pct 0.778). The supertype mixes O-LM (*Pvalb*-sparse) with bistratified cells (*Sst*+/*Pvalb*+/*Tac1*+), and the elevated *Pvalb* mean reflects this admixture rather than a contradiction of the classical O-LM negative marker — *(note: bistratified-cell occupancy of Sst Gaba_3 is documented in the companion bistratified report and in the classical literature [4][7])*.
- DISTRIBUTED_ACROSS_CLUSTERS: Sst Gaba_3 contains at least three classical CA1 stratum oriens Sst-IN types (O-LM, bistratified, hippocampo-septal) that are not separable at supertype level; the supertype-level call is the broadest defensible mapping.
- The supertype also contains a substantial non-CA1 component (prosubiculum, posterior amygdala in the painted MERFISH counts); supertype membership alone does not localise to CA1.

**Marker evidence provenance:**
- *Sst*, *Reln*, *Chrna2*, *Npy*, *Pnoc* are all anchored to Winterer 2019 [4], which performed scRNA-seq on Cre-driver-targeted (Sst-Cre and Htr3a-Cre) OLM cells with morphology-verified identity — transcript-level evidence on confirmed-OLM cells, the strongest available provenance.
- *Chrna2* additionally supported by Nichol et al. 2018 [6] as an OLM-specific marker in dorsal CA1.
- *Pvalb* as a negative marker carries only the Winterer-reported "sparse expression" provenance [4]; the atlas-side elevated value at supertype reflects bistratified admixture, not a marker discrepancy for the classical O-LM type.

**What would upgrade confidence:**
- A patch-seq or Cre-driver-targeted O-LM annotation transfer onto WMBv1 reaching F1 ≥ 0.80 at CLUSTER level (would add an `AnnotationTransferEvidence` resolving O-LM to a specific Sst Gaba_3 child cluster).
- Targeted literature trawl for whether the multiple *Pnoc* / *Chrna2*+ O-LM subpopulations described in the classical literature align one-to-one with Sst Gaba_3 child clusters.

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · 🟡 MODERATE

**Supporting evidence:**
- This cluster sits within the leading O-LM supertype (Sst Gaba_3, supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216]) and carries the highest within-supertype within-CA1 stratum oriens count (Field CA1, stratum oriens [MBA:399] count_100um=261; region_fraction_100um 0.818) — soma location is squarely consistent with O-LM identity.
- Marker concordance: *Sst* (val=12.70; cohort_pct 0.992), *Chrna2* (val=0.57; cohort_pct 0.950), *Reln* (val=10.65; cohort_pct 0.975), *Npy* (val=7.58; cohort_pct 0.857) all CONSISTENT.
- Cluster 0768 leads the Winterer 2019 Cre-driver-targeted OLM pool's cluster-level distribution as the top-coverage Sst Gaba_3 child (see figure) — *(note: this is sidecar-grounded figure context only; cluster 0768 does not carry a direct AnnotationTransferEvidence item on this edge, and the cluster-level call rests on supertype membership + property concordance)*.

**Property comparison (Table 1).**

| Property | Classical | Cluster 0768 | Alignment |
|---|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | Field CA1, stratum oriens [MBA:399] count_100um=261; region_fraction_100um 0.818 | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| *Sst* (defining) | defining marker | val=12.70; cohort_pct 0.992 | CONSISTENT |
| *Chrna2* (defining) | defining marker | val=0.57; cohort_pct 0.950 | CONSISTENT |
| *Reln* (defining) | defining marker | val=10.65; cohort_pct 0.975 | CONSISTENT |
| *Pvalb* (negative) | absent | val=3.12; cohort_pct 0.866 | DISCORDANT |
| *Sst* (neuropeptide) | neuropeptide | val=12.70; cohort_pct 0.992 | CONSISTENT |
| *Npy* (neuropeptide) | neuropeptide | val=7.58; cohort_pct 0.857 | CONSISTENT |
| *Pnoc* (neuropeptide) | neuropeptide | val=2.51; cohort_pct 0.479 | APPROXIMATE |

*Chrna2* present on 0768 (val=0.57) but at lower cohort percentile than on the sibling 0771 (val=0.65; cohort_pct 0.958); 0773 carries the highest *Chrna2* (0.65; cohort_pct 0.958). *Pnoc* is depleted on 0768 relative to siblings 0770 (val=6.98) and 0775 (val=7.20); this is a within-supertype heterogeneity signal rather than a contradiction of the classical O-LM identity.

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (region + counts) | Atlas metadata | PARTIAL | region_fraction_100um=0.818 at MBA:399 (CA1 stratum oriens) | atlas-internal |

**Concerns:**
- *Pvalb* DISCORDANT (val=3.12; cohort_pct 0.866; atlas MERFISH-panel category). The elevated *Pvalb* mean on 0768 is at odds with the classical *Pvalb*-sparse signature for O-LM cells [4]. This may reflect a *Pvalb*+ bistratified-cell admixture within 0768 or a real *Pvalb*-permissive O-LM subpopulation; the heterogeneity has not been resolved in the gathered literature and is flagged as an open question.
- *Pnoc* APPROXIMATE (val=2.51; cohort_pct 0.479) — depleted relative to other Sst Gaba_3 children. If 0768 is the O-LM-leading cluster, this implies the *Pnoc*+ O-LM subpopulation reported by Winterer 2019 may not be 0768 but a sibling (0770 *Pnoc*=6.98, or 0775 *Pnoc*=7.20).
- AMBIGUOUS_MAPPING: 0768 does not carry a direct AT evidence item from a morphology-confirmed O-LM dataset on this edge; the cluster-level call is supported via supertype membership and property concordance plus figure-level Winterer-pool scatter, not by an on-edge cluster-level AT F1.

**Marker evidence provenance:**
- All concordant markers anchor to the same Winterer 2019 scRNA-seq evidence as in the supertype paragraph — confirmed-OLM source cells, transcript-level. *Pnoc* depletion on 0768 specifically is an atlas-precomputed-stats observation absent from the gathered literature; targeted lit search for "*Pnoc* heterogeneity within OLM" would help interpret.
- ⚠ **Atlas annotation/expression discrepancy**: *Sst* is in the atlas NEUROPEPTIDE category on this cluster and expression is high (val=12.70); no discrepancy. *Pvalb* is in the MERFISH probe panel (category: MERFISH) and shows val=3.12; MERFISH-panel presence is a probe-selection signal, not an expression-quality signal — but the elevated mean still requires biological interpretation (likely admixture, see Concerns).

**What would upgrade confidence:**
- An O-LM-specific (Chrna2-Cre or post-hoc-morphology) annotation transfer reaching F1 ≥ 0.80 at CLUSTER level against CS20230722_CLUS_0768, producing an `AnnotationTransferEvidence` on this edge.
- Targeted literature trawl for *Pvalb* heterogeneity within the classical O-LM type — to determine whether the elevated atlas-side *Pvalb* on 0768 is a real O-LM subpopulation signal or bistratified-cell contamination.
- Subcluster-level *Pnoc* / *Chrna2* expression profiling to determine whether 0768, 0770, 0772, 0773, 0775 each correspond to a distinct O-LM subpopulation (multiple subpopulations reported but not yet aligned to atlas clusters).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | 🟡 MODERATE | Winterer + Harris OLM AT converge here; Sst+/Reln+/Chrna2+ panel CONSISTENT | Primary (supertype) |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | 🟡 MODERATE | Leading Sst Gaba_3 child by Winterer-pool cluster coverage; CA1 SO region_fraction_100um=0.818 | Secondary (best cluster within supertype) |
| 0770 Sst Gaba_3 [CS20230722_CLUS_0770] | 0216 Sst Gaba_3 | 404 | 🔴 LOW | Pvalb=0.00 (CONSISTENT); Pnoc=6.98; Npy=1.04 (APPROXIMATE) — alternative Sst Gaba_3 child | Supports broader mapping (Pnoc+ O-LM subpop candidate) |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | 🔴 LOW | All markers CONSISTENT but Pvalb=0.34 DISCORDANT; Npy=8.22; Pnoc=1.65 APPROXIMATE | Supports broader mapping (sibling Sst Gaba_3 child) |
| 0773 Sst Gaba_3 [CS20230722_CLUS_0773] | 0216 Sst Gaba_3 | 156 | 🔴 LOW | Highest Chrna2 (val=0.65; cohort_pct 0.958); Pvalb=0.36 DISCORDANT; Npy=1.61 APPROXIMATE | Supports broader mapping (Chrna2-leading sibling) |
| 0775 Sst Gaba_3 [CS20230722_CLUS_0775] | 0216 Sst Gaba_3 | 143 | 🔴 LOW | Pnoc=7.20 highest of Sst Gaba_3 children; region APPROXIMATE (CA1 stratum oriens count_100um=58) | Supports broader mapping (Pnoc+ sibling) |
| 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | — | 4064 | 🔴 LOW | Markers Sst+/Chrna2+/Reln+ atlas-DEFINING but soma location Isocortex/Cortical subplate (region_fraction_100um=0.016) | Eliminated (wrong region — Isocortex not CA1) |
| 0217 Sst Gaba_4 [CS20230722_SUPT_0217] | — | 14335 | 🔴 LOW | Sst+/Chrna2 atlas-DEFINING_SCOPED; soma in Isocortex (region_fraction_100um=0.015) | Eliminated (wrong region — cortical Sst Gaba_4) |
| 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | — | 2905 | 🔴 LOW | Sst+/Npy+ very high but Chrna2=0.00 DISCORDANT; soma Isocortex/corpus callosum | Eliminated (Chrna2 absent + wrong region) |
| 0239 Sst Chodl Gaba_2 [CS20230722_SUPT_0239] | — | 1306 | 🔴 LOW | Chrna2=0.00 DISCORDANT; soma Striatum (region DESCENDANT_ONLY) | Eliminated (Chrna2 absent + wrong region) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The O-LM cell is defined here on a CLASSICAL_MULTIMODAL basis — convergent anatomical (soma in CA1 stratum oriens [UBERON:0014552], axon in CA1 stratum lacunosum moleculare [UBERON:0014557]; [1][2][3]), neurochemical (GABAergic [4]), and molecular evidence (*Sst*+/*Chrna2*+/*Reln*+ defining markers, *Pvalb*-sparse [4][6]; *Sst*/*Npy*/*Pnoc* neuropeptides [4]).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

*Run: at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1*

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 cell type labels — Sst subclass, n=273 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

*Run: at_run_20260512_harris_class_mmc_wmbv1*

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 CA1 inhibitory neuron published Class labels — Sst.Pnoc.Calb1.Igfbp5 class is the OLM-type cluster, n=254 of 3663 total) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Caveats | This run record scores Harris 2018's published Class labels against WMBv1; shares its MapMyCells output with the Chamberland subfamily companion run record (at_run_20260512_chamberland_subfamily_mmc_wmbv1). |

*Run: at_run_20260512_chamberland_subfamily_mmc_wmbv1*

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 cells re-labelled by Chamberland 2024 in-silico gene-pair subfamily rules — per-cluster, dropout-robust; *Chrna2*-OLM label propagated from Harris classes by Chrna2>Ndnf>Sst_Nos1>Sst_Tac1 priority) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) — same MMC output as the Harris Class companion run, re-aggregated under Chamberland subfamily labels via class_to_subfamily.tsv |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_chamberland_by_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/f1_matrix_chamberland_by_class.csv) |
| Caveats | Per-cluster derivation is the primary result (dropout-robust); per-cell derivation is retained but subject to scRNA-seq dropout on gene-pair markers. Headline cluster-level finding for *Chrna2*-OLM: CS20230722_CLUS_0771 with F1=0.65 (recall=0.81). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:30+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER ×3 | PARTIAL/SUPPORT | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_CLUS_0775 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0217 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0239 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence (supertype), with 0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the leading cluster-level candidate within that supertype at MODERATE confidence. Key support: convergent annotation transfer from morphology- and Cre-confirmed O-LM cells (Winterer 2019; figure F1=0.97 at supertype, n=43 of 46) and from Harris 2018 *Sst.Pnoc.Calb1.Igfbp5* (edge F1=0.51 at supertype, coverage=0.97); marker concordance across *Sst*/*Chrna2*/*Reln*/*Npy* on both supertype and cluster 0768. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (Sst Gaba_3 mixes O-LM, bistratified, and HS classical types at supertype level); *Pvalb* DISCORDANT on cluster 0768 (val=3.12; cohort_pct 0.866) — interpretable as bistratified-cell admixture or a real *Pvalb*-permissive O-LM subpopulation but unresolved.

No Cell Ontology term currently assigned. CL:4023017 *sst GABAergic interneuron* is the nearest superclass but does not capture O-LM-specific morphology (axonal projection to SLM, soma in stratum oriens) — candidate for a new CL term.

### Proposed experiments and follow-ups

**1. O-LM-targeted annotation transfer onto WMBv1.**
- **What:** MapMyCells annotation transfer of a Chrna2-Cre-targeted O-LM scRNA-seq cohort (e.g. Winterer 2019 GSE124847 re-mapped, or a new patch-seq O-LM dataset) onto CCN20230722.
- **Target:** F1 ≥ 0.80 at CLUSTER level against a Sst Gaba_3 child.
- **Expected output:** `AnnotationTransferEvidence` on the edge to the resolved CLUS_, with `source_cluster_label` naming the Cre line and morphology criteria.
- **Resolves:** primary cluster-level identity of O-LM within Sst Gaba_3 (CLUS_0768 vs sibling); open questions 1, 2, 3 (see below). Note that GEO:GSE124847 is referenced in the SUPT_0216 evidence narrative but no AnnotationTransferEvidence item with structured metrics_by_level rows is yet attached to this edge — that re-mapping would close the gap.

**2. Targeted literature trawl for *Pvalb* and *Pnoc* heterogeneity within O-LM.**
- **What:** cite-traverse query for "Pvalb heterogeneity OLM hippocampus", "Pnoc OLM subpopulations CA1", "Chrna2 subclusters OLM".
- **Target:** identify whether the multiple *Chrna2*+ subpopulations reported in the classical literature, the *Pnoc*+ subset detected by Winterer 2019, and the elevated atlas-side *Pvalb* on CLUS_0768 correspond to real O-LM subpopulations vs admixture.
- **Expected output:** `LiteratureEvidence` snippets on the classical node and per-edge `caveats[]` updates documenting the resolved heterogeneity.
- **Resolves:** open questions 1, 2.

**3. Sub-stratum-oriens layer alignment (Chamberland 2024 depth gradient vs atlas clusters).**
- **What:** assess whether the O-LM sub-stratum-oriens depth gradient described by Chamberland 2024 [7] (*Chrna2*-INs deepest, *Sst*-*Tac1*-INs closest to pyramidal layer) corresponds to atlas-side MERFISH soma-depth differences across Sst Gaba_3 child clusters (0768, 0770, 0772, 0773, 0775).
- **Expected output:** atlas-side MERFISH depth analysis; if a clean gradient emerges, may upgrade specific child clusters to *Chrna2*-O-LM identity.
- **Resolves:** open question 3.

### Open questions

1. Does the elevated *Pvalb* expression on CLUS_0768 (val=3.12; cohort_pct 0.866) reflect bistratified-cell admixture within the cluster or a real *Pvalb*-permissive O-LM subpopulation? The classical literature reports O-LM as *Pvalb*-sparse [4], not *Pvalb*-absent — the boundary is not well-resolved.
2. Which Sst Gaba_3 child cluster (0768, 0770, 0772, 0773, 0775) corresponds to the *Pnoc*+ O-LM subpopulation reported by Winterer 2019 (Pnoc detected in 27 of 46 OLM cells across Sst-Cre and Htr3a-Cre)? *Pnoc* expression varies markedly across these children (0.479 to 0.966 cohort_pct).
3. Do the multiple *Chrna2*+ O-LM subpopulations described in the classical literature align one-to-one with Sst Gaba_3 child clusters, or does the molecular heterogeneity cross-cut child-cluster boundaries?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Friend et al. 2019 · PMID:[30987110](https://pubmed.ncbi.nlm.nih.gov/30987110) | 30987110 | soma location |
| [2] | Tecuatl et al. 2020 · PMID:[33361464](https://pubmed.ncbi.nlm.nih.gov/33361464) | 33361464 | soma location |
| [3] | Bezaire et al. 2016 · PMID:[28009257](https://pubmed.ncbi.nlm.nih.gov/28009257) | 28009257 | soma location |
| [4] | Winterer et al. 2019 · PMID:[31420995](https://pubmed.ncbi.nlm.nih.gov/31420995) | 31420995 | soma location |
| [5] | Leão et al. 2012 · PMID:[23042082](https://pubmed.ncbi.nlm.nih.gov/23042082) | 23042082 | soma location |
| [6] | Nichol et al. 2018 · PMID:[29487503](https://pubmed.ncbi.nlm.nih.gov/29487503) | 29487503 | soma location |
| [7] | Chamberland et al. 2024 · PMID:[38640347](https://pubmed.ncbi.nlm.nih.gov/38640347) | 38640347 | soma location |
| [8] | Chamberland et al. 2023 · PMID:[37162922](https://pubmed.ncbi.nlm.nih.gov/37162922) | 37162922 | *Sst* marker |

---

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.7
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Convergent annotation transfer from Harris 2018
    Sst.Pnoc.Calb1.Igfbp5 (F1=0.51, coverage=0.97 at CS20230722_SUPT_0216 in
    at_run_20260512_harris_class_mmc_wmbv1) and from Chamberland 2024
    Chrna2-OLM per-cluster subfamily labels (F1=0.33 at supertype, F1=0.65
    at sibling cluster CS20230722_CLUS_0771 in
    at_run_20260512_chamberland_subfamily_mmc_wmbv1), together with Yao 2021
    Sst subclass mapping (F1=0.98 at subclass CS20230722_SUBC_053 in
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1), place OLM cells on Sst
    Gaba_3 at supertype resolution. 6 of 7 markers CONSISTENT (Sst, Chrna2,
    Reln, Npy, Pnoc, Sst-neuropeptide); Pvalb DISCORDANT
    reflects bistratified-cell admixture within Sst Gaba_3 rather than a
    classical-type contradiction. Cluster-level resolution requires Cre-line
    annotation transfer; surveys 1:n onto multiple Sst Gaba_3 children.
  reconciliation_note: >
    Paired with cluster-level survivor edge
    edge_olm_cell_ca1_to_CS20230722_CLUS_0768 (best Sst Gaba_3 child by
    Winterer 2019 Cre-driver-targeted pool coverage; see figure
    f1_for_olm_hippocampus.png). Supertype-level skos:broadMatch + 1:n is
    the canonical OLM-type resolution given documented distribution across
    Sst Gaba_3 children.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Sst Gaba_3 supertype contains at least three classical hippocampal
        cell types — OLM, bistratified, and hippocampo-septal — that are not
        separable at supertype level. Cluster-level resolution requires
        Cre-driver-targeted annotation transfer (e.g. Chrna2-Cre + MapMyCells).
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Pvalb DISCORDANT at supertype (val=1.48; cohort_pct 0.778) reflects
        bistratified-cell occupancy of Sst Gaba_3 rather than a contradiction
        of the classical Pvalb-sparse OLM signature reported by Winterer 2019
        on Cre-driver-targeted OLM cells.
    - caveat_type: OTHER
      description: >
        Sst Gaba_3 also contains substantial non-CA1 cells (prosubiculum,
        posterior amygdala in MERFISH counts); supertype membership alone
        does not localise to CA1.
  proposed_experiments:
    - >
      Annotation transfer of a Chrna2-Cre-targeted OLM scRNA-seq cohort
      (e.g. Winterer 2019 GSE124847 re-mapped, or a new patch-seq OLM
      dataset) onto CCN20230722; target F1 >= 0.80 at CLUSTER level against
      a Sst Gaba_3 child cluster.
    - >
      Targeted literature trawl (cite-traverse) for Pvalb heterogeneity
      within OLM and for the multiple Chrna2+ OLM subpopulations described
      in the classical literature.
  unresolved_questions:
    - >
      Trawl literature for Pvalb heterogeneity within the OLM type — the
      atlas-side elevated Pvalb on Sst Gaba_3 may be bistratified admixture
      or a real subpopulation signal not yet captured in the synthesised
      evidence.
    - >
      Determine whether the multiple Chrna2+ OLM subpopulations reported in
      the classical literature align one-to-one with Sst Gaba_3 child
      clusters (CLUS_0768, CLUS_0770, CLUS_0772, CLUS_0773, CLUS_0775).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0768 sits within the OLM-leading supertype
    CS20230722_SUPT_0216 and carries the highest within-supertype CA1
    stratum oriens occupancy (region_fraction_100um=0.818 at MBA:399).
    5 of 7 markers CONSISTENT (Sst val=12.70, Chrna2 val=0.57, Reln
    val=10.65, Npy val=7.58, Sst-neuropeptide all CONSISTENT);
    Pvalb DISCORDANT (val=3.12; atlas MERFISH category — likely
    bistratified-cell admixture); Pnoc APPROXIMATE (val=2.51) — depleted
    relative to siblings, suggesting CLUS_0768 is not the Pnoc+ OLM
    subpopulation. The cluster-level call rests on supertype membership
    plus property concordance plus figure-level Winterer 2019 OLM-pool
    cluster scatter; no direct on-edge cluster-level AT F1 yet.
  reconciliation_note: >
    Paired with supertype-level survivor edge
    edge_olm_cell_ca1_to_CS20230722_SUPT_0216 (skos:broadMatch + 1:n).
    Cluster-level skos:closeMatch + 1:1 reflects the best available
    within-supertype resolution; sibling Sst Gaba_3 children
    (CLUS_0770, CLUS_0772, CLUS_0773, CLUS_0775) carry alternative
    marker profiles consistent with documented OLM molecular
    heterogeneity (multiple Chrna2+ and Pnoc+ subpopulations).
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Pvalb DISCORDANT (val=3.12; cohort_pct 0.866) on a cluster
        proposed for the Pvalb-sparse classical OLM type. Interpretable
        as bistratified-cell admixture within CLUS_0768 or as a real
        Pvalb-permissive OLM subpopulation; not resolved in gathered
        literature.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        No direct AnnotationTransferEvidence with metrics_by_level at
        CLUSTER level on this edge from a morphology-confirmed OLM
        dataset; cluster identity rests on supertype-membership plus
        marker concordance plus figure-level Winterer-pool cluster
        scatter.
  proposed_experiments:
    - >
      cluster annotation transfer of a Chrna2-Cre-targeted or
      post-hoc-morphology-confirmed OLM cohort onto CCN20230722; target
      F1 >= 0.80 at CLUSTER level against CS20230722_CLUS_0768.
    - >
      Atlas-side MERFISH soma-depth analysis across Sst Gaba_3 child
      clusters to test whether the Chamberland 2024 sub-stratum-oriens
      depth gradient (Chrna2-INs deepest, Sst-Tac1-INs closest to
      pyramidal layer) aligns with cluster boundaries.
  unresolved_questions:
    - >
      Which Sst Gaba_3 child cluster corresponds to the Pnoc+ OLM
      subpopulation reported by Winterer 2019 (Pnoc detected in 27 of
      46 OLM cells)? CLUS_0768 has Pnoc APPROXIMATE (val=2.51) while
      siblings CLUS_0770 (val=6.98) and CLUS_0775 (val=7.20) carry
      much higher Pnoc.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] CS20230722_CLUS_0770 is a Sst Gaba_3 child cluster with
    all markers CONSISTENT (Sst val=10.54, Chrna2 val=0.52, Reln
    val=8.82, Pvalb val=0.00 — the only Sst Gaba_3 child with Pvalb
    truly absent) but Npy is APPROXIMATE (val=1.04; cohort_pct 0.353)
    and Pnoc is the highest among Sst Gaba_3 children (val=6.98). This
    is plausibly a Pnoc+ OLM subpopulation but is not the leading
    Winterer 2019 OLM-pool cluster; supports the broader supertype
    mapping without being the primary cluster-level survivor.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] CS20230722_CLUS_0772 is a Sst Gaba_3 child with all
    positive markers CONSISTENT (Sst val=11.92, Chrna2 val=0.46, Reln
    val=10.13, Npy val=8.22) but Pvalb DISCORDANT (val=0.34;
    cohort_pct 0.571) and Pnoc APPROXIMATE (val=1.65). A sibling
    Sst Gaba_3 candidate; supports the broader supertype mapping
    without being the primary cluster-level survivor.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] CS20230722_CLUS_0773 is a Sst Gaba_3 child carrying the
    highest Chrna2 expression among the Sst Gaba_3 children (val=0.65;
    cohort_pct 0.958) with Sst (val=11.43), Reln (val=9.24), and Pnoc
    (val=4.40) all CONSISTENT; Pvalb DISCORDANT (val=0.36) and Npy
    APPROXIMATE (val=1.61). A plausible Chrna2-leading OLM sibling
    cluster; supports the broader supertype mapping without being the
    primary cluster-level survivor.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_CLUS_0775 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0775 is a Sst Gaba_3 child with Pnoc
    very high (val=7.20; cohort_pct 0.966) and Chrna2 (val=0.73)
    highest among the Sst Gaba_3 children, but soma location is only
    APPROXIMATE (region_fraction_100um=0.442 at MBA:399; prosubiculum
    count_100um=59) and Pvalb DISCORDANT (val=2.39). Sibling candidate;
    supports the broader supertype mapping without being the primary
    cluster-level survivor.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 (Sst Gaba_13) carries strong marker
    concordance (Sst val=12.08 atlas DEFINING, Chrna2 val=0.61, Reln
    val=8.98, Npy val=9.70) but soma location is DISCORDANT — Isocortex
    [MBA:315] count_100um=1021 with region_fraction_100um=0.016 at
    MBA:399 (CA1 stratum oriens). This is a cortical Sst Gaba_13
    population, not the CA1 OLM cell.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_SUPT_0217 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0217 (Sst Gaba_4) carries Sst val=10.79,
    Chrna2 val=1.90 (atlas DEFINING_SCOPED), and Reln val=10.16 — a
    Chrna2-rich Sst supertype — but soma location is DISCORDANT,
    centred in Isocortex [MBA:315] count_100um=4066 with
    region_fraction_100um=0.015 at MBA:399. This is the cortical
    Chrna2+ Sst population (Sst Gaba_4), not the CA1 OLM cell.
  reconciliation_note: >
    The classical OLM type may be a hippocampal homologue of the
    cortical Chrna2+ Sst Gaba_4 population; the present mapping rules
    that out at the level of CA1-specific identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0241 (Sst Chodl Gaba_4) carries very
    high Sst (val=12.33) and Npy (val=12.08) but Chrna2 DISCORDANT
    (val=0.00, below MIN_DETECTABLE), and soma location is DISCORDANT
    (Isocortex [MBA:315] count_100um=1377; corpus callosum
    count_100um=460; region_fraction_100um=0.021 at MBA:399). The
    Sst Chodl identity (long-range-projecting, Chrna2-negative) is
    incompatible with the classical OLM Chrna2+ defining marker.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_cell_ca1_to_CS20230722_SUPT_0239 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0239 (Sst Chodl Gaba_2) carries high
    Sst (val=11.95) and Npy (val=11.10) but Chrna2 DISCORDANT
    (val=0.00, below MIN_DETECTABLE) and soma is in Striatum
    [MBA:477] (region_evidence DESCENDANT_ONLY at MBA:399). Chrna2
    absence plus striatal location refute the OLM mapping; this is
    consistent with a striatal Sst Chodl long-range projecting type,
    not the CA1 hippocampal OLM cell.
```
<!-- verdict-block-end -->
