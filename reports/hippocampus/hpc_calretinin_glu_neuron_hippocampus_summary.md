# hippocampal calretinin-positive glutamatergic neuron — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | glutamatergic neuron (CL:0000679) | |
| Soma location | stratum lacunosum-moleculare / outer molecular layer [UBERON:0002421] | [1] [2] |
| NT | glutamatergic |  |
| Markers | Calb2+ |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0135 HPF CR Glut_1 [CS20230722_SUPT_0135] |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## 0135 HPF CR Glut_1 · 🔴 LOW

**Supporting evidence:**

- SUPT_0135 (0135 HPF CR Glut_1) is the only WMBv1 glutamatergic supertype located in the stratum lacunosum-moleculare / outer molecular layer of the HPF, matching the anatomical location of hpc_calretinin_glu_neuron_hippocampus. Analysis of the WMBv1 precomputed stats (CCN20230722) reveals high Calb2 expression in SUPT_0135 reference cells (mean 4.5-8.2 UMIs/cell across 5 clusters; n=1 each) compared to near-absent Calb2 in DG Glut supertypes (0.08-0.16 UMIs). SUPT_0135 reference cells co-express high Reln (12-13 UMIs/cell) and Trp73 (8.8-9.7 UMIs/cell), consistent with Cajal-Retzius cell identity, placing these cells in the SLM/OML. SUPT_0135 is the only HPF Glut supertype not assigned to DG, CA1, CA2, CA3, or SUB subclasses. Confidence is LOW because: (1) Slc17a8 (VGluT3), the second defining marker of this classical node, is essentially absent from SUPT_0135 (0-0.3 UMIs in 2/5 clusters only); (2) the reference population is extremely small (n=5 cells total across 5 clusters), limiting statistical confidence; (3) the WMBv1 'HPF CR' designation may specifically capture developmentally transient Cajal-Retzius cells rather than the proposed VGluT3+/Calb2+ glutamatergic population described in the hippocampal literature. [Atlas metadata]

**Concerns:**

- **location** (APPROXIMATE): A=stratum lacunosum-moleculare / outer molecular layer (UBERON:0002421, compartment: SOMA) / B=HPF CR Glut_1 — only HPF Glut supertype outside DG/CA/SUB subclasses; MERFISH anatomy not assessed. SUPT_0135 is the only WMBv1 glutamatergic supertype in the HPF that falls outside the DG, CA1-ProS, CA2-FC-IG, CA3, and SUB-ProS subclasses. The SLM/OML location of the classical node is consistent with the HPF CR designation, though precise MERFISH soma assignments have not been assessed.
- SUPT_0135 reference cells strongly express Reln and Trp73 (both Cajal-Retzius cell markers) alongside Calb2. Classical Cajal-Retzius cells are developmentally transient (largely absent in adult rodent hippocampus) and may not correspond to the Calb2+/Slc17a8+ glutamatergic neurons described in adult SLM/OML. The SUPT_0135 supertype has n=5 reference cells total (1 per cluster), which is the smallest representation of any HPF Glut supertype in WMBv1, consistent with either extreme rarity or a poorly sampled cell type. The 'CR' designation in WMBv1 may specifically label Cajal-Retzius remnants captured during adult brain profiling.

**What would upgrade confidence:**

- *Unresolved:* Is SUPT_0135 a Cajal-Retzius remnant population or does it represent the adult SLM/OML Calb2+/Slc17a8+ glutamatergic neurons described in the literature? ISH validation of Trp73 and Calb2 co-expression in adult SLM/OML would resolve this.
- *Unresolved:* Why is Slc17a8 (VGluT3) absent from SUPT_0135 given that SLM glutamatergic neurons are described as VGluT3+? Is VGluT3 expression limited to a subset of Calb2+ SLM cells, or is the classical node definition too broad?
- *Proposed:* Run annotation transfer from a dataset with validated Calb2+/Slc17a8+ SLM cells onto WMBv1 to confirm whether these cells map to SUPT_0135 or to other supertypes.
- *Proposed:* Check MERFISH soma locations for SUPT_0135 cells in WMBv1 (via atlas browser or MERFISH cell type distribution data) to confirm SLM/OML placement.

---

## Proposed experiments

### 1 — Other

- Run annotation transfer from a dataset with validated Calb2+/Slc17a8+ SLM cells onto WMBv1 to confirm whether these cells map to SUPT_0135 or to other supertypes.
*Resolves: edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135*

### 2 — MERFISH / spatial transcriptomics

- Check MERFISH soma locations for SUPT_0135 cells in WMBv1 (via atlas browser or MERFISH cell type distribution data) to confirm SLM/OML placement.
*Resolves: edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135*

---

## Open questions

1. Is SUPT_0135 a Cajal-Retzius remnant population or does it represent the adult SLM/OML Calb2+/Slc17a8+ glutamatergic neurons described in the literature? ISH validation of Trp73 and Calb2 co-expression in adult SLM/OML would resolve this.
2. Why is Slc17a8 (VGluT3) absent from SUPT_0135 given that SLM glutamatergic neurons are described as VGluT3+? Is VGluT3 expression limited to a subset of Calb2+ SLM cells, or is the classical node definition too broad?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_hpc_calretinin_glu_neuron_hippocampus_to_supt_0135 | Atlas metadata | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wheeler et al. 2015 · PMID:26402459 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | soma location |
| [2] | Ceranik et al. 1997 · PMID:9204922 | [9204922](https://pubmed.ncbi.nlm.nih.gov/9204922/) | soma location |
