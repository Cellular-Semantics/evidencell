# Central amygdala ISL1-expressing long-range projection neuron — CCN20230722 Mapping Report
*Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala ISL1-expressing long-range projection neuron is a GABAergic cell type resident in the central amygdala [UBERON:0002883] that was identified as a novel, previously unresolved class through a combined single-cell RNA sequencing, multiplexed fluorescent in situ hybridization, immunohistochemistry, and long-range projection-mapping study [1]. Together with an Nr2f2-expressing non-canonical CeA subpopulation, these ISL1+ neurons constitute approximately one-third of all CeA neurons and account for a disproportionate fraction of CeA long-range output projections — a fraction that had been attributed collectively to the canonical Prkcd/Sst+ classes. Mapping this type to the Allen WMBv1 atlas (CCN20230722) is important for understanding which transcriptomic cluster(s) encode CeA projection output identity and for connecting the developmentally defined LGEv lineage to the adult transcriptomic taxonomy.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Cell type name | Central amygdala ISL1-expressing long-range projection neuron | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | [1] |
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | [1] |
| Defining markers | Isl1 | [1], [2] |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** scRNA-seq combined with multiplexed FISH, IHC, and long-range projection mapping · mouse CeA · [1]

- **Neurotransmitter — GABAergic:** scRNA-seq (O'Leary et al. 2022 CeA cell-type classification) · [1]

- **Defining marker — Isl1:** scRNA-seq + IHC (O'Leary et al. 2022) · [1]

  > Such work has typically defined molecular cell types by classical inhibitory marker genes; consequently, whether marker-gene- defined cell types exhaustively cover the CEA and co-vary with connectivity remains unresolved. Here, we combined single-cell RNA sequencing, multiplexed fluorescent in situ hybridization, immunohistochemistry, and long-range projection mapping to derive a "bottom-up" understanding of CEA cell types. In doing so, we identify two major cell types, encompassing one-third of all CEA neurons, that have gone unresolved in previous studies. In spatially mapping these novel types, we identify a non-canonical CEA subdomain associated with Nr2f2 expression and uncover an Isl1-expressing medial cell type that accounts for many long-range CEA projections.
  > — O'Leary et al. 2022, Central amygdala cell types · [1] <!-- quote_key: 253356112_2fc294b0 -->

- **Defining marker — Isl1 (developmental lineage context):** histogenetic developmental anatomy review · rodent/avian CeA · [2]

  > cells derived from the ventral LGEv express Islet1 (Waclaw et al., 2010; Bupesh et al., 2011a) and show a trend to locate in the lateral and medial subdivisions of the nucleus (Bupesh et al., 2011a), partially overlapping the neurons expressing corticotropin releasing factor or other peptides/proteins (dynorphin, calbindin) that concentrate in different parts of the lateral subdivision
  > — Vicario et al. 2014, INTRODUCTION · [2] <!-- quote_key: 10856039_51074be7 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; 1385 CEA-BST Ebf1 Pdyn Gaba_1 [CS20230722_CLUS_1385] within supertype 0384 CEA-BST Ebf1 Pdyn Gaba_1 is the primary mapping at MODERATE confidence. The mapping carries a 1:n cardinality caveat: five CEA-BST clusters score identically on Isl1 expression alone, and the classical type likely spans this cluster family rather than mapping cleanly to a single rank-0 node. Annotation transfer from Hochgerner 2023 GABA-18-Isl1-Tac1 cells (n=27) supports the CEA-BST Ebf1 Pdyn Gaba subclass [CS20230722_SUBC_082] but achieves only low F1 at that subclass level (F1=0.17), consistent with the predicted 1:n scatter.

### Mapping candidates overview

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 1385 CEA-BST Ebf1 Pdyn Gaba_1 [CS20230722_CLUS_1385] | 0384 CEA-BST Ebf1 Pdyn Gaba_1 | 81 | 🟡 MODERATE | Isl1 CONSISTENT · location CONSISTENT | Best candidate |

*1 edge total; relationship: `skos:broadMatch` (1:n — five CEA-BST rank-0 clusters score equivalently on Isl1; CLUS_1385 ranks highest by CeA region_fraction).*

---

### Property alignment: 1385 CEA-BST Ebf1 Pdyn Gaba_1 [CS20230722_CLUS_1385]

**Table 1 — Property comparison**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | CEA region_fraction 0.489 (highest among rank-0 candidates); label "CEA-BST Ebf1 Pdyn Gaba_1" confirms CEA-BST lineage | CONSISTENT |
| Isl1 expression | Defining marker (PMID:36425768) | Isl1 precomputed mean_expression 6.62 (CeA GABAergic cohort 96.4th pct; tier 2; applied_score 2.0) | CONSISTENT |
| Sex ratio | Not documented | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| O'Leary et al. 2022 scRNA-seq + projection mapping | Literature | SUPPORT | Isl1+ medial CeA class accounts for many long-range projections | [1] |
| Atlas precomputed expression (CLUS_1385) | Atlas metadata | SUPPORT | Isl1 mean 6.62; 96.4th pct of CeA GABAergic cohort; region_fraction 0.489 | atlas-internal |
| MapMyCells AT (Hochgerner 2023 GABA-18-Isl1-Tac1; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) | Annotation transfer | PARTIAL | F1=0.17 at SUBCLASS CS20230722_SUBC_082 "CEA-BST Ebf1 Pdyn Gaba" | — |

*(Child-cluster breakdown not assessed across the full CEA-BST Ebf1 Pdyn family at rank-0 — five clusters score identically on Isl1; see proposed experiments.)*

---

### 1385 CEA-BST Ebf1 Pdyn Gaba_1 [CS20230722_CLUS_1385] · 🟡 MODERATE

**Supporting evidence**

- **Literature [1]:** O'Leary et al. 2022 combined scRNA-seq, multiplexed FISH, immunohistochemistry, and long-range projection mapping in mouse CeA, identifying ISL1-expressing neurons as a major medial CeA class responsible for a large fraction of long-range projections. The cell type was identified through a bottom-up transcriptomic approach, providing strong cell-type specificity. ISL1 marks developmentally distinct LGEv-derived CeA neurons [2].

- **Atlas metadata (CLUS_1385):** 1385 CEA-BST Ebf1 Pdyn Gaba_1 [CS20230722_CLUS_1385] expresses Isl1 at the 96.4th percentile of the CeA GABAergic survival cohort (n=5 rank-0 clusters; region=MBA:536; tier-2 reliable; mean_expression 6.62), with a CEA region_fraction of 0.489 — the highest among all rank-0 candidates. The "CEA-BST" cluster label directly confirms central amygdala–bed nucleus of the stria terminalis lineage. Four of five rank-0 candidates belong to the CEA-BST Ebf1 Pdyn family, providing a coherent transcriptomic family assignment for the ISL1 projection neuron class. *(Note: region_fraction 0.489 falls in the boundary band 0.3–0.7; it supports but does not strongly confirm exclusive CeA localisation, consistent with the CEA-BST dual-region label.)*

- **Annotation transfer — MapMyCells (`at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`):** The Hochgerner 2023 source cluster GABA-18-Isl1-Tac1 (n=27 naive cells from ArrayExpress:E-MTAB-12096) maps at SUBCLASS level to 082 CEA-BST Ebf1 Pdyn Gaba [CS20230722_SUBC_082] with F1=0.17 (coverage 0.89, purity 0.10). The correct subclass family is identified, confirming the CEA-BST Ebf1 Pdyn Gaba lineage assignment. Low purity (0.10) is consistent with the 1:n scatter of source cells across five rank-0 clusters within this subclass. At CLASS level the mapping goes to 11 CNU-HYa GABA [CS20230722_CLAS_11] with F1=0.03 (coverage 1.0, purity 0.02), confirming GABAergic CNU-HYa identity broadly but providing no cluster-level resolution. The low F1 values reflect the structural 1:n cardinality rather than a mismatch.

**Marker evidence provenance**

- **Isl1 (defining marker):** Evidence is multi-modal — transcript-level (scRNA-seq) and protein-level (IHC) from O'Leary et al. 2022 [1]. The cell-type specificity is strong: cells were classified by scRNA-seq first, then validated by IHC in the same study, not as part of a bulk "Isl1+ interneuron" assay. Vicario et al. 2014 [2] provides developmental lineage context (LGEv origin → Islet1 expression → medial/lateral CeA location) but is a histogenetic review paper, not a primary functional study of adult mouse CeA. *(Note: Vicario et al. 2014 reports data primarily from avian amygdala homologue with reference to rodent data; the cross-species developmental lineage inference is well-supported but is not a direct primary study of mouse adult CeA.)*
  - The atlas precomputed mean_expression of 6.62 (tier 2, EXPRESSION source) in CLUS_1385 is consistent with sustained adult Isl1 expression, but independent adult protein-level IHC in atlas age/condition tissue has not been extracted into the KB as a separate evidence item.

**Concerns**

- **DISTRIBUTED_ACROSS_CLUSTERS:** Five CEA-BST rank-0 clusters (CLUS_1316, CLUS_1385, CLUS_1386, CLUS_1395, CLUS_1397) all score 3/3 on Isl1 + region + NT. Discovery score = 3, next_best_score = 3, cohort_size = 5 — a maximal tie; no dominance signal at rank-0. CLUS_1385 is the representative edge based on highest CeA region_fraction (0.489), but this distinction is marginal.

- **Annotation transfer PARTIAL:** F1=0.17 at SUBCLASS level from Hochgerner 2023 GABA-18-Isl1-Tac1 (n=27) is low; purity=0.10 indicates that only 10% of the CEA-BST Ebf1 Pdyn Gaba subclass cells are mapped from this source group, reflecting the 1:n scatter. The AT result supports subclass assignment but does not resolve 1:n cardinality at rank-0. No rank-0 cluster-level F1 data are available.

- **Adult ISL1 expression:** ISL1 is a developmental transcription factor. Adult atlas precomputed expression (mean 6.62 in CLUS_1385) is consistent with maintained adult expression, and O'Leary et al. 2022 [1] used IHC in adult CeA tissue. However, the specific atlas age/sex/condition for the WMBv1 reference has not been independently confirmed for ISL1 protein in gathered evidence.

**What would upgrade confidence**

- **MapMyCells on ISL1-lineage or FACS-sorted Isl1+ CeA cells** (AnnotationTransferEvidence): A targeted AT run using Isl1-Cre × reporter-sorted or TRAP-purified CeA neurons would resolve which of the five CEA-BST Ebf1 Pdyn clusters (CLUS_1316, CLUS_1385, CLUS_1386, CLUS_1395, CLUS_1397) best captures this population. Target: F1 ≥ 0.50 at CLUSTER level. Resolves open questions 1 and 2.

- **ISL1 IHC in adult mouse CeA** (LiteratureEvidence with `method: immunohistochemistry`): Confirm sustained ISL1 protein expression in mature CeA neurons under WMBv1 age/sex conditions. Target: documented ISL1+ cell fraction in medial CeA matching O'Leary et al. 2022 proportional estimates. Resolves open question 3.

- **Targeted cite-traverse** for "Isl1 central amygdala adult mouse" or "ISL1 CeA long-range projections Ebf1 Pdyn": May identify subsequent studies that have already resolved cluster-level assignment or confirmed adult expression. This is a KB-only step requiring no new experiment.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The `cea_isl1_projection_neuron` classical node is defined on a CLASSICAL basis. Defining marker: Isl1 [1], [2]. Neurotransmitter type: GABAergic [1]. Soma location: Central amygdaloid nucleus [UBERON:0002883] [1]. The node was identified by O'Leary et al. 2022 using single-cell RNA sequencing combined with multiplexed FISH, IHC, and long-range projection mapping; the Isl1+ class was identified as a novel medial CeA type accounting for many long-range projections and constituting approximately one-third of all CeA neurons together with an Nr2f2+ non-canonical subdomain. Prkcd and Sst exhibit mixed expression across multiple scRNA-seq clusters, indicating these canonical markers alone do not resolve all CeA projection cell types.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:536, NT type GABAergic, Isl1 defining marker). Survival cohort: 5 rank-0 clusters. Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer**

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 (source cluster: GABA-18-Isl1-Tac1) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). Input h5ad built from Hochgerner 2023 figshare UMI count table: genes × cells TSV converted to cells × genes h5ad, filtered to naive neuronal cells. Gene names are gene symbols as in source file. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.7 |
| n cells | 55514 total (filtered to 7777 naive neuronal) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/mapping_result.csv`](../../research/medial_temporal_lobe_amygdala/annotation_transfer/hochgerner2023_amygdala/mapping_result.csv) |
| Caveats | Source labels are transcriptomically-defined types, not classical morpho-electrophysiological types. Matching to KB classical nodes requires a mapping step (Hochgerner type → classical node) based on shared molecular markers. Fear-conditioned cells excluded to avoid transcriptional-state confounds. Non-neuronal cells excluded. Gene symbols used (not Ensembl IDs); matched against WMBv1 marker genes. |

**Anti-hallucination.**
All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_isl1_projection_neuron_to_cs20230722_clus_1385 | LITERATURE; ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; SUPPORT; PARTIAL | [1]; atlas-internal; — |

*Generated by evidencell `8d79cdb` at 2026-06-11T09:44:21+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Central amygdala ISL1-expressing long-range projection neuron → 1385 CEA-BST Ebf1 Pdyn Gaba_1 [CS20230722_CLUS_1385] at MODERATE confidence. Key support: Isl1 marker CONSISTENT (precomputed mean_expression 6.62, CeA GABAergic cohort 96.4th percentile) and CeA soma location CONSISTENT (region_fraction 0.489; CEA-BST label); annotation transfer from Hochgerner 2023 GABA-18-Isl1-Tac1 identifies the correct subclass family (CS20230722_SUBC_082) at PARTIAL support. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS (five CEA-BST rank-0 clusters score identically on Isl1; 1:n cardinality unresolved at cluster level); AT F1=0.17 at SUBCLASS level does not resolve rank-0 cardinality.

No Cell Ontology term is currently assigned. The ISL1-expressing CeA projection class is a recently characterised type (O'Leary et al. 2022 [1]) not yet represented in CL; it is a candidate for a new CL term request.

### Proposed experiments and follow-ups

The `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` annotation transfer run partially addresses the mapping by confirming the CEA-BST Ebf1 Pdyn Gaba subclass assignment, but does not resolve 1:n cardinality at rank-0 (F1=0.17 at SUBCLASS; no cluster-level F1 data). A more targeted AT experiment is still needed:

1. **MapMyCells on ISL1-lineage or FACS-sorted Isl1+ CeA cells**
   - **What:** Annotation transfer (cell_type_mapper v1.7.1 or later) using Isl1-Cre × reporter-sorted or TRAP-purified CeA neurons from a dedicated dataset
   - **Target:** F1 ≥ 0.50 at CLUSTER level against CCN20230722
   - **Expected output:** `AnnotationTransferEvidence` items on `edge_cea_isl1_projection_neuron_to_cs20230722_clus_1385` and sibling CEA-BST edges; non-matching rank-0 clusters down-weighted
   - **Resolves:** Open questions 1 and 2

2. **ISL1 IHC in adult mouse CeA**
   - **What:** Immunohistochemistry with ISL1 antibody in adult mouse CeA at WMBv1 age/sex conditions, optionally co-labelled with retrograde tracer from known long-range projection targets
   - **Target:** Document ISL1+ cell fraction in medial CeA matching O'Leary et al. 2022 estimates; confirm projection identity
   - **Expected output:** `LiteratureEvidence` with `method: immunohistochemistry`
   - **Resolves:** Open question 3

3. **Targeted cite-traverse** ("Isl1 central amygdala adult mouse" or "ISL1 CeA Ebf1 Pdyn projection")
   - **What:** Literature search for post-2022 studies confirming adult ISL1 expression or cluster-level AT in CeA
   - **Target:** `LiteratureEvidence` item with adult-expression or cluster-level correspondence
   - **Expected output:** Additional `LiteratureEvidence` or `MarkerEvidence` items
   - **Resolves:** Open questions 2 and 3 (partially)

### Open questions

1. Which CEA-BST Ebf1 Pdyn cluster (CLUS_1316, CLUS_1385, CLUS_1386, CLUS_1395, or CLUS_1397) best represents the ISL1 long-range projection neuron? Five rank-0 clusters score identically on Isl1 alone; AT evidence from Hochgerner 2023 GABA-18-Isl1-Tac1 resolves subclass but not rank-0 cardinality.
2. Is ISL1 expression maintained in adult CeA neurons, or does the atlas capture a developmental remnant of LGEv neurogenesis?
3. Does the LGEv developmental origin documented by Vicario et al. 2014 [2] (primarily avian data with rodent references) apply directly to the mouse adult CeA ISL1+ population characterised by O'Leary et al. 2022 [1]? *(Note: cross-species developmental lineage inference is well-supported but is not a direct primary study of adult mouse CeA — confirm with targeted cite-traverse.)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | O'Leary et al. 2022 · *iScience* · DOI:10.1016/j.isci.2022.105497 | [36425768](https://pubmed.ncbi.nlm.nih.gov/36425768/) | Soma location; NT type; Isl1 defining marker; long-range projection identity |
| [2] | Vicario et al. 2014 · *Front. Neuroanat.* · DOI:10.3389/fnana.2014.00090 | [25309337](https://pubmed.ncbi.nlm.nih.gov/25309337/) | Isl1 marker (LGEv developmental lineage) |

---

<!-- verdict-block-start: edge_cea_isl1_projection_neuron_to_cs20230722_clus_1385 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.52
  rationale: >
    marker_Isl1 CONSISTENT (precomputed mean_expression 6.62, CeA GABAergic cohort 96.4th
    pct; tier 2 reliable; EXPRESSION source); location_soma CONSISTENT (region_fraction
    0.489 at MBA:536; CEA-BST label confirms lineage); nt_type CONSISTENT (GABAergic/GABA).
    1 of 1 markers CONSISTENT. AT evidence (at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1;
    source GABA-18-Isl1-Tac1, n=27 cells) provides partial support: F1=0.17 at SUBCLASS
    (CS20230722_SUBC_082 "082 CEA-BST Ebf1 Pdyn Gaba"; coverage 0.89, purity 0.10) confirms
    correct subclass family but does not resolve rank-0 cardinality. Five rank-0 CEA-BST
    clusters score identically on Isl1 alone (DISTRIBUTED_ACROSS_CLUSTERS; discovery score
    = 3, next_best_score = 3, cohort_size = 5); skos:broadMatch 1:n is the appropriate
    predicate. Confidence is MODERATE on basis of LITERATURE + ATLAS_METADATA + PARTIAL AT
    converging on CEA-BST Ebf1 Pdyn family, with 1:n cardinality as primary unresolved caveat.
  reconciliation_note: null
  lit_to_lit_edges: []
  unresolved_questions:
    - "Which CEA-BST Ebf1 Pdyn cluster (CS20230722_CLUS_1385 vs 1386 vs 1395 vs 1397 vs 1316) best represents the ISL1 long-range projection neuron? Five rank-0 clusters score identically on Isl1 alone; AT from Hochgerner 2023 GABA-18-Isl1-Tac1 resolves subclass but not rank-0 cardinality."
    - "Is ISL1 expression maintained in adult CeA neurons, or does the atlas capture a developmental remnant of LGEv neurogenesis?"
```
<!-- verdict-block-end -->
