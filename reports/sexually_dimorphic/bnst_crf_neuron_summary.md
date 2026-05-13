# BNST (anterolateral) corticotropin-releasing factor (CRF) neuron — WMBv1 Mapping Report
*2026-04-25 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

---

## Introduction

The anterolateral bed nucleus of the stria terminalis (BNST) houses a population of GABAergic neurons defined by their release of corticotropin-releasing factor (CRF/Crh). These neurons participate in the affective component of pain processing and show a well-documented sexual dimorphism — CRF+ neurons in the anterolateral BNST are larger and more numerous in females than males [1][2]. Mapping this classically defined population to a WMBv1 transcriptomic cluster matters both for placing the sexual-dimorphism phenotype in a single-cell taxonomic frame and because the Cell Ontology currently lacks a BNST-specific CRF neuron term.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Bed nuclei of the stria terminalis [MBA:174] (dlBNST, ovBNST, alBNST sub-nuclei) | [1], [2] |
| Defining markers | Crh | — |
| Negative markers | Calb1 | — |
| Neuropeptides | Crh | [1], [2] |
| CL term | corticotropin-releasing neuron (CL:4072021) — BROAD | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / neuropeptide:** classical neuroanatomical / pharmacological literature · rat dlBNST and mouse alBNST · [1], [2]
  > The BNST modulates pain sensitivity by releasing corticotropin-releasing factor (CRF) from neurons in the anterolateral subdivision (Ide et al., 2013). Female mice have larger CRF neurons in the anterolateral BNST than male mice (Uchida et al., 2019). Dopaminergic projection from the periaqueductal gray (PAG) to the BNST, which preferentially targets the dorsal part, including the anterolateral subdivision (Gungor et al., 2016), drives pain-related behaviors differently between male and female mice (Yu et al., 2021b).
  > — Frontiers review 2025, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 279874350_b2b4adba -->

  > Pain is a complex experience composed of sensory and affective components. Although the neural systems of the sensory component of pain have been studied extensively, those of its affective component remain to be determined. In the present study, we examined the effects of corticotropin-releasing factor (CRF) and neuropeptide Y (NPY) injected into the dorsolateral bed nucleus of the stria terminalis (dlBNST) on pain-induced aversion and nociceptive behaviors in rats to examine the roles of these peptides in affective and sensory components of pain, respectively. In vivo microdialysis showed that formalin-evoked pain enhanced the release of CRF in this brain region. Using a conditioned place aversion (CPA) test, we found that intra-dlBNST injection of a CRF1 or CRF2 receptor antagonist suppressed pain-induced aversion. Intra-dlBNST CRF injection induced CPA even in the absence of pain stimulation. On the other hand, intra-dlBNST NPY injection suppressed pain-induced aversion. Coadministration of NPY inhibited CRF-induced CPA. This inhibitory effect of NPY was blocked by coadministration of a Y1 or Y5 receptor antagonist. Furthermore, whole-cell patch-clamp electrophysiology in dlBNST slices revealed that CRF increased neuronal excitability specifically in type II dlBNST neurons, whereas NPY decreased it in these neurons. Excitatory effects of CRF on type II dlBNST neurons were suppressed by NPY. These results have uncovered some of the neuronal mechanisms underlying the affective component of pain by showing opposing roles of intra-dlBNST CRF and NPY in pain-induced aversion and opposing actions of these peptides on neuronal excitability converging on the same target, type II neurons, within the dlBNST.
  > — Ide et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 14550592_292dccea -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] (BROAD).

The BNST-specific, female-biased anterolateral CRF population is not separately resolved in CL; the parent CRH-secreting-neuron term covers it but is not sub-nucleus specific.

---

## Results

Two candidate WMBv1 supertypes were assessed; neither reaches MODERATE confidence. SUPT_0358 (MEA-BST Lhx6 Nfib Gaba_2) is held at LOW pending direct Crh confirmation, and SUPT_0393 (CEA-BST Rai14 Pdyn Crh Gaba_2) is currently UNCERTAIN because its supertype-level Calb1 expression conflicts with the classical Calb1-negative definition.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0358 MEA-BST Lhx6 Nfib Gaba_2 | CS20230722_SUPT_0358 | 666 | 🔴 LOW | BST δ-rank · Crh NOT_ASSESSED | Speculative |
| — | 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 | CS20230722_SUPT_0393 | 231 | ⚪ UNCERTAIN | Crh CONSISTENT · Calb1 DISCORDANT | Eliminated (negative_Calb1) |

Total edges: 2 (both PARTIAL_OVERLAP).

### Property alignment — SUPT_0358 (primary, LOW)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic (CRF+ BST neurons predominantly GABAergic) | GABAergic (Lhx6 Nfib Gaba_2) | not assessed | CONSISTENT |
| Soma location | MBA:351 (Bed nuclei of stria terminalis) | Multiple child clusters; CLUS_1290 primary soma=BST | CLUS_1290 → BST | APPROXIMATE |
| Crh | POSITIVE (defining marker) | NOT_ASSESSED — Knoedler sorted on Esr1, not Crh | not assessed | NOT_ASSESSED |
| Sex ratio | sexually dimorphic (anterolateral BST CRF+ neurons larger in females) | child cluster MFRs span 0.82 to 99.0 | CLUS_1293 MFR=99 (male-biased) | APPROXIMATE |

*(4 of SUPT_0358's child clusters appear in the top-10 BNST_FR vs VMH_FR δ ranking — CLUS_1295, CLUS_1291, CLUS_1290 (BST primary soma), CLUS_1293 (MFR=99, male-biased). The MFR spread (0.82–99) indicates SUPT_0358 contains heterogeneous sex-biased subpopulations; best BST-localised match is CLUS_1290.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Knoedler 2022 TRAP-seq (Esr1+ BNST_FR vs VMH_FR) | Bulk transcriptomic correlation | PARTIAL | best_child_cluster=CLUS_1295 (rank 4, δ=0.0161); 4 SUPT_0358 child clusters in top 10 | [3] |

![Top 10 clusters by δ for BNST_FR_vs_VMH_FR (CS20230722_SUPT_0358)](figures/bnst_crf_neuron_BNST_FR_vs_VMH_FR_b7a35400.png)

### 0358 MEA-BST Lhx6 Nfib Gaba_2 · 🔴 LOW

**Supporting evidence**

- Knoedler 2022 Esr1+ TRAP-seq paired-bulk contrast (BNST female-receptive vs VMH female-receptive) places four child clusters of SUPT_0358 in the top 10 δ ranks: CLUS_1295 (rank 4, δ=0.0161), CLUS_1291 (rank 5, δ=0.0160), CLUS_1290 (rank 9, δ=0.0156; primary soma BST), CLUS_1293 (rank 10, δ=0.0152). CLUS_1290 is the BST-localised hit by atlas primary anatomy [3].
- GABAergic NT identity (Lhx6 Nfib Gaba_2) is consistent with the literature inference that BNST CRF+ neurons are predominantly GABAergic.
- Sex-ratio direction is partially supported: the supertype contains child clusters across a wide MFR range (0.82–99), so a female-biased child cluster is plausible but not directly identified by this evidence type.

| Rank | Cluster | Supertype | δ | MFR | Top anatomy |
|---:|---|---|---:|---:|---|
| 1 | CLUS_0707 | SUPT_0199 | 0.0175 | 1.56 | Secondary motor area, layer 1 |
| 2 | CLUS_0642 | SUPT_0177 | 0.0172 | 1.7 | Secondary motor area, layer 2/3 |
| 3 | CLUS_1143 | SUPT_0322 | 0.0164 | 1.33 | ventral hippocampal commissure |
| **4** | **CLUS_1295** | **SUPT_0358** | **0.0161** | **0.82** | **Medial amygdalar nucleus** |
| **5** | **CLUS_1291** | **SUPT_0358** | **0.0160** | **1.27** | **Medial amygdalar nucleus** |
| 6 | CLUS_1144 | SUPT_0322 | 0.0159 | 1.44 | third ventricle |
| 7 | CLUS_1073 | SUPT_0305 | 0.0156 | 0.92 | Lateral septal nucleus, rostral |
| 8 | CLUS_1186 | SUPT_0336 | 0.0156 | 0.61 | Lateral septal nucleus, rostral |
| **9** | **CLUS_1290** | **SUPT_0358** | **0.0156** | **2.23** | **Bed nuclei of the stria terminalis** |
| **10** | **CLUS_1293** | **SUPT_0358** | **0.0152** | **99.0** | **Medial amygdalar nucleus** |

**Marker evidence provenance**

- **Crh (defining marker, neuropeptide):** Classical evidence is protein-level pharmacological + microdialysis [2] and review-level synthesis [1] — i.e. CRF release was directly measured in dlBNST and the cell type's identity rests on its CRF secretion. The Knoedler TRAP-seq contrast that identifies SUPT_0358 sorted on Esr1, *not* on Crh, so atlas-side Crh expression in SUPT_0358 is **not assessed** in this evidence. SUPT_0358 carries no DEFINING Crh annotation in WMBv1 metadata (contrast with SUPT_0393, where Crh=7.96 is DEFINING_SCOPED). Source-side Crh evidence is solid; target-side Crh confirmation is the key gap.
- **Calb1 (negative marker):** The classical type is defined as Calb1-negative to distinguish it from the calbindin+ principal nucleus of BNST. SUPT_0358 Calb1 expression is not reported in this facts set, so target-side cross-check is not assessed.

**Concerns**

- Crh expression in SUPT_0358 is NOT_ASSESSED — Knoedler used Esr1+ TRAP-seq, so SUPT_0358's claim rests on Esr1-positive co-localisation, not on direct Crh measurement. The Esr1+/Crh+ overlap fraction in BNST is unknown from this run.
- Location APPROXIMATE: SUPT_0358 spans BST and MEA at the supertype level; only CLUS_1290 has BST as its primary soma anatomy. *(adjacent / cross-region supertype — supertype-level location is mixed but a BST-resident child cluster exists, so this is moderate counter-evidence.)*
- Sex-ratio APPROXIMATE with a within-supertype contradiction — CLUS_1293 shows MFR=99 (extreme male bias), inconsistent with the female-biased classical phenotype. The female-biased BNST-CRF population, if present, is likely one of the lower-MFR child clusters (e.g. CLUS_1295 MFR=0.82).
- AMBIGUOUS_MAPPING: this edge is co-primary with SUPT_0393. SUPT_0393 carries direct Crh evidence (DEFINING_SCOPED, mean 7.96) but fails on Calb1; SUPT_0358 carries Esr1+ BST localisation but no direct Crh signal. The two supertypes may capture distinct portions of a heterogeneous BNST-CRF population.
- NO_DISCRIMINATING_MARKER for Crh on SUPT_0358 — the mapping depends entirely on bulk-correlation co-localisation evidence.

**What would upgrade confidence**

- **ISH / MERFISH co-staining for Crh, Esr1, Calb1 in BNST** to quantify the Esr1+/Crh+/Calb1− triple-positive fraction at sub-nucleus resolution and discriminate SUPT_0358 vs SUPT_0393 anatomical boundaries (resolves UQ1, UQ2; target: ≥50% Esr1+ overlap with Crh+ in dlBNST).
- **MapMyCells annotation transfer** of an external BNST scRNA-seq dataset carrying Crh+ subset annotations onto WMBv1 (target: F1 ≥ 0.60 at SUPERTYPE level; expected output `AnnotationTransferEvidence` for SUPT_0358 vs SUPT_0393).
- **Per-child-cluster sex-ratio / Crh / Calb1 readout** under SUPT_0358 to pinpoint a single best cluster matching the female-biased Crh+ Calb1− profile.

## Eliminated candidates

### 0393 CEA-BST Rai14 Pdyn Crh Gaba_2 (CS20230722_SUPT_0393, n=231) — ⚪ UNCERTAIN

The primary disqualifying signal is **Calb1 DISCORDANT**: SUPT_0393 carries supertype-mean Calb1=5.57, but the classical type is defined as Calb1-negative (to distinguish dlBNST CRF neurons from the Calb1+ principal nucleus of BNST).

- **Crh CONSISTENT:** SUPT_0393 has Crh=7.96 (DEFINING_SCOPED) and is the only rank-1 candidate with BST location + Crh DEFINING marker + GABAergic NT. By the Crh axis this is the strongest atlas match.
- **NT CONSISTENT:** GABAergic (Gad2 DEFINING, Gaba label).
- **Location CONSISTENT:** MBA:351 (BNST) primary location, n=140 cells. *(same region as the classical type at the MBA parent level; sub-nucleus identity unconfirmed because WMBv1 MERFISH uses parent BNST without dlBNST/ovBNST/alBNST sub-assignment — MERFISH_REGISTRATION_UNCERTAINTY.)*
- **Calb1 DISCORDANT:** mean expression 5.57 contradicts the negative-marker definition. *(within-target discrepancy — SUPT_0393 likely aggregates Calb1+ and Calb1− BNST GABAergic subtypes; a child cluster with low Calb1 and high Crh would be a more specific candidate.)*
- **MARKER_NOT_SPECIFIC** caveat: the elimination is at supertype level only; child-cluster-resolved Calb1 might still rescue the mapping. Hence "Eliminated" applies to the supertype; the underlying child-cluster question remains open.

Counter-evidence strength: the Calb1 discrepancy is a real within-region marker mismatch (strong counter-evidence at supertype resolution). A Calb1-low / Crh-high child cluster would warrant re-promoting this edge.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** `bnst_crf_neuron` is defined on a CLASSICAL_NEUROCHEMICAL basis: Crh as the defining marker and neuropeptide, Calb1 as a negative marker distinguishing dlBNST CRF neurons from the Calb1+ principal-nucleus BNST population, soma in the anterolateral, dorsolateral, and oval BNST sub-nuclei (all under MBA:174 Bed nuclei of the stria terminalis). The female-biased sexual dimorphism (larger / more numerous CRF neurons in alBNST in females) and the type II electrophysiology classification within dlBNST are derived from classical pharmacology and patch-clamp work [1][2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Bulk transcriptomic correlation.**

| Field | Value |
|---|---|
| Source publication | Knoedler et al. 2022 · PMID:35143761 · [3] |
| GEO accession | GSE183092 |
| Technique | TRAP-seq |
| n pools | 12 |
| Atlas | CCN20230722 (SHA-256: b21ca985) |
| Statistic | spearman_rho |
| Parameters | pseudobulk_transform=log1p(sum/n_cells); pool_transform=log1p(replicate_mean(DESeq2_normalised_counts)); gene_id_space=ensembl_mouse_via_symbol_lookup (conf/gene_mapping_CCN20230722.tsv); gene_intersection=intersection_across_4_regions∩atlas_col_names; n_replicates_per_pool=3. |
| Script | [correlate.py](https://github.com/Cellular-Semantics/evidencell/blob/4e67d6b/kb/correlation_runs/corr_run_20260428_knoedler_esr1_wmbv1/correlate.py) |
| Code version | 4e67d6b |
| Caveats | Cross-sex within-region δ contrasts (Male vs FR or Male vs FNR) are artefactual: across all three regions tested (POA, VMH, BNST) the top hits are hindbrain Calcb cholinergic motor neurons — a global male-vs-female expression bias that swamps region-specific signals. Suspected causes: Y-linked/X-inactivation gene dosage, batch effects, sex-specific TRAP-seq pulldown efficiency. METHODOLOGICAL RULE: paired-bulk δ requires the two pools to differ in cell population (region/marker/state) holding sex constant. Cross-sex δ within a single population is not a valid use of this method. TRAP-seq vs scRNA-seq pseudobulk: polysome-bound mRNA shifts absolute ρ values lower than for FACS-bulk inputs (Stephens-style), but Spearman rank-based statistics handle the magnitude offset; δ rankings are comparable across the two run types. |

**Atlas data sources.**

- WMBv1 · CCN20230722 · pseudobulk source `conf/mapmycells/CCN20230722/precomputed_stats.h5` · SHA-256 `b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b`.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:18+00:00 from [kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml](kb/graphs/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_bnst_crf_neuron_to_cs20230722_supt_0358 | BULK_CORRELATION | PARTIAL | [3] |
| edge_bnst_crf_neuron_to_cs20230722_supt_0393 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** BNST (anterolateral) corticotropin-releasing factor (CRF) neuron → 0358 MEA-BST Lhx6 Nfib Gaba_2 [CS20230722_SUPT_0358] at LOW confidence. Key support: Knoedler 2022 Esr1+ TRAP-seq paired-bulk δ ranking (four child clusters in top 10; CLUS_1290 BST-primary). Key caveats: AMBIGUOUS_MAPPING (co-primary with SUPT_0393) and NO_DISCRIMINATING_MARKER (no DEFINING Crh on SUPT_0358 — mapping rests on Esr1+ proxy).

The Cell Ontology has no specific term for this population; corticotropin-releasing neuron [[CL:4072021](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4072021)] is the closest ancestor. CL:4072021 covers all CRH-secreting neurons across brain regions (PVN, hippocampus, BNST, etc.). BNST CRF neurons do secrete CRH, making this a valid BROAD match. A BNST-specific child term does not yet exist — the female-biased dlBNST CRF population is a potential CL contribution.

### Proposed experiments and follow-ups

The two edges share a single underlying experimental need: cluster-resolved co-localisation of Crh, Esr1, and Calb1 in BNST. Existing evidence (Knoedler bulk correlation) addresses BNST localisation of an Esr1+ supertype but does not directly measure Esr1+/Crh+ overlap, so the experiments below are *additive* to that run, not duplicates of it.

- **What:** ISH or MERFISH co-staining for Crh, Esr1, and Calb1 in BNST sub-nuclei (dlBNST, ovBNST, alBNST).
  **Target:** ≥50% Crh+ overlap with Esr1+ in dlBNST; Calb1-negative fraction quantified.
  **Expected output:** sub-nucleus-resolved marker profile feeding back as `LiteratureEvidence` or `AtlasMetadata` cross-reference.
  **Resolves:** Q1, Q2 — SUPT_0358 vs SUPT_0393 ambiguity; the Calb1 discordance at SUPT_0393.
- **What:** MapMyCells annotation transfer of published BNST scRNA-seq with Crh+ subset annotations onto WMBv1.
  **Target:** F1 ≥ 0.60 at SUPERTYPE level; expected split between SUPT_0358 and SUPT_0393.
  **Expected output:** `AnnotationTransferEvidence` on both edges.
  **Resolves:** Q2 — which supertype (or both) captures the classical BNST-CRF population at transcriptomic level.
- **What:** Per-child-cluster query of precomputed expression for Calb1 across SUPT_0393 children.
  **Target:** identify any child cluster with Calb1 < 1.0 and Crh > 5.0.
  **Expected output:** refined `MappingEdge` at CLUSTER level with `AtlasMetadata` evidence.
  **Resolves:** Q3 — whether SUPT_0393 can be rescued at child-cluster resolution.

### Open questions

1. What fraction of SUPT_0358 cells co-express Esr1 and Crh? ISH or scRNA-seq for Crh+/Esr1+ overlap in BST would resolve this.
2. Is SUPT_0393 (high Crh) or SUPT_0358 (Esr1+ proxy) the better mapping for the sexually dimorphic anterolateral BST CRF+ population? (depends on Q1)
3. Do individual clusters under SUPT_0393 segregate into Calb1-high and Calb1-low populations? A Calb1-low, Crh-high child cluster would support confidence upgrade.
4. Does SUPT_0393 show female-biased sex ratio consistent with bnst_crf_neuron? Per-child-cluster MFR query needed; the SUPT_0358 case shows that supertype-level MFR aggregates can hide opposing per-cluster directions.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | https://doi.org/10.3389/fncir.2025.1593443 | — | soma location |
| [2] | [Ide et al. 2013 · PMID:23554470](https://pubmed.ncbi.nlm.nih.gov/23554470) | 23554470 | soma location |
| [3] | [Knoedler et al. 2022 · PMID:35143761](https://pubmed.ncbi.nlm.nih.gov/35143761) | 35143761 | Knoedler 2022 (PMID:35143761) Esr1+ TRAP-seq pooled BNST female-receptive vs VMH |
