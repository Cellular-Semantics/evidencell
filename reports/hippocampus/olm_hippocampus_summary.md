# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*2026-03-25 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_OLM.yaml`*

---

## Introduction

Oriens-Lacunosum Moleculare (O-LM) interneurons are a canonical class of
GABAergic, somatostatin-positive hippocampal interneurons whose somata and
horizontally oriented dendrites lie in stratum oriens of CA1, with axons
arborising in stratum lacunosum-moleculare where they innervate the apical
tufts of pyramidal cells [1][2][3][4]. OLM cells generate feedback inhibition,
participate in theta-rhythmic activity, and have been proposed as gatekeepers
of intrahippocampal versus entorhinal information flow [7][8]. Resolving the
WMBv1 transcriptomic correlate of this classical type is a non-trivial test
of the atlas because OLM cells are defined primarily by morphology and
Cre-driver targeting rather than by a unique transcript signature.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371]; hippocampus stratum lacunosum moleculare [UBERON:0007640] (axonal target) | [1][2][3] |
| NT type | GABAergic | [4][5] |
| Defining markers | Sst; Chrna2; mGluR1 (Grm1, 96% detection in OLM scRNA-seq GSE124847) | [6][7][8][2] |
| Negative markers | PV; CB; CR; NOS; VIP | — |
| Neuropeptides | Sst; Npy; Pnoc | [7][9] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / morphology:**
  > oriens-lacunosum-moleculare (OLM) cells also had both the cell body and dendritic tree in the stratum oriens, but their horizontally running dendrites were often densely decorated with long spines. Their axon frequently originated from a proximal dendrite, and after ramification the main axon without boutons could be followed into the stratum lacunosum-moleculare. In this layer the axon ramified extensively bearing heavily packed varicosities. Some axon collaterals with boutons were also observed in the stratum oriens.
  > — Zemankovics et al. 2010, Anatomical Location and Morphology · [1] <!-- quote_key: 3106274_e54f60e9 -->

  > These CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare (SLM; Cajal, 1911;(McBain et al., 1994)(Sik et al., 1995)(Maccaferri et al., 2000)(Losonczy et al., 2002)(Leão et al., 2012)
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_2414c9e9 -->

  > CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
  > — Tecuatl et al. 2020, Projection Patterns and Connectivity · [3] <!-- quote_key: 229694907_6865b9db -->

- **NT type / GABAergic identity:**
  > GABAergic inhibitory oriens lacunosum-moleculare (O-LM) cells in the hippocampal area CA1 of the rat
  > — Böhm et al. 2015, Anatomical Location and Morphology · [4] <!-- quote_key: 15101210_5604b9a4 -->

  > EGFP was found to be expressed in a subpopulation of somatostatin-containing GABAergic interneurons in the hippocampus and neocortex
  > — Oliva et al. 2000, Molecular Markers and Gene Expression · [5] <!-- quote_key: 13398453_9154fc23 -->

- **Sst marker:**
  > Type I interneurons had large horizontally oriented cell somata located at the border of stratum oriens and the alveus, indicating that these cells were most likely identical with the previously described somatostatin-positive oriens-lacunosum moleculare (O-LM) cells (Freund et al., 1998). Reconstruction of type I interneurons revealed their horizontally oriented dendritic tree in stratum oriens and their axonal arborizations in stratum lacunosum-moleculare (n = 5) (Fig. 2 A), and in situ hybridization for somatostatin showed that four of four cells were indeed positive for somatostatin (Fig. 2 B)
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_215c5f40 -->

  > oriens-lacunosum moleculare (OLM) interneurons. OLMs express somatostatin (Sst), generate feedback inhibition and play important roles in theta oscillations and fear encoding
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_69dc904d -->

- **Chrna2 marker:**
  > The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
  > — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_644f1e68 -->

  > The vast diversity of GABAergic interneurons is believed to endow hippocampal microcircuits with the required flexibility for memory encoding and retrieval. However, dissection of the functional roles of defined interneuron types has been hampered by the lack of cell-specific tools. We identified a precise molecular marker for a population of hippocampal GABAergic interneurons known as oriens lacunosum-moleculare (OLM) cells. By combining transgenic mice and optogenetic tools, we found that OLM cells are important for gating the information flow in CA1, facilitating the transmission of intrahippocampal information (from CA3) while reducing the influence of extrahippocampal inputs (from the entorhinal cortex). Furthermore, we found that OLM cells were interconnected by gap junctions, received direct cholinergic inputs from subcortical afferents and accounted for the effect of nicotine on synaptic plasticity of the Schaffer collateral pathway. Our results suggest that acetylcholine acting through OLM cells can control the mnemonic processes executed by the hippocampus.
  > — Leão et al. 2012, Projection Patterns and Connectivity · [8] <!-- quote_key: 7952877_ae03c6e0 -->

- **mGluR1 (Grm1) marker:**
  > Type I interneurons responded with a large inward current of ≈ 224pA, were positive for somatostatin, and the majority expressed both mGluR1 and mGluR5
  > — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_17d10a9e -->

- **Npy neuropeptide:**
  > we found a surprisingly consistent expression of Npy in OLMs
  > — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_8d16e821 -->

- **Pnoc neuropeptide / three subclusters:**
  > The Chrna2 gene expression is restricted to the stratum oriens in the hippocampus in both rats and mice (Ishii et al., 2005) and is specifically expressed in a subset of CA1 hippocampal interneurons, the oriens lacunosummoleculare (OLM) cells (Leão et al., 2012). Traditionally, OLM cells have been identified through their expression of somatostatin (Sst). However, in-depth single-cell transcriptomic cluster analysis has unveiled at least 11 distinct subpopulations of Sst-expressing interneurons (2017). Within these clusters, various classes of interneurons were identified, including back projecting, hippocampo-septal, oriens-bistratified, and OLM cells. Among these clusters, OLM cells were classified into a Sst and Prepronociceptin (Pnoc) co-expressing group (further divided into three subclusters)
  > — Thulin et al. 2025, Projection Patterns and Connectivity · [9] <!-- quote_key: 280420054_8a6529c5 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Five candidate WMBv1 clusters were assessed against the OLM classical
definition. The primary mapping is to **0769 Sst Gaba_3
[CS20230722_CLUS_0769]** at MODERATE confidence, with the broader signal
falling at the **0216 Sst Gaba_3 [CS20230722_SUPT_0216]** supertype level
(pooled F1=0.97). A speculative LOW-confidence link to **0727 Lamp5 Lhx6 Gaba_1
[CS20230722_CLUS_0727]** and three UNCERTAIN candidates in the **Sst Gaba_6**
supertype are eliminated by the ABC Atlas Chrna2 filter and by zero
annotation-transfer cells mapping to them.

![Filtered AT figure for Oriens-Lacunosum Moleculare (O-LM) interneuron](../../kb/annotation_transfer_runs/20260408_winterer_olm_mmc_wmbv1/figures/f1_for_olm_hippocampus.png)

*F1 across taxonomy levels for the Winterer 2019 OLM cells (Sst-OLM +
Htr3a-OLM pooled to a single `OLM` group; n=46), per `--emit-metrics`
sidecar `figures/f1_for_olm_hippocampus_metrics.json`. Nodes are
coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown
inline: Coverage = fraction of source-group cells landing on this
target; Purity = fraction of this target's cells coming from the source
group. With multiple source groups in the figure, Purity differentiates
them; with a single pooled source, Purity is 1.0 at every target and
only Coverage discriminates — that is the case here. Best target per
level: CLASS 07 CTX-MGE GABA F1=0.99 (Pur=1.00, Cov=0.98); SUBCLASS 053
Sst Gaba F1=0.99 (Pur=1.00, Cov=0.98); SUPERTYPE 0216 Sst Gaba_3 F1=0.97
(Pur=1.00, Cov=0.94); CLUSTER CS20230722_CLUS_0768 within Sst Gaba_3
F1=0.65 (Pur=1.00, Cov=0.48). Pooling is justified because the Sst-OLM
and Htr3a-OLM Cre-line subtypes show no distinguishing transcriptomic
signal: both map overwhelmingly to the same Sst Gaba_3 supertype and
scatter across the same sibling clusters. OLM identity is captured at
the supertype level; the cluster-level Coverage drop reflects scatter
across siblings 0767–0774, not a different cell population.*

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | n/a | 🟡 MODERATE | Sst CONSISTENT · Chrna2 APPROXIMATE · full neuropeptide triad | Best candidate |
| 2 | 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | (Lamp5 Lhx6) | n/a | 🔴 LOW | Sst APPROXIMATE · Npy DISCORDANT · subclass mismatch | Speculative |
| — | 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | Sst Gaba_6 | n/a | ⚪ UNCERTAIN | Chrna2 DISCORDANT · Pnoc DISCORDANT · 0/46 AT cells | Eliminated (Chrna2) |
| — | 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | Sst Gaba_6 | n/a | ⚪ UNCERTAIN | Chrna2 DISCORDANT · 0/46 AT cells | Eliminated (Chrna2) |
| — | 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | Sst Gaba_6 | n/a | ⚪ UNCERTAIN | Chrna2 DISCORDANT · amygdala-dominated · 0/46 AT cells | Eliminated (Chrna2) |

Total edges: 5; relationship: `skos:broadMatch`.

### Property alignment — primary candidate (0769 Sst Gaba_3)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | stratum oriens [UBERON:0005371]; SLM [UBERON:0007640] | not available | CA1 SO [MBA:399] (87 cells); prosubiculum (61); posterior amygdala (95) | APPROXIMATE |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Sst | defining marker | Sst Gaba subclass | Sst subclass | CONSISTENT |
| Chrna2 | defining marker | Chrna2 expressed (scattered) in Sst Gaba_3 supertype per ABC Atlas | Chrna2 scattered (not defining at cluster level) | APPROXIMATE |
| mGluR1 (Grm1) | confirmed 96% detection in OLM scRNA-seq (GSE124847) | not available | Grm1 mean_expression=8.29 | NOT_ASSESSED |
| Sst neuropeptide | Sst | not available | present | CONSISTENT |
| Npy neuropeptide | Npy | not available | present | CONSISTENT |
| Pnoc neuropeptide | Pnoc | not available | present | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| ABC Atlas / cluster metadata | Atlas metadata | PARTIAL | CA1 SO 87 cells; full Sst/Npy/Pnoc triad; no SLM | atlas-internal |
| Winterer 2019 OLM MapMyCells | Annotation transfer | PARTIAL | Pooled F1=0.99 at CLASS/SUBCLASS; F1=0.97 at SUPT_0216; cluster F1=0.65 at CLUS_0768; 0/46 cells to CLUS_0769 | atlas-internal |

*(Child-cluster breakdown: within CS20230722_SUPT_0216 the AT signal localises
to CS20230722_CLUS_0768 (pooled cluster F1=0.65), not to
CS20230722_CLUS_0769 (0/45 cells). The mapping is robust at supertype but the
specific sibling cluster is not strongly determined.)*

### Property alignment — secondary LOW candidate (0727 Lamp5 Lhx6 Gaba_1)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | stratum oriens [UBERON:0005371]; SLM [UBERON:0007640] | not available | CA3 SO [MBA:486]; CA3 SLM [MBA:471] | APPROXIMATE |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Sst | defining marker | not available | Sst in neuropeptides, not defining_markers; Lamp5 Lhx6 subclass | APPROXIMATE |
| Chrna2 | defining marker | not available | not present | NOT_ASSESSED |
| mGluR1 (Grm1) | confirmed 96% detection in OLM scRNA-seq (GSE124847) | not available | Grm1 mean_expression=5.85 | NOT_ASSESSED |
| Sst neuropeptide | Sst | not available | present | CONSISTENT |
| Npy neuropeptide | Npy | not available | absent | DISCORDANT |
| Pnoc neuropeptide | Pnoc | not available | present | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Cluster metadata (CA3 SO+SLM, Lamp5 Lhx6 subclass) | Atlas metadata | PARTIAL | SO+SLM anatomy match but Lamp5 Lhx6 (CGE) ≠ Sst (MGE) | atlas-internal |
| Winterer 2019 OLM MapMyCells | Annotation transfer | REFUTE | 0/46 cells to Lamp5 Lhx6 subclass | atlas-internal |

### 0769 Sst Gaba_3 [CS20230722_CLUS_0769] · 🟡 MODERATE

**Supporting evidence**

- **Strongest CA1 anatomical signal.** Cluster metadata records 87 cells in CA1 SO [MBA:399] — the primary OLM soma location — and a full Sst/Npy/Pnoc neuropeptide triad matching the literature classical profile [1][2][7][9].
- **Sst subclass consistent.** The cluster sits within the 053 Sst Gaba subclass and 0216 Sst Gaba_3 supertype, both consistent with the canonical Sst-defining identity of OLM cells [6][7].
- **Annotation transfer (Winterer 2019, GEO:GSE124847).** MapMyCells (cell_type_mapper v1.7.1, raw normalization) of the pooled OLM cohort (Sst-OLM + Htr3a-OLM combined, 46 cells) reaches pooled F1=0.99 at CLASS/SUBCLASS (053 Sst Gaba), pooled F1=0.97 at the 0216 Sst Gaba_3 supertype, and pooled F1=0.65 at the best child cluster CS20230722_CLUS_0768 (run_ref `at_run_20260408_winterer_olm_mmc_wmbv1`). The evidence-item narrative records: *"MapMyCells annotation transfer of the pooled OLM cohort (46 cells; Sst-OLM + Htr3a-OLM combined; GSE124847, Winterer 2019) strongly supports the parent Sst Gaba_3 supertype (43/45 classified cells; pooled F1=0.97) but OLM cells scatter across sibling clusters 0767–0774 within it. Cluster 0769 specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/45, best pooled cluster-level F1=0.65). This indicates OLM identity is captured at the Sst Gaba_3 supertype rather than at any single child cluster. The high pooled supertype F1 reflects the fact that, once Sst-OLM and Htr3a-OLM are scored as a single OLM-equivalence group, the inter-source mis-attribution penalty that depresses per-source F1 disappears."*
- **Direct expression of Grm1 / mGluR1.** Cluster-level precomputed mean_expression of Grm1 = 8.29 is moderate-to-high, consistent with mGluR1 being a defining OLM marker by electrophysiology + somatostatin ISH on the same cells [6] and by direct re-analysis of GSE124847 (44/46 OLM cells, 96%) [7]. *(note: this is interpretive — atlas defining_markers are selected by differential expression rules, not by absolute level)*

**Marker evidence provenance**

- **Sst** — established by protein-level ISH/IHC in morphologically reconstructed OLM cells [6] and by transcriptomic profiling in Cre-targeted OLM populations [7]. Both protein- and transcript-level evidence. Cluster Sst subclass placement is concordant.
- **Chrna2** — Cre-line marker with restricted stratum oriens expression [2][8], confirmed by scRNA-seq [7] and replicated in Thulin et al. 2025 [9]. Atlas-side: Chrna2 is not in the cluster-level defining_markers panel of CS20230722_CLUS_0769; ABC Atlas filtering retains the parent Sst Gaba_3 supertype (consistent with scattered low-level expression) but eliminates Sst Gaba_6.
- **mGluR1 (Grm1)** — established by morphological reconstruction + voltage-clamp + somatostatin ISH on the same cells [6], reinforced by source-side scRNA-seq detection (44/46 OLM cells in GSE124847). Atlas-side Grm1 mean_expression=8.29 supports presence at the cluster level but Grm1 is not on the cluster's defining_markers list — the marker is informative for OLM identity but does not discriminate among Sst Gaba_3 sibling clusters.

**Concerns**

- **AT signal localises to a sibling cluster.** Within CS20230722_SUPT_0216, OLM cells preferentially map to CS20230722_CLUS_0768 (22/45 classified cells, pooled cluster F1=0.65) rather than to CS20230722_CLUS_0769 (0/45 cells). The cluster-rank choice is anatomically motivated (CA1 SO presence in 0769) but is not supported by the transcriptomic AT signal. The mapping is best read as OLM ↔ CS20230722_SUPT_0216, with CLUS_0769 the most anatomically appropriate child.
- **Extra-hippocampal cells.** 61 cells in prosubiculum and 95 cells in posterior amygdala dilute the cluster's hippocampus specificity *(prosubiculum is adjacent to CA1 — weak counter-evidence; posterior amygdala is a distant region — stronger counter-evidence that the cluster aggregates more than one anatomical type)*.
- **SLM absent in cluster.** The cluster shows no stratum lacunosum-moleculare cells. *(note: this is expected — for an MGE-derived OLM whose soma is in SO and whose axons project to SLM, atlas registration of soma position should record SO, not SLM; `has_merfish_location=false` for this graph means atlas location semantics are not adjudicated here)*.
- **Chrna2 not a cluster-level defining marker.** Marker scattered across SUPT_0216 children per ABC Atlas; therefore not a positive discriminator among Sst Gaba_3 siblings.

**What would upgrade confidence**

- Targeted re-mapping of Chrna2-Cre-labelled CA1 SO neurons via MapMyCells (`AnnotationTransferEvidence`, target F1 ≥ 0.80 at CLUSTER level) would test whether the Chrna2+ subset within SUPT_0216 localises preferentially to 0769 vs 0768.
- Targeted MERFISH or scRNA-seq of Chrna2+ stratum oriens neurons (`AnnotationTransferEvidence` / `MarkerAnalysisEvidence`).
- Resolution of why OLM cells preferentially map to CLUS_0768 rather than CLUS_0769 within Sst Gaba_3 (hippocampal-enrichment comparison across child clusters).

### 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] · 🔴 LOW

**Supporting evidence**

- **CA3 SO + SLM anatomy.** The cluster's primary location signal — CA3 SO [MBA:486] and CA3 SLM [MBA:471] — matches the OLM SO/SLM motif, though in CA3 rather than CA1 *(adjacent subfield — weak counter-evidence; classical OLM is best characterised in CA1)*.
- **GABA NT consistent.**
- **Some neuropeptide overlap.** Sst and Pnoc are present (in the cluster's neuropeptide annotations, not in defining markers); Npy is absent.

**Marker evidence provenance**

- **Subclass mismatch.** The cluster is in the Lamp5 Lhx6 subclass (CGE-derived Lhx6+ Lamp5+ lineage), not the Sst subclass. Classical OLM cells are MGE-derived Sst interneurons [6][7][8] — the developmental origin is incompatible with canonical OLM identity *(note: developmental-lineage interpretation goes slightly beyond the facts file; the lineage assignment of Lamp5 Lhx6 is established in mouse cortical-interneuron literature not cited here)*.
- **Chrna2** — listed as "not present" on the cluster; Chrna2 is a defining OLM marker [2][8], so its absence is meaningful.
- **mGluR1 / Grm1** — atlas-side cluster mean_expression=5.85 is the lowest of the five candidates; consistent with Grm1 not being enriched in this Lamp5 Lhx6 type relative to Sst Gaba_3.

**Concerns**

- **Annotation transfer refutes.** The evidence-item narrative records: *"MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer 2019) mapped 0/46 cells to Lamp5 Lhx6 subclass. All 45 successfully classified cells mapped to Sst Gaba subclass (Sst Gaba_3 supertype). Zero support for this Lamp5 Lhx6 cluster as an OLM target."*
- **Npy DISCORDANT** — OLM expresses Npy [7]; this cluster does not.
- **Developmental-lineage mismatch.** CGE-derived (Lamp5 Lhx6) vs MGE-derived (Sst) — biologically surprising for canonical Sst+ OLM. Requires independent validation.
- **CA3 vs CA1** — adjacent subfield but classical OLM literature characterises CA1 cells [1][2][3][4].

**What would upgrade confidence**

- Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens with morphological recovery (`MarkerAnalysisEvidence` / `AnnotationTransferEvidence`) — would directly test whether any OLM-morphology cells fall into this cluster despite the subclass mismatch.
- Chrna2-Cre + MapMyCells to test whether any Chrna2+ neurons map here (target F1 — currently 0).

---

## Eliminated candidates

All three Sst Gaba_6 candidates share a primary disqualifying signal: filtering
the ABC Atlas on HPF anatomy + GABA + Chrna2 expression eliminates the entire
Sst Gaba_6 supertype, and MapMyCells (run_ref `at_run_20260408_winterer_olm_mmc_wmbv1`)
assigns 0/46 OLM cells to any Sst Gaba_6 cluster [A]. Chrna2 is a defining OLM
marker [2][8], so its absence at the supertype level is decisive.

### 0785 Sst Gaba_6 [CS20230722_CLUS_0785] · ⚪ UNCERTAIN

- Chrna2 DISCORDANT — eliminated by ABC Atlas filter (HPF/GABA/Chrna2) [A].
- Pnoc DISCORDANT — OLM expresses Pnoc [9]; this cluster does not.
- Annotation transfer REFUTE — 0/46 OLM cells map to Sst Gaba_6.
- CA3-enriched (CA3 SO [MBA:486] 39 cells; CA3 SLM [MBA:471] 11 cells) — classical OLM is best characterised in CA1 *(adjacent subfield — weak counter-evidence on its own)*.
- Atlas-side Grm1 mean_expression=10.30 is the highest of any candidate, but this does not rescue the Chrna2 elimination.

### 0788 Sst Gaba_6 [CS20230722_CLUS_0788] · ⚪ UNCERTAIN

- Chrna2 DISCORDANT — eliminated by ABC Atlas filter (HPF/GABA/Chrna2) [A].
- Annotation transfer REFUTE — 0/46 OLM cells map to Sst Gaba_6.
- 50 cells total; CA1 SO [MBA:399] (8) + CA3 SO [MBA:486] (13) + no SLM; small numbers; corpus callosum cells (4) likely contamination.
- Full Sst/Npy/Pnoc triad plus Cort at the cluster level — but neuropeptide presence is not sufficient given the Chrna2 elimination.
- Atlas-side Grm1 mean_expression=9.08.

### 0789 Sst Gaba_6 [CS20230722_CLUS_0789] · ⚪ UNCERTAIN

- Chrna2 DISCORDANT — eliminated by ABC Atlas filter (HPF/GABA/Chrna2) [A].
- Annotation transfer REFUTE — 0/46 OLM cells map to Sst Gaba_6.
- Amygdala-dominated (medial amygdala 31; posterior amygdala 18; CA3 SO [MBA:486] 25; no CA1; no SLM) *(amygdala is a distant region — stronger counter-evidence that this cluster aggregates a primarily non-hippocampal Sst type)*.
- Atlas-side Grm1 mean_expression=8.00.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Oriens-Lacunosum Moleculare (O-LM) classical
type (`definition_basis: CLASSICAL_MULTIMODAL`) is defined here by: GABAergic
NT identity [4][5]; defining markers Sst [6][7], Chrna2 [2][8][7], and mGluR1
(Grm1) [6][7]; neuropeptide expression of Sst, Npy, and Pnoc [7][9]; and soma
location in hippocampus stratum oriens [UBERON:0005371] with axonal
arborisation in stratum lacunosum-moleculare [UBERON:0007640] [1][2][3].
Negative markers: PV, CB, CR, NOS, VIP.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers, sex bias when
applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE124847 (Sst-OLM, Htr3a-OLM; per-cell labels in source_cell_labels.json) |
| Source species | NCBITaxon:10090 (Mus musculus) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization). Bootstrap-iteration assignment with default thresholds; per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 46 (filtered to 45) |
| Run record | [`kb/annotation_transfer_runs/20260408_winterer_olm_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/20260408_winterer_olm_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md ((external; precomputed)) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix.csv`](../../kb/annotation_transfer_runs/20260408_winterer_olm_mmc_wmbv1/f1_matrix.csv) |
| Caveats | Source dataset has only 46 OLM cells (Winterer 2019); 45 retained after bootstrap filtering. The "Sst-OLM" and "Htr3a-OLM" source labels reflect Cre-driver subgroups in the Winterer dataset and are scored separately. At cluster (rank 0) resolution per-source F1 is low across all candidates (max 0.26 for Sst-OLM → CLUS_0768 within Sst Gaba_3 supertype) — the OLM cell type is captured at supertype/subclass level (pooled Sst Gaba_3 / Sst Gaba; pooled F1=0.97 / 0.99) but scatters across sibling clusters at the cluster level (pooled CLUS_0768 F1=0.65). This is a real biological signal, not a methodological failure: OLM is a transcriptomic subtype not yet resolved at WMBv1 cluster rank. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature
quotes in this report are validated against the evidencell knowledge base
at write time. Authored-prose evidence narratives are validated against
their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `1914ced` at 2026-05-14T08:28:21+00:00 from [kb/graphs/hippocampus/hippocampus_OLM.yaml](kb/graphs/hippocampus/hippocampus_OLM.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_olm_to_wmb_clus_0769 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_olm_to_wmb_clus_0727 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; REFUTE | atlas-internal |
| edge_olm_to_wmb_clus_0785 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL; REFUTE; REFUTE | atlas-internal; [A] |
| edge_olm_to_wmb_clus_0788 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL; REFUTE; REFUTE | atlas-internal; [A] |
| edge_olm_to_wmb_clus_0789 | ATLAS_METADATA; ATLAS_QUERY; ANNOTATION_TRANSFER | PARTIAL; REFUTE; REFUTE | atlas-internal; [A] |

</details>

---

## Discussion

**Primary mapping:** Oriens-Lacunosum Moleculare (O-LM) interneuron → 0769 Sst
Gaba_3 [CS20230722_CLUS_0769] at MODERATE confidence. Key support: atlas
metadata (CA1 SO presence, full Sst/Npy/Pnoc triad, Sst subclass) plus
MapMyCells annotation transfer to the parent supertype 0216 Sst Gaba_3
[CS20230722_SUPT_0216] (pooled F1=0.97, with pooled CLASS/SUBCLASS F1=0.99).
Key caveats: the AT signal localises to a
sibling cluster (CS20230722_CLUS_0768, pooled F1=0.65) rather than to 0769
(DISTRIBUTED_ACROSS_CLUSTERS), and the cluster-level value of mGluR1 (Grm1)
is recorded as a precomputed mean_expression (8.29) rather than as a defining
marker (MARKER_NOT_SPECIFIC). The mapping is best read as OLM ↔ Sst Gaba_3
supertype, with 0769 the most anatomically appropriate child cluster.

No Cell Ontology term currently assigned. This classical type is a candidate
for CL contribution.

### Proposed experiments and follow-ups

A round of MapMyCells annotation transfer from Winterer 2019 OLM cells
(GEO:GSE124847) into WMBv1 was already executed (run_ref
`at_run_20260408_winterer_olm_mmc_wmbv1`); pooling Sst-OLM + Htr3a-OLM into
a single OLM-equivalence group it established strong supertype-level mapping
(pooled F1=0.97 at CS20230722_SUPT_0216, pooled F1=0.99 at CLASS/SUBCLASS)
but did not resolve OLM identity to a single cluster (pooled CLUS_0768
F1=0.65). Remaining experiments:

- **Chrna2-Cre + MapMyCells from Chrna2-Cre-labelled CA1 SO neurons.**
  - **What:** scRNA-seq of Chrna2-Cre-targeted CA1 stratum oriens neurons followed by MapMyCells against WMBv1.
  - **Target:** F1 ≥ 0.80 at CLUSTER level.
  - **Expected output:** `AnnotationTransferEvidence` distinguishing CLUS_0768 vs CLUS_0769 and excluding Lamp5 Lhx6 / Sst Gaba_6 candidates.
  - **Resolves:** edge_olm_to_wmb_clus_0769 sibling-cluster ambiguity; edge_olm_to_wmb_clus_0727 subclass-mismatch hypothesis; open questions 2, 3.
- **Targeted MERFISH or scRNA-seq of Chrna2+ stratum oriens neurons.**
  - **What:** MERFISH panel with Chrna2 + Sst + Pnoc + Npy + Grm1 in CA1 SO.
  - **Target:** quantify co-expression and assign cells to WMBv1 clusters via spatial proximity to atlas reference.
  - **Expected output:** `MarkerAnalysisEvidence` / `AnnotationTransferEvidence`.
  - **Resolves:** open question 1 (whether CA1 SO cells in CLUS_0769 are OLM-morphology) and the prosubiculum / posterior-amygdala dilution caveat.
- **Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens.**
  - **What:** Patch-clamp + morphology + scRNA-seq of CA3 SO Lamp5/Lhx6+ neurons.
  - **Target:** establish whether any OLM-morphology cells fall into CLUS_0727 despite the CGE-derived subclass.
  - **Expected output:** `MarkerAnalysisEvidence` / morphology evidence.
  - **Resolves:** edge_olm_to_wmb_clus_0727 LOW-confidence speculative status.
- **Region-specific dissection of CA3 SO vs amygdala cells in CLUS_0789.**
  - **What:** spatial / regional sorting before scRNA-seq.
  - **Resolves:** open question 4 (identity of the amygdala population in CLUS_0789), which tidies the Sst Gaba_6 supertype interpretation but does not change the OLM mapping (already eliminated by Chrna2).

### Open questions

1. Are the 87 CA1 SO cells in CS20230722_CLUS_0769 OLM-morphology, and what is the identity of the 95 posterior-amygdala cells in the same cluster?
2. Why do OLM cells map preferentially to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within the Sst Gaba_3 supertype? Do these sibling clusters differ in hippocampal enrichment?
3. Does any OLM-morphology cell fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 (CGE) vs Sst (MGE) developmental-lineage mismatch?
4. Given Chrna2 absence at the Sst Gaba_6 supertype, is CS20230722_CLUS_0785 a non-OLM Sst stratum oriens type? What is the identity of the amygdala-dominated population in CS20230722_CLUS_0789?
5. Are the CA1 SO and CA3 SO cells in CS20230722_CLUS_0788 OLM-morphology, and what are the corpus callosum cells in the same cluster?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [PMID:20421280](https://pubmed.ncbi.nlm.nih.gov/20421280) | soma location |
| [2] | Nichol et al. 2018 | [PMID:29487503](https://pubmed.ncbi.nlm.nih.gov/29487503) | soma location |
| [3] | Tecuatl et al. 2020 | [PMID:33361464](https://pubmed.ncbi.nlm.nih.gov/33361464) | soma location |
| [4] | Böhm et al. 2015 | [PMID:26021702](https://pubmed.ncbi.nlm.nih.gov/26021702) | neurotransmitter type |
| [5] | Oliva et al. 2000 | [PMID:10777798](https://pubmed.ncbi.nlm.nih.gov/10777798) | neurotransmitter type |
| [6] | Hooft et al. 2000 | [PMID:10804195](https://pubmed.ncbi.nlm.nih.gov/10804195) | Sst marker |
| [7] | Winterer et al. 2019 | [PMID:31420995](https://pubmed.ncbi.nlm.nih.gov/31420995) | Sst marker |
| [8] | Leão et al. 2012 | [PMID:23042082](https://pubmed.ncbi.nlm.nih.gov/23042082) | Chrna2 marker |
| [9] | Thulin et al. 2025 | [PMID:40757734](https://pubmed.ncbi.nlm.nih.gov/40757734) | Pnoc neuropeptide |
| [A] | ABC Atlas | [view](https://tinyurl.com/a4f3kd4v) | anatomy=HPF; NT=GABA; expression=Chrna2 |

---

<!-- verdict-block-start: edge_olm_to_wmb_clus_0769 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.6
  rationale: >
    Primary mapping to CS20230722_CLUS_0769 within CS20230722_SUPT_0216 (Sst Gaba_3)
    is anchored by atlas metadata (CA1 SO presence, full Sst/Npy/Pnoc neuropeptide
    triad, Sst subclass) and by MapMyCells annotation transfer of Winterer 2019 OLM
    cells (run_ref at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq with MERFISH
    spatial registration on the target side) reaching pooled F1=0.99 at
    CLASS/SUBCLASS, pooled F1=0.97 at the SUPERTYPE level (CS20230722_SUPT_0216),
    and pooled F1=0.65 at the best child cluster CS20230722_CLUS_0768; cluster
    Grm1 mean_expression=8.29 is qualitatively concordant with mGluR1 being a
    defining OLM marker by electrophysiology and scRNA-seq. 4 of 6 markers
    CONSISTENT (Sst, Sst-NP, Npy-NP, Pnoc-NP) with Chrna2 APPROXIMATE and
    mGluR1 NOT_ASSESSED at the atlas defining-markers panel.
  unresolved_questions:
    - "Why do OLM cells map preferentially to CS20230722_CLUS_0768 rather than CS20230722_CLUS_0769 within CS20230722_SUPT_0216?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0727 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    CS20230722_CLUS_0727 (Lamp5 Lhx6 Gaba_1) is refuted as an OLM target by
    MapMyCells annotation transfer (run_ref at_run_20260408_winterer_olm_mmc_wmbv1,
    scRNA-seq): 0/46 OLM cells map to the Lamp5 Lhx6 subclass and all 45 classified
    cells map instead to CS20230722_SUPT_0216 (Sst Gaba_3). Npy is DISCORDANT,
    Sst is APPROXIMATE only (in neuropeptide annotations, not defining_markers),
    cluster Grm1 mean_expression=5.85 is the lowest among candidates, and Chrna2
    is absent. 2 of 6 markers CONSISTENT (Sst-NP, Pnoc-NP) against a Lamp5 Lhx6
    (CGE-derived) vs Sst (MGE-derived) subclass and developmental-lineage
    mismatch; CA3 SO + SLM anatomy (morphology-relevant) is suggestive but not
    sufficient.
  unresolved_questions:
    - "Do any OLM-morphology cells fall into CS20230722_CLUS_0727 despite the Lamp5 Lhx6 (CGE) vs Sst (MGE) lineage mismatch?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0785 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_CLUS_0785 (Sst Gaba_6) is refuted by two independent signals:
    (1) ABC Atlas filter (HPF + GABA + Chrna2 expression, scRNA-seq) eliminates
    the entire Sst Gaba_6 supertype, and (2) MapMyCells annotation transfer
    (run_ref at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq) maps 0/46 OLM
    cells to Sst Gaba_6, with all 45 classified cells going to
    CS20230722_SUPT_0216 instead. Chrna2 DISCORDANT and Pnoc DISCORDANT; 3 of 6
    markers CONSISTENT (Sst, Sst-NP, Npy-NP) but the Chrna2 elimination is
    decisive. CA3-enriched anatomy further weakens the candidate. Cluster Grm1
    mean_expression=10.30 does not rescue the Chrna2 elimination.
  unresolved_questions:
    - "Given Chrna2 absence at Sst Gaba_6, is CS20230722_CLUS_0785 a non-OLM Sst stratum oriens type?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0788 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_CLUS_0788 (Sst Gaba_6) is refuted by ABC Atlas filter
    (HPF + GABA + Chrna2 expression, scRNA-seq) eliminating the Sst Gaba_6
    supertype and by MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq; 0/46 OLM cells to
    Sst Gaba_6). Chrna2 DISCORDANT; 4 of 6 markers CONSISTENT (Sst, Sst-NP,
    Npy-NP, Pnoc-NP) but the Chrna2 elimination is
    decisive. Cluster is small (50 cells total) with CA1 SO (8) plus CA3 SO (13)
    and no SLM; cluster Grm1 mean_expression=9.08 does not rescue the Chrna2
    elimination.
  unresolved_questions:
    - "Are the CA1 SO and CA3 SO cells in CS20230722_CLUS_0788 OLM-morphology, and what are the corpus callosum cells in the same cluster?"
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_olm_to_wmb_clus_0789 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    CS20230722_CLUS_0789 (Sst Gaba_6) is refuted by ABC Atlas filter
    (HPF + GABA + Chrna2 expression, scRNA-seq) eliminating the Sst Gaba_6
    supertype and by MapMyCells annotation transfer (run_ref
    at_run_20260408_winterer_olm_mmc_wmbv1, scRNA-seq; 0/46 OLM cells to
    Sst Gaba_6). Chrna2 DISCORDANT; cluster is amygdala-dominated (28% amygdala
    cells; CA3 SO 25; no CA1; no SLM). 4 of 6 markers CONSISTENT (Sst, Sst-NP,
    Npy-NP, Pnoc-NP) but Chrna2 elimination plus extra-hippocampal
    (morphology/region) location are decisive. Cluster Grm1 mean_expression=8.00
    does not rescue.
  unresolved_questions:
    - "What is the identity of the amygdala population dominating CS20230722_CLUS_0789?"
```
<!-- verdict-block-end -->
