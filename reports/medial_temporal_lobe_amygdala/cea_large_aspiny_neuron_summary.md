# Central amygdala large aspiny neuron — CCN20230722 Mapping Report
*Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala large aspiny neuron is one of three morphologically defined neuronal classes in the central nucleus of the amygdala [UBERON:0002883], distinguished by large soma size and thick, aspiny primary dendrites that branch into secondary processes with sparse spines. This type was originally delineated alongside medium spiny and small aspiny neurons using classical histological and Golgi methods. Establishing a transcriptomic atlas correspondence for this type matters because the CeA is a major output hub for fear, pain, and autonomic circuits, and disaggregating its morphological classes into molecularly defined clusters would open access to Cre-line tools and projection targeting strategies.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | [1] |
| Neurotransmitter | GABAergic | [2] |
| Defining markers | None recorded | — |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Morphology | Large soma; thick aspiny primary dendrites; secondary processes seldom spiny | [1] |
| Definition basis | CLASSICAL | — |
| Notes | Classical morphological class described alongside medium spiny and small aspiny neurons | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / Morphology:** Morphological description from review of CeA cell types · [1]

  > "Morphologically, there are several types of neurons located in the central nucleus of the amygdala (CeA). In the lateral sector of the central nucleus, a predominant cell type with ovoid soma is located. These cells have several primary nonspiny dendrites, branching onto spiny secondary and tertiary dendrite. Their axons begin branching even before leaving the nucleus, which is why these cells are called "medium spiny neurons" (Hall, 2004)(McDonald, 1982). Another type of neurons located in the central nuclei have big soma with thick aspiny dendrites, branching on to secondary seldom spiny processes (McDonald, 1982)(Cassell et al., 1989) (Schiess et al., 1999). The third type of cells are small aspiny neurons (Cassell et al., 1989)"
  > — Nikolenko et al. 2020, Central amygdala cell types · [1] <!-- quote_key: 220976356_f1fe3fe1 -->

- **Neurotransmitter:** CeA neurons described as predominantly GABAergic based on their subpallial, striatal-like organisation · [2]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

**Null result.** A scan of CCN20230722 at rank 0 (cluster) within the GABAergic-CeA cohort confirmed that no candidate cluster can be positively mapped to the central amygdala large aspiny neuron: no molecular markers are defined for this type, all five surviving candidates scored identically (score = 1, region filter only), and the returned candidate pool is identical to that returned for `cea_medium_spiny_neuron` and `cea_small_aspiny_neuron`. One edge was retained at UNCERTAIN confidence as a placeholder; it carries no positive mapping evidence.

A complete scan of CCN20230722 (rank 0) at MBA:536 (Central amygdalar nucleus) with a GABAergic filter produced a survival cohort of 5 clusters, all scoring identically. CS20230722_CLUS_0705 ("RHP-COA Ndnf Gaba_6") appeared at rank 2 of 5 in cohort ordering with a region_fraction of 0.014. This is not positive evidence for the mapping — the selection is rank-order only among ties, not a biological signal.

### Mapping candidates overview

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0705 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0705] | 0198 RHP-COA Ndnf Gaba_6 | 61 | ⚪ UNCERTAIN | NT CONSISTENT; region filter only; no markers | Eliminated |

*1 edge assessed; all UNCERTAIN. Relationship type: evidencell:UncertainRelationship.*

---

## Eliminated candidates

All candidates in the CeA GABAergic cohort share an identical disqualifying signal: no molecular markers are defined on `cea_large_aspiny_neuron`, making every candidate equally uninformative. The score-1 result reflects a region filter contribution only — it is not evidence of identity.

### CS20230722_CLUS_0705 ("RHP-COA Ndnf Gaba_6") ⚪ UNCERTAIN

- NT type comparison: GABAergic (classical) vs. GABA (atlas label) — CONSISTENT, but NT consistency is uninformative here because all five CeA cohort clusters are GABAergic.
- Location comparison: UBERON:0002883 classical vs. MBA:536 CeA present at region_fraction 0.014 — CONSISTENT in kind but very low fraction (rank 2 of 5 in cohort), suggesting CeA is a minor component of this cluster.
- Morphology / markers: NOT_ASSESSED — WMBv1 provides no morphological or electrophysiological annotations; no molecular markers are defined on the classical node to test against atlas expression.
- Discovery score = 1, cohort_size = 5, all five candidates tied at score = 1. CLUS_0705 is assigned rank 2 by cohort ordering only.
- ATLAS_METADATA evidence: NO_EVIDENCE — selected by region filter only; no expression markers matched.

**Shared caveat across all three CeA morphological types:** The candidate pool for `cea_large_aspiny_neuron` is identical to the candidate pools for `cea_medium_spiny_neuron` and `cea_small_aspiny_neuron`. All three classical morphological classes are transcriptomically indistinguishable with currently available evidence; no molecular markers separate them.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The central amygdala large aspiny neuron is defined on a CLASSICAL basis — morphological description from Golgi and light-microscopic studies. Defining features are large soma and thick aspiny primary dendrites (Nikolenko et al. 2020 [1]; citing McDonald 1982, Cassell et al. 1989, Schiess et al. 1999). The NT type (GABAergic) follows from the general CeA striatal-like organisation documented by Yeh et al. 2024 [2]. No molecular markers, neuropeptides, or electrophysiological properties are recorded on this node; definition_basis = CLASSICAL.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.** CCN20230722 taxonomy; pseudobulk source and SHA-256 not populated in this edge's metadata.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_large_aspiny_neuron_to_cs20230722_clus_0705 | LITERATURE; ATLAS_METADATA | PARTIAL; NO_EVIDENCE | [1]; atlas-internal |

*Generated by evidencell `8d79cdb` at 2026-06-11T09:44:20+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Central amygdala large aspiny neuron → CS20230722_CLUS_0705 at UNCERTAIN confidence. Key support: none — region filter only. Key caveats: NO_DISCRIMINATING_MARKER (no molecular markers defined on the classical node); AMBIGUOUS_MAPPING (identical candidate pool to `cea_medium_spiny_neuron` and `cea_small_aspiny_neuron`).

No Cell Ontology term currently assigned. This type lacks molecular definition and is a candidate for CL contribution if molecular identity is established.

### Proposed experiments and follow-ups

**Patch-seq of morphologically identified large aspiny CeA neurons**
- **What:** Whole-cell patch-clamp with post-hoc biocytin fill and morphological reconstruction, followed by single-cell RNA-seq (patch-seq) to simultaneously profile morphology, electrophysiology, and transcriptome.
- **Target:** WMBv1 cluster assignment with sufficient cells (at least 10 morphologically confirmed large aspiny neurons) to identify the corresponding atlas cluster unambiguously.
- **Expected output:** Defining molecular markers for `cea_large_aspiny_neuron`; AnnotationTransferEvidence linking to a specific WMBv1 cluster; a property_comparison entry for morphology_aspiny_large.
- **Resolves:** edge_cea_large_aspiny_neuron_to_cs20230722_clus_0705 (upgrades from UNCERTAIN); disambiguates from `cea_medium_spiny_neuron` and `cea_small_aspiny_neuron`.

**Targeted literature search for CeA large aspiny neuron markers**
- **What:** Cite-traverse for "large aspiny neuron central amygdala" and "CeA interneuron fast-spiking PV" to assess whether any published single-cell studies have characterised this morphological class transcriptomically or linked it to known marker genes.
- **Target:** Identification of at least one defining marker supported by a primary study with confirmed morphology.
- **Expected output:** LiteratureEvidence items with quote_keys; updated `defining_markers` on the classical node if supported.
- **Resolves:** Open question 1 (below).

### Open questions

1. Do large aspiny CeA neurons correspond to the fast-spiking internuncial class described electrophysiologically, and if so, do they share markers with PV or other known fast-spiking interneuron clusters? *(from edge_cea_large_aspiny_neuron_to_cs20230722_clus_0705)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nikolenko et al. 2020 | [32751957](https://pubmed.ncbi.nlm.nih.gov/32751957/) | Soma location; morphological class definition |
| [2] | Yeh et al. 2024 | [38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | Neurotransmitter type (CeA GABAergic) |

---

<!-- verdict-block-start: edge_cea_large_aspiny_neuron_to_cs20230722_clus_0705 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    No molecular markers are defined on cea_large_aspiny_neuron; discovery returned
    score 1 for all 5 candidates in the GABAergic-CeA cohort (cohort_size=5,
    rank_in_cohort=2, all tied at score=1). CS20230722_CLUS_0705 was selected by
    region filter only (region_fraction=0.014 at MBA:536; region_evidence=SELF).
    NT type is CONSISTENT (GABAergic/GABA) but uninformative given all cohort
    members are GABAergic. Soma/dendrite comparison (aspiny large form) is
    NOT_ASSESSED — WMBv1 provides no soma/dendrite annotations. The ATLAS_METADATA
    evidence item explicitly records NO_EVIDENCE. The candidate pool is identical to
    cea_medium_spiny_neuron and cea_small_aspiny_neuron; the three CeA soma-defined
    types are transcriptomically indistinguishable without molecular markers.
  reconciliation_note: >
    Indistinguishable from cea_medium_spiny_neuron and cea_small_aspiny_neuron
    across all available panels (no markers, identical region filter, no AT data);
    all three return the same 5-member GABAergic-CeA candidate pool at score=1.
    Patch-seq of histologically confirmed cells is the only path to resolution.
  unresolved_questions:
    - >
      Do large aspiny CeA neurons correspond to the fast-spiking internuncial class
      described electrophysiologically, and if so, do they share markers with PV or
      other known fast-spiking interneuron clusters?
```
<!-- verdict-block-end -->
