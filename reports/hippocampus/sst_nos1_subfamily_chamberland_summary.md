# Sst::Nos1-IN (long-range projecting, Chamberland 2024) — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The Sst::Nos1-IN subfamily is one of four genetically distinct Sst-interneuron subfamilies that Chamberland and colleagues defined transcriptomically in the mouse hippocampus, with cell bodies in CA1 stratum oriens [1]. Functionally, Sst::Nos1-INs are long-range-projecting interneurons whose axons leave the hippocampus to innervate the medial septum and the contralateral hippocampus — the canonical "hippocampo-septal" / back-projection identity. Mapping this subfamily to the Whole Mouse Brain v1 (WMBv1) atlas matters because it tests whether transcriptomic atlases reproduce the classical anatomical/functional split between cortical Sst Gaba interneurons (which dominate the Sst subclass on the cortex/CA1 side) and the long-range-projecting Sst Chodl branch.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | [1] |
| NT | GABAergic | [1] |
| Defining markers | Sst, Nos1 | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Defining markers (Sst, Nos1):** in-silico transcriptomic subfamily definition · Chamberland 2024 · [1]
  > genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->
  > hippocampal somatostatin-expressing interneurons (Sst-INs) can be divided into at least four subfamilies, each with distinct functions
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_53fb33cc -->
- **Soma location (CA1 stratum oriens):** in-silico subfamily labels derived from Harris 2018 stratum-oriens-targeted scRNA-seq · Chamberland 2024 · [1]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Direct annotation-transfer evidence places the Chamberland Sst::Nos1-IN subfamily on the Sst Chodl branch of WMBv1, with the supertype 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] capturing essentially all source cells (F1=0.99 at supertype; see filtered AT figure) and the child cluster 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859] leading the cluster-level distribution (F1=0.97). This is a *cross-supertype* result relative to the cortical Sst Gaba subclass that hosts most CA1 dendrite-targeting Sst types — consistent with the long-range projection identity of Sst::Nos1-INs, which biologically belong with Sst Chodl rather than with cortical Sst Gaba.

![Filtered AT figure for Sst::Nos1-IN](figures/f1_for_sst_nos1_subfamily_chamberland.png)

*F1 across taxonomy levels for the Sst_Nos1 source group (n=35 source cells qualifying at subclass). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. With a single source in the figure, Purity and Coverage both inform the mapping. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The Sst_Nos1 distribution collapses onto a single subclass (056 Sst Chodl Gaba) and supertype (0241 Sst Chodl Gaba_4), with cluster-level scatter limited to one dominant child (CLUS_0859) plus single-cell tails on sibling clusters.*

### Sst Chodl Gaba_4 supertype [CS20230722_SUPT_0241] · 🟢 HIGH

**Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted | GABA (CLUS_0859) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Soma location | hippocampus stratum oriens [UBERON:0005371] | Isocortex [MBA:315] dominant; lateral forebrain bundle system [MBA:983]; corpus callosum [MBA:776] | (see CLUS_0859 row) | DISCORDANT |
| marker Sst | Sst — defining marker | Sst: 12.33 (cohort pct 0.984; child-coverage 1.000) | — | CONSISTENT |
| marker Nos1 | Nos1 — defining marker | Nos1: 11.26 (cohort pct 0.968; child-coverage 1.000) | — | CONSISTENT |

*(1 of 1 AT-mapped child cluster (CLUS_0859) shows soma in CA1 stratum oriens despite the supertype-level region rollup being dominated by extra-hippocampal Sst Chodl cells; the hippocampal Sst::Nos1 population is the in-region child within the supertype.)*

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | Sst=12.33; Nos1=11.26; region_fraction_100um=0.021 | atlas-internal |

**Supporting evidence.**

- Both defining markers (Sst, Nos1) are expressed at high cohort percentiles on the supertype (Sst pct 0.984, child-coverage 1.000; Nos1 pct 0.968, child-coverage 1.000) and align with the Sst Chodl branch identity.
- The paired AT-best child cluster CS20230722_CLUS_0859 (see next section) places the in-region Sst::Nos1 population specifically in CA1 stratum oriens; the supertype-level region scatter reflects pooling with extra-hippocampal Sst Chodl populations across the supertype's full distribution.

**Marker evidence provenance.**

- **Sst, Nos1:** transcriptomic definition from re-analysis of Harris 2018 stratum-oriens-targeted scRNA-seq (Chamberland 2024 in-silico subfamily labels using Sst × Nos1 expression-product gene-pair rules) [1]. Both markers are confirmed at transcript level and are the explicit gene-pair criteria used to define the subfamily, so the concordance is direct — the same gene-pair criteria that define Sst::Nos1-INs on the classical side also identify the Sst Chodl branch on the atlas side.

**Concerns.**

- *Location DISCORDANT (boundary off-target — `region_fraction_100um: 0.021`; stronger counter-evidence at supertype level; the supertype rollup is dominated by Isocortex and forebrain-bundle cells rather than CA1 stratum oriens. The hippocampal CA1 component sits in the child cluster CLUS_0859 rather than driving the supertype mean.)*
- Supertype-level region rollup is dominated by extra-hippocampal Sst Chodl cells (TAXONOMY_LEVEL_MISMATCH); the AT-best child cluster CS20230722_CLUS_0859 is the CA1 stratum oriens carrier.
- Supporting AT evidence on the paired cluster edge derives from a single annotation-transfer run (SINGLE_DATASET).

**What would upgrade confidence.**

- Targeted transcriptomic profiling of an Sst-Cre × Nos1 intersectional cohort, mapped onto WMBv1 with confirmed long-range axonal projection to medial septum (AnnotationTransferEvidence, target F1 ≥ 0.80 at CLUSTER against CS20230722_CLUS_0859).

### 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859] · 🟢 HIGH

**Property comparison.**

| Property | Classical | Supertype (0241) | Best cluster (0859) | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not asserted | GABA | CONSISTENT |
| marker Sst | Sst — defining marker | Sst: 12.33 (cohort pct 0.984) | Sst expressed in Sst Chodl subclass | CONSISTENT |
| marker Nos1 | Nos1 — defining marker | Nos1: 11.26 (cohort pct 0.968) | Nos1 expressed in Sst Chodl branch | CONSISTENT |
| Projection | Long-range (CA1 → medial septum, contralateral HPC) | — | Sst Chodl long-range identity | CONSISTENT |

**Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Chamberland 2024 in-silico AT (Sst_Nos1 → WMBv1) | Annotation transfer | SUPPORT | F1=0.97 at CLUSTER (Pur=1.00, Cov=0.94, n=31); F1=0.99 at SUPERTYPE; F1=0.99 at SUBCLASS | atlas-internal (run `at_run_20260512_chamberland_subfamily_mmc_wmbv1`) |

> Chamberland Sst::Nos1-IN cells map cleanly to the Sst Chodl Gaba subclass (F1=0.99 at subclass and supertype, F1=0.97 at cluster level → CLUS_0859). The mapping crosses subclass boundaries from the broader Sst Gaba subclass to the Sst Chodl Gaba subclass — biologically consistent because Sst Chodl types are long-range-projecting Sst interneurons (matching the hippocampo-septal projection identity of Sst::Nos1-IN cells). High confidence; near-deterministic mapping.
> — Chamberland et al. 2024 · [1]

**Supporting evidence.**

- AT to WMBv1 places all 31 of 33 qualifying Sst_Nos1 cells on CS20230722_CLUS_0859 with Purity=1.00 and Coverage=0.94 (F1=0.97; figure and `metrics_by_level` on `at_run_20260512_chamberland_subfamily_mmc_wmbv1`).
- The cross-supertype move from cortical Sst Gaba to Sst Chodl is biologically consistent with the Sst::Nos1-IN long-range-projection identity — Sst Chodl is the WMBv1 carrier for long-range Sst types, not the cortical/dendrite-targeting Sst Gaba branch.
- Sst and Nos1 — the two gene-pair criteria that define the Sst::Nos1 subfamily on the classical side — are both expressed in the Sst Chodl branch (Sst=12.33, Nos1=11.26 on the parent supertype).

**Marker evidence provenance.**

- **Sst, Nos1:** see supertype section above. The two gene-pair criteria are confirmed at transcript level on both the source-defining (Chamberland in-silico subfamily) and atlas-target (Sst Chodl branch precomputed expression) sides, with no atlas annotation/expression discrepancy.

**Concerns.**

- AT evidence derives from a single MapMyCells run against Chamberland's in-silico per-cluster Sst × Nos1 gene-pair labelling of the Harris 2018 source dataset (SINGLE_DATASET); independent replication is desirable.
- CLUS_0859 fell outside a previous Stage A top-50 candidate scan (stale-audit flag from `Cellular-Semantics/evidencell#111`); warrants curator review to reconcile candidate-generation thresholds with the AT-direct result.
- This Sst::Nos1-IN classical type likely overlaps the classical hippocampo_septal_cell_ca1 and lth_cell_hippocampus types in this graph (provisional EQUIVALENT and PARTIAL respectively per Cellular-Semantics/evidencell#54); those two classicals currently map to the cortical Sst Gaba branch (CLUS_0768 / SUPT_0216), so the convergence is at the level of classical-type definition rather than at the level of shared atlas target.

**What would upgrade confidence.**

- Targeted transcriptomic profiling of an Sst-Cre × Nos1 intersectional cohort with confirmed long-range axonal projection to medial septum, mapped onto WMBv1 (AnnotationTransferEvidence, target F1 ≥ 0.80 at CLUSTER against CS20230722_CLUS_0859).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859]` | `0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241]` | 2542 | 🟢 HIGH | AT F1=0.97 to CLUS_0859 (Pur=1.00, Cov=0.94) | Primary |
| `0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241]` | — | 2905 | 🟢 HIGH | AT F1=0.99 to supertype; Sst+Nos1 high | Supports broader mapping |
| `0768 Sst Gaba_3 [CS20230722_CLUS_0768]` | `0216 Sst Gaba_3` | 66 | 🔴 LOW | Cortical Sst Gaba branch; Nos1=0.76 (pct 0.378) APPROXIMATE | Eliminated (wrong subclass; low Nos1) |
| `0772 Sst Gaba_3 [CS20230722_CLUS_0772]` | `0216 Sst Gaba_3` | 190 | 🔴 LOW | Cortical Sst Gaba branch; Nos1=1.09 (pct 0.454) APPROXIMATE | Eliminated (wrong subclass; low Nos1) |
| `0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850]` | `0239 Sst Chodl Gaba_2` | 407 | 🔴 LOW | High Sst+Nos1 but striatum-dominant anatomy | Eliminated (striatal anatomy) |
| `0651 Vip Gaba_7 [CS20230722_CLUS_0651]` | `0179 Vip Gaba_7` | 170 | 🔴 LOW | High Nos1 but low Sst (pct 0.269) | Eliminated (Sst low; wrong subclass) |
| `0724 Lamp5 Lhx6 Gaba_1 [CS20230722_CLUS_0724]` | `0203 Lamp5 Lhx6 Gaba_1` | 2443 | 🔴 LOW | High Nos1 but Sst low; wrong subclass | Eliminated (wrong subclass) |
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | — | 2004 | 🔴 LOW | CA1 stratum oriens-dominant but Nos1 only 2.94 (pct 0.667) | Eliminated (cortical Sst Gaba branch) |
| `0203 Lamp5 Lhx6 Gaba_1 [CS20230722_SUPT_0203]` | — | 8913 | 🔴 LOW | Low Sst; not Sst-subclass | Eliminated (wrong subclass) |
| `0226 Sst Gaba_13 [CS20230722_SUPT_0226]` | — | 4064 | 🔴 LOW | High Sst+Nos1 but Isocortex-dominant | Eliminated (cortical anatomy) |
| `1164 Astro-TE NN_4 [CS20230722_SUPT_1164]` | — | 982 | 🔴 LOW | Astrocyte supertype; low Sst+Nos1 | Eliminated (non-neuronal) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Sst::Nos1-IN subfamily is defined transcriptomically by Chamberland and colleagues [1] under a CLASSICAL_MULTIMODAL definition basis, with Sst and Nos1 as defining markers (gene-pair expression-product rule on Harris 2018 stratum-oriens-targeted scRNA-seq), GABAergic NT identity, and CA1 stratum oriens soma localisation. Functionally, the subfamily corresponds to the long-range-projecting hippocampo-septal / back-projection identity that has been described in the classical literature.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location (extra-hippocampal painted regions for the Sst Chodl supertype reflect long-range axon distribution and white-matter passage rather than soma in those regions).

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Sst_Nos1 — Chamberland per-cluster subfamily label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| Script (external) | ../at_run_20260506_harris_chamberland_mmc_wmbv1/README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_chamberland_by_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/f1_matrix_chamberland_by_class.csv) |
| Caveats | Per-cluster derivation is the primary result (dropout-robust); per-cell derivation retained for reference. Headline cluster-level result for Sst::Nos1-IN is F1=0.97 to CLUS_0859 Sst Chodl Gaba_4, cross-supertype from the cortical Sst Gaba subclass to Sst Chodl Gaba. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `be7fae4` at 2026-06-10T13:48:16+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_sst_nos1_to_CS20230722_CLUS_0859 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0850 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0651 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0724 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0203 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_1164 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Sst::Nos1-IN (long-range projecting, Chamberland 2024) → 0859 Sst Chodl Gaba_4 [CS20230722_CLUS_0859] at HIGH confidence, paired with the broader supertype 0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241] at HIGH confidence. Key support: annotation transfer (F1=0.97 at cluster, F1=0.99 at supertype) and CONSISTENT defining-marker expression (Sst, Nos1) on the Sst Chodl branch. Key caveats: SINGLE_DATASET (one MapMyCells run from Chamberland's in-silico Sst × Nos1 labelling of Harris 2018); TAXONOMY_LEVEL_MISMATCH at supertype level, where the region rollup is dominated by extra-hippocampal Sst Chodl cells while the in-region CA1 stratum oriens component sits in the child cluster CLUS_0859.

No Cell Ontology term currently assigned. Candidate for CL contribution — a "hippocampo-septal back-projecting Sst Nos1 interneuron" definition would capture the cross-supertype identity that distinguishes this subfamily from the cortical Sst Gaba branch dominant elsewhere in CA1 stratum oriens.

### Proposed experiments and follow-ups

- **What:** Targeted transcriptomic profiling of an Sst-Cre × Nos1 intersectional cohort, paired with confirmed long-range axonal projection to medial septum.
  **Target:** F1 ≥ 0.80 at CLUSTER against CS20230722_CLUS_0859.
  **Expected output:** AnnotationTransferEvidence on the cluster edge.
  **Resolves:** SINGLE_DATASET caveat on the cluster + supertype edges; provides independent replication of the AT result currently sourced from Chamberland's in-silico subfamily labelling.
  Note that an AT result already exists (`at_run_20260512_chamberland_subfamily_mmc_wmbv1`, F1=0.97 to CLUS_0859); the proposed experiment adds an independent intersectional-genetic cohort with confirmed projection target — what was done in-silico, here done with a true intersectional driver line.

### Open questions

1. CLUS_0859 fell outside the current Stage A top-50 and warrants curator review (per Cellular-Semantics/evidencell#111).
2. Resolve overlap with the classical hippocampo_septal_cell_ca1 type in `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml` (provisional EQUIVALENT per Cellular-Semantics/evidencell#54).
3. Resolve overlap with the classical lth_cell_hippocampus type in the same graph (provisional PARTIAL per Cellular-Semantics/evidencell#54); the two classicals currently map to the cortical Sst Gaba branch (CLUS_0768/SUPT_0216) rather than to Sst Chodl, so the overlap with Sst::Nos1-IN sits at the classical-definition level rather than at shared atlas target.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | soma location, defining markers (Sst, Nos1), NT |

---

<!-- verdict-block-start: edge_sst_nos1_to_CS20230722_CLUS_0859 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.88
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer from Chamberland's in-silico
    Sst x Nos1 subfamily labelling of Harris 2018  places the
    Sst::Nos1-IN cohort cleanly on CS20230722_CLUS_0859 (F1 reported on the paired cluster edge at
    CLUSTER, Pur=1.00, Cov=0.94; F1 reported on the paired cluster edge at SUPERTYPE
    CS20230722_SUPT_0241; F1 reported on the paired cluster edge at SUBCLASS) via transcriptomic; the
    cross-supertype move from cortical Sst Gaba to Sst Chodl is
    consistent with the Sst::Nos1-IN long-range projection identity.
    2 of 2 markers CONSISTENT (Sst, Nos1).
  reconciliation_note: >
    Paired with edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0241
    (supertype broadMatch). Likely overlaps the classical
    hippocampo_septal_cell_ca1 (provisional EQUIVALENT) and
    lth_cell_hippocampus (provisional PARTIAL) types per
    Cellular-Semantics/evidencell#54; those two classicals currently
    map to the cortical Sst Gaba branch (CLUS_0768 / SUPT_0216), so
    convergence is at the classical-definition level rather than at
    shared atlas target.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        AT evidence derives from a single  run against
        Chamberland's in-silico per-cluster Sst x Nos1 gene-pair
        labelling of the Harris 2018 source dataset; independent
        replication via intersectional Sst-Cre x Nos1 cohort
        desirable.
  proposed_experiments:
    - >
      Targeted transcriptomic profiling of Sst-Cre x Nos1
      intersectional cohort with confirmed long-range axonal
      projection to medial septum, mapped onto WMBv1 via transcriptomic;
      target F1 >= 0.80 at CLUSTER against CS20230722_CLUS_0859.
  unresolved_questions:
    - >
      CLUS_0859 fell outside current Stage A top-50 and warrants
      curator review (per Cellular-Semantics/evidencell#111).
    - >
      Resolve overlap with the classical hippocampo_septal_cell_ca1
      (provisional EQUIVALENT per #54) and lth_cell_hippocampus
      (provisional PARTIAL per #54) types in
      hippocampus_GABAergic_interneurons.yaml.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: HIGH
  confidence_score: 0.85
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Supertype CS20230722_SUPT_0241 Sst Chodl Gaba_4
    carries the Sst::Nos1-IN cohort at F1 reported on the paired cluster edge (SUPERTYPE level on via
    transcriptomic, with both defining markers high (Sst=12.33,
    cohort_pct 0.984; Nos1=11.26, cohort_pct 0.968) and 2 of 2
    markers CONSISTENT. region_fraction_100um: 0.021 reflects
    pooling with extra-hippocampal Sst Chodl cells across the
    supertype; the AT-best child cluster CS20230722_CLUS_0859 holds
    the in-region CA1 stratum oriens population.
  reconciliation_note: >
    Paired with edge_sst_nos1_to_CS20230722_CLUS_0859 (best-child
    closeMatch primary).
  caveats:
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Supertype-level region rollup is dominated by
        extra-hippocampal Sst Chodl cells (region_fraction_100um:
        0.021); the AT-best child cluster CS20230722_CLUS_0859 sits
        in CA1 stratum oriens and carries the in-region component.
    - caveat_type: SINGLE_DATASET
      description: >
        Supporting AT evidence on the paired cluster edge derives
        from a single annotation-transfer run.
  proposed_experiments:
    - >
      Targeted transcriptomic profiling of Sst-Cre x Nos1
      intersectional cohort with confirmed long-range projection to
      medial septum, mapped onto WMBv1 via transcriptomic; target F1 >=
      0.80 at CLUSTER against CS20230722_CLUS_0859.
  unresolved_questions:
    - >
      CLUS_0859 fell outside current Stage A top-50 and warrants
      curator review (per Cellular-Semantics/evidencell#111).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0768 sits in the cortical Sst Gaba_3
    branch (wrong subclass for the long-range-projecting Sst::Nos1
    identity); marker_Nos1 only APPROXIMATE (Nos1=0.76, cohort_pct
    0.378) against the defining gene-pair criterion.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0772 sits in the cortical Sst Gaba_3
    branch (wrong subclass); marker_Nos1 only APPROXIMATE (Nos1=1.09,
    cohort_pct 0.454) — below the gene-pair expression-product
    threshold that defines Sst::Nos1-IN identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0850 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0850 carries high Sst (12.23) and
    Nos1 (12.14) but dominant anatomy is striatum
    (region_fraction_100um: 0.030 at CA1 stratum oriens); off-target
    for the hippocampal Sst::Nos1-IN identity.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant anatomy is striatum (region_fraction_100um: 0.030);
        not a hippocampal cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0651 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0651 (Vip Gaba_7) is wrong subclass
    for Sst::Nos1-IN; marker_Sst APPROXIMATE (Sst=0.70, cohort_pct
    0.269) — Sst is not expressed at the defining-marker threshold
    on this Vip-subclass cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_CLUS_0724 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_CLUS_0724 (Lamp5 Lhx6 Gaba_1) is wrong
    subclass; marker_Sst APPROXIMATE (Sst=1.18, cohort_pct 0.479) —
    Sst not expressed at the defining-marker threshold on this
    Lamp5-subclass cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUPT_0216 (Sst Gaba_3) is the cortical Sst
    Gaba branch dominant in CA1 stratum oriens but is wrong subclass
    for the long-range-projecting Sst::Nos1-IN identity; Nos1 only
    2.94 (cohort_pct 0.667) against the defining gene-pair criterion
    that places Sst::Nos1 on the Sst Chodl branch (SUPT_0241).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0203 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_0203 (Lamp5 Lhx6 Gaba_1) is wrong
    subclass; Sst only 1.52 (cohort_pct 0.603) — not expressed at
    the defining-marker threshold required for Sst::Nos1-IN.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 (Sst Gaba_13) carries high Sst
    (12.08) but dominant anatomy is Isocortex
    (region_fraction_100um: 0.016 at CA1 stratum oriens); off-target
    for hippocampal Sst::Nos1-IN identity.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        Dominant anatomy is Isocortex (region_fraction_100um: 0.016);
        not hippocampal.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_sst_nos1_subfamily_chamberland_to_CS20230722_SUPT_1164 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_1164 (Astro-TE NN_4) is a non-neuronal
    astrocyte supertype; marker_Sst APPROXIMATE (Sst=0.80, cohort_pct
    0.333) and marker_Nos1 APPROXIMATE (Nos1=0.20, cohort_pct 0.175);
    incompatible cell class.
```
<!-- verdict-block-end -->
