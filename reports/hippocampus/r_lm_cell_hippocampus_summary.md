# Radiatum-lacunosum moleculare (R-LM) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Stratum oriens of hippocampus [UBERON:0014548] | [1] |
| Neurotransmitter | GABAergic | — |
| Defining markers | Sst | [2] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — | — |

**Notes on evidence quality:** The R-LM cell was characterised in a single study (Oliva et al. 2000) [2] using GIN transgenic mice that label SST+ interneurons. The soma is reported in stratum oriens, but the cell's defining morphological feature is its axonal arborisation into stratum radiatum and stratum lacunosum-moleculare — the feature that gives the type its name. No subsequent transcriptomic characterisation of this type has been reported. This node is flagged as thin evidence and may require a targeted literature search before a confident mapping edge can be assigned.

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | — | ⚪ UNCERTAIN | NT consistent; stratum oriens location consistent; Sst implicit; R-LM vs OLM unresolvable at supertype level | Eliminated |

**Total edges:** 1 (UNCERTAIN). No MODERATE or LOW edges are present; the single candidate has been eliminated pending morpho-transcriptomic evidence capable of separating R-LM from OLM cells.

---

## Eliminated candidates

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · ⚪ UNCERTAIN

**Supporting evidence**

- NT alignment is CONSISTENT: the R-LM cell is GABAergic and the atlas supertype belongs to the Sst Gaba subclass (GABA identity, Sst-expressing). [2]
- Stratum oriens soma location is CONSISTENT: SUPT_0216 has strong CA1 stratum oriens representation (818 cells in atlas metadata), matching the reported soma location of R-LM cells. [1]
- Sst marker alignment is CONSISTENT: Sst is the defining classical marker [2]; SUPT_0216 carries Sst expression (precomputed mean: 11.44), and additional defining markers include Reln, Rbp4, and Npffr1 — Reln co-expression may be informative for distinguishing R-LM from OLM cells (see Concerns below).
- Annotation transfer (MapMyCells; Yao 2021, GEO:GSE185862; n=273 HIP SST+ cells) places the Sst subclass onto WMBv1 at subclass level with high confidence (F1=0.983; best target: 053 Sst Gaba), confirming overall SST+ identity. At supertype level, SUPT_0216 receives 83/273 Sst cells (F1=0.488, target_purity=1.0), indicating that a subset of SST+ hippocampal cells projects to this supertype.

**Marker evidence provenance**

- Sst marker evidence derives from Oliva et al. 2000 [2] using the GIN transgenic reporter line — a protein-reporter strategy, not single-cell transcriptomics. The GIN line labels a subset of SST+ interneurons; specificity to R-LM cells versus other SST+ stratum oriens types (OLM, bistratified, hippocampo-septal, oriens-oriens) is not established.
- No quantitative detection rates or mean expression values from re-analysis or raw-count single-cell sources are available specifically for R-LM cells.
- SUPT_0216 Reln, Rbp4, and Npffr1 expression is reported at supertype level from atlas metadata; cell-level co-expression with Sst in morphologically confirmed R-LM cells has not been assessed.

**Concerns**

- **OLM cell ambiguity (AMBIGUOUS_MAPPING):** SUPT_0216 (Sst Gaba_3) is simultaneously the primary OLM cell candidate supertype based on annotation transfer from Chrna2-Cre data (PMID:31420995). R-LM and OLM cells share SST+ identity and stratum oriens soma location; they are not separable at this supertype level from atlas metadata alone.
- **Single-study evidence (SINGLE_STUDY):** The R-LM cell was described in a single study (Oliva et al. 2000) [2] using GIN transgenics. No subsequent transcriptomic characterisation has been reported. It remains unclear whether R-LM cells represent a transcriptomically separable type from OLM or P-LM cells.
- **No discriminating marker (NO_DISCRIMINATING_MARKER):** No axon-projection markers or laminar markers distinguishing R-LM from OLM cells are present in the atlas supertype metadata. Morphological distinction (axon in stratum radiatum/lacunosum-moleculare vs. alveus/oriens for OLM) is not captured transcriptomically at this resolution.
- Annotation transfer F1 at supertype level is modest (0.488), indicating SUPT_0216 captures only a fraction of Sst-subclass cells. The dominant SST+ supertype target is SUPT_0219 (Sst Gaba_6, F1=0.759); the R-LM cell could reside in SUPT_0219 rather than SUPT_0216.
- The Yao 2021 SSv4 Sst subclass used for annotation transfer (GEO:GSE185862, n=273 HIP cells) is a mixed population encompassing OLM, bistratified, hippocampo-septal, oriens-oriens, and other SST+ types; subtype resolution requires a source dataset with morphologically identified SST interneuron labels.

**What would upgrade confidence**

- Targeted single-cell or patch-seq RNA-seq of GIN+ neurons with confirmed R-LM morphology (soma in stratum oriens; axon arborising into stratum radiatum and lacunosum-moleculare) would allow direct transcriptomic placement in WMBv1.
- Annotation transfer from a source dataset with morphologically resolved SST+ hippocampal interneuron identities could separate R-LM from OLM at supertype or cluster level.
- Examination of Reln, Rbp4, and Npffr1 co-expression in GIN+ R-LM cells would test whether SUPT_0216's defining markers are enriched in R-LM versus OLM morphologies.
- Multiplexed smFISH/RNAscope with laminar marker combinations (Sst, Reln, Chrna2, Npffr1) in CA1 sections could spatially resolve whether R-LM cells match a distinct transcriptomic signature.

---

## Proposed experiments

### Patch-seq / morpho-transcriptomics
- Patch-seq recording of GIN+ neurons in CA1 stratum oriens with post-hoc morphological reconstruction to identify R-LM (axon in stratum radiatum/lacunosum-moleculare) versus OLM (axon in alveus) configurations, followed by WMBv1 label transfer. This is the most direct path to a confident atlas mapping.

### Annotation transfer from labeled source datasets
- Re-run MapMyCells annotation transfer using a source dataset with morphologically validated SST+ hippocampal interneuron identity labels (e.g., Cembrowski et al. 2016 CA1 interneurome data, or recent patch-seq atlases with morphological reconstructions) to obtain supertype-level probabilities for R-LM cells specifically.
- Annotate GEO:GSE185862 Sst-subclass cells at finer resolution using marker combinations (Reln, Chrna2, Npy, Penk) before re-running atlas mapping, to reduce mixing of OLM, R-LM, and bistratified cells in the source.

### Spatial marker validation
- Multiplexed smFISH or RNAscope in hippocampal sections probing Sst, Reln, Chrna2, and Npffr1 (or Rbp4), combined with laminar position scoring, to test whether a Reln+/Chrna2– stratum oriens population consistent with SUPT_0216 identity co-occurs with cells showing R-LM axon morphology.

---

## Open questions

1. Does the R-LM cell represent a transcriptomically distinct type from OLM cells, or is it a morphological variant within the same transcriptomic cluster?
2. What WMBv1 supertype does R-LM map to — SUPT_0216 (Sst Gaba_3) or SUPT_0219 (Sst Gaba_6, the dominant SST+ annotation-transfer target at supertype level)?
3. Is the GIN transgenic line specific enough to R-LM cells to serve as an enrichment strategy for transcriptomic profiling, or does it label a heterogeneous mixture of SST+ stratum oriens interneurons?
4. Are Reln, Rbp4, and Npffr1 (the defining markers of SUPT_0216) expressed in morphologically confirmed R-LM cells?
5. Should R-LM be treated as a provisional cell type requiring targeted literature search and morpho-transcriptomic validation before any mapping edge can advance beyond UNCERTAIN confidence?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | Soma location (stratum oriens) |
| [2] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst defining marker |
