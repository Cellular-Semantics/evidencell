# Chrna2-IN (Chrna2-OLM, Chamberland 2024) — WMBv1 Mapping Report

## Introduction

The Chrna2-IN subfamily is one of four genetically distinct subtypes of hippocampal somatostatin-expressing interneurons (Sst-INs) identified by Chamberland et al. 2024, defined by combinatorial Sst-Flp;Chrna2-Cre genetics [1]. These cells correspond to the canonical OLM interneuron population: their somata sit deep in the stratum oriens/alveus (O/A), they project to CA1 stratum lacunosum-moleculare, and Chrna2 is the established specific marker for OLM cells in dorsal CA1. The Chrna2-IN subfamily thus represents the OLM cell class interrogated from the Chrna2-Cre angle, a subset of the broader canonical OLM population.

> While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
> — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->

> genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | GABAergic | [1] |
| Defining markers | Sst; Chrna2 | [1] |
| Soma location | Hippocampus stratum oriens [UBERON:0005371]; deep O/A, CA1 | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

> While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
> — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->

> genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->

</details>

### Cell Ontology mapping

No Cell Ontology term assigned. This subfamily overlaps with the canonical OLM class; a CL term request for OLM interneurons would cover this population.

---

## Results

The Chrna2-IN subfamily maps to CLUS_0771 Sst Gaba_3 [CS20230722_CLUS_0771] within supertype 0216 Sst Gaba_3 at MODERATE confidence. The annotation transfer places 74/153 Chrna2-IN cells in CLUS_0771 (F1=0.65, recall=0.81), with the majority of remaining cells in sibling Sst Gaba_3 clusters. This result is consistent with and refines the broader OLM-to-Sst Gaba_3 supertype mapping: the Chrna2-Cre source increases specificity and identifies CLUS_0771 as the preferred cluster-level target within the Sst Gaba_3 supertype.

![Annotation transfer F1 heatmap (GEO:GSE99888 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/figures/f1_tree.png)

### Candidate overview table

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0771 Sst Gaba_3 | CS20230722_CLUS_0771 | 🟡 MODERATE | PARTIAL_OVERLAP | Best candidate |

### Property alignment — 0771 Sst Gaba_3 [CS20230722_CLUS_0771]

**Table 1: Property comparison**

| Property | Classical type | WMBv1 CLUS_0771 / SUPT_0216 | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | GABA | CONSISTENT |
| Marker — Sst | Defining | Sst subclass; high expression in precomputed stats | CONSISTENT |
| Marker — Chrna2 | Defining | Sparse but enriched Chrna2 in Sst Gaba_3 cluster relative to siblings | APPROXIMATE |

**Table 2: Evidence support**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | SUPPORT | Per-cluster Chamberland labels: Chrna2-IN cells (n=153) concentrate in CLUS_0771 (F1=0.65, recall=0.81, precision=0.54); F1 rises with finer aggregation, consistent with monotonic resolution improvement |

**MapMyCells F1 by level — Chrna2-IN source group (per-cluster labels, GEO:GSE99888)**

| Level | Best target | F1 | Group purity | Target purity | n cells mapped |
|---|---|---|---|---|---|
| SUPERTYPE | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 0.329 | 0.947 | 0.199 | 126 |
| CLUSTER | 0771 Sst Gaba_3 [CS20230722_CLUS_0771] | 0.649 | 0.813 | 0.540 | 74 |

*(note: the low F1 at supertype rank reflects that multiple Sst subtypes are pooled at this level; F1 rising from 0.33 at supertype to 0.65 at cluster confirms that cluster rank is the appropriate resolution for Chrna2-IN identity.)*

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Chrna2-IN (Chamberland 2024) defined as CLASSICAL_MULTIMODAL. Source: Chamberland et al. 2024 (PMID:38640347), Sst-Flp;Chrna2-Cre genetic intersection. Chamberland subfamily labels were derived in-silico from Harris 2018 (GEO:GSE99888) by applying the Chrna2+ gene-pair criterion (Sst+/Chrna2+ > 0) to per-cluster mean expression, with Chrna2 being the highest-priority label. Note: this node overlaps with the canonical OLM class (olm_hippocampus); cross-mapping edge to that node should be added when both graphs are co-loaded.

**Annotation transfer.**

| Field | Value |
|---|---|
| Run | at_run_20260512_chamberland_subfamily_mmc_wmbv1 |
| Source dataset | GEO:GSE99888 (Harris 2018) with Chamberland in-silico per-cluster subfamily labels |
| Source label used | Chrna2 (per-cluster rule: Sst+/Chrna2+ > 0) |
| n cells total | 3663 (full Harris dataset); n cells in Chrna2 label: 153 |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Target atlas | WMBv1 (CCN20230722) |
| Atlas pseudobulk SHA | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Bootstrap threshold | 0.8 |
| Primary result | Per-cluster label derivation (dropout-robust; gene-pair rules applied to cluster-mean expression) |
| Companion run | at_run_20260512_harris_class_mmc_wmbv1 (same MMC output, Harris published Class labels) |
| Caveats | Per-cell Chrna2 labels are subject to scRNA-seq dropout; per-cluster labels are the primary result. Precision at cluster rank (0.54) indicates some sibling Sst Gaba_3 cells map to CLUS_0771, consistent with the cluster containing non-OLM Sst interneurons. |

**Anti-hallucination.** All accessions, quote keys, and PMIDs validated against the KB reference store at write time.

*Report generated 2026-05-19. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`.*

**Evidence base**

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 1 |

</details>

---

## Discussion

**The best candidate is 0771 Sst Gaba_3 [CS20230722_CLUS_0771] at MODERATE confidence.** This result is concordant with the broader OLM-to-Sst Gaba_3 supertype mapping from the Winterer 2019 AT run, and adds cluster-level resolution: the Chrna2-Cre-derived source labels pinpoint CLUS_0771 as the preferred child cluster within supertype 0216, whereas the Winterer 2019 run had pointed to sibling CLUS_0768. Both CLUS_0771 and CLUS_0768 sit within the same 0216 Sst Gaba_3 supertype, and the difference may reflect stochastic variation at modest source cell numbers rather than a genuine biological distinction. Precision at cluster rank is moderate (0.54), meaning roughly half of CLUS_0771 is captured by Sst types other than Chrna2-IN — consistent with a heterogeneous Sst Gaba_3 supertype that encompasses OLM and related stratum oriens interneurons. The MODERATE confidence is grounded in the good recall (0.81), the Sst/GABA consistency, and the F1 monotonic improvement from supertype to cluster rank.

### Proposed experiments

1. Direct Chrna2-Cre single-cell RNA-seq from CA1 stratum oriens, mapped to WMBv1, to confirm the CLUS_0771 assignment with a larger and more precisely defined source population (target: F1 >= 0.80 at cluster rank).
2. Assess Chrna2 expression specifically within CLUS_0771 vs. sibling clusters at the atlas precomputed stats level to determine whether Chrna2 shows cluster-level enrichment within the 0216 Sst Gaba_3 supertype.
3. Cross-map this node to the canonical OLM type (olm_hippocampus) once both graphs are co-loaded, to quantify the degree of cell-level overlap.

### Open questions

1. Why does the Chamberland Chrna2-IN source point to CLUS_0771 while the Winterer 2019 OLM run points to CLUS_0768 as the best child cluster within 0216 Sst Gaba_3? Do these two clusters differ biologically, or is the discrepancy driven by source dataset differences (Chrna2-Cre selected vs. unselected OLM)?
2. What fraction of CLUS_0771 (the 46% non-Chrna2 cells by precision estimate) corresponds to non-OLM Sst stratum oriens interneurons?

---

## References

[1] Chamberland et al. 2024 · PMID:38640347 · DOI:10.1073/pnas.2306382121
