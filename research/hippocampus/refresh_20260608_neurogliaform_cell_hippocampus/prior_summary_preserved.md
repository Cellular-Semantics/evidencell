# Neurogliaform cell (NGC) — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | neurogliaform cell (CL:0000693) — EXACT mapping | — |
| Soma location | Stratum lacunosum moleculare [UBERON:0005403] (CA1) | [1] [2] [3] |
| Neurotransmitter | GABAergic | — |
| Defining markers | Nos1, Npy, Lamp5, Id2 | Nos1: [1] [2]; Npy: [1] [4]; Lamp5: [2] [5]; Id2: [2] |
| Negative markers | Pvalb, Sst, Calb2 | — |
| Neuropeptides | Npy | [1] |

> "IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR."
> — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 2405079_6850b924 -->

> "TranscripZonal profiling indicates conserved strong Grin3a expression levels in neocorZcal NGFCs defined by Id2 and Lamp5 expression"
> — Kim et al. 2025, Transcriptomic Interneuron Classifications · [2] <!-- quote_key: 282312227_bb365351 -->

> "Lamp5 interneurons include ivy and neurogliaform cells (NGFCs). The ivy cell is the most common interneuron type in CA1; it has a distinct morphology with a relatively extensive axonal cloud extending over several hippocampal layers and co-expresses neuronal nitric oxide synthase (nNOS)"
> — Tzilivaki et al. 2023, INTERNEURON TYPES AND MICROCIRCUITS · [5] <!-- quote_key: 259953057_9718900f -->

**Notes.** The classical NGC node unifies two developmental lineages — MGE-derived nNOS+ NGCs (NGFC.M: Lhx6+/Lamp5+/Id2+/Nos1+) and CGE-derived nNOS− NGCs (NGFC.C: Lhx6−/Lamp5+/Id2+/Ndnf+). Nos1 as a defining marker reflects the MGE majority; the Lamp5/Id2 signature is shared across both lineages. Each mapping edge below targets one lineage specifically.

---

## Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] (supertype) | — | 🟡 MODERATE | Location CONSISTENT · Ndnf APPROXIMATE · Nos1 DISCORDANT (lineage-specific) | Best candidate (CGE lineage) |
| 2 | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] (supertype) | — | 🔴 LOW | Lamp5 CONSISTENT · Nos1 CONSISTENT · Location DISCORDANT | Speculative (MGE lineage) |

Total: 2 edges · relationship type: PARTIAL_OVERLAP for both.

---

## 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] · 🟡 MODERATE

**Supporting evidence**

- **Location match (CONSISTENT)**: SUPT_0193 has cells in Field CA1 stratum lacunosum-moleculare (MBA:391, 55 cells) and CA3 SLM (MBA:471, 52 cells), directly matching the classical NGC soma location in stratum lacunosum moleculare [UBERON:0005403] [1][2][3].
- **CGE-lineage identity**: Ndnf is a defining marker of SUPT_0193 and is a canonical CGE lineage marker. Classical NGCs include a well-characterised Ndnf+ CGE-derived subpopulation (nNOS− NGCs, NGFC.C: Lhx6−/Lamp5+/Id2+/Ndnf+). Although Ndnf does not appear in the classical `defining_markers` list, its presence at the atlas supertype level is biologically expected for this lineage. *(note: the CGE lineage interpretation is from atlas edge metadata; dedicated hippocampal NGFC.C literature not indexed in this reference set.)*
- **Comprehensive precomputed stats marker match (SUPPORT)**: All four classical defining markers are detected in SUPT_0193 (Nos1 mean=2.26, Npy mean=2.61, Lamp5 mean=3.65, Id2 mean=4.88) and all three negative markers are at low levels (Pvalb mean=0.27, Sst mean=1.51, Calb2 mean=0.31). No defining markers are at zero.
- **Annotation transfer (PARTIAL)**: MapMyCells local annotation transfer of Yao 2021 hippocampal Sncg subclass cells (GEO:GSE185862; n=384 HIP cells) onto WMBv1 shows that at SUBCLASS level, Sncg cells map to subclass RHP-COA Ndnf Gaba (F1=0.759, 219/384 cells). At SUPERTYPE level, SUPT_0193 receives 76 cells (F1=0.340). PARTIAL: the Sncg population is heterogeneous and F1 at SUPERTYPE level is low; the best supertype hit is SUPT_0197 (RHP-COA Ndnf Gaba_5; 82 cells, F1=0.361). The SUBCLASS-level F1 (0.759) is more informative and supports the Ndnf lineage assignment.

**Marker evidence provenance**

- **Nos1** (defining; IHC and transcript): Cited from Tricoire et al. 2010 [1] and Kim et al. 2025 [2]. Nos1 as a defining marker primarily reflects MGE-derived NGCs (NGFC.M, nNOS+). CGE-derived NGCs (NGFC.C, nNOS−) have been described as Nos1-negative. Because SUPT_0193 is a CGE/Ndnf supertype, the Nos1 DISCORDANT alignment is lineage-specific: this edge covers only the CGE NGC subset, where nNOS− identity is expected. Precomputed Nos1 (mean=2.26) is present but low compared with SUPT_0203 (mean=7.79). The DISCORDANT call reflects the lineage split, not a global mismatch.

- **Npy** (defining; IHC): Cited from Tricoire et al. 2010 [1] and Wierenga et al. 2010 [4]. Npy alignment is CONSISTENT (precomputed mean=2.61). Wierenga et al. 2010 [4] established NPY-positive multipolar cells as Ivy cells and neurogliaform cells in hippocampus without separating the two types by morphology — cell-type specificity for NGCs alone is therefore moderate:

> "The labeled cell types correspond well to previously described NPY-positive multipolar cells, often referred to as Ivy cells and neurogliaform cells"
> — Wierenga et al. 2010, Molecular profiles · [4] <!-- quote_key: 8617990_2d09820f -->

- **Lamp5** (defining; transcript): Cited from Kim et al. 2025 [2] and Tzilivaki et al. 2023 [5]. Lamp5 is detected in SUPT_0193 (precomputed mean=3.65) despite not appearing among SUPT_0193's named atlas markers. The NGFC.C annotation (Lhx6−/Lamp5+/Id2+/Ndnf+) predicts Lamp5/Ndnf coexpression. The precomputed value provides direct evidence of transcript presence, reducing the strength of the DISCORDANT call. *(note: the "TranscripZonal" transcription artefact in the Kim et al. 2025 quote is verbatim from the source text — likely a PDF extraction artefact in the ingested corpus.)*

- **Id2** (defining; transcript): Cited from Kim et al. 2025 [2] only. Id2 is detected in SUPT_0193 (precomputed mean=4.88). The single citation from Kim et al. 2025 [2] covers neocortical NGFCs; direct confirmation in hippocampus-specific, morphology-confirmed NGCs would strengthen this marker. *(note: this is a citation coverage gap, not evidence of absence.)*

- **Negative markers (Pvalb, Sst, Calb2)**: No dedicated negative-marker citations on the classical node. Tricoire et al. 2010 [1] confirms PV, SOM, and CR negativity at protein level for the combined NGC/Ivy cell population. Low precomputed stats values (Pvalb=0.27, Sst=1.51, Calb2=0.31) are consistent with negativity.

**Concerns**

- **marker_Nos1 (DISCORDANT)**: Classical node lists Nos1 as a defining marker, but SUPT_0193 is a CGE-lineage (Ndnf+) supertype where nNOS− identity is expected. The discordance is lineage-specific (MGE vs CGE NGC subpopulations) rather than a global mismatch. Precomputed Nos1 (mean=2.26) is low but not zero.
- **marker_Lamp5 (DISCORDANT)**: Lamp5 is listed as a defining marker [2][5] and detected in SUPT_0193 (mean=3.65), yet it is not among SUPT_0193's named atlas markers. The NGFC.C annotation predicts Lamp5/Ndnf coexpression and the precomputed value confirms transcript presence — this discordance is weaker than it appears. *(note: the atlas marker list may not enumerate all genes expressed at defining levels — SUPT_0193's primary defining marker is Ndnf.)*
- **marker_Ndnf (APPROXIMATE)**: Ndnf is the defining atlas marker of SUPT_0193 but is not listed on the classical node. The CGE-derived NGC subpopulation is known to be Ndnf+, but this is not captured in the classical node's `defining_markers`.
- **SUPT_0193 subclass scope**: The RHP-COA Ndnf Gaba subclass spans retrohippocampal and cortical-amygdaloid areas beyond hippocampus proper. The classical NGC node is hippocampus-specific; SUPT_0193 may include neurogliaform-like Ndnf+ cells from non-hippocampal regions.
- **Classical node heterogeneity**: The classical NGC node conflates two developmental lineages. This MODERATE edge covers the CGE lineage only.
- **Annotation transfer F1**: At SUPERTYPE level the F1 for SUPT_0193 is only 0.340; SUPT_0197 actually receives more cells (82 cells, F1=0.361). The SUBCLASS-level F1 (0.759) is more informative.

**What would upgrade confidence**

- **Targeted Ndnf-lineage literature search**: A cite-traverse for "NGFC.C Ndnf nNOS hippocampus" or "CGE neurogliaform Ndnf CA1 SLM" to confirm Nos1 status and Lamp5 coexpression in the CGE NGC subpopulation. This is a literature gap — no new experiments needed to address this.
- **Patch-seq of morphology-confirmed NGCs in SLM**: Direct patch-seq of CA1 SLM cells with confirmed NGC morphology would add LiteratureEvidence or AnnotationTransferEvidence with unambiguous cell-type specificity, resolving the lineage split and placing cells on the WMBv1 taxonomy.
- **Hippocampus-specific annotation transfer**: Running MapMyCells on a hippocampus-enriched dataset of morphology-confirmed NGCs (rather than the broad Sncg subclass) would test whether confirmed hippocampal NGCs map to SUPT_0193 at SUPERTYPE level. Target: F1 ≥ 0.70 at SUPERTYPE.
- **Negative-marker primary citations**: Identifying a primary study that confirmed Calb2−, Pvalb−, and Sst− in morphology-confirmed hippocampal NGCs.

---

## 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🔴 LOW

**Supporting evidence**

- **MGE-lineage marker consistency**: SUPT_0203 is MGE-derived (Lhx6+ DEFINING_SCOPED) and Lamp5+ (DEFINING_SCOPED). Classical NGCs include an MGE-derived subpopulation (NGFC.M: Lhx6+/Lamp5+/Id2+/Nos1+). Marker alignments for Lamp5, Id2, Npy, and all negative markers are CONSISTENT, with precomputed means: Nos1=7.79, Npy=4.62, Lamp5=4.40, Id2=9.35.
- **Strong Nos1 expression**: Precomputed Nos1 mean=7.79 in SUPT_0203 (vs 2.26 in SUPT_0193) is consistent with the MGE-derived nNOS+ NGC identity predicted for NGFC.M. This evidence upgraded this edge from UNCERTAIN.
- **Annotation transfer (PARTIAL, shared with Ivy cell)**: MapMyCells annotation transfer of Yao 2021 SSv4 Lamp5 subclass (GEO:GSE185862; n=868 HIP cells) shows SUPT_0203 is the dominant supertype target (F1=0.898, 711/868 cells; purity=0.989). At SUBCLASS level, 710/868 cells map to subclass Lamp5 Lhx6 Gaba (F1=0.898). This strongly supports the Lamp5 Lhx6 identity but does not discriminate between NGC and Ivy cell (both share SUPT_0203; see edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203).

**Marker evidence provenance**

- **Nos1 (CONSISTENT but absent from atlas marker list)**: Precomputed Nos1 mean=7.79 strongly suggests this is the nNOS+ MGE-derived NGC subtype. Yet Nos1 does not appear among SUPT_0203's named atlas defining markers. This is a data-source discrepancy — Nos1 is high by precomputed stats but absent from the formal atlas marker list. Investigation of the SUPT_0203 marker list against full expression data is recommended.
- **Lamp5 (CONSISTENT)**: Lamp5 is DEFINING_SCOPED in SUPT_0203 and confirmed at mean=4.40. Primary citations from Kim et al. 2025 [2] and Tzilivaki et al. 2023 [5] establish Lamp5 in NGCs.
- **Id2 (CONSISTENT)**: Precomputed mean=9.35 in SUPT_0203 — the highest-expressed defining marker here. Single citation from Kim et al. 2025 [2] covers neocortical data; hippocampus-specificity caveat applies.
- **Npy (CONSISTENT)**: Precomputed mean=4.62 in SUPT_0203. Cited from Tricoire et al. 2010 [1] and Wierenga et al. 2010 [4]. Wierenga 2010 [4] groups Ivy cells and NGCs together — the same cell-type specificity caveat applies.

**Concerns**

- **location_slm (DISCORDANT)**: Classical NGC soma is in stratum lacunosum moleculare [UBERON:0005403]. SUPT_0203 has no CA1 SLM representation — its cells are in DG mol layer (263 cells), CA3 stratum oriens (179 cells), and CA3 stratum radiatum (235 cells). *(note: DG mol layer and CA3 SO/SR are anatomically distant from CA1 SLM as an NGC soma location — this is a strong counter-evidence item, not a registration boundary artefact.)*
- **Shared SUPT_0203 with Ivy cell**: SUPT_0203 is the best atlas candidate for hippocampal Ivy cells (MODERATE confidence). The annotation transfer cannot discriminate between NGC (MGE lineage, SLM) and Ivy cell (MGE lineage, SP/SO) within this supertype.
- **SLM absence**: No CA1 SLM anatomical location in SUPT_0203 significantly weakens this as a hippocampal NGC candidate. If MGE-derived NGCs are genuinely present in CA1 SLM, they may constitute a small cluster not resolved at SUPERTYPE level or may be undersampled in WMBv1.

**What would upgrade confidence**

- **Patch-seq targeting CA1 SLM nNOS+ cells**: Identification and patch-seq of Nos1+ cells specifically in CA1 SLM would test whether any exist and if so whether they map to SUPT_0203 or another supertype. Output: LiteratureEvidence or AnnotationTransferEvidence resolving the SLM location discordance.
- **MERFISH single-cell spatial data**: Spatially resolved transcriptomic data with cell-level resolution in CA1 SLM could confirm or deny the presence of Lamp5+Lhx6+ cells in SLM. Output: AnnotationTransferEvidence with spatial context.
- **Targeted cite-traverse for MGE NGC SLM**: Literature search for "nNOS Lhx6 neurogliaform SLM hippocampus" to determine whether MGE-derived NGCs in CA1 SLM are documented.

---

## Proposed experiments

### Patch-seq of morphology-confirmed hippocampal NGCs

- **What**: Patch-clamp recording + morphological reconstruction + single-cell sequencing (Patch-seq) in CA1 SLM, targeting nNOS+ (SUPT_0203 candidate) and Ndnf+ (SUPT_0193 candidate) cells.
- **Target**: F1 ≥ 0.70 at SUPERTYPE level for hippocampal SLM cells mapping to either SUPT_0193 or SUPT_0203.
- **Expected output**: `AnnotationTransferEvidence` or `LiteratureEvidence` items on both edges.
- **Resolves**: Location DISCORDANT on SUPT_0203; Nos1 DISCORDANT on SUPT_0193; NGC vs Ivy cell discrimination within SUPT_0203.

### Targeted annotation transfer (hippocampal NGC-enriched source)

- **What**: MapMyCells annotation transfer using a source dataset enriched for confirmed hippocampal NGCs (e.g. Ndnf-Cre or nNOS-Cre+ hippocampal cells), mapped to WMBv1.
- **Target**: F1 ≥ 0.70 at SUPERTYPE level on SUPT_0193 or SUPT_0203.
- **Expected output**: `AnnotationTransferEvidence` replacing or supplementing the current Sncg-based and Lamp5-based AT evidence.
- **Resolves**: Low SUPERTYPE F1 on SUPT_0193 (currently 0.340); NGC/Ivy ambiguity on SUPT_0203.

### Targeted literature search (CGE NGC Ndnf lineage)

- **What**: Cite-traverse for "NGFC.C Ndnf nNOS hippocampus" and "CGE neurogliaform Lamp5 CA1".
- **Target**: Primary publications confirming Nos1−, Lamp5+, Ndnf+ phenotype in hippocampal CGE-derived NGCs.
- **Expected output**: `LiteratureEvidence` items on edge `edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193` upgrading Nos1 DISCORDANT and Lamp5 DISCORDANT alignments.
- **Resolves**: Open questions 1 and 3.

---

## Open questions

1. Are CGE-derived hippocampal NGCs uniformly nNOS− (Nos1−) in mouse, or is there a subset that retains Nos1 expression? This determines whether the Nos1 DISCORDANT call on SUPT_0193 is expected or indicates a mismatch.
2. Are MGE-derived nNOS+ NGCs (NGFC.M) present in CA1 SLM in mouse? Their absence from SUPT_0203's anatomical distribution (no CA1 SLM cells) raises the possibility that the MGE NGC subtype resides elsewhere in hippocampus or is underrepresented in WMBv1.
3. Is Lamp5 coexpressed with Ndnf in CGE-derived NGCs in mouse hippocampus? Precomputed stats support it (mean=3.65 in SUPT_0193), but the atlas marker list does not name Lamp5 as a defining marker of SUPT_0193.
4. Can neurogliaform and ivy cells be transcriptomically resolved within SUPT_0203? Both classical types share Lamp5+/Lhx6+/Nos1+/Npy+ identity; annotation transfer cannot currently discriminate them within this supertype.

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ATLAS_METADATA | PARTIAL | Ndnf CGE lineage + SLM location match; Nos1/Lamp5 discordant (lineage-specific) |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ATLAS_METADATA (precomputed stats) | SUPPORT | All 4 markers confirmed; all 3 negative markers absent |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, Sncg subclass, n=384) | PARTIAL | SUBC RHP-COA Ndnf F1=0.759; SUPT_0193 F1=0.340 (76 cells) |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA | PARTIAL | Lamp5 Lhx6 MGE marker match; CA1 SLM absent (DISCORDANT) |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA (precomputed stats) | SUPPORT | Nos1=7.79, Lamp5=4.40, Id2=9.35, Npy=4.62; all markers positive |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, Lamp5 subclass, n=868) | PARTIAL | SUPT_0203 F1=0.898 (711 cells); shared with Ivy cell |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tricoire et al. 2010 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | Soma location; Nos1 marker; Npy marker; neuropeptides |
| [2] | Kim et al. 2025 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | Soma location; Lamp5 marker; Id2 marker |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | Soma location |
| [4] | Wierenga et al. 2010 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Npy marker |
| [5] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Lamp5 marker |
