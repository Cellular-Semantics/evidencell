# entorhinal cortex layer III PCP4-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/_demo_ec_l3_20260607.yaml`*

---

## Introduction

Layer III principal neurons of the entorhinal cortex (EC) are glutamatergic
pyramidal cells distinguished from neighbouring EC populations by expression
of Purkinje cell protein 4 (PCP4). Together with EC layer II stellate and
pyramidal cells, EC layer III principal neurons are the main source of
direct cortical input to the hippocampus, projecting to CA1 and the subiculum
via the temporoammonic pathway [1]. Resolving this population against
the Whole Mouse Brain Atlas (WMBv1, CCN20230722) is a useful test case for
the mechanical Stage B emitter under no-AT conditions: the candidate set is
dense (multiple PCP4-positive glutamatergic EC clusters at rank 0 and
broader supertype groups at rank 1) but is supported only by atlas
metadata + classical literature.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer III) | — |
| NT | glutamatergic | [1] |
| Markers | Pcp4 (defining) | [2], [1] |
| CL term | pyramidal neuron [CL:0000598] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **NT (glutamatergic):** literature · [1]
  > Principal neurons in entorhinal cortex layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum (Ohara et al., 2021).
  > — Ohara et al., 2021, Entorhinal Cortex Glutamatergic Populations · [1] <!-- quote_key: 244909998_c43772d2 -->
- **Pcp4 (defining marker):** literature · [1], [2]
  > Principal neurons in EC layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum
  > — Ohara et al., 2021, INTRODUCTION · [1] <!-- quote_key: 244909998_bdbb7689 -->

  > Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2
  > — Antonio et al., 2014, abstract · [2] <!-- quote_key: 18746823_614030d2 -->

  *(note: Antonio et al. 2014 [2] establishes Pcp4 as a CA2 marker rather than an EC layer III marker. It supports Pcp4 as a discriminator among hippocampal-formation principal cells but does not directly attest the EC layer III population — that assertion rests on [1].)*
</details>

### Cell Ontology mapping

Cell Ontology mapping: pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] (BROAD).

---

## Results

Ten candidate atlas nodes were assessed across rank 0 (cluster) and rank 1
(supertype) under the filter `region=MBA:909 (entorhinal area)` /
`nt_type=glutamatergic`. No annotation-transfer evidence is available for
this classical node, so candidate assessment rests on ATLAS_METADATA
(precomputed Pcp4 expression, region distribution) plus literature support
for the classical type. MBA:909 (entorhinal area) is a non-painted CCF2020
parent; the per-candidate `region_fraction_100um` values therefore derive
from exact rollup edges over the painted EC descendants
(`region_count_completeness: exact` on every candidate). The mechanical
Stage B emitter assigned `evidencell:UncertainRelationship` to every edge;
the verdict blocks below revise this where evidence supports a stronger
relationship call.

### Candidate overview

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0024 L5/6 IT TPE-ENT Glut_1 [CS20230722_CLUS_0024] | 0007 L5/6 IT TPE-ENT Glut_1 | 751 | 🟡 MODERATE | Pcp4 CONSISTENT (10.92; pct 0.895) · loc CONSISTENT | best Pcp4-high rank-0 candidate; layer mismatch (L5/6) — closeMatch |
| 2 | 0025 L5/6 IT TPE-ENT Glut_1 [CS20230722_CLUS_0025] | 0007 L5/6 IT TPE-ENT Glut_1 | 512 | 🟡 MODERATE | Pcp4 CONSISTENT (9.46; pct 0.690) · loc CONSISTENT | sibling of 0024; same supertype; layer mismatch — closeMatch |
| 3 | 0010 L5/6 IT TPE-ENT Glut_4 [CS20230722_SUPT_0010] | — (supertype) | 1791 | 🟡 MODERATE | Pcp4 CONSISTENT (8.44; pct 0.641); region CONSISTENT (0.864) | rank-1 broader match; layer mismatch (L5/6 not L3) — broadMatch |
| 4 | 0027 L5/6 IT TPE-ENT Glut_2 [CS20230722_CLUS_0027] | 0008 L5/6 IT TPE-ENT Glut_2 | 739 | 🔴 LOW | Pcp4 CONSISTENT (8.15; pct 0.538) · loc CONSISTENT | distinct supertype; layer mismatch |
| — | 0014 IT EP-CLA Glut_2 [CS20230722_CLUS_0014] | 0004 IT EP-CLA Glut_2 | 849 | ⚪ UNCERTAIN | Pcp4 APPROXIMATE (5.46; pct 0.404) | EP-CLA off-target supertype |
| — | 0015 IT EP-CLA Glut_2 [CS20230722_CLUS_0015] | 0004 IT EP-CLA Glut_2 | 304 | ⚪ UNCERTAIN | Pcp4 APPROXIMATE (5.98; pct 0.427) | EP-CLA off-target supertype |
| — | 0068 ENTmv-PA-COAp Glut_3 [CS20230722_SUPT_0068] | — | 963 | ⚪ UNCERTAIN | Pcp4 APPROXIMATE (2.80; pct 0.326) | medial EC / PA / COA supertype, low Pcp4 |
| — | 0067 ENTmv-PA-COAp Glut_2 [CS20230722_SUPT_0067] | — | 943 | ⚪ UNCERTAIN | Pcp4 APPROXIMATE (1.66; pct 0.250) | medial EC / PA / COA supertype, low Pcp4 |
| — | 0054 L2 IT ENT-po Glut_4 [CS20230722_SUPT_0054] | — | 1867 | ⚪ UNCERTAIN | Pcp4 APPROXIMATE (1.53; pct 0.196); region 0.979 | EC layer 2 — wrong layer; low Pcp4 |
| — | 0053 L2 IT ENT-po Glut_3 [CS20230722_SUPT_0053] | — | 495 | ⚪ UNCERTAIN | Pcp4 APPROXIMATE (1.42; pct 0.141); region 0.989 | EC layer 2 — wrong layer; lowest Pcp4 |

10 edges total; all stamped `evidencell:UncertainRelationship` by the Stage B
emitter. Per-edge verdict blocks below revise four edges to MODERATE/LOW
under skos:closeMatch / skos:broadMatch.

### 0024 L5/6 IT TPE-ENT Glut_1 · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer III) | not available | Hippocampal formation [MBA:1089] count_100um=311; Entorhinal area, lateral part [MBA:918] count_100um=287; Entorhinal area, lateral part, layer 5 [MBA:139] count_100um=251 (CLUS_0024) | CONSISTENT (region); *(note: cluster's dominant painted layer label is L5 — see Concerns)* |
| NT type | glutamatergic | not available | Glut (CLUS_0024) | CONSISTENT |
| Pcp4 expression | defining marker | not available | Pcp4: 10.92; cohort_pct 0.895 (CLUS_0024) | CONSISTENT |
| Sex ratio | not documented | not available | MFR=1.13 (CLUS_0024) | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.753; Pcp4=10.92 (cohort pct 0.895); MFR=1.13; n_cells=751 | atlas-internal |

**Supporting evidence**
- Pcp4 expression in CLUS_0024 (10.92) sits at the top of the 5-member
  rank-0 EC-glutamatergic cohort (cohort percentile 0.895) — the highest
  precomputed Pcp4 of any rank-0 candidate.
- Region alignment is strong (`region_fraction_100um: 0.753`,
  `region_fraction: 0.626`, `region_count_completeness: exact`); the cluster
  sits within the entorhinal area (MBA:909) under exact rollup edges.
- NT type matches (Glut vs glutamatergic).

**Marker evidence provenance**
- **Pcp4 (defining):** classical-type assertion rests on Ohara et al. 2021
  [1] (EC layer III principal neurons express PCP4); Antonio et al. 2014 [2]
  is the primary PCP4 antibody / immunostaining citation but characterises
  CA2, not EC layer III. The direct EC-layer-III attribution thus relies on
  a single primary citation [1]. *(note: a targeted cite-traverse for
  primary EC layer III PCP4 evidence — e.g. Ramsden et al. 2015 — would
  strengthen this.)*

**Concerns**
- **Layer mismatch (interpretive).** The supertype label is "L5/6 IT
  TPE-ENT Glut_1" and the dominant painted descendant is
  *Entorhinal area, lateral part, layer 5 [MBA:139]* (count_100um=251 of
  ~311 painted EC cells); the classical type is EC **layer III**. The
  atlas-side L5/6 annotation contradicts the classical L3 assertion.
  *(note: MBA paints EC layer 5 and layer 6 distinctly but does not paint
  layer 3 explicitly in WMBv1 metadata exported here; the literal label
  may not exclude L3 cells, but it is the strongest counter-signal for
  this candidate.)*
- Sex ratio not documented for the classical type, so MFR=1.13 cannot be
  scored.

**What would upgrade confidence**
- Annotation transfer from a labelled EC-layer-III Pcp4+ source (e.g. a
  Ramsden / Canto-style patch-seq or layer-resolved scRNA-seq dataset)
  with F1 ≥ 0.75 at CLUSTER level would resolve the layer-assignment
  ambiguity directly.
- Targeted literature trawl for primary EC layer III PCP4 evidence beyond
  the single Ohara 2021 citation.

### 0025 L5/6 IT TPE-ENT Glut_1 · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer III) | not available | Hippocampal formation [MBA:1089] count_100um=184; Entorhinal area, lateral part [MBA:918] count_100um=181; Entorhinal area, lateral part, layer 5 [MBA:139] count_100um=170 (CLUS_0025) | CONSISTENT (region); layer mismatch noted |
| NT type | glutamatergic | not available | Glut | CONSISTENT |
| Pcp4 expression | defining marker | not available | Pcp4: 9.46; cohort_pct 0.690 | CONSISTENT |
| Sex ratio | not documented | not available | MFR=1.22 | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.698; Pcp4=9.46 (cohort pct 0.690); n_cells=512 | atlas-internal |

**Supporting evidence**
- Sibling cluster of CLUS_0024 under the same supertype 0007
  (L5/6 IT TPE-ENT Glut_1); Pcp4 expression CONSISTENT at 9.46
  (cohort percentile 0.690).
- Region match `region_fraction_100um: 0.698` (exact rollup).

**Concerns**
- Same layer mismatch as CLUS_0024: dominant painted descendant is EC
  lateral, layer 5 [MBA:139]. The classical L3 assertion is not
  positively supported by atlas metadata.
- Lower n_cells (512 vs 849/751 for sibling clusters); cohort percentile
  is lower than CLUS_0024.

**What would upgrade confidence**
- As for CLUS_0024.

### 0010 L5/6 IT TPE-ENT Glut_4 · 🟡 MODERATE (rank-1 / supertype)

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer III) | Hippocampal formation [MBA:1089] count_100um=1280; Entorhinal area, lateral part [MBA:918] count_100um=1035; Entorhinal area, lateral part, layer 5 [MBA:139] count_100um=877 | not assessed | CONSISTENT (region); layer mismatch noted |
| NT type | glutamatergic | not asserted | not assessed | NOT_ASSESSED |
| Pcp4 expression | defining marker | Pcp4: 8.44; cohort_pct 0.641; child-coverage 1.000 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.864; Pcp4=8.44 (cohort pct 0.641, child-coverage 1.000); n_cells=1791 | atlas-internal |

*(Child-cluster Pcp4 coverage = 1.000: every child cluster of the supertype
expresses Pcp4 above MIN_DETECTABLE, so the supertype-mean is not driven by
a minority of children.)*

**Supporting evidence**
- Rank-1 candidate with the strongest region alignment of the L5/6 IT
  TPE-ENT group (`region_fraction_100um: 0.864`); cohort dominance is
  weak (rank 1 of 5 in a tied cohort, score 4 vs next-best 4 — Stage A
  does not separate this candidate from siblings on aggregate score).
- Pcp4 CONSISTENT at 8.44 (cohort percentile 0.641) with full
  child-coverage 1.000.

**Concerns**
- Supertype-level granularity: this is a broader candidate spanning
  multiple child clusters; the EC layer III specificity is not directly
  resolvable at this level.
- Layer mismatch: supertype label is L5/6 IT TPE-ENT — not L3.
- NT type not asserted at this supertype level (NOT_ASSESSED), though
  it is consistently Glut at child-cluster level.

**What would upgrade confidence**
- Drill down to child clusters that carry NT type asserted and check
  whether a specific child is enriched for any L3-restricted signal.

### 0027 L5/6 IT TPE-ENT Glut_2 · 🔴 LOW

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | entorhinal cortex [UBERON:0002728] (layer III) | not available | Hippocampal formation [MBA:1089] count_100um=665; Entorhinal area, lateral part [MBA:918] count_100um=519; Entorhinal area, lateral part, layer 5 [MBA:139] count_100um=447 (CLUS_0027) | CONSISTENT (region); layer mismatch noted |
| NT type | glutamatergic | not available | Glut | CONSISTENT |
| Pcp4 expression | defining marker | not available | Pcp4: 8.15; cohort_pct 0.538 | CONSISTENT |
| Sex ratio | not documented | not available | MFR=1.13 | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.637; Pcp4=8.15 (cohort pct 0.538); n_cells=739 | atlas-internal |

**Supporting evidence**
- Pcp4 CONSISTENT at 8.15 (cohort percentile 0.538); region match
  `region_fraction_100um: 0.637`.

**Concerns**
- Distinct supertype (0008 L5/6 IT TPE-ENT Glut_2) from the primary pair
  (0007); the L5/6 layer mismatch applies and there is no positive
  signal that distinguishes CLUS_0027 from the higher-Pcp4 0007 siblings.
- Cohort percentile (0.538) sits below CLUS_0024 (0.895) and CLUS_0025
  (0.690).

**What would upgrade confidence**
- AT-based assignment that distinguishes the 0007 vs 0008 supertypes for
  Pcp4+ EC L3 source cells.

## Eliminated candidates

All six edges below are UNCERTAIN. The shared disqualifying signal is **low
Pcp4 expression** (cohort percentile ≤ 0.43, well below the Pcp4-CONSISTENT
candidates at ≥ 0.54), with a secondary layer / supertype mismatch in two
sub-groups.

**EP-CLA supertype (0004 IT EP-CLA Glut_2 — CLUS_0014, CLUS_0015).** The
supertype label "IT EP-CLA Glut_2" assigns these cells to EP (endopiriform)
/ CLA (claustrum) rather than entorhinal cortex, even though the rollup
region_fraction_100um is high (0.751 / 0.670). Pcp4 expression is
APPROXIMATE (5.46, pct 0.404 for CLUS_0014; 5.98, pct 0.427 for CLUS_0015) —
appreciably lower than the L5/6 IT TPE-ENT siblings. The region alignment
likely reflects EC-adjacent piriform / claustrum cells captured by the
rollup; the supertype label is the strong counter-signal.

**ENTmv-PA-COAp supertypes (SUPT_0067, SUPT_0068).** Medial EC / piriform
amygdalar / cortical amygdalar populations. Pcp4 is APPROXIMATE at low
absolute values (1.66 / 2.80) and low cohort percentile (0.250 / 0.326).
Region alignment is decent (`region_fraction_100um: 0.631` / `0.711`,
exact rollup) but Pcp4 is too low to support an EC-layer-III mapping.

**L2 IT ENT-po supertypes (SUPT_0053, SUPT_0054).** Explicit EC **layer 2**
supertype labels — direct layer DISCORDANT with the classical L3 assertion.
Region alignment is the highest of any candidate (`region_fraction_100um:
0.989` / `0.979`) but Pcp4 is the lowest in the cohort (1.42, pct 0.141;
1.53, pct 0.196). Strong counter-evidence: wrong layer + low Pcp4.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** EC layer III PCP4-positive pyramidal cells
are glutamatergic [1] principal neurons of the entorhinal cortex layer III
[UBERON:0002728] defined by Pcp4 expression [2], [1] (definition_basis:
CLASSICAL_MULTIMODAL).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the
WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) under
the filter `region=MBA:909 (entorhinal area)` / `nt_type=glutamatergic`.
MBA:909 is a non-painted CCF2020 parent, so per-candidate region fractions
come from exact rollup edges over painted EC descendants
(`region_count_completeness: exact` on every candidate edge). Full scoring
rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the
`property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical
values came from precomputed expression on the cluster (cluster.yaml in
the taxonomy reference store) and from MERFISH spatial registration
rollups for soma location.

**Annotation transfer.** No AT runs are available for this classical node
in the canonical artifact path; the mapping rests on ATLAS_METADATA +
literature support only.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs,
and verbatim literature quotes in this report are validated against the
evidencell knowledge base at write time. Authored-prose evidence
narratives are validated against their source `evidence_items[*].explanation`
fields. The pre-write hook rejects any unresolvable identifier or
unattributed blockquote. Specific mapping limitations and caveats are
documented per-candidate in the Discussion section.

*Generated by evidencell `0934db5` at 2026-06-07T18:26:57+00:00 from
[kb/graphs/hippocampus/_demo_ec_l3_20260607.yaml](kb/graphs/hippocampus/_demo_ec_l3_20260607.yaml).*

**Evidence base.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_…_to_CS20230722_CLUS_0014 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_CLUS_0015 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_CLUS_0024 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_CLUS_0025 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_CLUS_0027 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_SUPT_0010 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_SUPT_0053 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_SUPT_0054 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_SUPT_0067 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_…_to_CS20230722_SUPT_0068 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** entorhinal cortex layer III PCP4-positive pyramidal
cell → 0024 L5/6 IT TPE-ENT Glut_1 [CS20230722_CLUS_0024] at MODERATE
confidence. Key support: precomputed atlas expression (Pcp4=10.92, cohort
percentile 0.895; the highest of any rank-0 candidate) with strong region
alignment (`region_fraction_100um: 0.753`, exact rollup). Key caveats:
atlas-side supertype label assigns the cluster to L5/6 (not L3), and the
mapping rests on a single literature primary [1] for EC-layer-III PCP4.
The Cell Ontology has no specific term for EC layer III PCP4-positive
pyramidal cells; pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)]
is the closest ancestor. EC layer III PCP4-positive pyramidal cells project
to CA1 and the subiculum. PCP4 is shared with CA2 pyramidal cells but
distinguishes EC layer III from layer II populations. CL:0000598
(pyramidal neuron) is the best available match; no EC layer III-specific
CL term exists.

### Proposed experiments and follow-ups

- **What:** MapMyCells annotation transfer from a layer-resolved EC scRNA-seq
  / patch-seq source labelled for Pcp4+ EC L3 (e.g. Ramsden / Canto / Ohara
  follow-on).
  **Target:** F1 ≥ 0.75 at CLUSTER level for CS20230722_CLUS_0024 or
  CLUS_0025.
  **Expected output:** AnnotationTransferEvidence on the primary edges.
  **Resolves:** open questions 1, 2 (cluster/sibling resolution, layer
  ambiguity).
- **What:** Targeted literature cite-traverse on "PCP4 entorhinal cortex
  layer III" to corroborate Ohara et al. 2021 [1] with a second primary
  citation (Antonio et al. 2014 [2] does not directly attest EC L3).
  **Target:** ≥ 1 additional primary study with morphology / layer-resolved
  PCP4 IHC of EC layer III cells.
  **Expected output:** LiteratureEvidence on the classical node.
  **Resolves:** marker provenance concern.

### Open questions

1. Does the L5/6 IT TPE-ENT supertype label (0007) reflect an atlas
   layer-painting limitation (no explicit L3 paint in WMBv1 metadata) or
   a genuine spatial mismatch between the PCP4+ EC L3 population and the
   atlas cluster soma distribution?
2. Are CLUS_0024 and CLUS_0025 transcriptomically distinguishable
   subtypes within the same EC layer III PCP4+ population, or atlas
   over-clustering of a single biological cell type? (No AT or
   indistinguishability evidence is currently on file; pool_candidates
   was empty.)
3. Is the EP-CLA cohort (CLUS_0014, CLUS_0015) capturing genuine
   EC-adjacent piriform/claustrum Pcp4+ cells, and if so are they
   misannotated as IT EP-CLA when they may belong to EC?

---

## References

| # | Citation | PMID | Used for |
|---:|---|---|---|
| [1] | Ohara et al., 2021. *Laminar Organization of the Entorhinal Cortex in Macaque Monkeys Based on Cell-Type-Specific Markers and Connectivity.* | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | neurotransmitter type; EC layer III Pcp4 marker |
| [2] | Antonio et al., 2014. *Distinct physiological and developmental properties of hippocampal CA2 subfield revealed by using anti-Purkinje cell protein 4 antibody.* | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 antibody / immunostaining method |

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0024 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  rationale: >
    Pcp4 CONSISTENT at 10.92 (cohort_pct 0.895 in a 5-member rank-0
    EC-glutamatergic survival cohort) and region_fraction_100um 0.753
    (exact rollup over MBA:909 descendants) on CS20230722_CLUS_0024
    anchor a skos:closeMatch despite the atlas-side L5/6 supertype label
    contradicting the classical L3 assertion; 1 of 1 markers CONSISTENT
    via precomputed atlas expression on CS20230722_CLUS_0024. No annotation-transfer evidence is
    available, capping confidence at MODERATE under the no-AT rubric.
  reconciliation_note: >
    Stage B emitter assigned evidencell:UncertainRelationship; under the
    2026-05-26 rubric this should be skos:closeMatch (1:1 shape with the
    L5/6-vs-L3 layer-label contradiction documented). Recommend
    curator-review pass to migrate the predicate.
  unresolved_questions:
    - "Does the L5/6 IT TPE-ENT supertype label reflect a WMBv1 layer-painting limitation (no explicit L3 paint) or a true spatial mismatch with PCP4+ EC L3 cells?"
    - "Are CS20230722_CLUS_0024 and CS20230722_CLUS_0025 distinct subtypes of a single EC L3 PCP4+ population, or atlas over-clustering — pool_candidates was empty so no Stage 2b indistinguishability surfaced."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0025 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.50
  rationale: >
    Sibling of CS20230722_CLUS_0024 under the same supertype 0007 L5/6 IT
    TPE-ENT Glut_1; Pcp4 CONSISTENT at 9.46 (cohort_pct 0.690) and
    region_fraction_100um 0.698 (exact rollup) support skos:closeMatch; 1
    of 1 markers CONSISTENT via precomputed atlas expression. Same L5/6-vs-L3
    layer-label contradiction as CLUS_0024; no annotation-transfer
    evidence caps confidence at MODERATE.
  reconciliation_note: >
    Stage B emitter assigned evidencell:UncertainRelationship; under the
    2026-05-26 rubric this should be skos:closeMatch (sibling of
    CS20230722_CLUS_0024 in supertype 0007).
  unresolved_questions:
    - "Is CS20230722_CLUS_0025 transcriptomically distinct from CS20230722_CLUS_0024 in the EC L3 PCP4+ context, or is the split atlas over-clustering?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0010 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.50
  rationale: >
    Rank-1 supertype CS20230722_SUPT_0010 (0010 L5/6 IT TPE-ENT Glut_4) has
    Pcp4 CONSISTENT at 8.44 (cohort_pct 0.641, child-coverage 1.000 — every
    child cluster expresses Pcp4 above MIN_DETECTABLE) and the strongest
    region alignment of the L5/6 IT TPE-ENT group
    (region_fraction_100um 0.864, exact rollup); 1 of 1 markers
    CONSISTENT via precomputed atlas expression (child-coverage 1.000 across the supertype). This is a skos:broadMatch (1:n)
    — the supertype is broader than the EC L3 PCP4+ classical type and
    carries the L5/6 layer-label contradiction. NT_TYPE is NOT_ASSESSED
    at this rank.
  reconciliation_note: >
    Stage B assigned evidencell:UncertainRelationship; rubric supports
    skos:broadMatch with mapping_cardinality 1:n given the rank-1
    granularity.
  unresolved_questions:
    - "Drill down to child clusters of CS20230722_SUPT_0010 to test whether a specific child is enriched for any L3-restricted signal beyond Pcp4."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0027 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    CS20230722_CLUS_0027 belongs to supertype 0008 L5/6 IT TPE-ENT Glut_2,
    distinct from the primary 0007 siblings. Pcp4 CONSISTENT at 8.15
    (cohort_pct 0.538) and region_fraction_100um 0.637 (exact rollup)
    support a skos:closeMatch in shape, but cohort percentile is below
    the 0007 siblings (CLUS_0024 0.895, CLUS_0025 0.690) and no positive
    signal distinguishes the 0008 supertype from 0007 for the EC L3 PCP4+
    target; 1 of 1 markers CONSISTENT via precomputed atlas expression.
  reconciliation_note: >
    Stage B assigned evidencell:UncertainRelationship; rubric supports a
    weak skos:closeMatch at LOW confidence (single evidence type,
    contradictions partially unresolved between 0007 vs 0008).
  unresolved_questions:
    - "AT-based assignment is needed to distinguish supertypes 0007 vs 0008 of L5/6 IT TPE-ENT for the EC L3 PCP4+ population."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0014 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    CS20230722_CLUS_0014 belongs to supertype 0004 IT EP-CLA Glut_2
    (endopiriform / claustrum, not entorhinal). Pcp4 APPROXIMATE at 5.46
    (cohort_pct 0.404) is substantially below the L5/6 IT TPE-ENT
    Pcp4-CONSISTENT candidates; 0 of 1 markers CONSISTENT under the
    APPROXIMATE call. region_fraction_100um 0.751 likely reflects
    EC-adjacent piriform/claustrum cells in the exact rollup, not EC
    proper.
  reconciliation_note: >
    Predicate evidencell:UncertainRelationship is consistent with the
    APPROXIMATE marker + supertype-mismatch evidence; retain.
  unresolved_questions:
    - "Are the IT EP-CLA Glut_2 cells (CS20230722_CLUS_0014, CS20230722_CLUS_0015) genuine EC-adjacent Pcp4+ piriform/claustrum cells, or atlas-misannotated EC cells?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_CLUS_0015 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    Sibling of CS20230722_CLUS_0014 under supertype 0004 IT EP-CLA Glut_2.
    Pcp4 APPROXIMATE at 5.98 (cohort_pct 0.427); 0 of 1 markers
    CONSISTENT under the APPROXIMATE call; supertype assignment to
    EP-CLA contradicts the EC L3 classical type.
  reconciliation_note: >
    Predicate evidencell:UncertainRelationship is consistent with the
    evidence; retain.
  unresolved_questions:
    - "Resolve whether CS20230722_CLUS_0014 and CS20230722_CLUS_0015 represent EC-misannotated cells or genuine EP-CLA Pcp4+ populations."
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0068 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    CS20230722_SUPT_0068 (0068 ENTmv-PA-COAp Glut_3) is a medial EC /
    piriform amygdalar / cortical amygdalar supertype. Pcp4 APPROXIMATE
    at 2.80 (cohort_pct 0.326, child-coverage 1.000); 0 of 1 markers
    CONSISTENT. region_fraction_100um 0.711 (exact rollup) is partially
    supportive but the off-target ENTmv/PA/COAp supertype assignment and
    low Pcp4 disqualify the mapping. NT_TYPE NOT_ASSESSED at this rank.
  reconciliation_note: >
    Predicate evidencell:UncertainRelationship is consistent with the
    evidence; retain.
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0067 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  rationale: >
    CS20230722_SUPT_0067 (0067 ENTmv-PA-COAp Glut_2) sibling of SUPT_0068.
    Pcp4 APPROXIMATE at 1.66 (cohort_pct 0.250, child-coverage 1.000); 0
    of 1 markers CONSISTENT. Off-target ENTmv/PA/COAp supertype and low
    Pcp4 disqualify the mapping; region_fraction_100um 0.631 (exact
    rollup) is uninformative against the supertype label.
  reconciliation_note: >
    Predicate evidencell:UncertainRelationship is consistent with the
    evidence; retain.
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0054 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_SUPT_0054 (0054 L2 IT ENT-po Glut_4) is an EC layer 2
    supertype — direct layer DISCORDANT with the classical EC layer 3
    assertion. Pcp4 APPROXIMATE at 1.53 (cohort_pct 0.196, child-coverage
    1.000); 0 of 1 markers CONSISTENT. The very high region_fraction_100um
    0.979 (exact rollup) confirms the cluster is EC but with the wrong
    layer assignment.
  reconciliation_note: >
    Predicate should remain evidencell:UncertainRelationship or be
    migrated to a refuted/null-match form; the layer-2 atlas label is a
    direct contradiction of EC L3.
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ec_layer3_pyramidal_cell_hippocampus_to_CS20230722_SUPT_0053 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_SUPT_0053 (0053 L2 IT ENT-po Glut_3) is an EC layer 2
    supertype — direct layer DISCORDANT with the classical EC layer 3
    assertion. Pcp4 APPROXIMATE at 1.42 (cohort_pct 0.141, child-coverage
    1.000) is the lowest in the cohort; 0 of 1 markers CONSISTENT.
    region_fraction_100um 0.989 (exact rollup) confirms EC location but
    with the wrong layer.
  reconciliation_note: >
    Predicate should remain evidencell:UncertainRelationship or be
    migrated to a refuted/null-match form; layer-2 atlas label directly
    contradicts EC L3.
  unresolved_questions: []
```
<!-- verdict-block-end -->
