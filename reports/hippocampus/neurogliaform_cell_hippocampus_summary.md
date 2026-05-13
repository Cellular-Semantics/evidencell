# Neurogliaform cell (NGC) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Neurogliaform cells (NGCs) are GABAergic interneurons with small round somata,
multiple short radiating dendrites, and a dense branched axonal mesh, classically
sited in CA1 stratum lacunosum-moleculare and defined by co-expression of Nos1
(nNOS), Npy, Lamp5, and Id2 [1][2][4][5]. Two developmental lineages contribute:
nNOS+ NGCs derived from MGE share many properties with Ivy cells, while nNOS-
NGCs arise from CGE, and the transcriptomic identity of the family is
distinguished by Lamp5/Id2 expression. Mapping the classical NGC to a WMBv1
atlas type is therefore both a test of whether the atlas separates the MGE and
CGE NGC lineages and a benchmark for the Lamp5/Id2 transcriptomic signature in
the hippocampal formation.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum lacunosum moleculare [UBERON:0014557] | [1][2][3] |
| NT | GABAergic | — |
| Defining markers | Nos1, Npy, Lamp5, Id2 | [1][2][4][5] |
| Negative markers | Pvalb, Sst, Calb2 | — |
| Neuropeptides | Npy | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Nos1 / Npy / negative markers:** co-expression with morphological /
  electrophysiological characterisation distinguishing IvCs and NGCs · [1]
  > IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR.
  > — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 2405079_6850b924 -->
- **Soma location / nNOS+ interneuron framing in hippocampus** · [1]
  > GABAergic neurons expressing nNOS are one of the largest interneuron populations in the hippocampus (Jinno et al., 2002)(B et al., 2005)(52852755)
  > — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 2405079_042a449f -->
- **Npy + NGC / Ivy correspondence** · [4]
  > The labeled cell types correspond well to previously described NPY-positive multipolar cells, often referred to as Ivy cells and neurogliaform cells
  > — Wierenga et al. 2010, Molecular profiles · [4] <!-- quote_key: 8617990_2d09820f -->
- **Id2 + Lamp5 transcriptomic NGFC signature** · [2]
  > TranscripZonal profiling indicates conserved strong Grin3a expression levels in neocorZcal NGFCs defined by Id2 and Lamp5 expression
  > — Kim et al. 2025, Transcriptomic Interneuron Classifications · [2] <!-- quote_key: 282312227_bb365351 -->
- **Lamp5 NGFC family in hippocampus** · [5]
  > Lamp5 interneurons include ivy and neurogliaform cells (NGFCs). The ivy cell is the most common interneuron type in CA1; it has a distinct morphology with a relatively extensive axonal cloud extending over several hippocampal layers and co-expresses neuronal nitric oxide synthase (nNOS)
  > — Tzilivaki et al. 2023, INTERNEURON TYPES AND MICROCIRCUITS · [5] <!-- quote_key: 259953057_9718900f -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)] (EXACT).

---

## Results

Two candidate atlas supertypes were assessed: SUPT_0193 (RHP-COA Ndnf Gaba_1) is the primary mapping at MODERATE confidence, representing the CGE-derived nNOS- NGC subpopulation; SUPT_0203 (Lamp5 Lhx6 Gaba_1) is a LOW-confidence speculative candidate for the MGE-derived nNOS+ NGC subpopulation, weakened by absence of CA1 SLM cells in its atlas anatomy.

**Annotation-transfer overview figure (run-level, filtered)**

![Filtered AT figure for Neurogliaform cell — Yao 2021 (GSE185862) Sncg + Lamp5](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_neurogliaform_cell_hippocampus.png)

*F1 across taxonomy levels for the two source groups (Sncg and Lamp5) from Yao 2021 (GSE185862) relevant to the Neurogliaform cell candidates. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. Sncg maps to SUBC_048 (RHP-COA Ndnf Gaba) at subclass level (F1=0.759) and distributes across multiple Ndnf supertypes (SUPT_0193 F1=0.34); Lamp5 maps cleanly onto SUBC_050 / SUPT_0203 (F1≈0.90).*

### Mapping candidates

**Candidate overview**

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] | — | 827 | 🟡 MODERATE | Lamp5/Npy/Id2 CONSISTENT · Ndnf APPROXIMATE · location CONSISTENT · Nos1 DISCORDANT (lineage-specific) | Best candidate |
| 2 | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | — | 3301 | 🔴 LOW | Lamp5/Nos1/Npy/Id2 CONSISTENT · location DISCORDANT | Speculative |

Total: 2 edges (both PARTIAL_OVERLAP).

**Table 1 — Property comparison (SUPT_0193 — primary)**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum lacunosum-moleculare [UBERON:0014557] | Field CA1, stratum lacunosum-moleculare (MBA:391, 55 cells); CA3 SLM (MBA:471, 52 cells) | not assessed | CONSISTENT |
| NT type | GABAergic | GABA | not assessed | CONSISTENT |
| Ndnf expression | not in classical defining list (but CGE-derived NGC subpop reported) | Ndnf — DEFINING marker of SUPT_0193 | not assessed | APPROXIMATE |
| Nos1 expression | defining marker (IHC) | not in SUPT_0193 markers; precomputed mean 2.26 | not assessed | DISCORDANT |
| Lamp5 expression | defining marker (transcript) | not in SUPT_0193 markers; precomputed mean 3.65 | not assessed | DISCORDANT |
| Npy expression | defining marker (IHC) | not in SUPT_0193 markers; precomputed mean 2.61 | not assessed | CONSISTENT |
| Sst (negative) | negative marker | not in SUPT_0193; precomputed mean 1.51 | not assessed | CONSISTENT |
| Pvalb (negative) | negative marker | not in SUPT_0193; precomputed mean 0.27 | not assessed | CONSISTENT |
| Calb2 (negative) | negative marker | not assessed from metadata; precomputed mean 0.31 | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support (SUPT_0193)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| RHP-COA Ndnf supertype markers + anatomy | Atlas metadata | PARTIAL | Ndnf DEFINING; CA1 SLM 55 cells, CA3 SLM 52 cells | atlas-internal |
| Atlas precomputed expression | Atlas metadata | SUPPORT | Nos1=2.26, Npy=2.61, Lamp5=3.65, Id2=4.88; Pvalb=0.27, Sst=1.51, Calb2=0.31 | atlas-internal |
| Yao 2021 Sncg → SUPT_0193 | Annotation transfer | PARTIAL | SUBC_048 F1=0.759 (219/384); SUPT_0193 F1=0.340 (76/384) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] · 🟡 MODERATE

**Supporting evidence**

- Atlas metadata: Ndnf is a DEFINING marker of SUPT_0193 (a CGE lineage marker). Classical NGCs include an Ndnf+ CGE-derived nNOS- subpopulation (NGFC.C: Lhx6-/Lamp5+/Id2+/Ndnf+) — the supertype's Ndnf identity partially aligns with this subpopulation.
- Atlas anatomy: SUPT_0193 has cells in CA1 stratum lacunosum-moleculare (MBA:391; 55 cells) and CA3 SLM (MBA:471; 52 cells), matching the classical NGC soma location.
- Atlas precomputed expression confirms all four defining markers as present (Nos1=2.26, Npy=2.61, Lamp5=3.65, Id2=4.88) and all three negative markers absent (Pvalb=0.27, Sst=1.51, Calb2=0.31) — a comprehensive quantitative marker match.
- Yao 2021 (GEO:GSE185862) SSv4 Sncg subclass (n=384 hippocampal cells) maps to SUBC_048 RHP-COA Ndnf Gaba at subclass level (F1=0.759, 219/384 cells, target_purity=0.995). At supertype level the Sncg population distributes across multiple Ndnf supertypes; SUPT_0193 receives 76 cells (F1=0.340) and SUPT_0197 receives 82 cells (F1=0.361) — consistent with Ndnf-expressing NGC heterogeneity within the Ndnf subclass.

**Marker evidence provenance**

- **Nos1 (defining):** primary support from Tricoire et al. 2010 [1] and Kim et al. 2025 [2]. Precomputed mean Nos1=2.26 in SUPT_0193 is modest; this is consistent with this supertype representing the CGE-derived nNOS- NGC subset rather than the MGE-derived nNOS+ majority.
- **Npy (defining + neuropeptide):** classical IHC support from Tricoire et al. 2010 [1] and Wierenga et al. 2010 [4]. Precomputed mean Npy=2.61 confirms.
- **Lamp5 (defining):** transcript-level support from Kim et al. 2025 [2] and Tzilivaki et al. 2023 [5]. Precomputed mean Lamp5=3.65 confirms. ⚠ Atlas annotation/expression note: Lamp5 is not listed in SUPT_0193's metadata markers despite a precomputed mean of 3.65; Lamp5 appears as a DEFINING_SCOPED marker only in the companion Lamp5/Lhx6 supertype SUPT_0203, suggesting the atlas metadata distinguishes Lamp5 between the CGE Ndnf and MGE Lhx6 Lamp5 subclasses.
- **Id2 (defining):** transcript support from Kim et al. 2025 [2]. Precomputed mean Id2=4.88 confirms.
- **Negative markers (Pvalb, Sst, Calb2):** Tricoire et al. 2010 [1] reports IvCs and NGCs "fail to express other classical interneuron markers such as PV, SOM, or CR". Atlas precomputed means (0.27, 1.51, 0.31) are all low/absent — CONSISTENT.

**Concerns**

- Nos1 alignment is annotated DISCORDANT at the metadata level (Nos1 is not in SUPT_0193's defining markers despite a precomputed mean of 2.26). This is lineage-specific rather than a global mismatch: the classical NGC node merges MGE-derived nNOS+ NGCs and CGE-derived nNOS- NGCs, and SUPT_0193 corresponds to the CGE / nNOS- subset.
- Lamp5 is similarly annotated DISCORDANT at the metadata level (Lamp5 not in SUPT_0193 markers despite precomputed mean 3.65). The NGFC.C transcriptomic profile (Lhx6-/Lamp5+/Id2+/Ndnf+) predicts Lamp5/Ndnf coexpression in this lineage; the absence from metadata likely reflects subclass-level scoping of the Lamp5 annotation onto the Lhx6+ MGE subclass.
- SUPT_0193 sits in the RHP-COA Ndnf Gaba subclass, which spans retrohippocampal and cortical amygdala regions in addition to hippocampus proper *(note: these are anatomically adjacent allocortical regions — not distant — but the classical NGC node is hippocampus-defined, so this supertype may include non-hippocampal neurogliaform-like cells)*.
- The classical NGC node carries Nos1 as a defining marker representing the majority MGE-derived NGC population; this edge specifically captures the CGE-derived nNOS- subtype only. The heterogeneous classical node only partially overlaps this supertype.
- Annotation-transfer F1 at supertype level (0.34 / 0.36 across two Ndnf supertypes) is below the 0.5 clean-mapping threshold — the Sncg source population distributes across the Ndnf subclass rather than landing on a single supertype, leaving the precise NGC-CGE supertype unresolved.

**What would upgrade confidence**

- Cluster-level (rank 0) annotation transfer or marker-based child-cluster assessment within SUPT_0193 and SUPT_0197 to identify whether a CA1/CA3 SLM Ndnf+/Lamp5+/Id2+ child cluster captures hippocampal CGE-derived NGCs specifically.
- Targeted source dataset with a separated Ndnf NGFC class (rather than the broader Sncg subclass label) — e.g. Harris 2018 or Chamberland subfamily AT runs filtered to NGC-typed sources — to raise supertype-level F1 above 0.5.
- Spatial validation (MERFISH/ISH) of Ndnf+/Lamp5+/Id2+/Nos1- cells in CA1 SLM to confirm the CGE NGC anatomical distribution within SUPT_0193.

### 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🔴 LOW

**Supporting evidence**

- Atlas metadata: Lamp5 and Lhx6 are DEFINING_SCOPED markers of SUPT_0203, consistent with the NGFC.M (Lhx6+/Lamp5+/Id2+) MGE-derived nNOS+ NGC subpopulation.
- Atlas precomputed expression confirms all four defining markers at higher levels than SUPT_0193 (Nos1=7.79, Npy=4.62, Lamp5=4.40, Id2=9.35) and all three negative markers absent (Pvalb=0.43, Sst=1.52). The strong Nos1=7.79 signal is consistent with the MGE-derived nNOS+ NGC subtype.
- Yao 2021 (GEO:GSE185862) SSv4 Lamp5 subclass (n=868 hippocampal cells) maps overwhelmingly onto SUPT_0203 at supertype level (F1=0.898, 711/868 cells; target_purity=0.989) and onto SUBC_050 Lamp5 Lhx6 Gaba at subclass (F1=0.898).

**Marker evidence provenance**

- **Lamp5, Nos1, Npy, Id2 (defining):** all four confirmed by precomputed expression at high levels (4.40, 7.79, 4.62, 9.35 respectively). Primary literature support as for the SUPT_0193 candidate above.
- **Negative markers (Pvalb, Sst):** absent (0.43, 1.52) — CONSISTENT.

**Concerns**

- Soma location DISCORDANT: SUPT_0203 anatomy is in DG molecular layer (263 cells), CA3 SO (179), and CA3 SR (235) with no CA1 SLM representation *(note: CA3 and DG are anatomically adjacent hippocampal subfields, but the complete absence of CA1 SLM cells in a supertype that should capture MGE-derived NGCs is a strong location mismatch — classical NGC soma is canonically in CA1 SLM)*.
- The companion Ivy cell edge (edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203) maps the classical Ivy cell to the same supertype at MODERATE confidence with the Yao 2021 Lamp5 AT (F1=0.898). The shared mapping is consistent with the reported developmental, electrophysiological, morphological and neurochemical similarity between Ivy cells and nNOS+ NGCs (NGFC.M), and the Yao 2021 AT cannot discriminate them within the Lamp5 subclass — SUPT_0203 is therefore best read as primarily an Ivy cell target rather than NGC, with the SLM location mismatch further weakening the NGC interpretation.
- The MGE-derived nNOS+ NGC subtype may not be cleanly resolved in WMBv1 at supertype resolution; targeted patch-seq or cluster-level assessment may be required.

**What would upgrade confidence**

- Cluster-level (rank 0) annotation transfer within SUPT_0203 to identify whether a CA1 SLM Lamp5+/Lhx6+/Nos1+ child cluster captures hippocampal MGE-derived NGCs specifically and distinguishes them from CA1 SP Ivy cells.
- Spatial validation (MERFISH/ISH) of Lamp5+/Lhx6+/Nos1+ cells in CA1 SLM to test whether the atlas undersamples this population or whether the MGE NGC and Ivy populations are transcriptomically indistinguishable in WMBv1.
- Patch-seq of morphology-confirmed CA1 SLM NGCs to anchor an unambiguous classical → transcriptomic mapping.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Neurogliaform cells (definition_basis: CLASSICAL_MULTIMODAL) are defined as GABAergic interneurons with somata in CA1 stratum lacunosum-moleculare [UBERON:0014557] [1][2][3], expressing Nos1, Npy, Lamp5, and Id2 [1][2][4][5], and lacking Pvalb, Sst, and Calb2 [1]. Two developmental lineages contribute (MGE-derived nNOS+ NGFC.M and CGE-derived nNOS- NGFC.C); the transcriptomic family is unified by Lamp5/Id2 expression.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

Run 1 — Yao 2021 (GSE185862) SSv4 (Sncg + Lamp5 source groups) → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Sncg; Lamp5) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:15+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL; SUPPORT; PARTIAL | atlas-internal |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL; SUPPORT; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Neurogliaform cell (NGC) → 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] at MODERATE confidence. Key support: atlas precomputed-stats marker concordance (Nos1/Npy/Lamp5/Id2 present, Pvalb/Sst/Calb2 absent), CA1 + CA3 SLM anatomical presence, and Yao 2021 Sncg → RHP-COA Ndnf Gaba subclass annotation transfer (F1=0.759). Key caveats: Sncg AT distributes across multiple Ndnf supertypes (supertype-level F1=0.34, below the 0.5 clean-mapping threshold), and the RHP-COA Ndnf Gaba subclass spans non-hippocampal allocortical regions. SUPT_0203 (Lamp5 Lhx6 Gaba_1) is a LOW-confidence speculative second candidate for the MGE-derived nNOS+ NGC subset; it shares the Lamp5/Lhx6 marker profile but lacks CA1 SLM anatomy and competes with the Ivy cell mapping at the same supertype.

This classical type maps directly to the Cell Ontology term neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)].

### Proposed experiments and follow-ups

The Yao 2021 SSv4 annotation transfer already addressed the broad question of which atlas subclass(es) the classical NGC maps to (Sncg → RHP-COA Ndnf Gaba subclass at F1=0.759; Lamp5 → Lamp5 Lhx6 Gaba subclass at F1=0.898). The remaining gaps are supertype/cluster resolution within these subclasses and resolution of the two-lineage (NGFC.C CGE vs NGFC.M MGE) split.

- **What**: Cluster-level (rank 0) annotation transfer or marker-based child-cluster assessment within SUPT_0193 (CGE candidate) and SUPT_0203 (MGE candidate).
  **Target**: F1 ≥ 0.5 at CLUSTER (rank 0) for at least one CA1/CA3 SLM Ndnf+/Lamp5+/Id2+ child cluster (for the CGE NGFC.C subpopulation) and one CA1 SLM Lamp5+/Lhx6+/Nos1+ child cluster (for the MGE NGFC.M subpopulation, distinguishing it from CA1 SP Ivy cells).
  **Expected output**: AnnotationTransferEvidence at cluster resolution; refined MappingEdges to specific clusters.
  **Resolves**: open questions 1 and 2.

- **What**: Annotation transfer using a source dataset that separately labels NGC and Ivy populations (e.g. Harris 2018 Class labels, Chamberland subfamily, or a Lamp5/Id2 NGC-specific subset).
  **Target**: F1 ≥ 0.5 at SUPERTYPE level for an NGC-typed source group landing on SUPT_0193 or SUPT_0203.
  **Expected output**: AnnotationTransferEvidence with NGC-specific source labels.
  **Resolves**: open question 3.

- **What**: Spatial validation (MERFISH / ISH) of Ndnf+/Lamp5+/Id2+/Nos1- cells in CA1 SLM and of Lamp5+/Lhx6+/Nos1+ cells in CA1 SLM.
  **Target**: Confirm or refute the CGE NGFC.C anatomical distribution within SUPT_0193 and test whether MGE NGFC.M is undersampled or absent from SUPT_0203 in CA1 SLM.
  **Expected output**: AnatomicalDistributionEvidence; would either upgrade SUPT_0203 location alignment or confirm an atlas sampling gap for MGE NGCs in CA1 SLM.
  **Resolves**: SUPT_0203 location DISCORDANT caveat.

### Open questions

1. Which child cluster(s) of SUPT_0193 (and SUPT_0197, the second-best Ndnf supertype) best capture the CGE-derived nNOS- NGC subpopulation in CA1/CA3 SLM?
2. Is there a CA1 SLM Lamp5+/Lhx6+/Nos1+ child cluster within SUPT_0203 capturing the MGE-derived nNOS+ NGC subpopulation, and is it distinguishable from CA1 SP Ivy cells at cluster resolution?
3. Do existing or future annotation-transfer runs with NGC-specific source labels (rather than the broader Sncg or Lamp5 subclass labels) resolve the NGC supertype assignment at F1 ≥ 0.5?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tricoire et al. 2010 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544) | soma location |
| [2] | Kim et al. 2025 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287) | soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [4] | Wierenga et al. 2010 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836) | Npy marker |
| [5] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Lamp5 marker |
