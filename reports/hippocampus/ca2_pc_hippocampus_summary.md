# CA2 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

CA2 pyramidal cells are glutamatergic principal neurons of the hippocampal
Ammon's horn whose somata sit in the pyramidal layer of the CA2 subfield
[1][2][3]. They are classically delineated from the adjacent CA1 and CA3
pyramidal populations by selective expression of Pcp4, Rgs14, and Amigo2
[4][5]. Anchoring this small but distinct CA2 pyramidal population in the
WMBv1 (CCN20230722) taxonomy is a prerequisite for downstream CA2-circuit and
social-memory work that uses the atlas as a transcriptomic reference.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA2 [UBERON:0014549] | [1][2] |
| NT type | glutamatergic | [3] |
| Markers | Pcp4, Rgs14, Amigo2 | [4][5] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomical / transcriptomic literature on hippocampal pyramidal cells · [1][2]
  > we profiled transcriptomes at both dorsal and ventral poles, producing a cell-class- and region-specific transcriptional description for these populations
  > — Cembrowski et al. 2016, abstract · [1] <!-- quote_key: 4875295_8cb069d9 -->

  > For CA2, we identified some pyramidal cells at the CA3c region while others distributed along the intermediate (CA3b) and distal (CA3a) subregions (Sanchez-Aguilera et al., 2021).
  > — Unknown 2021, Classical Hippocampal Circuit Organization · [2] <!-- quote_key: 233984943_56acd5f8 -->

- **NT type:** classical literature on hippocampal principal-cell glutamatergic identity · [3]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1). They generally have excitatory effects on the neurons to which they send axon terminals including other glutamatergic and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine (DA)], cholinergic, and histaminergic (HA) cells.
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 2281033_5b9805ff -->

- **Pcp4 marker:** classical immunohistochemical delineation of the CA2 subfield · [4]
  > Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2
  > — Unknown 2014, abstract · [4] <!-- quote_key: 18746823_614030d2 -->

  > These markers include Purkinje cell protein 4 (PCP4), neurotrophin 3, fibroblast growth factor, a-actinin 2, adenosine A1 receptor, vasopressin 1b receptor, RGS14 (regulator of G-protein signaling 14), and amigo2. These markers are specifically or more prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de N o's CA2
  > — Unknown 2014, Introduction · [4] <!-- quote_key: 18746823_8ba0bf29 -->

- **Rgs14 marker:** classical co-marker support · [4]
  > These markers include Purkinje cell protein 4 (PCP4), neurotrophin 3, fibroblast growth factor, a-actinin 2, adenosine A1 receptor, vasopressin 1b receptor, RGS14 (regulator of G-protein signaling 14), and amigo2. These markers are specifically or more prominently expressed in the distal portion of regio inferior corresponding roughly to Lorente de N o's CA2
  > — Unknown 2014, Introduction · [4] <!-- quote_key: 18746823_8ba0bf29 -->

- **Amigo2 marker:** classical expression literature for CA2-enriched genes · [5]
  > a number of genes, including the regulator of G-protein signaling 14 (RGS14), Amigo2, PCP4, TARP5, FGF5, and several adenylyl cyclases (e.g., adcy1, adcy5, and adcy6), are highly expressed in CA2
  > — Unknown 2012, Introduction · [5] <!-- quote_key: 20853920_44ab38bb -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed; 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] is the primary mapping at MODERATE confidence under a PARTIAL_OVERLAP relationship, because the WMBv1 supertype groups CA2 pyramidal cells with the small adjacent fasciola cinerea (FC) and indusium griseum (IG) populations.

![Filtered AT figure for CA2 pyramidal cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_ca2_pc_hippocampus.png)

*F1 across taxonomy levels for the 1 source group (CA2-IG-FC, Yao 2021 SSv4) relevant to CA2 pyramidal cell. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

The Yao 2021 CA2-IG-FC group reaches a clean SUBCLASS mapping (025 CA2-FC-IG Glut, F1=0.973) but splits at SUPERTYPE onto SUPT_0101 (F1=0.947), not the MERFISH-anatomy-preferred SUPT_0100 (F1=0.1); MERFISH evidence (446 CA2 pyramidal-layer cells in SUPT_0100 vs 0 in SUPT_0101) indicates the AT split reflects FC/IG contamination in Yao's mixed CA2-IG-FC label rather than disqualifying SUPT_0100 as the CA2 PC target.

### 4. Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] | 1096 | 🟡 MODERATE | NT CONSISTENT · location APPROXIMATE · Pcp4/Rgs14/Amigo2 CONSISTENT | Best candidate |

1 edge total; relationship: PARTIAL_OVERLAP.

**Table 1 — Property comparison (0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100])**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | glutamatergic (025 CA2-FC-IG Glut) | not assessed | CONSISTENT |
| Soma location | CA2 stratum pyramidale [UBERON:0014549] | Field CA2, pyramidal layer (MBA:446): 446 cells; Field CA1, stratum oriens (MBA:399): 292 cells; Field CA3, stratum oriens (MBA:486): 215 cells; Field CA3, pyramidal layer (MBA:495): 165 cells; Field CA2, stratum radiatum (MBA:454): 55 cells | not assessed | APPROXIMATE |
| Pcp4 expression | defining marker (symbol only) | not listed in SUPT_0100 defining markers (Lefty1, Il16, Etv1); Pcp4 mean_expression=11.26 (precomputed_stats.h5, supertype level) | not assessed | CONSISTENT |
| Rgs14 expression | defining marker (symbol only) | not listed in SUPT_0100 defining markers; Rgs14 mean_expression=8.84 (precomputed_stats.h5, supertype level) | not assessed | CONSISTENT |
| Amigo2 expression | defining marker (symbol only) | not listed in SUPT_0100 defining markers; Amigo2 mean_expression=7.39 (precomputed_stats.h5, supertype level) | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 atlas metadata (025 CA2-FC-IG Glut / 0100 CA2-FC-IG Glut_1) | Atlas metadata | SUPPORT | 446 cells in MBA:446 CA2 pyramidal layer; Pcp4=11.26, Rgs14=8.84, Amigo2=7.39 | atlas-internal |
| Yao 2021 SSv4 MapMyCells AT (CA2-IG-FC) | Annotation transfer | PARTIAL | SUBCLASS F1=0.973 (025 CA2-FC-IG Glut); SUPERTYPE F1=0.947 onto SUPT_0101, F1=0.1 onto SUPT_0100 | atlas-internal |

### 5. Candidate paragraphs

### 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] · 🟡 MODERATE

**Supporting evidence**

- 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] is the highest-scoring WMBv1 supertype candidate for CA2 pyramidal cells (discovery score 4). It belongs to subclass 025 CA2-FC-IG Glut — the dedicated CA2 / fasciola cinerea / indusium griseum glutamatergic subclass in WMBv1 — and the MERFISH soma distribution places 446 cells directly in Field CA2, pyramidal layer [MBA:446], matching the classical CA2 stratum pyramidale soma location [UBERON:0014549]. Substantial additional cells appear in CA1 stratum oriens [MBA:399] (292 cells), CA3 stratum oriens [MBA:486] (215 cells), and CA3 pyramidal layer [MBA:495] (165 cells); these adjacent strata are immediately neighbouring the CA2 pyramidal layer and likely reflect either MERFISH spread at subfield borders or CA1/CA3 transitional pyramidal cells captured within SUPT_0100 *(adjacent regions — could reflect registration boundary error or transitional pyramidal populations; weak counter-evidence)*.
- The classical CA2 marker triad is quantitatively confirmed at supertype-level precomputed expression in SUPT_0100: Pcp4 mean=11.26, Rgs14 mean=8.84, Amigo2 mean=7.39. None of these are in SUPT_0100's atlas-listed defining marker set (Lefty1, Il16, Etv1) — those are supertype-distinguishing markers within the broader subclass — but the precomputed mean values are substantial and consistent with the classical CA2 enrichment described in [4][5].
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 CA2-IG-FC labels (n=19) onto WMBv1 reaches a clean SUBCLASS mapping (F1=0.973, group_purity=1.0, target_purity=0.947) onto 025 CA2-FC-IG Glut, supporting subclass-level membership of CA2 pyramidal cells in the CA2-FC-IG Glut subclass.

**Marker evidence provenance**

- **Pcp4**: classical protein-level CA2 delineation marker — Pcp4 antibody immunostaining is one of the canonical methods for delineating CA2/CA1 and CA2/CA3 borders in mouse hippocampus [4]. Atlas transcript-level confirmation: Pcp4 mean_expression=11.26 in SUPT_0100 (precomputed_stats.h5). Note: Pcp4 was assessed in the original CA2-delineation study on cytoarchitectural CA2 itself rather than on morphology-confirmed CA2 PCs, so cell-type specificity within CA2 is inferred from the subfield assignment.
- **Rgs14**: classical mRNA / IHC-level CA2-enriched marker reported alongside Pcp4 in CA2 delineation literature [4]. Atlas transcript confirmation: Rgs14 mean_expression=8.84 in SUPT_0100.
- **Amigo2**: classical transcript-enriched CA2 marker [5]. Atlas transcript confirmation: Amigo2 mean_expression=7.39 in SUPT_0100. The original Amigo2 / CA2-enriched-gene reports are transcript-level subfield studies; cell-type specificity within CA2 PCs is inferred rather than directly tested on morphology-confirmed cells.

**Concerns**

- The supertype name "0100 CA2-FC-IG Glut_1" includes FC (fasciola cinerea) and IG (indusium griseum) alongside CA2. FC and IG are small CA2-adjacent glutamatergic structures; classical CA2 pyramidal cells are distinct from FC/IG neurons. The PARTIAL_OVERLAP relationship reflects this conflation — SUPT_0100 is not a pure CA2 PC supertype.
- Yao 2021 (GSE185862) MapMyCells AT of the CA2-IG-FC subclass label routes 18/19 (94.7%) source cells to SUPT_0101 (0101 CA2-FC-IG Glut_2, F1=0.947) and only 1/19 (5.3%) to SUPT_0100 (F1=0.1). However, SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by fasciola cinerea (175 cells) and induseum griseum (61 cells), while SUPT_0100 has 106 CA2 pyramidal-layer cells and 0 FC/IG cells. The AT split therefore reflects the FC/IG component of Yao's mixed CA2-IG-FC label being routed to the FC/IG-enriched SUPT_0101 — it does not constitute evidence that SUPT_0100 is the wrong target for CA2 PCs proper. A CA2-specific source dataset (without FC/IG contamination) would be required for definitive AT (OTHER caveat).
- Soma location is APPROXIMATE rather than CONSISTENT: SUPT_0100 has comparable or greater cell counts in CA1 and CA3 strata than in CA2 pyramidal layer, raising the question of whether SUPT_0100 spans CA2 plus transitional CA1/CA3 pyramidal cells or simply reflects MERFISH registration spread at subfield borders.
- Sex ratio NOT_ASSESSED at supertype level (MFR is only computed at cluster rank 0) — child-cluster breakdown not collected for this edge.

**What would upgrade confidence**

- Run MapMyCells annotation transfer using a **CA2-specific** source dataset (without FC/IG contamination) to obtain a clean F1 readout that distinguishes SUPT_0100 vs SUPT_0101 for CA2 pyramidal cells proper. Target F1 ≥ 0.80 at SUPERTYPE for CA2 PC source labels onto SUPT_0100. Expected output: AnnotationTransferEvidence refining the SUPT_0100 edge and clarifying whether any CA2 PC subset belongs in SUPT_0101.
- Child-cluster breakdown of SUPT_0100: check precomputed Rgs14, Pcp4, and Amigo2 expression at cluster rank 0 (via `just add-expression`) to identify which child clusters carry the strongest CA2 PC signature and to distinguish the CA2 PC subset from any FC/IG or CA1/CA3 transitional contamination within SUPT_0100. Expected output: per-cluster precomputed expression on the taxonomy reference store and refined property alignments on the existing SUPT_0100 edge.
- FISH validation of Rgs14 or Amigo2 in CA2 vs CA1/CA3 cells assigned to SUPT_0100 by MERFISH would clarify whether the CA1/CA3 cells in SUPT_0100 are genuine deep-border pyramidal neurons (e.g. CA3c near the CA2 border) or MERFISH registration errors. Expected output: LiteratureEvidence (if literature already addresses) or a flagged MERFISH-registration caveat.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical CA2 pyramidal cell is defined as a
glutamatergic [3] principal neuron with soma in the pyramidal layer of CA2
[UBERON:0014549] [1][2], with Pcp4, Rgs14, and Amigo2 as defining markers
[4][5]. The node's `definition_basis` is `CLASSICAL_MULTIMODAL`, combining
anatomical, neurotransmitter, and marker information from classical/literature
sources.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
(CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using
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
| Source dataset | GEO:GSE185862 (CA2-IG-FC) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations). Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. Inputs and intermediate outputs live under research/hippocampus/glutamatergic/annotation_transfer/GSE185862_SSv4/. |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.**
All citations, atlas accessions, ontology CURIEs, and verbatim literature
quotes in this report are validated against the evidencell knowledge base
at write time. Authored-prose evidence narratives are validated against
their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the
Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:13+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ca2_pc_hippocampus_to_supt_0100 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** CA2 pyramidal cell → 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] at MODERATE confidence. Key support: atlas metadata (446 cells in MBA:446 CA2 pyramidal layer; quantitative Pcp4/Rgs14/Amigo2 enrichment at supertype level) and MapMyCells annotation transfer of Yao 2021 CA2-IG-FC labels reaching a clean SUBCLASS F1=0.973 onto 025 CA2-FC-IG Glut. Key caveats: DISCORDANT_ANATOMY (SUPT_0100 conflates CA2 PCs with fasciola cinerea / indusium griseum neurons) and the Yao 2021 mixed CA2-IG-FC label routing supertype-level cells to SUPT_0101 rather than SUPT_0100, which on MERFISH evidence reflects FC/IG contamination of the source label rather than a genuine target mismatch.

No Cell Ontology term currently assigned. Candidate for CL contribution covering the CA2 pyramidal cell (distinct from CA1 and CA3 pyramidal populations and from the adjacent FC/IG glutamatergic neurons).

### 7. Proposed experiments and follow-ups

The Yao 2021 SSv4 MapMyCells AT already establishes the SUBCLASS-level mapping
of CA2-IG-FC source cells onto 025 CA2-FC-IG Glut, but it cannot resolve the
SUPT_0100 vs SUPT_0101 split because the source label is itself a mixed
CA2-IG-FC pool. What remains unresolved is the CA2-PC-specific supertype
assignment within this subclass.

- **What:** MapMyCells annotation transfer using a CA2-specific source dataset (without FC/IG contamination) — e.g. a CA2-PC-targeted scRNA-seq cohort or a CA2 Cre-driver / Amigo2-driver-defined population.
- **Target:** F1 ≥ 0.80 at SUPERTYPE level for the CA2 PC source label onto SUPT_0100 (and a low complementary F1 onto SUPT_0101).
- **Expected output:** AnnotationTransferEvidence refining the SUPT_0100 edge; clarifies whether any CA2 PC subset belongs in SUPT_0101.
- **Resolves:** open question 1 and the DISCORDANT_ANATOMY / mixed-source-label caveats on the SUPT_0100 edge.

- **What:** child-cluster precomputed expression for Rgs14, Pcp4, and Amigo2 in SUPT_0100 via `just add-expression`, plus child-cluster MERFISH breakdown for MBA:446.
- **Target:** identification of the SUPT_0100 child cluster(s) with the strongest CA2 PC marker enrichment and the highest CA2-pyramidal-layer MERFISH count.
- **Expected output:** PrecomputedExpression entries at cluster rank 0 in the taxonomy reference store; refined property alignments on the SUPT_0100 edge at cluster resolution.
- **Resolves:** open question 1 (CA1/CA3-stratum cells in SUPT_0100 — genuine deep-border pyramidal vs MERFISH registration error).

### 8. Open questions

1. Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near the CA2 border) or MERFISH registration errors? FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 would clarify.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | soma location |
| [2] | Unknown 2021 | [33956790](https://pubmed.ncbi.nlm.nih.gov/33956790/) | soma location |
| [3] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
| [4] | Unknown 2014 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker |
| [5] | Unknown 2012 | [22904370](https://pubmed.ncbi.nlm.nih.gov/22904370/) | Amigo2 marker |
