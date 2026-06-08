# Central amygdala protein kinase C-delta (PKC-delta) neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala protein kinase C-delta (PKC-delta) neuron is a well-characterised GABAergic cell class of the lateral subdivision of the central amygdala (CeL). First molecularly defined by Haubensak et al. 2010, PKC-delta+ (Prkcd+) neurons constitute the CeL-OFF population — units inhibited by a conditioned stimulus — and are reciprocally connected with the functionally opposing PKC-delta− population. Together with somatostatin-expressing (Sst+) neurons, they account for the majority of CeL neurons. Mapping this cell type to a transcriptomic atlas cluster is a prerequisite for integrating circuit-level findings with single-cell genomics and for cross-species alignment of amygdala cell-type classifications.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdala [UBERON:0002883], lateral subdivision (CeL) | [1] [2] [3] |
| Neurotransmitter | GABAergic | [2] [4] |
| Defining markers | Prkcd (protein kinase C-delta; protein and transcript) | [1] [2] [3] [5] [6] |
| Negative markers | Sst (somatostatin) | [2] |
| Neuropeptides | None recorded | — |
| Definition basis | CLASSICAL | — |
| Notes | Largely non-overlapping with Sst+ CeL neurons; together with Sst+ cells these account for most CeL neurons | [1] |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** Slice electrophysiology and circuit tracing · mouse CeL · [1] [2] [3]
  > "The role of different amygdala nuclei (neuroanatomical subdivisions) in processing Pavlovian conditioned fear has been studied extensively, but the function of the heterogeneous neuronal subtypes within these nuclei remains poorly understood. Here we use molecular genetic approaches to map the functional connectivity of a subpopulation of GABA-containing neurons, located in the lateral subdivision of the central amygdala (CEl), which express protein kinase C-δ (PKC-δ)."
  > — Haubensak et al. 2010, Central amygdala cell types · [2] <!-- quote_key: 2270983_0fa016d1 -->

- **Neurotransmitter (GABAergic):** Molecular genetics and circuit tracing · mouse CeL · [2]; review article · [4]
  > "The central amygdala (CeA) plays a central role in physiological and behavioral responses to fearful stimuli, stressful stimuli, and drug-related stimuli. The CeA receives dense inputs from cortical regions, is the major output region of the amygdala, is primarily GABAergic (inhibitory), and expresses high levels of pro- and anti-stress peptides."
  > — Gilpin et al. 2014, Central amygdala cell types · [4] <!-- quote_key: 442779_deea5502 -->

- **Defining marker Prkcd:** Cre-driver in vivo silencing and morphological identification · mouse · [2]; CeA circuit anatomy · mouse · [1]; cross-species scRNA-seq · primate CeA · [3] [5] [6]
  > "Two genetically identified cell types, protein kinase Cdexpressing (PKCd⁺) neurons and somatostatin-expressing (Som⁺) neurons, constitute most CeLC neurons and are largely non-overlapping (Li et al., 2013;Kim et al., 2017;Wilson et al., 2019)."
  > — Adke et al. 2019, Central amygdala cell types · [1] <!-- quote_key: 209598438_053c1083 -->

  > "It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice."
  > — Yeh et al. 2024, Central amygdala cell types · [3] <!-- quote_key: 267685584_daaf5612 -->

  > "We also identified clusters corresponding to protein kinase C-δ⁺ (PKRCD⁺/SST⁻) interneurons in the central nucleus"
  > — Totty et al. 2024, GABAergic neuron types in the primate amygdala show distributed or subregion specific expression patterns · [5] <!-- quote_key: 273531817_722a2099 -->

- **Negative marker Sst:** Cre-driver molecular genetics · mouse CeL · [2]
  The Sst-negativity criterion is directly established by Haubensak et al. 2010: PKC-delta+ and Sst+ neurons are defined as mutually exclusive (see [2] quote above).

- **scRNA-seq context:** O'Leary et al. 2022 CeA scRNA-seq · mouse · [6]
  > "Prkcd and Sst each exhibited mixed expression across multiple scRNA-seq-clusters"
  > — O'Leary et al. 2022, Results · [6] <!-- quote_key: 253356112_39b8cae2 -->
  *(note: this observation from O'Leary et al. 2022 directly anticipates the Sst discordance concern raised for CLUS_1333 below.)*

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_1333 (CEA-BST Six3 Cyp26b1 Gaba_2) at LOW confidence. No annotation-transfer evidence is available for this node; confidence is capped accordingly. The primary finding is a strong Prkcd expression match offset by a DISCORDANT Sst signal that constitutes the key concern for this mapping.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_1333 (CEA-BST Six3 Cyp26b1 Gaba_2) | — | n/a | 🔴 LOW | Prkcd CONSISTENT · Sst DISCORDANT | PRIMARY — broadMatch with Sst caveat |

*Note: 1 edge assessed; relationship type skos:broadMatch. n_cells field is null — taxonomy DB predates PR #21 n_cells column; rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` to populate.*

---

### Property alignment table — CS20230722_CLUS_1333

**Table 1 — Property comparison**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA (cluster label suffix "_Gaba_2") | CONSISTENT |
| Soma location | Central amygdala [UBERON:0002883] | MBA:536 CeA; region_fraction 0.567 (MERFISH); cluster label "CEA-BST Six3 Cyp26b1 Gaba_2" directly confirms CeA identity | CONSISTENT |
| Prkcd expression | Defining marker (protein/transcript) | Precomputed mean_expression 7.44 (CeA GABAergic cohort 99.1th percentile); highest Prkcd among all CEA-BST candidates | CONSISTENT |
| Sst expression | Negative marker (PKC-delta neurons are Sst-negative) | Precomputed mean_expression 1.21 (CeA GABAergic cohort 57.5th percentile; ABOVE minimum-detectable threshold) | DISCORDANT |
| Sex ratio | Not documented on classical node | Not available at cluster level (n_cells null; MFR not computable) | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Haubensak 2010 CeL circuit | Literature | SUPPORT | PKC-delta+ neurons as CeL-OFF population; Prkcd + Sst-negativity canonical pair | [2] |
| Adke 2019 CeA circuit anatomy | Literature | SUPPORT | PKC-delta+ and Sst+ as major non-overlapping CeL classes | [1] |
| O'Leary 2022 CeA scRNA-seq | Literature | SUPPORT | CEA-BST Six3 Cyp26b1 family as dominant CeA transcriptomic family | [6] |
| WMBv1 atlas metadata (CLUS_1333) | Atlas metadata | SUPPORT | Prkcd mean 7.44 (99.1th pct CeA cohort); 56.7% CeA cells; CEA-BST Six3/Cyp26b1 lineage label | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### CS20230722_CLUS_1333 (CEA-BST Six3 Cyp26b1 Gaba_2) · 🔴 LOW

**Supporting evidence:**

- **Prkcd expression — strongest positive signal.** CLUS_1333 shows a precomputed mean Prkcd expression of 7.44, placing it at the 99.1th percentile of the CeA GABAergic cohort (n=20 clusters, region=MBA:536, nt_type=GABAergic). This is the highest Prkcd expression among all CEA-BST candidates examined, providing a strong positive marker anchor for this classical type. The Stage A discovery score awarded `applied_score: 2.0` for Prkcd (tier 2, EXPRESSION source).

- **Soma location — CONSISTENT.** The cluster label "CEA-BST Six3 Cyp26b1 Gaba_2" directly names central amygdala as the primary region. MERFISH spatial registration places 56.7% of cells in MBA:536 (CeA). Region_fraction 0.567 sits in the boundary band (0.3–0.7); it drove the broadMatch relationship choice (not exactMatch) given the BST minority fraction.

- **NT type — CONSISTENT.** The cluster label suffix "_Gaba_2" and the atlas NT annotation both designate GABA; the classical type is GABAergic.

- **Literature support — CeA PKC-delta circuit.** Haubensak et al. 2010 [2] established the PKC-delta+ CeL neuron as a defined circuit element using Cre-driver-based in vivo silencing and channelrhodopsin-assisted circuit mapping:

  > "The role of different amygdala nuclei (neuroanatomical subdivisions) in processing Pavlovian conditioned fear has been studied extensively, but the function of the heterogeneous neuronal subtypes within these nuclei remains poorly understood. Here we use molecular genetic approaches to map the functional connectivity of a subpopulation of GABA-containing neurons, located in the lateral subdivision of the central amygdala (CEl), which express protein kinase C-δ (PKC-δ). Channelrhodopsin-2-assisted circuit mapping in amygdala slices and cell-specific viral tracing indicate that PKC-δ+ neurons inhibit output neurons in the medial central amygdala (CEm), and also make reciprocal inhibitory synapses with PKC-δ− neurons in CEl."
  > — Haubensak et al. 2010, Central amygdala cell types · [2] <!-- quote_key: 2270983_0fa016d1 -->

- **Literature support — CeL cellular composition.** Adke et al. 2019 [1] confirm the major non-overlapping CeL cell classes:

  > "Two genetically identified cell types, protein kinase Cdexpressing (PKCd⁺) neurons and somatostatin-expressing (Som⁺) neurons, constitute most CeLC neurons and are largely non-overlapping (Li et al., 2013;Kim et al., 2017;Wilson et al., 2019)."
  > — Adke et al. 2019, Central amygdala cell types · [1] <!-- quote_key: 209598438_053c1083 -->

- **Literature support — CEA-BST Six3 Cyp26b1 lineage.** O'Leary et al. 2022 [6] identified the CEA-BST Six3 Cyp26b1 cluster family as the dominant CeA transcriptomic family in mouse scRNA-seq, consistent with the PKC-delta neuron lineage. Notably, O'Leary et al. also documented that Prkcd and Sst show mixed expression across multiple scRNA-seq clusters:

  > "Prkcd and Sst each exhibited mixed expression across multiple scRNA-seq-clusters"
  > — O'Leary et al. 2022, Results · [6] <!-- quote_key: 253356112_39b8cae2 -->

**Marker evidence provenance:**

- **Prkcd:** Evidence is protein-level (PKC-delta immunostaining) and transcript-level (scRNA-seq, ISH) and spans multiple studies [1][2][3][5][6]. Haubensak et al. 2010 [2] confirmed cell identity via Cre-driver targeting (PKC-delta-Cre) with circuit-level physiological validation (CeL-OFF units), providing the highest-confidence cell-type specificity. Adke et al. 2019 [1] and Yeh et al. 2024 [3] used morphological and immunofluorescence methods in mouse and primate CeA, respectively. Totty et al. 2024 [5] explicitly identified Prkcd+/Sst− clusters in primate CeA scRNA-seq. Evidence provenance for Prkcd as a defining marker is strong across multiple independent studies and methods.

- **Sst (negative marker):** The Sst-negativity criterion is established primarily by Haubensak et al. 2010 [2] via Cre-driver genetic tools showing non-overlap of PKC-delta+ and Sst+ populations. This is a robust original study with clear genetic labelling. However, the quantitative threshold at the single-cell level (what fraction of PKC-delta+ neurons is Sst-negative, and at what expression level?) is not explicitly resolved in the gathered literature. The O'Leary et al. 2022 scRNA-seq finding [6] that "Prkcd and Sst each exhibited mixed expression across multiple scRNA-seq-clusters" directly anticipates the cluster-average discordance seen for CLUS_1333 and suggests the clean mutual exclusivity observed in Cre-driver studies may not hold uniformly at the transcriptome-wide, population-average level captured by atlas pseudobulk.

  ⚠ **Atlas annotation/expression discordance for Sst:** Sst is listed as a negative marker for this classical type (Prkcd+/Sst− canonical pair; PMID:21068836) but CLUS_1333 shows precomputed mean Sst expression = 1.21 (57.5th percentile in the CeA GABAergic cohort — above minimum-detectable threshold). The Stage A discovery scored this as a penalty (`raw_tier: -1`, `applied_score: -1.0`). This discordance is the primary concern for this edge and may reflect: (a) population-level averaging where a subset of CLUS_1333 cells co-expresses Sst; (b) a genuine overlap with Sst+ neurons that is resolved only at sub-cluster resolution; or (c) the "mixed expression across clusters" phenomenon documented by O'Leary et al. 2022. Individual-cell validation is required to resolve this.

**Concerns:**

- **DISCORDANT Sst — primary concern.** Sst mean_expression = 1.21 (57.5th percentile, CeA GABAergic cohort) is above the minimum-detectable threshold. The classical type is defined as Sst-negative by multiple genetic and immunohistochemical studies [2][5]. This is the most significant counter-evidence for this edge. The discordance may reflect cluster-level averaging over a mixed population (Prkcd+/Sst- and Sst+ cells co-binned), as suggested by the O'Leary et al. 2022 finding [6]. Nevertheless, until sub-cluster analysis resolves the cell-fraction breakdown, this remains a formal DISCORDANT alignment that constrains confidence to LOW.

- **DISTRIBUTED_ACROSS_CLUSTERS caveat.** Multiple CEA-BST Six3 Cyp26b1 clusters (CLUS_1331–1335 under one supertype; CLUS_1342–1343 under another) all have high Prkcd expression and CeA fractions of 0.37–0.65. The classical PKC-delta neuron type likely spans more than one Cyp26b1 Gaba cluster, implying 1:n cardinality. The broadMatch relationship reflects this; CLUS_1333 is the best single-cluster representative by Prkcd expression rank, but a complete mapping may require referencing the entire Cyp26b1 Gaba_2/4 family.

- **No annotation-transfer evidence.** No MapMyCells AT run has been completed for this node. Confidence is capped at LOW in the absence of AT evidence. The Sst discordance cannot be resolved by AT alone, but AT would provide an independent, cell-level transcriptomic anchor.

- **region_fraction 0.567 — boundary band.** The 56.7% CeA fraction drives the broadMatch (not exactMatch) relationship. A substantial BST minority fraction means the cluster is not exclusively CeA-localised, consistent with the CEA-BST naming of the lineage.

- **n_cells field null.** The taxonomy DB record for CLUS_1333 was generated before PR #21 added the n_cells column; the 10x cell count cannot be reported until the DB is rebuilt.

**What would upgrade confidence:**

- **Sub-cluster re-clustering (highest priority).** Re-cluster CLUS_1333 (and neighbouring Cyp26b1 clusters CLUS_1331–1335, CLUS_1342–1343) to identify a Prkcd-high/Sst-low subgroup. If a clean Prkcd+/Sst− sub-cluster emerges, replace the broadMatch to CLUS_1333 with a more specific edge to that sub-cluster. This directly resolves the DISCORDANT Sst alignment and could upgrade confidence to MODERATE. Expected output: revised MappingEdge with updated `node_b_id`.

- **RNAscope co-staining in mouse CeL.** Dual-fluorescence RNAscope for Prkcd and Sst in mouse CeL sections, quantifying the fraction of Prkcd+ cells that are Sst− and mapping those cells onto WMBv1 cluster boundaries. This would confirm or refute mutual exclusivity at the single-cell level and determine whether the CLUS_1333 Sst mean reflects a true subpopulation or population-averaging artefact. Expected output: LiteratureEvidence or MarkerAnalysisEvidence item on this edge.

- **MapMyCells annotation transfer.** Run MapMyCells on a CeA Prkcd-enriched dataset (e.g. from PKC-delta-Cre sorted neurons or a bulk RNA-seq dataset from a Cre-intersectional approach). F1 ≥ 0.70 at CLUSTER level against CLUS_1333 or a child cluster would support upgrading to MODERATE (absent major contradictions). Expected output: AnnotationTransferEvidence on this edge.

- **Targeted literature search.** A trawl for Sst heterogeneity within PKC-delta+ CeL neurons — specifically whether any publication has reported a Sst-expressing subpopulation of PKC-delta+ cells, or whether the O'Leary et al. 2022 "mixed expression" finding is replicated — could either document the heterogeneity (allowing the discordance to be acknowledged as a known biological feature and cited in the rationale without forcing demotion) or confirm true mutual exclusivity. Query: "Prkcd Sst co-expression central amygdala heterogeneity scRNA-seq".

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The CEA PKC-delta neuron (`cea_pkc_delta_neuron`) is defined on a CLASSICAL basis: defining markers include Prkcd [1][2][3][5][6]; NT type is GABAergic [2][4]; soma location is the central amygdala [UBERON:0002883], lateral subdivision [1][2][3]; negative marker is Sst [2]. The classical node carries no recorded neuropeptides, morphology, or electrophysiology fields.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match MBA:536, NT type GABAergic, defining markers Prkcd, negative marker Sst). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_pkc_delta_neuron_to_cs20230722_clus_1333 | LITERATURE; LITERATURE; LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT; SUPPORT; SUPPORT | [2]; [1]; [6]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:48+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Central amygdala protein kinase C-delta (PKC-delta) neuron → CS20230722_CLUS_1333 (CEA-BST Six3 Cyp26b1 Gaba_2) at LOW confidence. Key support: Prkcd precomputed mean_expression 7.44 at 99.1th percentile of the CeA GABAergic cohort (CONSISTENT); soma location CONSISTENT (56.7% CeA by MERFISH); cluster label directly names CEA; three independent literature sources converge on PKC-delta+ CeL neuron definition. Key caveats: Sst mean_expression = 1.21 (57.5th percentile, DISCORDANT with classical Sst-negativity criterion); classical type likely spans multiple Cyp26b1 Gaba clusters (1:n cardinality); no annotation-transfer evidence available.

No Cell Ontology term currently assigned. The PKC-delta+ CeL neuron is a candidate for CL contribution as a distinct amygdala GABAergic subtype.

### Proposed experiments and follow-ups

**1. Sub-cluster re-clustering of CLUS_1333 and neighbouring Cyp26b1 Gaba clusters**
- **What:** Unsupervised re-clustering of CEA-BST Six3 Cyp26b1 clusters (CLUS_1331–1335, CLUS_1342–1343) at higher resolution using the WMBv1 count matrix.
- **Target:** Identify a Prkcd-high/Sst-low subgroup with clean DISCORDANT-to-CONSISTENT transition for the Sst negative marker.
- **Expected output:** Revised MappingEdge with updated `node_b_id` to the resolved sub-cluster; Sst alignment upgraded from DISCORDANT.
- **Resolves:** Unresolved question 1 (Sst-negative subpopulation in CLUS_1333); caveat DISTRIBUTED_ACROSS_CLUSTERS; Sst DISCORDANT alignment.

**2. RNAscope dual-fluorescence (Prkcd + Sst) in mouse CeL**
- **What:** In situ hybridisation with dual probes for Prkcd and Sst in mouse CeL sections, with single-cell resolution.
- **Target:** Quantify the fraction of Prkcd+ cells that are Sst−; confirm or refute mutual exclusivity at the single-cell level.
- **Expected output:** LiteratureEvidence item on this edge documenting the quantified co-expression rate; if mutual exclusivity is confirmed, supports downgrading the Sst discordance to a population-averaging artefact in the KB rationale.
- **Resolves:** Unresolved question 1; the DISCORDANT Sst alignment.

**3. MapMyCells annotation transfer**
- **What:** Run MapMyCells (CCN20230722 target) on a CeA Prkcd-enriched dataset (PKC-delta-Cre sorted cells or equivalent).
- **Target:** F1 ≥ 0.70 at CLUSTER level against CLUS_1333 or a child sub-cluster.
- **Expected output:** AnnotationTransferEvidence on `edge_cea_pkc_delta_neuron_to_cs20230722_clus_1333`; would enable confidence upgrade to MODERATE if F1 threshold met and Sst concern is documented.
- **Resolves:** Unresolved question 2 (correct WMBv1 cluster for CeL PKC-delta-OFF neurons); absent AT evidence caveat.

**4. Targeted literature search for Sst heterogeneity in PKC-delta+ CeL neurons**
- **What:** Cite-traverse for "Prkcd Sst co-expression central amygdala heterogeneity scRNA-seq" to determine whether any publication has reported Sst-expressing subpopulations within PKC-delta+ cells.
- **Target:** Establish whether the DISCORDANT Sst alignment is a known biological feature or a genuine technical artefact.
- **Expected output:** LiteratureEvidence item on this edge; if heterogeneity is documented, cite in rationale and reclassify the discordance.
- **Resolves:** Marker contradiction protocol — Sst discordance not yet documented in gathered literature.

### Open questions

1. Does CLUS_1333 contain a Sst-negative subpopulation identifiable by sub-cluster re-clustering? Are the Prkcd-high cells the Sst-negative ones?
2. Is the CEA-BST Six3 Cyp26b1 Gaba_2 family the correct WMBv1 cluster for CeL PKC-delta-OFF neurons, or is there a more specific Prkcd+/Sst- cluster at higher resolution?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Adke et al. 2019 | [PMID:33188006](https://pubmed.ncbi.nlm.nih.gov/33188006/) | Soma location; Prkcd marker; CeL cell-type composition |
| [2] | Haubensak et al. 2010 | [PMID:21068836](https://pubmed.ncbi.nlm.nih.gov/21068836/) | Soma location; NT type; Prkcd defining marker; Sst negative marker; CeL-OFF circuit |
| [3] | Yeh et al. 2024 | [PMID:38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | Soma location; Prkcd cross-species conservation |
| [4] | Gilpin et al. 2014 | [PMID:25433901](https://pubmed.ncbi.nlm.nih.gov/25433901/) | Neurotransmitter type (GABAergic CeA) |
| [5] | Totty et al. 2024 | [PMID:39463931](https://pubmed.ncbi.nlm.nih.gov/39463931/) | Prkcd marker; primate CeA scRNA-seq Prkcd+/Sst− confirmation |
| [6] | O'Leary et al. 2022 | [PMID:36425768](https://pubmed.ncbi.nlm.nih.gov/36425768/) | Prkcd marker; CEA-BST Six3 Cyp26b1 lineage; mixed Prkcd/Sst expression across clusters |

---

<!-- verdict-block-start: edge_cea_pkc_delta_neuron_to_cs20230722_clus_1333 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  rationale: >
    `marker_Prkcd` CONSISTENT — precomputed mean_expression 7.44 (CeA GABAergic cohort 99.1th
    percentile; tier 2; applied_score 2.0), highest among all CEA-BST candidates;
    `location_soma` CONSISTENT — 56.7% CeA cells by MERFISH (region_fraction 0.567, boundary-band);
    `nt_type` CONSISTENT — GABA label confirmed. Primary concern: `negative_marker_Sst` DISCORDANT —
    Sst mean_expression 1.21 (57.5th pct CeA GABAergic cohort), above minimum-detectable threshold,
    conflicting with canonical Sst-negativity criterion (PMID:21068836); O'Leary et al. 2022
    scRNA-seq (PMID:36425768) documents mixed Prkcd and Sst expression across clusters, suggesting
    population-averaging as a plausible mechanism. No annotation-transfer evidence available;
    confidence capped at LOW. Stage A discovery scored rank 12 of 20 in CeA GABAergic cohort
    (score 2 vs next-best 3) reflecting the Sst penalty (applied_score −1.0) offsetting the
    Prkcd tier-2 gain.
  unresolved_questions:
    - "Trawl literature for Sst heterogeneity within PKC-delta+ CeL neurons — the cluster-average Sst expression may reflect a real subpopulation signal; O'Leary et al. 2022 documents mixed expression but does not quantify the Prkcd+/Sst+ fraction."
    - "Sub-cluster CLUS_1333 and neighbouring CEA-BST Cyp26b1 clusters (CLUS_1331–1335, CLUS_1342–1343) to identify a Prkcd-high/Sst-low subgroup; 1:n cardinality likely across the Gaba_2/4 family."
```
<!-- verdict-block-end -->
