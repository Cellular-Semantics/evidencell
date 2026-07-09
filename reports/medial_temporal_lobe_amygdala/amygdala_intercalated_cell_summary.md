# Amygdala intercalated cell — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/medial_temporal_lobe_amygdala/amygdala_intercalated_cell.yaml`*

---

## Introduction

The intercalated cells of the amygdala (ITCs, or intercalated cell masses / IA) are
small clusters of densely packed GABAergic neurons wedged between the basolateral and
centromedial amygdala, where they act as inhibitory gates on information flow through the
amygdaloid circuit. They are among the amygdaloid populations that sit outside the
canonical basolateral / cortical-like / centromedial grouping, and they are defined
molecularly by the transcription factor Foxp2 together with dopamine-receptor and
opioid-receptor signalling genes.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | intercalated amygdaloid nuclei [UBERON:0002884] | [1], [2], [3] |
| NT type | GABAergic | [3], [4] |
| Markers | Foxp2, Drd1, Oprm1 | Foxp2 [5], [6]; Drd1 [6]; Oprm1 [5] |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / identity:** review + primary anatomy · human and rodent amygdala · [3]
  > . In addition to the four groups, a few nuclei of the amygdala remain unclassified, among them the intercalated cell masses which are small clusters of densely packed GABAergic neurons (Palomares-Castillo et al., 2012).
  > — Veinante et al. 2013, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 15449738_a21bd562 -->

- **NT type (GABAergic):** anatomical / neurochemical · rat · [4]
  > In some regions, such as the intercalated nuclei, virtually all of the resident neurons appeared to be GABAergic
  > — Pitkānen & Amaral 1994, abstract · [4] <!-- quote_key: 14068807_9efc175b -->

- **Foxp2 (defining marker):** single-cell transcriptomics · mouse · [5]
  > We identified distinct subtypes of FOXP2+ interneurons in the intercalated cell masses and protein-kinase C-δ interneurons in the central nucleus. We also establish that glutamatergic, pyramidal-like neurons are transcriptionally specialized within the basal, lateral, or accessory basal nuclei
  > — Totty et al. 2024, Medial, cortical/superficial, and intercalated cell populations · [5] <!-- quote_key: 273531817_88e4457f -->

- **Drd1 / Tshz1 (marker, subtype axis):** cross-species single-cell transcriptomics · mammalian · [6]
  > the IA subnuclei were highly conserved, and all mammals in our datasets contained two types of TSHZ1+ neurons, i.e., DRD1+ and DRD1−.
  > — Yu et al. 2023, Results · [6] <!-- quote_key: 256832817_4f39c6f9 -->

</details>

Cell Ontology mapping: No Cell Ontology term currently covers this type — candidate for a
new CL term.

---

## Results

Annotation transfer from four Foxp2+ intercalated molecular subtypes (Hochgerner 2023
amygdala single-cell data, mapped with MapMyCells) resolves the classical intercalated
cell onto the 0288 STR-PAL Chst9 Gaba_4 supertype [CS20230722_SUPT_0288] and its dominant
child 1011 STR-PAL Chst9 Gaba_4 [CS20230722_CLUS_1011], with a second subtype landing on
1015 STR-PAL Chst9 Gaba_5 [CS20230722_CLUS_1015] (see figure and property comparison
tables). Each source subtype maps to a *distinct* atlas supertype rather than converging on
one, which is expected biology for a heterogeneous classical population but leaves no single
atlas node that captures the whole intercalated masses; soma location aligns only
approximately because WMBv1 registers these cells under striatal / cortical-subplate
nomenclature (see figure).

![Filtered AT figure for amygdala intercalated cell](figures/f1_for_amygdala_intercalated_cell.png)

*F1 across taxonomy levels for the four Foxp2+ intercalated source subtypes relevant to the
amygdala intercalated cell (GABA-1-Foxp2_Fmod, GABA-2-Foxp2_Adra2a, GABA-3-Foxp2_Col6a1,
GABA-4-Foxp2_Htr1f; Hochgerner 2023). Each panel row is one source subtype; nodes are
coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage =
fraction of source-subtype cells landing on this target; Purity = fraction of this target's
cells coming from the source subtype. With multiple source groups in the figure, Purity
differentiates them. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The
four subtypes disperse to four different GABAergic supertypes: GABA-3 transfers most cleanly
onto the 0288 STR-PAL Chst9 Gaba_4 supertype (F1=0.82), GABA-4 onto the 1015 STR-PAL Chst9
Gaba_5 cluster (F1=0.70), and GABA-1 onto the 065 IA Mgp Gaba subclass (F1=0.90), while
GABA-2 lands on a separate Chst9 supertype not among the current candidate edges.*

This dispersion is the central result: the intercalated masses are transcriptomically
several distinct GABAergic types in WMBv1, so the mapping is one classical type to many
narrower atlas subtype-clusters rather than a single 1:1 correspondence.

### 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype (0288) | Best cluster (1011) | Alignment |
|---|---|---|---|---|
| Soma location | intercalated amygdaloid nuclei [UBERON:0002884] | Striatum / Cortical subplate / Central amygdalar nucleus (region_fraction_100um 0.114) | Striatum / Cortical subplate / Central amygdalar nucleus (region_fraction_100um 0.107) | APPROXIMATE |
| NT type | GABAergic | not asserted | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Foxp2 | defining marker | 10.30 (cohort_pct 0.871) | 10.69 (cohort_pct 0.913) | CONSISTENT |
| Drd1 | defining marker | 5.04 (cohort_pct 0.935) | 5.79 (cohort_pct 0.960) | CONSISTENT |
| Oprm1 | defining marker | 6.94 (cohort_pct 0.887) | 7.33 (cohort_pct 0.881) | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um 0.114 | atlas-internal |
| GABA-1-Foxp2_Fmod AT | Annotation transfer | PARTIAL | F1=0.13 (class) | — |
| GABA-2-Foxp2_Adra2a AT | Annotation transfer | PARTIAL | F1=0.50 (subclass) | — |
| GABA-3-Foxp2_Col6a1 AT | Annotation transfer | SUPPORT | F1=0.82 (supertype) | — |
| GABA-4-Foxp2_Htr1f AT | Annotation transfer | PARTIAL | F1=0.11 (subclass) | — |

*(3 of 3 markers concordant with the classical type on this supertype; the child-cluster
coverage for each marker is 1.000, i.e. every child cluster of 0288 expresses Foxp2, Drd1
and Oprm1. The subtype signal concentrates in child cluster 1011 STR-PAL Chst9 Gaba_4
[CS20230722_CLUS_1011].)*

This supertype is the strongest atlas landing for the classical intercalated cell: the
Foxp2+ intercalated subtype GABA-3-Foxp2_Col6a1 transfers here with F1=0.82 and purity 0.96,
and all three defining markers are concordant.

**Supporting evidence:**
- Annotation transfer of GABA-3-Foxp2_Col6a1 lands on this supertype with F1=0.82, purity
  0.96, coverage 0.72 — 96% of the atlas cells receiving this subtype belong to 0288, a
  clean and specific transfer.
- All three defining markers (Foxp2, Drd1, Oprm1) are CONSISTENT, each at high cohort
  percentile among GABAergic amygdala types.

**Marker evidence provenance:**
- **Foxp2:** established at transcript level in intercalated cells by single-cell
  transcriptomics [5] and confirmed conserved across mammals [6]; atlas category TF on this
  supertype. Strong, primary, transcript-level support.
- **Drd1:** anchored to the DRD1+/DRD1− ITC subtype axis reported by [6]; atlas category
  DEFINING on the sibling 0284 supertype and expressed here (5.04). The classical
  intercalated masses contain both DRD1+ and DRD1− types [6], so partial Drd1 across atlas
  subtypes is expected.
- **Oprm1:** reported as an intercalated marker [5]; expressed here (6.94). Transcript-level
  atlas confirmation.

**Concerns:**
- Soma location is APPROXIMATE (region_fraction_100um 0.114; strict region_fraction 0.044):
  the atlas annotates 0288 as STR-PAL and most cells register to Striatum [MBA:477],
  Cortical subplate [MBA:703] and Central amygdalar nucleus [MBA:536]. *(note: the
  intercalated masses sit at the striato-amygdalar border and in CCF register to adjacent
  striatal / cortical-subplate voxels; the low in-region fraction reflects atlas registration
  nomenclature rather than a distant-region mismatch — weak counter-evidence.)*
- NT type is not asserted at supertype level in the atlas (assessable only at cluster level,
  where it is CONSISTENT).

**What would upgrade confidence:**
- Transgene- or reporter-targeted validation of the GABA-3 → 0288 correspondence (e.g.
  Foxp2 / Tshz1 labelling of the intercalated masses followed by spatial confirmation in the
  striato-amygdalar border), which would raise the location alignment from APPROXIMATE.

### 1011 STR-PAL Chst9 Gaba_4 [CS20230722_CLUS_1011] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Cluster (1011) | Alignment |
|---|---|---|---|
| Soma location | intercalated amygdaloid nuclei [UBERON:0002884] | Striatum / Cortical subplate / Central amygdalar nucleus (region_fraction_100um 0.107) | APPROXIMATE |
| NT type | GABAergic | GABA | CONSISTENT |
| Foxp2 | defining marker | 10.69 (cohort_pct 0.913) | CONSISTENT |
| Drd1 | defining marker | 5.79 (cohort_pct 0.960) | CONSISTENT |
| Oprm1 | defining marker | 7.33 (cohort_pct 0.881) | CONSISTENT |
| Sex ratio | not documented | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um 0.107 | atlas-internal |
| GABA-1-Foxp2_Fmod AT | Annotation transfer | PARTIAL | F1=0.13 (class) | — |
| GABA-2-Foxp2_Adra2a AT | Annotation transfer | PARTIAL | F1=0.50 (subclass) | — |
| GABA-3-Foxp2_Col6a1 AT | Annotation transfer | SUPPORT | F1=0.81 (cluster) | — |
| GABA-4-Foxp2_Htr1f AT | Annotation transfer | PARTIAL | F1=0.11 (subclass) | — |

*(3 of 3 markers concordant with the classical type on this cluster. This is the child
cluster of 0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288] where the GABA-3 subtype
concentrates.)*

The dominant child of 0288, cluster 1011 receives the Foxp2+ GABA-3 subtype at cluster
resolution with F1=0.81 and purity 0.99 — essentially all of this cluster's cells are the
transferred intercalated subtype, which is why the supertype-level signal is driven by this
child.

**Supporting evidence:**
- Annotation transfer of GABA-3-Foxp2_Col6a1 lands on this cluster with F1=0.81, purity 0.99,
  coverage 0.69: the tightest cluster-level intercalated transfer in the candidate set.
- All three defining markers CONSISTENT, each above the 88th cohort percentile.

**Marker evidence provenance:**
- **Foxp2 / Drd1 / Oprm1:** same primary transcript-level basis as for 0288 above ([5], [6]);
  all three expressed on 1011 at high cohort percentile.

**Concerns:**
- Soma location APPROXIMATE (region_fraction_100um 0.107; strict 0.034) for the same
  atlas-registration reason as the parent supertype. *(note: striato-amygdalar border
  registration; weak counter-evidence.)*

**What would upgrade confidence:**
- Cluster-level spatial or reporter confirmation that the GABA-3 intercalated subtype
  occupies the intercalated masses, distinguishing true localisation from CCF boundary
  scatter.

### 1015 STR-PAL Chst9 Gaba_5 [CS20230722_CLUS_1015] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Cluster (1015) | Alignment |
|---|---|---|---|
| Soma location | intercalated amygdaloid nuclei [UBERON:0002884] | Striatum / Cortical subplate / Basomedial amygdalar nucleus (region_fraction_100um 0.283) | APPROXIMATE |
| NT type | GABAergic | GABA | CONSISTENT |
| Foxp2 | defining marker | 10.49 (cohort_pct 0.873) | CONSISTENT |
| Drd1 | defining marker | 6.41 (cohort_pct 0.976) | CONSISTENT |
| Oprm1 | defining marker | 7.06 (cohort_pct 0.841) | CONSISTENT |
| Sex ratio | not documented | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um 0.283 | atlas-internal |
| GABA-1-Foxp2_Fmod AT | Annotation transfer | PARTIAL | F1=0.13 (class) | — |
| GABA-2-Foxp2_Adra2a AT | Annotation transfer | PARTIAL | F1=0.50 (subclass) | — |
| GABA-3-Foxp2_Col6a1 AT | Annotation transfer | PARTIAL | F1=0.69 (subclass) | — |
| GABA-4-Foxp2_Htr1f AT | Annotation transfer | SUPPORT | F1=0.70 (cluster) | — |

*(3 of 3 markers concordant with the classical type on this cluster; this cluster is the
specific landing site of a *different* intercalated subtype, GABA-4-Foxp2_Htr1f, than the
GABA-3 subtype that maps to 0288 / 1011.)*

Cluster 1015 is the clean landing site of a second Foxp2+ intercalated subtype,
GABA-4-Foxp2_Htr1f (F1=0.70, coverage 0.89 at cluster level), and it carries the strongest
in-region location signal of any candidate (region_fraction_100um 0.283, including cells at
the Basomedial amygdalar nucleus [MBA:319] and Cortical subplate [MBA:703]).

**Supporting evidence:**
- Annotation transfer of GABA-4-Foxp2_Htr1f lands on this cluster with F1=0.70 and coverage
  0.89 — the only clean landing for this subtype anywhere in the candidate set; the same
  subtype gives NO evidence on the D1 Sema5a clusters, confirming the specificity of the
  1015 assignment.
- All three defining markers CONSISTENT.
- Highest proximity fraction of the candidate set, with cells at amygdala-adjacent
  structures.

**Marker evidence provenance:**
- **Foxp2 / Drd1 / Oprm1:** transcript-level primary basis [5], [6]; all expressed on 1015.

**Concerns:**
- Soma location APPROXIMATE rather than in-region (region_fraction_100um 0.283; strict 0.048).
  *(note: proximity is higher than the other candidates and includes true amygdalar
  structures, so this is the weakest location concern of the survivors — boundary scatter
  rather than distant-region mismatch.)*
- Purity at cluster level is moderate (0.57), i.e. GABA-4 is not the only source subtype
  reaching 1015.

**What would upgrade confidence:**
- A higher-resolution or transgene-targeted transfer that raises the GABA-4 cluster F1 above
  0.80 and resolves the moderate purity.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0288 STR-PAL Chst9 Gaba_4 [CS20230722_SUPT_0288]` | — | 4588 | 🟡 MODERATE | GABA-3 AT F1=0.82 to supertype | Primary (supertype) |
| `1011 STR-PAL Chst9 Gaba_4 [CS20230722_CLUS_1011]` | 0288 STR-PAL Chst9 Gaba_4 | 4242 | 🟡 MODERATE | GABA-3 AT F1=0.81 to cluster | Primary (best child) |
| `1015 STR-PAL Chst9 Gaba_5 [CS20230722_CLUS_1015]` | 0289 STR-PAL Chst9 Gaba_5 | 966 | 🟡 MODERATE | GABA-4 AT F1=0.70 to cluster | Secondary (distinct subtype) |
| `0998 STR D1 Sema5a Gaba_3 [CS20230722_CLUS_0998]` | 0283 STR D1 Sema5a Gaba_3 | 424 | 🔴 LOW | GABA-4 no transfer; GABA-3 class-only | Eliminated (D1 striatal; location discordant) |
| `1000 STR D1 Sema5a Gaba_4 [CS20230722_CLUS_1000]` | 0284 STR D1 Sema5a Gaba_4 | 2301 | 🔴 LOW | GABA-4 no transfer | Eliminated (D1 striatal; no subtype landing) |
| `1009 STR-PAL Chst9 Gaba_3 [CS20230722_CLUS_1009]` | 0287 STR-PAL Chst9 Gaba_3 | 3132 | 🔴 LOW | GABA-3 subclass-only, collapses higher | Eliminated (no cluster-level transfer) |
| `0284 STR D1 Sema5a Gaba_4 [CS20230722_SUPT_0284]` | — | 2413 | 🔴 LOW | GABA-4 no transfer | Eliminated (D1 striatal) |
| `0285 STR-PAL Chst9 Gaba_1 [CS20230722_SUPT_0285]` | — | 4125 | 🔴 LOW | Subclass-only; Drd1 at cohort floor | Eliminated (weak transfer; Drd1 low) |
| `0287 STR-PAL Chst9 Gaba_3 [CS20230722_SUPT_0287]` | — | 3822 | 🔴 LOW | GABA-3 subclass-only, F1=0.10 supertype | Eliminated (no supertype-level transfer) |
| `0290 IA Mgp Gaba_1 [CS20230722_SUPT_0290]` | — | 608 | ⚪ UNCERTAIN | GABA-1 to IA Mgp subclass F1=0.90 | Eliminated (AT-best IA Mgp target not this edge) |

Total: 10 candidate edges assessed; all inherited the `evidencell:UncertainRelationship`
stub from candidate generation. The intercalated cell resolves to multiple narrower atlas
subtype-clusters (one classical type to many atlas targets).

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The amygdala intercalated cell is a GABAergic type [3], [4]
with soma in the intercalated amygdaloid nuclei [UBERON:0002884] [1], [2], [3], defined by
Foxp2 [5], [6], Drd1 [6] and Oprm1 [5]. Its `definition_basis` is CLASSICAL_MULTIMODAL — the
type rests on classical neuroanatomy plus molecular markers rather than a single modality.
The source report notes no further subtypes; the Foxp2/Tshz1 GABA-5..7 (Pax6/Tacr3/Tshz2)
types are intercalated-related but centrally located and were excluded from the declared
source correspondence.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy
(CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region
match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the
corresponding atlas-side value via the `property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from
precomputed expression on the cluster and from spatial registration for soma location.

**Annotation transfer.** The intercalated cell declared a source correspondence of four
Foxp2+ molecular subtypes from Hochgerner 2023, each a SUBSET of the classical type; MapMyCells
scored each subtype's cells against WMBv1.

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 (GABA-1-Foxp2_Fmod, GABA-2-Foxp2_Adra2a, GABA-3-Foxp2_Col6a1, GABA-4-Foxp2_Htr1f) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.7 |
| n cells | 55514 (filtered to 7777) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Source labels are transcriptomically-defined subtypes, not classical morpho-electrophysiological types; matching to the classical node rests on shared Foxp2/Drd1/Oprm1 markers. Fear-conditioned and non-neuronal cells excluded. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim
literature quotes in this report are validated against the evidencell knowledge base at write
time. Authored-prose evidence narratives are validated against their source
`evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable
identifier or unattributed blockquote. Specific mapping limitations and caveats are documented
per-candidate in the Discussion section.

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_…_CLUS_1011 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / SUPPORT (GABA-3) | atlas-internal |
| edge_…_SUPT_0288 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / SUPPORT (GABA-3) | atlas-internal |
| edge_…_CLUS_1015 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / SUPPORT (GABA-4) | atlas-internal |
| edge_…_CLUS_0998 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / NO_EVIDENCE (GABA-4) | atlas-internal |
| edge_…_CLUS_1000 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / NO_EVIDENCE (GABA-4) | atlas-internal |
| edge_…_CLUS_1009 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL | atlas-internal |
| edge_…_SUPT_0284 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / NO_EVIDENCE (GABA-4) | atlas-internal |
| edge_…_SUPT_0285 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL | atlas-internal |
| edge_…_SUPT_0287 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL | atlas-internal |
| edge_…_SUPT_0290 | ATLAS_METADATA; ANNOTATION_TRANSFER ×4 | PARTIAL / NO_EVIDENCE (GABA-4) | atlas-internal |

*Generated by evidencell `db6b114` at 2026-07-09T18:13:44+00:00 from
[kb/graphs/medial_temporal_lobe_amygdala/amygdala_intercalated_cell.yaml](kb/graphs/medial_temporal_lobe_amygdala/amygdala_intercalated_cell.yaml).*

</details>

---

## Discussion

**Primary mapping:** Amygdala intercalated cell → 0288 STR-PAL Chst9 Gaba_4
[CS20230722_SUPT_0288] and its child 1011 STR-PAL Chst9 Gaba_4 [CS20230722_CLUS_1011] at
MODERATE confidence, with a second Foxp2+ subtype mapping to 1015 STR-PAL Chst9 Gaba_5
[CS20230722_CLUS_1015]. Key support: annotation transfer of Foxp2+ intercalated subtypes plus
concordant Foxp2/Drd1/Oprm1 marker expression. Key caveats: soma location is only APPROXIMATE
(atlas registers these cells under striatal / cortical-subplate nomenclature), and the
classical type is transcriptomically several distinct atlas subtype-clusters rather than one,
so no single atlas node captures the whole intercalated masses.

No Cell Ontology term is currently assigned; this population is a candidate for a new CL term
covering the Foxp2+ GABAergic intercalated cells of the amygdala.

The most informative negative result is the dispersion pattern. Each declared source subtype
(GABA-1 to GABA-4) transfers to a *different* GABAergic supertype, and the two subtypes with
the cleanest supertype/cluster landings (GABA-3 → 0288 / 1011; GABA-4 → 1015) also carry
concordant markers. Meanwhile GABA-1-Foxp2_Fmod transfers most cleanly of all to the 065 IA
Mgp Gaba subclass — the atlas subclass whose very name (IA = intercalated amygdala) matches
the classical type — but its best-scoring supertype and cluster within that subclass are not
present among the current candidate edges. GABA-2-Foxp2_Adra2a similarly concentrates on a
Chst9 Gaba_2 supertype that is not among the candidate edges. These two AT-best targets should
be emitted and re-assessed before the mapping is considered complete.

### Proposed experiments and follow-ups

Annotation transfer has already been run (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`,
ArrayExpress:E-MTAB-12096 against CCN20230722), so the outstanding work is candidate-set
completion and targeted validation, not a first-pass transfer:

- **Emit and assess the AT-best IA Mgp and Chst9 Gaba_2 targets.** GABA-1-Foxp2_Fmod maps to
  the IA Mgp Gaba subclass at F1=0.90 and GABA-2-Foxp2_Adra2a to a Chst9 Gaba_2 supertype;
  neither best-scoring supertype/cluster is currently an edge. Add these targets and score
  their marker and location alignment so the full intercalated-to-atlas correspondence is
  captured. *Resolves open questions 1 and 2.*
- **Transgene- or reporter-targeted spatial validation.** Foxp2 / Tshz1 labelling of the
  intercalated masses with spatial recovery would test whether the GABA-3 → 0288 / 1011 and
  GABA-4 → 1015 assignments occupy the intercalated masses, converting the APPROXIMATE
  location alignment (driven by CCF striatal registration) into a positive in-region signal.
  Expected output: strengthened location property comparisons and an upgrade from MODERATE.

### Open questions

1. The AT-best target for GABA-1-Foxp2_Fmod (the 065 IA Mgp Gaba subclass, F1=0.90) is not
   represented by its best supertype/cluster among the candidate edges — emit and assess it.
2. The AT-best target for GABA-2-Foxp2_Adra2a (a Chst9 Gaba_2 supertype) is likewise absent
   from the candidate edges — emit and assess it.
3. Does any single atlas supertype capture the whole intercalated population, or is the
   classical type intrinsically a union of several GABAergic subtype-clusters in WMBv1? Present
   evidence favours the latter.
4. The soma-location APPROXIMATE alignment across all survivors stems from WMBv1's striatal /
   cortical-subplate registration of intercalated cells — does spatial re-examination of these
   clusters place them in the intercalated masses?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Ignacio et al. 2014 | [25309888](https://pubmed.ncbi.nlm.nih.gov/25309888) | soma location |
| [2] | Nardelli et al. 2024 | [39130512](https://pubmed.ncbi.nlm.nih.gov/39130512) | soma location |
| [3] | Veinante et al. 2013 | [25408902](https://pubmed.ncbi.nlm.nih.gov/25408902) | soma location; NT type |
| [4] | Pitkānen & Amaral 1994 | [8158266](https://pubmed.ncbi.nlm.nih.gov/8158266) | neurotransmitter type |
| [5] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931) | Foxp2, Oprm1 markers |
| [6] | Yu et al. 2023 | [36788214](https://pubmed.ncbi.nlm.nih.gov/36788214) | Foxp2, Drd1 markers |

---

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0288 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.62
  relationship: skos:narrowMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer of the Foxp2+ intercalated subtype
    GABA-3-Foxp2_Col6a1 lands cleanly on this supertype (F1=0.82, purity 0.96) in
    at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1, and 3 of 3 markers CONSISTENT
    (Foxp2, Drd1, Oprm1). Soma location is APPROXIMATE (region_fraction_100um: 0.114)
    because the atlas registers CS20230722_SUPT_0288 under striatal / cortical-subplate
    nomenclature; this is border registration rather than a distant-region mismatch.
    GABA-3 is one molecular subtype of the broader classical intercalated population, so
    the atlas supertype is narrower than the classical type.
  reconciliation_note: >
    Paired with the best child cluster CS20230722_CLUS_1011, where the GABA-3 subtype
    concentrates and drives the supertype-level signal. GABA-3 is one of four Foxp2+
    intercalated subtypes; GABA-4 maps separately onto CS20230722_CLUS_1015, while GABA-1
    and GABA-2 map best onto IA Mgp and Chst9 Gaba_2 supertypes not currently among the
    candidate edges.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Soma location APPROXIMATE (region_fraction_100um: 0.114; strict region_fraction:
        0.044); atlas registers these intercalated cells under striatal / cortical-subplate
        voxels at the striato-amygdalar border.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        The classical intercalated masses correspond to several distinct atlas subtype-clusters
        rather than to this supertype alone.
  proposed_experiments:
    - >
      Foxp2 / Tshz1 reporter labelling of the intercalated masses with spatial recovery to
      test whether the GABA-3 subtype mapping to CS20230722_SUPT_0288 occupies the
      intercalated masses, upgrading the APPROXIMATE location alignment.
  unresolved_questions:
    - "Emit and assess the AT-best IA Mgp (GABA-1-Foxp2_Fmod) and Chst9 Gaba_2 (GABA-2-Foxp2_Adra2a) targets, which outscore several current candidate edges but are not yet represented."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1011 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.62
  relationship: skos:narrowMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] The Foxp2+ intercalated subtype GABA-3-Foxp2_Col6a1 transfers to this
    cluster at F1=0.81 (purity 0.99) in
    at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1 — the tightest cluster-level
    intercalated landing in the candidate set — with 3 of 3 markers CONSISTENT (Foxp2, Drd1,
    Oprm1). Soma location is APPROXIMATE (region_fraction_100um: 0.107) for the same
    striato-amygdalar border-registration reason as its parent supertype. As one molecular
    subtype of the broader classical type, this cluster is narrower than the classical
    intercalated population.
  reconciliation_note: >
    Best child cluster of CS20230722_SUPT_0288; the supertype- and cluster-level GABA-3
    signals are the same molecular subtype resolved at two ranks. A distinct subtype,
    GABA-4-Foxp2_Htr1f, maps to CS20230722_CLUS_1015.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Soma location APPROXIMATE (region_fraction_100um: 0.107; strict region_fraction:
        0.034); striato-amygdalar border registration in the atlas.
  proposed_experiments:
    - >
      Cluster-level spatial or reporter confirmation that the GABA-3 intercalated subtype
      occupies the intercalated masses, distinguishing true localisation from CCF boundary
      scatter on CS20230722_CLUS_1011.
  unresolved_questions:
    - "Emit and assess the AT-best IA Mgp (GABA-1-Foxp2_Fmod) and Chst9 Gaba_2 (GABA-2-Foxp2_Adra2a) targets, which outscore several current candidate edges but are not yet represented."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1015 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:narrowMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] A second Foxp2+ intercalated subtype, GABA-4-Foxp2_Htr1f, lands cleanly and
    specifically on this cluster (F1=0.70, coverage 0.89) in
    at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1 — the only clean landing for this
    subtype in the candidate set — with 3 of 3 markers CONSISTENT (Foxp2, Drd1, Oprm1). This
    cluster carries the strongest in-region proximity of any candidate
    (region_fraction_100um: 0.283), including cells at amygdalar structures, so location is
    APPROXIMATE rather than discordant. It is narrower than the classical type, representing
    one subtype of the intercalated masses.
  reconciliation_note: >
    Represents a different molecular subtype (GABA-4) than the GABA-3 subtype mapping to
    CS20230722_SUPT_0288 / CS20230722_CLUS_1011; the classical intercalated cell corresponds
    to both.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Soma location APPROXIMATE (region_fraction_100um: 0.283; strict region_fraction:
        0.048) — highest proximity of the candidates, but still below in-region threshold.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Cluster-level purity is moderate (0.57); GABA-4 is not the sole subtype reaching this
        cluster.
  proposed_experiments:
    - >
      Higher-resolution or transgene-targeted transfer raising the GABA-4 cluster F1 above
      0.80 and resolving the moderate purity on CS20230722_CLUS_1015.
  unresolved_questions:
    - "Emit and assess the AT-best IA Mgp (GABA-1-Foxp2_Fmod) and Chst9 Gaba_2 (GABA-2-Foxp2_Adra2a) targets, which outscore several current candidate edges but are not yet represented."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_0998 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] This D1 Sema5a striatal cluster receives only class-level GABA-3 signal
    (F1=0.56) and no evidence from GABA-4, and soma location is discordant
    (region_fraction_100um: 0.029) in striatum / pallidum / substantia innominata.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1000 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] The D1 Sema5a Gaba_4 cluster receives only class-level GABA-3 signal
    (F1=0.56) with no GABA-4 evidence, and soma location is discordant
    (region_fraction_100um: 0.035) in striatum / nucleus accumbens / caudoputamen.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_CLUS_1009 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] GABA-3 transfer peaks only at subclass (F1=0.69) and collapses at supertype
    (F1=0.10), with soma location discordant (region_fraction_100um: 0.022) in striatum /
    nucleus accumbens / pallidum.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0284 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] This D1 Sema5a supertype receives only class-level GABA-3 signal (F1=0.56)
    and no GABA-4 evidence, with soma location discordant (region_fraction_100um: 0.035) in
    striatum / caudoputamen / nucleus accumbens.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0285 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] GABA-3 transfer is subclass-only (F1=0.69) with no supertype landing, Drd1
    sits near the cohort floor, and soma location is discordant (region_fraction_100um:
    0.014) in striatum / caudoputamen / pallidum.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0287 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] GABA-3 transfer peaks at subclass (F1=0.69) with no supertype-level landing
    (F1=0.10), and soma location is discordant (region_fraction_100um: 0.037) in striatum /
    nucleus accumbens / pallidum.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_CS20230722_SUPT_0290 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.35
  rationale: >
    [tier:CUT] The Foxp2 subtype GABA-1-Foxp2_Fmod transfers to the IA Mgp subclass at
    F1=0.90, but this specific supertype is not where GABA-1 concentrates and the AT-best IA
    Mgp supertype/cluster are not among the candidate edges; Drd1 is near-absent (APPROXIMATE)
    and soma location is discordant (region_fraction_100um: 0.092) in olfactory areas.
  reconciliation_note: >
    Biologically the most intriguing miss — IA Mgp is the intercalated-amygdala-named
    subclass — but the strong GABA-1 signal belongs to a sibling IA Mgp supertype/cluster
    that should be emitted and assessed rather than to CS20230722_SUPT_0290.
  unresolved_questions:
    - "Emit and assess the AT-best IA Mgp (GABA-1-Foxp2_Fmod) and Chst9 Gaba_2 (GABA-2-Foxp2_Adra2a) targets, which outscore several current candidate edges but are not yet represented."
```
<!-- verdict-block-end -->
