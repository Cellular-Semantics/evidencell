# PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Introduction

### Classical type

**PVN corticotropin-releasing factor receptor 1 (CRFR1) neuron** is defined neurochemically by
expression of CRFR1 (Crhr1) and obligate co-expression of estrogen receptor alpha (Esr1, moderate)
and androgen receptor (Ar, high). Somas are concentrated in the paraventricular hypothalamic
nucleus (PVN). The population is male-biased (males > females), with the sex difference emerging
during puberty/early adulthood and persisting into old age; adult gonadectomy in males (but not
females) reduces CRFR1-immunoreactive cell counts, indicating gonadal-hormone-dependent
regulation. Characterisation rests on a single primary source (Rosinger 2019).

CL term: **corticotropin-releasing neuron (CL:4072021)** — mapping is RELATED only. CL:4072021
defines neurons by CRH *secretion*, while this node is defined by CRFR1 *receptor* expression.
No exact CL term exists; this is a candidate for a new term.

| Property | Value | References |
|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | [1] |
| Defining markers | Crhr1 (transcript), Esr1 (transcript, moderate co-expression), Ar (transcript, high co-expression) | [1] |
| CL term | CL:4072021 (corticotropin-releasing neuron) — RELATED only | |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[1] Rosinger et al. 2019 · PMID:31055007 — Soma location, Crhr1/Esr1/Ar markers, sex dimorphism**

> Sex differences in neural structures are generally believed to underlie sex differences reported in anxiety, depression, and the hypothalamic-pituitary-adrenal axis, although the specific circuitry involved is largely unclear. Using a corticotropin-releasing factor receptor 1 (CRFR1) reporter mouse line, we report a sexually dimorphic distribution of CRFR1 expressing cells within the paraventricular hypothalamus (PVN; males > females). Relative to adult levels, PVN CRFR1-expressing cells are sparse and not sexually dimorphic at postnatal days 0, 4, or 21. This suggests that PVN cells might recruit CRFR1 during puberty or early adulthood in a sex-specific manner. The adult sex difference in PVN CRFR1 persists in old mice (20-24 months). Adult gonadectomy (6 weeks) resulted in a significant decrease in CRFR1-immunoreactive cells in the male but not female PVN. CRFR1 cells show moderate co-expression with estrogen receptor alpha (ERα) and high co-expression with androgen receptor, indicating potential mechanisms through which circulating gonadal hormones might regulate CRFR1 expression and function. Finally, we demonstrate that a psychological stressor, restraint stress, induces a sexually dimorphic pattern of neural activation in PVN CRFR1 cells (males >females) as assessed by co-localization with the transcription/neural activation marker phosphorylated CREB. Given the known role of CRFR1 in regulating stress-associated behaviors and hormonal responses, this CRFR1 PVN sex difference might contribute to sex differences in these functions.
> — Rosinger et al. 2019, Introduction · [1] <!-- quote_key: 143424909_2b990710 -->

</details>

---

## Results

### Mapping candidates

One mapping edge is recorded for pvn_crfr1_neuron: a supertype-level edge to SUPT_0585
(0585 PVH-SO-PVa Otp Glut_1), the highest rank-1 candidate by DB score (=3) among PVN-localised
supertypes.

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] | (self) | 183 | 🟡 MODERATE | Esr1 APPROXIMATE; Ar APPROXIMATE; Crhr1 APPROXIMATE (low) | Best candidate |
1 edge total. Relationship type: PARTIAL_OVERLAP.

### Property alignment — primary candidate (SUPT_0585)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Paraventricular hypothalamic nucleus [MBA:38] | MBA:38 (PVN) n=98 (primary location) | not assessed | CONSISTENT |
| NT type | not stated; PVN principal neurons predominantly glutamatergic | Glutamatergic (PVH-SO-PVa Otp Glut) | not assessed | CONSISTENT |
| Crhr1 expression | POSITIVE (transcript, primary defining marker) | precomputed mean_expression=0.84 | not assessed | APPROXIMATE |
| Esr1 expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=3.65 (DEFINING_SCOPED atlas marker) | not assessed | APPROXIMATE |
| Ar expression | POSITIVE (transcript, defining marker) | precomputed mean_expression=4.95 | not assessed | APPROXIMATE |
| Sex ratio | MALE_BIASED (males > females; emerges at puberty; gonadectomy-sensitive in males) | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| SUPT_0585 atlas metadata (PVN n=98; Crhr1/Esr1/Ar; rank-1 DB score=3) | Atlas metadata | PARTIAL | MBA:38 n=98; Crhr1=0.84; Esr1=3.65 (DEFINING_SCOPED); Ar=4.95; Crh=2.5 | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments. Note: rank-0 candidate CLUS_2382, child of SUPT_0589, has male_female_ratio=2.7 consistent with male-biased dimorphism, suggesting SUPT_0589 is an alternative or co-equal mapping target.)*

---



### 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] · 🟡 MODERATE

### Supporting evidence

- **Direct PVN soma location match.** SUPT_0585 (PVH-SO-PVa Otp Glut_1) has Paraventricular
  hypothalamic nucleus [MBA:38] as its primary location with n=98 cells, providing CONSISTENT
  anatomical alignment with the classical node's PVN soma criterion [1].
- **Steroid hormone receptor co-expression strongly supported.** Precomputed mean expression
  Esr1=3.65 (a DEFINING_SCOPED atlas marker for SUPT_0585) and Ar=4.95 directly support the
  classical node's defining estrogen receptor alpha (moderate) and androgen receptor (high)
  co-expression profile. The relative magnitudes — Ar > Esr1 — are consistent with the
  "high androgen receptor / moderate ERα" pattern reported in [1].
- **Glutamatergic identity is concordant.** The supertype carries a Glut label (PVH-SO-PVa Otp
  Glut), consistent with the predominantly glutamatergic phenotype expected of PVN principal
  neurons. The classical node does not specify NT type, but glutamatergic identity is the
  expected default for non-magnocellular PVN populations *(note: NT type not stated in [1];
  glutamatergic is inferred from regional convention and the supertype Otp Glut label.)*
- **Crh expression confirms PVN neuroendocrine identity.** Precomputed mean Crh = 2.5 within
  SUPT_0585 confirms the supertype is part of the PVN CRH/neuroendocrine network, the expected
  context in which CRFR1+ cells reside.
- **Highest DB score among rank-1 candidates.** SUPT_0585 was selected as the best candidate
  by DB score = 3, the highest among rank-1 PVN-localised supertypes.

### Marker evidence provenance

- **Crhr1** — classical node evidence is from a CRFR1 reporter mouse line (transgenic
  fluorescent reporter; protein-level cell counting) [1], with co-expression confirmed by
  immunofluorescence (CRFR1-IR cells). Atlas precomputed Crhr1 = 0.84 is transcript-based
  (10x Chromium). The atlas value is low — consistent with CRFR1+ neurons being a *subset*
  of SUPT_0585 rather than the entire supertype. *(note: this is the expected pattern when a
  classical type is defined by a sparsely expressed receptor whose protein is detectable by
  reporter line but whose transcript is diluted across a heterogeneous transcriptomic
  supertype.)* No data-source contradiction; the discrepancy reflects scope, not absence.
- **Esr1** — classical node evidence is protein-level (ERα immunoreactivity co-localisation
  with CRFR1) [1]. Atlas precomputed Esr1 = 3.65 is transcript-based and listed as a
  DEFINING_SCOPED atlas marker for SUPT_0585. Strong cross-modal agreement.
- **Ar** — classical node evidence is protein-level (androgen receptor immunoreactivity
  co-localisation with CRFR1, "high" co-expression) [1]. Atlas precomputed Ar = 4.95 is
  transcript-based and is the highest of the three steroid-related markers, in agreement with
  the "high" qualitative ranking in [1]. Strong cross-modal agreement.
- **Single-source caveat.** All three defining markers (Crhr1, Esr1, Ar) and the soma location
  are sourced from a single primary study (Rosinger 2019, PMID:31055007). Marker provenance is
  internally consistent but lacks independent literature replication.

### Concerns

- **Crhr1 expression is low at supertype level (APPROXIMATE).** Precomputed mean Crhr1 = 0.84
  indicates CRFR1+ neurons are a minority subset of SUPT_0585. Mapping at supertype resolution
  averages the CRFR1 signal across many cells, most of which may not express Crhr1.
  Cluster-level resolution would be required to identify the specific Crhr1-enriched
  subpopulation. *(weak counter-evidence — expected pattern for a subset-defining marker.)*
- **Sex ratio not available at supertype level.** Male-biased sex dimorphism — a defining
  feature of pvn_crfr1_neuron [1] — cannot be assessed from supertype-level metadata
  (male_female_ratio is computed only at rank 0). The rank-0 candidate CLUS_2382 (parent
  SUPT_0589, *not* SUPT_0585) shows male_female_ratio = 2.7, consistent with male-biased
  dimorphism — raising the possibility that SUPT_0589 is a better or co-equal mapping target.
- **Alternative supertype (SUPT_0589) not yet assessed in detail.** Because the male-biased
  child cluster CLUS_2382 belongs to SUPT_0589 rather than SUPT_0585, curator review is needed
  to determine whether SUPT_0589 should be added as a co-equal or preferred mapping edge.
- **Single-dataset characterisation.** All classical-node evidence is from Rosinger 2019
  (PMID:31055007). Confidence is capped at MODERATE pending secondary literature validation.
- **Annotation transfer NOT_ASSESSED.** No independent, data-driven cell-level mapping of
  CRFR1+ PVN cells to WMBv1 has been run.

### What would upgrade confidence

- **Child-cluster expression analysis of SUPT_0585** to identify the specific cluster(s)
  combining peak Crhr1 expression with male-biased sex ratio (male_female_ratio > 1) would
  resolve unresolved question 1 and clarify whether the CRFR1 subset is concentrated in one
  child cluster. Expected output: refined `MappingEdge` at cluster level with stronger
  Crhr1 alignment and (where MFR is available) CONSISTENT sex-ratio support.
- **Comparative assessment of SUPT_0589** (parent of male-biased CLUS_2382, MFR=2.7) against
  SUPT_0585 to determine whether SUPT_0589 is a better or co-equal mapping target. Expected
  output: an additional `MappingEdge` to SUPT_0589 with property comparisons documenting the
  sex-ratio agreement.
- **MapMyCells annotation transfer** of an external CRFR1-reporter or Crhr1+ FACS-sorted PVN
  scRNA-seq dataset against WMBv1 at cluster resolution; F1 ≥ 0.50 at the supertype level
  would upgrade this edge. Expected output: `AnnotationTransferEvidence`.
- **Targeted cite-traverse** for primary studies independently profiling PVN Crhr1+ neurons
  (scRNA-seq, RNAscope, or alternative reporter lines) would address the SINGLE_DATASET caveat
  and could promote confidence beyond MODERATE.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** See classical type table in Introduction; defining_basis on the classical node and per-property literature support are listed there. The KB-side definition lives at the source graph file linked in the reproducibility footer.

**Atlas mapping query.** Candidate atlas clusters were retrieved from CCN20230722 at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property was compared to the corresponding atlas-side value via the `property_comparisons` schema; alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.



**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `0c97cfa` from [`kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`](../../kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** → 0585 PVH-SO-PVa Otp Glut_1 [CS20230722_SUPT_0585] at MODERATE confidence. Key support: ATLAS_METADATA (PVN/SO/PVa anatomy match; Otp Glut subclass consistent with neuroendocrine PVN identity). Key caveats: `MARKER_NOT_SPECIFIC` (Crhr1 expression not directly resolvable in atlas metadata).

No Cell Ontology term currently assigned for this classical type.

### Proposed experiments and follow-ups

### 1. Child-cluster expression analysis of SUPT_0585 (and SUPT_0589) for Crhr1 and male-biased MFR

**What:** For each child cluster of SUPT_0585 and SUPT_0589, retrieve precomputed
mean_expression for Crhr1, Esr1, Ar, and male_female_ratio. Identify cluster(s) with peak
Crhr1 combined with MFR > 1.

**Target:** At least one cluster with Crhr1 ≥ supertype mean and MFR ≥ 1.5 (male-biased).

**Expected output:** A refined `MappingEdge` at cluster level (rank 0) with stronger
Crhr1 alignment and CONSISTENT sex-ratio support.

**Resolves:** Open questions 1 and 2.

### 2. MapMyCells annotation transfer of an external CRFR1+ PVN scRNA-seq dataset against WMBv1

**What:** Retrieve a published scRNA-seq dataset enriched for PVN CRFR1+ neurons
(e.g., Crhr1-Cre or CRFR1-reporter sorted preparations, sex-stratified). Run MapMyCells
against WMBv1 at cluster resolution.

**Target:** F1 ≥ 0.50 at SUPT_0585 (or SUPT_0589) level; F1 ≥ 0.80 at the best child cluster.

**Expected output:** `AnnotationTransferEvidence` entry on the edge, atlas: WMBv1, tool:
MapMyCells, output: F1 matrix per cluster.

**Resolves:** The annotation_transfer_f1 NOT_ASSESSED gap and questions 1–2.

### 3. Targeted cite-traverse for secondary literature on PVN Crhr1+ neurons

**What:** Run a `cite-traverse` skill query for primary studies independently profiling PVN
Crhr1+ neurons (scRNA-seq, RNAscope, alternative reporter lines, or sex-stratified
characterisations).

**Target:** At least one independent primary study (non-Rosinger) describing PVN Crhr1+
neuron molecular profile or sex dimorphism.

**Expected output:** Additional `LiteratureEvidence` entries; lifts the SINGLE_DATASET caveat
and could support upgrading confidence beyond MODERATE.

**Resolves:** SINGLE_DATASET caveat.

---

### Open questions

1. Which cluster within the PVH-SO-PVa Otp Glut subclass shows highest Crhr1 expression
   combined with male-biased sex ratio?
2. Is SUPT_0589 a better or co-equal mapping target compared to SUPT_0585? *(The rank-0
   candidate CLUS_2382, with male_female_ratio = 2.7 consistent with male-biased dimorphism,
   is a child of SUPT_0589 rather than SUPT_0585.)*

---

### Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_pvn_crfr1_neuron_to_cs20230722_supt_0585 | ATLAS_METADATA | PARTIAL — MBA:38 PVN n=98 (primary); Crhr1=0.84 (low, subset); Esr1=3.65 (DEFINING_SCOPED); Ar=4.95; Crh=2.5; rank-1 DB score=3 |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rosinger et al. 2019 | [PMID:31055007](https://pubmed.ncbi.nlm.nih.gov/31055007/) | Soma location (PVN); Crhr1, Esr1, Ar markers; male-biased sex dimorphism; gonadectomy and stress-activation findings |
