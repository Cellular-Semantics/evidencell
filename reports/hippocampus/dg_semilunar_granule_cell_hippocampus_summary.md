# Dentate gyrus semilunar granule cell — WMBv1 (CCN20230722) Mapping Report
*2026-05-19 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

Semilunar granule cells (SGCs) are a morpho-physiologically distinct subpopulation of the dentate gyrus that reside at the inner/outer border of the stratum granulosum and receive disproportionately strong medial entorhinal cortex and associational synaptic drive compared to conventional granule cells [1][2]. Defined by two-photon imaging, infrared-DIC microscopy, and patch-clamp recordings, they display spiny, granule-like somata and characteristic physiology including an absence of short-term facilitation of lateral EC inputs [1], positioning them as a specialised information-routing population within the DG circuit. Mapping SGCs to a single-cell atlas is challenging because no transcript-level marker has been independently validated across datasets; the current evidence relies on enrichment of recently described transcriptomic markers (Sorcs3, Nptx2) from Bhatt 2025 in a minor WMBv1 DG supertype.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus granule cell layer [UBERON:0005381] (inner/outer border) | [1] |
| NT | Glutamatergic | [2] |
| Defining markers | — (none established at transcript level) | |
| Negative markers | — | |
| Neuropeptides | — | |
| CL term | dentate gyrus granule cell [CL:2000089] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location and morpho-physiological identity** [1]
  > We used two-photon imaging, infrared-differential interference contrast microscopy and patch clamp recordings from rat hippocampal slices to define the intrinsic physiology and synaptic targets of spiny, granule-like neurons in the IML, termed semilunar granule cells (SGCs)
  > — Unknown 2007 · [1] <!-- quote_key: 30068647_4c023496 -->

- **MEC and associational drive; circuit distinction from conventional granule cells** [2]
  > SGCs receive stronger medial entorhinal cortex and associational synaptic drive but lack short-term facilitation of lateral entorhinal cortex inputs observed in GCs
  > — Unknown 2025 · [2] <!-- quote_key: 277071421_57aeddb7 -->

</details>

Cell Ontology mapping: dentate gyrus granule cell [[CL:2000089](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:2000089)] (BROAD). No SGC-specific CL term exists; CL:2000089 is the closest parent. This node is a candidate for a CL new term request.

---

## Results

Two annotation-transfer runs inform this node. The primary evidence for an SGC-specific atlas mapping comes from Bhatt 2025 (GSE280167), in which SGC markers Sorcs3 and Nptx2 are markedly enriched in WMBv1 supertype 0138 DG Glut_3 [CS20230722_SUPT_0138]. A supporting run from Yao 2021 (GSE185862) SSv4 maps the broader DG subclass to the dominant supertype 0137 DG Glut_2 [CS20230722_SUPT_0137] but cannot resolve SGCs from conventional granule cells.

**Filtered AT figure — Yao 2021 DG source group (Bhatt 2025 run has no F1 figure; see Methods).**

![Filtered AT figure for dentate gyrus semilunar granule cell — Yao 2021 DG source group](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_dg_semilunar_granule_cell_hippocampus.png)

*F1 across taxonomy levels for the DG source group from Yao 2021 (GEO:GSE185862, n=2,473 DG subclass cells). The Yao 2021 DG subclass maps overwhelmingly to 0137 DG Glut_2 [CS20230722_SUPT_0137] (F1=0.935, group_purity=0.878, target_purity=1.000). This reflects the dominant conventional granule cell population; no SGC-specific signal is discernible because Yao 2021 does not provide SGC-resolved cluster labels. Shown as supporting context for the LOW-confidence SUPT_0137 edge.*

### Mapping candidates table

| Rank | WMBv1 supertype | Cells (WMBv1) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0138 DG Glut_3 [CS20230722_SUPT_0138] | 626 | 🟡 MODERATE | NT CONSISTENT · Sorcs3 6× enriched · Nptx2 elevated | Best candidate |
| 2 | 0137 DG Glut_2 [CS20230722_SUPT_0137] | 21,781 | 🔴 LOW | NT CONSISTENT · location APPROXIMATE · no SGC-specific markers | Speculative |

Total: 2 edges; relationship PARTIAL_OVERLAP for both.

### Primary candidate property alignment — 0138 DG Glut_3 [CS20230722_SUPT_0138] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glutamatergic (SUBC_037 DG Glut) | CONSISTENT |
| Soma location | DG granule cell layer [UBERON:0005381] inner/outer border | DG Glut subclass; MERFISH anatomy not assessed for SUPT_0138 | APPROXIMATE |
| Sorcs3 (SGC marker) | Established as SGC marker (Bhatt 2025) | 53.7% of SUPT_0138 cells express Sorcs3 (mean=4.93 UMI) vs 9.1% in SUPT_0137 — 6× enrichment | CONSISTENT |
| Nptx2 (SGC marker) | Established as SGC marker (Bhatt 2025) | Nptx2 in 15.9% of SUPT_0138 cells vs <1% in other DG supertypes | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Bhatt 2025 (GSE280167) MapMyCells, DG Glut proxy (n=11,327 cells) | Annotation transfer | SUPPORT | 67/11,327 DG Glut cells map to SUPT_0138 (0.59%); Sorcs3 6× enriched; Nptx2 elevated vs other DG supertypes | at_run_20260508_bhatt2025_dg_mmc_wmbv1 |

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0138 belongs to subclass CS20230722_SUBC_037 (037 DG Glut), a glutamatergic subclass. The classical semilunar granule cell is glutamatergic [2].

- **Sorcs3 enrichment — CONSISTENT.** MapMyCells local annotation transfer of Bhatt 2025 (GEO:GSE280167) DG snRNA-seq (VV wild-type, 4 animals, n=11,327 DG Glut cells after QC) onto WMBv1. SUPT_0138 captures 67 of these cells (0.59%); within them, Sorcs3 is expressed in 53.7% of cells (mean=4.93 UMI) vs 9.1% in SUPT_0137 (mean=0.20) — a ~6× relative enrichment. Sorcs3 is reported as the primary SGC marker in Bhatt 2025 [2].

- **Nptx2 enrichment — CONSISTENT.** Nptx2, a second SGC marker [2], is detected in 15.9% of SUPT_0138 cells vs near-absent in other DG supertypes (<1%). Dual-marker enrichment (Sorcs3 + Nptx2) constitutes the primary evidence for SUPT_0138 as the SGC-corresponding supertype.

- **Cell count consistent with SGC rarity.** SUPT_0138 represents 0.59% of DG Glut cells, consistent with the known rarity of SGCs in the granule cell layer.

**Concerns**

- **Location APPROXIMATE.** MERFISH anatomy for SUPT_0138 was not assessed. SGCs reside at the inner/outer border of the stratum granulosum; direct spatial validation is needed.

- **Enrichment-based evidence only; no formally annotated SGC cluster.** The Bhatt 2025 paper uses ATAC + RNA together for cluster annotation; the RNA-only MapMyCells analysis may miss the full SGC signature. Penk (the third Bhatt 2025 SGC marker) shows <2% detection across all DG supertypes, likely due to nuclear RNA dropout. SUPT_0138 atlas markers Lct and Atf3 are not classical SGC markers and their relationship to SGC identity is unresolved. F1 scoring is not possible because published per-cell cluster annotations are absent from GEO:GSE280167 raw data.

**What would upgrade confidence**

- Obtain Bhatt 2025 published cluster annotations for GSE280167, formally identify the SGC cluster (Cluster 18, Sorcs3+/Penk+/Nptx2+), and run MapMyCells AT to WMBv1 to generate a formal F1 score. Expected: F1 ≥ 0.70, confidence upgrade MODERATE → HIGH.
- Run `just add-expression` for Sorcs3 and Nptx2 on DG Glut supertypes (SUBC_037) to formalise the enrichment at the atlas level.
- Assess MERFISH spatial distribution of SUPT_0138 cells for enrichment at the inner/outer border of the granule cell layer.

### Secondary candidate — 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🔴 LOW

SUPT_0137 is the dominant DG glutamatergic supertype (21,781 cells). The Yao 2021 DG subclass maps here with high purity (F1=0.935, group_purity=0.878, target_purity=1.000), confirming this as the canonical granule cell supertype. SGCs share the granule cell layer and glutamatergic identity with conventional granule cells, so a proportion may be transcriptomically indistinguishable at current atlas resolution. This edge is retained as a speculative alternative pending SGC-specific marker validation. It is shared with the dg_granule_cell_hippocampus node, and no evidence currently supports preferential SGC enrichment in SUPT_0137.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The dentate gyrus semilunar granule cell is defined on a CLASSICAL_MULTIMODAL basis: morphological and electrophysiological characterisation places the soma at the inner/outer border of the dentate gyrus granule cell layer [UBERON:0005381] [1]; the type is glutamatergic [2]; no molecular markers are established at transcript level.

**Atlas mapping query.** Candidate atlas clusters were retrieved from WMBv1 (CCN20230722) at rank 1 (supertype) using NT type (glutamatergic) and region (DG) as primary filters. SGC-specific scoring was informed by Sorcs3 and Nptx2 enrichment in the Bhatt 2025 annotation transfer output.

**Property alignment.** Alignments graded CONSISTENT / APPROXIMATE / NOT_ASSESSED. Atlas-side marker expression values derived from the Bhatt 2025 annotation transfer output (GSE280167 snRNA-seq cells mapped to WMBv1 supertypes).

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1 (supporting context, LOW-confidence SUPT_0137 edge):

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse HPF SMART-Seq v4) |
| Source group | DG subclass (Yao 2021 Allen Institute taxonomy) |
| n cells (DG) | 2,473 |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default params, raw norm, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells total | 6,398 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 DG subclass does not resolve SGCs from conventional granule cells; F1=0.935 at SUPT_0137 reflects conventional granule cell population. |

Run 2 — Bhatt 2025 DG snRNA-seq → WMBv1 (primary evidence, MODERATE SUPT_0138 edge):

| Field | Value |
|---|---|
| Source dataset | GEO:GSE280167 (Bhatt 2025 mouse DG snRNA-seq, VV wild-type) |
| Source group | DG Glut subclass proxy (CS20230722_SUBC_037); samples GSM8643987–GSM8643990 merged |
| n cells total | 17,354 |
| n cells after QC | 11,327 |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default params, raw norm, 100 bootstrap iterations; Ensembl IDs; min_genes ≥ 200) |
| Tool version | cell_type_mapper v1.7.1 |
| Atlas pseudobulk SHA-256 | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_bhatt2025_dg_mmc_wmbv1/` |
| Output | `research/hippocampus/glutamatergic/annotation_transfer/GSE280167_bhatt2025/mmc_output.csv` |
| Caveats | F1 scores cannot be computed: Bhatt 2025 cluster annotations absent from GEO raw data. 67/11,327 DG Glut cells map to SUPT_0138; Sorcs3 and Nptx2 enrichment assessed from per-cell expression in those 67 cells. A filtered AT figure could not be generated for this node (no published SGC cluster label in SSv4 dataset). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes are validated against the evidencell knowledge base at write time. The pre-write hook rejects unresolvable identifiers and unattributed blockquotes.

*Generated by evidencell `07c6dbd` at 2026-05-19 from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0138 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE280167) | SUPPORT — Sorcs3 6× enriched in SUPT_0138 vs SUPT_0137; Nptx2 elevated; 67 cells | at_run_20260508_bhatt2025_dg_mmc_wmbv1 |
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0137 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | PARTIAL — F1=0.935 but reflects conventional granule cell population; no SGC-specific signal | at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 |

</details>

---

## Discussion

**Primary mapping: dentate gyrus semilunar granule cell → 0138 DG Glut_3 [CS20230722_SUPT_0138] · MODERATE.** In the Bhatt 2025 (GSE280167) DG snRNA-seq dataset, 67 of 11,327 DG Glut cells (0.59%) map to SUPT_0138, and within these cells the SGC markers Sorcs3 and Nptx2 are markedly enriched (Sorcs3: 53.7% of cells, mean=4.93 UMI vs 9.1% in the dominant SUPT_0137; Nptx2: 15.9% vs <1%). The minor cell count is consistent with the known rarity of SGCs. Key caveats: F1 scoring is not possible because published per-cell cluster annotations are absent from GEO:GSE280167 raw data; SUPT_0138 atlas markers Lct and Atf3 are not classical SGC markers; and MERFISH anatomy for SUPT_0138 has not been assessed. A secondary LOW-confidence edge to SUPT_0137 is retained to account for the possibility that a fraction of SGCs are transcriptomically indistinguishable from conventional granule cells at current atlas resolution.

The Cell Ontology has no specific term for the semilunar granule cell; dentate gyrus granule cell [CL:2000089] is used as BROAD mapping. A CL new term request is warranted.

### Proposed experiments

1. **Obtain Bhatt 2025 published cluster annotations for GSE280167** to formally identify the SGC cluster (Cluster 18, Sorcs3+/Penk+/Nptx2+) and run MapMyCells AT to WMBv1. Expected: F1 ≥ 0.70 at SUPT_0138, AnnotationTransferEvidence entry, confidence upgrade to HIGH. Highest-priority step.

2. **Run `just add-expression` for Sorcs3 and Nptx2 on DG Glut supertypes (SUBC_037)** via CCN20230722 precomputed stats to formalise the enrichment signal at the atlas level.

3. **Differential expression between Sorcs3-high SUPT_0138 cells and SUPT_0137 cells in GSE280167** to identify additional SGC-specific transcriptomic markers.

4. **Assess MERFISH spatial distribution of SUPT_0138** for enrichment at the inner/outer border of the DG granule cell layer.

5. **CL new term request** for "dentate gyrus semilunar granule cell" via `workflows/cl-term-request.md`.

### Open questions

1. Does Sorcs3 appear in the SUPT_0138 defining markers in the WMBv1 precomputed stats? Running add-expression for Sorcs3 and Nptx2 in DG Glut supertypes (SUBC_037) would formalise this.
2. Are SUPT_0138 cells enriched at the inner/outer border of the DG granule cell layer in WMBv1 MERFISH data?
3. Does the Bhatt 2025 SGC cluster (Cluster 18) map specifically to SUPT_0138 or to a SUPT_0137 sub-cluster?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2007 · PMID:18077687 | [18077687](https://pubmed.ncbi.nlm.nih.gov/18077687/) | soma location; morpho-physiological definition |
| [2] | Unknown 2025 · PMID:40161709 | [40161709](https://pubmed.ncbi.nlm.nih.gov/40161709/) | neurotransmitter type; Sorcs3 and Nptx2 as SGC markers |
