# CA1 radiatum giant cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml`*

---

## Introduction

The CA1 radiatum giant cell is a rare specialised excitatory projection neuron with soma in hippocampus stratum radiatum [UBERON:0005372], first described by Kirson and Yaari (2000) [1]. It is glutamatergic and exhibits NMDA-receptor-driven burst firing on synaptic activation:

> a recently discovered excitatory projection neuron, the CA1 radiatum giant cell (RGC). Glutamatergic synaptic activation, even after blocking non-NMDA receptors, fired an NMDA receptor-dependent burst of action potentials in RGCs
> — Kirson et al. 2000, Synaptic Properties and Neurotransmitter Systems · [1] <!-- quote_key: 502543_4f78ac74 -->

Placing this classical type within a single-cell transcriptomic atlas matters because the RGC sits at the boundary of stratum radiatum and the CA1 pyramidal layer, and because no transcriptomic profile of the RGC has been published — atlas placement here rests on soma location and broad neurotransmitter class only.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum radiatum [UBERON:0005372] | [1] |
| NT | glutamatergic | [1] |
| Defining markers | not documented | — |
| Negative markers | not documented | — |
| Neuropeptides | not documented | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomical description in rat CA1 stratum radiatum · [1]
- **NT type:** glutamatergic projection neuron with NMDA-receptor-dependent burst firing · [1]
  > a recently discovered excitatory projection neuron, the CA1 radiatum giant cell (RGC). Glutamatergic synaptic activation, even after blocking non-NMDA receptors, fired an NMDA receptor-dependent burst of action potentials in RGCs
  > — Kirson et al. 2000, Synaptic Properties and Neurotransmitter Systems · [1] <!-- quote_key: 502543_4f78ac74 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Soma-location alignment to the CA1 region supports a broad placement of the CA1 radiatum giant cell within the 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] supertype, with the top-ranked child cluster being 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] (see property comparison tables below). Because no defining transcript or protein markers have been entered for this classical type, the assessment rests entirely on regional concordance and broad glutamatergic identity, and cannot resolve which (if any) CA1-ProS Glut_1 cluster corresponds specifically to the radiatum giant cell.

### 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum radiatum [UBERON:0005372] | Hippocampal formation [MBA:1089]; Field CA1 [MBA:382]; Field CA1, pyramidal layer [MBA:407] (region_fraction_100um=0.934) | Field CA1, pyramidal layer [MBA:407] on 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] (region_fraction_100um=0.969) | CONSISTENT |
| NT type | glutamatergic | not asserted on supertype | Glut on 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |

*(Child-cluster breakdown: 4 of the 5 top rank-0 candidates in this report — 0261, 0262, 0263, 0269 CA1-ProS Glut_1 — are children of supertype 0069 and all sit within CA1 with `region_fraction_100um` between 0.558 and 0.969. The radiatum giant cell distributes across these CA1-ProS Glut_1 children at supertype level; no single child is preferred on biological grounds because markers are not available.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas soma-location overlap | Atlas metadata | PARTIAL | region_fraction_100um=0.934; strict region_fraction=0.231 | atlas-internal |

**Supporting evidence**
- Soma of 0069 CA1-ProS Glut_1 is concentrated in Field CA1 (Field CA1, pyramidal layer count_100um=27305 of 28476 in the hippocampal formation rollup), placing the supertype unambiguously within CA1 — the anatomical region of the radiatum giant cell.
- The supertype's name (CA1-ProS Glut_1) is internally consistent with a glutamatergic CA1 projection-neuron identity matching [1].

**Concerns**
- The atlas supertype carries no NT assertion at rank 1 (`nt_type: NOT_ASSESSED`); the NT match is inherited from the child clusters (all Glut).
- Soma location captures the pyramidal layer, not stratum radiatum specifically. WMBv1 location records soma position; the radiatum giant cell soma sits in stratum radiatum, an adjacent (not identical) layer. The CA1 rollup is consistent but the layer-level distinction is not resolved here *(note: stratum radiatum is immediately apical to the pyramidal layer; CA1-rollup concordance is expected even for a stratum-radiatum-resident neuron, and is therefore weak supporting signal)*.
- No transcript or protein markers are available on the classical side to break the tie among the four CA1-ProS Glut_1 children.

**What would upgrade confidence**
- Targeted literature trawl for any transcriptomic, neuropeptide, or transcription-factor characterisation of the CA1 radiatum giant cell — none is currently in the KB.
- Any future dataset that genetically targets or post-hoc identifies CA1 radiatum giant cells and provides annotation-transfer evidence onto WMBv1, with a per-level F1 readout — would let one of the CA1-ProS Glut_1 children be preferred over the supertype call.

### 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum radiatum [UBERON:0005372] | (parent SUPT_0069: region_fraction_100um=0.934) | Field CA1, pyramidal layer [MBA:407] count_100um=19403; region_fraction_100um=0.969 | CONSISTENT |
| NT type | glutamatergic | (parent NT not asserted) | Glut | CONSISTENT |

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas soma-location overlap | Atlas metadata | PARTIAL | region_fraction_100um=0.969; strict region_fraction=0.266 | atlas-internal |

**Supporting evidence**
- 0262 CA1-ProS Glut_1 has the highest proximity-weighted CA1 fraction of any rank-0 candidate in the cohort (region_fraction_100um=0.969) and a 12,018-cell population, making it the largest and most regionally-concordant CA1-ProS Glut_1 cluster.
- Its glutamatergic NT annotation aligns with [1].
- It sits as a child of the primary supertype call (0069 CA1-ProS Glut_1), so a close-match call on this cluster is consistent with the supertype broad-match on its parent.

**Concerns**
- Without classical-side markers, picking 0262 over sibling children (0261, 0263, 0269 CA1-ProS Glut_1) is a tie-breaker on location proximity alone, not on biological specificity.
- The atlas does not annotate stratum-radiatum versus pyramidal-layer residence at the soma resolution recorded for WMBv1 clusters; the layer-level question stays unresolved *(note: as for the supertype, CA1-pyramidal-layer registration is expected to dominate even for radiatum-resident neurons whose somata lie near the layer boundary)*.

**What would upgrade confidence**
- A primary-literature characterisation of CA1 radiatum giant cell transcriptomic markers, or any single-cell dataset that targets and labels these cells, to test whether 0262 (or one of its siblings) carries an RGC-distinguishing signature.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] | — | 19061 | 🟡 MODERATE | CA1 soma region_fraction_100um=0.934 | Primary (supertype) |
| 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] | 0069 CA1-ProS Glut_1 | 12018 | 🟡 MODERATE | CA1 soma region_fraction_100um=0.969; Glut | Secondary (best child within supertype) |
| 0263 CA1-ProS Glut_1 [CS20230722_CLUS_0263] | 0069 CA1-ProS Glut_1 | 4105 | 🔴 LOW | CA1 soma region_fraction_100um=0.934 | Eliminated (sibling of best child; no markers to discriminate) |
| 0269 CA1-ProS Glut_1 [CS20230722_CLUS_0269] | 0069 CA1-ProS Glut_1 | 1894 | 🔴 LOW | CA1 soma region_fraction_100um=0.919 | Eliminated (sibling of best child; no markers to discriminate) |
| 0261 CA1-ProS Glut_1 [CS20230722_CLUS_0261] | 0069 CA1-ProS Glut_1 | 215 | 🔴 LOW | CA1 stratum oriens region_fraction_100um=0.558 | Eliminated (lower proximity; oriens-leaning) |
| 0271 CA1-ProS Glut_2 [CS20230722_CLUS_0271] | 0070 CA1-ProS Glut_2 | 419 | 🔴 LOW | CA1 stratum oriens region_fraction_100um=0.567 | Eliminated (different supertype; oriens-leaning) |
| 0072 CA1-ProS Glut_4 [CS20230722_SUPT_0072] | — | 3493 | 🔴 LOW | CA1 region_fraction_100um=0.873; NT not asserted | Eliminated (not parent of primary child cohort) |
| 0070 CA1-ProS Glut_2 [CS20230722_SUPT_0070] | — | 4609 | 🔴 LOW | CA1 region_fraction_100um=0.682; NT not asserted | Eliminated (oriens-leaning supertype) |
| 0074 CA1-ProS Glut_6 [CS20230722_SUPT_0074] | — | 1921 | 🔴 LOW | Prosubiculum count_100um=1062; region_fraction_100um=0.651 | Eliminated (prosubiculum-leaning) |
| 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] | — | 143 | ⚪ UNCERTAIN | Field CA3 dominant; region_fraction_100um=0.555 | Eliminated (CA3/CA2-FC-IG context; not CA1) |

</details>

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The CA1 radiatum giant cell is defined on a CLASSICAL_MULTIMODAL basis — soma in CA1 stratum radiatum, glutamatergic neurotransmitter identity, and NMDA-receptor-dependent burst firing reported in Kirson and Yaari (2000) [1]. Defining molecular markers have not been entered; this is a known gap surfaced in the node's notes field.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values for region come from soma-position counts at the queried anat term (strict and 100µm-proximity).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `acff35d` at 2026-06-10T13:19:28+00:00 from [kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml](kb/graphs/hippocampus/20260427_hippocampus_glutamatergic_report_ingest.yaml).*

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0069 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0262 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0263 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0269 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0261 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0271 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0072 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0070 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0074 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0100 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** CA1 radiatum giant cell → 0069 CA1-ProS Glut_1 [CS20230722_SUPT_0069] at MODERATE confidence, with 0262 CA1-ProS Glut_1 [CS20230722_CLUS_0262] as the best-aligned child within that supertype. Key support: soma-location concordance to CA1 (region_fraction_100um=0.934 at the supertype; 0.969 on the best child) and consistent glutamatergic identity on the child clusters. Key caveats: absence of molecular markers on the classical side (curation gap), and the atlas's pyramidal-layer-leaning soma registration cannot resolve stratum radiatum residence.

No Cell Ontology term currently assigned. This is a rare specialised excitatory projection neuron first described by Kirson and Yaari (2000) [1] for which modern transcriptomic characterisation is still missing; the node is flagged as a candidate for a CL contribution.

### Proposed experiments and follow-ups

- **What:** Targeted literature search for transcriptomic, neuropeptide, or TF characterisation of the CA1 radiatum giant cell.
  **Target:** Recover one or more primary studies establishing transcript-level markers, neuropeptide profile, or developmental-origin features for the radiatum giant cell.
  **Expected output:** LiteratureEvidence items + DEFINING_MARKER / NEUROPEPTIDE entries on the classical node.
  **Resolves:** Open question 1.

- **What:** Re-analysis of any public single-cell or single-nucleus hippocampal dataset that retains soma-position metadata at sub-layer resolution, looking for a population matching CA1 stratum radiatum somata with CA1-ProS Glut_1 identity.
  **Target:** Identify a transcriptomic signature that distinguishes 0262 CA1-ProS Glut_1 from siblings 0261, 0263, 0269 CA1-ProS Glut_1 and that can be tested against radiatum-giant-cell soma position.
  **Expected output:** New evidence items on the SUPT_0069 and CLUS_0262 edges.
  **Resolves:** Open questions 1 and 2.

### Open questions

1. No primary or transcriptomic characterisation of the CA1 radiatum giant cell has yet been entered in the KB; markers and neuropeptide profile are unknown.
2. Among the four CA1-ProS Glut_1 children of supertype 0069, no available evidence selects one over the others; the 0262 call is a location-proximity tie-breaker and not a biological identification.
3. Per GH #80, two prior mapping edges to CS20230722_CLUS_0261 and CS20230722_SUPT_0069 were proposed on after_merge_20260508 and deferred during the PR #79 hippocampus port. The Stage A/B emission on 2026-06-10 generated a fresh top-K candidate set under proximity-aware scoring; curator should review whether the deferred candidates remain relevant or are superseded.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| 1 | Kirson & Yaari 2000 | [10864941](https://pubmed.ncbi.nlm.nih.gov/10864941) | soma location, NT type, electrophysiology |

---

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0069 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Soma-location concordance to Field CA1 places the CA1
    radiatum giant cell within CS20230722_SUPT_0069 (region_fraction_100um=0.93;
    strict region_fraction=0.23); NT assertion is absent at rank 1 but Glut on
    all assessed children. Absent classical-side defining markers, the
    supportable call is at supertype level (1:n across the four CA1-ProS Glut_1
    children CS20230722_CLUS_0261, CS20230722_CLUS_0262, CS20230722_CLUS_0263,
    CS20230722_CLUS_0269).
  reconciliation_note: >
    Paired with the best-child call on CS20230722_CLUS_0262
    (edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0262, skos:closeMatch +
    1:1) — the supertype broadMatch covers the distribution across CA1-ProS
    Glut_1 children, while the cluster closeMatch records the highest-
    proximity child as a tentative best alignment.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No defining molecular markers, negative markers, or neuropeptides are
        currently entered for the CA1 radiatum giant cell; mapping rests on
        soma location and broad NT class only.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Atlas soma-position records CA1 pyramidal layer dominance on
        CS20230722_SUPT_0069; classical soma is in stratum radiatum, an
        adjacent CA1 layer not separately registered at this resolution.
    - caveat_type: OTHER
      description: >
        nt_type is not asserted on CS20230722_SUPT_0069 (rank 1); Glut identity
        is inherited from the child clusters CS20230722_CLUS_0261,
        CS20230722_CLUS_0262, CS20230722_CLUS_0263, CS20230722_CLUS_0269.
  proposed_experiments:
    - >
      Targeted literature trawl for transcriptomic, neuropeptide, or TF
      characterisation of the CA1 radiatum giant cell; expected output:
      LiteratureEvidence on the classical node with DEFINING_MARKER /
      NEUROPEPTIDE entries that can be tested against atlas children of
      CS20230722_SUPT_0069.
    - >
      Re-analysis of public hippocampal single-cell datasets retaining
      sub-layer soma position, to identify any transcript-level signature
      that distinguishes one CA1-ProS Glut_1 child cluster (CS20230722_CLUS_0261,
      CS20230722_CLUS_0262, CS20230722_CLUS_0263, CS20230722_CLUS_0269) as
      a stratum-radiatum-resident population.
  unresolved_questions:
    - >
      No primary transcriptomic characterisation of the CA1 radiatum giant
      cell is in the KB; markers and neuropeptide profile are unknown.
    - >
      Among the four CA1-ProS Glut_1 children of CS20230722_SUPT_0069, no
      available evidence selects one over the others.
    - >
      Per GH #80, two prior mapping edges to CS20230722_CLUS_0261 and
      CS20230722_SUPT_0069 were proposed on after_merge_20260508 and deferred
      during the PR #79 hippocampus port. The Stage A/B emission on
      2026-06-10 generated a fresh top-K candidate set under proximity-aware
      scoring; curator should review whether the deferred candidates remain
      relevant or are superseded.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0262 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.45
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0262 has the highest CA1 proximity of any
    rank-0 candidate (region_fraction_100um=0.97; strict region_fraction=0.27)
    and is annotated Glut, consistent with the classical glutamatergic
    identity. Selected as the tentative best child within the primary
    supertype call (CS20230722_SUPT_0069) on location-proximity alone, given
    the absence of classical-side defining markers.
  reconciliation_note: >
    Paired with the supertype broadMatch on CS20230722_SUPT_0069
    (edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0069, skos:broadMatch +
    1:n) — this child-cluster closeMatch is provisional and should be
    re-assessed if any classical-side defining marker is established that
    distinguishes CS20230722_CLUS_0262 from siblings CS20230722_CLUS_0261,
    CS20230722_CLUS_0263, CS20230722_CLUS_0269.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Selection of CS20230722_CLUS_0262 over the three sibling CA1-ProS
        Glut_1 children rests on location proximity only; no transcript or
        protein markers are available on the classical side to discriminate.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Atlas soma-position on CS20230722_CLUS_0262 is dominated by Field CA1,
        pyramidal layer; classical soma is in CA1 stratum radiatum (adjacent
        layer not separately registered).
  proposed_experiments:
    - >
      A transcriptomic signature distinguishing CS20230722_CLUS_0262 from
      CS20230722_CLUS_0261, CS20230722_CLUS_0263, and CS20230722_CLUS_0269
      that can be tested against CA1 radiatum giant cells (e.g. via
      sub-layer-resolved soma position or any targeting strategy that
      labels radiatum giant cells specifically).
  unresolved_questions:
    - >
      Selection of CS20230722_CLUS_0262 among CA1-ProS Glut_1 children is a
      tie-breaker on location proximity, not a biological identification.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0263 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0263 is a sibling CA1-ProS Glut_1 child of
    CS20230722_SUPT_0069 with region_fraction_100um=0.93; covered by the
    supertype broadMatch and not preferred over CS20230722_CLUS_0262 in the
    absence of classical-side markers to discriminate.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0269 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0269 is a sibling CA1-ProS Glut_1 child of
    CS20230722_SUPT_0069 with region_fraction_100um=0.92; covered by the
    supertype broadMatch and not preferred in the absence of discriminating
    markers.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0261 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_CLUS_0261 is a small (n=215) CA1-ProS Glut_1 child
    of CS20230722_SUPT_0069 with region_fraction_100um=0.56 leaning to CA1
    stratum oriens rather than the classical stratum radiatum location;
    weaker proximity than the best-child CS20230722_CLUS_0262.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_CLUS_0271 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0271 sits under CS20230722_SUPT_0070 (a
    different CA1-ProS Glut supertype from the primary supertype call),
    with region_fraction_100um=0.57 leaning to Field CA1 stratum oriens;
    outside the supertype that best covers the classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0072 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    [tier:CUT] CS20230722_SUPT_0072 (0072 CA1-ProS Glut_4) has Field CA1
    soma dominance (region_fraction_100um=0.87) but is not the supertype
    of the primary cluster cohort; no positive evidence selects it over
    CS20230722_SUPT_0069 and NT is not asserted at rank 1.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0070 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] CS20230722_SUPT_0070 (0070 CA1-ProS Glut_2) shows
    region_fraction_100um=0.68 with Field CA1 stratum oriens as the
    dominant sub-region; oriens-leaning soma distribution argues against
    a stratum-radiatum classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0074 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0074 (0074 CA1-ProS Glut_6) has
    region_fraction_100um=0.65 with Prosubiculum count_100um=1062
    contributing substantially to the rollup; prosubiculum-leaning soma
    distribution is inconsistent with a CA1 stratum radiatum classical
    type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca1_radiatum_giant_cell_to_CS20230722_SUPT_0100 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0100 (0100 CA2-FC-IG Glut_1) is dominated by
    Field CA3 cells (region_fraction_100um=0.56; strict region_fraction=0.09)
    and represents a CA2-FC-IG context rather than CA1; not a candidate for
    the CA1 radiatum giant cell.
```
<!-- verdict-block-end -->
