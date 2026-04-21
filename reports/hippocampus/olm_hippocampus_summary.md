# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*draft · 2026-03-25 · Source: `kb/draft/hippocampus/hippocampus_OLM.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Location note

> **Location note.** WMBv1 location data derives from MERFISH spatial
> registration and records **soma position** only. Axonal and dendritic
> projection targets are not reflected in atlas cluster location fields and
> are not used in mapping assessments.

The O-LM interneuron is defined in part by its axonal projection target: the soma and dendrites reside in stratum oriens [UBERON:0014548], but the axon travels vertically through strata pyramidale and radiatum to arborize exclusively in stratum lacunosum-moleculare [UBERON:0007637], where it innervates the apical tufts of pyramidal cells. Because WMBv1 MERFISH location records soma position only, the hallmark SLM axonal arborization is invisible to the atlas. Absence of SLM soma signal in an atlas cluster is therefore expected for OLM cells and must not be treated as a contra-indicator. The MERFISH location data captures only the somatic half of the OLM morphological definition and cannot discriminate axonal projection targets across strata.

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | stratum oriens of hippocampus [UBERON:0014548] (CA1); axon projects to stratum lacunosum-moleculare of hippocampus [UBERON:0007637] | [1], [2], [3] |
| Neurotransmitter | GABAergic | [4], [5] |
| Defining markers | Sst, Chrna2, mGluR1/Grm1. Direct detection rates from re-analysis of GSE124847 raw counts (46 OLM cells, Winterer 2019 [7]): Grm1 96% (44/46 cells); Chrna2 detected in a substantial fraction (specific cluster-level rate not available); Sst 100% (46/46 cells). | Sst: [6], [7]; Chrna2: [2], [8], [7]; mGluR1: [6], [7] |
| Negative markers | PV, CB (Calb1), CR (Calb2), NOS, VIP | — |
| Neuropeptides | Sst, Npy, Pnoc | Sst: [7]; Npy: [7]; Pnoc: [9], [7] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | Sst Gaba_3 | 243 | 🟡 MODERATE | Neuropeptide triad CONSISTENT · Chrna2 APPROXIMATE | Best candidate |
| 2 | 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | Lamp5 Lhx6 | 98 | 🔴 LOW | Sst APPROXIMATE · Npy DISCORDANT | Speculative |
| — | 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | Sst Gaba_6 | 186 | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |
| — | 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | Sst Gaba_6 | 50 | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |
| — | 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | Sst Gaba_6 | 177 | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |

Total: 5 edges. Relationship type: TYPE_A_SPLITS (classical OLM maps across multiple WMBv1 clusters; no single cluster captures the full classical type).

---

## 0769 Sst Gaba_3 [CS20230722_CLUS_0769] · 🟡 MODERATE

### Supporting evidence

- **GABA neurotransmitter type consistent.** The cluster belongs to the Sst Gaba subclass, fully consistent with the GABAergic identity of O-LM cells [4], [5].
- **Sst subclass consistent.** The cluster is defined at subclass level by Sst expression, directly matching the canonical OLM marker [6], [7].
- **Full neuropeptide triad matched.** Cluster 0769 carries all three OLM neuropeptides — Sst, Npy, and Pnoc — the complete triad expected for OLM cells [7], [9]. No other evaluated cluster achieves this combination without missing at least one peptide.
- **Best CA1 stratum oriens signal.** Atlas metadata shows 87 cells in CA1 SO, the primary soma location of O-LM cells [1], [2], [3]. This is the strongest CA1 SO count among all evaluated clusters.
- **Chrna2 expression retained at supertype level.** ABC Atlas filtering on HPF anatomy, GABAergic NT, and Chrna2 expression retains the Sst Gaba_3 supertype while eliminating Sst Gaba_6 entirely [A]. Chrna2 expression is scattered across clusters of this supertype and is not a defining marker at cluster level, but its presence at the supertype level is consistent with an OLM marker profile.
- **Annotation transfer strongly supports parent Sst Gaba_3 supertype.** MapMyCells annotation transfer of 46 OLM interneurons (GEO:GSE124847, Winterer et al. 2019 [7]; cell_type_mapper v1.7.1, raw normalization; WMBv1 CCN20230722) mapped 43/46 cells (group purity = 0.96) to the Sst Gaba_3 supertype (F1 = 0.67 at supertype level; median bootstrap = 1.0). At broader levels the mapping is robust: 45/46 cells map to Sst Gaba subclass (F1 = 0.68) and to class 07 CTX-MGE GABA (F1 = 0.68). The Sst Gaba_3 supertype, which contains cluster 0769, is the dominant transcriptomic attractor for OLM cells in this atlas.

### Marker evidence provenance

- **Sst (defining marker):** Evidence is both protein-level (ISH in morphologically reconstructed cells, [6]) and transcript-level (scRNA-seq, [7]). Hooft et al. 2000 [6] confirmed Sst by in situ hybridisation in cells whose axon was reconstructed into stratum lacunosum-moleculare — cell-type specificity is high. Winterer et al. 2019 [7] confirm 100% Sst detection in 46 OLM cells from GSE124847 (re-analysis of raw counts). Sst is CONSISTENT at subclass level for cluster 0769. No provenance concerns.
- **Chrna2 (defining marker):** Evidence is transcript-level / lineage-based (Chrna2-Cre transgenic mice used to target OLM cells, validated by electrophysiology and morphology, [8]; reviewed in [2]). Leão et al. 2012 [8] identified Chrna2 as a specific OLM marker using optogenetics and patch-clamp on Chrna2-Cre-targeted cells — cell-type specificity is high. In atlas metadata, Chrna2 expression is described as scattered across clusters of the Sst Gaba_3 supertype, not as a defining marker at cluster 0769 specifically. The ABC Atlas filter [A] retains Sst Gaba_3 overall but the per-cluster Chrna2 status for 0769 is unresolved (APPROXIMATE alignment). Source-side Chrna2 detection in OLM cells is well-supported; target-side is only APPROXIMATE. A query of per-cluster Chrna2 expression in the ABC Atlas would resolve whether 0769 or its sibling clusters (e.g. 0768) show higher Chrna2 enrichment.
- **mGluR1 / Grm1 (defining marker):** Evidence is protein-level (immunostaining paired with electrophysiology and ISH in reconstructed cells, [6]) and transcript-level (scRNA-seq re-analysis, [7]). Hooft et al. 2000 [6] confirmed mGluR1 and mGluR5 protein expression in cells with recorded OLM electrophysiology and morphological reconstruction — cell-type specificity is high. Source-side: Grm1 detected in 44/46 OLM cells (96%) by raw-count re-analysis of GSE124847. **Target-side: Grm1 is not resolvable from atlas metadata for cluster 0769** — it does not appear in the cluster's defining_markers or neuropeptides fields. Source-side confirmed at 96%; target-side still unresolvable from atlas metadata. This is a substantive gap.
- **Negative markers (PV, CB/Calb1, CR/Calb2, NOS, VIP):** All five are listed on the classical node without a primary citation in the reference index. Exclusion of PV and Calb1 is classically used to distinguish OLM from basket and bistratified cells; exclusion of VIP and CR from interneurons in stratum oriens is a common working assumption. However, no specific citation testing morphology-confirmed OLM cells for these markers appears in the reference index. This is a provenance gap. A targeted cite-traverse for "calbindin OLM hippocampus", "parvalbumin OLM hippocampus", and "VIP OLM hippocampus" is recommended to supply primary citations.
- **Npy (neuropeptide):** Transcript-level evidence from scRNA-seq [7]. Winterer et al. 2019 [7] report "a surprisingly consistent expression of Npy in OLMs." Cell-type specificity is good — the dataset uses Sst-Cre-selected OLM cells confirmed by morphology. Npy is CONSISTENT at atlas level for cluster 0769.
- **Pnoc (neuropeptide):** Transcript-level evidence from scRNA-seq [9]. Thulin et al. 2025 [9] identify three Sst/Pnoc subclusters within OLM cells with differential dorsal–ventral connectivity. Pnoc co-expression with Sst is used to define the OLM group in single-cell transcriptomic analysis — cell-type specificity is good. Pnoc is CONSISTENT at atlas level for cluster 0769.

### Concerns

- **Location APPROXIMATE — extra-hippocampal spread.** CA1 SO is well represented (87 cells), but the cluster also contains 61 cells in prosubiculum and 95 cells in posterior amygdala. The prosubiculum is immediately adjacent to CA1 in the hippocampal formation *(adjacent region — could reflect registration boundary error; weak counter-evidence)*. The posterior amygdala is anatomically distant from CA1 stratum oriens *(distant region — stronger counter-evidence; classical OLM cells may still be a subtype of the Sst Gaba_3 T-type, but not the CA1 stratum oriens population specifically)*. The cluster likely aggregates Sst interneurons from multiple hippocampal-adjacent structures rather than being OLM-specific.
- **Annotation transfer resolves to supertype, not cluster 0769 specifically.** Although Sst Gaba_3 supertype receives strong OLM signal, cluster 0769 received 0/46 cells from the annotation transfer. OLM cells preferentially mapped to sibling cluster 0768 Sst Gaba_3 (15/46 cells after bootstrap filtering; best cluster-level F1 = 0.47 for cluster 0768 [CS20230722_CLUS_0768]). The mapping is currently most appropriate at supertype rather than cluster level.
- **Chrna2 APPROXIMATE at cluster level.** Chrna2 expression is present across the Sst Gaba_3 supertype but is not confirmed as a defining marker at cluster 0769 specifically.
- **mGluR1 (Grm1) NOT_ASSESSED at atlas level.** Despite source-side 96% detection, Grm1 cannot be cross-checked against cluster-level atlas metadata.

### What would upgrade confidence

- **Chrna2-Cre MapMyCells at cluster resolution (AnnotationTransferEvidence).** Mapping with a Chrna2-Cre-enriched CA1 stratum oriens dataset would test whether Chrna2-selected OLM cells converge on cluster 0769 vs 0768. What has already been done: GSE124847 annotation transfer resolved to Sst Gaba_3 supertype (F1 = 0.67) but placed 0/46 cells at cluster 0769. The existing dataset is not Chrna2-enriched and mixes Sst-OLM and Htr3a-OLM subtypes. Refined target: F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3. Expected output: `AnnotationTransferEvidence` distinguishing whether the edge should point to 0769 or 0768. Resolves open question 2.
- **Grm1 cluster-level expression query (ATLAS_QUERY).** Querying the ABC Atlas or Allen Cell Types Database for Grm1 expression per cluster within Sst Gaba_3 would convert the NOT_ASSESSED alignment to CONSISTENT or DISCORDANT. Expected output: `ATLAS_QUERY` evidence item. Given the 96% source-side detection, this is a high-priority cross-check.
- **Targeted transcriptomics of Chrna2+ stratum oriens neurons (LiteratureEvidence or AnnotationTransferEvidence).** MERFISH or scRNA-seq with Chrna2 spatial annotation in CA1 SO. Resolves open question 1 and the Grm1 NOT_ASSESSED gap.
- **Primary citations for OLM negative markers (LiteratureEvidence).** A cite-traverse on "calbindin OLM hippocampus", "parvalbumin OLM hippocampus", and "VIP OLM hippocampus" would supply citations for PV, Calb1, Calb2, NOS, and VIP negative markers on the classical node — currently all lack primary citations.

---

## 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] · 🔴 LOW

### Supporting evidence

- **GABA neurotransmitter type consistent.** GABAergic identity is shared with O-LM cells [4], [5].
- **Both SO and SLM layers represented.** Atlas metadata shows cells in CA3 SO (MBA:486) and CA3 SLM (MBA:471). Both layers of the OLM morphological circuit are present — consistent with a cell type whose soma sits in SO and whose axon zone is SLM. Note that WMBv1 MERFISH records soma position only; cells appearing in SLM in this atlas carry somata in SLM, which is atypical for canonical OLM (whose somata are in SO).
- **Sst and Pnoc neuropeptides present.** Two of three OLM neuropeptides (Sst, Pnoc) are detected, consistent with partial peptide overlap.

### Marker evidence provenance

- **Sst:** In cluster 0727, Sst appears in neuropeptides but is NOT a defining marker — the subclass is Lamp5 Lhx6, not Sst. Sst expression is present at a level insufficient to define the subclass. The alignment is APPROXIMATE. For OLM, Sst is a defining marker confirmed by ISH in reconstructed cells [6]; a cluster where Sst is only a secondary neuropeptide feature is a substantially weaker match. *(note: it is biologically conceivable that some CA3 Lamp5 Lhx6 interneurons co-express Sst at transcript level without Sst being their primary defining marker.)*
- **Chrna2:** Not present in this cluster's atlas metadata (alignment NOT_ASSESSED rather than DISCORDANT — absent from metadata rather than confirmed absent at cell level). However, the ABC Atlas Chrna2 filter [A] retained Sst Gaba_3 while leaving Lamp5 Lhx6 unmentioned among surviving supertypes, implying Chrna2 is not characteristically expressed in this lineage. Source-side Chrna2 is well-established as OLM-specific [8], [2]; target-side absence (even if unconfirmed) is a concern.
- **Npy:** OLM cells consistently express Npy [7]; cluster 0727 has Npy absent (DISCORDANT). This is a marker-level mismatch independent of subclass identity.
- **mGluR1 / Grm1:** NOT_ASSESSED for this cluster. Source-side 96% detection in 46 OLM cells (GSE124847 re-analysis). Target-side unresolvable from atlas metadata. Same gap as for cluster 0769. Source-side confirmed at 96%; target-side still unresolvable from atlas metadata.
- **Negative markers:** Same provenance concern as for cluster 0769 — no primary citations in the reference index for PV, Calb1, Calb2, NOS, VIP as OLM negative markers.

### Concerns

- **Subclass mismatch — Lamp5 Lhx6, not Sst.** This is the primary biological concern. Canonical OLM cells are Sst-defined and MGE-derived [4], [5], [6]. Lamp5 Lhx6 subclass cells form a distinct lineage branch in the WMBv1 taxonomy. Sst appears in neuropeptides only, not as a defining marker — biologically surprising for a cluster proposed to capture canonical OLM identity. *(note: Lhx6 is characteristically expressed in MGE-derived cells, so Lamp5 Lhx6 cells do share the MGE origin, but their transcriptomic divergence from the Sst subclass is a meaningful concern.)*
- **Npy DISCORDANT.** Cluster 0727 lacks Npy; Winterer et al. 2019 [7] document consistent Npy expression in OLM cells. This disrupts the full neuropeptide triad that distinguishes OLM from related Sst SO interneuron types.
- **Location APPROXIMATE — CA3-enriched, not CA1.** SO and SLM are present but in CA3, not CA1. CA3 is adjacent to CA1 *(adjacent region — could reflect a CA3 OLM-like population or registration overlap; weak counter-evidence on location alone)*, but the absence of CA1 SO signal is notable for canonical OLM cells [2], [3].
- **Annotation transfer: zero cells mapped to Lamp5 Lhx6 subclass.** MapMyCells (GEO:GSE124847, 46 OLM cells) mapped 0/46 cells to the Lamp5 Lhx6 subclass; all 45 classified cells mapped to Sst Gaba subclass. This is strong direct counter-evidence against this cluster as an OLM target.
- **Chrna2 and mGluR1 not assessable from atlas metadata.** Both defining OLM markers cannot be evaluated from cluster-level fields.

### What would upgrade confidence

- **Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens (LiteratureEvidence).** Patch-seq targeting Lamp5-Cre or Lhx6-Cre neurons in CA3 SO would test directly whether any carry OLM morphology (axon in SLM), OLM electrophysiology (theta resonance, Ih sag), and OLM markers (Sst, Chrna2, Grm1). Target: morphological reconstruction in ≥5 cells. Without morphological confirmation, the Lamp5 Lhx6 subclass assignment argues strongly against OLM identity. Resolves open question 3.
- **Chrna2-Cre MapMyCells (AnnotationTransferEvidence).** Annotation transfer of Chrna2-Cre-selected CA1 SO neurons would determine whether any cells map to Lamp5 Lhx6, adding `AnnotationTransferEvidence` to this edge. The existing result (0/46 cells from a broader OLM dataset) already argues against this, but a Chrna2-enriched source dataset would be definitive. Resolves open question 3.
- **Targeted literature search.** A cite-traverse for "Lamp5 Lhx6 stratum oriens" or "CGE OLM interneuron hippocampus" would determine whether any published study has described OLM morphology in Lamp5 Lhx6 cells. This gap is addressable by literature review without new experiments and could either elevate or eliminate this edge.

---

## Eliminated candidates

All three remaining clusters — 0785 Sst Gaba_6 [CS20230722_CLUS_0785], 0788 Sst Gaba_6 [CS20230722_CLUS_0788], and 0789 Sst Gaba_6 [CS20230722_CLUS_0789] — share a single disqualifying signal: **Chrna2 DISCORDANT across all three**. ABC Atlas filtering on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the entire Sst Gaba_6 supertype [A]. All three clusters belong to this supertype. MapMyCells annotation transfer of 46 OLM cells (GEO:GSE124847, Winterer et al. [7]) independently mapped 0/46 cells to Sst Gaba_6 for each cluster; all 45 classified cells went to Sst Gaba_3 instead. Two independent lines of evidence — atlas Chrna2 expression filtering and annotation transfer — converge on the same conclusion for all three clusters.

### 0785 Sst Gaba_6 [CS20230722_CLUS_0785] · 186 cells

- **Chrna2 DISCORDANT (strong counter-evidence).** ABC Atlas Chrna2 expression filter eliminates the Sst Gaba_6 supertype entirely [A]. Chrna2 is a defining OLM marker [8]; its absence at supertype level is the principal disqualifier.
- **Annotation transfer: 0/46 cells** mapped to Sst Gaba_6 supertype. Zero transcriptomic support for OLM identity.
- **Pnoc DISCORDANT.** Pnoc is absent from this cluster, inconsistent with the OLM neuropeptide profile [9]. This is an additional independent marker-level mismatch.
- **Location APPROXIMATE — CA3 SO only, not CA1 SO.** CA3 SO (39 cells) and CA3 SLM (11 cells) are present. CA3 is adjacent to CA1 *(adjacent region — weak counter-evidence on location alone)*. However, Chrna2 absence and annotation transfer failure are the primary disqualifiers, not location.
- **Open question:** Given Chrna2 absence and Pnoc discordance, cluster 0785 likely represents a non-OLM Sst stratum oriens interneuron type — possibly oriens-bistratified or back-projecting. No experiments are proposed for this edge pending resolution of supertype identity.

### 0788 Sst Gaba_6 [CS20230722_CLUS_0788] · 50 cells

- **Chrna2 DISCORDANT (strong counter-evidence).** Sst Gaba_6 supertype eliminated by ABC Atlas Chrna2 expression filter [A].
- **Annotation transfer: 0/46 cells** mapped to Sst Gaba_6 supertype.
- **Location APPROXIMATE — small CA1/CA3 SO counts, SLM absent.** CA1 SO: 8 cells, CA3 SO: 13 cells. The CA1 SO signal is present but based on very few cells. CA1 and CA3 are adjacent supertypes *(adjacent regions — weak counter-evidence on location alone)*.
- **Low cell count (50 total).** Four corpus callosum cells may represent contamination; cluster reliability is uncertain.
- **Full neuropeptide triad present (plus Cort).** The presence of Sst, Npy, and Pnoc is notable but outweighed by the Chrna2 disqualifier and zero annotation transfer support.

### 0789 Sst Gaba_6 [CS20230722_CLUS_0789] · 177 cells

- **Chrna2 DISCORDANT (strong counter-evidence).** Sst Gaba_6 supertype eliminated by Chrna2 expression filter [A].
- **Annotation transfer: 0/46 cells** mapped to Sst Gaba_6 supertype.
- **Location APPROXIMATE — CA3 SO only, no CA1 SO or SLM.** No CA1 SO signal at all; 25 cells in CA3 SO only. CA3 is adjacent to CA1 *(adjacent region — weak counter-evidence on location alone)*, but the complete absence of CA1 representation is notable.
- **Major amygdala component (~28% of cluster).** Medial amygdala (31 cells) and posterior amygdala (18 cells) together comprise approximately 28% of this cluster. The posterior amygdala is anatomically distant from hippocampal CA1 stratum oriens *(distant region — stronger counter-evidence; amygdalar Sst interneurons represent a distinct population from canonical hippocampal OLM cells)*.

---

## Proposed experiments

### Annotation transfer — status of completed work

MapMyCells annotation transfer (GEO:GSE124847, Winterer et al. 2019 [7]; cell_type_mapper v1.7.1, default parameters, raw normalization; WMBv1 CCN20230722) has already been run on 46 OLM interneurons.

**What this resolved:** Sst Gaba subclass (F1 = 0.68), Sst Gaba_3 supertype (F1 = 0.67, group purity 0.96) confirmed as the OLM mapping target. Sst Gaba_6 supertype eliminated (F1 = 0.0 for all three clusters). Lamp5 Lhx6 subclass eliminated (F1 = 0.0). Both Sst-OLM and Htr3a-OLM subtypes from GSE124847 converge on Sst Gaba_3.

**What remains unresolved:** The within-Sst-Gaba_3 cluster identity. OLM cells scattered across sibling clusters 0767–0774; best cluster-level recipient was 0768 Sst Gaba_3 (F1 = 0.47, 15/46 cells), not 0769. The existing source dataset is not Chrna2-enriched.

A refined annotation transfer experiment using a Chrna2-Cre-selected source is therefore still warranted and is listed as Experiment 1 below.

---

### Group 1 — Chrna2-Cre enriched annotation transfer (MapMyCells)

- **What:** MapMyCells (cell_type_mapper, WMBv1 CCN20230722) on Chrna2-Cre-selected CA1 stratum oriens neurons. Differs from the completed round in using Chrna2 lineage selection to reduce contamination by non-OLM Sst SO interneurons.
- **Target:** F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3
- **Expected output:** `AnnotationTransferEvidence` on edge_olm_to_wmb_clus_0769; would determine whether the edge should point to 0769, 0768, or remain at Sst Gaba_3 supertype level
- **Resolves:** Open questions 1 and 2

### Group 2 — Targeted scRNA-seq or MERFISH of Chrna2+ stratum oriens neurons

- **What:** MERFISH or targeted scRNA-seq with spatial layer annotation restricted to Chrna2+ CA1 SO neurons; or query of an existing MERFISH dataset that includes Chrna2 in its probe panel
- **Target:** WMBv1 cluster assignment of ≥30 Chrna2+ OLM cells with layer confirmation (soma in SO)
- **Expected output:** `LiteratureEvidence` or `AnnotationTransferEvidence` on edge_olm_to_wmb_clus_0769; would also provide atlas-side Grm1/mGluR1 expression data at cluster level
- **Resolves:** Open question 1; Grm1 NOT_ASSESSED gap on all MODERATE and LOW edges

### Group 3 — Patch-seq of stratum oriens interneurons

- **What:** Patch-seq (simultaneous electrophysiology, morphology reconstruction, scRNA-seq) of CA1 and CA3 stratum oriens interneurons; targeting both Sst-Cre and Lamp5-Cre neurons
- **Target:** WMBv1 cluster assignment with confirmed OLM morphology (axon in SLM) and Chrna2/Grm1 expression in ≥10 cells per cluster
- **Expected output:** `LiteratureEvidence` on edge_olm_to_wmb_clus_0769 (morphological confirmation of CA1 SO cells in 0769) and edge_olm_to_wmb_clus_0727 (test whether any Lamp5 Lhx6 CA3 SO cells carry OLM morphology)
- **Resolves:** Open questions 1, 2, and 3

### Group 4 — Atlas query: Grm1 cluster-level expression

- **What:** Query ABC Atlas or Allen Cell Types Database for Grm1 expression specifically in clusters 0767–0774 (Sst Gaba_3 supertype)
- **Target:** Identify which cluster within Sst Gaba_3 shows highest Grm1 detection rate; compare against 96% source-side rate
- **Expected output:** `ATLAS_QUERY` evidence item converting the NOT_ASSESSED Grm1 alignment to CONSISTENT or DISCORDANT
- **Resolves:** Grm1 NOT_ASSESSED gap on all MODERATE and LOW edges (open across edge_olm_to_wmb_clus_0769 and edge_olm_to_wmb_clus_0727)

### Group 5 — Targeted literature search: OLM negative markers

- **What:** Cite-traverse on "calbindin OLM hippocampus", "calretinin OLM hippocampus", "parvalbumin OLM hippocampus", "NOS OLM hippocampus", "VIP OLM hippocampus". Objective: find primary studies that confirmed OLM identity (morphological reconstruction or electrophysiology) and tested PV, Calb1, Calb2, NOS, VIP expression.
- **Target:** ≥1 primary citation per negative marker with morphology-confirmed OLM cells
- **Expected output:** `LiteratureEvidence` for each negative marker on the classical node
- **Resolves:** Marker evidence provenance gap for all five negative markers; no new experiments required beyond literature search

---

## Open questions

1. **Are the CA1 SO cells in cluster 0769 [CS20230722_CLUS_0769] OLM-morphology?** Atlas MERFISH records soma position only — axonal projection to SLM is unverified for the 87 CA1 SO cells. What are the posterior amygdala cells (n=95) within the same cluster? *(edge_olm_to_wmb_clus_0769)*

2. **Why do OLM cells map to cluster 0768 rather than 0769 in the annotation transfer?** Do clusters 0768 Sst Gaba_3 and 0769 Sst Gaba_3 differ in hippocampal enrichment, Chrna2 expression, or other OLM-relevant properties? Should the edge be reassigned to 0768 or broadened to Sst Gaba_3 supertype level? *(edge_olm_to_wmb_clus_0769)*

3. **Is Sst expression in cluster 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] biologically meaningful for OLM identity?** Does this cluster contain cells with OLM morphology or electrophysiology? The Lamp5 Lhx6 subclass lineage is unexpected for canonical MGE-derived Sst+ OLM cells. *(edge_olm_to_wmb_clus_0727)*

4. **Given Chrna2 absence from Sst Gaba_6, are clusters 0785, 0788, and 0789 non-OLM Sst stratum oriens types?** If so, what classical interneuron types do they represent (oriens-bistratified, back-projecting, hippocampal Sst without OLM morphology, other)? *(shared across edges 0785, 0788, 0789)*

5. **What is the biological identity of the posterior amygdala population in cluster 0769 (n=95) and 0789 (n=49)?** Are these Sst interneurons molecularly related to hippocampal OLM cells, or are they co-clustered incidentally? *(edges 0769 and 0789)*

---

## Evidence base

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_olm_to_wmb_clus_0769 | ATLAS_METADATA | SUPPORT | Atlas metadata; CA1 SO enrichment (87 cells), full neuropeptide triad, Chrna2 retained at Sst Gaba_3 supertype |
| edge_olm_to_wmb_clus_0769 | ANNOTATION_TRANSFER | PARTIAL | GSE124847, MapMyCells; F1=0.67 at Sst Gaba_3 supertype; 0/46 cells at cluster 0769 specifically; best cluster-level F1=0.47 for sibling 0768 |
| edge_olm_to_wmb_clus_0727 | ATLAS_METADATA | PARTIAL | Atlas metadata; CA3 SO + SLM present; Lamp5 Lhx6 subclass discordant; Npy absent |
| edge_olm_to_wmb_clus_0727 | ANNOTATION_TRANSFER | REFUTE | GSE124847, MapMyCells; 0/46 cells mapped to Lamp5 Lhx6 subclass |
| edge_olm_to_wmb_clus_0785 | ATLAS_METADATA | PARTIAL | Atlas metadata; Sst subclass consistent; Chrna2 absent from supertype; Pnoc absent |
| edge_olm_to_wmb_clus_0785 | ATLAS_QUERY | REFUTE | ABC Atlas [A]; HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 supertype entirely |
| edge_olm_to_wmb_clus_0785 | ANNOTATION_TRANSFER | REFUTE | GSE124847, MapMyCells; 0/46 cells mapped to Sst Gaba_6 supertype |
| edge_olm_to_wmb_clus_0788 | ATLAS_METADATA | PARTIAL | Atlas metadata; mixed CA1/CA3 SO (small counts); Chrna2 absent from supertype; low total cell count |
| edge_olm_to_wmb_clus_0788 | ATLAS_QUERY | REFUTE | ABC Atlas [A]; HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 supertype entirely |
| edge_olm_to_wmb_clus_0788 | ANNOTATION_TRANSFER | REFUTE | GSE124847, MapMyCells; 0/46 cells mapped to Sst Gaba_6 supertype |
| edge_olm_to_wmb_clus_0789 | ATLAS_METADATA | PARTIAL | Atlas metadata; CA3 SO only; major amygdala component (~28%); Chrna2 absent from supertype |
| edge_olm_to_wmb_clus_0789 | ATLAS_QUERY | REFUTE | ABC Atlas [A]; HPF/GABA/Chrna2 filter eliminates Sst Gaba_6 supertype entirely |
| edge_olm_to_wmb_clus_0789 | ANNOTATION_TRANSFER | REFUTE | GSE124847, MapMyCells; 0/46 cells mapped to Sst Gaba_6 supertype |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Zemankovics et al. 2010 | [20421280](https://pubmed.ncbi.nlm.nih.gov/20421280/) | Soma location |
| [2] | Nichol et al. 2018 | [29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/) | Soma location; Chrna2 as specific OLM marker |
| [3] | Tecuatl et al. 2020 | [33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/) | Soma location |
| [4] | Böhm et al. 2015 | [26021702](https://pubmed.ncbi.nlm.nih.gov/26021702/) | Neurotransmitter type (GABAergic) |
| [5] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Neurotransmitter type (GABAergic) |
| [6] | Hooft et al. 2000 | [10804195](https://pubmed.ncbi.nlm.nih.gov/10804195/) | Sst marker; mGluR1 marker |
| [7] | Winterer et al. 2019 | [31420995](https://pubmed.ncbi.nlm.nih.gov/31420995/) | Sst marker; Chrna2 marker; mGluR1; neuropeptides Sst/Npy/Pnoc; source dataset GSE124847 for annotation transfer |
| [8] | Leão et al. 2012 | [23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/) | Chrna2 as molecular marker for OLM cells |
| [9] | Thulin et al. 2025 | [40757734](https://pubmed.ncbi.nlm.nih.gov/40757734/) | Pnoc neuropeptide; OLM subclusters with differential dorsal–ventral connectivity |
| [A] | ABC Atlas | [view](https://tinyurl.com/a4f3kd4v) | HPF/GABA/Chrna2 expression filter; retains Sst Gaba_3 supertype; eliminates Sst Gaba_6 supertype |
