# hippocampal calretinin-positive glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type definition

| Property | Value | References |
|---|---|---|
| Soma location | Hippocampal formation [UBERON:0002421] (*stratum lacunosum-moleculare / outer molecular layer*) | [1][2] |
| Neurotransmitter | Glutamatergic | — |
| Defining markers | *Calb2* (calretinin), *Slc17a8* (VGluT3) | — |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | glutamatergic neuron [CL:0000679] (BROAD) | — |

*(note: the NT type reference and defining marker references are absent from the classical node; see Concerns below)*

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0135 | 0135 HPF CR Glut_1 | n=5 reference cells (atlas) | 🔴 LOW | NT consistent; *Calb2* high in atlas (CONSISTENT); location approximate; *Slc17a8* absent (DISCORDANT) | Speculative |

**Total edges: 1 · Relationship type: PARTIAL_OVERLAP.** *(note: SUPT_0135 is the only WMBv1 glutamatergic HPF supertype outside DG/CA/SUB subclasses; its 'CR' designation and co-expression of Cajal-Retzius markers Reln and Trp73 introduce significant identity ambiguity)*

---

## 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] · 🔴 LOW

### Supporting evidence

**Atlas metadata.** SUPT_0135 [CS20230722_SUPT_0135] (0135 HPF CR Glut_1) is the only WMBv1 glutamatergic supertype located in the stratum lacunosum-moleculare / outer molecular layer of the HPF, matching the anatomical location of the classical node. Analysis of the WMBv1 precomputed stats (CCN20230722) reveals high *Calb2* expression in SUPT_0135 reference cells (mean 4.5–8.2 UMIs/cell across 5 clusters; n=1 each), compared to near-absent *Calb2* in DG Glut supertypes (0.08–0.16 UMIs) — a 30–100x enrichment. SUPT_0135 is the only HPF Glut supertype not assigned to DG, CA1-ProS, CA2-FC-IG, CA3, or SUB-ProS subclasses. Neurotransmitter type is consistent: SUPT_0135 belongs to subclass SUBC_036 (HPF CR Glut), confirming glutamatergic identity.

SUPT_0135 reference cells also co-express high *Reln* (mean 12–13 UMIs/cell) and *Trp73* (mean 8.8–9.7 UMIs/cell). Both *Reln* and *Trp73* are markers of Cajal-Retzius (CR) cells, placing these reference cells in the SLM/OML consistent with the classical node soma location.

Confidence is LOW due to: (1) *Slc17a8* (VGluT3), a defining marker of the classical node, is essentially absent from SUPT_0135 (0–0.3 UMIs; detectable in 2/5 clusters only — DISCORDANT); (2) the reference population is extremely small (n=5 cells total across 5 clusters), limiting statistical confidence; (3) the WMBv1 'HPF CR' designation may specifically capture developmentally transient Cajal-Retzius cells rather than the adult Calb2+/Slc17a8+ glutamatergic population described in the hippocampal literature.

### Marker evidence provenance

- ***Calb2* (calretinin)** — defining marker of the classical node. High expression confirmed in SUPT_0135 reference cells (mean 4.5–8.2 UMIs/cell, n=5 clusters), 30–100x higher than in DG Glut supertypes. This is the primary positive evidence for this mapping. However, no source references for *Calb2* as a defining marker are recorded in the classical node reference_index — **recommend cite-traverse on calretinin and hippocampal SLM glutamatergic neurons to identify peer-reviewed primary sources**.
- ***Slc17a8* (VGluT3)** — defining marker of the classical node. LOW/absent in SUPT_0135 reference cells (0–0.3 UMIs; detectable in only 2/5 clusters). This is a DISCORDANT comparison and the primary reason for LOW confidence. The WMBv1 HPF CR population may be a Calb2+/Reln+/Trp73+ Cajal-Retzius population rather than the Calb2+/Slc17a8+ SLM glutamatergic neurons described in some hippocampal transcriptomic literature. No source references for *Slc17a8* are recorded in the classical node reference_index — **recommend cite-traverse on VGluT3 and hippocampal calretinin-positive neurons to identify peer-reviewed primary sources**.
- ***Reln* and *Trp73*** — co-expressed in SUPT_0135 reference cells at high levels. These are Cajal-Retzius cell markers and are not part of the classical node definition. Their presence introduces identity ambiguity (see Concerns below).
- **NT type references** are absent from the classical node. The glutamatergic classification is implied by the node definition and atlas supertype assignment (HPF CR Glut) but is unsourced — **recommend adding a primary reference for the glutamatergic NT type**.

### Concerns

- **Ambiguous mapping — Cajal-Retzius identity:** SUPT_0135 reference cells strongly express *Reln* and *Trp73* (both established Cajal-Retzius cell markers) alongside *Calb2*. Classical Cajal-Retzius cells are developmentally transient (largely absent in adult rodent hippocampus) and may not correspond to the Calb2+/Slc17a8+ glutamatergic neurons described in adult SLM/OML. The 'CR' designation in WMBv1 may specifically label Cajal-Retzius remnants captured during adult brain profiling rather than a stable adult population.
- **Extremely small reference population:** SUPT_0135 has n=5 reference cells total (1 per cluster), the smallest representation of any HPF Glut supertype in WMBv1. This is consistent with either extreme rarity or a poorly sampled cell type, and precludes reliable marker enrichment statistics.
- ***Slc17a8* absent — DISCORDANT:** The second defining marker of the classical node (VGluT3/Slc17a8) is essentially absent from SUPT_0135. This is not easily reconciled with the classical type definition and is the key vulnerability of this mapping.

### What would upgrade confidence

- Run annotation transfer from a dataset with validated Calb2+/Slc17a8+ SLM cells onto WMBv1 to confirm whether these cells map to SUPT_0135 or to other supertypes.
- Check MERFISH soma locations for SUPT_0135 cells in WMBv1 (via atlas browser or MERFISH cell type distribution data) to confirm SLM/OML placement.
- Add primary literature references for *Calb2* and *Slc17a8* as defining markers of the classical node, including specification of whether *Slc17a8* expression is limited to a subset of Calb2+ SLM cells or is a universal marker.
- Perform ISH validation of *Trp73* and *Calb2* co-expression in adult SLM/OML to determine whether SUPT_0135 represents developmentally persistent Cajal-Retzius cells or an adult SLM population.

---

## Eliminated candidates

No edges have been eliminated as UNCERTAIN. There are no other WMBv1 HPF Glut supertypes outside the DG/CA/SUB subclasses. If SUPT_0135 does not correspond to the classical node, the cell type may be unmapped in WMBv1 or sub-threshold for supertype-level resolution given its likely rarity.

---

## Proposed experiments

### Annotation transfer from Calb2+/Slc17a8+ SLM dataset

| Attribute | Detail |
|---|---|
| **What** | Run annotation transfer from a dataset with validated Calb2+/Slc17a8+ SLM cells onto WMBv1 (CCN20230722) via MapMyCells |
| **Target** | Primary mapping to SUPT_0135 [CS20230722_SUPT_0135] with group_purity ≥ 0.5 |
| **Expected output** | AnnotationTransferEvidence entry for edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135 |
| **Resolves** | Key ambiguity: whether SUPT_0135 captures Calb2+/Slc17a8+ SLM glutamatergic neurons or exclusively Cajal-Retzius cells |

### MERFISH soma location check — SUPT_0135

| Attribute | Detail |
|---|---|
| **What** | Check MERFISH soma locations for SUPT_0135 cells in WMBv1 via atlas browser or MERFISH cell-type distribution data |
| **Target** | Majority of SUPT_0135 cells assigned to SLM (stratum lacunosum-moleculare) or OML (outer molecular layer) in the MERFISH atlas |
| **Expected output** | Location evidence entry confirming or refuting SLM/OML soma assignment |
| **Resolves** | APPROXIMATE location comparison; location alignment UBERON:0002421 vs. SLM/OML for SUPT_0135 |

### ISH validation — adult SLM Cajal-Retzius vs. SLM glutamatergic neurons

| Attribute | Detail |
|---|---|
| **What** | ISH or IHC validation of *Trp73* and *Calb2* co-expression in adult mouse SLM/OML; separate *Slc17a8* (VGluT3) expression in the same region |
| **Target** | Determine whether *Trp73*+/*Calb2*+ and *Slc17a8*+/*Calb2*+ are overlapping or non-overlapping populations in adult SLM/OML |
| **Expected output** | Characterisation of SUPT_0135 as adult Cajal-Retzius remnant or adult SLM glutamatergic population |
| **Resolves** | Core identity question for this classical node and SUPT_0135 correspondence |

---

## Open questions

1. Is SUPT_0135 a Cajal-Retzius remnant population or does it represent the adult SLM/OML Calb2+/Slc17a8+ glutamatergic neurons described in the literature? ISH validation of *Trp73* and *Calb2* co-expression in adult SLM/OML would resolve this.
2. Why is *Slc17a8* (VGluT3) absent from SUPT_0135 given that SLM glutamatergic neurons are described as VGluT3+? Is VGluT3 expression limited to a subset of Calb2+ SLM cells, or is the classical node definition too broad?

---

## Evidence base

| Edge ID | Evidence type | Details | Supports |
|---|---|---|---|
| edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135 | ATLAS_METADATA | SUPT_0135 [CS20230722_SUPT_0135] in subclass SUBC_036 HPF CR Glut; n=5 reference cells; *Calb2* mean 4.5–8.2 UMIs (30–100x DG enrichment); *Slc17a8* absent (0–0.3 UMIs); *Reln* and *Trp73* highly expressed (CR markers) | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wheeler et al. 2015 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | Soma location |
| [2] | Ceranik et al. 1997 | [9204922](https://pubmed.ncbi.nlm.nih.gov/9204922/) | Soma location |
