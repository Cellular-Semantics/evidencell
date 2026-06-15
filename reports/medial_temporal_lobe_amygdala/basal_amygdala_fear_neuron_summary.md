# Basal amygdala fear neuron — CCN20230722 Mapping Report
*2026-05-28 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Basal amygdala fear neurons are functionally defined principal neurons of the basal nucleus of the amygdala (basolateral amygdala, BLA) [UBERON:0002887] whose activity is triggered by conditioned stimuli during fear expression [1][2].

> Recent advances in neuroscience give us a better view of the inner structure of the amygdala, of its relations with other regions in the Medial Temporal Lobe (MTL) and of the prominent role of neuromodulation. They have particularly shed light on two kinds of neurons in the basal nucleus of the amygdala, the so-called fear neurons and extinction neurons.
> — Carrere & Alexandre 2015, Cell-type diversity maps and specialized functional neuron classes · [1] <!-- quote_key: 14375617_d7af88e4 -->

Fear neurons are paired with extinction neurons as opposing functional populations within the same nucleus [2]. They are classically characterised by their response to conditioned stimuli, their BLA soma location, and their glutamatergic identity [3]; however, no molecular markers have been established that uniquely identify this population at the transcript level in the current KB node. This absence of defining molecular markers represents the central obstacle for atlas mapping at this time.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Basal nucleus of the amygdala (basolateral amygdala) [UBERON:0002887] | [1][2] |
| Neurotransmitter type | Glutamatergic | [3] |
| Defining markers | None documented | — |
| Negative markers | None documented | — |
| Neuropeptides | None documented | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** Literature review · Basal nucleus of the amygdala · [1]

  > Recent advances in neuroscience give us a better view of the inner structure of the amygdala, of its relations with other regions in the Medial Temporal Lobe (MTL) and of the prominent role of neuromodulation. They have particularly shed light on two kinds of neurons in the basal nucleus of the amygdala, the so-called fear neurons and extinction neurons.
  > — Carrere & Alexandre 2015, Cell-type diversity maps and specialized functional neuron classes · [1] <!-- quote_key: 14375617_d7af88e4 -->

- **Soma location:** Literature review · BLA principal neurons · [2]

  > With respect to fear expression, BLA principal neurons can be divided into two functionally distinct, non-overlapping populations. Activation of "fear" neurons is triggered by the conditioned stimulus, while "extinction" neurons become active only after repetitive presentations of the conditioned stimulus that are not followed by the unconditioned stimulus (Herry et al., 2008). Both types of neurons project to the mPFC but only extinction neurons receive reciprocal input from the mPFC, which makes their activity susceptible to mPFC modulation (Herry et al., 2008).
  > — Cardenas et al. 2019, Basal amygdala fear neurons and extinction neurons · [2] <!-- quote_key: 4940771_cb8fa215 -->

- **Neurotransmitter type:** Literature · BLA glutamatergic composition · [3]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

A complete scan of CCN20230722 GABAergic supertypes with representation in the basolateral amygdala region (MBA:295, proximity 100 µm) returned five candidates at supertype rank (rank 1), all scoring equally (score = 1.0). No marker-based discrimination was possible: the basal amygdala fear neuron node currently carries no defining molecular markers, preventing any expression-based ranking or alignment. The single top-ranked candidate, 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005], has only 2.2% of its cells in the BLA-adjacent intercalated amygdalar nucleus (MBA:1105), with the dominant representation in striatum and cortical subplate — a poor anatomical match. No annotation transfer evidence and no literature-evidence mapping are available for this node. No candidates meet the evidence threshold for a supported mapping verdict.

*(note: The BLA [UBERON:0002887] is the primary nucleus targeted in fear-conditioning studies. The WMBv1 intercalated amygdalar nucleus (MBA:1105) and the broader amygdala region (MBA:295) are anatomically adjacent but not synonymous with the classical BLA used in the fear-conditioning literature; the 2.2% regional representation of CS20230722_SUPT_0005 in MBA:1105 does not constitute meaningful anatomical alignment.)*

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | — | 798 | ⚪ UNCERTAIN | No molecular markers; poor BLA representation | Eliminated (no defining markers; poor anatomical match) |

*1 edge assessed (rank 1 supertype); 0 survivors.*

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The basal amygdala fear neuron is defined on a `CLASSICAL` basis: soma location in the basal nucleus of the amygdala (BLA) [UBERON:0002887] [1][2], glutamatergic neurotransmitter type [3], and functional identity (conditioned stimulus-triggered activity during fear expression). No molecular markers define this population at the transcript level in the current KB node. The absence of defining_markers is the primary limitation for atlas-level mapping under the CCN20230722 framework.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 1 (supertype) using metadata-based scoring (region match MBA:295/MBA:1105, NT type). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | NO_EVIDENCE | — |

*Generated by evidencell `bfdb7f1` at 2026-06-15T10:48:32+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** No supported mapping. The basal amygdala fear neuron currently lacks the molecular marker profile required for atlas-level transcriptomic assignment. The single candidate returned by the discovery pipeline, 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005], was ranked purely by region proximity with no marker-based discrimination (all five GABAergic amygdala supertypes scored equally at 1.0). Anatomical alignment is poor (2.2% of the supertype in the BLA-adjacent intercalated nucleus). A supported mapping verdict requires first establishing defining molecular markers for this functional population, most likely through activity-dependent transcriptomic profiling of fear-conditioned BLA neurons.

No Cell Ontology term currently assigned. The node is a candidate for a new CL term once molecular characterisation is available.

### Proposed experiments and follow-ups

**Activity-dependent marker discovery (highest priority)**

- **What:** Combine fear conditioning with activity-dependent cell labelling (e.g. TRAP2/Fos-TRAP, CaMKII-IRES-Cre driven by immediate-early gene activation) followed by single-cell RNA sequencing on isolated, labelled BLA neurons.
- **Target:** Identify ≥ 3 molecular markers (transcript-level) that discriminate fear-activated from extinction-activated or non-conditioned BLA principal neurons.
- **Expected output:** Defining markers encoded as `defining_markers[]` on the KB node, enabling re-run of `map-cell-type` and expression-based atlas candidate ranking.
- **Resolves:** All open questions 1 and 2; enables a meaningful atlas mapping pass.

**Neurotransmitter type confirmation**

- **What:** Confirm glutamatergic identity of fear neurons by targeted literature search or primary experiments (in-situ hybridisation for Slc17a7/vGluT1 or Slc17a6/vGluT2 on fear-conditioned cells).
- **Target:** Confirm or refute glutamatergic NT type; update `nt_type` on the KB node if currently misannotated.
- **Expected output:** `nt_type` with a primary citation; enables NT-type-filtered cohort queries in subsequent atlas mapping passes.
- **Resolves:** Open question 2; note also that the current edge's NT comparison references a GABAergic supertype label (STR Prox1 Lhx6 Gaba_3) inconsistent with the SUPT_0005 node name (0005 IT EP-CLA Glut_3 — glutamatergic), which should be resolved by curator review of the discovery pipeline output (open question 3).

### Open questions

1. What molecular markers co-express specifically in fear-conditioned BLA neurons? Activity-dependent labelling + transcriptomics (e.g. Fos-TRAP) would identify defining_markers to enable atlas mapping.
2. Is the glutamatergic NT annotation confirmed by primary literature? Absence of NT type is a fundamental gap for cohort-level filtering.
3. Curator review needed: the NT annotation in the edge property_comparison references a GABAergic label (STR Prox1 Lhx6 Gaba_3) inconsistent with the SUPT_0005 node name (0005 IT EP-CLA Glut_3); this may reflect a discovery pipeline data entry issue.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Carrere & Alexandre 2015 | [25852499](https://pubmed.ncbi.nlm.nih.gov/25852499/) | Soma location |
| [2] | Cardenas et al. 2019 | [31193505](https://pubmed.ncbi.nlm.nih.gov/31193505/) | Soma location; functional definition |
| [3] | Chung et al. 2016 | [27053114](https://pubmed.ncbi.nlm.nih.gov/27053114/) | Neurotransmitter type |

---

<!-- verdict-block-start: edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] No molecular markers are defined on the classical node, preventing
    any expression-based alignment with atlas supertypes. The single discovery-mode
    candidate CS20230722_SUPT_0005 (0005 IT EP-CLA Glut_3) was returned by region
    proximity filter only (all 5 GABAergic amygdala supertypes scored score=1 in a
    cohort of 5, rank 1 tied); anatomical overlap is poor (region_fraction: 0.022
    in MBA:1105, with dominant representation in striatum/cortical subplate). No
    ANNOTATION_TRANSFER evidence and no LITERATURE evidence support this edge.
    Mapping is not possible without first establishing defining molecular markers
    via activity-dependent transcriptomics (e.g. Fos-TRAP + scRNA-seq on
    fear-conditioned BLA neurons). A data entry issue is also flagged: the NT
    property_comparison references a GABAergic supertype label (STR Prox1 Lhx6
    Gaba_3) inconsistent with the SUPT_0005 node name (0005 IT EP-CLA Glut_3 —
    glutamatergic); curator review needed.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No defining molecular markers are recorded on the basal_amygdala_fear_neuron
        node. Without transcript-level markers, atlas candidate scoring relies solely
        on region and NT type, producing a flat, uninformative cohort (all 5 supertypes
        tied at score=1). This is the primary blocker for a supported mapping verdict.
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0005 has only 2.2% of its cells (region_fraction: 0.022) in
        MBA:1105 (intercalated amygdalar nucleus, BLA-adjacent), with dominant
        representation in striatum and cortical subplate. The classical type's soma
        location is the basolateral amygdala (UBERON:0002887); this supertype is not
        BLA-specific.
    - caveat_type: OTHER
      description: >
        The edge property_comparison for nt_type references a GABAergic label (STR
        Prox1 Lhx6 Gaba_3) inconsistent with SUPT_0005's own name (0005 IT EP-CLA
        Glut_3, glutamatergic). This appears to be a discovery pipeline data entry
        issue. Curator review is needed before re-running the mapping query.
  proposed_experiments:
    - >
      Activity-dependent labelling (Fos-TRAP2 or CaMKII-driven IEG reporter) combined
      with single-cell RNA sequencing on fear-conditioned BLA neurons to identify ≥ 3
      transcript-level defining markers for the fear neuron population. Encode results
      as defining_markers[] on the KB node; re-run map-cell-type at rank 0 and rank 1.
    - >
      Confirm glutamatergic identity (Slc17a7/Slc17a6 expression) by targeted ISH or
      re-analysis of available BLA transcriptomic datasets; update nt_type with a
      primary citation.
    - >
      Curator review of the discovery pipeline output: resolve the NT-label discrepancy
      (GABAergic label vs. glutamatergic SUPT name) for edge
      edge_basal_amygdala_fear_neuron_to_cs20230722_supt_0005 before next mapping run.
  unresolved_questions:
    - >
      What molecular markers co-express specifically in fear-conditioned BLA neurons?
      Activity-dependent labelling + transcriptomics (e.g. Fos-TRAP) would identify
      defining_markers to enable atlas mapping.
    - >
      Is the glutamatergic NT annotation confirmed by primary literature? Absence of a
      confirmed NT type is a fundamental gap for cohort-level filtering.
    - >
      Curator review needed: NT annotation in the edge property_comparison references a
      GABAergic label (STR Prox1 Lhx6 Gaba_3) inconsistent with SUPT_0005 node name
      (0005 IT EP-CLA Glut_3); may reflect a discovery pipeline data entry issue.
```
<!-- verdict-block-end -->
