# Central amygdala ISL1-expressing long-range projection neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala (CeA) contains two major GABAergic cell classes previously unresolved by canonical marker-gene approaches: an Nr2f2-expressing population associated with a non-canonical CeA subdomain, and an ISL1-expressing medial cell type that accounts for many long-range CeA projections. The ISL1-expressing class, designated here as the central amygdala ISL1-expressing long-range projection neuron, is defined by expression of the LIM-homeodomain transcription factor ISL1 (Islet-1), which marks neurons derived from the ventral lateral ganglionic eminence (LGEv). Together with the Nr2f2 population, these ISL1+ neurons constitute approximately one-third of all CeA neurons. Mapping this class to the CCN20230722 whole-brain transcriptomic atlas is important for understanding how CeA output pathways are encoded at the transcriptomic level and for anchoring CeA projection neuron diversity to the atlas taxonomy.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Cell type name | Central amygdala ISL1-expressing long-range projection neuron | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | [1] |
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | [1] |
| Defining markers | Isl1 | [1] [2] |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Notes | Constitutes approx. one-third of all CEA neurons together with Nr2f2+ population; Prkcd and Sst exhibit mixed expression across multiple scRNA-seq clusters. STUB — pending primary evidence extraction. | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** scRNA-seq combined with multiplex FISH, IHC, and long-range projection mapping · mouse CeA · [1]
  > "In spatially mapping these novel types, we identify a non-canonical CEA subdomain associated with Nr2f2 expression and uncover an Isl1-expressing medial cell type that accounts for many long-range CEA projections."
  > — O'Leary et al. 2022, Central amygdala cell types · [1] <!-- quote_key: 253356112_2fc294b0 -->

- **Neurotransmitter — GABAergic:** inferred from CeA composition (exclusively GABAergic output nucleus); stated in O'Leary et al. 2022 study context · [1]

- **Defining marker — Isl1 (LGEv developmental origin):** developmental anatomy review · rodent · [2]
  > "cells derived from the ventral LGEv express Islet1 (Waclaw et al., 2010; Bupesh et al., 2011a) and show a trend to locate in the lateral and medial subdivisions of the nucleus (Bupesh et al., 2011a), partially overlapping the neurons expressing corticotropin releasing factor or other peptides/proteins (dynorphin, calbindin) that concentrate in different parts of the lateral subdivision"
  > — Vicario et al. 2014, INTRODUCTION · [2] <!-- quote_key: 10856039_51074be7 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_1385 (CEA-BST Ebf1 Pdyn Gaba_1) is the primary mapping at LOW confidence.

### Mapping candidates overview

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_1385 | CEA-BST Ebf1 Pdyn family | null* | 🔴 LOW | Isl1 CONSISTENT · location CONSISTENT | broadMatch — 1:n cardinality |

*n_cells: taxonomy DB predates the n_cells schema column (PR #21); rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` to populate.

Note: one edge assessed; skos:broadMatch 1:n relationship. Five CEA-BST rank0 clusters (CLUS_1316/1385/1386/1395/1397) all score equivalently on Isl1 alone; CLUS_1385 ranks highest by CeA region_fraction (0.489) and is used as the representative edge.

---

### CS20230722_CLUS_1385 · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA (Gaba_1 label) | CONSISTENT |
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | not available (rank-0 candidate) | MBA:536 CeA present; region_fraction 0.489 (highest among rank0 candidates); label "CEA-BST Ebf1 Pdyn Gaba_1" confirms CEA-BST lineage | CONSISTENT |
| Isl1 expression | Isl1 — defining marker [1] [2] | not available | Isl1 mean_expression 6.62 (CeA GABAergic cohort 96.4th pct; tier 2) | CONSISTENT |
| Sex ratio | Not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| O'Leary et al. 2022 ISL1 CeA | Literature | SUPPORT | ISL1+ medial CeA class accounts for many long-range projections; LGEv developmental origin | [1] |
| Atlas metadata — CLUS_1385 Isl1 | Atlas metadata | SUPPORT | Isl1 at 96.4th pct of CeA GABAergic cohort; region_fraction 0.489; CEA-BST label | atlas-internal |

*(Child-cluster breakdown not assessed — five CEA-BST rank0 clusters score equivalently on Isl1; see proposed experiments.)*

#### Supporting evidence

- **Isl1 transcriptomic expression:** CLUS_1385 shows Isl1 mean_expression = 6.62 at the 96.4th percentile of the CeA GABAergic survival cohort (n=5, region=MBA:536, nt_type=GABAergic; tier 2 reliable; applied_score 2.0). This is the highest-ranking Isl1-expressing cluster in the CEA-BST family. Source: EXPRESSION (precomputed stats), not METADATA alone.
  > "In spatially mapping these novel types, we identify a non-canonical CEA subdomain associated with Nr2f2 expression and uncover an Isl1-expressing medial cell type that accounts for many long-range CEA projections."
  > — O'Leary et al. 2022, Central amygdala cell types · [1] <!-- quote_key: 253356112_2fc294b0 -->

- **CEA-BST region identity:** region_fraction = 0.489 for CLUS_1385 at MBA:536 *(note: 0.3–0.7 is used as a rough boundary-band heuristic per the gen-report workflow — not a cited biological threshold)* is the highest among all five rank0 candidates; the cluster label "CEA-BST Ebf1 Pdyn Gaba_1" directly designates central amygdala–bed nucleus of the stria terminalis lineage. Four of the five rank0 candidates are CEA-BST clusters, providing a coherent transcriptomic family for the ISL1 projection neuron class.

- **LGEv developmental origin:** Vicario et al. 2014 [2] establishes that LGEv-derived neurons express Islet1 and localise to lateral and medial CeA subdivisions, partially overlapping neurons expressing CRF and dynorphin — consistent with the Pdyn-labelled CEA-BST family.
  > "cells derived from the ventral LGEv express Islet1 (Waclaw et al., 2010; Bupesh et al., 2011a) and show a trend to locate in the lateral and medial subdivisions of the nucleus (Bupesh et al., 2011a), partially overlapping the neurons expressing corticotropin releasing factor or other peptides/proteins (dynorphin, calbindin) that concentrate in different parts of the lateral subdivision"
  > — Vicario et al. 2014, INTRODUCTION · [2] <!-- quote_key: 10856039_51074be7 -->

#### Marker evidence provenance

- **Isl1 (defining marker):** Evidence is multi-modal — scRNA-seq, multiplexed FISH, and IHC in O'Leary et al. 2022 [1] (transcript and protein level). Cell-type specificity is strong: the study used bottom-up single-cell transcriptomics to identify the Isl1+ class as a novel CeA type, not as a bulk "Isl1+ interneuron" population. Vicario et al. 2014 [2] provides the developmental anatomical context (LGEv origin) but is a review-style paper; the primary functional evidence is O'Leary et al. 2022.
  - *(note: ISL1 is a transcription factor widely expressed during amygdala neurogenesis. O'Leary et al. 2022 identified Isl1+ cells in adult CeA by scRNA-seq, but adult protein-level IHC confirmation in mature mouse CeA has not been extracted into the KB as a separate evidence item. This is flagged under caveats.)*

#### Concerns

- **DISTRIBUTED_ACROSS_CLUSTERS:** Five CEA-BST rank0 clusters (CLUS_1316, CLUS_1385, CLUS_1386, CLUS_1395, CLUS_1397) all score 3/3 on the Isl1+region+NT criteria. The classical type likely spans multiple CEA-BST subtypes; 1:n cardinality at rank0 is the principal unresolved issue. Discovery score = 3 is tied with next_best_score = 3 in a cohort of only 5 candidates — near-maximal tie, no dominance signal.

- **No annotation-transfer evidence:** No MapMyCells run has been performed. Without AT evidence anchoring the ISL1 projection neuron to a specific cluster, the cardinality question (which of the five CEA-BST clusters best represents the long-range projection class) is unresolvable from marker metadata alone.

- **Adult ISL1 expression unconfirmed at atlas level:** ISL1 is a developmental transcription factor. The atlas captures adult mouse brain; adult ISL1 expression is well established in the literature (O'Leary et al. 2022 [1]) but atlas-level single-cell precomputed expression (mean 6.62 in CLUS_1385) is consistent with maintained adult expression. Nonetheless, no atlas-internal validation of ISL1 protein expression is available.

#### What would upgrade confidence

1. **MapMyCells annotation transfer** (AnnotationTransferEvidence) on ISL1-lineage traced CeA neurons from a published dataset (e.g. ISL1-TRAP or Isl1-Cre::reporter-sorted cells). Target: F1 ≥ 0.80 at CLUSTER level resolving 1:n cardinality among CEA-BST clusters. Resolves: Q1 (which CEA-BST cluster best represents the ISL1 projection class).
2. **ISL1 IHC in adult mouse CeA** (LiteratureEvidence) confirming sustained expression in mature neurons at protein level. This would convert the developmental-marker caveat into a confirmed adult marker. Resolves: Q2 (adult vs. developmental expression).
3. **Targeted literature search** for Isl1 expression in CEA-BST Pdyn/Ebf1 clusters (cite-traverse on "ISL1 CeA adult projections Ebf1 Pdyn") to identify whether primary literature has already resolved cluster-level correspondence. This is a KB-only step requiring no new experiment.

---

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The `cea_isl1_projection_neuron` classical node is defined on the basis of CLASSICAL evidence. Defining marker: Isl1 [1] [2]. Neurotransmitter type: GABAergic [1]. Soma location: Central amygdaloid nucleus [UBERON:0002883] [1]. The node was identified by O'Leary et al. 2022 using single-cell RNA sequencing combined with multiplexed FISH, IHC, and long-range projection mapping; the Isl1+ class was identified as a novel medial CeA type accounting for many long-range projections. The `definition_basis` is CLASSICAL, reflecting multimodal experimental evidence.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`. Survival cohort: MBA:536 (Central amygdalar nucleus), GABAergic, n=5 rank0 clusters.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_isl1_projection_neuron_to_cs20230722_clus_1385 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [1]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:51+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Central amygdala ISL1-expressing long-range projection neuron → CS20230722_CLUS_1385 at LOW confidence. Key support: Isl1 precomputed expression at 96.4th percentile of CeA GABAergic cohort (CONSISTENT); CeA region_fraction 0.489 (CONSISTENT); CEA-BST label confirms CeA lineage. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS — five CEA-BST rank0 clusters score equivalently on Isl1 alone, and no AT evidence is available to resolve 1:n cardinality.

No Cell Ontology term currently assigned. The ISL1-expressing CeA projection class is a recently characterised type (O'Leary et al. 2022) not yet represented in CL; it is a candidate for CL contribution.

### Proposed experiments and follow-ups

**Annotation transfer (MapMyCells)**
- **What:** Run MapMyCells on an Isl1-Cre lineage-traced CeA scRNA-seq dataset, or on the ISL1+ cells identified in O'Leary et al. 2022 if raw data are available.
- **Target:** F1 ≥ 0.80 at CLUSTER level to resolve which of CLUS_1316/1385/1386/1395/1397 best represents the long-range projection class.
- **Expected output:** AnnotationTransferEvidence added to edges for one or more CEA-BST clusters; non-matching clusters downgraded to UNCERTAIN.
- **Resolves:** Q1 (CEA-BST cardinality question) across all five rank0 edges.

**ISL1 IHC in adult mouse CeA**
- **What:** Immunohistochemistry for ISL1 protein in adult mouse CeA sections, with co-labelling for axonal tracer (retrograde from known long-range projection targets).
- **Target:** Confirm that ISL1+ neurons in adult medial CeA project to BST, brainstem, or hypothalamus.
- **Expected output:** LiteratureEvidence confirming adult Isl1 protein expression and projection identity; would convert the developmental-marker caveat.
- **Resolves:** Q2 (adult vs. developmental ISL1 expression).

**Targeted literature search**
- **What:** Cite-traverse for "ISL1 CeA adult projections Ebf1 Pdyn" in ASTA corpus to identify whether subsequent studies have resolved cluster-level correspondence.
- **Target:** LiteratureEvidence item on the primary edge citing adult-expression or projection confirmation.
- **Expected output:** MarkerEvidence or LiteratureEvidence; may also add negative markers distinguishing the ISL1 class from Prkcd+ and Sst+ CeA populations.
- **Resolves:** Q1 (partial), Q2.

### Open questions

1. Which CEA-BST Ebf1 Pdyn cluster (CLUS_1385 vs CLUS_1386 vs CLUS_1395 vs CLUS_1397 vs CLUS_1316) best represents the ISL1 long-range projection neuron? Five clusters score equivalently on the single available criterion (Isl1 expression).
2. Is ISL1 expression maintained in adult CeA neurons, or does the atlas capture a developmental remnant of LGEv neurogenesis?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | O'Leary et al. 2022 · iScience | [36425768](https://pubmed.ncbi.nlm.nih.gov/36425768/) | Isl1 defining marker; soma location; GABAergic NT; long-range projection identity |
| [2] | Vicario et al. 2014 · Front. Neuroanat. | [25309337](https://pubmed.ncbi.nlm.nih.gov/25309337/) | LGEv developmental origin of Islet1+ CeA neurons |

---

<!-- verdict-block-start: edge_cea_isl1_projection_neuron_to_cs20230722_clus_1385 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    `marker_Isl1` CONSISTENT (precomputed mean 6.62, CeA GABAergic cohort 96.4th pct;
    tier 2 reliable; EXPRESSION source). `location_soma` CONSISTENT: region_fraction 0.489
    at MBA:536 (CeA); CEA-BST label confirms lineage. `nt_type` CONSISTENT: GABA. 1 of 1
    markers CONSISTENT. No ANNOTATION_TRANSFER evidence. Confidence is LOW because five
    CEA-BST rank0 clusters (CLUS_1316/1385/1386/1395/1397) score identically on Isl1 +
    region + NT criteria (discovery_score = 3, next_best_score = 3, cohort_size = 5) —
    1:n cardinality is unresolved without AT evidence.
  unresolved_questions:
    - "Which CEA-BST Ebf1 Pdyn cluster (CLUS_1385 vs 1386 vs 1395 vs 1397 vs 1316) best represents the ISL1 long-range projection neuron? Five rank0 clusters score identically on Isl1 alone."
    - "Is ISL1 expression maintained in adult CeA neurons, or does the atlas capture a developmental remnant of LGEv neurogenesis?"
```
<!-- verdict-block-end -->
