# Cell Type Mapping Report: basal_amygdala_fear_neuron
*Basal amygdala fear neuron · glutamatergic · basolateral amygdala (UBERON:0002887)*

Fear neurons are a functionally defined subpopulation of principal neurons in the basal nucleus of the amygdala (BA) that are selectively activated by a conditioned stimulus (CS+) and whose activity drives the expression of conditioned fear responses. They are paired with a non-overlapping population of extinction neurons that become active only after repeated CS presentations without an unconditioned stimulus.

> With respect to fear expression, BLA principal neurons can be divided into two functionally distinct, non-overlapping populations. Activation of "fear" neurons is triggered by the conditioned stimulus, while "extinction" neurons become active only after repetitive presentations of the conditioned stimulus that are not followed by the unconditioned stimulus (Herry et al., 2008). Both types of neurons project to the mPFC but only extinction neurons receive reciprocal input from the mPFC, which makes their activity susceptible to mPFC modulation (Herry et al., 2008).
> — Cardenas et al. 2019, Basal amygdala fear neurons and extinction neurons  <!-- quote_key: 4940771_cb8fa215 -->

No CL term mapping is currently recorded for this node, and no new CL term has been proposed.

---

## Candidate atlas types

| Candidate | Relationship | Confidence | Key evidence | Region support |
|---|---|---|---|---|
| 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | evidencell:UncertainRelationship | UNCERTAIN | Eliminated: atlas metadata only; anatomy discordant (2.2% in BLA-adjacent territory); NT-label inconsistency in discovery pipeline output | 0.022 |

---

## Evidence gaps

- **MARKER_EXPRESSION**: No defining molecular markers are recorded for this node. Without transcript-level markers, candidate scoring relies solely on region and NT type, producing a flat uninformative cohort (all five supertypes tied at score=1.0). This is the primary blocker for any supported mapping verdict.
- **AT_DATA**: No annotation transfer evidence exists. MapMyCells cannot be applied without a transcriptomically defined source cluster linked to this classical type.
- **LITERATURE**: No quote-key evidence directly asserting molecular identity (e.g., transcription factor expression, neuropeptide co-expression, calcium-binding protein profile) is available for the fear neuron population. The existing literature evidence establishes the functional definition and BLA location but does not discriminate this population from co-residing BLA principal neurons at the molecular level.
- **EPHYS**: No electrophysiology profile is recorded. Fear neurons have been characterised by in vivo firing patterns during conditioning paradigms, but no in vitro patch-clamp profile distinguishing them from other BLA principal neurons is encoded in the KB node.
- **MORPHOLOGY**: No morphology profile is recorded. Fear neurons are presumed to be principal (glutamatergic pyramidal-like) neurons, but this has not been encoded with a primary citation on the node.

---

## Proposed experiments

**1. Activity-dependent transcriptomic labelling of fear neurons**
*Tool*: Fos-TRAP2 knock-in mouse (FosTRAP2;Rosa26-LSL-Sun1-sfGFP) or CaMKII-driven IEG reporter crossed with fear conditioning protocol; alternatively, targeted single-nucleus RNA sequencing on BLA tissue from fear-conditioned animals with activity-tagged nuclei (pS6 or Arc immunolabelling)
*Assay*: Single-cell or single-nucleus RNA sequencing of labelled (TRAP+) BLA neurons; identify ≥3 transcript-level markers enriched in fear-activated vs. extinction-activated neurons; run MapMyCells at cluster level against CCN20230722, requiring F1 ≥ 0.60 at supertype level as a passing threshold
*Expected output*: AnnotationTransferEvidence entries linking basal_amygdala_fear_neuron to one or more atlas clusters; LiteratureEvidence items encoding the identified defining_markers[] on the KB node

**2. Glutamatergic NT-type confirmation by targeted in situ hybridisation**
*Tool*: RNAscope or smFISH probes for Slc17a7 (vGlut1) and Slc17a6 (vGlut2) combined with a fear-neuron activity marker (Fos, Arc) in fear-conditioned mouse BLA
*Assay*: Co-expression analysis of vGlut1/2 and activity marker in basal nucleus neurons; encode result with a primary citation as nt_type on the KB node
*Expected output*: LiteratureEvidence item confirming glutamatergic identity for basal_amygdala_fear_neuron, enabling unambiguous NT-type filtering in the next mapping run

---

## Verdict block

---
<!-- verdict-block-start: edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:UnreviewedManualMapping
  rationale: >
    [tier:CUT] The sole candidate, CS20230722_SUPT_0005 (0005 IT EP-CLA Glut_3), was identified by atlas-metadata survival cohort filtering (region MBA:295, NT=GABAergic) and represents only the top-ranked entry in a five-way tied cohort (all scored 1.0); no marker-based discrimination was possible. The node carries no defining molecular markers, making it impossible to score expression-level concordance against any atlas cluster. CS20230722_SUPT_0005 has only 2.2% of its cells within MBA:1105 (intercalated amygdalar nucleus, BLA-adjacent), with dominant representation in striatum and cortical subplate — this anatomy is strongly discordant with the classical type's basolateral amygdala location (UBERON:0002887). Additionally, the discovery pipeline's NT-type filter referenced a GABAergic label (STR Prox1 Lhx6 Gaba_3) inconsistent with the supertype node name (0005 IT EP-CLA Glut_3, glutamatergic), suggesting a data entry issue that must be resolved before re-running. No AT evidence, no precomputed expression data, and no literature evidence linking this supertype to fear-conditioned BLA neurons exist; the mapping cannot be supported at any confidence level.
  reconciliation_note: >
    This node requires molecular marker annotation before any atlas mapping can be attempted. The priority action is activity-dependent transcriptomic labelling (e.g., Fos-TRAP2) of fear-conditioned BLA neurons to identify defining_markers[]; the NT-label discrepancy in the discovery pipeline output also requires curator review before the next map-cell-type run.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: No defining molecular markers are recorded on the basal_amygdala_fear_neuron node; all five BLA GABAergic supertypes scored equally (1.0), making the cohort uninformative for mapping.
    - caveat_type: DISCORDANT_ANATOMY
      description: CS20230722_SUPT_0005 has only 2.2% of its cells in MBA:1105 (BLA-adjacent intercalated nucleus), with dominant representation in striatum and cortical subplate; this is strongly discordant with the classical type's basolateral amygdala location.
    - caveat_type: OTHER
      description: The discovery pipeline NT-type filter referenced a GABAergic label (STR Prox1 Lhx6 Gaba_3) inconsistent with the supertype name (0005 IT EP-CLA Glut_3, glutamatergic); curator review of this data entry issue is required.
  proposed_experiments:
    - Activity-dependent labelling (Fos-TRAP2) combined with single-cell RNA sequencing of fear-conditioned BLA neurons to identify ≥3 defining transcript-level markers; encode as defining_markers[] on the KB node and re-run map-cell-type.
    - Targeted ISH (RNAscope) for Slc17a7/Slc17a6 with an activity marker (Fos or Arc) in fear-conditioned BLA tissue to confirm glutamatergic identity and resolve the NT-type annotation gap.
  unresolved_questions:
    - What transcript-level markers co-express specifically in fear-conditioned BLA neurons, and do they discriminate this population from extinction neurons or other co-residing BLA principal neurons?
    - Is the glutamatergic NT annotation supported by primary literature with a citable PMID, and does the discovery pipeline NT-filter reflect the correct supertype NT type?
    - Can the fear neuron population be distinguished from the broader BLA glutamatergic principal neuron class at the transcriptomic level, or is it a purely functional subdivision of a single molecular type?
```
<!-- verdict-block-end -->
