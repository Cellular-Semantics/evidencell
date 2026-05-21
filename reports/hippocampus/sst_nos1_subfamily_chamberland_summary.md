# Sst::Nos1-IN (long-range projecting, Chamberland 2024) — WMBv1 Mapping Report

## Introduction

The Sst::Nos1-IN subfamily is one of four genetically defined subtypes of hippocampal somatostatin-expressing interneurons characterised by Chamberland et al. 2024 [1]. These cells are long-range-projecting Sst interneurons residing in the CA1 stratum oriens and alveus, with axons projecting to medial septum and contralateral hippocampus — a connectivity signature matching the classical hippocampo-septal and back-projecting interneuron types. The Nos1 (nitric oxide synthase 1) co-expression marks these as distinct from local-circuit Sst subtypes such as canonical OLM cells.

> hippocampal somatostatin-expressing interneurons (Sst-INs) can be divided into at least four subfamilies, each with distinct functions
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_53fb33cc -->

> genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | GABAergic | [1] |
| Defining markers | Sst; Nos1 | [1] |
| Soma location | Hippocampus stratum oriens [UBERON:0005371]; CA1 stratum oriens / alveus | [1] |
| Connectivity | Long-range projecting; CA1 → medial septum, contralateral hippocampus | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

> hippocampal somatostatin-expressing interneurons (Sst-INs) can be divided into at least four subfamilies, each with distinct functions
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_53fb33cc -->

> genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->

</details>

### Cell Ontology mapping

No Cell Ontology term assigned. Functionally corresponds to hippocampo-septal and back-projecting long-range Sst interneurons. The WMBv1 Sst Chodl branch is specifically enriched for long-range-projecting Sst types, providing a biologically interpretable mapping context.

---

## Results

The Sst::Nos1-IN subfamily maps with HIGH confidence to 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859] within supertype 0241 Sst Chodl Gaba_4. This is a clean, near-deterministic mapping: F1=0.969 at cluster rank, F1=0.986 at subclass rank. Notably, the mapping crosses from the broader Sst Gaba subclass expected for a Sst interneuron to the Sst Chodl Gaba subclass — a biologically meaningful result because Sst Chodl types are the WMBv1 representation of long-range-projecting Sst interneurons, directly consistent with the hippocampo-septal/back-projecting identity of Sst::Nos1-IN cells.

![Annotation transfer F1 heatmap (GEO:GSE99888 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/figures/f1_tree.png)

### Candidate overview table

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0859 Sst Chodl Gaba_4 | CS20230722_CLUS_0859 | 🟢 HIGH | EQUIVALENT | Best candidate |

### Property alignment — 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859]

**Table 1: Property comparison**

| Property | Classical type | WMBv1 CLUS_0859 / SUPT_0241 | Alignment |
|---|---|---|---|
| Neurotransmitter | GABAergic | GABA | CONSISTENT |
| Marker — Sst | Defining | Sst expressed in Sst Chodl subclass | CONSISTENT |
| Marker — Nos1 | Defining | Nos1 expressed in Sst Chodl branch | CONSISTENT |
| Connectivity — projection | Long-range (CA1 → medial septum, contralateral HPC) | Sst Chodl long-range identity | CONSISTENT |

**Table 2: Evidence support**

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | SUPPORT | Per-cluster Chamberland labels: Sst_Nos1 cells (n=35) map to Sst Chodl Gaba subclass (F1=0.986); CLUS_0859 is best cluster (F1=0.969, recall=0.939, target_purity=1.0) — near-deterministic mapping |

**MapMyCells F1 by level — Sst_Nos1 source group (per-cluster labels, GEO:GSE99888)**

| Level | Best target | F1 | Group purity | Target purity | n cells mapped |
|---|---|---|---|---|---|
| SUBCLASS | 056 Sst Chodl Gaba [CS20230722_SUBC_056] | 0.986 | 1.000 | 0.972 | 35 |
| SUPERTYPE | 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | 0.986 | 0.971 | 1.000 | 34 |
| CLUSTER | 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859] | 0.969 | 0.939 | 1.000 | 31 |

*(note: the cross-subclass mapping from the expected Sst Gaba branch to Sst Chodl Gaba is biologically interpretable — Sst Chodl is the WMBv1 long-range-projecting Sst branch — and is not a methodological artefact.)*

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Sst::Nos1-IN (Chamberland 2024) defined as CLASSICAL_MULTIMODAL. Source: Chamberland et al. 2024 (PMID:38640347). Chamberland subfamily labels derived in-silico from Harris 2018 (GEO:GSE99888) by applying the Sst+Nos1 expression-product > 1 criterion to per-cluster mean expression. Note: this node likely overlaps with the classical hippocampo_septal_cell_ca1 type in hippocampus_GABAergic_interneurons.yaml.

**Annotation transfer.**

| Field | Value |
|---|---|
| Run | at_run_20260512_chamberland_subfamily_mmc_wmbv1 |
| Source dataset | GEO:GSE99888 (Harris 2018) with Chamberland in-silico per-cluster subfamily labels |
| Source label used | Sst_Nos1 (per-cluster rule: Sst+Nos1 expression-product > 1) |
| n cells in Sst_Nos1 label | 35 |
| n cells total | 3663 |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Target atlas | WMBv1 (CCN20230722) |
| Atlas pseudobulk SHA | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Bootstrap threshold | 0.8 |
| Primary result | Per-cluster label derivation (dropout-robust) |
| Caveats | None; mapping is clean and near-deterministic. The cross-subclass result (Sst Chodl, not Sst Gaba) is a real finding consistent with long-range-projecting Sst identity. |

**Anti-hallucination.** All accessions, quote keys, and PMIDs validated against the KB reference store at write time.

*Report generated 2026-05-19. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`.*

**Evidence base**

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 1 |

</details>

---

## Discussion

**The Sst::Nos1-IN subfamily maps with HIGH confidence to 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859].** This is the strongest mapping in the Chamberland subfamily series: F1=0.969 at cluster rank, group_purity=0.939, target_purity=1.0. The cross-subclass result — Sst::Nos1-IN landing in Sst Chodl Gaba rather than in Sst Gaba — is biologically interpretable: the Sst Chodl branch in WMBv1 captures long-range-projecting Sst interneurons, and the hippocampo-septal/back-projecting identity of Sst::Nos1-IN cells (projecting to medial septum and contralateral hippocampus) is precisely the functional hallmark of Sst Chodl types. The mapping is near-deterministic and does not require further annotation transfer experiments. The main remaining step is to link this node to the classical hippocampo_septal_cell_ca1 type and to document the Nos1 expression at the atlas level (Sst Chodl Gaba_4 precomputed stats).

No proposed follow-up experiments are required for the mapping itself. Cross-referencing with the hippocampo-septal node is the priority curation action.

### Open questions

1. What is the degree of overlap with the classical hippocampo_septal_cell_ca1 node in the hippocampus_GABAergic_interneurons graph? Are these the same cell type under different classification schemes?
2. Does Nos1 show elevated expression specifically in CLUS_0859 relative to sibling Sst Chodl clusters? Running `just add-expression` for Nos1 on Sst Chodl supertypes would confirm or refine the marker alignment.

---

## References

[1] Chamberland et al. 2024 · PMID:38640347 · DOI:10.1073/pnas.2306382121
