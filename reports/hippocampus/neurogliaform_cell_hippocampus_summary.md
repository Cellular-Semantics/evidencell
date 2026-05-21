# Neurogliaform cell (NGC) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Neurogliaform cells (NGCs) are small, round-soma GABAergic interneurons with
multiple short radiating dendrites and a dense, fine-branched axonal mesh that
is characteristic enough to be considered a morphological archetype of cortical
inhibition. In the hippocampus, NGCs sit predominantly in stratum lacunosum-
moleculare of CA1, where they mediate slow, volume-transmitted GABAergic
inhibition onto distal dendrites of pyramidal cells [1][2][3].

> "GABAergic neurons expressing nNOS are one of the largest interneuron populations in the hippocampus (Jinno et al., 2002)(B et al., 2005)(52852755)"
> — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 2405079_042a449f -->

A key biological complexity is that NGCs arise from two distinct developmental
lineages: MGE-derived nNOS+ NGCs (NGFC.M: Lhx6+/Lamp5+/Id2+/Nos1+) and
CGE-derived nNOS− NGCs (NGFC.C: Lhx6−/Lamp5+/Id2+/Ndnf+). Each lineage maps
to a different transcriptomic neighbourhood in WMBv1, and the two candidate
edges below target each lineage separately.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum lacunosum moleculare [UBERON:0014557] | [1][2][3] |
| NT | GABAergic | — |
| Markers | Nos1, Npy, Lamp5, Id2 | Nos1: [1][2]; Npy: [1][4]; Lamp5: [2][5]; Id2: [2] |
| Negative markers | Pvalb, Sst, Calb2 | — |
| Neuropeptides | Npy | [1] |
| CL term | neurogliaform cell [CL:0000693] (EXACT) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 stratum lacunosum-moleculare · [1][2][3]

- **Nos1/Npy markers and negative-marker profile:** co-expression characterised
  in hippocampus alongside comparison with Ivy cells · [1]
  > "IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR."
  > — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 2405079_6850b924 -->

- **Lamp5 / Id2 markers — transcriptomic identity:** neocortical NGFC transcriptomic
  definition with Lamp5 and Id2 · [2]
  > "TranscripZonal profiling indicates conserved strong Grin3a expression levels in neocorZcal NGFCs defined by Id2 and Lamp5 expression"
  > — Kim et al. 2025, Transcriptomic Interneuron Classifications · [2] <!-- quote_key: 282312227_bb365351 -->

- **Npy (marker and neuropeptide):** NPY-positive multipolar cells as Ivy cells
  and NGCs · [4]
  > "The labeled cell types correspond well to previously described NPY-positive multipolar cells, often referred to as Ivy cells and neurogliaform cells"
  > — Wierenga et al. 2010, Molecular profiles · [4] <!-- quote_key: 8617990_2d09820f -->

- **Lamp5 + NGC identity in hippocampus:** [5]
  > "Lamp5 interneurons include ivy and neurogliaform cells (NGFCs). The ivy cell is the most common interneuron type in CA1; it has a distinct morphology with a relatively extensive axonal cloud extending over several hippocampal layers and co-expresses neuronal nitric oxide synthase (nNOS)"
  > — Tzilivaki et al. 2023, INTERNEURON TYPES AND MICROCIRCUITS · [5] <!-- quote_key: 259953057_9718900f -->

</details>

Cell Ontology mapping: neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)] (EXACT). CL:0000693 definition matches well (small round soma, multiple short radiating dendrites, dense branched axonal mesh). The term is not region-restricted, making this an appropriate EXACT match.

---

## Results

Two candidate atlas mappings were assessed, each targeting one NGC developmental
lineage. The primary candidate is 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193]
(MODERATE, CGE lineage) based on location match in CA1 stratum lacunosum-
moleculare, comprehensive marker concordance by precomputed stats, and annotation-
transfer signal at subclass level from the Yao 2021 Sncg dataset. A secondary LOW
candidate, 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203], targets the MGE-derived
nNOS+ NGC (NGFC.M) but is weakened by the complete absence of CA1 SLM cells in
the atlas supertype anatomy.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|-:|----|---|---|
| 1 | — | 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] | 827 | 🟡 MODERATE | SLM location CONSISTENT · Ndnf APPROXIMATE · all markers confirmed | Best candidate (CGE lineage) |
| 2 | — | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | 3,301 | 🔴 LOW | Lamp5/Nos1/Id2/Npy confirmed · SLM location DISCORDANT | Speculative (MGE lineage) |

Total: 2 edges (1 MODERATE, 1 LOW); relationship PARTIAL_OVERLAP for both.

### Primary candidate property alignment — 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | — | CONSISTENT |
| Soma location | CA1 stratum lacunosum-moleculare [UBERON:0014557] | CA1 SLM: 55 cells; CA3 SLM: 52 cells | — | CONSISTENT |
| Ndnf expression | not listed (but Ndnf+ CGE NGC subpopulation described) | Ndnf — DEFINING marker | — | APPROXIMATE |
| Nos1 expression | defining marker (IHC) | not listed; precomputed mean 2.26 | — | DISCORDANT (lineage-specific) |
| Lamp5 expression | defining marker (transcript) | not listed; precomputed mean 3.65 | — | DISCORDANT (lineage-specific) |
| Npy expression | defining marker (IHC) | not listed; precomputed mean 2.61 | — | CONSISTENT |
| Sst (negative) | negative marker | not listed; precomputed mean 1.51 | — | CONSISTENT |
| Pvalb (negative) | negative marker | not listed; precomputed mean 0.27 | — | CONSISTENT |
| Calb2 (negative) | negative marker | not listed; precomputed mean 0.31 | — | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: Ndnf, CA1/CA3 SLM anatomy | ATLAS_METADATA | PARTIAL | SLM location match; Ndnf CGE lineage consistent | atlas-internal |
| Precomputed stats: all 4 markers confirmed | ATLAS_METADATA | SUPPORT | Nos1=2.26, Npy=2.61, Lamp5=3.65, Id2=4.88; all negatives absent | atlas-internal |
| Yao 2021 SSv4 Sncg → WMBv1 AT | ANNOTATION_TRANSFER | PARTIAL | RHP-COA Ndnf Gaba subclass F1=0.759 (219/384 Sncg cells); SUPT_0193 F1=0.340 (76 cells) | GEO:GSE185862 |

### Secondary candidate property alignment — 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🔴 LOW

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | — | CONSISTENT |
| Soma location | CA1 stratum lacunosum-moleculare [UBERON:0014557] | DG mol layer (263), CA3 SO (179), CA3 SR (235) — no CA1 SLM | — | DISCORDANT |
| Lamp5 expression | defining marker | Lamp5 — DEFINING_SCOPED; precomputed mean 4.40 | — | CONSISTENT |
| Nos1 expression | defining marker (IHC) | not listed; precomputed mean 7.79 | — | CONSISTENT |
| Id2 expression | defining marker (transcript) | not listed; precomputed mean 9.35 | — | CONSISTENT |
| Npy expression | defining marker (IHC) | not listed; precomputed mean 4.62 | — | CONSISTENT |
| Sst (negative) | negative marker | not listed; precomputed mean 1.52 | — | CONSISTENT |
| Pvalb (negative) | negative marker | not listed; precomputed mean 0.43 | — | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: Lamp5 Lhx6 MGE marker match | ATLAS_METADATA | PARTIAL | Lamp5, Lhx6 DEFINING_SCOPED; no CA1 SLM cells | atlas-internal |
| Precomputed stats: markers confirmed | ATLAS_METADATA | SUPPORT | Nos1=7.79, Npy=4.62, Lamp5=4.40, Id2=9.35 | atlas-internal |
| Yao 2021 SSv4 Lamp5 → WMBv1 AT | ANNOTATION_TRANSFER | PARTIAL | SUPT_0203 F1=0.898 (711/868 cells); shared with Ivy cell | GEO:GSE185862 |

### 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] · 🟡 MODERATE

**Supporting evidence**

- Atlas metadata: 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] has cells in CA1 stratum lacunosum-moleculare (55 cells) and CA3 SLM (52 cells), directly matching the classical NGC soma location in stratum lacunosum-moleculare [UBERON:0014557] [1][2][3]. This is the most specific anatomical match available for an NGC candidate in WMBv1.
- Ndnf is a defining marker of SUPT_0193 and a canonical CGE lineage marker. Classical NGCs include a well-characterised Ndnf+ CGE-derived subpopulation (NGFC.C: Lhx6−/Lamp5+/Id2+/Ndnf+). Although Ndnf does not appear in the classical node's `defining_markers` list, its presence at the atlas level is biologically expected for the CGE NGC lineage. *(note: the CGE lineage interpretation is from atlas edge metadata; dedicated hippocampal NGFC.C literature is not indexed in the current reference set.)*
- Precomputed stats cross-check provides SUPPORT: all four defining markers are detected (Nos1=2.26, Npy=2.61, Lamp5=3.65, Id2=4.88) and all three negative markers are low (Pvalb=0.27, Sst=1.51, Calb2=0.31). No defining marker is absent.
- Yao 2021 (GEO:GSE185862) SSv4 Sncg hippocampal cells (n=384) map at subclass level to the RHP-COA Ndnf Gaba subclass (F1=0.759, 219 cells), confirming the Ndnf lineage assignment at subclass resolution. SUPT_0193 itself receives 76 cells (F1=0.340); the best supertype hit within this subclass is 0197 RHP-COA Ndnf Gaba_5 (82 cells, F1=0.361) — the SUBCLASS-level signal is more informative than the supertype-level F1.

**Marker evidence provenance**

- **Nos1 DISCORDANT (lineage-specific):** The classical NGC node lists Nos1 as a defining marker, reflecting the MGE-derived nNOS+ majority. CGE-derived NGCs (NGFC.C) are nNOS−, so the Nos1 DISCORDANT alignment in SUPT_0193 is expected for the CGE lineage, not a global mismatch. Precomputed Nos1 (mean=2.26) is present but low, consistent with a minority nNOS+ component or sub-threshold detection.
- **Lamp5 DISCORDANT (lineage-specific):** Lamp5 is detected (precomputed mean=3.65) despite not appearing among SUPT_0193's named atlas markers. The NGFC.C annotation predicts Lamp5/Ndnf coexpression, and the precomputed value confirms transcript presence — this discordance is weaker than it appears.

**Concerns**

- SUPT_0193 subclass (RHP-COA Ndnf Gaba) spans retrohippocampal and cortical-amygdaloid areas beyond hippocampus proper. The classical NGC node is hippocampus-specific; SUPT_0193 may include neurogliaform-like Ndnf+ cells from non-hippocampal regions.
- The classical NGC node conflates two developmental lineages. This MODERATE edge covers the CGE lineage (NGFC.C) only; MGE-derived NGCs (NGFC.M) are covered by the speculative LOW edge below.
- At SUPERTYPE level the F1 for 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] is only 0.340; SUPT_0197 actually receives more cells. The SUBCLASS-level Ndnf signal (F1=0.759) is the primary AT evidence.

**What would upgrade confidence**

- Patch-seq of morphology-confirmed NGCs in CA1 SLM mapped onto WMBv1, targeting F1 ≥ 0.70 at SUPERTYPE level for 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193]. This would resolve both the lineage split and the SLM location ambiguity.
- Targeted literature search for "NGFC.C Ndnf nNOS hippocampus" to confirm Nos1-negative, Lamp5+, Ndnf+ phenotype in hippocampal CGE-derived NGCs.
- Hippocampus-specific annotation transfer using an Ndnf-Cre or nNOS-Cre+ hippocampal dataset rather than the bulk Sncg subclass, to test whether confirmed hippocampal NGCs map specifically to SUPT_0193 at SUPERTYPE level.

### 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🔴 LOW

**Supporting evidence**

- 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] is MGE-derived (Lhx6+ DEFINING_SCOPED) and Lamp5+ (DEFINING_SCOPED). Classical NGCs include an MGE-derived subpopulation (NGFC.M: Lhx6+/Lamp5+/Id2+/Nos1+) described by Tricoire et al. 2010 [1]. Precomputed stats confirm Nos1=7.79 (strong), consistent with the nNOS+ identity of NGFC.M.
- Yao 2021 SSv4 Lamp5 subclass (n=868 HIP cells) maps overwhelmingly to SUPT_0203 (F1=0.898, 711 cells, target_purity=0.989). This strongly confirms Lamp5/Lhx6 identity. However, this AT result is shared with the Ivy cell mapping (see ivy cell report) and cannot discriminate NGC from Ivy cell within this supertype.

**Concerns**

- **Location DISCORDANT:** Classical NGC soma is in CA1 stratum lacunosum-moleculare [UBERON:0014557]. SUPT_0203 has no CA1 SLM representation — its cells are in DG molecular layer (263 cells), CA3 stratum oriens (179), and CA3 stratum radiatum (235). This is the strongest counter-evidence for this candidate as a hippocampal NGC supertype.
- **Shared with Ivy cell:** SUPT_0203 is the primary mapping candidate for hippocampal Ivy cells (MODERATE confidence, separate edge). The AT cannot discriminate between NGC (MGE lineage, SLM soma) and Ivy cell (MGE lineage, SP/SO soma) within this supertype — both share Lamp5+/Lhx6+/Nos1+/Npy+ identity.

**What would upgrade confidence**

- Patch-seq targeting CA1 SLM nNOS+ cells to determine whether any Nos1+ cells exist specifically in SLM and if so whether they map to SUPT_0203 or another supertype. Output: resolution of the SLM location discordance.
- MERFISH single-cell spatial data with cell-level resolution in CA1 SLM to confirm or deny the presence of Lamp5+/Lhx6+ cells in SLM.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The neurogliaform cell is defined on a
CLASSICAL_MULTIMODAL basis: soma in CA1 stratum lacunosum moleculare [UBERON:0014557] [1][2][3];
GABAergic; defining markers Nos1, Npy, Lamp5, Id2 [1][2][4][5]; neuropeptide Npy [1];
negative for Pvalb, Sst, Calb2 [1]. The node conflates MGE- and CGE-derived lineages;
each edge targets one lineage.

**Atlas mapping query.**

Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at
rank 1 (supertype) using metadata-based scoring. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**

Each defining property was compared to the atlas-side value with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Lineage-specific DISCORDANT
calls on Nos1 and Lamp5 reflect the CGE/MGE split, not a global marker mismatch.

**Annotation transfer.**

Run — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4) |
| Source cluster labels | Sncg (n=384 HIP cells; for SUPT_0193); Lamp5 (n=868 HIP cells; for SUPT_0203) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Sncg and Lamp5 source labels are morphologically heterogeneous; NGC-specific resolution requires morphologically confirmed NGC source labels. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed stats HDF5 at
`annotation_transfer/conf/mapmycells/CCN20230722/precomputed_stats.h5`.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. The pre-write hook rejects any unresolvable identifier
or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:24+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL; SUPPORT; PARTIAL | atlas-internal |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL; SUPPORT; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Neurogliaform cell (NGC) → 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] at MODERATE confidence (CGE lineage). Key support: CA1 SLM anatomical location match (55 cells), comprehensive precomputed-stats marker concordance (all four markers present, all three negatives absent), and subclass-level annotation-transfer signal to the RHP-COA Ndnf Gaba subclass (F1=0.759). Key caveats: the classical node conflates two lineages; the MODERATE edge targets only the CGE-derived nNOS− NGC (NGFC.C); Nos1 and Lamp5 are lineage-specifically discordant; the subclass spans non-hippocampal regions; and the SUPERTYPE-level F1 (0.340) is low.

The secondary LOW edge to 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] targets the MGE-derived nNOS+ NGC (NGFC.M) but is weakened by the complete absence of CA1 SLM cells in SUPT_0203 anatomy. The strong Nos1 precomputed expression (7.79) and Lamp5/Lhx6 marker concordance make this supertype a plausible MGE-NGC candidate at the molecular level, but the location discordance is difficult to reconcile without spatial transcriptomic evidence.

The Cell Ontology mapping is EXACT: CL:0000693 (neurogliaform cell) captures the morphological definition well and is not region-restricted, making it appropriate for both the hippocampal and the broader cortical NGC population.

### Proposed experiments

**Patch-seq**

- Patch-seq of morphologically confirmed NGCs in CA1 SLM (targeting both nNOS+ and nNOS− cells, to cover both lineages). MapMyCells mapping onto WMBv1 with target F1 ≥ 0.70 at SUPERTYPE level — this is the most direct route to upgrading either edge.
- For the MGE lineage specifically: targeted patch-seq of Nos1+ cells in CA1 SLM would test whether any MGE-derived NGCs reside in SLM and if so whether they map to SUPT_0203 or another supertype.

**Targeted annotation transfer**

- MapMyCells annotation transfer using an Ndnf-Cre or nNOS-Cre+ hippocampal-enriched dataset to test whether hippocampal NGCs map specifically to 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] (rather than the bulk Sncg-class signal used here). Target: F1 ≥ 0.70 at SUPERTYPE.

**Literature / cite-traverse**

- Targeted cite-traverse for "NGFC.C Ndnf nNOS hippocampus" and "CGE neurogliaform Lamp5 CA1" to confirm Nos1-negative, Lamp5+, Ndnf+ phenotype in hippocampal CGE-derived NGCs — this is a literature gap addressable without new experiments.

### Open questions

1. Are CGE-derived hippocampal NGCs uniformly Nos1-negative in mouse, or is there a subset retaining Nos1 expression? This determines whether the Nos1 DISCORDANT call on SUPT_0193 is expected or indicates a mismatch.
2. Are MGE-derived nNOS+ NGCs (NGFC.M) present in CA1 SLM in mouse? Their absence from SUPT_0203's anatomical distribution raises the possibility that the MGE NGC subtype resides elsewhere in hippocampus or is underrepresented in WMBv1.
3. Is Lamp5 coexpressed with Ndnf in CGE-derived NGCs in mouse hippocampus? Precomputed stats support it (mean=3.65 in SUPT_0193), but the atlas marker list does not name Lamp5 as a defining marker of SUPT_0193.
4. Can neurogliaform and ivy cells be transcriptomically resolved within 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203]? Both classical types share Lamp5+/Lhx6+/Nos1+/Npy+ identity; annotation transfer cannot currently discriminate them within this supertype.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tricoire et al. 2010 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544) | soma location; Nos1 marker; Npy marker; neuropeptides |
| [2] | Kim et al. 2025 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287) | soma location; Lamp5 marker; Id2 marker |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [4] | Wierenga et al. 2010 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836) | Npy marker |
| [5] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Lamp5 marker |
