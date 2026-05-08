# Hippocampo-septal (HS) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | sst chodl GABAergic interneuron (CL:4023121) — RELATED mapping | — |
| Soma location | Stratum oriens [UBERON:0005383] (CA1) | [1] [2] [3] [4] |
| Neurotransmitter | GABAergic | — |
| Defining markers | Sst | [1] [5] [6] |
| Neuropeptides | Sst | — |

> "SST+ cells were mainly found close to the alveus in the stratum-oriens of CA1 of both SAMR1 and SAMP8"
> — (preprint), Molecular Markers and Gene Expression · [1] <!-- quote_key: 132515344_fb36f967 -->

> "horizontal interneurons in stratum oriens of the hippocampal CA1 area are often studied as a single group of interneurons, they include several cell types in addition to O-LM cells"
> — Oren et al. 2009, Conclusions · [4] <!-- quote_key: 1015389_2738d858 -->

**Notes.** Very limited reference coverage (one direct quote available). Electrophysiology is not characterised, removing a potentially discriminating property. The relationship to Chodl+ long-range projecting cortical interneurons is unclear. HS cells are one of two main Sst+ interneuron types in CA1 alongside OLM cells; the defining feature distinguishing them is their long-range axonal projection to the medial septum, which cannot be resolved from atlas metadata alone.

---

## Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (supertype) | — | 🔴 LOW | Sst CONSISTENT · CA1 SO CONSISTENT · Reln DISCORDANT | Speculative |

1 edge total · relationship type: PARTIAL_OVERLAP.

---

## 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

### Supporting evidence

- **Neurotransmitter match (CONSISTENT)**: 0216 Sst Gaba_3 [CS20230722_SUPT_0216] is annotated as a GABA interneuron, fully consistent with the GABAergic identity of HS cells.
- **Stratum oriens location (CONSISTENT)**: Atlas metadata places the largest cell count for this supertype in Field CA1, stratum oriens (MBA:399, 818 cells), directly matching the canonical soma location of HS cells in CA1 stratum oriens [UBERON:0005383] [1][2][3][4]. Property comparison: CONSISTENT.
- **Sst marker expression (CONSISTENT)**: Sst is a defining marker at the Sst Gaba subclass level; precomputed expression mean for Sst = 11.44 across this supertype, consistent with robust Sst expression expected in HS cells [1][5][6].
- **Annotation transfer — subclass coherence**: MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Sst subclass (n=273 HIP cells) maps 265/273 cells to the Sst Gaba subclass at subclass level (F1=0.983, group_purity=0.989, target_purity=0.978), confirming strong subclass-level coherence for Sst interneurons in this atlas.
- **Annotation transfer — supertype fraction (PARTIAL)**: At supertype level, 0216 Sst Gaba_3 [CS20230722_SUPT_0216] receives 83/273 Sst cells (F1=0.488, target_purity=1.0). The Yao 2021 SSv4 'Sst' subclass encompasses multiple Sst interneuron types (OLM, bistratified, hippocampo-septal, oriens-oriens, and others); HS-specific resolution cannot be achieved from this source alone.

### Marker evidence provenance

- **Sst**: Positivity in HS cells is established by IHC in mouse hippocampus in multiple independent studies [1][5][6]. However, Sst is a shared subclass-level marker across all stratum oriens Sst+ interneurons (OLM, bistratified, HS, oriens-oriens) and does not discriminate HS cells at the transcript level.
- **Neuropeptide Sst**: Listed for HS cells but lacks direct quantitative support specific to HS cells; the precomputed expression mean of 11.44 reflects the full 0216 Sst Gaba_3 supertype, not a resolved HS subset.
- **Rbp4**: Listed as a defining marker of SUPT_0216 in the atlas; this gene has no annotation in the HS classical node and the alignment was not assessed. *(note: if HS cells express Rbp4, this could be a useful distinguishing feature — warrants targeted investigation.)*
- The Yao 2021 SSv4 "Sst" subclass (n=273 HIP cells) used for annotation transfer encompasses multiple Sst interneuron types without morphological labels; annotation transfer results are interpretable only at the population level.

### Concerns

- **Reln DISCORDANT**: Reln is listed as a DEFINING marker of 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (precomputed mean = 7.9), but Reln is a well-established marker of OLM cells (Chrna2::Reln co-expression confirmed in the literature). Its prominence as a defining marker of this supertype strongly suggests SUPT_0216 predominantly captures OLM cells rather than HS cells. Reln is not a listed feature of HS cells.
- **Shared, OLM-enriched supertype**: MapMyCells annotation transfer of OLM interneurons from an earlier dataset maps 43/46 OLM cells to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] with F1=0.67, confirming this is an OLM-enriched supertype. Bistratified cells (Pvalb/Sst/Tac1+) may also contribute. HS-specific long-range projection identity cannot be verified from atlas metadata alone.
- **SUPT_0219 dominance**: At supertype level, 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is the dominant recipient of Sst cells in the annotation transfer (161/273 cells, F1=0.759, group_purity=0.626), making it the primary Sst supertype target overall; SUPT_0216 captures a smaller and distinct fraction.
- **No HS-defining projecting feature assessable**: The long-range axonal projection to the medial septum that defines HS cells is not encoded in atlas metadata and cannot be evaluated with current evidence.
- **Limited reference coverage**: Very limited reference support (one direct quote), and electrophysiology is uncharacterised, removing an additional discriminating property.

### What would upgrade confidence

- Determine whether 0216 Sst Gaba_3 [CS20230722_SUPT_0216] contains any long-range projecting Sst+ neurons or is exclusively a local-circuit (OLM-dominant) supertype. Retrograde tracing combined with single-cell transcriptomics would resolve this directly.
- Clarify the relationship to Chodl+ long-range projecting interneurons: the CL RELATED term (CL:4023121) is the sst chodl GABAergic interneuron. If HS cells are Chodl+, checking Chodl expression across Sst supertypes could identify a more specific WMBv1 supertype.
- Investigate whether a more appropriate WMBv1 supertype for HS cells exists outside the Sst Gaba_3 supertype — for example within a different Sst supertype or a Chodl+ supertype.
- Obtain a reference dataset with morphologically or projection-confirmed HS cell labels and run MapMyCells annotation transfer to assign supertype-level cluster correspondences directly.

---

## Proposed experiments

### Retrograde tracing + single-cell transcriptomics

- Perform retrograde labelling from the medial septum in mouse, followed by single-cell RNA-seq or patch-seq of CA1 stratum oriens neurons. This would directly identify the transcriptomic profile of HS cells and enable targeted annotation transfer to WMBv1 supertypes.
- Cross-check: no current evidence exists for the transcriptomic identity of projection-confirmed HS cells; this is the primary evidence gap.

### Multiplexed FISH / IHC

- Test co-expression of Sst, Chodl, Reln, and Rbp4 in CA1 stratum oriens to define the molecular boundary between HS and OLM cells at protein and transcript level. *(note: Reln positivity is expected in OLM cells and would argue against HS identity for a given cell; Chodl positivity would support a long-range projecting identity consistent with HS cells.)*
- Cross-check: the Reln DISCORDANT property comparison (precomputed mean = 7.9 in SUPT_0216) makes this experiment informative for both candidate typing and supertype interpretation.

### Annotation transfer with labelled reference

- Apply MapMyCells to a dataset with morphologically or projection-confirmed HS cell labels and compare F1 profiles across Sst supertypes (SUPT_0216 vs SUPT_0219 and others) to identify the best WMBv1 supertype correspondence.
- Cross-check: current annotation transfer uses the bulk Sst subclass (Yao 2021 SSv4; GEO:GSE185862) without HS-specific labelling; a resolved reference would directly address the primary ambiguity.

---

## Open questions

1. Does 0216 Sst Gaba_3 [CS20230722_SUPT_0216] contain any long-range projecting Sst+ neurons, or is it exclusively a local-circuit (OLM-dominant) supertype?
2. Is there a more appropriate WMBv1 supertype for HS cells outside the Sst Gaba_3 supertype — for example a Chodl+ supertype or a different Sst subtype?

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | Sst+, GABA, CA1 SO consistent; Reln defining marker discordant; supertype OLM-enriched |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER | PARTIAL | GEO:GSE185862 SSv4 Sst subclass; SUBC F1=0.983; SUPT_0216 F1=0.488 (83 cells); mixed population, HS fraction not resolved |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | (preprint) https://doi.org/10.1101/598599 | — | Soma location; Sst marker |
| [2] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747/) | Soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | Soma location |
| [4] | Oren et al. 2009 | [19176803](https://pubmed.ncbi.nlm.nih.gov/19176803/) | Soma location |
| [5] | Takács et al. 2024 | [38470935](https://pubmed.ncbi.nlm.nih.gov/38470935/) | Sst marker |
| [6] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | Sst marker |
