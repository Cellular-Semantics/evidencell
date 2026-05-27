# CA2 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA2 [UBERON:0014549] | [1][2] |
| NT | Glutamatergic | [3] |
| Defining markers | Pcp4, Rgs14, Amigo2 | Pcp4: [4]; Rgs14: [4]; Amigo2: [5] |
| Negative markers | — | |
| Neuropeptides | — | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] | CA2-FC-IG Glut | 446 (CA2 pyramidal layer, MBA:446) | 🟡 MODERATE | NT CONSISTENT · location APPROXIMATE · Pcp4/Rgs14/Amigo2 expression CONSISTENT | Best candidate |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP.

---

## 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0100 belongs to subclass CS20230722_SUBC_025 (025 CA2-FC-IG Glut). The subclass name indicates glutamatergic identity, consistent with the CA2 pyramidal cell's glutamatergic neurotransmitter type [3].

- **Soma location — APPROXIMATE (supporting).** SUPT_0100 has 446 cells in Field CA2, pyramidal layer (MBA:446), consistent with the classical soma location in pyramidal layer of CA2 [UBERON:0014549] [1][2]. This is the highest-scoring WMBv1 supertype candidate for CA2 pyramidal cells (discovery score 4). The CA2 pyramidal layer representation is a positive anatomical correspondence.

- **Pcp4 expression — CONSISTENT.** Pcp4 is a defining marker of the classical CA2 pyramidal cell [4]. Although Pcp4 is not listed among SUPT_0100's atlas defining markers (Lefty1, Il16, Etv1), precomputed stats from the WMBv1 HDF5 file show mean expression = 11.26 in SUPT_0100 at the supertype level — indicating substantial Pcp4 expression even though the gene was not selected as a cluster-discriminating marker.

- **Rgs14 expression — CONSISTENT.** Rgs14 is a defining marker of CA2 pyramidal cells [4]. Precomputed stats show mean expression = 8.84 in SUPT_0100, confirming expression in this supertype.

- **Amigo2 expression — CONSISTENT.** Amigo2 is a defining marker of CA2 pyramidal cells [5]. Precomputed stats show mean expression = 7.39 in SUPT_0100, confirming expression in this supertype.

- **Annotation transfer at subclass level — PARTIAL.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 CA2-IG-FC subclass label (n=19) onto WMBv1 (CCN20230722) shows 18/19 cells (94.7%) mapping to SUBC_025 CA2-FC-IG Glut at SUBCLASS level (F1=0.973, coverage=1.0, purity=0.947). This strongly supports SUBC_025 membership for the classical CA2 pyramidal cell. At SUPERTYPE level, 18/19 cells (94.7%) map to SUPT_0101 (CA2-FC-IG Glut_2, F1=0.947) rather than SUPT_0100 (F1=0.1); however, SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by Fasciola cinerea (175 cells) and Indusium griseum (61 cells). This discrepancy reflects FC/IG contamination in the Yao mixed CA2-IG-FC label, not evidence against SUPT_0100 as the CA2 PC target.

**Marker evidence provenance**

- **Pcp4** [4]: Evidence is protein-level (IHC/immunostaining). Reference [4] confirmed Pcp4 by immunostaining with a Purkinje cell protein 4 (PCP4) antibody in mouse brain sections, identifying it as a robust delineator of CA3/CA2 and CA2/CA1 borders, in agreement with prior cytoarchitectural definitions of CA2. Cell-type specificity is strong: the antibody specifically marks the CA2 region with well-defined boundaries. Precomputed atlas stats show Pcp4 is expressed in SUPT_0100 (mean=11.26) without being selected as a cluster discriminator — consistent with the gene being region-enriched rather than cluster-exclusive. No discrepancy between sources.

- **Rgs14** [4]: Evidence is transcript-level from the same source [4], listing Rgs14 among a set of markers specifically or more prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de No's CA2. Cell-type specificity: the listing is region-level (CA2) rather than confirmed by single-cell morphological reconstruction. Precomputed atlas stats confirm expression in SUPT_0100 (mean=8.84). No discrepancy between sources. *(Recommendation: A targeted cite-traverse for "Rgs14 CA2 pyramidal cell mouse" may identify primary studies with stronger single-cell specificity.)*

- **Amigo2** [5]: Evidence is transcript-level [5], reporting that Rgs14, Amigo2, and PCP4 are among genes highly expressed in CA2. Cell-type specificity: transcript enrichment in the CA2 region; not confirmed by patch-clamp or morphological fill. Precomputed atlas stats confirm expression in SUPT_0100 (mean=7.39). No discrepancy between sources. Both [4] and [5] support region-level CA2 enrichment; neither provides single-cell morphologically verified CA2 PC specificity. *(Recommendation: A targeted cite-traverse for "Amigo2 CA2 pyramidal cell specificity" may resolve this gap.)*

**Concerns**

- **Location — APPROXIMATE.** SUPT_0100 has 446 cells in Field CA2, pyramidal layer (MBA:446) but also substantial cells in Field CA1, stratum oriens (MBA:399): 292 cells; Field CA3, stratum oriens (MBA:486): 215 cells; Field CA3, pyramidal layer (MBA:495): 165 cells; and Field CA2, stratum radiatum (MBA:454): 55 cells. CA2 pyramidal layer cells are present but SUPT_0100 has comparable or greater totals in adjacent CA1/CA3 strata. *(note: CA1 and CA3 immediately flank CA2 in the hippocampal formation — the off-target counts could reflect MERFISH registration noise at subfield borders or genuine inclusion of transitional CA3c/CA1-proximal cells; this is weak counter-evidence consistent with adjacent region spread.)*

- **FC/IG contamination.** SUPT_0100's name includes FC (fasciola cinerea) and IG (indusium griseum) alongside CA2. These are small CA2-adjacent structures; classical CA2 pyramidal cells are distinct from FC/IG neurons. The PARTIAL_OVERLAP relationship reflects uncertainty about whether this supertype cleanly captures CA2 PCs or conflates them with FC/IG populations.

- **Supertype-level AT inconsistency.** At SUPERTYPE level, the Yao 2021 annotation transfer maps 18/19 cells (94.7%) to SUPT_0101 (F1=0.947) rather than SUPT_0100 (F1=0.1). SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by Fasciola cinerea (175 cells) and Indusium griseum (61 cells). This result reflects FC/IG contamination in the Yao CA2-IG-FC mixed label — it does not constitute evidence that SUPT_0100 is the wrong target for CA2 pyramidal cells.

**What would upgrade confidence**

- **Annotation transfer from a CA2-specific dataset** (AnnotationTransferEvidence): run MapMyCells (WMBv1 target, CCN20230722) using a source dataset with clean CA2 pyramidal cell labels — expected F1 ≥ 0.80 at SUPERTYPE level for SUPT_0100 [CS20230722_SUPT_0100]. This would distinguish SUPT_0100 vs SUPT_0101 correspondence for CA2 pyramidal cells proper and resolve the FC/IG contamination issue. Resolves open question 1.

- **FISH validation of Rgs14 or Amigo2** (LiteratureEvidence): FISH validation in CA2 cells assigned to SUPT_0100 by MERFISH would clarify whether off-target cells in CA1/CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors. Resolves open question 1.

- **Targeted literature search** (LiteratureEvidence): A cite-traverse for "Rgs14 CA2 pyramidal cell mouse" and "Amigo2 CA2 hippocampus specificity" could identify primary studies with stronger cell-type specificity — weak marker evidence at the single-cell level is a gap that literature review can address without new experiments.

---

## Proposed experiments

*Note on existing AT evidence:* The Yao 2021 (GEO:GSE185862) annotation transfer yields subclass F1=0.973 to SUBC_025 — strong partial support. Supertype resolution requires a CA2-only label source. The completed AT round is insufficient for SUPT_0100 vs SUPT_0101 disambiguation because the source label conflates CA2 with FC/IG cells.

### Annotation transfer (CA2-specific dataset)

- **What:** MapMyCells annotation transfer to WMBv1 (CCN20230722) using a source dataset with clean CA2 pyramidal cell labels (no FC/IG contamination).
- **Target:** F1 ≥ 0.80 at SUPERTYPE level for SUPT_0100 [CS20230722_SUPT_0100].
- **Expected output:** AnnotationTransferEvidence entry on edge_ca2_pc_hippocampus_to_supt_0100.
- **Resolves:** Open question 1 (FC/IG contamination; SUPT_0100 vs SUPT_0101 disambiguation).

### FISH / spatial validation

- **What:** FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 by MERFISH.
- **Target:** Confirm Rgs14+/Amigo2+ signal specifically in CA2 pyramidal layer; assess whether off-target cells in CA1/CA3 strata are marker-positive.
- **Expected output:** LiteratureEvidence entries supporting or refuting the APPROXIMATE location alignment on edge_ca2_pc_hippocampus_to_supt_0100.
- **Resolves:** Open question 1 (MERFISH registration noise vs. genuine CA3c/CA1 pyramidal cell inclusion).

---

## Open questions

1. Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors? FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 would clarify.

---

## Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ca2_pc_hippocampus_to_supt_0100 | ATLAS_METADATA | SUPPORT — SUPT_0100 highest-scoring CA2 Glut supertype; NT CONSISTENT, 446 cells in CA2 pyramidal layer (MBA:446); Pcp4 mean=11.26, Rgs14 mean=8.84, Amigo2 mean=7.39 |
| edge_ca2_pc_hippocampus_to_supt_0100 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | PARTIAL — Subclass F1=0.973 to SUBC_025 SUPPORT; supertype-level mapping to SUPT_0101 reflects FC/IG contamination in source label |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Soma location |
| [2] | Unknown 2021 · PMID:33956790 | [33956790](https://pubmed.ncbi.nlm.nih.gov/33956790/) | Soma location |
| [3] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | Neurotransmitter type |
| [4] | Unknown 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker; Rgs14 marker |
| [5] | Unknown 2012 · PMID:22904370 | [22904370](https://pubmed.ncbi.nlm.nih.gov/22904370/) | Amigo2 marker |
