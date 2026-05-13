# Pyramidale-lacunosum moleculare (P-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The Pyramidale-lacunosum moleculare (P-LM) cell is a GABAergic, somatostatin (Sst)-expressing hippocampal CA1 interneuron whose soma sits in the pyramidal layer of CA1 (stratum pyramidale) [1]. It was described together with the R-LM cell in a single study (Oliva et al. 2000); the two types differ only in soma laminar position (stratum pyramidale for P-LM, stratum oriens for R-LM) and have not been characterised transcriptomically. The mapping question is whether P-LM corresponds to any resolved WMBv1 supertype or cluster, given its very thin classical evidence base.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] (stratum pyramidale) | — |
| NT | GABAergic | — |
| Markers | Sst (defining) | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Sst (defining marker):** literature · [1]

No verbatim quotes are available in the facts file for this node.
</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed (0219 Sst Gaba_6 [CS20230722_SUPT_0219]); the verdict is UNCERTAIN — the candidate is retained as a placeholder based on the shared Sst+ GABAergic signature, but the atlas anatomy of the candidate (CA3-enriched) is discordant with the CA1 location of the classical type.

![Filtered AT figure for Pyramidale-lacunosum moleculare (P-LM) cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_p_lm_cell_hippocampus.png)

*F1 across taxonomy levels for the 1 source group (Sst) relevant to the P-LM cell. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.* The Yao 2021 SSv4 "Sst" subclass (n=273 HIP cells) maps cleanly at SUBCLASS level (F1=0.983 to the 053 Sst Gaba subclass) and resolves partially at SUPERTYPE (F1=0.759 to 0219 Sst Gaba_6 [CS20230722_SUPT_0219]); subtype-level resolution for a specific Sst interneuron type such as P-LM is not achievable from this aggregated source label.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | 0219 Sst Gaba_6 | 1,495 | ⚪ UNCERTAIN | Sst CONSISTENT · CA1 location DISCORDANT | Eliminated |

Total edges: 1 (UNCERTAIN; relationship UNCERTAIN).

A complete scan of CCN20230722 at the supertype rank did not yield a Sst supertype enriched in CA1 stratum pyramidale matching the P-LM description. The single retained candidate (SUPT_0219) is Sst+ but is CA3-anchored in atlas metadata; the assignment is a weak placeholder rather than a positive mapping. The thin classical record (one study; no transcriptomic characterisation) is the primary limit on tightening this mapping.

---

### 0219 Sst Gaba_6 · ⚪ UNCERTAIN

**Supporting evidence:**
- Atlas metadata: SUPT_0219 is a member of the Sst Gaba subclass and carries Sst as a DEFINING marker (precomputed mean = 10.17), consistent with the P-LM classical type's Sst+ GABAergic identity.
- Annotation transfer (Yao 2021 SSv4 Sst subclass, n=273 HIP cells → WMBv1): SUPT_0219 is the single dominant supertype target for HIP Sst cells (F1=0.759; group purity 0.626; target purity 0.964; 161/273 cells), confirming that SUPT_0219 receives a substantial share of generic hippocampal Sst+ cells.

**Property alignment table — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA (Sst Gaba subclass) | not assessed | CONSISTENT |
| Soma location (stratum pyramidale) | stratum pyramidale [UBERON:0014548] (SOMA) | CA3 pyramidal layer (261 cells); no CA1 pyramidal layer | not assessed | DISCORDANT |
| Sst | Sst — defining marker | Sst — DEFINING marker in SUPT_0219; precomputed stats mean: 10.17 | not assessed | CONSISTENT |

**Property alignment table — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas SST+ subclass; CA3-anchored anatomy | Atlas metadata | WEAK | Sst DEFINING; SUPT_0219 CA3-enriched, no CA1 | atlas-internal |
| Yao 2021 SSv4 Sst → WMBv1 MapMyCells | Annotation transfer | PARTIAL | F1=0.759 (SUPERTYPE); F1=0.983 (SUBCLASS) | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Marker evidence provenance:**
- **Sst (defining):** transcript-level evidence in atlas (precomputed mean = 10.17, well above background) and listed as DEFINING for SUPT_0219; classical citation [1] is a primary anatomical/electrophysiological study (Oliva et al. 2000). No atlas annotation/expression discrepancy. The Sst signature is robust but non-specific — it is shared across all CA1 and CA3 Sst+ interneuron subtypes and therefore cannot, on its own, discriminate P-LM from other Sst+ types.

**Concerns:**
- Soma location DISCORDANT — SUPT_0219 has 261 cells in CA3 pyramidal layer and no CA1 representation, while the P-LM cell is documented in CA1 stratum pyramidale *(note: CA3 and CA1 are different hippocampal subfields with distinct cell-type complements; this is stronger than a boundary-error caveat — the classical P-LM type may still be a subtype of Sst Gaba but is not the SUPT_0219 population specifically.)*
- DISCORDANT_ANATOMY caveat: a CA1-enriched Sst supertype may be a closer match, but the choice of SUPT_0219 was motivated by the unusual stratum pyramidale soma position; the mapping is left as a placeholder pending P-LM-specific data.
- SINGLE_STUDY caveat: P-LM is described in one study (Oliva et al. 2000) and has no transcriptomic characterisation.
- AMBIGUOUS_MAPPING caveat: R-LM and P-LM differ only by soma layer (oriens vs pyramidale) and may represent a single transcriptomic type with variable soma position rather than two distinct types.
- Annotation transfer is informative only at SUBCLASS (F1=0.983) and partially at SUPERTYPE (F1=0.759); the source label "Sst" encompasses OLM, bistratified, hippocampo-septal, oriens-oriens and other Sst+ types, so it cannot resolve P-LM specifically.

**What would upgrade confidence:**
- Targeted AnnotationTransferEvidence from a hippocampal dataset that labels Sst+ interneurons by morphology / soma layer (distinguishing stratum pyramidale–soma cells from stratum oriens–soma cells) — target F1 ≥ 0.80 at SUPERTYPE level for the P-LM-specific subset.
- Targeted LiteratureEvidence: a cite-traverse for studies that revisit the Oliva et al. 2000 P-LM/R-LM distinction (e.g. follow-up morphological or molecular characterisation) — this is the most cost-effective gap to address, given the SINGLE_STUDY and AMBIGUOUS_MAPPING caveats.
- A CA1-anchored Sst supertype comparison: re-running candidate discovery to enumerate CA1-enriched Sst supertypes and testing whether P-LM maps more naturally to a CA1 supertype than to the CA3-anchored SUPT_0219.

---

## Eliminated candidates

The single assessed candidate (0219 Sst Gaba_6 [CS20230722_SUPT_0219]) is the eliminated candidate above; there are no additional UNCERTAIN edges to collapse here. The shared disqualifying signal is the absence of CA1 representation in the atlas metadata for SUPT_0219.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The P-LM cell is a GABAergic, Sst+ hippocampal interneuron with soma in the pyramidal layer of CA1 [UBERON:0014548], described in a single anatomical/electrophysiological study (Oliva et al. 2000 [1]). The classical node's `definition_basis` is CLASSICAL_MULTIMODAL: it rests on the morphological/electrophysiological characterisation of Oliva et al. and on Sst as the only defining transcript-level marker; no transcriptomic characterisation exists for this type. The notes field records this as a THIN EVIDENCE stub flagged for re-evaluation alongside the R-LM cell.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 cell type labels — Allen Institute taxonomy; subclass labels include Sst, Pvalb, Lamp5, Vip, Sncg, Sst Chodl among non-interneuron classes) |
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

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:16+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA; ANNOTATION_TRANSFER | WEAK; PARTIAL | atlas-internal; — |

</details>

---

## Discussion

**Primary mapping:** Pyramidale-lacunosum moleculare (P-LM) cell → 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at UNCERTAIN confidence. Key support: shared Sst+ GABAergic identity in atlas metadata, and Yao 2021 SSv4 generic "Sst" cells mapping predominantly to SUPT_0219. Key caveats: DISCORDANT_ANATOMY (SUPT_0219 is CA3-anchored, P-LM is a CA1 type) and SINGLE_STUDY / AMBIGUOUS_MAPPING (the P-LM/R-LM pair are described once, never transcriptomically resolved, and may not be separable).

No Cell Ontology term currently assigned. The P-LM cell is a candidate for a new CL term, but resolution should wait until its transcriptomic identity (and separability from the R-LM cell) is established.

### Proposed experiments and follow-ups

Existing AT evidence (Yao 2021 SSv4 Sst subclass → WMBv1) already addresses the question of where generic hippocampal Sst+ cells land in WMBv1 (SUPT_0219 dominant; F1=0.759), but it cannot resolve P-LM specifically because the source label "Sst" aggregates many Sst+ interneuron types. Refined experiments are therefore needed:

- **What:** Annotation transfer from a Sst-interneuron–resolved hippocampal dataset (morphology- or driver-line–labelled) onto WMBv1.
  **Target:** F1 ≥ 0.80 at SUPERTYPE for a P-LM-equivalent labelled group, ideally with explicit stratum pyramidale soma annotation.
  **Expected output:** AnnotationTransferEvidence with `source_cluster_label` distinguishing pyramidale-soma from oriens-soma Sst+ cells.
  **Resolves:** the DISCORDANT_ANATOMY caveat (by testing whether a CA1-enriched Sst supertype is a better match) and the AMBIGUOUS_MAPPING caveat (by checking whether P-LM and R-LM map to the same or different targets).

- **What:** Targeted literature search (cite-traverse) for follow-up studies that revisit the Oliva et al. 2000 P-LM/R-LM distinction — molecular, viral, or driver-line characterisation of Sst+ stratum-pyramidale interneurons in CA1.
  **Target:** at least one primary study post-2000 that confirms or refutes the P-LM phenotype.
  **Expected output:** LiteratureEvidence updating the SINGLE_STUDY caveat; potentially additional defining markers beyond Sst.
  **Resolves:** the SINGLE_STUDY caveat and feeds richer marker evidence into a re-run of candidate discovery.

- **What:** Re-run of candidate discovery against CA1-enriched Sst supertypes using region-restricted scoring.
  **Target:** identification of any CA1-anchored Sst supertype/cluster with pyramidal-layer cells.
  **Expected output:** new MappingEdge candidate(s) or confirmation that SUPT_0219 is the closest available match.
  **Resolves:** test whether the current placeholder mapping is the best available among CA1 Sst supertypes.

### Open questions

(No `unresolved_questions` recorded in the edge YAML; the items below are derived from the caveats and proposed experiments above.)

1. Does a CA1-enriched Sst supertype provide a closer match to the P-LM soma-pyramidale phenotype than the CA3-anchored SUPT_0219?
2. Are the P-LM and R-LM cells transcriptomically separable, or are they a single Sst+ type with variable soma laminar position?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Oliva et al. 2000 · PMID:10777798 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst marker |
