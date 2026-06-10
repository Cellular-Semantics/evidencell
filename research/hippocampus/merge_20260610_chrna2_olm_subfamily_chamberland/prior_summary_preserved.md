# Chrna2-IN (Chrna2-OLM, Chamberland 2024) — WMBv1 Mapping Report
*2026-05-12 · Source: `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`*

---

## Introduction

The Chrna2-IN subfamily is a genetically defined subset of CA1 *stratum oriens* somatostatin interneurons, isolated in Chamberland et al. 2024 by intersectional Sst-Flp; Chrna2-Cre targeting. The classical literature places these cells deep in the oriens/alveus border with axons projecting to *stratum lacunosum-moleculare* — the canonical morphology associated with OLM cells. The Chamberland labelling thus carves out a transcriptomically and genetically defined fraction of the broader OLM population [1].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] (named in source as "CA1 stratum oriens") | [1] |
| NT | GABAergic | [1] |
| Markers | Sst (defining); Chrna2 (defining) | [1] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Chamberland et al. 2024 · [1]
  > While Sst;;Tac1-INs were located closer to the CA1 pyramidal layer, Ndnf;;Nkx2-1-INs and Chrna2-INs were found progressively deeper in O/A
  > — Chamberland et al. 2024, Results · [1] <!-- quote_key: 269246896_1b1ebab4 -->
- **Defining context:** Chamberland et al. 2024 · [1]
  > genetically distinct subfamilies of Sst-INs form specialized circuits in the hippocampus.
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [1] <!-- quote_key: 269246896_c87fdbd0 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer of Chamberland-criterion Chrna2-IN cells onto WMBv1 places the subfamily on the Sst Gaba_3 supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (F1=0.33; coverage 0.95) with the highest-resolution call concentrating on cluster 0771 Sst Gaba_3 [CS20230722_CLUS_0771] (F1=0.65, coverage 0.81; see figure). The supertype-level low purity reflects multiple Sst Gaba_3 children sharing this Cre-marked label, with one cluster — 0771 Sst Gaba_3 [CS20230722_CLUS_0771] — clearly leading at cluster resolution.

![Filtered AT figure for Chrna2-IN (Chrna2-OLM, Chamberland 2024)](figures/f1_for_chrna2_olm_subfamily_chamberland.png)

*F1 across taxonomy levels for the Chrna2 source group (Chamberland per-cluster subfamily label applied to Harris 2018 cells; n=153). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. The cluster-level peak at 0771 Sst Gaba_3 (F1=0.65) is the principal mapping; supertype-level scatter into other Sst Gaba_3 children dampens 0216 Sst Gaba_3's purity.*

The mapping holds at *stratum oriens* (region_fraction_100um: 0.45 at cluster 0771 Sst Gaba_3 [CS20230722_CLUS_0771]; 0.54 at supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216]) and is supported by concordant defining marker expression for both Sst and Chrna2 (see property comparison table for each survivor below).

### 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

The parent supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] captures the Chrna2-IN cohort with high coverage but low purity (F1=0.33; coverage 0.95; purity 0.20) — the population scatters across multiple Sst Gaba_3 children, only one of which (0771 Sst Gaba_3 [CS20230722_CLUS_0771]) leads at cluster resolution. The supertype is the right resolution at which to claim a broad mapping: Chrna2-IN cells are Sst Gaba_3 cells, but the supertype itself contains additional Sst+ populations that the Chamberland labelling does not address.

**Table 1 — Property comparison (supertype level).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | Hippocampal formation [MBA:1089] / Field CA1 [MBA:382] / Field CA1, stratum oriens [MBA:399]; region_fraction_100um: 0.539 | Field CA1, stratum oriens [MBA:399]; region_fraction_100um: 0.454 (CLUS_0771) | CONSISTENT |
| NT type | GABAergic | not asserted | GABA | NOT_ASSESSED at supertype |
| Sst expression | defining marker | 11.44 (cohort_pct 0.905; child-coverage 1.000) | 11.62 (cohort_pct 0.924; CLUS_0771) | CONSISTENT |
| Chrna2 expression | defining marker | 0.61 (cohort_pct 0.952; child-coverage 0.667) | 2.56 (cohort_pct 0.992; CLUS_0771) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(2 of 3 child clusters in 0216 Sst Gaba_3 [CS20230722_SUPT_0216] show detectable Chrna2; the supertype-mean Chrna2 value of 0.61 is driven by the Chrna2-high child 0771 Sst Gaba_3 [CS20230722_CLUS_0771]. Best match: 0771 Sst Gaba_3 [CS20230722_CLUS_0771].)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| MapMyCells AT (subfamily relabel) | Annotation transfer | PARTIAL | supertype F1=0.33; cluster F1=0.65 (via paired CLUS_0771 edge) | atlas-internal |
| Atlas precomputed expression | Atlas metadata | PARTIAL | Sst 11.44; Chrna2 0.61 | atlas-internal |

**Supporting evidence:**
- Atlas-side soma location concentrates in Field CA1, stratum oriens [MBA:399] (region_fraction_100um: 0.539; strict region_fraction: 0.305), matching the classical *stratum oriens* placement.
- Sst is a defining marker on both sides; the supertype carries the Sst NEUROPEPTIDE annotation in WMBv1 metadata.
- Chrna2, the diagnostic marker for this subfamily, is detectable at the supertype with cohort_pct 0.952; child-cluster coverage 0.667 indicates Chrna2 is concentrated in a minority of children rather than uniform across 0216 Sst Gaba_3 [CS20230722_SUPT_0216].

**Marker evidence provenance:**
- **Sst** — transcript-level expression evidence on supertype matches the Chamberland classical assertion; cohort percentile 0.905 places it among the high-Sst supertypes.
- **Chrna2** — defining_marker concordance on the supertype is partially nominal: only one of the three children carries Chrna2 at robust levels (0771 Sst Gaba_3 [CS20230722_CLUS_0771]). This is the HIDDEN-1:1 signature — the supertype-mean is driven by a subset of children; the cluster-level resolution is the right one for this label.

**Concerns:**
- Low purity (0.20) at supertype level is the dominant counter-signal; cells of other Sst Gaba_3 children that are *not* Chrna2-IN inflate the denominator. The supertype is a broad match, not a clean one.
- NT type is `not asserted` at supertype level in the atlas YAML — alignment is NOT_ASSESSED rather than CONSISTENT; the child cluster carries `GABA`.

**What would upgrade confidence:**
- Drilling subfamily labels into other Sst Gaba_3 children would clarify whether the residual cells under 0216 Sst Gaba_3 [CS20230722_SUPT_0216] correspond to Sst::Tac1-IN / Sst::Nos1-IN / Ndnf::Nkx2-1-IN subfamilies. The companion `at_run_20260512_chamberland_subfamily_mmc_wmbv1` already scores other subfamilies under this same MMC output.

### 0771 Sst Gaba_3 [CS20230722_CLUS_0771] · 🟡 MODERATE

Cluster-level annotation transfer of Chamberland Chrna2-IN cells concentrates on 0771 Sst Gaba_3 [CS20230722_CLUS_0771] (F1=0.65; coverage 0.81; purity 0.54; n=74 cells mapped from a source pool of n=153 Chrna2-rule-positive cells), with Chrna2 expression on the atlas-side cluster at val=2.56 (cohort_pct 0.992) — the highest Chrna2 value among the assessed Sst Gaba_3 children. This is the highest-resolution clean call for the subfamily.

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | hippocampus stratum oriens [UBERON:0005371] | (see supertype row) | Field CA1, stratum oriens [MBA:399] count_100um=179; region_fraction_100um: 0.454; strict region_fraction: 0.239 | APPROXIMATE |
| NT type | GABAergic | not asserted | GABA | CONSISTENT |
| Sst expression | defining marker | 11.44 (cohort_pct 0.905) | 11.62 (cohort_pct 0.924) | CONSISTENT |
| Chrna2 expression | defining marker | 0.61 (cohort_pct 0.952) | 2.56 (cohort_pct 0.992) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(0771 Sst Gaba_3 [CS20230722_CLUS_0771] is the AT-best child of 0216 Sst Gaba_3 [CS20230722_SUPT_0216]; the parent supertype is also a survivor (paired) — the supertype edge encodes the broad relationship, this cluster edge encodes the principal cluster-level call.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| MapMyCells AT (Chamberland subfamily relabel) | Annotation transfer | SUPPORT | F1=0.65 at cluster; recall 0.81 | atlas-internal |
| Atlas precomputed expression | Atlas metadata | PARTIAL | Sst 11.62; Chrna2 2.56 | atlas-internal |

**Supporting evidence:**
- MapMyCells (cell_type_mapper v1.7.1; raw normalization; bootstrap_iteration=100) under `at_run_20260512_chamberland_subfamily_mmc_wmbv1` places 74 of 91 cluster-resolution mapped Chrna2-IN cells onto 0771 Sst Gaba_3 [CS20230722_CLUS_0771]; F1=0.65, recall 0.81, precision 0.54.
- Chrna2 atlas-side value of 2.56 on 0771 Sst Gaba_3 [CS20230722_CLUS_0771] (cohort percentile 0.992) is several-fold higher than on any other Sst Gaba_3 child cluster (CLUS_0768: 0.57; CLUS_0770: 0.52; CLUS_0772: 0.46; CLUS_0773: 0.65). Chrna2 is present on CLUS_0771 in a manner consistent with the Chamberland labelling criterion (Sst+/Chrna2+ > 0).
- Sst expression (val=11.62; cohort_pct 0.924) confirms the cluster carries the broader Sst-IN identity.
- Atlas soma location places the cluster predominantly in *stratum oriens* (region_fraction_100um: 0.454).

**Marker evidence provenance:**
- **Sst** — atlas category NEUROPEPTIDE; transcript-level expression on the cluster is high. The Chamberland classical assertion is anchored in Sst-Flp targeting, which intersects this annotation directly.
- **Chrna2** — transcript-level expression confirmation is the discriminator for this cluster among the Sst Gaba_3 children: val=2.56 vs ≤0.65 elsewhere in 0216 Sst Gaba_3 [CS20230722_SUPT_0216]. The marker is not in the WMBv1 atlas DEFINING tag set for CLUS_0771 (no atlas category label was emitted), but the precomputed expression is decisive.

**Concerns:**
- Location alignment is APPROXIMATE rather than CONSISTENT: `region_fraction_100um: 0.454` is in the boundary band, with strict `region_fraction: 0.239` — boundary scatter at the *stratum oriens* edge. The cluster is anchored in CA1 oriens but some cells sit at the registration boundary; could reflect MERFISH registration error or true distribution across adjacent CA1 layers; weak counter-evidence.
- Precision 0.54 at cluster level means roughly half the cells in 0771 Sst Gaba_3 [CS20230722_CLUS_0771] are not Chrna2-rule-positive under the Chamberland per-cluster criterion — the cluster contains additional Sst+ cells beyond the Chrna2-IN subfamily.

**What would upgrade confidence:**
- Patch-seq evidence on Chrna2-Cre-targeted OLM cells with morphological recovery, mapped against CCN20230722 at cluster resolution, would directly anchor the Chamberland subfamily to 0771 Sst Gaba_3 [CS20230722_CLUS_0771] (target: F1 ≥ 0.80 at cluster level, AnnotationTransferEvidence).
- Marker panel re-analysis confirming that the ~46% non-Chrna2-rule cells in CLUS_0771 are technical-dropout Chrna2 cases rather than a co-resident non-OLM Sst type.

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | (self) | 2004 | 🟡 MODERATE | AT supertype F1=0.33, coverage 0.95 | Primary (supertype) |
| 0771 Sst Gaba_3 [CS20230722_CLUS_0771] | 0216 Sst Gaba_3 | 462 | 🟡 MODERATE | AT cluster F1=0.65; Chrna2 cohort_pct 0.992 | Primary (cluster) |
| 0768 Sst Gaba_3 [CS20230722_CLUS_0768] | 0216 Sst Gaba_3 | 66 | 🔴 LOW | AT F1=0.07; Chrna2=0.57 | Eliminated (Chrna2 low; AT scatter) |
| 0770 Sst Gaba_3 [CS20230722_CLUS_0770] | 0216 Sst Gaba_3 | 404 | 🔴 LOW | Chrna2=0.52; not AT-supported | Eliminated (Chrna2 low; not AT-best) |
| 0772 Sst Gaba_3 [CS20230722_CLUS_0772] | 0216 Sst Gaba_3 | 190 | 🔴 LOW | Chrna2=0.46; AT F1=0.014 | Eliminated (Chrna2 low; AT scatter) |
| 0773 Sst Gaba_3 [CS20230722_CLUS_0773] | 0216 Sst Gaba_3 | 156 | 🔴 LOW | Chrna2=0.65; AT F1=0.11 | Eliminated (not AT-best) |
| 0226 Sst Gaba_13 [CS20230722_SUPT_0226] | (self) | 4064 | 🔴 LOW | location DISCORDANT (Isocortex / endopiriform) | Eliminated (wrong region) |
| 0217 Sst Gaba_4 [CS20230722_SUPT_0217] | (self) | 14335 | 🔴 LOW | location DISCORDANT (Isocortex / motor cortex) | Eliminated (wrong region) |
| 0224 Sst Gaba_11 [CS20230722_SUPT_0224] | (self) | 2677 | 🔴 LOW | location DISCORDANT (Isocortex-dominant) | Eliminated (wrong region) |
| 0225 Sst Gaba_12 [CS20230722_SUPT_0225] | (self) | 2126 | 🔴 LOW | location DISCORDANT (entorhinal-dominant) | Eliminated (wrong region) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Chamberland 2024 Chrna2-IN subfamily is defined by intersectional Sst-Flp; Chrna2-Cre genetics (definition_basis: CLASSICAL_MULTIMODAL), with somata in CA1 *stratum oriens* deep band [1]; defining markers Sst and Chrna2 [1]; GABAergic NT [1]. Chamberland 2024 describes this as a genetically isolated subset of the canonical OLM population.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Chrna2 — Chamberland per-cluster subfamily label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_chamberland_by_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/f1_matrix_chamberland_by_class.csv) |
| Caveats | Per-cluster derivation is the primary result (gene-pair rules applied to Harris cluster-mean expression, dropout-robust). Per-cell derivation is retained but subject to scRNA-seq dropout on the gene-pair markers. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:45+00:00 from [kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml](kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml).*

**Evidence base.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_chrna2_olm_to_CS20230722_CLUS_0771 | ANNOTATION_TRANSFER | SUPPORT | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0771 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0217 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0224 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0225 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Chrna2-IN (Chrna2-OLM, Chamberland 2024) → 0771 Sst Gaba_3 [CS20230722_CLUS_0771] at MODERATE confidence, with a paired supertype broad mapping to 0216 Sst Gaba_3 [CS20230722_SUPT_0216]. Key support: annotation transfer of Chamberland-criterion Chrna2-IN cells (cluster F1=0.65; supertype coverage 0.95) plus precomputed Chrna2 expression on CLUS_0771 (val=2.56; cohort_pct 0.992) that is several-fold higher than on any sibling Sst Gaba_3 cluster. Key caveats: boundary-band soma location (region_fraction_100um: 0.454 at CLUS_0771) and supertype-level low purity (0.20) driven by other Sst Gaba_3 children that are not Chrna2-IN.

No Cell Ontology term currently assigned. Candidate for CL contribution as a Chrna2-defined subset of the OLM cell population.

### Proposed experiments and follow-ups

- **Patch-seq targeting Chrna2-Cre-marked oriens INs** — Target: F1 ≥ 0.80 at CLUSTER resolution against CCN20230722. Expected output: AnnotationTransferEvidence anchoring the Chamberland subfamily to 0771 Sst Gaba_3 [CS20230722_CLUS_0771] with morphology-confirmed OLM identity. Resolves: cluster-level precision question; subfamily-to-cluster identity.
- **Subfamily breakdown across other Sst Gaba_3 children** — Target: re-score Sst::Tac1, Sst::Nos1, and Ndnf::Nkx2-1 Chamberland subfamilies against CLUS_0768/0770/0772/0773 using the existing `at_run_20260512_chamberland_subfamily_mmc_wmbv1` output. Expected output: AnnotationTransferEvidence for sibling subfamilies that would clarify the supertype-level purity gap. Resolves: open question 2.

### Open questions

1. Are the ~46% of cells in 0771 Sst Gaba_3 [CS20230722_CLUS_0771] that are not Chamberland-rule-positive a technical-dropout artefact of the Sst+/Chrna2+ gene-pair criterion, or a co-resident non-Chrna2 OLM subset?
2. Which of the other Sst Gaba_3 children of 0216 Sst Gaba_3 [CS20230722_SUPT_0216] correspond to other Chamberland subfamilies (Sst::Tac1, Sst::Nos1, Ndnf::Nkx2-1)?
3. Curator removal of duplicate edge `edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0771` — legacy/fresh-emit ID collision on taxonomy_type CS20230722_CLUS_0771; the AT-bearing edge `edge_chrna2_olm_to_CS20230722_CLUS_0771` should be the surviving record.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland et al. 2024 · PMID:[38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | 38640347 | soma location, defining markers, NT, classical-type definition |

---

<!-- verdict-block-start: edge_chrna2_olm_to_CS20230722_CLUS_0771 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer of Chamberland Chrna2-IN cells under
    at_run_20260512_chamberland_subfamily_mmc_wmbv1 places the subfamily on
    CS20230722_CLUS_0771 (F1=0.65, coverage 0.81, purity 0.54); Chrna2
    precomputed expression on this cluster (2.56; cohort_pct 0.992) is
    several-fold higher than on sibling Sst Gaba_3 clusters under
    CS20230722_SUPT_0216, and Sst (11.62) confirms the broader Sst-IN
    identity. 2 of 2 markers CONSISTENT. region_fraction_100um: 0.454
    indicates boundary scatter at the stratum oriens edge — registration
    imprecision rather than off-target.
  reconciliation_note: >
    Paired with the supertype edge to CS20230722_SUPT_0216 (skos:broadMatch
    + 1:n); this cluster edge carries the principal cluster-level call.
    Legacy/fresh-emit duplicate edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0771
    targets the same accession with only ATLAS_METADATA; flagged for
    curator removal.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        Annotation transfer evidence rests on a single source dataset
        (GEO:GSE99888) re-labelled under Chamberland's gene-pair rule;
        no independent dataset replicates the F1=0.65 to CS20230722_CLUS_0771.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Soma location alignment is APPROXIMATE: region_fraction_100um: 0.454
        with strict region_fraction: 0.239 indicates boundary scatter at the
        stratum oriens edge.
  proposed_experiments:
    - >
      Targeted profiling on Chrna2-Cre-labelled oriens interneurons,
      pairing functional and morphological characterisation with
      single-cell transcriptomics, with the resulting transcriptomes
      mapped against CCN20230722; target F1 ≥ 0.80 at CLUSTER level on
      CS20230722_CLUS_0771.
    - >
      Re-score Sst::Tac1-IN, Sst::Nos1-IN, and Ndnf::Nkx2-1-IN Chamberland
      subfamilies against sibling Sst Gaba_3 clusters under
      CS20230722_SUPT_0216 using existing
      at_run_20260512_chamberland_subfamily_mmc_wmbv1 output.
  unresolved_questions:
    - >
      Are the ~46% of cells in CS20230722_CLUS_0771 that are not
      Chamberland-rule-positive a scRNA-seq dropout artefact of the Sst+/Chrna2+
      gene-pair criterion, or a co-resident non-Chrna2 OLM subset?
    - >
      Curator removal of duplicate edge
      edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0771 —
      legacy/fresh-emit ID collision on taxonomy_type CS20230722_CLUS_0771.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_SUPT_0216 is the Sst Gaba_3 supertype parent
    of CS20230722_CLUS_0771, the cluster carrying the Chrna2-high
    signature for the Chamberland Chrna2-IN subfamily (see paired cluster
    edge edge_chrna2_olm_to_CS20230722_CLUS_0771 for the AT-bearing
    record). At supertype the Chrna2-IN identity is diluted because
    multiple Sst Gaba_3 children share this supertype while only
    CS20230722_CLUS_0771 carries the Chrna2-high signature. 2 of 2
    markers CONSISTENT (Sst 11.44, Chrna2 0.61). Chrna2 child-coverage
    0.667 is the HIDDEN-1:1 signature — supertype mean is driven by a
    minority of children. region_fraction_100um: 0.539 places the
    supertype centroid in Field CA1 stratum oriens.
  reconciliation_note: >
    Paired with the cluster edge edge_chrna2_olm_to_CS20230722_CLUS_0771
    (skos:closeMatch + 1:1); this supertype edge encodes the broad
    relationship to the Sst Gaba_3 supertype as a whole.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        Cells of the Chrna2-IN subfamily concentrate on CS20230722_CLUS_0771
        but cluster-level scatter into other Sst Gaba_3 children under
        CS20230722_SUPT_0216 dampens supertype purity to 0.20.
    - caveat_type: SINGLE_DATASET
      description: >
        Supertype-level evidence rests on the same single source dataset
        (GEO:GSE99888) re-labelled under Chamberland's gene-pair rule.
  proposed_experiments:
    - >
      Subfamily-resolved annotation transfer of the remaining Chamberland
      labels against CS20230722_SUPT_0216 children, to verify that
      residual non-Chrna2 cells correspond to other Sst-IN subfamilies and
      not unrelated populations.
  unresolved_questions:
    - >
      Which sibling clusters of CS20230722_CLUS_0771 within
      CS20230722_SUPT_0216 carry the Sst::Tac1, Sst::Nos1, and
      Ndnf::Nkx2-1 Chamberland subfamilies?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0768 carries low Chrna2 (0.57) compared to
    the AT-best CS20230722_CLUS_0771 (2.56), and the Chamberland-labelled
    AT signal at this cluster is negligible — not the cluster carrying
    the Chrna2-IN identity within CS20230722_SUPT_0216.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0772 carries low Chrna2 (0.46) relative to
    the AT-best CS20230722_CLUS_0771 (2.56); Chamberland-labelled AT signal
    on this cluster is minimal. Sibling Sst Gaba_3 cluster, not the
    Chrna2-IN home.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0773 shows Chrna2=0.65 — well below
    CS20230722_CLUS_0771 (2.56) — and Chamberland-labelled AT signal on
    this cluster is non-leading. Sibling under CS20230722_SUPT_0216, not
    the Chrna2-IN home.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0770 carries low Chrna2 (0.52) compared
    with CS20230722_CLUS_0771 (2.56) and shows no leading
    Chamberland-labelled AT signal. Sibling Sst Gaba_3 cluster, not the
    Chrna2-IN home.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_CLUS_0771 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  rationale: >
    [tier:CUT] Legacy/fresh-emit duplicate edge targeting
    CS20230722_CLUS_0771; the substantive AT-bearing record lives on
    edge_chrna2_olm_to_CS20230722_CLUS_0771 (skos:closeMatch). This edge
    carries only ATLAS_METADATA and should be retired by the curator.
  reconciliation_note: >
    Duplicate of edge_chrna2_olm_to_CS20230722_CLUS_0771 on the same
    taxonomy_type accession.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 soma distribution is DISCORDANT with
    classical CA1 stratum oriens — region_fraction_100um: 0.016 with the
    bulk of cells in Isocortex and endopiriform regions. Marker
    concordance is nominal (Sst+/Chrna2+) but the supertype is a cortical
    Sst-IN population, not the hippocampal one.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0217 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0217 soma distribution is DISCORDANT —
    region_fraction_100um: 0.015 with cells dominated by Isocortex
    (motor areas). Cortical Sst-IN supertype, not the hippocampal
    Chrna2-IN home.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0224 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0224 soma distribution is DISCORDANT —
    region_fraction_100um: 0.032 with Isocortex-dominated location.
    Chrna2 atlas-side value (0.10) is also marginal. Cortical Sst-IN
    population, not the hippocampal Chrna2-IN home.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_chrna2_olm_subfamily_chamberland_to_CS20230722_SUPT_0225 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0225 soma distribution is DISCORDANT —
    region_fraction_100um: 0.017 with cells dominated by entorhinal
    cortex. Chrna2 atlas-side (0.23) is low. Entorhinal Sst-IN
    population, not the hippocampal Chrna2-IN home.
```
<!-- verdict-block-end -->
