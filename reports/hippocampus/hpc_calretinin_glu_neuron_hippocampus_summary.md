# hippocampal calretinin-positive glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

| Property | Value | References |
|---|---|---|
| CL term | glutamatergic neuron (CL:0000679) | |
| Soma location | stratum lacunosum-moleculare / outer molecular layer [UBERON:0002421] | [1][2] |
| NT | glutamatergic | |
| Defining markers | Calb2 (calretinin) | |
| Negative markers | — | |
| Neuropeptides | — | |

*Note: NT type and Calb2 marker entries carry no citations in the facts file. The soma location references establish the SLM/OML position of this population. See Marker evidence provenance for the citation gap.*

---

## 2. Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] | HPF CR Glut | — | 🔴 LOW | Calb2 CONSISTENT · Location APPROXIMATE | Speculative |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP (SUPT_0135 is the only HPF glutamatergic supertype outside DG/CA/SUB subclasses; Cajal-Retzius identity is a significant concern).

---

## 3. Candidate paragraphs

## 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] · 🔴 LOW

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0135 belongs to subclass SUBC_036 HPF CR Glut, a glutamatergic subclass in the hippocampal formation. The classical hippocampal calretinin-positive glutamatergic neuron is defined as glutamatergic, consistent with this subclass.

- **Anatomical exclusion argument — APPROXIMATE.** SUPT_0135 (0135 HPF CR Glut_1) is the only WMBv1 glutamatergic supertype in the HPF that falls outside the DG, CA1-ProS, CA2-FC-IG, CA3, and SUB-ProS subclasses. The stratum lacunosum-moleculare (SLM) and outer molecular layer (OML) position of the classical calretinin-positive glutamatergic neuron is consistent with the 'HPF CR' designation; no other HPF glutamatergic supertype lacks a specific subfield assignment. This process-of-elimination argument provides weak positive support for the mapping.

- **Calb2 expression — CONSISTENT.** Analysis of WMBv1 precomputed stats (CCN20230722, supertype level) reveals high Calb2 expression in SUPT_0135 reference cells (mean 4.5–8.2 UMIs/cell across 5 clusters; n=1 each) — 30–100× higher than in DG Glut supertypes (0.08–0.16 UMIs). This is the primary molecular positive evidence for this mapping; Calb2 expression at this level is the highest among all HPF glutamatergic supertypes.

**Marker evidence provenance**

- **Calb2 (calretinin):** No primary citation is recorded in the facts file for the Calb2 marker entry on this node. The defining marker is listed without a specific reference supporting the assertion that this population is specifically Calb2+. This represents an unsourced marker entry — a significant weakness for the mapping rationale. The quantitative precomputed stats evidence (Calb2 mean 4.5–8.2 UMIs in SUPT_0135) provides indirect support via atlas metadata, but without a primary citation establishing Calb2 expression in morphology-confirmed SLM/OML glutamatergic neurons, the specificity of this marker for this classical type is not documented in the KB. *(Recommendation: A targeted cite-traverse for "calretinin glutamatergic SLM hippocampus" or "Calb2 stratum lacunosum-moleculare neuron" should be run to identify primary citations establishing this marker. The current marker evidence is a critical gap.)*

- **NT type (glutamatergic):** The NT entry also carries no citation. *(Recommendation: A targeted cite-traverse for "glutamatergic calretinin SLM hippocampus" would identify the primary evidence for this classical node definition.)*

- **Slc17a8 (VGluT3) — marker absent from atlas.** Although the Calb2/Slc17a8 co-expression pattern is part of the classical description of SLM glutamatergic neurons in the literature (per the atlas metadata evidence explanation), Slc17a8 mean expression in SUPT_0135 is effectively absent (0–0.3 UMIs in 2/5 clusters only). This is a significant discrepancy: if the classical node specifically requires VGluT3+ expression, SUPT_0135 fails this criterion. The Slc17a8 absence is not reconciled by current evidence and represents a concern rather than a confirmed marker absence.

**Concerns**

- **Cajal-Retzius cell identity conflict.** SUPT_0135 reference cells strongly co-express Reln (12–13 UMIs/cell) and Trp73 (8.8–9.7 UMIs/cell), both canonical Cajal-Retzius cell markers. Classical Cajal-Retzius cells are developmentally transient, largely absent in the adult rodent hippocampus, and molecularly distinct from the adult Calb2+/Slc17a8+ glutamatergic population described in the SLM/OML literature. The 'CR' designation in WMBv1 may specifically capture rare Cajal-Retzius remnants present in adult hippocampus profiling rather than the functionally characterised SLM glutamatergic population. This is the primary reason for the LOW confidence rating.

- **Extremely small reference population (n=5).** SUPT_0135 has only 5 reference cells total (1 per cluster), the smallest representation of any HPF Glut supertype in WMBv1. This is consistent with either extreme rarity (Cajal-Retzius remnants are rare in adult brain) or a poorly sampled cell type. Statistical uncertainty is very high.

- **Slc17a8 (VGluT3) absent from SUPT_0135.** If VGluT3 expression is part of the classical node definition, the near-zero Slc17a8 in SUPT_0135 represents a marker DISCORDANT for a defining characteristic of the population. Whether VGluT3 expression is limited to a subset of Calb2+ SLM cells, or whether the classical node definition is overly broad, is unresolved.

- **Location APPROXIMATE.** SUPT_0135 MERFISH soma assignments have not been assessed; the SLM/OML location is inferred from the absence of DG/CA/SUB subclass membership rather than direct spatial confirmation. This is a weaker location argument than would be available from direct MERFISH inspection.

**What would upgrade confidence**

- **Targeted literature search for marker citations:** Adding a primary citation for Calb2 and NT type (glutamatergic) to this classical node — via a cite-traverse for "calretinin glutamatergic SLM hippocampus" — would establish whether the classical type definition is adequately supported. This is the most urgent gap and can be addressed without new experiments.

- **MERFISH soma location check for SUPT_0135:** Checking WMBv1 MERFISH soma assignments for SUPT_0135 cells (via the atlas browser or MERFISH distribution data) would confirm or disconfirm SLM/OML placement, resolving the location APPROXIMATE. If SUPT_0135 cells are confirmed in SLM/OML, this would upgrade the location alignment and strengthen the case for PARTIAL_OVERLAP.

- **Annotation transfer from Calb2+/Slc17a8+ SLM dataset:** Running annotation transfer from a dataset with validated Calb2+/Slc17a8+ SLM glutamatergic neurons onto WMBv1 would directly test whether these cells map to SUPT_0135 or to an alternative supertype. Target: F1 ≥ 0.70 at SUPERTYPE level. Expected output: AnnotationTransferEvidence resolving Open question 1.

- **ISH validation of Trp73/Calb2 co-expression in adult SLM:** ISH data from Allen Brain Atlas or similar resource confirming whether Trp73 and Calb2 co-express in adult mouse SLM would determine whether SUPT_0135 captures Cajal-Retzius remnants (Trp73+/Calb2+) or the adult SLM glutamatergic population (Calb2+/Trp73-).

---

## 4. Proposed experiments

### 1 — Targeted literature search (marker citations)

**What:** Cite-traverse for "calretinin glutamatergic stratum lacunosum-moleculare hippocampus" and "Calb2 SLM neuron hippocampus" to identify primary citations for the classical node marker definition.

**Target:** At least one primary study (morphology-confirmed or anatomically defined) establishing Calb2 expression in SLM/OML glutamatergic neurons.

**Expected output:** LiteratureEvidence entries added to the KB node; reference_index updated.

**Resolves:** Unsourced Calb2 and NT marker entries (critical evidence gap).

### 2 — MERFISH / spatial transcriptomics

**What:** Check WMBv1 MERFISH soma assignments for SUPT_0135 cells (via atlas browser or MERFISH cell type distribution data) to confirm SLM/OML vs. other placement.

**Target:** Majority of SUPT_0135 cells in SLM or OML spatial bins.

**Expected output:** Atlas metadata evidence (ATLAS_METADATA) clarifying location alignment from APPROXIMATE to CONSISTENT or DISCORDANT.

**Resolves:** Open question 2 (SUPT_0135 soma location); could upgrade confidence if SLM/OML placement confirmed.

### 3 — MapMyCells / Annotation transfer (Calb2+/VGluT3+ SLM cells)

**What:** Run annotation transfer from a dataset containing validated Calb2+/Slc17a8+ SLM glutamatergic neurons (if such a dataset exists) onto WMBv1 (CCN20230722).

**Target:** F1 ≥ 0.70 at SUPERTYPE level.

**Expected output:** AnnotationTransferEvidence confirming or disconfirming SUPT_0135 as the target for SLM Calb2+ glutamatergic neurons.

**Resolves:** Open question 1 (whether SUPT_0135 represents adult SLM Calb2+ glutamatergic neurons or Cajal-Retzius remnants).

---

## 5. Open questions

1. Is SUPT_0135 a Cajal-Retzius remnant population (Calb2+/Reln+/Trp73+, developmentally transient) or does it represent the adult SLM/OML Calb2+ glutamatergic neurons described in the hippocampal literature? ISH validation of Trp73 and Calb2 co-expression in adult SLM/OML, and annotation transfer from a Calb2+/VGluT3+ SLM dataset, would resolve this. This question appears on the single edge to SUPT_0135.

2. Why is Slc17a8 (VGluT3) absent from SUPT_0135 (0–0.3 UMIs) if the classical node is described as a VGluT3+ glutamatergic population? Is VGluT3 expression limited to a subset of Calb2+ SLM cells, or is the classical node definition too broad (should be restricted to Calb2+ only, without VGluT3 requirement)?

---

## 6. Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135 | ATLAS_METADATA (WMBv1 precomputed stats; exclusion argument + Calb2 expression) | SUPPORT (partial) — SUPT_0135 is only HPF Glut supertype outside DG/CA/SUB subclasses; Calb2 mean 4.5–8.2 UMIs (highest among HPF Glut); but Slc17a8 absent and Cajal-Retzius co-expression (Reln, Trp73) raises conflicting identity |

---

## 7. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wheeler et al. 2015 · PMID:26402459 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | Soma location |
| [2] | Ceranik et al. 1997 · PMID:9204922 | [9204922](https://pubmed.ncbi.nlm.nih.gov/9204922/) | Soma location |
