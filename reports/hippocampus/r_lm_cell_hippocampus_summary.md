# Radiatum-lacunosum moleculare (R-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The Radiatum-lacunosum moleculare (R-LM) cell is a GABAergic hippocampal
interneuron with soma in CA1 stratum oriens, originally described in GIN
transgenic mice by Oliva et al. 2000 [2]. R-LM cells were identified on
the basis of somatostatin (Sst) expression and a morphology projecting
to the stratum radiatum/lacunosum-moleculare boundary, and have not been
characterised transcriptomically in a subsequent dedicated study. The
mapping of this classical type to the WMBv1 taxonomy is therefore
inherently speculative — it is included here primarily to mark the cell
type's position in the literature and to document why transcriptomic
discrimination from co-resident Sst+ stratum oriens types (e.g. OLM) is
not currently possible from atlas metadata alone.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Markers | Sst | [2] |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 stratum oriens · [1]
- **Sst marker:** GIN transgenic labelling, Oliva et al. 2000 · [2]
</details>

**Cell Ontology mapping.** No Cell Ontology term currently covers this
type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed; **0216 Sst Gaba_3
[CS20230722_SUPT_0216] is UNCERTAIN** — the supertype is the most
plausible host of Sst+ stratum oriens interneurons but cannot be
distinguished from the co-resident OLM mapping at this resolution.

![Filtered AT figure for R-LM cell (Yao 2021 Sst subclass to WMBv1)](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_r_lm_cell_hippocampus.png)

*F1 across taxonomy levels for the single source group (Yao 2021 SSv4
"Sst" subclass) relevant to R-LM cell. Each panel row is a source-cell
group; nodes are coloured by F1 with precision (P) and recall (R) shown
inline. The Sst subclass maps cleanly at the SUBCLASS level (F1=0.983)
but disperses across multiple Sst supertypes at SUPERTYPE resolution,
reflecting the heterogeneity of morphologically defined Sst interneuron
types contained within a single transcriptomic subclass label.*

### Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---:|---|---|---|
| — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 2712 | UNCERTAIN | NT + soma + Sst CONSISTENT | Eliminated |

Total edges: 1 (UNCERTAIN, relationship UNCERTAIN).

## Eliminated candidates

The single assessed supertype is eliminated not because of discordant
properties — all three compared properties (NT, soma location, Sst
expression) align — but because the same supertype is the primary
candidate for OLM cells, and no metadata feature in the atlas
distinguishes R-LM from OLM at this resolution.

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] — n_cells (10x) = 2712

Disqualifying / limiting evidence:

- **Ambiguity with OLM mapping:** Sst Gaba_3 is the primary OLM cell
  candidate supertype based on MapMyCells annotation transfer (Chrna2-Cre
  data on the same WMBv1 supertype). R-LM and OLM cells share Sst+
  identity and stratum oriens soma location and cannot be distinguished
  at this supertype level from atlas metadata alone.
- **Single-study basis for R-LM:** The R-LM cell type was described only
  in Oliva et al. 2000 [2] using GIN transgenic labelling, with no
  subsequent transcriptomic characterisation. It may not be a
  transcriptomically separable type from OLM or P-LM cells.
- **No discriminating marker:** No axon-projection or laminar marker
  separating R-LM from OLM is recorded in WMBv1 supertype metadata.
- **Annotation transfer is non-specific:** MapMyCells transfer of the
  Yao 2021 SSv4 "Sst" subclass (n=273 HIP cells) hits
  CS20230722_SUPT_0216 with F1=0.488 (target_purity=1.0,
  group_purity=0.323) — the source label is a heterogeneous Sst subclass
  containing OLM, bistratified, hippocampo-septal, oriens-oriens, and
  other Sst types, so the AT signal cannot resolve R-LM-specific
  identity. The dominant Sst supertype target in the same run is 0219
  Sst Gaba_6 (F1=0.759), not CS20230722_SUPT_0216.

Supporting (but non-specific) alignment:

- **Soma location CONSISTENT:** CS20230722_SUPT_0216 has strong CA1
  stratum oriens representation (818 cells), consistent with R-LM somata
  in stratum oriens [UBERON:0014552].
- **NT type CONSISTENT:** GABA (Sst Gaba subclass).
- **Sst marker CONSISTENT:** Sst is implicit at the Sst Gaba subclass
  level; precomputed stats mean expression for Sst is 11.44 on
  CS20230722_SUPT_0216 (Reln, Rbp4, Npffr1 are listed as scoped defining
  markers).

What would upgrade (or definitively eliminate) this mapping:

- A morphologically identified Sst-IN reference dataset (e.g. Patch-seq
  with reconstructed R-LM axonal projection to the radiatum/lacunosum
  border) re-run through MapMyCells against WMBv1. AnnotationTransferEvidence
  with F1 >= 0.8 at the SUPERTYPE or CLUSTER level for an R-LM-labelled
  source would establish whether a separable atlas niche exists.
- A targeted literature search for any post-2000 transcriptomic or
  Cre-driver characterisation of R-LM cells (currently the type rests on
  a single 2000 study).
- Higher-resolution review of axonal projection / laminar markers
  available at the cluster (rank 0) level under CS20230722_SUPT_0216,
  paired with the OLM mapping result, to see whether any child cluster
  preferentially carries R-LM-consistent or R-LM-incompatible features.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The R-LM cell is defined as a GABAergic
interneuron with soma in CA1 stratum oriens [UBERON:0014552] [1]
expressing Sst as its defining marker [2]. Definition basis:
CLASSICAL_MULTIMODAL. The classical node notes record this as a
THIN-EVIDENCE stub — the type was described in a single study (Oliva
et al. 2000) using GIN transgenic labelling and has no subsequent
transcriptomic characterisation.

**Atlas mapping query.** Candidate atlas clusters were retrieved from
the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype)
using metadata-based scoring (region match, NT type, defining markers,
sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type
was compared to the corresponding atlas-side value via the
`property_comparisons` schema, with alignments graded CONSISTENT /
APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values
came from precomputed expression on the cluster (cluster.yaml in the
taxonomy reference store) and from MERFISH spatial registration for
soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 SSv4 hippocampal formation, Sst subclass label) |
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

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature
quotes in this report are validated against the evidencell knowledge base
at write time. Authored-prose evidence narratives are validated against
their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:16+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

<details>
<summary>Evidence base table</summary>

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

</details>

</details>

---

## Discussion

**Primary mapping:** No primary mapping is established. R-LM cell →
0216 Sst Gaba_3 [CS20230722_SUPT_0216] is UNCERTAIN. Key (non-specific)
support: Sst+ identity and stratum oriens soma representation
(ATLAS_METADATA), and Sst-subclass AT signal (ANNOTATION_TRANSFER,
F1=0.488 at SUPERTYPE). Key caveats: AMBIGUOUS_MAPPING (same supertype
is the primary OLM candidate), SINGLE_STUDY (Oliva et al. 2000 is the
sole source for R-LM identity), NO_DISCRIMINATING_MARKER.

No Cell Ontology term currently assigned. The classical node is a
thin-evidence stub from a single 2000 study and would need confirmatory
transcriptomic or morphological characterisation before a CL contribution
could be justified.

### Proposed experiments and follow-ups

- **Morphologically resolved Sst-IN reference dataset to MapMyCells.**
  *What:* Patch-seq or morphology-confirmed scRNA-seq targeting Sst+
  stratum oriens cells with axonal reconstructions classifying R-LM vs
  OLM vs bistratified vs hippocampo-septal, run through MapMyCells against
  WMBv1. *Target:* F1 >= 0.80 at SUPERTYPE or CLUSTER level for an
  R-LM-labelled source group. *Expected output:* AnnotationTransferEvidence
  refining (or eliminating) the CS20230722_SUPT_0216 mapping. *Resolves:*
  AMBIGUOUS_MAPPING and NO_DISCRIMINATING_MARKER caveats; current AT run
  (Yao 2021 "Sst" subclass) is too coarse to separate Sst stratum oriens
  types.
- **Targeted literature traversal for post-2000 R-LM cell evidence.**
  *What:* Cite-traverse / focused literature search for any subsequent
  transcriptomic, Cre-driver, or morphology study referencing R-LM
  identity. *Expected output:* LiteratureEvidence and/or refinement of
  the classical node's marker / location fields. *Resolves:* SINGLE_STUDY
  caveat.

### Open questions

1. Is the R-LM cell a transcriptomically separable type, or does it fall
   within an existing OLM / bistratified / hippocampo-septal cluster
   under CS20230722_SUPT_0216?
2. Are there axon-projection or laminar markers (not yet inspected at
   the rank 0 cluster level) that would discriminate R-LM from OLM
   within CS20230722_SUPT_0216?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [2] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst marker |
