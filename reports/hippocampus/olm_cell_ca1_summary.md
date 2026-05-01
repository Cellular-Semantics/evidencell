# Oriens-Lacunosum Moleculare (O-LM) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum oriens [UBERON:0005383] (CA1 stratum oriens); stratum lacunosum moleculare [UBERON:0005403] (CA1 stratum lacunosum-moleculare) | [1][2][3][4][5][6][7] |
| NT | GABAergic | [4] |
| Defining markers | Sst, Chrna2, Reln | [4][5][6][8] |
| Negative markers | Pvalb | — |
| Neuropeptides | Sst, Npy, Pnoc | [4] |

**Notes:** No CL term exists for OLM cell. CL:4023017 'sst GABAergic interneuron' is the nearest superclass but does not capture OLM-specific morphology. The type is molecularly heterogeneous: it contains a PV+ subpopulation with distinct theta vs gamma coupling. Npy expression is consistent in mouse but absent in rat (species difference). The Ndnf::Nkx2-1 intersection selectively targets OLM cells. At least 3 Chrna2+ subclusters have been identified.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | — | 🟡 MODERATE | Sst CONSISTENT · Chrna2 APPROXIMATE | Best candidate |

Total: 1 edge (PARTIAL_OVERLAP relationship).

---

## 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

### Supporting evidence

- **NT type (CONSISTENT):** The atlas supertype belongs to the Sst subclass with GABA neurotransmitter type, fully consistent with the GABAergic identity of OLM cells [4]. Molecular confirmation: GABAergic markers Gad1, Gad2, and Slc6a1 are consistently expressed across OLM interneurons, while glutamate-related transporters Slc17a7 (2/46 cells) and Slc17a6 (1/46 cells) are essentially absent.

> "Independent of the Cre line used for cell collection, we found consistent expression of GABA release‐related Gad1, Gad2 and Slc6a1 in all OLM interneurons. By contrast, glutamate release‐related vesicular glutamate transporter Slc17a7 (detected in 2/46 cells) and Slc17a6 (detected in 1/46 cells) genes were virtually not expressed across the whole population."
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d024a35 -->

- **Soma location — CA1 stratum oriens (CONSISTENT):** The Sst Gaba_3 supertype has 818 cells registered to CA1 stratum oriens (MBA:399), matching the primary OLM soma location in stratum oriens [UBERON:0005383] [1][2][3][4][5][6][7].

> "Hippocampal CA1 stratum oriens interneuron subtypes include oriens lacunosum-moleculare (O-LM) interneurons, which can be identified by the expression of somatostatin and have regular-to-fast action potential spiking patterns (Oren et al., 2009)(Nicholson et al., 2014)(Huh et al., 2016). O-LM cell soma and dendrites reside in the stratum oriens and their axons project to the stratum lacunosum-moleculare layer"
> — Friend et al. 2019, Electrophysiological Properties and Function · [1] <!-- quote_key: 116862536_5f5f2ae8 -->

> "CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010)."
> — Tecuatl et al. 2020, Projection Patterns and Connectivity · [2] <!-- quote_key: 229694907_6865b9db -->

> "oriens-lacunosum moleculare (O-LM) cells (these SOM+ cells project to the distal dendrites in the stratum lacunosum-moleculare though their somata are located in the stratum oriens)"
> — Bezaire et al. 2016, Molecular Markers and Gene Expression · [3] <!-- quote_key: 4776309_dd48b1ec -->

- **Sst marker (CONSISTENT):** Sst is a subclass-defining marker; precomputed stats mean = 11.44 in this supertype [4][8]. Consistent expression confirmed in morphologically reconstructed OLM cells:

> "we found consistent expression of Sst and Reln, and sparse expression of Pvalb across both OLM neuron types"
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_2d5a5fb3 -->

- **Reln marker (CONSISTENT):** Reln is in the defining markers of the Sst Gaba_3 supertype; precomputed stats mean = 7.90. Consistent Reln expression confirmed by RT-PCR in morphologically reconstructed OLM cells [4]. Reln as a supertype-defining marker strengthens the match beyond Sst alone.

- **Negative marker Pvalb (CONSISTENT):** Precomputed stats mean = 1.48 for Pvalb in this Sst supertype, consistent with the Pvalb-negative or Pvalb-low phenotype of OLM cells [4].

- **Neuropeptide Sst (CONSISTENT):** Precomputed stats mean = 11.44 for Sst. Npy also confirmed at atlas level (mean = 5.07) and Pnoc confirmed (mean = 3.69) [4]:

> "we found a surprisingly consistent expression of Npy in OLMs"
> — Winterer et al. 2019, Molecular Markers and Gene Expression · [4] <!-- quote_key: 201041756_8d16e821 -->

> "we detected Pnoc in both Htr3aCre‐OLM (14/23) and SstCre‐OLM (13/23)"
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d20426d -->

- **Annotation transfer (PARTIAL support):** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. At SUBCLASS level, Sst cells map strongly to Sst Gaba subclass (accession CS20230722_SUBC_053, F1=0.983, 265 cells). At SUPERTYPE level, the Sst population splits between 0219 Sst Gaba_6 [CS20230722_SUPT_0219] (F1=0.759, 161 cells) and 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.488, 83 cells; target_purity=1.0). The Yao 2021 SSv4 Sst subclass is a mixed population encompassing OLM, bistratified, hippocampo-septal, oriens-oriens, and other Sst types; OLM-specific resolution cannot be achieved from this source dataset alone.

### Marker evidence provenance

- **Sst:** Transcript-level evidence (RT-PCR and scRNA-seq). Winterer et al. 2019 [4] used single-cell RT-PCR on patch-clamp filled and morphologically reconstructed neurons with confirmed OLM identity by post-hoc biocytin fills — strong cell-type specificity basis. Chamberland et al. 2023 [8] provides additional transcript-level support. Both levels are consistent with the atlas (transcript-level scRNA-seq). No discrepancy between sources.

- **Chrna2:** Established at protein and transcript level. Nichol et al. 2018 [6] characterised Chrna2 as a specific OLM marker in dorsal CA1 (anatomical identification basis). Winterer et al. 2019 [4] confirmed at transcript level in morphologically reconstructed OLM cells.

> "The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus"
> — Nichol et al. 2018, Anatomical Location and Morphology · [6] <!-- quote_key: 3591966_644f1e68 -->

> "as well as expression of Chrna2, which has been used as a marker for hippocampal OLM interneurons"
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_bd56f851 -->

  Cell-type specificity basis is strong in both studies. However, Chrna2 is not a defining marker of the Sst Gaba_3 supertype in the atlas (precomputed stats mean = 1.53; APPROXIMATE alignment). The atlas notes scattered expression across clusters within this supertype, consistent with OLM cells being a subpopulation. A targeted literature search for "Chrna2 OLM hippocampus CA1 single-cell" is recommended to find studies that may have mapped Chrna2+ cells to specific WMBv1 clusters.

- **Reln:** Transcript-level (RT-PCR) in morphologically reconstructed OLM cells by Winterer et al. 2019 [4]. Consistent in OLM interneurons; cell-type specificity basis is strong. Reln is also a defining marker of the Sst Gaba_3 supertype (mean = 7.90), making this one of the better-supported alignment points with no discrepancy.

- **Pvalb (negative marker):** No specific primary citation is provided for Pvalb as an OLM negative marker on the classical node. Winterer et al. 2019 [4] reports "sparse expression of Pvalb across both OLM neuron types" — this is a weak exclusion signal, not an absolute negative. The atlas precomputed stats mean of 1.48 for Pvalb is consistent with sparse (not absent) expression. The known PV+ OLM subpopulation noted in the node further weakens this negative marker. A targeted literature search for "Pvalb OLM hippocampus CA1" is recommended to find a primary study testing Pvalb on morphologically confirmed OLM cells.

- **Npy (neuropeptide):** Consistent at transcript level in mouse OLM cells per Winterer et al. 2019 [4] (morphologically identified cells). Important species caveat: Npy expression is consistent in mouse but reportedly absent in rat — the atlas is mouse (WMBv1), so mouse data are directly relevant. Atlas precomputed stats confirm Npy mean = 5.07. No discrepancy between mouse literature and atlas.

- **Pnoc (neuropeptide):** Transcript-level detection in 14/23 Htr3aCre-OLM and 13/23 SstCre-OLM cells by Winterer et al. 2019 [4]. Cell-type specificity basis is good (Cre-driver targeting with morphological reconstruction). Atlas precomputed stats confirm Pnoc mean = 3.69. No discrepancy.

### Concerns

- **Chrna2 APPROXIMATE:** Chrna2 is a defining marker for OLM cells but shows only scattered expression in the Sst Gaba_3 supertype (precomputed stats mean = 1.53; not a defining supertype marker). The ABC Atlas HPF/GABA/Chrna2 filter retains Sst Gaba_3 (unlike Sst Gaba_6) but expression is spread across clusters within the supertype rather than concentrated in one cluster. *(note: this likely reflects that OLM cells are a subpopulation within this supertype and Chrna2 expression marks those cells specifically but is diluted across the mixed supertype — a biological inference consistent with the DISTRIBUTED_ACROSS_CLUSTERS caveat.)*

- **DISTRIBUTED_ACROSS_CLUSTERS:** Sst Gaba_3 supertype contains at least three classical hippocampal cell types: OLM cells, bistratified cells, and HS (hippocampo-septal) cells. These are not separable at supertype level. The PARTIAL_OVERLAP relationship and MODERATE confidence reflect this limitation. Cluster-level resolution requires either MapMyCells annotation transfer with a morphologically labelled OLM dataset or Chrna2-Cre targeting.

- **Non-hippocampal cells in supertype:** Prosubiculum (259 cells) and posterior amygdala (780 cells) are prominent in this supertype. *(note: posterior amygdala is anatomically distant from CA1 stratum oriens — this is a distant-region signal suggesting the supertype contains non-OLM Sst interneurons from other brain regions. Stronger counter-evidence than an adjacent-region spread; the classical OLM type may still correspond to a subtype of this T-type but the posterior amygdala population is not the CA1 OLM population specifically.)*

- **Annotation transfer ambiguity:** The dominant Sst supertype in the MapMyCells transfer is 0219 Sst Gaba_6 [CS20230722_SUPT_0219] (F1=0.759, 161 cells), not 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.488, 83 cells). This raises uncertainty about whether OLM cells preferentially occupy SUPT_0216 or SUPT_0219. The Yao 2021 SSv4 Sst subclass used as source is a mixed population, so the supertype split reflects cell-type heterogeneity rather than a direct OLM signal.

- **Sparse Pvalb expression:** Winterer et al. 2019 [4] reports sparse (not absent) Pvalb expression across OLM neurons. The atlas precomputed stats mean of 1.48 is consistent with this, but the classical node treats Pvalb as a negative marker. The known PV+ OLM subpopulation means Pvalb negativity is not absolute.

### What would upgrade confidence

1. **OLM-specific annotation transfer** (see Proposed experiments): MapMyCells with a morphologically or genetically labelled OLM source dataset, targeting F1 ≥ 0.80 at CLUSTER level. This would add AnnotationTransferEvidence and potentially resolve the SUPT_0216 vs SUPT_0219 ambiguity.

2. **Cluster-level Chrna2/Sst/Reln co-expression analysis:** Identifying which WMBv1 cluster(s) within Sst Gaba_3 show highest Chrna2 co-expression alongside Sst and Reln would provide cluster-level specificity without new experiments.

3. **Targeted literature search for Chrna2 OLM CA1 single-cell:** A cite-traverse for "Chrna2 OLM hippocampus CA1 single-cell" may reveal studies that directly mapped Chrna2+ cells to WMBv1 clusters. This resolves the Chrna2 APPROXIMATE alignment with existing literature rather than requiring new experiments.

4. **Targeted literature search for Pvalb OLM negative marker:** A cite-traverse for "Pvalb OLM hippocampus CA1 negative marker" is needed to validate or revise this negative marker designation.

---

## Proposed experiments

### Annotation transfer — OLM-specific source dataset

**Status note:** An annotation transfer using Yao 2021 SSv4 Sst subclass (GEO:GSE185862, n=273 HIP cells) has already been performed and is recorded as evidence on this edge (SUPT_0216: F1=0.488, 83 cells; Sst Gaba subclass: F1=0.983, 265 cells). This used a mixed Sst population — it establishes the Sst subclass baseline but does not resolve OLM-cell specificity. The refined experiment must use an OLM-enriched source.

- **What:** MapMyCells annotation transfer using a source dataset with morphologically or genetically identified OLM cells (Chrna2-Cre or Ndnf::Nkx2-1 labelled Sst+ cells; e.g. Winterer et al. 2019 dataset if available as cell x gene matrix)
- **Target:** F1 ≥ 0.80 at CLUSTER level against WMBv1 (CCN20230722)
- **Expected output:** AnnotationTransferEvidence items on edge `edge_olm_cell_ca1_to_CS20230722_SUPT_0216` specifying cluster-level hits; potentially a new cluster-level edge if a specific cluster within Sst Gaba_3 is resolved
- **Resolves:** Open question 1 (SUPT_0216 vs SUPT_0219); DISTRIBUTED_ACROSS_CLUSTERS caveat; Chrna2 APPROXIMATE alignment

### Targeted literature search — Chrna2 OLM CA1

- **What:** cite-traverse for "Chrna2 OLM hippocampus CA1 single-cell" targeting papers from 2018–2026
- **Target:** Identify a study that maps Chrna2+ hippocampal neurons to a transcriptomic atlas or performs scRNA-seq on Chrna2-Cre cells
- **Expected output:** LiteratureEvidence item with Chrna2 alignment data at cluster level
- **Resolves:** Open question 2; Chrna2 APPROXIMATE alignment

### Targeted literature search — Pvalb OLM negative marker

- **What:** cite-traverse for "Pvalb OLM hippocampus CA1 negative marker"
- **Target:** Find primary study testing Pvalb on morphologically confirmed OLM cells
- **Expected output:** LiteratureEvidence item confirming or revising the Pvalb-negative marker status
- **Resolves:** Open question 3; weak evidence for Pvalb exclusion criterion

---

## Open questions

1. Do OLM cells preferentially map to WMBv1 supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] or 0219 Sst Gaba_6 [CS20230722_SUPT_0219] when a morphologically labelled source dataset is used? The Yao 2021 mixed Sst transfer cannot answer this — it requires a morphologically or genetically enriched OLM source.

2. Which specific WMBv1 cluster(s) within the Sst Gaba_3 supertype carry the highest Chrna2 expression co-expressed with Sst and Reln? If a single cluster concentrates Chrna2+/Sst+/Reln+ cells, it becomes the primary OLM candidate for a cluster-level edge.

3. What is the basis for Pvalb as an OLM negative marker? Winterer et al. 2019 [4] reports sparse (not absent) Pvalb expression. Is there a primary study that confirms this exclusion in morphologically identified OLM cells, and does the known PV+ OLM subpopulation invalidate this as an exclusion criterion?

4. Are the non-hippocampal cells in Sst Gaba_3 (posterior amygdala: 780 cells; prosubiculum: 259 cells) Sst+ OLM-like neurons, or unrelated Sst interneuron types? This affects interpretation of the supertype cell count but does not block OLM mapping.

---

## Evidence base table

| Edge ID | Evidence type | Supports | Source |
|---|---|---|---|
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA — Sst subclass, GABA NT type, CA1 stratum oriens location (818 cells), Reln as defining marker | PARTIAL | WMBv1 atlas metadata |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA — precomputed stats: Sst=11.44, Reln=7.90, Chrna2=1.53, Pvalb=1.48, Npy=5.07, Pnoc=3.69 | SUPPORT | WMBv1 precomputed expression stats |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER — Yao 2021 SSv4 Sst subclass (GEO:GSE185862) → WMBv1; Sst Gaba subclass F1=0.983 (265 cells); SUPT_0216 F1=0.488 (83 cells, target_purity=1.0) | PARTIAL | GEO:GSE185862 via MapMyCells |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Friend et al. 2019 | [30987110](https://pubmed.ncbi.nlm.nih.gov/30987110/) | soma location |
| [2] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | soma location |
| [3] | Bezaire et al. 2016 | [28009257](https://pubmed.ncbi.nlm.nih.gov/28009257/) | soma location |
| [4] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | soma location; NT type; Sst, Chrna2, Reln markers; Npy, Pnoc neuropeptides |
| [5] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | soma location; Sst marker |
| [6] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | soma location; Chrna2 marker |
| [7] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | soma location |
| [8] | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Sst marker |
