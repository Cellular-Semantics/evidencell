# Sst::Tac1-IN (bistratified-like, Chamberland 2024) — WMBv1 Mapping Report

## Introduction

The Sst::Tac1-IN subfamily is one of four genetically defined subtypes of hippocampal somatostatin-expressing interneurons characterised by Chamberland et al. 2024 [1]. These cells are defined by the Sst-Flp;Tac1-Cre intersection, sit closer to the CA1 pyramidal layer than the deeper OLM-type subfamilies, and function as bistratified-like interneurons that overwhelmingly target fast-spiking Pvalb interneurons rather than pyramidal cells — making them interneuron-selective inhibitors rather than principal-cell-targeting feedback inhibitors.

> the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c084d5c0 -->

> While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
> — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->

> hippocampal somatostatin-expressing interneurons (Sst-INs) can be divided into at least four subfamilies, each with distinct functions
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_53fb33cc -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | GABAergic | [1] |
| Defining markers | Sst; Tac1 | [1] |
| Soma location | Hippocampus stratum oriens [UBERON:0005371]; closer to CA1 pyramidal layer | [1] |
| Connectivity | Interneuron-selective; targets fast-spiking Pvalb interneurons | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

> the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c084d5c0 -->

> While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
> — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->

</details>

### Cell Ontology mapping

No Cell Ontology term assigned. Likely overlaps with the classical bistratified_cell_hippocampus type. The cross-subclass mapping to Pvalb (see Results) surfaces a transcriptomic Sst-Pvalb continuum for bistratified-type interneurons.

---

## Results

The Sst::Tac1-IN subfamily maps at MODERATE confidence to the 052 Pvalb Gaba subclass [CS20230722_SUBC_052], concentrating around supertype 0206 Pvalb Gaba_2 and cluster 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737]. This is a cross-subclass result: Sst::Tac1-IN cells are defined as Sst-expressing, but MapMyCells assigns them to a Pvalb subclass. This is biologically interpretable as a transcriptomic Sst-Pvalb continuum for bistratified interneurons, consistent with the functional identity of these cells as interneuron-selective types that target fast-spiking Pvalb interneurons. The subclass-level F1=0.578 (recall=0.783) provides moderate but informative support; at cluster rank the signal distributes across multiple Pvalb Gaba_2 clusters, with CLUS_0737 as the best single cluster (F1=0.466).

![Annotation transfer F1 heatmap (GEO:GSE99888 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/figures/f1_tree.png)

### Candidate overview table

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 052 Pvalb Gaba (subclass) | CS20230722_SUBC_052 | 🟡 MODERATE | PARTIAL_OVERLAP | Best candidate |

### Property alignment — 052 Pvalb Gaba [CS20230722_SUBC_052]

**Table 1: Property comparison**

| Property | Classical type | WMBv1 Pvalb Gaba subclass | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | GABA | CONSISTENT |
| Marker — Sst | Defining | Sst not in Pvalb subclass defining set; transcriptomic Sst-Pvalb continuum | APPROXIMATE |
| Connectivity — target | Fast-spiking Pvalb interneurons | Pvalb cluster (postsynaptic target not annotated in atlas, but transcriptomic placement is independently consistent) | APPROXIMATE |

**Table 2: Evidence support**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | SUPPORT | Per-cluster Chamberland labels: Sst_Tac1 cells (n=167) map to Pvalb Gaba subclass (F1=0.578, recall=0.783); cross-subclass result is consistent with transcriptomic Sst-Pvalb continuity for bistratified types |

**MapMyCells F1 by level — Sst_Tac1 source group (per-cluster labels, GEO:GSE99888)**

| Level | Best target | F1 | Group purity | Target purity | n cells mapped |
|---|---|---|---|---|---|
| SUBCLASS | 052 Pvalb Gaba [CS20230722_SUBC_052] | 0.578 | 0.783 | 0.458 | 126 |
| SUPERTYPE | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | 0.566 | 0.437 | 0.802 | 69 |
| CLUSTER | 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] | 0.466 | 0.310 | 0.939 | 31 |

*(note: PARTIAL_OVERLAP at subclass rank reflects that Sst::Tac1-IN by functional definition spans multiple WMBv1 Pvalb clusters rather than a single one. The low group_purity at supertype (0.437) indicates that Sst::Tac1-IN cells are spread across more than one Pvalb Gaba supertype.)*

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Sst::Tac1-IN (Chamberland 2024) defined as CLASSICAL_MULTIMODAL. Source: Chamberland et al. 2024 (PMID:38640347). Chamberland subfamily labels derived in-silico from Harris 2018 (GEO:GSE99888) by applying the Sst+Tac1 expression-product > 1 criterion to per-cluster mean expression. Note: this node likely overlaps with the classical bistratified_cell_hippocampus type in hippocampus_GABAergic_interneurons.yaml.

**Annotation transfer.**

| Field | Value |
|---|---|
| Run | at_run_20260512_chamberland_subfamily_mmc_wmbv1 |
| Source dataset | GEO:GSE99888 (Harris 2018) with Chamberland in-silico per-cluster subfamily labels |
| Source label used | Sst_Tac1 (per-cluster rule: Sst+Tac1 expression-product > 1) |
| n cells in Sst_Tac1 label | 167 |
| n cells total | 3663 |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Target atlas | WMBv1 (CCN20230722) |
| Atlas pseudobulk SHA | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Bootstrap threshold | 0.8 |
| Primary result | Per-cluster label derivation (dropout-robust) |
| Caveats | The cross-subclass result (Pvalb Gaba, not Sst Gaba) is the primary finding — biologically interpretable as transcriptomic Sst-Pvalb continuity for bistratified types. The Sst::Tac1-IN population distributes across multiple Pvalb Gaba_2 clusters, consistent with a functional definition spanning multiple transcriptomic clusters. |

**Anti-hallucination.** All accessions, quote keys, and PMIDs validated against the KB reference store at write time.

*Report generated 2026-05-19. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`.*

**Evidence base**

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 1 |

</details>

---

## Discussion

**The best candidate is the 052 Pvalb Gaba subclass [CS20230722_SUBC_052] at MODERATE confidence**, with the subclass-level best target being supertype 0206 Pvalb Gaba_2 and best cluster CLUS_0737 Pvalb Gaba_2 [CS20230722_CLUS_0737]. The cross-subclass mapping of Sst::Tac1-IN cells to a Pvalb subclass is the key biological finding of this analysis: it surfaces a transcriptomic Sst-Pvalb continuum for bistratified-type interneurons. Bistratified cells are known to span both Sst and Pvalb identity markers depending on sub-subtype, and the functional connectivity of Sst::Tac1-INs (targeting fast-spiking Pvalb interneurons) is consistent with their transcriptomic placement in the Pvalb branch. The PARTIAL_OVERLAP relationship reflects that the Sst::Tac1-IN functional class spans multiple WMBv1 Pvalb clusters rather than mapping to a single discrete cluster. MODERATE rather than HIGH confidence is appropriate because: (a) the source-side Sst expression does not match the Pvalb subclass assignment at the marker level; and (b) cluster-level precision is low (0.31 for CLUS_0737).

The main curation action is to link this node to the classical bistratified_cell_hippocampus node and assess whether the cross-subclass Pvalb mapping resolves or complicates that classical assignment.

### Proposed experiments

1. Obtain or generate Sst-Flp;Tac1-Cre targeted scRNA-seq from CA1 stratum oriens using Chamberland's genetic strategy, and run MapMyCells onto WMBv1, to test whether the Pvalb subclass assignment is reproduced with a source population that is directly validated by genetics rather than in-silico labelling.
2. Assess Tac1 expression in CLUS_0737 and neighbouring Pvalb Gaba_2 clusters at the atlas precomputed stats level to determine whether Tac1 shows cluster-level enrichment within the Pvalb Gaba_2 supertype.
3. Cross-map to the classical bistratified_cell_hippocampus node once both graphs are co-loaded, to quantify overlap and determine whether both nodes converge on the same WMBv1 clusters or diverge.

### Open questions

1. What proportion of CLUS_0737 (Pvalb Gaba_2) contains canonical bistratified morphology, and what proportion are Pvalb-only interneurons? Patch-seq or multiplexed FISH of CA1 stratum oriens neurons in this cluster would answer this.
2. Does the cross-subclass placement of Sst::Tac1-IN cells in the Pvalb Gaba branch indicate that the Sst-Pvalb transcriptomic boundary is not a strict boundary for bistratified types, or does it indicate that the Chamberland Sst::Tac1 label has some contamination from Pvalb-only cells?

---

## References

[1] Chamberland et al. 2024 · PMID:38640347 · DOI:10.1073/pnas.2306382121
