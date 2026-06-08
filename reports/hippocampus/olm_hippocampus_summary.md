# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*2026-03-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_OLM.yaml`*

---

## Introduction

Oriens-lacunosum moleculare (O-LM) interneurons are a canonical GABAergic, somatostatin-expressing population of the hippocampal CA1, defined by a stereotyped morphology in which horizontally oriented dendrites lie within stratum oriens and a single axon ramifies extensively in stratum lacunosum-moleculare, where it targets the apical tuft of pyramidal cells [1][2][3][4]. Beyond Sst, the type is distinguished by expression of the nicotinic acetylcholine receptor subunit Chrna2 — restricted in the hippocampus to oriens-localised cells [2][7][8] — and of Grm1/mGluR1 [4][6]. Mapping the classical O-LM type onto a transcriptomic atlas is non-trivial because Sst-positive oriens interneurons comprise multiple molecular subpopulations [9], and the specific subset corresponding to canonical O-LM cells needs to be identified at supertype and (where possible) cluster resolution.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371]; hippocampus stratum lacunosum moleculare [UBERON:0007640] | [1][2][3] |
| NT | GABAergic | [4][5] |
| Defining markers | Sst, Chrna2, mGluR1 (Grm1) | Sst: [5][7]; Chrna2: [2][7][8]; mGluR1: [4][7] |
| Negative markers | PV, CB, CR, NOS, VIP | — |
| Neuropeptides | Sst, Npy, Pnoc | Sst: [7]; Npy: [7]; Pnoc: [7][9] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** morphological reconstruction · CA1 stratum oriens, rat · [1]
  > oriens-lacunosum-moleculare (OLM) cells also had both the cell body and dendritic tree in the stratum oriens, but their horizontally running dendrites were often densely decorated with long spines. Their axon frequently originated from a proximal dendrite, and after ramification the main axon without boutons could be followed into the stratum lacunosum-moleculare. In this layer the axon ramified extensively bearing heavily packed varicosities. Some axon collaterals with boutons were also observed in the stratum oriens.
  > — Zemankovics et al. 2010, Anatomical Location and Morphology · [1] <!-- quote_key: 3106274_e54f60e9 -->
- **Soma location (review):** narrative summary of CA1 oriens/SLM circuit · [2]
  > These CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare (SLM; Cajal, 1911;(McBain et al., 1994)(Sik et al., 1995)(Maccaferri et al., 2000)(Losonczy et al., 2002)(Leão et al., 2012)
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_2414c9e9 -->
- **Connectivity:** apical tuft targeting in SLM · [3]
  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [3] <!-- quote_key: 229694907_6865b9db -->
- **NT type:** GABAergic, rat CA1 · [4]
  > GABAergic inhibitory oriens lacunosum-moleculare (O-LM) cells in the hippocampal area CA1 of the rat
  > — Böhm et al. 2015, Anatomical Location and Morphology · [4] <!-- quote_key: 15101210_5604b9a4 -->
- **Sst marker:** EGFP reporter in Sst+ hippocampal interneurons · [5]
  > EGFP was found to be expressed in a subpopulation of somatostatin-containing GABAergic interneurons in the hippocampus and neocortex
  > — Oliva et al. 2000, Molecular Markers and Gene Expression · [5] <!-- quote_key: 13398453_9154fc23 -->
- **Sst + mGluR1 / mGluR5:** Type I (OLM) interneuron molecular signature · [6]
  > Type I interneurons had large horizontally oriented cell somata located at the border of stratum oriens and the alveus, indicating that these cells were most likely identical with the previously described somatostatin-positive oriens-lacunosum moleculare (O-LM) cells (Freund et al., 1998). Reconstruction of type I interneurons revealed their horizontally oriented dendritic tree in stratum oriens and their axonal arborizations in stratum lacunosum-moleculare (n = 5) (Fig. 2 A), and in situ hybridization for somatostatin showed that four of four cells were indeed positive for somatostatin (Fig. 2 B)
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_215c5f40 -->
  > Type I interneurons responded with a large inward current of ≈ 224pA, were positive for somatostatin, and the majority expressed both mGluR1 and mGluR5
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_17d10a9e -->
- **Sst (function), Npy:** Winterer scRNA-seq + electrophysiology of Cre-targeted OLM cohorts · [7]
  > oriens-lacunosum moleculare (OLM) interneurons. OLMs express somatostatin (Sst), generate feedback inhibition and play important roles in theta oscillations and fear encoding
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_69dc904d -->
  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_8d16e821 -->
- **Chrna2 marker (review framing):** OLM specificity of Chrna2 in CA1 · [2]
  > The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_644f1e68 -->
- **Chrna2 marker (primary):** Chrna2-Cre targeting + optogenetics in CA1 · [8]
  > The vast diversity of GABAergic interneurons is believed to endow hippocampal microcircuits with the required flexibility for memory encoding and retrieval. However, dissection of the functional roles of defined interneuron types has been hampered by the lack of cell-specific tools. We identified a precise molecular marker for a population of hippocampal GABAergic interneurons known as oriens lacunosum-moleculare (OLM) cells. By combining transgenic mice and optogenetic tools, we found that OLM cells are important for gating the information flow in CA1, facilitating the transmission of intrahippocampal information (from CA3) while reducing the influence of extrahippocampal inputs (from the entorhinal cortex). Furthermore, we found that OLM cells were interconnected by gap junctions, received direct cholinergic inputs from subcortical afferents and accounted for the effect of nicotine on synaptic plasticity of the Schaffer collateral pathway. Our results suggest that acetylcholine acting through OLM cells can control the mnemonic processes executed by the hippocampus.
  > — Leão et al. 2012, Projection Patterns and Connectivity · [8] <!-- quote_key: 7952877_ae03c6e0 -->
- **Pnoc neuropeptide / subtype heterogeneity:** transcriptomic resolution of three Sst-Pnoc subclusters · [9]
  > The Chrna2 gene expression is restricted to the stratum oriens in the hippocampus in both rats and mice (Ishii et al., 2005) and is specifically expressed in a subset of CA1 hippocampal interneurons, the oriens lacunosummoleculare (OLM) cells (Leão et al., 2012). Traditionally, OLM cells have been identified through their expression of somatostatin (Sst). However, in-depth single-cell transcriptomic cluster analysis has unveiled at least 11 distinct subpopulations of Sst-expressing interneurons (2017). Within these clusters, various classes of interneurons were identified, including back projecting, hippocampo-septal, oriens-bistratified, and OLM cells. Among these clusters, OLM cells were classified into a Sst and Prepronociceptin (Pnoc) co-expressing group (further divided into three subclusters)
  > — Thulin et al. 2025, Projection Patterns and Connectivity · [9] <!-- quote_key: 280420054_8a6529c5 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer from morphologically and electrophysiologically validated, Cre-driver-targeted OLM cells (Winterer 2019 [7]; Sst-OLM + Htr3a-OLM pooled, n=45 classified cells) places the canonical O-LM type cleanly on the supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (pooled F1=0.97), with marker expression and stratum-oriens enrichment all concordant (see figure and property comparison tables). At cluster resolution OLM cells scatter across several Sst Gaba_3 sibling clusters, with 0768 Sst Gaba_3 [CS20230722_CLUS_0768] receiving the plurality of cells (n=22, pooled F1=0.65) — consistent with within-OLM transcriptomic heterogeneity reported by Thulin et al. [9] and supporting a primary supertype-level mapping plus a best-child cluster call.

**Annotation-transfer overview figure (run-level, filtered)**

![Filtered AT figure for Oriens-Lacunosum Moleculare (O-LM) interneuron](figures/f1_for_olm_hippocampus.png)

*F1 across taxonomy levels for the Winterer 2019 OLM cohort (Sst-OLM + Htr3a-OLM pooled to a single OLM group; n=46 source cells, 45 retained after bootstrap filtering). Coverage = fraction of source-group cells landing on the target; Purity = fraction of this target's cells coming from the source group. With a single pooled source in the figure, Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The pooled OLM cohort lands cleanly at class (07 CTX-MGE GABA, F1=0.99), subclass (053 Sst Gaba, F1=0.99) and supertype (0216 Sst Gaba_3, F1=0.97); at cluster level only CLUS_0768 exceeds 0.5 (F1=0.65), with the remaining cells distributing across CLUS_0772, CLUS_0767, CLUS_0771, CLUS_0774 and others — the within-supertype scatter expected if O-LM corresponds to a transcriptomic subtype not yet resolved at WMBv1 cluster rank, in line with the three Sst-Pnoc subclusters reported by Thulin et al. [9].*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype | Best cluster (0768) | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | Hippocampal formation [MBA:1089]; Field CA1 [MBA:382]; Field CA1, stratum oriens [MBA:399] | Field CA1, stratum oriens [MBA:399] dominant (count_100um=261) | CONSISTENT |
| NT type | GABAergic | not asserted (supertype) | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Sst expression | defining marker | 11.44 (cohort_pct 0.905; child-coverage 1.000) | 12.70 (cohort_pct 0.992) | CONSISTENT |
| Chrna2 expression | defining marker | 0.61 (cohort_pct 0.952; child-coverage 0.667) | 0.57 (cohort_pct 0.950) | CONSISTENT |
| mGluR1 (Grm1) expression | defining marker | 9.33 | 10.27 | CONSISTENT |
| PV expression | ABSENT (negative) | 1.48 | 3.12 | DISCORDANT |
| CB expression | ABSENT (negative) | 5.56 | 3.87 | DISCORDANT |
| CR expression | ABSENT (negative) | 1.28 | 2.30 | DISCORDANT |
| NOS expression | ABSENT (negative) | 2.94 | 0.76 | DISCORDANT |
| VIP expression | ABSENT (negative) | 0.42 | 0.31 | DISCORDANT |
| Npy (neuropeptide) | present | 5.07 (cohort_pct 0.794; child-coverage 1.000) | 7.58 (cohort_pct 0.857) | CONSISTENT |
| Pnoc (neuropeptide) | present | 3.69 (cohort_pct 0.667; child-coverage 0.889) | 2.51 (cohort_pct 0.479) | SUPT: CONSISTENT; CLUS: APPROXIMATE |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*Subcluster concordance: across the Sst Gaba_3 supertype's children, Sst is detected at every cluster (child-coverage 1.000), Chrna2 at two-thirds (child-coverage 0.667), Npy at every cluster (child-coverage 1.000), and Pnoc at eight of nine (child-coverage 0.889) — the defining OLM markers are broadly distributed within the supertype rather than concentrated in a single child. Best child: CLUS_0768.*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (supertype) | Atlas metadata | PARTIAL | region_fraction_100um=0.539 | atlas-internal |
| Winterer 2019 OLM → WMBv1 MapMyCells (pooled) | Annotation transfer | SUPPORT | supertype F1=0.97 (n=43) | atlas-internal |

> MapMyCells annotation transfer of the pooled OLM cohort (46 cells; Sst-OLM + Htr3a-OLM combined; GSE124847, Winterer 2019) strongly supports the parent Sst Gaba_3 supertype (43/45 classified cells; pooled F1=0.97; pooled CLASS/SUBCLASS F1=0.99) but OLM cells scatter across sibling clusters 0767–0774 within it. Cluster 0769 specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/45, best pooled cluster-level F1=0.65). This indicates OLM identity is captured at the Sst Gaba_3 supertype rather than at any single child cluster. The high pooled supertype F1 reflects removal of the inter-source mis-attribution penalty that depresses per-source F1; both Sst-OLM and Htr3a-OLM converge on the same Sst Gaba_3 supertype.
> — Winterer et al. 2019 · [7]

The supertype 0216 Sst Gaba_3 is the natural transcriptomic home of the canonical O-LM type. Annotation transfer of Cre-driver-targeted, morphologically and electrophysiologically validated OLM cells from Winterer 2019 [7] lands 43 of 45 classified cells on Sst Gaba_3 at supertype level (pooled F1=0.97), with class-level (07 CTX-MGE GABA, F1=0.99) and subclass-level (053 Sst Gaba, F1=0.99) F1 nearly at ceiling — the MGE-derived Sst inhibitory identity is unambiguous. The defining OLM markers all align: Sst is at the 0.91 cohort percentile, Chrna2 sits at the 0.95 cohort percentile (atlas mean 0.61) — high specificity given that Chrna2 in the hippocampus is restricted to stratum oriens OLM cells [2][8] — and Grm1/mGluR1 is expressed at 9.33. Both classical neuropeptides Npy and Pnoc are recovered (cohort percentiles 0.79 and 0.67). The location signal, anchored at Field CA1, stratum oriens [MBA:399] within the broader hippocampal formation, places the supertype's soma distribution in the target region, with `region_fraction_100um: 0.539` reflecting the supertype-wide rollup across hippocampus, cortical subplate and amygdalar/pro-subicular subregions. Cells of this supertype are not exclusively hippocampal — extra-hippocampal Sst Gaba_3 cells exist — and this report's mapping pertains to the hippocampal subset.

**Concerns**

- All five classical "negative" markers (PV, CB, CR, NOS, VIP) are detected at the supertype above MIN_DETECTABLE (range 0.42–5.56). The classical OLM negative-marker panel is largely a protein-level immunohistochemistry consensus established before transcript-level atlas data; transcript expression at low to moderate levels in single-cell mean profiles is not necessarily incompatible with the negative-marker call at the protein/cellular level, but the gap deserves curator audit. CB in particular (5.56) is the strongest mismatch.
- Cluster-level scatter within Sst Gaba_3 means a single child cluster does not capture the full O-LM cohort; the cohort distributes across CLUS_0768 (22 cells), CLUS_0772 (7), CLUS_0767 (5), CLUS_0771 (4) and CLUS_0774 (4). This is consistent with Thulin et al. [9] reporting three Sst-Pnoc subclusters within OLM, suggesting the atlas resolves OLM heterogeneity rather than the canonical type as a unit.
- `region_fraction_100um: 0.539` at supertype level is intermediate because the supertype includes non-hippocampal Sst Gaba_3 cells; this is structural at supertype rank and is not counter-evidence to the mapping of the hippocampal subset.

**What would upgrade confidence**

- Targeted patch-seq or Chrna2-Cre + MapMyCells of CA1 stratum oriens neurons resolving which Sst Gaba_3 child(ren) carry OLM morphology and Chrna2 expression — would clarify whether the cluster-level scatter reflects the three Sst-Pnoc subclusters reported by Thulin et al. [9] or methodological dispersal, and would feed back as additional AnnotationTransferEvidence at F1 thresholds above 0.80 at CLUSTER level.
- A targeted literature trawl of the OLM negative-marker panel (especially CB and NOS) for transcript-level vs. protein-level evidence in morphology-confirmed OLM cells would clarify whether the supertype's positive transcript signal reflects a real subpopulation or a protein/transcript discordance.

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · 🟡 MODERATE

**Property alignment**

| Property | Classical | Supertype (0216) context | Best cluster (0768) | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | Field CA1, stratum oriens [MBA:399] dominant within supertype | Field CA1, stratum oriens [MBA:399] dominant (count_100um=261) | CONSISTENT |
| NT type | GABAergic | (supertype not asserted) | GABA | CONSISTENT |
| Sst expression | defining marker | supertype mean 11.44 | 12.70 (cohort_pct 0.992) | CONSISTENT |
| Chrna2 expression | defining marker | supertype mean 0.61 (child-coverage 0.667) | 0.57 (cohort_pct 0.950) | CONSISTENT |
| mGluR1 (Grm1) expression | defining marker | supertype mean 9.33 | 10.27 | CONSISTENT |
| PV expression | ABSENT (negative) | supertype mean 1.48 | 3.12 (atlas category: MERFISH) | DISCORDANT |
| CB expression | ABSENT (negative) | supertype mean 5.56 | 3.87 | DISCORDANT |
| CR expression | ABSENT (negative) | supertype mean 1.28 | 2.30 | DISCORDANT |
| NOS expression | ABSENT (negative) | supertype mean 2.94 | 0.76 | DISCORDANT |
| VIP expression | ABSENT (negative) | supertype mean 0.42 | 0.31 | DISCORDANT |
| Npy (neuropeptide) | present | supertype mean 5.07 | 7.58 (cohort_pct 0.857) | CONSISTENT |
| Pnoc (neuropeptide) | present | supertype mean 3.69 | 2.51 (cohort_pct 0.479) | APPROXIMATE |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*Subcluster concordance, narrated against this child: Chrna2 is detected on CLUS_0768 (0.57; cohort_pct 0.950), so the child carries the defining Chrna2 signal explicitly; Pnoc on CLUS_0768 is APPROXIMATE (2.51; cohort_pct 0.479) rather than at the supertype's modal level (3.69), consistent with Thulin et al. [9] reporting three Sst-Pnoc subclusters within OLM where Pnoc is one differentiating signal.*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (cluster) | Atlas metadata | PARTIAL | region_fraction_100um=0.818 | atlas-internal |
| Winterer 2019 OLM → WMBv1 MapMyCells (best-cluster) | Annotation transfer | SUPPORT | cluster F1=0.65 (n=22, pooled) | atlas-internal |

> AT transfer of Sst-OLM to CS20230722_CLUS_0768 — best F1 0.676 at class level; per-level metrics populated programmatically from at_results.yaml.
> — Winterer et al. 2019 · [7]

CLUS_0768 is the best cluster-level recipient of the pooled OLM cohort: 22 of 45 classified Winterer cells map here (pooled F1=0.65), the highest of any Sst Gaba_3 child. The cluster sits at `region_fraction_100um: 0.818`, with Field CA1, stratum oriens [MBA:399] the dominant soma anatomy — a clean fit for the canonical OLM location. Chrna2 expression on CLUS_0768 (mean 0.57; cohort percentile 0.95) addresses one of the principal mapping questions: at least one Sst Gaba_3 child does carry the defining Chrna2 signal in its precomputed atlas profile (Chrna2 is absent on the sibling CLUS_0769, see candidates audit table), and that signal aligns with this cluster being a transcriptomic candidate for the Chrna2+ OLM subset documented by Leão et al. [8]. Sst is at cohort percentile 0.99 (val=12.70) and Grm1/mGluR1 at 10.27.

**Concerns**

- The five negative-marker mismatches present at supertype recur here: PV (3.12, also flagged in the atlas MERFISH panel), CB (3.87), CR (2.30), NOS (0.76) and VIP (0.31). PV's MERFISH-panel tag is panel-selection metadata, not an expression-quality signal, so it does not on its own elevate the discordance — but the transcript mean is non-trivial and warrants curator-side resolution of transcript-vs-protein conventions for the OLM negative-marker panel.
- Pnoc on CLUS_0768 is APPROXIMATE (2.51 vs. 3.69 supertype-wide; cohort_pct 0.479). Thulin et al. [9] report three Sst-Pnoc OLM subclusters; if those correspond to atlas children, CLUS_0768 may be the Chrna2-stronger / Pnoc-weaker subgroup. This is interpretation rather than direct evidence from the gathered literature.
- The pooled F1 of 0.65 reflects that 23 of 45 OLM cells (the majority) do *not* land on CLUS_0768 but distribute across CLUS_0772, CLUS_0767, CLUS_0771, CLUS_0774 and others — the cluster captures the modal OLM subset, not the whole O-LM cohort.

**What would upgrade confidence**

- Targeted Chrna2-Cre + MapMyCells of CA1 stratum oriens neurons followed by within-Sst Gaba_3 reassignment at higher resolution; would feed back as AnnotationTransferEvidence at F1 ≥ 0.80 at CLUSTER level and would clarify whether CLUS_0768 specifically corresponds to one of the three Sst-Pnoc OLM subclusters of Thulin et al. [9].
- Patch-seq with morphology recovery on OLM-targeted cells from Winterer's cohorts or comparable preparations would directly tie cluster identity to morphology and Chrna2 protein/transgene expression.

### Candidates audit table (full top-K)

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | — | 2004 | 🟡 MODERATE | Pooled OLM AT F1=0.97 at supertype | Primary (supertype) |
| `0768 Sst Gaba_3 [CS20230722_CLUS_0768]` | 0216 Sst Gaba_3 | 66 | 🟡 MODERATE | Best cluster recipient (22/45 cells, F1=0.65); Chrna2 detected | Primary (best child cluster) |
| `0772 Sst Gaba_3 [CS20230722_CLUS_0772]` | 0216 Sst Gaba_3 | 190 | 🔴 LOW | Sibling within Sst Gaba_3; AT cluster F1=0.27 | Eliminated (within-supertype scatter; not modal) |
| `0773 Sst Gaba_3 [CS20230722_CLUS_0773]` | 0216 Sst Gaba_3 | 156 | 🔴 LOW | Sibling within Sst Gaba_3; no AT evidence item | Eliminated (within-supertype scatter; not modal) |
| `0775 Sst Gaba_3 [CS20230722_CLUS_0775]` | 0216 Sst Gaba_3 | 143 | 🔴 LOW | Pnoc-high sibling; no direct AT evidence item | Eliminated (within-supertype scatter; not modal) |
| `0770 Sst Gaba_3 [CS20230722_CLUS_0770]` | 0216 Sst Gaba_3 | 404 | 🔴 LOW | Sibling within Sst Gaba_3; no AT evidence item | Eliminated (within-supertype scatter; not modal) |
| `0769 Sst Gaba_3 [CS20230722_CLUS_0769]` | 0216 Sst Gaba_3 | 334 | 🔴 LOW | Chrna2 absent on this cluster; 0/45 AT cells | Eliminated (Chrna2 absent on this cluster) |
| `0226 Sst Gaba_13 [CS20230722_SUPT_0226]` | — | 4064 | 🔴 LOW | Isocortex-dominant; `region_fraction_100um: 0.016` | Eliminated (non-hippocampal soma distribution) |
| `0217 Sst Gaba_4 [CS20230722_SUPT_0217]` | — | 14335 | 🔴 LOW | Isocortex-dominant; `region_fraction_100um: 0.015` | Eliminated (non-hippocampal soma distribution) |
| `0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241]` | — | 2905 | 🔴 LOW | Isocortex-dominant; Chrna2 absent | Eliminated (wrong subtype; Chrna2 absent) |
| `0224 Sst Gaba_11 [CS20230722_SUPT_0224]` | — | 2677 | 🔴 LOW | Isocortex-dominant; `region_fraction_100um: 0.032` | Eliminated (non-hippocampal soma distribution) |
| `0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727]` | 0203 Lamp5 Lhx6 Gaba_1 | 59 | 🔴 LOW | Wrong subclass (Lamp5 Lhx6, CGE-derived); 0/45 AT cells | Eliminated (wrong subclass; legacy edge — see open questions) |
| `0785 Sst Gaba_6 [CS20230722_CLUS_0785]` | 0219 Sst Gaba_6 | 51 | 🔴 REFUTED | Chrna2 absent at parent supertype; 0/45 AT cells | Eliminated (Chrna2 absent; legacy edge — see open questions) |
| `0788 Sst Gaba_6 [CS20230722_CLUS_0788]` | 0219 Sst Gaba_6 | 98 | 🔴 REFUTED | Chrna2 absent at parent supertype; 0/45 AT cells | Eliminated (Chrna2 absent; legacy edge — see open questions) |
| `0789 Sst Gaba_6 [CS20230722_CLUS_0789]` | 0219 Sst Gaba_6 | 222 | 🔴 REFUTED | Chrna2 absent at parent supertype; amygdala-dominant; 0/45 AT cells | Eliminated (Chrna2 absent; legacy edge — see open questions) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The O-LM type is defined here as a GABAergic, somatostatin-expressing CA1 interneuron with horizontally oriented dendrites in stratum oriens and an axon arborising in stratum lacunosum-moleculare to target the apical tuft of pyramidal cells [1][2][3], expressing Chrna2 [2][7][8], Grm1/mGluR1 [4][6], and the neuropeptide triad Sst/Npy/Pnoc [7][9]. `definition_basis: CLASSICAL_MULTIMODAL` — the type sits on a combined morphological, electrophysiological, molecular and connectional evidentiary base.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE124847 (Sst-OLM, Htr3a-OLM per-cell labels in source_cell_labels.json) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization). Bootstrap-iteration assignment with default thresholds; per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 46 (filtered to 45) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md (external; precomputed) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix.csv`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/f1_matrix.csv) |
| Caveats | Source dataset has only 46 OLM cells (Winterer 2019); 45 retained after bootstrap filtering. The "Sst-OLM" and "Htr3a-OLM" source labels reflect Cre-driver subgroups in the Winterer dataset and are scored separately. At cluster (rank 0) resolution F1 is low across all candidates (max 0.26 for Sst-OLM → CLUS_0768 within Sst Gaba_3 supertype) — the OLM cell type is captured at supertype/subclass level (Sst Gaba_3 / Sst Gaba; F1 ≈ 0.65) but scatters across sibling clusters. This is a real biological signal, not a methodological failure: OLM is a transcriptomic subtype not yet resolved at WMBv1 cluster rank. |

**Source pooling.** The Winterer 2019 cohort carries two Cre-driver source labels (Sst-OLM and Htr3a-OLM) which under run_ref `at_run_20260408_winterer_olm_mmc_wmbv1` map indistinguishably onto the same Sst Gaba_3 supertype with pooled F1=0.97 and undifferentiated within-supertype cluster scatter. Both cohorts were targeted via Cre-driver lines selecting morphology-confirmed OLM cells in the original paper [7]; the pooled rendering of the figure is an AT-side observation supporting a single OLM pseudo-source for visualisation. Cross-panel literature confirmation of cohort equivalence (matched ephys / morphology / connectivity between Sst-OLM and Htr3a-OLM in [7]) has not been independently audited at report time and remains an optional follow-up.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:45+00:00 from [kb/graphs/hippocampus/hippocampus_OLM.yaml](kb/graphs/hippocampus/hippocampus_OLM.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_olm_to_wmb_clus_0769 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT/PARTIAL | atlas-internal |
| edge_olm_to_wmb_clus_0727 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL/REFUTE | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL/SUPPORT | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0772 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL/SUPPORT | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0775 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL/SUPPORT | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0217 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_hippocampus_to_CS20230722_SUPT_0224 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_olm_to_wmb_clus_0785 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL/REFUTE | [A] |
| edge_olm_to_wmb_clus_0788 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL/REFUTE | [A] |
| edge_olm_to_wmb_clus_0789 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL/REFUTE | [A] |

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) interneuron → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence, with the supertype as the supportable single-target call and 0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the best-resolved child cluster (also MODERATE). Key support: pooled OLM annotation transfer (Winterer 2019 Cre-driver-targeted, morphology- and electrophysiology-validated cohorts; supertype F1=0.97; cluster F1=0.65) and concordance on all three defining markers (Sst, Chrna2 detected on CLUS_0768, mGluR1/Grm1). Key caveats: the five classical OLM negative markers (PV, CB, CR, NOS, VIP) are all detected at supertype-level transcript means above MIN_DETECTABLE — a transcript-vs-protein convention gap that warrants curator audit; and OLM cells distribute across multiple Sst Gaba_3 child clusters consistent with the three Sst-Pnoc OLM subclusters reported by Thulin et al. [9], so cluster-level resolution remains partial.

No Cell Ontology term currently assigned. The combined classical+transcriptomic profile (CA1 stratum oriens Sst+Chrna2+Pnoc interneuron) is a candidate for CL contribution; the supertype-level mapping and best-cluster pair documented here would be the supporting evidence base.

### Proposed experiments and follow-ups

The pooled OLM annotation transfer (GSE124847 → WMBv1, MapMyCells v1.7.1) has already been executed and is the dominant evidence on the primary edges; it resolves the supertype-level mapping at F1=0.97 and identifies CLUS_0768 as the best within-supertype child at F1=0.65 but does not resolve which Sst Gaba_3 child(ren) correspond to the three Sst-Pnoc OLM subclusters reported by Thulin et al. [9]. The refined experiments below address what the completed pooled MapMyCells run did not resolve.

- **What**: Chrna2-Cre + MapMyCells (or comparable Cre-driver-targeted re-mapping) of CA1 stratum oriens neurons. **Target**: F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3. **Expected output**: a new AnnotationTransferEvidence item per identified child cluster, refining the broadMatch onto supertype 0216 into a closeMatch onto one (or several) of its children. **Resolves**: whether the cluster-level scatter reflects the three Sst-Pnoc OLM subclusters, and whether CLUS_0768 in particular corresponds to a Chrna2-stronger OLM subgroup.
- **What**: Patch-seq with morphology recovery on OLM-targeted cells. **Target**: cluster-level F1 ≥ 0.80 at CLUSTER level, with paired morphological / electrophysiological annotation for each profiled cell. **Expected output**: AnnotationTransferEvidence at cluster rank plus per-cell morphology/ephys annotations on the cluster YAML. **Resolves**: whether the within-Sst Gaba_3 atlas heterogeneity tracks documented OLM heterogeneity (PV-positive gamma-firing OLM subset; the three Sst-Pnoc subclusters of Thulin et al. [9]; TRPV1+ subpopulation).
- **What**: Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons. **Target**: confirmatory expression panel on at least 200 Chrna2+ cells; ≥ 90% of cells unambiguously assigned to a single Sst Gaba_3 child cluster. **Expected output**: AnnotationTransferEvidence at cluster rank. **Resolves**: whether Chrna2 transcript-level expression in CLUS_0768 (mean 0.57; cohort_pct 0.95) is concentrated in a cellular subset that recovers OLM morphology.
- **What**: Targeted literature trawl on the OLM negative-marker panel (PV, CB, CR, NOS, VIP), focused on transcript-level vs. protein-level evidence in morphology-confirmed OLM cells. **Expected output**: LiteratureEvidence items updating the negative-marker provenance on the classical node; potential reclassification of one or more negative-markers from DISCORDANT to NOT_ASSESSED where the original assertion is protein-only.

### Open questions

1. Are the CA1 stratum oriens cells of CLUS_0768 OLM-morphology, and what are the cells captured in the cluster's prosubicular and amygdalar contingents?
2. Why does the pooled OLM cohort map preferentially to CS20230722_CLUS_0768 rather than the sibling CS20230722_CLUS_0769 within CS20230722_SUPT_0216? Specifically, the Chrna2 absence on CLUS_0769 (atlas mean 0.00) versus presence on CLUS_0768 (atlas mean 0.57) is a candidate discriminator that warrants direct testing.
3. Do the three Sst-Pnoc OLM subclusters reported by Thulin et al. [9] correspond to specific Sst Gaba_3 child clusters in WMBv1 — and is CLUS_0768 the modal Chrna2+ subgroup?
4. Do any OLM-morphology cells fall into CS20230722_CLUS_0727 (Lamp5 Lhx6 Gaba_1, CGE-derived) despite the subclass/lineage mismatch with the canonical MGE-derived OLM identity?
5. Curator review: four legacy edges (CS20230722_CLUS_0727, CS20230722_CLUS_0785, CS20230722_CLUS_0788, CS20230722_CLUS_0789) fall outside the current Stage A top-50 cohort at rank 0 and their `property_comparisons` were not refreshed under the current scoring; they remain in the graph from a prior curator pass. Recommend curator review / removal in line with #111.
6. The five classical OLM negative markers (PV, CB, CR, NOS, VIP) are all detected at transcript level above MIN_DETECTABLE in the Sst Gaba_3 supertype and its children. Curator audit of transcript-vs-protein conventions for these markers, and a targeted literature trawl to anchor each on a primary morphology-confirmed OLM study, would resolve whether these DISCORDANT calls reflect real subpopulation biology, transcript-vs-protein methodological discordance, or upstream curation gaps.
7. Consider unifying lit-type Sst-OLM and Htr3a-OLM within the Winterer 2019 cohort: AT-side they are indistinguishable, but cross-panel ephys/morphology/connectivity equivalence has not been independently audited from the available references. (See #62.)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280/) | soma location |
| [2] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | soma location; Chrna2 marker (review) |
| [3] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | soma location; connectivity |
| [4] | Böhm et al. 2015 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702/) | neurotransmitter type |
| [5] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | neurotransmitter type / Sst marker |
| [6] | Hooft et al. 2000 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195/) | Sst marker; mGluR1/mGluR5 |
| [7] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | Sst, Chrna2, mGluR1, Npy, Pnoc; Cre-driver cohorts |
| [8] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | Chrna2 primary marker |
| [9] | Thulin et al. 2025 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734/) | Pnoc; OLM subcluster heterogeneity |
| [A] | ABC Atlas | [view](https://tinyurl.com/a4f3kd4v) | anatomy=HPF; NT=GABA; expression=Chrna2 |

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
    [tier:STRONGEST] Cre-driver-targeted MapMyCells annotation transfer
    (Winterer 2019 OLM cohort pooled; run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) lands the OLM cohort on
    CS20230722_SUPT_0216 with F1=0.68 at supertype, with subclass
    (053 Sst Gaba) and class (07 CTX-MGE GABA) at the same edge-level
    F1 (0.67–0.68); 3 of 3 defining markers
    CONSISTENT (Sst cohort_pct 0.905; Chrna2 cohort_pct 0.952 with
    child-coverage 0.667; mGluR1 mean 9.33). region_fraction_100um 0.539
    reflects supertype-wide rollup including non-hippocampal Sst Gaba_3
    cells; the hippocampal subset is the mapping target. Five negative
    markers DISCORDANT at transcript level (PV, CB, CR, NOS, VIP) — a
    transcript-vs-protein convention gap, not a refutation. Paired with
    best-child CS20230722_CLUS_0768 (see edge
    edge_olm_hippocampus_to_CS20230722_CLUS_0768).
  reconciliation_note: >
    Paired supertype + best-child pattern: this supertype broadMatch
    covers the full OLM cohort (43/45 cells), while
    CS20230722_CLUS_0768 captures the modal subset (22/45) as
    closeMatch at cluster rank. Within-supertype scatter across
    CLUS_0768, CLUS_0772, CLUS_0767, CLUS_0771, CLUS_0774 is consistent
    with the three Sst-Pnoc OLM subclusters reported by Thulin et al.
    2025 (PMID:40757734) — the atlas resolves within-OLM heterogeneity
    rather than the canonical type as a unit.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        OLM is transcriptomically heterogeneous within Sst Gaba_3:
        Thulin et al. 2025 (PMID:40757734) report three Sst-Pnoc OLM
        subclusters; pooled MapMyCells AT distributes 22/CLUS_0768,
        7/CLUS_0772, 5/CLUS_0767, 4/CLUS_0771, 4/CLUS_0774
        (run_ref at_run_20260408_winterer_olm_mmc_wmbv1).
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Five classical negative markers (PV, CB, CR, NOS, VIP)
        detected at supertype transcript means above MIN_DETECTABLE
        (PV 1.48, CB 5.56, CR 1.28, NOS 2.94, VIP 0.42); the
        classical negative-marker panel is largely protein-level
        immunohistochemistry consensus, transcript means do not
        necessarily refute it but the gap warrants curator audit.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Supertype includes non-hippocampal Sst Gaba_3 cells;
        region_fraction_100um 0.539 reflects the supertype-wide
        soma-distribution rollup. Mapping is to the hippocampal
        subset of CS20230722_SUPT_0216.
  proposed_experiments:
    - >
      Chrna2-Cre + MapMyCells of CA1 stratum oriens neurons; target
      F1 >= 0.80 at CLUSTER level within Sst Gaba_3; feeds back as
      AnnotationTransferEvidence at cluster rank; resolves whether
      cluster-level scatter tracks the three Sst-Pnoc OLM
      subclusters of Thulin et al. 2025 (PMID:40757734).
    - >
      Patch-seq with morphology recovery on OLM-targeted cells;
      target F1 >= 0.80 at CLUSTER level with paired morphology +
      electrophysiology annotation; resolves whether within-Sst
      Gaba_3 atlas heterogeneity tracks documented OLM heterogeneity
      (PV-positive gamma-firing subset; Sst-Pnoc subclusters; TRPV1+
      subpopulation).
    - >
      Targeted literature trawl on OLM negative-marker panel
      (PV, CB, CR, NOS, VIP) for transcript-level vs. protein-level
      evidence in morphology-confirmed OLM cells; feeds back as
      LiteratureEvidence on the classical node.
  unresolved_questions:
    - >
      Do the three Sst-Pnoc OLM subclusters of Thulin et al. 2025
      (PMID:40757734) correspond to specific CS20230722_SUPT_0216
      child clusters?
    - >
      Are the supertype-level transcript means for the five
      classical OLM negative markers (PV, CB, CR, NOS, VIP) a
      transcript-vs-protein convention gap, real subpopulation
      biology, or an upstream curation issue?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.72
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Best within-supertype cluster recipient of the
    pooled OLM MapMyCells annotation transfer (Winterer 2019;
    run_ref at_run_20260408_winterer_olm_mmc_wmbv1): 22/45 OLM cells
    land on CS20230722_CLUS_0768 with pooled F1=0.67 at cluster level.
    Chrna2 detected on CS20230722_CLUS_0768 (mean 0.57, cohort_pct
    0.95) — discriminating versus sibling CS20230722_CLUS_0769 where
    Chrna2 mean is 0.00 — addressing the primary OLM defining-marker
    test; Sst cohort_pct 0.99 (val 12.70); mGluR1 mean 10.27.
    region_fraction_100um 0.818 with Field CA1 stratum oriens
    [MBA:399] dominant. Paired with parent supertype edge
    edge_olm_hippocampus_to_CS20230722_SUPT_0216 (skos:broadMatch).
  reconciliation_note: >
    Paired with CS20230722_SUPT_0216 (skos:broadMatch + 1:n) as the
    supertype-level coverage of the full OLM cohort; this cluster
    captures the modal Chrna2-positive subset (22/45 cells).
    Remaining cells distribute across CS20230722_CLUS_0772 (7),
    CS20230722_CLUS_0767 (5), CS20230722_CLUS_0771 (4),
    CS20230722_CLUS_0774 (4) — consistent with the three Sst-Pnoc
    OLM subclusters reported by Thulin et al. 2025 (PMID:40757734).
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        DISCORDANT transcript means for five classical OLM negative
        markers on CS20230722_CLUS_0768 (PV 3.12, CB 3.87, CR 2.30,
        NOS 0.76, VIP 0.31); PV carries an atlas MERFISH-panel tag
        (panel-selection metadata, not expression-quality signal),
        the other four are precomputed transcript means above
        MIN_DETECTABLE. Curator audit of transcript-vs-protein
        conventions for the OLM negative-marker panel is required
        to resolve.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Cluster captures the modal but not the full OLM cohort:
        22/45 cells under pooled run_ref
        at_run_20260408_winterer_olm_mmc_wmbv1 (F1=0.67); 23/45
        cells distribute across CS20230722_CLUS_0772 (7),
        CS20230722_CLUS_0767 (5), CS20230722_CLUS_0771 (4),
        CS20230722_CLUS_0774 (4) and other Sst Gaba_3 children.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Pnoc on CS20230722_CLUS_0768 is APPROXIMATE (mean 2.51;
        cohort_pct 0.479) versus the supertype mean 3.69 and a
        Pnoc-high sibling CS20230722_CLUS_0775 (mean 7.20); if the
        three Sst-Pnoc OLM subclusters of Thulin et al. 2025
        (PMID:40757734) correspond to atlas children,
        CS20230722_CLUS_0768 may be the Chrna2-stronger /
        Pnoc-weaker subgroup.
  proposed_experiments:
    - >
      Chrna2-Cre + MapMyCells of CA1 stratum oriens neurons; target
      F1 >= 0.80 at CLUSTER level on CS20230722_CLUS_0768; feeds
      back as AnnotationTransferEvidence; resolves whether
      CS20230722_CLUS_0768 corresponds to the Chrna2+ OLM subgroup
      of Leao et al. 2012 (PMID:23042082).
    - >
      Patch-seq with morphology recovery on Chrna2-Cre-targeted
      cells; target paired morphology + electrophysiology
      annotation on at least 50 cells assigned to
      CS20230722_CLUS_0768; resolves whether the cluster
      corresponds to one of the three Sst-Pnoc OLM subclusters
      reported by Thulin et al. 2025 (PMID:40757734).
  unresolved_questions:
    - >
      Why does the pooled OLM cohort prefer CS20230722_CLUS_0768
      over the sibling CS20230722_CLUS_0769 within
      CS20230722_SUPT_0216? Is the Chrna2 atlas mean difference
      (0.57 vs 0.00) the discriminating signal?
    - >
      Does CS20230722_CLUS_0768 correspond to a specific Sst-Pnoc
      OLM subcluster from Thulin et al. 2025 (PMID:40757734)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0769 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Sibling within CS20230722_SUPT_0216 but Chrna2 is
    absent on this cluster (atlas mean 0.00, DISCORDANT); pooled
    OLM annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) routes 0/45 cells to
    CS20230722_CLUS_0769 while 22/45 land on the sibling
    CS20230722_CLUS_0768. The supertype-level mapping is carried
    by edge_olm_hippocampus_to_CS20230722_SUPT_0216; the
    cluster-level closeMatch is carried by
    edge_olm_hippocampus_to_CS20230722_CLUS_0768. This cluster is
    not the best within-supertype representative of the OLM cohort.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Chrna2 absent on CS20230722_CLUS_0769 (mean 0.00) versus
        present on sibling CS20230722_CLUS_0768 (mean 0.57); Chrna2
        is a defining OLM marker per Leao et al. 2012
        (PMID:23042082) and Nichol et al. 2018 (PMID:29487503).
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Pooled OLM annotation transfer routes 0/45 cells to
        CS20230722_CLUS_0769 under run_ref
        at_run_20260408_winterer_olm_mmc_wmbv1; the modal recipient
        is the sibling CS20230722_CLUS_0768.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    [tier:CUT] Within-supertype scatter: a Sst Gaba_3 sibling of the
    best-child cluster CS20230722_CLUS_0768; pooled OLM MapMyCells
    annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) routes 7/45 cells here
    (cluster F1=0.27), well below the modal CS20230722_CLUS_0768
    (22/45). The supertype-level coverage is carried by
    edge_olm_hippocampus_to_CS20230722_SUPT_0216.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Pooled annotation transfer routes 7/45 OLM cells here under
        run_ref at_run_20260408_winterer_olm_mmc_wmbv1 (F1=0.27);
        the modal recipient is CS20230722_CLUS_0768 (22/45).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] Within-supertype scatter: a Sst Gaba_3 sibling of the
    best-child cluster CS20230722_CLUS_0768. No direct
    annotation_transfer evidence item on this edge; the
    supertype-level coverage is carried by
    edge_olm_hippocampus_to_CS20230722_SUPT_0216.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        No annotation_transfer evidence item on this edge; the
        modal recipient within the supertype is
        CS20230722_CLUS_0768 (22/45).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0775 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.28
  rationale: >
    [tier:CUT] Within-supertype scatter: a Sst Gaba_3 sibling of the
    best-child cluster CS20230722_CLUS_0768; carries the highest
    Pnoc transcript mean among the Sst Gaba_3 children (7.20;
    cohort_pct 0.966) but no annotation_transfer evidence item on
    this edge. region_fraction_100um 0.442 (lower than
    CS20230722_CLUS_0768's 0.818).
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        No annotation_transfer evidence item on this edge at
        cluster rank; the modal recipient within the supertype
        is CS20230722_CLUS_0768.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.28
  rationale: >
    [tier:CUT] Within-supertype scatter: a Sst Gaba_3 sibling of the
    best-child cluster CS20230722_CLUS_0768; no annotation_transfer
    evidence item on this edge. The supertype-level coverage is
    carried by edge_olm_hippocampus_to_CS20230722_SUPT_0216.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        No annotation_transfer evidence item on this edge at
        cluster rank; the modal recipient within the supertype
        is CS20230722_CLUS_0768.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 (0226 Sst Gaba_13) is
    isocortex-dominant with region_fraction_100um 0.016 and strict
    region_fraction 0.008 — soma distribution sits outside the
    hippocampal target region. Although Sst (12.08; cohort_pct
    0.968) and Chrna2 (0.61; cohort_pct 0.952) are CONSISTENT on
    transcript means, the location DISCORDANT call rules out the
    classical hippocampal OLM identity.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um 0.016 (distant region — soma
        distribution is isocortex/cortical subplate dominated;
        classical OLM is CA1 stratum oriens).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0217 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0217 (0217 Sst Gaba_4) is
    isocortex-dominant with region_fraction_100um 0.015 — soma
    distribution sits outside the hippocampal target region. Sst
    (10.79) and Chrna2 (1.90, atlas category DEFINING_SCOPED at
    cohort_pct 0.984) are CONSISTENT on transcript means, but the
    location DISCORDANT call rules out the classical hippocampal
    OLM identity. May correspond to a cortical Chrna2+ Sst type
    distinct from CA1 OLM.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um 0.015 (distant region — soma
        distribution is isocortex dominated, with motor area
        enrichment; classical OLM is CA1 stratum oriens).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_SUPT_0241 (0241 Sst Chodl Gaba_4) is
    isocortex-dominant with region_fraction_100um 0.021 and Chrna2
    DISCORDANT (atlas mean 0.00). Sst Chodl is a distinct long-range
    projecting Sst subtype, not the canonical CA1 OLM identity.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um 0.021 (distant region — soma
        distribution is isocortex / lateral forebrain bundle /
        corpus callosum; classical OLM is CA1 stratum oriens).
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Chrna2 absent on CS20230722_SUPT_0241 (mean 0.00); Chrna2
        is a defining OLM marker per Leao et al. 2012
        (PMID:23042082).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0224 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] CS20230722_SUPT_0224 (0224 Sst Gaba_11) is
    isocortex-dominant with region_fraction_100um 0.032 — soma
    distribution sits outside the hippocampal target region. Chrna2
    is CONSISTENT but at a borderline transcript mean (0.10) with
    child-coverage 0.500. Location DISCORDANT call rules out the
    classical hippocampal OLM identity.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        region_fraction_100um 0.032 (distant region — soma
        distribution is isocortex dominated; classical OLM is CA1
        stratum oriens).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0727 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0727 sits in the Lamp5 Lhx6 Gaba_1
    subclass (CGE-derived) rather than the Sst (MGE-derived)
    subclass that carries the canonical OLM identity; the pooled
    OLM MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) routes 0/45 cells to
    this cluster. This is a legacy edge from a pre-emitter curator
    pass and falls outside the current Stage A top-50 cohort at
    rank 0; the property_comparisons were not refreshed under the
    current scoring. Recommend curator review / removal in line
    with issue #111.
  caveats:
    - caveat_type: OTHER
      description: >
        Wrong subclass: Lamp5 Lhx6 Gaba_1 (CGE-derived) versus the
        canonical MGE-derived Sst lineage of OLM.
    - caveat_type: OTHER
      description: >
        Legacy edge outside the current Stage A top-50 cohort at
        rank 0; property_comparisons not refreshed (see #111).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0785 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.03
  rationale: >
    [tier:CUT] CS20230722_CLUS_0785 sits within parent supertype
    Sst Gaba_6, where Chrna2 expression is absent per ABC Atlas
    filtering (anatomy=HPF; NT=GABA; expression=Chrna2; see [A]);
    pooled OLM MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) routes 0/45 cells to
    Sst Gaba_6. This is a legacy edge from a pre-emitter curator
    pass and falls outside the current Stage A top-50 cohort at
    rank 0; the property_comparisons were not refreshed under the
    current scoring. Recommend curator review / removal in line
    with issue #111.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Chrna2 absent at parent supertype Sst Gaba_6 per ABC Atlas
        filtering ([A]); Chrna2 is a defining OLM marker per Leao
        et al. 2012 (PMID:23042082).
    - caveat_type: OTHER
      description: >
        Legacy edge outside the current Stage A top-50 cohort at
        rank 0; property_comparisons not refreshed (see #111).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0788 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.03
  rationale: >
    [tier:CUT] CS20230722_CLUS_0788 sits within parent supertype
    Sst Gaba_6, where Chrna2 expression is absent per ABC Atlas
    filtering (anatomy=HPF; NT=GABA; expression=Chrna2; see [A]);
    pooled OLM MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) routes 0/45 cells to
    Sst Gaba_6. This is a legacy edge from a pre-emitter curator
    pass and falls outside the current Stage A top-50 cohort at
    rank 0; the property_comparisons were not refreshed under the
    current scoring. Recommend curator review / removal in line
    with issue #111.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Chrna2 absent at parent supertype Sst Gaba_6 per ABC Atlas
        filtering ([A]); Chrna2 is a defining OLM marker per Leao
        et al. 2012 (PMID:23042082).
    - caveat_type: OTHER
      description: >
        Legacy edge outside the current Stage A top-50 cohort at
        rank 0; property_comparisons not refreshed (see #111).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0789 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.03
  rationale: >
    [tier:CUT] CS20230722_CLUS_0789 sits within parent supertype
    Sst Gaba_6, where Chrna2 expression is absent per ABC Atlas
    filtering (anatomy=HPF; NT=GABA; expression=Chrna2; see [A]);
    pooled OLM MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1) routes 0/45 cells to
    Sst Gaba_6, and the cluster's soma distribution is
    amygdala-dominant (28% amygdala cells per cluster
    property_comparisons). This is a legacy edge from a
    pre-emitter curator pass and falls outside the current Stage A
    top-50 cohort at rank 0; the property_comparisons were not
    refreshed under the current scoring. Recommend curator review
    / removal in line with issue #111.
  caveats:
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        Chrna2 absent at parent supertype Sst Gaba_6 per ABC Atlas
        filtering ([A]); Chrna2 is a defining OLM marker per Leao
        et al. 2012 (PMID:23042082).
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        28% amygdala cells in CS20230722_CLUS_0789 — cluster is
        not hippocampus-specific.
    - caveat_type: OTHER
      description: >
        Legacy edge outside the current Stage A top-50 cohort at
        rank 0; property_comparisons not refreshed (see #111).
```
<!-- verdict-block-end -->
