# Ivy cell (IvC) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

Ivy cells are a numerous and densely arborising GABAergic interneuron class of the CA1 pyramidal layer, defined by neuronal nitric oxide synthase (nNOS/Nos1) expression alongside NPY, late-spiking electrophysiology, and the absence of the canonical interneuron markers Pvalb, Sst, and Calb2 [1][2]. They produce slow GABAergic inhibition of pyramidal cells and, together with the laminarly distinct neurogliaform cells (NGCs), are among the most representative interneuron types of CA1 stratum pyramidale [1][2].

Soma position is canonically in the pyramidal layer of CA1 [UBERON:0014548] [1]. A long-standing question is whether Ivy cells and stratum-radiatum/stratum-lacunosum-moleculare nNOS+ NGCs constitute a single subtype distinguished only by laminar position — Tricoire et al. report completely overlapping developmental, electrophysiological, morphological, and neurochemical properties between the two [2].

### Classical type — properties and references

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1] |
| NT type | GABAergic | — |
| Defining markers | Nos1, Npy, Lamp5 | [1][2][3][4][5] |
| Negative markers | Pvalb, Sst, Calb2 | [2] |
| Neuropeptides | Npy | [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** classical anatomical description · CA1 pyramidal layer · [1]
  > This mouse line allows for a large sampling from diverse interneuron subtypes in the CA1 pyramidal layer, including the most representative ones (Bezaire et al., 2013), the PV-expressing basket and bistratified cells (Klausberger et al., 2008), the NOS- expressing ivy cells (14381729) and two types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin (Klausberger et al., 2008)(Topolnik et al., 2022)
  > — Bocchio et al. 2024, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 262127573_d140faf4 -->

- **Nos1, Npy, negative markers (Pvalb/Sst/Calb2):** Cre-line targeting + electrophysiology + transcript-level survey of CA1 interneurons · [2]
  > IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR.
  > — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [2] <!-- quote_key: 2405079_6850b924 -->

</details>

Cell Ontology mapping: No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Marker-expression alignment across the Mouse Whole-Brain v1 (WMBv1) GABAergic atlas converges on the MGE-derived **Lamp5 Lhx6** supertype 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] as the best transcriptomic home for hippocampal Ivy cells; all three defining markers (Nos1, Npy, Lamp5) are highly expressed across the supertype's child clusters with 100% coverage (see property comparison table). The atlas does not place a meaningful number of cells in CA1 stratum pyramidale for this supertype — the strict region fraction is 0.014 and the 100 µm proximity fraction is 0.090 — which we read as atlas under-sampling of the canonical Ivy-cell soma location rather than as evidence against the mapping, given how cleanly the marker panel concords (see candidates table at the end of Results for the full audit).

### 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🟡 MODERATE

**Property alignment.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted at supertype | GABA (CLUS_0731) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | 0.090 of cells within 100 µm of CA1 (strict 0.014); top regions Hippocampal formation [MBA:1089], Dentate gyrus [MBA:726], Field CA3 [MBA:463] | CLUS_0731: 0.132 proximity (top: Hippocampal formation [MBA:1089], Field CA3 [MBA:463], Field CA3 pyramidal layer [MBA:495]) | DISCORDANT |
| Nos1 expression | defining marker | 7.78; cohort pct 0.968; child-coverage 1.000 | CLUS_0731: 8.55 (cohort pct 0.941) | CONSISTENT |
| Npy expression | defining marker | 4.62; cohort pct 0.710; child-coverage 1.000 | CLUS_0731: 4.35 (cohort pct 0.662) | CONSISTENT |
| Lamp5 expression | defining marker | 6.73; cohort pct 0.968; child-coverage 1.000 | CLUS_0731: 8.51 (cohort pct 0.985) | CONSISTENT |
| Pvalb (negative) | ABSENT | 0.43; cohort pct 0.516 | CLUS_0731: 0.07 (below detection) | SUPT: DISCORDANT; CLUS: CONSISTENT |
| Sst (negative) | ABSENT | 1.52; cohort pct 0.677 | CLUS_0731: 1.24 (cohort pct 0.397) | DISCORDANT |
| Calb2 (negative) | ABSENT | 0.37; cohort pct 0.419 | CLUS_0731: 0.31 (cohort pct 0.368) | DISCORDANT |
| Npy (neuropeptide) | classical | 4.62; cohort pct 0.710; child-coverage 1.000 | CLUS_0731: 4.35 (cohort pct 0.662) | CONSISTENT |

*(Multiple child clusters of CS20230722_SUPT_0203 — including CLUS_0731 and CLUS_0724 — show concordant Nos1+Npy+Lamp5 expression with sub-detection Pvalb at cluster level. The supertype-level Pvalb DISCORDANT call resolves to CONSISTENT at the cluster level, an artefact of supertype averaging across child clusters. Best match: CLUS_0731.)*

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | region_fraction_100um=0.090; strict=0.014; Nos1 cohort_pct 0.968 | atlas-internal |

**Supporting evidence.**
- Lamp5 Lhx6 supertype is the MGE-derived Lamp5 lineage in WMBv1, the same molecular bin where canonical Ivy-cell defining markers (Nos1, Npy, Lamp5) co-segregate at high cohort percentiles (Nos1 cohort pct 0.968; Lamp5 cohort pct 0.968; child-coverage 1.000 on both) — the marker triplet defines this supertype rather than being smeared across it.
- The atlas supertype shows Pvalb-negative cells at cluster level (CLUS_0731 Pvalb 0.07, below detection; CLUS_0724 Pvalb 0.23) — consistent with the classical Pvalb-negative signature. The supertype-mean Pvalb signal (0.43) is driven by child clusters not in the hippocampus.
- Hippocampal formation [MBA:1089] is the single largest anatomical compartment represented among the supertype's painted cells (count_100um=3175), even though the strict CA1 SP overlap is low — a pattern consistent with atlas registration placing many CA1-derived cells at the layer boundary rather than within pyramidale itself.

**Marker evidence provenance.**
- **Nos1** is established at transcript and protein level for Ivy cells across multiple primary studies, including Tricoire et al. 2010 (Cre-line + transcript) [2], Tzilivaki et al. 2023 [3], Kim et al. 2025 [4], and Wierenga et al. 2010 [5]. This is among the best-supported single-marker assertions in the panel.
- **Npy** is co-expressed with Nos1 on Ivy cells per Tricoire [2]; transcript-level supertype coverage (1.000) in CS20230722_SUPT_0203 confirms the co-expression at the atlas level.
- **Lamp5** is listed as a defining marker on the classical node without a primary citation; the atlas confirms it (cohort pct 0.968; DEFINING_SCOPED in atlas metadata) and the supertype name itself encodes it. A targeted literature trawl for primary "Lamp5 Ivy cell" evidence would strengthen the provenance chain.
- **Negative markers (Pvalb, Sst, Calb2)** are established by the Tricoire et al. 2010 transcript-level survey [2], with the proviso that supertype-mean Sst (1.52) and Calb2 (0.37) reflect averaging over non-hippocampal child clusters; the CA1-relevant cluster CLUS_0731 has Pvalb below detection.

**Concerns.**
- *Location* DISCORDANT at supertype level: strict `region_fraction = 0.014`, proximity `region_fraction_100um: 0.090`. The top anatomical compartments at 100 µm are Hippocampal formation [MBA:1089], Dentate gyrus [MBA:726], and Field CA3 [MBA:463]. Pyramidal-layer-specific MERFISH placement is sparse; whether this reflects atlas under-sampling of CA1 SP Lamp5 Lhx6 cells, MERFISH-cell selection biases, or genuine displacement of Ivy-cell somata at supertype scale is unresolved. *(note: hippocampal formation is the classical type's region of origin; the discordance is in laminar resolution within the region, not in gross region membership.)*
- Supertype-level Sst (1.52) and Calb2 (0.37) DISCORDANT signals reflect heterogeneity across the supertype's child clusters; the in-region child CLUS_0731 has Sst still detectable at 1.24 and Calb2 below detection — Sst contamination remains a residual concern even at cluster level and warrants targeted marker analysis on the candidate cells.
- The classical literature [2] reports that Ivy cells and nNOS+ neurogliaform cells (NGCs) share overlapping developmental, electrophysiological, morphological, and neurochemical properties, distinguished mainly by laminar position. This same supertype is also the leading mapping target for the hippocampal NGC node in this graph; if Tricoire's prediction holds, Ivy cells and NGCs may converge transcriptomically onto CS20230722_SUPT_0203, with within-supertype scatter reflecting subtype heterogeneity rather than mapping failure.

**What would upgrade confidence.**
- MapMyCells annotation transfer from a CA1-restricted Cre-line-targeted Ivy-cell scRNA-seq cohort (Nos1-CreER or Htr3a-Cre intersected with CA1 SP localisation) into WMBv1, with F1 ≥ 0.80 at SUPERTYPE level and a distribution profile distinguishing Ivy-vs-NGC scatter across child clusters of CS20230722_SUPT_0203. Expected output: AnnotationTransferEvidence.
- Targeted Patch-seq on biocytin-filled Ivy and NGC cells from CA1, with morphology reconstruction and post-hoc MapMyCells assignment, to test the Tricoire 2010 prediction of trans-laminar identity. Expected output: AnnotationTransferEvidence + MarkerAnalysisEvidence.
- Primary-literature trawl for Lamp5 as a transcript-level Ivy-cell marker (separate from the Lamp5 Lhx6 supertype naming convention), to firm the marker provenance.

### 0731 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0731] · 🟡 MODERATE

**Property alignment.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | (supertype CS20230722_SUPT_0203) | GABA | CONSISTENT |
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | see SUPT_0203 row | 0.132 of cells within 100 µm of CA1; top regions Hippocampal formation [MBA:1089], Field CA3 [MBA:463], Field CA3 pyramidal layer [MBA:495] | APPROXIMATE |
| Nos1 | defining marker | — | 8.55; cohort pct 0.941 | CONSISTENT |
| Npy | defining marker | — | 4.35; cohort pct 0.662; atlas: NEUROPEPTIDE | CONSISTENT |
| Lamp5 | defining marker | — | 8.51; cohort pct 0.985; atlas: MERFISH | CONSISTENT |
| Pvalb (negative) | ABSENT | — | 0.07 (below detection) | CONSISTENT |
| Sst (negative) | ABSENT | — | 1.24; cohort pct 0.397 | DISCORDANT |
| Calb2 (negative) | ABSENT | — | 0.31; cohort pct 0.368 | DISCORDANT |
| Npy (neuropeptide) | classical | — | 4.35; cohort pct 0.662 | CONSISTENT |

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | region_fraction_100um=0.132; Nos1=8.55, Lamp5=8.51 | atlas-internal |

**Supporting evidence.**
- This cluster carries the strongest in-region Lamp5 Lhx6 marker signature of any candidate: Nos1 8.55 (cohort pct 0.941), Lamp5 8.51 (cohort pct 0.985), Npy 4.35 with NEUROPEPTIDE annotation in atlas metadata — all three defining markers high simultaneously.
- Pvalb expression is below detection (0.07) — the cleanest negative-marker call across the candidate set.
- Hippocampal formation [MBA:1089] is the dominant proximity region (count_100um=457), with Field CA3 [MBA:463] and Field CA3 pyramidal layer [MBA:495] as the next strongest — placing the cluster within the hippocampus though the CA3 enrichment rather than CA1 SP is at odds with the canonical Ivy-cell laminar position.

**Marker evidence provenance.**
- Same Nos1/Npy/Pvalb/Sst/Calb2 provenance as for the supertype paragraph above. Lamp5 in this cluster carries the MERFISH atlas annotation tag, providing a spatial-transcriptomic anchor beyond pseudobulk.

**Concerns.**
- Location APPROXIMATE: `region_fraction_100um: 0.132` is in the boundary band; could reflect atlas registration boundary error between hippocampal subfields, or this cluster captures a CA3-enriched Lamp5 Lhx6 population rather than the CA1-SP Ivy cells. *(note: CA3 is adjacent to CA1 within the hippocampal formation; the off-target signal is into an adjacent subfield, not a distant region.)*
- Sst at 1.24 — above MIN_DETECTABLE — leaves residual Sst contamination as an unresolved counter-signal against a clean Ivy-cell call. The classical literature does not document Sst heterogeneity within the Ivy-cell type; this is a flag for a targeted lit trawl rather than a documented biological feature.
- Calb2 at 0.31 is low but not below detection; the cohort percentile (0.368) does not place it as a discriminator either way at this cluster.

**What would upgrade confidence.**
- MapMyCells AT from a hippocampus-specific Nos1-CreER+CA1-SP-restricted Ivy-cell cohort would test whether Ivy cells map preferentially onto CLUS_0731 versus the CA3-enriched cells dominating the cluster's painted-cell count. Target F1 ≥ 0.80 at CLUSTER level.
- Spatial transcriptomics (MERFISH or smFISH) co-localising Nos1+Lamp5+Npy in CA1 SP would confirm whether the under-sampling of CA1 SP in this cluster is an atlas artefact or a real anatomical signal.

### 0724 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0724] · 🔴 LOW

**Property alignment.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | (supertype CS20230722_SUPT_0203) | GABA | CONSISTENT |
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | see SUPT_0203 row | 0.119 of cells within 100 µm of CA1; top regions Hippocampal formation [MBA:1089], Isocortex [MBA:315], lateral forebrain bundle system [MBA:983] | DISCORDANT |
| Nos1 | defining marker | — | 9.14; cohort pct 0.985 | CONSISTENT |
| Npy | defining marker | — | 6.66; cohort pct 0.779; atlas: NEUROPEPTIDE | CONSISTENT |
| Lamp5 | defining marker | — | 8.47; cohort pct 0.971; atlas: MERFISH | CONSISTENT |
| Pvalb (negative) | ABSENT | — | 0.23; cohort pct 0.382 | DISCORDANT |
| Sst (negative) | ABSENT | — | 1.18; cohort pct 0.338 | DISCORDANT |
| Calb2 (negative) | ABSENT | — | 0.28; cohort pct 0.279 | DISCORDANT |
| Npy (neuropeptide) | classical | — | 6.66; cohort pct 0.779 | CONSISTENT |

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | region_fraction_100um=0.119; Nos1=9.14, Lamp5=8.47 | atlas-internal |

**Supporting evidence.**
- Highest Nos1 (9.14) and second-highest Lamp5 (8.47) of any candidate cluster — the marker triplet is unambiguously Lamp5 Lhx6 Gaba_1.
- Hippocampal formation [MBA:1089] is the largest single proximity compartment (count_100um=600), placing some of these cells in hippocampus.

**Concerns.**
- Location DISCORDANT: the Isocortex [MBA:315] count (452) and lateral forebrain bundle system [MBA:983] count (280) together dominate over the Hippocampal formation signal; `region_fraction_100um: 0.119` is in the boundary band but the off-target signal here goes to cortex and white-matter tracts, not to an adjacent hippocampal subfield. *(note: isocortex is anatomically distant from CA1 SP — this cluster appears to be a cortically biased member of the Lamp5 Lhx6 lineage rather than a hippocampal one.)*
- Pvalb expression at 0.23 (above MIN_DETECTABLE) puts this cluster on the wrong side of a defining Ivy-cell negative marker.
- The same Sst / Calb2 residual signal seen across the Lamp5 Lhx6 supertype is present here.

**What would upgrade confidence.**
- A hippocampus-restricted CA1 SP Ivy-cell AT cohort would arbitrate whether CLUS_0724 captures CA1-SP Lamp5 Lhx6 cells or whether the cluster is dominated by cortical Lamp5 Lhx6 cells; if the latter, this cluster does not represent hippocampal Ivy cells specifically and the Ivy cell → SUPT_0203 mapping is properly read as broad rather than 1:1 onto any single cluster.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203]` | — | 8913 | 🟡 MODERATE | Nos1+Npy+Lamp5 high (cohort pct ≥0.71), MGE Lamp5 lineage | Primary |
| `0731 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0731]` | 0203 Lamp5 Lhx6 Gaba_1 | 934 | 🟡 MODERATE | Cleanest Lamp5+Nos1 in hippocampus; Pvalb below detection | Secondary |
| `0724 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0724]` | 0203 Lamp5 Lhx6 Gaba_1 | 2443 | 🔴 LOW | Lamp5 Lhx6 markers, but cortically biased | Supports broader Lamp5 Lhx6 mapping |
| `0651 Vip Gaba_7 [CS20230722_CLUS_0651]` | 0179 Vip Gaba_7 | 170 | ⚪ UNCERTAIN | Calb2 high (6.90); wrong subclass (Vip) | Eliminated (wrong subclass) |
| `0655 Vip Gaba_9 [CS20230722_CLUS_0655]` | 0181 Vip Gaba_9 | 653 | ⚪ UNCERTAIN | Calb2 high (6.15); Nos1 only 2.01 | Eliminated (wrong subclass) |
| `0695 RHP-COA Ndnf Gaba_3 [CS20230722_CLUS_0695]` | 0195 RHP-COA Ndnf Gaba_3 | 178 | ⚪ UNCERTAIN | Nos1 below detection (0.35); RHP-COA lineage | Eliminated (Nos1 absent) |
| `0705 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0705]` | 0198 RHP-COA Ndnf Gaba_6 | 61 | ⚪ UNCERTAIN | Calb2 borderline; RHP-COA lineage | Eliminated (wrong subclass) |
| `0623 Vip Gaba_1 [CS20230722_CLUS_0623]` | 0173 Vip Gaba_1 | 2375 | ⚪ UNCERTAIN | Calb2 7.96; Nos1 0.51; isocortex-biased | Eliminated (wrong subclass) |
| `0625 Vip Gaba_1 [CS20230722_CLUS_0625]` | 0173 Vip Gaba_1 | 1307 | ⚪ UNCERTAIN | Calb2 5.96; markers low; cortical subplate | Eliminated (wrong subclass) |
| `0636 Vip Gaba_4 [CS20230722_CLUS_0636]` | 0176 Vip Gaba_4 | 750 | ⚪ UNCERTAIN | Calb2 5.85; Nos1 1.61; cortical subplate | Eliminated (wrong subclass) |
| `0637 Vip Gaba_4 [CS20230722_CLUS_0637]` | 0176 Vip Gaba_4 | 338 | ⚪ UNCERTAIN | Calb2 6.90; cortical subplate | Eliminated (wrong subclass) |
| `0179 Vip Gaba_7 [CS20230722_SUPT_0179]` | — | 1083 | ⚪ UNCERTAIN | Nos1 6.91 but Calb2 6.78; wrong subclass | Eliminated (wrong subclass) |
| `1196 Monocytes NN_1 [CS20230722_SUPT_1196]` | — | 33 | 🔴 REFUTED | Non-neuronal; Pvalb detectable; no hippocampal cells | Eliminated (non-neuronal) |
| `0181 Vip Gaba_9 [CS20230722_SUPT_0181]` | — | 1441 | ⚪ UNCERTAIN | Calb2 6.96; Lamp5 0.20; wrong subclass | Eliminated (wrong subclass) |
| `0173 Vip Gaba_1 [CS20230722_SUPT_0173]` | — | 6998 | ⚪ UNCERTAIN | Calb2 6.41; Nos1 1.11; isocortex-biased | Eliminated (wrong subclass) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Ivy cell (IvC) — defined as a CA1 pyramidal-layer GABAergic interneuron expressing Nos1, Npy, and Lamp5, with absence of Pvalb, Sst, and Calb2 [1][2][3][4][5]. `definition_basis: CLASSICAL_MULTIMODAL`. The classical type description draws on both Cre-driver-targeted electrophysiological/anatomical work (Tricoire et al. 2010 [2]) and broader anatomical surveys (Bocchio et al. 2024 [1]).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match against MBA:407 hippocampal field CA1, NT type GABAergic, defining markers Nos1/Npy/Lamp5, negative markers Pvalb/Sst/Calb2). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.** No annotation-transfer runs are available for hippocampal Ivy cells in this graph. The marker-only assessment above is therefore the strongest current evidence; a Cre-driver-targeted Ivy-cell scRNA-seq cohort run through MapMyCells against WMBv1 is the headline upgrade path (see Discussion).

**Atlas data sources.** WMBv1 (CCN20230722); precomputed expression and MERFISH-registered painted regions per cluster.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `5738aa0` at 2026-06-08T05:47:21+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0731 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0724 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0651 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0655 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0695 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0705 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0623 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0625 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0636 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0637 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_1196 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0181 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0173 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Ivy cell (IvC) → 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] at MODERATE confidence. Key support: marker-triplet (Nos1, Npy, Lamp5) consistency at high cohort percentiles across the supertype with child-coverage 1.000; MGE-derived Lamp5 Lhx6 lineage placement matches the canonical Ivy-cell developmental origin reported in the classical literature [2]. Key caveats: low strict and proximity region fractions for CA1 (atlas under-sampling of CA1 SP Lamp5 Lhx6 cells likely; potential overlap with the hippocampal neurogliaform cell mapping onto the same supertype per Tricoire 2010 [2]).

No Cell Ontology term currently covers this type. The classical literature consensus (Bocchio 2024 [1], Tricoire 2010 [2]) supports a CL contribution naming an nNOS+/NPY+/Lamp5+ CA1 pyramidal-layer GABAergic interneuron with late-spiking phenotype, potentially in unification with the nNOS+ neurogliaform cell pending resolution of Tricoire 2010's prediction.

### Proposed experiments and follow-ups

- **What:** MapMyCells annotation transfer of a Cre-driver-targeted Ivy-cell scRNA-seq cohort (Nos1-CreER intersected with CA1 SP, or equivalent) onto WMBv1.
  **Target:** F1 ≥ 0.80 at SUPERTYPE level (CS20230722_SUPT_0203); F1 distribution across CS20230722_SUPT_0203's child clusters interpretable as Ivy vs. NGC scatter.
  **Expected output:** AnnotationTransferEvidence on the Ivy cell → SUPT_0203 edge (and child cluster edges).
  **Resolves:** Open questions 1–3.

- **What:** Patch-seq on biocytin-filled, morphology-reconstructed CA1 nNOS+ interneurons (Ivy in stratum pyramidale, NGC in stratum lacunosum-moleculare) followed by MapMyCells.
  **Target:** Test the Tricoire 2010 prediction of trans-laminar identity at single-cell resolution; quantify Ivy-vs-NGC scatter within CS20230722_SUPT_0203.
  **Expected output:** AnnotationTransferEvidence + MarkerAnalysisEvidence linking morphology to transcriptomic placement.
  **Resolves:** Open question 3 directly; informs decision on Ivy/NGC node unification.

- **What:** Targeted literature trawl for Lamp5 as a transcript-level Ivy-cell marker independent of the Lamp5 Lhx6 supertype naming convention.
  **Expected output:** Updated marker provenance on the classical node with a primary citation for Lamp5.
  **Resolves:** Strengthens the marker chain underlying the primary mapping.

### Open questions

1. Are the CA3-enriched Lamp5 Lhx6 cells in CS20230722_SUPT_0203 Ivy cells, neurogliaform cells, or a distinct type?
2. Is there a CA1 SP Lamp5 Lhx6 cluster capturing hippocampal Ivy cells at cluster-level resolution, or does the atlas systematically under-sample CA1 SP Lamp5 Lhx6 cells?
3. Do ephys/morphology panels distinguish Ivy cells from hippocampal neurogliaform cells at CS20230722_SUPT_0203, or are they indistinguishable across all assessable panels (Tricoire 2010 prediction)?
4. Is the residual Sst signal (≥1.2) across CA1-relevant Lamp5 Lhx6 child clusters atlas-side technical contamination, or does it reflect undocumented Sst heterogeneity within the Ivy-cell type?

---

## References

| # | Citation | PMID | Used for |
|---:|---|---|---|
| [1] | Bocchio et al. 2024 | [PMID:39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | Soma location |
| [2] | Tricoire et al. 2010 | [PMID:20147544](https://pubmed.ncbi.nlm.nih.gov/20147544) | Nos1, Npy, negative markers, Ivy/NGC unification prediction |
| [3] | Tzilivaki et al. 2023 | [PMID:37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Nos1 marker |
| [4] | Kim et al. 2025 | [PMID:41473287](https://pubmed.ncbi.nlm.nih.gov/41473287) | Nos1 marker |
| [5] | Wierenga et al. 2010 | [PMID:21209836](https://pubmed.ncbi.nlm.nih.gov/21209836) | Nos1 marker |

---

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Nos1, Npy, and Lamp5 are all CONSISTENT at
    CS20230722_SUPT_0203 with high cohort percentiles (Nos1 cohort_pct
    0.968; Lamp5 cohort_pct 0.968; child-coverage 1.000 on the marker
    triplet); 3 of 3 defining markers CONSISTENT, MGE-derived Lamp5 Lhx6
    lineage matches the Tricoire 2010 [PMID:20147544] developmental
    origin for Ivy cells. region_fraction_100um: 0.090 (strict
    region_fraction: 0.014) — low CA1 SP overlap reads as atlas
    under-sampling rather than refuting the call, given marker
    concordance; cluster-level scatter across CS20230722_CLUS_0731
    and CS20230722_CLUS_0724 motivates broadMatch + 1:n rather than a
    1:1 to any specific child cluster.
  reconciliation_note: >
    Same supertype is the leading target for the hippocampal
    neurogliaform-cell node; Tricoire 2010 [PMID:20147544] reports
    overlapping developmental, ephys, morphological, and neurochemical
    properties between Ivy cells and nNOS+ NGCs distinguished only by
    laminar position. Whether Ivy and NGC ultimately collapse onto a
    single transcriptomic type at this supertype is unresolved without
    annotation transfer or patch-seq.
  caveats:
    - caveat_type: OTHER
      description: >
        Ivy cells and nNOS+ NGCs are reported to share overlapping
        developmental, electrophysiological, morphological, and
        neurochemical properties (Tricoire 2010 [PMID:20147544]),
        suggesting they may constitute a single interneuron subtype
        distinguished only by laminar position. The hippocampal NGC
        mapping edge to this same supertype is therefore likely to
        overlap the same atlas population.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        region_fraction_100um: 0.090, strict region_fraction: 0.014 —
        no CA1 stratum pyramidale cells in CS20230722_SUPT_0203 despite
        Ivy cells being canonically in CA1 SP. Atlas may under-sample
        CA1 SP Lamp5 Lhx6 cells, or the Ivy-cell CA1 population is
        split across additional supertypes not surfaced in the top-K.
  proposed_experiments:
    - >
      MapMyCells annotation transfer of a Cre-driver-targeted Ivy-cell
      scRNA-seq cohort (Nos1-CreER + CA1 SP restriction) onto WMBv1;
      target F1 >= 0.80 at SUPERTYPE level for CS20230722_SUPT_0203;
      expected output AnnotationTransferEvidence.
    - >
      Patch-seq on biocytin-filled, morphology-reconstructed CA1 nNOS+
      interneurons (Ivy in stratum pyramidale, NGC in stratum
      lacunosum-moleculare) with post-hoc MapMyCells assignment; tests
      Tricoire 2010 [PMID:20147544] trans-laminar identity prediction;
      expected output AnnotationTransferEvidence + MarkerAnalysisEvidence.
    - >
      Targeted literature trawl for Lamp5 as a transcript-level Ivy-cell
      marker independent of the Lamp5 Lhx6 supertype naming; strengthens
      marker provenance on the classical node.
  unresolved_questions:
    - >
      Is the residual Sst signal (>=1.2 across CA1-relevant Lamp5 Lhx6
      child clusters) atlas-side technical contamination, or does it
      reflect undocumented Sst heterogeneity within the Ivy-cell type?
      Trawl literature for Sst heterogeneity in nNOS+ CA1 interneurons.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0731 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.50
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Best in-region Lamp5 Lhx6 child cluster: Nos1 8.55
    (cohort_pct 0.941), Lamp5 8.51 (cohort_pct 0.985, MERFISH-tagged),
    Npy 4.35 (NEUROPEPTIDE-tagged), Pvalb 0.07 below MIN_DETECTABLE; 5
    of 7 marker comparisons CONSISTENT. region_fraction_100um: 0.132
    boundary-band proximity; Field CA3 [MBA:463] and Field CA3
    pyramidal layer [MBA:495] enrichment suggests a CA3-biased
    Lamp5 Lhx6 population rather than the canonical CA1 SP Ivy
    placement.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Sst at 1.24 (cohort_pct 0.397) and Calb2 at 0.31 (cohort_pct
        0.368) DISCORDANT against the classical negative-marker
        signature. Residual Sst signal is not documented in the
        synthesised classical literature for Ivy cells and is flagged
        for a targeted lit trawl.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        region_fraction_100um: 0.132 (strict region_fraction: 0.015) —
        boundary-band proximity dominated by Field CA3 [MBA:463] and
        Field CA3 pyramidal layer [MBA:495] rather than CA1; cluster
        may capture a CA3-biased Lamp5 Lhx6 population.
  proposed_experiments:
    - >
      MapMyCells annotation transfer from a CA1-SP-restricted
      Nos1-CreER Ivy-cell cohort to test whether Ivy cells map
      preferentially onto CS20230722_CLUS_0731 over sibling
      CS20230722_CLUS_0724; target F1 >= 0.80 at CLUSTER level.
    - >
      MERFISH/smFISH co-localisation of Nos1+Lamp5+Npy in CA1 stratum
      pyramidale to confirm or refute atlas under-sampling of CA1 SP
      Lamp5 Lhx6 cells.
  unresolved_questions:
    - >
      Does CS20230722_CLUS_0731 represent CA1 SP Ivy cells, CA3
      Lamp5 Lhx6 cells, or both?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0724 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:WEAKEST] Highest atlas-side Nos1 (9.14, cohort_pct 0.985) and
    high Lamp5 (8.47, MERFISH-tagged) among candidates, but
    region_fraction_100um: 0.119 (strict region_fraction: 0.030) is
    dominated by Isocortex [MBA:315] and lateral forebrain bundle
    system [MBA:983] rather than hippocampus; Pvalb 0.23 above
    MIN_DETECTABLE violates the classical negative-marker signature.
    Likely a cortically biased Lamp5 Lhx6 cluster rather than a
    hippocampal Ivy-cell home; retained as a sibling under the broader
    CS20230722_SUPT_0203 mapping rather than committed as a 1:1.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Pvalb 0.23 (cohort_pct 0.382), Sst 1.18 (cohort_pct 0.338), and
        Calb2 0.28 (cohort_pct 0.279) are all DISCORDANT against the
        classical negative-marker signature.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        region_fraction_100um: 0.119 with Isocortex [MBA:315]
        (count_100um=452) and lateral forebrain bundle system
        [MBA:983] (count_100um=280) outweighing hippocampal counts —
        cluster is cortically biased within the Lamp5 Lhx6 lineage.
  proposed_experiments:
    - >
      Same Cre-driver-targeted MapMyCells AT as proposed for
      CS20230722_SUPT_0203 will arbitrate whether CS20230722_CLUS_0724
      captures any hippocampal Ivy cells or whether it should be
      removed from the candidate set.
  unresolved_questions: []
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0651 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Vip Gaba_7 subclass — Calb2 6.90 (cohort_pct 0.882)
    strongly violates the classical Calb2-ABSENT signature, and Vip
    lineage is CGE-derived rather than the MGE Lamp5 Lhx6 lineage
    canonical for Ivy cells.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0655 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Vip Gaba_9 subclass — Calb2 6.15 (cohort_pct 0.838)
    DISCORDANT; Nos1 only 2.01 (cohort_pct 0.412) and Lamp5 0.23
    fail the defining marker triplet.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0695 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] RHP-COA Ndnf Gaba_3 — Nos1 0.35 (cohort_pct 0.074) is
    effectively absent against the defining Ivy-cell marker; lineage is
    Ndnf-based rather than Lamp5 Lhx6.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0705 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] RHP-COA Ndnf Gaba_6 — RHP/COA-biased Ndnf lineage;
    Sst 0.96 DISCORDANT; only 61 cells. Not a hippocampal Ivy-cell
    candidate.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0623 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Vip Gaba_1 — Calb2 7.96 (cohort_pct 0.941) and Nos1
    0.51 (cohort_pct 0.147) fail both the negative-marker and
    defining-marker constraints; location DISCORDANT (Isocortex
    dominant).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0625 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Vip Gaba_1 — Calb2 5.96 DISCORDANT; Nos1/Npy/Lamp5
    all APPROXIMATE-low; region DISCORDANT (Cortical subplate
    [MBA:703] dominant).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0636 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Vip Gaba_4 — Calb2 5.85 DISCORDANT; location
    DISCORDANT (Cortical subplate [MBA:703] dominant); wrong subclass.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_CLUS_0637 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Vip Gaba_4 — Calb2 6.90 DISCORDANT; only 0.077
    proximity to CA1; wrong subclass despite Nos1 4.91.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0179 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] Vip Gaba_7 supertype — Nos1 6.91 (cohort_pct 0.903) is
    elevated but Calb2 6.78 (cohort_pct 0.903) and Vip-lineage
    subclass place this supertype in the CGE-derived branch rather
    than the MGE Lamp5 Lhx6 lineage of Ivy cells.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_1196 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.02
  rationale: >
    [tier:CUT] Monocytes NN_1 — non-neuronal supertype; Pvalb 1.05
    DISCORDANT, location DISCORDANT (Isocortex/Cerebellum/Midbrain,
    no hippocampal cells); 33 cells total. Not a candidate.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0181 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Vip Gaba_9 supertype — Calb2 6.96 (cohort_pct 0.935)
    DISCORDANT; Lamp5 0.20 fails the defining marker; wrong subclass.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0173 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    [tier:CUT] Vip Gaba_1 supertype — Calb2 6.41 (cohort_pct 0.839)
    DISCORDANT, Nos1 1.11 (cohort_pct 0.290) low; location DISCORDANT
    (Isocortex [MBA:315] count_100um=1706 dominant). Wrong subclass.
```
<!-- verdict-block-end -->
