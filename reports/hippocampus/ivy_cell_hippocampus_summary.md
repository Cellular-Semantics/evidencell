# Ivy cell (IvC) — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA1 stratum pyramidale [UBERON:0005401] | [1] |
| NT | GABAergic |  |
| Markers | Nos1+, Npy+, Lamp5+ | [2] [1] [3] [4] [5] |
| Negative | Pvalb−, Sst−, Calb2− | |
| Neuropeptides | Npy | [2] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0203 Lamp5 Lhx6 Gaba_1 · 🟡 MODERATE

**Supporting evidence:**

- Lamp5 Lhx6 Gaba_1 supertype is MGE-derived (Lhx6+) Lamp5+ GABA interneuron. Ivy cells are nNOS+ (Nos1+) Lamp5+ GABAergic interneurons, soma near stratum pyramidale, MGE-derived (Lhx6+ expected). The supertype markers include Lamp5 and Lhx6 as DEFINING_SCOPED, consistent with Ivy cell identity. Tricoire 2011 and Bhatt 2023 confirm Ivy cells are NGFC.M type (Lhx6+/Lamp5+/Id2+). However, anatomy shows CA3 SO (179), CA3 SR (235), DG mol (263) with no CA1 stratum pyramidale — Ivy cell preferred location in CA1 SP is absent. [Atlas metadata]
- Precomputed stats cross-check: all 3 defining markers confirmed (Nos1=7.79, Npy=4.62, Lamp5=4.40) and all 3 negative markers absent (Pvalb=0.43, Sst=1.52, Calb2=0.37). Strong marker support for Ivy cell identity in Lamp5 Lhx6 supertype. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Lamp5 subclass (n=868 HIP cells) onto WMBv1. SUPT_0203 (Lamp5 Lhx6 Gaba_1) is overwhelmingly the top supertype target (F1=0.898, 711/868 cells, target_purity=0.989). At SUBCLASS level, 710/868 Lamp5 HIP cells map to SUBC_050 (Lamp5 Lhx6 Gaba, F1=0.898), confirming Lamp5 Lhx6 identity. Ivy cells are the predominant Lamp5+Lhx6+ hippocampal interneuron type; this strong and specific hit is consistent with the ivy cell → SUPT_0203 assignment. The high target_purity (0.989) confirms SUPT_0203 is almost exclusively populated by Lamp5 cells in this dataset. [Annotation transfer]

**Concerns:**

- **location_sp** (DISCORDANT): A=CA1 stratum pyramidale (UBERON:0005401) — SOMA / B=DG mol layer (263), CA3 SO (179), CA3 SR (235) — no CA1 SP. Classical Ivy cell soma is in or near CA1 stratum pyramidale. This supertype has no CA1 pyramidal layer representation. CA3 is enriched — may reflect species difference or subregional bias in the atlas dataset.

- Ivy cells and nNOS+ NGCs (NGFC.M) are reported to share completely overlapping developmental, electrophysiological, morphological, and neurochemical properties (Tricoire 2011), suggesting they may constitute a single interneuron subtype distinguished only by laminar position. Edge 2b (NGC→SUPT_0203) and this edge may therefore overlap the same atlas population; see edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203.
- No CA1 stratum pyramidale cells in SUPT_0203 despite Ivy cell soma being canonically in CA1 SP. Atlas may undersample CA1 SP Lamp5 Lhx6 cells, or the Ivy cell CA1 population is split across additional supertypes.

**What would upgrade confidence:**

- *Unresolved:* Are the CA3-enriched Lamp5 Lhx6 cells in SUPT_0203 Ivy cells, NGCs, or a distinct type?
- *Unresolved:* Is there a CA1 SP Lamp5 Lhx6 cluster capturing hippocampal Ivy cells at the cluster level?

---

## Open questions

1. Are the CA3-enriched Lamp5 Lhx6 cells in SUPT_0203 Ivy cells, NGCs, or a distinct type?
2. Is there a CA1 SP Lamp5 Lhx6 cluster capturing hippocampal Ivy cells at the cluster level?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | Atlas metadata | PARTIAL |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | Atlas metadata | SUPPORT |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [2] | Tricoire et al. 2010 · PMID:20147544 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | Nos1 marker |
| [3] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Nos1 marker |
| [4] | Kim et al. 2025 · PMID:41473287 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | Nos1 marker |
| [5] | Wierenga et al. 2010 · PMID:21209836 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Nos1 marker |
