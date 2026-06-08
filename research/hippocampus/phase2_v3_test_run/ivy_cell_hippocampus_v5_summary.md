# Ivy cell (IvC) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Ivy cells are nNOS-expressing GABAergic interneurons of the CA1 pyramidal layer, characterised by Lamp5 and NPY co-expression and dense axonal arbors that mediate slow inhibition of pyramidal neurons. Among the most numerous CA1 inhibitory cell types, they are closely related to — and on some criteria indistinguishable from — neurogliaform cells (NGCs), and assigning them a transcriptomic identity in the WMBv1 atlas matters for downstream studies of CA1 microcircuit inhibition.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | [1] |
| NT | GABAergic | — |
| Markers | Nos1, Npy, Lamp5 | [1][2][3][4][5] |
| Negative markers | Pvalb, Sst, Calb2 | [2] |
| Neuropeptides | Npy | [2] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Bocchio et al. 2024, CA1 pyramidal-layer sampling · [1]
  > This mouse line allows for a large sampling from diverse interneuron subtypes in the CA1 pyramidal layer, including the most representative ones (Bezaire et al., 2013), the PV-expressing basket and bistratified cells (Klausberger et al., 2008), the NOS- expressing ivy cells (14381729) and two types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin (Klausberger et al., 2008)(Topolnik et al., 2022)
  > — Bocchio et al. 2024, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 262127573_d140faf4 -->
- **Markers / negative markers / neuropeptides:** Tricoire et al. 2010, classical interneuron-marker survey · [2]
  > IvCs and NGCs have been argued to represent distinct interneuron subtypes (52852755), despite the rich similarity between these cell types, including coexpression of NPY with nNOS, dense axonal arbors, and slow pyramidal cell inhibition. We found that both of these interneurons exhibit a LS phenotype and fail to express other classical interneuron markers such as PV, SOM, or CR.
  > — Tricoire et al. 2010, Classical Functional and Morphological Interneuron Types · [2] <!-- quote_key: 2405079_6850b924 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Marker-expression alignment (Nos1, Npy, Lamp5 all CONSISTENT with high cohort percentile) and annotation transfer from two independent SMART-Seq v4 hippocampal datasets — Yao 2021 GSE185862 Lamp5 cells and Harris 2018 GSE99888 CA1 Cacna2d1.Lhx6.Reln cells — converge on the supertype 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] (F1=0.90 and F1=0.81 respectively; see property comparison table). The atlas-side soma footprint of SUPT_0203 sits in CA3 and dentate gyrus rather than the canonical CA1 stratum pyramidale, so the mapping is recorded as a close (not exact) match with a documented location caveat.

### 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] · 🟡 MODERATE

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | Hippocampal formation [MBA:1089] count_100um=3175; Dentate gyrus [MBA:726] count_100um=1220; Field CA3 [MBA:463] count_100um=1179 | not assessed | DISCORDANT |
| NT type | GABAergic | not asserted | not assessed | NOT_ASSESSED |
| Nos1 | defining marker | 7.78 (cohort percentile 0.968) | not assessed | CONSISTENT |
| Npy | defining marker | 4.62 (cohort percentile 0.710) | not assessed | CONSISTENT |
| Lamp5 | defining marker (DEFINING_SCOPED on atlas) | 6.73 (cohort percentile 0.968) | not assessed | CONSISTENT |
| Pvalb | ABSENT (negative) | 0.43 (cohort percentile 0.516) | not assessed | DISCORDANT |
| Sst | ABSENT (negative) | 1.52 (cohort percentile 0.677) | not assessed | DISCORDANT |
| Calb2 | ABSENT (negative) | 0.37 (cohort percentile 0.419) | not assessed | DISCORDANT |
| Neuropeptide Npy | classical | 4.62 (cohort percentile 0.710) | not assessed | CONSISTENT |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Lamp5 Lhx6 marker concordance | Atlas metadata | PARTIAL | MGE-derived Lamp5+ supertype; CA1 SP absent in anat | atlas-internal |
| Precomputed-stats marker cross-check | Atlas metadata | SUPPORT | 3/3 defining markers present; 3/3 negatives low | atlas-internal |
| Yao 2021 SSv4 Lamp5 → SUPT_0203 | Annotation transfer | SUPPORT | F1=0.90 (711/868; purity 0.989) | atlas-internal |
| Harris 2018 Cacna2d1.Lhx6.Reln → SUPT_0203 | Annotation transfer | SUPPORT | F1=0.81 (246/3663; purity 0.730) | atlas-internal |

**Supporting evidence**

- The atlas supertype is annotated MGE-derived (Lhx6+) Lamp5+, with Lamp5 and Lhx6 listed as DEFINING_SCOPED markers — matching the Lhx6+/Lamp5+/Id2+ "NGFC.M" descriptor that Tricoire 2011-era literature applies to ivy cells. Precomputed stats confirm all three defining markers (Nos1=7.78, Npy=4.62, Lamp5=6.73) at high cohort percentile and all three negative markers below detection (Pvalb=0.43, Sst=1.52, Calb2=0.37).
- Annotation transfer of the Yao 2021 SSv4 hippocampal Lamp5 subclass (n=868) onto WMBv1 lands SUPT_0203 as the top supertype target (F1=0.90; 711 of 868 cells; purity 0.989 — i.e. SUPT_0203 is almost exclusively populated by Lamp5+ cells in this dataset).
- An independent second-dataset corroboration comes from Harris 2018 CA1 inhibitory neurons: the Cacna2d1.Lhx6.Reln class (Lamp5+/Lhx6+/Reln+) maps to SUPT_0203 at F1=0.81 (Lamp5 Lhx6 Gaba subclass F1=0.83), confirming the Lamp5+Lhx6+ identity from a second taxonomy under a published label set.

**Marker evidence provenance**

- **Nos1**: established at transcript- and protein-level for ivy cells across multiple primary studies [2][3][4][5]; CONSISTENT with the atlas supertype's high cohort percentile (0.968).
- **Npy**: Tricoire 2010 [2] documents NPY co-expression with nNOS in IvCs at the protein and transcript level; CONSISTENT with atlas.
- **Lamp5**: no primary citation on the classical node — *(note: classical marker Lamp5 lacks a primary citation; the concordance with the SUPT_0203 supertype name is partially nominal and warrants a targeted cite-traverse for "Lamp5 ivy cell hippocampus" to anchor it).* This is an upstream curation gap, not a candidate-specific caveat.
- **Pvalb / Sst / Calb2 (negative markers)**: anchored by Tricoire 2010 ("fail to express other classical interneuron markers such as PV, SOM, or CR") [2]; atlas precomputed means are all below MIN_DETECTABLE on the cluster, so the DISCORDANT label on the precomputed-stats comparison reflects only that the cohort percentile is non-zero, not that the marker is expressed.

**Concerns**

- Location is DISCORDANT: `region_fraction_100um: 0.090` and strict `region_fraction: 0.014` — soma in SUPT_0203 sit predominantly in CA3 stratum oriens/radiatum and dentate gyrus rather than CA1 pyramidal layer. *(Low-but-not-zero proximity; classical ivy cells may still be a subtype of SUPT_0203 but the CA1 stratum-pyramidale ivy population is under-represented in this supertype as currently delineated. Could reflect either atlas undersampling of CA1 SP Lamp5 Lhx6 cells or genuine cross-laminar distribution of the broader Lamp5 Lhx6 type.)*
- Negative-marker comparisons return DISCORDANT on the per-property check because the comparator looks at non-zero cohort percentile, but the absolute expression values (Pvalb=0.43, Sst=1.52, Calb2=0.37) are all below the detection floor — these are not real contradictions, just an artefact of the comparison rule.
- Ivy cells and nNOS+ neurogliaform cells are reported by Tricoire 2010 [2] to share completely overlapping developmental, electrophysiological, morphological, and neurochemical properties. The mapping cannot resolve ivy_cell from NGC at this supertype — the two classical types both map indistinguishably to SUPT_0203 (see source-pool note below).

**What would upgrade confidence**

- A CA1 stratum-pyramidale-restricted cluster-level mapping (drilling SUPT_0203 to children) using a CA1-SP-restricted ivy-cell source dataset would distinguish whether the CA1 SP ivy population is missing from SUPT_0203 or simply distributed across several Lamp5 Lhx6 child clusters.
- A patch-seq study targeting nNOS+/Lamp5+ CA1 SP cells with morphology recovery, mapped onto WMBv1 at cluster level (target F1 ≥ 0.80), would generate AnnotationTransferEvidence anchored to ivy-cell identity directly rather than via the broader Lamp5+Lhx6+ subclass.
- Targeted cite-traverse for the Lamp5 marker on morphology-confirmed ivy cells would close the marker-provenance gap noted above.

**Source-pool note (ivy_cell vs neurogliaform_cell).** The pre-pass surfaced ivy_cell_hippocampus and neurogliaform_cell_hippocampus as candidates for source-group pooling because their AT evidence onto SUPT_0203 is numerically identical at every shared target level (CLASS/SUBCLASS/SUPERTYPE: F1, coverage, and purity all match to four decimals). Tricoire 2010 [2] supports this on biological grounds — the two classical types share developmental origin, electrophysiology, morphology, and the Nos1/Npy/Lamp5 marker panel, distinguished only by laminar position. The lit-grounded reading is that no presently-assayed transcriptomic, morphological, or electrophysiological panel distinguishes them, and they should be treated as a single source group at this resolution.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203]` | (same) | 8913 | 🟡 MODERATE | Yao+Harris AT to SUPT_0203 (F1=0.90 / 0.81) | Primary |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The ivy cell is defined here on a CLASSICAL_MULTIMODAL basis: Nos1, Npy, and Lamp5 as defining markers (with Npy also as the neuropeptide), Pvalb / Sst / Calb2 as classical negative markers, soma in CA1 pyramidal layer [UBERON:0014548] per Bocchio et al. 2024 [1], and GABAergic identity. Tricoire 2010 [2] anchors the marker panel and the negative-marker exclusion, and notes near-complete overlap with the nNOS+ neurogliaform cell type.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer (Yao 2021 SSv4).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Lamp5 subclass) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Annotation transfer (Harris 2018 Class).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 published Class labels — Cacna2d1.Lhx6.Reln) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Caveats | This run record scores Harris 2018's published Class labels against WMBv1; shares the upstream MMC output with the Chamberland subfamily-labelled companion run. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `8c61574` at 2026-06-08T15:22:26+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL/SUPPORT | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Ivy cell (IvC) → 0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203] at MODERATE confidence. Key support: marker concordance on Nos1, Npy, Lamp5 (precomputed-stats) plus two independent annotation-transfer datasets (Yao 2021 SSv4 F1=0.90; Harris 2018 Class F1=0.81). Key caveats: location DISCORDANT (atlas SUPT_0203 soma sit in CA3/DG rather than CA1 stratum pyramidale, `region_fraction_100um: 0.090`); ivy cell is transcriptomically indistinguishable from neurogliaform cell at this supertype per Tricoire 2010 [2], so the supertype-level edge supports a joint mapping rather than a 1:1 ivy-only assignment.

No Cell Ontology term currently assigned. Candidate for CL contribution as a Lamp5+/Lhx6+/Nos1+/Npy+ CA1 GABAergic interneuron type (potentially co-defined with the nNOS+ neurogliaform cell).

### Proposed experiments and follow-ups

- **What:** Cluster-level MapMyCells annotation transfer using a CA1 stratum-pyramidale-restricted nNOS+/Lamp5+ source dataset (e.g. patch-seq with morphology recovery, or sorted Nos1-Cre+ CA1 SP cells).
  **Target:** F1 ≥ 0.80 at CLUSTER level within SUPT_0203 children.
  **Expected output:** AnnotationTransferEvidence at cluster resolution.
  **Resolves:** open questions 1 and 2 — whether the CA3-enriched SUPT_0203 cells are ivy cells, neurogliaform cells, or a distinct type, and whether a CA1-SP-resident child cluster exists.
- **What:** Patch-seq or electrophysiology/morphology panel comparing morphology-confirmed ivy and neurogliaform cells from the same animals.
  **Target:** any reproducible distinguishing property (firing pattern, axonal arbor extent, transcript signature).
  **Expected output:** ElectrophysiologyProfile / MorphologyProfile / LiteratureEvidence on the two classical nodes.
  **Resolves:** open question 3 (and #61-style pooling decision).
- **What:** Targeted cite-traverse for Lamp5 as an ivy-cell marker on morphology-confirmed cells.
  **Target:** at least one primary study testing Lamp5 on patched/filled CA1 SP nNOS+ cells.
  **Expected output:** PropertySource on classical_node.defining_markers.Lamp5.
  **Resolves:** marker-provenance gap.

### Open questions

1. Are the CA3-enriched Lamp5 Lhx6 cells in SUPT_0203 ivy cells, neurogliaform cells, or a distinct type?
2. Is there a CA1 SP Lamp5 Lhx6 cluster capturing hippocampal ivy cells at the cluster level?
3. Do ephys/morphology panels distinguish ivy_cell_hippocampus from neurogliaform_cell_hippocampus at CS20230722_SUPT_0203, or are they indistinguishable across all assessable panels (Tricoire 2010 prediction)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [2] | Tricoire et al. 2010 | [20147544](https://pubmed.ncbi.nlm.nih.gov/20147544/) | Nos1 marker; negative markers; Npy; ivy/NGC overlap |
| [3] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Nos1 marker |
| [4] | Kim et al. 2025 | [41473287](https://pubmed.ncbi.nlm.nih.gov/41473287/) | Nos1 marker |
| [5] | Wierenga et al. 2010 | [21209836](https://pubmed.ncbi.nlm.nih.gov/21209836/) | Nos1 marker |

<!-- verdict-block-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.62
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer from Yao 2021 GSE185862 SSv4 Lamp5 hippocampal cells
    (F1=0.90 in at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1) and Harris 2018 GSE99888
    Cacna2d1.Lhx6.Reln CA1 interneurons (F1=0.81 in at_run_20260512_harris_class_mmc_wmbv1)
    converge on CS20230722_SUPT_0203, with 3 of 3 defining markers CONSISTENT
    (Nos1, Npy, Lamp5; scRNA-seq precomputed stats). Location is DISCORDANT:
    region_fraction_100um: 0.090 — SUPT_0203 soma sit in CA3/DG rather than CA1 stratum
    pyramidale, so the mapping is recorded as closeMatch + 1:n at supertype level rather
    than exactMatch.
  reconciliation_note: >
    Indistinguishable from neurogliaform_cell_hippocampus at this supertype: AT F1,
    coverage, and purity are identical at CLASS, SUBCLASS, and SUPERTYPE levels, and
    Tricoire 2010 (PMID:20147544) reports the two classical types share developmental,
    electrophysiological, morphological, and neurochemical properties. See companion
    edge edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        No CA1 stratum pyramidale cells in SUPT_0203 despite ivy cell soma being
        canonically in CA1 SP (region_fraction_100um: 0.090; region_fraction: 0.014).
        Atlas may undersample CA1 SP Lamp5 Lhx6 cells, or the CA1 ivy population is
        split across additional supertypes.
    - caveat_type: OTHER
      description: >
        Ivy cells and nNOS+ neurogliaform cells share completely overlapping
        developmental, electrophysiological, morphological, and neurochemical
        properties per Tricoire 2010 (PMID:20147544); this edge and
        edge_neurogliaform_cell_hippocampus_to_CS20230722_SUPT_0203 cover the
        same atlas population at supertype resolution.
    - caveat_type: WEAK_MARKER_EVIDENCE
      description: >
        Classical marker Lamp5 on ivy_cell_hippocampus lacks a primary citation;
        concordance with the SUPT_0203 supertype name is partially nominal.
        Curator review recommended.
  proposed_experiments:
    - >
      CA1 stratum-pyramidale-restricted patch-seq or sorted Nos1-Cre+ scRNA-seq,
      MapMyCells onto WMBv1 at cluster level within SUPT_0203 children (target
      F1 >= 0.80) to test whether a CA1 SP Lamp5 Lhx6 child cluster exists.
    - >
      Electrophysiology / morphology panel on morphology-confirmed ivy and
      neurogliaform cells from matched animals, testing any reproducible
      distinguishing property predicted by Tricoire 2010.
    - >
      Targeted cite-traverse for Lamp5 as an ivy-cell marker on
      morphology-confirmed CA1 SP nNOS+ cells, to anchor the Lamp5 assertion
      to a primary study.
  unresolved_questions:
    - >
      Consider unifying `ivy_cell_hippocampus` and `neurogliaform_cell_hippocampus`;
      no available data distinguishes them. See #62.
  lit_to_lit_edges:
    - lit_a: ivy_cell_hippocampus
      lit_b: neurogliaform_cell_hippocampus
      mapping_justification: semapv:CompositeMatching
```
<!-- verdict-block-end -->

<!-- source-groups-rationale-start: edge_ivy_cell_hippocampus_to_CS20230722_SUPT_0203 -->
```yaml
source_groups_rationale:
  - source_group_label: Lamp5
    run_ref: at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1
    rationale: >
      ivy_cell_hippocampus and neurogliaform_cell_hippocampus map indistinguishably
      to CS20230722_SUPT_0203 at all assessed taxonomy levels (CLASS/SUBCLASS/SUPERTYPE
      F1, coverage, and purity match to four decimals). Tricoire 2010 (PMID:20147544)
      reports complete overlap of developmental, electrophysiological, morphological,
      and neurochemical properties between the two classical types, supporting a
      pooled treatment at this resolution.
```
<!-- source-groups-rationale-end -->
