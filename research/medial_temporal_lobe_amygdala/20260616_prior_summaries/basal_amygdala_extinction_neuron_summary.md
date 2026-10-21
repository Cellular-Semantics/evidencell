# Cell Type Mapping Report: basal_amygdala_extinction_neuron
*Basal amygdala extinction neuron · Glutamatergic · Basolateral amygdala (UBERON:0002887)*

The basal amygdala extinction neuron is a glutamatergic principal neuron of the basal nucleus of the amygdala (BA), functionally defined by selective activation during extinction of conditioned fear — the "Fear-Off" state — in contrast to the adjacent fear neuron population, which is activated by the conditioned stimulus itself. These two populations together tile the behavioural valence space of BA principal neurons and are thought to be non-overlapping:

> "With respect to fear expression, BLA principal neurons can be divided into two functionally distinct, non-overlapping populations. Activation of \"fear\" neurons is triggered by the conditioned stimulus, while \"extinction\" neurons become active only after repetitive presentations of the conditioned stimulus that are not followed by the unconditioned stimulus (Herry et al., 2008). Both types of neurons project to the mPFC but only extinction neurons receive reciprocal input from the mPFC, which makes their activity susceptible to mPFC modulation (Herry et al., 2008)."
> — Cardenas et al. 2019, Basal amygdala fear neurons and extinction neurons  <!-- quote_key: 4940771_cb8fa215 -->

Their molecular identity was first approached by McCullough et al. 2016, who identified Ntsr2-expressing neurons within the BLA as a putative Fear-Off population:

> .These experiments identify and validate Ntsr2-expressing neurons within the BLA, as a putative 'Fear-Off' population.
> — McCullough et al. 2016, Basal amygdala fear neurons and extinction neurons  <!-- quote_key: 104297085_20a79f85 -->

> .RNA sequencing identifies genes strongly upregulated in RNA of this population, including Ntsr2, Dkk3, Rspo2 and Wnt7a
> — McCullough et al. 2016, Basal amygdala fear neurons and extinction neurons  <!-- quote_key: 104297085_710ab8bc -->

No CL term has been assigned and no `proposed_cl_term` has been generated for this node. A CL term request may be warranted once a stable transcriptomic identity is confirmed.

---

## Candidate atlas types

| Candidate | Relationship | Confidence | Key evidence | Region support |
|---|---|---|---|---|
| 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | evidencell:UncertainRelationship | UNCERTAIN | Atlas metadata only; no expression data; incorrect NT filter at candidate generation | 2.2% of supertype in MBA:1105; dominant distribution in striatum/cortical subplate — DISCORDANT |

*No candidate survives to full narrative. See Evidence gaps and Proposed experiments below.*

---

## Evidence gaps

The mapping for this node is entirely unresolved. The following gaps prevent any confident transcriptomic assignment:

1. **NT filter error at candidate generation.** The single candidate in this cohort was generated using a GABAergic NT filter, which is inconsistent with the glutamatergic identity of BLA principal neurons (confirmed by Hochgerner et al. 2023, PMID:37884748, and Totty et al. 2025, PMID:40961182). The cohort therefore does not represent the biologically appropriate search space, and the surviving candidate — despite carrying "Glut" in its cluster name — was scored without NT-based discrimination.

2. **No precomputed expression data for defining markers.** Expression values for Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 are not available in the CCN20230722 atlas for BLA-adjacent supertypes. Without these values, no marker-based discrimination is possible among the five cohort candidates. All were scored equally (score = 1.0).

3. **Discordant anatomy for the surviving candidate.** CS20230722_SUPT_0005 distributes predominantly to striatum and cortical subplate; only 2.2% of cells fall in MBA:1105 (Intercalated amygdalar nucleus). This is weak anatomical support for a basal amygdala principal neuron population, and the intercalated nucleus is not the basal nucleus.

4. **Activity-gated definition without a stable molecular signature.** The extinction neuron is operationally defined by its behaviour during fear extinction and by its reciprocal mPFC connectivity. While McCullough et al. 2016 identified a candidate molecular signature (Ntsr2/Dkk3/Rspo2/Wnt7a), this has not been cross-validated against a modern single-nucleus RNA-seq dataset covering the mouse BLA at cluster resolution.

5. **No annotation transfer evidence.** No AnnotationTransferEvidence exists for this node. There are no F1 scores, no source labels, and no AT run has been applied.

6. **No prior SSSOM mapping.** This classical type has no existing validated mapping to any atlas accession. The current report represents the first attempt at transcriptomic assignment.

---

## Proposed experiments

1. **Re-run candidate discovery with a glutamatergic NT filter.** Once precomputed expression data for Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 becomes available for CCN20230722 BLA-adjacent clusters, re-run `just find-candidates` at rank 0 and rank 1 using a glutamatergic (not GABAergic) NT constraint. Target at least CONSISTENT or APPROXIMATE alignment on 3 of 5 defining markers to elevate any candidate to MODERATE confidence.

2. **Annotation transfer from a Ntsr2-Cre or Thy1-eYFP BLA single-nucleus dataset.** Use a published Ntsr2-Cre or Thy1-eYFP BLA neuronal transcriptomics dataset (mouse) as the AT source against WMBv1 (CCN20230722). An F1 ≥ 0.60 at supertype level would identify the transcriptomic cluster(s) housing Fear-Off neurons and provide the first Tier B or Tier A evidence for this mapping.

3. **Search for TRAP-seq or activity-seq data from BLA extinction experiments.** Published Fos-TRAP or activity-sequencing profiling of BLA neurons during fear extinction would allow direct assessment of overlap with the McCullough 2016 Ntsr2/Dkk3/Rspo2/Wnt7a signature. If such a dataset exists, the resulting gene expression profile should be compared against CCN20230722 cluster-level centroids.

---

## Verdict block

---
<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:UnreviewedManualMapping
  rationale: >
    [tier:UNCERTAIN] The basal amygdala extinction neuron is a well-characterised
    glutamatergic principal neuron of the BA defined by its Ntsr2/Dkk3/Rspo2/Wnt7a
    molecular signature (McCullough et al. 2016) and its Fear-Off behavioural identity.
    The sole candidate edge (CS20230722_SUPT_0005) was generated under an incorrect
    GABAergic NT filter and carries no expression data for any of the five defining
    markers. Region support is strongly discordant: the supertype's dominant distribution
    is in striatum and cortical subplate, with only 2.2% of cells in the intercalated
    amygdalar nucleus — not the basal nucleus. No annotation transfer evidence exists.
    The mapping is unresolved pending re-discovery under a glutamatergic filter with
    marker expression data.
  reconciliation_note: >
    This candidate should be treated as a placeholder only. A new candidate discovery
    run is required using a glutamatergic NT filter; the current cohort was generated
    under an erroneous GABAergic constraint. Once precomputed expression data for Ntsr2
    is available in CCN20230722 BLA-adjacent clusters, marker-based discrimination will
    be possible. Until then, no mapping verdict can be assigned with confidence above
    UNCERTAIN.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: No precomputed expression data exists for the defining markers (Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1) in BLA-adjacent supertypes of CCN20230722; marker-based discrimination between cohort candidates was not possible.
    - caveat_type: DISCORDANT_ANATOMY
      description: CS20230722_SUPT_0005 has only 2.2% of its cells in MBA:1105 (Intercalated amygdalar nucleus); the dominant distribution is in striatum/cortical subplate, which is inconsistent with a basal nucleus principal neuron.
    - caveat_type: OTHER
      description: The classical type is defined by activity-gated behaviour and mPFC connectivity, not by a validated stable molecular signature; transcriptomic atlas mapping is intrinsically uncertain until cross-validated against a modern single-nucleus BLA dataset.
    - caveat_type: OTHER
      description: Candidate generation was run under a GABAergic NT filter; the extinction neuron is glutamatergic; the cohort does not represent the correct search space.
  proposed_experiments:
    - Re-run candidate discovery at CCN20230722 rank 0 and rank 1 with a glutamatergic NT filter once precomputed expression data for Ntsr2, Dkk3, Rspo2, Wnt7a, and Thy1 is available for amygdala-adjacent clusters; target CONSISTENT or APPROXIMATE alignment on ≥3 of 5 markers to elevate any candidate to MODERATE confidence.
    - Perform annotation transfer from a Ntsr2-Cre or Thy1-eYFP BLA single-nucleus transcriptomics dataset against WMBv1; F1 ≥ 0.60 at supertype level would provide initial Tier B evidence for cluster assignment.
    - Search published literature for Fos-TRAP or activity-sequencing profiling of BLA neurons during fear extinction and assess overlap with the McCullough 2016 Ntsr2/Dkk3/Rspo2/Wnt7a signature.
  unresolved_questions:
    - Does a molecularly distinct transcriptomic cluster exist for BLA extinction neurons, or do they represent a transient activity state within the broader BLA glutamatergic principal neuron population?
    - Has the McCullough 2016 Ntsr2/Rspo2/Dkk3/Wnt7a molecular signature been independently replicated in a subsequent single-nucleus or single-cell RNA-seq study of the mouse BLA?
    - Is the NT filter discrepancy (GABAergic filter applied to a glutamatergic classical type) a metadata error in the KB YAML or in the candidate generation configuration, and has it propagated to other BLA principal neuron nodes?
```
<!-- verdict-block-end -->
