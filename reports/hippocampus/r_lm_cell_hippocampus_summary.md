# Radiatum-lacunosum moleculare (R-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The radiatum-lacunosum moleculare (R-LM) cell is an SST-positive GABAergic interneuron of the hippocampus whose defining morphological feature is an axon arborising into stratum radiatum and stratum lacunosum-moleculare, with soma reported near the stratum oriens border [1][2]. Identified using the GIN transgenic reporter line by Oliva et al. 2000 [2], the R-LM cell has not been transcriptomically characterised in any subsequent study, making its relationship to modern single-cell atlases speculative and its distinction from the morphologically similar OLM cell an unresolved open question.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Markers | Sst (defining) | [2] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — (no mapping) | — |

<details><summary>Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 stratum oriens reported by Perez et al. 2020 [1]; the GIN reporter study (Oliva et al. 2000 [2]) characterised soma position. Perez et al. 2020 [1] provide transcriptomic context for R-LM-like neurons:

  > their transcriptomes were closest to RLMb and Neuroglialform interneurons whose somata are located at the border between the stratum radiatum (sr) and the slm and exhibit short dendrites
  > — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [1] <!-- quote_key: 224817966_e829ad95 -->

- **Sst marker:** GIN transgenic reporter labelling (protein/reporter level) in Oliva et al. 2000 [2]. The GIN line marks a subset of SST+ interneurons; specificity to R-LM cells versus other SST+ stratum oriens types (OLM, bistratified, hippocampo-septal, oriens-oriens) is not established.

</details>

Cell Ontology mapping: no CL term is mapped for this node. Given thin evidence and uncertain transcriptomic identity, a CL term request should be deferred until morpho-transcriptomic validation is available.

---

## Results

One candidate atlas supertype was assessed and eliminated as UNCERTAIN. No MODERATE or LOW edges were resolved. The primary obstacle is that the proposed candidate supertype (Sst Gaba_3, SUPT_0216) is simultaneously the primary OLM cell candidate, and R-LM and OLM cells cannot be separated at supertype resolution from available atlas metadata or the current annotation transfer.

![Annotation transfer F1 heatmap — Yao 2021 SSv4 Sst subclass → WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_r_lm_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) SSv4 Sst source group (n=273 HIP cells) mapped to WMBv1. The Sst subclass maps cleanly at subclass level (F1=0.983); at supertype level, SUPT_0216 (Sst Gaba_3) receives 83/273 cells (F1=0.488, target_purity=1.0), but the dominant Sst supertype target is SUPT_0219 (Sst Gaba_6, F1=0.759, 161 cells). The Sst label is morphologically unresolved and R-LM-specific signal cannot be extracted.*

### Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | — | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 2712 | ⚪ UNCERTAIN | NT CONSISTENT · CA1 SO CONSISTENT · Sst CONSISTENT · OLM ambiguity | Eliminated |

1 edge total · relationship type: UNCERTAIN.

## Eliminated candidates

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] — ⚪ UNCERTAIN

The primary disqualifying signal is that SUPT_0216 is simultaneously the primary OLM cell candidate supertype (based on annotation transfer from Chrna2-Cre data on separate edges); R-LM and OLM cells share SST+ identity and stratum oriens soma location and are not separable at this supertype level from atlas metadata alone.

**Supporting evidence**

- NT alignment is CONSISTENT: R-LM cell is GABAergic; SUPT_0216 belongs to the Sst Gaba subclass.
- Stratum oriens soma location is CONSISTENT: SUPT_0216 has strong CA1 stratum oriens representation (818 cells), matching the reported soma location [1].
- Sst marker is CONSISTENT: Sst is the defining classical marker [2]; SUPT_0216 expresses Sst (precomputed mean 11.44). Additional atlas-defining markers Reln, Rbp4, and Npffr1 may inform distinction from other Sst subtypes.
- Annotation transfer: MapMyCells local, Yao 2021 (GEO:GSE185862) SSv4 Sst subclass (n=273 HIP cells). Sst subclass maps robustly at subclass level (265/273 cells, F1=0.983). At supertype level, SUPT_0216 receives 83/273 Sst cells (F1=0.488, target_purity=1.0), indicating a substantial Sst+ hippocampal fraction projects to this supertype. R-LM cells, if Sst+, would be expected within this fraction.

**Concerns**

- AMBIGUOUS_MAPPING: SUPT_0216 (Sst Gaba_3) is the primary OLM cell candidate supertype. R-LM and OLM cells share SST+ identity and stratum oriens soma location; they cannot be distinguished at supertype resolution from atlas metadata alone.
- SINGLE_STUDY: R-LM cell described in a single study [2] using GIN transgenic mice. No subsequent transcriptomic characterisation. May not be a transcriptomically separable type from OLM or P-LM cells.
- NO_DISCRIMINATING_MARKER: no axon-projection or laminar markers distinguishing R-LM from OLM cells are present in atlas supertype metadata.
- The dominant Sst+ supertype target in the annotation transfer is SUPT_0219 (Sst Gaba_6, F1=0.759, 161 cells); R-LM cells could reside in SUPT_0219 rather than SUPT_0216.

**What would upgrade confidence**

- Targeted patch-seq or scRNA-seq of GIN+ neurons with confirmed R-LM morphology (soma in stratum oriens; axon arborising in stratum radiatum and lacunosum-moleculare) to yield a definitive transcriptomic profile for direct atlas cluster assignment.
- Annotation transfer from a source dataset with morphologically resolved SST+ hippocampal interneuron identity labels separating R-LM from OLM at supertype or cluster level.
- Examination of Reln, Rbp4, and Npffr1 co-expression in GIN+ R-LM cells to test whether SUPT_0216's defining markers are enriched in R-LM versus OLM morphologies.

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The R-LM cell is defined on a CLASSICAL_MULTIMODAL basis: soma in CA1 stratum oriens [UBERON:0014552] [1]; GABAergic neurotransmitter type; defining marker Sst [2]. Primary characterisation from Oliva et al. 2000 (PMID:10777798) using GIN transgenic mice; no subsequent transcriptomic characterisation is recorded. Perez et al. 2020 (PMID:33404500) provides supporting transcriptomic context [1].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at rank 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Numerical values from precomputed expression on the supertype in the taxonomy reference store.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4) |
| Source cluster label | Sst (n=273 HIP cells; morphologically unresolved) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398; Sst subclass n=273 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| Code reference | https://github.com/AllenInstitute/cell_type_mapper |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 SSv4 Sst label encompasses OLM, bistratified, hippocampo-septal, oriens-oriens, and other Sst types; R-LM-specific resolution is not achievable from this morphologically unresolved source. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed expression from supertype YAML in the taxonomy reference store.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:26+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_r_lm_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** R-LM cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at UNCERTAIN confidence; candidate is ELIMINATED. Key support: SUPT_0216 has strong CA1 stratum oriens representation (818 cells) consistent with the soma location [1]; Sst expression is CONSISTENT (precomputed mean 11.44); annotation transfer of the Yao 2021 Sst subclass (n=273) places 83/273 cells at SUPT_0216 (F1=0.488, target_purity=1.0). Transcriptomic context from Perez et al. 2020 [1] places R-LM-like cells at the stratum radiatum/lacunosum-moleculare border. Key caveats: SUPT_0216 is simultaneously the primary OLM cell candidate; R-LM and OLM cells share SST+ identity and stratum oriens soma position and cannot be separated at supertype resolution; the R-LM cell was described in a single study [2] using the GIN transgenic line with no subsequent transcriptomic characterisation; the dominant Sst annotation transfer target is SUPT_0219 (F1=0.759), raising the possibility that R-LM cells may reside in SUPT_0219 rather than SUPT_0216.

### Proposed experiments

**Patch-seq from GIN+ neurons with morphological reconstruction.**

- Patch-seq of GIN+ neurons in CA1 stratum oriens with post-hoc morphological reconstruction to identify R-LM (axon in SR/SLM) versus OLM (axon in alveus) configurations, followed by WMBv1 label transfer via MapMyCells.
- Cross-check: current AT uses the bulk Sst subclass (morphologically unresolved); direct transcriptomic placement requires a morphologically confirmed R-LM labelled reference. This is the primary bottleneck for confidence upgrade and for resolving the R-LM vs. OLM ambiguity.

**Annotation transfer from labelled source datasets.**

- Run MapMyCells annotation transfer using a source dataset with morphologically validated SST+ hippocampal interneuron identity labels (R-LM morphology confirmed). Aim for F1 >= 0.70 at supertype level to resolve SUPT_0216 vs. SUPT_0219 ambiguity.
- Cross-check: current AT cannot resolve R-LM from OLM at supertype level; a morphologically resolved source dataset is required.

**Spatial marker validation — Sst + Reln + Chrna2 + Npffr1.**

- Multiplexed smFISH or RNAscope in hippocampal sections probing Sst, Reln, Chrna2, and Npffr1/Rbp4, combined with laminar position scoring. Identify a Reln+/Chrna2- stratum oriens population consistent with SUPT_0216 identity that co-occurs with R-LM axon morphology.
- Cross-check: SUPT_0216 defining markers include Reln; if R-LM cells are Reln+/Chrna2-, they would be distinguishable from canonical OLM cells (Chrna2+/Reln+) and consistent with SUPT_0216. *(note: Reln positivity in OLM cells and the Chrna2 OLM marker profile are documented in the OLM mapping graph; these are the expected reference points for the comparison.)*

### Open questions

1. Does the R-LM cell represent a transcriptomically distinct type from OLM cells, or is it a morphological variant within the same transcriptomic cluster?
2. Which WMBv1 supertype does R-LM map to — SUPT_0216 (Sst Gaba_3, OLM-associated, CA1 SO-enriched) or SUPT_0219 (Sst Gaba_6, the dominant Sst annotation transfer target)?
3. Is the GIN transgenic line specific enough to R-LM cells to serve as an enrichment strategy for transcriptomic profiling, or does it label a heterogeneous mixture of SST+ stratum oriens interneurons?
4. Are Reln, Rbp4, and Npffr1 (the defining markers of SUPT_0216) expressed in morphologically confirmed R-LM cells, or are they OLM-restricted?
5. Should the R-LM node be treated as a provisional cell type requiring targeted morpho-transcriptomic validation before any mapping edge can advance beyond UNCERTAIN confidence?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location; transcriptomic context for R-LM-like neurons |
| [2] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst defining marker |
