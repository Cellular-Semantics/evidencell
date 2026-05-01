# Ivy cell (IvC) — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum pyramidale [UBERON:0005401] | [1] |
| NT | GABAergic | |
| Markers | Nos1+, Npy+, Lamp5+ | [2] [1] [3] [4] [5] |
| Negative markers | Pvalb−, Sst−, Calb2− | |
| Neuropeptides | Npy | [2] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | — | — | 🟡 MODERATE | Lamp5 CONSISTENT · location_sp DISCORDANT | Best candidate |

1 edge total · relationship type: PARTIAL_OVERLAP.

---

## 0203 Lamp5 Lhx6 Gaba_1 · 🟡 MODERATE

**Supporting evidence:**

- The 0203 Lamp5 Lhx6 Gaba_1 supertype [CS20230722_SUPT_0203] is an MGE-derived (Lhx6+) Lamp5+ GABAergic interneuron. Ivy cells are Nos1+ Lamp5+ GABAergic interneurons with an MGE lineage, making this supertype the expected transcriptomic home. Lamp5 and Lhx6 appear as DEFINING_SCOPED markers of the supertype, consistent with Ivy cell identity. Bocchio et al. 2024 [1] explicitly names NOS-expressing ivy cells as among the most representative interneuron subtypes sampled in the CA1 pyramidal layer, supporting the soma location and Nos1+ identity. The atlas anatomy records CA3 SO (179), CA3 SR (235), and DG mol (263), with no CA1 stratum pyramidale — the canonical Ivy cell location is absent from this supertype's atlas representation. [Atlas metadata]
- Precomputed stats cross-check: all three defining markers are confirmed at meaningful expression levels (Nos1=7.79, Npy=4.62, Lamp5=4.40) and all three negative markers are absent (Pvalb=0.43, Sst=1.52, Calb2=0.37). The complete negative-marker panel reinforces that SUPT_0203 is not a PV, SST, or Calretinin+ type. [Atlas metadata]
- MapMyCells annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Lamp5 subclass (n=868 HIP cells) onto WMBv1: SUPT_0203 (Lamp5 Lhx6 Gaba_1) [CS20230722_SUPT_0203] is the overwhelmingly top supertype target (F1=0.898, 711/868 cells, target_purity=0.989). At SUBCLASS level, 710/868 Lamp5 HIP cells map to SUBC_050 (Lamp5 Lhx6 Gaba, F1=0.898, target_purity=0.992), confirming the Lamp5 Lhx6 assignment. Ivy cells are the predominant Lamp5+Lhx6+ hippocampal interneuron type; this strong, specific F1 hit is consistent with the Ivy cell → SUPT_0203 assignment. The near-perfect target purity (0.989) confirms SUPT_0203 is almost exclusively populated by Lamp5 cells in this dataset. [Annotation transfer; GEO:GSE185862]

**Marker evidence provenance:**

- **Nos1 (nNOS):** Five sources cited, spanning IHC (protein-level) and literature review: Tricoire et al. 2010 [2] (primary study — IHC and electrophysiology in morphologically reconstructed IvCs and NGCs, strongest cell-type specificity), Bocchio et al. 2024 [1] (functional CA1 interneuron subtypes study), Tzilivaki et al. 2023 [3] (GABAergic interneurons review), Kim et al. 2025 [4] (discrete interneuron subsets study), and Wierenga et al. 2010 [5] (GFP-expressing interneuron characterisation). The Tricoire et al. 2010 [2] evidence is the strongest — cells were confirmed as IvCs or NGCs by combined electrophysiology, morphological reconstruction, and IHC before nNOS positivity was assessed. Despite the rich citation support, Nos1 does not appear as a listed atlas marker for SUPT_0203; however, the precomputed stats (mean=7.79) confirm robust transcript-level expression in the supertype population, indicating the omission from the marker list likely reflects an atlas specificity threshold rather than genuine absence.
- **Npy:** Evidence is protein-level from Tricoire et al. 2010 [2], where NPY was confirmed by IHC in morphologically reconstructed IvCs. Npy is also listed as a neuropeptide for this node with the same citation. Precomputed stats for SUPT_0203 show Npy mean=4.62, confirming transcript-level expression. The evidence chain is self-consistent across protein and transcript levels.
- **Lamp5:** Listed as a defining marker on this classical node without a specific primary citation (no refs recorded in the facts file). The Lamp5 assignment appears to derive from the atlas-side supertype matching rather than from an independent primary study directly measuring Lamp5 in morphologically confirmed Ivy cells. Precomputed stats confirm expression (mean=4.40) in SUPT_0203. A targeted cite-traverse for "Lamp5 ivy cell hippocampus" or "Lamp5 nNOS GABA hippocampus" is recommended to establish whether any primary study has directly measured Lamp5 in confirmed IvCs, which would strengthen this marker's evidence chain.
- **Negative markers (Pvalb, Sst, Calb2):** No individual citations are attached to the negative marker assertions on this node. The finding that IvCs fail to express PV, SST, or CR is explicitly stated by Tricoire et al. 2010 [2] (see quote below). Precomputed stats for SUPT_0203 confirm low atlas-side expression: Pvalb=0.43, Sst=1.52, Calb2=0.37 — all consistent with the expected negative profile.

> IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR.
> — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [2] <!-- quote_key: 2405079_6850b924 -->

> This mouse line allows for a large sampling from diverse interneuron subtypes in the CA1 pyramidal layer, including the most representative ones (Bezaire et al., 2013), the PV-expressing basket and bistratified cells (Klausberger et al., 2008), the NOS- expressing ivy cells (14381729) and two types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin (Klausberger et al., 2008)(Topolnik et al., 2022)
> — Bocchio et al. 2024, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 262127573_d140faf4 -->

**Concerns:**

- **location_sp (DISCORDANT):** Classical Ivy cell soma is in CA1 stratum pyramidale [UBERON:0005401], but SUPT_0203 [CS20230722_SUPT_0203] has no CA1 pyramidal layer representation in the atlas (recorded locations: DG mol layer, CA3 SO, CA3 SR). *(note: CA3 is directly adjacent to CA1 in the hippocampal trisynaptic circuit, but the CA1 versus CA3 subfield distinction represents a genuine anatomical mismatch — this is a moderate counter-evidence concern, not a registration boundary artefact.)*
- **IvC/NGC overlap caveat:** Ivy cells and nNOS+ NGCs (NGFC.M) are reported to share completely overlapping developmental, electrophysiological, morphological, and neurochemical properties, suggesting they may constitute a single interneuron subtype distinguished only by laminar position. Both the Ivy cell mapping (this edge) and the NGC mapping to SUPT_0203 may therefore capture the same atlas population; see also edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203.
- **DISTRIBUTED_ACROSS_CLUSTERS:** Atlas may undersample CA1 SP Lamp5 Lhx6 cells, or the canonical Ivy cell CA1 population may be split across additional supertypes not recovered by this supertype-level analysis.

**What would upgrade confidence:**

- **Annotation transfer at CLUSTER level** using a dataset enriched for CA1 Nos1+/nNOS+ cells (e.g. nNOS-Cre sorted hippocampal cells), targeting F1 ≥ 0.80 at CLUSTER level — this would identify which specific WMBv1 cluster(s) capture CA1 IvC cells and resolve the CA1 SP underrepresentation concern (adds AnnotationTransferEvidence; resolves Q1 and Q2 below).
- **Targeted literature search** for "Lamp5 ivy cell hippocampus" or "Lamp5 nNOS GABA hippocampus" to establish whether any primary study directly measured Lamp5 in morphologically confirmed IvCs. This would strengthen the Lamp5 marker assertion without new experiments (resolves the unsourced Lamp5 marker evidence gap).

---

## Proposed experiments

### Annotation transfer — cluster-level resolution

MapMyCells annotation transfer was already performed at SUPERTYPE level (GEO:GSE185862, F1=0.898, 711/868 cells mapped to SUPT_0203 [CS20230722_SUPT_0203]). This round established that the Lamp5 Lhx6 supertype is the dominant WMBv1 destination for hippocampal Lamp5 cells and provides strong SUPPORT for the Ivy cell → SUPT_0203 mapping.

**What remains unresolved:** The supertype-level hit does not reveal which specific clusters within SUPT_0203 correspond to the CA1 stratum pyramidale Ivy cell population, nor whether the CA3-enriched atlas anatomy reflects a true absence of CA1 SP cells or an undersampling artefact.

**Refined experiment:**

- **What:** MapMyCells cluster-level annotation transfer using a dataset enriched for CA1 Nos1+/nNOS+ cells (e.g. nNOS-Cre sorted or nNOS-GFP sorted hippocampal cells)
- **Target:** F1 ≥ 0.80 at CLUSTER level on the best-matching WMBv1 cluster within SUPT_0203 [CS20230722_SUPT_0203]
- **Expected output:** AnnotationTransferEvidence on edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203, and/or identification of a CA1 SP cluster not recovered at supertype level
- **Resolves:** Q1 (IvC vs. NGC vs. distinct type in CA3-enriched Lamp5 Lhx6) and Q2 (CA1 SP Lamp5 Lhx6 cluster existence)

---

## Open questions

1. Are the CA3-enriched Lamp5 Lhx6 cells in SUPT_0203 Ivy cells, NGCs, or a distinct type?
2. Is there a CA1 SP Lamp5 Lhx6 cluster capturing hippocampal Ivy cells at the cluster level?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA — supertype marker and anatomy comparison | PARTIAL |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA — precomputed stats marker cross-check | SUPPORT |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ANNOTATION_TRANSFER — MapMyCells (GEO:GSE185862, supertype level, F1=0.898) | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bocchio et al. 2024 · PMID:39401246 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [2] | Tricoire et al. 2010 · PMID:20147544 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | Nos1 marker |
| [3] | Tzilivaki et al. 2023 · PMID:37467748 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Nos1 marker |
| [4] | Kim et al. 2025 · PMID:41473287 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | Nos1 marker |
| [5] | Wierenga et al. 2010 · PMID:21209836 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Nos1 marker |
