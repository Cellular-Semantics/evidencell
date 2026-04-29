# Ventral premammillary nucleus (PMv) oxytocin receptor neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

**Ventral premammillary nucleus (PMv) oxytocin receptor neuron** is a male-biased
sexually dimorphic population in the ventral premammillary nucleus, defined by
neurochemical criteria (Oxtr, Slc6a3, Adcyap1). The classical node aggregates
three molecularly defined subpopulations of the PMv that may not fully overlap:
PMv-OTR (Oxtr+), PMv-DAT (Slc6a3+, dopaminergic), and PMv-PACAP (Adcyap1+).
No CL term currently maps this population — it is a candidate for new term creation.

| Property | Value | References |
|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | [1], [2] |
| Defining markers | Oxtr (transcript), Slc6a3, Adcyap1 | [1], [2] |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[2] Newmaster et al. 2019 · PMID:32313029 — Neuronal Markers and Molecular Characteristics**

> Sexual dimorphism of OTR expression. OTR is expressed in a sexually dimorphic manner as a part of neural circuit mechanism to generate behavioral differences in males and females 34,35 . Therefore, we compared OTR-Venus expression in male and female mice (N = 5 in male and female brains at different ages) to determine if there were any regions showing strong sexual dimorphism. Across the entire brain region throughout the postnatal development, we found significant sexual dimorphism in two hypothalamic regions (Fig. 7). The ventral premammillary nucleus (PMv) showed significantly higher OTR expression in males compared to females between P14 and P56 (Fig. 7a-d). In contrast, the anteroventral periventricular nucleus (AVPV) near the medial preoptic area showed higher OTR expression in females than males at P56, but not before (Fig. 7e-h). A recent study identified abundant estrogen- dependent OTR-expressing cells in the AVPV, co-expressing estrogen receptor in female mice 36 . This result suggests a potential role of OTR in sexual behavior [36][37][38] .
> — Newmaster et al. 2019, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 201207691_ff444c30 -->

**[1] Hemminger et al. 2024 · PMID:39416191 — Sexually Dimorphic Brain Regions and Structures**

> We identified two adjacent regions within the hypothalamus that exhibited significant sexual dimorphism. Region 1 overlaps with the anterior hypothalamic nucleus (AHN), while Region 2 primarily overlaps with the ventral premammillary nucleus (PMv). Both regions are known to be sexually dimorphic (Vries et al., 2002) , though they have been studied to different extents
> — Hemminger et al. 2024, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 273240437_ed3a4faa -->

**[1] Hemminger et al. 2024 · PMID:39416191 — Sexually Dimorphic Brain Regions and Structures**

> Our findings of specific neuronal subclass differences help further refine the molecular resolution of its dimorphic nature and providing a cellular basis for its role in sex-specific behaviors like aggression and parental care. Region 2, the PMv, is a well- established sexually dimorphic region, with roles in maternal aggression 38 , reproductive control 39 , male social behavior 40 , and intermale aggression 41 . Previous studies identified sexually dimorphic neuron populations within the PMv (e.g., PMv-DAT 42 , PMv- PACAP 43 ), complementing our systematic identification of subclass-level abundance changes.
> — Hemminger et al. 2024, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 273240437_af6642f9 -->

</details>

---

## 4. Mapping candidates

### 4a. Candidate overview

Two mapping edges are recorded for pmv_otr_neuron: a supertype-level edge to SUPT_0607
(the highest-DB-scoring candidate at any rank, expressing all three classical defining
markers) and a child-cluster edge to CLUS_2470 (the PMv-dominant child cluster with
the highest expression of all three markers).

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] | 0607 PMv-TMv Pitx2 Glut_3 | n=192 (PMv) | 🔴 LOW | Oxtr/Slc6a3/Adcyap1 CONSISTENT; sex ratio NOT_ASSESSED | Speculative |
| 2 | 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] | (self) | n=347 (PMv) | 🔴 LOW | Oxtr/Slc6a3/Adcyap1 CONSISTENT; nt_type APPROXIMATE | Speculative |

2 edges total. Relationship type: PARTIAL_OVERLAP (CLUS_2470) and CROSS_CUTTING (SUPT_0607).

### 4b. Property alignment — primary candidate (CLUS_2470)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | MBA:1004 (Ventral premammillary nucleus) | MBA:1004 (PMv) n=347 (dominant location) | MBA:1004 (PMv) n=192 (primary soma — dominant location) | CONSISTENT |
| Oxtr expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=2.0 (DEFINING_SCOPED atlas marker) | precomputed mean_expression=4.45 (vs supertype mean 2.0) | CONSISTENT |
| Slc6a3 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=3.07 (DEFINING atlas marker) | precomputed mean_expression=6.02 (vs supertype mean 3.07) | CONSISTENT |
| Adcyap1 expression | POSITIVE (defining marker) | precomputed mean_expression=4.8 | precomputed mean_expression=8.13 (vs supertype mean 4.8) | CONSISTENT |
| NT type | not specified; DAT+ subpopulation implies dopaminergic co-release | Glutamatergic (PMv-TMv Pitx2 Glut) | not assessed | SUPT: APPROXIMATE |
| Sex ratio | male-biased (PMv OTR expression higher in males, P14–P56) | not available | NOT_ASSESSED — MFR absent from DB for CLUS_2470 | NOT_ASSESSED |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (CLUS_2470 Oxtr/Slc6a3/Adcyap1) | Atlas metadata | SUPPORT | Oxtr=4.45, Slc6a3=6.02, Adcyap1=8.13; PMv n=192; MFR absent | atlas-internal |
| SUPT_0607 atlas metadata (top DB score across all ranks) | Atlas metadata | SUPPORT | DB score=4 (top); Oxtr=2.0, Slc6a3=3.07, Adcyap1=4.8; Tac1=8.95; PMv n=347 | atlas-internal |

*(1 of multiple SUPT_0607 child clusters — CLUS_2470 — concentrates the Oxtr/Slc6a3/Adcyap1 co-expression at PMv (n=192) with all three markers substantially above supertype means; sister supertype SUPT_0605 may capture an additional portion of the OTR+ population. MFR is absent at both supertype level and for CLUS_2470. Best match: CLUS_2470.)*

---

## 5. Candidate paragraphs

## 2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] · 🔴 LOW

### Supporting evidence

- **All three classical defining markers reach CONSISTENT alignment at cluster level.** CLUS_2470 shows substantially higher expression than the supertype mean for all three: Oxtr = 4.45 (vs supertype 2.0), Slc6a3 = 6.02 (vs 3.07), Adcyap1 = 8.13 (vs 4.8). Expression concentrates the marker-expressing PMv cells of SUPT_0607 into this cluster.
- **PMv soma location is the dominant annotation.** MBA:1004 (Ventral premammillary nucleus) is the primary soma for n=192 cells in CLUS_2470 — the largest PMv cluster in SUPT_0607, providing a direct anatomical link to the classical type.
- **Cluster was identified as the best PMv child within the top-DB supertype.** SUPT_0607 received the highest DB score (4) of any candidate at any rank for pmv_otr_neuron [1], [2]; CLUS_2470 is the child cluster within SUPT_0607 that concentrates all three classical marker signals at PMv.

### Marker evidence provenance

- **Oxtr** — at CLUS_2470, Oxtr = 4.45 and is annotated as DEFINING_SCOPED at supertype level (mean = 2.0). Classical evidence is transcript-based ([2] Newmaster 2019, OTR-Venus reporter expression). Atlas precomputed values are transcript-based (10x Chromium). No data-source discrepancy.
- **Slc6a3** — CLUS_2470 Slc6a3 = 6.02 and is a DEFINING atlas marker at supertype level (mean = 3.07). Classical evidence comes from [1] Hemminger 2024, identifying PMv-DAT as a sexually dimorphic PMv subpopulation. Both classical and atlas signals are transcript-based — no data-source discrepancy.
- **Adcyap1** — CLUS_2470 Adcyap1 = 8.13 (vs supertype 4.8). Classical evidence in the facts file lacks a specific PMID citation on the Adcyap1 marker (`refs: []` on the classical node). This is a gap: PMv-PACAP is referenced via [1] Hemminger 2024 in the broader sexually-dimorphic-PMv-subpopulations narrative, but a primary citation establishing Adcyap1 as a defining marker for this classical type is not in the facts. *(note: a targeted cite-traverse for "Adcyap1 PACAP PMv" may resolve this).*

### Concerns

- **Sex bias cannot be confirmed at cluster level.** male_female_ratio is absent from the DB for CLUS_2470 (n=192). Until sex bias is confirmed, confidence is capped at LOW. The absent MFR may reflect a DB ingest gap rather than a genuine absence in the precomputed stats. CLUS_2473 (PMv, n=86) has MFR=2.23 (mild male bias) but very low marker expression — it is a distinct PMv subtype, not a surrogate. *(note: source-side sex bias is well established at population level in [2]; target-side still unresolvable from atlas metadata until MFR is recovered or annotation transfer is run.)*
- **Marker co-expression may conflate three classical subpopulations.** CLUS_2470 co-expresses Oxtr, Slc6a3, and Adcyap1 at levels suggesting it captures the PMv-OTR, PMv-DAT, and PMv-PACAP subpopulations simultaneously. If these are functionally distinct cell types, a single cluster-level edge conflates them. Node splitting (pmv_otr, pmv_dat, pmv_pacap) may be required before a higher-confidence cluster assignment can be made.
- **Annotation transfer not yet performed.** No independent, data-driven cell-level mapping of published PMv scRNA-seq or Oxtr-Cre / Slc6a3-Cre lineage data has been run against WMBv1. This is the most important remaining gap in the evidence base.

### What would upgrade confidence

- **Direct precomputed-HDF5 query** for CLUS_2470 male_female_ratio (proposed in this edge) would distinguish a DB ingest gap from a genuine absence in the precomputed stats and immediately address the primary uncertainty cap on this edge.
- **MapMyCells annotation transfer** of published PMv scRNA-seq or Oxtr-Cre / Slc6a3-Cre lineage data against WMBv1 at cluster resolution; F1 ≥ 0.80 against CLUS_2470 would substantially support upgrading to MODERATE/HIGH confidence and would add `AnnotationTransferEvidence`.
- **Single-cell co-expression analysis within CLUS_2470** to determine whether Oxtr, Slc6a3, and Adcyap1 mark separable subpopulations or co-localise within individual cells. Resolution informs whether pmv_otr_neuron should be split into separate sub-nodes.

---

## 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] · 🔴 LOW

### Supporting evidence

- **Highest DB candidate score across all ranks.** SUPT_0607 received the top DB score (4) of any candidate at any rank for pmv_otr_neuron — the single best supertype hit by atlas-metadata scoring.
- **Direct PMv anatomical match.** MBA:1004 (Ventral premammillary nucleus) is the dominant soma location with n=347 cells in SUPT_0607.
- **All three classical defining markers are present.** Precomputed mean expression: Oxtr = 2.0 (DEFINING_SCOPED atlas marker), Slc6a3 = 3.07 (DEFINING atlas marker), Adcyap1 = 4.8. The supertype simultaneously expresses all three markers corresponding to the potentially distinct PMv subpopulations (PMv-OTR, PMv-DAT, PMv-PACAP).
- **Child cluster CLUS_2470 concentrates the marker-expressing PMv cells.** Within SUPT_0607, CLUS_2470 (n=192 PMv) shows substantially higher Oxtr (4.45), Slc6a3 (6.02), and Adcyap1 (8.13) than the supertype means — see CLUS_2470 edge above.

### Marker evidence provenance

- **Oxtr** — DEFINING_SCOPED at supertype level (mean = 2.0). Classical evidence transcript-based via OTR-Venus reporter [2]. Atlas value transcript-based (10x Chromium). Moderate atlas value at supertype level is expected for a marker concentrated in a child cluster (CLUS_2470 = 4.45).
- **Slc6a3** — DEFINING atlas marker (mean = 3.07). Classical evidence via PMv-DAT subpopulation [1]. Both transcript-based — no data-source discrepancy.
- **Adcyap1** — atlas mean = 4.8. Classical evidence on the node lacks a specific PMID (`refs: []`); PMv-PACAP is referenced in [1] but without a primary citation in the facts. Flag as weak source-side evidence.
- **Tac1 — atlas annotation/literature discrepancy.** Tac1 = 8.95 is the *highest-expressing* DEFINING atlas marker for SUPT_0607 but is absent from the classical pmv_otr_neuron definition. SUPT_0607 may be more accurately characterised as a Tac1+ PMv population with OTR/DAT/PACAP as co-expressed subtype markers. *(note: this suggests the classical definition may underspecify Tac1 — a candidate for a targeted literature search on Tac1 in PMv).*

### Concerns

- **Supertype is glutamatergic, not dopaminergic.** SUPT_0607 carries a Glut_3 (glutamatergic) label (PMv-TMv Pitx2 Glut). The classical node's PMv-DAT subpopulation implies dopaminergic co-release, which is captured only APPROXIMATEly at supertype level. Glutamatergic identity is likely for the OTR+ and PACAP+ populations; dopaminergic co-release is possible for the Slc6a3+ subset. *(adjacent NT phenotype — weak counter-evidence; co-release is biologically plausible).*
- **Cross-cutting marker pattern conflates three classical subpopulations.** SUPT_0607 expresses all three marker signatures (Oxtr, Slc6a3, Adcyap1) simultaneously, indicating the supertype aggregates neurons the classical taxonomy may treat as distinct subtypes (PMv-OTR, PMv-DAT, PMv-PACAP). Sister supertype SUPT_0605 (PMv-TMv Pitx2 Glut_1, DB score = 2) may capture an additional portion of the OTR+ male-biased population.
- **Tac1 as the strongest atlas marker is unaccounted for.** Tac1 = 8.95 (DEFINING) is higher than any of the three classical markers at supertype level, but is not in the classical node definition. This is a marker mismatch flagged for investigation.
- **Sex ratio not available at supertype level.** MFR is computed only at rank 0 (cluster); the male-biased dimorphism — a defining feature of pmv_otr_neuron [2] — cannot be assessed from supertype metadata.
- **Annotation transfer NOT_ASSESSED.**

### What would upgrade confidence

- **Child-cluster expression query for SUPT_0607.** Query Oxtr, Slc6a3, Adcyap1, Tac1 expression in all child clusters of SUPT_0607 to determine whether subpopulations are resolvable at cluster level — partially addressed for CLUS_2470 above.
- **Annotation transfer** (MapMyCells) of published PMv scRNA-seq data against WMBv1; F1 ≥ 0.50 at SUPT_0607 level would upgrade this edge; F1 ≥ 0.80 at CLUS_2470 level would support the cluster-level edge. Expected output: `AnnotationTransferEvidence`.
- **Targeted literature search** for primary citations on Adcyap1 (PMv-PACAP) and Tac1 in PMv to resolve the marker provenance gap.
- **Node split decision.** Decide whether pmv_otr_neuron should be split into pmv_otr, pmv_dat, and pmv_pacap sub-nodes prior to final mapping, given that SUPT_0607 cross-cuts the three subpopulations.

---

## 6. Proposed experiments

### 1. Direct precomputed-HDF5 query for CLUS_2470 male_female_ratio

**What:** Query the precomputed HDF5 stats directly for CLUS_2470 male_female_ratio, bypassing the DB ingest layer.

**Target:** Recover MFR for CLUS_2470 (n=192 cells) and confirm whether sex bias matches the classical male-biased dimorphism.

**Expected output:** Updated property_comparison on the CLUS_2470 edge with sex_ratio alignment resolved (CONSISTENT / DISCORDANT / NOT_ASSESSED if genuinely absent in the source HDF5).

**Resolves:** Open question 1 (the primary cap on confidence for the CLUS_2470 edge). Distinguishes a DB ingest gap from a genuine absence.

### 2. MapMyCells annotation transfer of an external PMv scRNA-seq dataset against WMBv1

**What:** Retrieve a published scRNA-seq dataset enriched for PMv neurons (e.g. Oxtr-Cre, Slc6a3-Cre, or PMv-DAT lineage preparations; sex-stratified hypothalamic atlases). Run MapMyCells against WMBv1 at cluster resolution.

**Target:** F1 ≥ 0.50 at SUPT_0607 level; F1 ≥ 0.80 at CLUS_2470 level for Oxtr+/Slc6a3+/Adcyap1+ cells.

**Expected output:** `AnnotationTransferEvidence` entries on both edges (edge_pmv_otr_neuron_to_cs20230722_supt_0607 and edge_pmv_otr_neuron_to_cs20230722_clus_2470). Atlas: WMBv1. Tool: MapMyCells. Output format: F1 matrix per cluster, fed back as `AnnotationTransferEvidence` YAML.

**Resolves:** Open questions 2 and 3. Addresses the `annotation_transfer_f1` NOT_ASSESSED gap on both edges.

### 3. Single-cell marker co-expression analysis within CLUS_2470

**What:** Within-cluster re-clustering of CLUS_2470 cells, stratified by Oxtr+/Slc6a3+/Adcyap1+ profiles. Determine whether the three markers co-localise within individual cells or mark separable subpopulations.

**Target:** Detection of separable PMv-OTR, PMv-DAT, and PMv-PACAP sub-populations within CLUS_2470, or formal demonstration that they are co-extensive at this resolution.

**Expected output:** Additional `MarkerAnalysisEvidence` records and a node-split decision (pmv_otr / pmv_dat / pmv_pacap as separate classical nodes, or retain as a single aggregated node).

**Resolves:** Open questions 2 and 4 (node splitting decision).

### 4. Targeted literature search for Adcyap1 and Tac1 in PMv

**What:** Cite-traverse for primary citations establishing Adcyap1 as a defining marker for the classical PMv-PACAP population, and for Tac1 expression in PMv.

**Target:** Recover primary PMID(s) supporting Adcyap1 as a PMv-PACAP defining marker; assess whether Tac1 should be added to the classical node definition.

**Expected output:** Additional `LiteratureEvidence` entries; updated classical node definition if Tac1 is supported.

**Resolves:** Adcyap1 marker provenance gap; Tac1 atlas/literature discrepancy (open question 5).

---

## 7. Open questions

1. Why is MFR absent for CLUS_2470 (n=192 cells)? Is this a DB ingest gap or a genuine absence in precomputed stats? *(Appears on the cluster edge.)*
2. Do Oxtr, Slc6a3, and Adcyap1 co-localise within individual CLUS_2470 cells, or do they mark distinct subpopulations within the cluster? *(Appears on the cluster edge.)*
3. Do individual clusters within SUPT_0607 segregate by marker (Oxtr-high, Slc6a3-high, Adcyap1-high), allowing sub-resolution mapping? *(Appears on the supertype edge; partially addressed by CLUS_2470 ATLAS_METADATA evidence.)*
4. Should pmv_otr_neuron be split into separate pmv_otr, pmv_dat, pmv_pacap sub-nodes prior to final mapping? *(Appears on the supertype edge.)*
5. What is the role of Tac1 (mean = 8.95, highest DEFINING atlas marker in SUPT_0607) relative to the classical pmv_otr_neuron definition? Should it be added as a co-expressed marker or treated as a distinguishing feature of a related but distinct supertype? *(Appears on the supertype edge.)*

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_pmv_otr_neuron_to_cs20230722_supt_0607 | ATLAS_METADATA | SUPPORT — DB top score=4; Oxtr=2.0 (DEFINING_SCOPED), Slc6a3=3.07 (DEFINING), Adcyap1=4.8; Tac1=8.95 unexpected; MBA:1004 PMv n=347 |
| edge_pmv_otr_neuron_to_cs20230722_clus_2470 | ATLAS_METADATA | SUPPORT — Oxtr=4.45, Slc6a3=6.02, Adcyap1=8.13 (all above supertype means); MBA:1004 PMv n=192 (largest PMv cluster); MFR absent |

All evidence is atlas-metadata only. No literature, annotation transfer, or direct experimental evidence has been incorporated at this stage.

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hemminger et al. 2024 | [PMID:39416191](https://pubmed.ncbi.nlm.nih.gov/39416191/) | Soma location (PMv); PMv-DAT and PMv-PACAP sexually dimorphic subpopulations |
| [2] | Newmaster et al. 2019 | [PMID:32313029](https://pubmed.ncbi.nlm.nih.gov/32313029/) | Soma location (PMv); Oxtr (OTR) marker; male-biased PMv OTR expression P14–P56 |
