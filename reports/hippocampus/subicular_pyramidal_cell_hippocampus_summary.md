# Subicular pyramidal cell — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Subiculum [UBERON:0002191] | [1][2][3][4] |
| NT type | Glutamatergic | [5] |
| Defining markers | Np65 | Unsourced |
| CL term | Pyramidal neuron (CL:0000598) — BROAD mapping | — |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0096 SUB-ProS Glut_1 | — | — | 🟡 MODERATE | Glutamatergic; subicular location; high AT F1 (0.798 supertype); near-perfect target purity (1.000) | Best candidate (primary IT subicular supertype) |

1 edge total. Relationship type: TYPE_A_SPLITS.

---

## 0096 SUB-ProS Glut_1 · 🟡 MODERATE

**Supporting evidence**

- Annotation transfer (MapMyCells local, CCN20230722) of Yao 2021 (GEO:GSE185862) SSv4 hippocampal cells onto WMBv1. Yao 2021 SUB-ProS subclass cells (n=471), representing IT subicular pyramidal neurons, map primarily to three SUB-ProS supertypes: SUPT_0096 (66.5% of cells, F1=0.798), SUPT_0097 (14.6%, F1=0.253), and SUPT_0098 (18.0%, F1=0.305). Together, these three supertypes account for 99.1% of SUB-ProS cells.
- SUPT_0096 achieves near-perfect target purity (1.000) at supertype level (313/471 cells assigned), indicating that all cells assigned to SUPT_0096 originate from subicular neurons in the source dataset.
- Glutamatergic NT type is CONSISTENT between the classical node and SUPT_0096 (SUBC_023 SUB-ProS Glut).
- Location comparison: SUPT_0096 is assigned to subicular/prosubicular layers in WMBv1 MERFISH, CONSISTENT with the classical subicular pyramidal cell soma location.

**Marker evidence provenance**

- Np65 (unsourced): No reference in facts.reference_index for this marker. Np65 is the NPTN gene product (neuroplastin-65), broadly expressed in hippocampal pyramidal neurons and not subiculum-specific. Its absence from SUPT_0096 defining markers (Fn1, Rxfp1, Fyb2) does not exclude expression. Flagged as unsourced; targeted cite-traverse recommended to confirm subicular specificity. NOT_ASSESSED pending `add-expression` for Nptn on the precomputed stats.

**Concerns**

- TYPE_A_SPLITS relationship: The classical subicular pyramidal cell type encompasses the full range of IT projection neurons in the subiculum. WMBv1 resolves this into at least three IT SUB-ProS supertypes (SUPT_0096–0098). This edge targets only SUPT_0096 as the primary and most abundant supertype; SUPT_0097 and SUPT_0098 are not yet mapped, leaving the full classical type only partially covered.
- WMBv1 also contains CT SUB supertypes (SUPT_0120–0121) and NP SUB supertypes (SUPT_0127–0128), which represent corticothalamic and near-projection subpopulations. Whether these constitute distinct functional populations or additional subtypes of the classical subicular pyramidal cell (e.g. corresponding to weak-burst WB and strong-burst SB firing types) is unresolved.
- F1 scores for SUPT_0097 (0.253) and SUPT_0098 (0.305) are low, indicating these supertypes are not well-captured by the Yao 2021 SUB-ProS source cells, possibly reflecting transcriptomic divergence or source dataset underrepresentation.

**What would upgrade confidence**

- Add edges to SUPT_0097 (F1=0.253) and SUPT_0098 (F1=0.305) to complete the IT subicular pyramidal cell mapping.
- Run `add-expression` for Nptn on the precomputed stats to test whether Np65 expression distinguishes any of the three SUB-ProS supertypes.

---

## Proposed experiments

**Complete the supertype mapping**
- What: Add MappingEdge entries for SUPT_0097 and SUPT_0098 with TYPE_A_SPLITS relationship.
- Target: Cover 99.1% of SUB-ProS IT cells across three supertypes.
- Expected output: Complete mapping for the IT subicular pyramidal cell group within WMBv1.
- Resolves: AMBIGUOUS_MAPPING caveat; TYPE_A_SPLITS coverage.

**Precomputed expression query**
- What: Run `add-expression` for Nptn (Np65) on SUPT_0096–0098 and CT/NP SUB supertypes.
- Target: Detect differential Np65 expression across subicular supertypes.
- Expected output: Expression evidence establishing whether Np65 is a useful marker for distinguishing subicular supertypes.
- Resolves: marker_Np65 NOT_ASSESSED comparison; potential marker-based confidence upgrade.

**Electrophysiology-transcriptomics correlation**
- What: Patch-seq or similar approach in subicular pyramidal neurons, combined with WMBv1-level annotation.
- Target: Identify which of SUPT_0096, 0097, 0098 (IT) and SUPT_0120/0121 (CT), SUPT_0127/0128 (NP) correspond to regular-firing (RF), weak-burst (WB), and strong-burst (SB) firing types.
- Expected output: Firing-type labels added to SUB-ProS supertypes; functional resolution of the TYPE_A_SPLITS relationship.
- Resolves: Unresolved question on electrophysiological subtypes and WMBv1 supertype correspondence.

---

## Open questions

1. Which of the three electrophysiological subtypes of subicular pyramidal cells (regular-firing RF, weak-burst WB, strong-burst SB) correspond to SUPT_0096, 0097, and 0098? F1 scores for each subtype would require datasets with electrophysiologically characterised single-cell transcriptomics.
2. Does Np65 expression distinguish any of the three SUB-ProS supertypes? Running `add-expression` for Nptn on the precomputed stats would clarify.

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_subicular_pyramidal_cell_hippocampus_to_supt_0096 | ANNOTATION_TRANSFER (GSE185862, SUB-ProS cells n=471; F1=0.798 supertype, target_purity=1.000) | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2026 | [PMID:41693678](https://pubmed.ncbi.nlm.nih.gov/41693678/) | Soma location |
| [2] | Unknown 2016 | [PMID:27150503](https://pubmed.ncbi.nlm.nih.gov/27150503/) | Soma location |
| [3] | Unknown 2025 | [PMID:41509312](https://pubmed.ncbi.nlm.nih.gov/41509312/) | Soma location |
| [4] | Unknown 2013 | [PMID:24303119](https://pubmed.ncbi.nlm.nih.gov/24303119/) | Soma location |
| [5] | Dale et al. 2015 | [PMID:26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | Neurotransmitter type |
