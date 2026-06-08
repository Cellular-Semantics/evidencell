# Trilaminar cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The trilaminar cell is a hippocampal GABAergic interneuron with soma in CA1 stratum oriens, distinguished by parvalbumin (Pvalb) and M2 muscarinic receptor (M2R / Chrm2) expression in the absence of somatostatin (Sst), and by its long-range axonal projection to the subiculum and medial septum. It is one of several morphologically and connectivity-defined PV+ interneuron classes that share stratum oriens as a soma layer; resolving its transcriptomic identity matters because its projection identity makes it functionally distinct from the locally arborizing PV basket and axo-axonic cells with which it co-occurs.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Markers | Pvalb, M2R (Chrm2) | — |
| Negative markers | Sst | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Katona et al. 2017 (Hippocampus) anchors the CA1 stratum oriens soma assignment for trilaminar cells [1].

No verbatim quotes are stored in the facts file for this node; marker and NT assignments lack primary citations on the classical node and are carried from cite-traverse stubs (see notes under Concerns).
</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Atlas metadata and a single broad-Pvalb annotation transfer run point to the Pvalb Gaba_2 supertype as the most defensible WMBv1 placement for the trilaminar cell, with cluster 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] as the leading child by stratum-oriens proximity (see figure and property comparison tables below). Confidence is LOW: the available source-label (broad Yao 2021 SMART-Seq Pvalb) cannot resolve trilaminar identity within the PV+ interneuron pool, the negative marker Sst is expressed above the classical absence call in every candidate (see candidates audit table), and the long-range projection phenotype is not assessable from atlas metadata or from any current evidence item on this node.

![Filtered AT figure for trilaminar cell](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Yao 2021 (GSE185862) SMART-Seq v4 Pvalb subclass source (n=66 hippocampal cells) mapped onto WMBv1 by cluster annotation transfer. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. The Pvalb subclass label is a heterogeneous pool of PV basket, axo-axonic, bistratified and other PV+ types; SUPT_0206 (Pvalb Gaba_2) receives 12 of 66 cells (F1=0.32, Purity=0.80) — consistent with trilaminar cells being one of several PV+ identities present in the source pool but not specifically resolved by this transfer.*

### 0206 Pvalb Gaba_2 · 🔴 LOW

**Property comparison (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | Hippocampal formation [MBA:1089] (count_100um=2145; painted); Field CA1 [MBA:382] (1559); Field CA1, stratum oriens [MBA:399] (1463) | CA1 stratum oriens cells dominant on 0737 (MBA:399 count_100um=614) | CONSISTENT (SUPT); APPROXIMATE (CLUS) |
| NT type | GABAergic | not asserted | GABA | NOT_ASSESSED (SUPT); CONSISTENT (CLUS) |
| Pvalb | defining marker | 1.48; cohort_pct 0.778; child-coverage 0.889 | 8.27 on CLUS_0737; cohort_pct 0.966 | CONSISTENT |
| M2R | defining marker | 2.51; cohort_pct 0.683; child-coverage 1.000 | 5.90 on CLUS_0737; cohort_pct 0.882 | CONSISTENT |
| Sst (negative) | absent | 11.44; cohort_pct 0.905 | 4.39 on CLUS_0737; cohort_pct 0.689 (atlas category: NEUROPEPTIDE) | DISCORDANT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(2 of 3 markers CONSISTENT at the supertype level; the negative marker Sst is DISCORDANT on the supertype mean but markedly lower on the best child CLUS_0737 than on the Sst-rich neighbours. Best match: CLUS_0737.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Pvalb Gaba_2 region + marker profile | Atlas metadata | PARTIAL | Pvalb=8.74, M2R=4.52 at supertype; stratum-oriens enriched | atlas-internal |
| Sst negative-marker cross-check | Atlas metadata | PARTIAL | Sst=2.72 at supertype (low but non-zero) | atlas-internal |
| Yao 2021 SSv4 Pvalb → WMBv1 (MapMyCells) | Annotation transfer | PARTIAL | F1=0.32; Purity=0.80; Coverage=0.18 (n=66 Pvalb cells) | atlas-internal |

**Supporting evidence.**

- Pvalb Gaba_2 is enriched in CA1 stratum oriens (493 cells) and CA3 stratum oriens (152 cells) per atlas metadata, matching the trilaminar cell's defining soma layer.
- Both defining markers are positive at supertype level (Pvalb 1.48 with child-coverage 0.889, M2R 2.51 with child-coverage 1.000) and strongly positive on the leading child CLUS_0737 (Pvalb 8.27; M2R 5.90).
- The Yao 2021 SMART-Seq Pvalb subclass transfers 12 of 66 hippocampal cells onto SUPT_0206 (F1=0.32, Purity=0.80) — Purity ≈ 0.8 means the cells that did land here are predominantly Pvalb-subclass, consistent with the trilaminar's PV identity, even though Coverage is modest because the source pool is heterogeneous.

**Concerns.**

- The Yao 2021 source label "Pvalb" is a mixed PV+ population — basket, axo-axonic, bistratified, and likely trilaminar all collapse onto it — so the transfer cannot identify trilaminar cells specifically; the F1=0.32 at the class level is the headline ceiling.
- Negative marker Sst is DISCORDANT at supertype (11.44) and modestly elevated on the best child (4.39). Some low-level Sst co-expression in Pvalb interneurons is documented, but values this high on the parent supertype suggest the supertype-mean is pulled up by an Sst-positive subset of children rather than supporting trilaminar identity directly.
- SUPT_0206 is the same supertype assigned to PV basket cells in this graph (per the AMBIGUOUS_MAPPING caveat on the edge); the supertype is not specific to trilaminar cells and likely contains multiple PV+ types.
- The discriminating biological feature — long-range projection to subiculum and medial septum — is not assessable from atlas metadata, precomputed expression, or the current SMART-Seq transfer.
- All defining markers on the classical node lack primary citations (Pvalb and M2R carry no `refs[]`), so concordance with the supertype's PV/Chrm2 profile is partly nominal — anchoring those markers to morphology-confirmed trilaminar studies (e.g. Katona et al. 2017) would strengthen the call.

**What would upgrade confidence.**

- A targeted annotation transfer from a dataset with morphology-confirmed or projection-confirmed trilaminar cells (retrograde labelling from subiculum/medial septum followed by patch-seq, or a Chrm2-Cre intersection with Pvalb-Flp) would resolve the subtype-specific identity that the broad Pvalb source cannot.
- Independent confirmation of M2R (Chrm2) and the Sst-absent profile on morphology-confirmed trilaminar cells would anchor the marker concordance to a primary study.
- Curator addition of a primary citation for Pvalb and M2R on the classical node would close the nominal-concordance gap.

### 0737 Pvalb Gaba_2 · 🔴 LOW

**Property comparison (Table 1).**

| Property | Classical | Cluster value | Alignment |
|---|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | Hippocampal formation [MBA:1089] count_100um=995; Field CA1 [MBA:382] count_100um=668; Field CA1, stratum oriens [MBA:399] count_100um=614 (`region_fraction_100um: 0.468`) | APPROXIMATE |
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb | defining marker | 8.27; cohort_pct 0.966 | CONSISTENT |
| M2R | defining marker | 5.90; cohort_pct 0.882 | CONSISTENT |
| Sst (negative) | absent | 4.39; cohort_pct 0.689 (atlas category: NEUROPEPTIDE) | DISCORDANT |
| Sex ratio | not documented | not assessed | NOT_ASSESSED |

*(Chrna2 not applicable here; on CLUS_0737 the AT-best child of SUPT_0206, Pvalb and M2R are present at 8.27 and 5.90 respectively, both above cohort 0.88 percentile; Sst at 4.39 is the discordant feature but lower than the supertype mean.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Stratum-oriens proximity scan | Atlas metadata | PARTIAL | region_fraction_100um=0.468; strict=0.280 | atlas-internal |

**Supporting evidence.**

- CLUS_0737 is the SUPT_0206 child whose soma distribution sits most heavily within Field CA1, stratum oriens [MBA:399] (614 cells at 100µm proximity) — the strongest stratum-oriens overlap available in the candidate set.
- Pvalb and M2R are both strongly positive (Pvalb 8.27, M2R 5.90), matching the classical defining markers.

**Concerns.**

- Sst is atlas-annotated as NEUROPEPTIDE on this cluster with a precomputed mean of 4.39, contradicting the trilaminar cell's defining Sst-negative status. The classical literature does not record Sst heterogeneity within trilaminar cells; this is unresolved counter-evidence.
- `region_fraction_100um: 0.468` is in the boundary band — soma centroids sit at the edge of the queried stratum-oriens region rather than centred inside it (registration scatter could account for the strict vs. proximity gap, but the cluster is not exclusively a stratum-oriens type).
- No projection-resolving or morphology-resolving evidence is available; cluster-level identity rests on metadata + precomputed expression only.
- Pairs with the SUPT_0206 verdict above — CLUS_0737 is the best-child representative of that supertype call.

**What would upgrade confidence.**

- Same projection-confirmed or morphology-confirmed dataset would anchor CLUS_0737 vs. its siblings (CLUS_0739, CLUS_0732 chandelier within SUPT_0204) more decisively.
- Re-querying expression at higher resolution (per-cell rather than cluster mean) would clarify whether the Sst=4.39 signal is a contaminating minority or a true bimodal pattern.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]` | — | 650 | 🔴 LOW | Pvalb/M2R+; AT F1=0.32 (mixed Pvalb source) | Primary (supertype broadMatch) |
| `0737 Pvalb Gaba_2 [CS20230722_CLUS_0737]` | 0206 Pvalb Gaba_2 | 170 | 🔴 LOW | Highest stratum-oriens proximity child of SUPT_0206 | Secondary (best-child closeMatch) |
| `0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732]` | 0204 Pvalb chandelier Gaba_1 | 309 | ⚪ UNCERTAIN | Pvalb/M2R+ but chandelier identity | Eliminated (wrong morphology type — chandelier) |
| `0704 RHP-COA Ndnf Gaba_6 [CS20230722_CLUS_0704]` | 0198 RHP-COA Ndnf Gaba_6 | 211 | ⚪ UNCERTAIN | M2R high but Pvalb=0.47 (transcript-level weak) | Eliminated (Pvalb not transcriptomically defining) |
| `0739 Pvalb Gaba_2 [CS20230722_CLUS_0739]` | 0206 Pvalb Gaba_2 | 55 | ⚪ UNCERTAIN | Sibling of CLUS_0737; lower stratum-oriens fraction | Eliminated (CLUS_0737 leads the supertype) |
| `0767 Sst Gaba_3 [CS20230722_CLUS_0767]` | 0216 Sst Gaba_3 | 104 | 🔴 REFUTED | Sst=10.78 + atlas-NEUROPEPTIDE | Eliminated (Sst-positive — contradicts defining negative) |
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | — | 2004 | 🔴 REFUTED | Sst=11.44 across supertype | Eliminated (Sst-positive supertype) |
| `0198 RHP-COA Ndnf Gaba_6 [CS20230722_SUPT_0198]` | — | 272 | ⚪ UNCERTAIN | Pvalb=0.23 (child-coverage 0.500) | Eliminated (Pvalb sparse at supertype) |
| `0212 Pvalb Gaba_8 [CS20230722_SUPT_0212]` | — | 7777 | 🔴 REFUTED | Isocortex-dominant; `region_fraction_100um: 0.053` | Eliminated (cortical, not hippocampal) |
| `0204 Pvalb chandelier Gaba_1 [CS20230722_SUPT_0204]` | — | 3470 | 🔴 REFUTED | Isocortex/olfactory areas; `region_fraction_100um: 0.065` | Eliminated (cortical chandelier, not hippocampal) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Trilaminar cell is defined here on multimodal classical criteria (`definition_basis: CLASSICAL_MULTIMODAL`): GABAergic NT, defining markers Pvalb and M2R (Chrm2), Sst as a defining negative marker, soma in CA1 stratum oriens [1]. Long-range projection to subiculum and medial septum is noted on the classical node but is not represented as a structured property.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4 cell type labels: Pvalb subclass, among others) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

The source-cluster label "Pvalb" is a heterogeneous pool of PV+ types (basket, axo-axonic, bistratified, trilaminar and likely others) at the SMART-Seq v4 subclass level. Subtype-specific resolution is not achievable from this run.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:38+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0737 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0732 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0704 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0739 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0767 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0198 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0212 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0204 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Trilaminar cell → 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] at LOW confidence (broadMatch + 1:n), with 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] as the best-child closeMatch within that supertype. Key support: Pvalb and M2R are both transcriptomically positive on the supertype and on the best-child cluster, with stratum-oriens enrichment in atlas metadata. Key caveats: AMBIGUOUS_MAPPING (the supertype is shared with PV basket cells and likely other PV+ types, and the available cluster annotation transfer source label cannot resolve trilaminar identity within the PV+ pool); MARKER_NOT_SPECIFIC (the long-range projection identity that defines the trilaminar cell is not assessable from atlas metadata, and the Sst negative-marker constraint is contradicted by the precomputed Sst values on every candidate).

No Cell Ontology term currently assigned. The trilaminar cell's combination of soma in stratum oriens, Pvalb+/M2R+/Sst−, and long-range projection to subiculum and medial septum is well-documented in classical literature [1] but does not match an existing CL class at the resolution required; this is a candidate for CL contribution.

### Proposed experiments and follow-ups

- **What:** Targeted annotation transfer from a morphology- or projection-confirmed trilaminar dataset (retrograde labelling from subiculum or medial septum + patch-seq, or a Chrm2-Cre × Pvalb-Flp intersection followed by single-cell sequencing). **Target:** F1 ≥ 0.75 at WMBv1 cluster level. **Expected output:** AnnotationTransferEvidence on the SUPT_0206 / CLUS_0737 edges (and on any sibling cluster the data argue for). **Resolves:** open question 1; would replace the current heterogeneous Yao 2021 Pvalb subclass transfer with a trilaminar-specific source.
- **What:** Curator literature trawl for primary citations on Pvalb and M2R expression in morphology-confirmed trilaminar cells (e.g. Somogyi-lab studies including Katona et al. 2017 [1]). **Target:** at least one PMID per defining marker on the classical node. **Expected output:** PropertySource entries on the classical node's marker objects. **Resolves:** open question 2.
- **What:** Targeted re-analysis of per-cell Sst expression in CLUS_0737 to determine whether the precomputed mean of 4.39 reflects a contaminating Sst-positive minority or a bimodal pattern, and whether Sst-expressing cells in CLUS_0737 are morphologically distinct from Sst-negative cells. **Target:** quantitative detection rate. **Expected output:** updated PropertyComparison and (if needed) a heterogeneity note on CLUS_0737. **Resolves:** open question 3.

The existing Yao 2021 MapMyCells run is already on file but does not address subtype-specific identity (heterogeneous source label), so a refined version with a trilaminar-specific source is required rather than a re-run with the same source.

### Open questions

1. Does the trilaminar cell map preferentially to SUPT_0206 (Pvalb Gaba_2) or to a sibling Pvalb supertype when assayed against a morphology/projection-confirmed source population?
2. Pvalb and M2R lack primary citations on the classical trilaminar node — does the gathered literature (Katona et al. 2017 [1] and the broader Somogyi-lab corpus) anchor both markers at transcript level on morphology-confirmed cells?
3. Is the precomputed Sst signal on CLUS_0737 (mean=4.39) driven by an Sst-positive contaminating subset or by genuine low-level co-expression across the cluster, and does either reading affect the trilaminar mapping call?
4. At the broader PV+ subclass level, AT alone cannot distinguish trilaminar cells from axo-axonic cells (markers and NT panels do not discriminate; only anatomical distribution differs modestly across CLAS_07) — what experimental panel would resolve them transcriptomically?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| 1 | Katona et al. 2017 · PMID:[27997999](https://pubmed.ncbi.nlm.nih.gov/27997999) | 27997999 | soma location |

---

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Pvalb and M2R both CONSISTENT on CS20230722_SUPT_0206
    (Pvalb child-coverage 0.889; M2R child-coverage 1.000) and the supertype
    is enriched in CA1 stratum oriens; cluster annotation transfer of the
    Yao 2021 SMART-Seq Pvalb subclass (run_ref at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1)
    places F1=0.12 on this supertype's class (CS20230722_CLAS_07), consistent with
    trilaminar identity being one of several PV+ types collapsed into the
    source label. 2 of 3 markers CONSISTENT; the negative marker Sst is
    DISCORDANT (Sst=11.44 at supertype). Best child within the supertype is
    CS20230722_CLUS_0737 (paired closeMatch verdict).
  reconciliation_note: >
    Paired with edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0737
    (best-child closeMatch). Pool candidate with axo_axonic_cell_hippocampus
    at the class level (CS20230722_CLAS_07): markers and nt panels do not
    distinguish the two source groups in the current evidence — AT-only
    indistinguishability (CASE B); cross-panel discrimination not assessed
    in the available data, so no lit_to_lit edge emitted.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_SUPT_0206 is shared with PV basket cells and likely
        other PV+ interneuron types in this graph; the cluster annotation
        transfer source label (Yao 2021 SMART-Seq Pvalb subclass) pools
        PV basket, axo-axonic, bistratified, and trilaminar identities
        and cannot resolve trilaminar specifically.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        The long-range projection identity to subiculum and medial septum
        — the defining feature of the trilaminar cell — is not assessable
        from atlas metadata, precomputed expression, or the current
        cluster annotation transfer.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Negative marker Sst is DISCORDANT (Sst=11.44 at the supertype),
        which weakens the Sst-absent constraint as a discriminator at
        this taxonomic level.
    - caveat_type: SINGLE_STUDY
      description: >
        Pvalb and M2R on the classical node lack primary citations; only
        soma location is anchored (Katona et al. 2017, PMID:27997999).
  proposed_experiments:
    - >
      Targeted cluster annotation transfer from a morphology- or
      projection-confirmed trilaminar dataset (retrograde labelling from
      subiculum or medial septum followed by patch-seq, or a Chrm2-Cre
      x Pvalb-Flp intersection) onto WMBv1; target F1 >= 0.75 at
      cluster level to confirm or revise the SUPT_0206 placement.
    - >
      Curator literature trawl for primary citations anchoring Pvalb and
      M2R on morphology-confirmed trilaminar cells; expected output
      PropertySource entries on the classical node's marker objects.
  unresolved_questions:
    - >
      Does the trilaminar cell map preferentially to CS20230722_SUPT_0206
      or to a sibling Pvalb supertype when assayed against a
      morphology/projection-confirmed source population?
    - >
      AT alone cannot distinguish the trilaminar source group from the
      axo_axonic source group at CS20230722_CLAS_07; what experimental
      panel would resolve them transcriptomically?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0737 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0737 is the child of CS20230722_SUPT_0206
    with the strongest stratum-oriens proximity (region_fraction_100um
    0.47) and Pvalb / M2R both CONSISTENT on the cluster
    (Pvalb=8.27 cohort_pct 0.97; M2R=5.90 cohort_pct 0.88).
    2 of 3 markers CONSISTENT; Sst=4.39 is DISCORDANT and atlas-
    annotated as NEUROPEPTIDE on this cluster, weakening the
    Sst-absent constraint.
  reconciliation_note: >
    Paired with edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206
    (parent supertype broadMatch). This is the best-child within
    SUPT_0206 by stratum-oriens overlap; CS20230722_CLUS_0739 is the
    sibling with the second-highest proximity but lower
    region_fraction_100um (0.39) and lower M2R (cohort_pct 0.93 vs
    0.88 here).
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_CLUS_0737 is one of several Pvalb children within
        CS20230722_SUPT_0206; the cluster has not been independently
        resolved as trilaminar-specific in the current evidence.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        The trilaminar cell's defining long-range projection to
        subiculum / medial septum is not represented in atlas
        metadata or precomputed expression on this cluster.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Sst=4.39 on this cluster contradicts the classical
        Sst-negative defining feature; the literature on the
        classical node does not record Sst heterogeneity within
        trilaminar cells, so the discordance is unresolved.
  proposed_experiments:
    - >
      Per-cell re-analysis of Sst expression on CS20230722_CLUS_0737
      to determine whether the cluster-mean value reflects a
      contaminating Sst-positive minority or genuine low-level
      co-expression; expected output a heterogeneity note plus
      potential revision of the Sst PropertyComparison.
  unresolved_questions:
    - >
      Is the CS20230722_CLUS_0737 Sst signal (mean=4.39) driven by an
      Sst-positive contaminating subset or by uniform low-level
      co-expression across the cluster?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0732 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0732 sits under the Pvalb chandelier
    supertype (0204 Pvalb chandelier Gaba_1); although Pvalb and M2R
    are CONSISTENT, the atlas-assigned chandelier-supertype identity
    is a distinct PV+ interneuron subtype from the trilaminar cell
    and not the trilaminar target.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_CLUS_0732 belongs to the Pvalb chandelier
        supertype, which is not the trilaminar identity even though
        the basic PV/M2R markers overlap.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0704 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] On CS20230722_CLUS_0704 Pvalb is only 0.47 (cohort_pct
    0.70), well below transcript-level "defining marker" thresholds
    seen on the Pvalb Gaba_2 candidates; M2R is high (10.26) but the
    Pvalb sparsity disqualifies this as a trilaminar candidate.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Pvalb at 0.47 on CS20230722_CLUS_0704 does not support
        defining-marker status; the cluster sits in an Ndnf
        subtype family rather than a Pvalb subtype family.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0739 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_CLUS_0739 is a sibling of CS20230722_CLUS_0737
    within CS20230722_SUPT_0206 but has lower stratum-oriens
    proximity (region_fraction_100um 0.39 vs 0.47) and smaller cell
    count (55 vs 170); CS20230722_CLUS_0737 leads the supertype as
    best child.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_CLUS_0739 is one of several Pvalb Gaba_2 children;
        CS20230722_CLUS_0737 dominates the stratum-oriens overlap and
        carries the best-child verdict for trilaminar.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_CLUS_0767 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_CLUS_0767 belongs to CS20230722_SUPT_0216
    (Sst Gaba_3) and shows Sst=10.78 (atlas-annotated NEUROPEPTIDE);
    Sst-positive identity directly contradicts the trilaminar cell's
    defining Sst-negative marker.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        CS20230722_CLUS_0767 is Sst-positive at a level inconsistent
        with the trilaminar classical definition (Sst absent).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0216 (Sst Gaba_3) shows Sst=11.44
    across the supertype, contradicting the trilaminar cell's
    defining Sst-negative status; this is the OLM / Sst-interneuron
    supertype rather than a PV-interneuron supertype.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        CS20230722_SUPT_0216 is a Sst-positive supertype, inconsistent
        with the trilaminar Sst-negative defining feature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0198 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0198 (RHP-COA Ndnf Gaba_6) carries
    Pvalb=0.23 at supertype with child-coverage 0.500, indicating
    Pvalb is sparse and not a defining feature; M2R is high but
    Pvalb sparsity disqualifies the supertype as a trilaminar
    candidate.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Pvalb at 0.23 on CS20230722_SUPT_0198 with child-coverage
        0.500 fails the trilaminar defining-marker test.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0212 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0212 (Pvalb Gaba_8) is cortical:
    Isocortex count_100um=6762 dominates with region_fraction_100um
    0.05, well below boundary band; cortical PV interneurons are
    not the hippocampal trilaminar target even though Pvalb and
    M2R are positive.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0212 soma distribution is dominated by
        Isocortex; region_fraction_100um 0.053 is below boundary
        scatter and indicates a non-hippocampal cell population.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0204 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0204 (Pvalb chandelier Gaba_1) is
    cortical and olfactory-area dominated (region_fraction_100um
    0.065); chandelier-cell identity and non-hippocampal anatomy
    both disqualify it as a trilaminar candidate.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0204 is dominated by Isocortex and
        olfactory areas, with region_fraction_100um 0.065 well
        below the hippocampal-region threshold.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CS20230722_SUPT_0204 is the Pvalb chandelier supertype,
        which is morphologically distinct from the trilaminar
        cell.
```
<!-- verdict-block-end -->
