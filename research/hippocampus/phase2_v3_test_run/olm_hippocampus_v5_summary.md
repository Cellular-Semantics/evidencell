# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*2026-03-25 · Source: `kb/graphs/hippocampus/hippocampus_OLM.yaml`*

---

## Introduction

OLM cells are a well-characterised population of CA1 GABAergic interneurons defined by horizontally oriented somata and dendrites in stratum oriens and a dense axonal arbour in stratum lacunosum-moleculare, where they innervate the apical tufts of pyramidal cells [1][2][3]. They express somatostatin together with the nicotinic α2 subunit Chrna2 and group I metabotropic glutamate receptor mGluR1, generate theta-frequency feedback inhibition, and gate intrahippocampal versus entorhinal input through CA1 [7][8]. Establishing a transcriptomic anchor for this morphologically and functionally defined type is necessary for downstream mechanistic work and for placing it within reference whole-brain taxonomies.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] (CA1) | [1][2] |
| Axon target | hippocampus stratum lacunosum moleculare [UBERON:0007640] | [1][3] |
| NT | GABAergic | [4][5] |
| Defining markers | Sst, Chrna2, mGluR1 (Grm1) | [6][7][8][2] |
| Negative markers | PV, CB, CR, NOS, VIP | — |
| Neuropeptides | Sst, Npy, Pnoc | [7][9] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical light-microscopy + biocytin fills · CA1 stratum oriens · [1][2][3]
  > oriens-lacunosum-moleculare (OLM) cells also had both the cell body and dendritic tree in the stratum oriens, but their horizontally running dendrites were often densely decorated with long spines. Their axon frequently originated from a proximal dendrite, and after ramification the main axon without boutons could be followed into the stratum lacunosum-moleculare. In this layer the axon ramified extensively bearing heavily packed varicosities. Some axon collaterals with boutons were also observed in the stratum oriens.
  > — Zemankovics et al. 2010, Anatomical Location and Morphology · [1] <!-- quote_key: 3106274_e54f60e9 -->

  > These CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare (SLM; Cajal, 1911;(McBain et al., 1994)(Sik et al., 1995)(Maccaferri et al., 2000)(Losonczy et al., 2002)(Leão et al., 2012)
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_2414c9e9 -->

  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [3] <!-- quote_key: 229694907_6865b9db -->

- **NT type:** GABAergic · [4][5]
  > GABAergic inhibitory oriens lacunosum-moleculare (O-LM) cells in the hippocampal area CA1 of the rat
  > — Böhm et al. 2015, Anatomical Location and Morphology · [4] <!-- quote_key: 15101210_5604b9a4 -->

- **Sst marker:** transgenic GFP + ISH on morphology-recovered cells · [5][6][7]
  > Type I interneurons had large horizontally oriented cell somata located at the border of stratum oriens and the alveus, indicating that these cells were most likely identical with the previously described somatostatin-positive oriens-lacunosum moleculare (O-LM) cells (Freund et al., 1998). Reconstruction of type I interneurons revealed their horizontally oriented dendritic tree in stratum oriens and their axonal arborizations in stratum lacunosum-moleculare (n = 5) (Fig. 2 A), and in situ hybridization for somatostatin showed that four of four cells were indeed positive for somatostatin (Fig. 2 B)
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_215c5f40 -->

- **Chrna2 marker:** Chrna2-Cre transgenic targeting + morphological reconstruction · [2][8][7]
  > The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_644f1e68 -->

  > The vast diversity of GABAergic interneurons is believed to endow hippocampal microcircuits with the required flexibility for memory encoding and retrieval. However, dissection of the functional roles of defined interneuron types has been hampered by the lack of cell-specific tools. We identified a precise molecular marker for a population of hippocampal GABAergic interneurons known as oriens lacunosum-moleculare (OLM) cells. By combining transgenic mice and optogenetic tools, we found that OLM cells are important for gating the information flow in CA1, facilitating the transmission of intrahippocampal information (from CA3) while reducing the influence of extrahippocampal inputs (from the entorhinal cortex). Furthermore, we found that OLM cells were interconnected by gap junctions, received direct cholinergic inputs from subcortical afferents and accounted for the effect of nicotine on synaptic plasticity of the Schaffer collateral pathway. Our results suggest that acetylcholine acting through OLM cells can control the mnemonic processes executed by the hippocampus.
  > — Leão et al. 2012, Projection Patterns and Connectivity · [8] <!-- quote_key: 7952877_ae03c6e0 -->

- **mGluR1 marker:** patch + post-hoc ISH on identified OLM cells · [6][7]
  > Type I interneurons responded with a large inward current of ≈ 224pA, were positive for somatostatin, and the majority expressed both mGluR1 and mGluR5
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_17d10a9e -->

- **Pnoc neuropeptide:** scRNA-seq subcluster analysis · [9][7]
  > The Chrna2 gene expression is restricted to the stratum oriens in the hippocampus in both rats and mice (Ishii et al., 2005) and is specifically expressed in a subset of CA1 hippocampal interneurons, the oriens lacunosummoleculare (OLM) cells (Leão et al., 2012). Traditionally, OLM cells have been identified through their expression of somatostatin (Sst). However, in-depth single-cell transcriptomic cluster analysis has unveiled at least 11 distinct subpopulations of Sst-expressing interneurons (2017). Within these clusters, various classes of interneurons were identified, including back projecting, hippocampo-septal, oriens-bistratified, and OLM cells. Among these clusters, OLM cells were classified into a Sst and Prepronociceptin (Pnoc) co-expressing group (further divided into three subclusters)
  > — Thulin et al. 2025, Projection Patterns and Connectivity · [9] <!-- quote_key: 280420054_8a6529c5 -->

- **Npy neuropeptide:** scRNA-seq + ISH on Chrna2-Cre cells · [7]
  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_8d16e821 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer from the Winterer 2019 Chrna2-Cre-targeted and Htr3a-Cre-targeted OLM cohorts (pooled OLM; n=45 cells after bootstrap filtering) and marker-expression alignment from WMBv1 precomputed stats together support a supertype-level mapping to 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.97; see figure and property comparison table). Within that supertype, OLM cells distribute across several sibling clusters but concentrate most strongly on 0768 Sst Gaba_3 [CS20230722_CLUS_0768] (F1=0.65), which is also the only Sst Gaba_3 child carrying detectable Chrna2 expression in the cohort percentile band consistent with the classical defining marker.

![Filtered AT figure for OLM hippocampus](figures/f1_for_olm_hippocampus.png)

*F1 across taxonomy levels for the pooled OLM cohort (Sst-OLM + Htr3a-OLM merged to a single OLM group; n=45 cells classified). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells from the source group. With a single pooled source, Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The high CLASS/SUBCLASS/SUPERTYPE F1 with cluster-level scatter across Sst Gaba_3 children is consistent with the within-OLM subcluster heterogeneity reported by Thulin et al. 2025 [9].*

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

This Sst-subclass supertype is the cleanest transcriptomic resolution at which the Winterer 2019 OLM cohort lands: 43 of 45 classified cells are assigned here (pooled F1=0.97 at supertype level; F1=0.99 at the parent Sst Gaba subclass and 07 CTX-MGE GABA class). The mapping is a supertype-level broad correspondence because OLM cells then split across several Sst Gaba_3 child clusters rather than concentrating on a single one — a pattern that matches the three-subcluster Sst+Pnoc structure reported by Thulin et al. 2025 [9]. Property alignment is strong on all three defining markers and on the Sst+Npy+Pnoc neuropeptide triad (see property table); negative-marker discordances (CB, NOS, PV at trace levels) are read as background expression in the atlas pseudobulk rather than as biological refutation of the OLM call.

**Table 1 — Property comparison (0216 Sst Gaba_3).**

| Property | Classical | Supertype (SUPT_0216) | Best cluster (CLUS_0768) | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | Hippocampal formation [MBA:1089] count_100um=2145; Field CA1 [MBA:382] count_100um=1559; CA1 stratum oriens [MBA:399] count_100um=1463 | CA1 stratum oriens [MBA:399] count_100um=261 | CONSISTENT (`region_fraction_100um: 0.539` supertype; `0.818` cluster) |
| NT type | GABAergic | not asserted at supertype | GABA | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Sst | defining marker | 11.44 (cohort_pct 0.905; child-coverage 1.000) | 12.70 (cohort_pct 0.992) | CONSISTENT |
| Chrna2 | defining marker | 0.61 (cohort_pct 0.952; child-coverage 0.667) | 0.57 (cohort_pct 0.950) | CONSISTENT |
| mGluR1 (Grm1) | defining marker | 9.33 | 10.27 | CONSISTENT |
| Npy | neuropeptide | 5.07 (cohort_pct 0.794; child-coverage 1.000) | 7.58 (cohort_pct 0.857) | CONSISTENT |
| Pnoc | neuropeptide | 3.69 (cohort_pct 0.667; child-coverage 0.889) | 2.51 (cohort_pct 0.479) | SUPT: CONSISTENT; CLUS: APPROXIMATE |
| PV | absent | 1.48 | 3.12 (atlas category: MERFISH) | DISCORDANT |
| CB | absent | 5.56 | 3.87 | DISCORDANT |
| CR | absent | 1.28 | 2.30 | DISCORDANT |
| NOS | absent | 2.94 | 0.76 | DISCORDANT |
| VIP | absent | 0.42 | 0.31 | DISCORDANT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(2 of 3 covered Sst Gaba_3 children show Chrna2 detectable (`child-coverage 0.667`); Sst and Npy are covered at all children (`child-coverage 1.000`). Within-supertype cluster-level F1 distribution leads on CLUS_0768; remaining Sst Gaba_3 children — CLUS_0772, CLUS_0767, CLUS_0771, CLUS_0774, CLUS_0773 — each capture ≤7 OLM cells.)*

**Table 2 — Evidence support (0216 Sst Gaba_3).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 precomputed expression on SUPT_0216 | Atlas metadata | PARTIAL | region_fraction_100um=0.539 | atlas-internal |
| Winterer 2019 → WMBv1 MapMyCells (pooled OLM, supertype level) | Annotation transfer | SUPPORT | F1=0.97 (43/45 cells) | [7] |

**Supporting evidence**
- WMBv1 precomputed mean expression shows OLM defining markers concentrated at this supertype: Sst 11.44 (cohort percentile 0.905), Chrna2 0.61 (cohort percentile 0.952), mGluR1 9.33, with child-cluster coverage of 1.000 for Sst/Npy and 0.667 for Chrna2 (atlas-internal).
- MapMyCells annotation transfer of the pooled OLM cohort places 43 of 45 classified cells on this supertype (F1=0.97; `at_run_20260408_winterer_olm_mmc_wmbv1`); the parent Sst Gaba subclass and 07 CTX-MGE GABA class both receive F1=0.99. The Winterer 2019 cohort was identified by Chrna2-Cre and Htr3a-Cre targeting in CA1, so the AT signal is direct evidence on Cre-targeted OLM cells rather than generic Sst+ convergence [7].

  > MapMyCells annotation transfer of the pooled OLM cohort (46 cells; Sst-OLM + Htr3a-OLM combined; GSE124847, Winterer 2019) strongly supports the parent Sst Gaba_3 supertype (43/45 classified cells; pooled F1=0.97; pooled CLASS/SUBCLASS F1=0.99) but OLM cells scatter across sibling clusters 0767–0774 within it. Cluster 0769 specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/45, best pooled cluster-level F1=0.65). This indicates OLM identity is captured at the Sst Gaba_3 supertype rather than at any single child cluster. The high pooled supertype F1 reflects removal of the inter-source mis-attribution penalty that depresses per-source F1; both Sst-OLM and Htr3a-OLM converge on the same Sst Gaba_3 supertype.
  > — Winterer et al. 2019 · [7]

**Marker evidence provenance**
- *Sst:* atlas category NEUROPEPTIDE; primary citations Oliva 2000 [5] and Winterer 2019 [7] (Chrna2-Cre + Htr3a-Cre targeted cells, scRNA-seq). Concordant across all five Sst Gaba_3 children (`child-coverage 1.000`).
- *Chrna2:* primary Leão 2012 [8] (Chrna2-Cre transgenic with morphology recovery) + Winterer 2019 [7]. Atlas-side mean 0.61 with `child-coverage 0.667` — present in two of three covered Sst Gaba_3 children, supporting within-supertype heterogeneity rather than a uniform-supertype call.
- *mGluR1 (Grm1):* primary Hooft 2000 [6] (patch + ISH); not annotated in atlas defining-marker or NEUROPEPTIDE panels, so concordance rests on the precomputed mean expression value alone.
- *Pnoc:* primary Thulin 2025 [9] (scRNA-seq; identified Pnoc co-expression and three OLM subclusters). Supertype-mean Pnoc 3.69 (cohort percentile 0.667) with `child-coverage 0.889`.
- ⚠ **Atlas annotation/expression mismatch (PV):** PV is not on the classical defining-marker list (it is an OLM negative marker); the atlas tags PV as MERFISH for CLUS_0768. The MERFISH category is panel-selection metadata rather than an expression-quality assertion, so the PV value 3.12 at the cluster (and 1.48 at the supertype) is treated as panel-level inclusion rather than evidence of OLM PV co-expression — flagged for review.

**Concerns**
- Cluster-level scatter inside Sst Gaba_3 means the supertype does not collapse to a single OLM cluster in this atlas release. Best supported child is CLUS_0768 (see next section); other children of the supertype are weakly populated by the AT and are listed in the audit table.
- Negative markers PV, CB, CR, NOS, VIP all read DISCORDANT at the supertype against the classical absence, but the values are trace-to-moderate and likely reflect background contamination in pseudobulk averaging rather than coexpression in the OLM population *(note: interpretation based on standard handling of low-magnitude pseudobulk negative-marker reads)*.
- Sst Gaba_3 also draws cells from prosubiculum and posterior amygdala in WMBv1, so the supertype is not hippocampus-exclusive (`region_fraction_100um: 0.539`); the OLM-relevant population is the CA1 stratum-oriens fraction within it.

**What would upgrade confidence**
- Per-cell MERFISH or in situ on Chrna2+ stratum-oriens neurons confirming the within-supertype assignment to CLUS_0768 vs. its siblings.
- Patch-seq of Chrna2-Cre cells in CA1 stratum oriens with morphological reconstruction (target: AT F1 ≥ 0.80 at cluster level on the same WMBv1 build) to test whether the OLM type can be resolved at rank 0 once cell counts are higher.

### 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · 🟡 MODERATE

The best-supported child cluster within 0216 Sst Gaba_3 is 0768 Sst Gaba_3 [CS20230722_CLUS_0768], which receives the largest share of the pooled OLM cohort at cluster level (22 of 45 classified cells; pooled cluster-level F1=0.65; coverage 0.48; purity 1.0). Defining-marker concordance is strong: Sst 12.70 (cohort percentile 0.992), Chrna2 0.57 (cohort percentile 0.950), mGluR1 10.27 — the only Sst Gaba_3 child with the full marker triad above detection in the cohort percentile range expected from the classical literature. CA1 stratum-oriens enrichment is also highest for this cluster (`region_fraction_100um: 0.818`). This is the supertype's best-child correspondence to the OLM type and is paired with the SUPT_0216 mapping above.

**Table 1 — Property comparison (0768 Sst Gaba_3).** See the property table under 0216 Sst Gaba_3 — the "Best cluster" column reports this cluster's values directly.

**Table 2 — Evidence support (0768 Sst Gaba_3).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 precomputed expression on CLUS_0768 | Atlas metadata | PARTIAL | region_fraction_100um=0.818 | atlas-internal |
| Winterer 2019 → WMBv1 MapMyCells (pooled OLM, cluster level) | Annotation transfer | SUPPORT | F1=0.65 (22/45 cells) | [7] |

**Supporting evidence**
- Highest CA1 stratum-oriens enrichment of any candidate (`region_fraction_100um: 0.818`; strict `region_fraction: 0.458`). Stage A scored this cluster as the top of its 50-member region-filtered GABAergic cohort (score 10 vs next-best 9), driven by Sst at applied_score 2.0 (cohort percentile 0.992) and Chrna2 at applied_score 1.0 (cohort percentile 0.950) (atlas-internal).
- MapMyCells pooled-cohort transfer places 22 of 45 OLM cells on CLUS_0768 (F1=0.65, coverage 0.48, purity 1.0; `at_run_20260408_winterer_olm_mmc_wmbv1`). Per-cell labels in the Winterer source come from Chrna2-Cre and Htr3a-Cre transgenic targeting in dorsal CA1 [7][8] — direct cellular provenance, not generic Sst+ convergence.

**Marker evidence provenance**
- Marker provenance as for SUPT_0216 above, with the addition that Chrna2 detection on CLUS_0768 specifically (`Chrna2: 0.57; cohort_pct 0.950`) anchors the within-supertype call. Of the Sst Gaba_3 children with edge-level property comparisons in the facts file, CLUS_0769 shows Chrna2 below detection (0.00) and is excluded as the OLM-bearing child by this single property even though it carries other Sst Gaba_3 features.
- ⚠ **Atlas annotation/expression mismatch (PV):** as noted above — atlas tag MERFISH on a classical negative marker; informational only.

**Concerns**
- Cluster-level F1 of 0.65 is moderate: 23 of 45 OLM cells fall outside this cluster (primarily CLUS_0772 with 7 cells and CLUS_0767/0771/0774 with 4–5 each). The within-supertype scatter likely reflects the three-subcluster Sst+Pnoc OLM structure reported by Thulin et al. 2025 [9] rather than misclassification; CLUS_0768 is one face of a multi-cluster OLM substructure, not the whole of it.
- Negative-marker discordances (PV 3.12, CB 3.87, CR 2.30, NOS 0.76, VIP 0.31) are as discussed for the supertype — pseudobulk background rather than refutation *(note: same interpretation as for SUPT_0216)*.

**What would upgrade confidence**
- A morphology-confirmed Chrna2-Cre patch-seq cohort with ≥100 OLM cells (target: cluster-level F1 ≥ 0.80) would test whether OLM identity at the current WMBv1 release is best read as one cluster (CLUS_0768) or as a structured multi-cluster pattern within Sst Gaba_3.
- Sex-stratified analysis of CLUS_0768 to populate the currently-NOT_ASSESSED sex ratio property comparison.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | 🟡 MODERATE | Pooled-OLM AT F1=0.97 at supertype | Primary (supertype) |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 66 | 🟡 MODERATE | Pooled-OLM AT F1=0.65, full marker triad | Primary (best child of SUPT_0216) |
| 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 334 | 🔴 LOW | Chrna2=0.00 on cluster; 0/45 OLM cells | Eliminated (Chrna2 absent on this child) |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 190 | 🔴 LOW | Pooled-OLM AT F1=0.27 (7 cells) | Eliminated (secondary AT scatter) |
| 0773 Sst Gaba_3 [CS20230722_CLUS_0773] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 156 | 🔴 LOW | Pooled-OLM AT F1=0.04 (1 cell) | Eliminated (AT scatter, not lead) |
| 0775 Sst Gaba_3 [CS20230722_CLUS_0775] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 143 | 🔴 LOW | 0 OLM cells; prosubiculum-enriched | Eliminated (off-target region scatter) |
| 0770 Sst Gaba_3 [CS20230722_CLUS_0770] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | 404 | 🔴 LOW | 0 OLM cells in cluster | Eliminated (no AT support) |
| 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | — | 4064 | 🔴 LOW | `region_fraction_100um: 0.016`; Isocortex-resident | Eliminated (wrong region — cortex) |
| 0217 Sst Gaba_4 [CS20230722_SUPT_0217] | — | 14335 | 🔴 LOW | `region_fraction_100um: 0.015`; Isocortex-resident | Eliminated (wrong region — cortex) |
| 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] | — | 2905 | 🔴 LOW | Chrna2=0.00 + Isocortex/white matter | Eliminated (Chrna2 absent + wrong region) |
| 0224 Sst Gaba_11 [CS20230722_SUPT_0224] | — | 2677 | 🔴 LOW | `region_fraction_100um: 0.032`; Isocortex-resident | Eliminated (wrong region — cortex) |
| 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | 0203 Lamp5 Lhx6 Gaba_1 | 59 | 🔴 REFUTED | 0/46 OLM cells; CGE-derived Lamp5 subclass | Eliminated (wrong subclass) |
| 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | 0219 Sst Gaba_6 | 51 | 🔴 REFUTED | Chrna2 absent on parent supertype; 0/46 OLM cells | Eliminated (Chrna2 absent) |
| 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | 0219 Sst Gaba_6 | 98 | 🔴 REFUTED | Chrna2 absent on parent supertype; 0/46 OLM cells | Eliminated (Chrna2 absent) |
| 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | 0219 Sst Gaba_6 | 222 | 🔴 REFUTED | Chrna2 absent on parent supertype; 28% amygdala | Eliminated (Chrna2 absent) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** OLM is defined here as a CLASSICAL_MULTIMODAL classical node: CA1 stratum-oriens GABAergic interneuron with horizontal dendrites in stratum oriens and axonal arbour in stratum lacunosum-moleculare [1][2][3], defined by Sst, Chrna2, and mGluR1 expression [6][7][8][2], with Sst, Npy, and Pnoc co-expressed as neuropeptides [7][9]. The classical node carries a heterogeneity note recording subpopulation signal (PV+ OLM subset; Sst/Pnoc three-subcluster structure per Thulin et al. 2025 [9]) — this is the basis for reading cluster-level scatter inside Sst Gaba_3 as biology rather than failure.

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
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix.csv`](../../kb/annotation_transfer_runs/at_run_20260408_winterer_olm_mmc_wmbv1/f1_matrix.csv) |
| Caveats | Source dataset has only 46 OLM cells (Winterer 2019); 45 retained after bootstrap filtering. The "Sst-OLM" and "Htr3a-OLM" source labels reflect Cre-driver subgroups in the Winterer dataset and are scored separately. At cluster (rank 0) resolution F1 is low across all candidates (max 0.26 for Sst-OLM → CLUS_0768 within Sst Gaba_3 supertype) — the OLM cell type is captured at supertype/subclass level (Sst Gaba_3 / Sst Gaba; F1 ≈ 0.65) but scatters across sibling clusters. This is a real biological signal, not a methodological failure: OLM is a transcriptomic subtype not yet resolved at WMBv1 cluster rank. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `8c61574` at 2026-06-08T15:36:20+00:00 from [kb/graphs/hippocampus/hippocampus_OLM.yaml](kb/graphs/hippocampus/hippocampus_OLM.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_olm_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | [7] |
| edge_olm_hippocampus_to_CS20230722_CLUS_0768 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | [7] |
| edge_olm_to_wmb_clus_0769 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; PARTIAL | [7] |
| edge_olm_hippocampus_to_CS20230722_CLUS_0772 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | [7] |
| edge_olm_hippocampus_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_hippocampus_to_CS20230722_CLUS_0775 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_hippocampus_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_hippocampus_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_hippocampus_to_CS20230722_SUPT_0217 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_hippocampus_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_hippocampus_to_CS20230722_SUPT_0224 | ATLAS_METADATA | PARTIAL | — |
| edge_olm_to_wmb_clus_0727 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; REFUTE | [7] |
| edge_olm_to_wmb_clus_0785 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL; REFUTE; REFUTE | [A][7] |
| edge_olm_to_wmb_clus_0788 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL; REFUTE; REFUTE | [A][7] |
| edge_olm_to_wmb_clus_0789 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL; REFUTE; REFUTE | [A][7] |

</details>

---

## Discussion

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) interneuron → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence (supertype-level broadMatch, 1:n), paired with a best-child correspondence to 0768 Sst Gaba_3 [CS20230722_CLUS_0768] at MODERATE confidence (closeMatch, 1:1). Key support: pooled-cohort MapMyCells annotation transfer of Chrna2-Cre/Htr3a-Cre-targeted OLM cells (F1=0.97 supertype; F1=0.65 cluster) and full Sst/Chrna2/mGluR1 marker concordance plus Sst+Npy+Pnoc neuropeptide concordance on the precomputed atlas stats. Key caveats: cluster-level scatter inside Sst Gaba_3 (DISTRIBUTED_ACROSS_CLUSTERS) consistent with within-OLM transcriptomic heterogeneity [9]; classical negative markers (PV, CB, CR, NOS, VIP) read DISCORDANT at trace-to-moderate atlas pseudobulk values and are treated as background.

No Cell Ontology term currently assigned. Candidate for CL contribution — the OLM type is a long-recognised CA1 GABAergic interneuron class with a defined marker triad (Sst + Chrna2 + mGluR1), morphological signature (horizontal SO dendrites, SLM axon), and functional role (theta-frequency feedback inhibition gating CA3 vs entorhinal input [8]); see `workflows/cl-term-request.md`.

### Proposed experiments and follow-ups

- **What:** Chrna2-Cre targeted scRNA-seq or MERFISH of CA1 stratum-oriens neurons. **Target:** ≥100 morphology-confirmed OLM cells; cluster-level AT F1 ≥ 0.80 on the current WMBv1 build. **Expected output:** AnnotationTransferEvidence resolving whether CLUS_0768 is one face of multi-cluster OLM substructure or the OLM cluster as such. **Resolves:** open questions 1, 2.
- **What:** Patch-seq of Chrna2+ stratum-oriens neurons with morphological reconstruction. **Target:** confirm in-cluster mGluR1 detection (currently atlas-only) and link electrophysiology + morphology to the WMBv1 cluster assignment. **Expected output:** AnnotationTransferEvidence + classical-side `PATCH_SEQ` `PropertySource`. **Resolves:** open question 3.
- **What:** Targeted literature trawl for OLM transcriptomic heterogeneity (PV+ OLM subset reports; Thulin 2025 follow-ups). **Target:** anchor or refute the PV+ OLM subset and the three-subcluster Sst+Pnoc structure within Sst Gaba_3. **Expected output:** LiteratureEvidence on the classical node. **Resolves:** open question 4.

### Open questions

1. Is the within-Sst Gaba_3 cluster-level scatter (best at CLUS_0768; secondary at CLUS_0772/0767/0771/0774) the OLM three-subcluster substructure reported by Thulin et al. 2025 [9], or AT noise from low-n source data?
2. Why does CLUS_0769 carry Chrna2=0.00 despite belonging to Sst Gaba_3, and what is the non-OLM identity of the cells in CLUS_0769?
3. Are the CA1 SO cells in CLUS_0768 morphology-confirmed OLM, and what is the identity of the prosubiculum and posterior-amygdala component of Sst Gaba_3 sibling clusters?
4. What is the relationship between the Sst Gaba_6 supertype (Chrna2-negative; rejected here) and the Sst+ stratum-oriens non-OLM populations described in classical literature (e.g. bistratified, hippocampo-septal)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280) | soma location, projection |
| [2] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503) | soma location, Chrna2 marker |
| [3] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464) | projection |
| [4] | Böhm et al. 2015 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702) | neurotransmitter type |
| [5] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798) | Sst marker |
| [6] | Hooft et al. 2000 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195) | Sst, mGluR1 markers |
| [7] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995) | Sst, Chrna2, Npy, AT source |
| [8] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082) | Chrna2 marker, function |
| [9] | Thulin et al. 2025 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734) | Pnoc, OLM subclusters |
| [A] | ABC Atlas — HPF/GABA/Chrna2 query | — ([view](https://tinyurl.com/a4f3kd4v)) | anatomy/NT/expression filter |

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.78
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Pooled-cohort annotation transfer of Chrna2-Cre
    and Htr3a-Cre targeted OLM cells (F1=0.97 in
    at_run_20260408_winterer_olm_mmc_wmbv1; 43/45 cells on
    CS20230722_SUPT_0216) plus Sst/Chrna2/mGluR1 CONSISTENT marker
    alignment (3 of 3 markers CONSISTENT) anchor the supertype-level
    broadMatch; OLM cells then scatter across Sst Gaba_3 children
    (best child CS20230722_CLUS_0768 F1=0.65), consistent with the
    three-subcluster Sst+Pnoc OLM structure reported by Thulin 2025.
  reconciliation_note: >
    Paired with edge_olm_hippocampus_to_CS20230722_CLUS_0768
    (skos:closeMatch + 1:1) — the supertype broadMatch captures the
    OLM type as a whole while CS20230722_CLUS_0768 is the
    best-supported child; both should be read together.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Within CS20230722_SUPT_0216 the pooled-OLM cohort distributes
        across CS20230722_CLUS_0768 (22 cells), CS20230722_CLUS_0772
        (7), CS20230722_CLUS_0767 (5), CS20230722_CLUS_0771 (4),
        CS20230722_CLUS_0774 (4), CS20230722_CLUS_0773 (1) — likely
        within-OLM transcriptomic heterogeneity (Thulin 2025) rather
        than methodological scatter.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical negative markers PV, CB, CR, NOS, VIP read
        DISCORDANT at supertype-mean values 1.48, 5.56, 1.28, 2.94,
        0.42 respectively; interpreted as pseudobulk background
        rather than refutation given the source OLM cohort was
        assayed by Chrna2-Cre and Htr3a-Cre transgenic targeting.
  proposed_experiments:
    - Chrna2-Cre patch-seq of CA1 stratum oriens with morphological
      reconstruction; target cluster-level AT F1 >= 0.80 against
      CCN20230722 (AnnotationTransferEvidence).
    - Targeted MERFISH of Chrna2+ stratum-oriens neurons to confirm
      within-supertype assignment to CS20230722_CLUS_0768 vs sibling
      Sst Gaba_3 clusters (AnnotationTransferEvidence).
    - Literature trawl on OLM transcriptomic heterogeneity (PV+ OLM
      subset; Sst+Pnoc subclusters per Thulin 2025) to anchor the
      within-supertype scatter to a biological substructure
      (LiteratureEvidence).
  unresolved_questions:
    - Is the cluster-level scatter inside CS20230722_SUPT_0216 the
      three-subcluster Sst+Pnoc OLM structure (Thulin 2025) or AT
      noise from low source-n?
    - Why does CS20230722_CLUS_0769 carry Chrna2=0.00 despite
      belonging to Sst Gaba_3?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Within CS20230722_SUPT_0216, the pooled OLM cohort
    concentrates most strongly on CS20230722_CLUS_0768 (F1=0.65 in
    at_run_20260408_winterer_olm_mmc_wmbv1; 22/45 cells), and this
    cluster carries the full Sst/Chrna2/mGluR1 marker triad above
    detection (3 of 3 markers CONSISTENT) with the highest CA1
    stratum-oriens enrichment of any candidate
    (region_fraction_100um: 0.818). closeMatch rather than
    exactMatch because cluster F1 < 0.75 and OLM cells also
    populate sibling Sst Gaba_3 clusters.
  reconciliation_note: >
    Paired with edge_olm_hippocampus_to_CS20230722_SUPT_0216
    (skos:broadMatch + 1:n) — this cluster is the best-supported
    child within the OLM supertype mapping; both encode the
    OLM-to-Sst-Gaba_3 correspondence together.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Cluster-level F1=0.65 with 23 of 45 OLM cells falling on
        sibling Sst Gaba_3 clusters (primarily CS20230722_CLUS_0772
        with 7 cells); CS20230722_CLUS_0768 is one face of a
        multi-cluster OLM substructure rather than the whole type.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Classical negative markers PV (3.12; atlas category
        MERFISH), CB (3.87), CR (2.30), NOS (0.76), VIP (0.31) read
        DISCORDANT on this cluster; treated as pseudobulk background.
  proposed_experiments:
    - Morphology-confirmed Chrna2-Cre patch-seq cohort (n >= 100)
      with cluster-level AT against CCN20230722; target F1 >= 0.80
      (AnnotationTransferEvidence).
    - Sex-stratified expression analysis on CS20230722_CLUS_0768 to
      populate the currently NOT_ASSESSED sex-ratio property
      comparison.
  unresolved_questions:
    - Is CS20230722_CLUS_0768 the OLM cluster as such, or one of
      several Sst Gaba_3 children that together constitute the OLM
      type at the current WMBv1 release?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0769 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] Within Sst Gaba_3 supertype but Chrna2=0.00 on
    CS20230722_CLUS_0769 (cohort_pct 0.000) — discordant with the
    OLM defining marker — and 0/45 pooled-OLM cells assigned by
    annotation transfer (at_run_20260408_winterer_olm_mmc_wmbv1);
    OLM signal lands on sibling CS20230722_CLUS_0768 instead.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.18
  rationale: >
    [tier:CUT] Sibling of CS20230722_CLUS_0768 within
    CS20230722_SUPT_0216 with full marker triad CONSISTENT but only
    7 of 45 pooled-OLM cells assigned (F1=0.27 in
    at_run_20260408_winterer_olm_mmc_wmbv1); secondary AT scatter
    within the OLM supertype rather than a primary cluster
    correspondence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Sibling of CS20230722_CLUS_0768 within
    CS20230722_SUPT_0216; only 1 of 45 pooled-OLM cells assigned
    (F1=0.04 in at_run_20260408_winterer_olm_mmc_wmbv1); AT scatter,
    not a lead cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0775 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Sibling Sst Gaba_3 child with 0 pooled-OLM cells and
    region_fraction_100um: 0.442 driven by prosubiculum
    (CS20230722_CLUS_0775 is not the lead OLM child within
    CS20230722_SUPT_0216).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] Sibling Sst Gaba_3 child with 0 pooled-OLM cells
    assigned by annotation transfer
    (at_run_20260408_winterer_olm_mmc_wmbv1); not the OLM-bearing
    child within CS20230722_SUPT_0216.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 is isocortex-resident
    (region_fraction_100um: 0.016) — wrong region for a CA1
    stratum-oriens OLM mapping despite full Sst/Chrna2/mGluR1 marker
    concordance at supertype mean.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0217 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_SUPT_0217 is isocortex-resident
    (region_fraction_100um: 0.015); marker concordance on Sst/Chrna2
    reflects within-Sst Gaba subclass-wide expression rather than
    OLM identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0241 (Sst Chodl Gaba_4) is
    Chrna2-negative (val=0.00; cohort_pct 0.000) and isocortex/white
    matter resident (region_fraction_100um: 0.021) — both refute the
    OLM mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_hippocampus_to_CS20230722_SUPT_0224 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  rationale: >
    [tier:CUT] CS20230722_SUPT_0224 is isocortex-resident
    (region_fraction_100um: 0.032) with only 0.500 child-coverage on
    Chrna2 — wrong region for a CA1 stratum-oriens mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0727 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0727 sits in the Lamp5 Lhx6 subclass
    (CGE-derived) rather than Sst (MGE-derived); 0/46 pooled-OLM
    cells assigned by annotation transfer
    (at_run_20260408_winterer_olm_mmc_wmbv1). Subclass mismatch
    refutes the OLM correspondence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0785 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Parent supertype Sst Gaba_6 is Chrna2-negative per
    ABC Atlas HPF/GABA/Chrna2 filter; 0/46 pooled-OLM cells
    assigned to CS20230722_CLUS_0785 by annotation transfer
    (at_run_20260408_winterer_olm_mmc_wmbv1). Chrna2 absence
    refutes the OLM mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0788 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Parent supertype Sst Gaba_6 is Chrna2-negative;
    0/46 pooled-OLM cells assigned to CS20230722_CLUS_0788 by
    annotation transfer (at_run_20260408_winterer_olm_mmc_wmbv1).
    Chrna2 absence refutes the OLM mapping.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0789 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Parent supertype Sst Gaba_6 is Chrna2-negative;
    0/46 pooled-OLM cells assigned to CS20230722_CLUS_0789 by
    annotation transfer (at_run_20260408_winterer_olm_mmc_wmbv1)
    and 28% of cluster cells sit in amygdala — refutes the OLM
    mapping.
```
<!-- verdict-block-end -->
