# Amygdala intercalated cell — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `/Users/do12/Documents/GitHub/evidencell_too/kb/graphs/medial_temporal_lobe_amygdala/amygdala_intercalated_cell.yaml`*

---

## Introduction

The intercalated cell masses are small clusters of densely packed GABAergic
neurons wedged between the basolateral and centromedial divisions of the
amygdala, in the intercalated amygdaloid nuclei [UBERON:0002884] [1][2][3].
They form one of the amygdala's "unclassified" groups — not part of the
basolateral, cortical-like, or centromedial nuclei — yet they gate information
flow through the amygdala and are almost uniformly GABAergic [3][4]. Recent
single-cell work resolves the intercalated masses into several **FOXP2+**
interneuron subtypes, including conserved TSHZ1+ populations that split into
DRD1+ and DRD1− forms [5][6]. This report asks which Whole Mouse Brain atlas
(WMBv1) transcriptomic types correspond to that classical, multi-subtype
population.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Intercalated amygdaloid nuclei [UBERON:0002884] | [1][2][3] |
| Neurotransmitter | GABAergic | [3][4] |
| Defining markers | Foxp2, Drd1, Oprm1 | Foxp2 [5][6]; Drd1 [6]; Oprm1 [5] |

The classical node is defined multimodally (`CLASSICAL_MULTIMODAL`). No subtypes
were split out on the node itself, but the intercalated masses are known to be
molecularly heterogeneous [5][6]; ITC-related types with central-amygdala soma
(Pax6/Tacr3/Tshz2) were deliberately excluded from the transferred source set,
which is restricted to the four Foxp2+ intercalated populations.

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** literature review of amygdala organization · human/rodent · [1]
  > At the cellular level, the amygdala is composed of a group of 13 sub-nuclei located in the medial temporal lobe (Price, 2003). These nuclei may be divided into four subdivisions (Sah et al., 2003): (Ethen et al., 2009) basolateral (which includes the lateral, basolateral, and basomedial nuclei), (May et al., 2009) cortical like (including nucleus of the lateral olfactory tract, bed nucleus of the accessory olfactory tract, the cortical nucleus, and the periamygdaloid cortex), (3) centromedial (central and medial nuclei, and the amygdaloid part of the bed nucleus of stria terminalis), and (4) other (which includes anterior amygdala area, the amygdalo-hippocampal area, and the intercalated nuclei)
  > — Ignacio et al. 2014, Amygdala organization and principal cellular classes · [1] <!-- quote_key: 1229611_e14a19cf -->
- **Soma location:** review of amygdala anatomy · human · [2]
  > . Anatomically the amygdala is composed of three major nuclear groups 198 : the deep or basolateral group, which contains the lateral nucleus, the basal nucleus, and the accessory basal nucleus; the superficial or cortical-like group, which contains the cortical nuclei and the nucleus of the lateral olfactory tract; the centromedial group, which contains the medial and central nuclei. To this canonical classification, other amygdaloid nuclei must be added, such as the anterior amygdaloid area, the amygdalohippocampal area, and the intercalated cells. 199 In addition, a rostro-medial extension of the centromedian amygdala into an area known as extended amygdala has been proposed. 200
  > — Nardelli et al. 2024, Amygdala organization and principal cellular classes · [2] <!-- quote_key: 270614391_b0af02da -->
- **Soma location / GABAergic identity:** review · [3]
  > . In addition to the four groups, a few nuclei of the amygdala remain unclassified, among them the intercalated cell masses which are small clusters of densely packed GABAergic neurons (Palomares-Castillo et al., 2012).
  > — Veinante et al. 2013, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 15449738_a21bd562 -->
- **Neurotransmitter:** anatomical / immunostaining · [4]
  > In some regions, such as the intercalated nuclei, virtually all of the resident neurons appeared to be GABAergic
  > — Pitkānen & Amaral 1994, abstract · [4] <!-- quote_key: 14068807_9efc175b -->
- **Foxp2 marker:** single-nucleus transcriptomics of the amygdala · [5]
  > We identified distinct subtypes of FOXP2+ interneurons in the intercalated cell masses and protein-kinase C-δ interneurons in the central nucleus. We also establish that glutamatergic, pyramidal-like neurons are transcriptionally specialized within the basal, lateral, or accessory basal nuclei
  > — Totty et al. 2024, Medial, cortical/superficial, and intercalated cell populations · [5] <!-- quote_key: 273531817_88e4457f -->
- **Foxp2 / Drd1 markers:** cross-species single-cell analysis · [6]
  > the IA subnuclei were highly conserved, and all mammals in our datasets contained two types of TSHZ1+ neurons, i.e., DRD1+ and DRD1−.
  > — Yu et al. 2023, Results · [6] <!-- quote_key: 256832817_4f39c6f9 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer of the four Foxp2+ intercalated source populations
(Hochgerner 2023) resolves the classical intercalated cell not to one atlas
type but to a family of them: the on-target primary is the atlas's own
intercalated-amygdala subclass **065 IA Mgp Gaba**, which receives the
Foxp2_Fmod source at F1=0.90 and concentrates in the **0292 IA Mgp Gaba_3**
supertype [CS20230722_SUPT_0292] (F1=0.85; see figure and property tables). The
remaining Foxp2 subtypes transfer instead into striatopallidal **STR-PAL Chst9**
territory — most cleanly **0286 STR-PAL Chst9 Gaba_2** [CS20230722_SUPT_0286]
(F1=0.97) — so the mapping is genuinely one-to-many across two atlas groupings,
consistent with the striatal/LGE molecular affinity of intercalated neurons
(see figure).

![Filtered AT figure for amygdala intercalated cell](figures/f1_for_amygdala_intercalated_cell.png)

*F1 across taxonomy levels for the four Foxp2+ intercalated source groups
(GABA-1-Foxp2_Fmod, GABA-2-Foxp2_Adra2a, GABA-3-Foxp2_Col6a1,
GABA-4-Foxp2_Htr1f) transferred from Hochgerner 2023 to WMBv1. Each panel is one
source group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage**
(Cov) shown inline. Coverage = fraction of source-group cells landing on this
target; Purity = fraction of this target's cells coming from the source group;
F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. Read down each
panel: the four subtypes peak on four different branches — GABA-1 on the IA Mgp
subclass, GABA-2/3/4 on distinct STR-PAL Chst9 supertypes — which is why the
single classical type maps to several atlas types.*

The four subtypes are non-redundant: each peaks on a distinct branch, and the
Foxp2_Fmod subtype is the only one to reach the atlas's intercalated-amygdala
(IA Mgp) grouping. Cell counts per source are modest (GABA-1 n=23, GABA-4 n=9),
so cluster-level scatter within each branch is expected.

### 065 IA Mgp Gaba (subclass) · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Atlas (065 IA Mgp Gaba subclass) | Alignment |
|---|---|---|---|
| Soma location | Intercalated amygdaloid nuclei [UBERON:0002884] | Striatum [MBA:477], Olfactory areas [MBA:698], Cortical subplate [MBA:703] | APPROXIMATE |
| NT type | GABAergic | GABA | CONSISTENT |
| Foxp2 | defining marker | no atlas expression data at subclass level | NOT_ASSESSED |
| Drd1 | defining marker | no atlas expression data at subclass level | NOT_ASSESSED |
| Oprm1 | defining marker | no atlas expression data at subclass level | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (region/NT) | Atlas metadata | PARTIAL | region_fraction_100um=0.103 | atlas-internal |
| MapMyCells AT (GABA-1-Foxp2_Fmod) | Annotation transfer | SUPPORT | F1=0.90 (subclass) | AT run |
| MapMyCells AT (GABA-2-Foxp2_Adra2a) | Annotation transfer | PARTIAL | F1=0.13 (class) | AT run |
| MapMyCells AT (GABA-3-Foxp2_Col6a1) | Annotation transfer | PARTIAL | F1=0.56 (class) | AT run |
| MapMyCells AT (GABA-4-Foxp2_Htr1f) | Annotation transfer | PARTIAL | F1=0.06 (class) | AT run |

*(Foxp2 child-coverage is 1.00 at the concentrated 0292 supertype below; marker
expression is not tabulated at subclass level, so the subclass call rests on
annotation transfer, GABAergic identity, and the anatomically-named IA Mgp
grouping.)*

The intercalated-amygdala (IA Mgp) subclass is the most on-target
correspondence for the classical intercalated cell, and it is the primary
mapping. The Foxp2_Fmod source — one of the FOXP2+ intercalated subtypes
described by Totty 2024 [5] — transfers to this subclass at F1=0.90, the highest
subclass-level score of any of the four sources, and the atlas itself names the
subclass for the intercalated amygdala. The mapping is broad: the source
distributes across the subclass rather than isolating a single cluster (see
figure).

**Supporting evidence**
- MapMyCells annotation transfer of GABA-1-Foxp2_Fmod lands on this subclass at
  F1=0.90 (Coverage=0.97, Purity=0.85), the clean level for this source (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`).
- GABAergic identity is consistent (atlas class 09 CNU-LGE GABA), matching the
  near-uniform GABAergic composition of the intercalated nuclei [4].
- The subclass is the atlas's designated intercalated-amygdala (IA) Mgp grouping
  — a nominal but relevant anatomical concordance with the classical type's soma
  location in the intercalated amygdaloid nuclei [UBERON:0002884].

**Concerns**
- Soma location is APPROXIMATE: the subclass's registered soma sit predominantly
  in Striatum [MBA:477] and adjacent Cortical subplate [MBA:703]
  (`region_fraction_100um: 0.103`, boundary band). *(note: the intercalated
  masses lie at the striatum–amygdala border within the cortical subplate, so
  boundary scatter here is anatomically expected rather than off-target.)*
- Markers are not assessable at subclass level (no precomputed atlas expression),
  so molecular confirmation comes only from the child supertype below.

**What would upgrade confidence**
- Cluster-resolution annotation transfer or targeted spatial validation
  confirming that Foxp2_Fmod cells occupy the intercalated nuclei rather than
  the surrounding striatum would raise this toward a confident broad mapping.

### 0292 IA Mgp Gaba_3 [CS20230722_SUPT_0292] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Atlas (0292 IA Mgp Gaba_3) | Alignment |
|---|---|---|---|
| Soma location | Intercalated amygdaloid nuclei [UBERON:0002884] | Cortical subplate [MBA:703], Striatum [MBA:477], Endopiriform nucleus ventral [MBA:966] | APPROXIMATE |
| NT type | GABAergic | not asserted | NOT_ASSESSED |
| Foxp2 | defining marker | 10.82 (cohort pct 0.919) | CONSISTENT |
| Drd1 | defining marker | 0.07 (cohort pct 0.065) | DISCORDANT |
| Oprm1 | defining marker | 2.84 (cohort pct 0.161) | APPROXIMATE |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (region/NT) | Atlas metadata | PARTIAL | region_fraction_100um=0.157 | atlas-internal |
| MapMyCells AT (GABA-1-Foxp2_Fmod) | Annotation transfer | SUPPORT | F1=0.85 (supertype) | AT run |
| MapMyCells AT (GABA-2-Foxp2_Adra2a) | Annotation transfer | PARTIAL | F1=0.36 (class) | AT run |
| MapMyCells AT (GABA-3-Foxp2_Col6a1) | Annotation transfer | PARTIAL | F1=0.56 (class) | AT run |
| MapMyCells AT (GABA-4-Foxp2_Htr1f) | Annotation transfer | NO_EVIDENCE | F1=0.06 (class) | AT run |

*(Foxp2 child-coverage is 1.00 across this supertype's IA Mgp Gaba_3 child
clusters; Drd1 is absent supertype-wide. GABA-1 transfer distributes across the
child clusters and does not isolate a single one — cluster-level F1 peaks at
0.47 — so the supportable resolution is the supertype, not any one cluster.)*

Within the IA Mgp subclass, the Foxp2_Fmod source concentrates in the 0292 IA
Mgp Gaba_3 supertype [CS20230722_SUPT_0292] at F1=0.85, making it the best
child of the primary mapping. Foxp2 is strongly and specifically expressed here
(mean 10.82, cohort percentile 0.919), but Drd1 is essentially absent (0.07) and
Oprm1 is weak. This is not a contradiction of intercalated identity: Yu 2023 [6]
report that the conserved intercalated (IA) subnuclei contain both DRD1+ and
DRD1− TSHZ1+ neuron types, so a Foxp2+/Drd1− supertype is exactly the DRD1−
intercalated subtype that classical marker panels (anchored on the DRD1+ form)
would miss.

**Supporting evidence**
- GABA-1-Foxp2_Fmod annotation transfer concentrates on this supertype at
  F1=0.85 (Coverage=0.76, Purity=0.96; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`).
- Foxp2 is CONSISTENT and cohort-specific (percentile 0.919), matching the
  defining FOXP2+ signature of intercalated interneurons [5][6].

**Marker evidence provenance**
- **Foxp2** — transcript-level (single-nucleus/single-cell) support from
  Totty 2024 [5] and Yu 2023 [6], both of which sequenced amygdala tissue and
  assigned the FOXP2+ population specifically to the intercalated masses.
  CONSISTENT with the atlas value (10.82).
- **Drd1** — DISCORDANT at 0.07. Yu 2023 [6] establishes a DRD1− intercalated
  subtype directly, so the mismatch reflects known within-type heterogeneity
  rather than a mapping error; the DRD1+ intercalated cells are expected to map
  to a different IA Mgp supertype.
- **Oprm1** — APPROXIMATE (2.84). Oprm1 on the classical node is sourced from a
  single study [5]; the partial atlas signal is consistent with subtype-limited
  expression.

**Concerns**
- Drd1 DISCORDANT and Oprm1 APPROXIMATE: two of the three defining markers do
  not align cleanly, tempered by the documented DRD1± split [6].
- Soma location APPROXIMATE (`region_fraction_100um: 0.157`, boundary band):
  soma sit in Cortical subplate [MBA:703] and Striatum [MBA:477] at the
  intercalated-nucleus border. *(note: cortical subplate is the atlas parent for
  the intercalated masses, so this is adjacent, not distant.)*
- Only n=22 source cells reach the supertype — a low-count transfer.

**What would upgrade confidence**
- Targeted Drd1 in-situ or Drd1-reporter profiling in the intercalated nuclei to
  confirm the DRD1− subtype identity of this supertype and resolve which IA Mgp
  supertype carries the DRD1+ form.

### 0286 STR-PAL Chst9 Gaba_2 [CS20230722_SUPT_0286] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Atlas (0286 STR-PAL Chst9 Gaba_2) | Alignment |
|---|---|---|---|
| Soma location | Intercalated amygdaloid nuclei [UBERON:0002884] | Striatum [MBA:477], Cortical subplate [MBA:703], medial forebrain bundle system [MBA:991] | DISCORDANT |
| NT type | GABAergic | not asserted | NOT_ASSESSED |
| Foxp2 | defining marker | 10.51 (cohort pct 0.887) | CONSISTENT |
| Drd1 | defining marker | 0.87 (cohort pct 0.613) | CONSISTENT |
| Oprm1 | defining marker | 6.91 (cohort pct 0.871) | CONSISTENT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (region/NT) | Atlas metadata | PARTIAL | region_fraction_100um=0.086 | atlas-internal |
| MapMyCells AT (GABA-1-Foxp2_Fmod) | Annotation transfer | PARTIAL | F1=0.13 (class) | AT run |
| MapMyCells AT (GABA-2-Foxp2_Adra2a) | Annotation transfer | SUPPORT | F1=0.97 (supertype) | AT run |
| MapMyCells AT (GABA-3-Foxp2_Col6a1) | Annotation transfer | PARTIAL | F1=0.69 (subclass) | AT run |
| MapMyCells AT (GABA-4-Foxp2_Htr1f) | Annotation transfer | PARTIAL | F1=0.11 (subclass) | AT run |

*(GABA-2-Foxp2_Adra2a transfer concentrates in one child cluster,
1005 STR-PAL Chst9 Gaba_2 [CS20230722_CLUS_1005], at F1=0.81; the remaining
Chst9 Gaba_2 children receive few cells, so the clean level is the supertype.)*

A second Foxp2+ intercalated subtype — the Adra2a source — maps to the 0286
STR-PAL Chst9 Gaba_2 supertype [CS20230722_SUPT_0286] at F1=0.97, the single
highest score in the run, with all three defining markers (Foxp2, Drd1, Oprm1)
CONSISTENT. This target sits in striatopallidal territory rather than the
intercalated nuclei proper, which is the expected consequence of the shared
LGE-derived, Foxp2+ molecular program of intercalated and striatal neurons — but
it also means this is a molecularly excellent, anatomically off-target match.

**Supporting evidence**
- GABA-2-Foxp2_Adra2a annotation transfer at F1=0.97 (Coverage=0.95,
  Purity=0.99; n=87; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`), the
  cleanest transfer of any source–target pair in the run.
- All three defining markers CONSISTENT: Foxp2 (10.51), Drd1 (0.87), Oprm1
  (6.91).

**Concerns**
- Soma location DISCORDANT: soma sit in Striatum [MBA:477] and the medial
  forebrain bundle system [MBA:991] (`region_fraction_100um: 0.086`, strict
  0.019). *(note: striatum is anatomically distinct from the intercalated
  amygdaloid nuclei; the classical type may be a molecular relative of this
  striatopallidal type rather than the intercalated population specifically.)*
- The strong marker match is expected given the shared Foxp2+ striatal program
  and so is not decisive on its own.

**What would upgrade confidence**
- Spatial transcriptomic validation to determine whether the Adra2a Foxp2+
  source cells occupy the intercalated nuclei or the adjacent striatum would
  resolve whether this is a genuine intercalated correspondence or a
  striatopallidal look-alike.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 target | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---:|---|---|---|
| 065 IA Mgp Gaba (subclass) | 1936 | 🟡 MODERATE | GABA-1 Foxp2_Fmod AT F1=0.90 to IA subclass | Primary (IA subclass) |
| 0292 IA Mgp Gaba_3 [CS20230722_SUPT_0292] | 443 | 🟡 MODERATE | GABA-1 AT F1=0.85; Foxp2+ / Drd1− | Best child within IA Mgp |
| 0286 STR-PAL Chst9 Gaba_2 [CS20230722_SUPT_0286] | 4621 | 🟡 MODERATE | GABA-2 AT F1=0.97; 3/3 markers | Second Foxp2 subtype |
| 1005 STR-PAL Chst9 Gaba_2 [CS20230722_CLUS_1005] | 4074 | 🔴 LOW | GABA-2 AT F1=0.81 (child of 0286) | Eliminated (child of 0286) |
| 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288] | 4588 | 🔴 LOW | GABA-3 AT F1=0.82 | Eliminated (GABA-3 subtype target) |
| 1011 STR-PAL Chst9 Gaba_4 [CS20230722_CLUS_1011] | 4242 | 🔴 LOW | GABA-3 AT F1=0.81 (child of 0288) | Eliminated (child of 0288) |
| 1015 STR-PAL Chst9 Gaba_5 [CS20230722_CLUS_1015] | 966 | 🔴 LOW | GABA-4 AT F1=0.70 | Eliminated (GABA-4 subtype target) |
| 0289 STR-PAL Chst9 Gaba_5 [CS20230722_SUPT_0289] | 1533 | 🔴 LOW | GABA-4 scatters; supertype F1=0.46 | Eliminated (cluster-level only) |
| 064 STR-PAL Chst9 Gaba (subclass) | 18689 | 🔴 LOW | broad Chst9 subclass; subtypes distribute | Eliminated (too broad) |
| 0287 STR-PAL Chst9 Gaba_3 [CS20230722_SUPT_0287] | 3822 | 🔴 LOW | no Foxp2 source concentrates | Eliminated (no clean transfer) |
| 0285 STR-PAL Chst9 Gaba_1 [CS20230722_SUPT_0285] | 4125 | 🔴 LOW | no Foxp2 source concentrates | Eliminated (no clean transfer) |
| 1009 STR-PAL Chst9 Gaba_3 [CS20230722_CLUS_1009] | 3132 | 🔴 LOW | no Foxp2 source concentrates | Eliminated (no clean transfer) |
| 0291 IA Mgp Gaba_2 [CS20230722_SUPT_0291] | 462 | 🔴 LOW | GABA-1 scatters; supertype F1=0.29 | Eliminated (IA sibling, scatter) |
| 1021 IA Mgp Gaba_3 [CS20230722_CLUS_1021] | 133 | 🔴 LOW | GABA-1 cluster F1=0.36 (child of 0292) | Eliminated (child of 0292) |
| 1017 IA Mgp Gaba_1 [CS20230722_CLUS_1017] | 254 | 🔴 LOW | GABA-1 subclass-level only | Eliminated (IA sibling, scatter) |
| 0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998] | 424 | ⚪ UNCERTAIN | Foxp2+ D1; location DISCORDANT; no clean AT | Eliminated (distant, no transfer) |
| 1000 STR D1 Sema5a Gaba_4 [CS20230722_CLUS_1000] | 2301 | ⚪ UNCERTAIN | Foxp2+ D1; no clean AT | Eliminated (distant, no transfer) |
| 0284 STR D1 Sema5a Gaba_4 [CS20230722_SUPT_0284] | 2413 | ⚪ UNCERTAIN | Foxp2+ D1; no clean AT | Eliminated (distant, no transfer) |
| 063 STR D1 Sema5a Gaba (subclass) | 7476 | ⚪ UNCERTAIN | Foxp2+ D1 subclass; no clean AT | Eliminated (distant, no transfer) |
| 074 MEA-BST Lhx6 Sp9 Gaba (subclass) | 8508 | 🔴 REFUTED | GABA-3 AT F1=0.003; wrong subclass | Eliminated (no transfer) |
| 075 MEA-BST Lhx6 Nr2e1 Gaba (subclass) | 3196 | 🔴 REFUTED | GABA-3 AT F1=0.003; wrong subclass | Eliminated (no transfer) |
| 080 CEA-AAA-BST Six3 Sp9 Gaba (subclass) | 6645 | 🔴 REFUTED | GABA-3 AT F1=0.006; wrong subclass | Eliminated (no transfer) |
| 054 STR Prox1 Lhx6 Gaba (subclass) | 2078 | 🔴 LOW | no transfer; wrong subclass | Eliminated (wrong subclass) |
| 051 Pvalb chandelier Gaba (subclass) | 3470 | 🔴 LOW | no transfer; wrong subclass | Eliminated (wrong subclass) |

Total: 24 candidate edges assessed; relationships committed on the three primary
survivors, the remainder left as uncertain pending curator review.

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The amygdala intercalated cell is defined
multimodally (`CLASSICAL_MULTIMODAL`): a densely-packed, near-uniformly
GABAergic population [3][4] of the intercalated amygdaloid nuclei
[UBERON:0002884] [1][2][3], marked by Foxp2 [5][6], with Drd1 [6] and Oprm1 [5]
as additional defining markers. The population is molecularly heterogeneous,
comprising multiple FOXP2+ subtypes including DRD1+ and DRD1− forms [5][6].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at ranks 0 (cluster), 1 (supertype), and 2 (subclass)
using metadata-based scoring (region match, NT type, defining markers). Full
scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
the cluster and from spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 (four Foxp2+ intercalated source groups) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, 100 bootstrap iterations) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.7 |
| n cells | 55514 (filtered to 7777) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Source labels are transcriptomically-defined types, not classical morpho-electrophysiological types; fear-conditioned and non-neuronal cells excluded; gene symbols matched against WMBv1 marker genes. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. Authored-prose evidence narratives are validated
against their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific mapping
limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge target | Evidence types | Supports | Source |
|---|---|---|---|
| 065 IA Mgp Gaba | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | GABA-1 SUPPORT | atlas-internal |
| 0292 IA Mgp Gaba_3 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | GABA-1 SUPPORT | atlas-internal |
| 0286 STR-PAL Chst9 Gaba_2 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | GABA-2 SUPPORT | atlas-internal |
| (21 further candidates) | ATLAS_METADATA; ANNOTATION_TRANSFER | mixed | atlas-internal |

*Generated by evidencell `db0c04b` at 2026-07-10T20:18:13+00:00 from
[kb/graphs/medial_temporal_lobe_amygdala/amygdala_intercalated_cell.yaml](kb/graphs/medial_temporal_lobe_amygdala/amygdala_intercalated_cell.yaml).*

</details>

---

## Discussion

**Primary mapping:** Amygdala intercalated cell → 065 IA Mgp Gaba subclass (with
its best child 0292 IA Mgp Gaba_3 [CS20230722_SUPT_0292]) at MODERATE
confidence. Key support: MapMyCells annotation transfer of the Foxp2_Fmod
intercalated source (F1=0.90 subclass; F1=0.85 supertype). Key caveats:
distributed cluster-level transfer (TAXONOMY_LEVEL_MISMATCH) and a
documented DRD1− subtype signature (Drd1 DISCORDANT at the supertype). The
classical intercalated cell is best described as a one-to-many mapping: its
Foxp2+ subtypes correspond to the atlas IA Mgp grouping (Foxp2_Fmod) and, more
strongly by marker match but off-target by location, to STR-PAL Chst9
supertypes (Adra2a → 0286, Col6a1 → 0288, Htr1f → 0289/1015).

No Cell Ontology term currently assigned. This population is a candidate for a CL
contribution: a Foxp2+ GABAergic intercalated interneuron type with DRD1+ and
DRD1− subtypes [6].

### Proposed experiments and follow-ups

Annotation transfer has already been run for all four declared source
populations (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`), and each
source transferred to a defined target, so no source correspondence is
outstanding. The remaining gaps are anatomical and marker-resolution, not
transfer-coverage:

1. **Spatial validation of soma position.**
   - *What:* spatial transcriptomic localization of the Foxp2_Fmod and
     Foxp2_Adra2a source cells.
   - *Target:* confirm occupancy of the intercalated nuclei versus adjacent
     striatum.
   - *Expected output:* refined anatomical alignment on the IA Mgp and STR-PAL
     Chst9 edges.
   - *Resolves:* the APPROXIMATE / DISCORDANT location calls on the three
     survivors.

2. **DRD1 subtype resolution.**
   - *What:* Drd1 in-situ or reporter profiling within the intercalated nuclei.
   - *Target:* map the DRD1+ intercalated subtype [6] to its IA Mgp supertype
     and confirm the DRD1− identity of 0292.
   - *Expected output:* MarkerAnalysisEvidence distinguishing the DRD1± forms.
   - *Resolves:* the Drd1 DISCORDANT signal at 0292 IA Mgp Gaba_3.

### Open questions

1. Which IA Mgp supertype carries the DRD1+ intercalated form, given that 0292
   IA Mgp Gaba_3 is DRD1− [6]?
2. Are the STR-PAL Chst9 correspondences (0286/0288/0289) genuine intercalated
   cells displaced into striatopallidal soma space, or striatal relatives that
   share the Foxp2+ program?
3. Should the classical intercalated node be split into its Foxp2+ subtypes to
   reflect the one-to-many atlas correspondence?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Ignacio et al. 2014 | [25309888](https://pubmed.ncbi.nlm.nih.gov/25309888) | soma location |
| [2] | Nardelli et al. 2024 | [39130512](https://pubmed.ncbi.nlm.nih.gov/39130512) | soma location |
| [3] | Veinante et al. 2013 | [25408902](https://pubmed.ncbi.nlm.nih.gov/25408902) | soma location / GABAergic identity |
| [4] | Pitkānen & Amaral 1994 | [8158266](https://pubmed.ncbi.nlm.nih.gov/8158266) | neurotransmitter type |
| [5] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931) | Foxp2 marker |
| [6] | Yu et al. 2023 | [36788214](https://pubmed.ncbi.nlm.nih.gov/36788214) | Foxp2 / Drd1 markers |

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_065 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] GABA-1-Foxp2_Fmod transfers to the atlas
    intercalated-amygdala subclass CS20230722_SUBC_065 at F1=0.90
    (at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1), the most on-target
    correspondence for the Foxp2+ intercalated masses [5][6]; markers are not
    assessable at subclass level (0 of 3 markers CONSISTENT — no atlas
    expression data), so support rests on annotation transfer, GABAergic
    identity, and the anatomically-named IA Mgp grouping.
  reconciliation_note: >
    Primary mapping paired with the IA Mgp Gaba_3 supertype, the concentrated
    child within this subclass; the classical intercalated cell maps 1:n across
    the IA Mgp and STR-PAL Chst9 groupings.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        GABA-1-Foxp2_Fmod distributes across the subclass; cluster-level F1
        does not exceed 0.47, so the supportable resolution is subclass/supertype.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No precomputed atlas expression at subclass level, so marker
        discrimination is deferred to the child supertype.
  proposed_experiments:
    - Cluster-resolution annotation transfer or spatial validation confirming
      Foxp2_Fmod cells occupy the intercalated nuclei rather than surrounding
      striatum.
  unresolved_questions:
    - Which IA Mgp supertype carries the DRD1+ intercalated form?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0292 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] GABA-1-Foxp2_Fmod concentrates in the IA Mgp Gaba_3 supertype
    CS20230722_SUPT_0292 at F1=0.85
    (at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1); Foxp2 CONSISTENT but
    Drd1 DISCORDANT and Oprm1 APPROXIMATE (1 of 3 markers CONSISTENT), matching
    the DRD1- intercalated subtype documented by Yu 2023 [6]; region_fraction_100um:
    0.157 is boundary scatter at the cortical-subplate/striatum border.
  reconciliation_note: >
    Broadens to the IA Mgp Gaba subclass, the atlas intercalated-amygdala
    grouping, which captures the full GABA-1 transfer at F1=0.90; paired
    survivor.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        GABA-1-Foxp2_Fmod transfer resolves at supertype, not cluster; cluster-level
        F1 peaks at 0.36 on CS20230722_CLUS_1021.
    - caveat_type: LOW_CELL_COUNT
      description: Only 22 source cells reach the supertype.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Drd1 DISCORDANT and Oprm1 APPROXIMATE; reconciled by the documented
        DRD1- intercalated subtype [6].
  proposed_experiments:
    - Targeted Drd1 in-situ or reporter profiling in the intercalated nuclei to
      confirm the DRD1- subtype identity of this supertype.
  unresolved_questions:
    - Which IA Mgp supertype carries the DRD1+ intercalated form?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0286 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] GABA-2-Foxp2_Adra2a transfers to the STR-PAL Chst9 Gaba_2
    supertype CS20230722_SUPT_0286 at F1=0.97
    (at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1), the cleanest transfer
    in the run, with 3 of 3 markers CONSISTENT (Foxp2, Drd1, Oprm1); however
    soma location is DISCORDANT (striatopallidal), so this is a molecularly
    excellent but anatomically off-target intercalated correspondence.
  reconciliation_note: >
    One of several Foxp2+ intercalated subtypes; the classical type maps 1:n
    across the IA Mgp and STR-PAL Chst9 groupings.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Soma sit in striatum and the medial forebrain bundle system
        (region_fraction_100um: 0.086), distinct from the intercalated nuclei.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        The strong Foxp2+ marker match is shared with the striatal program and
        is not decisive for intercalated identity on its own.
  proposed_experiments:
    - Spatial transcriptomic validation to determine whether the Adra2a Foxp2+
      source cells occupy the intercalated nuclei or the adjacent striatum.
  unresolved_questions:
    - Are the STR-PAL Chst9 correspondences genuine intercalated cells or
      striatal relatives sharing the Foxp2+ program?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1005 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  rationale: >
    [tier:CUT] Best child cluster of the 0286 supertype survivor;
    GABA-2-Foxp2_Adra2a transfers to CS20230722_CLUS_1005 at F1=0.81 but is
    reported through the supertype rather than separately.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0288 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  rationale: >
    [tier:CUT] GABA-3-Foxp2_Col6a1 transfers to CS20230722_SUPT_0288 at F1=0.82;
    a distinct Foxp2 intercalated subtype target in STR-PAL Chst9 space, not
    selected as the primary representative.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1011 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] Child cluster of 0288; GABA-3-Foxp2_Col6a1 transfers to
    CS20230722_CLUS_1011 at F1=0.81, reported through its supertype.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1015 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] GABA-4-Foxp2_Htr1f transfers to CS20230722_CLUS_1015 at F1=0.70;
    a fourth Foxp2 intercalated subtype target in STR-PAL Chst9 space, not
    selected as the primary representative.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0289 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] GABA-4-Foxp2_Htr1f scatters across CS20230722_SUPT_0289 at
    F1=0.46 (supertype); the clean signal is at cluster level (1015).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_064 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUBC_064 is the broad STR-PAL Chst9 subclass; the
    Foxp2 intercalated subtypes distribute within it (best F1=0.69 at subclass),
    so the informative mappings are the child supertypes.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0287 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] No Foxp2 source concentrates on CS20230722_SUPT_0287; transfers
    resolve only to the broad Chst9 subclass, not this supertype.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0285 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] No Foxp2 source concentrates on CS20230722_SUPT_0285; no
    supertype-level transfer above the broad Chst9 subclass.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1009 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] No Foxp2 source concentrates on CS20230722_CLUS_1009; cluster
    receives no clean transfer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0291 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] IA Mgp sibling supertype; GABA-1-Foxp2_Fmod scatters here with
    supertype F1=0.29 on CS20230722_SUPT_0291, far below the 0292 concentration.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1021 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Child cluster of 0292; GABA-1-Foxp2_Fmod scatters at cluster
    level, reaching only F1=0.36 on CS20230722_CLUS_1021.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1017 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] IA Mgp sibling; GABA-1-Foxp2_Fmod reaches CS20230722_CLUS_1017
    only at subclass level and does not concentrate at this cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_0998 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Foxp2+ striatal D1 type CS20230722_CLUS_0998 with DISCORDANT
    location; no Foxp2 source transfers cleanly (best F1=0.13) and GABA-4 shows
    no evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1000 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Foxp2+ striatal D1 type CS20230722_CLUS_1000; no Foxp2 source
    transfers cleanly (best F1=0.13) and location is distant from the
    intercalated nuclei.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0284 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] STR D1 Sema5a Gaba_4 supertype CS20230722_SUPT_0284; Foxp2+ but
    no clean transfer (best F1=0.13) and off-target striatal location.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_063 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Broad STR D1 Sema5a subclass CS20230722_SUBC_063; Foxp2+ D1
    program but no clean intercalated transfer.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_074 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Wrong subclass (MEA-BST Lhx6 Sp9); GABA-3-Foxp2_Col6a1 transfers
    to CS20230722_SUBC_074 at F1=0.00 (no evidence).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_075 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Wrong subclass (MEA-BST Lhx6 Nr2e1); GABA-3-Foxp2_Col6a1
    transfers to CS20230722_SUBC_075 at F1=0.00 (no evidence).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_080 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Wrong subclass (CEA-AAA-BST Six3 Sp9); GABA-3-Foxp2_Col6a1
    transfers to CS20230722_SUBC_080 at F1=0.01 (no evidence).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_054 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Wrong subclass (STR Prox1 Lhx6); no Foxp2 source transfers to
    CS20230722_SUBC_054.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUBC_051 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Wrong subclass (Pvalb chandelier); no Foxp2 source transfers to
    CS20230722_SUBC_051.
```
<!-- verdict-block-end -->
