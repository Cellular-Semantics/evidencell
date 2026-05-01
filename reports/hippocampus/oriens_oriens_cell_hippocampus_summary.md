# Oriens-oriens (O-O) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Stratum oriens of hippocampus [UBERON:0014548] (CA1) | — |
| Neurotransmitter | GABAergic | — |
| Defining markers | Sst, Nos1 | [1], — |
| Negative markers | — | — |
| Neuropeptides | — | — |

**Notes on definition:** The O-O cell is a GABAergic interneuron defined by soma and axon confinement to stratum oriens. Its molecular identity rests on co-expression of Sst and Nos1, characterised via intersectional Sst;;Nos1 Cre/Flp genetics by Chamberland et al. 2024 [1]; 12 of 15 cells matching this intersectional label were consistent with the O-O morphological description. The O-O cell is distinguished from OLM cells by axon confinement: OLM axons project to stratum lacunosum-moleculare, whereas O-O axons remain in stratum oriens.

*(note: The original description of O-O cells by Blasco-Ibáñez & Freund (1995) defined this interneuron type by axonal topology alone in CA1. The molecular handles Sst and Nos1 are consistent with that description and were used by Chamberland et al. to isolate and electrophysiologically characterise them. Evidence for this as a discrete classical type remains thin — a single study with n = 12–15 cells.)*

---

## Mapping candidates

| Rank | WMBv1 supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | ⚪ UNCERTAIN | Sst CONSISTENT; Nos1 APPROXIMATE; location APPROXIMATE (CA3 vs CA1) | Eliminated — plausible but unconfirmed |

**Total edges: 1.** Relationship type: UNCERTAIN. No MODERATE or LOW candidates were established for this node.

---

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] · ⚪ UNCERTAIN

**Supporting evidence**

- Sst expression is strongly consistent: precomputed stats mean = 10.17 for 0219 Sst Gaba_6 [CS20230722_SUPT_0219], matching the Sst-positive identity of O-O cells [1].
- 0219 Sst Gaba_6 [CS20230722_SUPT_0219] falls within the 053 Sst Gaba subclass, which is consistent with the GABAergic / Sst interneuron classification of O-O cells.
- Annotation transfer (MapMyCells; Yao 2021 Sst SSv4, GEO:GSE185862, n = 273 HIP cells) maps the Sst subclass to WMBv1 with high fidelity at subclass level (F1 = 0.983, group purity = 0.989, target purity = 0.978, n = 265 cells mapped to 053 Sst Gaba subclass).
- At supertype level, 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is the dominant annotation transfer target within this subclass (F1 = 0.759, 161/273 cells, target purity = 0.964), indicating that it captures the largest fraction of hippocampal Sst interneurons in the Yao 2021 dataset.
- NT type is CONSISTENT: 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is GABA-type, matching the GABAergic classification of O-O cells.

**Marker evidence provenance**

- **Sst:** Defined as a co-expressing marker by Chamberland et al. 2024 [1] using intersectional Sst-Cre genetics. Atlas precomputed stats (mean = 10.17 for 0219 Sst Gaba_6 [CS20230722_SUPT_0219]) confirm robust Sst expression at supertype resolution. This is the strongest molecular anchor for the proposed correspondence.
- **Nos1:** Critically, Nos1 is the second arm of the Sst;;Nos1 intersectional label used to isolate O-O cells [1], and it is the key feature that distinguishes them from OLM and other Sst+ interneuron types in CA1. However, 0219 Sst Gaba_6 [CS20230722_SUPT_0219] does not list Nos1 among its defining markers in the atlas, and precomputed stats show a low mean = 1.81 — consistent with low but non-zero expression. Whether this reflects genuine absence, heterogeneous expression within the supertype, or sub-threshold detection at supertype resolution is unknown.
- **Id3, Adamtsl1, Sp9:** These are atlas-defined markers of 0219 Sst Gaba_6 [CS20230722_SUPT_0219] that have no correspondence established in the O-O classical literature — their status relative to O-O cells is NOT_ASSESSED.
- **Annotation transfer caveat:** The annotation transfer source (Yao 2021 SSv4 Sst subclass) is a subclass-level label encompassing multiple Sst interneuron types — OLM, bistratified, hippocampo-septal, oriens-oriens, and others. Supertype-level resolution from this label cannot distinguish O-O cells from co-resident Sst+ types. Subtype resolution would require a dataset with morphologically identified Sst interneuron labels.

**Concerns**

- **Subregional mismatch:** O-O cells were characterised in CA1 stratum oriens [UBERON:0014548] by Chamberland et al. 2024 [1]. In contrast, 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is CA3-enriched: its top location is Field CA3, stratum oriens (305 cells), with no explicit CA1 SO entry prominent in the top cell distribution. This is an APPROXIMATE alignment and represents a meaningful subregional discrepancy.
- **Nos1 not confirmed at atlas level:** The low Nos1 mean (1.81) in 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is concerning given that Sst+/Nos1+ co-expression is the defining intersectional signature used to isolate O-O cells [1]. Its absence from the atlas marker list does not definitively exclude expression, but it raises the question of whether a different supertype or cluster with higher Nos1 may be a better candidate.
- **Single-study evidence base:** The O-O cell as a classically distinct interneuron type is currently supported by one study [1] with a small cell sample (n = 12–15). The robustness of the Sst+/Nos1+ O-O definition and its distinctness from other CA1 Sst+ interneurons awaits independent replication.
- **Supertype resolution insufficient:** The 053 Sst Gaba subclass contains multiple supertypes. Without Nos1 verification at atlas level, it is unclear which supertype within this subclass — if any — specifically captures the O-O cell population.

**What would upgrade confidence**

- Demonstration of Nos1 expression in 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at cluster level (e.g., cluster-level precomputed stats or scRNA-seq re-analysis of a Sst;;Nos1 intersectional dataset mapped to WMBv1) would be required to move to LOW confidence.
- Identification of a CA1 stratum oriens-enriched Sst+/Nos1+ supertype or cluster within the Sst Gaba subclass could shift the primary mapping candidate and raise confidence to LOW or MODERATE.
- An independent replication of the O-O cell morphological and molecular phenotype — ideally from a publicly available single-cell dataset with morphologically identified neurons — would strengthen the classical-side evidence sufficiently to attempt a more definitive mapping.

---

## Proposed experiments

**Intersectional genetics + transcriptomics**

- Generate scRNA-seq or snRNA-seq from Sst-Cre;;Nos1-Flp intersectional mouse hippocampus (CA1 enriched). Map resulting cells to WMBv1 using MapMyCells to identify the supertype(s) capturing the O-O population directly.
- Alternatively, re-analyse existing CA1 Sst interneuron scRNA-seq datasets with morphological labels to identify Nos1 co-expressing subclusters.

**Multiplex fluorescence in situ hybridisation**

- Use multiplex FISH (e.g. HiPlex RNAscope) to co-stain CA1 and CA3 stratum oriens for Sst + Nos1 + Id3 + Sp9. This would simultaneously test whether Nos1-co-expressing cells exist in clusters of the 0219 Sst Gaba_6 [CS20230722_SUPT_0219] supertype and resolve the CA1 vs CA3 enrichment discrepancy.

**Atlas cluster re-analysis**

- Inspect individual cluster-level (not supertype-level) Nos1 expression within the 053 Sst Gaba subclass. Identify any cluster with high Nos1 mean expression and hippocampal CA1 SO enrichment as a candidate replacement for 0219 Sst Gaba_6 [CS20230722_SUPT_0219] as the primary O-O cell mapping target.

---

## Open questions

1. Does 0219 Sst Gaba_6 [CS20230722_SUPT_0219] express Nos1 at meaningful penetrance? If so, is this confined to a specific cluster within the supertype?
2. Are the CA3 stratum oriens cells in 0219 Sst Gaba_6 [CS20230722_SUPT_0219] analogous to the CA1 O-O cells described by Chamberland et al. 2024 [1], or does the CA3 enrichment reflect a functionally distinct population?
3. Is there a CA1 stratum oriens-enriched Sst+/Nos1+ supertype in WMBv1 that better matches O-O cell identity than 0219 Sst Gaba_6 [CS20230722_SUPT_0219]?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_oriens_oriens_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA (×2), ANNOTATION_TRANSFER | PARTIAL (all items) |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker; intersectional Sst;;Nos1 O-O cell identification |
