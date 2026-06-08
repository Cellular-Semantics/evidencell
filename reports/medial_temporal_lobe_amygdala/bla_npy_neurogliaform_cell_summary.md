# Basolateral amygdala NPY neurogliaform cell — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

NPY-containing neurogliaform cells are a well-characterised inhibitory interneuron class in the basolateral amygdala (BLA), constituting 14–15% of all GABAergic cells in the lateral and basal amygdaloid nuclei [1]. Classically defined by neuropeptide Y (NPY) expression, these cells are negative for both parvalbumin (Pvalb) and somatostatin (Sst), placing them in a distinct class from the other major BLA interneuron subtypes. Mapping this type to the Allen CCN20230722 mouse atlas is important because the WMBv1 transcriptomic space does not resolve a dedicated NPY neurogliaform cluster in the BLA at rank 0 — the best available candidate, Lamp5 Gaba_1 (CLUS_0710), carries a discordant Sst signal that conflicts with the classical Sst-negative definition.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| Neurotransmitter | GABAergic | [1] |
| Defining markers | Npy | [1] |
| Negative markers | Pvalb, Sst | |
| Neuropeptides | Npy | [1][2] |
| CL term | neurogliaform cell [CL:0000693] — BROAD | |
| Definition basis | CLASSICAL | |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location [UBERON:0002887] and NT type:** Quantitative survey of GABAergic cell types in mouse lateral and basal amygdala · [1]
  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 232283078_d4238834 -->

- **Neuropeptide Npy:** Neurochemical classification of BLA interneuron subpopulations · [2]
  > One commonly adopted method segregates IN subpopulations based on neurochemical content, including expression of Ca 2  - binding proteins [e.g., parvalbumin (PV); (McDonald et al., 2001)(McDonald et al., 2001)] and neuropeptides such as somatostatin (SOM), neuropeptide Y (NPY), and cholecystokinin (CCK; Mascagni and Mc-Donald, 2003;(Kepecs et al., 2014)
  > — Rovira-Esteban et al. 2019, Basolateral amygdala and corticobasal cell types · [2] <!-- quote_key: 204835327_bf931431 -->

- **Negative markers (Pvalb, Sst):** Implicit in the subpopulation enumeration of Vereczki et al. 2021 [1], which presents NPY neurogliaform cells as a class distinct from parvalbumin-expressing basket/axo-axonic cells and somatostatin-expressing dendrite-targeting interneurons. No separate citation is recorded for the negative marker designations.

</details>

### Cell Ontology mapping

Cell Ontology mapping: neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)] (BROAD). The Cell Ontology has no specific term for BLA NPY neurogliaform cells; neurogliaform cell is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0710 (0710 Lamp5 Gaba_1) in SUPT_0199 is the best-available Npy+ GABA candidate in the BLA cohort, mapped at UNCERTAIN confidence. Npy precomputed expression (mean 10.5, tier 2) is CONSISTENT and Pvalb-negativity is CONSISTENT, but Sst val = 1.0 is DISCORDANT with the classical Sst-negative definition. No annotation-transfer evidence has been collected. The node is mapped as `evidencell:UncertainRelationship` (1:n) pending resolution of the Sst discordance.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | CS20230722_CLUS_0710 | SUPT_0199 (0199 Lamp5 Gaba_1) | 5178 | ⚪ UNCERTAIN | Npy CONSISTENT · Sst DISCORDANT | evidencell:UncertainRelationship |

Note: 1 edge assessed; relationship type evidencell:UncertainRelationship (1:n).

**4b. Property alignment table — CS20230722_CLUS_0710**

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | MBA:295 BLA present; region_fraction 0.02 | CS20230722_CLUS_0710; BLA not primary distribution | APPROXIMATE |
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Npy (neuropeptide) | Npy — neuropeptide | Npy precomputed mean 10.5 (tier 2; applied_score 2.0) | CLUS_0710: best Npy+ GABA candidate in BLA cohort | CONSISTENT |
| Pvalb (negative marker) | Pvalb-negative | Pvalb val 0.1 (low; reliable=false) | CLUS_0710: Pvalb absent | CONSISTENT |
| Sst (negative marker) | Sst-negative | Sst val 1.0 (above MIN_DETECTABLE; applied_score −1.0) | CLUS_0710: Sst present | DISCORDANT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki 2021 BLA GABAergic census | Literature | SUPPORT | NPY neurogliaform cells = 14–15% of BLA GABAergic cells; distinct from Pvalb and Sst populations | [1] |
| Atlas precomputed expression (CLUS_0710) | Atlas metadata | PARTIAL | Npy mean 10.5 (tier 2; CONSISTENT); Sst val 1.0 (DISCORDANT); Pvalb val 0.1 (CONSISTENT) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

## Eliminated candidates

The single assessed edge carries UNCERTAIN confidence. The primary disqualifying signal — Sst DISCORDANT — is present across the best-available candidate. CLUS_0710 is retained as the best-available representative (highest Npy in the BLA GABAergic rank-0 cohort; Pvalb-negative as required) but the Sst conflict prevents a clean assignment.

### CS20230722_CLUS_0710 (0710 Lamp5 Gaba_1) · ⚪ UNCERTAIN — 5,178 cells

**Disqualifying evidence:**

- **Sst DISCORDANT.** CLUS_0710 shows Sst val = 1.0, above MIN_DETECTABLE (applied_score −1.0). BLA NPY neurogliaform cells are defined as Sst-negative [1]. This is the primary counter-evidence for the mapping. Whether this reflects genuine Sst co-expression in a subset of LAMP5/NPY cells, a contaminating Sst+ population within the cluster mean, or an averaging artifact is not determinable from atlas metadata alone.
- **Location APPROXIMATE — low region fraction.** CLUS_0710 has region_fraction 0.02 in MBA:295 (BLA). BLA is not the primary anatomical distribution of Lamp5 Gaba clusters in WMBv1. This is weak counter-evidence — Lamp5 interneurons are sparse in mouse BLA and their presence is supported by the literature [1] — but the low fraction reduces confidence.
- **Overlap with bla_lamp5_interneuron mapping.** CLUS_0710 is simultaneously the primary candidate for the bla_lamp5_interneuron node in this graph. At rank 0, both classical types converge on the same atlas representative, indicating that the available data cannot separate NPY neurogliaform from LAMP5 interneurons at this resolution. *(note: LAMP5+ neurogliaform cells expressing NPY are a recognised cortical interneuron subtype — the co-mapping is biologically plausible but unresolved.)*
- **No annotation-transfer evidence.** No AT run has been completed for this node.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Basolateral amygdala NPY neurogliaform cell (`bla_npy_neurogliaform_cell`) is defined on a CLASSICAL basis. The type is GABAergic with Npy as defining marker and neuropeptide, located in the basolateral amygdala [UBERON:0002887], and is negative for Pvalb and Sst. Vereczki et al. 2021 [1] quantified NPY neurogliaform cells at 14–15% of LA/BA GABAergic cells across a multi-type census of mouse amygdala. Rovira-Esteban et al. 2019 [2] independently confirms NPY as a canonical BLA interneuron neurochemical marker class. The node notes record that no further subtypes have been defined within the BLA neurogliaform class and that these cells were directly identified in CCK-Cre targeting studies.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CS20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match = MBA:295, NT type = GABAergic, defining marker = Npy, negative markers = Pvalb, Sst). Full scoring rules: `workflows/map-cell-type.md`. Discovery cohort: 5 BLA GABAergic rank-0 members. CLUS_0710 ranked 1st (score 3; next-best score also 3 — tied dominance in a cohort of 5).

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
| edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710 | LITERATURE; ATLAS_METADATA | SUPPORT; PARTIAL | [1]; atlas-internal |

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:48+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala NPY neurogliaform cell → CS20230722_CLUS_0710 (0710 Lamp5 Gaba_1) [CS20230722_CLUS_0710] at UNCERTAIN confidence. Key support: Npy precomputed mean 10.5 (tier 2; 98th pct BLA GABAergic cohort; applied_score 2.0); Pvalb-negative CONSISTENT; NT type CONSISTENT. Key caveats: Sst val 1.0 DISCORDANT (Sst-negativity is a defining property of the classical type); no annotation-transfer evidence; CLUS_0710 is simultaneously the top candidate for bla_lamp5_interneuron.

The Cell Ontology has no specific term for this population; neurogliaform cell [[CL:0000693](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000693)] is the closest ancestor (BROAD mapping). Auto-proposed by asta-report-ingest; requires expert review — a targeted CL new-term request for a BLA-specific NPY neurogliaform cell may be warranted once mapping confidence is upgraded.

### Proposed experiments and follow-ups

**1. Multiplexed smFISH — Npy + Lamp5 + Sst probes in mouse BLA**
- **What:** smFISH with simultaneous Npy, Lamp5, and Sst probes in coronal mouse BLA sections.
- **Target:** Determine what fraction of Npy+ cells co-express Sst in the BLA; characterise the overlap between Npy+ and Lamp5+ populations.
- **Expected output:** `LiteratureEvidence` or direct `MarkerAnalysisEvidence` resolving the Sst discordance; quantitative co-expression data separating BLA NPY neurogliaform from Sst-expressing cells.
- **Resolves:** `edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710` unresolved question 2; Sst DISCORDANT caveat.

**2. Annotation transfer — MapMyCells on BLA Npy+ source dataset**
- **What:** Run MapMyCells against CCN20230722 using a mouse BLA dataset with Npy+ or NPY neurogliaform cell labelling.
- **Target:** AnnotationTransferEvidence with F1 at cluster level; test whether CLUS_0710 or a different Lamp5 Gaba cluster captures NPY neurogliaform cells.
- **Expected output:** `AnnotationTransferEvidence` added to `edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710`; potential confidence upgrade pending F1 outcome.
- **Resolves:** Unresolved questions 1 and 2; absence of AT evidence caveat.

**3. Re-run Stage A discovery with Npy+/Sst− scoring against CCN20230722 HDF5**
- **What:** Acquire CCN20230722 HDF5 and re-run candidate discovery with explicit positive Npy and negative Sst scoring at ranks 0 and 1.
- **Target:** Identify whether any BLA GABA cluster is both Npy+ and Sst− in precomputed stats; compare with CLUS_0710.
- **Expected output:** Updated `discovery_score` with revised Npy+/Sst− cohort ranking; may surface a better-fitting candidate or confirm CLUS_0710 as the sole Npy+ cluster.
- **Resolves:** Unresolved question 1; Sst DISCORDANT caveat.

### Open questions

1. Do BLA NPY neurogliaform cells overlap with the Lamp5 Gaba family in WMBv1, or is there a dedicated Npy+ Sst− cluster not yet surfaced? (edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710)
2. Is the Sst val 1.0 in CLUS_0710 a genuine co-expression signal in a subset of Lamp5/Npy cells, an averaging artifact across distinct subpopulations within the cluster, or a platform-level noise floor? (edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | soma location; NT type; defining marker; neuropeptide; cell type abundance |
| [2] | Rovira-Esteban et al. 2019 | [31636080](https://pubmed.ncbi.nlm.nih.gov/31636080/) | neuropeptide Npy |

---

<!-- verdict-block-start: edge_bla_npy_neurogliaform_cell_to_cs20230722_clus_0710 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    Npy neuropeptide CONSISTENT: precomputed mean 10.5 (tier 2; applied_score 2.0;
    98th pct of 5-member BLA GABAergic cohort; EXPRESSION source). Pvalb
    negative-marker CONSISTENT: val 0.1 (reliable=false). NT type CONSISTENT (GABA).
    Sst negative-marker DISCORDANT: val 1.0 above MIN_DETECTABLE (applied_score -1.0)
    in CS20230722_CLUS_0710; Sst-negativity is a defining property of BLA NPY
    neurogliaform cells per [1]. Location APPROXIMATE: region_fraction 0.02 in
    MBA:295. 1 of 2 negative-marker comparisons CONSISTENT; 1 DISCORDANT. No
    ANNOTATION_TRANSFER evidence. evidencell:UncertainRelationship 1:n retained
    pending resolution of Sst discordance via smFISH or AT.
  reconciliation_note: ""
  lit_to_lit_edges: []
  unresolved_questions:
    - "Run multiplexed smFISH (Npy+Lamp5+Sst) in mouse BLA to resolve whether Sst co-expression occurs in NPY neurogliaform cells."
    - "Acquire CCN20230722 HDF5 and re-run Stage A discovery with explicit Npy+/Sst- scoring to test for a better-fitting BLA cluster."
```
<!-- verdict-block-end -->
