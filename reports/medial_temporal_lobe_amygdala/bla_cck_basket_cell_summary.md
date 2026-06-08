# Basolateral amygdala cholecystokinin basket cell — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala cholecystokinin (CCK) basket cell is a classically defined GABAergic interneuron of the lateral and basal amygdaloid nuclei (basolateral amygdaloid area [UBERON:0002887]). It is distinguished by co-expression of cholecystokinin (Cck) and the calcium-binding protein calbindin-D28K (Calb1), and by the absence of parvalbumin (Pvalb), forming a perisomatic inhibitory system chemically distinct from the parvalbumin basket cell class [1], [2], [3]. Vereczki et al. 2021 estimated that CCK basket cells constitute 7–9% of all GABAergic neurons in the lateral and basal amygdala, confirming that this is a numerically minor but functionally important inhibitory subtype [2]. Mapping this classical type to the CCN20230722 transcriptomic atlas is important for linking classical neurochemical descriptions of BLA inhibitory circuits to genome-wide expression profiles.

---

### Classical type table

| Property | Value | References |
|---|---|---|
| Node ID | `bla_cck_basket_cell` | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | [1], [2] |
| Soma location | Basolateral amygdaloid area [UBERON:0002887] | [1], [2] |
| Defining markers | Cck, Calb1 | [1], [2], [3], [4] |
| Neuropeptides | Cck | [1], [2] |
| Negative markers | Pvalb | [2] |
| CL mapping | basket cell [CL:0000118] — BROAD | — |
| Notes | Large multipolar CCK+/CB+ neurons (McDonald et al., 2012) and CCK basket cells (Vereczki et al., 2021) may represent overlapping or distinct populations. | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (UBERON:0002887), NT type (GABAergic), defining markers Cck and Calb1, neuropeptide Cck:** Literature synthesis of BLA GABAergic interneuron subtypes · [1]
  > "The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982)(McDonald, 1985)(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003(Millhouse et al., 1983)(Fuller et al., 1987)(Carlsen et al., 1988)(McDonald et al., 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;"
  > — McDonald et al. 2012, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 11544073_ea8d2bb3 -->

- **Defining markers Cck and Calb1, neuropeptide Cck, NT type (GABAergic), negative marker Pvalb:** Quantitative census of GABAergic cell types in mouse lateral and basal amygdala · [2]
  > "we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions."
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [2] <!-- quote_key: 232283078_d4238834 -->

- **Defining markers Cck and Calb1:** Classification of BLA interneurons by calcium-binding protein and neuropeptide content · [3]
  > "Four populations of interneurons have been described in the BLA: those expressing parvalbumin (McDonald, 1992;Mc-Donald and Betette, 2001), those expressing somatostatin (Mc-Donald and Mascagni, 2002), those expressing cholecystokinin"
  > — Woodruff & Sah 2007, Basolateral amygdala neuronal subtypes · [3] <!-- quote_key: 161407_eb8bfaf0 -->

- **Defining marker Cck (cross-species snRNA-seq):** Primate amygdala snRNA-seq identifies a CCK+/CNR1+ cluster proposed as homologue of mouse CCK basket cells · [4]
  > "A third cluster of CCK + neurons (CCK + /CNR1 + ) consisted of 5.28% of all inhibitory neurons analyzed... This CCK + /CNR1 + cluster is likely homologous to mouse CCK + basket cells, which synapse onto the soma and proximal dendrites of excitatory neurons"
  > — Totty et al. 2024, GABAergic neuron types in the primate am · [4] <!-- quote_key: 273531817_26309a28 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD). The Cell Ontology has no specific term for this population; basket cell is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster was assessed: 0664 Sncg Gaba_1 [CS20230722_CLUS_0664], 179 cells (10x), supertype 0185 Sncg Gaba_1. The primary verdict is LOW confidence (`skos:closeMatch`), supported by precomputed expression showing Cck mean 11.15 (98.3rd pct) and Cnr1 mean 12.36 (98.5th pct) — both tier-2 reliable — and corroborated by a literature evidence item from Vereczki et al. 2021 confirming 71.1% of BLA CCK+ interneurons are CCK+/CB1+ basket cells. Confidence is capped at LOW because no annotation-transfer evidence has been run, and five sibling Sncg Gaba_1 clusters score equally on the Cck+Cnr1 profile, leaving the 1:N cardinality unresolved.

**Note on overlap with `bla_cck_cb1_basket_cell`.** Both `bla_cck_basket_cell` (this node) and `bla_cck_cb1_basket_cell` are mapped to the same atlas cluster, CS20230722_CLUS_0664. The classical nodes may partially overlap: the `bla_cck_basket_cell` definition emphasises Calb1 co-expression and Pvalb negativity, while `bla_cck_cb1_basket_cell` emphasises Cnr1 (CB1). Calb1 co-expression could not be assessed from current atlas data (no precomputed Calb1 comparison is available). Curator review of node distinctiveness is recommended.

### 4a. Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10×) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0664 Sncg Gaba_1 [CS20230722_CLUS_0664] | 0185 Sncg Gaba_1 | 179 | 🔴 LOW | Cck CONSISTENT · NT CONSISTENT | skos:closeMatch |

*1 edge total; relationship: `skos:closeMatch`.*

### 4b. Property alignment — 0664 Sncg Gaba_1 [CS20230722_CLUS_0664]

**Table 1 — Property comparison.**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| Soma location | Basolateral amygdaloid area [UBERON:0002887] | MBA:295 BLA present; region_fraction 0.031 | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Cck (neuropeptide) | Cck — neuropeptide | precomputed mean 11.15 (98.3rd pct; tier 2); Sncg supertype is canonical CCK co-expression group | CONSISTENT |
| Calb1 expression | defining marker | not assessed — no precomputed Calb1 comparison available | NOT_ASSESSED |
| Pvalb expression | negative marker | Sncg lineage is circumstantially consistent with Pvalb-negativity; not formally assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki et al. 2021 CCK basket cell fraction | Literature | SUPPORT | 71.1% of CCK+ interneurons confirmed CCK+/CB1+ basket cells by GFP-targeted patch recording | [2] |
| CLUS_0664 atlas precomputed expression | Atlas metadata | SUPPORT | Cnr1 mean 12.36 (98.5th pct), Cck mean 11.15 (98.3rd pct) — both tier-2 reliable | atlas-internal |

*(Child-cluster breakdown not assessed — five sibling Sncg Gaba_1 clusters all score equally on Cnr1+Cck; see proposed experiments.)*

---

### 0664 Sncg Gaba_1 [CS20230722_CLUS_0664] · 🔴 LOW

**Supporting evidence:**

- **Atlas expression anchor.** CS20230722_CLUS_0664 carries Cnr1 mean 12.36 (98.5th pct) and Cck mean 11.15 (98.3rd pct) in the BLA GABAergic rank-0 cohort. Both are tier-2 reliable from EXPRESSION source. The Sncg supertype is the canonical CCK co-expression group in the WMBv1 mouse atlas, providing a lineage-level anchor consistent with the CCK basket cell profile. *(atlas-internal)*

- **Vereczki et al. 2021 direct quantification.** A key literature evidence item confirms that the dominant fate of CCK+ interneurons in mouse LA/BA is the CCK+/CB1+ basket cell identity: 71.1% of GFP-expressing CCK+ neurons recorded in vivo were confirmed basket cells by CB1 immunoreactivity on axon terminals [2].

  > "the vast majority of GFP-expressing interneurons was CCK+/CB1+ basket cell (71.1 %, n = 38 recorded green neurons) as these interneurons had axon terminals immunoreactive for CB1"
  > — Vereczki et al. 2021, CCK+/CB1+ basket cells · [2] <!-- quote_key: 232283078_6d9c6756 -->

- **NT type.** NT type is CONSISTENT: the classical type is GABAergic and CLUS_0664 is classified GABA in the atlas. *(atlas-internal)*

- **Location.** Soma location is CONSISTENT: MBA:295 (basolateral amygdaloid area) is recorded as present for CLUS_0664 at region_fraction 0.031. *(note: region_fraction 0.031 is low — the cluster is distributed across multiple regions — but BLA-presence is confirmed and supports the anatomical assignment at this confidence tier.)*

**Marker evidence provenance:**

- **Cck:** Evidence is consistent across sources [1], [2], [3], and the primate homologue study [4]. The Vereczki et al. 2021 evidence item provides the highest specificity: CCK-GFP mice allowed targeted identification of CCK+ interneurons confirmed by post-hoc CB1 immunoreactivity on axon terminals, providing direct evidence that CCK basket cells are the numerically dominant CCK+ interneuron class in BLA [2]. The Totty et al. 2024 data are from primate; *(note: cross-species differences are possible, but the study explicitly proposes homology with mouse CCK basket cells based on Cnr1/CCK co-expression.)*
- **Calb1:** Listed as a defining marker based on McDonald et al. 2012 [1] and Woodruff & Sah 2007 [3]. However, no precomputed Calb1 expression comparison is available for CS20230722_CLUS_0664 in the current atlas build, so this co-expression criterion cannot be assessed. This is a material gap: Calb1 co-expression is one of the features used classically to distinguish CCK basket cells from the CCK+/CR+ small bipolar subclass [1].

  **Atlas annotation/expression gap (Calb1):** Calb1 is listed as a defining marker on this classical node but no precomputed expression comparison is present in the facts file for CS20230722_CLUS_0664. Calb1 atlas-level coverage should be verified once precomputed expression data are available; absence would weaken the rationale for distinguishing this node from `bla_cck_cb1_basket_cell`.

- **Pvalb (negative):** Pvalb negativity is listed as a defining negative marker based on Vereczki et al. 2021 [2]. No precomputed Pvalb comparison is available for CLUS_0664, but the Sncg lineage is circumstantially consistent with Pvalb-negativity — Sncg-lineage clusters are not classified as Pvalb-expressing in WMBv1 atlas metadata. This is indirect evidence only; direct confirmation would require precomputed Pvalb expression to be compared.

**Concerns:**

- **No annotation-transfer evidence.** The mapping rests entirely on atlas metadata and a single literature item. Annotation-transfer evidence (e.g. MapMyCells applied to BLA CCK basket cell transcriptomes) has not been run. This is the primary ceiling on confidence.
- **1:N cardinality — five sibling clusters.** Five Sncg Gaba_1 clusters at rank 0 all score equally on Cnr1+Cck. CS20230722_CLUS_0664 is not distinguished from its siblings on current metadata; the closest BLA-enriched sibling is unknown. *(caveat: DISTRIBUTED_ACROSS_CLUSTERS)*
- **Calb1 not assessed.** Calb1 is a defining marker of this classical type but no atlas-side comparison is available. If Calb1 is absent or low in CLUS_0664 this would weaken the closeMatch rationale relative to `bla_cck_cb1_basket_cell`, which does not require Calb1.
- **Overlap with `bla_cck_cb1_basket_cell`.** Both nodes currently map to CS20230722_CLUS_0664. This either indicates that the two classical nodes represent the same population (Calb1 being a partial marker of CCK/CB1 basket cells rather than a distinguishing criterion) or that the 1:N cardinality hides a child cluster more specific to each. This ambiguity is not resolved by available evidence.
- **region_fraction 0.031 is low** but does not disqualify — BLA-presence is confirmed at MBA:295; this is within the boundary band for a BLA-specific interneuron type represented by a scattered atlas cluster.

**What would upgrade confidence:**

- **MapMyCells annotation transfer** on BLA CCK basket cell single-cell transcriptomes (or CCK-GFP FACS-sorted BLA neurons) mapped to CCN20230722 at rank 0. Target: F1 ≥ 0.60 at CLUSTER level to distinguish the best Sncg Gaba_1 sibling and provide an `AnnotationTransferEvidence` item. Resolves the 1:N cardinality and the primary low-evidence ceiling.
- **Precomputed Calb1 expression for CCN20230722.** Adding Calb1 to the atlas expression build would allow a direct CONSISTENT/DISCORDANT comparison for the defining marker that is currently NOT_ASSESSED. Resolves the Calb1 gap and would sharpen the distinction from `bla_cck_cb1_basket_cell`.
- **Curator review of `bla_cck_basket_cell` vs `bla_cck_cb1_basket_cell` node identity.** If the two nodes are judged to represent the same classical population, they should be merged or one deprecated, with the mapping attributed to the retained node.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The `bla_cck_basket_cell` node is defined on a CLASSICAL basis: neurochemical and anatomical criteria from targeted studies in mouse and rat BLA. Defining markers: Cck ([1], [3], [2], [4]) and Calb1 ([1], [3], [2]). Neuropeptide: Cck ([1], [2]). Negative marker: Pvalb ([2]). Neurotransmitter: GABAergic ([1], [2]). Soma location: basolateral amygdaloid area [UBERON:0002887] ([1], [2]).

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_cck_basket_cell_to_cs20230722_clus_0664 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [2]; atlas-internal |

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:47+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala cholecystokinin basket cell → 0664 Sncg Gaba_1 [CS20230722_CLUS_0664] at LOW confidence. Key support: precomputed atlas expression showing Cck mean 11.15 (98.3rd pct) and Cnr1 mean 12.36 (98.5th pct) in the BLA GABAergic cohort; Vereczki et al. 2021 quantification that 71.1% of BLA CCK+ interneurons are CCK+/CB1+ basket cells. Key caveats: no annotation-transfer evidence; five sibling Sncg Gaba_1 clusters are indistinguishable on available data (DISTRIBUTED_ACROSS_CLUSTERS); Calb1 expression not assessable from current atlas build.

The Cell Ontology has no specific term for this population; basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**Experiment 1 — Annotation transfer (MapMyCells)**
- **What:** MapMyCells applied to BLA CCK basket cell single-cell transcriptomes (or CCK-GFP FACS-sorted BLA neurons) against CCN20230722 at rank 0.
- **Target:** F1 ≥ 0.60 at CLUSTER level, to identify the best-matching Sncg Gaba_1 sibling and resolve the 1:N cardinality.
- **Expected output:** `AnnotationTransferEvidence` item on the edge; upgrade to MODERATE confidence if F1 threshold is met and no major marker contradiction arises.
- **Resolves:** 1:N cardinality; Open questions 1 and 2.

**Experiment 2 — Precomputed Calb1 expression for CCN20230722**
- **What:** Add Calb1 to the atlas precomputed expression build (`just add-expression`) to populate a direct Calb1 comparison for CLUS_0664 and its Sncg siblings.
- **Target:** Calb1 expression comparison graded CONSISTENT or DISCORDANT for CLUS_0664 vs sibling clusters.
- **Expected output:** Updated `property_comparisons[marker_Calb1]` entry; enables distinction of `bla_cck_basket_cell` from `bla_cck_cb1_basket_cell` at the atlas level.
- **Resolves:** Calb1 NOT_ASSESSED gap; Open question 3.

**Experiment 3 — Curator review of `bla_cck_basket_cell` vs `bla_cck_cb1_basket_cell`**
- **What:** Compare the two classical nodes for marker overlap. Both currently map to CS20230722_CLUS_0664. Determine whether Calb1 co-expression and Pvalb negativity (the distinguishing criteria on `bla_cck_basket_cell`) are sufficient to warrant a separate atlas mapping, or whether the two nodes represent the same population described from different experimental angles.
- **Expected output:** Either a curator decision to merge the two nodes (retaining the node with the more complete marker panel), or a literature evidence item that distinguishes CCK/Calb1 basket cells from CCK/CB1 basket cells in the BLA.
- **Resolves:** Open question 3; note on both nodes in the KB.

### Open questions

1. Which of the five sibling Sncg Gaba_1 clusters (rank 0) in CCN20230722 is most enriched for cells from the basolateral amygdaloid area [UBERON:0002887]? All five are indistinguishable on Cck+Cnr1 expression alone.
2. Does an annotation-transfer experiment on BLA CCK basket cell transcriptomes resolve the 1:N cardinality toward CS20230722_CLUS_0664 specifically, or does the AT signal distribute across multiple Sncg Gaba_1 siblings?
3. Do `bla_cck_basket_cell` and `bla_cck_cb1_basket_cell` represent overlapping populations? Both nodes map to CS20230722_CLUS_0664; Calb1 expression is the key unassessed discriminant. Curator review of node distinctiveness and potential merger is recommended.

---

## References

| Label | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 | [PMID:22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | soma location; NT type; Cck and Calb1 markers; Cck neuropeptide |
| [2] | Vereczki et al. 2021 | [PMID:33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | soma location; NT type; Cck and Calb1 markers; Cck neuropeptide; CCK basket cell fraction estimate; Pvalb negative marker |
| [3] | Woodruff & Sah 2007 | [PMID:17234587](https://pubmed.ncbi.nlm.nih.gov/17234587/) | Cck and Calb1 markers |
| [4] | Totty et al. 2024 | [PMID:39463931](https://pubmed.ncbi.nlm.nih.gov/39463931/) | Cck marker (primate snRNA-seq cross-species homologue) |

---

<!-- verdict-block-start: edge_bla_cck_basket_cell_to_cs20230722_clus_0664 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    CS20230722_CLUS_0664 (0664 Sncg Gaba_1) carries Cck mean 11.15
    (98.3rd pct) and Cnr1 mean 12.36 (98.5th pct) in the BLA GABAergic
    rank-0 cohort — both tier-2 reliable from EXPRESSION source. Vereczki
    et al. 2021 (PMID:33837051) confirms 71.1% of BLA CCK+ interneurons
    are CCK+/CB1+ basket cells; NT type CONSISTENT (GABAergic/GABA);
    location_soma CONSISTENT (MBA:295, region_fraction=0.031). Confidence
    is LOW: no annotation-transfer evidence; Calb1 (a defining marker)
    is NOT_ASSESSED; five sibling Sncg Gaba_1 clusters are
    indistinguishable on available data (DISTRIBUTED_ACROSS_CLUSTERS
    caveat). Overlap with bla_cck_cb1_basket_cell (same target cluster)
    requires curator review.
  reconciliation_note: >
    Both bla_cck_basket_cell and bla_cck_cb1_basket_cell map to
    CS20230722_CLUS_0664; Calb1 (defining marker on bla_cck_basket_cell)
    is NOT_ASSESSED in the current atlas build. Curator review of node
    distinctiveness recommended before upgrading confidence.
  unresolved_questions:
    - "Which Sncg Gaba_1 sibling cluster is the most BLA-enriched once AT evidence is available?"
    - "Do bla_cck_basket_cell and bla_cck_cb1_basket_cell represent overlapping populations that should be merged?"
```
<!-- verdict-block-end -->
