# dentate gyrus semilunar granule cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus granule cell (CL:2000089) | |
| Soma location | dentate gyrus stratum granulosum (inner/outer border) [UBERON:0001885] | [1] |
| NT | glutamatergic | [2] |
| Markers |  |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0138 DG Glut_3 [CS20230722_SUPT_0138] |  | — | 🟡 MODERATE | Best candidate |
| 2 | 0137 DG Glut_2 [CS20230722_SUPT_0137] |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## 0138 DG Glut_3 · 🟡 MODERATE

**Supporting evidence:**

- MapMyCells local annotation transfer of Bhatt 2025 (GSE280167) dentate gyrus snRNA-seq (wild-type VV samples, 4 animals, 11,601 DG Glut cells) onto WMBv1 (CCN20230722). Among the four DG Glut supertypes, SUPT_0138 (DG Glut_3, n=82 cells, 0.7% of DG cells) shows marked enrichment for the semilunar granule cell (SGC) marker Sorcs3: 53.7% of SUPT_0138 cells express Sorcs3 (mean=4.93 UMIs) vs 9.1% in SUPT_0137 (mean=0.20). Nptx2, a second SGC marker, is also elevated in SUPT_0138 (15.9% cells) vs near-absent in other DG supertypes (<1%). Penk, the third Bhatt 2025 SGC marker, is sparsely detected across all DG supertypes (<2%), likely due to nuclear RNA dropout in snRNA-seq. The minor cell count (0.7% of DG) is consistent with the known rarity of SGCs in the DG granule cell layer. SUPT_0138 markers Lct and Atf3 are not classical SGC markers but may reflect the transcriptomic state captured by WMBv1. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=dentate gyrus stratum granulosum inner/outer border (UBERON:0001885) / B=SUPT_0138 in DG Glut subclass; anatomy not assessed in MERFISH. 
- The SGC evidence is based on marker enrichment (Sorcs3, Nptx2) in SUPT_0138 from GSE280167, not from a formally annotated SGC cluster. The Bhatt 2025 paper uses ATAC and RNA data together for cluster annotation; our RNA-only analysis may miss the full SGC signature. SUPT_0138 (n=82 in GSE280167, n=28 in Yao 2021) is a minor DG subpopulation. The edge to SUPT_0137 (dg_semilunar_granule_cell edge to dominant DG supertype) should be retained as the major mapping uncertainty.

**What would upgrade confidence:**

- *Unresolved:* Does Sorcs3 appear in the SUPT_0138 defining markers in the WMBv1 precomputed stats? Running add-expression for Sorcs3 and Nptx2 in DG Glut supertypes (SUBC_037) would formalize this enrichment at the atlas level.

- *Unresolved:* Are SUPT_0138 cells specifically enriched at the inner/outer border of the DG granule cell layer (the anatomical location of SGCs) in the WMBv1 MERFISH data?

- *Proposed:* Run differential expression between Sorcs3-high SUPT_0138 cells and SUPT_0137 cells in GSE280167 to find additional SGC-specific markers.

- *Proposed:* Obtain the Bhatt 2025 published cluster annotations for GSE280167 to formally identify Cluster 18 (SGC) and confirm SUPT_0138 correspondence.


---

## 0137 DG Glut_2 · 🔴 LOW

**Supporting evidence:**

- Annotation transfer of Yao 2021 (GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722) via local MapMyCells. Yao 2021 DG subclass cells (n=2473) map to SUPT_0137 with group_purity=0.878 and F1=0.935, confirming SUPT_0137 as the dominant DG glutamatergic supertype. SUPT_0137 is shared between dg_granule_cell_hippocampus and this node (dg_semilunar_granule_cell_hippocampus); the semilunar granule cell is a morpho-physiologically distinct DG subpopulation for which no transcriptome-specific markers are available in this dataset. PARTIAL_SUPPORT reflects that this edge targets the same atlas node as the regular granule cell — a more specific sub-supertype mapping requires either molecular markers (see gaps in validation_notes.json) or the Bhatt 2025 (GSE280167) SGC snRNA-seq data. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=dentate gyrus stratum granulosum inner/outer border (UBERON:0001885) / B=SUPT_0137 includes cells in DG granule cell layer and molecular layer. Semilunar granule cells are found at the inner/outer border of the stratum granulosum; the MERFISH assignment for SUPT_0137 covers the granule cell layer broadly (MBA:632).

- Semilunar granule cells (SGCs) share the SUPT_0137 target with dg_granule_cell_hippocampus (see edge_dg_granule_cell_hippocampus_to_supt_0137). Without molecular markers specific to SGCs, there is no evidence that SUPT_0137 preferentially captures SGCs vs. regular granule cells. SUPT_0139 (DG Glut_4, 9.1% of DG cells) is also a candidate for a morpho-physiologically distinct DG subpopulation.

**What would upgrade confidence:**

- *Unresolved:* Bhatt 2025 (GSE280167) identifies a SGC-enriched cluster (Cluster 18, Sorcs3+/Penk+/Nptx2+). Does this cluster map specifically to SUPT_0139 or to a SUPT_0137 sub-cluster? Running MapMyCells on GSE280167 will resolve.

- *Unresolved:* Are there transcriptomic markers that distinguish SGCs from regular DG granule cells in the Yao 2021 dataset? Differential expression between DG cells mapping to SUPT_0139 vs SUPT_0137 might reveal candidate markers.

- *Proposed:* Run add-expression for Sorcs3 and Nptx2 in DG Glut supertypes (SUBT_037) via CCN20230722 precomputed stats to validate the SUPT_0138 enrichment signal seen in GSE280167 cells.


---

## Proposed experiments

### 1 — Other

- Run add-expression for Sorcs3 and Nptx2 in DG Glut supertypes (SUBT_037) via CCN20230722 precomputed stats to validate the SUPT_0138 enrichment signal seen in GSE280167 cells.
- Run differential expression between Sorcs3-high SUPT_0138 cells and SUPT_0137 cells in GSE280167 to find additional SGC-specific markers.
- Obtain the Bhatt 2025 published cluster annotations for GSE280167 to formally identify Cluster 18 (SGC) and confirm SUPT_0138 correspondence.
*Resolves: edge_dg_semilunar_granule_cell_hippocampus_to_supt_0137, edge_dg_semilunar_granule_cell_hippocampus_to_supt_0138*

---

## Open questions

1. Does Sorcs3 appear in the SUPT_0138 defining markers in the WMBv1 precomputed stats? Running add-expression for Sorcs3 and Nptx2 in DG Glut supertypes (SUBC_037) would formalize this enrichment at the atlas level.
2. Are SUPT_0138 cells specifically enriched at the inner/outer border of the DG granule cell layer (the anatomical location of SGCs) in the WMBv1 MERFISH data?
3. Bhatt 2025 (GSE280167) identifies a SGC-enriched cluster (Cluster 18, Sorcs3+/Penk+/Nptx2+). Does this cluster map specifically to SUPT_0139 or to a SUPT_0137 sub-cluster? Running MapMyCells on GSE280167 will resolve.
4. Are there transcriptomic markers that distinguish SGCs from regular DG granule cells in the Yao 2021 dataset? Differential expression between DG cells mapping to SUPT_0139 vs SUPT_0137 might reveal candidate markers.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0138 | Annotation transfer | SUPPORT |
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0137 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2007 · PMID:18077687 | [18077687](https://pubmed.ncbi.nlm.nih.gov/18077687/) | soma location |
| [2] | Unknown 2025 · PMID:40161709 | [40161709](https://pubmed.ncbi.nlm.nih.gov/40161709/) | neurotransmitter type |
