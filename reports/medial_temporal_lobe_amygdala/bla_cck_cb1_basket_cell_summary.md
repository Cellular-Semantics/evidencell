# Basolateral amygdala cholecystokinin/CB1+ basket cell — CCN20230722 Mapping Report
*· Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala cholecystokinin/CB1+ (CCK/CB1) basket cell is a classically defined GABAergic interneuron of the BLA distinguished from parvalbumin (PV) basket cells by its co-expression of the neuropeptide cholecystokinin and the cannabinoid receptor type 1 (CB1/CNR1). These cells innervate the soma and proximal dendrites of BLA pyramidal projection neurons, forming a perisomatic inhibitory network that is chemically and functionally distinct from the PV basket cell system. Mapping this cell type to a transcriptomic atlas cluster is important for connecting classical electrophysiological and neurochemical descriptions with genome-wide expression data and for enabling cell-type-resolved circuit analysis.

---

## Classical Node Properties

| Property | Value | References |
|---|---|---|
| Node ID | `bla_cck_cb1_basket_cell` | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | [2] |
| Soma location | Basolateral amygdaloid area [UBERON:0002887] | [1] |
| Defining markers | Cnr1 (CB1 cannabinoid receptor) | [1], [3], [4] |
| Neuropeptides | Cck | [1], [2], [3] |
| Negative markers | None encoded | — |
| CL mapping | basket cell [CL:0000118] — BROAD | — |
| Notes | Estimated 7–9% of GABAergic cells in LA/BA. CNR1 (CB1) marks this population as distinct from PV basket cells; several CCK interneuron subclasses identified in the basal amygdala in fear-extinction work. | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (UBERON:0002887):** Anatomy confirmed by targeted recording and immunohistochemistry in mouse BLA. · [1]
  > ".We found that the soma and proximal dendrites of PCs were innervated primarily by two neurochemically distinct basket cell types expressing parvalbumin (PVBC) or cholecystokinin and CB1 cannabinoid receptors (CCK/CB1BC). The innervation of the initial segment of PC axons was found to be parceled out by PVBCs and axo-axonic cells (AAC)"
  > — Vereczki et al. 2016, Basolateral amygdala and corticobasal cell types · [1] <!-- quote_key: 16327247_9b5e6962 -->

- **Neurotransmitter (GABAergic):** Review of GABAergic interneuron populations in BLA; CCK+ neurons described as a distinct GABAergic subpopulation · [2]
  > "The cell types in all of these amygdalar nuclei are similar, but they have been studied primarily in the basolateral amygdala. The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter"
  > — McDonald et al. 2012, Classical neuron classes across amygdala subdivisions · [2] <!-- quote_key: 11544073_94689603 -->

- **Defining marker Cnr1 and neuropeptide Cck:** Four interneuron types identified among EYFP-expressing cells in BLA, including CCK/CB1R basket cells. Identity confirmed by cell-type-specific targeting and morphological characterisation. · [3]
  > ".four IN types could be identified among the EYFP-expressing cells: CCK/cannabinoid receptor type 1 (CB1R)-expressing basket cells, neurogliaform cells, PV+ basket cells, and PV+ axo-axonic cells."
  > — Rovira-Esteban et al. 2019, Basolateral amygdala and corticobasal cell types · [3] <!-- quote_key: 204835327_91ea43a5 -->

- **Defining marker Cnr1:** Woodruff & Sah 2007 [4] — primary electrophysiological and morphological study of CCK basket cell physiology in mouse BLA; CNR1 confirmed at protein level.

</details>

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD). The Cell Ontology has no specific term for this population; basket cell is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster (CS20230722_CLUS_0664, Sncg Gaba_1) was assessed. This cluster ranks first within the BLA GABAergic cohort on the Stage A discovery score (score 5/5, rank 1 of 5 tied-scoring Sncg clusters), supported by two independent literature evidence items and precomputed expression confirmation of both Cnr1 and Cck. The primary mapping verdict is LOW confidence owing to absent annotation-transfer evidence and a 1:N cardinality caveat (five sibling Sncg Gaba clusters all score equally).

### 4a. Mapping Candidates

| Rank | WMBv1 cluster | Supertype | Cells (10×) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0664 (Sncg Gaba_1) | — | — | 🔴 LOW | Cnr1 CONSISTENT · Cck CONSISTENT | skos:closeMatch |

*1 edge total; relationship: `skos:closeMatch`.*

Note: `n_cells` is null in the current facts file — the taxonomy DB n_cells column may predate the present build; see proposed experiment 3 below.

### 4b. Property Alignment — CS20230722_CLUS_0664

**Table 1 — Property comparison.**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| Soma location | Basolateral amygdaloid area [UBERON:0002887] | MBA:295 SOMA cell_count=2 cell_ratio=0.063 (Zhuang 2023 MERFISH); region_fraction=0.031 | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Cnr1 expression | defining marker (CB1 cannabinoid receptor) | precomputed mean 12.36 (cohort 98.5th pct; tier 2; applied_score 2.0) — highest in BLA GABAergic cohort | CONSISTENT |
| Cck (neuropeptide) | Cck — neuropeptide | expression_score 11.15; precomputed mean 11.15 (cohort 98.3rd pct; tier 2); Sncg supertype is canonical CCK co-expression group in mouse | CONSISTENT |
| Sex ratio | not documented | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki et al. 2021 in vivo quantification | Literature | SUPPORT | 71.1% of CCK+ interneurons confirmed CCK+/CB1+ basket cells by GFP-targeted patch recording | [5] |
| Yu et al. 2024 primate snRNA-seq | Literature | SUPPORT | CCK+/CNR1+ cluster in primate amygdala homologous to mouse CCK basket cell; Sncg co-expression noted | [6] |
| CLUS_0664 precomputed expression | Atlas metadata | SUPPORT | Cnr1 mean 12.36 (98.5th pct); Cck mean 11.15 (98.3rd pct); both tier-2 reliable | atlas-internal |

*(Child-cluster breakdown not assessed — the five Sncg Gaba_1 clusters 0664/0665/0666/0672/0677 all score 5/5 with high Cnr1 and Cck; see proposed experiments.)*

---

### CS20230722_CLUS_0664 (Sncg Gaba_1) · 🔴 LOW

**Supporting evidence:**

- **In vivo quantification (GFP-targeted patch recording, mouse LA/BA, [5]):** Vereczki et al. 2021 report that 71.1% of CCK+ interneurons recorded from CCK-IRES-Cre::Ai9 mice in LA/BA were CCK+/CB1+ basket cells confirmed by CB1 immunoreactivity on axon terminals. This primary quantitative evidence anchors the CCK/CB1 basket cell as the dominant CCK interneuron type in BLA and directly supports mapping to an atlas cluster with high Cnr1 and Cck expression.

  > "the vast majority of GFP-expressing interneurons was CCK+/CB1+ basket cell (71.1 %, n = 38 recorded green neurons) as these interneurons had axon terminals immunoreactive for CB1"
  > — Vereczki et al. 2021, CCK+/CB1+ basket cells · [5] <!-- quote_key: 232283078_6d9c6756 -->

- **Cross-species transcriptomic homology (primate snRNA-seq, [6]):** Yu et al. 2024 identify a CCK+/CNR1+ cluster in primate amygdala snRNA-seq data that is noted as homologous to mouse CCK basket cells, with Sncg co-expression explicitly described. This directly links the Sncg Gaba_1 supertype label in the mouse atlas to CCK basket cell identity.

  > "This CCK + /CNR1 + cluster is likely homologous to mouse CCK + basket cells, which synapse onto the soma and proximal dendrites of excitatory neurons"
  > — Totty et al. 2024, GABAergic neuron types in the primate amygdala show distributed or subregion specific expression patterns · [6] <!-- quote_key: 273531817_f8731728 -->

- **Precomputed expression confirmation (CLUS_0664, atlas-internal):** Cnr1 precomputed mean expression is 12.36, placing CLUS_0664 at the 98.5th percentile within the BLA GABAergic cohort (tier 2 reliable, applied_score 2.0). Cck mean expression is 11.15 (98.3rd pct; tier 2 reliable). Both values are cohort-dominant. The Sncg supertype is the recognised mouse transcriptomic surrogate for the CCK interneuron group.

- **Morphology support ([1], [3]):** The perisomatic basket morphology — targeting soma and proximal dendrites of pyramidal cells — is the defining characteristic of this type, distinguished from axo-axonic cells that target the axon initial segment. Both Vereczki et al. 2016 and Rovira-Esteban et al. 2019 confirm this morphological class exists as a discrete population in mouse BLA.

**Marker evidence provenance:**

- **Cnr1 (defining marker):** Evidence is multimodal. [1] (Vereczki et al. 2016) establishes Cnr1/CB1 protein-level expression by immunohistochemistry in morphology-confirmed basket cells (GFP-targeted recording + biocytin fill). [3] (Rovira-Esteban et al. 2019) uses a CCK-IRES-Cre driver with EYFP expression and confirms CCK/CB1R basket cells by their four-type taxonomy with GFP-targeted recordings. [4] (Woodruff & Sah 2007) provides primary electrophysiological characterisation. Cell-type specificity is robust: all three studies used targeted approaches (Cre-driver or morphological reconstruction) to confirm they were recording from CCK/CB1 basket cells specifically. Atlas-side Cnr1 is not in the formal DEFINING list for CLUS_0664 but precomputed expression (mean 12.36, 98.5th pct) is tier-2 reliable and cohort-dominant — consistent with strong expression; *(note: the absence from the formal marker list may reflect a data-integration artefact rather than biological absence — interpretive inference not stated in facts.)*

- **Cck (neuropeptide):** Evidence is multimodal: protein-level (IHC, [1] [2]) and transcript-level (CCK-IRES-Cre driver, [3]). McDonald et al. 2012 [2] describes CCK+ large multipolar neurons in BLA as a distinct subpopulation. Vereczki et al. 2016 [1] and Rovira-Esteban et al. 2019 [3] both confirm CCK co-expression with CB1 in recorded basket cells. The Sncg Gaba_1 atlas supertype is the canonical mouse CCK co-expression group, strongly supporting neuropeptide Cck assignment to CLUS_0664. Atlas precomputed Cck mean 11.15 (98.3rd pct, tier 2) is cohort-dominant and consistent.

**Concerns:**

- **No annotation-transfer evidence (AT_ABSENT):** Confidence is capped at LOW without MapMyCells or equivalent AT evidence. The `skos:closeMatch` predicate is provisional.

- **1:N cardinality (CARDINALITY_1_N):** Five Sncg Gaba_1 clusters (CLUS_0664, CLUS_0665, CLUS_0666, CLUS_0672, CLUS_0677) all score 5/5 with equivalent Cnr1 and Cck expression. No available data distinguishes which single cluster (if any) should be the primary 1:1 match, or whether the classical type spans all five. The CARDINALITY_1_N caveat is the primary remaining gap.

- **Low BLA cell count for CLUS_0664 (LOW_BLA_CELL_COUNT):** MERFISH data (Zhuang 2023) records only 2 BLA soma for CLUS_0664 (MBA:295, cell_ratio=0.063). The match rests on Cnr1 + Cck expression pattern rather than regional restriction. *(note: the low count likely reflects the broad cortical distribution of Sncg clusters rather than genuine regional absence — interpretive inference grounded in facts property_comparisons notes.)*

- **Location note:** The `region_fraction` of 0.031 is low (< 0.3), consistent with the broad cortical distribution of Sncg interneurons. Per the reporting rubric, this low value does not independently drive the relationship choice; marker expression is the primary evidence.

**What would upgrade confidence:**

1. **MapMyCells annotation transfer** (AnnotationTransferEvidence; target: F1 ≥ 0.50 at CLUSTER level across CLUS_0664 vs sibling clusters) using a CCK/CB1 basket cell patch-seq or snRNA-seq source dataset from mouse BLA. This would resolve 1:N cardinality and potentially upgrade to MODERATE or HIGH.
2. **Multiplexed smFISH** (Sncg + Cnr1 + Cck in mouse BLA) to confirm co-expression at single-cell level and quantify which Sncg clusters are present in BLA and co-express the full CCK/CB1 marker panel.
3. **Taxonomy DB rebuild** (`just build-taxonomy-db CCN20230722`) to populate `n_cells` for all Sncg clusters; this will allow cell-count-informed cardinality assessment and confirm whether CLUS_0664 is the numerically dominant Sncg cluster in BLA.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The `bla_cck_cb1_basket_cell` node is defined on a CLASSICAL basis: morphological, neurochemical, and electrophysiological criteria from targeted studies in mouse BLA. Defining marker: Cnr1 (CB1 cannabinoid receptor), with supporting sources at protein (IHC, [1]) and transcript level (Cre-driver targeting, [3], [4]). Neuropeptide: Cck, supported by IHC ([1], [2]) and Cre-driver transcript ([3]). Neurotransmitter: GABAergic [2]. Soma location: basolateral amygdaloid area [UBERON:0002887] [1].

**Atlas mapping query.**
Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:295, NT type GABAergic, defining markers Cnr1, neuropeptide Cck). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.**
Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration (Zhuang 2023, atlas-internal) for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source evidence_items[*].explanation fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_cck_cb1_basket_cell_to_cs20230722_clus_0664 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [5]; [6]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:47+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala cholecystokinin/CB1+ basket cell → CS20230722_CLUS_0664 (Sncg Gaba_1) at LOW confidence. Key support: in vivo GFP-targeted patch recording quantifying CCK+/CB1+ basket cells as 71.1% of CCK interneurons in mouse LA/BA [5], and atlas precomputed Cnr1 (mean 12.36, 98.5th pct) and Cck (mean 11.15, 98.3rd pct) expression both tier-2 reliable and cohort-dominant. Key caveats: AT_ABSENT (no annotation-transfer evidence; confidence ceiling applies) and CARDINALITY_1_N (five sibling Sncg Gaba_1 clusters score equally; the classical type may span multiple clusters).

The Cell Ontology has no specific term for this population; basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**Experiment 1 — Annotation transfer (MapMyCells)**
- **What:** MapMyCells AT on a BLA CCK/CB1 basket cell patch-seq or snRNA-seq source dataset, mapping to CCN20230722 at cluster level.
- **Target:** F1 ≥ 0.50 at CLUSTER level, discriminating CLUS_0664 from sibling Sncg clusters (0665, 0666, 0672, 0677).
- **Expected output:** AnnotationTransferEvidence items on the edge; confidence upgrade to MODERATE or HIGH pending F1 outcome.
- **Resolves:** CARDINALITY_1_N caveat; AT_ABSENT caveat; Open question 1.

**Experiment 2 — Multiplexed smFISH**
- **What:** Multiplexed smFISH with Sncg + Cnr1 + Cck probes in mouse BLA sections.
- **Target:** Confirm co-expression at single-cell level; quantify proportion of Sncg+ cells that are Cnr1+Cck+ in BLA; identify if any Sncg subpopulation is BLA-enriched vs cortically distributed.
- **Expected output:** LiteratureEvidence with marker co-expression rates; region_fraction re-assessment.
- **Resolves:** LOW_BLA_CELL_COUNT caveat; Open question 2.

**Experiment 3 — Taxonomy DB rebuild**
- **What:** Run `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` for this node.
- **Target:** Populate `n_cells` for CLUS_0664 and all sibling Sncg clusters; enable cell-count-informed cardinality table.
- **Expected output:** Updated facts file with `n_cells` values.
- **Resolves:** Missing cell count in mapping candidates table.

### Open questions

1. What distinguishes CS20230722_CLUS_0664 from sibling clusters CLUS_0665, CLUS_0666, CLUS_0672, CLUS_0677 — all score 5/5 equally on Cnr1 and Cck? Is there a sub-expression feature (co-expressed gene, splicing variant, layer preference) that resolves the 1:N to a 1:1?
2. Is Cnr1 confirmed at single-cell level in CLUS_0664 in the full expression matrix, or does the precomputed mean reflect a subset of cells? The absence of Cnr1 from the formal DEFINING atlas marker list warrants targeted investigation.

---

## References

| Label | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vereczki et al. 2016 | PMID:27013983 | soma location; morphology; Cnr1 marker; Cck neuropeptide |
| [2] | McDonald et al. 2012 | PMID:22837739 | neurotransmitter type; Cck neuropeptide |
| [3] | Rovira-Esteban et al. 2019 | PMID:31636080 | Cnr1 marker; Cck neuropeptide |
| [4] | Woodruff & Sah 2007 | PMID:17234587 | Cnr1 marker |
| [5] | Vereczki et al. 2021 | PMID:33837051 | 71.1% of CCK+ interneurons confirmed as CCK+/CB1+ basket cells |
| [6] | Totty et al. 2024 | PMID:39463931 | primate snRNA-seq CCK+/CNR1+ cluster homologous to mouse CCK basket cell; Sncg co-expression |

---

<!-- verdict-block-start: edge_bla_cck_cb1_basket_cell_to_cs20230722_clus_0664 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.28
  rationale: >
    CS20230722_CLUS_0664 (Sncg Gaba_1) is the top-ranked BLA GABAergic cluster
    candidate, with Cnr1 precomputed mean 12.36 (cohort 98.5th pct; tier 2) and
    Cck mean 11.15 (cohort 98.3rd pct; tier 2) — both markers CONSISTENT with
    the classical CCK/CB1 basket cell definition. Vereczki et al. 2021
    (PMID:33837051) provides primary in vivo quantification via
    GFP-targeted patch recording confirming CCK+/CB1+ basket cells as 71.1%
    of CCK interneurons in mouse LA/BA. Yu et al. 2024 (PMID:39463931) provides
    cross-species snRNA-seq support linking the Sncg supertype label to CCK basket
    cell identity. Confidence capped at LOW: no annotation-transfer evidence exists
    (AT_ABSENT), and 1 of 1 marker comparisons CONSISTENT does not resolve the
    CARDINALITY_1_N caveat (five Sncg Gaba_1 clusters score equally).
  reconciliation_note: >
    Five sibling clusters (CLUS_0664, CLUS_0665, CLUS_0666, CLUS_0672, CLUS_0677)
    are indistinguishable from available atlas metadata on Cnr1 and Cck expression
    alone. The classical CCK/CB1 basket cell may map 1:N to this Sncg cluster group.
    Annotation transfer is required to resolve cardinality before confidence can
    exceed LOW.
  unresolved_questions:
    - "What distinguishes CS20230722_CLUS_0664 from sibling CLUS_0665/0666/0672/0677 — all score 5/5 equally?"
    - "Is Cnr1 confirmed at single-cell level in CLUS_0664 in the full expression matrix?"
```
<!-- verdict-block-end -->
