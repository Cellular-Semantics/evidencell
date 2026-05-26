# Radiatum-lacunosum moleculare (R-LM) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Stratum oriens of hippocampus [UBERON:0014548] | [1] |
| NT | GABAergic | — |
| Markers | Sst+ | [2] |

**Node notes:** Stub from cite-traverse (2026-04-10). THIN EVIDENCE — described in one study (Oliva et al. 2000 [2]) using GIN transgenic mice labelling SST+ interneurons. The defining morphological feature is axonal arborisation into stratum radiatum and stratum lacunosum-moleculare. No subsequent transcriptomic characterisation has been reported. This node is flagged as thin evidence and may require a targeted literature search before a confident mapping edge can be assigned.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | ⚪ UNCERTAIN | NT CONSISTENT · stratum oriens CONSISTENT · R-LM vs OLM unresolvable | Eliminated |

1 edge total · relationship type: UNCERTAIN. No MODERATE or LOW edges are present.

---

## Eliminated candidates

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] — ⚪ UNCERTAIN

The primary disqualifying signal is that SUPT_0216 [CS20230722_SUPT_0216] is simultaneously the primary OLM cell candidate supertype; R-LM and OLM cells share SST+ identity and stratum oriens soma location and are not separable at this supertype level from atlas metadata alone.

**Supporting evidence**

- NT alignment: CONSISTENT — R-LM cell is GABAergic; SUPT_0216 belongs to the Sst Gaba subclass.
- Stratum oriens soma location: CONSISTENT — SUPT_0216 [CS20230722_SUPT_0216] has strong CA1 stratum oriens representation (818 cells), matching the reported soma location [1].
- Sst marker: CONSISTENT — Sst is the defining classical marker [2]; SUPT_0216 expresses Sst (precomputed mean 11.44). Additional atlas markers Reln, Rbp4, and Npffr1 may inform distinction from other Sst subtypes (see below).
- Annotation transfer (MapMyCells; Yao 2021, GEO:GSE185862; n=273 HIP Sst cells): Sst subclass maps to WMBv1 at subclass level with high confidence (F1=0.983). At supertype level, SUPT_0216 [CS20230722_SUPT_0216] receives 83/273 Sst cells (F1=0.488, purity=1.0), indicating that a subset of SST+ hippocampal cells projects to this supertype.

Additionally, Perez et al. 2020 [1] provide transcriptomic context for R-LM-like neurons:

> their transcriptomes were closest to RLMb and Neuroglialform interneurons whose somata are located at the border between the stratum radiatum (sr) and the slm and exhibit short dendrites
> — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [1] <!-- quote_key: 224817966_e829ad95 -->

**Marker evidence provenance**

- **Sst:** Evidence from Oliva et al. 2000 [2] using the GIN transgenic reporter line (protein/reporter-level). The GIN line labels a subset of SST+ interneurons; specificity to R-LM cells versus other SST+ stratum oriens types (OLM, bistratified, hippocampo-septal, oriens-oriens) is not established.
- No quantitative detection rates or mean expression values from re-analysis or raw-count single-cell sources are available specifically for R-LM cells.
- SUPT_0216 [CS20230722_SUPT_0216] Reln, Rbp4, and Npffr1 are reported at supertype level from atlas metadata; cell-level co-expression with Sst in morphologically confirmed R-LM cells has not been assessed. Reln co-expression may be informative for distinguishing R-LM from OLM cells *(note: Chrna2+/Reln+ is the canonical OLM marker profile; R-LM cells may be Reln+/Chrna2−, but this has not been confirmed transcriptomically)*.

**Concerns**

- **OLM cell ambiguity (AMBIGUOUS_MAPPING).** SUPT_0216 [CS20230722_SUPT_0216] is simultaneously the primary OLM cell candidate supertype based on annotation transfer from Chrna2-Cre data *(note: this evidence is in the atlas edge for OLM cells; the corresponding publication is not indexed in this report's reference list)*. R-LM and OLM cells cannot be separated at this supertype level from atlas metadata alone.
- **Single-study evidence (SINGLE_STUDY).** R-LM cell described in a single study (Oliva et al. 2000 [2]). No subsequent transcriptomic characterisation. May not be a transcriptomically separable type from OLM or P-LM cells.
- **No discriminating marker (NO_DISCRIMINATING_MARKER).** No axon-projection or laminar markers distinguishing R-LM from OLM cells are present in atlas supertype metadata.
- **Annotation transfer F1 modest (0.488).** The dominant SST+ supertype target is SUPT_0219 (Sst Gaba_6, F1=0.759). R-LM cell could reside in SUPT_0219 rather than SUPT_0216 [CS20230722_SUPT_0216].

**What would upgrade confidence**

- Targeted single-cell or patch-seq RNA-seq of GIN+ neurons with confirmed R-LM morphology (soma in stratum oriens; axon arborising in stratum radiatum and lacunosum-moleculare) would allow direct transcriptomic placement in WMBv1.
- Annotation transfer from a source dataset with morphologically resolved SST+ hippocampal interneuron identities could separate R-LM from OLM at supertype or cluster level.
- Examination of Reln, Rbp4, and Npffr1 co-expression in GIN+ R-LM cells would test whether SUPT_0216's defining markers are enriched in R-LM versus OLM morphologies.

---

## Proposed experiments

### Patch-seq / morpho-transcriptomics
- **What:** Patch-seq of GIN+ neurons in CA1 stratum oriens with post-hoc morphological reconstruction to identify R-LM (axon in SR/SLM) versus OLM (axon in alveus) configurations, followed by WMBv1 label transfer
- **Target:** Direct transcriptomic assignment to WMBv1 supertype
- **Expected output:** AnnotationTransferEvidence on this edge; or identification of SUPT_0219 as the better-fitting target
- **Resolves:** Open questions 1 and 2

### Annotation transfer from labelled source datasets
- **What:** Re-run MapMyCells annotation transfer using a source dataset with morphologically validated SST+ hippocampal interneuron identity labels (R-LM morphology confirmed)
- **Target:** Supertype-level probabilities for R-LM cells specifically; F1 ≥ 0.70 at SUPERTYPE level
- **Expected output:** AnnotationTransferEvidence on this edge; resolve SUPT_0216 vs SUPT_0219 ambiguity
- **Resolves:** Open question 2

### Spatial marker validation
- **What:** Multiplexed smFISH or RNAscope in hippocampal sections probing Sst, Reln, Chrna2, and Npffr1/Rbp4, combined with laminar position scoring
- **Target:** Identify a Reln+/Chrna2− stratum oriens population consistent with SUPT_0216 identity co-occurring with R-LM axon morphology
- **Expected output:** LiteratureEvidence supporting SUPT_0216 as R-LM candidate; or evidence of molecular identity shared with OLM
- **Resolves:** Open questions 1, 3, 4

---

## Open questions

1. Does the R-LM cell represent a transcriptomically distinct type from OLM cells, or is it a morphological variant within the same transcriptomic cluster?
2. What WMBv1 supertype does R-LM map to — SUPT_0216 [CS20230722_SUPT_0216] (Sst Gaba_3) or SUPT_0219 (Sst Gaba_6, the dominant SST+ annotation-transfer target)?
3. Is the GIN transgenic line specific enough to R-LM cells to serve as an enrichment strategy for transcriptomic profiling, or does it label a heterogeneous mixture of SST+ stratum oriens interneurons?
4. Are Reln, Rbp4, and Npffr1 (the defining markers of SUPT_0216 [CS20230722_SUPT_0216]) expressed in morphologically confirmed R-LM cells?
5. Should R-LM be treated as a provisional cell type requiring targeted literature search and morpho-transcriptomic validation before any mapping edge can advance beyond UNCERTAIN confidence?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA — supertype marker and anatomy comparison | PARTIAL |
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Sst subclass n=273 HIP cells | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | Soma location (stratum oriens) |
| [2] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst defining marker |
