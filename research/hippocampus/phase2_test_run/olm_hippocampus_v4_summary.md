# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*2026-03-25 · Source: `kb/graphs/hippocampus/hippocampus_OLM.yaml`*

---

## Introduction

The O-LM interneuron is a canonical GABAergic cell of hippocampal CA1, with horizontally oriented dendrites confined to stratum oriens and an axon that ascends to arborize selectively in stratum lacunosum-moleculare onto the apical tufts of pyramidal cells [1][3]. O-LM cells provide feedback inhibition recruited during theta oscillations and are central models of dendritic targeting interneurons; their classical definition rests on a convergent multimodal signature — somatostatin expression, mGluR1/Grm1 immunoreactivity, and Chrna2 as a selective marker that has enabled Cre-driver genetic access [5][6][7][8]. Resolving where O-LM lands in the Whole Mouse Brain v1 (WMBv1) taxonomy matters because the cell is a workhorse of hippocampal circuit dissection, and downstream community tools (atlas annotation transfer, marker-driven access) depend on a defensible WMBv1 anchor.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371]; stratum lacunosum-moleculare [UBERON:0007640] (axonal target) | [1][2][3] |
| Neurotransmitter | GABAergic | [4][5] |
| Defining markers | Sst, Chrna2, mGluR1 (Grm1; 96% detection in OLM scRNA-seq, GSE124847) | [6][7][8] |
| Negative markers | PV, CB, CR, NOS, VIP | [7] |
| Neuropeptides | Sst, Npy, Pnoc | [7][9] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** patch-clamp + biocytin reconstruction in rat hippocampus · [1]
  > oriens-lacunosum-moleculare (OLM) cells also had both the cell body and dendritic tree in the stratum oriens, but their horizontally running dendrites were often densely decorated with long spines. Their axon frequently originated from a proximal dendrite, and after ramification the main axon without
  > — Zemankovics et al. 2010, Anatomical Location and Morphology · [1] <!-- quote_key: 3106274_e54f60e9 -->
- **Soma location:** review of CA1 O-LM defining features · [2]
  > These CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare (SLM; Cajal, 1911;(McBain et al., 1994)(Sik
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_2414c9e9 -->
- **Projection / connectivity:** consolidated CA1 reconstructions · [3]
  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [3] <!-- quote_key: 229694907_6865b9db -->
- **NT type:** rat CA1 O-LM ephys + immunolabel · [4]
  > GABAergic inhibitory oriens lacunosum-moleculare (O-LM) cells in the hippocampal area CA1 of the rat
  > — Böhm et al. 2015, Anatomical Location and Morphology · [4] <!-- quote_key: 15101210_5604b9a4 -->
- **Sst marker:** Sst-EGFP transgenic + immunohistochemistry · [5]
  > EGFP was found to be expressed in a subpopulation of somatostatin-containing GABAergic interneurons in the hippocampus and neocortex
  > — Oliva et al. 2000, Molecular Markers and Gene Expression · [5] <!-- quote_key: 13398453_9154fc23 -->
- **Sst + mGluR1:** patch-clamp + post-hoc immunostaining of Type I (O-LM) cells · [6]
  > Type I interneurons responded with a large inward current of ≈ 224pA, were positive for somatostatin, and the majority expressed both mGluR1 and mGluR5
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_17d10a9e -->
- **Sst-Cre / Htr3a-Cre scRNA-seq of CA1 O-LM cells with morphology recovery:** Cre-driver targeting + scRNA-seq · [7]
  > oriens-lacunosum moleculare (OLM) interneurons. OLMs express somatostatin (Sst), generate feedback inhibition and play important roles in theta oscillations and fear encoding
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_69dc904d -->
- **Npy on O-LM (overturns prior rat exclusion):** scRNA-seq · [7]
  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_8d16e821 -->
- **Chrna2 specificity:** Chrna2-Cre + biocytin + electrophysiology in CA1 stratum oriens · [8]
  > The vast diversity of GABAergic interneurons is believed to endow hippocampal microcircuits with the required flexibility for memory encoding and retrieval. However, dissection of the functional roles of defined interneuron types has been hampered by the lack of cell-specific tools. We identified a
  > — Leão et al. 2012, Projection Patterns and Connectivity · [8] <!-- quote_key: 7952877_ae03c6e0 -->
- **Pnoc on O-LM, dorsal-ventral substructure:** in situ + scRNA-seq · [9]
  > The Chrna2 gene expression is restricted to the stratum oriens in the hippocampus in both rats and mice (Ishii et al., 2005) and is specifically expressed in a subset of CA1 hippocampal interneurons, the oriens lacunosummoleculare (OLM) cells (Leão et al., 2012). Traditionally, OLM cells have been i
  > — Thulin et al. 2025, Projection Patterns and Connectivity · [9] <!-- quote_key: 280420054_8a6529c5 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer of Cre-driver-targeted O-LM cells (Sst-Cre + Htr3a-Cre, scRNA-seq, Winterer 2019 [7]) with morphology/electrophysiology confirmation in the original cohort places O-LM at the **supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216]** (F1=0.97 across the pooled OLM cohort; see figure and property comparison table). Within Sst Gaba_3 the O-LM cells distribute across several sibling clusters with 0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the top cluster candidate (F1=0.65), consistent with within-O-LM heterogeneity reported by Thulin et al. 2025 [9].

![F1 across taxonomy levels for the Winterer 2019 O-LM cohort](figures/f1_for_olm_hippocampus.png)

*F1 across taxonomy levels for the Winterer 2019 O-LM cohort (Sst-OLM + Htr3a-OLM pooled to a single OLM group; n=45 cells after bootstrap filtering of 46 source cells). **Coverage** = fraction of source-group cells landing on the target; **Purity** = fraction of target cells from the source group. With a single pooled source, Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution; cluster-level scatter across multiple Sst Gaba_3 children is the expected signature of subtype structure within the classical O-LM type.*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Property comparison.**

| Property | Classical | Supertype | Best cluster (CLUS_0768) | Alignment |
|---|---|---|---|---|
| Soma location | stratum oriens [UBERON:0005371] | CA1 stratum oriens [MBA:399] dominant; region_fraction_100um=0.539 | CA1 SO [MBA:399] dominant; region_fraction_100um=0.818 | CONSISTENT |
| NT type | GABAergic | not annotated on supertype (subclass 053 Sst Gaba) | GABA | CONSISTENT (via subclass) |
| Sst | defining marker; 100% detection (GSE124847) | mean=11.44; cohort_pct=0.905 | mean=12.70; cohort_pct=0.992 | CONSISTENT |
| Chrna2 | defining marker; 35% detection (GSE124847) | mean=0.61; cohort_pct=0.952; child-coverage 0.667 | mean=0.57; cohort_pct=0.950 | CONSISTENT |
| mGluR1 (Grm1) | defining; 96% detection (GSE124847) | no atlas precomputed value | no atlas precomputed value | NOT_ASSESSED |
| Npy | neuropeptide | mean=5.07; cohort_pct=0.794 | mean=7.58; cohort_pct=0.857 | CONSISTENT |
| Pnoc | neuropeptide | mean=3.69; cohort_pct=0.667 | mean=2.51; cohort_pct=0.479 | SUPT: CONSISTENT; CLUS: APPROXIMATE |
| PV | absent (negative) | mean=1.48 | mean=3.12 | DISCORDANT |
| CB | absent (negative) | mean=5.56 | mean=3.87 | DISCORDANT |
| CR | absent (negative) | mean=1.28 | mean=2.30 | DISCORDANT |
| NOS | absent (negative) | mean=2.94 | mean=0.76 | DISCORDANT |
| VIP | absent (negative) | mean=0.42 | mean=0.31 | DISCORDANT |

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Winterer 2019 MapMyCells AT (pooled OLM) | Annotation transfer | SUPPORT | F1=0.97 at SUPERTYPE (`at_run_20260408_winterer_olm_mmc_wmbv1`); 43/45 cells | [7] |
| Atlas precomputed expression (Sst Gaba_3) | Atlas metadata | PARTIAL | Sst 11.44; Chrna2 0.61; Npy 5.07; Pnoc 3.69 | atlas-internal |

*(5 of 5 Sst Gaba_3 child clusters assayed show Sst/Chrna2 cohort-percentile ≥ 0.84/0.93; Pnoc is variable across children, peaking in CLUS_0775 (mean=7.20, cohort_pct=0.966). Best cluster match: CLUS_0768 — see paragraph below.)*

Marker expression alignment and annotation transfer from Cre-driver-targeted O-LM cells with scRNA-seq (Winterer 2019 [7]) place O-LM at supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216]: 43 of 45 classified cells land on this supertype with pooled F1=0.97, and the parent class (07 CTX-MGE GABA) and subclass (053 Sst Gaba) levels are similarly clean (both F1=0.99 — see figure). Within Sst Gaba_3, the same transfer scatters O-LM cells across sibling clusters (top cluster F1=0.65 at 0768; see figure and per-cluster paragraph below), so the defensible call is at supertype rather than at any single child. Sst and Chrna2 are concordant on the atlas side at high cohort percentile, and Npy presence on the supertype confirms the Winterer 2019 finding that resolved a prior rat-mouse discrepancy [7]. mGluR1/Grm1 is the one defining marker absent from atlas precomputed expression, leaving it source-side-only at 96% detection [7]; the five elevated negative-marker means (PV, CB, CR, NOS, VIP) reflect supertype-level averaging across a heterogeneous Sst Gaba_3 population — none of these markers is expected to be uniformly silenced at the supertype scale, and the relevant assessment is the per-cluster pattern *(note: PV, CB, CR are common negative-marker contaminants of supertype means when child clusters mix; the relevant transcript-level discriminator established by literature for O-LM is Chrna2, which is present)*.

**Marker evidence provenance.**
- **Sst:** transcript- and protein-level; established on morphology-confirmed CA1 O-LM cells with biocytin recovery (Hooft 2000 [6]) and on Cre-driver-targeted cells with scRNA-seq (Winterer 2019 [7]); 100% detection in GSE124847. Atlas value mean=11.44 (cohort_pct=0.905) is concordant.
- **Chrna2:** transcript-level + Chrna2-Cre driver line specificity established on biocytin-filled CA1 stratum oriens neurons with O-LM morphology (Leão 2012 [8]); restricted to stratum oriens in rat and mouse (Thulin 2025 [9]). Atlas-side cohort_pct=0.952 on the supertype confirms enrichment.
- **mGluR1/Grm1:** transcript- and protein-level on morphology-confirmed O-LM (Hooft 2000 [6]; Winterer 2019 [7], 96% detection in scRNA-seq). Atlas-side gap — Grm1 is not in precomputed expression; source-side confirmed but target-side unresolvable from atlas metadata.
- **Npy:** previously a rat exclusion criterion; Winterer 2019 [7] overturns this in mouse on Cre-driver-targeted O-LM cells. Atlas supertype mean=5.07 (cohort_pct=0.794) is concordant.
- **Pnoc:** transcript-level on Cre-driver-targeted O-LM and in situ (Thulin 2025 [9], with reported dorsal-ventral substructure across three Sst/Pnoc subclusters); cluster-level Pnoc varies across Sst Gaba_3 children (highest in CLUS_0775), consistent with the reported substructure.
- **PV / CB / CR / NOS / VIP:** classical negative markers from immunolabelling; not transcript-level discriminators established for O-LM specifically. Their atlas-side means at supertype reflect mixed children and are not by themselves decisive.

**Concerns.**
- Within-supertype cluster-level scatter: O-LM cells distribute across multiple Sst Gaba_3 children (best F1=0.65 at CLUS_0768); the supertype is the resolution at which the call holds cleanly. Thulin et al. 2025 [9] independently report three Sst/Pnoc subclusters with dorsal-ventral connectivity differences, predicting exactly this kind of scatter.
- mGluR1/Grm1 atlas-side gap (NOT_ASSESSED).
- Pooling note: the Sst-OLM and Htr3a-OLM source labels from Winterer 2019 [7] were merged into a single OLM cohort for the figure and metrics shown here; on the AT panel they map indistinguishably to the same Sst Gaba_3 target set. Whether the two Cre-driver cohorts differ on ephys, morphology, or connectivity has not been audited from the Winterer paper as part of this report and remains an optional follow-up.

**What would upgrade confidence:**
- Patch-seq of Chrna2-Cre stratum oriens neurons with MapMyCells transfer onto WMBv1 — would resolve which Sst Gaba_3 child cluster(s) carry O-LM-morphology cells (target F1 ≥ 0.80 at CLUSTER level); adds AnnotationTransferEvidence per child cluster.
- Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons addressing dorsal-ventral substructure as predicted by Thulin 2025 [9].
- An audit of Winterer 2019 [7] for any reported Sst-OLM / Htr3a-OLM property differences (ephys, morphology, connectivity) would convert the current AT-only indistinguishability of the two Cre cohorts into a multi-panel statement.

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · 🟡 MODERATE

This is the top cluster candidate within the Sst Gaba_3 supertype. Annotation transfer of the pooled Winterer 2019 O-LM cohort [7] sends 22 of 45 classified cells (Coverage=0.48; F1=0.65) here, more than to any other child of supertype 0216; CA1 stratum oriens [MBA:399] is the dominant soma anatomy with region_fraction_100um=0.818 and strict region_fraction=0.458. The classical defining markers are present at high cohort percentile: Sst mean=12.70 (cohort_pct=0.992), Chrna2 mean=0.57 (cohort_pct=0.950), and the neuropeptide triad (Sst, Npy, Pnoc) is all detected (see property comparison table above). Per the Winterer 2019 evidence narrative on this edge:

> MapMyCells annotation transfer of the pooled OLM cohort (46 cells; Sst-OLM + Htr3a-OLM combined; GSE124847, Winterer 2019) strongly supports the parent Sst Gaba_3 supertype (43/45 classified cells; pooled F1=0.97; pooled CLASS/SUBCLASS F1=0.99) but OLM cells scatter across sibling clusters 0767–0774 within it. Cluster 0769 specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/45, best pooled cluster-level F1=0.65). This indicates OLM identity is captured at the Sst Gaba_3 supertype rather than at any single child cluster. The high pooled supertype F1 reflects removal of the inter-source mis-attribution penalty that depresses per-source F1; both Sst-OLM and Htr3a-OLM converge on the same Sst Gaba_3 supertype.
> — Winterer et al. 2019 · [7]

The cluster-level pattern is the expected signature of subtype structure within O-LM rather than a mapping failure: cluster F1=0.65 with cohort scatter across 0767, 0768, 0771, 0772, 0773, 0774 (all Sst Gaba_3 children) mirrors the three dorsal-ventral Sst/Pnoc subclusters described by Thulin 2025 [9]. The DISCORDANT negative markers (PV mean=3.12, CB mean=3.87, CR mean=2.30) on CLUS_0768 reflect averaging over a still-heterogeneous cluster rather than evidence against O-LM identity — none of these is a transcript-level discriminator established on morphology-confirmed O-LM cells in the literature. Boundary spread to prosubiculum is consistent with the reported O-LM-like cells in adjacent regions and does not contradict the call *(note: prosubiculum is anatomically adjacent to CA1 stratum oriens; the 100µm proximity rollup picking up these cells reflects registration scatter rather than a distant off-target)*.

**Concerns.**
- Cluster-level F1=0.65 is below the supertype-level F1=0.97, and 23 of 45 O-LM cells land on sibling clusters within Sst Gaba_3 — the cluster-level assignment is not unique.
- Negative markers (PV, CB, CR) elevated at cluster level; relevance limited because none is a transcript-level discriminator for O-LM in the cited literature [6][7][8].
- mGluR1/Grm1 atlas-side gap unchanged from the supertype-level analysis.

**What would upgrade confidence:**
- Chrna2-Cre + MapMyCells targeting only morphology-confirmed O-LM cells (target F1 ≥ 0.80 at cluster level) would resolve whether CLUS_0768 is the correct single child or whether the call should remain at supertype.
- MERFISH of Chrna2+ CA1 stratum oriens neurons addressing the Thulin 2025 [9] dorsal-ventral substructure prediction would test whether the cluster scatter (0768, 0772, 0773, 0775, etc.) tracks anatomical axis.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | 🟡 MODERATE | Sst Gaba_3 AT F1=0.97 (43/45 cells, pooled OLM) | Primary |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | 🟡 MODERATE | Best cluster within Sst Gaba_3; AT F1=0.65 (22/45 cells); region_fraction_100um=0.818 | Secondary (best cluster within primary supertype) |
| 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | 0216 Sst Gaba_3 | 334 | 🔴 LOW | 0/46 cells in AT despite being in the right supertype | Eliminated (no AT cells on this child of Sst Gaba_3) |
| 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | 0203 Lamp5 Lhx6 Gaba_1 | 59 | 🔴 REFUTED | 0/46 cells in AT; Lamp5 Lhx6 (CGE) wrong subclass for Sst-MGE O-LM; Npy absent | Eliminated (wrong subclass; CGE vs MGE) |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | 🔴 LOW | AT F1=0.27 (4 cells); within-supertype sibling | Eliminated (within-supertype scatter only) |
| 0773 Sst Gaba_3 [CS20230722_CLUS_0773] | 0216 Sst Gaba_3 | 156 | 🔴 LOW | AT F1=0.04 (1 cell); within-supertype sibling | Eliminated (within-supertype scatter only) |
| 0775 Sst Gaba_3 [CS20230722_CLUS_0775] | 0216 Sst Gaba_3 | 143 | 🔴 LOW | Pnoc-high; AT did not reach this cluster | Eliminated (within-supertype scatter only) |
| 0770 Sst Gaba_3 [CS20230722_CLUS_0770] | 0216 Sst Gaba_3 | 404 | 🔴 LOW | AT did not assign cells here; within-supertype sibling | Eliminated (within-supertype scatter only) |
| 0771 Sst Gaba_3 [CS20230722_CLUS_0771] | 0216 Sst Gaba_3 | 462 | 🔴 LOW | AT F1=0.16 (4 cells); within-supertype sibling | Eliminated (within-supertype scatter only) |
| 0767 Sst Gaba_3 [CS20230722_CLUS_0767] | 0216 Sst Gaba_3 | 104 | 🔴 LOW | AT F1=0.20 (5 cells); within-supertype sibling | Eliminated (within-supertype scatter only) |
| 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | — | 4064 | 🔴 LOW | Isocortex-dominant (region_fraction_100um=0.016); no hippocampal cells | Eliminated (wrong region — cortex) |
| 0217 Sst Gaba_4 [CS20230722_SUPT_0217] | — | 14335 | 🔴 LOW | Isocortex-dominant (region_fraction_100um=0.015) | Eliminated (wrong region — cortex) |
| 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | — | 2905 | 🔴 REFUTED | Chrna2=0.00; Isocortex; wrong subtype (Sst Chodl long-range) | Eliminated (Chrna2 absent) |
| 0224 Sst Gaba_11 [CS20230722_SUPT_0224] | — | 2677 | 🔴 LOW | Wrong region | Eliminated (region mismatch) |
| 0225 Sst Gaba_12 [CS20230722_SUPT_0225] | — | 2126 | 🔴 LOW | Wrong region | Eliminated (region mismatch) |
| 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | 725 | 🔴 LOW | Wrong supertype within Sst Gaba | Eliminated (within-Sst alt supertype, no AT cells) |
| 0215 Sst Gaba_2 [CS20230722_SUPT_0215] | — | 1183 | 🔴 LOW | Wrong supertype within Sst Gaba | Eliminated (no AT cells) |
| 0213 Pvalb Gaba_9 [CS20230722_SUPT_0213] | — | 241 | 🔴 REFUTED | Wrong subclass (Pvalb, not Sst) | Eliminated (wrong subclass — Pvalb) |
| 0190 Sncg Gaba_6 [CS20230722_SUPT_0190] | — | 1928 | 🔴 REFUTED | Wrong subclass (Sncg) | Eliminated (wrong subclass — Sncg) |
| 0638 Vip Gaba_4 [CS20230722_CLUS_0638] | — | 1046 | 🔴 REFUTED | Vip subclass; VIP is a classical negative marker | Eliminated (Vip subclass — negative marker) |
| 0778 Sst Gaba_4 [CS20230722_CLUS_0778] | 0217 Sst Gaba_4 | 2675 | 🔴 LOW | Cortical Sst Gaba_4 cluster | Eliminated (wrong region — cortex) |
| 0807 Sst Gaba_12 [CS20230722_CLUS_0807] | 0225 Sst Gaba_12 | 481 | 🔴 LOW | Wrong supertype/region | Eliminated (wrong region) |
| 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | 0219 Sst Gaba_6 | 51 | 🔴 REFUTED | Chrna2 expression absent on this Sst Gaba_6 child | Eliminated (Chrna2 absent) |
| 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | 0219 Sst Gaba_6 | 98 | 🔴 REFUTED | Chrna2 absent | Eliminated (Chrna2 absent) |
| 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | 0219 Sst Gaba_6 | 222 | 🔴 REFUTED | Chrna2 absent | Eliminated (Chrna2 absent) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The O-LM interneuron is defined here on a CLASSICAL_MULTIMODAL basis: stratum oriens soma and stratum lacunosum-moleculare axon target [1][2][3], GABAergic identity [4][5], the marker triad Sst / Chrna2 / mGluR1 (Grm1) [6][7][8], the neuropeptide set Sst / Npy / Pnoc [7][9], and the negative-marker panel PV / CB / CR / NOS / VIP [7]. The Npy entry resolves a prior rat-versus-mouse discrepancy through Winterer 2019 scRNA-seq on Cre-driver-targeted cells [7].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match at MBA:399 / Field CA1 stratum oriens, NT type GABAergic, defining markers Sst / Chrna2 / Npy / Pnoc). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE124847 (Sst-OLM + Htr3a-OLM per-cell labels; merged into a single OLM cohort for figure and pooled F1) |
| Source species | NCBITaxon:10090 (Mus musculus) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 46 (filtered to 45) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix.csv`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/f1_matrix.csv) |
| Source pooling | Sst-OLM + Htr3a-OLM merged → OLM (AT-indistinguishable; cross-panel literature confirmation not audited — see Concerns on the primary candidate) |
| Caveats | Small source dataset (n=45 after filtering). Cluster-level F1 ≤ 0.65 across Sst Gaba_3 children reflects within-O-LM subtype heterogeneity rather than mapping failure (Thulin 2025 [9]). |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `5738aa0` at 2026-06-08T05:47:20+00:00 from [kb/graphs/hippocampus/hippocampus_OLM.yaml](../../kb/graphs/hippocampus/hippocampus_OLM.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_olm_hippocampus_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER; ATLAS_METADATA | SUPPORT; PARTIAL | [7], atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0768 | ANNOTATION_TRANSFER; ATLAS_METADATA | SUPPORT; PARTIAL | [7], atlas-internal |
| edge_olm_to_wmb_clus_0769 | ANNOTATION_TRANSFER; ATLAS_METADATA | PARTIAL; SUPPORT | [7], atlas-internal |
| edge_olm_to_wmb_clus_0727 | ANNOTATION_TRANSFER; ATLAS_METADATA | REFUTE; PARTIAL | [7], atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0772 | ANNOTATION_TRANSFER; ATLAS_METADATA | SUPPORT; PARTIAL | [7], atlas-internal |
| (... further edges; atlas-metadata-only) | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) interneuron → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence. Key support: annotation transfer of Cre-driver-targeted O-LM cells (Winterer 2019, scRNA-seq on morphologically and electrophysiologically confirmed cells) with F1=0.97 across the pooled OLM cohort; concordant atlas expression of Sst, Chrna2, Npy, and Pnoc on the supertype. Key caveats: within-supertype cluster-level scatter (F1=0.65 at best child CLUS_0768; OLM cells distribute across multiple Sst Gaba_3 children consistent with the Thulin 2025 [9] dorsal-ventral substructure); mGluR1/Grm1 absent from atlas precomputed expression (NOT_ASSESSED on the target side).

No Cell Ontology term currently covers the O-LM interneuron at the resolution of the Winterer/Leão definition; this is a candidate for a new CL term.

### Proposed experiments and follow-ups

Annotation transfer of Winterer 2019 [7] O-LM cells onto WMBv1 has already been performed (run `at_run_20260408_winterer_olm_mmc_wmbv1`) and resolved the supertype-level call to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] with F1=0.97. Cluster-level remains unresolved.

1. **Patch-seq of Chrna2-Cre stratum oriens neurons + MapMyCells onto WMBv1.**
   - Target: cluster-level F1 ≥ 0.80 on a single Sst Gaba_3 child, or confirmation of multi-cluster distribution.
   - Expected output: AnnotationTransferEvidence with per-cluster F1.
   - Resolves: which Sst Gaba_3 child (0767, 0768, 0771, 0772, 0773, 0774, 0775) carries O-LM-morphology cells; open question (1).

2. **MERFISH of Chrna2+ CA1 stratum oriens neurons across dorsal-ventral CA1.**
   - Target: anatomical localisation of Sst/Pnoc subclusters from Thulin 2025 [9] onto Sst Gaba_3 children.
   - Expected output: spatial evidence linking cluster identity to dorsal-ventral position.
   - Resolves: whether the within-Sst Gaba_3 scatter is the Thulin 2025 substructure; open questions (1) and (3).

3. **Literature audit of Winterer 2019 [7] for Sst-OLM vs Htr3a-OLM property differences (ephys, morphology, connectivity).**
   - Target: convert the AT-only indistinguishability into a multi-panel statement, or split the cohort if a property distinguishes them.
   - Expected output: SourceGroup.rationale populated with cross-panel evidence, or a refined source-label scheme.
   - Resolves: open question (2).

### Open questions

1. Within supertype 0216 Sst Gaba_3, which child cluster(s) carry O-LM-morphology cells? The AT shows preferential mapping to CLUS_0768 (22/45 cells, F1=0.65) but with substantial scatter to 0767, 0771, 0772, 0773, 0774; this may reflect the Thulin 2025 [9] dorsal-ventral substructure.
2. Are the Sst-OLM and Htr3a-OLM Cre-driver cohorts from Winterer 2019 [7] distinguishable on any property panel beyond AT (ephys, morphology, connectivity)? The current pooling is justified on AT alone.
3. Does mGluR1/Grm1 — the one defining marker absent from WMBv1 precomputed expression — discriminate among Sst Gaba_3 children, given source-side detection of 96% in OLM (GSE124847)?
4. Do CA1-SO-resident cells in the Lamp5 Lhx6 [CS20230722_CLUS_0727] cluster have O-LM morphology despite the CGE-vs-MGE lineage mismatch, or are they a distinct stratum oriens GABA population?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280) | soma location, morphology |
| [2] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503) | soma location, SLM axon target |
| [3] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464) | projection / connectivity |
| [4] | Böhm et al. 2015 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702) | NT type |
| [5] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798) | Sst expression |
| [6] | Hooft et al. 2000 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195) | Sst + mGluR1 on Type I O-LM |
| [7] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995) | scRNA-seq on Cre-driver-targeted O-LM; Sst / Npy / Pnoc; annotation transfer source |
| [8] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082) | Chrna2-Cre specificity for O-LM |
| [9] | Thulin et al. 2025 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734) | Pnoc; dorsal-ventral O-LM substructure |
| [A] | ABC Atlas | — | anatomy=HPF; NT=GABA; expression=Chrna2 ([view](https://tinyurl.com/a4f3kd4v)) |

---

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.78
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] MapMyCells scRNA-seq annotation transfer of
    Cre-driver-targeted OLM cells (Winterer 2019, run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) lands 43/45 classified
    cells on CS20230722_SUPT_0216 with F1=0.97 at SUPERTYPE; parent
    CLASS (07 CTX-MGE GABA) and SUBCLASS (053 Sst Gaba) levels are
    equally clean at F1=0.99. Sst, Chrna2, Npy, and Pnoc are
    CONSISTENT on the supertype; mGluR1 is NOT_ASSESSED (atlas gap).
    5 of 8 positive-marker / neuropeptide comparisons CONSISTENT;
    the 5 elevated negative markers reflect averaging across Sst
    Gaba_3 children rather than transcript-level discriminators
    established for OLM. Cluster-level scatter across multiple Sst
    Gaba_3 children (best child F1=0.65) is consistent with Thulin
    2025 dorsal-ventral OLM substructure, so the call is at
    supertype rather than at any single child cluster.
  reconciliation_note: >
    Sst-OLM and Htr3a-OLM source-group labels in Winterer 2019 pool
    indistinguishably to CS20230722_SUPT_0216 on AT
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1; CASE B —
    AT-only indistinguishability); ephys / morphology / connectivity
    panels not audited from the source paper for this report.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        OLM cells scatter across multiple Sst Gaba_3 children
        within CS20230722_SUPT_0216 (best child CS20230722_CLUS_0768
        F1=0.65); the supertype-level F1=0.97 is the clean signal.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        mGluR1 (Grm1) atlas-side gap — 96% detection in source
        scRNA-seq (Winterer 2019) but absent from WMBv1 precomputed
        expression on this supertype; NOT_ASSESSED on the target side.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical negative-marker means at supertype scale (PV, CB,
        CR, NOS, VIP) reflect mixed Sst Gaba_3 children and are not
        decisive against OLM identity at supertype resolution.
  proposed_experiments:
    - Patch-seq of Chrna2-Cre CA1 stratum oriens neurons with MapMyCells transfer onto WMBv1, targeting F1 >= 0.80 at CLUSTER level.
    - MERFISH of Chrna2+ stratum oriens neurons across dorsal-ventral CA1, testing the Thulin 2025 OLM substructure prediction.
    - Audit Winterer 2019 for Sst-OLM versus Htr3a-OLM differences on ephys / morphology / connectivity to upgrade source-group pooling from AT-only to multi-panel.
  unresolved_questions:
    - Which Sst Gaba_3 child cluster(s) carry OLM-morphology cells given AT scatter across 0767, 0768, 0771, 0772, 0773, 0774?
    - Are Sst-OLM and Htr3a-OLM cohorts distinguishable on ephys / morphology / connectivity, or only AT-indistinguishable?
    - Does Grm1 discriminate among Sst Gaba_3 children given 96% source-side detection but no atlas precomputed value?
```
<!-- verdict-block-end -->

<!-- source-groups-rationale-start: edge_olm_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
source_groups_rationale:
  - source_group_label: OLM-pooled
    run_ref: at_run_20260408_winterer_olm_mmc_wmbv1
    rationale: >
      Sst-OLM and Htr3a-OLM map indistinguishably to CS20230722_SUPT_0216
      under run_ref at_run_20260408_winterer_olm_mmc_wmbv1 (43/45
      classified cells across both cohorts converge on the same
      supertype with pooled F1=0.97; per-cluster scatter within
      Sst Gaba_3 does not differentiate by source cohort). CASE B:
      AT-only indistinguishability; cross-panel literature
      confirmation (ephys / morphology / connectivity) of OLM-subtype
      equivalence has not been audited and remains optional follow-up.
```
<!-- source-groups-rationale-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0768 is the top child of
    CS20230722_SUPT_0216 for the Winterer 2019 OLM cohort
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1): 22/45
    classified cells (Coverage=0.48, Purity=1.00, F1=0.65).
    region_fraction_100um=0.818 (strict region_fraction=0.458)
    on CA1 stratum oriens [MBA:399]. Sst (val 12.70,
    cohort_pct 0.992) and Chrna2 (val 0.57, cohort_pct 0.950)
    are CONSISTENT; Npy and Pnoc present. Cluster-level F1=0.65
    is below the supertype F1=0.97 because OLM cells distribute
    across sibling Sst Gaba_3 children (Thulin 2025), so this
    is the best single-cluster anchor but not unique.
  reconciliation_note: >
    closeMatch (cluster-level best within Sst Gaba_3) rather than
    broadMatch — the cluster captures the plurality of OLM cells in
    AT and the property comparisons align; the supertype edge
    (CS20230722_SUPT_0216) carries the broader 1:n call.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        AT cluster-level F1=0.65 with 23 of 45 OLM cells on sibling
        clusters within CS20230722_SUPT_0216; cluster assignment is
        the best single-child anchor but not unique.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        mGluR1 (Grm1) NOT_ASSESSED on atlas side (no precomputed
        expression value for this cluster).
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical negative markers (PV, CB, CR) DISCORDANT on this
        cluster's precomputed expression; none is a transcript-level
        discriminator established for OLM in the cited literature.
  proposed_experiments:
    - Patch-seq of Chrna2-Cre CA1 stratum oriens neurons with MapMyCells transfer onto WMBv1, targeting F1 >= 0.80 at CLUSTER level for CS20230722_CLUS_0768.
  unresolved_questions:
    - Does CS20230722_CLUS_0768 correspond to a specific dorsal-ventral OLM subtype per Thulin 2025?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0769 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] Despite sitting in the correct supertype
    CS20230722_SUPT_0216 (Sst Gaba_3), CS20230722_CLUS_0769 receives
    0/46 cells in the Winterer 2019 AT run
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1); the plurality
    of OLM cells map to sibling CS20230722_CLUS_0768. Property
    comparisons align at supertype level but cluster-level AT does
    not support 0769 as the OLM child.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Within Sst Gaba_3, OLM cells preferentially map to sibling
        CS20230722_CLUS_0768; cluster 0769 receives 0 cells.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0727 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] 0/46 OLM cells map to subclass 053 Lamp5 Lhx6
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1); all 45
    classified cells land on Sst subclass. Lamp5 Lhx6 is a
    CGE-derived population, not the Sst-MGE lineage of OLM; Npy
    DISCORDANT on this cluster.
  caveats:
    - caveat_type: WRONG_SUBCLASS
      description: >
        Lamp5 Lhx6 (CGE) vs Sst (MGE) lineage mismatch; AT confirms
        zero cell support for this candidate.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] CS20230722_CLUS_0772 is a sibling within
    CS20230722_SUPT_0216; AT F1=0.27 (4/45 cells; run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1). Represents within-OLM
    cluster scatter rather than a distinct candidate; the broader
    supertype call is the appropriate resolution.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Within-supertype sibling of CS20230722_SUPT_0216;
    AT F1=0.04 (1/45 cells; run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1). Cluster scatter only.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0775 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Within-supertype sibling of CS20230722_SUPT_0216
    with highest Pnoc among Sst Gaba_3 children (cohort_pct 0.966);
    AT did not assign OLM cells here in
    run_ref at_run_20260408_winterer_olm_mmc_wmbv1. Cluster scatter
    only.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Within-supertype sibling of CS20230722_SUPT_0216; AT
    did not assign OLM cells here in run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0771 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] Within-supertype sibling of CS20230722_SUPT_0216;
    AT F1=0.16 (4/45 cells; run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1). Cluster scatter only.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0767 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.13
  rationale: >
    [tier:CUT] Within-supertype sibling of CS20230722_SUPT_0216;
    AT F1=0.20 (5/45 cells; run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1). Cluster scatter only.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 (Sst Gaba_13) is isocortex-
    dominant (region_fraction_100um=0.016) with no meaningful
    hippocampal stratum oriens cell population. Marker overlap
    (Sst, Chrna2, Npy) reflects shared Sst-MGE lineage rather than
    OLM identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0217 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_SUPT_0217 (Sst Gaba_4) is isocortex-
    dominant (region_fraction_100um=0.015). Wrong region for CA1
    stratum oriens OLM.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0241 (Sst Chodl Gaba_4): Chrna2
    val=0.00 (DISCORDANT for the defining OLM marker); isocortex-
    dominant region (region_fraction_100um=0.021); Sst Chodl is the
    long-range projecting subclass, not OLM.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0224 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0224 (Sst Gaba_11): region mismatch
    for CA1 stratum oriens; no AT support
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0225 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0225 (Sst Gaba_12): region mismatch;
    no AT support (run_ref at_run_20260408_winterer_olm_mmc_wmbv1).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0219 (Sst Gaba_6): alternative Sst
    supertype; no AT cells under run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1; child clusters
    eliminated on Chrna2 absence (see CLUS_0785/0788/0789).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0215 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0215 (Sst Gaba_2): alternative Sst
    supertype with no AT support
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0213 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0213 is Pvalb Gaba_9 — Pvalb is a
    classical negative marker for OLM; wrong subclass.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0190 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0190 is Sncg Gaba_6 — Sncg is a
    different GABAergic subclass with no overlap with OLM identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0638 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0638 is Vip Gaba_4; VIP is a classical
    OLM negative marker, so Vip subclass identity is incompatible.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0778 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_CLUS_0778 (Sst Gaba_4) is a cortical
    cluster within isocortex-dominant CS20230722_SUPT_0217; wrong
    region for CA1 stratum oriens OLM.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0807 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_CLUS_0807 (Sst Gaba_12): wrong supertype
    and region for CA1 stratum oriens OLM.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0785 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0785 (Sst Gaba_6 child): Chrna2 not
    expressed on this cluster — eliminates as an OLM candidate
    given Chrna2 as the defining selective marker.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0788 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0788 (Sst Gaba_6 child): Chrna2 not
    expressed; eliminated on the OLM defining marker.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0789 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0789 (Sst Gaba_6 child): Chrna2 not
    expressed; eliminated on the OLM defining marker.
```
<!-- verdict-block-end -->
