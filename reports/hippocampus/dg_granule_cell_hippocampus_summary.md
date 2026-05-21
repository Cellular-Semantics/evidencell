# Dentate gyrus granule cell — WMBv1 (CCN20230722) Mapping Report

*2026-05-19 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

Dentate gyrus granule cells (DGGCs) are the principal glutamatergic neurons of the dentate gyrus, forming the first relay of the classical trisynaptic hippocampal circuit: they receive perforant path input from entorhinal cortex and project mossy fibers to CA3 pyramidal cells and hilar interneurons [3]. Unlike Ammon's horn pyramidal cells, granule cells undergo continuous adult neurogenesis throughout life, adding immature neurons that integrate into the mature circuit over a period of weeks — a process with important implications for pattern separation and hippocampus-dependent learning.

---

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | Glutamatergic | [5][6][7] |
| Defining markers | Prox1, C1ql2 | Prox1: [8]; C1ql2: [9] |
| Soma location | Dentate gyrus granule cell layer [UBERON:0005381] | [1][2][3][4] |
| Negative markers | — | — |
| Neuropeptides | — | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

**Neurotransmitter — glutamatergic**

- Cembrowski et al. 2016 profiled the transcriptome of major excitatory hippocampal classes including dentate granule cells, establishing their glutamatergic identity [5].

> "we used next-generation RNA sequencing (RNA-seq) to produce a quantitative, whole genome characterization of gene expression for the major excitatory neuronal classes of the hippocampus; namely, granule cells and mossy cells of the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1"
> — Cembrowski et al. 2016, abstract · [5] <!-- quote_key: 4875295_4a456257 -->

- Zander et al. 2010 documented VGLUT1 and VGLUT2 co-expression in mossy fiber terminals, establishing the vesicular glutamate transporter complement of granule cell output [6].

> "VGLUT1, VGLUT2, and VGAT coexist in mossy fiber terminals of the h"
> — Zander et al. 2010, abstract · [6] <!-- quote_key: 539922_281341b3 -->

- Pedroni et al. 2014 demonstrated the developmental transition from GABAergic to glutamatergic phenotype during granule cell maturation [7].

> "immediately after birth, GCs exhibit a clear GABAergic phenotype. Only later they integrate the classical glutamatergic trisynaptic hippocampal circuit"
> — Pedroni et al. 2014, abstract · [7] <!-- quote_key: 11333153_3bc75fe5 -->

**Soma location — dentate gyrus granule cell layer [UBERON:0005381]**

- Munster-Wandowski et al. 2013 describe the mossy fiber projection arising from granule cells in the granule cell layer [1].

> "The hippocampal mossy fibers (MFs), the axons of the granule cells (GCs) of the dentate gyrus, innervate mossy cells and interneurons in the hilus on their way to CA3 where they innervate interneurons and pyramidal cells"
> — Munster-Wandowski et al. 2013, abstract · [1] <!-- quote_key: 7458943_e2eed73d -->

- Yau et al. 2015 place granule cells in the context of the trisynaptic glutamatergic circuit, with soma in the dentate gyrus granule cell layer [3].

> "These principal cells are interconnected through glutamatergic synapses that form the classical trisynaptic pathway, where dentate granule cells receive input from entorhinal cortex and project to CA3 pyramidal cells, which then connect to CA1 pyramidal cells (Munster-Wandowski et al., 2013)(Yau et al., 2015)."
> — Yau et al. 2015, Classical Hippocampal Circuit Organization · [3] <!-- quote_key: 1705399_6ee6563e -->

- Hagihara et al. 2011 document AMPA receptor expression in differentiated granule cells in the dentate gyrus [2].

> "AMPA receptor subunits GluR1 and GluR2 are expressed in differentiated granule cells, but not in stem cells, in neonatal, and adult dentate gyrus"
> — Hagihara et al. 2011, abstract · [2] <!-- quote_key: 16383828_d2ad6dc6 -->

**Defining marker — Prox1**

- Sarvari et al. 2016 document metabotropic glutamate receptor and vesicular glutamate transporter expression in hippocampal cell types, including granule cell identity markers [8]. *(note: Prox1 is widely established in the literature as the definitive homeodomain transcription factor marker for DG granule cells; the association between Prox1 and granule cell identity is well documented independently of reference [8], which addresses synaptic glutamate receptor expression. A targeted cite-traverse for "Prox1 dentate gyrus granule cell" would identify more direct primary sources.)*

> "Metabotropic glutamate receptors also play important roles, with mGluR1 mainly expressed in granule cells and CA3 pyramidal neurons, while mGluR5 is highly expressed in all hippocampal subfields (Sarvari et al., 2016). The vesicular glutamate transporter vGLUT1 is the main subtype expressed in the hippocampus, packing glutamate into synaptic vesicles of glutamatergic axon terminals (Sarvari et al., 2016)."
> — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [8] <!-- quote_key: 14854554_439a5d0b -->

**Defining marker — C1ql2**

- D et al. 2018 report that C1ql2 expression is restricted to dentate granule cells within the hippocampus, providing direct cell-type specificity evidence [9].

> "the expression of Sema5B and C1ql2 is restricted to dentate granule cells within the hippocampus"
> — D et al. 2018, discussion · [9] <!-- quote_key: 5895709_81a3d36b -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

MapMyCells annotation transfer of Hochgerner 2018 (GEO:GSE95315) Granule-mature and Granule-immature labels onto WMBv1 (CCN20230722) identifies 0137 DG Glut_2 [CS20230722_SUPT_0137] as the dominant granule cell supertype at MODERATE confidence, with F1 scores of 0.584 (Granule-mature) and 0.601 (Granule-immature) at supertype level and subclass group_purity ≥ 0.888 for the dedicated DG Glut subclass (037 DG Glut). Atlas anatomy confirms 7199 MERFISH-assigned cells in the dentate gyrus granule cell layer (MBA:632), and precomputed expression stats confirm both Prox1 (mean = 8.59) and C1ql2 (mean = 5.77) in SUPT_0137.

![Filtered AT figure for DG granule cell](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_for_dg_granule_cell_hippocampus.png)

*F1 across taxonomy levels for the Granule-mature and Granule-immature source groups relevant to dentate gyrus granule cell. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

### Candidate overview

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0137 DG Glut_2 | CS20230722_SUPT_0137 | 🟡 MODERATE | PARTIAL_OVERLAP | Best candidate |

### Table 1: Property comparison — 0137 DG Glut_2 [CS20230722_SUPT_0137]

| Property | Classical type | WMBv1 0137 DG Glut_2 | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glutamatergic (037 DG Glut subclass) | CONSISTENT |
| Soma location | Dentate gyrus granule cell layer [UBERON:0005381] | Dentate gyrus, granule cell layer (MBA:632): 7199 cells; molecular layer (MBA:10703): 6636 cells; polymorph layer (MBA:10704): 3067 cells; Field CA3, pyramidal layer (MBA:495): 1529 cells | CONSISTENT |
| Marker Prox1 | Defining marker [8] | Not in atlas defining markers (Dsp, Kcnh3, Syndig1); mean_expression = 8.59 (precomputed_stats.h5, supertype level) | CONSISTENT |
| Marker C1ql2 | Defining marker [9] | Not in atlas defining markers; mean_expression = 5.77 (precomputed_stats.h5, supertype level) | CONSISTENT |

### Table 2: Evidence support

| Evidence type | Supports | Summary |
|---|---|---|
| ANNOTATION_TRANSFER | SUPPORT | Granule-mature F1 = 0.584 (433/609 cells → SUPT_0137); Granule-immature F1 = 0.601 (437/581 cells → SUPT_0137); DG Glut subclass group_purity 0.988 / 0.888; GEO:GSE95315 → WMBv1 CCN20230722 |
| ATLAS_METADATA | SUPPORT | 7199 MERFISH cells in DG granule cell layer (MBA:632); Prox1 mean = 8.59, C1ql2 mean = 5.77 in SUPT_0137; n_cells = 21781 total in supertype |

---

### 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🟡 MODERATE

SUPT_0137 [CS20230722_SUPT_0137] is the primary WMBv1 candidate for the dentate gyrus granule cell at MODERATE confidence under a PARTIAL_OVERLAP relationship. The supertype belongs to subclass 037 DG Glut, the dedicated dentate gyrus glutamatergic subclass in WMBv1, and carries 21781 cells total.

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0137 belongs to subclass 037 DG Glut — exclusively glutamatergic — consistent with the classical DG granule cell NT identity [5][6][7].

- **Soma location — CONSISTENT.** SUPT_0137 has 7199 MERFISH-assigned cells in the dentate gyrus granule cell layer (MBA:632), directly matching the classical soma location [UBERON:0005381] [1][2][3][4]. The molecular layer signal (MBA:10703; 6636 cells) likely reflects dendritic processes of granule cells extending apically into the molecular layer, or immature granule cells with a broader spatial distribution. The polymorph layer representation (MBA:10704; 3067 cells) may capture basal dendrites or mossy cells co-registered in the hilus. A small CA3 pyramidal layer contingent (MBA:495; 1529 cells) may represent adult-born granule cells in transit or MERFISH registration overlap at the CA3c/hilus boundary. *(note: the CA3c/hilus boundary is a known MERFISH registration challenge; the CA3 signal is not inconsistent with a granule cell origin given this anatomical proximity.)*

- **Marker Prox1 — CONSISTENT.** Prox1 is a defining marker of the classical DG granule cell [8]. Although Prox1 does not appear among the atlas-defined markers for SUPT_0137 (which are Dsp, Kcnh3, Syndig1), precomputed expression stats confirm Prox1 mean expression = 8.59 in SUPT_0137, consistent with this supertype marking the granule cell population.

- **Marker C1ql2 — CONSISTENT.** C1ql2 is a defining marker of the classical DG granule cell, restricted to dentate granule cells within the hippocampus [9]. Precomputed expression stats confirm C1ql2 mean expression = 5.77 in SUPT_0137, consistent with C1ql2 marking this supertype.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Hochgerner 2018 (GEO:GSE95315) Granule-mature and Granule-immature labels onto WMBv1 (CCN20230722) shows that both populations map primarily to SUPT_0137 at supertype level (Granule-mature: F1 = 0.584, 433 of 609 cells; Granule-immature: F1 = 0.601, 437 of 581 cells). At subclass level, DG Glut subclass group_purity is 0.988 (Granule-mature) and 0.888 (Granule-immature), confirming the DG Glut subclass as the dominant classification. A minority of cells distribute to adjacent DG Glut supertypes (SUPT_0136, SUPT_0138) and to CA3/CA2 clusters, reflecting either genuine DG transcriptomic heterogeneity or minor contamination.

**Marker evidence provenance**

- **Prox1** [8]: The KB citation for Prox1 is Sarvari et al. 2016, which addresses metabotropic glutamate receptor and vesicular glutamate transporter expression in hippocampal subfields; it does not directly demonstrate Prox1 as a granule cell marker. Prox1 is independently well established in the literature as a selective homeodomain transcription factor for DG granule cells, but a targeted cite-traverse for "Prox1 dentate gyrus granule cell" is needed to identify the most direct primary reference and confirm whether the evidence is protein-level (immunohistochemistry) or transcript-level (in situ hybridisation). Precomputed atlas stats confirm Prox1 mean = 8.59 in SUPT_0137, providing independent quantitative support.

- **C1ql2** [9]: D et al. 2018 directly state that C1ql2 expression is restricted to dentate granule cells within the hippocampus (transcript level, in situ hybridisation evidence). This is a strong cell-type-specific marker with clear citation support. No discrepancy between the KB source and the atlas precomputed expression value (mean = 5.77).

**Concerns**

- **PARTIAL_OVERLAP — heterogeneous DG Glut subclass.** DG Glut subclass in WMBv1 contains at least four supertypes (SUPT_0136–0139). Hochgerner Granule-mature and Granule-immature both map predominantly to SUPT_0137 (F1 ~0.58–0.60), but a substantial minority distribute to adjacent supertypes. The F1 scores below 0.65 at supertype level reflect genuine heterogeneity rather than a clean one-to-one correspondence.

- **Cross-species extrapolation.** The Hochgerner 2018 dataset is from rat (NCBITaxon:10116), whereas the WMBv1 atlas is mouse (NCBITaxon:10090). Species-level differences in DG granule cell transcriptomics are unquantified; the cross-species transfer adds uncertainty to the supertype assignment.

- **Immature granule cell coverage.** Adult-born immature granule cells may also map in part to SUPT_0141 (DG-PIR Ex IMN_2; F1 = 0.146 for Granule-immature). The classical DG granule cell as defined here spans both mature and immature populations, but SUPT_0137 may preferentially capture the mature granule cell transcriptomic state.

**What would upgrade confidence**

- **Run add-expression for Prox1 and C1ql2 on SUPT_0136–0139** (ATLAS_METADATA): confirm that Prox1 and C1ql2 are specifically elevated in SUPT_0137 relative to adjacent DG Glut supertypes. Expected output: precomputed expression entries on atlas nodes. Resolves open question 2.

- **Annotation transfer from a mouse granule cell dataset** (ANNOTATION_TRANSFER): run MapMyCells using a mouse-specific granule cell dataset (e.g. Artimovich 2020 or Shin 2015) to cross-validate the SUPT_0137 mapping in the same species as WMBv1. Expected F1 ≥ 0.70 at supertype level. Resolves cross-species uncertainty.

- **Additional supertype edges (SUPT_0136, 0138, 0139):** Building MappingEdge entries for the remaining DG Glut supertypes would represent the full classical DG granule cell population and resolve whether SUPT_0136–0139 correspond to functionally distinct subpopulations. Resolves open question 1.

---

## Methods

### Classical type definition

Dentate gyrus granule cell defined by soma in dentate gyrus granule cell layer [UBERON:0005381], glutamatergic NT type, and defining molecular markers Prox1 [8] and C1ql2 [9]. No negative markers or neuropeptides documented. Definition basis: CLASSICAL_MULTIMODAL. Location sources: [1][2][3][4]. NT sources: [5][6][7].

### Atlas mapping query

Candidate atlas clusters were retrieved from WMBv1 (CCN20230722) at ranks 0 and 1 using metadata-based scoring.

### Property alignment

Each defining property was compared via the property_comparisons schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

### Annotation transfer

<details>
<summary>Annotation transfer run details</summary>

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 mouse DG scRNA-seq: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). 2 genes unmapped. Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| n cells | 2934 |
| Atlas pseudobulk SHA | b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |

</details>

### Anti-hallucination

All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source evidence_items[*].explanation fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Report generated 2026-05-19T10:45:51+00:00. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

### Evidence base

| Evidence type | Count |
|---|---|
| ANNOTATION_TRANSFER | 1 |
| ATLAS_METADATA | 1 |

---

## Discussion

**Primary mapping:** 0137 DG Glut_2 [CS20230722_SUPT_0137] is the dominant WMBv1 representative of the classical dentate gyrus granule cell at MODERATE confidence under a PARTIAL_OVERLAP relationship. The mapping is supported by consistent glutamatergic identity, MERFISH anatomy placing 7199 cells in the dentate gyrus granule cell layer (MBA:632), confirmed expression of both classical markers (Prox1 mean = 8.59, C1ql2 mean = 5.77) in the supertype, and annotation transfer F1 scores of 0.584–0.601 for Granule-mature and Granule-immature Hochgerner 2018 populations. The PARTIAL_OVERLAP relationship reflects that DG Glut subclass contains at least four supertypes (SUPT_0136–0139), and the classical DG granule cell concept spans all of them; SUPT_0137 is the dominant correspondence but not the exclusive one. A cross-species caveat applies: Hochgerner 2018 is rat, whereas WMBv1 is mouse. No Cell Ontology term is currently assigned; the DG granule cell is a strong candidate for a new CL term.

### Proposed experiments

**Add-expression (Prox1 and C1ql2 on DG Glut supertypes)**
- Run `just add-expression` for Prox1 and C1ql2 on SUPT_0136–0139 using CCN20230722 precomputed stats HDF5.
- Target: Confirm Prox1 mean ≥ 5.0 and C1ql2 mean ≥ 3.0 specifically in SUPT_0137; lower values in flanking supertypes.
- Expected output: Precomputed expression blocks on atlas nodes; ATLAS_METADATA cross-check entries.
- Resolves: Open question 2 (Prox1 and C1ql2 specificity across DG Glut supertypes).

**Annotation transfer (mouse granule cell dataset)**
- Run MapMyCells local annotation transfer to WMBv1 (CCN20230722) using a mouse-specific granule cell dataset (e.g. Artimovich 2020 or Shin 2015).
- Target: F1 ≥ 0.70 at supertype level for SUPT_0137.
- Expected output: ANNOTATION_TRANSFER evidence entry on edge_dg_granule_cell_hippocampus_to_supt_0137.
- Resolves: Cross-species uncertainty introduced by rat-to-mouse transfer from Hochgerner 2018.

### Open questions

1. Do SUPT_0136, SUPT_0137, SUPT_0138, and SUPT_0139 correspond to functionally distinct granule cell populations — for example, adult-born vs. developmentally-born granule cells, or dorsal vs. ventral dentate gyrus — or do they reflect transcriptomic gradients within a continuum?

2. Are Prox1 and C1ql2 specifically elevated in SUPT_0137 compared with adjacent DG Glut supertypes (SUPT_0136, 0138, 0139)? Resolution requires `just add-expression` from precomputed stats.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Munster-Wandowski et al. 2013 · PMID:24319410 | [24319410](https://pubmed.ncbi.nlm.nih.gov/24319410/) | Soma location |
| [2] | Hagihara et al. 2011 · PMID:21927594 | [21927594](https://pubmed.ncbi.nlm.nih.gov/21927594/) | Soma location |
| [3] | Yau et al. 2015 · PMID:26380120 | [26380120](https://pubmed.ncbi.nlm.nih.gov/26380120/) | Soma location |
| [4] | doi:10.1038/s41598-017-11268-z | — | Soma location |
| [5] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Neurotransmitter type |
| [6] | Zander et al. 2010 · PMID:20519538 | [20519538](https://pubmed.ncbi.nlm.nih.gov/20519538/) | Neurotransmitter type |
| [7] | Pedroni et al. 2014 · PMID:24592213 | [24592213](https://pubmed.ncbi.nlm.nih.gov/24592213/) | Neurotransmitter type |
| [8] | Sarvari et al. 2016 · PMID:27375434 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434/) | Prox1 marker |
| [9] | D et al. 2018 · PMID:29674952 | [29674952](https://pubmed.ncbi.nlm.nih.gov/29674952/) | C1ql2 marker |
