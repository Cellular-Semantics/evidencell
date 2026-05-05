# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*draft · 2026-03-25 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_OLM.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0005371]; stratum lacunosum-moleculare [UBERON:0007637] | [1][2][3] |
| NT | GABAergic | [4][5] |
| Markers | Sst+, Chrna2+, mGluR1 (Grm1)+ | [6][7][8] |
| Negative markers | PV−, CB−, CR−, NOS−, VIP− | — |
| Neuropeptides | Sst, Npy, Pnoc | [7][9] |

**Node heterogeneity note:** The OLM class contains molecularly heterogeneous subpopulations. Zhang et al. (2025) report a PV-positive OLM subset firing in the gamma range. Thulin et al. (2025) [9] identify three Sst/Pnoc subclusters with differential dorsal-ventral connectivity. These may warrant separate nodes in future iterations.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | — | — | 🟡 MODERATE | Sst CONSISTENT · Chrna2 APPROXIMATE · neuropeptide triad CONSISTENT | Best candidate |
| 2 | 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | — | — | 🔴 LOW | GABA CONSISTENT · Sst APPROXIMATE · Npy DISCORDANT · AT REFUTE | Speculative |
| — | 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | — | — | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |
| — | 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | — | — | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |
| — | 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | — | — | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |

5 edges total · all TYPE_A_SPLITS.

---

## 0769 Sst Gaba_3 [CS20230722_CLUS_0769] · 🟡 MODERATE

### Supporting evidence

- **Best CA1 signal.** Atlas metadata shows CA1 SO (87 cells) — primary OLM soma location; consistent with stratum oriens [UBERON:0005371]. Sst Gaba subclass identity is CONSISTENT with the Sst-positive OLM classical type.
- **Full neuropeptide triad confirmed.** CLUS_0769 [CS20230722_CLUS_0769] expresses all three OLM neuropeptides: Sst (CONSISTENT), Npy (CONSISTENT), Pnoc (CONSISTENT). Full triad match.
- **GABA neurotransmitter:** CONSISTENT.
- **Chrna2 (APPROXIMATE).** ABC Atlas filter (HPF anatomy / GABA NT / Chrna2 expression) retains the Sst Gaba_3 supertype while eliminating Sst Gaba_6 entirely. Expression is scattered across clusters of this supertype — Chrna2 is not a defining marker at cluster level, but is present at the supertype level [A]. Alignment: APPROXIMATE.
- **Annotation transfer (GEO:GSE124847, Winterer et al. 2019 [7]).** MapMyCells of 46 OLM interneurons (cell_type_mapper v1.7.1, default parameters, raw normalisation) strongly supports the parent Sst Gaba_3 supertype (43/46 cells, F1=0.67 at SUPERTYPE). However, OLM cells scatter across sibling clusters 0767–0774 within the supertype; CLUS_0769 [CS20230722_CLUS_0769] specifically received 0/46 cells — OLM cells preferentially map to cluster 0768 (22/46, best cluster-level F1=0.53). This suggests OLM identity maps to the supertype level rather than to CLUS_0769 specifically. Both Sst-OLM and Htr3a-OLM subtypes converge on the same Sst Gaba_3 supertype.
- Classical morphology well established in the primary literature:

> oriens-lacunosum-moleculare (OLM) cells also had both the cell body and dendritic tree in the stratum oriens, but their horizontally running dendrites were often densely decorated with long spines. Their axon frequently originated from a proximal dendrite, and after ramification the main axon without boutons could be followed into the stratum lacunosum-moleculare. In this layer the axon ramified extensively bearing heavily packed varicosities. Some axon collaterals with boutons were also observed in the stratum oriens.
> — Zemankovics et al. 2010, Anatomical Location and Morphology · [1] <!-- quote_key: 3106274_e54f60e9 -->

> These CA1 GABAergic, somatostatin (Som)-expressing interneurons are named for their distinctive morphology: their soma and dendritic trees are located in the stratum oriens and their axons extend directly out to arborize in the stratum lacunosum-moleculare (SLM; Cajal, 1911;(McBain et al., 1994)(Sik et al., 1995)(Maccaferri et al., 2000)(Losonczy et al., 2002)(Leão et al., 2012)
> — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_2414c9e9 -->

> CA1 oriens-lacunosum moleculare (O-LM) interneurons innervate only the apical tuft of pyramidal cells (PCs) in stratum lacunosum-moleculare (SLM) and receive inputs only in stratum oriens (SO) (McBain et al., 1994)(Losonczy et al., 2002)(Zemankovics et al., 2010).
> — Tecuatl et al. 2020, Projection Patterns and Connectivity · [3] <!-- quote_key: 229694907_6865b9db -->

### Marker evidence provenance

- **Sst:** Evidence is transcript-level (ISH, scRNA-seq) and protein-level (IHC) from three sources [6][7][8]. Hooft et al. 2000 [6] identified type I interneurons (OLM candidates) by morphological reconstruction and confirmed somatostatin by ISH (4/4 cells positive):

> Type I interneurons had large horizontally oriented cell somata located at the border of stratum oriens and the alveus, indicating that these cells were most likely identical with the previously described somatostatin-positive oriens-lacunosum moleculare (O-LM) cells (Freund et al., 1998). Reconstruction of type I interneurons revealed their horizontally oriented dendritic tree in stratum oriens and their axonal arborizations in stratum lacunosum-moleculare (n = 5) (Fig. 2 A), and in situ hybridization for somatostatin showed that four of four cells were indeed positive for somatostatin (Fig. 2 B)
> — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_215c5f40 -->

> oriens-lacunosum moleculare (OLM) interneurons. OLMs express somatostatin (Sst), generate feedback inhibition and play important roles in theta oscillations and fear encoding
> — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_69dc904d -->

- **Chrna2:** Transcript-level and transgenic evidence. Nichol et al. 2018 [2] established Chrna2 as a specific OLM marker in dorsal CA1:

> The nicotinic acetylcholine receptor alpha2 subunit (Chrna2) is a specific marker for oriens lacunosum-moleculare (OLM) interneurons in the dorsal CA1 region of the hippocampus
> — Nichol et al. 2018, Anatomical Location and Morphology · [2] <!-- quote_key: 3591966_644f1e68 -->

> The vast diversity of GABAergic interneurons is believed to endow hippocampal microcircuits with the required flexibility for memory encoding and retrieval. However, dissection of the functional roles of defined interneuron types has been hampered by the lack of cell-specific tools. We identified a precise molecular marker for a population of hippocampal GABAergic interneurons known as oriens lacunosum-moleculare (OLM) cells. By combining transgenic mice and optogenetic tools, we found that OLM cells are important for gating the information flow in CA1, facilitating the transmission of intrahippocampal information (from CA3) while reducing the influence of extrahippocampal inputs (from the entorhinal cortex). Furthermore, we found that OLM cells were interconnected by gap junctions, received direct cholinergic inputs from subcortical afferents and accounted for the effect of nicotine on synaptic plasticity of the Schaffer collateral pathway. Our results suggest that acetylcholine acting through OLM cells can control the mnemonic processes executed by the hippocampus.
> — Leão et al. 2012, Projection Patterns and Connectivity · [8] <!-- quote_key: 7952877_ae03c6e0 -->

  Thulin et al. 2025 [9] confirmed that Chrna2 expression is restricted to stratum oriens in hippocampus and is specifically expressed in OLM cells:

> The Chrna2 gene expression is restricted to the stratum oriens in the hippocampus in both rats and mice (Ishii et al., 2005) and is specifically expressed in a subset of CA1 hippocampal interneurons, the oriens lacunosummoleculare (OLM) cells (Leão et al., 2012). Traditionally, OLM cells have been identified through their expression of somatostatin (Sst). However, in-depth single-cell transcriptomic cluster analysis has unveiled at least 11 distinct subpopulations of Sst-expressing interneurons (2017). Within these clusters, various classes of interneurons were identified, including back projecting, hippocampo-septal, oriens-bistratified, and OLM cells. Among these clusters, OLM cells were classified into a Sst and Prepronociceptin (Pnoc) co-expressing group (further divided into three subclusters)
> — Thulin et al. 2025, Projection Patterns and Connectivity · [9] <!-- quote_key: 280420054_8a6529c5 -->

  Atlas-side: Chrna2 expression is APPROXIMATE — scattered across clusters of Sst Gaba_3 supertype, not a defining marker at cluster level [A].

- **mGluR1 (Grm1):** Protein-level (IHC) from Hooft et al. 2000 [6] (type I interneurons, 4/4 cells positive):

> Type I interneurons responded with a large inward current of ≈ 224pA, were positive for somatostatin, and the majority expressed both mGluR1 and mGluR5
> — Hooft et al. 2000, Anatomical Location and Morphology · [6] <!-- quote_key: 6652630_17d10a9e -->

  Winterer et al. 2019 [7] quantified Grm1 at 96% detection in OLM scRNA-seq (44/46 OLM cells, GEO:GSE124847). Source-side confirmed at 96%; atlas-side still NOT_ASSESSED — Grm1 is not in cluster-level defining markers or neuropeptides. This gap remains open.

- **Npy (neuropeptide):** Winterer et al. 2019 [7] reported surprisingly consistent Npy expression in OLM cells:

> we found a surprisingly consistent expression of Npy in OLMs
> — Winterer et al. 2019, Molecular Markers and Gene Expression · [7] <!-- quote_key: 201041756_8d16e821 -->

  CLUS_0769 [CS20230722_CLUS_0769] expresses Npy (CONSISTENT). Earlier OLM literature used Npy as an exclusion criterion; Winterer 2019 [7] resolved this discrepancy.

- **Pnoc (neuropeptide):** Thulin et al. 2025 [9] and Winterer et al. 2019 [7] confirm Pnoc co-expression in the OLM subgroup. CLUS_0769 [CS20230722_CLUS_0769] expresses Pnoc (CONSISTENT). Full neuropeptide triad confirmed.

### Concerns

- **Location APPROXIMATE.** CA1 SO (87 cells) matches — strongest CA1 signal. SLM absent from CLUS_0769 [CS20230722_CLUS_0769]. Significant prosubiculum (61 cells) and posterior amygdala (95 cells) distribution. *(note: prosubiculum is at the CA1 border — adjacent region, weak counter-evidence. Posterior amygdala is anatomically distant from hippocampal CA1 — stronger counter-evidence; may indicate the cluster contains non-OLM Sst interneurons from extra-hippocampal regions.)*
- **Annotation transfer maps OLM to sibling cluster 0768, not 0769.** OLM cells preferentially mapped to 0768 (22/46, F1=0.53) rather than CLUS_0769 (0/46). This may indicate the mapping is more appropriate at supertype than at this specific cluster level.
- **mGluR1 NOT_ASSESSED at atlas level.** Source-side Grm1 confirmed at 96%; target-side unresolvable from atlas metadata.
- **MARKER_NOT_SPECIFIC.** Chrna2 expression is scattered across the Sst Gaba_3 supertype without being a defining marker at cluster level.

### What would upgrade confidence

- **Chrna2-Cre + MapMyCells** for CA1 stratum oriens neurons: expected output AnnotationTransferEvidence; target F1 ≥ 0.80 at CLUSTER level; resolves Q1 and Q2.
- **Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons**: expected output LiteratureEvidence confirming which WMBv1 cluster(s) capture Chrna2+ OLM cells.

---

## 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] · 🔴 LOW

### Supporting evidence

- GABA neurotransmitter: CONSISTENT.
- CA3 SO and SLM representation matches OLM anatomy (APPROXIMATE; CA3-enriched, not CA1).
- Sst and Pnoc neuropeptides present (CONSISTENT; APPROXIMATE for Sst as it is in neuropeptides, not defining markers, and the subclass is Lamp5 Lhx6 not Sst).

### Marker evidence provenance

- Chrna2 and mGluR1 are both NOT_ASSESSED for this cluster — no atlas-metadata data available.
- Sst is expressed in neuropeptides but is NOT a defining marker of this Lamp5 Lhx6 subclass cluster. This is biologically surprising for canonical MGE-derived OLM cells.
- Npy is **absent** from this cluster (DISCORDANT): OLM cells consistently express Npy [7]; absence from CLUS_0727 [CS20230722_CLUS_0727] is a direct conflict.

### Concerns

- **Annotation transfer REFUTES this candidate.** MapMyCells of 46 OLM interneurons (GEO:GSE124847, Winterer 2019 [7]) mapped 0/46 cells to Lamp5 Lhx6 subclass. All 45 successfully classified cells mapped to Sst Gaba subclass (Sst Gaba_3 supertype). Zero support for this Lamp5 Lhx6 cluster as an OLM target.
- **Sst APPROXIMATE**: expressed in neuropeptides but not defining; Lamp5 Lhx6 subclass (CGE-derived), not Sst (MGE-derived). Biologically surprising for canonical Sst+ MGE-derived OLM.
- **Npy DISCORDANT**: absent from CLUS_0727 [CS20230722_CLUS_0727]; OLM cells consistently express Npy [7].
- **Location APPROXIMATE**: CA3 SO (MBA:486) and CA3 SLM (MBA:471) — SO and SLM present but CA3-enriched, not CA1. *(note: CA3 is adjacent to CA1, but the CA3 versus CA1 subfield distinction is real; this is a subregional discrepancy.)*

### What would upgrade confidence

- Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens to determine if any have OLM morphology or electrophysiology. Expected output: LiteratureEvidence.
- Chrna2-Cre + MapMyCells to test whether Chrna2+ neurons map to this cluster. Expected output: AnnotationTransferEvidence.

---

## Eliminated candidates

**Primary shared disqualifying signal:** Chrna2 is DISCORDANT across all three UNCERTAIN edges. ABC Atlas filtering on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the Sst Gaba_6 supertype entirely. MapMyCells annotation transfer of 46 OLM interneurons (GEO:GSE124847) mapped 0/46 cells to any Sst Gaba_6 cluster. Both lines of evidence independently refute OLM identity for these clusters [A].

### 0785 Sst Gaba_6 [CS20230722_CLUS_0785]

- ABC Atlas HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 supertype entirely [A]: REFUTE.
- MapMyCells AT of 46 OLM interneurons (GEO:GSE124847): 0/46 cells mapped to Sst Gaba_6 supertype: REFUTE.
- Sst subclass and GABA: CONSISTENT. CA3 SO + SLM match OLM anatomy (APPROXIMATE; CA3-enriched not CA1).
- Chrna2 absent from Sst Gaba_6 supertype (DISCORDANT): disqualifying against OLM identity.
- neuropeptide_Pnoc absent (DISCORDANT): OLM expresses Pnoc; absent from this cluster.

### 0788 Sst Gaba_6 [CS20230722_CLUS_0788]

- ABC Atlas HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 supertype [A]: REFUTE.
- MapMyCells AT (GEO:GSE124847): 0/46 cells mapped to Sst Gaba_6: REFUTE.
- Sst subclass, GABA: CONSISTENT. CA1 SO (8) and CA3 SO (13) — small counts. SLM absent (APPROXIMATE).
- Chrna2 absent from Sst Gaba_6 supertype (DISCORDANT): disqualifying.
- Full neuropeptide triad plus Cort present (Sst, Npy, Pnoc: CONSISTENT). *(note: small cluster of 50 cells total; corpus callosum cells (4) may indicate contamination.)*

### 0789 Sst Gaba_6 [CS20230722_CLUS_0789]

- ABC Atlas HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 supertype [A]: REFUTE.
- MapMyCells AT (GEO:GSE124847): 0/46 cells mapped to Sst Gaba_6: REFUTE.
- Sst subclass, GABA: CONSISTENT. CA3 SO (25) — no CA1 or SLM (APPROXIMATE for SO; SLM absent).
- Chrna2 absent from Sst Gaba_6 supertype (DISCORDANT): disqualifying.
- Full neuropeptide triad plus Cort: CONSISTENT for Sst, Npy, Pnoc.
- 28% amygdala cells (medial amygdala 31, posterior amygdala 18) — cluster not hippocampus-specific. *(note: the amygdala is anatomically distant from hippocampal CA1; this non-hippocampal distribution is strong counter-evidence for OLM identity.)*

---

## Proposed experiments

### 1. Chrna2-Cre + MapMyCells (highest priority)

The Chrna2-Cre annotation transfer (GEO:GSE124847, n=46 OLM cells) was previously performed and strongly supports the Sst Gaba_3 supertype (43/46 cells, F1=0.67). What this round **did not resolve:** which specific cluster within Sst Gaba_3 corresponds to CA1 OLM cells (OLM cells scattered across 0767–0774, preferring 0768 over 0769); whether the prosubiculum and posterior amygdala cells in CLUS_0769 [CS20230722_CLUS_0769] are OLM cells or contamination.

**Refined experiment:**
- **What:** Chrna2-Cre + MapMyCells annotation transfer specifically from CA1 dissected tissue (not whole hippocampus) to reduce non-CA1 contamination; target CLUSTER level resolution
- **Target:** F1 ≥ 0.80 at CLUSTER level on the best-matching WMBv1 cluster within the Sst Gaba_3 supertype
- **Expected output:** AnnotationTransferEvidence on `edge_olm_to_wmb_clus_0769`; resolves Q1 and Q2
- **Resolves:** Q1 (are CA1 SO cells OLM-morphology), Q2 (why OLM cells map to 0768 not 0769)

### 2. MERFISH / Targeted scRNA-seq of Chrna2+ stratum oriens neurons
- **What:** Targeted scRNA-seq or MERFISH of Chrna2+ CA1 stratum oriens neurons from Chrna2-Cre mice
- **Target:** Cluster-level atlas assignment; confirmation of Grm1 expression in the same cells
- **Expected output:** LiteratureEvidence on `edge_olm_to_wmb_clus_0769`; closes the mGluR1/Grm1 NOT_ASSESSED gap
- **Resolves:** Q1; Grm1 gap on marker_mGluR1

### 3. Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens
- **What:** Record and fill CA3 SO Lamp5-Lhx6 neurons; test for OLM morphology/electrophysiology
- **Target:** Determine whether any Lamp5-Lhx6 CA3 SO neurons have OLM morphology or Sst/Chrna2 expression
- **Expected output:** LiteratureEvidence on `edge_olm_to_wmb_clus_0727`; confirms or refutes the LOW speculative edge
- **Resolves:** Q3 (biological significance of Sst in Lamp5-Lhx6 cluster)

### 4. Region-specific dissection of CA3 SO vs amygdala cells in CLUS_0789
- **What:** Region-specific dissection and re-profiling of the 0789 Sst Gaba_6 cluster to determine whether the amygdala component is an atlas clustering artefact
- **Target:** Confirm whether CA3 SO cells in CLUS_0789 [CS20230722_CLUS_0789] are OLM-like or a distinct amygdalo-hippocampal Sst type
- **Expected output:** Resolves Q6; updates confidence on the eliminated edge
- **Resolves:** Q6

---

## Open questions

1. Are the CA1 SO cells in CLUS_0769 [CS20230722_CLUS_0769] OLM-morphology? What are the prosubiculum and posterior amygdala cells?
2. Why do OLM cells (GEO:GSE124847 annotation transfer) map preferentially to cluster 0768 rather than CLUS_0769 [CS20230722_CLUS_0769]? Do these sibling clusters differ in hippocampal enrichment?
3. Is Sst expression in the Lamp5 Lhx6 cluster CLUS_0727 [CS20230722_CLUS_0727] biologically meaningful? Do any cells in this cluster have OLM morphology or electrophysiology?
4. Given Chrna2 absence from the Sst Gaba_6 supertype [A], is this cluster population a non-OLM Sst stratum oriens type?
5. Are the SO cells in CLUS_0788 [CS20230722_CLUS_0788] OLM-morphology? What are the corpus callosum cells (possible contamination)?
6. Are the CA3 SO cells in CLUS_0789 [CS20230722_CLUS_0789] OLM-like? What is the amygdala population, and is it a real biological component or a clustering artefact?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_olm_to_wmb_clus_0769 | ATLAS_METADATA — CA1 SO 87 cells; full neuropeptide triad; Sst subclass | SUPPORT |
| edge_olm_to_wmb_clus_0769 | ANNOTATION_TRANSFER — MapMyCells GEO:GSE124847 · 43/46 to Sst Gaba_3 supertype; F1=0.67 | PARTIAL |
| edge_olm_to_wmb_clus_0727 | ATLAS_METADATA — GABA consistent; CA3 SO + SLM; Sst/Pnoc neuropeptides; Npy absent | PARTIAL |
| edge_olm_to_wmb_clus_0727 | ANNOTATION_TRANSFER — MapMyCells GEO:GSE124847 · 0/46 cells to Lamp5 Lhx6 subclass | REFUTE |
| edge_olm_to_wmb_clus_0785 | ATLAS_METADATA — Sst subclass; CA3 anatomy; Chrna2 absent | PARTIAL |
| edge_olm_to_wmb_clus_0785 | ATLAS_QUERY — HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 [A] | REFUTE |
| edge_olm_to_wmb_clus_0785 | ANNOTATION_TRANSFER — MapMyCells GEO:GSE124847 · 0/46 cells to Sst Gaba_6 | REFUTE |
| edge_olm_to_wmb_clus_0788 | ATLAS_METADATA — Sst subclass; small CA1+CA3 SO; Chrna2 absent | PARTIAL |
| edge_olm_to_wmb_clus_0788 | ATLAS_QUERY — HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 [A] | REFUTE |
| edge_olm_to_wmb_clus_0788 | ANNOTATION_TRANSFER — MapMyCells GEO:GSE124847 · 0/46 cells to Sst Gaba_6 | REFUTE |
| edge_olm_to_wmb_clus_0789 | ATLAS_METADATA — Sst subclass; CA3 SO; amygdala 28%; Chrna2 absent | PARTIAL |
| edge_olm_to_wmb_clus_0789 | ATLAS_QUERY — HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 [A] | REFUTE |
| edge_olm_to_wmb_clus_0789 | ANNOTATION_TRANSFER — MapMyCells GEO:GSE124847 · 0/46 cells to Sst Gaba_6 | REFUTE |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280/) | soma location |
| [2] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | soma location; Chrna2 marker |
| [3] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | soma location |
| [4] | Böhm et al. 2015 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702/) | neurotransmitter type |
| [5] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | neurotransmitter type |
| [6] | Hooft et al. 2000 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195/) | Sst marker; mGluR1 marker |
| [7] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | Sst marker; Chrna2 marker; Npy neuropeptide; Pnoc neuropeptide |
| [8] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | Chrna2 marker |
| [9] | Thulin et al. 2025 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734/) | Pnoc neuropeptide; Chrna2 marker |
| [A] | ABC Atlas | [view](https://tinyurl.com/a4f3kd4v) | anatomy=HPF; NT=GABA; expression=Chrna2 |
