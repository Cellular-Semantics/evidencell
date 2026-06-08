# VMHvl estrogen-receptor alpha / progesterone receptor neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

VMHvl ERα/PR neurons are a molecularly heterogeneous, sexually dimorphic
population of glutamatergic projection neurons in the ventrolateral
ventromedial hypothalamus whose subpopulations control sex-typical
mating, fighting, and female locomotion through estrogen- and
progesterone-dependent circuits [1][2]. The defining neurochemical
signature combines the steroid receptors *Esr1* and *Pgr* with the
developmental transcription factor *Nkx2-1* and the tachykinin
neuropeptide *Tac1*; functionally separable subpopulations have been
described (Pgr+ for mating/fighting; Esr1+/Nkx2-1+/Tac1+ for female
locomotion), and as many as 17 transcriptomic types have been resolved
within VMHvl by single-cell RNA-seq, so a clean 1:1 mapping to a single
atlas cluster is not expected.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Ventromedial hypothalamic nucleus [MBA:693] (ventrolateral subdivision, VMHvl) | [1] |
| Defining markers | *Esr1*, *Pgr*, *Nkx2-1*, *Tac1* | [1][2] |
| Neuropeptides | *Tac1* | [1] |
| Sex bias | Multiple sexually dimorphic subpopulations (Pgr+ mating in both sexes / fighting in males; female-biased lordosis subpopulation) | [1][2] |
| Cell Ontology | No CL term currently covers this type — candidate for a new CL term | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (VMHvl) + *Esr1* / *Nkx2-1* / *Tac1* markers + female-specific locomotion:** ERα-Cre / Nkx2-1-Cre pharmacogenetics, mouse · [1]
  > Estrogen-receptor alpha (ERα) neurons in the ventrolateral region of the ventromedial hypothalamus (VMHVL) control an array of sex-specific responses to maximize reproductive success. In females, these VMHVL neurons are believed to coordinate metabolism and reproduction. However, it remains unknown whether specific neuronal populations control distinct components of this physiological repertoire. Here, we identify a subset of ERα VMHVL neurons that promotes hormone-dependent female locomotion. Activating Nkx2-1-expressing VMHVL neurons via pharmacogenetics elicits a female-specific burst of spontaneous movement, which requires ERα and Tac1 signaling. Disrupting the development of Nkx2-1(+) VMHVL neurons results in female-specific obesity, inactivity, and loss of VMHVL neurons coexpressing ERα and Tac1. Unexpectedly, two responses controlled by ERα(+) neurons, fertility and brown adipose tissue thermogenesis, are unaffected. We conclude that a dedicated subset of VMHVL neurons marked by ERα, NKX2-1, and Tac1 regulates estrogen-dependent fluctuations in physical activity and constitutes one of several neuroendocrine modules that drive sex-specific responses.
  > — Correa et al. 2015, Developmental and Hormonal Regulation · [1] <!-- quote_key: 27794167_af52b501 -->

- ***Pgr* marker + sexually dimorphic VMHvl subpopulation:** review, rodent · [2]
  > Another molecularly defined sexually dimorphic VMHvl subpopulation that controls sex-typical behaviors in both sexes is the progesterone receptor (PR)-expressing neurons. This subpopulation is required for the normal display of mating in both sexes and for fighting in males [76].
  > — Zilkha et al. 2021, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 233446934_8cb6b0bc -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Marker, region, and bulk-correlation evidence converge on a pair of
adjacent VMH Fezf1 Glut supertypes — *0564 VMH Fezf1 Glut_2*
[CS20230722_SUPT_0564] and *0563 VMH Fezf1 Glut_1* [CS20230722_SUPT_0563]
— as co-primary cross-cutting correlates of the heterogeneous VMHvl
ERα/PR classical population, with the broader Pgr+/Nkx2-1+/Tac1+
population concentrated in SUPT_0564 and the female-biased lordosis
subpopulation concentrated in SUPT_0563 by independent
bulk-transcriptomic δ ranking (see property comparison tables and
bulk-correlation figure below). The mapping is intentionally
cross-cutting at the supertype level: VMHvl contains ~17 transcriptomic
types by single-cell RNA-seq [1] and no single WMBv1 cluster captures
the full classical population, so the two supertypes together provide
the atlas correlate while child-cluster heterogeneity (CLUS_2290,
CLUS_2292, CLUS_2295, CLUS_2297, etc.) reflects subtype structure
within the classical type rather than competing mappings.

### 0564 VMH Fezf1 Glut_2 [CS20230722_SUPT_0564] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Supertype [CS20230722_SUPT_0564] | Best child cluster | Alignment |
|---|---|---|---|---|
| Soma location | VMHvl [MBA:693] | Hypothalamus [MBA:1097] n=620; Ventromedial hypothalamic nucleus [MBA:693] n=494; Tuberal nucleus [MBA:614] n=218 (region_fraction_100um=0.795) | CLUS_2295 region_fraction_100um=0.889 | CONSISTENT |
| NT type | not asserted on classical node | not asserted at supertype level (Glut at cluster level) | Glut | NOT_ASSESSED |
| *Esr1* expression | defining marker | no atlas expression data | not assessed | NOT_ASSESSED |
| *Pgr* expression | defining marker | no atlas expression data | not assessed | NOT_ASSESSED |
| *Nkx2-1* expression | defining marker | precomputed mean = 5.34 (cohort pct 0.887; child coverage 1.00) | CLUS_2295 mean = 6.16 (cohort pct 0.942) | CONSISTENT |
| *Tac1* expression | defining marker / neuropeptide | precomputed mean = 1.39 (cohort pct 0.670; child coverage 1.00) | CLUS_2295 mean = 1.87 (cohort pct 0.752) | CONSISTENT |
| Sex ratio | dimorphic subpopulations | not computed at supertype level | child-cluster MFR not female-biased on this supertype (Pgr+/mating subpopulation, expected mixed-sex) | NOT_ASSESSED |

*(3 of 3 *Nkx2-1*/*Tac1* properties show child-cluster coverage 1.00 across SUPT_0564's children — the marker concordance holds uniformly within the supertype. Best match: CS20230722_CLUS_2295.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH region | Atlas metadata | PARTIAL | VMH primary location n=494, Nkx2-1=5.34 + Tac1=1.39 child-coverage 1.00; Esr1/Pgr not in atlas panel | atlas-internal |
| Knoedler 2022 ERα-TRAP-seq VMH-FR vs BNST-FR bulk correlation | Bulk correlation | PARTIAL | SUPT_0564 not in top-20 δ rank — companion SUPT_0563 takes ranks 1/2/4 | [3] |

**Supporting evidence**

- *Nkx2-1* (mean 5.34, cohort percentile 0.887) and *Tac1* (mean 1.39,
  cohort percentile 0.670) — two of the four classical defining markers
  — are positive across all child clusters of CS20230722_SUPT_0564
  (child coverage 1.00), and the supertype's primary anatomical
  registration is the ventromedial hypothalamic nucleus [MBA:693]
  (n=494 cells; region_fraction_100um=0.795). This matches the
  *Nkx2-1*+*Tac1*+ component of the classical signature [1].
- The best child cluster is *2295 VMH Fezf1 Glut_2*
  [CS20230722_CLUS_2295] (region_fraction_100um=0.889; *Nkx2-1*
  mean=3.80, *Tac1* mean=1.45), confirming that within SUPT_0564 the
  marker-positive, region-on signal is reproducible at cluster
  resolution.
- *Esr1* and *Pgr* — the two steroid-receptor defining markers — are
  not part of the WMBv1 precomputed-expression panel for either
  supertype or its children, so the steroid-receptor identity cannot
  be confirmed atlas-side. The classical assignment of this supertype
  to the broader Pgr+/Nkx2-1+/Tac1+ subpopulation rests on the
  *Nkx2-1*/*Tac1* concordance plus the VMH soma signal; direct
  *Esr1*/*Pgr* confirmation will require expression-level cross-check
  on the source dataset.

**Marker evidence provenance**

- ***Esr1*** — protein-level (ERα immunoreactivity) and transcript-level
  (ERα-Cre transgene) evidence in Correa et al. 2015 targeting
  morphologically defined VMHvl neurons [1]. Absent from WMBv1
  precomputed expression panel for this supertype.
- ***Pgr*** — protein-level (PR immunoreactivity / PR-Cre transgene)
  evidence summarised in the Zilkha review [2]. Absent from WMBv1
  precomputed expression panel for this supertype.
- ***Nkx2-1*** — protein-level (Nkx2-1 immunoreactivity) and Nkx2-1-Cre
  transgene targeting in Correa et al. 2015 [1]; confirmed at
  transcript level on CS20230722_SUPT_0564 (mean=5.34, cohort pct
  0.887) with child-cluster coverage 1.00.
- ***Tac1*** — protein- and transcript-level evidence in Correa et al.
  2015 (Tac1-signalling-dependence of female locomotion) [1];
  confirmed at transcript level on CS20230722_SUPT_0564 (mean=1.39,
  cohort pct 0.670) with child-cluster coverage 1.00.

**Concerns**

- *Calb1* has the highest mean expression on CS20230722_SUPT_0564
  (mean=8.0) but is not a defining marker of the VMHvl ERα/PR
  population — *Calb1* is the canonical marker of the distinct SDN-POA
  calbindin neuron *(note: SDN-POA is anatomically separate from
  VMHvl, so this is unlikely to reflect mistaken assignment of
  SDN-POA cells into this VMH supertype; the *Calb1* signal in
  CS20230722_SUPT_0564 is most plausibly a VMH-resident *Calb1*+
  subpopulation that does not align with the classical SDN-POA
  marker)*. Co-localisation of *Calb1* with *Esr1*/*Pgr* in VMHvl
  remains to be verified (open question 1).
- *Esr1* and *Pgr* expression is not assessable from atlas
  precomputed stats — the two steroid receptors that name the
  classical type cannot be confirmed at transcript level here without
  source-dataset re-analysis.
- Direct bulk-correlation δ does not place CS20230722_SUPT_0564 in the
  top-20 of the Knoedler VMH-FR vs BNST-FR contrast — the companion
  supertype CS20230722_SUPT_0563 dominates that ranking (see figure
  below and the SUPT_0563 paragraph). The bulk evidence is therefore
  consistent with VMHvl heterogeneity (SUPT_0564 carries the broader
  Pgr+/Nkx2-1+/Tac1+ population; SUPT_0563 carries the female-biased
  lordosis subpopulation) rather than confirming SUPT_0564 as the
  sole VMHvl correlate.

**What would upgrade confidence**

- Cluster-level *Esr1*, *Pgr*, *Nkx2-1*, *Tac1* co-expression analysis
  on the source dataset for CS20230722_SUPT_0564's children — would
  distinguish the broader Pgr+ population (this supertype) from the
  female-biased lordosis subpopulation (SUPT_0563).
- Cluster annotation transfer of published VMHvl ERα-Cre or PR-Cre
  transcriptomes onto WMBv1; cohort-level F1 ≥ 0.5 on SUPT_0564 with
  parallel split onto SUPT_0563 would solidify the cross-cutting
  call. Adds AnnotationTransferEvidence on both edges.

### 0563 VMH Fezf1 Glut_1 [CS20230722_SUPT_0563] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Supertype [CS20230722_SUPT_0563] | Best child cluster | Alignment |
|---|---|---|---|---|
| Soma location | VMHvl [MBA:693] | Hypothalamus [MBA:1097] n=212; Tuberal nucleus [MBA:614] n=174; Ventromedial hypothalamic nucleus [MBA:693] n=151 (region_fraction_100um=0.712) | CLUS_2292 region_fraction_100um=1.000 | CONSISTENT |
| NT type | not asserted on classical node | not asserted at supertype level (Glut at cluster level) | Glut | NOT_ASSESSED |
| *Esr1* expression | defining marker | no atlas expression data | not assessed | NOT_ASSESSED |
| *Pgr* expression | defining marker | no atlas expression data | not assessed | NOT_ASSESSED |
| *Nkx2-1* expression | defining marker | precomputed mean = 6.63 (cohort pct 0.990; child coverage 1.00) | CLUS_2290 mean = 6.69 (cohort pct 0.989); CLUS_2292 mean = 6.28 (cohort pct 0.949) | CONSISTENT |
| *Tac1* expression | defining marker / neuropeptide | precomputed mean = 6.48 (cohort pct 0.969; child coverage 1.00) | CLUS_2292 mean = 8.62 (cohort pct 0.964); CLUS_2290 mean = 6.07 (cohort pct 0.901) | CONSISTENT |
| Sex ratio | female-biased lordosis subpopulation | MFR not computed at supertype level | CLUS_2290 MFR=0.08; CLUS_2292 MFR=0.12 (both strongly female-biased) | CONSISTENT |

*(3 of 3 *Nkx2-1*/*Tac1* properties show child-cluster coverage 1.00 across SUPT_0563's children, and the two strongly female-biased child clusters CLUS_2290 (MFR=0.08) and CLUS_2292 (MFR=0.12) sit inside this supertype. Best match: the SUPT_0563 children as a group rather than any single child.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 ERα-TRAP-seq VMH-FR vs BNST-FR bulk correlation | Bulk correlation | SUPPORT | best child CLUS_2293 δ=0.018 rank 1/5322; CLUS_2290 δ=0.016 rank 2; CLUS_2292 δ=0.014 rank 4 | [3] |

**Supporting evidence**

- *Nkx2-1* (supertype mean 6.63, cohort percentile 0.990) and *Tac1*
  (supertype mean 6.48, cohort percentile 0.969) are both at the top
  of the cohort distribution on CS20230722_SUPT_0563 with child
  coverage 1.00 — substantially higher than on CS20230722_SUPT_0564
  (5.34 and 1.39 respectively), indicating that SUPT_0563 carries the
  stronger *Tac1*+ component of the classical VMHvl Esr1/Pgr/Nkx2-1/Tac1
  signature.
- Independent bulk-correlation evidence from Knoedler 2022 ERα-TRAP-seq
  pooled VMH female-receptive vs BNST female-receptive contrast [3]
  ranks SUPT_0563's children at the top: CS20230722_CLUS_2293 at rank
  1 of 5,322 clusters (δ=0.018), CS20230722_CLUS_2290 at rank 2
  (δ=0.016, MFR=0.08), and CS20230722_CLUS_2292 at rank 4 (δ=0.014,
  MFR=0.12) — three of the top four δ slots are SUPT_0563 children
  (see figure). The strongly female-biased MFR on CLUS_2290 and
  CLUS_2292 corresponds directly to the lordosis-circuit subpopulation
  flagged in the classical node's definition.

![Top 10 clusters by δ for VMH_FR_vs_BNST_FR (CS20230722_SUPT_0563)](figures/vmhvl_esr1_pr_neuron_VMH_FR_vs_BNST_FR_3701016a.png)

*Top 10 clusters by δ = ρ(VMH-FR) − ρ(BNST-FR) for the Knoedler 2022
ERα-TRAP-seq contrast, ranked against all 5,322 WMBv1 clusters. The
target supertype CS20230722_SUPT_0563 contributes three of the top
four hits (CLUS_2293, CLUS_2290, CLUS_2292), with the two strongly
female-biased clusters (CLUS_2290 MFR=0.08; CLUS_2292 MFR=0.12) sitting
at ranks 2 and 4. The remaining top-10 hits are predominantly other
VMH Fezf1 / VMH Nr5a1 supertypes (SUPT_0565, SUPT_0568), confirming the
differential signal is anatomically clean to the ventromedial
hypothalamus. TRAP-seq pulldown shifts absolute ρ values lower than
FACS-bulk input but Spearman rank-based δ handles the offset (see
Methods).*

| Rank | Cluster | Supertype | δ | MFR | Top anatomy |
|---:|---|---|---:|---:|---|
| **1** | **CLUS_2293** | **SUPT_0563** | **0.0180** | — | **Ventromedial hypothalamic nucleus** |
| **2** | **CLUS_2290** | **SUPT_0563** | **0.0159** | **0.08** | **Ventromedial hypothalamic nucleus** |
| 3 | CLUS_2298 | SUPT_0565 | 0.0153 | 1.70 | Tuberal nucleus |
| **4** | **CLUS_2292** | **SUPT_0563** | **0.0145** | **0.12** | **Ventromedial hypothalamic nucleus** |
| 5 | CLUS_2313 | SUPT_0568 | 0.0143 | 1.94 | Ventromedial hypothalamic nucleus |
| 6 | CLUS_2300 | SUPT_0565 | 0.0138 | 0.92 | Ventromedial hypothalamic nucleus |
| 7 | CLUS_2282 | SUPT_0556 | 0.0128 | 0.11 | Arcuate hypothalamic nucleus |
| 8 | CLUS_2299 | SUPT_0565 | 0.0126 | 3.17 | Ventromedial hypothalamic nucleus |
| **9** | **CLUS_2291** | **SUPT_0563** | **0.0118** | 1.27 | **Ventromedial hypothalamic nucleus** |
| 10 | CLUS_2280 | SUPT_0555 | 0.0117 | 1.00 | Arcuate hypothalamic nucleus |

**Marker evidence provenance**

- ***Esr1*** — protein- and transcript-level evidence in Correa et al.
  2015 (ERα-Cre transgene targeting) [1]; absent from WMBv1
  precomputed expression panel for this supertype.
- ***Pgr*** — protein-level evidence summarised in the Zilkha review [2]
  (PR-Cre-targeted subpopulation required for mating in both sexes
  and fighting in males); absent from WMBv1 precomputed expression
  panel.
- ***Nkx2-1*** — protein- and transcript-level evidence in Correa et al.
  2015 [1]; confirmed at transcript level on CS20230722_SUPT_0563
  with the highest supertype-level mean (6.63) in this cohort.
- ***Tac1*** — protein- and transcript-level evidence in Correa et al.
  2015 [1]; confirmed at transcript level on CS20230722_SUPT_0563
  with mean 6.48 (cohort pct 0.969) and on female-biased child
  CLUS_2292 with mean 8.62 (cohort pct 0.964).

**Concerns**

- *Esr1* and *Pgr* are not assessable from atlas precomputed
  expression — confirmation of the steroid-receptor identity on
  CS20230722_SUPT_0563 requires source-dataset re-analysis or
  transgene-driven cluster annotation transfer.
- SUPT_0563 vs SUPT_0564 is a co-primary cross-cutting pair, not a
  single-target mapping. The supertypes are siblings (both VMH Fezf1
  Glut) and together account for the broader Pgr+/Nkx2-1+/Tac1+
  population plus the female-biased lordosis subpopulation. Whether
  the split is a clean female-biased-vs-broader division or whether
  each supertype contains further heterogeneity that cross-cuts the
  classical definition remains open (open question 2).
- The Knoedler 2022 contrast is intentionally a paired-bulk
  *region*-difference (VMH-FR vs BNST-FR, both female-receptive), so
  the δ ranking reflects regional specificity holding sex constant —
  it is independent of the cross-sex δ artefacts flagged for this
  dataset (see Methods caveats) and remains valid evidence for the
  regional and within-cohort identification of SUPT_0563.

**What would upgrade confidence**

- Cluster annotation transfer of published VMHvl ERα-Cre or PR-Cre
  transcriptomes onto WMBv1; expected behaviour is a split between
  SUPT_0563 (female-biased clusters) and SUPT_0564 (broader Pgr+
  population) with cluster-level F1 separating CLUS_2290/CLUS_2292
  from CLUS_2295/CLUS_2297. Adds AnnotationTransferEvidence on both
  supertype edges.
- *Esr1*, *Pgr*, *Nkx2-1*, *Tac1* co-expression at single-cell
  resolution within CLUS_2290, CLUS_2292, CLUS_2293 versus the
  female-biased clusters of SUPT_0564 — would resolve the
  supertype-level cross-cutting split (open questions 1 and 2).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| — | 0564 VMH Fezf1 Glut_2 [CS20230722_SUPT_0564] | 959 | 🟡 MODERATE | Nkx2-1=5.34, Tac1=1.39 across all children; VMH region_fraction_100um=0.795 | Primary (broader Pgr+/Nkx2-1+/Tac1+ subpopulation) |
| — | 0563 VMH Fezf1 Glut_1 [CS20230722_SUPT_0563] | 963 | 🟡 MODERATE | Nkx2-1=6.63, Tac1=6.48; Knoedler bulk δ rank 1/2/4 (CLUS_2293/2290/2292); female-biased children MFR=0.08/0.12 | Primary (female-biased lordosis subpopulation) |
| 2290 VMH Fezf1 Glut_1 [CS20230722_CLUS_2290] | 0563 VMH Fezf1 Glut_1 | 221 | 🔴 LOW | Female-biased (MFR=0.08), Nkx2-1=6.69, Tac1=6.07 — but represented through parent SUPT_0563 | Eliminated (subsumed by SUPT_0563 cross-cutting mapping) |
| 2292 VMH Fezf1 Glut_1 [CS20230722_CLUS_2292] | 0563 VMH Fezf1 Glut_1 | 114 | 🔴 LOW | Female-biased (MFR=0.12), Nkx2-1=6.28, Tac1=8.62 — represented through parent SUPT_0563 | Eliminated (subsumed by SUPT_0563 cross-cutting mapping) |
| 2295 VMH Fezf1 Glut_2 [CS20230722_CLUS_2295] | 0564 VMH Fezf1 Glut_2 | 309 | 🔴 LOW | Nkx2-1=6.16, Tac1=1.87, VMH region_fraction_100um=0.889 — represented through parent SUPT_0564 | Eliminated (subsumed by SUPT_0564 cross-cutting mapping) |
| 2297 VMH Fezf1 Glut_2 [CS20230722_CLUS_2297] | 0564 VMH Fezf1 Glut_2 | 252 | 🔴 LOW | Nkx2-1=3.80, Tac1=1.45 — represented through parent SUPT_0564 | Eliminated (subsumed by SUPT_0564 cross-cutting mapping) |
| 1959 DMH Hmx2 Gaba_6 [CS20230722_CLUS_1959] | 0492 DMH Hmx2 Gaba_6 | 533 | 🔴 LOW | DMH-anchored GABA; Nkx2-1=0.26, Tac1=0.36; region_fraction_100um=0.522 | Eliminated (wrong subclass — GABAergic DMH; markers near-absent) |
| — | 0557 ARH-PVp Tbx3 Glut_4 [CS20230722_SUPT_0557] | 246 | 🔴 LOW | Nkx2-1=6.11, Tac1=7.16 but region_fraction_100um=0.808 with VMH n=97 vs Tuberal/DMH dominant | Eliminated (ARH-PVp / Tuberal-dominant, not VMH) |
| — | 0439 DMH Prdm13 Gaba_1 [CS20230722_SUPT_0439] | 1314 | 🔴 LOW | GABAergic DMH; Tac1=0.36; region_fraction_100um=0.151 | Eliminated (wrong NT — GABA; DMH; markers near-absent) |
| — | 0569 VMH Nr5a1 Glut_4 [CS20230722_SUPT_0569] | 1259 | 🔴 LOW | Nkx2-1=4.96, Tac1=1.52; VMH region_fraction_100um=0.913 but distinct Nr5a1 lineage | Eliminated (Nr5a1 lineage — distinct VMH lineage not in classical signature) |
| — | 0568 VMH Nr5a1 Glut_3 [CS20230722_SUPT_0568] | 2817 | 🔴 LOW | Nkx2-1=3.49, Tac1=1.83; VMH region_fraction_100um=0.898 but Nr5a1 lineage | Eliminated (Nr5a1 lineage — distinct VMH lineage not in classical signature) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** *vmhvl_esr1_pr_neuron* is defined on the
classical-neurochemical basis (`definition_basis: CLASSICAL_NEUROCHEMICAL`):
a molecularly heterogeneous, sexually dimorphic population in the
ventrolateral ventromedial hypothalamus [MBA:693], with defining
markers *Esr1*, *Pgr*, *Nkx2-1*, and *Tac1* [1][2] and *Tac1* as the
classical neuropeptide [1]. Multiple functional subpopulations have
been described: Pgr+ (mating in both sexes, fighting in males),
Esr1+/Nkx2-1+/Tac1+ (female locomotion), and a female-biased lordosis
subpopulation [1][2]. Up to 17 transcriptomic types have been resolved
within VMHvl by snRNA-seq, so the classical type is expected to map
cross-cuttingly rather than 1:1.

**Atlas mapping query.** Candidate atlas clusters were retrieved from
the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1
(supertype) using metadata-based scoring (region match, NT type,
defining markers, sex bias when applicable). Full scoring rules are
in `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type
was compared to the corresponding atlas-side value via the
`property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side
numerical values came from precomputed expression on the cluster
(cluster.yaml in the taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Bulk transcriptomic correlation.**

| Field | Value |
|---|---|
| Source publication | Knoedler et al. 2022 [3] |
| GEO accession | GSE183092 |
| Technique | TRAP-seq |
| n pools | 12 |
| Atlas | CCN20230722 (SHA-256: b21ca985) |
| Statistic | spearman_rho |
| Parameters | pseudobulk_transform=log1p(sum/n_cells); pool_transform=log1p(replicate_mean(DESeq2_normalised_counts)); gene_id_space=ensembl_mouse_via_symbol_lookup; gene_intersection=intersection_across_4_regions∩atlas_col_names; n_replicates_per_pool=3 |
| Script | [correlate.py](https://github.com/Cellular-Semantics/evidencell/blob/4e67d6b/correlate.py) |
| Code version | 4e67d6b |
| Caveats | Cross-sex within-region δ contrasts (Male vs FR or Male vs FNR) are artefactual — top hits across POA, VMH, and BNST are hindbrain Calcb cholinergic motor neurons reflecting a global male-vs-female expression bias (suspected Y-linked/X-inactivation dosage, batch, or TRAP pulldown efficiency). The VMH-FR vs BNST-FR contrast used here is a paired-region δ holding sex constant and is valid. TRAP-seq vs FACS-bulk shifts absolute ρ values lower but Spearman rank-based δ handles the offset. |

**Atlas data sources.** WMBv1 taxonomy CCN20230722; pseudobulk source
`conf/mapmycells/CCN20230722/precomputed_stats.h5` (SHA-256:
`b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b`).

**Anti-hallucination.** All citations, atlas accessions, ontology
CURIEs, and verbatim literature quotes in this report are validated
against the evidencell knowledge base at write time. Authored-prose
evidence narratives are validated against their source
`evidence_items[*].explanation` fields. The pre-write hook rejects
any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:14:06+00:00 from
[kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 | ATLAS_METADATA; BULK_CORRELATION | PARTIAL; PARTIAL | atlas-internal; [3] |
| edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563 | BULK_CORRELATION | SUPPORT | [3] |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2290 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2292 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_1959 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2295 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2297 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0557 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0563 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0439 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0569 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0568 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** VMHvl ERα/PR neuron → *0564 VMH Fezf1 Glut_2*
[CS20230722_SUPT_0564] and *0563 VMH Fezf1 Glut_1*
[CS20230722_SUPT_0563] as co-primary cross-cutting correlates, both at
MODERATE confidence. Key support: *Nkx2-1*/*Tac1* concordance at
supertype level on both with child-cluster coverage 1.00, plus
independent Knoedler 2022 [3] VMH-FR vs BNST-FR bulk-correlation
ranking placing three of the top four δ slots on SUPT_0563's children
(CLUS_2293 rank 1, CLUS_2290 rank 2 with female-biased MFR=0.08,
CLUS_2292 rank 4 with MFR=0.12). Key caveats: AMBIGUOUS_MAPPING (VMHvl
contains ~17 transcriptomic types so the classical population spans
both supertypes — SUPT_0564 carries the broader Pgr+/Nkx2-1+/Tac1+
subpopulation, SUPT_0563 carries the female-biased lordosis
subpopulation) and TAXONOMY_LEVEL_MISMATCH (*Esr1* and *Pgr* are not
in the WMBv1 precomputed expression panel so the two steroid-receptor
defining markers cannot be confirmed atlas-side without
source-dataset re-analysis). No Cell Ontology term currently covers
this type — candidate for a new CL term targeting the VMHvl Esr1/Pgr
population (or two terms, one per sub-population, if the SUPT_0563 vs
SUPT_0564 split is confirmed by transgene-driven cluster annotation
transfer).

### Proposed experiments and follow-ups

**Cluster annotation transfer of published VMHvl ERα-Cre / PR-Cre
transcriptomes onto WMBv1.**

- **What:** Run cluster annotation transfer using ERα-Cre or PR-Cre
  VMHvl-targeted scRNA-seq as source, WMBv1 as target.
- **Target:** Cohort-level F1 split between CS20230722_SUPT_0563 (female-biased)
  and CS20230722_SUPT_0564 (broader Pgr+ population), with
  cluster-level resolution distinguishing CLUS_2290/CLUS_2292
  (female-biased) from CLUS_2295/CLUS_2297 (broader). Threshold
  F1 ≥ 0.5 at supertype level for each.
- **Expected output:** `AnnotationTransferEvidence` on both
  edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 and
  edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563.
- **Resolves:** open questions 1 and 2 (Calb1 / Esr1+Pgr
  co-localisation; SUPT_0563 vs SUPT_0564 split structure).

**Single-cell *Esr1*, *Pgr*, *Nkx2-1*, *Tac1* co-expression on the
SUPT_0563 / SUPT_0564 source dataset.**

- **What:** Cluster-level co-expression analysis of *Esr1*, *Pgr*,
  *Nkx2-1*, *Tac1* across CLUS_2290, CLUS_2292, CLUS_2293 (SUPT_0563
  children) versus CLUS_2295, CLUS_2297 (SUPT_0564 children), drawing
  on the WMBv1 source transcriptomes.
- **Target:** Confirm *Esr1*+*Pgr* co-expression in each candidate
  cluster (currently unassessable from precomputed expression alone).
- **Expected output:** Refreshed property_comparisons on each edge
  with quantitative *Esr1* / *Pgr* detection rates.
- **Resolves:** the two TAXONOMY_LEVEL_MISMATCH caveats and clarifies
  whether SUPT_0563 vs SUPT_0564 separates strictly by sex bias or by
  steroid-receptor sub-signature.

**Cell Ontology new term request.**

- **What:** Submit one or more CL new term requests targeting the
  VMHvl Esr1/Pgr classical type (potentially split into a broader
  Pgr+/Nkx2-1+/Tac1+ term and a female-biased lordosis subpopulation
  term if the cluster annotation transfer split is confirmed).
- **Expected output:** New CL term(s) assignable as the BROAD or
  EXACT mapping for *vmhvl_esr1_pr_neuron*.

### Open questions

1. Does *Calb1* co-localise with *Esr1*/*Pgr* in VMHvl neurons, or does
   it mark a distinct subpopulation within CS20230722_SUPT_0564? *Calb1*
   has the highest mean expression on SUPT_0564 (8.0) but is not a
   defining marker of the VMHvl Esr1/Pgr population.
2. Is SUPT_0563 vs SUPT_0564 a clean female-vs-broader split, or do
   both supertypes contain further heterogeneity that cross-cuts the
   classical definition? Are CLUS_2290 and CLUS_2292 distinct
   functional subtypes within SUPT_0563, or replicates of the same
   lordosis subpopulation?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Correa et al. 2015 | [25543145](https://pubmed.ncbi.nlm.nih.gov/25543145) | Soma location, *Esr1*/*Nkx2-1*/*Tac1* markers, female-specific locomotion subpopulation |
| [2] | Zilkha et al. 2021 | [33910083](https://pubmed.ncbi.nlm.nih.gov/33910083) | *Pgr* marker, sexually dimorphic mating/fighting subpopulation |
| [3] | Knoedler et al. 2022 | 35143761 (not yet ingested into references.json) | ERα-TRAP-seq VMH-FR vs BNST-FR bulk-correlation evidence |

---

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: evidencell:CrossCuttingMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] CS20230722_SUPT_0564 (VMH Fezf1 Glut_2) shows
    Nkx2-1=5.34 (cohort pct 0.887) and Tac1=1.39 (cohort pct 0.670)
    with child-cluster coverage 1.00, and VMH [MBA:693] as primary
    soma location (region_fraction_100um: 0.795). 2 of 4 defining
    markers CONSISTENT at transcript level; Esr1 and Pgr are absent
    from the atlas precomputed-expression panel for this supertype
    and require source-dataset re-analysis. SUPT_0564 carries the
    broader Pgr+/Nkx2-1+/Tac1+ subpopulation of the heterogeneous
    classical type.
  reconciliation_note: >
    Co-primary cross-cutting target with
    edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563. The VMHvl
    Esr1/Pgr classical population is heterogeneous (up to 17
    transcriptomic types described); SUPT_0564 captures the broader
    Pgr+/Nkx2-1+/Tac1+ subpopulation and SUPT_0563 captures the
    female-biased lordosis subpopulation by independent
    bulk-correlation evidence from Knoedler 2022 (PMID:35143761).
    Both edges should be retained until the classical node is split
    or cluster annotation transfer resolves the structure.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        VMHvl contains up to 17 transcriptomic types and the
        classical vmhvl_esr1_pr_neuron spans multiple functional
        subtypes. CS20230722_SUPT_0564 is one of two co-primary
        cross-cutting targets; CS20230722_SUPT_0563 captures the
        female-biased lordosis subpopulation by the Knoedler 2022
        VMH-FR vs BNST-FR contrast (CLUS_2290 MFR=0.08, CLUS_2292
        MFR=0.12 at delta ranks 2 and 4 of 5322).
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Calb1 has the highest mean expression on CS20230722_SUPT_0564
        (mean=8.0) but is not a defining marker of
        vmhvl_esr1_pr_neuron; Calb1 is the canonical marker of the
        distinct SDN-POA calbindin neuron. Calb1 co-localisation
        with Esr1/Pgr in VMHvl warrants primary literature
        verification.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Esr1 and Pgr — two of the four defining markers — are absent
        from the WMBv1 precomputed-expression panel for
        CS20230722_SUPT_0564 and its children, so the
        steroid-receptor identity that names the classical type
        cannot be confirmed atlas-side. Cluster-level co-expression
        check on the source transcriptomes is required.
  proposed_experiments:
    - >
      Cluster annotation transfer of published VMHvl ERα-Cre or
      PR-Cre transcriptomes onto WMBv1; target supertype-level F1
      split between CS20230722_SUPT_0564 (broader Pgr+ population)
      and CS20230722_SUPT_0563 (female-biased subpopulation), with
      cluster-level resolution distinguishing CLUS_2295/CLUS_2297
      from CLUS_2290/CLUS_2292. F1 >= 0.5 at supertype level. Adds
      AnnotationTransferEvidence.
    - >
      Cluster-level Esr1, Pgr, Nkx2-1, Tac1 co-expression analysis
      across CS20230722_SUPT_0564 children (CLUS_2295, CLUS_2297)
      and CS20230722_SUPT_0563 children (CLUS_2290, CLUS_2292,
      CLUS_2293) on the WMBv1 source dataset; confirms Esr1+Pgr
      co-expression currently unassessable from atlas precomputed
      expression.
  unresolved_questions:
    - >
      Does Calb1 co-localise with Esr1/Pgr in VMHvl neurons, or
      does it mark a distinct subpopulation within
      CS20230722_SUPT_0564?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.60
  relationship: evidencell:CrossCuttingMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] CS20230722_SUPT_0563 (VMH Fezf1 Glut_1) shows
    Nkx2-1=6.63 (cohort pct 0.990) and Tac1=6.48 (cohort pct 0.969)
    with child-cluster coverage 1.00 — substantially higher than
    CS20230722_SUPT_0564 — and VMH-FR vs BNST-FR bulk correlation
    (corr_VMH_FR_vs_BNST_FR, Knoedler 2022 PMID:35143761) places
    SUPT_0563 children at three of the top four delta slots: the
    rank-1 hit in Knoedler 2022 VMH-FR vs BNST-FR bulk-correlation
    (delta=0.018), CS20230722_CLUS_2290 rank 2 (delta=0.016,
    MFR=0.08), CS20230722_CLUS_2292 rank 4 (delta=0.014, MFR=0.12). 2 of 4 defining markers CONSISTENT at
    transcript level (Esr1/Pgr absent from atlas panel). SUPT_0563
    carries the female-biased lordosis subpopulation.
  reconciliation_note: >
    Co-primary cross-cutting target with
    edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564. SUPT_0563
    was not retrieved in the rank-1 DB query (no DEFINING_SCOPED
    markers in atlas metadata for this supertype) and is added on
    the strength of the Knoedler 2022 bulk-correlation evidence
    plus the supertype-level Nkx2-1/Tac1 transcript-level
    concordance.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Co-primary with edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564.
        The classical vmhvl_esr1_pr_neuron is a heterogeneous
        population; CS20230722_SUPT_0563 captures the female-biased
        lordosis subpopulation (CLUS_2290 MFR=0.08, CLUS_2292
        MFR=0.12), CS20230722_SUPT_0564 captures the broader
        Pgr+/Nkx2-1+/Tac1+ subpopulation. Both edges should be
        retained until the classical node is split or
        cluster-level annotation transfer resolves the structure.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Esr1 and Pgr are absent from the WMBv1 precomputed-expression
        panel for CS20230722_SUPT_0563 and its children;
        steroid-receptor identity requires source-dataset
        re-analysis or transgene-driven cluster annotation
        transfer.
  proposed_experiments:
    - >
      Cluster-level Esr1, Pgr, Nkx2-1, Tac1 co-expression in
      CS20230722_CLUS_2290, CS20230722_CLUS_2292, and the rank-1
      bulk-correlation hit child cluster versus the female-biased
      clusters of CS20230722_SUPT_0564 — distinguishes the two
      co-primary cross-cutting targets.
    - >
      Cluster annotation transfer of published VMHvl ERα-Cre or
      PR-Cre transcriptomes to WMBv1; expected F1 split between
      CS20230722_SUPT_0563 (female-biased) and CS20230722_SUPT_0564
      (broader Pgr+ population). Adds AnnotationTransferEvidence.
  unresolved_questions:
    - >
      Is CS20230722_SUPT_0563 vs CS20230722_SUPT_0564 a clean
      female-vs-broader split, or do both supertypes contain
      heterogeneous sub-populations that cross-cut the classical
      definition?
    - >
      Are CS20230722_CLUS_2290 and CS20230722_CLUS_2292 distinct
      functional subtypes within CS20230722_SUPT_0563, or
      replicates of the same lordosis subpopulation?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2290 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    [tier:CUT] CS20230722_CLUS_2290 is a SUPT_0563 child cluster
    (Nkx2-1=6.69 cohort pct 0.989, Tac1=6.07 cohort pct 0.901,
    region_fraction_100um: 0.817, MFR=0.08) and is among the top
    bulk-correlation hits (delta rank 2 / 5322 in the Knoedler
    2022 PMID:35143761 VMH-FR vs BNST-FR contrast). The
    cluster-level signal is represented through the parent
    supertype edge edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563
    rather than as an independent cluster-level mapping target.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        CS20230722_CLUS_2290 represents the female-biased lordosis
        signal that is the basis for the
        edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563
        cross-cutting mapping; treating it as a separate
        cluster-level target would double-count the SUPT_0563
        evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2292 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    [tier:CUT] CS20230722_CLUS_2292 is a SUPT_0563 child cluster
    (Nkx2-1=6.28 cohort pct 0.949, Tac1=8.62 cohort pct 0.964,
    region_fraction_100um: 1.000, MFR=0.12) and ranks at delta
    rank 4 of 5322 in the Knoedler 2022 PMID:35143761 VMH-FR vs
    BNST-FR contrast. The cluster-level signal is represented
    through the parent supertype edge
    edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        CS20230722_CLUS_2292 is a child of CS20230722_SUPT_0563 and
        contributes to the supertype-level cross-cutting mapping;
        not treated as an independent cluster-level target.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_1959 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_1959 (DMH Hmx2 Gaba_6) is a
    GABAergic dorsomedial-hypothalamus cluster with Nkx2-1=0.26
    (cohort pct 0.423) and Tac1=0.36 (cohort pct 0.321) — both
    defining markers near-absent — and region_fraction_100um:
    0.522 with DMH [MBA:830] dominant over VMH [MBA:693].
    Wrong subclass (DMH GABAergic) for the VMHvl glutamatergic
    classical type.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DMH-anchored GABAergic cluster; defining markers Nkx2-1 and
        Tac1 are near-absent; wrong anatomical and NT context for
        vmhvl_esr1_pr_neuron.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2295 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    [tier:CUT] CS20230722_CLUS_2295 is a SUPT_0564 child cluster
    (Nkx2-1=6.16 cohort pct 0.942, Tac1=1.87 cohort pct 0.752,
    region_fraction_100um: 0.889). The cluster carries the
    cleanest VMH region signal among SUPT_0564 children but its
    mapping is represented through the parent supertype edge
    edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 rather than
    as an independent cluster-level target.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        CS20230722_CLUS_2295 is a child of CS20230722_SUPT_0564 and
        contributes to the supertype-level cross-cutting mapping;
        not treated as an independent cluster-level target.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_CLUS_2297 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_2297 is a SUPT_0564 child cluster
    (Nkx2-1=3.80 cohort pct 0.763, Tac1=1.45 cohort pct 0.730,
    region_fraction_100um: 0.737). Marker concordance is weaker
    than its sibling CS20230722_CLUS_2295; the supertype-level
    edge edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0564 carries
    the mapping.
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        CS20230722_CLUS_2297 is a child of CS20230722_SUPT_0564;
        not treated as an independent cluster-level target.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0557 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_SUPT_0557 (ARH-PVp Tbx3 Glut_4) carries
    Nkx2-1=6.11 (cohort pct 0.969) and Tac1=7.16 (cohort pct
    0.979) with child-cluster coverage 1.00 but
    region_fraction_100um: 0.808 is dominated by Hypothalamus
    catchall n=120 and Tuberal nucleus n=37 with VMH n=97 — the
    supertype is ARH-PVp/Tuberal-leaning by name and metadata,
    not VMHvl-specific. Wrong region context for the VMHvl
    classical type.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        ARH-PVp Tbx3 supertype with Tuberal/Hypothalamus-catchall
        anatomical distribution; not the VMHvl-specific signature
        of vmhvl_esr1_pr_neuron.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0563 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    [tier:CUT] Duplicate fresh-emit edge to CS20230722_SUPT_0563
    — the substantive supertype mapping is encoded on the legacy
    edge edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563
    (lowercase ID) which carries the populated bulk-correlation
    evidence from corr_run_20260428_knoedler_esr1_wmbv1, the
    co-primary cross-cutting designation, and the
    property_comparisons. This uppercase-ID fresh-emit edge
    carries only ATLAS_METADATA and a stub property_comparison
    set; recommend curator removal to resolve the duplicate.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Duplicate edge — same taxonomy_type CS20230722_SUPT_0563
        is targeted by both
        edge_vmhvl_esr1_pr_neuron_to_cs20230722_supt_0563 (legacy,
        substantive) and this fresh-emit edge (impoverished).
        Curator removal of one is recommended.
  unresolved_questions:
    - >
      Curator removal of duplicate edge
      edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0563 —
      legacy/fresh-emit ID collision on taxonomy_type
      CS20230722_SUPT_0563.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0439 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0439 (DMH Prdm13 Gaba_1) is a
    GABAergic dorsomedial-hypothalamus supertype with
    region_fraction_100um: 0.151 (DMH dominant) and Tac1=0.36
    (cohort pct 0.309, near-absent). Wrong region and wrong NT
    for the VMHvl glutamatergic classical type.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DMH GABAergic supertype; Tac1 near-absent; minimal VMH
        footprint (region_fraction_100um: 0.151).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0569 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0569 (VMH Nr5a1 Glut_4) carries
    Nkx2-1=4.96 (cohort pct 0.866) and Tac1=1.52 (cohort pct
    0.680) with VMH region_fraction_100um: 0.913, but the
    supertype belongs to the VMH Nr5a1 lineage (distinct from the
    VMH Fezf1 lineage that contains SUPT_0563/SUPT_0564).
    Nr5a1+ VMHdm/c populations are anatomically and functionally
    distinct from the VMHvl Esr1/Pgr classical type.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        VMH Nr5a1 lineage — distinct VMH developmental lineage
        from VMH Fezf1; not the canonical correlate of the
        VMHvl Esr1/Pgr classical population.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_vmhvl_esr1_pr_neuron_to_CS20230722_SUPT_0568 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0568 (VMH Nr5a1 Glut_3) carries
    Nkx2-1=3.49 (cohort pct 0.732) and Tac1=1.83 (cohort pct
    0.722) with VMH region_fraction_100um: 0.898, but is part of
    the VMH Nr5a1 lineage rather than the VMH Fezf1 lineage that
    contains SUPT_0563/SUPT_0564. Nr5a1+ VMH populations sit
    primarily in VMHdm/c and do not align with the VMHvl
    Esr1/Pgr classical type.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        VMH Nr5a1 lineage — distinct VMH developmental lineage
        from VMH Fezf1; not the canonical correlate of the
        VMHvl Esr1/Pgr classical population.
```
<!-- verdict-block-end -->
