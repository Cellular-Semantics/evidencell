# Neurogliaform cell (NGC) — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | neurogliaform cell (CL:0000693) | |
| Soma location | CA1 stratum lacunosum-moleculare [UBERON:0005403] | [1] [2] [3] |
| NT | GABAergic |  |
| Markers | Nos1+, Npy+, Lamp5+, Id2+ | [1] [2] [4] [5] |
| Negative | Pvalb−, Sst−, Calb2− | |
| Neuropeptides | Npy | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0193 RHP-COA Ndnf Gaba_1 [CS20230722_SUPT_0193] |  | — | 🟡 MODERATE | Best candidate |
| 2 | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## 0193 RHP-COA Ndnf Gaba_1 · 🟡 MODERATE

**Supporting evidence:**

- RHP-COA Ndnf Gaba_1 supertype: Ndnf is a CGE lineage marker. Classical NGCs include an Ndnf+ CGE-derived subpopulation (nNOS- NGCs, described by Tricoire et al. 2011). Supertype has cells in CA1 SLM (55 cells) and CA3 SLM (52 cells) matching NGC soma location in stratum lacunosum-moleculare. Lamp5 is a NGC defining marker and is present as DEFINING_SCOPED in the related SUPT_0203 but not in SUPT_0193; Ndnf is defining here. The Lamp5+/Id2+ profile of CGE-derived NGCs (NGFC.C: Lhx6-/Lamp5+/Id2+/Ndnf+) partially aligns with Ndnf expression here, though the subclass is RHP-COA Ndnf not hippocampus-specific. [Atlas metadata]
- Precomputed stats cross-check: all 4 defining markers confirmed (Nos1=2.26, Npy=2.61, Lamp5=3.65, Id2=4.88) and all 3 negative markers absent (Pvalb=0.27, Sst=1.51, Calb2=0.31). Comprehensive marker match. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Sncg subclass (n=384 HIP cells) onto WMBv1. At SUBCLASS level, Sncg cells map to SUBC_048 (RHP-COA Ndnf Gaba, F1=0.759, 219/384 cells), consistent with Ndnf-expressing neurogliaform cells. At SUPERTYPE level, Sncg cells distribute across multiple Ndnf supertypes; SUPT_0193 (RHP-COA Ndnf Gaba_1) receives 76 cells (F1=0.340). PARTIAL because the Sncg population is heterogeneous and the 'RHP-COA' label in SUPT_0193 suggests enrichment in retrohippocampal and cortical-amygdaloid areas rather than CA1. Hippocampal neurogliaform cells have a Ndnf/Lamp5 Lhx6 transcriptomic profile; SUPT_0203 (via Lamp5 label) may be an equally valid target. [Annotation transfer]

**Concerns:**

- **marker_Ndnf** (APPROXIMATE): A=not listed as classical marker — but Ndnf+ CGE-derived NGC subpopulation reported / B=Ndnf — DEFINING marker of SUPT_0193. Tricoire 2011 identifies Ndnf+ subset as CGE-derived NGCs (NGFC.C). Ndnf is not in classical defining_markers list but is consistent with the known CGE lineage of nNOS- NGCs.

- **marker_Nos1** (DISCORDANT): A=Nos1 (nNOS) — defining marker (IHC, mouse hippocampus) / B=not present in SUPT_0193 markers; precomputed stats mean: 2.26. Classical NGC node uses Nos1 as a defining marker, but this reflects the MGE-derived nNOS+ NGC majority. CGE-derived NGCs (the lineage represented here) are nNOS-. The discordance is lineage-specific, not a global mismatch.

- **marker_Lamp5** (DISCORDANT): A=Lamp5 — defining marker (transcript, hippocampus) / B=not listed in SUPT_0193 markers; precomputed stats mean: 3.65. Lamp5 is listed as DEFINING_SCOPED in SUPT_0203 (MGE Lamp5 Lhx6), not in this Ndnf CGE supertype. However, NGFC.C annotation is Lhx6-/Lamp5+/Id2+/Ndnf+ — Lamp5 and Ndnf coexpression expected in this lineage.

- SUPT_0193 subclass is RHP-COA Ndnf Gaba, which spans retrohippocampal and cortical amygdala regions in addition to hippocampus proper. The classical NGC node is hippocampus-defined; this supertype may include non-hippocampal neurogliaform-like cells.
- The classical NGC node has Nos1 as a defining marker representing the majority MGE-derived NGC population. This edge specifically represents the CGE-derived nNOS- NGC subtype only. The heterogeneous classical node partially overlaps this supertype.

---

## 0203 Lamp5 Lhx6 Gaba_1 · 🔴 LOW

**Supporting evidence:**

- Lamp5 Lhx6 Gaba_1 supertype is MGE-derived (Lhx6+) Lamp5+ GABA interneuron. Classical NGCs include a nNOS+ MGE-derived subpopulation (NGFC.M: Lhx6+/Lamp5+/Id2+) described by Tricoire 2011 and Bhatt et al. 2023. This MGE lineage has Lamp5 as a DEFINING_SCOPED marker and Lhx6 as DEFINING_SCOPED. However the atlas supertype lacks SLM representation (no CA1 SLM cells; DG mol layer 263, CA3 SO 179, CA3 SR 235) — inconsistent with NGC soma position in SLM. This casts doubt on this supertype as an NGC hippocampal candidate. [Atlas metadata]
- Precomputed stats cross-check: all 4 defining markers confirmed at higher levels than SUPT_0193 (Nos1=7.79, Npy=4.62, Lamp5=4.40, Id2=9.35), all 3 negative markers absent. Stronger Nos1 expression suggests MGE-derived nNOS+ NGC subtype identity. Upgraded from UNCERTAIN. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Lamp5 subclass (n=868 HIP cells) onto WMBv1. SUPT_0203 (Lamp5 Lhx6 Gaba_1) is the dominant supertype target (F1=0.898, 711/868 cells). Neurogliaform cells in hippocampus are Lamp5+Lhx6+ (Ndnf+) interneurons; SUPT_0203 being the top Lamp5 target supports this edge. PARTIAL because SUPT_0203 is shared with ivy cells (both are Lamp5 Lhx6+), and the AT cannot discriminate neurogliaform from ivy within the Lamp5 population. See edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 for the same AT result interpreted for ivy cells. [Annotation transfer]

**Concerns:**

- **location_slm** (DISCORDANT): A=CA1 stratum lacunosum-moleculare (UBERON:0005403) — SOMA / B=Dentate gyrus mol layer (263), CA3 SO (179), CA3 SR (235) — no CA1 SLM. Classical NGCs in hippocampus have soma in SLM. This supertype has no CA1 SLM representation. Makes it an unlikely hippocampal NGC candidate.

- No CA1 SLM anatomical location in SUPT_0203. Classical NGC soma is in stratum lacunosum-moleculare. Location mismatch significantly weakens this candidate for hippocampal NGCs.
- This edge represents the MGE-derived (nNOS+, Lhx6+) NGC subtype only. Even within that subset, the SLM location discordance makes this assignment uncertain. Consider Ivy cell (edge 3) as the primary Lamp5 Lhx6 candidate; hippocampal NGC→Lamp5 Lhx6 may require targeted patch-seq to resolve.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | Atlas metadata | PARTIAL |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | Atlas metadata | SUPPORT |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0193 | Annotation transfer | PARTIAL |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | Atlas metadata | PARTIAL |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | Atlas metadata | SUPPORT |
| edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tricoire et al. 2010 · PMID:20147544 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | soma location |
| [2] | Kim et al. 2025 · PMID:41473287 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | soma location |
| [3] | Perez et al. 2020 · PMID:33404500 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [4] | Wierenga et al. 2010 · PMID:21209836 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Npy marker |
| [5] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Lamp5 marker |
