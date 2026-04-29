# CA2 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA2 [UBERON:0014549] (CA2 stratum pyramidale) | [1], [2], [3] |
| Neurotransmitter | Glutamatergic | [4] |
| Defining markers | Pcp4, Rgs14, Amigo2 | Pcp4: [5]; Rgs14: [5]; Amigo2: [6] |

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] | CA2-FC-IG Glut | — | 🔴 LOW | NT CONSISTENT · Location APPROXIMATE · Markers NOT_ASSESSED | Speculative |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP — classical CA2 pyramidal cell identity is partially captured by Supertype [CS20230722_SUPT_0100], but the supertype conflates CA2 with fasciola cinerea (FC) and indusium griseum (IG) populations.

---

## 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] · 🔴 LOW

### Supporting evidence

- **Glutamatergic neurotransmitter type consistent.** Supertype [CS20230722_SUPT_0100] belongs to subclass CS20230722_SUBC_025 (025 CA2-FC-IG Glut), fully consistent with the glutamatergic identity of CA2 pyramidal cells [4]. The NT match is the strongest positive signal for this edge.
- **CA2 pyramidal layer cells present.** Atlas MERFISH data registers 446 cells in Field CA2, pyramidal layer (MBA:446), directly consistent with the expected soma location of CA2 PCs in pyramidal layer of CA2 [UBERON:0014549] [1], [2], [3]. This is the primary anatomical support.
- **Highest-scoring WMBv1 supertype candidate.** Supertype [CS20230722_SUPT_0100] received a discovery score of 4 — the highest among evaluated WMBv1 supertypes — based on the combination of glutamatergic NT type, CA2 subfield name, and pyramidal layer MERFISH enrichment.

### Marker evidence provenance

- **Pcp4 (defining marker):** Protein-level evidence: Antonio et al. 2014 [5] used immunostaining with a PCP4 antibody to identify and delineate the CA2 region, demonstrating that Pcp4 effectively marks CA3/CA2 and CA2/CA1 borders. Cell-type specificity is high — the CA2 region is defined by this marker in mouse. Source: "Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2" (Antonio et al. 2014, abstract [5]). Target-side: Pcp4 does not appear in Supertype [CS20230722_SUPT_0100] defining markers (listed: Lefty1, Il16, Etv1). Atlas expression status NOT_ASSESSED without precomputed stats.

- **Rgs14 (defining marker):** Protein-level evidence from Antonio et al. 2014 [5], listing Rgs14 among markers specifically or more prominently expressed in the distal portion of regio inferior corresponding to CA2: "These markers include Purkinje cell protein 4 (PCP4), neurotrophin 3, fibroblast growth factor, a-actinin 2, adenosine A1 receptor, vasopressin 1b receptor, RGS14 (regulator of G-protein signaling 14), and amigo2. These markers are specifically or more prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de Nó's CA2" (Antonio et al. 2014, Introduction [5]). Cell-type specificity is high. Target-side: Rgs14 does not appear in Supertype [CS20230722_SUPT_0100] defining markers; atlas expression status NOT_ASSESSED.

- **Amigo2 (defining marker):** Transcript-level evidence from Caruana et al. 2012 [6]: "a number of genes, including the regulator of G-protein signaling 14 (RGS14), Amigo2, PCP4, TARP5, FGF5, and several adenylyl cyclases (e.g., adcy1, adcy5, and adcy6), are highly expressed in CA2" (Caruana et al. 2012, Introduction [6]). Specificity is moderate — the citation does not provide direct ISH or protein-level data for Amigo2 in isolation but lists it among confirmed CA2-enriched transcripts. Target-side: Amigo2 does not appear in Supertype [CS20230722_SUPT_0100] defining markers; atlas expression status NOT_ASSESSED.

### Concerns

- **FC and IG components conflate with CA2 identity.** The Supertype [CS20230722_SUPT_0100] name explicitly includes fasciola cinerea (FC) and indusium griseum (IG) alongside CA2. These are small CA2-adjacent structures; classical CA2 pyramidal cells are morphologically, electrophysiologically, and molecularly distinct from FC/IG neurons. The PARTIAL_OVERLAP relationship reflects genuine uncertainty about whether this supertype cleanly captures CA2 PCs or conflates them with FC/IG populations.
- **Location APPROXIMATE — substantial non-CA2 cell counts.** Supertype [CS20230722_SUPT_0100] MERFISH distribution: 446 cells in Field CA2, pyramidal layer (MBA:446); 292 cells in Field CA1, stratum oriens (MBA:399); 215 cells in Field CA3, stratum oriens (MBA:486); 165 cells in Field CA3, pyramidal layer (MBA:495); 55 cells in Field CA2, stratum radiatum (MBA:454). The CA1 and CA3 strata contribute comparable or greater total cell counts than the primary CA2 pyramidal layer signal, raising the possibility that this supertype spans CA2 and transitional CA1/CA3 pyramidal cells or contains MERFISH registration noise at subfield borders. *(note: deep CA3c cells near the CA2 border are known to share some molecular features with CA2 PCs; their inclusion cannot be ruled out from atlas metadata alone.)*
- **All three defining markers NOT_ASSESSED at atlas level.** Pcp4, Rgs14, and Amigo2 — the canonical CA2 markers — do not appear in Supertype [CS20230722_SUPT_0100] defining marker fields. Without precomputed expression statistics, it is impossible to determine whether these markers are expressed in the CA2 cells of this supertype or are diluted out by the FC/IG component.
- **Annotation transfer indicates FC/IG component dominates.** Annotation transfer of the Yao 2021 (GSE185862) CA2-IG-FC subclass label (n=19) maps 94.7% of cells to the sibling supertype CS20230722_SUPT_0101 (0101 CA2-FC-IG Glut_2, F1=0.947), not to Supertype [CS20230722_SUPT_0100] (F1=0.1). Notably, CS20230722_SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by fasciola cinerea (175 cells) and indusium griseum (61 cells), while Supertype [CS20230722_SUPT_0100] has 106 CA2 pyramidal layer cells and 0 FC/IG cells. *(note: this AT result is not counter-evidence against Supertype [CS20230722_SUPT_0100] as the CA2 PC target — it reflects the FC/IG component of Yao's mixed CA2-IG-FC label mapping to the FC/IG-enriched atlas supertype CS20230722_SUPT_0101. A CA2-specific source dataset is required for a valid annotation transfer test.)*

### What would upgrade confidence

- **Precomputed expression for Rgs14 and Pcp4 in Supertype [CS20230722_SUPT_0100] (ATLAS_QUERY / add-expression).** Querying per-supertype expression of Rgs14, Pcp4, and Amigo2 would convert all three NOT_ASSESSED marker alignments to CONSISTENT or DISCORDANT. If all three are enriched, confidence would upgrade to MODERATE or HIGH. This is the highest-priority action.
- **Annotation transfer from a CA2-specific dataset (AnnotationTransferEvidence).** Running MapMyCells on a dataset with a pure CA2 pyramidal cell label (e.g. Caramello 2024 CA2 scRNA-seq, or Yao 2021 CA2 pyramidal cells isolated from the CA2-IG-FC label by spatial filtering) would test whether CA2 PCs preferentially map to Supertype [CS20230722_SUPT_0100] vs CS20230722_SUPT_0101. A successful F1 ≥ 0.70 at supertype level on a CA2-only source would upgrade to MODERATE. Resolves open question 1.
- **FISH validation of Rgs14 or Amigo2 co-labelled with SUPT_0100 defining markers (LiteratureEvidence).** Double-label FISH of Rgs14 or Amigo2 with one of the Supertype [CS20230722_SUPT_0100] defining genes (Lefty1, Il16, or Etv1) in the CA2 pyramidal layer would provide spatial confirmation that marker-positive CA2 cells fall within this transcriptomic supertype. Resolves open question 1.

---

## Proposed experiments

### Group 1 — Atlas expression query

- **What:** Query ABC Atlas or Allen Cell Types Database precomputed expression statistics for Rgs14, Pcp4, and Amigo2 in Supertype [CS20230722_SUPT_0100] (0100 CA2-FC-IG Glut_1) using `just add-expression` or direct HDF5 stats access.
- **Target:** Detection rate and mean expression for each of the three canonical CA2 markers in Supertype [CS20230722_SUPT_0100].
- **Expected output:** ATLAS_QUERY evidence item converting the three NOT_ASSESSED marker alignments to CONSISTENT or DISCORDANT. If enriched, upgrade edge confidence to MODERATE.
- **Resolves:** NOT_ASSESSED marker gaps for Pcp4, Rgs14, Amigo2; open question 1.

### Group 2 — Annotation transfer from CA2-specific dataset

- **What:** MapMyCells (cell_type_mapper, WMBv1 CCN20230722) on a CA2-only source dataset (e.g. Caramello et al. 2024 CA2 scRNA-seq; or Yao 2021 CA2 pyramidal cells isolated from the CA2-IG-FC label by spatial filtering). Differs from the completed Yao 2021 AT round, which used a mixed CA2-IG-FC label dominated by FC/IG cells.
- **Target:** F1 ≥ 0.70 at supertype level for Supertype [CS20230722_SUPT_0100]; distinguish Supertype [CS20230722_SUPT_0100] vs CS20230722_SUPT_0101 as the CA2 PC transcriptomic target.
- **Expected output:** AnnotationTransferEvidence on edge_ca2_pc_hippocampus_to_supt_0100; would clarify whether Supertype [CS20230722_SUPT_0100] or CS20230722_SUPT_0101 better captures CA2 pyramidal cell identity.
- **Resolves:** Open question 1.

### Group 3 — FISH spatial validation

- **What:** Double-label fluorescence in situ hybridisation (FISH) or smFISH of Rgs14 (or Amigo2) co-stained with one of the Supertype [CS20230722_SUPT_0100] defining markers (Lefty1, Il16, or Etv1) in CA2 pyramidal layer sections.
- **Target:** Spatial confirmation of ≥50% overlap between Rgs14+ CA2 pyramidal layer cells and Supertype [CS20230722_SUPT_0100] defining marker expression.
- **Expected output:** LiteratureEvidence on edge_ca2_pc_hippocampus_to_supt_0100; direct spatial proof linking classical CA2 marker identity to atlas supertype.
- **Resolves:** Open question 1; marker alignment gaps.

---

## Open questions

1. Do the CA2 pyramidal layer cells registered to Supertype [CS20230722_SUPT_0100] (n=446, MBA:446) express the canonical CA2 markers Pcp4, Rgs14, and Amigo2? Are the substantial non-CA2 cells in this supertype (CA1 stratum oriens: 292; CA3 stratum oriens: 215; CA3 pyramidal layer: 165) genuine pyramidal neurons (e.g. deep CA3c cells near the CA2 border) or MERFISH registration artefacts? FISH validation of Rgs14 or Amigo2 co-labelled with Supertype [CS20230722_SUPT_0100] defining markers in the CA2 pyramidal layer would resolve both issues. *(edge_ca2_pc_hippocampus_to_supt_0100)*

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ca2_pc_hippocampus_to_supt_0100 | ATLAS_METADATA | SUPPORT — NT match; 446 CA2 pyramidal layer cells present; substantial non-CA2 counts (APPROXIMATE location); all three CA2 markers NOT_ASSESSED |
| edge_ca2_pc_hippocampus_to_supt_0100 | ANNOTATION_TRANSFER (indirect) | NEUTRAL — Yao 2021 CA2-IG-FC mixed label maps to CS20230722_SUPT_0101 (FC/IG component dominates); does not test pure CA2 PC identity; CA2-only AT not yet performed |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Soma location |
| [2] | CorpusId:18555666 | — | Soma location |
| [3] | Sanchez-Aguilera et al. 2021 | [33956790](https://pubmed.ncbi.nlm.nih.gov/33956790/) | Soma location |
| [4] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | Neurotransmitter type (glutamatergic) |
| [5] | Antonio et al. 2014 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 and Rgs14 markers |
| [6] | Caruana et al. 2012 | [22904370](https://pubmed.ncbi.nlm.nih.gov/22904370/) | Amigo2 marker |
