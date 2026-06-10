# Basal amygdala extinction neuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Extinction neurons in the basal nucleus of the amygdala are a functionally defined cell class identified by their activity during the recall of fear extinction learning — the counterpart to fear neurons in the same nucleus [1]. Unlike canonical neurochemically defined interneurons or principal neurons, this population is characterised entirely by in vivo activity patterns and circuit-level physiology: no defining molecular markers, neurotransmitter type, or neuropeptide content are recorded for this classical type as presently defined in the knowledge base. Mapping this functional type to a transcriptomic atlas cluster is therefore blocked by the same fundamental barrier as the parallel basal amygdala fear neuron node: without a gene expression signature, property-based atlas matching is not possible.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Basal nucleus of the amygdala [UBERON:0002887] | [1] |
| NT type | Not defined (functional type) | — |
| Defining markers | None encoded | — |
| Negative markers | None encoded | — |
| Neuropeptides | None encoded | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report · amygdala literature synthesis · [1]
  > Recent advances in neuroscience give us a better view of the inner structure of the amygdala, of its relations with other regions in the Medial Temporal Lobe (MTL) and of the prominent role of neuromodulation. They have particularly shed light on two kinds of neurons in the basal nucleus of the amygdala, the so-called fear neurons and extinction neurons.
  > — Carrere et al. 2015, Cell-type diversity maps and specialized functional neuron classes · [1] <!-- quote_key: 14375617_d7af88e4 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

**No transcriptomic atlas type in CCN20230722 can be assigned to basal amygdala extinction neurons.** One candidate supertype was returned by discovery-mode region and NT-type filtering; it carries NO_EVIDENCE support and is rated UNCERTAIN. The fundamental blocker is the absence of any molecular definition for this functional cell class: without defining markers or a neurotransmitter identity, property-based atlas matching is not possible.

### Candidate overview table

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|---|---|---|
| — | 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | 798 | ⚪ UNCERTAIN | No markers; location APPROXIMATE | Eliminated |

*1 edge total; all UNCERTAIN. Relationship type: `evidencell:UncertainRelationship`.*

### Property alignment — 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005]

**Table 1 — Property comparison**

| Property | Classical | Supertype | Alignment |
|---|---|---|---|
| Soma location | Basal nucleus of amygdala [UBERON:0002887] | MBA:1105 Intercalated amygdalar nucleus (2.2% of supertype); dominant Striatum/Cortical subplate | APPROXIMATE |
| NT type | Not defined (functional type) | GABA (inferred from supertype label STR Prox1 Lhx6 Gaba_3) | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Discovery-mode survival cohort filter | Atlas metadata | NO_EVIDENCE | score=1, rank 1/5, tied (next_best=1); no marker discrimination possible | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

## Eliminated candidates

All edges for this node are UNCERTAIN. The shared disqualifying signal is the complete absence of defining molecular markers on the classical node: the extinction neuron is a functional circuit concept, not a molecularly characterised cell type. No marker-based discrimination between atlas supertypes is possible.

### 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] · n=798 cells

- **NT type (NOT_ASSESSED):** The classical node carries no NT annotation (functional type; NT identity not established from available literature). The supertype label "STR Prox1 Lhx6 Gaba_3" listed in the NT property comparison reflects the GABAergic cohort filter that was applied; it is inconsistent with the atlas node name "IT EP-CLA Glut_3", indicating a data entry issue in the discovery pipeline. No NT comparison is assessable.
- **Soma location (APPROXIMATE):** The classical soma location is basal amygdala [UBERON:0002887]. The supertype's dominant distribution is Striatum/Cortical subplate; only 2.2% of its cells fall in MBA:1105 (Intercalated amygdalar nucleus), a BLA-adjacent structure. The location filter admitted amygdala-adjacent entries; this is a weak signal, not a confirmed BLA placement. *(note: MBA:1105, the intercalated amygdalar nucleus, is anatomically adjacent to the basal/lateral amygdala — but with no marker support this borderline proximity has no practical bearing on the UNCERTAIN verdict.)*
- **Discovery score:** Stage A returned this candidate ranked 1 of 5 with score=1.0, tied with all other supertypes in the 5-member GABAergic BLA cohort (next_best_score=1.0; cohort_size=5). No marker-based discrimination was possible; the candidate appears first only by position, without differentiating evidence.
- **Atlas metadata evidence (NO_EVIDENCE):** The single evidence item on this edge carries `supports: NO_EVIDENCE` — the edge was created to record the survival-cohort discovery output, not because positive alignment was found.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Basal amygdala extinction neuron (node `basal_amygdala_extinction_neuron`) has `definition_basis: CLASSICAL` and is characterised by soma location in the basal nucleus of the amygdala [UBERON:0002887] [1]. No NT type, defining markers, negative markers, or neuropeptides are encoded on this node. The type is defined by its functional role in extinction learning (activity-based identity), not by molecular or anatomical criteria beyond soma region. Node notes: "Counterpart to fear neurons in the same nucleus."

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | NO_EVIDENCE | atlas-internal |

*Generated by evidencell `f1aa396` at 2026-06-10T14:09:30+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Basal amygdala extinction neuron → no assignable atlas type. All 1 edge assessed is UNCERTAIN. Key support: none — discovery-mode filter only, NO_EVIDENCE rated. Key caveats: no molecular identity is defined for this functional type; the sole atlas candidate was returned by position in a 5-way tied cohort with no differentiating evidence.

No Cell Ontology term is currently assigned to this type. The functional definition (activity-based, no molecular markers) means it cannot yet be linked to a CL class without a molecular characterisation bridging this gap. This type is a candidate for a new CL term once molecular identity is established.

### Proposed experiments and follow-ups

The core gap is the absence of a molecular definition for basal amygdala extinction neurons. Published annotation-transfer experiments are not yet feasible without first establishing a marker signature.

**1. Targeted literature retrieval for molecular characterisation**
- **What:** Focused cite-traverse for primary studies that profiled BLA extinction-active neurons using activity-dependent tagging (TRAP-seq, Fos-TRAP2, or calcium-tag strategies) with subsequent transcriptomics.
- **Target:** Identification of at least one defining marker or gene signature distinguishing extinction-active neurons from fear-active or quiescent BLA neurons.
- **Expected output:** Defining markers added to the classical node YAML → re-run of `map-cell-type` enables marker-based scoring.
- **Resolves:** Q1 and Q2 below; enables MapMyCells experiment (step 2).

**2. Activity-dependent transcriptomics (new experiment if literature search is negative)**
- **What:** Activity-dependent labelling (e.g. TRAP, Fos-TRAP2) of extinction-active BLA neurons in mouse followed by single-cell transcriptomic profiling and direct CCN20230722 atlas mapping via MapMyCells.
- **Target:** Gene expression signature sufficient for `map-cell-type` query; F1 ≥ 0.60 at supertype level to shift confidence to LOW; F1 ≥ 0.80 at cluster level for MODERATE.
- **Expected output:** `AnnotationTransferEvidence` on the edge, plus encoded markers on the classical node.
- **Resolves:** All edges for this node; would also resolve `basal_amygdala_fear_neuron` if the same experiment profiles both populations in parallel.

**3. Curator review of NT annotation discrepancy**
- **What:** Resolve the inconsistency between the supertype name "IT EP-CLA Glut_3" (glutamatergic) and the property comparison NT label "GABA (inferred from supertype label STR Prox1 Lhx6 Gaba_3)" on this edge and the parallel fear neuron edge.
- **Expected output:** Corrected NT annotation in the property comparison YAML.
- **Resolves:** Data integrity issue present on both sibling edges.

### Open questions

1. Does a molecularly distinct transcriptomic signature exist for BLA extinction neurons, or do they represent a transient activity state within the BLA glutamatergic principal neuron population?
2. Has activity-dependent transcriptomic profiling (TRAP-seq or equivalent) of BLA extinction-active neurons been published with a gene expression signature that can be mapped to CCN20230722?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Carrere & Alexandre 2015 · PMID:25852499 | [25852499](https://pubmed.ncbi.nlm.nih.gov/25852499/) | Soma location; functional description of extinction neurons |

---

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Extinction neurons are a circuit-level functional concept defined by activity during
    fear extinction, not by molecular identity. No defining markers are encoded on the
    classical node; `marker_nt_type` alignment is NOT_ASSESSED. The sole discovery-mode
    candidate (CS20230722_SUPT_0005; score=1 of 5-member GABAergic cohort, tied
    next_best_score=1) carries NO_EVIDENCE support. `location_soma` is APPROXIMATE only
    (MBA:1105, 2.2% of supertype). No molecular basis for mapping exists until
    activity-dependent transcriptomic profiling defines a marker signature.
  reconciliation_note: >
    Extinction neurons are a functional circuit-level concept defined by activity during
    fear extinction, not by molecular markers. Like fear neurons, they are likely a
    subpopulation within BLA glutamatergic principal neurons. No specific molecular atlas
    type corresponds to this functional identity; molecular characterisation is needed.
    See also edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 for the parallel
    fear neuron case; both share the same absence-of-molecular-identity blocker.
  unresolved_questions:
    - "Does a molecularly distinct transcriptomic signature exist for BLA extinction neurons, or do they represent a transient activity state within the BLA glutamatergic principal neuron population?"
    - "Has activity-dependent transcriptomic profiling (TRAP-seq or equivalent) of BLA extinction-active neurons been published with a gene expression signature that can be mapped to CCN20230722?"
```
<!-- verdict-block-end -->
