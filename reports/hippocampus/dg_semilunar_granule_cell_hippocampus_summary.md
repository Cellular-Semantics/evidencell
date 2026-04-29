# dentate gyrus semilunar granule cell — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus of hippocampal formation [UBERON:0001885] (*DG stratum granulosum, inner/outer border*) | [1] |
| Neurotransmitter | Glutamatergic | [2] |
| Defining markers | — | — |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | dentate gyrus granule cell [CL:2000089] (BROAD) | — |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells mapped | Confidence | Key alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0138 | 0138 DG Glut_3 | 82 (GSE280167) | 🟡 MODERATE | NT consistent; *Sorcs3* 6x enrichment; *Nptx2* elevated | Best candidate |
| 2 | CS20230722_SUPT_0137 | 0137 DG Glut_2 | 2172 (GSE185862) | 🔴 LOW | NT consistent; location approximate; no SGC-specific marker evidence | Speculative |

**Total edges: 2 · Relationship type: PARTIAL_OVERLAP.** *(note: semilunar granule cells are a minor morpho-physiologically distinct subpopulation within the DG granule cell layer; the dominant granule cell type maps to SUPT_0137 — see dg_granule_cell_hippocampus)*

---

## 0138 DG Glut_3 [CS20230722_SUPT_0138] · 🟡 MODERATE

### Supporting evidence

**Annotation transfer — GSE280167 (Bhatt 2025).** MapMyCells local annotation transfer of Bhatt 2025 (GEO:GSE280167) dentate gyrus snRNA-seq data (wild-type VV samples, 4 animals, 11,601 DG Glut cells) onto WMBv1 (CCN20230722). Among the four DG Glut supertypes, SUPT_0138 [CS20230722_SUPT_0138] (DG Glut_3, n=82 cells, 0.7% of DG cells) shows marked enrichment for the semilunar granule cell (SGC) marker *Sorcs3*: 53.7% of SUPT_0138 cells express *Sorcs3* (mean 4.93 UMIs) versus 9.1% in SUPT_0137 — a 6-fold enrichment. *Nptx2*, a second SGC marker, is also elevated in SUPT_0138 (15.9% cells expressing) versus near-absent in other DG supertypes (<1%). *Penk*, the third Bhatt 2025 SGC marker, is sparsely detected across all DG supertypes (<2%), likely due to nuclear RNA dropout in snRNA-seq. The minor cell count (0.7% of DG cells) is consistent with the known rarity of SGCs in the DG granule cell layer.

### Marker evidence provenance

- ***Sorcs3*** — established as an SGC marker in Bhatt 2025 (GEO:GSE280167). SUPT_0138 shows 6x relative enrichment compared to SUPT_0137 (53.7% vs 9.1% cells expressing; mean 4.93 vs 0.20 UMIs). This is the primary positive evidence for this mapping. No marker is listed as a primary source reference in the classical node reference_index — **recommend cite-traverse on *Sorcs3* and semilunar granule cells to identify peer-reviewed primary sources**.
- ***Nptx2*** — established as an SGC marker in Bhatt 2025 (GEO:GSE280167). Elevated in SUPT_0138 (15.9% cells) vs <1% in other DG supertypes. No primary literature citation available in the current reference_index — **recommend cite-traverse on *Nptx2* and dentate gyrus SGC to identify peer-reviewed primary sources**.
- ***Penk*** — identified as an SGC marker in Bhatt 2025 but undetectable in this analysis due to snRNA-seq nuclear RNA dropout. Not assessed in SUPT_0138.
- **SUPT_0138 atlas markers** (*Lct*, *Atf3*) are not classical SGC markers. Their biological significance in the context of SGC identity is unknown — they may reflect the transcriptomic state captured by WMBv1 or technical factors.

### Concerns

- **Ambiguous mapping:** The SGC evidence is based on marker enrichment (*Sorcs3*, *Nptx2*) in SUPT_0138 from GSE280167, not from a formally annotated SGC cluster. The Bhatt 2025 paper uses both ATAC and RNA data together for cluster annotation; the RNA-only analysis here may miss the full SGC signature.
- **Very small reference population:** SUPT_0138 has n=82 cells in GSE280167 and an estimated n=28 in Yao 2021, consistent with either genuine rarity or poor sampling. Low cell counts reduce the statistical confidence of enrichment estimates.
- **Mapping uncertainty with SUPT_0137:** SUPT_0137 (DG Glut_2) is the dominant DG mapping target for regular granule cells and cannot be excluded as a partial SGC target without formal cluster annotations from Bhatt 2025.

### What would upgrade confidence

- Obtain the Bhatt 2025 published cluster annotations for GSE280167 to formally identify the SGC cluster (Cluster 18, *Sorcs3*+/*Penk*+/*Nptx2*+) and confirm it maps specifically to SUPT_0138.
- Run differential expression between *Sorcs3*-high SUPT_0138 cells and SUPT_0137 cells in GSE280167 to find additional SGC-specific markers for property comparison.
- Query WMBv1 precomputed expression statistics for *Sorcs3* and *Nptx2* across all DG Glut supertypes (SUBC_037) via `just add-expression` to confirm atlas-level enrichment in SUPT_0138.
- Assess MERFISH soma locations for SUPT_0138 cells to determine whether they are enriched at the inner/outer border of the DG granule cell layer (the anatomical location of SGCs).

---

## 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🔴 LOW

### Supporting evidence

**Annotation transfer — GSE185862 (Yao 2021 SSv4).** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722). Yao 2021 DG subclass cells (n=2473) map to SUPT_0137 [CS20230722_SUPT_0137] with group_purity=0.878 and F1=0.935, confirming SUPT_0137 as the dominant DG glutamatergic supertype in that dataset. This edge is PARTIAL_SUPPORT: SUPT_0137 is the shared target with dg_granule_cell_hippocampus (the regular granule cell). Without molecular markers specific to SGCs, Yao 2021 DG cells cannot be distinguished as SGC vs. regular granule cell.

### Marker evidence provenance

- **No molecular markers are established for SGCs** on the classical node, preventing direct comparison with SUPT_0137 defining markers (*Dsp*, *Kcnh3*, *Syndig1*). The marker comparison is recorded as NOT_ASSESSED.
- **SUPT_0137 atlas markers** (*Dsp*, *Kcnh3*, *Syndig1*) have not been reported as SGC-specific in the literature — these likely represent regular granule cell identity.

### Concerns

- **Ambiguous mapping — shared target:** SUPT_0137 is the primary mapping target for the regular DG granule cell (dg_granule_cell_hippocampus). There is no positive evidence from the Yao 2021 dataset that SUPT_0137 captures SGCs specifically rather than the dominant regular granule cell population.
- **No SGC-specific markers available:** Without molecular markers distinguishing SGCs from regular granule cells in any currently available dataset, this edge cannot be resolved from atlas metadata alone.
- **SUPT_0139 also a candidate:** SUPT_0139 (DG Glut_4, 9.1% of DG cells) is an unassessed candidate for a morpho-physiologically distinct DG subpopulation and should be considered in future mapping rounds.

### What would upgrade confidence

- Obtain Bhatt 2025 (GSE280167) cluster annotations for SGCs and run annotation transfer to test whether the SGC cluster maps to SUPT_0137, SUPT_0138, or SUPT_0139.
- Differential expression between DG cells mapping to SUPT_0139 vs. SUPT_0137 in Yao 2021 may reveal candidate SGC markers.

---

## Eliminated candidates

No edges have been eliminated as UNCERTAIN. SUPT_0139 (DG Glut_4) remains an unassessed candidate and should be considered in future mapping rounds.

---

## Proposed experiments

### Formal SGC cluster identification — Bhatt 2025

| Attribute | Detail |
|---|---|
| **What** | Obtain published cluster annotations from Bhatt 2025 (GSE280167) and confirm that the SGC cluster maps to SUPT_0138 [CS20230722_SUPT_0138] via MapMyCells |
| **Target** | Group_purity ≥ 0.5 and F1 ≥ 0.6 for SGC cluster → SUPT_0138 |
| **Expected output** | AnnotationTransferEvidence entry upgrading SUPT_0138 edge to MODERATE/HIGH |
| **Resolves** | Primary ambiguity: whether SUPT_0138 formally captures the SGC transcriptome |

### Atlas expression query — Sorcs3 and Nptx2

| Attribute | Detail |
|---|---|
| **What** | Query WMBv1 precomputed expression statistics for *Sorcs3* and *Nptx2* across all DG Glut supertypes (SUBC_037) using `just add-expression` |
| **Target** | Confirmed higher mean expression and fraction-expressing in SUPT_0138 vs. SUPT_0137 |
| **Expected output** | MarkerSource entries on SUPT_0138 node for *Sorcs3* and *Nptx2* |
| **Resolves** | NOT_ASSESSED status for SGC marker enrichment in atlas; formalises SUPT_0138 as atlas-level SGC-enriched supertype |

### Differential expression — SGC vs. regular granule cells

| Attribute | Detail |
|---|---|
| **What** | Run differential expression between *Sorcs3*-high SUPT_0138 cells and SUPT_0137 cells in GSE280167 |
| **Target** | ≥ 5 genes with ≥ 2-fold enrichment and adjusted p < 0.05 in the SGC-enriched population |
| **Expected output** | Candidate SGC-specific marker list for cite-traverse follow-up |
| **Resolves** | Absence of defining markers on the classical SGC node; provides candidates for primary literature search |

---

## Open questions

1. Does *Sorcs3* appear in the SUPT_0138 defining markers in the WMBv1 precomputed stats? Running `add-expression` for *Sorcs3* and *Nptx2* in DG Glut supertypes (SUBC_037) would formalise this enrichment at the atlas level.
2. Are SUPT_0138 cells specifically enriched at the inner/outer border of the DG granule cell layer (the anatomical location of SGCs) in the WMBv1 MERFISH data?

---

## Evidence base

| Edge ID | Evidence type | Details | Supports |
|---|---|---|---|
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0138 | ANNOTATION_TRANSFER | GSE280167 (Bhatt 2025 snRNA-seq); 82 DG cells → SUPT_0138 [CS20230722_SUPT_0138]; *Sorcs3* 53.7% cells (mean 4.93 UMIs), 6x enrichment vs SUPT_0137; *Nptx2* 15.9% cells | SUPPORT |
| edge_dg_semilunar_granule_cell_hippocampus_to_supt_0137 | ANNOTATION_TRANSFER | GSE185862 (Yao 2021 SSv4); 2172/2473 DG cells → SUPT_0137 [CS20230722_SUPT_0137]; group_purity=0.878, F1=0.935; no SGC-specific marker evidence | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2007 | [18077687](https://pubmed.ncbi.nlm.nih.gov/18077687/) | Soma location |
| [2] | Unknown 2025 | [40161709](https://pubmed.ncbi.nlm.nih.gov/40161709/) | Neurotransmitter type |
