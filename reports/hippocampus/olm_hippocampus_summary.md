# Oriens-Lacunosum Moleculare (O-LM) interneuron — WMBv1 Mapping Report
*draft · 2026-03-25 · Source: `kb/draft/hippocampus/hippocampus_GABA_stratum_oriens_stubs.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Location note

> **Location note.** WMBv1 location data derives from MERFISH spatial
> registration and records **soma position** only. Axonal and dendritic
> projection targets are not reflected in atlas cluster location fields and
> are not used in mapping assessments.

The O-LM interneuron is defined in part by its axonal projection: the soma resides in stratum oriens [UBERON:0014548] while the axon travels vertically and terminates exclusively in stratum lacunosum-moleculare [UBERON:0007637], where it innervates the apical tufts of pyramidal cells. Because WMBv1 MERFISH location records soma position only, the SLM axonal arborisation — a hallmark feature distinguishing O-LM cells from other stratum oriens interneurons such as oriens-bistratified and back-projecting cells — is invisible to the atlas. Matching on MERFISH location therefore captures only the somatic half of the morphological definition and cannot discriminate axonal projection targets.

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum oriens of hippocampus [UBERON:0014548] (CA1); stratum lacunosum-moleculare of hippocampus [UBERON:0007637] (axon terminal zone) | [1], [2], [3] |
| Neurotransmitter | GABAergic | [4], [5] |
| Defining markers | Sst, Chrna2, mGluR1/Grm1 | Sst: [6], [7]; Chrna2: [2], [8], [7]; mGluR1: [6], [7] |
| Negative markers | PV, CB, CR, NOS, VIP | — |
| Neuropeptides | Sst, Npy, Pnoc | Sst: [7]; Npy: [7]; Pnoc: [9], [7] |

**Notes on marker quantification.** Detection rates from re-analysis of GSE124847 raw counts (Winterer et al. 2019 [7]): Sst (100% of OLM cells), Chrna2 (35%), mGluR1/Grm1 (96%). Chrna2 is detected in a minority of cells at transcript level in this dataset but remains the most OLM-specific marker available [2], [8].

**Morphology summary.** Large horizontally oriented soma at the stratum oriens/alveus border. Horizontal dendrites in stratum oriens densely decorated with long spines. Axon projects vertically through stratum pyramidale and radiatum, arborizing extensively in stratum lacunosum-moleculare with densely packed varicosities. Minor axon collaterals remain in stratum oriens.

**Electrophysiology.** Regular-to-fast spiking, tonic or mildly adapting firing. Pronounced sag response (Ih via HCN2 h-channels). Theta resonance (4–12 Hz). High input resistance, slow membrane time constants. Anti-Hebbian LTP dependent on Ca²⁺-permeable AMPA receptors.

**Heterogeneity note.** The OLM class contains molecularly heterogeneous subpopulations. Thulin et al. 2025 [9] identify three Sst/Pnoc subclusters with differential dorsal–ventral connectivity. These may warrant separate nodes in future iterations.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0769 Sst Gaba_3 [CS20230722_CLUS_0769] | Sst Gaba_3 | 243 | 🟡 MODERATE | Chrna2 APPROXIMATE · Npy CONSISTENT | Best candidate |
| 2 | 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] | Lamp5 Lhx6 Gaba_1 | 98 | 🔴 LOW | Npy DISCORDANT · Sst APPROXIMATE | Speculative |
| — | 0785 Sst Gaba_6 [CS20230722_CLUS_0785] | Sst Gaba_6 | 186 | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |
| — | 0788 Sst Gaba_6 [CS20230722_CLUS_0788] | Sst Gaba_6 | 50 | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |
| — | 0789 Sst Gaba_6 [CS20230722_CLUS_0789] | Sst Gaba_6 | 177 | ⚪ UNCERTAIN | Chrna2 DISCORDANT | Eliminated (Chrna2) |

Total: 5 edges. Relationship type: TYPE_A_SPLITS (classical OLM maps across multiple WMBv1 clusters; no single cluster captures the full classical type).

---

## 0769 Sst Gaba_3 [CS20230722_CLUS_0769] · 🟡 MODERATE

### Supporting evidence

- **GABA neurotransmitter type consistent.** The cluster belongs to the Sst Gaba subclass, fully consistent with the GABAergic identity of O-LM cells [4], [5].
- **Sst subclass consistent.** The cluster is defined at the subclass level by Sst expression, directly matching the canonical OLM marker [6], [7].
- **Full neuropeptide triad matched.** Cluster 0769 carries all three OLM neuropeptides — Sst, Npy, and Pnoc — the complete triad expected for OLM cells [7], [9]. No other evaluated cluster achieves this combination without missing at least one peptide.
- **Best CA1 stratum oriens signal.** Atlas metadata shows 87 cells located in CA1 SO (MBA:399), the primary soma location of O-LM cells. This is the strongest CA1 SO count among all evaluated clusters.
- **Chrna2 expression retained at supertype level.** ABC Atlas filtering on HPF anatomy, GABAergic NT, and Chrna2 expression retains the Sst Gaba_3 supertype while eliminating Sst Gaba_6 entirely [A]. Chrna2 expression is scattered across clusters of this supertype and is not a defining marker at cluster level, but its presence at the supertype level is consistent with an OLM marker profile.
- **Annotation transfer strongly supports parent Sst Gaba_3 supertype.** MapMyCells annotation transfer of 46 OLM interneurons (GSE124847, Winterer et al. 2019 [7]; cell_type_mapper v1.7.1, raw normalization; WMBv1 CCN20230722) mapped 43/46 cells (93%) to the Sst Gaba_3 supertype (F1 = 0.67 at supertype level; group purity = 0.96; median bootstrap = 1.0). At broader levels the mapping is essentially perfect: 45/46 cells map to Sst Gaba subclass (F1 = 0.68) and to class 07 CTX-MGE GABA (F1 = 0.68). The Sst Gaba_3 supertype, which contains cluster 0769, is the dominant transcriptomic attractor for OLM cells in this atlas.

### Concerns

- **Location APPROXIMATE — extra-hippocampal spread.** While CA1 SO is well represented (87 cells), the cluster also contains 61 cells in prosubiculum and 95 cells in posterior amygdala. The prosubiculum is adjacent to CA1 *(adjacent region — could reflect registration boundary error; weak counter-evidence)*. The posterior amygdala is anatomically distant *(distant region — stronger counter-evidence; canonical OLM cells may still be a subtype of the Sst Gaba_3 T-type, but not the CA1 population specifically)*. The cluster appears to aggregate Sst interneurons from multiple hippocampal-adjacent structures rather than being OLM-specific.
- **SLM absent from MERFISH location data.** The defining axonal projection to stratum lacunosum-moleculare is not recorded (MERFISH records soma position only — see location note above). Absence of SLM soma signal is expected for OLM cells and is not diagnostic here.
- **Annotation transfer resolves to supertype, not cluster 0769.** Although Sst Gaba_3 supertype receives strong OLM signal, cluster 0769 specifically received 0/46 cells from the annotation transfer. OLM cells preferentially mapped to sibling cluster 0768 (15/46 cells after bootstrap filtering; best cluster-level F1 = 0.47 for 0768). The mapping is most appropriate at supertype rather than cluster level; the edge to 0769 is a placeholder for the Sst Gaba_3 supertype rather than a confirmed cluster-level match.
- **mGluR1 (Grm1) not resolvable from atlas metadata.** Grm1 is detected in 96% of OLM cells (GSE124847 re-analysis), but is absent from the cluster's defining_markers or neuropeptides fields in WMBv1 — the comparison cannot be made at cluster level at this time.
- **Cluster may include non-OLM Sst interneurons.** Prosubiculum (61 cells) and posterior amygdala (95 cells) inflate cell count and reduce specificity for an OLM assignment.

### What would upgrade confidence

- **Annotation transfer at higher resolution (refined experiment).** A round of MapMyCells using a Chrna2-Cre-enriched CA1 stratum oriens dataset would add `AnnotationTransferEvidence` and test whether Chrna2-selected OLM cells converge on cluster 0769 vs 0768 or remain scattered across the Sst Gaba_3 supertype.
  - *What has already been done:* MapMyCells run on GSE124847 (46 OLM interneurons, Winterer et al. [7]), F1 = 0.67 at Sst Gaba_3 supertype. This resolved subclass (Sst Gaba) and supertype identity and eliminated Sst Gaba_6 and Lamp5 Lhx6 subclasses.
  - *What remains unresolved:* The within-supertype cluster identity (0769 vs 0768). The existing dataset mixes Sst-OLM and Htr3a-OLM subtypes and is not Chrna2-enriched.
  - *Refined version:* MapMyCells of Chrna2-Cre-selected CA1 SO neurons. Target: F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3. Expected output: `AnnotationTransferEvidence` on edge_olm_to_wmb_clus_0769.
- **Targeted transcriptomics of Chrna2+ stratum oriens neurons.** MERFISH or targeted scRNA-seq with spatial layer annotation restricted to Chrna2+ CA1 SO cells would identify which WMBv1 cluster(s) contain Chrna2-high OLM cells, and would add Grm1/mGluR1 expression data on the atlas side. Expected output: `LiteratureEvidence` or `AnnotationTransferEvidence`. Resolves open questions 1 and the Grm1 NOT_ASSESSED caveat.
- **Morphological validation of CA1 SO cells in cluster 0769.** Patch-seq of CA1 SO cells mapped to this cluster would confirm OLM morphology (axon in SLM) and add `LiteratureEvidence` for the TYPE_A_SPLITS relationship, resolving open question 2.

---

## 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] · 🔴 LOW

### Supporting evidence

- **GABA neurotransmitter type consistent.** GABAergic identity is shared with O-LM cells [4], [5].
- **Both SO and SLM layers represented.** Atlas metadata shows cells in CA3 SO (MBA:486) and CA3 SLM (MBA:471) — both layers of the OLM morphological circuit are present, consistent with a cell type whose soma sits in SO and whose axon innervates SLM.
- **Sst and Pnoc neuropeptides present.** Two of three OLM neuropeptides (Sst, Pnoc) are detected, consistent with partial peptide overlap.

### Concerns

- **Subclass DISCORDANT — Lamp5 Lhx6, not Sst.** This cluster belongs to the Lamp5 Lhx6 subclass. Canonical OLM cells are Sst-defined and MGE-derived. Lamp5 Lhx6 cells are also Lhx6+ (hence MGE-derived) but form a distinct lineage branch in the WMBv1 taxonomy. Sst appears in the neuropeptides field here, not as a defining marker — biologically surprising for a cluster proposed to capture canonical OLM identity.
- **Npy DISCORDANT.** This cluster lacks Npy, which is consistently expressed in OLM cells [7]. Npy absence disrupts the full neuropeptide triad that helps distinguish OLM from related Sst interneuron types.
- **Location APPROXIMATE — CA3-enriched, not CA1.** SO and SLM are present but in CA3, not CA1. CA3 is adjacent to CA1 *(adjacent region — could reflect a CA3 OLM-like population or registration overlap; weak counter-evidence on location alone)*, but the absence of CA1 SO signal is notable for canonical OLM.
- **Annotation transfer: zero cells mapped to Lamp5 Lhx6 subclass.** MapMyCells (GSE124847, 46 OLM cells) mapped 0/46 cells to the Lamp5 Lhx6 subclass; all 45 classified cells mapped to Sst Gaba subclass. This is strong direct counter-evidence against this cluster as an OLM target.
- **Chrna2 and mGluR1 not assessable.** Both defining OLM markers cannot be evaluated from cluster metadata.

### What would upgrade confidence

- **Patch-seq of Lamp5-Lhx6 neurons in CA3 stratum oriens.** Would add `LiteratureEvidence` directly testing whether Lamp5-Lhx6 CA3 SO cells have OLM morphology (axon in SLM) and Chrna2/mGluR1 expression. Without morphological and marker confirmation the Lamp5 Lhx6 subclass assignment argues against OLM identity.
- **Chrna2-Cre + MapMyCells (refined experiment).** Annotation transfer of Chrna2-Cre-selected CA1 SO neurons would test whether any cells map to the Lamp5 Lhx6 subclass, adding `AnnotationTransferEvidence` to this edge. If none map, the edge would be formally demoted to UNCERTAIN.
  - *What has already been done:* General OLM annotation transfer (GSE124847) already maps 0/46 cells to the Lamp5 Lhx6 subclass.
  - *What remains unresolved:* Whether the Chrna2+ OLM subpopulation specifically maps here (unlikely given the existing result, but a Chrna2-enriched dataset would provide definitive evidence).

---

## Eliminated candidates

All three remaining clusters — 0785 Sst Gaba_6 [CS20230722_CLUS_0785], 0788 Sst Gaba_6 [CS20230722_CLUS_0788], and 0789 Sst Gaba_6 [CS20230722_CLUS_0789] — share a single disqualifying signal: **Chrna2 DISCORDANT**. ABC Atlas filtering on HPF anatomy, GABAergic NT, and Chrna2 expression eliminates the entire Sst Gaba_6 supertype [A]. All three clusters belong to this supertype. In parallel, MapMyCells annotation transfer of 46 OLM cells (GSE124847, Winterer et al. [7]) mapped 0/46 cells to the Sst Gaba_6 supertype; all 45 classified cells went to Sst Gaba_3 instead. Two independent lines of evidence — atlas expression filtering and annotation transfer — converge on the same conclusion.

### 0785 Sst Gaba_6 [CS20230722_CLUS_0785] · 186 cells

- **Chrna2 DISCORDANT (strong).** ABC Atlas Chrna2 expression filter eliminates the Sst Gaba_6 supertype entirely [A]. Chrna2 is a defining marker of OLM cells; its absence at the supertype level is a principal disqualifier.
- **Annotation transfer: 0/46 cells** mapped to Sst Gaba_6. Zero transcriptomic support for OLM identity.
- **Location APPROXIMATE — CA3 SO, not CA1 SO.** CA3 is adjacent to CA1 *(adjacent region — weak counter-evidence on location alone)*, but Chrna2 absence and annotation transfer failure are the primary disqualifiers.
- **Pnoc DISCORDANT.** Pnoc is absent from this cluster, inconsistent with the OLM neuropeptide profile [9].
- **CA3-enriched, no CA1 SO.** Classical OLM is best characterized in CA1; CA3 enrichment without CA1 representation is inconsistent with canonical OLM anatomy.

### 0788 Sst Gaba_6 [CS20230722_CLUS_0788] · 50 cells

- **Chrna2 DISCORDANT (strong).** Same argument as 0785: Sst Gaba_6 supertype eliminated by ABC Atlas Chrna2 expression filter [A].
- **Annotation transfer: 0/46 cells** mapped to Sst Gaba_6.
- **Location APPROXIMATE — mixed CA1/CA3 SO, SLM absent.** Small cell counts in SO (CA1 SO: 8 cells, CA3 SO: 13 cells) and no SLM signal. Marginal anatomical alignment.
- **Low total cell count (50 cells).** Possible contamination from corpus callosum (4 cells noted in caveats). Cluster reliability is uncertain.
- **Full neuropeptide triad present (plus Cort).** This is the only Sst Gaba_6 cluster with all three OLM neuropeptides — in isolation this would be noteworthy, but it is outweighed by the Chrna2 and annotation transfer disqualifiers.

### 0789 Sst Gaba_6 [CS20230722_CLUS_0789] · 177 cells

- **Chrna2 DISCORDANT (strong).** Sst Gaba_6 supertype eliminated by Chrna2 expression filter [A].
- **Annotation transfer: 0/46 cells** mapped to Sst Gaba_6.
- **Location APPROXIMATE — CA3 SO only, no CA1 SO or SLM.** No CA1 SO or SLM signal at all. CA3 is adjacent to CA1 *(adjacent region — weak counter-evidence on location alone)*, but the absence of CA1 and SLM representation is notable.
- **Major amygdala component (~28% of cells).** Medial amygdala (31 cells) and posterior amygdala (18 cells) together account for ~28% of this cluster. The amygdala is anatomically distant from hippocampal CA1 *(distant region — stronger counter-evidence; any OLM-like cells in amygdala would constitute a distinct population from canonical hippocampal OLM cells)*.

---

## Proposed experiments

### Group 1 — Chrna2-Cre targeted annotation transfer (MapMyCells)

**What has already been done.** MapMyCells annotation transfer of GSE124847 (46 OLM interneurons, Winterer et al. 2019 [7]; cell_type_mapper v1.7.1; WMBv1 CCN20230722) resolved subclass (Sst Gaba), supertype (Sst Gaba_3), and eliminated Sst Gaba_6 and Lamp5 Lhx6 subclasses. F1 = 0.67 at supertype level; 0/46 cells mapped to cluster 0769 specifically.

**What remains unresolved.** The within-Sst-Gaba_3 cluster identity (0769 vs sibling cluster 0768). The existing dataset is not Chrna2-enriched and mixes Sst-OLM and Htr3a-OLM subtypes.

**Refined experiment — Chrna2-Cre-selected CA1 SO → MapMyCells.**

- **What:** MapMyCells (cell_type_mapper, WMBv1 CCN20230722) on Chrna2-Cre-selected CA1 stratum oriens neurons
- **Target:** F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3
- **Expected output:** `AnnotationTransferEvidence` on edge_olm_to_wmb_clus_0769
- **Resolves:** Open questions 1 and 2; whether the edge should be reassigned from 0769 to 0768 or broadened to supertype level

### Group 2 — MERFISH or targeted scRNA-seq of Chrna2+ stratum oriens neurons

- **What:** MERFISH or targeted scRNA-seq with spatial layer annotation restricted to Chrna2+ CA1 SO neurons
- **Target:** Cluster-level WMBv1 assignment of ≥30 Chrna2+ OLM cells with layer confirmation (soma in SO)
- **Expected output:** `LiteratureEvidence` or `AnnotationTransferEvidence` on edge_olm_to_wmb_clus_0769; would also provide atlas-side Grm1/mGluR1 expression data
- **Resolves:** Open question 1 (OLM morphology of CA1 SO cells in 0769); Grm1 NOT_ASSESSED caveat on all edges

### Group 3 — Patch-seq of stratum oriens interneurons

- **What:** Patch-seq (simultaneous electrophysiology, morphology reconstruction, scRNA-seq) of CA1 and CA3 stratum oriens interneurons
- **Target:** WMBv1 cluster assignment with confirmed OLM morphology (axon in SLM) and Chrna2/mGluR1 expression for ≥10 cells per cluster
- **Expected output:** `LiteratureEvidence` on edge_olm_to_wmb_clus_0769 (confirm OLM morphology) and edge_olm_to_wmb_clus_0727 (test whether Lamp5-Lhx6 CA3 SO cells have OLM morphology)
- **Resolves:** Open question 2 (cluster 0769 vs 0768 within Sst Gaba_3); open question 3 (Lamp5-Lhx6 OLM morphology); would also address whether the amygdala population in 0769 is biologically related to OLM

---

## Open questions

1. **Are the CA1 SO cells in cluster 0769 [CS20230722_CLUS_0769] OLM-morphology?** Atlas metadata shows 87 CA1 SO cells but MERFISH records soma position only — axonal projection to SLM is unverified. What are the posterior amygdala cells (n=95) within the same cluster? *(edge_olm_to_wmb_clus_0769)*

2. **Why do OLM cells map to cluster 0768 rather than 0769 in the annotation transfer?** Do clusters 0768 and 0769 differ in hippocampal enrichment, Chrna2 expression, or other properties relevant to OLM identity? Should the edge be reassigned to 0768 or broadened to Sst Gaba_3 supertype level? *(edge_olm_to_wmb_clus_0769)*

3. **Is Sst expression in cluster 0727 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0727] biologically meaningful for OLM?** Does this cluster contain cells with OLM morphology or electrophysiology? The Lamp5 Lhx6 lineage is unexpected for canonical MGE-derived Sst+ OLM cells. *(edge_olm_to_wmb_clus_0727)*

4. **Given Chrna2 absence from Sst Gaba_6, is cluster 0785 [CS20230722_CLUS_0785] a non-OLM Sst stratum oriens type?** If so, what classical interneuron type does it represent (oriens-bistratified, back-projecting, other)? *(edge_olm_to_wmb_clus_0785)*

5. **Are the CA3 SO / CA1 SO cells in cluster 0788 [CS20230722_CLUS_0788] OLM-morphology?** What are the corpus callosum cells (n=4) — biological or contamination? *(edge_olm_to_wmb_clus_0788)*

6. **Are the CA3 SO cells in cluster 0789 [CS20230722_CLUS_0789] OLM-like?** What is the biological identity of the amygdala population (~28% of cluster, 49 cells total)? *(edge_olm_to_wmb_clus_0789)*

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
