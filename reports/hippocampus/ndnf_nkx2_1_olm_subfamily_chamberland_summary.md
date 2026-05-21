# Ndnf::Nkx2-1-IN (Ndnf-OLM, Chamberland 2024) — WMBv1 Mapping Report

## Introduction

The Ndnf::Nkx2-1-IN subfamily is one of four genetically defined subtypes of hippocampal somatostatin-expressing interneurons identified by Chamberland et al. 2024 [1]. These cells are identified by the Sst-Flp;Ndnf-Cre;Nkx2-1-Cre triple intersection, sit progressively deeper in the stratum oriens/alveus (O/A) than Sst::Tac1-INs, and function as oriens-lacunosum-moleculare (OLM)-type interneurons that selectively target CA1 pyramidal cells rather than fast-spiking interneurons.

> the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c084d5c0 -->

> hippocampal somatostatin-expressing interneurons (Sst-INs) can be divided into at least four subfamilies, each with distinct functions
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_53fb33cc -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | GABAergic | [1] |
| Defining markers | Sst; Ndnf; Nkx2-1 | [1] |
| Soma location | Hippocampus stratum oriens [UBERON:0005371]; deep O/A, CA1 | [1] |
| Connectivity | Selectively targets CA1 pyramidal cells | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

> While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
> — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->

> the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c084d5c0 -->

</details>

### Cell Ontology mapping

No Cell Ontology term assigned. This subfamily is functionally OLM-like (pyramidal-cell-targeting, deep O/A soma) but defined by distinct genetics from the canonical Chrna2+ OLM population.

---

## Results

**The Ndnf::Nkx2-1-IN subfamily is not cleanly resolved in WMBv1.** The in-silico Ndnf-derived source pool is small (n=19 cells qualified at the per-cluster threshold) and fragments across multiple WMBv1 targets (Lamp5, Sncg, Sst subclasses) with F1 < 0.1 at every level. No confident WMBv1 assignment can be made from this AT evidence alone. A single speculative LOW edge is recorded to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] based on biological prior (Sst+ OLM-like identity), but this is not supported by the AT data.

![Annotation transfer F1 heatmap (GEO:GSE99888 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/figures/f1_tree.png)

### Candidate overview table

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0216 Sst Gaba_3 | CS20230722_SUPT_0216 | 🔴 LOW | UNCERTAIN | Speculative |

### Property alignment — 0216 Sst Gaba_3 [CS20230722_SUPT_0216]

**Table 1: Property comparison**

| Property | Classical type | WMBv1 SUPT_0216 | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | GABA | CONSISTENT |
| Marker — Sst | Defining (subset) | Sst expressed in Sst Gaba_3 supertype | APPROXIMATE |

**Table 2: Evidence support**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | PARTIAL | n=19 Ndnf-labelled cells fragment across Lamp5, Sncg, and Sst targets; F1 < 0.1 everywhere; best target at supertype is Lamp5 Gaba_1 (F1=0.055) — no credible assignment possible |

**MapMyCells F1 by level — Ndnf source group (per-cluster labels, GEO:GSE99888)**

| Level | Best target | F1 | Group purity | Target purity | n cells mapped |
|---|---|---|---|---|---|
| SUBCLASS | 049 Lamp5 Gaba | 0.039 | 0.353 | 0.021 | 6 |
| SUPERTYPE | 0199 Lamp5 Gaba_1 | 0.055 | 0.368 | 0.030 | 7 |

*(note: the Sst Gaba_3 supertype [CS20230722_SUPT_0216] is the speculative edge target based on biological prior, not on AT evidence — the AT best hit at supertype rank is Lamp5 Gaba_1, which reflects dispersal rather than a meaningful signal.)*

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Ndnf::Nkx2-1-IN (Chamberland 2024) defined as CLASSICAL_MULTIMODAL. Source: Chamberland et al. 2024 (PMID:38640347). Chamberland subfamily labels derived in-silico from Harris 2018 (GEO:GSE99888) by applying Ndnf co-expression criteria to per-cluster mean expression. Only one Harris Class qualified at the per-cluster Ndnf threshold, giving a source pool of n=19 cells — too small for reliable F1 scoring.

**Annotation transfer.**

| Field | Value |
|---|---|
| Run | at_run_20260512_chamberland_subfamily_mmc_wmbv1 |
| Source dataset | GEO:GSE99888 (Harris 2018) with Chamberland in-silico per-cluster subfamily labels |
| Source label used | Ndnf (per-cluster rule) |
| n cells in Ndnf label | 19 |
| n cells total | 3663 |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Target atlas | WMBv1 (CCN20230722) |
| Atlas pseudobulk SHA | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Bootstrap threshold | 0.8 |
| Primary result | Per-cluster label derivation (dropout-robust) |
| Caveats | Source pool is very small (n=19; single Harris Class qualified at Ndnf threshold). AT result is uninformative — fragmentation across multiple WMBv1 targets with F1 < 0.1 everywhere reflects insufficient source-side specificity, not atlas failure. Targeted Ndnf::Nkx2-1 scRNA-seq or a larger source dataset is required before a meaningful WMBv1 assignment can be made. |

**Anti-hallucination.** All accessions, quote keys, and PMIDs validated against the KB reference store at write time.

*Report generated 2026-05-19. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`.*

**Evidence base**

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 1 |

</details>

---

## Discussion

**The Ndnf::Nkx2-1-IN subfamily cannot be mapped to WMBv1 at the current evidence level.** The speculative edge to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] is motivated entirely by biological prior (Sst+ OLM-like connectivity, deep O/A soma) and is not supported by the AT data, which fragments completely across unrelated WMBv1 types. The root cause is the small in-silico source pool: only one Harris 2018 transcriptomic Class qualified the per-cluster Ndnf threshold, yielding n=19 cells — too few for reliable F1 scoring. This is a source-side limitation, not a failure of WMBv1 resolution. The most informative path forward is to obtain targeted Ndnf::Nkx2-1 scRNA-seq from CA1 stratum oriens using Chamberland's genetic strategy and then run MapMyCells from that curated source.

### Proposed experiments

1. Obtain or generate a targeted Ndnf::Nkx2-1-IN scRNA-seq dataset from CA1 stratum oriens using the Sst-Flp;Ndnf-Cre;Nkx2-1-Cre triple-intersection strategy, and run MapMyCells onto WMBv1.
2. Query whether Chamberland 2024 published single-cell transcriptomic data for the Ndnf::Nkx2-1-IN subtype specifically, which could serve as a more reliable source pool than the in-silico re-labelling of Harris 2018.
3. If a larger Ndnf/Nkx2-1 expression dataset is available, re-run the per-cluster label derivation with a relaxed Ndnf threshold to increase the source pool, and assess whether the fragmentation pattern persists.

### Open questions

1. Why does the in-silico Ndnf labelling produce such a small source pool (n=19) compared to the other Chamberland subfamilies (Chrna2: 153, Sst_Nos1: 35, Sst_Tac1: 167)? Is Ndnf expression genuinely rare in the Harris 2018 dataset, or is the threshold too stringent?
2. Does the Ndnf::Nkx2-1 intersection actually capture a distinct WMBv1 type not resolved in Harris 2018, or does it define a functional property of cells that could belong to multiple transcriptomic clusters?

---

## References

[1] Chamberland et al. 2024 · PMID:38640347 · DOI:10.1073/pnas.2306382121
