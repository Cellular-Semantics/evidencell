# Neurogliaform cell (NGC) — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | neurogliaform cell (CL:0000693) | |
| Soma location | stratum lacunosum moleculare [UBERON:0005403] | [1] [2] [3] |
| NT | GABAergic | |
| Markers | Nos1+, Npy+, Lamp5+, Id2+ | [1] [2] [4] [5] |
| Negative markers | Pvalb−, Sst−, Calb2− | |
| Neuropeptides | Npy | [1] |

*Note: the classical NGC node unifies two developmental lineages — MGE-derived nNOS+ NGCs (NGFC.M: Lhx6+/Lamp5+/Id2+/Nos1+) and CGE-derived nNOS− NGCs (NGFC.C: Lhx6−/Lamp5+/Id2+/Ndnf+). Nos1 as a defining marker reflects the MGE majority; the Lamp5/Id2 signature is shared across both lineages. Each mapping edge below targets one lineage specifically.*

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] | — | — | 🟡 MODERATE | Location CONSISTENT · Ndnf APPROXIMATE | Best candidate (CGE lineage) |
| 2 | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | — | — | 🔴 LOW | Lamp5 CONSISTENT · Location DISCORDANT | Speculative (MGE lineage) |

Total: 2 edges. Relationship type: `PARTIAL_OVERLAP` for both.

---

## 0193 RHP-COA Ndnf Gaba_1 · 🟡 MODERATE

**Supporting evidence:**

- **Location match.** SUPT_0193 has cells in Field CA1 stratum lacunosum-moleculare (MBA:391, 55 cells) and CA3 SLM (MBA:471, 52 cells), directly matching the classical NGC soma location in stratum lacunosum moleculare [UBERON:0005403] [1][2][3]. Location comparison is CONSISTENT.
- **CGE-lineage identity.** Ndnf is a defining marker of SUPT_0193 and is a canonical CGE lineage marker. Classical NGCs include a well-characterised Ndnf+ CGE-derived subpopulation (nNOS− NGCs, NGFC.C: Lhx6−/Lamp5+/Id2+/Ndnf+). Although Ndnf does not appear in the classical `defining_markers` list, its presence at the atlas supertype level is biologically expected for this lineage. *(note: the CGE lineage interpretation is from atlas edge metadata; dedicated hippocampal NGFC.C literature not indexed in this reference set.)*
- **Comprehensive precomputed stats marker match.** Cross-check against atlas precomputed expression statistics confirms all four classical defining markers are detected in SUPT_0193 (Nos1 mean=2.26, Npy mean=2.61, Lamp5 mean=3.65, Id2 mean=4.88) and all three negative markers are at low levels (Pvalb mean=0.27, Sst mean=1.51, Calb2 mean=0.31). No defining markers are at zero.
- **Annotation transfer.** MapMyCells local annotation transfer of Yao 2021 hippocampal Sncg subclass cells (GEO:GSE185862; n=384 HIP cells) onto WMBv1 shows that at SUBCLASS level, Sncg cells map to subclass RHP-COA Ndnf Gaba (F1=0.759, 219/384 cells mapped). At SUPERTYPE level SUPT_0193 receives 76 cells (F1=0.340), consistent with Ndnf-expressing neurogliaform cells mapping to this supertype. PARTIAL support: the Sncg population in Yao 2021 is heterogeneous and F1 at SUPERTYPE level is low, indicating the Sncg population distributes across multiple Ndnf supertypes.

**Marker evidence provenance:**

- **Nos1** (defining; IHC and transcript). Nos1 is cited from Tricoire et al. 2010 [1] and Kim et al. 2025 [2]. Both are primary studies in mouse hippocampus. The Tricoire et al. 2010 paper establishes the NGC–Ivy cell distinction and their co-expression of nNOS and NPY:

> "IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR."
> — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 2405079_6850b924 -->

However, Nos1 as a defining marker primarily reflects MGE-derived NGCs (NGFC.M, nNOS+). CGE-derived NGCs (NGFC.C, nNOS−) have been described as Nos1-negative. Because SUPT_0193 is a CGE/Ndnf supertype, the Nos1 DISCORDANT alignment is lineage-specific: this edge covers only the CGE NGC subset, where nNOS− identity is expected. Precomputed Nos1 (mean=2.26) is present but low compared with SUPT_0203 (mean=7.79). A targeted literature search for "NGFC.C Nos1 hippocampus CGE" could confirm whether CGE-derived NGCs in mouse hippocampus are uniformly nNOS−.

- **Npy** (defining; IHC). Cited from Tricoire et al. 2010 [1] and Wierenga et al. 2010 [4]. Npy alignment is CONSISTENT (precomputed mean=2.61 in SUPT_0193). Wierenga et al. 2010 [4] established NPY-positive multipolar cells as Ivy cells and neurogliaform cells in hippocampus without separating the two types by morphology — cell-type specificity for NGCs alone is therefore moderate.

- **Lamp5** (defining; transcript). Cited from Kim et al. 2025 [2] and Tzilivaki et al. 2023 [5]. Kim et al. 2025 identifies Lamp5 as part of a transcriptomic NGC (NGFC) signature:

> "TranscripZonal profiling indicates conserved strong Grin3a expression levels in neocorZcal NGFCs defined by Id2 and Lamp5 expression"
> — Kim et al. 2025, Transcriptomic Interneuron Classifications · [2] <!-- quote_key: 282312227_bb365351 -->

Lamp5 is detected in SUPT_0193 (precomputed mean=3.65) despite not appearing among SUPT_0193's named atlas markers. The DISCORDANT alignment reflects the absence of Lamp5 from the formal atlas marker list; the NGFC.C annotation (Lhx6−/Lamp5+/Id2+/Ndnf+) predicts Lamp5/Ndnf coexpression. The precomputed value (3.65) provides direct evidence of transcript presence, reducing the strength of the DISCORDANT call. *(note: the "TranscripZonal" transcription artefact in the Kim et al. 2025 quote is verbatim from the source text — likely a PDF extraction artefact in the ingested corpus.)*

- **Id2** (defining; transcript). Cited from Kim et al. 2025 [2] only. Id2 is detected in SUPT_0193 (precomputed mean=4.88). The single citation from Kim et al. 2025 [2] covers neocortical NGFCs; direct confirmation in hippocampus-specific, morphology-confirmed NGCs would strengthen this marker's inclusion. *(note: this is a citation coverage gap, not evidence of absence.)*

- **Negative markers (Pvalb, Sst, Calb2).** No dedicated negative-marker citations on the classical node. Pvalb (mean=0.27), Sst (mean=1.51), and Calb2 (mean=0.31) are all low in SUPT_0193. The Tricoire et al. 2010 quote above [1] confirms PV, SOM, and CR negativity at protein level for the combined NGC/Ivy cell population. Low precomputed stats values are consistent with negativity.

**Concerns:**

- **marker_Nos1** (DISCORDANT): Classical node lists Nos1 as a defining marker, but SUPT_0193 is a CGE-lineage (Ndnf+) supertype where nNOS− identity is expected. The discordance is lineage-specific (MGE vs CGE NGC subpopulations) rather than a global mismatch. Precomputed Nos1 (mean=2.26) is low but not zero.
- **marker_Lamp5** (DISCORDANT): Lamp5 is listed as a defining marker of the classical NGC node [2][5] and detected in SUPT_0193 (mean=3.65), yet it is not among SUPT_0193's named atlas markers. This discordance is weaker than it appears: NGFC.C are predicted to be Lamp5+, and the precomputed value confirms transcript presence. *(note: the atlas marker list may not enumerate all genes expressed at defining levels — SUPT_0193's primary defining marker is Ndnf.)*
- **marker_Ndnf** (APPROXIMATE): Ndnf is the defining atlas marker of SUPT_0193 but is not listed on the classical node. Alignment is APPROXIMATE because the CGE-derived NGC subpopulation is known to be Ndnf+, but this is not captured in the classical node's `defining_markers`.
- **SUPT_0193 subclass scope (caveat).** The RHP-COA Ndnf Gaba subclass spans retrohippocampal and cortical-amygdaloid areas beyond hippocampus proper. The classical NGC node is hippocampus-specific; SUPT_0193 may include neurogliaform-like Ndnf+ cells from non-hippocampal regions.
- **Classical node heterogeneity (caveat).** The classical NGC node conflates two developmental lineages (MGE-derived Nos1+ NGCs and CGE-derived Nos1− NGCs). This MODERATE edge covers the CGE lineage only. A comprehensive NGC mapping requires a second edge for the MGE-derived subtype (see LOW edge below).
- **Annotation transfer F1 (concern).** At SUPERTYPE level the best F1 for SUPT_0193 is only 0.340. SUPT_0197 actually receives more cells at SUPERTYPE level (82 cells, F1=0.361). The SUBCLASS-level F1 (0.759) is more informative and supports the Ndnf lineage assignment.

**What would upgrade confidence:**

- **Targeted Ndnf-lineage literature search.** A cite-traverse for "NGFC.C Ndnf nNOS hippocampus" or "CGE neurogliaform Ndnf CA1 SLM" to confirm Nos1 status and Lamp5 coexpression in the CGE NGC subpopulation would upgrade or clarify the DISCORDANT calls on Nos1 and Lamp5. This is a literature gap — no new experiments needed.
- **Patch-seq of morphology-confirmed NGCs in SLM.** Direct patch-seq of CA1 SLM cells with confirmed NGC morphology (long axonal reach across SLM) would add LiteratureEvidence or AnnotationTransferEvidence with unambiguous cell-type specificity, resolving the lineage split and placing cells on the WMBv1 taxonomy.
- **Hippocampus-specific annotation transfer.** Running MapMyCells on a hippocampus-enriched dataset of morphology-confirmed NGCs (rather than the broad Sncg subclass) would test whether confirmed hippocampal NGCs map to SUPT_0193 at SUPERTYPE level (target F1 ≥ 0.70 at SUPERTYPE).
- **Negative-marker primary citations.** Identifying a primary study that confirmed Calb2−, Pvalb−, and Sst− in morphology-confirmed hippocampal NGCs would remove the evidence gap on negative markers.

---

## 0203 Lamp5 Lhx6 Gaba_1 · 🔴 LOW

**Supporting evidence:**

- **MGE-lineage marker consistency.** SUPT_0203 is MGE-derived (Lhx6+ DEFINING_SCOPED) and Lamp5+ (DEFINING_SCOPED). Classical NGCs include an MGE-derived subpopulation (NGFC.M: Lhx6+/Lamp5+/Id2+/Nos1+). Marker alignments for Lamp5, Id2, Npy, and all negative markers are CONSISTENT, with precomputed means: Nos1=7.79, Npy=4.62, Lamp5=4.40, Id2=9.35.
- **Strong Nos1 expression.** Precomputed Nos1 mean=7.79 in SUPT_0203 (vs 2.26 in SUPT_0193) is consistent with the MGE-derived nNOS+ NGC identity predicted for NGFC.M. This upgraded the edge from UNCERTAIN.
- **Annotation transfer (shared with Ivy cell).** MapMyCells annotation transfer of Yao 2021 SSv4 Lamp5 subclass (GEO:GSE185862; n=868 HIP cells) shows SUPT_0203 is the dominant supertype target (F1=0.898, 711/868 cells; target_purity=0.989). At SUBCLASS level, 710/868 cells map to subclass Lamp5 Lhx6 Gaba (F1=0.898). This strongly supports the Lamp5 Lhx6 identity but does not discriminate between NGC and Ivy cell (both share SUPT_0203; see edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203).

**Marker evidence provenance:**

- **Nos1** (CONSISTENT but absent from atlas marker list). Precomputed Nos1 mean=7.79 strongly suggests this is the nNOS+ MGE-derived NGC subtype. Yet Nos1 does not appear among SUPT_0203's named atlas defining markers. The atlas edge notes flag this as unexpected: "Its absence from the atlas supertype defining markers is unexpected and may indicate this supertype does not correspond to the nNOS+ NGC population." This is a data-source discrepancy — Nos1 is high by precomputed stats but absent from the formal atlas marker list. Investigation of the SUPT_0203 marker list against full expression data is recommended.
- **Lamp5** (CONSISTENT). Lamp5 is DEFINING_SCOPED in SUPT_0203 and confirmed at mean=4.40. Primary citations from Kim et al. 2025 [2] and Tzilivaki et al. 2023 [5] establish Lamp5 in NGCs.
- **Id2** (CONSISTENT). Precomputed mean=9.35 in SUPT_0203. Id2 is the highest-expressed defining marker here. Single citation from Kim et al. 2025 [2] covers neocortical data; the same hippocampus-specificity caveat applies.
- **Npy** (CONSISTENT). Precomputed mean=4.62 in SUPT_0203. Cited from Tricoire et al. 2010 [1] and Wierenga et al. 2010 [4]. Wierenga 2010 [4] groups Ivy cells and NGCs together — the same cell-type specificity caveat applies.

**Concerns:**

- **location_slm** (DISCORDANT): Classical NGC soma is in stratum lacunosum moleculare [UBERON:0005403]. SUPT_0203 has no CA1 SLM representation — its cells are in DG mol layer (263 cells), CA3 stratum oriens (179 cells), and CA3 stratum radiatum (235 cells). CA1 SLM is absent. *(note: DG mol layer and CA3 stratum oriens/radiatum are anatomically distant from CA1 SLM as an NGC soma location — this is a strong counter-evidence item, not a registration boundary artefact.)*
- **Shared SUPT_0203 with Ivy cell.** SUPT_0203 is the best atlas candidate for hippocampal Ivy cells (MODERATE confidence). The annotation transfer cannot discriminate between NGC (MGE lineage, SLM) and Ivy cell (MGE lineage, SP/SO) within this supertype. The AT evidence is therefore shared and cannot independently support either edge.
- **SLM absence caveat.** No CA1 SLM anatomical location in SUPT_0203 significantly weakens this as a hippocampal NGC candidate. If MGE-derived NGCs are genuinely present in CA1 SLM, they may constitute a small cluster not resolved at the SUPERTYPE level or may be undersampled in the WMBv1 atlas.

**What would upgrade confidence:**

- **Patch-seq targeting CA1 SLM nNOS+ cells.** Identification and patch-seq of Nos1+ cells specifically in CA1 SLM would test whether any exist and if so whether they map to SUPT_0203 or another supertype. Expected output: LiteratureEvidence or AnnotationTransferEvidence resolving the SLM location discordance.
- **MERFISH single-cell spatial data.** Spatially resolved transcriptomic data with cell-level resolution in CA1 SLM could confirm or deny the presence of Lamp5+Lhx6+ cells in SLM. Expected output: AnnotationTransferEvidence with spatial context.
- **Targeted cite-traverse for MGE NGC SLM.** A literature search for "nNOS Lhx6 neurogliaform SLM hippocampus" could determine whether MGE-derived NGCs in CA1 SLM are documented and whether any transcriptomic data exist for this subpopulation.

---

## Proposed experiments

No `proposed_experiments` fields are populated on either edge. The following are derived from the concerns and open questions above.

### Patch-seq of morphology-confirmed hippocampal NGCs
- **What:** Patch-clamp recording + morphological reconstruction + single-cell sequencing (Patch-seq) in CA1 SLM, targeting nNOS+ (SUPT_0203 candidate) and Ndnf+ (SUPT_0193 candidate) cells.
- **Target:** F1 ≥ 0.70 at SUPERTYPE level for hippocampal SLM cells mapping to either SUPT_0193 or SUPT_0203.
- **Expected output:** AnnotationTransferEvidence or LiteratureEvidence items on both edges.
- **Resolves:** Location DISCORDANT on SUPT_0203; Nos1 DISCORDANT on SUPT_0193; NGC vs Ivy cell discrimination within SUPT_0203.

### Targeted annotation transfer (hippocampal NGC-enriched source)
- **What:** MapMyCells annotation transfer using a source dataset enriched for confirmed hippocampal NGCs (e.g. Ndnf-Cre or nNOS-Cre+ hippocampal cells), mapped to WMBv1.
- **Target:** F1 ≥ 0.70 at SUPERTYPE level on SUPT_0193 or SUPT_0203.
- **Expected output:** AnnotationTransferEvidence replacing or supplementing the current Sncg-based AT evidence.
- **Resolves:** Low SUPERTYPE F1 on SUPT_0193 (currently 0.340); NGC/Ivy ambiguity on SUPT_0203.

### Targeted literature search (CGE NGC Ndnf lineage)
- **What:** Cite-traverse for "NGFC.C Ndnf nNOS hippocampus" and "CGE neurogliaform Lamp5 CA1".
- **Target:** Primary publications confirming Nos1−, Lamp5+, Ndnf+ phenotype in hippocampal CGE-derived NGCs.
- **Expected output:** LiteratureEvidence items on edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 upgrading Nos1 DISCORDANT and Lamp5 DISCORDANT alignments.
- **Resolves:** Open questions 1 and 3.

---

## Open questions

1. Are CGE-derived hippocampal NGCs uniformly nNOS− (Nos1−) in mouse, or is there a subset that retains Nos1 expression? This determines whether the Nos1 DISCORDANT call on SUPT_0193 is expected or indicates a mismatch.
2. Are MGE-derived nNOS+ NGCs (NGFC.M) present in CA1 SLM in mouse? Their absence from SUPT_0203's anatomical distribution (no CA1 SLM cells) raises the possibility that the MGE NGC subtype resides elsewhere in hippocampus or is underrepresented in WMBv1.
3. Is Lamp5 coexpressed with Ndnf in CGE-derived NGCs in mouse hippocampus? Precomputed stats support it (mean=3.65 in SUPT_0193), but the atlas marker list does not name Lamp5 as a defining marker of SUPT_0193.
4. Can neurogliaform and ivy cells be transcriptomically resolved within SUPT_0203? Both classical types share Lamp5+/Lhx6+/Nos1+/Npy+ identity; annotation transfer cannot currently discriminate them within this supertype.

---

## Evidence base

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ATLAS_METADATA | PARTIAL | Ndnf CGE lineage + SLM location match |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ATLAS_METADATA | SUPPORT | Precomputed stats: all markers consistent |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | ANNOTATION_TRANSFER | PARTIAL | Sncg→WMBv1 F1=0.759 (SUBCLASS), F1=0.340 (SUPT_0193) |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA | PARTIAL | Lamp5 Lhx6 MGE marker match; SLM absent |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA | SUPPORT | Precomputed stats: Nos1=7.79, all markers positive |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | ANNOTATION_TRANSFER | PARTIAL | Lamp5→WMBv1 F1=0.898 (SUPT_0203); shared with Ivy cell |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tricoire et al. 2010 · PMID:20147544 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | soma location, Nos1, Npy, neuropeptides |
| [2] | Kim et al. 2025 · PMID:41473287 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | soma location, Lamp5, Id2 |
| [3] | Perez et al. 2020 · PMID:33404500 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [4] | Wierenga et al. 2010 · PMID:21209836 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Npy marker |
| [5] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Lamp5 marker |
