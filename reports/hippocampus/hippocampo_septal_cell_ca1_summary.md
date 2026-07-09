# Hippocampo-septal (HS) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The hippocampo-septal (HS) cell is a GABAergic, somatostatin-expressing interneuron with somata in CA1 stratum oriens [UBERON:0014552] and a long-range axonal projection to the medial septum. It is one of the two principal SST+ interneuron classes in CA1 (alongside the OLM cell), and is of interest because its mapping to a transcriptomic taxonomy bears directly on whether long-range projecting SST+ interneurons constitute a hippocampal-specific cell type or share identity with the cortical Sst Chodl population.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1], [2], [3], [4] |
| NT | GABAergic | — |
| Defining markers | Sst | [1], [5], [6] |
| Neuropeptides | Sst | — |
| CL term | sst chodl GABAergic interneuron [CL:4023121] (RELATED) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Sst marker / soma location:**
  > SST+ cells were mainly found close to the alveus in the stratum-oriens of CA1 of both SAMR1 and SAMP8
  > — Lagartos-Donate et al. 2019, Molecular Markers and Gene Expression · [1] <!-- quote_key: 132515344_fb36f967 -->

- **Mixed-population caveat for CA1 stratum oriens horizontal interneurons:**
  > horizontal interneurons in stratum oriens of the hippocampal CA1 area are often studied as a single group of interneurons, they include several cell types in addition to O-LM cells
  > — Oren et al. 2009, Conclusions · [4] <!-- quote_key: 1015389_2738d858 -->

</details>

Cell Ontology mapping: sst chodl GABAergic interneuron [[CL:4023121](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023121)] (RELATED).

---

## Results

Marker expression and soma-location alignment from atlas precomputed expression and MERFISH-derived spatial counts in WMBv1 (CCN20230722) support a broad mapping of the HS cell to the supertype 0216 Sst Gaba_3 [CS20230722_SUPT_0216] (Sst cohort-percentile 0.905; CA1 stratum oriens region_fraction_100um=0.539), with the in-region child cluster 0768 Sst Gaba_3 [CS20230722_CLUS_0768] as the highest-region-fraction candidate (region_fraction_100um=0.818). Cluster annotation transfer of the Yao 2021 Sst subclass cells onto WMBv1 reaches the Sst Gaba subclass (F1=0.98) but does not resolve below subclass to discriminate the HS cell from OLM, bistratified, or other Sst+ CA1 oriens types (see candidates audit table for full top-K).

### Property alignment — 0216 Sst Gaba_3 [CS20230722_SUPT_0216] · 🟡 MODERATE

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | Hippocampal formation [MBA:1089] / Field CA1 [MBA:382] / Field CA1, stratum oriens [MBA:399] (region_fraction_100um=0.539) | Field CA1, stratum oriens [MBA:399] (region_fraction_100um=0.818, CLUS_0768) | CONSISTENT |
| NT type | GABAergic | not asserted | GABA (CLUS_0768) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Sst expression | defining marker | 11.44; cohort_pct 0.905 | 12.70; cohort_pct 0.992 (CLUS_0768) | CONSISTENT |
| Sst neuropeptide | classical neuropeptide | 11.44; cohort_pct 0.905 | 12.70; cohort_pct 0.992 (CLUS_0768; atlas category: NEUROPEPTIDE) | CONSISTENT |

*(6 of 6 child clusters of Sst Gaba_3 audited at rank 0 — all CA1-stratum-oriens-resident at region_fraction_100um ≥ 0.5 and all CONSISTENT for Sst at cohort_pct ≥ 0.8. Best in-region match: CLUS_0768 at region_fraction_100um=0.818.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH spatial | Atlas metadata | PARTIAL | Sst+, CA1 SO, Reln-DEFINING (OLM-overlap) | atlas-internal |
| Yao 2021 SSv4 Sst subclass → WMBv1 AT | Annotation transfer | PARTIAL | F1=0.49 (best level: subclass F1=0.98) | atlas-internal |

### 0216 Sst Gaba_3 — supporting evidence

- **Soma location:** WMBv1 painted MERFISH counts place SUPT_0216 predominantly in CA1 stratum oriens [MBA:399] with `region_fraction_100um: 0.539`, consistent with the HS soma location.
- **Sst expression:** SUPT_0216 sits in the 0.905 cohort-percentile for Sst (val=11.44) within the GABAergic CA1-stratum-oriens cohort (n_members=50); child-cluster coverage is 1.000, meaning every Sst Gaba_3 child cluster carries the marker — Sst is a uniform property of this supertype.
- **Cluster annotation transfer:** local MapMyCells transfer of the Yao 2021 (GEO:GSE185862) SMART-Seq v4 mouse hippocampal formation Sst subclass cells onto WMBv1 reaches Sst Gaba subclass at F1=0.98 (n=265 of 273 cells); at supertype level SUPT_0216 receives 83 of 273 Sst cells (F1=0.49, purity=1.0). This is consistent with HS cells being one of several Sst+ subtypes in the source label but does not isolate HS-specific identity.

**Concerns:**

- **Shared-supertype problem.** SUPT_0216 is the same supertype that an independent OLM annotation-transfer run (Winterer 2019 / GSE124847) maps to at F1=0.67 (43 of 46 cells), and bistratified cells (Pvalb/Sst/Tac1+) likely also contribute. The supertype is the CA1-oriens SST+ interneuron pool, not an HS-specific target. *(note: this is the canonical "Sst+ horizontal interneurons in oriens include several cell types in addition to O-LM cells" problem named by Oren et al. 2009 [4].)*
- **Defining-marker mismatch on the atlas side.** WMBv1's defining marker for SUPT_0216 is Reln, which is established as an OLM marker, not an HS marker — atlas-side marker curation favours OLM identity at this supertype.
- **AT source-label dilution.** The Yao 2021 SSv4 "Sst" subclass label (n=273 CA1 cells) pools HS, OLM, bistratified, oriens-oriens, and other Sst-IN morphological types; AT cannot distinguish HS-specific transfer without a morphology-confirmed source dataset.
- **Long-range projection identity is not assessable from atlas metadata.** Soma location and Sst expression cannot positively identify the HS axonal target (medial septum); the defining feature of the HS cell is not resolvable from MERFISH + expression alone.

**What would upgrade confidence:**

- Patch-seq or Cre-driver-targeted scRNA-seq of confirmed long-range projecting CA1 SST+ neurons (e.g. retrograde-tracer-labelled septally-projecting cells in stratum oriens) → AnnotationTransferEvidence at F1 ≥ 0.7 against a specific supertype or cluster within Sst Gaba_3.
- Cite-traverse for ChAT, Calb1, or other markers reported to discriminate HS from OLM in stratum oriens, to anchor a positive HS-side identification.

### Property alignment — 0768 Sst Gaba_3 [CS20230722_CLUS_0768] · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | (see SUPT_0216 above) | Field CA1, stratum oriens [MBA:399] count_100um=261 (region_fraction_100um=0.818) | CONSISTENT |
| NT type | GABAergic | not asserted | GABA | CONSISTENT |
| Sst expression | defining marker | 11.44 (SUPT_0216) | 12.70; cohort_pct 0.992 | CONSISTENT |
| Sst neuropeptide | classical neuropeptide | 11.44 (SUPT_0216) | 12.70; cohort_pct 0.992; atlas category: NEUROPEPTIDE | CONSISTENT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression + MERFISH spatial | Atlas metadata | PARTIAL | Sst cohort_pct 0.992; region_fraction_100um=0.818 | atlas-internal |

### 0768 Sst Gaba_3 — supporting evidence

- **Highest CA1-stratum-oriens region fraction within Sst Gaba_3.** Among the six Sst Gaba_3 child clusters reviewed (0767, 0768, 0770, 0772, 0773, plus the supertype rollup), CLUS_0768 has the highest proximity-based fraction in CA1 stratum oriens [MBA:399] (region_fraction_100um=0.818). It is the most spatially concentrated Sst Gaba_3 child for the HS soma compartment.
- **Sst expression at cluster level.** Sst=12.70, cohort_pct=0.992 (n_members=50) — top decile within the GABAergic CA1-stratum-oriens cohort. The atlas tags Sst as NEUROPEPTIDE-category on this cluster.

**Concerns:**

- **No HS-specific evidence at cluster level.** The reasons CLUS_0768 is offered as a candidate — Sst+, in CA1 stratum oriens — are properties shared with OLM, bistratified, and other CA1-SO Sst+ interneurons. There is no positive HS-specific signal (e.g. long-range axonal target, ChAT, or a morphology-specific marker) on this cluster.
- **Independent OLM evidence preferentially loads onto this same cluster.** Prior reporting in this graph indicates Winterer 2019 OLM AT loads strongly onto CLUS_0768 and its supertype, weakening the case that the HS cell — rather than OLM — is what CLUS_0768 represents.
- **AT source-label dilution.** Same CASE B issue as for SUPT_0216 — the Yao 2021 Sst SSv4 label cannot discriminate HS from OLM, so the broader supertype-level F1 does not transfer to a cluster-level HS call.

**What would upgrade confidence:**

- Patch-seq or retrograde-labelled scRNA-seq of septally-projecting CA1 stratum oriens SST+ neurons → AT at F1 ≥ 0.7 specifically onto CLUS_0768 (or some other Sst Gaba_3 child).
- A markered discriminator (e.g. lit-derived HS-specific transcript) tested against CLUS_0768's precomputed expression.

---

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 target | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | (supertype) | 2004 | 🟡 MODERATE | CA1 SO + Sst+; shared with OLM | Primary (supertype broadMatch) |
| `0768 Sst Gaba_3 [CS20230722_CLUS_0768]` | 0216 Sst Gaba_3 | 66 | 🔴 LOW | Best in-region Sst Gaba_3 child (region_fraction_100um=0.818) | Secondary (in-region child) |
| `0772 Sst Gaba_3 [CS20230722_CLUS_0772]` | 0216 Sst Gaba_3 | 190 | 🔴 LOW | Sst+ CA1 SO Sst Gaba_3 child | Eliminated (no HS-specific signal vs. CLUS_0768) |
| `0767 Sst Gaba_3 [CS20230722_CLUS_0767]` | 0216 Sst Gaba_3 | 104 | 🔴 LOW | Mixed CA1/forebrain-bundle location | Eliminated (off-region scatter) |
| `0770 Sst Gaba_3 [CS20230722_CLUS_0770]` | 0216 Sst Gaba_3 | 404 | 🔴 LOW | Sst+ CA1 SO Sst Gaba_3 child | Eliminated (lower region fraction than CLUS_0768) |
| `0773 Sst Gaba_3 [CS20230722_CLUS_0773]` | 0216 Sst Gaba_3 | 156 | 🔴 LOW | Sst+ CA1 SO Sst Gaba_3 child | Eliminated (lower region fraction than CLUS_0768) |
| `0241 Sst Chodl Gaba_4 [CS20230722_SUPT_0241]` | (supertype) | 2905 | 🔴 LOW | Isocortex location; not hippocampal | Eliminated (distant region — cortical Sst Chodl) |
| `0226 Sst Gaba_13 [CS20230722_SUPT_0226]` | (supertype) | 4064 | 🔴 LOW | Isocortex location; not hippocampal | Eliminated (distant region — cortical Sst) |
| `0219 Sst Gaba_6 [CS20230722_SUPT_0219]` | (supertype) | 725 | 🔴 LOW | CA3-pyramidal-layer-dominant | Eliminated (wrong subfield — CA3, not CA1) |
| `1164 Astro-TE NN_4 [CS20230722_SUPT_1164]` | (supertype) | 982 | ⚪ UNCERTAIN | Astrocyte; Sst=0.80 (cohort_pct 0.333) | Eliminated (wrong cell class — astrocyte) |

Total: 10 edges. Survivor relationships: 1 broadMatch (supertype) + 1 closeMatch candidate (in-region child cluster); remaining 8 left as `evidencell:UncertainRelationship`.

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The HS cell node is defined on CLASSICAL_MULTIMODAL evidence: Sst as a defining marker [1, 5, 6], GABAergic identity, and soma in CA1 stratum oriens [1, 2, 3, 4]. Reference coverage is sparse (single verbatim quote captured) and electrophysiology is not characterised; the relationship to cortical Chodl+ long-range projecting interneurons is unresolved.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Sst subclass; n=273 CA1 cells of broader 6,398-cell run) |
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
| Caveats | Yao 2021 SSv4 'Sst' subclass label pools multiple Sst+ interneuron morphological types (OLM, HS, bistratified, oriens-oriens, etc.); subtype resolution requires a morphology-tagged source dataset. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `25c2b32` at 2026-06-08T18:37:32+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0768 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0772 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0767 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0770 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0773 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0241 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0226 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_1164 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0219 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Hippocampo-septal (HS) cell → 0216 Sst Gaba_3 [CS20230722_SUPT_0216] at MODERATE confidence as a broad (supertype-level) match, with 0768 Sst Gaba_3 [CS20230722_CLUS_0768] [CS20230722_CLUS_0768] as a LOW-confidence in-region child-cluster candidate. Key support: Sst expression at cohort_pct 0.905 (supertype) / 0.992 (CLUS_0768) and CA1 stratum oriens MERFISH localisation (region_fraction_100um=0.539 / 0.818). Key caveats: shared-supertype contamination by OLM and bistratified cells, atlas defining marker Reln favouring OLM identity, and source-label dilution in the only available cluster annotation transfer run.

sst chodl GABAergic interneuron [[CL:4023121](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023121)] is a related but non-identical Cell Ontology term. CL:4023121 partially overlaps (long-range projecting SST+ INs) but HS cells are hippocampus-specific and may not express Chodl. The WMBv1 Sst Chodl supertype (0241 Sst Chodl Gaba_4) is cortical (region_fraction_100um=0.021 for CA1 stratum oriens), so the CL term's long-range-projection axis does not translate to a hippocampal mapping at the supertype level — the HS cell is a candidate for a more specific Cell Ontology term.

### Proposed experiments and follow-ups

**Already attempted (and partially resolved):**

- *Cluster annotation transfer of Sst+ CA1 cells onto WMBv1.* Done with Yao 2021 (GEO:GSE185862, n=273 CA1 Sst-subclass cells, MapMyCells). Reaches Sst Gaba subclass cleanly (F1=0.98); does not resolve subtype within the Sst Gaba_3 / Sst Gaba_6 supertypes because the source label is morphology-blind.

**Still needed:**

1. **Morphology-tagged or retrograde-labelled scRNA-seq of HS cells.** Method: retrograde-tracer labelling of medial-septum-projecting CA1 stratum oriens neurons, followed by FACS + scRNA-seq (or patch-seq with axon-recovery). Target: AT F1 ≥ 0.7 onto a specific Sst Gaba_3 child cluster or to the broader Sst Gaba_3 supertype with cluster-level resolution. Expected output: AnnotationTransferEvidence on the HS node. Resolves: Q1, Q2.
2. **Cite-traverse for HS-vs-OLM discriminating markers.** Method: targeted literature search for transcript-level discriminators between hippocampo-septal and OLM cells (candidates: ChAT, Calb1, m2-receptor density, Chodl expression in hippocampal SST+ cells). Expected output: additional defining_markers and/or negative_markers on the HS classical node, with primary citations. Resolves: Q1.

### Open questions

1. Does SUPT_0216 contain any long-range projecting Sst+ neurons, or is it exclusively local-circuit (OLM)?
2. Is there a more appropriate HS candidate outside the Sst Gaba_3 supertype (e.g. within the cortical Sst Chodl class, if a hippocampal subset exists)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Lagartos-Donate et al. 2019 (doi: [10.1101/598599](https://doi.org/10.1101/598599)) | — | soma location, Sst marker |
| [2] | Müller & Remy 2017 | [29250747](https://pubmed.ncbi.nlm.nih.gov/29250747) | soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | soma location |
| [4] | Oren et al. 2009 | [19176803](https://pubmed.ncbi.nlm.nih.gov/19176803) | soma location |
| [5] | Takács et al. 2024 | [38470935](https://pubmed.ncbi.nlm.nih.gov/38470935) | Sst marker |
| [6] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999) | Sst marker |

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Sst (cohort_pct 0.905) + CA1 stratum oriens
    (region_fraction_100um: 0.539) place HS within
    CS20230722_SUPT_0216; cluster annotation transfer of the Yao 2021
    Sst subclass (run_ref at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1)
    reaches Sst Gaba subclass cleanly (F1=0.98), but the source label
    pools multiple Sst+ CA1-SO morphological subtypes (OLM, HS,
    bistratified) so cluster-level discrimination is not possible;
    atlas-side defining marker Reln on SUPT_0216 favours OLM, capping
    confidence at MODERATE for a broadMatch at supertype.
  reconciliation_note: >
    Indistinguishable from sibling lit-types (olm_cell_ca1,
    bistratified_cell_hippocampus, p_lm_cell_hippocampus,
    r_lm_cell_hippocampus, oriens_oriens_cell_hippocampus,
    lth_cell_hippocampus) at the Yao 2021 Sst subclass annotation
    transfer level only (CASE B — AT-only); panels markers, anat, nt
    do not by themselves separate HS from OLM in the structured data
    here. Paired with edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0768
    (best in-region Sst Gaba_3 child); cluster-level mapping remains LOW.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        SUPT_0216 is shared across OLM, HS, and bistratified CA1-SO
        Sst+ interneurons; independent OLM cluster annotation transfer
        (Winterer 2019 / GSE124847) maps the majority of OLM cells to
        this supertype. HS-specific identity is not isolable here.
    - caveat_type: MARKER_NOT_SPECIFIC
      description: >
        WMBv1 defining marker for SUPT_0216 is Reln, established as an
        OLM marker; atlas-side curation favours OLM identity at this
        supertype.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No HS-specific marker is recorded on the classical node; long-range
        projection to medial septum (the defining HS feature) is not
        resolvable from MERFISH + precomputed expression alone.
  proposed_experiments:
    - >
      Retrograde-tracer-labelled scRNA-seq of medial-septum-projecting
      CA1 stratum oriens SST+ neurons → cluster annotation transfer
      onto WMBv1 at F1 ≥ 0.7 to isolate the HS-specific Sst Gaba_3 child.
    - >
      Targeted cite-traverse for HS-vs-OLM transcript-level
      discriminators (ChAT, Calb1, Chodl in hippocampal SST+ cells)
      to anchor positive HS-side markers on the classical node.
  unresolved_questions:
    - >
      Does SUPT_0216 contain any long-range projecting Sst+ neurons or
      is it exclusively local-circuit (OLM)?
    - >
      Is there a more appropriate HS candidate outside the Sst Gaba_3
      supertype (e.g. a hippocampal subset of the Sst Chodl class)?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0768 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.3
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:NEXT] CS20230722_CLUS_0768 has the highest CA1-stratum-oriens
    proximity within the Sst Gaba_3 supertype
    (region_fraction_100um: 0.818) and Sst cohort_pct 0.992, making it
    the best in-region child-cluster candidate; but no HS-specific
    evidence exists at cluster level, and independent OLM annotation
    transfer evidence preferentially loads onto this same cluster, so
    a cluster-level closeMatch cannot be supported.
  reconciliation_note: >
    Paired with edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0216
    (broadMatch primary). Relationship left as
    evidencell:UncertainRelationship pending HS-specific cluster
    annotation transfer.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        CLUS_0768 may instead represent OLM (independent Winterer 2019
        OLM AT reportedly loads onto this cluster within SUPT_0216).
        HS-specific cluster identity is not established.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No HS-specific transcript-level discriminator is documented on
        the classical node; cluster-level Sst, NT, and CA1 stratum
        oriens location are all shared with OLM.
  proposed_experiments:
    - >
      Cluster annotation transfer of retrograde-labelled septally-
      projecting CA1-SO SST+ neurons onto WMBv1 with cluster-level F1 ≥ 0.7
      to confirm or refute CLUS_0768 as the HS-specific child.
  unresolved_questions:
    - >
      Is there a cluster-level discriminator between HS and OLM within
      the Sst Gaba_3 supertype?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0772 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CLUS_0772 (Sst cohort_pct 0.958; region_fraction_100um:
    0.706) is a CA1-stratum-oriens Sst Gaba_3 child cluster but
    carries no HS-specific signal beyond shared supertype features;
    CLUS_0768 has a higher in-region fraction.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0767 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CLUS_0767 (region_fraction_100um: 0.578) shows off-region
    scatter into forebrain bundle systems and lacks any HS-specific
    signal; eliminated as a primary HS candidate.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0770 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] CLUS_0770 (region_fraction_100um: 0.506; Sst cohort_pct
    0.807) is a Sst Gaba_3 child with weaker CA1-stratum-oriens
    proximity than CLUS_0768 and no HS-specific evidence; eliminated.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_CLUS_0773 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.12
  rationale: >
    [tier:CUT] CLUS_0773 (region_fraction_100um: 0.648; Sst cohort_pct
    0.908) is a Sst Gaba_3 child clustering near but below CLUS_0768
    on the in-region fraction and contributes no HS-specific signal;
    eliminated.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0241 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0241 (Sst Chodl Gaba_4) is the cortical
    Sst Chodl population (Isocortex MBA:315 dominant;
    region_fraction_100um: 0.021 for CA1 stratum oriens); although it
    is the WMBv1 correspondent of the CL term CL:4023121 cited on the
    HS node, the hippocampus-specific HS cell does not map here on
    location grounds. Eliminated.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0226 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0226 (Sst Gaba_13) is Isocortex-dominant
    (region_fraction_100um: 0.016 for CA1 stratum oriens); off-region
    cortical Sst supertype, not a hippocampal HS candidate. Eliminated.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_1164 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.02
  rationale: >
    [tier:CUT] CS20230722_SUPT_1164 (Astro-TE NN_4) is an astrocyte
    supertype with Sst=0.80 (cohort_pct 0.333); wrong cell class for
    the GABAergic neuronal HS type. Eliminated.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_hippocampo_septal_cell_ca1_to_CS20230722_SUPT_0219 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.1
  rationale: >
    [tier:CUT] CS20230722_SUPT_0219 (Sst Gaba_6) is CA3-pyramidal-layer-
    dominant (region_fraction_100um: 0.132 for CA1 stratum oriens);
    wrong CA subfield for the CA1-SO HS soma compartment. Eliminated.
```
<!-- verdict-block-end -->
