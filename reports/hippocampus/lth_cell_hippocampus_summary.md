# Low-threshold high-Ih (LTH) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The low-threshold high-Ih (LTH) cell is a putative CA1 stratum oriens
GABAergic interneuron defined exclusively by physiological clustering of
SST-Cre Ai14 labelled cells (strong spike frequency adaptation, prominent
hyperpolarization-activated Ih) in a single study [1]. No morphological
reconstruction or molecular markers beyond Sst-Cre labelling have been
reported. Mapping this electrophysiology-only definition to a single-cell
transcriptomic atlas is intrinsically speculative — LTH may correspond to a
distinct transcriptomic type, or may be a physiological state/variant
within an existing Sst+ hippocampal interneuron type (e.g. OLM,
oriens-oriens, hippocampo-septal) rather than a separate type altogether.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Markers | Sst (Sst-Cre labelling only) | [1] |

Cell Ontology mapping: No Cell Ontology term currently covers this type —
candidate for a new CL term.

---

## Results

A single candidate atlas mapping was assessed and classified as UNCERTAIN
(eliminated as a primary mapping): 0219 Sst Gaba_6 [CS20230722_SUPT_0219].
The candidate sits within the Sst Gaba subclass (consistent with Sst-Cre
labelling) but its anatomy (CA3-enriched, no CA1 stratum oriens cells) is
discordant with the CA1 stratum oriens description of LTH cells, and the
underlying annotation-transfer signal derives from a Sst subclass that
mixes multiple morphologically distinct Sst+ hippocampal interneuron
types.

**Annotation-transfer overview figure (run-level, filtered).**

![Filtered AT figure for Low-threshold high-Ih (LTH) cell — Yao 2021 Sst SSv4 source](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_lth_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 SSv4 'Sst' source group from
GSE185862 mouse hippocampal formation (n=273 HIP cells). The Sst subclass
maps cleanly at subclass resolution (F1 = 0.983 to 053 Sst Gaba) and
resolves at supertype level to 0219 Sst Gaba_6 [CS20230722_SUPT_0219]
(F1 = 0.759, group_purity 0.626, target_purity 0.964). The Yao 2021 'Sst'
label is morphologically unresolved and mixes OLM, bistratified,
hippocampo-septal, oriens-oriens and other Sst+ interneuron types — so the
supertype landing cannot be attributed to LTH cells specifically without
an LTH-targeted source dataset.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — (supertype) | 1495 | ⚪ UNCERTAIN | Sst CONSISTENT · CA1 SO DISCORDANT | Eliminated |

Total edges: 1 (1 UNCERTAIN); relationship UNCERTAIN.

## Eliminated candidates

Shared disqualifying signal: the only candidate edge fails on anatomical
location (no CA1 stratum oriens cells in SUPT_0219; the supertype is
CA3-enriched) while the LTH definition pins the soma to CA1 stratum
oriens. The annotation-transfer signal that motivates this candidate is
derived from a Sst subclass that mixes multiple Sst+ hippocampal
interneuron types, so the supertype landing cannot be attributed to LTH
specifically.

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] · ⚪ UNCERTAIN

n_cells (10x): 1495

**Disqualifying evidence**
- Anatomy DISCORDANT: SUPT_0219 has 305 cells in CA3 stratum oriens and
  zero cells in CA1 stratum oriens; the LTH definition specifies CA1
  stratum oriens soma. *(distant region within the hippocampal formation
  — CA3 SO vs CA1 SO are different subfields; this is the main
  anatomical weakness of this candidate.)*
- ELECTROPHYSIOLOGY_ONLY_DEFINITION: the LTH classical type is defined
  exclusively by physiological clustering of SST-Cre Ai14 cells [1]. No
  morphological reconstruction or molecular markers beyond Sst-Cre
  labelling have been published; the transcriptomic identity is
  therefore unconstrained beyond "Sst-subclass" and the assignment to
  SUPT_0219 rather than another Sst supertype (e.g. SUPT_0216, the
  primary OLM target) is speculative.
- SINGLE_STUDY: single-study, single-lab evidence for LTH as a distinct
  cell type. Classification stability across datasets has not been
  established.
- AMBIGUOUS_MAPPING: LTH cells may overlap with OLM cells (both Sst+,
  CA1 stratum oriens soma) at the transcriptomic level; if so, SUPT_0216
  (the OLM-mapping Sst supertype) would be the correct target rather
  than SUPT_0219. The current SUPT_0219 assignment is a placeholder
  pending molecular characterisation.

**Supporting signal (weak)**
- Sst CONSISTENT: SUPT_0219 lists Sst as a DEFINING marker with
  precomputed mean expression 10.17, consistent with the Sst-Cre
  labelling that originally identified LTH cells [1].
- NT type CONSISTENT: SUPT_0219 is in the Sst Gaba subclass — GABAergic,
  matching the LTH classical type.
- Yao 2021 (GEO:GSE185862) SSv4 'Sst' subclass annotation transfer
  (n=273 HIP cells) places SUPT_0219 as the dominant supertype target
  (F1 = 0.759, 161/273 cells). However, the Yao 2021 'Sst' label is
  morphologically unresolved and encompasses multiple Sst interneuron
  types (OLM, bistratified, hippocampo-septal, oriens-oriens, and
  others); the SUPT_0219 landing cannot be attributed to LTH
  specifically.

**What would upgrade confidence**
- An LTH-targeted scRNA-seq or patch-seq dataset (cells matching the LTH
  electrophysiological signature: strong spike frequency adaptation +
  high Ih in SST-Cre Ai14 CA1 stratum oriens) with subsequent annotation
  transfer to WMBv1. Target: F1 ≥ 0.80 at CLUSTER level on a specific
  Sst supertype, with the candidate cluster carrying CA1 stratum oriens
  anatomy. Expected output: AnnotationTransferEvidence on the candidate
  edge.
- Targeted literature search for any subsequent publication that has
  morphologically reconstructed LTH cells or assigned them molecular
  markers beyond Sst-Cre labelling. This would constrain the candidate
  set substantially.
- Side-by-side comparison of LTH electrophysiology against OLM and
  oriens-oriens electrophysiology in the same dataset, to test whether
  LTH is a distinct type or a physiological variant within an existing
  type.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The LTH cell is defined here on a
CLASSICAL_MULTIMODAL basis but the multimodal evidence is in practice
single-modality: physiological clustering of SST-Cre Ai14 labelled cells
in CA1 stratum oriens, identifying a population with strong spike
frequency adaptation and prominent hyperpolarization-activated Ih [1]. No
morphological reconstruction or molecular markers beyond Sst-Cre
labelling have been reported.

**Atlas mapping query.**

Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722)
taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based
scoring (region match, NT type, defining markers, sex bias when
applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**

Each defining property of the classical type was compared to the
corresponding atlas-side value via the `property_comparisons` schema,
with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed
expression on the cluster (cluster.yaml in the taxonomy reference store)
and from MERFISH spatial registration for soma location.

**Annotation transfer.**

Yao 2021 SSv4 hippocampal formation → WMBv1 (supporting signal; not
LTH-specific):

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 Allen Institute taxonomy labels) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations). Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.**

All citations, atlas accessions, ontology CURIEs, and verbatim literature
quotes in this report are validated against the evidencell knowledge base
at write time. Authored-prose evidence narratives are validated against
their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:15+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_lth_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA; ANNOTATION_TRANSFER | WEAK; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** No primary mapping is supported. The LTH cell does
not have a confidently mappable atlas correspondent at present: the
single assessed candidate (0219 Sst Gaba_6 [CS20230722_SUPT_0219]) is
UNCERTAIN, with the CA1 stratum oriens classical anatomy DISCORDANT with
the CA3-enriched SUPT_0219 atlas distribution, and the underlying
annotation transfer drawn from a morphologically unresolved Sst subclass.
Key caveats: ELECTROPHYSIOLOGY_ONLY_DEFINITION (single-study,
single-modality physiological definition with no molecular characterisation
beyond Sst-Cre labelling), DISCORDANT_ANATOMY (no CA1 stratum oriens cells
in SUPT_0219), SINGLE_STUDY, and AMBIGUOUS_MAPPING (potential overlap with
OLM or oriens-oriens cells).

No Cell Ontology term currently assigned. The LTH cell is a candidate for
CL contribution only once a more constrained molecular/morphological
definition is in place — at present the electrophysiology-only definition
does not support a dedicated CL term.

### Proposed experiments and follow-ups

**Cross-check with existing AT evidence.** The only annotation-transfer
run that touches this node is Yao 2021 SSv4 'Sst' (n=273 HIP cells), which
is a Sst-subclass-level signal that mixes multiple morphologically distinct
Sst+ hippocampal interneuron types and so cannot be attributed to LTH
cells specifically. A refined LTH-targeted AT experiment is therefore not
already covered by existing evidence.

1. **LTH-targeted scRNA-seq / patch-seq → MapMyCells.**
   - What: patch-seq or fate-mapped scRNA-seq of CA1 stratum oriens
     SST-Cre Ai14 cells exhibiting the LTH electrophysiological signature
     (strong spike frequency adaptation + high Ih), with subsequent
     MapMyCells annotation transfer to WMBv1.
   - Target: F1 ≥ 0.80 at CLUSTER level on a Sst supertype whose atlas
     anatomy includes CA1 stratum oriens.
   - Expected output: AnnotationTransferEvidence on the candidate edge.
   - Resolves: the speculative SUPT_0219 assignment, the
     ELECTROPHYSIOLOGY_ONLY_DEFINITION gap (by adding transcriptomic
     constraints), and the AMBIGUOUS_MAPPING caveat (by distinguishing
     LTH from OLM and oriens-oriens at the cluster level).

2. **Targeted literature search for post-2021 LTH characterisation.**
   - What: cite-traverse and keyword search for any subsequent
     publication that has morphologically reconstructed LTH cells,
     assigned them molecular markers beyond Sst-Cre, or replicated the
     physiological clustering in an independent dataset.
   - Target: at least one independent primary study with morphology or
     molecular markers for LTH cells.
   - Expected output: LITERATURE evidence on the classical node;
     potential additional candidate edges if molecular markers narrow
     the atlas search.
   - Resolves: the SINGLE_STUDY caveat.

3. **Side-by-side electrophysiological comparison of LTH vs OLM vs
   oriens-oriens cells.**
   - What: dataset that records all three Sst+ CA1 stratum oriens
     populations under matched conditions, with cluster-membership
     assignment to LTH using the original electrophysiological criteria.
   - Target: test whether LTH is a distinct type or a physiological
     variant within an existing Sst+ type.
   - Expected output: refined or retracted LTH classical-type
     definition; this would either upgrade LTH to a robust standalone
     classical type or merge it into an existing type's notes.
   - Resolves: the AMBIGUOUS_MAPPING caveat and the underlying question
     of whether LTH is a type at all.

### Open questions

No `unresolved_questions[]` entries are recorded on the edge; the open
questions are implicit in the caveats and are folded into the proposed
experiments above.

1. Is the LTH electrophysiological signature attached to a distinct
   transcriptomic type, or to a physiological state/variant within an
   existing Sst+ CA1 stratum oriens type (OLM, oriens-oriens,
   hippocampo-septal)? (From the ELECTROPHYSIOLOGY_ONLY_DEFINITION and
   AMBIGUOUS_MAPPING caveats.)
2. If LTH is a distinct transcriptomic type, which Sst supertype does it
   correspond to — SUPT_0216 (OLM-associated), SUPT_0219 (the current
   speculative target, CA3-enriched), or another? (From the
   DISCORDANT_ANATOMY caveat on the current SUPT_0219 edge.)
3. Has the LTH classification been replicated outside Hewitt et al. 2021
   in any subsequent dataset? (From the SINGLE_STUDY caveat.)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hewitt et al. 2021 | [33991454](https://pubmed.ncbi.nlm.nih.gov/33991454) | soma location |
