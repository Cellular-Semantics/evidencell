# Hilar mossy cell — WMBv1 (CCN20230722) Mapping Report

## Introduction

Hilar mossy cells are the prominent glutamatergic cell type of the dentate gyrus hilus, distinguished from the numerically dominant granule cells by their soma in the dentate gyrus polymorph layer [UBERON:0002928] and an associational axon that projects primarily to the inner molecular layer of the dentate gyrus, with dorsal mossy cells additionally targeting the middle molecular layer [1, 3, 4, 5]. They form an excitatory loop that recurrently gates granule cell output, and their selective vulnerability in temporal lobe epilepsy has made them a focus of sustained investigation [4].

| Property | Value | References |
|---|---|---|
| Neurotransmitter | Glutamatergic | [3], [4], [5] |
| Defining markers | Gria4, Dkk3 | — |
| Soma location | Dentate gyrus polymorphic layer [UBERON:0002928] (polymorph layer / hilus) | [1], [2], [4] |

<details>
<summary>Per-property source evidence</summary>

- **Neurotransmitter (glutamatergic)** — Sun et al. 2017 [3]:

  > Hilar mossy cells are the prominent glutamatergic cell type in the dentate hilus of the dentate gyrus (DG)
  > — Sun et al. 2017, Mossy Cells: Specialized Glutamatergic Neurons · [3] <!-- quote_key: 3583187_ea3794f5 -->

- **Neurotransmitter (glutamatergic)** — Scharfman & Myers 2012 [4]:

  > there are two glutamatergic principal cells instead of one: granule cells, which are the vast majority of the cells in the DG, and the so-called "mossy cells."
  > — Scharfman & Myers 2012, abstract · [4] <!-- quote_key: 11290620_27f933af -->

- **Neurotransmitter (glutamatergic)** — Scharfman & Bernstein 2015 [5]:

  > mossy cells (MCs), a major DG cell type that is glutamatergic and innervates the primary output cells of the DG, the granule cells (GCs)
  > — Scharfman & Bernstein 2015, abstract · [5] <!-- quote_key: 13657743_1eea4393 -->

- **Soma location (dentate gyrus polymorph layer)** — Botterill et al. 2021 [1]:

  > Glutamatergic hilar mossy cells (MCs) have axons that terminate both near and far from their cell body but stay within the DG, making synapses primarily in the molecular layer
  > — Botterill et al. 2021, abstract · [1] <!-- quote_key: 231953329_3a0a57e1 -->

- **Soma location (dentate gyrus polymorph layer)** — Scharfman & Myers 2012 [4]:

  > A cell body in the hilus, defined as zone 4 of Amaral (1978). Glutamate as the primary transmitter (other markers are less valuable, as discussed below). An axon that innervates the inner molecular layer.
  > — Scharfman & Myers 2012, WHAT IS A MOSSY CELL? A PRACTICAL DEFINITION · [4] <!-- quote_key: 11290620_d7c0cc69 -->

</details>

#### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer from Hochgerner 2018 (GEO:GSE95315) mouse dentate gyrus scRNA-seq identifies two WMBv1 supertypes as the best transcriptomic matches to the hilar mossy cell: [CS20230722_SUPT_0078] (0078 CA3 Glut_4, F1 = 0.943 for the Mossy-Cyp26b1 source group) and [CS20230722_SUPT_0079] (0079 CA3 Glut_5, F1 = 0.833 for the Mossy-Adcyap1 source group), corresponding to molecularly distinct Cyp26b1+ and Adcyap1+ mossy cell subtypes respectively.

![Filtered AT figure for Hilar mossy cell](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_for_hilar_mossy_cell_hippocampus.png)

*F1 across taxonomy levels for the Mossy-Cyp26b1 and Mossy-Adcyap1 source groups relevant to hilar mossy cell. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

### Candidate overview

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0078 CA3 Glut_4 (Cyp26b1 subtype) | CS20230722_SUPT_0078 | 🟡 MODERATE | PARTIAL_OVERLAP | Best candidate |
| 0079 CA3 Glut_5 (Adcyap1 subtype) | CS20230722_SUPT_0079 | 🟡 MODERATE | PARTIAL_OVERLAP | Best candidate |

---

### Edge 1: Hilar mossy cell → 0078 CA3 Glut_4 [CS20230722_SUPT_0078] (Mossy-Cyp26b1)

**Table 1: Property comparison — 0078 CA3 Glut_4 [CS20230722_SUPT_0078]**

| Property | Classical type | WMBv1 0078 CA3 Glut_4 | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glutamatergic (SUBC_017 CA3 Glut, CS20230722_SUPT_0078) | CONSISTENT |
| Soma location | Dentate gyrus polymorph layer / hilus [UBERON:0002928] | Field CA3, pyramidal layer [MBA:495]: 1467 cells; Field CA3, stratum oriens [MBA:486]: 1381 cells; Field CA3, stratum radiatum [MBA:504]: 945 cells; Field CA3, stratum lucidum [MBA:479]: 868 cells; Field CA3, stratum lacunosum-moleculare [MBA:471]: 437 cells | DISCORDANT |
| Marker: Gria4 | Defining marker | Not in SUPT_0078 top markers (Homer3, Cldn22); mean_expression = 5.37 | CONSISTENT |
| Marker: Dkk3 | Defining marker | Not in SUPT_0078 top markers; mean_expression = 8.71 | CONSISTENT |

**Table 2: Evidence support — 0078 CA3 Glut_4 [CS20230722_SUPT_0078]**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | SUPPORT | 33/34 Mossy-Cyp26b1 cells map to SUPT_0078 at supertype level (F1 = 0.943; group_purity = 0.971, target_purity = 0.917). Best cluster: 0315 CA3 Glut_4 (n = 20, F1 = 0.833). At subclass level: CS20230722_SUBC_017 (F1 = 0.686). |

The Mossy-Cyp26b1 source group maps with exceptional fidelity to [CS20230722_SUPT_0078] (0078 CA3 Glut_4): 33 of 34 cells in the Hochgerner 2018 Mossy-Cyp26b1 cluster are assigned to this supertype, yielding an F1 of 0.943. Both mossy cell marker genes — Gria4 and Dkk3 — show substantial mean expression within SUPT_0078 (5.37 and 8.71 respectively), consistent with mossy cell identity even though neither appears among the supertype's top defining markers (Homer3, Cldn22). The critical caveat is anatomical: all MERFISH-registered SUPT_0078 cells fall within CA3 strata, with no cells assigned to the dentate gyrus polymorph layer [MBA:10704]. This DISCORDANT location alignment distinguishes this edge from the stronger anatomical correspondence seen for SUPT_0079. Two explanations remain open: (i) Cyp26b1+ mossy cells may preferentially reside at the CA3c/hilus border and thus register within MERFISH CA3 compartments rather than the polymorph layer; or (ii) SUPT_0078 may additionally capture CA3 pyramidal cells that share the Cyp26b1+ transcriptomic signature but are anatomically distinct from mossy cells. Resolving this requires targeted spatial validation of SUPT_0078 defining markers in the hilus.

---

### Edge 2: Hilar mossy cell → 0079 CA3 Glut_5 [CS20230722_SUPT_0079] (Mossy-Adcyap1)

**Table 1: Property comparison — 0079 CA3 Glut_5 [CS20230722_SUPT_0079]**

| Property | Classical type | WMBv1 0079 CA3 Glut_5 | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glutamatergic (SUBC_017 CA3 Glut, CS20230722_SUPT_0079) | CONSISTENT |
| Soma location | Dentate gyrus polymorph layer / hilus [UBERON:0002928] | Dentate gyrus, polymorph layer [MBA:10704]: 181 cells; Dentate gyrus, granule cell layer [MBA:632]: 147 cells; Field CA3, pyramidal layer [MBA:495]: 294 cells; Field CA3, stratum oriens [MBA:486]: 121 cells; Field CA3, stratum lucidum [MBA:479]: 175 cells; Field CA3, stratum radiatum [MBA:504]: 261 cells | APPROXIMATE |
| Marker: Gria4 | Defining marker | Not in SUPT_0079 top markers (Rcn3, Csf2rb2); mean_expression = 8.05 | CONSISTENT |
| Marker: Dkk3 | Defining marker | Not in SUPT_0079 top markers; mean_expression = 5.32 | CONSISTENT |

**Table 2: Evidence support — 0079 CA3 Glut_5 [CS20230722_SUPT_0079]**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | SUPPORT | 20/27 Mossy-Adcyap1 cells map to SUPT_0079 at supertype level (F1 = 0.833; group_purity = 0.741, target_purity = 0.952). At subclass level: CS20230722_SUBC_017 (F1 = 0.562). |

The Mossy-Adcyap1 source group maps with good fidelity to [CS20230722_SUPT_0079] (0079 CA3 Glut_5): 20 of 27 cells are assigned to this supertype (F1 = 0.833). The notably high target_purity of 0.952 indicates that Mossy-Adcyap1 cells dominate the SUPT_0079 signal captured by annotation transfer, suggesting this supertype may be specifically associated with the Adcyap1+ mossy cell molecular identity. Crucially, SUPT_0079 is the only CA3 Glut supertype in WMBv1 with MERFISH cells assigned to the dentate gyrus polymorph layer [MBA:10704] (181 cells), providing a direct anatomical correspondence with the classical hilar soma location of mossy cells. Gria4 and Dkk3 both show substantial expression in SUPT_0079 (mean_expression = 8.05 and 5.32 respectively), consistent with mossy cell identity. The APPROXIMATE location alignment reflects the fact that the majority of SUPT_0079 MERFISH cells reside in CA3 strata, which may indicate that the supertype encompasses both hilar mossy cells and CA3c pyramidal cells sharing the Adcyap1+ transcriptomic profile, or that MERFISH registration of hilus cells into adjacent CA3c partially inflates the CA3 counts.

Together, SUPT_0078 and SUPT_0079 represent a molecular subdivision of the single classical hilar mossy cell type into two WMBv1 transcriptomic supertypes, defined by differential expression of Cyp26b1 and Adcyap1. A third Hochgerner 2018 mossy cell label — Mossy-Klk8 (n = 6 cells) — maps ambiguously across multiple CA3 supertypes (best F1 = 0.308) and is insufficient to anchor an additional mapping edge.

---

## Methods

### Classical type definition

The hilar mossy cell was defined on a multimodal basis (CLASSICAL_MULTIMODAL). Glutamatergic neurotransmitter identity is established by Sun et al. 2017 [3], Scharfman & Myers 2012 [4], and Scharfman & Bernstein 2015 [5]. Soma location in the dentate gyrus polymorphic layer [UBERON:0002928], specifically the polymorph layer (hilus), is supported by Botterill et al. 2021 [1], Fredes & Shigemoto 2021 [2], and Scharfman & Myers 2012 [4], whose practical definition of mossy cells explicitly requires a cell body in the hilus. Defining markers (Gria4, Dkk3) were assigned without a primary literature citation on file (symbol-only annotation).

### Atlas mapping query

Candidate atlas clusters were retrieved from WMBv1 (CCN20230722) at ranks 0 and 1 using metadata-based scoring.

### Property alignment

Each defining property was compared via the property_comparisons schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

### Annotation transfer

<details>
<summary>AT run: at_run_20260427_hochgerner2018_dg_mmc_wmbv1</summary>

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 (GSE95315) mouse DG scRNA-seq cell type labels: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes.) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). 2 genes unmapped. Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| n cells | 2934 |
| Atlas pseudobulk SHA | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |

</details>

### Anti-hallucination

All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source evidence_items[*].explanation fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Report generated 2026-05-19T10:45:51+00:00. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

### Evidence base

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 2 |

---

## Discussion

**Primary mapping:** The hilar mossy cell maps at MODERATE confidence to two WMBv1 supertypes: [CS20230722_SUPT_0078] (0078 CA3 Glut_4; Mossy-Cyp26b1 subtype, F1 = 0.943) and [CS20230722_SUPT_0079] (0079 CA3 Glut_5; Mossy-Adcyap1 subtype, F1 = 0.833). These two supertypes represent a molecular subdivision of the single classical hilar mossy cell type into Cyp26b1+ and Adcyap1+ transcriptomic entities. Both edges carry PARTIAL_OVERLAP relationship designations, reflecting the fact that each supertype likely encompasses additional cell populations beyond hilar mossy cells sensu stricto. The anatomical evidence favours SUPT_0079 as the more faithful atlas correlate of the classical mossy cell: it is the only CA3 Glut supertype with MERFISH-registered cells in the dentate gyrus polymorph layer [MBA:10704] (181 cells). SUPT_0078, by contrast, shows entirely CA3 soma assignments and no hilar cells despite the near-perfect F1 for the Cyp26b1 source group — a discordance that remains the principal unresolved issue for that edge. MODERATE confidence is appropriate for both edges in the absence of orthogonal spatial or electrophysiological validation.

### Proposed experiments

**smFISH / spatial transcriptomics:**

- smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus to test whether soma positions span the CA3c/hilus boundary and resolve the anatomical discordance for Edge 1.
- ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype mossy cell split.

**Annotation transfer replication:**

- Run annotation transfer from a full Hochgerner 2018 mouse replication dataset to confirm species-generality of the SUPT_0078/0079 mossy cell split.

### Open questions

1. Are SUPT_0078 cells that map to CA3 pyramidal layer actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 (SUPT_0078 defining markers) in hilus/CA3c would resolve this.

2. What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)?

---

## References

[1] Botterill et al. 2021 · PMID:33600026 · DOI:10.1002/hipo.23314

[2] Fredes & Shigemoto 2021 · PMID:34214666 · DOI:10.1016/j.nlm.2021.107486

[3] Sun et al. 2017 · PMID:28451637 · DOI:10.1523/ENEURO.0097-17.2017

[4] Scharfman & Myers 2012 · PMID:23420672 · DOI:10.3389/fncir.2012.00106

[5] Scharfman & Bernstein 2015 · PMID:26347618 · DOI:10.3389/fnsys.2015.00112
