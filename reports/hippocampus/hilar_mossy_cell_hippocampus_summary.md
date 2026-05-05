# Hilar mossy cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus of hippocampal formation [UBERON:0001885] (polymorph layer / hilus) | [1][2] |
| NT | Glutamatergic | [3][4][5] |
| Defining markers | Gria4, Dkk3 | (no citations in KB) |
| Negative markers | — | |
| Neuropeptides | — | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0078 CA3 Glut_4 [CS20230722_SUPT_0078] | CA3 Glut | 1467 (CA3 pyramidal layer, MBA:495) | 🟡 MODERATE | AT F1=0.943 (Mossy-Cyp26b1) · NT CONSISTENT · location DISCORDANT | Best candidate — Cyp26b1+ mossy cell subtype |
| 2 | 0079 CA3 Glut_5 [CS20230722_SUPT_0079] | CA3 Glut | 181 (DG polymorph layer, MBA:10704) | 🟡 MODERATE | AT F1=0.833 (Mossy-Adcyap1) · NT CONSISTENT · location APPROXIMATE | Best candidate — Adcyap1+ mossy cell subtype |

Total: 2 edges. Relationship type: PARTIAL_OVERLAP for both edges.

---

## 0078 CA3 Glut_4 [CS20230722_SUPT_0078] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0078 belongs to subclass CS20230722_SUBC_017 (017 CA3 Glut), a glutamatergic subclass. The classical hilar mossy cell is glutamatergic [3][4][5], and SUBC_017 is exclusively glutamatergic.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Hochgerner 2018 (GEO:GSE95315) Mossy-Cyp26b1 label onto WMBv1 (CCN20230722). 33 of 34 Mossy-Cyp26b1 cells map to SUPT_0078 (0078 CA3 Glut_4) at the supertype level (F1=0.943; group_purity=0.971, target_purity=0.917). At cluster level, the best cluster is 0315 CA3 Glut_4 (n=20, F1=0.833) followed by 0314 CA3 Glut_4 (n=7). The high F1 indicates that Mossy-Cyp26b1 cells are a near-complete subset of SUPT_0078.

- **Marker Gria4 — CONSISTENT.** Gria4 is listed as a defining marker of the hilar mossy cell (no citation in KB). Precomputed expression stats (precomputed_stats.h5, supertype level) confirm Gria4 mean expression = 5.37 in SUPT_0078, consistent with Gria4 marking this supertype.

- **Marker Dkk3 — CONSISTENT.** Dkk3 is listed as a defining marker of the hilar mossy cell (no citation in KB). Precomputed expression stats confirm Dkk3 mean expression = 8.71 in SUPT_0078, consistent with Dkk3 marking this supertype.

**Marker evidence provenance**

- **Gria4** (no KB citation): Evidence basis is absent from the classical node — no reference is cited for Gria4 as a hilar mossy cell marker. This is a gap that requires a primary citation. *(Recommendation: Targeted cite-traverse for "Gria4 GluA4 mossy cell dentate gyrus hippocampus" is needed to identify the primary source and assess whether this is protein-level or transcript-level evidence.)*

- **Dkk3** (no KB citation): Evidence basis is absent from the classical node — no reference is cited for Dkk3 as a hilar mossy cell marker. This is a gap that requires a primary citation. *(Recommendation: Targeted cite-traverse for "Dkk3 mossy cell hippocampus" is needed to identify the primary source and confirm cell-type specificity.)*

**Concerns**

- **Location — DISCORDANT.** SUPT_0078 MERFISH soma assignments are entirely within CA3 strata: pyramidal layer (MBA:495; 1467 cells), stratum oriens (MBA:486; 1381 cells), stratum radiatum (MBA:504; 945 cells), stratum lucidum (MBA:479; 868 cells), and stratum lacunosum-moleculare (MBA:471; 437 cells). No cells are listed in the dentate gyrus polymorph layer (MBA:10704) or granule cell layer (MBA:632). Classical hilar mossy cells have soma in the hilus/polymorph layer. The CA3 location vs. hilar soma is anatomically discordant: *(note: the dentate hilus is immediately adjacent to CA3c and cells at this border are frequently co-registered to CA3 strata in MERFISH data; the discordance may reflect registration boundary effects at the CA3c/hilus border rather than a true anatomical mismatch; this is weak-to-moderate counter-evidence given the border anatomy.)*

- **PARTIAL_OVERLAP.** The high AT F1 (0.943) suggests Mossy-Cyp26b1 cells are transcriptomically equivalent to SUPT_0078, but SUPT_0078 may also include CA3c pyramidal cells sharing the Cyp26b1 transcriptomic profile. The PARTIAL_OVERLAP relationship reflects uncertainty about whether SUPT_0078 represents hilar mossy cells specifically or a broader population.

- **Missing citations for markers.** Gria4 and Dkk3 are listed as defining markers on the classical node without KB citations. The marker evidence provenance cannot be fully assessed without primary references.

**What would upgrade confidence**

- **smFISH / MERFISH spatial validation** (LiteratureEvidence): validate SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus to test whether soma positions span the CA3c/hilus boundary. If Homer3+ or Cldn22+ cells are confirmed in the hilus, this would upgrade to MODERATE-HIGH. Expected output: spatial anatomy evidence entry. Resolves open question 1.

- **Targeted cite-traverse for Gria4 and Dkk3** (LiteratureEvidence): identify primary references for both markers and assess cell-type specificity and evidence level (protein vs. transcript). Resolves marker provenance gap.

---

## 0079 CA3 Glut_5 [CS20230722_SUPT_0079] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0079 belongs to subclass CS20230722_SUBC_017 (017 CA3 Glut), a glutamatergic subclass. The classical hilar mossy cell is glutamatergic [3][4][5].

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Hochgerner 2018 (GEO:GSE95315) Mossy-Adcyap1 label onto WMBv1 (CCN20230722). 20 of 27 Mossy-Adcyap1 cells map to SUPT_0079 (0079 CA3 Glut_5) at the supertype level (F1=0.833; group_purity=0.741, target_purity=0.952). The high target_purity (0.952) indicates that Mossy-Adcyap1 cells account for the majority of SUPT_0079 cells captured by AT — suggesting this supertype may be specific to the Adcyap1+ mossy cell subtype.

- **Soma location — APPROXIMATE (supporting).** SUPT_0079 is the only WMBv1 CA3 Glut supertype with cells assigned to the dentate gyrus polymorph layer (MBA:10704; 181 cells), which is the hilus — the classical mossy cell soma location [UBERON:0001885]. This is a positive anatomical correspondence distinguishing SUPT_0079 from other CA3 Glut supertypes.

- **Marker Gria4 — CONSISTENT.** Precomputed expression stats confirm Gria4 mean expression = 8.05 in SUPT_0079, consistent with Gria4 marking hilar mossy cells.

- **Marker Dkk3 — CONSISTENT.** Precomputed expression stats confirm Dkk3 mean expression = 5.32 in SUPT_0079, consistent with Dkk3 marking hilar mossy cells.

**Marker evidence provenance**

- **Gria4** and **Dkk3**: Same provenance gaps apply as described for the SUPT_0078 edge above. Both markers lack primary KB citations on the classical node. *(Recommendation: Targeted cite-traverse for both markers is needed before these can provide strong positive evidence.)*

**Concerns**

- **Location — APPROXIMATE.** The majority of SUPT_0079 cells are in CA3 strata: Field CA3, pyramidal layer (MBA:495; 294 cells), stratum oriens (MBA:486; 121 cells), stratum lucidum (MBA:479; 175 cells), and stratum radiatum (MBA:504; 261 cells). Although 181 hilar cells are present, these are outnumbered by CA3 strata cells. The CA3 majority may reflect CA3c pyramidal cells sharing the Adcyap1+ transcriptomic signature, or MERFISH registration of hilus cells into adjacent CA3c. *(note: CA3c is immediately adjacent to the dentate hilus; the partial hilar representation and substantial CA3c representation are consistent with MERFISH registration spread at the CA3c/hilus boundary, which is weak counter-evidence.)*

- **PARTIAL_OVERLAP.** SUPT_0079 carries both hilar and CA3 cells; the Adcyap1+ mossy cell population is a subset of this broader supertype.

- **Three Hochgerner mossy cell subtypes — two resolved.** Hochgerner 2018 identifies three molecular subtypes of hilar mossy cells: Mossy-Cyp26b1, Mossy-Adcyap1, and Mossy-Klk8. The Mossy-Klk8 subtype (n=6 cells) maps ambiguously across multiple CA3 supertypes (best: SUPT_0077, F1=0.308) — insufficient evidence to build a separate edge. Together, SUPT_0078 and SUPT_0079 represent two of three molecular subtypes of the classical hilar mossy cell.

**What would upgrade confidence**

- **ISH co-labelling of Cyp26b1 and Adcyap1** (LiteratureEvidence): validate non-overlapping expression in dentate hilus to confirm the two-supertype mossy cell split. Expected output: LiteratureEvidence entries. Resolves open question 2.

- **Annotation transfer from a full mouse mossy cell dataset** (AnnotationTransferEvidence): run AT from a Hochgerner 2018 mouse replication to confirm species-generality of the SUPT_0078/0079 mossy cell split. Hochgerner 2018 is a rat dataset; cross-species confirmation needed. Expected output: AnnotationTransferEvidence entries for both edges.

---

## Proposed experiments

### smFISH / MERFISH spatial validation (SUPT_0078 hilus boundary)

- **What:** smFISH or MERFISH spot validation of SUPT_0078 defining markers (Homer3, Cldn22) in dentate hilus tissue sections.
- **Target:** Confirm Homer3+ or Cldn22+ cells in the hilus / CA3c border region.
- **Expected output:** Spatial anatomy evidence entry; LiteratureEvidence supporting or refuting DISCORDANT location alignment on edge_hilar_mossy_cell_hippocampus_to_supt_0078.
- **Resolves:** Open question 1 (are SUPT_0078 cells at the CA3c/hilar boundary?).

### ISH co-labelling (Cyp26b1 and Adcyap1)

- **What:** ISH or smFISH co-labelling of Cyp26b1 and Adcyap1 in dentate hilus.
- **Target:** Confirm non-overlapping expression; validate two-supertype molecular subdivision.
- **Expected output:** LiteratureEvidence entries on both edges.
- **Resolves:** Open question 2 (functional/anatomical distinction between Cyp26b1+ and Adcyap1+ subtypes).

### Annotation transfer (mouse mossy cell dataset)

- **What:** Run MapMyCells annotation transfer from a mouse hippocampus dataset with explicitly labelled mossy cells onto WMBv1 (CCN20230722).
- **Target:** F1 ≥ 0.80 at SUPERTYPE level for SUPT_0078 and/or SUPT_0079.
- **Expected output:** AnnotationTransferEvidence entries for both mossy cell edges; cross-species validation.
- **Resolves:** Cross-species uncertainty (Hochgerner 2018 is rat); open question 2.

---

## Open questions

1. Are SUPT_0078 cells that map to CA3 pyramidal layer actually at the CA3c/hilar boundary? High-resolution FISH of Homer3 or Cldn22 (SUPT_0078 defining markers) in hilus/CA3c would resolve this.

2. What is the functional and anatomical distinction between the SUPT_0078 (Cyp26b1+) and SUPT_0079 (Adcyap1+) mossy cell subtypes? Do they correspond to dorsal vs. ventral mossy cells, or to distinct projection patterns (IML-only vs. IML+MML in dorsal mossy cells)?

---

## Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_hilar_mossy_cell_hippocampus_to_supt_0078 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE95315; Mossy-Cyp26b1) | SUPPORT — F1=0.943; group_purity=0.971, target_purity=0.917; 33/34 Mossy-Cyp26b1 cells map to SUPT_0078 |
| edge_hilar_mossy_cell_hippocampus_to_supt_0079 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE95315; Mossy-Adcyap1) | SUPPORT — F1=0.833; group_purity=0.741, target_purity=0.952; 20/27 Mossy-Adcyap1 cells map to SUPT_0079 |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Botterill et al. 2021 · PMID:33600026 | [33600026](https://pubmed.ncbi.nlm.nih.gov/33600026/) | Soma location |
| [2] | Fredes & Shigemoto 2021 · PMID:34214666 | [34214666](https://pubmed.ncbi.nlm.nih.gov/34214666/) | Soma location |
| [3] | Sun et al. 2017 · PMID:28451637 | [28451637](https://pubmed.ncbi.nlm.nih.gov/28451637/) | Neurotransmitter type |
| [4] | Scharfman & Myers 2013 · PMID:23420672 | [23420672](https://pubmed.ncbi.nlm.nih.gov/23420672/) | Neurotransmitter type |
| [5] | Scharfman & Bernstein 2015 · PMID:26347618 | [26347618](https://pubmed.ncbi.nlm.nih.gov/26347618/) | Neurotransmitter type |
