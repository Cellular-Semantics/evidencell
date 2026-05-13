# Hilar mossy cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

Hilar mossy cells are the prominent glutamatergic principal cells resident in the polymorph layer (hilus) of the dentate gyrus of the hippocampal formation, where they form recurrent excitatory connections onto granule cells and contribute to dentate gyrus circuit function [3][4][5]. Mapping this classical anatomical/electrophysiological type to a transcriptomically defined WMBv1 cluster is needed because recent single-cell RNA-seq studies have identified multiple molecular subtypes within the mossy cell population, and resolving how those subtypes align with the WMBv1 supertype/cluster hierarchy is a prerequisite for downstream cross-atlas integration.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus of hippocampal formation [UBERON:0001885] (dentate gyrus polymorph layer) | [1][2] |
| NT | glutamatergic | [3][4][5] |
| Markers | Gria4, Dkk3 | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomical description · [1][2]
  > Glutamatergic hilar mossy cells (MCs) have axons that terminate both near and far from their cell body but stay within the DG, making synapses primarily in the molecular layer
  > — Botterill et al. 2021, abstract · [1] <!-- quote_key: 231953329_3a0a57e1 -->

  > The hippocampus has been studied for many decades for its largely known roles in encoding spatial memory, and a growing body of evidence indicates a differential involvement of dorsal and ventral hippocampal divisions in novelty detection
  > — Fredes & Shigemoto 2021, abstract · [2] <!-- quote_key: 235678538_22af50d5 -->

- **NT type:** classical literature description · [3][4][5]
  > Hilar mossy cells are the prominent glutamatergic cell type in the dentate hilus of the dentate gyrus (DG)
  > — Sun et al. 2017, Mossy Cells: Specialized Glutamatergic Neurons · [3] <!-- quote_key: 3583187_ea3794f5 -->

  > there are two glutamatergic principal cells instead of one: granule cells, which are the vast majority of the cells in the DG, and the so-called "mossy cells."
  > — Scharfman & Myers 2013, abstract · [4] <!-- quote_key: 11290620_27f933af -->

  > mossy cells (MCs), a major DG cell type that is glutamatergic and innervates the primary output cells of the DG, the granule cells (GCs)
  > — Scharfman & Bernstein 2015, abstract · [5] <!-- quote_key: 13657743_1eea4393 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Two MODERATE candidate atlas supertypes were assessed; the hilar mossy cell maps to two transcriptomically distinct CA3 Glut supertypes (SUPT_0078 and SUPT_0079), reflecting the molecular subdivision of mossy cells reported in Hochgerner 2018 into Cyp26b1+ and Adcyap1+ subtypes respectively.

![Filtered AT figure for Hilar mossy cell](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_for_hilar_mossy_cell_hippocampus.png)

*F1 across taxonomy levels for the 2 source groups (Mossy-Cyp26b1, Mossy-Adcyap1) relevant to Hilar mossy cell. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

The filtered figure shows Mossy-Cyp26b1 reaches a higher supertype F1 (0.943, SUPT_0078) than Mossy-Adcyap1 (0.833, SUPT_0079), with both subtypes mapping cleanly to distinct CA3 Glut supertypes within the same subclass (017 CA3 Glut).

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | 0078 CA3 Glut_4 [CS20230722_SUPT_0078] | CS20230722_SUPT_0078 | 5709 | 🟡 MODERATE | NT CONSISTENT · location DISCORDANT · Gria4/Dkk3 CONSISTENT | Best candidate (Cyp26b1+) |
| 2 | 0079 CA3 Glut_5 [CS20230722_SUPT_0079] | CS20230722_SUPT_0079 | 1308 | 🟡 MODERATE | NT CONSISTENT · location APPROXIMATE · Gria4/Dkk3 CONSISTENT | Best candidate (Adcyap1+) |

Total: 2 edges; both PARTIAL_OVERLAP.

### 0078 CA3 Glut_4 · 🟡 MODERATE

**Property comparison (Table 1)**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus polymorph layer / hilus [UBERON:0001885] | CA3 strata only: Field CA3, pyramidal layer [MBA:495] (1467 cells), Field CA3, stratum oriens [MBA:486] (1381 cells), Field CA3, stratum radiatum [MBA:504] (945 cells), Field CA3, stratum lucidum [MBA:479] (868 cells), Field CA3, stratum lacunosum-moleculare [MBA:471] (437 cells) | not assessed | DISCORDANT |
| NT type | glutamatergic | glutamatergic (SUBC_017 CA3 Glut) | not assessed | CONSISTENT |
| Gria4 expression | defining marker | mean=5.37 | not assessed | CONSISTENT |
| Dkk3 expression | defining marker | mean=8.71 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Evidence support (Table 2)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| MapMyCells AT (Mossy-Cyp26b1) | Annotation transfer | SUPPORT | F1=0.943 supertype; n=33/34 cells | atlas-internal |

*(Child-cluster breakdown not assessed — best child cluster reported in the evidence narrative is 0315 CA3 Glut_4, n=20, F1=0.833; see proposed experiments for higher-resolution validation.)*

**Supporting evidence**

- MapMyCells local AT of Hochgerner 2018 Mossy-Cyp26b1 cells onto WMBv1: 33 of 34 cells map to SUPT_0078 at supertype level with F1=0.943 (group_purity=0.971, target_purity=0.917) — a near-complete subset relationship at supertype resolution.
- Marker concordance: classical defining markers Gria4 and Dkk3 are both substantially expressed in SUPT_0078 (Gria4 mean=5.37; Dkk3 mean=8.71 in precomputed_stats.h5 at supertype level), consistent with their use as mossy cell markers.
- NT type CONSISTENT: SUBC_017 CA3 Glut / SUPT_0078 are annotated glutamatergic, matching the classical type.

**Marker evidence provenance**

- **Gria4**: defining marker on the classical node carries no primary citation in the facts file. Atlas-side mean expression is moderate (5.37) at supertype level; recommend a targeted cite-traverse for a primary source linking Gria4 to morphology-confirmed mossy cells.
- **Dkk3**: defining marker on the classical node carries no primary citation in the facts file. Atlas-side mean expression is high (8.71) at supertype level, consistent with marker status; recommend a targeted cite-traverse for primary support.

**Concerns**

- Soma location DISCORDANT: SUPT_0078 MERFISH cells are entirely within CA3 strata (pyramidal layer, oriens, radiatum, lucidum, lacunosum-moleculare); no cells appear in MBA:10704 (dentate gyrus polymorph layer / hilus) where classical hilar mossy cell soma reside. *(adjacent region — could reflect registration boundary error at the CA3c/hilus boundary; weak counter-evidence given the high AT F1 supporting transcriptomic equivalence.)* *(note: CA3 stratum oriens/pyramidal layer is anatomically adjacent to the dentate hilus at the CA3c border, so MERFISH registration boundary effects are plausible.)*
- DISCORDANT_ANATOMY caveat: the anatomical discordance between SUPT_0078 (CA3 strata) and classical hilar mossy cells (hilus/polymorph layer) is the principal unresolved issue; the mapping remains a hypothesis pending independent anatomy validation.

**What would upgrade confidence**

- smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus to test whether soma positions span the CA3c/hilus boundary (resolves open question 1; would add MarkerAnalysisEvidence or anatomical validation evidence).
- Targeted cite-traverse for primary citations supporting Gria4 and Dkk3 as mossy cell markers (would strengthen marker provenance without new experiments; would add LiteratureEvidence).

### 0079 CA3 Glut_5 · 🟡 MODERATE

**Property comparison (Table 1)**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus polymorph layer / hilus [UBERON:0001885] | Dentate gyrus, polymorph layer [MBA:10704] (181 cells); Dentate gyrus, granule cell layer [MBA:632] (147 cells); Field CA3, pyramidal layer [MBA:495] (294 cells); Field CA3, stratum oriens [MBA:486] (121 cells); Field CA3, stratum lucidum [MBA:479] (175 cells); Field CA3, stratum radiatum [MBA:504] (261 cells) | not assessed | APPROXIMATE |
| NT type | glutamatergic | glutamatergic (SUBC_017 CA3 Glut) | not assessed | CONSISTENT |
| Gria4 expression | defining marker | mean=8.05 | not assessed | CONSISTENT |
| Dkk3 expression | defining marker | mean=5.32 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Evidence support (Table 2)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| MapMyCells AT (Mossy-Adcyap1) | Annotation transfer | SUPPORT | F1=0.833 supertype; n=20/27 cells | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Supporting evidence**

- MapMyCells local AT of Hochgerner 2018 Mossy-Adcyap1 cells onto WMBv1: 20 of 27 cells map to SUPT_0079 at supertype level with F1=0.833 (target_purity=0.952). The high target_purity suggests SUPT_0079 is specific to the Adcyap1+ mossy cell subtype.
- SUPT_0079 is the only WMBv1 CA3 Glut supertype with cells assigned to the dentate gyrus polymorph layer [MBA:10704] (181 cells) — a direct positive anatomical correspondence with the classical hilar mossy cell soma location.
- Marker concordance: Gria4 mean=8.05 and Dkk3 mean=5.32 in SUPT_0079 at supertype level, consistent with mossy cell defining marker expectations.
- NT type CONSISTENT: SUBC_017 CA3 Glut / SUPT_0079 are annotated glutamatergic.

**Marker evidence provenance**

- **Gria4 / Dkk3**: same provenance gap as for SUPT_0078 (no primary citation in facts file). Atlas-side expression is higher for Gria4 in SUPT_0079 (8.05 vs. 5.37 in SUPT_0078) and lower for Dkk3 (5.32 vs. 8.71); these quantitative differences may help distinguish the two supertypes once primary marker citations are added.

**Concerns**

- Soma location APPROXIMATE: while SUPT_0079 has 181 cells in MBA:10704 (the hilus, the expected classical location), the majority of MERFISH-assigned cells are in CA3 strata. *(adjacent region — could reflect CA3c registration boundary error or genuine Adcyap1+ cell distribution spanning the hilus/CA3c boundary; weak counter-evidence.)*
- AMBIGUOUS_MAPPING caveat (shared across both edges): Hochgerner 2018 identifies three molecular mossy cell subtypes — Cyp26b1, Adcyap1, Klk8. Cyp26b1 maps to SUPT_0078 (F1=0.943) and Adcyap1 to SUPT_0079 (F1=0.833); Mossy-Klk8 (n=6) maps ambiguously across multiple CA3 supertypes (best SUPT_0077, F1=0.308) and is not promoted to an edge here. Two-supertype split therefore captures only two of three Hochgerner mossy cell subtypes.

**What would upgrade confidence**

- ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype mossy cell split (resolves open question 2; would add MarkerAnalysisEvidence).
- Run AT from a full Hochgerner 2018 mouse replication (or independent mossy-cell-enriched dataset) to confirm species-generality and reproducibility of the SUPT_0078/0079 split (would add a second AnnotationTransferEvidence run).

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical hilar mossy cell node (`definition_basis: CLASSICAL_MULTIMODAL`) is defined by glutamatergic neurotransmitter identity [3][4][5] and soma residence in the dentate gyrus polymorph layer / hilus [UBERON:0001885] [1][2], with Gria4 and Dkk3 listed as defining markers (no primary citations in the facts file at the time of report generation).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 mouse DG scRNA-seq cell type labels: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations); 2 genes unmapped |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 2934 (filtered to 2934) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |

**Atlas data sources.** None recorded in `methods_summary.atlas_data_sources` (atlas-side property values are sourced through the WMBv1 taxonomy reference store at gen-facts time).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:14+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_hilar_mossy_cell_hippocampus_to_supt_0078 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_hilar_mossy_cell_hippocampus_to_supt_0079 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Hilar mossy cell → 0078 CA3 Glut_4 [CS20230722_SUPT_0078] at MODERATE confidence, with a co-primary mapping to 0079 CA3 Glut_5 [CS20230722_SUPT_0079] at MODERATE confidence representing a transcriptomic subdivision. Key support: annotation-transfer F1 of 0.943 (Cyp26b1+) and 0.833 (Adcyap1+) at supertype level. Key caveats: DISCORDANT_ANATOMY (SUPT_0078 MERFISH cells fall entirely within CA3 strata rather than the hilus) and AMBIGUOUS_MAPPING (the third Hochgerner subtype, Mossy-Klk8, does not resolve to a single supertype).

No Cell Ontology term currently assigned. Candidate for CL contribution — a new CL term covering hilar mossy cells would help cross-resource integration.

### Proposed experiments and follow-ups

The two edges already carry an ANNOTATION_TRANSFER evidence item each (Hochgerner 2018 GSE95315, MapMyCells local v1.7.1). Refined / additional experiments below.

- **What:** smFISH (or MERFISH spot) validation of SUPT_0078 defining markers (Homer3, Cldn22) in the dentate hilus.
  **Target:** detectable Homer3/Cldn22 expression in hilar mossy cell soma at the CA3c/hilus boundary.
  **Expected output:** MarkerAnalysisEvidence or anatomical validation evidence.
  **Resolves:** open question 1 (SUPT_0078 anatomical placement at the CA3c/hilus border).

- **What:** ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus.
  **Target:** non-overlapping expression of the two markers within hilar mossy cells.
  **Expected output:** MarkerAnalysisEvidence supporting the two-supertype split.
  **Resolves:** open question 2 (functional/anatomical distinction between SUPT_0078 and SUPT_0079 subtypes).

- **What:** Independent annotation transfer from a second mossy-cell-enriched scRNA-seq dataset.
  **Target:** F1 ≥ 0.80 at SUPERTYPE level for at least one of the Cyp26b1+/Adcyap1+ subgroups in an independent source dataset.
  **Expected output:** AnnotationTransferEvidence.
  **Resolves:** generality of the SUPT_0078/0079 split beyond Hochgerner 2018; would also clarify whether a distinct supertype captures the Mossy-Klk8 subtype.

- **What:** Targeted cite-traverse for primary citations supporting Gria4 and Dkk3 as defining markers of morphology-confirmed hilar mossy cells.
  **Target:** at least one primary source per marker; reduces reliance on symbol-only marker assertions.
  **Expected output:** LiteratureEvidence on the classical node.
  **Resolves:** marker provenance gap noted in the per-candidate sections.

### Open questions

1. Are SUPT_0078 cells that map to CA3 pyramidal layer actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 (SUPT_0078 defining markers) in hilus/CA3c would resolve this.
2. What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)?
3. Where does the third Hochgerner 2018 mossy cell subtype (Mossy-Klk8) sit in WMBv1? With n=6 source cells it maps ambiguously across multiple CA3 supertypes (best SUPT_0077, F1=0.308); a larger source cohort is needed for a confident assignment.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Botterill et al. 2021 | [33600026](https://pubmed.ncbi.nlm.nih.gov/33600026) | soma location |
| [2] | Fredes & Shigemoto 2021 | [34214666](https://pubmed.ncbi.nlm.nih.gov/34214666) | soma location |
| [3] | Sun et al. 2017 | [28451637](https://pubmed.ncbi.nlm.nih.gov/28451637) | neurotransmitter type |
| [4] | Scharfman & Myers 2013 | [23420672](https://pubmed.ncbi.nlm.nih.gov/23420672) | neurotransmitter type |
| [5] | Scharfman & Bernstein 2015 | [26347618](https://pubmed.ncbi.nlm.nih.gov/26347618) | neurotransmitter type |
