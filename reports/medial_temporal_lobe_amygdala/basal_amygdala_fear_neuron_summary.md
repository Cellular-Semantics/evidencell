# Basal amygdala fear neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basal amygdala fear neuron is a functionally defined ensemble within the basal nucleus of the amygdala, distinguished from extinction neurons by its activation pattern during Pavlovian fear conditioning rather than by a stable molecular identity. The two populations — fear neurons and extinction neurons — are described as opposing functional classes residing within the same nucleus [1]. Because this type is defined entirely by circuit activity rather than by markers or transcriptomic signature, a transcriptomic atlas mapping is expected to be indeterminate until molecular correlates of fear-active neurons are established.

### Classical Type Properties

| Property | Value | References |
|---|---|---|
| Node ID | `basal_amygdala_fear_neuron` | — |
| Definition basis | CLASSICAL (functionally defined) | — |
| Neurotransmitter | Not defined | — |
| Soma location | Basal amygdala [UBERON:0002887] | [1] |
| Defining markers | None encoded | — |
| Negative markers | None encoded | — |
| Neuropeptides | None encoded | — |
| Morphology | Not defined by markers or morphology; active during fear states | [1] |
| CL mapping | None assigned | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location & type identity:** asta_report · amygdala/hippocampus literature synthesis · [1]
  > "Recent advances in neuroscience give us a better view of the inner structure of the amygdala, of its relations with other regions in the Medial Temporal Lobe (MTL) and of the prominent role of neuromodulation. They have particularly shed light on two kinds of neurons in the basal nucleus of the amygdala, the so-called fear neurons and extinction neurons."
  > — Carrere & Alexandre 2015, Cell-type diversity maps and specialized functional neuron classes · [1] <!-- quote_key: 14375617_d7af88e4 -->

</details>

### Cell Ontology Mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed (rank 1, CCN20230722); all edges are UNCERTAIN. **A complete scan of the BLA GABAergic survival cohort (5 supertypes at rank 1) yielded no discriminating evidence.** Because the basal amygdala fear neuron carries no molecular markers and is defined purely by functional activity during fear conditioning, no transcriptomic atlas type can be specifically matched to this node at present. The best available candidate (CS20230722_SUPT_0005) is retained as a placeholder only; it does not represent a positive mapping.

### Mapping Candidates Overview

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|---|---|---|
| — | 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | 798 | ⚪ UNCERTAIN | NT NOT_ASSESSED · location APPROXIMATE | Eliminated |

*1 edge assessed; all UNCERTAIN. Relationship type: `evidencell:UncertainRelationship`.*

---

**Null-result statement.** The basal amygdala fear neuron carries no encoding of neurotransmitter type, no defining molecular markers, and no quantitative expression profile. Stage A discovery used a survival cohort filter (region: MBA:295, NT: GABAergic) and returned 5 rank-1 supertypes each scoring 1.0 — a tied cohort with no basis for discrimination. The top-ranked candidate (CS20230722_SUPT_0005, 0005 IT EP-CLA Glut_3) was selected as a cohort representative only; the `discovery_score` of 1 in a 5-member tied cohort (next-best score also 1) carries no candidate-specific weight. No atlas cluster in CCN20230722 corresponds to a "fear-active" functional state.

---

### Property Alignment — Primary Candidate

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basal amygdala [UBERON:0002887] | MBA:1105 Intercalated amygdalar nucleus (2.2% of supertype); dominant Striatum/Cortical subplate | Not assessed | APPROXIMATE |
| NT type | Not defined (functional type) | GABA (inferred from supertype label STR Prox1 Lhx6 Gaba_3) | Not assessed | NOT_ASSESSED |
| Sex ratio | Not documented | Not available | Not available | NOT_ASSESSED |

*(Note: the supertype label "0005 IT EP-CLA Glut_3" names a Glutamatergic type (Glut_3), yet the property comparison records a GABAergic NT annotation inferred from a different supertype label. This internal inconsistency in the discovery record is noted for curator review — the NT_type comparison may apply to a different entry in the BLA GABAergic cohort rather than to SUPT_0005 itself.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas cohort filter | Atlas metadata | NO_EVIDENCE | 5 BLA GABAergic rank-1 supertypes, all score=1.0; top-ranked entry only | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

## Eliminated Candidates

All edges are UNCERTAIN. There is a single shared disqualifying signal: the classical node carries **no molecular identity whatsoever** — no NT type, no markers, no neuropeptides. A functional-activity concept cannot be matched to a transcriptomic atlas type without a molecular bridge.

### 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] ⚪ UNCERTAIN

- **Cohort tie:** Stage A scored all 5 BLA GABAergic rank-1 supertypes equally at score=1.0; CS20230722_SUPT_0005 is the top-ranked entry by position only. No marker evidence was available to discriminate between cohort members.
- **Location is only approximate:** The location comparison notes that MBA:1105 (Intercalated amygdalar nucleus) accounts for 2.2% of the supertype, with dominant representation in Striatum and Cortical subplate. *(note: MBA:1105 is adjacent to the basal amygdala but is not the basal nucleus proper — this reflects approximate rather than exact anatomical concordance; weak counter-evidence.)*
- **NT annotation inconsistency:** The property comparison records a GABAergic annotation "inferred from supertype label STR Prox1 Lhx6 Gaba_3", but the node name for CS20230722_SUPT_0005 is "0005 IT EP-CLA Glut_3" — a glutamatergic designation. This mismatch suggests the NT comparison was carried over from a different candidate in the discovery pipeline, or that the internal naming is inconsistent. Either way, no meaningful NT comparison can be made for this edge.
- **No molecular bridge:** Fear neurons are an activity-defined ensemble. They are conceptually a subpopulation within BLA principal neurons — likely glutamatergic — but no specific molecular markers distinguishing fear-active from non-fear-active neurons are encoded on this classical node. Atlas transcriptomics captures stable cell-type identity, not transient activity states.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The `basal_amygdala_fear_neuron` node is defined as CLASSICAL with a purely functional basis: a neuron ensemble in the basal nucleus of the amygdala [UBERON:0002887] that is active during fear conditioning and has been contrasted with extinction neurons in the same nucleus [1]. No NT type, no molecular markers, and no morphological descriptor are encoded. The `definition_basis` value is CLASSICAL, reflecting that this type is established in the neuroscience literature as a functionally defined population rather than a transcriptomically or morphologically characterised cell class.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 1 (supertype) using a survival cohort filter (region: MBA:295, NT: GABAergic). The filter returned 5 supertypes, all scoring equally at score=1.0. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Because the classical node carries no markers and no NT type, only the soma location property was assessed; the alignment was APPROXIMATE (minor supertype representation at the amygdala-adjacent intercalated nucleus, with dominant striatal/cortical subplate distribution).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `f00d68f` at 2026-06-04T12:07:34+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | NO_EVIDENCE | atlas-internal |

</details>

---

## Discussion

### Best Candidate + Caveats

**Primary mapping:** Basal amygdala fear neuron → 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] at UNCERTAIN confidence. Key support: none — the single evidence item is rated NO_EVIDENCE; the candidate was selected as the top-ranked entry in a 5-way tied cohort with no discriminating signal. Key caveats: (1) this type is defined by functional activity state, not molecular identity, making any transcriptomic atlas correspondence fundamentally indeterminate without a molecular bridge; (2) all 5 BLA GABAergic rank-1 supertypes scored equally and the cohort assignment carries no biological weight.

No Cell Ontology term currently assigned. Fear neurons are a functional circuit-level concept; no CL term for an activity-defined neuronal ensemble currently exists in the Cell Ontology.

### Proposed Experiments and Follow-Ups

**Molecular characterisation of fear-active BLA neurons (prerequisite for any atlas mapping)**
- **What:** Activity-dependent labelling coupled with transcriptomic profiling to identify molecular markers co-expressed in fear-conditioned BLA neurons. Suitable approaches include Fos-TRAP (targeted recombination in active populations), TRAP2-seq, or activity-dependent viral capture followed by single-nucleus sequencing.
- **Target:** Identification of at least 2–3 consistently enriched gene markers across fear-conditioning paradigms, enabling formal encoding of `defining_markers` on the classical node.
- **Expected output:** `LiteratureEvidence` items with a defined marker panel added to the `basal_amygdala_fear_neuron` KB node; subsequently enables re-running `map-cell-type` with a marker-guided query.
- **Resolves:** All unresolved questions on `edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005`; prerequisite for annotation-transfer or cluster-level mapping.

**Literature survey — molecular correlates of fear conditioning in the BLA**
- **What:** Targeted cite-traverse for "fear-conditioned basal amygdala neuron transcriptomics" or "amygdala fear engram cell molecular identity" to surface any published marker profiles for fear-active BLA neurons.
- **Target:** Identify any primary study reporting transcript-level markers for fear-active versus fear-inactive BLA neurons.
- **Expected output:** `LiteratureEvidence` items added to the KB node; may enable encoding of provisional `defining_markers`.
- **Resolves:** Open question #1 (see below).

### Open Questions

1. Have any published studies (e.g. activity-dependent labelling + transcriptomics in the BLA) identified molecular markers that reliably distinguish fear-conditioned BLA neurons from the surrounding principal neuron population? If so, these should be extracted and encoded as `defining_markers` on this node.
2. Are fear neurons a subpopulation within the BLA glutamatergic principal neuron population (as implied by their anatomical location and the principal-cell majority in the basal nucleus), or can they also include inhibitory interneurons? The absence of an NT type annotation is a fundamental gap.
3. The NT annotation in the single edge's property comparison references a GABAergic supertype label (STR Prox1 Lhx6 Gaba_3) that does not match the node name (0005 IT EP-CLA Glut_3) assigned to CS20230722_SUPT_0005. Curator review is needed to confirm whether this reflects a data entry error in the discovery pipeline or a genuine ambiguity in the candidate set.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Carrere & Alexandre 2015 — "A pavlovian model of the amygdala and its influence within the medial temporal lobe" | [25852499](https://pubmed.ncbi.nlm.nih.gov/25852499/) | Soma location; type identity |

---

<!-- verdict-block-start: edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Fear neurons are a purely activity-defined functional ensemble; no NT type, markers, or expression profile are encoded on this classical node. Stage A discovery returned a 5-member tied cohort (all score=1; next_best_score=1; cohort_size=5) with no basis for discrimination; CS20230722_SUPT_0005 is the top-ranked entry by position only, not by evidence. The single ATLAS_METADATA evidence item is rated NO_EVIDENCE. Location comparison is APPROXIMATE (MBA:1105, 2.2% of supertype); NT comparison is NOT_ASSESSED. No atlas cluster in CCN20230722 corresponds to a fear-conditioning activity state. Molecular characterisation (e.g. Fos-TRAP followed by single-nucleus sequencing) is required before a meaningful mapping can be assessed.
  reconciliation_note: >
    Fear neurons are a circuit-level functional concept defined by activity during Pavlovian fear conditioning, not by molecular markers. They are likely a subpopulation within BLA glutamatergic principal neurons but cannot be mapped to a specific atlas transcriptomic type without molecular characterisation. See also edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 for the parallel extinction neuron case; both share the same absence-of-molecular-identity blocker.
  lit_to_lit_edges: []
  unresolved_questions:
    - Identify molecular markers co-expressed in fear-conditioned BLA neurons via activity-dependent labelling + transcriptomics (e.g. Fos-TRAP); encode as defining_markers to enable atlas mapping.
    - Confirm NT type of fear neurons (glutamatergic vs. GABAergic) from primary literature; absence of NT type is a fundamental gap for cohort-level filtering.
    - Curator review needed — NT annotation in edge property_comparison references GABAergic label (STR Prox1 Lhx6 Gaba_3) inconsistent with SUPT_0005 node name (0005 IT EP-CLA Glut_3); may reflect a discovery pipeline data entry issue.
```
<!-- verdict-block-end -->
