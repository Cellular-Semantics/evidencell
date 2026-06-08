# Basolateral amygdala parvalbumin basket cell — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) parvalbumin (PV) basket cell is one of the dominant
GABAergic interneuron classes in the BLA, constituting 17–20% of all inhibitory neurons
in the lateral and basal amygdaloid nuclei [2]. Like their counterparts in neocortex and
hippocampus, these cells are defined by strong Pvalb expression and provide perisomatic
inhibition onto principal neuron somata — a connectivity pattern conserved across
cortical-like regions [1]. Establishing the transcriptomic identity of BLA PV basket
cells in the Allen Brain Cell Atlas (CCN20230722) matters both for linking classical
inhibitory circuit physiology with single-cell genomic data and for interpreting
fear-memory and anxiety circuit studies that target PV+ perisomatic populations.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1], [2] |
| NT type | GABAergic | [1], [2] |
| Defining marker | Pvalb | [1], [3], [4], [5], [6] |
| Negative markers | Sst | — |
| Neuropeptides | — | — |
| CL mapping | basket cell [CL:0000118] (BROAD) | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / NT type / Pvalb / population description:** LITERATURE evidence · McDonald et al. 2012 [1]

  > The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982)(McDonald, 1985)(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003(Millhouse et al., 1983)(Fuller et al., 1987)(Carlsen et al., 1988)(McDonald et al., 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;
  > — McDonald et al. 2012, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 11544073_ea8d2bb3 -->

- **Soma location / NT type / Pvalb / proportion:** LITERATURE evidence · Vereczki et al. 2021 [2]

  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [2] <!-- quote_key: 232283078_d4238834 -->

- **Pvalb (defining marker):** LITERATURE evidence · Woodruff & Sah 2007 [3]

  > Four populations of interneurons have been described in the BLA: those expressing parvalbumin (McDonald, 1992;Mc-Donald and Betette, 2001), those expressing somatostatin (Mc-Donald and Mascagni, 2002), those expressing cholecystokinin
  > — Woodruff & Sah 2007, Basolateral amygdala neuronal subtypes · [3] <!-- quote_key: 161407_eb8bfaf0 -->

- **Pvalb (defining marker, BLA–cortex parallels):** LITERATURE evidence · Ünal et al. 2020 [4]

  > The most salient parallels between BLA and other cortical regions with respect to their interneurons exist with respect to parvalbumin (PV) and somatostatin (SOM) positive interneurons.
  > — Ünal et al. 2020, Basolateral amygdala neuronal subtypes · [4] <!-- quote_key: 212579559_d2c2762c -->

- **Pvalb (defining marker, cross-species validation):** LITERATURE evidence · Totty et al. 2024 [6]

  > We identified 18 different types of inhibitory neurons in the primate amygdala (Fig. 3A) with representation of all major interneuron classes (SST, PVALB, VIP, CCK, and LAMP5).
  > — Totty et al. 2024, GABAergic neuron types in the primate am · [6] <!-- quote_key: 273531817_5ef8d3f9 -->

- **Sst (negative marker):** The Sst negative marker follows from the classical literature distinguishing non-overlapping Pvalb+ and Sst+ BLA interneuron populations [1], [3], [4]. No specific quote in the current evidence base directly tests Sst expression in Pvalb+ BLA cells; the negative-marker status is inferred from the established non-overlap of these two populations in cortical-like structures including the BLA.

</details>

### Cell Ontology mapping

Cell Ontology mapping: basket cell [[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)] (BROAD).

The BROAD mapping indicates that CL:0000118 ("basket cell") is a broader ancestor term covering multiple basket cell subtypes across brain regions; no term specifically covering BLA parvalbumin basket cells currently exists in the Cell Ontology. Auto-proposed by asta-report-ingest; requires expert review. This type is a candidate for CL contribution.

---

## Results

One candidate atlas cluster was assessed; 0738 Pvalb Gaba_2 [CS20230722_CLUS_0738] is
the primary mapping at LOW confidence. The mapping is supported by strong Pvalb
precomputed expression (mean 10.86, 99.8th percentile in the BLA GABAergic survival
cohort) and the highest BLA region_fraction among Pvalb clusters (0.178), but is
limited by the absence of annotation-transfer evidence and by 1:n cardinality: the
basket cell population may extend across additional Pvalb clusters in this taxonomy.

### 4a. Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0738 Pvalb Gaba_2 [CS20230722_CLUS_0738] | 0206 Pvalb Gaba_2 | 425 | 🔴 LOW | Pvalb CONSISTENT · location CONSISTENT | broadMatch (1:n) |

*1 edge assessed (skos:broadMatch, 1:n cardinality).*

### 4b. Property alignment table — 0738 Pvalb Gaba_2 [CS20230722_CLUS_0738]

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 BLA present; region_fraction 0.178 — highest among Pvalb clusters in BLA GABAergic cohort | CONSISTENT |
| Pvalb expression | Pvalb — defining marker | not available | Pvalb precomputed mean 10.86 (99.8th pct; tier 2). Cluster "0738 Pvalb Gaba_2" — non-chandelier Pvalb type | CONSISTENT |
| Basket cell label | perisomatic basket cell — soma-targeting | not available | Cluster "0738 Pvalb Gaba_2" — no explicit basket label; selected over CS20230722_CLUS_0733 (chandelier) for basket cell identity | APPROXIMATE |
| Sst expression | Sst — negative marker | not available | NOT_ASSESSED | NOT_ASSESSED |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki et al. 2021: PV+ basket cell proportion in BLA | Literature | SUPPORT | PV+ basket cells 17–20% of BLA GABAergic cells | [2] |
| Atlas precomputed expression + region fraction | Atlas metadata | SUPPORT | Pvalb mean 10.86 (99.8th pct); region_fraction 0.178 — highest BLA Pvalb cluster | atlas-internal |

**Supporting evidence**

- **Literature — cell-counting study (LA/BA):** Vereczki et al. 2021 established PV+
  basket cells as the single largest perisomatic interneuron class in the lateral and
  basal amygdala at 17–20% of GABAergic cells, and confirmed the BLA contains the
  same major GABAergic neuron types as other cortical regions [2]:

  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [2] <!-- quote_key: 232283078_d4238834 -->

- **Atlas metadata — precomputed expression and region fraction:** CS20230722_CLUS_0738
  "0738 Pvalb Gaba_2" shows Pvalb precomputed mean 10.86 at the 99.8th percentile in
  the BLA GABAergic survival cohort (cohort size 5, rank 0). The region_fraction for
  MBA:295 (Basolateral amygdalar nucleus) is 0.178 — the highest among Pvalb clusters
  in the BLA GABAergic cohort. This cluster was selected over CS20230722_CLUS_0733
  ("Pvalb chandelier Gaba_1") for basket cell identity based on the absence of a
  chandelier designation (atlas-internal evidence).

- **Discovery score context:** Stage A ranked CS20230722_CLUS_0738 at rank 3 in a
  5-member BLA GABAergic survival cohort (score 3, next_best_score 3 — cohort is tied).
  Pvalb contributed applied_score 2.0 from cohort-pct 0.998 of 5 members. The tied
  score reflects the small cohort at rank 0; the region_fraction (0.178, highest BLA
  Pvalb fraction) provides the biologically informative discriminant over the cohort
  score.

**Marker evidence provenance**

- **Pvalb (defining marker):** Multiple convergent literature sources support Pvalb as
  the defining marker [1], [3], [4], [5], [6]. McDonald et al. 2012 [1] reports the
  PV+/CB+ neuronal subpopulation in the CBL on the basis of dual-labelling studies.
  Woodruff & Sah 2007 [3] lists Pvalb+ interneurons as one of four established BLA
  interneuron populations. Ünal et al. 2020 [4] draws an explicit parallel between
  BLA and neocortical Pvalb+ populations. Hochgerner et al. 2023 [5] identified a
  Pvalb-type GABA neuron class in a mouse amygdala single-cell taxonomy. Totty et al.
  2024 [6] confirmed PVALB as a conserved interneuron class in the primate amygdala.
  Atlas-side: Pvalb precomputed mean 10.86 (99.8th pct) is consistent with defining
  marker status. No discrepancy between literature expectation and atlas expression.

- **Sst (negative marker):** The Sst negative-marker designation is inferred from the
  classical literature establishing non-overlapping Pvalb+ and Sst+ BLA interneuron
  populations [1], [3], [4]. No primary citation in the current evidence base tests
  Sst expression directly in identified Pvalb+ BLA cells. Atlas-side Sst expression
  for CS20230722_CLUS_0738 was not evaluated (NOT_ASSESSED): precomputed stats for
  Sst in this cluster are not recorded in the current facts extraction. A targeted
  literature search for "Pvalb Sst co-expression BLA amygdala" would clarify whether
  this negative-marker designation has direct experimental support or is strictly
  inferred from population non-overlap.

  *(note: In neocortex and hippocampus, Pvalb+ and Sst+ interneurons are well-established
  as largely non-overlapping populations. Extension of this rule to the BLA is
  biologically reasonable but has not been confirmed at single-cell resolution for
  this atlas taxonomy.)*

- **Basket cell label (APPROXIMATE alignment):** CS20230722_CLUS_0738 carries the
  label "Pvalb Gaba_2" with no explicit "basket" designation. The basket-cell
  identity assignment is based on exclusion: the co-occurring Pvalb cluster
  CS20230722_CLUS_0733 carries an explicit "chandelier" label, making CLUS_0738 the
  residual non-chandelier Pvalb cluster. This indirect label-based assignment is
  appropriate but not confirmed by functional connectivity or cell-targeting data
  at the cluster level.

**Concerns**

- **No AT evidence (AT_ABSENT):** No annotation-transfer evidence exists for this
  mapping. Per the confidence rubric, a broadMatch edge without AT evidence is
  capped at LOW confidence.
- **1:n cardinality — basket cells may be distributed:** The 1:n cardinality (multiple
  Pvalb Gaba_2 clusters may contain basket cells) means this mapping covers only the
  highest-BLA-fraction Pvalb cluster; the full basket-cell transcriptomic population
  may extend to sibling clusters. The discovery cohort at rank 0 contained 5 BLA
  GABAergic clusters; additional Pvalb clusters beyond CLUS_0738 have not been
  individually assessed for basket-cell identity.
- **Basket vs axo-axonic identity not confirmable from atlas labels alone:** The
  APPROXIMATE alignment on the basket-cell label property reflects that the WMBv1
  taxonomy does not provide a basket-specific designation for CLUS_0738 — the
  assignment relies on exclusion of the chandelier-labelled CLUS_0733. Transcriptomic
  profiles alone cannot confirm soma-targeting vs AIS-targeting within a Pvalb cluster.
- **Sst negative marker NOT_ASSESSED:** Atlas-side Sst expression for CLUS_0738 has
  not been evaluated. If Sst is expressed at detectable levels in this cluster, the
  negative-marker designation for the classical type would be in conflict.

**What would upgrade confidence**

- **Annotation transfer (AnnotationTransferEvidence):** Run MapMyCells on transcriptomes
  from BLA PV basket cells (e.g. labelled by Cre-line targeting in an amygdala
  single-cell dataset) against CCN20230722 at cluster level. F1 ≥ 0.60 at CLUSTER
  level for CS20230722_CLUS_0738 would support upgrade toward MODERATE; F1 ≥ 0.80
  with Pvalb marker confirmation would support HIGH confidence. Would also confirm
  or refute the 1:n call by revealing whether a single cluster accounts for the
  basket-cell population. Resolves open question 1 and AT_ABSENT caveat.
- **AnkG co-staining in mouse BLA (AnkG labelling + in-situ marker evidence):**
  Co-stain for ankryin-G (AIS marker) and soma-proximal basket terminal markers in
  mouse BLA to distinguish AIS-targeting CLUS_0733 cells from soma-targeting CLUS_0738
  cells at the tissue level. Would provide direct LiteratureEvidence resolving basket
  vs axo-axonic identity for both clusters. Resolves open question 1 and the
  APPROXIMATE basket-label alignment.
- **Sst expression check for CLUS_0738 (targeted atlas query or precomputed stats):**
  Retrieve Sst precomputed mean for CS20230722_CLUS_0738 from the taxonomy reference
  store or HDF5 stats to evaluate the Sst negative marker. Near-zero Sst would
  strengthen the mapping; detectable Sst would flag a negative-marker conflict.
  Resolves open question 2.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The basolateral amygdala parvalbumin basket cell
(`bla_pv_basket_cell`) is defined on a CLASSICAL basis: GABAergic NT type, Pvalb
as defining marker, Sst as negative marker, soma location in the basolateral amygdala
[UBERON:0002887]. The type constitutes 17–20% of GABAergic cells in the mouse lateral
and basal amygdala per cell-counting studies [2]. Pvalb expression has been documented
across rodent and primate amygdala [1], [3], [4], [5], [6]. The node notes that the
PV+/CB+ population in the BLA includes both basket cells and axo-axonic (chandelier)
cells, forming one of two parallel perisomatic inhibitory networks alongside CCK basket
cells. The classical literature establishes Pvalb+ and Sst+ populations as non-overlapping,
supporting Sst as a negative marker for this type [1], [3], [4].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722
taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based
scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring
rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the
corresponding atlas-side value via the `property_comparisons` schema, with alignments
graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values
came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference
store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim
literature quotes in this report are validated against the evidencell knowledge base at
write time. Authored-prose evidence narratives are validated against their source
`evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable
identifier or unattributed blockquote. Specific mapping limitations and caveats are
documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_pv_basket_cell_to_cs20230722_clus_0738 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [2], atlas-internal |

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:46+00:00 from
[kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Basolateral amygdala parvalbumin basket cell → 0738 Pvalb Gaba_2
[CS20230722_CLUS_0738] at LOW confidence with skos:broadMatch (1:n). Key support:
Pvalb precomputed mean 10.86 (99.8th pct in BLA GABAergic cohort) and region_fraction
0.178 (highest BLA fraction among Pvalb clusters in CCN20230722); NT type CONSISTENT.
Key caveats: (1) no annotation-transfer evidence (AT_ABSENT — confidence ceiling LOW
for broadMatch without AT); (2) basket vs axo-axonic identity is not confirmable from
atlas cluster labels alone; (3) 1:n cardinality indicates the basket-cell population
may be distributed across multiple Pvalb Gaba_2 clusters.

The Cell Ontology has no specific term for BLA parvalbumin basket cells; basket cell
[[CL:0000118](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000118)]
is the closest BROAD ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**1. Annotation transfer (AnnotationTransferEvidence)**

- **What:** Run annotation transfer (e.g. MapMyCells) on transcriptomes from
  BLA-labelled Pvalb+ cells against CCN20230722 at cluster and supertype levels,
  using a source dataset with labelled basket cell populations (e.g. Cre-driver
  targeting of Pvalb+ perisomatic interneurons in an amygdala single-cell dataset,
  or the Hochgerner et al. 2023 [5] taxonomy as source).
- **Target:** F1 ≥ 0.60 at CLUSTER level for CS20230722_CLUS_0738 as threshold for
  MODERATE confidence upgrade; F1 ≥ 0.80 with Pvalb CONSISTENT would approach HIGH.
- **Expected output:** AnnotationTransferEvidence on
  `edge_bla_pv_basket_cell_to_cs20230722_clus_0738`; clarifies whether 1:n
  broadMatch can be collapsed to a single best cluster.
- **Resolves:** open question 1; AT_ABSENT caveat; 1:n cardinality question.

**2. AnkG co-staining in mouse BLA (in situ cell-type discrimination)**

- **What:** Co-stain for ankryin-G (marks AIS) alongside perisomatic basket terminal
  markers in mouse BLA to distinguish soma-targeting CLUS_0738 cells from AIS-targeting
  CLUS_0733 cells at the tissue level.
- **Target:** >80% soma-targeting rate for CLUS_0738 cells in MBA:295.
- **Expected output:** LiteratureEvidence distinguishing CLUS_0738 (basket) from
  CLUS_0733 (chandelier) in BLA tissue; upgrades basket-label alignment from
  APPROXIMATE to CONSISTENT.
- **Resolves:** open question 1; APPROXIMATE alignment on atlas_label_basket.

**3. Sst expression check for CLUS_0738**

- **What:** Retrieve Sst precomputed mean for CS20230722_CLUS_0738 from the CCN20230722
  taxonomy reference store (cluster.yaml or HDF5) to evaluate the Sst negative marker.
- **Target:** Sst precomputed mean < 0.5 (near-zero) for CONSISTENT negative-marker
  alignment; Sst ≥ 0.5 flags a conflict.
- **Expected output:** Updated `negative_marker_Sst` property comparison from
  NOT_ASSESSED to CONSISTENT or DISCORDANT.
- **Resolves:** open question 2; strengthens or undermines the negative-marker
  evidence chain.

**4. Targeted literature search for Sst negative-marker confirmation**

- **What:** Cite-traverse for "parvalbumin somatostatin co-expression basolateral
  amygdala" to determine whether the Sst negative-marker designation for BLA PV
  basket cells has direct experimental support.
- **Target:** A primary citation confirming Sst absence in identified BLA Pvalb+ cells,
  or establishing the non-overlap at single-cell resolution.
- **Expected output:** LiteratureEvidence item supporting `negative_markers: [Sst]`.
- **Resolves:** open question 2; Sst negative-marker provenance gap.

### Open questions

1. Does CS20230722_CLUS_0738 contain predominantly basket cells vs axo-axonic
   cells in BLA, or is there a mixed population? AnkG co-staining in mouse BLA is
   needed to confirm AIS-targeting (CLUS_0733) vs soma-targeting (CLUS_0738) cell
   identity at the tissue level.
2. Does the Sst negative-marker designation for BLA PV basket cells have direct
   experimental support, or is it inferred solely from population-level non-overlap
   of Pvalb+ and Sst+ populations? Sst precomputed expression for CLUS_0738 is
   NOT_ASSESSED and should be retrieved.
3. Do additional Pvalb clusters in CCN20230722 (beyond CLUS_0738) contribute to the
   basket-cell population in BLA? The 1:n cardinality notation reflects this
   possibility; AT evidence could resolve whether a single cluster captures the
   basket-cell population or whether the 1:n call is warranted.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | Soma location, NT type, Pvalb marker |
| [2] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | Soma location, NT type, cell-type proportion |
| [3] | Woodruff & Sah 2007 | [17234587](https://pubmed.ncbi.nlm.nih.gov/17234587/) | Pvalb marker |
| [4] | Ünal et al. 2020 | [32144495](https://pubmed.ncbi.nlm.nih.gov/32144495/) | Pvalb marker, BLA–cortex parallels |
| [5] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Pvalb marker, amygdala single-cell taxonomy |
| [6] | Totty et al. 2024 | [39463931](https://pubmed.ncbi.nlm.nih.gov/39463931/) | Pvalb marker, cross-species validation |

---

<!-- verdict-block-start: edge_bla_pv_basket_cell_to_cs20230722_clus_0738 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    CS20230722_CLUS_0738 ("0738 Pvalb Gaba_2") is the highest-BLA-fraction Pvalb cluster
    in the CCN20230722 BLA GABAergic survival cohort: region_fraction=0.178 (highest among
    Pvalb clusters) and Pvalb precomputed mean 10.86 at cohort-pct 0.998 of 5-member cohort
    (applied_score 2.0; source: EXPRESSION). NT type CONSISTENT (GABAergic/GABA).
    ATLAS_METADATA SUPPORT: cluster label "Pvalb Gaba_2" with no chandelier designation —
    selected over CS20230722_CLUS_0733 (chandelier) for basket cell identity. LITERATURE
    SUPPORT: Vereczki et al. 2021 (PMID:33837051) establishes PV+ basket cells as 17–20%
    of BLA GABAergic cells. Atlas_label_basket APPROXIMATE: no explicit basket label; identity
    by chandelier-exclusion only. Sst negative_marker NOT_ASSESSED. AT_ABSENT: no
    annotation-transfer evidence; 1:n cardinality (basket population may distribute across
    multiple Pvalb Gaba_2 clusters). Confidence capped at LOW per broadMatch + AT_ABSENT rubric.
  reconciliation_note: >
    No pool candidates identified. Predicate skos:broadMatch with 1:n cardinality reflects
    that the basket-cell population likely spans multiple Pvalb clusters in CCN20230722;
    CLUS_0738 is the best single-cluster proxy by region_fraction but the 1:1 resolution
    requires AT evidence.
  lit_to_lit_edges: []
  unresolved_questions:
    - "Does CS20230722_CLUS_0738 contain predominantly basket cells vs axo-axonic cells in BLA? AnkG co-staining needed to confirm soma-targeting (CLUS_0738) vs AIS-targeting (CLUS_0733) identity in tissue."
    - "Sst precomputed mean for CS20230722_CLUS_0738 is NOT_ASSESSED — retrieve from taxonomy reference store to evaluate negative-marker alignment."
    - "Do additional Pvalb clusters in CCN20230722 contribute to the basket-cell population in BLA? AT evidence needed to resolve the 1:n cardinality call."
```
<!-- verdict-block-end -->
