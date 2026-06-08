# Ndnf::Nkx2-1-IN (Ndnf-OLM, Chamberland 2024) — WMBv1 Mapping Report
*2026-05-12 · Source: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`*

---

## Introduction

The Ndnf::Nkx2-1-IN subfamily is one of four genetically distinct somatostatin-expressing interneuron groups in the mouse hippocampus described by Chamberland et al. 2024 [1]. Operationally defined by co-expression of *Sst*, *Ndnf*, and the MGE transcription factor *Nkx2-1*, these cells are reported to be oriens-lacunosum-moleculare-like and to selectively target CA1 pyramidal cells, distinguishing them from the bistratified *Sst::Tac1* subfamily which targets fast-spiking interneurons.

> hippocampal somatostatin-expressing interneurons (Sst-INs) can be divided into at least four subfamilies, each with distinct functions
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_53fb33cc -->

> the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c084d5c0 -->

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | [1] |
| NT | GABAergic | [1] |
| Defining markers | Sst, Ndnf, Nkx2-1 | [1] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 stratum oriens, depth-graded within O/A · [1]
  > While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
  > — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->
- **Defining markers (Sst, Ndnf, Nkx2-1):** intersectional genetic targeting of the subfamily · [1]
  > the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c084d5c0 -->
- **Subfamily framing:** four-way classification of hippocampal Sst-INs · [1]
  > genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

No single WMBv1 cluster or supertype cleanly captures the Ndnf::Nkx2-1-IN subfamily: the annotation-transfer signal fragments across Lamp5, Sncg, and Sst types with F1 below 0.1 at every taxonomy level [1], and the candidates that score best on individual properties (location vs. Nkx2-1 expression vs. *Sst*/*Ndnf* expression) are mutually inconsistent. The mapping is reported as UNCERTAIN; the following candidates are the strongest partial matches.

![Filtered AT figure for Ndnf::Nkx2-1-IN](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Chamberland per-cluster Ndnf subfamily source group (n=19 cells from a single qualifying Harris Class). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution; here all targets sit far below that line. The fragmentation is consistent with the small, dropout-affected source pool noted by the run record.*

### 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🔴 LOW

**Supporting evidence:**
- *Nkx2-1* expression CONSISTENT at this supertype (val=1.85; cohort percentile 0.984; child-cluster coverage 0.750), the strongest signal for the MGE/Nkx2-1 axis among assessed candidates [A].
- *Sst* CONSISTENT (val=1.52; cohort percentile 0.603; child coverage 1.000) and *Ndnf* CONSISTENT (val=1.32; cohort percentile 0.873; child coverage 1.000) — all three defining markers detected across the supertype's children.
- Atlas metadata place a substantial fraction of the supertype's painted cells in Hippocampal formation [MBA:1089] (count_100um=3175) with smaller fractions in Dentate gyrus [MBA:726] and Field CA3 [MBA:463].

**Marker evidence provenance:**
- The classical defining-markers list (Sst, Ndnf, Nkx2-1) does not include *Lamp5*, but the supertype's name foregrounds *Lamp5* — *(note: the concordance asserted here is on Nkx2-1 + Sst + Ndnf, not on Lamp5; the supertype's Lamp5 identity is supplementary context rather than confirming evidence)*.
- All three Chamberland defining markers come from a single primary citation [1] grounded in intersectional genetic targeting — the *Nkx2-1* axis specifically is the strongest discriminator and is highest at this supertype among all assessed candidates.

**Concerns:**
- Location APPROXIMATE — `region_fraction_100um: 0.114`; the supertype's strict in-region fraction is 0.050, and Dentate gyrus and Field CA3 dominate the off-target painted counts rather than CA1 stratum oriens specifically *(note: Dentate gyrus and CA3 are within the broader hippocampal formation but anatomically distinct from CA1 O/A — the location is hippocampal but not the classical type's specific compartment)*.
- Annotation transfer does not concentrate on this supertype: the Chamberland per-cluster Ndnf source group's best supertype is 0199 Lamp5 Gaba_1 with F1=0.055, not 0203 [1].

*(2 of 3 child clusters show Nkx2-1 concordance with classical type at child-cluster coverage 0.750; *Sst* and *Ndnf* show full child-cluster coverage 1.000. Best child-cluster candidates with strongest Nkx2-1: 0724 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0724] (Nkx2-1=2.99) and 0725 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0725] (Nkx2-1=5.05).)*

**What would upgrade confidence:**
- A targeted Ndnf::Nkx2-1 intersectional patch-seq or Cre-line scRNA-seq dataset run through MapMyCells against WMBv1 at F1 ≥ 0.50 at SUPERTYPE level would be the direct discriminator between this Lamp5 Lhx6 supertype and the Sst Gaba_3 territory; the present AT run cannot adjudicate.
- Spatial registration that distinguishes CA1 O/A from Dentate gyrus / CA3 painted cells within the supertype.

### 0767 Sst Gaba_3 [CS20230722_CLUS_0767] · 🔴 LOW

**Supporting evidence:**
- Location CONSISTENT — `region_fraction_100um: 0.578`, with Hippocampal formation [MBA:1089] the top painted region (count_100um=164); the strict in-region fraction is 0.422. Highest hippocampal-proximity among assessed candidates [A].
- *Sst* CONSISTENT (val=10.78; cohort percentile 0.832; atlas category NEUROPEPTIDE) — high expression at the level expected of a *Sst*-INs subfamily.
- *Ndnf* CONSISTENT (val=1.03; cohort percentile 0.832) and *Nkx2-1* CONSISTENT (val=0.17; cohort percentile 0.874) — Nkx2-1 is at low absolute level but above the MIN_DETECTABLE threshold and ranks high within the cohort.

**Marker evidence provenance:**
- *Sst* is listed as a NEUROPEPTIDE marker in atlas metadata at this cluster; absolute value 10.78 confirms strong expression at transcript level — no annotation/expression discrepancy.
- *Nkx2-1* at val=0.17 is detectable but low in absolute terms; the cohort percentile (0.874) is high because most cohort members express *Nkx2-1* even more sparsely. Treat the Nkx2-1 evidence here as weaker than at the Lamp5 Lhx6 candidates above.

**Concerns:**
- AT signal: the Chamberland per-cluster Ndnf source group does NOT concentrate on this cluster; F1 at cluster level is below 0.1 across all targets [1] *(note: cluster 0767 sits within the 0216 Sst Gaba_3 supertype which is where AT scatter accumulates, but the F1 signal is not strong enough to support a clean mapping here)*.
- The cluster's *Nkx2-1* expression is low in absolute terms, weakening the MGE/Nkx2-1 axis that Chamberland 2024 used to define the subfamily [1].

*(All three markers CONSISTENT at this single cluster; child-cluster breakdown not applicable at cluster level.)*

**What would upgrade confidence:**
- Targeted Ndnf::Nkx2-1 patch-seq with morphology recovery (OLM dendrites + axonal arborisation in stratum lacunosum-moleculare) mapped to WMBv1 at F1 ≥ 0.50 at CLUSTER level would test whether OLM-like Ndnf::Nkx2-1 cells co-cluster with 0767.
- Re-analysis of Chamberland 2024's published Ndnf::Nkx2-1 intersectional scRNA-seq (if available) under cluster-level MapMyCells.

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🔴 LOW

**Supporting evidence:**
- *Sst* CONSISTENT (val=11.44; cohort percentile 0.905; child-cluster coverage 1.000) and *Ndnf* CONSISTENT (val=1.64; cohort percentile 0.889; child coverage 0.889) — both expression markers strongly support a Sst Gaba_3 reading at supertype level.
- Location CONSISTENT — `region_fraction_100um: 0.539`; the supertype's painted-cell counts are dominated by Hippocampal formation [MBA:1089] (count_100um=2145), Field CA1 [MBA:382] (count_100um=1559), and Field CA1, stratum oriens [MBA:399] (count_100um=1463) — the only supertype where the classical compartment dominates the location signal.
- Annotation transfer narrative on this edge: the Chamberland per-cluster Ndnf source group (n=19 cells in this Harris re-labelling) does not concentrate at any single WMBv1 cluster or supertype — signal is fragmented across Lamp5, Sncg, and Sst types with F1 below 0.1 everywhere; the per-cluster Ndnf threshold qualified only one Harris Class, so the source pool is small and noisy [1].

**Concerns:**
- *Nkx2-1* DISCORDANT (val=0.04; below MIN_DETECTABLE 0.1; cohort percentile 0.714) — the MGE/Nkx2-1 axis that defines the subfamily fails at this supertype. Among the three defining markers, this is the most diagnostic discriminator for the Ndnf::Nkx2-1 vs. other Sst-IN subfamilies distinction.
- Distributed AT signal across many WMBv1 supertypes — no single target captures the source population [1].

*(2 of 3 markers CONSISTENT at supertype level; *Nkx2-1* DISCORDANT is the decisive contradiction. Best child-cluster candidate within the supertype on location is 0767, narrated above.)*

**What would upgrade confidence:**
- Targeted Ndnf::Nkx2-1 intersectional scRNA-seq or patch-seq mapped to WMBv1 at F1 ≥ 0.50 at SUPERTYPE level — would directly test whether the marker-discordant Nkx2-1 signal is real or a thresholding artefact of the small Harris-relabel pool.
- Cluster-level breakdown of *Nkx2-1* expression within the Sst Gaba_3 children to test whether a minority of children carry the MGE/Nkx2-1 signal (HIDDEN-1:1 pattern).

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] | — | 8913 | 🔴 LOW | Nkx2-1 CONSISTENT high; location APPROXIMATE | Primary (Nkx2-1 axis) |
| 0767 Sst Gaba_3 [CS20230722_CLUS_0767] | 0216 Sst Gaba_3 | 104 | 🔴 LOW | Location CONSISTENT; all 3 markers CONSISTENT | Secondary (region) |
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2004 | 🔴 LOW | Sst/Ndnf high; Nkx2-1 DISCORDANT; AT scatter | Supports broader Sst Gaba_3 mapping |
| 0724 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0724] | 0203 Lamp5 Lhx6 Gaba_1 | 2443 | ⚪ UNCERTAIN | Nkx2-1 CONSISTENT high; Sst APPROXIMATE | Eliminated (Sst APPROXIMATE) |
| 0725 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0725] | 0203 Lamp5 Lhx6 Gaba_1 | 212 | ⚪ UNCERTAIN | Nkx2-1 highest; Sst APPROXIMATE | Eliminated (Sst APPROXIMATE) |
| 0726 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0726] | 0203 Lamp5 Lhx6 Gaba_1 | 4464 | 🔴 LOW | Markers CONSISTENT; location DISCORDANT (DG) | Eliminated (Dentate gyrus location) |
| 0730 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0730] | 0203 Lamp5 Lhx6 Gaba_1 | 112 | 🔴 LOW | Nkx2-1 DEFINING_SCOPED; location DISCORDANT (CA3) | Eliminated (CA3 location) |
| 0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204] | — | 3470 | 🔴 LOW | Nkx2-1 CONSISTENT; location DISCORDANT | Eliminated (isocortex/chandelier) |
| 0230 Sst Gaba_17 [CS20230722_SUPT_0230] | — | 956 | 🔴 LOW | Sst CONSISTENT; location DISCORDANT | Eliminated (cortical subplate) |
| 0233 STR Prox1 Lhx6 Gaba_1 [CS20230722_SUPT_0233] | — | 630 | 🔴 LOW | Markers CONSISTENT; location DISCORDANT | Eliminated (striatum) |
| 0215 Sst Gaba_2 [CS20230722_SUPT_0215] | — | 1183 | 🔴 LOW | Sst CONSISTENT; location DISCORDANT | Eliminated (olfactory/piriform) |

Total: 11 candidate edges (`evidencell:UncertainRelationship`).

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Ndnf::Nkx2-1-IN subfamily is defined by co-expression of *Sst*, *Ndnf*, and the MGE-lineage transcription factor *Nkx2-1*, with soma in CA1 stratum oriens [UBERON:0005371] and GABAergic neurotransmission [1]. Definition basis: CLASSICAL_MULTIMODAL.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Ndnf — Chamberland per-cluster subfamily label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100). Same MapMyCells run as at_run_20260512_harris_class_mmc_wmbv1; this record re-aggregates the shared mmc_results.csv under the Chamberland subfamily label scheme via class_to_subfamily.tsv. F1 scoring with bootstrap_threshold=0.8 default. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| Script (external) | ../at_run_20260506_harris_chamberland_mmc_wmbv1/README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_chamberland_by_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/f1_matrix_chamberland_by_class.csv) |
| Caveats | Per-cluster derivation is dropout-robust; per-cell derivation is subject to dropout on gene-pair markers. Ndnf::Nkx2-1-OLM not cleanly resolved — only one Harris Class qualified at the per-cluster Ndnf threshold. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:46+00:00 from [kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml](kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ndnf_nkx2_1_olm_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0724 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0725 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0767 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0726 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0730 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0203 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0204 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0230 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0233 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0215 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Ndnf::Nkx2-1-IN (Ndnf-OLM, Chamberland 2024) → no clean WMBv1 target at LOW confidence. The three competing partial matches are 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] (best on *Nkx2-1*), 0767 Sst Gaba_3 [CS20230722_CLUS_0767] (best on hippocampal CA1 stratum oriens location), and 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (best on *Sst*/*Ndnf* expression and the only candidate with annotation-transfer evidence). Key support: marker comparison and atlas spatial metadata. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (the small Harris-relabel pool yields F1 < 0.1 across all targets) and a fundamental Nkx2-1 vs. location trade-off — the marker axis points to Lamp5 Lhx6 cortical-leaning targets, the location axis points to Sst Gaba_3 hippocampal targets, and no single candidate satisfies both.

No Cell Ontology term currently assigned. Candidate for CL contribution as a new term for the Chamberland Ndnf::Nkx2-1-OLM subfamily once a clean WMBv1 anchor is obtained.

### Proposed experiments and follow-ups

**Targeted Ndnf::Nkx2-1 intersectional scRNA-seq or patch-seq.**
- **What:** Intersectional Ndnf;;Nkx2-1 Cre/Flp targeting of CA1 stratum oriens, scRNA-seq or patch-seq with morphology recovery (OLM dendrites in stratum oriens + axons in stratum lacunosum-moleculare).
- **Target:** F1 ≥ 0.50 at SUPERTYPE level (cluster-level F1 ≥ 0.50 would be preferred).
- **Expected output:** AnnotationTransferEvidence on the Ndnf::Nkx2-1-IN node mapped to WMBv1 via MapMyCells.
- **Resolves:** Resolves the Lamp5 Lhx6 vs. Sst Gaba_3 ambiguity by directly placing morphology-verified Ndnf::Nkx2-1-OLM cells on WMBv1; would also discriminate whether Nkx2-1=0.04 at SUPT_0216 is a real subfamily-discordant signal or a sampling artefact.
  *(Cross-check vs. completed work: the present AT run [1] was scored on Harris-class-relabelled cells, not on Chamberland's own intersectional dataset; a direct re-mapping of Chamberland's published Ndnf::Nkx2-1 cells if/when available would be a less expensive alternative starting point.)*

**Cluster-level *Nkx2-1* breakdown within Sst Gaba_3 children.**
- **What:** Per-cluster *Nkx2-1* expression survey across all 0216 Sst Gaba_3 children to test for HIDDEN-1:1 minority signal.
- **Target:** Identify any child cluster with *Nkx2-1* ≥ MIN_DETECTABLE (0.1).
- **Expected output:** Property-comparison refinements on CLUS-level edges.
- **Resolves:** Whether the Nkx2-1 DISCORDANT call at SUPT_0216 masks a minority of Nkx2-1+ children.

### Open questions

1. Is the *Nkx2-1* axis required for the Chamberland subfamily definition, or is it a graded continuum across hippocampal Sst-INs? The atlas-side cohort percentile of 0.714 at SUPT_0216 suggests Nkx2-1 is not zero across Sst Gaba_3 children even though the supertype mean falls below MIN_DETECTABLE.
2. Does Chamberland 2024 [1] have published per-cell Ndnf::Nkx2-1 intersectional scRNA-seq that could be re-mapped directly to WMBv1 without new wet-lab experiments?
3. Whether the depth gradient within CA1 O/A reported by Chamberland 2024 maps to a transcriptomic gradient within hippocampal Sst Gaba_3 / Lamp5 Lhx6 territories or is independent of the WMBv1 cluster structure.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 · PMID:[38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | 38640347 | soma location, defining markers, NT type, subfamily framing, AT evidence run record |

---

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:NEXT] Sst (val=11.44; cohort_pct 0.905) and Ndnf (val=1.64;
    cohort_pct 0.889) CONSISTENT at CS20230722_SUPT_0216, with region
    CONSISTENT (region_fraction_100um: 0.539; Field CA1, stratum oriens
    dominant). Nkx2-1 DISCORDANT (val=0.04, below MIN_DETECTABLE 0.1)
    breaks the MGE/Nkx2-1 axis defining the subfamily, and AT signal in
    at_run_20260512_chamberland_subfamily_mmc_wmbv1 is fragmented
    (best SUPERTYPE F1=0.06 at 0199 Lamp5 Gaba_1; cluster-level scatter
    across many targets). 2 of 3 markers CONSISTENT.
  reconciliation_note: >
    Sst/Ndnf/location point here; Nkx2-1 axis points to CS20230722_SUPT_0203
    (Lamp5 Lhx6 Gaba_1). The mapping is unresolved between Sst Gaba_3
    (region + Sst/Ndnf) and Lamp5 Lhx6 (Nkx2-1 marker). Predicate left
    uncertain pending targeted Ndnf::Nkx2-1 transcriptomic profiling.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        AT signal in at_run_20260512_chamberland_subfamily_mmc_wmbv1
        fragments across Lamp5, Sncg, and Sst types with all targets
        F1 < 0.1; the Chamberland per-cluster Ndnf source pool (n=19)
        is too small and noisy to support a confident assignment.
    - caveat_type: OTHER
      description: >
        Nkx2-1 DISCORDANT at CS20230722_SUPT_0216 (val=0.04, below
        MIN_DETECTABLE) breaks the subfamily-defining MGE/Nkx2-1 marker
        from Chamberland 2024.
  proposed_experiments:
    - >
      Targeted Ndnf::Nkx2-1 intersectional transcriptomic profiling,
      transferred onto WMBv1 at F1 >= 0.50 at SUPERTYPE level, to
      discriminate CS20230722_SUPT_0216 from competing Lamp5 Lhx6
      supertype candidates.
    - >
      Cluster-level Nkx2-1 expression survey across CS20230722_SUPT_0216
      children to test for HIDDEN-1:1 minority Nkx2-1+ signal masked at
      supertype mean.
  unresolved_questions:
    - >
      Is the Nkx2-1 axis a binary subfamily discriminator or a graded
      continuum within hippocampal Sst Gaba_3?
    - >
      Does Chamberland 2024 publish per-cell Ndnf::Nkx2-1 intersectional
      scRNA-seq that could be re-mapped directly to WMBv1?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0724 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  rationale: >
    [tier:CUT] Nkx2-1 CONSISTENT (val=2.99; cohort_pct 0.966) at
    CS20230722_CLUS_0724, but Sst APPROXIMATE (val=1.18; cohort_pct 0.479)
    and Ndnf APPROXIMATE (val=0.17; cohort_pct 0.471) — the Sst-IN
    subfamily defining marker is only weakly expressed. Location
    APPROXIMATE (region_fraction_100um: 0.158) with substantial Isocortex
    and lateral forebrain bundle off-target painted counts.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0725 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  rationale: >
    [tier:CUT] Nkx2-1 CONSISTENT (val=5.05; cohort_pct 0.992; highest among
    candidates) and Ndnf CONSISTENT at CS20230722_CLUS_0725, but Sst
    APPROXIMATE (val=1.05; cohort_pct 0.403). Location APPROXIMATE
    (region_fraction_100um: 0.159) with Field CA1, stratum radiatum
    dominant rather than stratum oriens.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0767 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:STRONGEST] All three defining markers CONSISTENT at
    CS20230722_CLUS_0767 (Sst val=10.78 cohort_pct 0.832; Ndnf val=1.03
    cohort_pct 0.832; Nkx2-1 val=0.17 cohort_pct 0.874) and location
    CONSISTENT (region_fraction_100um: 0.578; Hippocampal formation
    dominant). 3 of 3 markers CONSISTENT. No annotation-transfer evidence
    is recorded on this edge, so the relationship cannot be committed
    beyond the structural-signal match.
  reconciliation_note: >
    Best-region candidate within the Sst Gaba_3 territory; competes with a
    Lamp5 Lhx6 candidate on the Nkx2-1 axis where 0767 expresses Nkx2-1
    only weakly in absolute terms (val=0.17). Predicate left uncertain
    pending direct AT evidence on this edge.
  caveats:
    - caveat_type: OTHER
      description: >
        Nkx2-1 val=0.17 at CS20230722_CLUS_0767 is just above MIN_DETECTABLE;
        the MGE/Nkx2-1 axis is weaker here than at Lamp5 Lhx6 candidates,
        even though the cohort percentile (0.874) is high.
  proposed_experiments:
    - >
      Targeted Ndnf::Nkx2-1 intersectional transcriptomic profiling
      transferred onto WMBv1 at F1 >= 0.50 at CLUSTER level to
      test whether OLM-like Ndnf::Nkx2-1 cells co-cluster with
      CS20230722_CLUS_0767.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0726 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] All three markers CONSISTENT at CS20230722_CLUS_0726
    (Sst val=1.38; Ndnf val=0.89; Nkx2-1 val=3.90 cohort_pct 0.983) but
    location DISCORDANT (region_fraction_100um: 0.088; Dentate gyrus
    [MBA:726] dominant rather than CA1 stratum oriens).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_CLUS_0730 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] All three markers CONSISTENT at CS20230722_CLUS_0730
    (Sst val=1.39; Ndnf val=0.52; Nkx2-1 val=2.08 cohort_pct 0.958 atlas
    category DEFINING_SCOPED) but location DISCORDANT
    (region_fraction_100um: 0.063; Field CA3 pyramidal layer dominant
    rather than CA1 stratum oriens).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0203 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:STRONGEST] Nkx2-1 CONSISTENT (val=1.85; cohort_pct 0.984;
    child-cluster coverage 0.750) at CS20230722_SUPT_0203 — strongest
    MGE/Nkx2-1 axis among assessed candidates. Sst CONSISTENT (val=1.52;
    cohort_pct 0.603; child coverage 1.000) and Ndnf CONSISTENT (val=1.32;
    cohort_pct 0.873; child coverage 1.000). 3 of 3 markers CONSISTENT.
    Location APPROXIMATE (region_fraction_100um: 0.114; Hippocampal
    formation dominant in absolute counts but with Dentate gyrus and
    Field CA3 also contributing). No annotation-transfer evidence is
    recorded on this edge.
  reconciliation_note: >
    Best-Nkx2-1 candidate; competes with a Sst Gaba_3 supertype which
    leads on Sst/Ndnf expression and Field CA1, stratum oriens location.
    Predicate left uncertain pending direct AT evidence from a
    Ndnf::Nkx2-1 intersectional dataset.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Location APPROXIMATE with Dentate gyrus and Field CA3 contributing
        substantial off-target painted counts beyond CA1 stratum oriens;
        region_fraction_100um: 0.114 is in the boundary band.
  proposed_experiments:
    - >
      Targeted Ndnf::Nkx2-1 intersectional transcriptomic profiling,
      transferred onto WMBv1 at F1 >= 0.50 at SUPERTYPE level, to
      discriminate CS20230722_SUPT_0203 from competing Sst Gaba_3
      supertype candidates.
  unresolved_questions:
    - >
      Whether the depth gradient within CA1 O/A reported by Chamberland
      2024 maps to a transcriptomic gradient within Lamp5 Lhx6 vs. Sst
      Gaba_3 territories.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0204 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Nkx2-1 CONSISTENT (val=1.76; cohort_pct 0.968) at
    CS20230722_SUPT_0204 but Sst APPROXIMATE (val=0.95; cohort_pct 0.413)
    and Ndnf APPROXIMATE (val=0.17; cohort_pct 0.492). Location DISCORDANT
    (region_fraction_100um: 0.065; Isocortex dominant). This is the Pvalb
    chandelier supertype — wrong subclass for an OLM-like Sst-IN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0230 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Sst CONSISTENT (val=6.13; cohort_pct 0.746) and Nkx2-1
    CONSISTENT (val=1.17; cohort_pct 0.952) at CS20230722_SUPT_0230, but
    Ndnf APPROXIMATE (val=0.14; cohort_pct 0.429; child-cluster coverage
    0.333; HIDDEN-1:1 signal noted). Location DISCORDANT
    (region_fraction_100um: 0.055; Cortical subplate dominant rather than
    hippocampus).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0233 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] All three markers CONSISTENT at CS20230722_SUPT_0233
    (Sst val=3.22; Ndnf val=0.57; Nkx2-1 val=0.75) but location DISCORDANT
    (region_fraction_100um: 0.025; Striatum dominant). Wrong region for a
    hippocampal CA1 stratum oriens subfamily.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ndnf_nkx2_1_olm_subfamily_chamberland_to_CS20230722_SUPT_0215 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Sst CONSISTENT (val=11.32; cohort_pct 0.873) and Nkx2-1
    CONSISTENT (val=0.67; cohort_pct 0.905) and Ndnf CONSISTENT (val=0.19;
    cohort_pct 0.524) at CS20230722_SUPT_0215, but location DISCORDANT
    (region_fraction_100um: 0.024; Olfactory areas and Piriform area
    dominant). Wrong region for a hippocampal subfamily.
```
<!-- verdict-block-end -->
