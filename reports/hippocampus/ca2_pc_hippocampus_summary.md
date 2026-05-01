# CA2 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA2 [UBERON:0014549] | [1] [2] |
| NT | glutamatergic | [3] |
| Markers | Pcp4+, Rgs14+, Amigo2+ | [4] [5] |

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] | — | — | 🟡 MODERATE | NT CONSISTENT · location APPROXIMATE · Pcp4/Rgs14/Amigo2 expression CONSISTENT | Best candidate |

1 edge total; relationship type: `PARTIAL_OVERLAP`

---

## 0100 CA2-FC-IG Glut_1 · 🟡 MODERATE

**Supporting evidence:**

- **Atlas metadata (NT):** SUPT_0100 belongs to subclass CS20230722_SUBC_025 (025 CA2-FC-IG Glut). The subclass name indicates glutamatergic identity, consistent with the CA2 pyramidal cell's glutamatergic NT type. [Atlas metadata]
- **Atlas metadata (location):** SUPT_0100 has 446 cells in Field CA2, pyramidal layer (MBA:446), consistent with the classical soma location in CA2 stratum pyramidale [UBERON:0014549]. This is the highest-scoring WMBv1 supertype candidate for CA2 pyramidal cells (discovery score 4). [Atlas metadata]
- **Pcp4 expression (CONSISTENT):** Pcp4 is a defining marker of the classical CA2 pyramidal cell [4]. Although Pcp4 is not listed among SUPT_0100's atlas defining markers (which include Lefty1, Il16, Etv1), precomputed stats from the WMBv1 HDF5 file show a mean expression of 11.26 in SUPT_0100 at the supertype level — indicating substantial Pcp4 expression is present even if the gene was not selected as a cluster-discriminating marker.
- **Rgs14 expression (CONSISTENT):** Rgs14 is a defining marker of CA2 pyramidal cells [4]. Precomputed stats show mean expression of 8.84 in SUPT_0100, confirming expression in this supertype.
- **Amigo2 expression (CONSISTENT):** Amigo2 is a defining marker of CA2 pyramidal cells [5]. Precomputed stats show mean expression of 7.39 in SUPT_0100, confirming expression in this supertype.
- **Annotation transfer (subclass level, PARTIAL):** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 CA2-IG-FC subclass label (n=19) onto WMBv1 (CCN20230722) shows 18/19 cells (94.7%) mapping to SUBC_025 CA2-FC-IG Glut at SUBCLASS level (F1=0.973, group_purity=1.0, target_purity=0.947). This strongly supports SUBC_025 membership for the classical CA2 pyramidal cell. [Annotation transfer]

**Marker evidence provenance:**

- **Pcp4:** Evidence is protein-level (IHC/immunostaining). Reference [4] confirmed Pcp4 by immunostaining with a Purkinje cell protein 4 (PCP4) antibody in mouse brain sections, identifying it as a robust delineator of CA3/CA2 and CA2/CA1 borders, in agreement with prior cytoarchitectural definitions of CA2. Cell-type specificity is strong: the antibody specifically marks the CA2 region. Precomputed atlas stats show Pcp4 is expressed in SUPT_0100 (mean=11.26) without being selected as a cluster discriminator — consistent with the gene being region-enriched rather than cluster-exclusive.
- **Rgs14:** Evidence is transcript-level from the same source [4], listing Rgs14 among a set of markers specifically or prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de No's CA2. Cell-type specificity: the listing is region-level (CA2) rather than confirmed by single-cell morphological reconstruction. Precomputed atlas stats confirm expression in SUPT_0100 (mean=8.84). No discrepancy between sources.
- **Amigo2:** Evidence is transcript-level [5]. Reference [5] states that Rgs14, Amigo2, and PCP4 are among genes highly expressed in CA2. Cell-type specificity: transcript enrichment in the CA2 region, not confirmed by patch-clamp or morphological fill. Precomputed atlas stats confirm expression in SUPT_0100 (mean=7.39). No discrepancy between sources. *(note: both [4] and [5] support region-level CA2 enrichment; neither provides single-cell morphologically verified CA2 PC specificity. A targeted cite-traverse for "Amigo2 CA2 pyramidal cell specificity" or "Rgs14 CA2 hippocampus mouse" may identify primary studies with stronger cell-type specificity.)*

**Concerns:**

- **Location (APPROXIMATE):** SUPT_0100 has 446 cells in Field CA2, pyramidal layer (MBA:446) but also substantial cells in Field CA1, stratum oriens (MBA:399): 292 cells; Field CA3, stratum oriens (MBA:486): 215 cells; Field CA3, pyramidal layer (MBA:495): 165 cells; and Field CA2, stratum radiatum (MBA:454): 55 cells. CA2 pyramidal layer cells are present but SUPT_0100 has comparable or greater totals in CA1/CA3 strata. *(note: CA1 and CA3 are immediately flanking CA2 in the hippocampal formation — the off-target counts could reflect MERFISH registration noise at subfield borders or genuine inclusion of transitional CA3c/CA1-proximal cells; this is weak counter-evidence consistent with adjacent region spread.)*
- **FC/IG contamination (caveat):** SUPT_0100's name includes FC (fasciola cinerea) and IG (indusium griseum) alongside CA2. These are small CA2-adjacent structures; classical CA2 pyramidal cells are distinct from FC/IG neurons. The PARTIAL_OVERLAP relationship reflects uncertainty about whether this supertype cleanly captures CA2 PCs or conflates them with FC/IG populations.
- **Supertype-level AT inconsistency (caveat):** At SUPERTYPE level, the Yao 2021 annotation transfer maps 18/19 cells (94.7%) to SUPT_0101 (0101 CA2-FC-IG Glut_2, F1=0.947) rather than SUPT_0100 (F1=0.1). However, SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by Fasciola cinerea (175 cells) and Induseum griseum (61 cells). This result reflects FC/IG contamination in the Yao CA2-IG-FC mixed label, not evidence against SUPT_0100 as the CA2 PC target. A CA2-specific dataset without FC/IG contamination is required for definitive assessment.

**What would upgrade confidence:**

- **Annotation transfer from a CA2-specific dataset** (AnnotationTransferEvidence): run MapMyCells (WMBv1 target, CCN20230722) using a source dataset with clean CA2 pyramidal cell labels — expected F1 ≥ 0.80 at SUPERTYPE level for SUPT_0100 [CS20230722_SUPT_0100]. This would distinguish SUPT_0100 vs SUPT_0101 correspondence for CA2 pyramidal cells proper and resolve the FC/IG contamination issue. GEO:GSE185862 (Yao 2021) is available but uses a mixed label; a dataset with cell-type-specific CA2 labelling is preferred. Resolves open question 1.
- **FISH validation of Rgs14 or Amigo2** (LiteratureEvidence): FISH validation in CA2 cells assigned to SUPT_0100 by MERFISH would clarify whether off-target cells in CA1/CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors. Resolves open question 1.
- **Targeted literature search** (LiteratureEvidence): The marker citations [4][5] support region-level CA2 enrichment but do not confirm cell-type specificity by single-cell morphological reconstruction. A cite-traverse for "Rgs14 CA2 pyramidal cell mouse" and "Amigo2 CA2 hippocampus specificity" could identify primary studies with stronger specificity — weak marker evidence is a gap that literature review can address without new experiments.

---

## Proposed experiments

### 1 — Annotation transfer (CA2-specific dataset)

- **What:** MapMyCells annotation transfer to WMBv1 (CCN20230722) using a source dataset with clean CA2 pyramidal cell labels (no FC/IG contamination).
- **Target:** F1 ≥ 0.80 at SUPERTYPE level for SUPT_0100 [CS20230722_SUPT_0100].
- **Expected output:** AnnotationTransferEvidence entry on edge_ca2_pc_hippocampus_to_supt_0100.
- **Resolves:** Open question 1 (FC/IG contamination); distinction between SUPT_0100 and SUPT_0101 for CA2 pyramidal cells.
- **Note:** The existing Yao 2021 AT (GEO:GSE185862) yields subclass F1=0.973 to SUBC_025 — partial support. Supertype resolution requires a CA2-only label source. The completed AT round is insufficient for SUPT_0100 vs SUPT_0101 disambiguation because the source label conflates CA2 with FC/IG cells.

### 2 — FISH / spatial validation

- **What:** FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 by MERFISH.
- **Target:** Confirm Rgs14+/Amigo2+ signal specifically in CA2 pyramidal layer; assess whether off-target cells in CA1/CA3 strata are marker-positive.
- **Expected output:** LiteratureEvidence entries supporting or refuting the APPROXIMATE location alignment on edge_ca2_pc_hippocampus_to_supt_0100.
- **Resolves:** Open question 1 (MERFISH registration noise vs. genuine CA3c/CA1 pyramidal cell inclusion).

---

## Open questions

1. Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors? FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 would clarify.

---

## Evidence base

| Edge | Evidence type | Supports |
|---|---|---|
| edge_ca2_pc_hippocampus_to_supt_0100 | ATLAS_METADATA | SUPPORT |
| edge_ca2_pc_hippocampus_to_supt_0100 | ANNOTATION_TRANSFER | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | soma location |
| [2] | Unknown 2021 · PMID:33956790 | [33956790](https://pubmed.ncbi.nlm.nih.gov/33956790/) | soma location |
| [3] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
| [4] | Unknown 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker; Rgs14 marker |
| [5] | Unknown 2012 · PMID:22904370 | [22904370](https://pubmed.ncbi.nlm.nih.gov/22904370/) | Amigo2 marker |
