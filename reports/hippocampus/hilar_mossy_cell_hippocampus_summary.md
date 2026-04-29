# Hilar mossy cell — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus polymorph layer (hilus) [UBERON:0001885] | [1][2] |
| NT type | Glutamatergic | [3][4][5] |
| Defining markers | Gria4, Dkk3 | Both unsourced |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0078 CA3 Glut_4 | — | — | 🟡 MODERATE | Glutamatergic; near-complete AT overlap (F1=0.943 supertype); maps Mossy-Cyp26b1 subtype | Best candidate (Cyp26b1+ subtype) |
| 2 | 0079 CA3 Glut_5 | — | — | 🟡 MODERATE | Glutamatergic; 181 cells in hilus (MBA:10704); maps Mossy-Adcyap1 subtype | Best candidate (Adcyap1+ subtype) |

2 edges total. Relationship type: PARTIAL_OVERLAP (both).

---

## 0078 CA3 Glut_4 · 🟡 MODERATE

**Supporting evidence**

- Annotation transfer (MapMyCells local, CCN20230722) of Hochgerner 2018 (GEO:GSE95315) Mossy-Cyp26b1 label maps 33 of 34 cells to SUPT_0078 at supertype level (F1=0.943; group_purity=0.971, target_purity=0.917). The high target_purity indicates that Mossy-Cyp26b1 cells account for the near-entirety of the SUPT_0078 cells captured by annotation transfer.
- At cluster level, the best cluster is 0315 CA3 Glut_4 (n=20, F1=0.833) followed by 0314 CA3 Glut_4 (n=7), indicating tight transcriptomic correspondence within SUPT_0078.
- At subclass level, all 35 Mossy-Cyp26b1 cells map to 017 CA3 Glut (group_purity=1.000, F1=0.686), confirming glutamatergic subclass assignment.
- Glutamatergic NT type is CONSISTENT between the classical node and SUPT_0078 (SUBC_017 CA3 Glut).

**Marker evidence provenance**

- Gria4 (unsourced): No reference in facts.reference_index. Flagged as unsourced; targeted cite-traverse recommended to establish evidentiary basis. Gria4 is not listed among SUPT_0078 defining markers (Homer3, Cldn22); NOT_ASSESSED pending `add-expression`.
- Dkk3 (unsourced): No reference in facts.reference_index. Flagged as unsourced; targeted cite-traverse recommended. Dkk3 not listed in SUPT_0078 defining markers; NOT_ASSESSED pending `add-expression`.

**Concerns**

- DISCORDANT anatomy: SUPT_0078 MERFISH soma assignments are entirely within CA3 strata (pyramidal layer: 1,467 cells; stratum oriens: 1,381; stratum radiatum: 945; stratum lucidum: 868; stratum lacunosum-moleculare: 437). No cells are listed in the dentate gyrus polymorph layer (MBA:10704) or granule cell layer. Classical hilar mossy cells have soma in the hilus/polymorph layer. The high AT F1 (0.943) suggests Mossy-Cyp26b1 cells are transcriptomically equivalent to SUPT_0078 despite this anatomical discordance. Hilar mossy cells at the CA3c border may fall within MERFISH CA3 registration, or the Cyp26b1+ mossy cell subtype may have a distinct anatomical distribution compared to the broader mossy cell population *(note: this interpretation requires independent anatomical validation)*.
- The Hochgerner 2018 dataset uses rat tissue; the WMBv1 atlas is mouse. Species-level transcriptomic differences in mossy cell subtypes are unquantified.
- The PARTIAL_OVERLAP relationship reflects that SUPT_0078 may include CA3 pyramidal cells sharing the Cyp26b1 transcriptomic profile in addition to mossy cells.

**What would upgrade confidence**

- smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus and CA3c to test whether soma positions span the CA3c/hilus boundary.

---

## 0079 CA3 Glut_5 · 🟡 MODERATE

**Supporting evidence**

- Annotation transfer (MapMyCells local, CCN20230722) of Hochgerner 2018 (GEO:GSE95315) Mossy-Adcyap1 label maps 20 of 27 cells to SUPT_0079 at supertype level (F1=0.833; group_purity=0.741, target_purity=0.952). The high target_purity (0.952) indicates Mossy-Adcyap1 cells account for the majority of SUPT_0079 cells captured by annotation transfer.
- SUPT_0079 is the only WMBv1 CA3 Glut supertype with cells assigned to the dentate gyrus polymorph layer (181 cells, MBA:10704), which is the classical mossy cell soma location. This constitutes a positive anatomical correspondence.
- At subclass level, 27 Mossy-Adcyap1 cells map to 017 CA3 Glut (group_purity=0.931, F1=0.562), confirming glutamatergic subclass assignment.
- Glutamatergic NT type is CONSISTENT between the classical node and SUPT_0079 (SUBC_017 CA3 Glut).

**Marker evidence provenance**

- Gria4 (unsourced): No reference in facts.reference_index. Flagged as unsourced; targeted cite-traverse recommended. Gria4 not listed in SUPT_0079 defining markers (Rcn3, Csf2rb2); NOT_ASSESSED pending `add-expression`.
- Dkk3 (unsourced): No reference in facts.reference_index. Flagged as unsourced; targeted cite-traverse recommended. Dkk3 not listed in SUPT_0079 defining markers; NOT_ASSESSED pending `add-expression`.

**Concerns**

- APPROXIMATE anatomy: Although SUPT_0079 has 181 cells in the hilus (MBA:10704), the majority of cells are in CA3 strata (pyramidal layer: 294; stratum radiatum: 261; stratum lucidum: 175; stratum oriens: 121; granule cell layer: 147). This distribution may reflect CA3c pyramidal cells sharing the Adcyap1+ transcriptomic signature, or MERFISH registration of hilus cells into adjacent CA3c.
- Hochgerner 2018 Mossy-Klk8 (n=6 cells) maps ambiguously across multiple CA3 supertypes (best: SUPT_0077, F1=0.308) and could not be used to build a separate edge, leaving this third mossy cell molecular subtype unresolved.
- The Hochgerner 2018 dataset uses rat tissue; species-level differences are unquantified.

**What would upgrade confidence**

- ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus to confirm non-overlapping expression and validate the two-supertype mossy cell split.
- Annotation transfer from a mouse mossy cell dataset to confirm species-generality of the SUPT_0078/0079 mossy cell split.

---

## Proposed experiments

**smFISH/MERFISH anatomy validation**
- What: smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) and SUPT_0079 defining markers (Rcn3, Csf2rb2) in dentate hilus and CA3c.
- Target: Detect soma positions in the dentate gyrus polymorph layer (hilus).
- Expected output: MERFISH-compatible anatomical data confirming hilar vs. CA3 soma distribution for each supertype.
- Resolves: DISCORDANT_ANATOMY caveat for SUPT_0078; clarifies relative anatomical positions of both mossy cell supertypes.

**ISH co-labelling**
- What: ISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus.
- Target: Non-overlapping expression in distinct mossy cell populations; hilar enrichment for both markers.
- Expected output: Evidence for two molecularly distinct mossy cell subtypes in the hilus.
- Resolves: AMBIGUOUS_MAPPING caveat; functional/anatomical distinction between SUPT_0078 and SUPT_0079.

**Cross-species annotation transfer**
- What: Annotation transfer from a mouse mossy cell dataset to WMBv1.
- Target: F1 >= 0.80 at supertype level for SUPT_0078 and/or SUPT_0079.
- Expected output: AnnotationTransferEvidence in the same species as WMBv1, removing the rat-to-mouse extrapolation caveat.
- Resolves: Species extrapolation concern; confidence upgrade if F1 threshold is met.

---

## Open questions

1. Are SUPT_0078 cells that map to CA3 pyramidal layer actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 (SUPT_0078 defining markers) in hilus/CA3c would resolve this.
2. What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_hilar_mossy_cell_hippocampus_to_supt_0078 | ANNOTATION_TRANSFER (GSE95315, Mossy-Cyp26b1; F1=0.943 supertype, 0.686 subclass) | SUPPORT |
| edge_hilar_mossy_cell_hippocampus_to_supt_0079 | ANNOTATION_TRANSFER (GSE95315, Mossy-Adcyap1; F1=0.833 supertype, 0.562 subclass) | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Botterill et al. 2021 | [PMID:33600026](https://pubmed.ncbi.nlm.nih.gov/33600026/) | Soma location |
| [2] | Fredes & Shigemoto 2021 | [PMID:34214666](https://pubmed.ncbi.nlm.nih.gov/34214666/) | Soma location |
| [3] | Sun et al. 2017 | [PMID:28451637](https://pubmed.ncbi.nlm.nih.gov/28451637/) | Neurotransmitter type |
| [4] | Scharfman & Myers 2013 | [PMID:23420672](https://pubmed.ncbi.nlm.nih.gov/23420672/) | Neurotransmitter type |
| [5] | Scharfman & Bernstein 2015 | [PMID:26347618](https://pubmed.ncbi.nlm.nih.gov/26347618/) | Neurotransmitter type |
