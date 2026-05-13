# Ventral premammillary nucleus (PMv) oxytocin receptor neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The ventral premammillary nucleus (PMv) oxytocin-receptor (OTR) neuron is a classically defined neurochemical population in the PMv [MBA:1004]. OTR expression in the PMv is male-biased between P14 and P56 [2], and the PMv itself is a long-established sexually dimorphic hypothalamic nucleus with roles in maternal aggression, reproductive control, and male social behavior [1]. The classical type aggregates marker-defined PMv subpopulations (Oxtr+, Slc6a3+ "PMv-DAT", and Adcyap1+ "PMv-PACAP") whose mutual overlap is not fully resolved, making the mapping to WMBv1 supertype/cluster structure biologically informative for resolving subtype identity.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Ventral premammillary nucleus [MBA:1004] | [1], [2] |
| Defining markers | Oxtr [2]; Slc6a3 [1]; Adcyap1 | [1], [2] |
| Sex bias | Male-biased (PMv OTR expression higher in males, P14–P56) | [2] |
| Definition basis | CLASSICAL_NEUROCHEMICAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** PMv localisation supported by sexually dimorphic OTR expression mapping [2] and broader hypothalamic dimorphism survey [1].
  > Sexual dimorphism of OTR expression. OTR is expressed in a sexually dimorphic manner as a part of neural circuit mechanism to generate behavioral differences in males and females ... The ventral premammillary nucleus (PMv) showed significantly higher OTR expression in males compared to females between P14 and P56
  > — Newmaster et al. 2019, Neuronal Markers and Molecular Characteristics · [2] <!-- quote_key: 201207691_ff444c30 -->

  > We identified two adjacent regions within the hypothalamus that exhibited significant sexual dimorphism. Region 1 overlaps with the anterior hypothalamic nucleus (AHN), while Region 2 primarily overlaps with the ventral premammillary nucleus (PMv). Both regions are known to be sexually dimorphic
  > — Hemminger et al. 2024, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 273240437_ed3a4faa -->

- **Marker Oxtr:** Sexually dimorphic OTR expression characterised in PMv across P14–P56 [2].
- **Marker Slc6a3:** PMv-DAT subpopulation reported in sexually dimorphic PMv neuron survey [1].
  > Previous studies identified sexually dimorphic neuron populations within the PMv (e.g., PMv-DAT, PMv-PACAP), complementing our systematic identification of subclass-level abundance changes.
  > — Hemminger et al. 2024, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 273240437_af6642f9 -->

- **Marker Adcyap1:** Listed without a primary citation on the classical node; PMv-PACAP subpopulation referenced in [1].

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Two candidate atlas entries were assessed (one supertype, one child cluster); both are LOW-confidence speculative mappings, limited by the absence of cluster-level sex-bias data and by ambiguity over whether the classical type's three marker subpopulations (OTR+, DAT+, PACAP+) should be split.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0607 PMv-TMv Pitx2 Glut_3 (supertype) | — | 547 | 🔴 LOW | Oxtr/Slc6a3/Adcyap1 CONSISTENT; sex NOT_ASSESSED | Speculative |
| 2 | 2470 PMv-TMv Pitx2 Glut_3 | 0607 PMv-TMv Pitx2 Glut_3 | 284 | 🔴 LOW | All three markers CONSISTENT (above supertype mean); sex NOT_ASSESSED | Speculative |

Total: 2 edges; CROSS_CUTTING (supertype) and PARTIAL_OVERLAP (cluster) relationships.

### Primary candidate — supertype-level property alignment (SUPT_0607)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | MBA:1004 (PMv) | MBA:1004 (PMv) n=347 (dominant location) | MBA:1004 (PMv) n=192 (CLUS_2470) | CONSISTENT |
| Oxtr | POSITIVE (defining) | mean=2.0 (DEFINING_SCOPED) | mean=4.45 (CLUS_2470) | CONSISTENT |
| Slc6a3 | POSITIVE (defining) | mean=3.07 (DEFINING) | mean=6.02 (CLUS_2470) | CONSISTENT |
| Adcyap1 | POSITIVE (defining) | mean=4.8 | mean=8.13 (CLUS_2470) | CONSISTENT |
| NT type | Not specified; DAT+ implies dopaminergic co-release | Glutamatergic (PMv-TMv Pitx2 Glut) | Glutamatergic (CLUS_2470) | APPROXIMATE |
| Sex ratio | Male-biased | not available | MFR absent from DB (CLUS_2470) | NOT_ASSESSED |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (SUPT_0607) | Atlas metadata | SUPPORT | Highest DB score (4); Oxtr=2.0, Slc6a3=3.07, Adcyap1=4.8 | atlas-internal |
| Atlas precomputed expression (CLUS_2470) | Atlas metadata | SUPPORT | Oxtr=4.45, Slc6a3=6.02, Adcyap1=8.13; PMv n=192 | atlas-internal |

*(Of the supertype's child clusters, CLUS_2470 (n=192 PMv cells) shows all three classical markers substantially above supertype mean and is the best match. CLUS_2473 (n=86 PMv cells) has mild male-biased MFR=2.23 but very low marker expression, indicating it is a distinct PMv subtype rather than the OTR+ population. Best match: CLUS_2470.)*

### 0607 PMv-TMv Pitx2 Glut_3 · 🔴 LOW

**Supporting evidence**

- SUPT_0607 received the highest DB score (4) of any candidate at any rank for `pmv_otr_neuron`; MBA:1004 (PMv) is the dominant soma location (n=347 cells).
- All three classical defining markers are present on the supertype: Oxtr=2.0 (DEFINING_SCOPED), Slc6a3=3.07 (DEFINING), Adcyap1=4.8.
- The supertype simultaneously expresses all three markers corresponding to the potentially distinct PMv subpopulations (PMv-OTR, PMv-DAT, PMv-PACAP).

**Marker evidence provenance**

- **Oxtr:** Transcript-level evidence from Newmaster et al. 2019 [2] via an OTR-Venus reporter across postnatal development. Cell-type specificity is at the regional level (PMv), not at single-cell resolution; co-localisation with Slc6a3/Adcyap1 in individual PMv neurons is not established by the cited source.
- **Slc6a3:** Cited from Hemminger et al. 2024 [1], which references prior identification of a PMv-DAT subpopulation but does not itself test single-cell co-localisation with Oxtr.
- **Adcyap1:** Listed without a primary citation on the classical node; the PMv-PACAP subpopulation is mentioned in [1] but no primary study is referenced on the KB node. Targeted literature search for "PACAP PMv hypothalamus" recommended.
- **Atlas annotation vs. expression cross-check:** Oxtr (mean=2.0) and Slc6a3 (mean=3.07) are listed as DEFINING_SCOPED / DEFINING atlas markers and have non-trivial precomputed expression — consistent. Adcyap1 (mean=4.8) is high and supports the assignment. No annotation/expression discrepancy at supertype level.

**Concerns**

- **AMBIGUOUS_MAPPING:** SUPT_0607 expresses all three marker signatures simultaneously, indicating the supertype aggregates neurons the classical taxonomy may treat as distinct subtypes (PMv-OTR vs PMv-DAT vs PMv-PACAP). Sister supertype SUPT_0605 (PMv-TMv Pitx2 Glut_1, DB score=2) may capture an additional portion of the OTR+ male-biased population.
- **MARKER_NOT_SPECIFIC:** Tac1 is the highest-expressing DEFINING marker in SUPT_0607 (mean=8.95) but is absent from the classical `pmv_otr_neuron` definition. SUPT_0607 may be more accurately characterised as a Tac1+ PMv population with OTR/DAT/PACAP as co-expressed subtype markers.
- **NT type APPROXIMATE:** The atlas labels SUPT_0607 as glutamatergic; this is likely correct for OTR+ and PACAP+ subpopulations but dopaminergic co-release is possible for the Slc6a3+ subset, which is not reflected in the supertype-level NT annotation.
- **Sex ratio NOT_ASSESSED:** Male bias is the classical type's key discriminator but MFR is absent from the DB at supertype level and for the best child cluster CLUS_2470. *(Source-side confirmed at regional level [2]; target-side still unresolvable from atlas metadata.)*

**What would upgrade confidence**

- Query precomputed HDF5 directly for CLUS_2470 male_female_ratio to determine whether MFR is missing from DB ingest or genuinely absent in the precomputed stats.
- MapMyCells annotation transfer (target F1 ≥ 0.5 at SUPERTYPE level; ≥ 0.7 at CLUSTER) using a published PMv scRNA-seq dataset or Oxtr-Cre / Slc6a3-Cre lineage-targeted data, yielding AnnotationTransferEvidence on the SUPT_0607 / CLUS_2470 edges.
- Query Oxtr, Slc6a3, Adcyap1, and Tac1 expression across all child clusters of SUPT_0607 to determine whether the marker subpopulations resolve at cluster level.
- Targeted literature search for a primary Adcyap1/PACAP PMv reference to strengthen the classical node's marker citations.

### 2470 PMv-TMv Pitx2 Glut_3 · 🔴 LOW

**Supporting evidence**

- CLUS_2470 is the child cluster of SUPT_0607 with PMv (MBA:1004) as primary soma — n=192 cells, the largest PMv subset within the supertype.
- All three defining markers are substantially enriched above supertype mean: Oxtr=4.45 (vs SUPT 2.0), Slc6a3=6.02 (vs 3.07), Adcyap1=8.13 (vs 4.8). The cluster concentrates the marker-expressing PMv cells of SUPT_0607.

**Marker evidence provenance**

- Marker provenance is inherited from the classical node as for SUPT_0607 above. Quantitative cross-check at cluster level confirms strong co-enrichment of Oxtr, Slc6a3, and Adcyap1, but does not establish single-cell co-localisation (which would distinguish a single triple-positive population from three intermixed marker-defined subpopulations within the cluster).

**Concerns**

- **Sex bias unconfirmed at cluster level:** Classical type is MALE_BIASED [2] but MFR is absent from the DB for CLUS_2470 despite n=192 cells. The absent MFR may reflect a DB ingest gap rather than a genuine absence in the precomputed stats. Confidence capped at LOW until this is resolved.
- **AMBIGUOUS_MAPPING (cluster-level):** CLUS_2470 co-expresses Oxtr, Slc6a3, and Adcyap1 at levels suggesting it captures PMv-OTR, PMv-DAT, and PMv-PACAP subpopulations simultaneously. If these are functionally distinct cell types, a single cluster-level edge conflates them; node splitting (pmv_otr, pmv_dat, pmv_pacap) may be required before a higher-confidence cluster assignment can be made.
- A nearby PMv cluster CLUS_2473 (n=86) has MFR=2.23 (mild male bias) but very low marker expression, so it does not constitute a competing OTR-cluster candidate but flags that male-biased PMv cells distribute across multiple molecularly distinct clusters.

**What would upgrade confidence**

- Direct HDF5 query for `male_female_ratio` on CLUS_2470 to recover (or definitively rule out) sex bias data — revised ATLAS_METADATA evidence would follow.
- MapMyCells annotation transfer of a published PMv dataset against WMBv1 (target F1 ≥ 0.7 at CLUSTER level) producing AnnotationTransferEvidence.
- Single-cell co-localisation analysis (Oxtr / Slc6a3 / Adcyap1 multiplex) within CLUS_2470 to determine whether the three markers mark overlapping or distinct cells, resolving whether `pmv_otr_neuron` should be split.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** `pmv_otr_neuron` is defined as a CLASSICAL_NEUROCHEMICAL type with soma in the ventral premammillary nucleus (PMv) [MBA:1004] [1, 2] and three defining markers — Oxtr [2], Slc6a3 [1], and Adcyap1 — corresponding to three reported PMv subpopulations (OTR+, DAT+, PACAP+) whose mutual overlap is not established. NT type is not specified at the classical level; the DAT+ subpopulation implies possible dopaminergic co-release. Sex bias is male-biased between P14 and P56 [2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CS20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:19+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_pmv_otr_neuron_to_cs20230722_supt_0607 | ATLAS_METADATA | SUPPORT | atlas-internal |
| edge_pmv_otr_neuron_to_cs20230722_clus_2470 | ATLAS_METADATA | SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Ventral premammillary nucleus (PMv) oxytocin receptor neuron → 0607 PMv-TMv Pitx2 Glut_3 [CS20230722_SUPT_0607] at LOW confidence, with CLUS_2470 as the best child cluster (also LOW). Key support: atlas precomputed expression showing PMv (MBA:1004) as dominant soma location and strong co-enrichment of all three defining markers (Oxtr, Slc6a3, Adcyap1) at supertype and cluster level. Key caveats: AMBIGUOUS_MAPPING — the supertype/cluster aggregates three reported PMv subpopulations (OTR+, DAT+, PACAP+) whose mutual overlap is not established; MARKER_NOT_SPECIFIC — Tac1 (not in the classical definition) is the highest-expressing DEFINING marker in SUPT_0607; sex bias (the classical type's key discriminator) is NOT_ASSESSED because MFR is absent from the DB for CLUS_2470.

No Cell Ontology term currently assigned. Candidate for a new CL term once the heterogeneity question (single triple-positive PMv neuron vs. three distinct marker-defined subtypes) is resolved.

### Proposed experiments and follow-ups

- **What:** Direct HDF5 query for `male_female_ratio` on CLUS_2470 (and other PMv clusters within SUPT_0607).
  - **Target:** Recover MFR value or definitively confirm absence from the precomputed stats source.
  - **Expected output:** Revised ATLAS_METADATA evidence with sex_ratio alignment graded; if MFR is genuinely absent, a DB-ingest dev-request issue.
  - **Resolves:** Open questions Q1, Q3.

- **What:** MapMyCells annotation transfer using a published PMv scRNA-seq dataset (or Oxtr-Cre / Slc6a3-Cre lineage-targeted data) against WMBv1.
  - **Target:** F1 ≥ 0.5 at SUPERTYPE; F1 ≥ 0.7 at CLUSTER.
  - **Expected output:** AnnotationTransferEvidence on the SUPT_0607 and CLUS_2470 edges.
  - **Resolves:** `annotation_transfer_f1` NOT_ASSESSED on both edges; partial resolution of Q4.

- **What:** Cluster-level marker breakdown query across all child clusters of SUPT_0607 (Oxtr, Slc6a3, Adcyap1, Tac1).
  - **Target:** Determine whether marker subpopulations resolve at cluster level (e.g. distinct Oxtr-high vs Slc6a3-high clusters).
  - **Expected output:** Updated property_comparisons / new edges if subtypes resolve.
  - **Resolves:** Q2.

- **What:** Single-cell co-localisation analysis (multiplex ISH or scRNA-seq inspection) for Oxtr / Slc6a3 / Adcyap1 within CLUS_2470.
  - **Target:** Determine whether the three markers label overlapping or distinct cells in CLUS_2470.
  - **Expected output:** Evidence supporting either retention of `pmv_otr_neuron` as a single node or splitting into pmv_otr, pmv_dat, pmv_pacap.
  - **Resolves:** Q5; AMBIGUOUS_MAPPING caveat.

- **What:** Targeted literature search for primary Adcyap1/PACAP PMv references.
  - **Target:** Primary citation testing Adcyap1 expression in PMv neurons.
  - **Expected output:** LiteratureEvidence and updated `defining_markers[Adcyap1].refs` on the classical node.
  - **Resolves:** Adcyap1 marker provenance gap.

### Open questions

1. Why is MFR absent for CLUS_2470 (n=192 cells)? Is this a DB ingest gap or a genuine absence in precomputed stats?
2. Do individual clusters within SUPT_0607 segregate by marker (Oxtr-high, Slc6a3-high, Adcyap1-high), allowing sub-resolution mapping?
3. Can male bias of the OTR+ PMv population be confirmed at WMBv1 cluster level once MFR is recovered or measured?
4. Will annotation transfer of an external PMv dataset confirm SUPT_0607 / CLUS_2470 as the correct WMBv1 mapping for `pmv_otr_neuron`?
5. Do Oxtr, Slc6a3, and Adcyap1 co-localise within individual CLUS_2470 cells, or do they mark distinct subpopulations within the cluster (i.e. should `pmv_otr_neuron` be split into pmv_otr, pmv_dat, pmv_pacap sub-nodes)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hemminger et al. 2024 | [39416191](https://pubmed.ncbi.nlm.nih.gov/39416191) | soma location |
| [2] | Newmaster et al. 2019 | [32313029](https://pubmed.ncbi.nlm.nih.gov/32313029) | soma location |
