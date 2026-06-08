# Central amygdala corticotropin-releasing factor (CRF) neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

Corticotropin-releasing factor (CRF) neurons of the central amygdala (CeA) are GABAergic inhibitory neurons that express the neuropeptide Crh (CRF/CRH) and contribute to CeA output circuits mediating fear, stress, and autonomic responses. Alongside the PKC-δ (Prkcd) and somatostatin (Sst/SOM) populations, CRF neurons constitute one of the three classical neuropeptide-defined CeA cell classes identified in rodent studies and confirmed in other species [1]. Because the CeA is the principal output nucleus of the amygdaloid complex, understanding the molecular identity of CRF neurons — and their correspondence in single-cell transcriptomic atlases — is essential for translating circuit-level findings to human disease.

### Classical type description

| Property | Value | References |
|---|---|---|
| Cell type name | Central amygdala corticotropin-releasing factor (CRF) neuron | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | [1] |
| Soma location | central amygdala [UBERON:0002883] | [1] |
| Defining markers | None recorded | — |
| Negative markers | None recorded | — |
| Neuropeptides | Crh | [1] |
| Morphology | Not recorded | — |
| Electrophysiology | Not recorded | — |
| Notes | Often partially overlaps with other neuropeptide-defined CeA populations; not exhaustively characterized here. | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Neurotransmitter (GABAergic):** asta_report synthesis · amygdala literature synthesis · [1]
- **Soma location (central amygdala [UBERON:0002883]):** asta_report synthesis · CeA neuropeptide neuron classification · [1]
  > .It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice.
  > — Yeh et al. 2024, Central amygdala cell types · [1] <!-- quote_key: 267685584_daaf5612 -->
- **Neuropeptide Crh:** asta_report synthesis · amygdala literature synthesis · [1]
  > .It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice.
  > — Yeh et al. 2024, Central amygdala cell types · [1] <!-- quote_key: 267685584_daaf5612 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0901 within SUPT_0249 (NDB-SI-MA-STRv Lhx8 lineage) is the primary mapping at LOW confidence, reflecting a single neuropeptide marker (Crh), absence of AT evidence, and a 1:n cardinality in which the classical CRF population likely maps across multiple sibling clusters.

### Mapping candidates table

**4a. Candidate overview**

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0901 | SUPT_0249 (NDB-SI-MA-STRv Lhx8) | n/a | 🔴 LOW | Crh CONSISTENT · NT CONSISTENT | broadMatch 1:n |

Note: 1 edge assessed (broadMatch 1:n). Cells (10x) not available — taxonomy DB may need rebuild (n_cells = null in facts).

**4b. Property alignment — CS20230722_CLUS_0901 (NDB-SI-MA-STRv Lhx8 Gaba_6)**

**Table 1 — Property comparison**

| Property | Classical | Supertype (SUPT_0249) | Best cluster (CLUS_0901) | Alignment |
|---|---|---|---|---|
| Soma location | central amygdala [UBERON:0002883] | MBA:536 CeA present; region_fraction 0.167 (highest rank0 candidate); label: NDB-SI-MA-STRv Lhx8 Gaba_6 | MBA:536 CeA present; region_fraction 0.167 | CONSISTENT |
| NT type | GABAergic | GABA (from label suffix "Gaba_6") | GABA | CONSISTENT |
| Crh (neuropeptide) | Crh — neuropeptide | not available at supertype level | mean_expression 6.24 (97.4th pct of CeA GABAergic cohort; tier 2) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yeh 2024 CeA neuropeptide classification | Literature | SUPPORT | CRF identified as CeA neuropeptide marker alongside PKC-δ and SOM | [1] |
| Atlas metadata — CLUS_0901 Crh expression | Atlas metadata | SUPPORT | Crh mean 6.24; 97.4th pct CeA GABAergic cohort; region_fraction 0.167 | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### CS20230722_CLUS_0901 (NDB-SI-MA-STRv Lhx8 Gaba_6) · 🔴 LOW

**Supporting evidence:**

- **Literature [1]:** Yeh et al. 2024 identifies CRF as one of three canonical CeA neuropeptide populations (alongside PKC-δ/Prkcd and SOM/Sst), confirmed in human amygdala. This directly supports Crh as the defining neuropeptide for this classical type.

  > .It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice.
  > — Yeh et al. 2024, Central amygdala cell types · [1] <!-- quote_key: 267685584_daaf5612 -->

- **Atlas metadata:** CS20230722_CLUS_0901 ("NDB-SI-MA-STRv Lhx8 Gaba_6") expresses Crh at a precomputed mean of 6.24, placing it at the 97.4th percentile of the CeA GABAergic survival cohort (n=5 clusters, filtered to MBA:536 + GABAergic). This is the strongest Crh signal among all rank-0 candidates and the cluster with the highest CeA region_fraction (0.167) in the cohort. SUPT_0249 (NDB-SI-MA-STRv Lhx8) is a striato-amygdalar lineage consistent with CeA developmental origin despite the NDB/SI label prefix. *(note: all 5 cohort members tied at discovery score 3; CLUS_0901 is selected by region_fraction rank, not by a unique Crh score.)*

**Marker evidence provenance:**

- **Crh (neuropeptide):** Evidence is transcript-level via asta_report synthesis from Yeh et al. 2024. The original study synthesises prior literature (Pitts et al. 2009; Sanford et al. 2017 are cited in the Yeh review for CRF as a CeA marker) rather than providing primary single-cell characterisation of confirmed-identity CRF+ CeA neurons. No IHC or morphological confirmation of the specific CRF+ population is recorded in the current facts file. The atlas-side Crh expression value (mean 6.24; tier 2 = reliably expressed) corroborates neuropeptide presence at the cluster level with strong cohort-relative specificity (97.4th percentile). No discrepancy between literature and atlas on Crh as a CeA marker. *(note: absence of a primary morphology- or electrophysiology-confirmed study means the classical node rests on literature synthesis rather than direct cell-type confirmation.)*

**Concerns:**

- **DISTRIBUTED_ACROSS_CLUSTERS:** Four of five rank-0 CeA GABAergic clusters (CLUS_0899, CLUS_0900, CLUS_0901, CLUS_0903) are under the same supertype SUPT_0249; all share the Crh signal and tie at discovery score 3. The classical CRF population likely distributes across these sibling clusters, making a 1:1 assignment premature. Selection of CLUS_0901 reflects highest region_fraction (0.167) but not biological exclusivity.
- **TAXONOMY_LEVEL_MISMATCH:** SUPT_0249 (NDB-SI-MA-STRv Lhx8 Gaba_6) is labelled as primarily a diagonal-band / substantia-innominata / ventral-striatum type. CeA soma fraction (region_fraction 0.167) is a minority signal; CLUS_0901 cells also reside in NDB, SI, and STRv structures.
- **No AT evidence:** No MapMyCells or annotation-transfer run has been performed. Without AT, the 1:n broadMatch cannot be resolved to a specific cluster. This is the primary confidence limiter.
- **Co-expression uncertainty:** Crh co-expression with Sst or Prkcd in CeA is not assessed. CRF neurons may overlap substantially with the SST or PKC-delta classes, and the current evidence does not resolve whether CRF marks a distinct transcriptomic class or a neuropeptide-co-expressing subset.

**What would upgrade confidence:**

1. **Annotation transfer (MapMyCells):** Apply a CRH-Cre+ scRNA-seq source dataset to WMBv1 CCN20230722 via MapMyCells. Target: F1 ≥ 0.60 at cluster level would suggest a specific cluster match; F1 distributed across SUPT_0249 siblings would confirm the 1:n interpretation. Would add `AnnotationTransferEvidence` to the edge.
2. **Cre-dependent single-cell profiling:** scRNA-seq of CRH-Cre+ CeA neurons mapped to WMBv1 to resolve 1:n cardinality among SUPT_0249 siblings, and to distinguish CeM CRF projection neurons from CeL CRF interneurons.
3. **Dual ISH co-expression:** Crh + Sst and Crh + Prkcd fluorescent ISH in mouse CeA to quantify co-expression fractions. Would resolve whether CRF is a distinct class or a subset of other neuropeptide populations.
4. **Targeted literature search:** A cite-traverse for "CRF CeA single-cell transcriptomics" or "Crh amygdala scRNA-seq" may identify a published dataset directly matching CRF+ CeA cells to WMBv1 clusters. Current evidence rests on a single review-level reference.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.**
The central amygdala corticotropin-releasing factor (CRF) neuron classical node is defined on a CLASSICAL basis: GABAergic neurotransmitter type, soma location in the central amygdala [UBERON:0002883], and Crh as the sole neuropeptide marker. No defining molecular markers beyond Crh and no morphological or electrophysiological class are recorded. The definition derives from literature synthesis (asta_report method) via Yeh et al. 2024 [1].

**Atlas mapping query.**
Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:536, NT type GABAergic, neuropeptide Crh). Full scoring rules: `workflows/map-cell-type.md`. The discovery cohort comprised 5 CeA GABAergic clusters (survival filter: region=MBA:536, nt_type=GABAergic). All 5 tied at discovery score 3; CLUS_0901 was selected for highest CeA region_fraction (0.167).

**Property alignment.**
Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**
- Atlas: CCN20230722 (WMBv1); taxonomy_id: CCN20230722.
- Reference: Zhuang et al. 2023 (WMBv1; atlas-internal).

**Anti-hallucination.**
All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_crf_neuron_to_cs20230722_clus_0901 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [1]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:49+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Central amygdala corticotropin-releasing factor (CRF) neuron → CS20230722_CLUS_0901 (SUPT_0249, NDB-SI-MA-STRv Lhx8) at LOW confidence. Key support: Crh neuropeptide expression CONSISTENT (mean 6.24; 97.4th pct CeA GABAergic cohort) and NT type CONSISTENT (GABAergic). Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (four SUPT_0249 sibling clusters equally Crh-positive; broadMatch 1:n) and TAXONOMY_LEVEL_MISMATCH (SUPT_0249 spans NDB, SI, STRv — CeA cells are a minority fraction, region_fraction 0.167).

No Cell Ontology term currently assigned. Candidate for CL contribution (no existing CL term covers CRF-defined CeA neurons specifically).

### Proposed experiments and follow-ups

No experiments have been previously performed on this edge. The following are proposed:

**1. Annotation transfer — MapMyCells**
- **What:** Apply a CRH-Cre+ scRNA-seq source dataset (or a published CRF-reporter amygdala dataset) to WMBv1 CCN20230722 using MapMyCells.
- **Target:** F1 ≥ 0.60 at cluster level to resolve which SUPT_0249 sibling(s) capture CRF neurons; scatter distribution across siblings would diagnose the 1:n pattern.
- **Expected output:** `AnnotationTransferEvidence` added to `edge_cea_crf_neuron_to_cs20230722_clus_0901`.
- **Resolves:** Open questions Q1 (distinct class vs. subset of SST/PKCδ) and Q2 (CeM vs. CeL CRF neuron resolution); DISTRIBUTED_ACROSS_CLUSTERS caveat.

**2. Cre-dependent single-cell profiling**
- **What:** scRNA-seq of CRH-Cre+ CeA neurons, with cells mapped to WMBv1 clusters.
- **Target:** Cluster-level assignment of the majority (> 70%) of CRH-Cre+ CeA cells to one or two specific SUPT_0249 siblings.
- **Expected output:** `AnnotationTransferEvidence` or `LiteratureEvidence` citing the profiling study.
- **Resolves:** Q1, Q2, DISTRIBUTED_ACROSS_CLUSTERS caveat.

**3. Dual ISH co-expression study**
- **What:** Fluorescent ISH for Crh + Sst and Crh + Prkcd in mouse CeA.
- **Target:** Quantify co-expression fractions; ≤20% overlap would support CRF as a distinct transcriptomic class.
- **Expected output:** `LiteratureEvidence` with snippet documenting co-expression fractions.
- **Resolves:** Q1 (CRF vs. SST/PKCδ distinctness).

**4. Targeted literature search**
- **What:** Cite-traverse for "CRF CeA single-cell transcriptomics" or "Crh amygdala scRNA-seq" to identify any published dataset directly assigning CRF+ CeA cells to WMBv1 clusters.
- **Target:** At least one primary study with cell-type-confirmed CRF+ CeA neurons and transcriptomic profiling.
- **Expected output:** `LiteratureEvidence` entry with primary citation on the classical node.
- **Resolves:** Weak evidence provenance for Crh (currently rests on single review-level reference).

### Open questions

1. Is the CRF CeA neuron a distinct transcriptomic class or a subset of the SST or PKC-delta populations with Crh co-expression? *(On edge_cea_crf_neuron_to_cs20230722_clus_0901.)*
2. Which WMBv1 cluster specifically corresponds to CeM CRF projection neurons vs CeL CRF interneurons? *(On edge_cea_crf_neuron_to_cs20230722_clus_0901.)*

---

## References

| Label | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Yeh et al. 2024 | [PMID:38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | NT type, soma location, neuropeptide Crh |

---

<!-- verdict-block-start: edge_cea_crf_neuron_to_cs20230722_clus_0901 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    Crh neuropeptide expression is CONSISTENT (mean_expression 6.24; 97.4th pct CeA GABAergic survival cohort, n=5) and NT type is CONSISTENT (GABA) for CS20230722_CLUS_0901 under SUPT_0249 (NDB-SI-MA-STRv Lhx8 lineage). However, 4 of 4 sibling SUPT_0249 rank-0 clusters score equally on Crh alone (discovery score tied at 3; broadMatch 1:n cardinality confirmed). Region_fraction 0.167 at cluster level confirms CeA presence but the supertype spans NDB, SI, and STRv as primary locations. No annotation-transfer evidence is available; no defining markers beyond Crh are recorded on the classical node. Confidence capped at LOW: single neuropeptide marker, no AT, 1:n cardinality unresolved.
  unresolved_questions:
    - Is the CRF CeA neuron a distinct class or a subset of the SST or PKC-delta populations with Crh co-expression?
    - Which WMBv1 cluster specifically corresponds to CeM CRF projection neurons vs CeL CRF interneurons?
```
<!-- verdict-block-end -->
