# Basolateral amygdala LAMP5-expressing interneuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

LAMP5-expressing interneurons represent one of five major canonical inhibitory cell classes in the amygdala (SST, PVALB, VIP, CCK, and LAMP5), resolved by cross-species snRNA-seq atlases spanning rodents and primates [1][2]. They are GABAergic and are characterised by expression of the LAMP5 gene, encoding Lysosomal-Associated Membrane Protein Family Member 5. Mapping this type to the Allen CCN20230722 mouse atlas matters because LAMP5+ interneurons show pronounced primate enrichment relative to rodent amygdala — a cross-species asymmetry that complicates direct homology assignment and makes the mapping confidence ceiling lower than for more conserved interneuron classes.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| Neurotransmitter | GABAergic | [1][2] |
| Defining markers | Lamp5 | [1][2] |
| Negative markers | — | |
| Neuropeptides | — | |
| CL term | None assigned | |
| Definition basis | CLASSICAL (stub) | |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** snRNA-seq survey · primate amygdala (human + NHP) · [1]
  > The majority of amygdala neurons are located in the lateral, basal, accessory basal, intercalated and central nuclei
  > — Totty et al. 2024, Medial, cortical/superficial, and intercalated cell populations · [1] <!-- quote_key: 273531817_7816d0f1 -->

- **Neurotransmitter:** snRNA-seq · cross-species (human, macaque, mouse, rat) · [2]
  > In all four species, all major brain cell classes were identified according to canonical cell-type marker genes, including excitatory neurons, inhibitory neurons, astrocytes, oligodendrocytes, oligodendrocyte progenitor cells (OPC), ependymal cells, microglia/ macrophages, endothelial cells, and mural cells (Supplementary Fig. S1d, e).
  > — Yu et al. 2023, rodents · [2] <!-- quote_key: 256832817_37265577 -->

- **Defining marker — Lamp5:** snRNA-seq · primate amygdala · [1][2]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0710 in SUPT_0199 (Lamp5 Gaba_1) is the primary mapping at LOW confidence, driven by strong Lamp5 marker consistency but limited by low BLA region fraction, multi-cluster ambiguity, and absent annotation-transfer evidence.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0710 | SUPT_0199 (Lamp5 Gaba_1) | not available | 🔴 LOW | Lamp5 CONSISTENT · Location APPROXIMATE | skos:broadMatch |

Note: 1 edge assessed; relationship type skos:broadMatch (1:n).

**4b. Property alignment table — CS20230722_CLUS_0710**

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | MBA:295 BLA present; region_fraction 0.02 | CS20230722_CLUS_0710 (Lamp5 Gaba_1); BLA not primary distribution | APPROXIMATE |
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Lamp5 expression | defining marker (PMID:39463931, PMID:36788214) | Lamp5 mean 8.78 (BLA GABAergic cohort 99.8th pct; tier 2) | CS20230722_CLUS_0710 "Lamp5 Gaba_1" | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Totty 2024 primate snRNA-seq | Literature | SUPPORT | LAMP5 one of 5 canonical BLA interneuron classes; cross-species mouse homolog confirmed | [1] |
| Yu 2023 cross-species snRNA-seq | Literature | SUPPORT | All major interneuron classes including LAMP5 identified in 4 species | [2] |
| Atlas precomputed expression | Atlas metadata | SUPPORT | Lamp5 mean 8.78; 99.8th pct BLA GABAergic cohort; tier-2 reliable | atlas-internal |

*(Child-cluster breakdown not assessed in the available property comparisons — four rank-0 clusters (0710/0711/0712/0713) under SUPT_0199 all score equally on Lamp5 alone; see proposed experiments.)*

### CS20230722_CLUS_0710 (Lamp5 Gaba_1) · 🔴 LOW

**Supporting evidence:**

- **Lamp5 marker CONSISTENT.** CLUS_0710 ("Lamp5 Gaba_1") expresses Lamp5 at a precomputed mean of 8.78, placing it at the 99.8th percentile of the BLA GABAergic cohort (tier-2 reliable; EXPRESSION source). This provides strong marker-level support for the cluster assignment. The discovery cohort contained 5 BLA GABAergic members (rank 0, NT = GABAergic, region = MBA:295); CLUS_0710 ranked 1st, tied with three sibling clusters (all score 3/3 on Lamp5). Stage A discovery score: 3 in a cohort of 5, next-best score also 3 — tied dominance, not exclusive.
- **NT type CONSISTENT.** CLUS_0710 is annotated GABA in WMBv1, concordant with the classical type's GABAergic identity [1][2].
- **Cross-species literature support.** Totty et al. 2024 [1] resolves LAMP5 as one of 18 primate amygdala inhibitory types, with all five major interneuron classes (SST, PVALB, VIP, CCK, LAMP5) represented. Yu et al. 2023 [2] independently confirms LAMP5+ interneurons as a canonical class across four mammalian species. Both sources confirm the existence of a mouse BLA homolog, supporting atlas mapping in principle.

**Marker evidence provenance:**

- **Lamp5 (defining marker):** Evidence is transcript-level (snRNA-seq) from two independent cross-species atlases [1][2]. No protein-level (IHC, immunofluorescence) or electrophysiological confirmation is cited for mouse BLA LAMP5+ cells specifically. The canonical identity rests entirely on transcriptomic marker expression; morphological or functional properties of mouse BLA LAMP5+ interneurons are not documented in the gathered evidence. The stub note on the classical node explicitly flags this as a pending characterisation. The atlas-side Lamp5 expression value (mean 8.78, 99.8th pct) confirms strong, reliable expression, consistent with the marker classification.
- **Weak source-side specificity:** Both source papers characterise primate (human/NHP) amygdala. Mouse-specific validation of LAMP5+ interneuron identity in the BLA is inferred from cross-species homology. No primary citations confirm morphological reconstruction or electrophysiological characterisation of mouse BLA LAMP5+ cells. This underdetermined classical type definition is the primary limiter on mapping confidence.

**Concerns:**

- **Location APPROXIMATE — low region fraction.** CLUS_0710 has region_fraction 0.02 in MBA:295 (BLA). BLA is not the primary distribution of this cluster. The low fraction is biologically interpretable — cross-species snRNA-seq (Yu 2023 [2]) confirms LAMP5+ interneurons are notably more abundant in primate than rodent amygdala — but it means the mouse atlas does not densely represent this population in BLA. This is consistent with the primate-enriched biology described in the node notes, but remains a genuine concern for mapping specificity.
- **Multi-cluster ambiguity (DISTRIBUTED_ACROSS_CLUSTERS).** Five Lamp5 Gaba clusters score equally on Lamp5 alone: CLUS_0710, 0711, 0712, 0713 (all under SUPT_0199 / Lamp5 Gaba_1) and CLUS_0723 (under SUPT_0202 / Lamp5 Gaba_4). The classical type may span both SUPT_0199 and SUPT_0202 supertypes. CLUS_0710 is the top-ranked representative by discovery but is not distinguishable from its three SUPT_0199 siblings on available evidence alone.
- **CROSS_SPECIES_EXTRAPOLATION.** The classical type is defined primarily from primate data. Direct mouse-BLA LAMP5+ interneuron characterisation is absent. WMBv1 BLA representation is sparse (region_fraction 0.02–0.056 across rank-0 candidates).
- **Stub node with minimal evidence.** bla_lamp5_interneuron is a STUB node. Morphology, electrophysiology, and detailed species-specific evidence are absent. The underdetermined classical type definition limits the mapping confidence ceiling to LOW regardless of atlas-side evidence quality.
- **No annotation-transfer evidence.** No MapMyCells AT run has been completed for this node. AT evidence would be the most direct path to upgrading confidence.

**What would upgrade confidence:**

- **Annotation transfer (MapMyCells).** Run MapMyCells on a mouse BLA LAMP5+ scRNA-seq dataset against CCN20230722. Target: AnnotationTransferEvidence with F1 ≥ 0.60 at cluster level. Expected output: resolves ambiguity among CLUS_0710/0711/0712/0713 and tests the SUPT_0199 vs SUPT_0202 split. Resolves: `edge_bla_lamp5_interneuron_to_cs20230722_clus_0710`; unresolved questions 1 and 2.
- **Patch-seq in mouse BLA targeting Lamp5-Cre labelled cells.** Obtains transcriptomes with morphological and electrophysiological co-registration for direct WMBv1 cluster assignment. Expected output: AnnotationTransferEvidence or PATCH_SEQ evidence at cluster level. Resolves unresolved questions 1 and 2, and would upgrade morphology and electrophysiology fields on the classical node stub.
- **smFISH multiplex (Lamp5 + Cplx3 + Htr2a in mouse BLA).** Would quantify LAMP5+ cell abundance in mouse BLA and test SUPT_0199 cluster-marker co-expression. Expected output: LiteratureEvidence or direct MarkerAnalysisEvidence. Resolves the low-region-fraction concern and the multi-cluster ambiguity.
- **Targeted literature search.** A cite-traverse for "LAMP5 interneuron amygdala mouse" or "Lamp5 BLA rodent electrophysiology morphology" may uncover mouse-specific characterisation not captured in the gathered cross-species atlases. This is a low-cost preliminary step before committing to experimental work.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Basolateral amygdala LAMP5-expressing interneuron (bla_lamp5_interneuron) is defined on a CLASSICAL basis. The classical type is GABAergic with Lamp5 as its sole defining marker, located in the basolateral amygdala [UBERON:0002887]. It was identified as a major canonical inhibitory interneuron class in primate amygdala by Totty et al. 2024 [1] and independently confirmed by Yu et al. 2023 [2] in a four-species cross-species snRNA-seq atlas. This is a STUB node: morphological, electrophysiological, and species-specific rodent properties are not yet documented. The definition basis is CLASSICAL rather than CLASSICAL_MULTIMODAL due to the absence of functional or morphological corroboration.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match = MBA:295, NT type = GABAergic, defining marker = Lamp5). Full scoring rules: `workflows/map-cell-type.md`. Discovery cohort: 5 BLA GABAergic rank-0 members. CLUS_0710 selected as representative top-ranked candidate.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**

| Field | Value |
|---|---|
| Atlas | CCN20230722 |
| Taxonomy ID | CS20230722 |
| Node | CLUS_0710 / SUPT_0199 |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_lamp5_interneuron_to_cs20230722_clus_0710 | LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT | [1]; [2]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:52+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala LAMP5-expressing interneuron → CS20230722_CLUS_0710 (Lamp5 Gaba_1) at LOW confidence. Key support: Lamp5 marker CONSISTENT at 99.8th pct of BLA GABAergic cohort; GABAergic NT concordant; cross-species literature confirms existence of mouse homolog. Key caveats: BLA region_fraction 0.02 (primate-enriched biology, sparse in mouse atlas); stub node with underdetermined classical type definition; four sibling SUPT_0199 clusters are indistinguishable on Lamp5 alone; no annotation-transfer evidence.

No Cell Ontology term currently assigned. The node notes indicate this is a candidate for CL contribution once characterisation of mouse BLA LAMP5+ interneurons is advanced beyond the current stub level.

### Proposed experiments and follow-ups

**1. Annotation transfer — MapMyCells**
- **What:** Run MapMyCells against CCN20230722 using a mouse BLA scRNA-seq or snRNA-seq source dataset with Lamp5+ cell labelling.
- **Target:** F1 ≥ 0.60 at cluster level distinguishing CLUS_0710 from CLUS_0711/0712/0713; secondary test of SUPT_0199 vs SUPT_0202 separation.
- **Expected output:** `AnnotationTransferEvidence` added to `edge_bla_lamp5_interneuron_to_cs20230722_clus_0710`.
- **Resolves:** Unresolved questions 1 and 2; multi-cluster ambiguity caveat.

**2. Patch-seq in mouse BLA (Lamp5-Cre)**
- **What:** Patch-seq targeting Lamp5-Cre labelled cells in mouse BLA slice, with biocytin fill for morphology and electrophysiological characterisation, followed by single-cell RNA-seq for WMBv1 cluster assignment.
- **Target:** Cluster assignment to rank-0 cluster level; morphological and electrophysiological fields populated on the classical node.
- **Expected output:** `AnnotationTransferEvidence` (patch-seq); upgrade of classical node definition_basis from CLASSICAL to CLASSICAL_MULTIMODAL.
- **Resolves:** Unresolved questions 1 and 2; stub status of bla_lamp5_interneuron; cross-species extrapolation caveat.

**3. smFISH multiplex in mouse BLA**
- **What:** smFISH with Lamp5 + SUPT_0199 markers (Cplx3, Htr2a) and a SUPT_0202 marker in mouse BLA coronal sections.
- **Target:** Quantify LAMP5+ cell density in BLA; assess co-expression with SUPT_0199 vs SUPT_0202 markers.
- **Expected output:** `LiteratureEvidence` or direct `MarkerAnalysisEvidence` on the edge.
- **Resolves:** Low-region-fraction concern; multi-supertype ambiguity (SUPT_0199 vs SUPT_0202).

**4. Targeted literature search**
- **What:** Cite-traverse for "LAMP5 interneuron amygdala mouse" and "Lamp5 BLA rodent electrophysiology morphology" against the existing ASTA corpus and broader PubMed/Europe PMC.
- **Target:** Identify any primary rodent-BLA characterisation of LAMP5+ interneurons not captured in the current two cross-species atlases.
- **Expected output:** Additional `LiteratureEvidence` items; possibly upgrade of classical node marker set or morphology fields.
- **Resolves:** Underdetermined classical type definition; weak source-side specificity of marker evidence.

### Open questions

1. What distinguishes CS20230722_CLUS_0710 from CLUS_0711/0712/0713 — all four score equally on Lamp5 alone? (edge_bla_lamp5_interneuron_to_cs20230722_clus_0710)
2. Are there additional markers or electrophysiological properties of mouse BLA LAMP5+ interneurons that resolve cluster membership? (edge_bla_lamp5_interneuron_to_cs20230722_clus_0710)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931/) | soma location; defining marker; NT type |
| [2] | Yu et al. 2023 | [36788214](https://pubmed.ncbi.nlm.nih.gov/36788214/) | neurotransmitter type; defining marker |

---

<!-- verdict-block-start: edge_bla_lamp5_interneuron_to_cs20230722_clus_0710 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    Lamp5 marker CONSISTENT at 99.8th pct BLA GABAergic cohort (EXPRESSION source;
    precomputed mean 8.78; tier 2; applied_score 2.0); NT type CONSISTENT (GABA).
    Cross-species literature [1][2] confirms mouse BLA Lamp5+ homolog.
    skos:broadMatch 1:n justified by multi-cluster ambiguity: four sibling
    clusters (0710/0711/0712/0713) under SUPT_0199 and one under SUPT_0202 all
    score equally on Lamp5 alone; region_fraction 0.02 reflects primate-enriched
    biology sparse in mouse atlas. No ANNOTATION_TRANSFER evidence; classical node
    is a STUB with minimal available evidence on soma form, physiology, and
    species-specific properties.
  reconciliation_note: ""
  lit_to_lit_edges: []
  unresolved_questions:
    - "Run MapMyCells AT on mouse BLA Lamp5+ source dataset to resolve CLUS_0710 vs 0711/0712/0713 ambiguity and test SUPT_0199 vs SUPT_0202 split."
    - "Targeted literature search for Lamp5 interneuron amygdala mouse to identify rodent-specific characterisation beyond current cross-species atlases."
```
<!-- verdict-block-end -->
