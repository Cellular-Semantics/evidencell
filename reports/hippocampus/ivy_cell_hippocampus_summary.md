# Ivy cell (IvC) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum pyramidale [UBERON:0005401] (CA1) | [1] |
| NT | GABAergic | — |
| Markers | Nos1+, Npy+, Lamp5+ | [1][2][3][4][5] |
| Negative markers | Pvalb−, Sst−, Calb2− | — |
| Neuropeptides | Npy | [2] |

**Node notes:** No dedicated CL term. Ivy cells and nNOS+ NGCs are reported to share completely overlapping developmental, electrophysiological, morphological, and neurochemical properties, suggesting they may constitute a single interneuron subtype distinguished only by laminar position [2]. Both MGE and CGE developmental origins have been reported.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | — | 🟡 MODERATE | Lamp5 CONSISTENT · location DISCORDANT | Best candidate |

1 edge total · relationship type: PARTIAL_OVERLAP.

---

## 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🟡 MODERATE

### Supporting evidence

- **Lamp5 and Lhx6 defining markers** of SUPT_0203 are fully consistent with Ivy cell identity. Ivy cells are Lamp5+/Lhx6+ GABAergic interneurons of MGE origin; the Lhx6 component marks MGE lineage, expected for IvCs [2]. Lamp5 and Lhx6 appear as DEFINING_SCOPED markers of this supertype.
- **Precomputed stats marker cross-check.** All three Ivy cell defining markers are confirmed at high expression levels in SUPT_0203: Nos1 (mean 7.79), Npy (mean 4.62), Lamp5 (mean 4.40). All three negative markers are at low levels: Pvalb (0.43), Sst (1.52), Calb2 (0.37). The complete negative-marker panel is consistent with the Ivy cell profile.
- **GABA neurotransmitter** confirmed (GABA subclass in atlas; GABAergic classical type): CONSISTENT.
- **Annotation transfer (GEO:GSE185862).** MapMyCells local annotation transfer of Yao 2021 SSv4 Lamp5 hippocampal cells (n=868) onto WMBv1: SUPT_0203 (Lamp5 Lhx6 Gaba_1) [CS20230722_SUPT_0203] is overwhelmingly the top supertype target (711/868 cells, F1=0.898, target_purity=0.989). At SUBCLASS level, 710/868 cells map to 050 Lamp5 Lhx6 Gaba (F1=0.898, target_purity=0.992). Ivy cells are the predominant Lamp5+/Lhx6+ hippocampal interneuron type; this strong, specific hit is consistent with the Ivy cell → SUPT_0203 assignment. The near-perfect target purity (0.989) confirms SUPT_0203 is almost exclusively populated by Lamp5 cells in this dataset.
- **Annotation transfer (GEO:GSE99888) — independent corroboration.** Harris 2018 Class Cacna2d1.Lhx6.Reln (Lamp5+/Lhx6+/Reln+ CA1 inhibitory cluster, n=3,663 total dataset) maps predominantly to Lamp5 Lhx6 Gaba subclass (F1=0.825, group_purity=0.935, 245 cells) and to SUPT_0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] at supertype level (F1=0.812, group_purity=0.914, 246 cells). This is an independent dataset (STRT-seq, 3,663 CA1 inhibitory neurons) using a different source label — the convergence on the same supertype target as GSE185862 provides cross-dataset corroboration and strengthens the Ivy cell → SUPT_0203 assignment. The Reln co-expression in the Cacna2d1.Lhx6.Reln label is consistent with OLM-type Lamp5 cells; Cacna2d1 and Reln co-expression marks MGE-derived inhibitory neurons in CA1.
- Bocchio et al. 2024 [1] names NOS-expressing ivy cells as among the most representative CA1 pyramidal layer interneuron subtypes:

> This mouse line allows for a large sampling from diverse interneuron subtypes in the CA1 pyramidal layer, including the most representative ones (Bezaire et al., 2013), the PV-expressing basket and bistratified cells (Klausberger et al., 2008), the NOS- expressing ivy cells (14381729) and two types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin (Klausberger et al., 2008)(Topolnik et al., 2022)
> — Bocchio et al. 2024, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 262127573_d140faf4 -->

### Marker evidence provenance

- **Nos1 (nNOS):** Evidence spans protein-level (IHC) and transcript-level across five sources [1][2][3][4][5]. Tricoire et al. 2010 [2] is the primary morphological study — cells were confirmed as IvCs or NGCs by combined electrophysiology, morphological reconstruction, and IHC before nNOS positivity was assessed, providing the strongest cell-type specificity. Precomputed stats (mean 7.79) confirm robust atlas-side transcript expression; Nos1 absence from SUPT_0203 defining markers likely reflects an atlas specificity threshold rather than genuine absence.
- **Npy:** Protein-level evidence from Tricoire et al. 2010 [2], with NPY confirmed by IHC in morphologically reconstructed IvCs. Precomputed stats mean 4.62 confirms transcript-level atlas-side expression. Evidence chain is self-consistent.
- **Lamp5:** No primary citation is attached to the Lamp5 defining marker on this classical node (refs field is empty). The Lamp5 assignment appears to derive from atlas-side supertype matching rather than from an independent primary study directly measuring Lamp5 in morphologically confirmed Ivy cells. Precomputed stats confirm expression (mean 4.40) in SUPT_0203. A targeted cite-traverse for "Lamp5 ivy cell hippocampus" or "Lamp5 nNOS GABA hippocampus" is recommended to close this evidence gap.
- **Negative markers (Pvalb, Sst, Calb2):** No individual citations are attached on this node. Tricoire et al. 2010 [2] explicitly state that IvCs and NGCs fail to express PV, SOM, or CR (see quote below). Precomputed stats (Pvalb=0.43, Sst=1.52, Calb2=0.37) are all consistent with the expected negative profile.

> IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR.
> — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [2] <!-- quote_key: 2405079_6850b924 -->

### Concerns

- **location_sp (DISCORDANT):** Classical Ivy cell soma is in CA1 stratum pyramidale [UBERON:0005401] [1], but SUPT_0203 [CS20230722_SUPT_0203] has no CA1 pyramidal layer representation — atlas anatomy records DG mol layer (263 cells), CA3 SO (179), and CA3 SR (235). *(note: CA3 is directly adjacent to CA1 in the hippocampal trisynaptic circuit, but CA3 versus CA1 represents a genuine subfield difference, and SO versus SP a distinct laminar mismatch — this is moderate counter-evidence, not a registration boundary artefact.)*
- **IvC/NGC overlap (caveat).** Tricoire et al. [2] report that Ivy cells and nNOS+ NGCs share completely overlapping properties and may constitute a single type. The NGC mapping to SUPT_0203 and this edge likely capture the same atlas population; see edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203.
- **DISTRIBUTED_ACROSS_CLUSTERS caveat.** The atlas may undersample CA1 SP Lamp5 Lhx6 cells, or the canonical Ivy cell CA1 population may be split across additional supertypes not recovered at supertype level.

### What would upgrade confidence

- **Cluster-level annotation transfer** using a dataset enriched for CA1 Nos1+/nNOS+ cells (nNOS-Cre sorted hippocampal cells). Method: MapMyCells; target: F1 ≥ 0.80 at CLUSTER level within SUPT_0203 [CS20230722_SUPT_0203]. Expected output: AnnotationTransferEvidence on this edge; resolves Q1 and Q2.
- **Targeted literature search** for "Lamp5 ivy cell hippocampus" to establish a primary citation for the Lamp5 marker in morphologically confirmed IvCs. Resolves the unsourced Lamp5 marker evidence gap without new experiments.

---

## Proposed experiments

### Annotation transfer — cluster-level resolution

MapMyCells annotation transfer has been performed at SUPERTYPE level (GEO:GSE185862, F1=0.898, 711/868 cells, SUPT_0203 [CS20230722_SUPT_0203]). This round established Lamp5 Lhx6 supertype as the dominant WMBv1 destination for hippocampal Lamp5 cells.

**What remains unresolved:** Which specific clusters within SUPT_0203 correspond to the CA1 stratum pyramidale Ivy cell population; whether CA3-enriched atlas anatomy reflects genuine absence of CA1 SP cells or undersampling.

**Refined experiment:**

- **What:** MapMyCells cluster-level annotation transfer using a CA1 Nos1+/nNOS+ enriched dataset
- **Target:** F1 ≥ 0.80 at CLUSTER level on the best-matching WMBv1 cluster within SUPT_0203
- **Expected output:** AnnotationTransferEvidence on `edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203`; or identification of a CA1 SP cluster not recovered at supertype level
- **Resolves:** Q1 (IvC vs. NGC vs. distinct type in CA3 Lamp5 Lhx6); Q2 (CA1 SP Lamp5 Lhx6 cluster)

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
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ANNOTATION_TRANSFER — MapMyCells (GEO:GSE185862, SUPERTYPE, F1=0.898) | SUPPORT |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ANNOTATION_TRANSFER — MapMyCells local (GEO:GSE99888, SUBCLASS, F1=0.825; SUPERTYPE F1=0.812) | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [2] | Tricoire et al. 2010 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | Nos1 marker; Npy marker; negative markers |
| [3] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Nos1 marker |
| [4] | Kim et al. 2025 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | Nos1 marker |
| [5] | Wierenga et al. 2010 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Nos1 marker |
