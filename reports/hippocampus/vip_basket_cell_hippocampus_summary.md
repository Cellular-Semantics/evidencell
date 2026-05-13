# VIP-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The VIP-positive basket cell is a hippocampal GABAergic interneuron class first characterised as a discrete population providing perisomatic inhibition to CA1 pyramidal neurons via asynchronous GABA release, and notably distinguished from interneuron-selective (IS) VIP+ cells which target other interneurons rather than pyramidal somata. Establishing its transcriptomic counterpart in WMBv1 matters because Vip expression alone is shared across multiple hippocampal interneuron subtypes, so atlas-side resolution depends on additional markers and connectivity information that the atlas metadata does not yet carry.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] (stratum pyramidale) | — |
| NT | GABAergic | — |
| Markers | Vip | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

No per-property structured `PropertySource` entries are recorded on the classical node. The node was created as a cite-traverse stub citing Tyan et al. 2014 (PMID:24671999) as the primary functional characterisation; that reference has not yet been ingested into the regional `references.json` index.
</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed; the mapping is classified UNCERTAIN because Vip Gaba_7 (0179) [CS20230722_SUPT_0179] is the leading transcriptomic correspondent for the Yao 2021 SSv4 Vip subclass but cannot be resolved against IS interneurons without additional markers.

![Filtered AT figure for VIP-positive basket cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_vip_basket_cell_hippocampus.png)

*F1 across taxonomy levels for the 1 source group (Yao 2021 SSv4 `Vip`) relevant to the VIP-positive basket cell. Nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.* The Vip subclass mapping is clean at SUBCLASS rank (046 Vip Gaba, F1=0.969) but fragments across multiple supertypes at rank 1, reflecting that the source SSv4 `Vip` label pools VIP basket, IS cells, and other VIP interneuron subtypes (see caveats).

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | — | 215 | ⚪ UNCERTAIN | Vip CONSISTENT · location APPROXIMATE | Eliminated |

Total edges: 1 (relationship type: UNCERTAIN).

The mapping is not refuted on expression grounds — Vip is a DEFINING marker on SUPT_0179 with precomputed mean 6.82 — but is shared with the IS interneuron classical type, making the assignment ambiguous rather than wrong.

---

## Eliminated candidates

Primary disqualifying signal: SUPT_0179 (Vip Gaba_7) is co-claimed by IS interneurons; atlas metadata cannot discriminate VIP basket from IS identity.

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · ⚪ UNCERTAIN (215 cells)

**Property alignment**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA (Vip Gaba subclass) | not assessed | CONSISTENT |
| Soma location (stratum pyramidale) | stratum pyramidale (SOMA) | CA1 pyramidal layer (11 cells); CA3 pyramidal layer (23 cells) | not assessed | APPROXIMATE |
| Vip expression | Vip — defining marker | Vip — DEFINING marker in SUPT_0179; precomputed stats mean: 6.82 | not assessed | CONSISTENT |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + anatomy | Atlas metadata | PARTIAL | Vip DEFINING (mean 6.82); CA1 SP 11 / CA1 SO 24; CA3-enriched | atlas-internal |
| Yao 2021 SSv4 → WMBv1 MapMyCells AT | Annotation transfer | PARTIAL | F1=0.379 at SUPERTYPE; F1=0.969 at SUBCLASS (046 Vip Gaba) | atlas-internal |

**Disqualifying / partial evidence**

- Vip is confirmed as a DEFINING marker on SUPT_0179 (precomputed mean 6.82) — consistent with the classical marker profile but not specific: subclass 046 Vip Gaba spans many Vip+ types.
- Atlas anatomy includes CA1 pyramidal layer (only 11 cells) and CA1 stratum oriens (24 cells); the bulk of SUPT_0179 cells sit in CA3 (pyr 23, SO 25, SR 17, lucidum 11). *(note: CA3 vs CA1 is hippocampal-adjacent — soma in CA3 stratum pyramidale is not a distant region, but it is a different subfield from the classical type's CA1 description; this weakens but does not refute the mapping.)*
- MapMyCells AT: Vip cells map cleanly to SUBC_046 (F1=0.969). At supertype level F1 splits roughly equally across SUPT_0179 (F1=0.379, 96 cells, target_purity=0.970) and SUPT_0177 Vip Gaba_5 (F1=0.397, 101 cells), consistent with the source `Vip` label being a mixture rather than a pure basket-cell population.

**Marker evidence provenance**

- **Vip**: defining marker on the classical node, listed without a structured `PropertySource`. The node's prose notes cite Tyan et al. 2014 (PMID:24671999) as the primary characterisation, but that citation is not yet ingested into the regional references index, so no `[n]` label is available here. Atlas-side, Vip is annotated as DEFINING in SUPT_0179 metadata and the precomputed stats mean (6.82) confirms robust transcript-level expression — no atlas annotation/expression discrepancy. *(Recommendation: targeted cite-traverse for discriminating markers between VIP basket and IS cells, e.g. Cnr1, Calb2, Reln; ingest Tyan et al. 2014 as a structured reference with quote_key.)*

**Concerns**

- **Ambiguous mapping (AMBIGUOUS_MAPPING caveat):** SUPT_0179 is the leading candidate not only for the VIP-positive basket cell but also for IS interneurons (calretinin/VIP+ interneuron-selective cells). Without additional markers (e.g. Cnr1 for basket identity, Calb2 for IS identity), atlas metadata alone cannot resolve which physiological population the supertype represents.
- **Single-study evidence base (SINGLE_STUDY caveat):** VIP basket cells are described in a single primary characterisation; the classical type sits on a thin evidence base.
- **Low CA1 cell count (LOW_CELL_COUNT caveat):** Only 11 SUPT_0179 cells fall in the CA1 pyramidal layer, limiting the spatial confidence of any CA1-specific mapping.
- Location APPROXIMATE with CA3-enrichment in `notes` *(adjacent region — could reflect registration boundary error or a genuine CA3 contribution to the supertype; weak counter-evidence, but indicates the supertype is not narrowly CA1.)*

**What would upgrade confidence**

- **MapMyCells AT with a morphologically-resolved VIP-IN source dataset** (e.g. Patch-seq or RNA-seq from morphologically reconstructed VIP basket vs. IS cells). Target: F1 ≥ 0.80 at SUPERTYPE with VIP basket clearly preferring SUPT_0179 over SUPT_0177. Expected output: `AnnotationTransferEvidence` with a basket-cell-specific source label.
- **LiteratureEvidence** for discriminating markers (Cnr1, Calb2, Reln, or others) on classical VIP basket vs. IS cells, ingested with structured `PropertySource` entries on the classical node. This is a literature gap that does not require new experiments.
- **Spatial transcriptomics** (e.g. MERFISH) at sub-supertype resolution showing the CA1 stratum pyramidale fraction of SUPT_0179 carries a different marker profile from the CA3-enriched fraction.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The VIP-positive basket cell node sits on a CLASSICAL_MULTIMODAL basis: Vip as a defining marker, GABAergic NT type, and soma in pyramidal layer of CA1 [UBERON:0014548]. The node was created as a cite-traverse stub on 2026-04-10 citing Tyan et al. 2014 (PMID:24671999) as the primary functional characterisation; references have not yet been ingested into the regional `references.json` index.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 SSv4 Vip subclass label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:17+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** VIP-positive basket cell → 0179 Vip Gaba_7 [CS20230722_SUPT_0179] at UNCERTAIN confidence. Key support: Vip CONSISTENT as DEFINING marker (precomputed mean 6.82) plus MapMyCells AT (Yao 2021 SSv4 Vip → SUPT_0179 F1=0.379 at SUPERTYPE, F1=0.969 at SUBCLASS 046 Vip Gaba). Key caveats: AMBIGUOUS_MAPPING (shared with IS interneurons), SINGLE_STUDY evidence base, and LOW_CELL_COUNT in CA1 pyramidal layer (11 cells).

No Cell Ontology term currently assigned. The classical type is a candidate for a new CL term once a discriminating marker profile (vs. IS interneurons) has been established.

### Proposed experiments and follow-ups

A Yao 2021 SSv4 MapMyCells AT has already been run; it resolved the SUBCLASS-level placement (SUBC_046 Vip Gaba, F1=0.969) but did not discriminate basket from IS at supertype level because the source `Vip` subclass label pools both populations. The refined version of the experiment is therefore the natural next step.

- **What:** MapMyCells annotation transfer using a morphologically-resolved VIP interneuron dataset (Patch-seq or sorted VIP-IN single-cell RNA-seq with basket vs. IS labels).
- **Target:** F1 ≥ 0.80 at SUPERTYPE level for the basket-cell source label, with the basket label preferring SUPT_0179 over SUPT_0177 (or vice versa).
- **Expected output:** `AnnotationTransferEvidence` keyed to the new source dataset, distinguishing basket from IS within the Vip subclass.
- **Resolves:** the AMBIGUOUS_MAPPING caveat on edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 and the parallel mapping uncertainty on the IS interneuron node.

- **What:** Targeted literature curation for discriminating markers (Cnr1, Calb2, Reln, etc.) on classical VIP basket vs. IS cells.
- **Target:** at least one primary study per marker confirming morphology-validated basket-cell identity.
- **Expected output:** `LiteratureEvidence` with structured `PropertySource` entries on the classical node; ingest Tyan et al. 2014 (PMID:24671999) as the foundational reference.
- **Resolves:** the SINGLE_STUDY caveat and the marker-provenance gap noted above.

### Open questions

No `unresolved_questions[]` are recorded on the edge. The questions raised implicitly by the caveats — (1) which discriminating markers separate VIP basket from IS cells in WMBv1, (2) whether SUPT_0179's CA3-enriched bulk reflects a distinct subpopulation from the CA1 stratum pyramidale fraction, and (3) which classical type (basket vs. IS) should hold the primary claim on SUPT_0179 — are addressed by the proposed experiments above.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|

*No structured references are present in `facts.reference_index` for this node. The Tyan et al. 2014 (PMID:24671999) primary characterisation cited in the classical node's prose notes has not yet been ingested into `references/hippocampus/references.json`; once ingested it should be linked from the Vip defining marker and from the node's `definition_references`.*
