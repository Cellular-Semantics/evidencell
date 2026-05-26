# Ivy cell (IvC) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Ivy cells are nNOS-expressing GABAergic interneurons of the hippocampal CA1
field, with somata canonically located in or adjacent to stratum pyramidale
and an extensive fine axonal cloud that spreads across multiple hippocampal
layers. They are among the most numerically abundant CA1 interneuron types [1].
Ivy cells share remarkable developmental, electrophysiological, morphological,
and neurochemical overlap with nNOS+ neurogliaform cells (NGFC.M), to the
point that Tricoire et al. 2010 argued these two morphological classes may
constitute a single interneuron subtype distinguished only by laminar soma
position [2].

> "This mouse line allows for a large sampling from diverse interneuron subtypes in the CA1 pyramidal layer, including the most representative ones (Bezaire et al., 2013), the PV-expressing basket and bistratified cells (Klausberger et al., 2008), the NOS- expressing ivy cells (14381729) and two types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin (Klausberger et al., 2008)(Topolnik et al., 2022)"
> — Bocchio et al. 2024, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 262127573_d140faf4 -->

> "IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR."
> — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [2] <!-- quote_key: 2405079_6850b924 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1] |
| NT | GABAergic | — |
| Markers | Nos1, Npy, Lamp5 | Nos1: [2][1][3][4][5]; Npy: [2] |
| Negative markers | Pvalb, Sst, Calb2 | [2] |
| Neuropeptides | Npy | [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 pyramidal layer (stratum pyramidale) as the canonical
  soma position for Ivy cells · [1]

- **Nos1 / Npy markers and negative-marker profile:** characterisation of IvC
  shared neurochemical profile with NGCs · [2]

- **Ivy cell as most representative CA1 interneuron type:** [3]

</details>

Cell Ontology mapping: No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One MODERATE candidate atlas supertype was assessed. 0203 Lamp5 Lhx6 Gaba_1
[CS20230722_SUPT_0203] is the primary mapping at MODERATE confidence, supported
by two independent annotation-transfer runs (Yao 2021 Lamp5 and Harris 2018
Cacna2d1.Lhx6.Reln) and a confirmed Lamp5/Lhx6/Nos1/Npy marker profile by
precomputed expression statistics. The main caveat is a soma-location discrepancy:
no CA1 stratum pyramidale cells are present in the atlas supertype anatomy.

**Annotation-transfer overview figures (run-level, filtered)**

![Filtered AT figure for Ivy cell — Yao 2021 (GSE185862) Lamp5](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_ivy_cell_hippocampus.png)

*F1 across taxonomy levels for the Lamp5 source group from Yao 2021 (GEO:GSE185862). The overwhelmingly dominant hit at both subclass and supertype levels (F1=0.898) confirms Lamp5 Lhx6 identity for the predominant hippocampal Lamp5+ population, which Ivy cells are expected to comprise.*

![Filtered AT figure for Ivy cell — Harris 2018 (GSE99888) Cacna2d1.Lhx6.Reln](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/figures/f1_for_ivy_cell_hippocampus.png)

*F1 across taxonomy levels for the Cacna2d1.Lhx6.Reln source group (Harris 2018 published Class label for a Lamp5+/Lhx6+/Reln+ CA1 inhibitory cluster; n=246 cells mapped). Independent two-dataset corroboration of the Lamp5+/Lhx6+ identity, with supertype F1=0.812.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|-:|----|---|---|
| 1 | — | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | 3,301 | 🟡 MODERATE | Lamp5/Nos1/Npy CONSISTENT · location DISCORDANT | Best candidate |

Total: 1 edge (MODERATE); relationship type: PARTIAL_OVERLAP.

### Primary candidate property alignment — 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | — | CONSISTENT |
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | DG mol layer (263), CA3 SO (179), CA3 SR (235) — no CA1 SP | — | DISCORDANT |
| Lamp5 expression | defining marker | Lamp5 — DEFINING_SCOPED; precomputed mean 4.40 | — | CONSISTENT |
| Nos1 expression | defining marker (IHC + transcript) | not listed; precomputed mean 7.79 | — | CONSISTENT |
| Npy expression | defining marker (IHC) | not listed; precomputed mean 4.62 | — | CONSISTENT |
| Npy neuropeptide | present | precomputed mean 4.62 | — | CONSISTENT |
| Sst (negative) | negative marker | not listed; precomputed mean 1.52 | — | CONSISTENT |
| Pvalb (negative) | negative marker | not listed; precomputed mean 0.43 | — | CONSISTENT |
| Calb2 (negative) | negative marker | precomputed mean 0.37 | — | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: Lamp5, Lhx6 DEFINING_SCOPED | ATLAS_METADATA | PARTIAL | Lamp5 Lhx6 MGE marker match; no CA1 SP cells | atlas-internal |
| Precomputed stats: all markers confirmed | ATLAS_METADATA | SUPPORT | Nos1=7.79, Npy=4.62, Lamp5=4.40; Pvalb=0.43, Sst=1.52, Calb2=0.37 | atlas-internal |
| Yao 2021 SSv4 Lamp5 → SUPT_0203 | ANNOTATION_TRANSFER | SUPPORT | F1=0.898 (711/868 cells); target_purity=0.989 | GEO:GSE185862 |
| Harris 2018 Cacna2d1.Lhx6.Reln → SUPT_0203 | ANNOTATION_TRANSFER | SUPPORT | F1=0.812 (246 cells); group_purity=0.914 | GEO:GSE99888 |

*(Cluster-level resolution not assessed — see proposed experiments.)*

### 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🟡 MODERATE

**Supporting evidence**

- Atlas metadata: Lamp5 and Lhx6 are listed as DEFINING_SCOPED markers of 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203], consistent with the Ivy cell profile (Lamp5+/Lhx6+ MGE-derived GABAergic interneuron). Atlas precomputed expression confirms all three defining markers (Nos1=7.79, Npy=4.62, Lamp5=4.40) and all three negative markers absent (Pvalb=0.43, Sst=1.52, Calb2=0.37) — a strong quantitative match for the Ivy cell marker signature.
- Yao 2021 (GEO:GSE185862) SSv4 Lamp5 hippocampal cells (n=868) map overwhelmingly to SUPT_0203 at supertype level (F1=0.898; 711/868 cells; target_purity=0.989), and to the Lamp5 Lhx6 Gaba subclass at subclass level (F1=0.898). Ivy cells are the predominant Lamp5+/Lhx6+ hippocampal interneuron type, making this a specific hit.
- Harris 2018 (GEO:GSE99888) Class Cacna2d1.Lhx6.Reln (Lamp5+/Lhx6+/Reln+ CA1 inhibitory cluster) maps to the Lamp5 Lhx6 Gaba subclass (F1=0.825, group_purity=0.935) and SUPT_0203 at supertype level (F1=0.812, 246 cells) — independent second-dataset corroboration from an unbiased CA1 interneuron dataset.

**Marker evidence provenance**

- **Nos1 (defining):** primary transcript- and protein-level support from Tricoire et al. 2010 [2], with additional support from Bocchio et al. 2024 [1], Tzilivaki et al. 2023 [3], Kim et al. 2025 [4], and Wierenga et al. 2010 [5]. Atlas precomputed mean Nos1=7.79 is high and consistent. Although Nos1 is not a named defining marker of SUPT_0203 in the atlas marker list, the high precomputed value strongly suggests nNOS+ identity consistent with the NGFC.M/Ivy cell lineage.
- **Npy (defining + neuropeptide):** classical IHC and transcript support from Tricoire et al. 2010 [2] [4]. Atlas precomputed mean Npy=4.62 confirms. Wierenga et al. 2010 [5] groups Ivy cells and NGCs together as NPY-positive multipolar cells — some cell-type specificity caveat applies.
- **Lamp5 (defining):** no specific dedicated Lamp5/Ivy citation in the current reference set; supported here by the DEFINING_SCOPED atlas annotation and precomputed mean 4.40, plus Tzilivaki et al. 2023 [3] placing Ivy cells in the Lamp5 interneuron class.
- **Negative markers (Pvalb, Sst, Calb2):** Tricoire et al. 2010 [2] confirms PV, SOM, and CR negativity at protein level. Atlas precomputed means (0.43, 1.52, 0.37) are all low — CONSISTENT.

**Concerns**

- **Soma location DISCORDANT:** Classical Ivy cell soma is in or near CA1 stratum pyramidale [UBERON:0014548], but 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] anatomy shows DG molecular layer (263 cells), CA3 stratum oriens (179), and CA3 stratum radiatum (235) with no CA1 stratum pyramidale representation. *(note: CA3 and DG are adjacent hippocampal subfields to CA1 — this is not a distant-region discordance, but the absence of any CA1 SP cells in the supertype is unexpected and could reflect either undersampling of CA1 SP Lamp5/Lhx6 cells in the atlas dataset or a split of the CA1 Ivy population across additional supertypes.)*
- **Shared with nNOS+ NGC:** Ivy cells and nNOS+ NGCs (NGFC.M) share completely overlapping developmental, electrophysiological, morphological, and neurochemical properties (Tricoire et al. 2010 [2]), and both are strong candidates for SUPT_0203. The companion NGC → SUPT_0203 LOW edge may therefore overlap the same atlas population. Current AT evidence cannot discriminate the two morphological classes within this supertype.
- **Cluster-level resolution not assessed:** The mapping is at supertype only; child-cluster breakdown has not been performed.

**What would upgrade confidence**

- Cluster-level (rank 0) annotation-transfer or marker-based child-cluster assessment within 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] to identify whether a CA1 SP Lamp5/Lhx6 child cluster captures hippocampal Ivy cells specifically. Target: F1 ≥ 0.5 at CLUSTER for at least one CA1 SP Nos1+/Lamp5+/Lhx6+ child cluster.
- Spatial validation (MERFISH / ISH) of Nos1+/Lamp5+/Lhx6+ cells in CA1 stratum pyramidale to confirm or refute the absence of CA1 SP Lamp5/Lhx6 cells in the atlas dataset.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Ivy cells (definition_basis: CLASSICAL_MULTIMODAL)
are defined as GABAergic CA1 interneurons with somata in pyramidal layer of CA1
[UBERON:0014548] [1], expressing Nos1 (nNOS), Npy, and Lamp5 [1][2][3][4][5],
and lacking Pvalb, Sst, and Calb2 [2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based
scoring. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property was compared to atlas values with
alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Annotation transfer.**

Run 1 — Yao 2021 (GSE185862) SSv4 Lamp5 → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Lamp5; n=868 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

Run 2 — Harris 2018 (GSE99888) published Class labels → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Cacna2d1.Lhx6.Reln class; n cells from 3663 total) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells total | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| Script (external) | ../at_run_20260506_harris_chamberland_mmc_wmbv1/README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Caveats | Scores Harris 2018 published Class labels against WMBv1; shares MMC output with companion Chamberland-subfamily run. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. The pre-write hook rejects any unresolvable identifier
or unattributed blockquote. Specific mapping limitations and caveats are documented
per-candidate in the Discussion section.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:24+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL; SUPPORT; SUPPORT; SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Ivy cell → 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] at MODERATE confidence. Key support: atlas precomputed-stats marker concordance (Nos1/Npy/Lamp5 high, Pvalb/Sst/Calb2 low) plus two independent annotation-transfer hits (Yao 2021 Lamp5 F1=0.898; Harris 2018 Cacna2d1.Lhx6.Reln F1=0.812 at supertype). Key caveats: soma-location discordance (no CA1 stratum pyramidale in SUPT_0203 anatomy) and likely overlap with the nNOS+ neurogliaform cell (NGFC.M) mapping at the same supertype.

No Cell Ontology term is currently assigned to the Ivy cell. There is no specific CL class for hippocampal Ivy cells, making this a candidate for a CL new term request.

### Proposed experiments and follow-ups

Two independent annotation-transfer runs (Yao 2021 Lamp5 and Harris 2018 Cacna2d1.Lhx6.Reln) have already established the Lamp5/Lhx6 supertype identity at F1 ≈ 0.81–0.90. The remaining gaps are cluster-level resolution within SUPT_0203 and resolution of the Ivy / NGC laminar split.

**Cluster-level resolution**

- Cluster-level annotation transfer or marker-based child-cluster assessment within 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203]. Target: F1 ≥ 0.5 at CLUSTER for at least one CA1 SP Nos1+/Lamp5+/Lhx6+ child cluster. Expected output: AnnotationTransferEvidence at cluster resolution; refined MappingEdge to a specific cluster. Resolves: open questions 1 and 2.

**Spatial validation**

- MERFISH / ISH of Nos1+/Lamp5+/Lhx6+ cells in CA1 stratum pyramidale vs CA3 strata. Target: confirm or refute the absence of CA1 SP Lamp5/Lhx6 cells in the atlas dataset. Expected output: AnatomicalDistributionEvidence; would either upgrade location alignment or confirm a structural gap in the atlas sampling. Resolves: location DISCORDANT caveat.

**Literature**

- Targeted literature search for a primary Lamp5 / Ivy cell citation to close the Lamp5 marker provenance gap. Target: a primary study testing Lamp5 expression in morphology-confirmed Ivy cells.

**CL term request**

- Draft a CL new term request for hippocampal Ivy cell via `workflows/cl-term-request.md`. Target: a dedicated CL term. Expected output: CL term issue; subsequent CL mapping on this node.

### Open questions

1. Are the CA3-enriched Lamp5 Lhx6 cells in 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] Ivy cells, NGCs, or a distinct type?
2. Is there a CA1 SP Lamp5 Lhx6 cluster capturing hippocampal Ivy cells at the cluster level?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | soma location |
| [2] | Tricoire et al. 2010 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544) | Nos1 marker; Npy marker; negative markers |
| [3] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Nos1 marker |
| [4] | Kim et al. 2025 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287) | Nos1 marker |
| [5] | Wierenga et al. 2010 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836) | Nos1 marker |
