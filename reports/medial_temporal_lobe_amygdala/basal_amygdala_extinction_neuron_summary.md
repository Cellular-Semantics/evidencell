# Basal amygdala extinction neuron — CCN20230722 Mapping Report
*2026-06-15 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Extinction neurons are a functionally defined population of principal cells in the basal nucleus of the amygdala [UBERON:0002887] whose activity is selectively engaged during extinction of conditioned fear. They are distinct from the non-overlapping "fear neuron" population in the same nucleus and uniquely receive reciprocal input from the medial prefrontal cortex, placing them at the intersection of top-down fear regulation and amygdala output [2, 3]. McCullough et al. (2016) used Thy1-reporter and Thy1-Cre driver lines to behaviourally characterise and molecularly profile these Fear-Off cells, identifying a transcript-level signature that includes Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 [3].

**Location note.** Atlas location data derives from MERFISH spatial registration and records soma position only. Axonal projection targets — including the reciprocal mPFC connection that electrophysiologically distinguishes extinction from fear neurons — are not reflected in atlas cluster location fields and cannot be used in mapping assessments.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Basal amygdala [UBERON:0002887] | [1, 2, 3] |
| NT type | Not formally defined (BLA principal neuron, functionally characterised) | — |
| Defining markers | Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1 | [3] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Notes | Counterpart to fear neurons in the same nucleus | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** asta_report · amygdala/hippocampus literature synthesis · [1]
  > Recent advances in neuroscience give us a better view of the inner structure of the amygdala, of its relations with other regions in the Medial Temporal Lobe (MTL) and of the prominent role of neuromodulation. They have particularly shed light on two kinds of neurons in the basal nucleus of the amygdala, the so-called fear neurons and extinction neurons.
  > — Carrere et al. 2015, Cell-type diversity maps and specialized functional neuron classes · [1] <!-- quote_key: 14375617_d7af88e4 -->

- **Soma location / functional identity:** asta_report · review of BLA fear/extinction neuron circuit · [2]
  > With respect to fear expression, BLA principal neurons can be divided into two functionally distinct, non-overlapping populations. Activation of "fear" neurons is triggered by the conditioned stimulus, while "extinction" neurons become active only after repetitive presentations of the conditioned stimulus that are not followed by the unconditioned stimulus (Herry et al., 2008). Both types of neurons project to the mPFC but only extinction neurons receive reciprocal input from the mPFC, which makes their activity susceptible to mPFC modulation (Herry et al., 2008).
  > — Cardenas et al. 2019, Basal amygdala fear neurons and extinction neurons · [2] <!-- quote_key: 4940771_cb8fa215 -->

- **Defining markers (Ntsr2, Dkk3, Rspo2, Wnt7a):** transcript-level RNA-seq · mouse BLA, Thy1-labelled Fear-Off neurons · [3]
  > .RNA sequencing identifies genes strongly upregulated in RNA of this population, including Ntsr2, Dkk3, Rspo2 and Wnt7a
  > — McCullough et al. 2016, Basal amygdala fear neurons and extinction neurons · [3] <!-- quote_key: 104297085_710ab8bc -->

- **Defining markers (Ntsr2, Thy1) — cell identity validation:** Thy1-eNpHR / Thy1-Cre / Thy1-eYFP driver lines + behavioural characterisation · [3]
  > Here we demonstrate a comprehensive workflow for identification of pharmacologically tractable markers of behaviourally characterized cell populations. Thy1-eNpHR-, Thy1-Cre- and Thy1-eYFP-labelled neurons of the BLA consistently act as fear inhibiting or 'Fear-Off' neurons during behaviour
  > — McCullough et al. 2016, Basal amygdala fear neurons and extinction neurons · [3] <!-- quote_key: 104297085_cb656278 -->

- **Ntsr2 — functional validation:** Ntsr2-targeting strategy within BLA · [3]
  > .These experiments identify and validate Ntsr2-expressing neurons within the BLA, as a putative 'Fear-Off' population.
  > — McCullough et al. 2016, Basal amygdala fear neurons and extinction neurons · [3] <!-- quote_key: 104297085_20a79f85 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

A scan of CCN20230722 at supertype level (rank 1) restricted to GABAergic cells in or near the basolateral amygdala [UBERON:0002887] recovered five supertypes (cohort size = 5), all scored equally at the discovery stage because no precomputed expression data was available to discriminate candidates by marker concordance. The single top-ranked candidate, 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005], carries no marker-based supporting evidence and has only approximate spatial overlap with the basal amygdala (2.2% of supertype cells in MBA:1105). This mapping is currently unresolvable at the molecular level.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---:|---|---|---|---|
| 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | — | 798 | ⚪ UNCERTAIN | No marker data; 2.2% in amygdala region | Eliminated (no marker basis; off-target anatomy) |

*(1 edge assessed; 0 survivors; 1 cut. Relationship type: evidencell:UncertainRelationship.)*

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The basal amygdala extinction neuron is defined on the basis of functional electrophysiology and connectivity (CLASSICAL definition_basis). It is characterised by selective activation during extinction of Pavlovian fear conditioning and by reciprocal mPFC input, distinguishing it from the non-overlapping fear neuron population in the same nucleus [1, 2]. McCullough et al. (2016) supplemented this functional definition with a transcript-level molecular signature from RNA-seq of Thy1-driver-labelled BLA Fear-Off cells, identifying Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 as upregulated genes [3]. No NT type is formally assigned on the classical node; BLA principal neurons are generally glutamatergic *(note: based on standard neuroanatomical classification of BLA principal cells; not explicitly stated in gathered literature.)*, but the functional definition predates systematic molecular classification.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 1 (supertype) using metadata-based scoring (region match MBA:295/MBA:1105, NT type GABAergic). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. No atlas-side numerical values for the extinction neuron markers (Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1) were available from precomputed expression at the time of candidate generation.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `bfdb7f1` at 2026-06-15T10:48:32+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | NO_EVIDENCE | atlas-internal |

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** No confident mapping is currently possible for Basal amygdala extinction neuron → any CCN20230722 supertype or cluster. The single candidate assessed, 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005], is ranked by cohort position only (score=1, tied across all 5 cohort members) and carries no marker-based supporting evidence. Location alignment is only approximate (2.2% of supertype in MBA:1105 Intercalated amygdalar nucleus, with the dominant supertype distribution in striatum/cortical subplate). Key caveats: (1) the classical definition is functional (activity-gated), not molecular, making transcriptomic atlas mapping intrinsically difficult; (2) precomputed expression data for the defining markers (Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1) is absent for all BLA-adjacent supertypes in the current KB, preventing marker-based scoring.

No Cell Ontology term is currently assigned. The Ntsr2+/Thy1+ Fear-Off population characterised by McCullough et al. 2016 may be a candidate for a new CL term representing glutamatergic BLA principal neurons with an extinction-associated molecular signature, but this would require additional validation (e.g. confirmation of Ntsr2 at transcript level in a single-cell RNA-seq dataset with morphological or connectivity-based cell type confirmation).

### Proposed experiments and follow-ups

**Marker-based atlas query (priority).**
- **What:** Re-run the CCN20230722 candidate search with precomputed expression data for Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 once available. The `just find-candidates` call should be re-issued at both rank 0 (cluster) and rank 1 (supertype) with an expanded NT filter (include glutamatergic supertypes, since BLA principal neurons are typically glutamatergic *(note: based on standard neuroanatomical classification of BLA principal cells; not explicitly stated in gathered literature.)*).
- **Target:** At least one candidate with CONSISTENT or APPROXIMATE alignment on ≥ 3 of the 5 defining markers.
- **Expected output:** Updated `property_comparisons` entries on the edge YAML; new candidates at rank 0 if any cluster reaches a marker score ≥ moderate.
- **Resolves:** Both open questions (Q1, Q2 below).

**Annotation transfer from Thy1-eYFP or Ntsr2-Cre dataset.**
- **What:** Run MapMyCells annotation transfer using a Ntsr2-Cre or Thy1-eYFP BLA single-cell RNA-seq dataset as source, mapping onto WMBv1. If the McCullough et al. 2016 RNA-seq data (bulk or single-cell) is available in a public repository, it may be directly usable as source.
- **Target:** F1 ≥ 0.60 at supertype level as a minimum to support a candidate identification.
- **Expected output:** AnnotationTransferEvidence on the best-matching edge(s).
- **Resolves:** Q1 (whether a transcriptomic atlas equivalent exists for the Thy1+/Ntsr2+ population).

**Activity-dependent transcriptomic profiling (TRAP-seq or scRNA-seq post-fear-extinction).**
- **What:** Search published literature for TRAP-seq, activity-seq, or single-cell ATAC-seq profiling of BLA neurons during fear extinction (e.g. Fos-TRAP or equivalent approaches). Check for overlap with the Ntsr2/Dkk3/Rspo2/Wnt7a signature identified by McCullough et al. 2016.
- **Expected output:** LiteratureEvidence items on the edge; possibly a refined marker list for re-mapping.
- **Resolves:** Q2 (whether activity-dependent profiling has produced a mappable gene expression signature).

### Open questions

1. Does a molecularly distinct transcriptomic signature exist for BLA extinction neurons, or do they represent a transient activity state within the BLA glutamatergic principal neuron population? *(on edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005)*
2. Has activity-dependent transcriptomic profiling (TRAP-seq or equivalent) of BLA extinction-active neurons been published with a gene expression signature that can be mapped to CCN20230722? *(on edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005)*
3. The NT filter applied at candidate generation was GABAergic, but BLA principal neurons — the population from which extinction neurons are drawn — are generally glutamatergic. This mismatch should be resolved: re-run candidate generation with a glutamatergic filter (or no NT filter) to ensure the relevant atlas space is covered. *(note: based on standard neuroanatomical classification of BLA principal cells; not explicitly stated in gathered literature.)*
4. The property comparison for NT type notes "GABA (inferred from supertype label STR Prox1 Lhx6 Gaba_3)" but the candidate cluster is named "0005 IT EP-CLA Glut_3" — an apparent glutamatergic designation. This internal inconsistency in the edge data should be clarified by re-running the mapping with explicit NT-type checking.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Carrere & Alexandre 2015 | [25852499](https://pubmed.ncbi.nlm.nih.gov/25852499/) | soma location; functional description |
| [2] | Cardenas et al. 2019 | [31193505](https://pubmed.ncbi.nlm.nih.gov/31193505/) | soma location; fear/extinction neuron circuit |
| [3] | McCullough et al. 2016 | [27767183](https://pubmed.ncbi.nlm.nih.gov/27767183/) | defining markers; Thy1+ Fear-Off population characterisation |

---

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Sole discovery-mode candidate from a 5-member GABAergic BLA cohort (score=1, tied across all 5 members); carries NO_EVIDENCE support on the single ATLAS_METADATA evidence item. Location alignment is APPROXIMATE only (region_fraction: 0.022; MBA:1105 accounts for 2.2% of the supertype, dominant distribution in striatum/cortical subplate). No precomputed expression data was available for the defining markers (Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1) to assess marker concordance. The classical type is a functionally defined circuit concept with no current molecular atlas equivalent.
  reconciliation_note: >
    Extinction neurons are a functional circuit-level concept defined by activity during fear extinction, not by molecular markers. Like fear neurons, they are likely a subpopulation within BLA glutamatergic principal neurons. No specific molecular atlas type corresponds to this functional identity; molecular characterisation is needed. See also the parallel fear neuron case for the same absence-of-molecular-identity blocker. The NT filter applied at candidate generation (GABAergic) is likely incorrect for BLA principal neurons (typically glutamatergic); re-run with glutamatergic filter once marker data is available.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: No precomputed expression data exists for the defining markers (Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1) in the BLA-adjacent supertypes of CCN20230722. Marker-based discrimination between the 5 cohort candidates was not possible.
    - caveat_type: OTHER
      description: The classical type is defined by activity-gated behaviour during fear extinction and connectivity (reciprocal mPFC input), not by molecular identity. Transcriptomic atlas mapping is intrinsically uncertain until a stable molecular signature is confirmed in an appropriate neuronal transcriptomics dataset.
    - caveat_type: DISCORDANT_ANATOMY
      description: CS20230722_SUPT_0005 has 2.2% of its cells in MBA:1105 (Intercalated amygdalar nucleus); the dominant distribution is in striatum/cortical subplate. This is weak location support for a basal amygdala principal neuron population.
  proposed_experiments:
    - Re-run candidate discovery at CCN20230722 rank 0 and rank 1 with a glutamatergic NT filter (BLA principal neurons are typically glutamatergic) once precomputed expression data for Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 is available for amygdala-adjacent clusters. Target at least CONSISTENT or APPROXIMATE alignment on 3 of 5 defining markers to elevate any candidate to MODERATE confidence.
    - Run annotation transfer using a Ntsr2-Cre or Thy1-eYFP BLA neuronal transcriptomics dataset as source against WMBv1. F1 >= 0.60 at supertype level would support initial candidate identification. Expected output: AnnotationTransferEvidence.
    - Search published literature for TRAP-seq or activity-seq profiling of BLA neurons during fear extinction (Fos-TRAP or equivalent) and assess overlap with the McCullough 2016 Ntsr2/Dkk3/Rspo2/Wnt7a signature. Expected output: LiteratureEvidence items.
  unresolved_questions:
    - Does a molecularly distinct transcriptomic signature exist for BLA extinction neurons, or do they represent a transient activity state within the BLA glutamatergic principal neuron population?
    - Has activity-dependent transcriptomic profiling (TRAP-seq or equivalent) of BLA extinction-active neurons been published with a gene expression signature that can be mapped to CCN20230722?
    - The GABAergic NT filter applied at candidate generation is likely inappropriate for BLA principal neurons; confirm NT type of the source population and re-run discovery with glutamatergic or unfiltered NT constraint.
    - Apparent inconsistency between the property comparison NT label (GABA, inferred from STR Prox1 Lhx6 Gaba_3 supertype) and the candidate cluster name (0005 IT EP-CLA Glut_3) — clarify and correct before re-mapping.
```
<!-- verdict-block-end -->
