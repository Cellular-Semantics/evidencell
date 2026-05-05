# dentate gyrus semilunar granule cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus granule cell (CL:2000089) — BROAD mapping | |
| Soma location | Dentate gyrus of hippocampal formation [UBERON:0001885] (stratum granulosum inner/outer border) | [1] |
| NT | Glutamatergic | [2] |
| Defining markers | — (no molecular markers established for SGC) | |
| Negative markers | — | |
| Neuropeptides | — | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0138 DG Glut_3 [CS20230722_SUPT_0138] | DG Glut | 82 (Bhatt 2025 GSE280167) | 🟡 MODERATE | Sorcs3 6x enrichment · Nptx2 elevated · NT CONSISTENT · location APPROXIMATE | Best candidate — SGC-enriched minor DG supertype |
| 2 | 0137 DG Glut_2 [CS20230722_SUPT_0137] | DG Glut | 7199 (DG granule cell layer, MBA:632) | 🔴 LOW | NT CONSISTENT · location APPROXIMATE · no SGC-specific markers | Speculative — shared with regular granule cell |

Total: 2 edges. Relationship type: PARTIAL_OVERLAP for both edges.

---

## 0138 DG Glut_3 [CS20230722_SUPT_0138] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0138 belongs to subclass CS20230722_SUBC_037 (037 DG Glut), a glutamatergic subclass. The classical semilunar granule cell is glutamatergic [2].

- **Sorcs3 enrichment — CONSISTENT.** MapMyCells local annotation transfer of Bhatt 2025 (GEO:GSE280167) dentate gyrus snRNA-seq (wild-type VV samples, 4 animals, 11,601 DG Glut cells) onto WMBv1 (CCN20230722). SUPT_0138 (DG Glut_3, n=82 cells, 0.7% of DG cells) shows marked enrichment for the semilunar granule cell (SGC) marker Sorcs3: 53.7% of SUPT_0138 cells express Sorcs3 (mean = 4.93 UMIs) vs 9.1% in SUPT_0137 (mean = 0.20) — a ~6x relative enrichment. Sorcs3 is established as an SGC marker in Bhatt 2025 [2].

- **Nptx2 enrichment — CONSISTENT.** Nptx2, a second SGC marker from Bhatt 2025 [2], is elevated in SUPT_0138 (15.9% of cells) vs near-absent in other DG supertypes (<1%). This dual-marker enrichment (Sorcs3 + Nptx2) is the primary evidence supporting SUPT_0138 as the SGC-corresponding supertype.

- **Cell count consistent with SGC rarity.** SUPT_0138 represents 0.7% of DG cells in the Bhatt 2025 dataset, consistent with the known rarity of SGCs in the DG granule cell layer.

**Marker evidence provenance**

- **Sorcs3 and Nptx2** [2]: Both markers derive from Bhatt 2025 (GEO:GSE280167), which used combined ATAC and RNA snRNA-seq to characterise DG cell types. The SGC cluster was identified using ATAC + RNA together; the RNA-only analysis used here (MapMyCells annotation transfer) may miss the full SGC signature, particularly for ATAC-dependent features. Evidence is transcript-level (snRNA-seq counts). Cell-type specificity: Sorcs3 is reported as a marker for the SGC cluster (Cluster 18) in Bhatt 2025; our analysis confirms a 6x enrichment in SUPT_0138 at the atlas level, supporting but not formally proving SGC identity. Penk, the third Bhatt 2025 SGC marker, is sparsely detected across all DG supertypes (<2%), likely due to nuclear RNA dropout in snRNA-seq. The SUPT_0138 markers Lct and Atf3 in the WMBv1 atlas are not classical SGC markers; their relationship to SGC identity is unresolved.

- **No KB citations for classical SGC molecular markers.** The classical node has no defining markers — the cell type is defined morpho-physiologically (spiny granule-like neurons in the inner molecular layer with characteristic physiology [1]). The current mapping relies entirely on enrichment of recently described transcriptomic markers from Bhatt 2025, which has not yet been independently replicated.

**Concerns**

- **Location — APPROXIMATE.** SUPT_0138 is in the DG Glut subclass (SUBC_037); MERFISH anatomy for SUPT_0138 specifically was not assessed in the current evidence set. SGCs are found at the inner/outer border of the stratum granulosum, which overlaps with the DG granule cell layer broadly (MBA:632). *(note: The precise MERFISH location of SUPT_0138 cells relative to the inner molecular layer SGC position requires direct inspection of the WMBv1 MERFISH data for this supertype.)*

- **Enrichment-based evidence, not formally annotated SGC cluster.** The SGC evidence is based on marker enrichment (Sorcs3, Nptx2) in SUPT_0138 from Bhatt 2025, not from a formally annotated SGC cluster in the WMBv1 atlas. The Bhatt 2025 paper uses ATAC + RNA data together for cluster annotation; the RNA-only analysis may miss the full SGC signature. SUPT_0138 is a minor DG subpopulation (n=82 in GSE280167, n=28 in Yao 2021).

**What would upgrade confidence**

- **Obtain Bhatt 2025 published cluster annotations** (AnnotationTransferEvidence): formally identify Cluster 18 (SGC, Sorcs3+/Penk+/Nptx2+) from the published paper and confirm SUPT_0138 correspondence. Expected output: AnnotationTransferEvidence entry with F1 ≥ 0.70. Resolves open question 2.

- **Add-expression for Sorcs3 and Nptx2 on DG Glut supertypes** (ATLAS_METADATA): run `just add-expression` for Sorcs3 and Nptx2 on SUBC_037 supertypes using CCN20230722 precomputed stats to formalize the enrichment at the atlas level. Expected output: precomputed expression blocks confirming Sorcs3 and Nptx2 enrichment in SUPT_0138 vs SUPT_0137. Resolves open question 1.

- **MERFISH anatomy check for SUPT_0138:** inspect the WMBv1 MERFISH data to determine whether SUPT_0138 cells are specifically enriched at the inner/outer border of the DG granule cell layer. Resolves open question 2.

---

## 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🔴 LOW

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0137 belongs to subclass CS20230722_SUBC_037 (037 DG Glut), a glutamatergic subclass, consistent with the glutamatergic identity of the semilunar granule cell [2].

- **Annotation transfer — PARTIAL.** Annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722) via local MapMyCells. Yao 2021 DG subclass cells (n=2473) map to SUPT_0137 with group_purity=0.878 and F1=0.935, confirming SUPT_0137 as the dominant DG glutamatergic supertype. SUPT_0137 is shared between dg_granule_cell_hippocampus and this node; the semilunar granule cell is a morpho-physiologically distinct DG subpopulation for which no transcriptome-specific markers are available in this dataset. PARTIAL support reflects that this edge targets the same atlas node as the regular granule cell.

- **Location — APPROXIMATE.** Semilunar granule cells are found at the inner/outer border of the stratum granulosum; the MERFISH assignment for SUPT_0137 covers the granule cell layer broadly (MBA:632).

**Marker evidence provenance**

- **No defining markers** are established for the semilunar granule cell node. Without SGC-specific molecular markers, there is no evidence that SUPT_0137 preferentially captures SGCs vs. regular granule cells. SUPT_0137 defining markers (Dsp, Kcnh3, Syndig1) have not been compared against classical SGC transcriptomics — alignment is NOT_ASSESSED.

**Concerns**

- **SUPT_0137 is shared with the regular DG granule cell** (edge_dg_granule_cell_hippocampus_to_supt_0137). Without molecular markers specific to SGCs, there is no evidence that SUPT_0137 preferentially captures SGCs vs. regular granule cells. The LOW confidence assignment reflects this non-specific overlap.

- **SUPT_0139 (DG Glut_4, 9.1% of DG cells) is also a candidate** for a morpho-physiologically distinct DG subpopulation and should be evaluated once SGC-specific markers are established.

- **Defining markers NOT_ASSESSED.** SUPT_0137 atlas markers (Dsp, Kcnh3, Syndig1) have not been cross-checked against published SGC transcriptomics.

**What would upgrade confidence**

- **SGC-specific markers:** Establish transcriptomic markers specific to SGCs by running differential expression between DG cells mapping to SUPT_0138 vs SUPT_0137 in GSE280167 data. If Sorcs3 and Nptx2 are confirmed as SGC-specific, SUPT_0138 would become the primary candidate, demoting this SUPT_0137 edge further.

- **Bhatt 2025 cluster annotations** (GEO:GSE280167): obtain the published cluster annotations to determine whether Cluster 18 (SGC) maps to SUPT_0138 rather than SUPT_0137. Resolves open question 3.

---

## Proposed experiments

*Note on existing AT evidence:* The Yao 2021 (GEO:GSE185862) AT establishes SUPT_0137 as the dominant DG Glut supertype (F1=0.935, group_purity=0.878). The Bhatt 2025 (GEO:GSE280167) AT identifies SUPT_0138 as Sorcs3/Nptx2-enriched. A refined experiment obtaining the Bhatt 2025 published SGC cluster annotations would formally resolve which supertype corresponds to classical SGCs.

### Add-expression (Sorcs3 and Nptx2 in DG Glut supertypes)

- **What:** Run `just add-expression` for Sorcs3 and Nptx2 on DG Glut supertypes (SUBC_037; SUPT_0136–0139) via CCN20230722 precomputed stats.
- **Target:** Confirm Sorcs3 mean ≥ 3.0 and Nptx2 expression specifically elevated in SUPT_0138 vs SUPT_0137.
- **Expected output:** Precomputed expression blocks on atlas nodes; formal confirmation of SUPT_0138 SGC enrichment.
- **Resolves:** Open question 1 (does Sorcs3 appear in SUPT_0138 defining markers in WMBv1?).

### Obtain Bhatt 2025 published SGC annotations (GEO:GSE280167)

- **What:** Download Bhatt 2025 published cluster annotations for GSE280167; formally identify Cluster 18 (SGC, Sorcs3+/Penk+/Nptx2+); run MapMyCells AT to WMBv1.
- **Target:** F1 ≥ 0.70 at SUPERTYPE level for a formally annotated SGC cluster mapping to SUPT_0138.
- **Expected output:** AnnotationTransferEvidence entry on edge_dg_semilunar_granule_cell_hippocampus_to_supt_0138.
- **Resolves:** Open question 2 (formal SGC cluster confirmation); open question 3 (whether Bhatt 2025 Cluster 18 maps to SUPT_0137 or SUPT_0138).

### Differential expression (Sorcs3-high SUPT_0138 cells vs SUPT_0137 in GSE280167)

- **What:** Run differential expression between Sorcs3-high SUPT_0138 cells and SUPT_0137 cells in Bhatt 2025 GSE280167 data to find additional SGC-specific markers.
- **Target:** Identify ≥ 3 genes with fold-change ≥ 2 and detection rate ≥ 30% in SUPT_0138 Sorcs3-high cells.
- **Expected output:** Candidate SGC markers for future KB annotation and targeted literature search.
- **Resolves:** Open question 4 (are there additional transcriptomic markers distinguishing SGCs from regular granule cells?).

---

## Open questions

1. Does Sorcs3 appear in the SUPT_0138 defining markers in the WMBv1 precomputed stats? Running add-expression for Sorcs3 and Nptx2 in DG Glut supertypes (SUBC_037) would formalize this enrichment at the atlas level.

2. Are SUPT_0138 cells specifically enriched at the inner/outer border of the DG granule cell layer (the anatomical location of SGCs) in the WMBv1 MERFISH data?

3. Bhatt 2025 (GEO:GSE280167) identifies a SGC-enriched cluster (Cluster 18, Sorcs3+/Penk+/Nptx2+). Does this cluster map specifically to SUPT_0138 or to a SUPT_0137 sub-cluster? Running MapMyCells on the formally annotated GSE280167 cluster will resolve.

4. Are there transcriptomic markers that distinguish SGCs from regular DG granule cells in the Yao 2021 dataset? Differential expression between DG cells mapping to SUPT_0138 vs SUPT_0137 in GSE280167 might reveal candidate markers.

---

## Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0138 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE280167; Bhatt 2025) | SUPPORT — 82 cells (0.7% of DG); Sorcs3 6x enrichment (53.7% vs 9.1%); Nptx2 15.9% vs <1% in other supertypes |
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0137 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862; Yao 2021) | PARTIAL — F1=0.935 to dominant DG Glut supertype; no SGC-specific markers; shared target with regular granule cell |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2007 · PMID:18077687 | [18077687](https://pubmed.ncbi.nlm.nih.gov/18077687/) | Soma location |
| [2] | Unknown 2025 · PMID:40161709 | [40161709](https://pubmed.ncbi.nlm.nih.gov/40161709/) | Neurotransmitter type; Sorcs3 and Nptx2 as SGC markers |
