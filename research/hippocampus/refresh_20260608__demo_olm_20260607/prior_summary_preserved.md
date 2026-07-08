# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*2026-03-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/_demo_olm_20260607.yaml`*

## Introduction

Oriens-lacunosum moleculare (O-LM) cells are a canonical population of CA1 GABAergic, somatostatin-expressing interneurons whose distinctive morphology — horizontal dendrites in stratum oriens and a single axonal projection arborising in stratum lacunosum-moleculare — gives them their name [2][3][6]. They generate feedback inhibition onto pyramidal-cell apical tufts and have been implicated in theta-rhythm generation and fear encoding [7][8]. Mapping this classical type onto the Whole Mouse Brain v1 (WMBv1) transcriptomic taxonomy clarifies which atlas clusters most likely correspond to the O-LM population and is a useful test case because OLM is defined multimodally (morphology + Cre-driver targeting + transcriptomics) rather than from transcriptomics alone.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371]; with axon arbor in hippocampus stratum lacunosum moleculare [UBERON:0007640] | [1][2][3] |
| NT | GABAergic | [4][5] |
| Defining markers | Sst, Chrna2, mGluR1 (Grm1) | [6][7][8][2] |
| Negative markers | PV, CB, CR, NOS, VIP (immunohistochemical absence) | — |
| Neuropeptides | Sst, Npy, Pnoc | [7][9] |
| Cell Ontology term | (none assigned) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / morphology:** Zemankovics et al. 2010 · whole-cell recording + biocytin reconstruction · rat · [1]
  > oriens-lacunosum-moleculare (OLM) cells also had both the cell body and dendritic tree in the stratum oriens, but their horizontally running dendrites were often densely decorated with long spines. Their axon frequently originated from a proximal dendrite, and after ramification the main axon without boutons could be followed into the stratum lacunosum-moleculare. In this layer the axon ramified extensively bearing heavily packed varicosities. Some axon collaterals with boutons were also observed in the stratum oriens.
  > — Zemankovics et al. 2010, Anatomical Location and Morphology · [1] <!-- quote_key: 3106274_e54f60e9 -->

- **Soma location / Sst marker:** Nichol et al. 2018 · review · mouse · [2]
  > These CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare (SLM; Cajal, 1911;(McBain et al., 1994)(Sik et al., 1995)(Maccaferri et al., 2000)(Losonczy et al., 2002)(Leão et al., 2012)
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_2414c9e9 -->

- **Connectivity / dendrites SO only:** Tecuatl et al. 2020 · synthesis · [3]
  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [3] <!-- quote_key: 229694907_6865b9db -->

- **NT (GABAergic):** Böhm et al. 2015 · paired patch-clamp · rat · [4]
  > GABAergic inhibitory oriens lacunosum-moleculare (O-LM) cells in the hippocampal area CA1 of the rat
  > — Böhm et al. 2015, Anatomical Location and Morphology · [4] <!-- quote_key: 15101210_5604b9a4 -->

- **Sst marker:** Oliva et al. 2000 · GIN transgenic line / immunohistochemistry · mouse · [5]
  > EGFP was found to be expressed in a subpopulation of somatostatin-containing GABAergic interneurons in the hippocampus and neocortex
  > — Oliva et al. 2000, Molecular Markers and Gene Expression · [5] <!-- quote_key: 13398453_9154fc23 -->

- **Sst + mGluR1 marker:** Hooft et al. 2000 · whole-cell + in situ hybridization · rat · [6]
  > Type I interneurons had large horizontally oriented cell somata located at the border of stratum oriens and the alveus, indicating that these cells were most likely identical with the previously described somatostatin-positive oriens-lacunosum moleculare (O-LM) cells (Freund et al., 1998). Reconstruction of type I interneurons revealed their horizontally oriented dendritic tree in stratum oriens and their axonal arborizations in stratum lacunosum-moleculare (n = 5) (Fig. 2 A), and in situ hybridization for somatostatin showed that four of four cells were indeed positive for somatostatin (Fig. 2 B)
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_215c5f40 -->

  > Type I interneurons responded with a large inward current of ≈ 224pA, were positive for somatostatin, and the majority expressed both mGluR1 and mGluR5
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_17d10a9e -->

- **Sst marker / function:** Winterer et al. 2019 · single-cell RNA-seq (Cre-driver dataset behind the present AT run) · mouse · [7]
  > oriens-lacunosum moleculare (OLM) interneurons. OLMs express somatostatin (Sst), generate feedback inhibition and play important roles in theta oscillations and fear encoding
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_69dc904d -->

  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_8d16e821 -->

- **Chrna2 marker:** Nichol et al. 2018 · review · [2]
  > The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_644f1e68 -->

- **Chrna2 marker / Cre-driver:** Leão et al. 2012 · Chrna2-Cre transgenic + biocytin fills · mouse · [8]
  > The vast diversity of GABAergic interneurons is believed to endow hippocampal microcircuits with the required flexibility for memory encoding and retrieval. However, dissection of the functional roles of defined interneuron types has been hampered by the lack of cell-specific tools. We identified a precise molecular marker for a population of hippocampal GABAergic interneurons known as oriens lacunosum-moleculare (OLM) cells. By combining transgenic mice and optogenetic tools, we found that OLM cells are important for gating the information flow in CA1, facilitating the transmission of intrahippocampal information (from CA3) while reducing the influence of extrahippocampal inputs (from the entorhinal cortex). Furthermore, we found that OLM cells were interconnected by gap junctions, received direct cholinergic inputs from subcortical afferents and accounted for the effect of nicotine on synaptic plasticity of the Schaffer collateral pathway. Our results suggest that acetylcholine acting through OLM cells can control the mnemonic processes executed by the hippocampus.
  > — Leão et al. 2012, Projection Patterns and Connectivity · [8] <!-- quote_key: 7952877_ae03c6e0 -->

- **Pnoc neuropeptide + Sst/Pnoc subclusters:** Thulin et al. 2025 · scRNA-seq survey · [9]
  > The Chrna2 gene expression is restricted to the stratum oriens in the hippocampus in both rats and mice (Ishii et al., 2005) and is specifically expressed in a subset of CA1 hippocampal interneurons, the oriens lacunosummoleculare (OLM) cells (Leão et al., 2012). Traditionally, OLM cells have been identified through their expression of somatostatin (Sst). However, in-depth single-cell transcriptomic cluster analysis has unveiled at least 11 distinct subpopulations of Sst-expressing interneurons (2017). Within these clusters, various classes of interneurons were identified, including back projecting, hippocampo-septal, oriens-bistratified, and OLM cells. Among these clusters, OLM cells were classified into a Sst and Prepronociceptin (Pnoc) co-expressing group (further divided into three subclusters)
  > — Thulin et al. 2025, Projection Patterns and Connectivity · [9] <!-- quote_key: 280420054_8a6529c5 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Nine candidate atlas nodes were assessed (five WMBv1 rank-0 clusters and four rank-1 supertypes); the primary mapping is to **0216 Sst Gaba_3 [CS20230722_SUPT_0216]** at MODERATE confidence, with five sibling clusters under this supertype as LOW-confidence cluster-rank candidates and four distantly-located Sst supertypes eliminated.

### Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | (supertype) | 2004 | 🟡 MODERATE | Sst/Chrna2 CONSISTENT · region CONSISTENT · AT F1=0.67 supertype | skos:closeMatch |
| 2 | 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | 🔴 LOW | Sst/Chrna2 CONSISTENT · AT F1=0.44 cluster | skos:closeMatch |
| 3 | 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | 🔴 LOW | Sst/Chrna2 CONSISTENT · region CONSISTENT · AT F1=0.27 cluster | skos:closeMatch |
| 4 | 0773 Sst Gaba_3 [CS20230722_CLUS_0773] | 0216 Sst Gaba_3 | 156 | 🔴 LOW | Sst/Chrna2 CONSISTENT · region CONSISTENT | skos:closeMatch |
| 5 | 0775 Sst Gaba_3 [CS20230722_CLUS_0775] | 0216 Sst Gaba_3 | 143 | 🔴 LOW | Sst/Chrna2/Pnoc CONSISTENT · region APPROXIMATE | skos:closeMatch |
| 6 | 0770 Sst Gaba_3 [CS20230722_CLUS_0770] | 0216 Sst Gaba_3 | 404 | 🔴 LOW | Sst/Chrna2/Pnoc CONSISTENT · region CONSISTENT · PV CONSISTENT | skos:closeMatch |
| — | 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | (supertype) | 4064 | ⚪ UNCERTAIN | region DISCORDANT (Isocortex) | evidencell:UncertainRelationship |
| — | 0217 Sst Gaba_4 [CS20230722_SUPT_0217] | (supertype) | 14335 | ⚪ UNCERTAIN | region DISCORDANT (Isocortex) | evidencell:UncertainRelationship |
| — | 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | (supertype) | 2905 | ⚪ UNCERTAIN | region DISCORDANT · Chrna2 absent | evidencell:UncertainRelationship |
| — | 0224 Sst Gaba_11 [CS20230722_SUPT_0224] | (supertype) | 2677 | ⚪ UNCERTAIN | region DISCORDANT (Isocortex) | evidencell:UncertainRelationship |

Ten candidate edges total; the relationship type for the six MODERATE/LOW candidates is `skos:closeMatch` (1:1 shape but with documented contradictions in negative-marker comparisons; see Discussion).

![AT F1 heatmap for OLM source-cell mapping onto WMBv1 (GEO:GSE124847 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/figures/f1_heatmap.png)

*F1 across taxonomy levels for Sst-OLM source cells mapped onto WMBv1. Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.* The Sst-OLM cohort reaches F1=0.68 at CLASS (07 CTX-MGE GABA) and SUBCLASS (053 Sst Gaba), F1=0.67 at SUPERTYPE (0216 Sst Gaba_3), and degrades to F1=0.44 at the best CLUSTER (0768) — consistent with the run's caveat that OLM is captured at supertype/subclass level but scatters across sibling clusters at WMBv1 cluster rank.

### Property alignment — primary candidate (CS20230722_SUPT_0216)

**Table 1 — Property comparison**

| Property | Classical | Supertype (CS20230722_SUPT_0216) | Best cluster (CS20230722_CLUS_0768) | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | 1463 cells in Field CA1, stratum oriens [MBA:399]; `region_fraction_100um: 0.539` | 261 cells in MBA:399; `region_fraction_100um: 0.818` | SUPT: CONSISTENT; CLUS: CONSISTENT |
| NT type | GABAergic | not asserted | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Sst expression | defining marker | 11.44 (cohort_pct 0.905; child-coverage 1.000) | 12.70 (CLUS_0768; cohort_pct 0.992) | CONSISTENT |
| Chrna2 expression | defining marker | 0.61 (cohort_pct 0.952; child-coverage 0.667) | 0.57 (CLUS_0768; cohort_pct 0.950) | CONSISTENT |
| mGluR1 (Grm1) expression | defining marker | no atlas expression data | no atlas expression data | NOT_ASSESSED |
| Npy (neuropeptide) | classical | 5.07 (cohort_pct 0.794; child-coverage 1.000) | (n/a — see CLUS table) | CONSISTENT |
| Pnoc (neuropeptide) | classical | 3.69 (cohort_pct 0.667; child-coverage 0.889) | 2.51 (CLUS_0768; cohort_pct 0.479) | SUPT: CONSISTENT; CLUS: APPROXIMATE |
| PV (negative) | ABSENT | 1.48 | 3.12 | DISCORDANT |
| CB (negative) | ABSENT | 5.56 | 3.87 | DISCORDANT |
| CR (negative) | ABSENT | 1.28 | 2.30 | DISCORDANT |
| NOS (negative) | ABSENT | 2.94 | 0.76 | DISCORDANT |
| VIP (negative) | ABSENT | 0.42 | 0.31 | DISCORDANT |
| Sex ratio | not documented | not available | MFR=1.13 (CLUS_0768) | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression / region (SUPT_0216) | Atlas metadata | PARTIAL | n_cells=2004; `region_fraction_100um=0.539`; strict 0.305 | atlas-internal |
| MapMyCells AT (Sst-OLM → SUPT_0216) | Annotation transfer | SUPPORT | F1=0.67 (supertype rank); coverage 0.96, purity 0.51, n=22 | atlas-internal |

*(5 of 5 child clusters under SUPT_0216 in the queried cohort are concordant for Sst and Chrna2; child-cluster Pnoc coverage is 0.889 and Chrna2 coverage 0.667 — i.e. Chrna2 is detectable above MIN_DETECTABLE in only ≈2/3 of the supertype's children. Best match: CS20230722_CLUS_0768.)*

### Property alignment — best cluster-rank candidate (CS20230722_CLUS_0768)

**Table 1 — Property comparison**

| Property | Classical | Supertype (CS20230722_SUPT_0216) | Best cluster (CS20230722_CLUS_0768) | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | `region_fraction_100um: 0.539` | 261 cells in MBA:399; `region_fraction_100um: 0.818` | CONSISTENT |
| NT type | GABAergic | not asserted | GABA | CONSISTENT |
| Sst expression | defining marker | 11.44 | 12.70 (cohort_pct 0.992) | CONSISTENT |
| Chrna2 expression | defining marker | 0.61 | 0.57 (cohort_pct 0.950) | CONSISTENT |
| mGluR1 (Grm1) expression | defining marker | no atlas expression data | no atlas expression data | NOT_ASSESSED |
| Npy (neuropeptide) | classical | 5.07 | 7.58 (cohort_pct 0.857) | CONSISTENT |
| Pnoc (neuropeptide) | classical | 3.69 | 2.51 (cohort_pct 0.479) | APPROXIMATE |
| PV/CB/CR/NOS/VIP (negative) | ABSENT | (see SUPT row) | 3.12 / 3.87 / 2.30 / 0.76 / 0.31 | DISCORDANT |
| Sex ratio | not documented | not available | MFR=1.13 | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression / region (CLUS_0768) | Atlas metadata | PARTIAL | n_cells=66; `region_fraction_100um=0.818`; strict 0.458 | atlas-internal |
| MapMyCells AT (Sst-OLM → CLUS_0768) | Annotation transfer | SUPPORT | F1=0.44 (cluster rank); coverage 0.43, purity 0.45, n=10 | atlas-internal |

*(CLUS_0768 is the highest-AT-F1 cluster among the 5 SUPT_0216 children queried; its cluster-rank F1=0.44 falls below the 0.5 clean-mapping threshold — the OLM signal is genuinely distributed across SUPT_0216's children rather than concentrated in any one cluster.)*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Supporting evidence**

- **Region.** SUPT_0216 has 1463 cells in Field CA1, stratum oriens [MBA:399] and 2145 in the Hippocampal formation [MBA:1089]; `region_fraction_100um: 0.539` (proximity) with strict `region_fraction: 0.305` — both fractions point into hippocampal CA1, consistent with the classical OLM soma location [1][2][3]. The proximity > strict gap is the expected boundary-scatter signature for a sparsely-distributed interneuron type within a registered region.
- **Markers.** Sst (atlas mean 11.44, cohort percentile 0.905) and Chrna2 (mean 0.61, cohort_pct 0.952) are both CONSISTENT with the classical defining markers from scRNA-seq [7] and from Chrna2-Cre lineage tracing [2][8]. Npy and Pnoc (atlas means 5.07 and 3.69 respectively) match the classical neuropeptide profile [7][9]. mGluR1 (Grm1) is not present in WMBv1 precomputed stats so cannot be cross-checked.
- **Annotation transfer.** MapMyCells transfer of Winterer Sst-OLM cells onto WMBv1 reaches F1=0.67 at the SUPT_0216 supertype (coverage=0.96, purity=0.51, n=22 cells mapped; median_bootstrap=1.0) — i.e. essentially all Sst-OLM source cells land on SUPT_0216 but the supertype contains roughly an equal number of non-OLM Sst cells. The same F1=0.68 is reached at SUBC_053 (Sst Gaba) and CLAS_07 (CTX-MGE GABA).

**Marker evidence provenance**

- **Sst (defining + neuropeptide).** Protein- and transcript-level evidence converges: immunohistochemistry on biocytin-filled, morphology-confirmed OLM cells [6]; the GIN-EGFP transgenic line targeting Sst+ interneurons [5]; and the Winterer 2019 Chrna2-Cre + scRNA-seq dataset that is the source for the present AT run [7]. Cell-type specificity is strong (morphology + transgenic + transcriptomic convergence). Atlas SUPT_0216 mean = 11.44 with full child-coverage 1.000 — no atlas annotation/expression discrepancy.
- **Chrna2 (defining).** Specifically established by Leão et al. 2012 via Chrna2-Cre transgenic and biocytin-filled morphology confirmation in dorsal CA1 [8]; corroborated by Nichol et al. 2018 [2] and the Winterer Cre-driver dataset [7]. SUPT_0216 mean = 0.61 (cohort_pct 0.952) but child-cluster coverage is only 0.667 — i.e. Chrna2 is detectable above MIN_DETECTABLE in 2 of 3 child clusters of SUPT_0216, consistent with the documented Sst/Pnoc-subcluster heterogeneity of OLM [9].
- **mGluR1 (Grm1, defining).** Established in mGluR1+mGluR5 co-expressing horizontally-oriented O-LM cells by Hooft et al. 2000 [6] (whole-cell + ISH on morphology-confirmed cells), corroborated by Winterer 2019 [7]. Not assessed against the atlas because Grm1 is absent from Stage A `expression_detail` and `precomputed_expression` — a real data gap for this target.
- **Negative markers (PV, CB, CR, NOS, VIP).** The classical "negative for PV/CB/CR/NOS/VIP" claim derives from the immunohistochemical tradition (protein-level absence in morphology-confirmed OLM cells); no primary citation is recorded on the node for these. The atlas precomputed-expression values (transcript-level: PV=1.48, CB=5.56, CR=1.28, NOS=2.94, VIP=0.42 at SUPT_0216) are all above MIN_DETECTABLE — but mRNA presence does not directly contradict protein-level absence, particularly for low-expressed or post-translationally regulated calcium-binding proteins. A targeted cite-traverse for primary IHC studies of these negative markers in morphology-confirmed OLM cells would strengthen the negative-marker call. *(note: transcript-vs-protein discrepancy is the most likely reading here, not a true marker contradiction.)*
- **Pnoc (neuropeptide).** Established by Thulin et al. 2025 [9] via scRNA-seq cluster analysis (OLM identified as Sst/Pnoc co-expressing group with three subclusters) and corroborated by Winterer 2019 [7]. SUPT_0216 mean = 3.69 (cohort_pct 0.667) — consistent but mid-cohort, reflecting the cross-subcluster variability noted in [9].

**Concerns**

- **All five canonical negative markers show DISCORDANT atlas values at SUPT_0216** (PV 1.48, CB 5.56, CR 1.28, NOS 2.94, VIP 0.42). Five-of-five is a notable discordance signal, but as noted above the classical claim is at protein level (immunohistochemistry) and the atlas value is transcript-level — a known systematic mismatch for some of these markers (e.g. calbindin, calretinin) where mRNA is present without detectable protein.
- **AT F1=0.67 at SUPT_0216 is below the HIGH threshold (0.75).** Coverage is 0.96 (Sst-OLM source cells almost entirely land here) but purity is only 0.51, i.e. the supertype contains roughly as many non-OLM Sst cells as OLM cells. This is consistent with the AT-run caveat: OLM cell type is captured at supertype/subclass level (Sst Gaba_3 / Sst Gaba; F1 ≈ 0.65) but scatters across sibling clusters.
- **AT source size is small** — 46 Sst-OLM cells from the Winterer 2019 dataset, 45 retained after bootstrap filtering, 22 cells mapped at supertype rank. The F1 estimate has wide uncertainty intervals.
- **mGluR1 (Grm1) cannot be assessed** against the atlas because the gene is absent from precomputed_expression — a data gap, not a contradiction.

**What would upgrade confidence**

- A larger patch-seq dataset of morphology-confirmed OLM cells (e.g. Chrna2-Cre + biocytin + scRNA-seq, n ≥ 100) re-run through MapMyCells onto WMBv1; target F1 ≥ 0.75 at SUPT_0216. Expected output: a higher-purity `AnnotationTransferEvidence` item.
- Targeted cite-traverse for primary IHC studies establishing protein-level absence of PV/CB/CR/NOS/VIP in morphology-confirmed OLM cells — would attach `MarkerSource` provenance to the classical negative markers and let the report disambiguate "atlas-transcript-present, classical-protein-absent" cases from genuine contradictions.
- A `MarkerAnalysisEvidence` item assessing Grm1 expression at SUPT_0216 / its child clusters (the gene is in the source taxonomy but not in the precomputed stats currently exposed to Stage A).

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · 🔴 LOW

**Supporting evidence**

- **Region.** CLUS_0768 has 261 painted MERFISH cells in MBA:399 (Field CA1, stratum oriens); `region_fraction_100um: 0.818` (very high — i.e. effectively all spatially-registered cells sit in or adjacent to the OLM target region). Strict `region_fraction: 0.458`.
- **Markers.** Sst=12.70 (cohort_pct 0.992 — top of the queried cohort) and Chrna2=0.57 (cohort_pct 0.950) are both CONSISTENT. Npy=7.58 (cohort_pct 0.857) is CONSISTENT; Pnoc=2.51 is APPROXIMATE (cohort_pct 0.479, mid-cohort).
- **Annotation transfer.** F1=0.44 at the cluster rank (coverage=0.43, purity=0.45, n=10 cells mapped, median_bootstrap=1.0). This is the best cluster-rank F1 among the five SUPT_0216 children queried, but it falls below the 0.5 clean-mapping threshold.
- **Discovery context.** Score 10 (rank 1 of 5 in the rank-0 GABAergic / MBA:399 cohort), `next_best_score: 9` — moderately dominant within a small cohort.

**Concerns**

- **AT cluster-rank F1=0.44 is sub-threshold.** Caveat type `DISTRIBUTED_ACROSS_CLUSTERS`: Sst-OLM source cells scatter across CLUS_0768 (n=10), CLUS_0772 (n=4), and other siblings rather than concentrating on any single cluster. The cleaner AT signal lives at SUPT_0216 / SUBC_053 (F1≈0.67).
- Negative-marker DISCORDANCES (PV=3.12, CB=3.87, CR=2.30, NOS=0.76, VIP=0.31) — same transcript-vs-protein caveat as for the supertype.

**What would upgrade confidence**

- Larger patch-seq AT run (F1 ≥ 0.75 at cluster rank) — but the AT-run caveat suggests this is biologically infeasible at WMBv1 cluster resolution. The likely correct resolution is supertype-level.

### 0772 / 0773 / 0775 / 0770 Sst Gaba_3 (siblings under SUPT_0216) · 🔴 LOW

These four clusters are siblings of CLUS_0768 under the same supertype and share its broad Sst+/Chrna2+ profile. They are reported together because the OLM signal is genuinely distributed across them (per the AT-run caveat); none is independently a primary mapping.

**Supporting evidence (per cluster)**

- **CLUS_0772** (n_cells=190): Sst=11.92 (cohort_pct 0.958), Chrna2=0.46 (cohort_pct 0.933), Npy=8.22, region `region_fraction_100um: 0.706` — all CONSISTENT. AT F1=0.27 at cluster rank (n=4 cells mapped, median_bootstrap 0.735).
- **CLUS_0773** (n_cells=156): Sst=11.43 (cohort_pct 0.908), Chrna2=0.65 (cohort_pct 0.958), Pnoc=4.40 (cohort_pct 0.639 — CONSISTENT), region `region_fraction_100um: 0.648` — CONSISTENT. No AT evidence on this edge.
- **CLUS_0775** (n_cells=143): Sst=10.86, Chrna2=0.73 (cohort_pct 0.975 — highest in cohort), Pnoc=7.20 (cohort_pct 0.966 — strongest Pnoc signal in cohort). Region `region_fraction_100um: 0.442` — APPROXIMATE; the second-largest registered region for this cluster is Prosubiculum [MBA:484682470] with 59 cells *(note: prosubiculum is anatomically adjacent to CA1 stratum oriens, so this is plausibly boundary scatter rather than a distinct off-target population)*. The strong Chrna2 + Pnoc combination makes CLUS_0775 a candidate for the Pnoc-co-expressing OLM subcluster described by Thulin 2025 [9].
- **CLUS_0770** (n_cells=404): Sst=10.54, Chrna2=0.52, Pnoc=6.98 (cohort_pct 0.941 — CONSISTENT), region `region_fraction_100um: 0.506` — CONSISTENT. **Notably PV=0.00 (below MIN_DETECTABLE) — CONSISTENT** with the classical negative marker; the only cluster in the cohort where PV is genuinely absent at the transcript level. Also has the largest cell count (n=404).

**Concerns**

- AT only directly assessed for CLUS_0768 and CLUS_0772; CLUS_0773 / 0775 / 0770 have no AT evidence on these edges (the AT-run caveat says scatter is the rule, but per-cluster F1 outside the top hits is not recorded here).
- Negative-marker DISCORDANCES at the transcript level (except PV at CLUS_0770) — same transcript-vs-protein caveat as the supertype.
- CLUS_0775 has the lowest `region_fraction_100um` (0.442) of the SUPT_0216 children and the only non-CONSISTENT location alignment — interpret as boundary scatter into adjacent prosubiculum rather than a real off-target.

**What would upgrade confidence**

- Per-cluster AT F1 readouts at all five SUPT_0216 children from a larger OLM patch-seq dataset.
- Subtype-aware classical-node restructuring: Thulin 2025 [9] documents three Sst/Pnoc OLM subclusters with differential dorsal–ventral connectivity. The CLUS_0775 (high Pnoc) vs CLUS_0768/0772/0773 (low–mid Pnoc) vs CLUS_0770 (Pnoc-positive, PV-negative-at-transcript) distinction may map onto Thulin's subclusters; a follow-up cite-traverse on Thulin 2025 plus a dedicated mapping run would let us split the OLM classical node accordingly.

## Eliminated candidates

Four rank-1 Sst supertypes were retrieved as cohort members but are confidently eliminated by location:

- **CS20230722_SUPT_0226 (0226 Sst Gaba_13).** `region_fraction_100um: 0.016` (strict 0.008) — the dominant atlas region is Isocortex [MBA:315] with 1021 cells, with no meaningful hippocampal representation. Strong DISCORDANT: this is a cortical Sst supertype, not a hippocampal OLM candidate.
- **CS20230722_SUPT_0217 (0217 Sst Gaba_4).** `region_fraction_100um: 0.015` — dominant region Isocortex [MBA:315] (4066 cells), Secondary motor area [MBA:993] (583), Primary motor area [MBA:985] (494). Despite Chrna2=1.90 (cohort_pct 0.984 — even higher than any hippocampal candidate, and annotated as `DEFINING_SCOPED`), the cortical location makes this a different population. *(note: cortical Chrna2+/Sst+ interneurons are documented in non-hippocampal regions and would not be the CA1 OLM cells.)*
- **CS20230722_SUPT_0241 (0241 Sst Chodl Gaba_4).** `region_fraction_100um: 0.021` — dominant region Isocortex (1377 cells) and lateral forebrain bundle / corpus callosum. Additionally Chrna2=0.00 (below MIN_DETECTABLE; cohort_pct 0.000) — DISCORDANT on the second defining marker. Doubly disqualified.
- **CS20230722_SUPT_0224 (0224 Sst Gaba_11).** `region_fraction_100um: 0.032` — dominant region Isocortex (1077 cells); only 200 cells in Hippocampal formation. DISCORDANT.

Shared disqualifying signal: **all four have `region_fraction_100um` < 0.05 with dominant Isocortex localisation** — they are off-target by neuroanatomical region regardless of marker overlap.

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The OLM classical node has `definition_basis: CLASSICAL_MULTIMODAL`. Defining markers Sst, Chrna2, and mGluR1 (Grm1) are drawn from immunohistochemistry + biocytin morphology in rat [1][6], Chrna2-Cre transgenic + morphology in mouse [2][8], and the Winterer 2019 Cre-driver scRNA-seq dataset [7]. NT type is GABAergic [4][5]. Neuropeptides Sst, Npy, and Pnoc are drawn from [7] and [9]. Soma localisation in hippocampus stratum oriens [UBERON:0005371] with axon arbor in stratum lacunosum moleculare [UBERON:0007640] is established in [1][2][3].

**Atlas mapping query.**
Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CS20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**
Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE124847 (Sst-OLM, Htr3a-OLM; per-cell labels in source_cell_labels.json) |
| Source species | NCBITaxon:10090 (Mus musculus) |
| Target atlas | WMBv1 (CS20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization). Bootstrap-iteration assignment with default thresholds; per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 46 (filtered to 45) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md ((external; precomputed)) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix.csv`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/f1_matrix.csv) |
| Caveats | Source dataset has only 46 OLM cells (Winterer 2019); 45 retained after bootstrap filtering. The "Sst-OLM" and "Htr3a-OLM" source labels reflect Cre-driver subgroups in the Winterer dataset and are scored separately. At cluster (rank 0) resolution F1 is low across all candidates (max 0.26 for Sst-OLM → CLUS_0768 within Sst Gaba_3 supertype) — the OLM cell type is captured at supertype/subclass level (Sst Gaba_3 / Sst Gaba; F1 ≈ 0.65) but scatters across sibling clusters. This is a real biological signal, not a methodological failure: OLM is a transcriptomic subtype not yet resolved at WMBv1 cluster rank. |

**Anti-hallucination.**
All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `0934db5` at 2026-06-07T18:26:57+00:00 from [kb/graphs/hippocampus/_demo_olm_20260607.yaml](kb/graphs/hippocampus/_demo_olm_20260607.yaml).*

<details>
<summary>Evidence base table</summary>

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_olm_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0772 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0775 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0217 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0224 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

</details>

---

## Discussion

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) interneuron → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence. Key support: AT F1=0.67 at supertype rank (n=22 cells mapped; coverage 0.96) and CONSISTENT Sst (12.70 at CLUS_0768) / Chrna2 alignment. Key caveats: AMBIGUOUS_MAPPING from 5/5 negative-marker DISCORDANCES at the transcript level (interpreted as a transcript-vs-protein mismatch rather than a genuine identity contradiction) and DISTRIBUTED_ACROSS_CLUSTERS — the OLM signal genuinely scatters across the five SUPT_0216 children at WMBv1 cluster rank rather than concentrating on any single cluster (best cluster CLUS_0768, F1=0.44).

No Cell Ontology term currently assigned. This classical type is a candidate for a new CL term — the supertype-level granularity at which it cleanly maps to WMBv1 (`SUPT_0216`, "Sst Gaba_3") suggests a CL term scoped at the OLM level rather than the broader "GABAergic somatostatin interneuron of CA1" would be useful.

### Proposed experiments and follow-ups

- **Larger patch-seq AT run.** *What:* MapMyCells transfer of a morphology-confirmed OLM patch-seq dataset (n ≥ 100, ideally with Chrna2-Cre lineage) onto WMBv1 CS20230722. *Target:* F1 ≥ 0.75 at SUPT_0216 (already partially completed: the Winterer 2019 AT run at F1=0.67 supertype is undersized at n=45 cells). *Expected output:* a higher-purity `AnnotationTransferEvidence` item replacing the current run. *Resolves:* the AT-confidence ceiling on the primary mapping; would lift confidence to HIGH if F1 ≥ 0.75 holds.
- **Targeted IHC literature for negative markers.** *What:* cite-traverse for primary studies establishing protein-level absence of PV, CB, CR, NOS, VIP in morphology-confirmed OLM cells. *Expected output:* `MarkerSource` entries with `method: immunohistochemistry` attached to each classical negative marker. *Resolves:* the transcript-vs-protein interpretation of the negative-marker DISCORDANCES on the primary mapping.
- **Grm1 / mGluR1 atlas assessment.** *What:* extend Stage A `expression_detail` and `precomputed_expression` to include Grm1 at SUPT_0216 and its children. *Expected output:* `MarkerAnalysisEvidence` for the third defining marker. *Resolves:* the NOT_ASSESSED gap on mGluR1 across all hippocampal candidates.
- **OLM subcluster split.** *What:* dedicated cite-traverse on Thulin et al. 2025 [9] (three Sst/Pnoc OLM subclusters with differential dorsal–ventral connectivity), plus a follow-up mapping run with sub-typed classical nodes against the SUPT_0216 children. *Expected output:* multiple `MappingEdge` records at cluster rank with sub-typed classical sources. *Resolves:* the DISTRIBUTED_ACROSS_CLUSTERS caveat by splitting the OLM classical node along documented heterogeneity (Pnoc-high CLUS_0775 vs PV-transcript-absent CLUS_0770 vs the others).

### Open questions

1. Are the cluster-rank DISCORDANCES on PV/CB/CR/NOS/VIP at SUPT_0216's children true contradictions (some atlas Sst Gaba_3 child clusters might be non-OLM Sst+ interneurons) or transcript-vs-protein discordances? A primary-IHC cite-traverse on morphology-confirmed OLM cells would discriminate.
2. Does the Pnoc-high signature at CLUS_0775 (and CLUS_0770) correspond to the Sst/Pnoc co-expressing OLM subclusters described by Thulin 2025 [9]?
3. Is Grm1 (mGluR1) expression detectable in the WMBv1 SUPT_0216 dataset at all, and at which child clusters? Resolves the only un-assessable defining marker.
4. Should the OLM classical node be split into sub-types (e.g. Pnoc-high vs PV-positive-gamma-firing per Zhang 2025, noted in classical-node `notes`) to better match the WMBv1 cluster-rank structure?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280) | soma location, morphology |
| [2] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503) | soma location, Chrna2 marker |
| [3] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464) | soma / dendrite location |
| [4] | Böhm et al. 2015 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702) | NT type (GABAergic) |
| [5] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798) | Sst marker / NT |
| [6] | Hooft et al. 2000 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195) | Sst, mGluR1 markers + morphology |
| [7] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995) | Sst marker, Npy, function (source of present AT dataset) |
| [8] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082) | Chrna2 marker (Cre-driver) |
| [9] | Thulin et al. 2025 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734) | Pnoc neuropeptide, Sst/Pnoc OLM subclusters |

---

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  rationale: >
    Primary mapping at supertype rank. AT F1=0.67 in `at_run_20260408_winterer_olm_mmc_wmbv1`
    (MapMyCells, scRNA-seq source; n=22 cells mapped, coverage 0.96, purity 0.51 at
    CS20230722_SUPT_0216); 5 of 11 marker_-prefixed comparisons CONSISTENT (Sst 11.44 cohort_pct 0.905,
    Chrna2 0.61 cohort_pct 0.952; mGluR1/Grm1 NOT_ASSESSED — absent from atlas
    precomputed_expression); region CONSISTENT with `region_fraction_100um: 0.539` and
    strict region_fraction 0.305. Five negative-marker comparisons (PV/CB/CR/NOS/VIP)
    are DISCORDANT at the transcript level (MapMyCells / scRNA-seq atlas modality
    vs the classical protein-level negative claim). Confidence capped at MODERATE
    because F1 < 0.75 HIGH threshold and the AT source dataset is small (n=45 cells
    after filter).
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship` from mechanical Stage B emitter
    is inconsistent with the rubric: AT F1=0.67 + two defining markers CONSISTENT +
    region CONSISTENT supports `skos:closeMatch` (1:1 shape with documented
    transcript-vs-protein negative-marker contradictions). Curator-review should
    migrate the predicate.
  unresolved_questions:
    - Targeted IHC cite-traverse for primary studies of PV/CB/CR/NOS/VIP absence in morphology-confirmed OLM cells, to discriminate transcript-vs-protein discordance from true marker contradiction.
    - Extend Stage A expression_detail / precomputed_expression to include Grm1 (mGluR1) at SUPT_0216 and its children — currently the only un-assessable defining marker.
    - Repeat MapMyCells AT with a larger morphology-confirmed OLM patch-seq dataset (n ≥ 100); target F1 ≥ 0.75 at SUPT_0216 to lift confidence to HIGH.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.40
  rationale: >
    Best cluster-rank candidate under SUPT_0216 but AT F1=0.44 in
    `at_run_20260408_winterer_olm_mmc_wmbv1` (MapMyCells; n=10 cells mapped, coverage
    0.43, purity 0.45) is below the 0.5 clean-mapping threshold. Sst (12.70,
    cohort_pct 0.992) and Chrna2 (0.57, cohort_pct 0.950) CONSISTENT; 4 of 11 marker_-prefixed comparisons
    CONSISTENT (mGluR1 NOT_ASSESSED); region CONSISTENT with `region_fraction_100um:
    0.818` (strict 0.458). Five negative-marker comparisons DISCORDANT at the
    transcript level. Caveat DISTRIBUTED_ACROSS_CLUSTERS: per AT-run notes the OLM
    signal genuinely scatters across SUPT_0216's children at WMBv1 cluster rank.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship`; rubric supports
    `skos:closeMatch` for the 1:1 shape with sub-threshold AT and documented
    contradictions, but the rank-0 mapping is better expressed as a child of the
    SUPT_0216 primary mapping rather than as an independent close match. Curator-review
    may prefer to leave it as `evidencell:UncertainRelationship` at cluster rank
    pending a larger AT run.
  unresolved_questions:
    - Whether CLUS_0768 vs CLUS_0772/0773/0775/0770 distinction corresponds to Thulin 2025 Sst/Pnoc OLM subclusters; would resolve the cluster-rank scatter.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    Sibling cluster of CLUS_0768 under SUPT_0216. AT F1=0.27 at cluster rank in
    `at_run_20260408_winterer_olm_mmc_wmbv1` (n=4 cells mapped, coverage 0.17,
    purity 0.57, median_bootstrap 0.735). Sst (11.92, cohort_pct 0.958) and
    Chrna2 (0.46, cohort_pct 0.933) CONSISTENT; 4 of 11 marker_-prefixed comparisons CONSISTENT
    (mGluR1 NOT_ASSESSED); region CONSISTENT with `region_fraction_100um: 0.706`
    (strict 0.527). Five negative-marker comparisons DISCORDANT at transcript level.
    Caveat DISTRIBUTED_ACROSS_CLUSTERS — this is one of the destination clusters
    receiving scattered Sst-OLM source cells, not a primary mapping in its own right.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship`; rubric supports
    `skos:closeMatch` as a child-of-primary mapping but the low cluster-rank AT F1
    keeps confidence LOW.
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    Sibling cluster of CLUS_0768 under SUPT_0216. No AT evidence on this edge;
    relies on ATLAS_METADATA. Sst (11.43, cohort_pct 0.908) and Chrna2 (0.65,
    cohort_pct 0.958) CONSISTENT; 4 of 11 marker_-prefixed comparisons CONSISTENT (mGluR1 NOT_ASSESSED);
    Pnoc 4.40 (cohort_pct 0.639) CONSISTENT; region CONSISTENT with
    `region_fraction_100um: 0.648` (strict 0.355). Five negative-marker comparisons
    DISCORDANT at transcript level. LOW because AT was not assessed for this cluster
    and the SUPT_0216-level AT-run caveat says cluster-rank signal scatters.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship`; rubric supports
    `skos:closeMatch` as a child-of-primary mapping pending per-cluster AT F1.
  unresolved_questions:
    - Compute per-cluster AT F1 for CLUS_0773 (currently no AT evidence on this edge).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0775 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    Sibling cluster of CLUS_0768 under SUPT_0216 with the cohort's strongest
    Chrna2 (0.73, cohort_pct 0.975) and Pnoc (7.20, cohort_pct 0.966) signal —
    plausibly the Sst/Pnoc OLM subcluster described in Thulin 2025 [9]. No AT
    evidence on this edge. 5 of 11 marker_-prefixed comparisons CONSISTENT (mGluR1 NOT_ASSESSED). Location
    APPROXIMATE: `region_fraction_100um: 0.442` (boundary scatter — second-largest
    registered region is Prosubiculum [MBA:484682470], anatomically adjacent to
    CA1 stratum oriens; weak counter-evidence). Five negative-marker comparisons
    DISCORDANT at transcript level.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship`; rubric supports
    `skos:closeMatch` as a Pnoc-high candidate child-of-primary mapping pending
    per-cluster AT F1 and a Thulin-subcluster-aware re-mapping.
  unresolved_questions:
    - Does CLUS_0775 (Pnoc cohort_pct 0.966) correspond to the Sst/Pnoc OLM subcluster of Thulin 2025? A subtype-aware mapping pass would resolve this.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.32
  rationale: >
    Sibling cluster of CLUS_0768 under SUPT_0216 with the largest cell count (404)
    and — notably — PV=0.00 (below MIN_DETECTABLE) CONSISTENT with the classical
    negative marker, the only cluster in the cohort where PV negative is supported
    at the transcript level. No AT evidence on this edge. Sst (10.54, cohort_pct
    0.807) and Chrna2 (0.52, cohort_pct 0.941) CONSISTENT; 5 of 11 marker_-prefixed comparisons
    CONSISTENT (mGluR1 NOT_ASSESSED); Pnoc 6.98 (cohort_pct 0.941) CONSISTENT;
    region CONSISTENT `region_fraction_100um: 0.506` (strict 0.302). Remaining four
    negative-marker comparisons (CB/CR/NOS/VIP) DISCORDANT at transcript level.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship`; rubric supports
    `skos:closeMatch` as a child-of-primary mapping. CLUS_0770 is the cohort's
    strongest cluster-rank candidate by the transcript-level negative-marker check
    (PV genuinely absent) but lacks per-cluster AT support.
  unresolved_questions:
    - Compute per-cluster AT F1 for CLUS_0770 (no AT evidence on this edge currently); the PV-transcript-absent profile makes it the strongest cluster-rank candidate by the negative-marker rubric.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Eliminated by location. `region_fraction_100um: 0.016` (strict 0.008); dominant
    atlas region Isocortex [MBA:315] with 1021 cells, no meaningful hippocampal
    representation. Despite Sst (12.08, cohort_pct 0.968 — DEFINING in atlas) and
    Chrna2 (0.61, cohort_pct 0.952) CONSISTENT, this is a cortical Sst supertype,
    not the hippocampal OLM target. 5 of 11 marker_-prefixed comparisons CONSISTENT but neuroanatomically
    off-target.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship` is correct under the
    rubric (location DISCORDANT to a distant region disqualifies it for the
    hippocampus-specific OLM mapping).
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0217 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Eliminated by location. `region_fraction_100um: 0.015` (strict 0.009); dominant
    atlas region Isocortex [MBA:315] (4066 cells), Secondary motor area, Primary motor
    area. Sst (10.79) and Chrna2 (1.90, cohort_pct 0.984 — DEFINING_SCOPED) both
    CONSISTENT but the cortical motor-area localisation makes this a different
    population from CA1 OLM. 4 of 11 marker_-prefixed comparisons CONSISTENT but neuroanatomically off-target.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship` is correct under the
    rubric (distant region disqualifies).
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.03
  rationale: >
    Doubly eliminated. Location DISCORDANT: `region_fraction_100um: 0.021` (strict
    0.008); dominant atlas region Isocortex [MBA:315] (1377 cells), lateral forebrain
    bundle, corpus callosum. Additionally Chrna2=0.00 (below MIN_DETECTABLE; cohort_pct
    0.000) DISCORDANT on the second defining marker. 4 of 11 marker_-prefixed comparisons CONSISTENT (Sst at 12.33 among them, but Chrna2 DISCORDANT). Not a hippocampal OLM candidate.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship` is correct under the
    rubric (distant region + Chrna2 negative).
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0224 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Eliminated by location. `region_fraction_100um: 0.032` (strict 0.010); dominant
    atlas region Isocortex [MBA:315] (1077 cells); only 200 cells in Hippocampal
    formation. Sst (10.65) and Chrna2 (0.10, cohort_pct 0.905 but child-coverage
    only 0.500) CONSISTENT; 4 of 11 marker_-prefixed comparisons CONSISTENT (mGluR1 NOT_ASSESSED) but
    cortical localisation disqualifies for the CA1 OLM mapping.
  reconciliation_note: >
    Inherited predicate `evidencell:UncertainRelationship` is correct under the
    rubric (distant region disqualifies).
  unresolved_questions: []
```
<!-- verdict-block-end -->
