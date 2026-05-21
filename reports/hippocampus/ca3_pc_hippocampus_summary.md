# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report

## Introduction

CA3 pyramidal cells are the principal glutamatergic neurons of hippocampal area CA3, forming the main excitatory relay of the trisynaptic circuit: they receive mossy fiber input from dentate gyrus granule cells and project via Schaffer collaterals to CA1 [3]. Together with CA1 and CA2 pyramidal cells they constitute the glutamatergic backbone of Ammon's horn, and their dense recurrent collateral network is widely thought to underpin pattern completion in hippocampal memory models.

### Classical type table

| Property | Value | References |
|---|---|---|
| Neurotransmitter | Glutamatergic | [3] |
| Soma location | Pyramidal layer of CA3 [UBERON:0014550] | [1], [2] |

<details>
<summary>Per-property source evidence</summary>

- **Neurotransmitter (glutamatergic)** — Dale et al. 2015 [3]:

> There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1). They generally have excitatory effects on the neurons to which they send axon terminals including other glutamatergic and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine (DA)], cholinergic, and histaminergic (HA) cells.
> — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 2281033_5b9805ff -->

- **Soma location (pyramidal layer of CA3 [UBERON:0014550])** — Cembrowski et al. 2016 [1]:

> we used next-generation RNA sequencing (RNA-seq) to produce a quantitative, whole genome characterization of gene expression for the major excitatory neuronal classes of the hippocampus; namely, granule cells and mossy cells of the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
> — Cembrowski et al. 2016, abstract · [1] <!-- quote_key: 4875295_4a456257 -->

- **Soma location (pyramidal layer of CA3 [UBERON:0014550])** — Wheeler et al. 2015 [2]:

> Hippocampome.org is a comprehensive knowledge base of neuron types in the rodent hippocampal formation (dentate gyrus, CA3, CA2, CA1, subiculum, and entorhinal cortex)
> — Wheeler et al. 2015, abstract · [2] <!-- quote_key: 631148_edb9eac6 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer of the Yao 2021 hippocampal formation SMART-Seq v4 dataset (GEO:GSE185862) maps CA3 pyramidal cells with near-perfect fidelity at the subclass level (F1=0.994 to 017 CA3 Glut) and strong but partial coverage at the supertype level, where 0078 CA3 Glut_4 [CS20230722_SUPT_0078] emerges as the dominant correspondent (63.0% of CA3 cells, F1=0.773), consistent with a TYPE_A_SPLITS relationship spanning all five CA3 Glut supertypes.

![Filtered AT figure for CA3 pyramidal cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_ca3_pc_hippocampus.png)

*F1 across taxonomy levels for the CA3 source group relevant to CA3 pyramidal cell. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

### Candidate overview

| WMBv1 target | Accession | Confidence | Relationship | Verdict |
|---|---|---|---|---|
| 0078 CA3 Glut_4 | CS20230722_SUPT_0078 | 🟡 MODERATE | TYPE_A_SPLITS | Best candidate |

### Table 1: Property comparison

| Property | Classical type | WMBv1 (017 CA3 Glut supertype) | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glutamatergic (017 CA3 Glut subclass) | CONSISTENT |
| Soma location | Pyramidal layer of CA3 [UBERON:0014550] | Field CA3, pyramidal layer [MBA:495]: 1,467 cells; Field CA3, stratum oriens [MBA:486]: 1,381 cells; Field CA3, stratum radiatum [MBA:504]: 945 cells; Field CA3, stratum lucidum [MBA:479]: 868 cells; Field CA3, stratum lacunosum-moleculare [MBA:471]: 437 cells | CONSISTENT |

*(note: SUPT_0078 [CS20230722_SUPT_0078] MERFISH distribution is exclusively within CA3 strata. Pyramidal layer [MBA:495] (1,467 cells) and stratum oriens [MBA:486] (1,381 cells) are the dominant compartments; the stratum oriens representation adjacent to stratum pyramidale is expected for MERFISH soma assignment of large CA3 PC bodies. No artefactual off-target regions appear, in contrast with the earlier candidate SUPT_0075 which showed lateral ventricle and alveus entries.)*

### Table 2: Evidence support

| Evidence type | Supports | Summary |
|---|---|---|
| ATLAS_METADATA | SUPPORT | SUPT_0078 [CS20230722_SUPT_0078] belongs to the dedicated CA3 glutamatergic subclass (017 CA3 Glut). MERFISH anatomy is entirely within CA3 strata with no hilar representation. Atlas defining markers are Homer3 and Cldn22. |
| ANNOTATION_TRANSFER | SUPPORT | Yao 2021 (GEO:GSE185862) CA3 cells (n=322): 63.0% map to SUPT_0078 at supertype level; F1=0.773; target_purity=1.0. F1=0.994 at subclass level (017 CA3 Glut). |

---

### 0078 CA3 Glut_4 · 🟡 MODERATE

**0078 CA3 Glut_4** [CS20230722_SUPT_0078] is the leading WMBv1 supertype correspondence for the CA3 pyramidal cell, supported by both atlas anatomical metadata and direct annotation transfer evidence.

- **ATLAS_METADATA (SUPPORT):** SUPT_0078 [CS20230722_SUPT_0078] belongs to WMBv1 subclass 017 CA3 Glut, the dedicated CA3 glutamatergic subclass containing five supertypes (SUPT_0075–0079). MERFISH spatial data places SUPT_0078 cells exclusively within CA3 strata: pyramidal layer [MBA:495] (1,467 cells), stratum oriens [MBA:486] (1,381 cells), stratum radiatum [MBA:504] (945 cells), stratum lucidum [MBA:479] (868 cells), and stratum lacunosum-moleculare [MBA:471] (437 cells). The complete absence of hilar representation distinguishes SUPT_0078 from potential mossy cell contamination and from the earlier candidate SUPT_0075, which received only 16.8% of Yao 2021 CA3 cells (F1=0.288) and showed artefactual lateral ventricle and alveus entries. Atlas defining markers for SUPT_0078 are Homer3 and Cldn22.

- **ANNOTATION_TRANSFER (SUPPORT):** MapMyCells local transfer of 322 CA3-labelled cells from Yao 2021 (GEO:GSE185862) SSv4 hippocampus data onto WMBv1 (CCN20230722). SUPT_0078 [CS20230722_SUPT_0078] received 203 cells (63.0%) at the supertype level with F1=0.773 (group_purity=0.630, target_purity=1.0). The target_purity of 1.0 means that every cell assigned to SUPT_0078 came from the CA3 source label — a particularly clean result. At the subclass level, 017 CA3 Glut captures 99.4% of CA3 cells with F1=0.994. The remaining 34.8% of CA3 cells at the supertype level distribute across SUPT_0075 (16.8%), SUPT_0077 (11.5%), SUPT_0076 (6.5%), and SUPT_0079 (1.6%), consistent with a TYPE_A_SPLITS relationship in which the classical CA3 pyramidal cell spans all five CA3 Glut supertypes, with SUPT_0078 as the dominant correspondence.

- **Marker evidence:** Atlas defining markers (Homer3, Cldn22) derive from WMBv1 ATLAS_METADATA. No classical-side defining markers are documented in the current KB node; direct cross-validation against published CA3 PC marker literature is therefore NOT_ASSESSED for this edge.

- **Concerns:** The TYPE_A_SPLITS relationship is an important caveat: 34.8% of Yao 2021 CA3 cells map to supertypes other than SUPT_0078 within the same CA3 Glut subclass. Whether these splits reflect CA3 sublayer identity (CA3a/b/c), proximity to mossy fibre input zones, or other transcriptional axes is unresolved. An earlier interpretation tentatively attributed SUPT_0078–0079 to mossy cell populations; MERFISH anatomy for SUPT_0078 (zero hilar cells, exclusively CA3 strata) does not support that interpretation.

- **What would upgrade confidence to HIGH:** A sublayer-resolved annotation transfer (source dataset with CA3a/b/c labels) mapping onto SUPT_0075–0079 would clarify whether SUPT_0078 represents a specific CA3 sublayer population or a generic molecular state distributed across sublayers. Addition of classical defining markers and literature confirmation of Homer3/Cldn22 expression in CA3 stratum pyramidale would further strengthen the property alignment.

---

## Methods

<details>
<summary>Methods detail</summary>

#### Classical type definition

The CA3 pyramidal cell is defined on a CLASSICAL_MULTIMODAL basis. Neurotransmitter identity (glutamatergic) follows Dale et al. 2015 [3]. Soma location in the pyramidal layer of CA3 [UBERON:0014550] is established by Cembrowski et al. 2016 [1] and Wheeler et al. 2015 (Hippocampome.org) [2]. No defining transcriptomic markers, negative markers, or neuropeptides are currently documented on this classical node.

#### Atlas mapping query

Candidate atlas clusters were retrieved from WMBv1 (CCN20230722) at ranks 0 and 1 using metadata-based scoring.

#### Property alignment

Each defining property was compared via the property_comparisons schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

#### Annotation transfer

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4; source cluster label: CA3) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations). Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. Inputs and intermediate outputs live under research/hippocampus/glutamatergic/annotation_transfer/GSE185862_SSv4/. |
| Tool version | cell_type_mapper |
| n cells | 6398 |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

#### Anti-hallucination

All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source evidence_items[*].explanation fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

#### Evidence base

| Evidence type | Count |
|---|---|
| ATLAS_METADATA | 1 |
| ANNOTATION_TRANSFER | 1 |

*Report generated 2026-05-19T10:45:50+00:00. Framework commit: 07c6dbd. KB graph: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

</details>

---

## Discussion

**Primary mapping:** 0078 CA3 Glut_4 [CS20230722_SUPT_0078] is the dominant WMBv1 representative of the classical CA3 pyramidal cell at MODERATE confidence under a TYPE_A_SPLITS relationship. The mapping rests on two converging evidence streams: exclusive MERFISH placement within CA3 strata (pyramidal layer [MBA:495]: 1,467 cells; no hilar cells) and annotation transfer F1=0.773 with target_purity=1.0 from Yao 2021 CA3 cells. The subclass-level mapping to 017 CA3 Glut is near-perfect (F1=0.994), confirming that essentially all CA3 pyramidal cells resolve unambiguously to the CA3 glutamatergic subclass in WMBv1. The MODERATE rating reflects the TYPE_A_SPLITS structure: 34.8% of CA3 cells distribute across the other four CA3 Glut supertypes (SUPT_0075–0077, 0079), whose sublayer identities remain unresolved. No CL term is currently assigned; a new-term request is warranted given the absence of an existing CL class for the CA3 pyramidal cell.

**Proposed experiments:**

- *Sublayer-resolved annotation transfer:* Run annotation transfer from a CA3 sublayer-resolved dataset (with CA3a/b/c source annotations) to map sublayer correspondence among SUPT_0075–0079 and clarify whether SUPT_0078 represents a specific CA3 sublayer population or the dominant molecular state of CA3 pyramidal cells broadly.

*(note: CA3a/b/c sublayers differ in recurrent collateral density, dendritic morphology, and connectivity with CA1; a sublayer-resolved source dataset would be the most direct route to disentangling CA3 Glut supertype identity.)*

- *Marker validation:* Add molecular markers to the classical CA3 pyramidal cell node via targeted literature search for Homer3 and Cldn22 expression in CA3 stratum pyramidale, to cross-check whether SUPT_0078 defining markers are genuinely CA3 PC-specific.

**Open questions:**

1. Do SUPT_0075, 0076, 0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to other organisational principles (e.g. proximal vs. distal mossy fiber input zone)?

---

## References

[1] Cembrowski et al. 2016 · PMID:27113915

[2] Wheeler et al. 2015 · PMID:26402459

[3] Dale et al. 2015 · PMID:26346726
