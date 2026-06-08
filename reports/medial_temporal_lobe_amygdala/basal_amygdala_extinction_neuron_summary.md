# Basal amygdala extinction neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Extinction neurons in the basal nucleus of the amygdala are a functionally defined population active during the extinction of conditioned fear — the counterpart to fear neurons in the same nucleus [1]. Unlike classical neurochemical cell types, this population is identified by its activity pattern during extinction learning rather than by molecular markers, neuropeptide content, or projection anatomy. Mapping this type to a transcriptomic atlas cluster requires molecular characterisation that is not yet available.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Basal amygdala [UBERON:0002887] | [1] |
| NT type | Not defined (functional type) | — |
| Defining markers | None encoded | — |
| Negative markers | None encoded | — |
| Neuropeptides | None encoded | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report · amygdala/hippocampus literature synthesis · [1]
  > Recent advances in neuroscience give us a better view of the inner structure of the amygdala, of its relations with other regions in the Medial Temporal Lobe (MTL) and of the prominent role of neuromodulation. They have particularly shed light on two kinds of neurons in the basal nucleus of the amygdala, the so-called fear neurons and extinction neurons.
  > — Carrere et al. 2015, Cell-type diversity maps and specialized functional neuron classes · [1] <!-- quote_key: 14375617_d7af88e4 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

No transcriptomic atlas type in CCN20230722 can be assigned to the Basal amygdala extinction neuron. One candidate supertype was returned by the discovery-mode cohort filter; that candidate is eliminated as UNCERTAIN because no molecular identity has been established for this functionally defined population. All one edge assessed is UNCERTAIN.

**Primary null finding:** Extinction neurons in the basal amygdala [UBERON:0002887] are defined exclusively by circuit-level activity during extinction of conditioned fear. No defining molecular markers are encoded on this classical node. The CCN20230722 atlas candidate returned by the GABAergic BLA survival-cohort filter (5 supertypes at rank 1, all scoring equally at score=1.0) cannot be discriminated from one another or confirmed as a match in the absence of precomputed expression data and without molecular anchors for this functional type.

### Candidate overview

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|---|---|---|
| — | 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | 798 | ⚪ UNCERTAIN | NT NOT\_ASSESSED · Location APPROXIMATE | Eliminated |

*1 edge total; all UNCERTAIN. Relationship type: `evidencell:UncertainRelationship`.*

---

## Eliminated candidates

All edges for this node are UNCERTAIN. The shared disqualifying signal is the complete absence of defining molecular markers on the classical node: the extinction neuron is a functional circuit concept, not a molecularly characterised cell type. No marker-based discrimination between atlas supertypes is possible at this time.

### 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] · n=798 cells

- **NT type (NOT\_ASSESSED):** The classical node carries no NT annotation (functional type; NT identity not established from available literature). The supertype label ("STR Prox1 Lhx6 Gaba_3" inferred from the GABAergic cohort filter) is itself a filter artifact — the atlas node CS20230722_SUPT_0005 is a Glutamatergic ("Glut") entry — and no NT comparison is possible.
- **Soma location (APPROXIMATE):** The classical soma location is basal amygdala [UBERON:0002887]. This supertype's dominant distribution is Striatum/Cortical subplate; only 2.2% of cells fall in MBA:1105 (Intercalated amygdalar nucleus), a BLA-adjacent structure. The region filter passed because the GABAergic BLA survival cohort admitted amygdala-adjacent entries; this is a weak signal, not a positive location match.
- **Discovery score:** Stage A returned this candidate ranked 1 of 5 with score=1.0, tied with all other supertypes in the cohort (next\_best\_score=1.0; cohort\_size=5). No marker-based discrimination was possible; the candidate is the cohort top-ranked only because it appeared first with no differentiating evidence.
- **Atlas metadata (NO\_EVIDENCE):** The single evidence item on this edge carries `supports: NO_EVIDENCE` — the edge was created to record the survival-cohort output, not because any positive alignment was found.

*(note: the intercalated amygdalar nucleus (MBA:1105) is anatomically adjacent to the basal/lateral amygdala, separated by narrow interstitial zones. This proximity means the 2.2% representation represents borderline rather than clearly absent spatial signal — but with no marker support this distinction has no practical bearing on the verdict.)*

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Basal amygdala extinction neuron (node `basal_amygdala_extinction_neuron`) has `definition_basis: CLASSICAL` and is characterised by soma location in the basal amygdala [UBERON:0002887] [1]. No NT type, defining markers, negative markers, or neuropeptides are encoded on this node. The type is defined by its functional role in extinction learning (activity-based identity), not by molecular or anatomical criteria beyond soma region.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.** CCN20230722 (WMBv1). No pseudobulk SHA recorded for this run (no precomputed expression data ingested for this node).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | NO_EVIDENCE | atlas-internal |

*Generated by evidencell `f00d68f` at 2026-06-04T12:07:34+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Basal amygdala extinction neuron → no assignable atlas type. All 1 edge assessed is UNCERTAIN. The core blocker is the absence of molecular identity for this functionally defined population: without defining markers no atlas cluster can be matched. The single candidate returned by the survival-cohort filter (0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005]) is eliminated because the atlas evidence item carries NO_EVIDENCE support, the NT comparison is not assessable, and the 2.2% amygdala-adjacent representation (MBA:1105, Intercalated amygdalar nucleus) does not constitute a location match.

No Cell Ontology term currently assigned. Candidate for CL contribution pending molecular characterisation.

### Proposed experiments and follow-ups

**Molecular characterisation of extinction neurons (targeted literature retrieval)**
- **What:** Focused cite-traverse for primary studies that molecularly characterised BLA extinction neurons (activity-dependent tagging experiments, TRAP-seq, or activity-arc labelling with subsequent transcriptomic profiling).
- **Target:** Identification of at least one defining marker or a gene expression signature (e.g. from TRAP-seq, single-nucleus sequencing of tagged cells) that distinguishes extinction-active neurons from fear-active neurons.
- **Expected output:** Addition of `defining_markers` and/or `nt_type` to the classical node YAML; subsequent re-run of `map-cell-type` would enable marker-based candidate scoring.
- **Resolves:** edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 (unresolvable until molecular identity established).

**Activity-dependent transcriptomics (new experiment)**
- **What:** Activity-dependent labelling (e.g. TRAP, Fos-TRAP2, calcium-activated fluorescent tagging) of extinction-active BLA neurons in mouse, followed by single-cell transcriptomic profiling and direct atlas mapping.
- **Target:** Gene expression signature sufficient for `map-cell-type` query; F1 ≥ 0.60 at supertype level to shift confidence to LOW; F1 ≥ 0.80 at cluster level for MODERATE.
- **Expected output:** `AnnotationTransferEvidence` on the edge, plus encoded markers on the classical node.
- **Resolves:** All edges for this node; would also resolve the paired `basal_amygdala_fear_neuron` node if the same experiment profiles both populations.

### Open questions

1. Do extinction neurons in the mouse basal amygdala correspond to a molecularly distinct transcriptomic cluster, or do they represent a transient activity state within a broader principal-neuron population (e.g. BLA glutamatergic neurons)?
2. Is there published activity-dependent transcriptomic profiling (TRAP-seq, Fos-TRAP, or equivalent) of BLA extinction-active neurons that encodes a gene signature — and if so, does that signature discriminate from fear neurons within the same nucleus?
3. The classical description from [1] identifies fear and extinction neurons as opposing functional populations within the basal nucleus. Are there molecular correlates (e.g. differential Rspo2/Ppp1r1b expression, as proposed for some BLA functional subpopulations) that could serve as atlas-level anchors?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Carrere & Alexandre 2015 · *Front. Syst. Neurosci.* | [25852499](https://pubmed.ncbi.nlm.nih.gov/25852499/) | Soma location; functional definition of extinction neurons |

---

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Extinction neurons are a circuit-level functional concept defined by activity during fear extinction, not by molecular identity. No defining markers are encoded on the classical node; `marker_nt_type` alignment is NOT_ASSESSED. The sole discovery-mode candidate (CS20230722_SUPT_0005; score=1 of 5-member GABAergic cohort, tied next_best_score=1) carries NO_EVIDENCE support. `location_soma` is APPROXIMATE only (MBA:1105, 2.2% of supertype). No molecular basis for mapping exists until activity-dependent transcriptomic profiling defines a marker signature.
  reconciliation_note: >
    Extinction neurons are a functional circuit-level concept defined by activity during fear extinction, not by molecular markers. Like fear neurons, they are likely a subpopulation within BLA glutamatergic principal neurons. No specific molecular atlas type corresponds to this functional identity; molecular characterisation is needed.
  unresolved_questions:
    - "Does a molecularly distinct transcriptomic signature exist for BLA extinction neurons, or do they represent a transient activity state within the BLA glutamatergic principal neuron population?"
    - "Has activity-dependent transcriptomic profiling (TRAP-seq or equivalent) of BLA extinction-active neurons been published with a gene expression signature that can be mapped to CCN20230722?"
```
<!-- verdict-block-end -->
