# Oriens-Lacunosum Moleculare (O-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | No CL term exists — nearest superclass: sst GABAergic interneuron (CL:4023017) | — |
| Soma location | Stratum oriens [UBERON:0005383] (CA1); stratum lacunosum moleculare [UBERON:0005403] (CA1) | [1] [2] [3] [4] [5] [6] [7] |
| Neurotransmitter | GABAergic | [4] |
| Defining markers | Sst, Chrna2, Reln | Sst: [4] [8] [5] [6]; Chrna2: [6] [4]; Reln: [4] |
| Negative markers | Pvalb | — |
| Neuropeptides | Sst, Npy, Pnoc | [4] |

> "Hippocampal CA1 stratum oriens interneuron subtypes include oriens lacunosum-moleculare (O-LM) interneurons, which can be identified by the expression of somatostatin and have regular-to-fast action potential spiking patterns (Oren et al., 2009)(Nicholson et al., 2014)(Huh et al., 2016). O-LM cell soma and dendrites reside in the stratum oriens and their axons project to the stratum lacunosum-moleculare layer"
> — Friend et al. 2019, Electrophysiological Properties and Function · [1] <!-- quote_key: 116862536_5f5f2ae8 -->

> "CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010)."
> — Tecuatl et al. 2020, Projection Patterns and Connectivity · [2] <!-- quote_key: 229694907_6865b9db -->

> "oriens-lacunosum moleculare (O-LM) cells (these SOM+ cells project to the distal dendrites in the stratum lacunosum-moleculare though their somata are located in the stratum oriens)"
> — Bezaire et al. 2016, Molecular Markers and Gene Expression · [3] <!-- quote_key: 4776309_dd48b1ec -->

> "The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus"
> — Nichol et al. 2018, Anatomical Location and Morphology · [6] <!-- quote_key: 3591966_644f1e68 -->

**Notes.** No CL term exists for OLM cell. CL:4023017 'sst GABAergic interneuron' is the nearest superclass but does not capture OLM-specific morphology. The type is molecularly heterogeneous: it contains a PV+ subpopulation with distinct theta vs gamma coupling. Npy expression is consistent in mouse but absent in rat (species difference). The Ndnf::Nkx2-1 intersection selectively targets OLM cells. At least 3 Chrna2+ subclusters have been identified.

---

## Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (supertype) | — | 🟡 MODERATE | Sst CONSISTENT · Reln CONSISTENT · Chrna2 APPROXIMATE | Best candidate |

Total: 1 edge · relationship type: PARTIAL_OVERLAP.

---

## 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

### Supporting evidence

- **NT type (CONSISTENT)**: The atlas supertype belongs to the Sst subclass with GABA neurotransmitter type, fully consistent with the GABAergic identity of OLM cells [4]. Molecular confirmation: GABAergic markers Gad1, Gad2, and Slc6a1 are consistently expressed across OLM interneurons, while glutamate-related transporters are essentially absent [4]:

> "Independent of the Cre line used for cell collection, we found consistent expression of GABA release‐related Gad1, Gad2 and Slc6a1 in all OLM interneurons. By contrast, glutamate release‐related vesicular glutamate transporter Slc17a7 (detected in 2/46 cells) and Slc17a6 (detected in 1/46 cells) genes were virtually not expressed across the whole population."
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d024a35 -->

- **Soma location — CA1 stratum oriens (CONSISTENT)**: The Sst Gaba_3 supertype has 818 cells registered to CA1 stratum oriens (MBA:399), matching the primary OLM soma location in stratum oriens [UBERON:0005383] [1][2][3][4][5][6][7].

- **Sst marker (CONSISTENT)**: Sst is a subclass-defining marker; precomputed stats mean = 11.44 [4][8]:

> "we found consistent expression of Sst and Reln, and sparse expression of Pvalb across both OLM neuron types"
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_2d5a5fb3 -->

- **Reln marker (CONSISTENT)**: Reln is in the defining markers of the Sst Gaba_3 supertype; precomputed stats mean = 7.90. Consistent Reln expression confirmed by RT-PCR in morphologically reconstructed OLM cells [4].

- **Negative marker Pvalb (CONSISTENT)**: Precomputed stats mean = 1.48 for Pvalb, consistent with the Pvalb-negative or Pvalb-low phenotype of OLM cells [4].

- **Neuropeptide Sst (CONSISTENT)**: Precomputed stats mean = 11.44 for Sst. Npy confirmed at atlas level (mean = 5.07) and Pnoc confirmed (mean = 3.69) [4]:

> "we found a surprisingly consistent expression of Npy in OLMs"
> — Winterer et al. 2019, Molecular Markers and Gene Expression · [4] <!-- quote_key: 201041756_8d16e821 -->

> "we detected Pnoc in both Htr3aCre‐OLM (14/23) and SstCre‐OLM (13/23)"
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_1d20426d -->

- **Annotation transfer (GEO:GSE185862 — PARTIAL)**: MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) SSv4 Sst subclass (n=273 HIP cells) onto WMBv1. At SUBCLASS level, Sst cells map strongly to Sst Gaba subclass (CS20230722_SUBC_053, F1=0.983, 265 cells). At SUPERTYPE level, the Sst population splits between 0219 Sst Gaba_6 [CS20230722_SUPT_0219] (F1=0.759, 161 cells) and 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.488, 83 cells; target_purity=1.0). The Yao 2021 SSv4 Sst subclass is a mixed population encompassing OLM, bistratified, hippocampo-septal, oriens-oriens, and other Sst types; OLM-specific resolution cannot be achieved from this source dataset alone.
- **Annotation transfer (GEO:GSE99888, Sst.Pnoc.Calb1.Igfbp5 — SUPPORT)**: Harris 2018 Class Sst.Pnoc.Calb1.Igfbp5 (SST+/Pnoc+/Calb1+/Igfbp5+ CA1 inhibitory cluster, n=254 cells in the 3,663-cell dataset) maps with group_purity=0.965 to [CS20230722_SUPT_0216] Sst Gaba_3 at SUPERTYPE level (F1=0.514, 222 cells). The very high group_purity (0.965) means 96.5% of this Harris cluster concentrates in Sst Gaba_3 — a strong directional signal confirming that SST+/Pnoc+/Calb1+/Igfbp5+ OLM-type cells are enriched in this supertype. The low F1 reflects mixed target content rather than poor assignment. This is independent corroboration of the GSE185862 OLM evidence from a distinct CA1 inhibitory dataset. Sst.Pnoc.Calb1.Igfbp5 co-expression (Sst, Pnoc, Calb1, Igfbp5) is consistent with known OLM neuropeptide and marker profile.
- **Annotation transfer (GEO:GSE99888, Chamberland Chrna2 subfamily — SUPPORT)**: Harris 2018 cells labelled Chrna2-OLM by Chamberland 2024 per-cluster rules (n=153 cells, dropout-robust cluster-mean gene-pair labelling) map to CLUS_0771 (Sst Gaba_3 child cluster) at cluster level with F1=0.649 and group_purity=0.813. This sub-resolves the Chrna2-OLM subset within [CS20230722_SUPT_0216]: 81% of Chrna2-labelled Harris cells concentrate at a single WMBv1 cluster within the Sst Gaba_3 supertype, providing the first cluster-level AT support for OLM cell identity. Per-cluster labels are dropout-robust (cluster-mean gene-pair rules; see Harris 2018 AT run README).

### Marker evidence provenance

- **Sst**: Transcript-level evidence (RT-PCR and scRNA-seq). Winterer et al. 2019 [4] used single-cell RT-PCR on patch-clamp filled and morphologically reconstructed neurons with confirmed OLM identity — strong cell-type specificity basis. Chamberland et al. 2023 [8] provides additional transcript-level support. No discrepancy between sources.

- **Chrna2**: Established at protein and transcript level. Nichol et al. 2018 [6] characterised Chrna2 as a specific OLM marker in dorsal CA1. Winterer et al. 2019 [4] confirmed at transcript level in morphologically reconstructed OLM cells:

> "as well as expression of Chrna2, which has been used as a marker for hippocampal OLM interneurons"
> — Winterer et al. 2019, Results 3.3 · [4] <!-- quote_key: 201041756_bd56f851 -->

  Cell-type specificity is strong in both studies. However, Chrna2 is not a defining marker of the Sst Gaba_3 supertype (precomputed mean = 1.53; APPROXIMATE alignment). The ABC Atlas HPF/GABA/Chrna2 filter retains Sst Gaba_3 (unlike Sst Gaba_6) but expression is scattered across clusters within the supertype, consistent with OLM cells being a subpopulation.

- **Reln**: Transcript-level (RT-PCR) in morphologically reconstructed OLM cells by Winterer et al. 2019 [4]. Reln is also a defining marker of the Sst Gaba_3 supertype (mean = 7.90), making this one of the better-supported alignment points.

- **Pvalb (negative marker)**: No dedicated negative-marker citation on the classical node. Winterer et al. 2019 [4] reports "sparse expression of Pvalb across both OLM neuron types" — a weak exclusion signal, not an absolute negative. The known PV+ OLM subpopulation noted in the node further weakens this negative marker. Atlas precomputed stats mean of 1.48 is consistent with sparse (not absent) expression.

- **Npy (neuropeptide)**: Consistent at transcript level in mouse OLM cells per Winterer et al. 2019 [4]. Species caveat: Npy is consistent in mouse but reportedly absent in rat — the atlas is mouse (WMBv1), so mouse data are directly relevant. Atlas precomputed stats confirm Npy mean = 5.07.

- **Pnoc (neuropeptide)**: Transcript-level detection in 14/23 Htr3aCre-OLM and 13/23 SstCre-OLM cells by Winterer et al. 2019 [4]. Atlas precomputed stats confirm Pnoc mean = 3.69.

### Concerns

- **Chrna2 APPROXIMATE**: Chrna2 is a defining marker for OLM cells but shows only scattered expression in the Sst Gaba_3 supertype (precomputed mean = 1.53; not a defining supertype marker). *(note: this likely reflects that OLM cells are a subpopulation within this supertype and Chrna2 expression marks those cells specifically but is diluted across the mixed supertype — a biological inference consistent with the DISTRIBUTED_ACROSS_CLUSTERS caveat.)*
- **DISTRIBUTED_ACROSS_CLUSTERS**: Sst Gaba_3 supertype contains at least three classical hippocampal cell types: OLM cells, bistratified cells, and HS (hippocampo-septal) cells. These are not separable at supertype level.
- **Non-hippocampal cells in supertype**: Prosubiculum (259 cells) and posterior amygdala (780 cells) are prominent in this supertype. *(note: posterior amygdala is anatomically distant from CA1 stratum oriens — stronger counter-evidence; the classical OLM type may still correspond to a subtype of this T-type but the posterior amygdala population is not the CA1 OLM population specifically.)*
- **Annotation transfer ambiguity (GSE185862)**: The dominant Sst supertype in the GSE185862 MapMyCells transfer is 0219 Sst Gaba_6 [CS20230722_SUPT_0219] (F1=0.759, 161 cells), not 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.488, 83 cells). This raises uncertainty about whether OLM cells preferentially occupy SUPT_0216 or SUPT_0219. The Yao 2021 SSv4 Sst subclass is a mixed population, so the supertype split reflects cell-type heterogeneity rather than a direct OLM signal. The GSE99888 Harris AT evidence (Sst.Pnoc.Calb1.Igfbp5: group_purity=0.965 at SUPT_0216; Chrna2: F1=0.649 at CLUS_0771 within SUPT_0216) partially resolves this ambiguity in favour of SUPT_0216 as the OLM-type supertype.
- **Sparse Pvalb expression**: Winterer et al. 2019 [4] reports sparse (not absent) Pvalb expression across OLM neurons. The known PV+ OLM subpopulation means Pvalb negativity is not absolute.

### What would upgrade confidence

1. **OLM-specific annotation transfer** (see Proposed experiments): MapMyCells with a morphologically or genetically labelled OLM source dataset, targeting F1 ≥ 0.80 at CLUSTER level. This would add AnnotationTransferEvidence and potentially resolve the SUPT_0216 vs SUPT_0219 ambiguity.
2. **Cluster-level Chrna2/Sst/Reln co-expression analysis**: Identifying which WMBv1 cluster(s) within Sst Gaba_3 show highest Chrna2 co-expression alongside Sst and Reln would provide cluster-level specificity without new experiments.
3. **Targeted literature search for Chrna2 OLM CA1 single-cell**: A cite-traverse for "Chrna2 OLM hippocampus CA1 single-cell" may reveal studies that directly mapped Chrna2+ cells to WMBv1 clusters. Output: `LiteratureEvidence`.
4. **Targeted literature search for Pvalb OLM negative marker**: A cite-traverse for "Pvalb OLM hippocampus CA1 negative marker" to validate or revise this negative marker designation.

---

## Proposed experiments

### Annotation transfer — OLM-specific source dataset

*Status note:* Three AT runs have been performed. (1) GSE185862 — mixed Sst subclass (n=273 HIP cells); SUPT_0216: F1=0.488 (83 cells); Sst Gaba subclass: F1=0.983 (265 cells). Does not resolve OLM-cell specificity. (2) GSE99888 — Harris Sst.Pnoc.Calb1.Igfbp5 cluster: group_purity=0.965 at SUPT_0216 (SUPPORT). (3) GSE99888 — Chamberland Chrna2 per-cluster: CLUS_0771 F1=0.649 (SUPPORT, cluster level). Runs 2 and 3 partially resolve OLM identity within SUPT_0216, but a fully labelled OLM source dataset at cluster resolution is still needed.

- **What**: MapMyCells annotation transfer using a source dataset with morphologically or genetically identified OLM cells (Chrna2-Cre or Ndnf::Nkx2-1 labelled Sst+ cells)
- **Target**: F1 ≥ 0.80 at CLUSTER level against WMBv1 (CCN20230722)
- **Expected output**: `AnnotationTransferEvidence` items on edge `edge_olm_cell_ca1_to_CS20230722_SUPT_0216`; potentially a new cluster-level edge if a specific cluster within Sst Gaba_3 is resolved
- **Resolves**: Open question 1 (SUPT_0216 vs SUPT_0219); DISTRIBUTED_ACROSS_CLUSTERS caveat; Chrna2 APPROXIMATE alignment

### Targeted literature search — Chrna2 OLM CA1

- **What**: Cite-traverse for "Chrna2 OLM hippocampus CA1 single-cell" targeting papers from 2018–2026
- **Target**: Identify a study that maps Chrna2+ hippocampal neurons to a transcriptomic atlas or performs scRNA-seq on Chrna2-Cre cells
- **Expected output**: `LiteratureEvidence` item with Chrna2 alignment data at cluster level
- **Resolves**: Open question 2; Chrna2 APPROXIMATE alignment

### Targeted literature search — Pvalb OLM negative marker

- **What**: Cite-traverse for "Pvalb OLM hippocampus CA1 negative marker"
- **Target**: Primary study testing Pvalb on morphologically confirmed OLM cells
- **Expected output**: `LiteratureEvidence` item confirming or revising the Pvalb-negative marker status
- **Resolves**: Open question 3; weak evidence for Pvalb exclusion criterion

---

## Open questions

1. Do OLM cells preferentially map to WMBv1 supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] or 0219 Sst Gaba_6 [CS20230722_SUPT_0219] when a morphologically labelled source dataset is used?
2. Which specific WMBv1 cluster(s) within the Sst Gaba_3 supertype carry the highest Chrna2 expression co-expressed with Sst and Reln?
3. What is the basis for Pvalb as an OLM negative marker? Winterer et al. 2019 [4] reports sparse (not absent) Pvalb expression. Is there a primary study confirming this exclusion in morphologically identified OLM cells?
4. Are the non-hippocampal cells in Sst Gaba_3 (posterior amygdala: 780 cells; prosubiculum: 259 cells) Sst+ OLM-like neurons, or unrelated Sst interneuron types?

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA (Sst subclass, GABA NT, CA1 SO 818 cells, Reln defining) | PARTIAL | Mixed supertype; OLM, bistratified, HS co-occupy; non-hippocampal cells present |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA (precomputed stats: Sst=11.44, Reln=7.90, Chrna2=1.53, Pvalb=1.48, Npy=5.07, Pnoc=3.69) | SUPPORT | All markers consistent; Chrna2 low but present |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (MapMyCells, GEO:GSE185862, SSv4 Sst subclass, n=273) | PARTIAL | Sst Gaba SUBC F1=0.983; SUPT_0216 F1=0.488 (83 cells); SUPT_0219 dominant (F1=0.759) |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (MapMyCells local, GEO:GSE99888, Sst.Pnoc.Calb1.Igfbp5, SUPERTYPE F1=0.514, gp=0.965) | SUPPORT | High recall confirms OLM-type cluster concentrates in Sst Gaba_3 |
| edge_olm_cell_ca1_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER (MapMyCells local, GEO:GSE99888, Chamberland Chrna2, CLUSTER F1=0.649 at CLUS_0771) | SUPPORT | Chrna2-OLM sub-resolves to cluster level within SUPT_0216 |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Friend et al. 2019 | [30987110](https://pubmed.ncbi.nlm.nih.gov/30987110/) | Soma location |
| [2] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | Soma location |
| [3] | Bezaire et al. 2016 | [28009257](https://pubmed.ncbi.nlm.nih.gov/28009257/) | Soma location |
| [4] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | Soma location; NT type; Sst, Chrna2, Reln markers; Npy, Pnoc neuropeptides |
| [5] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | Soma location; Sst marker |
| [6] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | Soma location; Chrna2 marker |
| [7] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Soma location |
| [8] | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Sst marker |
