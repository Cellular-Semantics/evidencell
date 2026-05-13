# Trilaminar cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The trilaminar cell is a hippocampal GABAergic interneuron with a soma in CA1 stratum oriens [UBERON:0014552] and a distinctive long-range axonal projection profile that targets subiculum and medial septum [1]. It is reported as parvalbumin-positive (Pvalb) and muscarinic-acetylcholine-receptor-2-positive (M2R / Chrm2), and somatostatin-negative — a PV+/M2R+/Sst- profile that distinguishes it from PV basket cells, axo-axonic cells, and Sst-OLM cells of the same stratum oriens compartment. Mapping this classical type to the WMBv1 mouse-brain atlas matters because long-range PV projection neurons are an under-resolved branch of the inhibitory taxonomy: their somata overlap with locally-projecting PV interneurons but their connectivity is qualitatively different, and the atlas does not currently expose features that would distinguish them.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Defining markers | Pvalb, M2R (Chrm2) | — |
| Negative markers | Sst | — |

*Definition basis: CLASSICAL_MULTIMODAL. Curation note: well-documented by Somogyi-lab work (Katona et al. 2017); a long-range projection cell distinct from the hippocampo-septal cell, with a PV+/M2R+/Sst- profile.*

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One supertype-level candidate was assessed; 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] is the primary mapping at LOW confidence, reflecting consistent Pvalb-subclass / stratum-oriens placement but no atlas-side feature that resolves the trilaminar long-range-projection identity within the broader PV+ population.

![Filtered AT figure for Trilaminar cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_trilaminar_cell_hippocampus.png)

*F1 across taxonomy levels for the 1 source group (Yao 2021 SSv4 "Pvalb" subclass, n=66 HIP cells) relevant to Trilaminar cell. The Pvalb group reaches its highest F1 at SUBCLASS rank (best target: "051 Pvalb chandelier Gaba", F1=0.588) and splits across multiple Pvalb supertypes at finer resolution — consistent with the SSv4 Pvalb label being a mixed PV-interneuron population in which trilaminar identity is not separately resolvable.*

### 4. Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | 2860 | 🔴 LOW | Pvalb CONSISTENT · stratum oriens CONSISTENT · Sst CONSISTENT (low residual) | Speculative |

*Total edges: 1 (PARTIAL_OVERLAP).*

### Property alignment — 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA (Pvalb Gaba subclass) | not assessed | CONSISTENT |
| Soma location (stratum oriens) | stratum oriens (SOMA) | CA1 stratum oriens (493 cells), CA3 stratum oriens (152 cells) | not assessed | CONSISTENT |
| Pvalb expression | Pvalb — defining marker | Pvalb Gaba subclass (Pvalb implicit); precomputed stats mean: 8.74 | not assessed | CONSISTENT |
| M2R / Chrm2 expression | M2R (Chrm2) — defining marker | not present in supertype defining markers; precomputed stats mean: 4.52 | not assessed | CONSISTENT |
| Sst (negative) | Sst — negative marker | Sst absent from Pvalb Gaba_2 defining markers; precomputed stats mean: 2.72 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata — stratum oriens / Pvalb | Atlas metadata | PARTIAL | CA1 stratum oriens 493 cells; CA3 stratum oriens 152 cells | atlas-internal |
| Precomputed stats cross-check | Atlas metadata | PARTIAL | Pvalb=8.74, Chrm2=4.52, Sst=2.72 | atlas-internal |
| Yao 2021 SSv4 → WMBv1 MapMyCells AT | Annotation transfer | PARTIAL | F1=0.324 at SUPERTYPE (0206 Pvalb Gaba_2); F1=0.588 at SUBCLASS | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### 0206 Pvalb Gaba_2 · 🔴 LOW

**Supporting evidence**

- Atlas metadata places 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] in CA1 stratum oriens (493 cells) and CA3 stratum oriens (152 cells), matching the trilaminar soma compartment. The Pvalb subclass assignment is consistent with the PV+/Sst- marker profile.
- Precomputed atlas expression confirms the defining markers on the supertype: Pvalb mean = 8.74 and Chrm2 (M2R) mean = 4.52. Sst mean = 2.72 — non-zero, but Sst is not in the supertype's defining-marker list, so the negative-marker constraint is preserved at the classification level.
- MapMyCells annotation transfer of the Yao 2021 (GSE185862) SSv4 hippocampal-formation Pvalb subclass onto WMBv1 maps 12/66 Pvalb cells to 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] (group_purity=0.203, target_purity=0.800, F1=0.324). At SUBCLASS rank the best target is "051 Pvalb chandelier Gaba" with F1=0.588. The Pvalb-subclass-level signal therefore lands in the Pvalb branch of WMBv1, consistent with trilaminar PV+ identity, but does not isolate trilaminar cells from other PV+ interneurons.

**Marker evidence provenance**

- **Pvalb (defining):** No primary citation is listed on the classical node. Atlas precomputed expression is high (8.74), so the marker is robustly present at the supertype level; provenance for the trilaminar-specific claim rests on Katona et al. 2017 [1], cited for soma location. A targeted cite-traverse for primary Pvalb characterisation of morphologically-identified trilaminar cells would strengthen the chain.
- **M2R / Chrm2 (defining):** No primary citation on the classical node. Chrm2 mean = 4.52 in 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] confirms supertype-level expression, but the gene is not in the supertype's curated defining-marker list — i.e. M2R is not the property the atlas uses to define this supertype, and so the supertype contains both M2R+ (trilaminar) and M2R- (other PV+) cells. Subcluster-resolved M2R expression is needed to identify the trilaminar fraction.
- **Sst (negative):** No primary citation. Atlas precomputed Sst = 2.72 in 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] is low but non-zero. Low-level Sst co-expression in some Pvalb populations is documented *(note: from latent neuroanatomical knowledge; not asserted from facts)* — this does not disqualify the mapping but weakens Sst as a discriminating constraint at the supertype level.

**Concerns**

- AMBIGUOUS_MAPPING: 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] is the same supertype assigned to PV basket cells; it likely contains trilaminar, PV basket, and possibly axo-axonic cells. No transcriptomic features distinguishing trilaminar cells from other PV+ interneurons are exposed in atlas metadata.
- MARKER_NOT_SPECIFIC: M2R (Chrm2) — the key discriminating marker — is not in the supertype's defining-marker list. Atlas-level Chrm2 mean (4.52) cannot resolve whether the M2R signal is concentrated in a trilaminar subset.
- MARKER_NOT_SPECIFIC: Sst precomputed mean = 2.72 in 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] — low residual Sst expression weakens the negative-marker constraint, though it does not refute it.
- SINGLE_STUDY: The transcriptomic identity of trilaminar cells has not been independently confirmed beyond the Somogyi-lab anatomical/physiological characterisation [1].
- AT cohort limitation: the Yao 2021 SSv4 "Pvalb" subclass label (n=66 HIP cells) encompasses PV basket, axo-axonic, and bistratified cells, so the F1 signal at 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] cannot be uniquely attributed to trilaminar identity.

**What would upgrade confidence**

- A morphologically-identified PV-IN dataset (e.g. PV+ cells targeted by Cre driver and subjected to patch-seq with morphology reconstruction, with explicit subcluster labels for trilaminar / PV basket / axo-axonic) re-mapped to WMBv1 via MapMyCells. Threshold: F1 ≥ 0.80 at CLUSTER level for a trilaminar-labelled source group → would land an `AnnotationTransferEvidence` item that isolates trilaminar identity from the broader PV+ population.
- Atlas-side child-cluster expression breakdown of Chrm2 across the children of 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] to test whether an M2R-high subcluster co-localises with stratum oriens cells.
- Targeted cite-traverse for primary references establishing Pvalb, M2R (Chrm2), and Sst-negativity in morphologically-confirmed trilaminar cells — currently the marker list lacks primary citations on the classical node.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Trilaminar cell is defined as a GABAergic interneuron with soma in CA1 stratum oriens [UBERON:0014552] and a PV+/M2R+/Sst- marker profile; the soma-location citation is Katona et al. 2017 [1]. Definition basis: CLASSICAL_MULTIMODAL (the classical type is grounded in combined morphological, physiological and marker evidence in the cited literature, not in transcriptomic clustering).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 cell type labels, Allen Institute taxonomy) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations); per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
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
| --- | --- | --- | --- |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA; ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Trilaminar cell → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] at LOW confidence. Key support: stratum-oriens placement and Pvalb-subclass concordance in atlas metadata, plus partial PV-subclass signal from Yao 2021 SSv4 annotation transfer. Key caveats: AMBIGUOUS_MAPPING (the supertype co-houses PV basket and likely axo-axonic cells) and MARKER_NOT_SPECIFIC (M2R / Chrm2, the key discriminator, is not exposed as a defining marker at the supertype level, and Sst shows non-zero residual expression).

No Cell Ontology term currently assigned. Candidate for a CL new-term request once a transcriptomically isolable trilaminar subcluster is identified.

### Proposed experiments and follow-ups

- **What:** Re-map a morphologically-identified PV interneuron dataset (PV-Cre patch-seq with morphology reconstruction, or projection-targeted retrograde labelling separating subiculum / medial-septum projectors from local PV basket cells) onto WMBv1 with MapMyCells.
  - **Target:** F1 ≥ 0.80 at CLUSTER level for a trilaminar-labelled source group.
  - **Expected output:** `AnnotationTransferEvidence` item with explicit trilaminar source label.
  - **Resolves:** AMBIGUOUS_MAPPING (separates trilaminar from PV basket / axo-axonic within 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]); refines the LOW-confidence verdict (open questions 1, 2).
- **What:** Atlas-side child-cluster expression breakdown of Chrm2 and Pvalb across the children of 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206].
  - **Target:** identify any subcluster with Chrm2 substantially above the supertype mean (4.52) that retains stratum-oriens registration.
  - **Expected output:** updated `property_comparisons` with cluster-level values; potential `MarkerAnalysisEvidence`.
  - **Resolves:** MARKER_NOT_SPECIFIC for M2R; child-cluster concordance (open question 1).
- **What:** Targeted cite-traverse for primary references establishing Pvalb, M2R / Chrm2, and Sst-negativity in morphologically-confirmed trilaminar cells.
  - **Target:** at least one primary study per marker, ideally with morphological reconstruction.
  - **Expected output:** `LiteratureEvidence` with quote_key entries strengthening the classical-node marker citations.
  - **Resolves:** weak / missing marker provenance on the classical node.

### Open questions

1. Which of the children of 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] (if any) carries a Chrm2-enriched, stratum-oriens-localised signature that could correspond to trilaminar cells?
2. Can a long-range-projection retrograde-labelled PV+ dataset (subiculum / medial septum injection) be re-mapped to WMBv1 to isolate trilaminar identity from PV basket cells?
3. Is the low residual Sst (2.72) in 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] distributed homogeneously, or concentrated in a sub-population that should be excluded from the trilaminar mapping?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | soma location |
