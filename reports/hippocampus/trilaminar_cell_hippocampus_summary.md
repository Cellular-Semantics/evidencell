# Trilaminar cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The hippocampal trilaminar cell is a GABAergic interneuron with soma in CA1 stratum oriens, defined by long-range projections to the subiculum and medial septum, a distinctive burst-firing electrophysiology, and co-expression of parvalbumin (Pvalb) with the muscarinic receptor M2R (Chrm2) in the absence of somatostatin [1]. Its long-range projecting character and M2R positivity distinguish it from other PV+ interneurons in stratum oriens — including basket and bistratified cells — but no transcriptomic study has yet isolated this population, leaving its correspondence to the WMBv1 atlas entirely provisional.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Markers | Pvalb (defining), M2R/Chrm2 (defining) | — |
| Negative markers | Sst | — |
| Neuropeptides | — | — |
| CL term | — (no mapping) | — |

<details><summary>Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 stratum oriens documented by Katona et al. 2017 (Somogyi lab) · [1]. No verbatim quote is available in the current evidence set; the location assertion derives from the classical characterisation study.
- **PV+/M2R+/SOM- profile:** the three-marker combination is the canonical molecular signature of the trilaminar cell; M2R (Chrm2) positivity with Sst negativity are the discriminating features relative to other PV+ stratum oriens types. No primary-literature snippets with quote keys are recorded in the facts file for these properties.
- **Long-range projection identity:** the trilaminar cell projects to the subiculum and medial septum, distinguishing it from the PV basket cell whose axon is locally confined. This property cannot be assessed from atlas metadata alone.

</details>

Cell Ontology mapping: no CL term is mapped for this node. The well-documented multimodal definition warrants a CL new term request once a transcriptomic anchoring is established.

---

## Results

One candidate atlas supertype was assessed. The sole edge carries LOW confidence, reflecting that the Pvalb Gaba_2 supertype (SUPT_0206) is shared with PV basket cells and that the discriminating features of the trilaminar cell — M2R expression, long-range projection, burst-firing — cannot be resolved from atlas metadata or the current annotation transfer.

![Annotation transfer F1 heatmap — Yao 2021 SSv4 Pvalb subclass → WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_trilaminar_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) SSv4 Pvalb source group (n=66 HIP cells) mapped to WMBv1. The Pvalb label is morphologically unresolved; signal is distributed across Pvalb supertypes with SUPT_0206 (Pvalb Gaba_2) receiving 12/66 cells at supertype level (F1=0.324, target_purity=0.800).*

### Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key alignment | Verdict |
|---|---|---|---:|---|---|---|
| 1 | — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | 2860 | 🔴 LOW | Pvalb CONSISTENT · CA1 SO CONSISTENT · M2R not in atlas markers · Sst low-level present | Speculative |

1 edge total · relationship type: PARTIAL_OVERLAP.

### 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🔴 LOW

**Supporting evidence**

- Pvalb Gaba_2 belongs to the Pvalb Gaba subclass, confirming GABAergic identity consistent with the trilaminar cell.
- SUPT_0206 is enriched in CA1 stratum oriens (493 cells) and CA3 stratum oriens (152 cells), directly matching the trilaminar cell's soma location in CA1 stratum oriens [UBERON:0014552] [1].
- Precomputed expression: Pvalb mean 8.74 (CONSISTENT with PV+ immunoreactivity); Chrm2/M2R mean 4.52 (CONSISTENT with M2R positivity by precomputed stats, although Chrm2 is absent from SUPT_0206 defining markers — precomputed-stats confirmation only).
- Negative marker Sst: Sst is absent from SUPT_0206 defining markers (CONSISTENT at marker-list level); precomputed mean 2.72 indicates low but non-zero transcript level.
- Annotation transfer: MapMyCells local annotation transfer, Yao 2021 (GEO:GSE185862) SSv4 Pvalb subclass (n=66 HIP cells); SUPT_0206 receives 12/66 cells (F1=0.324, target_purity=0.800). PARTIAL: the SSv4 Pvalb label is morphologically unresolved (mixes basket, axo-axonic, bistratified, and any trilaminar cells); the best subclass-level hit is the Pvalb chandelier Gaba subclass (F1=0.588, n=25 cells), likely reflecting the well-separated chandelier/AAC component rather than trilaminar identity. *(note: this should not be interpreted as evidence for a chandelier/trilaminar relationship.)*

**Concerns**

- AMBIGUOUS_MAPPING: SUPT_0206 (Pvalb Gaba_2) is the same supertype assigned to PV basket cells. Trilaminar cells and PV basket cells share Pvalb expression and stratum oriens soma location; no transcriptomic features distinguishing them are available in atlas metadata.
- MARKER_NOT_SPECIFIC: M2R (Chrm2), the key discriminating marker, is not in SUPT_0206 defining markers. Long-range projection identity cannot be assessed from metadata.
- MARKER_NOT_SPECIFIC: Sst precomputed mean 2.72. Low-level Sst co-expression in Pvalb interneurons is known; does not disqualify the mapping but reduces the discriminating power of Sst negativity.
- SINGLE_STUDY: the classical trilaminar cell definition rests on Katona et al. 2017 [1]; no independent transcriptomic characterisation exists.

**What would upgrade confidence**

- Patch-seq from morphologically confirmed trilaminar cells (identified by long-range projection or burst-firing) to yield a definitive transcriptomic profile and enable direct cluster-level atlas assignment.
- Demonstration that Chrm2-high/Pvalb+/Sst-low cells within SUPT_0206 form a transcriptomically separable sub-cluster distinct from PV basket cells.

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The trilaminar cell is defined on a CLASSICAL_MULTIMODAL basis: soma in CA1 stratum oriens [UBERON:0014552] [1]; GABAergic neurotransmitter type; defining markers Pvalb and M2R (Chrm2); negative marker Sst. Primary characterisation from Katona et al. 2017 (Somogyi lab, PMID:27997999); no subsequent transcriptomic characterisation is recorded.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at rank 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Numerical values from precomputed expression on the supertype in the taxonomy reference store.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4) |
| Source cluster label | Pvalb (n=66 HIP cells; morphologically unresolved) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398; Pvalb subclass n=66 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| Code reference | https://github.com/AllenInstitute/cell_type_mapper |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 SSv4 Pvalb label encompasses PV basket, axo-axonic, bistratified, and any trilaminar cells; trilaminar-specific resolution is not achievable from this morphologically unresolved source. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed expression from supertype YAML in the taxonomy reference store.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:25+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA (x2); ANNOTATION_TRANSFER | PARTIAL; PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Trilaminar cell → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] at LOW confidence. Key support: SUPT_0206 is enriched in CA1 stratum oriens (493 cells), consistent with the trilaminar cell soma location [1]; Pvalb (precomputed mean 8.74) and GABA neurotransmitter type are CONSISTENT; Chrm2/M2R shows detectable expression (mean 4.52); MapMyCells annotation transfer of the Yao 2021 Pvalb subclass (n=66, morphologically unresolved) places 12/66 cells at SUPT_0206 (F1=0.324, target_purity=0.800). Key caveats: SUPT_0206 is the same supertype assigned to PV basket cells and likely contains multiple PV+ interneuron types that cannot be separated at supertype resolution; the discriminating features of the trilaminar cell (long-range projection, M2R specificity, burst-firing) are inaccessible from atlas metadata; Sst shows low-level expression (mean 2.72) weakening the negative-marker constraint; evidence rests on a single study [1].

### Proposed experiments

**Morphologically confirmed reference dataset + MapMyCells.**

- Record and fill trilaminar cells in acute hippocampal slices (identified by burst-firing and/or retrograde label from subiculum or medial septum), then extract cytoplasm for scRNA-seq and apply MapMyCells to assign WMBv1 cluster-level correspondences within SUPT_0206.
- Cross-check: current AT uses the bulk Yao 2021 Pvalb label (morphologically unresolved); trilaminar-specific resolution requires a morphologically or projection-confirmed labelled reference. This is the primary bottleneck for confidence upgrade.

**Retrograde tracing + single-cell transcriptomics.**

- Inject retrograde tracer into medial septum or subiculum; FACS-sort labelled neurons from CA1 stratum oriens for scRNA-seq. Directly identifies the transcriptomic profile of long-range projecting PV+ cells and distinguishes trilaminar from hippocampo-septal cells at the transcript level.
- Cross-check: no current evidence exists for the transcriptomic identity of projection-confirmed trilaminar cells; this is the most direct route to a definitive cluster assignment.

**Multiplexed FISH — Pvalb + Chrm2 + Sst.**

- Co-detect Pvalb, Chrm2/M2R, and Sst transcripts in CA1 stratum oriens sections to quantify the PV+/M2R-high/Sst-low fraction and compare against SUPT_0206 precomputed expression values, and to determine whether Chrm2 expression is enriched in a distinct subpopulation relative to PV basket cells.
- Cross-check: precomputed mean Chrm2=4.52 in SUPT_0206 motivates this experiment; if Chrm2 is heterogeneously distributed, it may identify a sub-cluster target.

### Open questions

1. Does SUPT_0206 (Pvalb Gaba_2) contain a transcriptomically distinct sub-cluster corresponding to long-range projecting Pvalb+/Chrm2-high trilaminar cells, or are trilaminar cells indistinguishable from PV basket cells at current atlas resolution?
2. Is Chrm2/M2R expression sufficiently high and selective within the Pvalb subclass to serve as a transcriptomic discriminator for trilaminar cells in WMBv1?
3. What is the transcriptomic relationship between the trilaminar cell and the hippocampo-septal cell — are they separable at any WMBv1 taxonomy level?
4. Can the low Sst signal (mean 2.72) in SUPT_0206 be attributed to a specific sub-cluster, or is it uniformly distributed, and does it compromise the Sst-negative criterion for trilaminar cell identity?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | soma location; PV+/M2R+/SOM- profile; classical type definition |
