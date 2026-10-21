# Ventral premammillary nucleus (PMv) oxytocin receptor neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The ventral premammillary nucleus (PMv) is a well-established sexually
dimorphic hypothalamic nucleus implicated in maternal aggression,
reproductive control, male social behaviour, and intermale aggression,
and is one of two hypothalamic regions identified by recent spatial
transcriptomic mapping as exhibiting significant male/female cellular
abundance differences [1]. Within the PMv, multiple molecularly defined
neuronal populations have been described, including dopamine-transporter
(Slc6a3) expressing neurons (PMv-DAT), PACAP (Adcyap1) expressing neurons
(PMv-PACAP), and oxytocin receptor (Oxtr) expressing neurons, whose
sexually dimorphic OTR expression was demonstrated by OTR-Venus reporter
mice across postnatal development with significantly higher PMv OTR in
males than in females from P14 to P56 [2]. The classical type addressed
here aggregates these intersecting marker-defined PMv subpopulations
under a single male-biased OTR+ entity; whether the OTR+, DAT+, and
PACAP+ subsets fully overlap inside the PMv is an open biological
question that bears directly on the resolution at which this type can
be mapped onto the WMBv1 taxonomy.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | [1], [2] |
| Defining markers | Oxtr [2]; Slc6a3 [1]; Adcyap1 | [1], [2] |
| Sex bias | Male-biased (males > females) | [2] |
| Definition basis | CLASSICAL_NEUROCHEMICAL | — |
| Notes | Aggregates potentially distinct PMv-OTR, PMv-DAT, PMv-PACAP subpopulations; candidate for new CL term | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (PMv) and sex-biased OTR expression:** OTR-Venus
  reporter immunolabelling across postnatal development, N=5 male and
  female brains per timepoint · [2]
  > Sexual dimorphism of OTR expression. OTR is expressed in a sexually
  > dimorphic manner as a part of neural circuit mechanism to generate
  > behavioral differences in males and females. […] The ventral
  > premammillary nucleus (PMv) showed significantly higher OTR
  > expression in males compared to females between P14 and P56.
  > — Newmaster et al. 2019, Neuronal Markers and Molecular
  > Characteristics · [2] <!-- quote_key: 201207691_ff444c30 -->

- **PMv sexual dimorphism and named subpopulations (PMv-DAT,
  PMv-PACAP):** spatial single-cell mapping across genetic backgrounds,
  prior PMv subpopulation literature · [1]
  > Region 2, the PMv, is a well- established sexually dimorphic region,
  > with roles in maternal aggression 38 , reproductive control 39 , male
  > social behavior 40 , and intermale aggression 41 . Previous studies
  > identified sexually dimorphic neuron populations within the PMv
  > (e.g., PMv-DAT 42 , PMv- PACAP 43 ), complementing our systematic
  > identification of subclass-level abundance changes.
  > — Hemminger et al. 2024, Sexually Dimorphic Brain Regions and
  > Structures · [1] <!-- quote_key: 273240437_af6642f9 -->

- **PMv as a sexually dimorphic region (corroborating):** spatial
  registration to MBA · [1]
  > Region 2 primarily overlaps with the ventral premammillary nucleus
  > (PMv). Both regions are known to be sexually dimorphic (Vries et al.,
  > 2002) , though they have been studied to different extents
  > — Hemminger et al. 2024, Sexually Dimorphic Brain Regions and
  > Structures · [1] <!-- quote_key: 273240437_ed3a4faa -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new
CL term. The classical definition spans multiple intersecting
marker-defined PMv subpopulations (Oxtr+, Slc6a3+/DAT+, Adcyap1+/PACAP+)
that do not yet have dedicated CL representatives.

---

## Results

Soma-location concordance with the queried PMv (MBA:1004) and atlas-side
co-expression of all three classical defining markers identify the PMv
hypothalamic glutamatergic supertype 0607 PMv-TMv Pitx2 Glut_3
[CS20230722_SUPT_0607] as the supertype-level match (see candidate
audit table and property comparison tables below), with its child
cluster 2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] as the
cluster-level lead (the largest PMv-resident child of the supertype,
concentrating Oxtr, Slc6a3, and Adcyap1 expression). The supertype
co-expresses all three classical markers simultaneously, indicating
that this WMBv1 type aggregates neurons the classical taxonomy treats
as potentially distinct PMv-OTR / PMv-DAT / PMv-PACAP subpopulations;
the supertype-level mapping is therefore committed as a broader,
many-to-one relationship while the cluster-level call is held at low
confidence pending male-bias and finer subpopulation confirmation.

### 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] · 🟡 MODERATE

**Property comparison (supertype).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | PMv 473/1165 cells at 100µm (region_fraction_100um=0.865; strict=0.634) | PMv 255/451 cells (region_fraction_100um=0.898; strict=0.676) at CLUS_2470 | CONSISTENT |
| NT type | not asserted on classical | not asserted at supertype | Glut at CLUS_2470 | NOT_ASSESSED (classical side) |
| Oxtr expression | Defining marker | mean=2.0 (DEFINING_SCOPED on atlas) | mean=4.45 at CLUS_2470 | CONSISTENT (both sides positive) |
| Slc6a3 expression | Defining marker | mean=3.07 (DEFINING on atlas) | mean=6.02 at CLUS_2470 | CONSISTENT |
| Adcyap1 expression | Defining marker | mean=4.8 | mean=8.13 at CLUS_2470 | CONSISTENT |
| Sex ratio | Male-biased | not available at supertype | not available — MFR absent from DB for CLUS_2470 | NOT_ASSESSED |

*(All five named PMv-resident child clusters of SUPT_0607 carry PMv as
the dominant or co-dominant soma location; CLUS_2470 leads on every
defining marker simultaneously. Within the supertype, the OTR / DAT /
PACAP marker signatures co-occur rather than segregate across children,
indicating supertype-level aggregation of the three classical
subpopulations. Best child: CLUS_2470.)*

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + region painting | Atlas metadata | SUPPORT | PMv region_fraction_100um=0.865; Oxtr=2.0, Slc6a3=3.07, Adcyap1=4.8 co-expressed | atlas-internal |

**Supporting evidence.**

- The PMv-TMv Pitx2 Glut_3 supertype is the highest-scoring candidate
  at any rank for this classical type. Of its 1165 cells, 473 (proximity
  count at 100µm) sit in PMv; the dominant atlas anatomical labels are
  Hypothalamus (count=546), Ventral premammillary nucleus
  [MBA:1004] (count=473), and Dorsomedial nucleus of the hypothalamus
  [MBA:830] (count=206), giving region_fraction_100um=0.865 (strict
  region_fraction=0.634).
- All three classical defining markers are detected at the supertype
  level (Oxtr=2.0, tagged DEFINING_SCOPED on the atlas annotation;
  Slc6a3=3.07, tagged DEFINING; Adcyap1=4.8).

**Marker evidence provenance.**

- **Oxtr:** classical-side evidence is OTR-Venus reporter
  immunolabelling across postnatal development in PMv [2] — a
  protein-level readout tied to a defined hypothalamic region, with
  explicit demonstration of male-biased PMv expression. Atlas-side
  Oxtr=2.0 is consistent with detectable expression but is tagged
  DEFINING_SCOPED, meaning it discriminates within the relevant atlas
  subclass rather than across the full taxonomy; the alignment is
  therefore supportive at the supertype level but not a strong
  cluster-level discriminator on its own.
- **Slc6a3:** referenced through prior PMv-DAT subpopulation literature
  [1] (which cites Slc6a3 as the PMv-DAT marker without re-deriving it
  in the cited study). Atlas-side Slc6a3=3.07 is tagged DEFINING for
  this supertype, providing transcript-level corroboration that the
  classical PMv-DAT signature is part of this WMBv1 type.
- **Adcyap1:** carries no primary citation on the classical node (the
  PMv-PACAP subpopulation is named in [1] only as a previously
  identified subpopulation, without an original-study citation
  available in the gathered corpus). Atlas-side Adcyap1=4.8 is the
  highest mean among the three defining markers but cannot currently
  be anchored to a primary study from the gathered references — a
  targeted literature search for PMv PACAP / Adcyap1 primary
  characterisation would close the provenance gap.
- **Unexpected high-expressing marker (Tac1):** Tac1 is tagged DEFINING
  on the atlas for this supertype with mean=8.95 — substantially higher
  than any of the three classical defining markers — and is absent from
  the classical pmv_otr_neuron definition. This is informational rather
  than disqualifying; it suggests the supertype may be more accurately
  characterised at the atlas level as a Tac1+ PMv glutamatergic
  population with OTR / DAT / PACAP signatures as co-expressed
  subtype-level features, and is recorded as a curator-facing follow-up
  caveat (see Discussion).

**Concerns.**

- **Cross-cutting marker aggregation.** SUPT_0607 simultaneously
  expresses Oxtr, Slc6a3, and Adcyap1, the three markers that the
  classical definition treats as potentially labelling distinct PMv
  subpopulations. If the OTR+, DAT+, and PACAP+ subsets are functionally
  separable populations, the supertype-level mapping inherently
  aggregates them; finer (cluster-level or sub-cluster) resolution is
  required to test whether they segregate. This is the basis for the
  many-to-one (broader) supertype call rather than an exact match.
- **Sister supertype 0605 PMv-TMv Pitx2 Glut_1 [CS20230722_SUPT_0605]**
  also resides predominantly in PMv (region_fraction_100um=0.631;
  strict=0.307) but did not surface co-expression of all three classical
  markers in the gathered facts. It may capture an additional portion
  of the OTR+ male-biased population not absorbed by SUPT_0607; it
  appears in the candidate audit table as a lower-ranked PMv-resident
  glutamatergic supertype.
- **Tac1 atlas DEFINING marker not in classical definition** — see
  marker provenance above.

**What would upgrade confidence.**

- Annotation transfer of published PMv transcriptomic datasets
  (e.g. Oxtr-targeted, DAT-Cre, or PACAP-Cre lineage RNA profiling)
  against WMBv1, with F1 ≥ 0.7 to SUPT_0607 at supertype level, would
  add an AnnotationTransferEvidence anchor for the classical → atlas
  relationship.
- Curator decision on whether to split `pmv_otr_neuron` into separate
  `pmv_otr`, `pmv_dat`, and `pmv_pacap` sub-nodes would clarify whether
  the natural mapping resolution is one supertype to one classical type
  (current) or three classical types to one supertype (cross-cutting).

### 2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] · 🔴 LOW

**Property comparison (cluster, child of SUPT_0607).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | PMv region_fraction_100um=0.865 at SUPT_0607 | PMv 255/451 cells (region_fraction_100um=0.898; strict=0.676) at CLUS_2470 | CONSISTENT |
| NT type | not asserted on classical | not asserted at SUPT_0607 | Glut at CLUS_2470 | NOT_ASSESSED (classical side) |
| Oxtr expression | Defining marker | mean=2.0 at SUPT_0607 | mean=4.45 at CLUS_2470 | CONSISTENT |
| Slc6a3 expression | Defining marker | mean=3.07 at SUPT_0607 | mean=6.02 at CLUS_2470 | CONSISTENT |
| Adcyap1 expression | Defining marker | mean=4.8 at SUPT_0607 | mean=8.13 at CLUS_2470 | CONSISTENT |
| Sex ratio | Male-biased | not available | MFR absent from precomputed-stats DB for CLUS_2470 | NOT_ASSESSED |

*(CLUS_2470 is the PMv-leading child of SUPT_0607: of the supertype's
children, it has the largest count of PMv-resident cells (n=192 at
strict region match within the precomputed location data) and the
highest mean expression of all three classical defining markers.)*

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + region painting | Atlas metadata | SUPPORT | Oxtr=4.45, Slc6a3=6.02, Adcyap1=8.13; PMv region_fraction_100um=0.898 | atlas-internal |

**Supporting evidence.**

- CLUS_2470 carries the highest expression of all three classical
  defining markers among the children of SUPT_0607: Oxtr=4.45,
  Slc6a3=6.02, Adcyap1=8.13 — each substantially above the supertype
  means. The cluster concentrates the marker-expressing PMv cells
  inside its parent supertype.
- The cluster's soma location is dominantly PMv: of its 451 cells, 255
  fall within the 100µm proximity of PMv (region_fraction_100um=0.898;
  strict region_fraction=0.676), with the next-largest atlas labels
  being the umbrella Hypothalamus [MBA:1097] and Dorsomedial nucleus of
  the hypothalamus [MBA:830] — adjacent to PMv and consistent with
  registration-boundary scatter rather than off-target placement.
- NT type at this cluster is Glut, consistent with the glutamatergic
  identity expected of PMv-DAT / PMv-PACAP / PMv-OTR neurons described
  in the cited literature [1], though the classical node does not
  itself assert an NT type.

**Concerns.**

- **Male-bias (MFR) not retrievable for CLUS_2470.** The classical
  definition is explicitly male-biased ([2]), and the survey cohort
  filter that surfaced this candidate was `sex_bias=male`. However,
  the male/female ratio is currently absent from the precomputed-stats
  DB for CLUS_2470. Confidence at cluster level is capped at LOW until
  the male bias is confirmed. The absence may reflect a DB ingest gap
  rather than genuine absence in the underlying precomputed stats —
  a direct query of the precomputed HDF5 is the recommended check.
- **Single-cluster aggregation of three potentially distinct
  subpopulations.** CLUS_2470 co-expresses all three classical defining
  markers at high levels. If PMv-OTR, PMv-DAT, and PMv-PACAP are
  functionally distinct cell types within PMv, a single cluster-level
  edge conflates them. Resolution at sub-cluster level (single-cell
  inspection within the cluster) would test whether the three marker
  signatures co-localise per cell or label distinct populations within
  CLUS_2470. This is also the basis for keeping the relationship
  cluster-level call non-exact (close, not exact).
- **Sister cluster CLUS_2471 in the same supertype** also sits in PMv
  but with lower proximity (region_fraction_100um=0.676;
  strict=0.341) and weaker marker co-expression in the gathered
  facts — it may capture additional PMv-resident OTR+ cells not in
  CLUS_2470, contributing to the supertype-level aggregation story.

**What would upgrade confidence.**

- Direct query of the precomputed HDF5 for CLUS_2470 male/female ratio
  to confirm whether the male bias documented at PMv tissue level [2]
  is reflected at this cluster. Confirmed male bias would lift cluster
  confidence to MODERATE.
- Within-cluster single-cell inspection (or cluster-resolved gene
  co-expression analysis) for Oxtr, Slc6a3, and Adcyap1 to determine
  whether the three classical subpopulations co-occur in individual
  cells or segregate within CLUS_2470.
- Cluster annotation transfer of published PMv lineage transcriptomic
  data (Oxtr-Cre, Slc6a3-Cre, or Adcyap1-Cre profiled cells) against
  WMBv1, with F1 ≥ 0.7 to CLUS_2470 at cluster level, would add a
  direct experimental anchor.

---

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] | — | 1165 | 🟡 MODERATE | PMv region_fraction_100um=0.865; all 3 markers co-expressed | Primary (supertype) |
| 2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] | 0607 PMv-TMv Pitx2 Glut_3 | 451 | 🔴 LOW | Highest Oxtr/Slc6a3/Adcyap1 child; PMv region_fraction_100um=0.898; MFR missing | Secondary (best child of primary supertype) |
| 2471 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2471] | 0607 PMv-TMv Pitx2 Glut_3 | 274 | ⚪ UNCERTAIN | PMv region_fraction_100um=0.676; sibling of CLUS_2470 | Eliminated (weaker PMv proximity and marker support than sister CLUS_2470) |
| 2314 VMH Nr5a1 Glut_4 [CS20230722_CLUS_2314] | 0569 VMH Nr5a1 Glut_4 | 231 | 🔴 LOW | region_fraction_100um=0.018; dominant in VMH not PMv | Eliminated (wrong region — VMH, not PMv) |
| 2575 MM Foxb1 Glut_2 [CS20230722_CLUS_2575] | 0631 MM Foxb1 Glut_2 | 487 | 🔴 LOW | region_fraction_100um=0.029; dominant in medial mammillary | Eliminated (wrong region — medial mammillary) |
| 2395 PH-ant-LHA Otp Bsx Glut_2 [CS20230722_CLUS_2395] | 0592 PH-ant-LHA Otp Bsx Glut_2 | 105 | ⚪ UNCERTAIN | PMv region_fraction_100um=0.596 but no marker support gathered | Eliminated (lower PMv proximity than primary supertype's children; no marker confirmation) |
| 0605 PMv-TMv Pitx2 Glut_1 [CS20230722_SUPT_0605] | — | 1202 | ⚪ UNCERTAIN | PMv region_fraction_100um=0.631; sister of primary supertype | Eliminated (no atlas marker support gathered; may carry residual OTR+ population — see Discussion) |
| 0557 ARH-PVp Tbx3 Glut_4 [CS20230722_SUPT_0557] | — | 246 | 🔴 LOW | region_fraction_100um=0.067; dominant in VMH | Eliminated (wrong region) |
| 0429 TMv-PMv Tbx3 Hist-Gaba_1 [CS20230722_SUPT_0429] | — | 534 | ⚪ UNCERTAIN | region_fraction_100um=0.247; histaminergic GABA | Eliminated (boundary PMv overlap; histaminergic GABA identity, not glutamatergic) |
| 0430 TMv-PMv Tbx3 Hist-Gaba_2 [CS20230722_SUPT_0430] | — | 321 | ⚪ UNCERTAIN | region_fraction_100um=0.157; histaminergic GABA | Eliminated (boundary PMv overlap; histaminergic GABA identity) |

A fresh-emit duplicate edge targets each of SUPT_0607 and CLUS_2470 with
only `discovery_score` and stub property comparisons (no curator-
authored caveats). The substantive structured evidence lives on the
legacy edges narrated above; the fresh-emit duplicates are recorded
for curator removal — see Discussion open questions.

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node `pmv_otr_neuron`
(definition basis: CLASSICAL_NEUROCHEMICAL) is defined by Oxtr [2],
Slc6a3 [1], and Adcyap1 expression, with soma in the Ventral
premammillary nucleus [MBA:1004] [1, 2] and a male-biased sex ratio
documented at the level of OTR+ PMv tissue by OTR-Venus reporter
immunolabelling [2]. The node carries an explicit curator note that
the three marker-defined subpopulations (PMv-OTR, PMv-DAT, PMv-PACAP)
may not fully overlap and could be split into separate sub-nodes
before final mapping. No CL term is currently assigned.

**Atlas mapping query.** Candidate atlas clusters were retrieved from
the WMBv1 taxonomy (CS20230722) at ranks 0 (cluster) and 1 (supertype)
using metadata-based scoring (region match against MBA:1004, NT type,
defining markers Oxtr / Slc6a3 / Adcyap1, sex bias filter for
`male`). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type
was compared to the corresponding atlas-side value via the
`property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side
numerical values came from precomputed expression on the cluster
and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology
CURIEs, and verbatim literature quotes in this report are validated
against the evidencell knowledge base at write time. Authored-prose
evidence narratives are validated against their source
`evidence_items[*].explanation` fields. The pre-write hook rejects
any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:14:10+00:00 from
[kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_pmv_otr_neuron_to_cs20230722_supt_0607 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_pmv_otr_neuron_to_cs20230722_clus_2470 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_CLUS_2471 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_CLUS_2470 (fresh-emit duplicate) | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_CLUS_2314 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_CLUS_2575 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_CLUS_2395 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_SUPT_0607 (fresh-emit duplicate) | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_SUPT_0605 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_SUPT_0557 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_SUPT_0429 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_pmv_otr_neuron_to_CS20230722_SUPT_0430 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Ventral premammillary nucleus (PMv) oxytocin
receptor neuron → 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] at
MODERATE confidence, with the supertype's PMv-resident child cluster
2470 PMv-TMv Pitx2 Glut_3 [CS20230722_CLUS_2470] held at LOW confidence
as the best cluster-level resolution available. Key support: atlas
precomputed expression of all three classical defining markers (Oxtr,
Slc6a3, Adcyap1) on a PMv-dominant glutamatergic supertype, with PMv
soma proximity at region_fraction_100um=0.865 at supertype level and
0.898 at the cluster. Key caveats: the supertype aggregates the three
marker-defined PMv subpopulations the classical definition treats as
potentially distinct (cross-cutting many-to-one); and male-bias at the
cluster level remains unconfirmed (MFR missing from the precomputed-
stats DB for CLUS_2470).

No Cell Ontology term currently covers this classical type. The
intersecting marker-defined PMv subpopulations described in the
literature (PMv-OTR, PMv-DAT, PMv-PACAP) do not yet have CL
representatives, and the type is flagged as a candidate for a new CL
term — the natural prerequisite is the curator decision (see open
questions) on whether the three subpopulations are one type or three.

### Proposed experiments and follow-ups

**Within-cluster marker co-expression resolution.**
- **What:** Single-cell inspection of Oxtr, Slc6a3, and Adcyap1
  co-expression within CLUS_2470 (and to a lesser extent CLUS_2471) to
  determine whether the three classical subpopulations co-localise per
  cell or segregate into separable subclusters.
- **Target:** Identify whether ≥ 90% of marker-positive cells co-express
  all three markers (one population) or whether the markers label
  largely non-overlapping cells (three populations within one cluster).
- **Expected output:** MarkerAnalysisEvidence on the cluster edge; if
  separation is found, basis for splitting `pmv_otr_neuron` into
  `pmv_otr`, `pmv_dat`, `pmv_pacap` sub-nodes.
- **Resolves:** open questions 1, 3.

**Cluster annotation transfer from PMv lineage datasets.**
- **What:** Cluster-level annotation transfer of published PMv
  transcriptomic data targeting PMv-OTR (via Oxtr-Cre or
  OTR-reporter-sorted cells), PMv-DAT (Slc6a3-Cre), or PMv-PACAP
  (Adcyap1-Cre) against WMBv1.
- **Target:** F1 ≥ 0.7 to SUPT_0607 at supertype level; F1 ≥ 0.6 to
  CLUS_2470 at cluster level.
- **Expected output:** AnnotationTransferEvidence on the supertype and
  cluster edges; direct experimental anchor for the classical → atlas
  identity at both resolutions.
- **Resolves:** open questions 1, 2, 4.

**Direct precomputed-stats query for cluster-level male/female ratio.**
- **What:** Direct HDF5 query of CLUS_2470 male/female cell counts to
  confirm whether the male bias documented for PMv OTR+ tissue [2] is
  reflected at this cluster, and whether the DB-level MFR absence is
  a genuine signal or an ingest gap.
- **Target:** Recover MFR; confirm male predominance consistent with
  [2] (males > females from P14–P56).
- **Expected output:** Sex-ratio property comparison populated; if
  confirmed, lifts cluster confidence to MODERATE.
- **Resolves:** open question 4.

**Curator decision on splitting `pmv_otr_neuron`.**
- **What:** Curator review of whether the classical node should be
  split into separate `pmv_otr`, `pmv_dat`, and `pmv_pacap` sub-nodes
  prior to committing a final mapping.
- **Expected output:** Either (a) confirmation that the aggregated type
  is the correct unit and the supertype-level broader call is the
  natural resolution, or (b) three classical nodes mapping into the
  same supertype as a cross-cutting many-to-one.
- **Resolves:** open questions 1, 3.

### Open questions

1. Do the PMv-OTR, PMv-DAT, and PMv-PACAP marker signatures co-localise
   in individual cells within CLUS_2470, or do they label distinct
   subpopulations within the cluster?
2. Do individual child clusters within SUPT_0607 segregate by marker
   (Oxtr-high, Slc6a3-high, Adcyap1-high), allowing higher-resolution
   sub-supertype mapping?
3. Should `pmv_otr_neuron` be split into separate `pmv_otr`, `pmv_dat`,
   and `pmv_pacap` sub-nodes prior to final mapping?
4. Why is MFR (male/female ratio) absent in the precomputed-stats DB
   for CLUS_2470 (n=192 PMv cells)? Is this a DB ingest gap or a
   genuine absence in the precomputed stats?
5. Does sister supertype 0605 PMv-TMv Pitx2 Glut_1 [CS20230722_SUPT_0605]
   capture an additional portion of the OTR+ male-biased PMv population
   not absorbed by SUPT_0607?
6. Is the atlas DEFINING marker Tac1 (mean=8.95 on SUPT_0607) a
   feature that should be added to the classical definition, or is it
   a co-expressed but classically irrelevant marker?
7. Curator removal of duplicate fresh-emit edges
   `edge_pmv_otr_neuron_to_CS20230722_SUPT_0607` and
   `edge_pmv_otr_neuron_to_CS20230722_CLUS_2470` — legacy/fresh-emit
   ID collisions on the same `taxonomy_type` accessions; the legacy
   edges carry the substantive evidence and should be retained.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hemminger et al. 2024. Spatial Single-Cell Mapping of Transcriptional Differences Across Genetic Backgrounds in Mouse Brains. | [39416191](https://pubmed.ncbi.nlm.nih.gov/39416191) | PMv soma location; PMv-DAT and PMv-PACAP subpopulation naming |
| [2] | Newmaster et al. 2019. (PMID 32313029) | [32313029](https://pubmed.ncbi.nlm.nih.gov/32313029) | OTR-Venus reporter demonstration of male-biased PMv OTR expression P14–P56; Oxtr marker; PMv soma location |

---

## Verdict blocks

<!-- verdict-block-start: edge_pmv_otr_neuron_to_cs20230722_supt_0607 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.62
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] PMv-resident glutamatergic supertype 0607
    PMv-TMv Pitx2 Glut_3 (region_fraction_100um=0.865; strict=0.634)
    co-expresses all three classical defining markers (Oxtr=2.0,
    Slc6a3=3.07, Adcyap1=4.8) and is the highest-scoring candidate
    at any rank; the broader 1:n call reflects supertype aggregation
    of the three classical PMv-OTR / PMv-DAT / PMv-PACAP subpopulations
    rather than a clean 1:1.
  reconciliation_note: >
    Supertype-level call (CS20230722_SUPT_0607) paired with cluster-level
    secondary CS20230722_CLUS_2470 (LOW); the supertype absorbs marker
    signatures that the classical definition treats as potentially
    distinct subpopulations, so the natural resolution is broader at
    supertype level and uncertain at cluster level pending male-bias
    and within-cluster co-expression resolution.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Cross-cutting marker aggregation — SUPT_0607 simultaneously
        expresses Oxtr, Slc6a3, and Adcyap1, the three markers the
        classical definition treats as potentially labelling distinct
        PMv subpopulations (PMv-OTR, PMv-DAT, PMv-PACAP); the
        supertype-level mapping inherently aggregates them and a
        sub-supertype split may be required if curator decides the
        subpopulations are functionally distinct.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Tac1 is tagged DEFINING on the atlas for this supertype with
        mean=8.95 — substantially higher than any of the three
        classical defining markers — and is absent from the classical
        pmv_otr_neuron definition; the supertype may be more
        accurately characterised at the atlas level as a Tac1+ PMv
        glutamatergic population with OTR / DAT / PACAP signatures
        as co-expressed subtype-level features.
    - caveat_type: OTHER
      description: >
        Sister supertype 0605 PMv-TMv Pitx2 Glut_1 also resides
        predominantly in PMv (region_fraction_100um=0.631; strict=0.307)
        and may capture an additional portion of the OTR+ male-biased
        population not absorbed by SUPT_0607.
  proposed_experiments:
    - >
      Cluster annotation transfer of published PMv lineage
      transcriptomic data (Oxtr-Cre, Slc6a3-Cre, or Adcyap1-Cre
      profiled cells) against WMBv1, with F1 >= 0.7 to SUPT_0607
      at supertype level, to provide an AnnotationTransferEvidence
      anchor for the classical-to-atlas relationship.
    - >
      Query Oxtr, Slc6a3, Adcyap1, and Tac1 expression across the
      child clusters of SUPT_0607 to test whether the three classical
      marker signatures segregate at cluster level (suggesting
      sub-supertype splitting) or co-occur across children (supporting
      the aggregated broader call).
    - >
      Curator decision on whether to split pmv_otr_neuron into
      separate pmv_otr, pmv_dat, and pmv_pacap sub-nodes, which would
      reframe this edge as a cross-cutting many-to-one mapping into
      SUPT_0607 rather than a single broader 1:n mapping.
  unresolved_questions:
    - >
      Do individual child clusters within SUPT_0607 segregate by
      marker (Oxtr-high, Slc6a3-high, Adcyap1-high), allowing
      sub-supertype resolution mapping?
    - >
      Should pmv_otr_neuron be split into separate pmv_otr, pmv_dat,
      pmv_pacap sub-nodes prior to final mapping?
    - >
      Is the atlas DEFINING marker Tac1 (mean=8.95 on SUPT_0607) a
      feature that should be added to the classical definition, or a
      co-expressed but classically irrelevant marker?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_cs20230722_clus_2470 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.38
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CLUS_2470 is the PMv-leading child of SUPT_0607
    (region_fraction_100um=0.898; strict=0.676; 255/451 cells in PMv)
    and concentrates the supertype's classical-marker expression
    (Oxtr=4.45, Slc6a3=6.02, Adcyap1=8.13); confidence held at LOW
    pending male-bias confirmation (MFR missing from precomputed-stats
    DB) and within-cluster co-expression resolution of the three
    putative subpopulations.
  reconciliation_note: >
    Cluster-level secondary to the supertype primary
    (CS20230722_SUPT_0607, MODERATE broadMatch); the cluster call
    is non-exact (close, not exact) because the cluster appears to
    aggregate the three classical marker-defined subpopulations into
    a single transcriptomic unit.
  caveats:
    - caveat_type: OTHER
      description: >
        Male-bias (MFR) not retrievable for CLUS_2470 — the classical
        definition is explicitly male-biased ([2]) but the male/female
        ratio is currently absent from the precomputed-stats DB for
        this cluster; absence may reflect a DB ingest gap rather than
        a genuine signal, and confidence is capped at LOW until the
        male bias is confirmed.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Single-cluster aggregation of three potentially distinct
        subpopulations — CLUS_2470 co-expresses Oxtr, Slc6a3, and
        Adcyap1 at high levels, and if PMv-OTR, PMv-DAT, and PMv-PACAP
        are functionally distinct cell types within PMv, a single
        cluster-level edge conflates them; resolution at sub-cluster
        level would test whether the three marker signatures
        co-localise per cell or label distinct populations within
        the cluster.
    - caveat_type: OTHER
      description: >
        Sister cluster CLUS_2471 in the same supertype also sits in
        PMv but with lower proximity (region_fraction_100um=0.676;
        strict=0.341) and weaker marker co-expression in the gathered
        facts — it may capture additional PMv-resident OTR+ cells not
        in CLUS_2470, contributing to the supertype-level aggregation.
  proposed_experiments:
    - >
      Direct query of the precomputed HDF5 for CLUS_2470 male/female
      ratio to confirm whether the male bias documented for PMv OTR+
      tissue [2] is reflected at this cluster, and whether the
      DB-level MFR absence is a genuine signal or an ingest gap;
      confirmed male predominance would lift cluster confidence to
      MODERATE.
    - >
      Within-cluster single-cell inspection (or cluster-resolved gene
      co-expression analysis) for Oxtr, Slc6a3, and Adcyap1 to
      determine whether the three classical subpopulations co-occur
      in individual cells or segregate within CLUS_2470.
    - >
      Cluster annotation transfer of published PMv lineage
      transcriptomic data (Oxtr-Cre, Slc6a3-Cre, or Adcyap1-Cre
      profiled cells) against WMBv1, with F1 >= 0.6 to CLUS_2470
      at cluster level, to add a direct experimental anchor.
  unresolved_questions:
    - >
      Do Oxtr, Slc6a3, and Adcyap1 co-localise within individual
      CLUS_2470 cells, or do they mark distinct subpopulations within
      the cluster?
    - >
      Why is MFR absent for CLUS_2470 (n=192 PMv cells)? DB ingest
      gap or genuine absence in precomputed stats?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_CLUS_2471 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.22
  rationale: >
    [tier:CUT] Sibling cluster of CLUS_2470 in SUPT_0607 with lower
    PMv proximity (region_fraction_100um=0.676; strict=0.341) and
    weaker marker support than its sister; eliminated in favour of
    CLUS_2470 as the best PMv-resident child.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_CLUS_2314 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Wrong region — CS20230722_CLUS_2314 is a VMH Nr5a1
    glutamatergic cluster dominant in the ventromedial hypothalamic
    nucleus (region_fraction_100um=0.018 against PMv), not PMv.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_CLUS_2575 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Wrong region — CS20230722_CLUS_2575 is a medial
    mammillary Foxb1 glutamatergic cluster (region_fraction_100um=0.029
    against PMv), not PMv.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_CLUS_2395 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.18
  rationale: >
    [tier:CUT] PH-ant-LHA Otp Bsx glutamatergic cluster with moderate
    PMv proximity (region_fraction_100um=0.596) but no atlas-side
    confirmation of the classical defining markers; weaker than the
    PMv-TMv Pitx2 Glut_3 lineage and eliminated.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_SUPT_0607 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Fresh-emit duplicate of the legacy supertype edge
    edge_pmv_otr_neuron_to_cs20230722_supt_0607, carrying only
    discovery_score and stub property comparisons; the substantive
    evidence lives on the legacy edge and this duplicate is recorded
    for curator removal.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_SUPT_0605 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Sister supertype to SUPT_0607 with PMv residency
    (region_fraction_100um=0.631; strict=0.307) but no atlas-side
    confirmation of the classical defining markers in the gathered
    facts; flagged as a possible carrier of additional OTR+ population
    but eliminated at this round pending direct marker evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_SUPT_0557 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Wrong region — ARH-PVp Tbx3 glutamatergic supertype
    dominant in VMH (region_fraction_100um=0.067 against PMv), not PMv.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_SUPT_0429 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.12
  rationale: >
    [tier:CUT] TMv-PMv histaminergic GABAergic supertype with boundary
    PMv overlap (region_fraction_100um=0.247) and a histaminergic
    GABA identity inconsistent with the glutamatergic PMv-OTR / DAT /
    PACAP populations described in the literature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_SUPT_0430 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.12
  rationale: >
    [tier:CUT] TMv-PMv histaminergic GABAergic supertype with boundary
    PMv overlap (region_fraction_100um=0.157) and a histaminergic
    GABA identity inconsistent with the glutamatergic PMv-OTR / DAT /
    PACAP populations described in the literature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_pmv_otr_neuron_to_CS20230722_CLUS_2470 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Fresh-emit duplicate of the legacy cluster edge
    edge_pmv_otr_neuron_to_cs20230722_clus_2470, carrying only
    discovery_score and stub property comparisons; the substantive
    evidence lives on the legacy edge and this duplicate is recorded
    for curator removal.
```
<!-- verdict-block-end -->
