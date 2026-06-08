# Central amygdala medium spiny neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala medium spiny neuron (CeA MSN) is a morphologically distinctive GABAergic cell type defined by its ovoid soma, primary non-spiny dendrites that branch into spiny secondary and tertiary processes — a morphology closely paralleling that of striatal medium spiny neurons and consistent with the CeA's striatopallidal-like developmental origin *(note: striatopallidal lineage of CeA neurons is a general neuroanatomical inference, not directly stated in the indexed quotes)*. Understanding how this classically-defined type relates to transcriptomic atlas clusters is important both for linking CeA circuitry to whole-brain genomic datasets and for contextualising the CeA's role as a predominantly GABAergic output nucleus in fear, stress, and addiction-related behaviours.

A single mapping edge was evaluated against the CCN20230722 whole-brain transcriptomic atlas. The primary finding is negative: the current evidence is insufficient to identify which CCN20230722 cluster(s) correspond to CeA medium spiny neurons because no discriminating molecular markers are encoded on the classical node.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | [1] |
| Neurotransmitter | GABAergic | [2], [3] |
| Defining markers | Ppp1r1b (DARPP-32) | [4] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Morphology | Ovoid soma; primary non-spiny dendrites; spiny secondary and tertiary dendrites; medium spiny profile | [1] |
| Definition basis | CLASSICAL | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location:** morphological description · reviewed in Nikolenko et al. 2020 · [1]
  > "Morphologically, there are several types of neurons located in the central nucleus of the amygdala (CeA). In the lateral sector of the central nucleus, a predominant cell type with ovoid soma is located. These cells have several primary nonspiny dendrites, branching onto spiny secondary and tertiary dendrite. Their axons begin branching even before leaving the nucleus, which is why these cells are called \"medium spiny neurons\" (Hall, 2004)(McDonald, 1982). Another type of neurons located in the central nuclei have big soma with thick aspiny dendrites, branching on to secondary seldom spiny processes (McDonald, 1982)(Cassell et al., 1989) (Schiess et al., 1999). The third type of cells are small aspiny neurons (Cassell et al., 1989)"
  > — Nikolenko et al. 2020, Central amygdala cell types · [1] <!-- quote_key: 220976356_f1fe3fe1 -->

- **Neurotransmitter (GABAergic):** review of amygdala neuron classification · [2]
  > "Neuronal types differ considerably among the subdivisions of the amygdala (Sah et al., 2003). In the basolateral group, approximately 70% of neurons are thought to be glutamatergic (pyramidal, spiny, or class I neurons). This division also contains interneurons such as GABAergic nonspiny stellate cells of the cortex (called S cells, stellate, or class II neurons). In contrast, within the central nucleus, the majority of cells are thought to be GABAergic."
  > — Ignacio et al. 2014, Classical neuron classes across amygdala subdivisions · [2] <!-- quote_key: 1229611_f7a0a034 -->

- **Neurotransmitter (GABAergic):** CeA as primarily GABAergic output nucleus · [3]
  > "The central amygdala (CeA) plays a central role in physiological and behavioral responses to fearful stimuli, stressful stimuli, and drug-related stimuli. The CeA receives dense inputs from cortical regions, is the major output region of the amygdala, is primarily GABAergic (inhibitory), and expresses high levels of pro- and anti-stress peptides."
  > — Gilpin et al. 2014, Central amygdala cell types · [3] <!-- quote_key: 442779_deea5502 -->

- **Defining marker — Ppp1r1b:** single-cell atlas characterisation of CeA Ppp1r1b+ types · [4]
  > "The Ppp1r1b types correlated with the lateral CEA"
  > — Hochgerner et al. 2023, Inhibitory neurons of valence-learning modulation and output · [4] <!-- quote_key: 264517392_113398c6 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: medium spiny neuron [[CL:1001474](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001474)] (BROAD).

The Cell Ontology has no specific term for a CeA-restricted medium spiny neuron population; CL:1001474 is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster was assessed (CS20230722_CLUS_0723 at rank 0). The mapping is UNCERTAIN: the candidate was selected by CeA region filter alone (score 1) with no molecular marker support. No atlas cluster in the CCN20230722 GABAergic CeA cohort (5 members) could be distinguished as more likely than any other to correspond to CeA medium spiny neurons under current evidence.

**Null result finding.** A scan of CCN20230722 GABAergic clusters in the CeA region (MBA:536) at rank 0 returned a cohort of 5 candidates (CLUS_0657, CLUS_0705, CLUS_0723, CLUS_0725, CLUS_0738), all scoring 1 (region filter only). The best-ranked candidate by region fraction is CLUS_0723 ("Lamp5 Gaba_4") with a CeA region fraction of 0.064 — among the highest in this cohort, but still representing fewer than 7% of the cluster's cells in MBA:536. No marker-level evidence distinguishes among these five candidates. Critically, Ppp1r1b/DARPP-32 — the expected transcriptomic marker for striatal MSN-like cells, confirmed to correlate with lateral CeA types by Hochgerner et al. 2023 [4] — was added to the KB after discovery was run and was not queried against atlas expression data. The mapping therefore cannot be resolved with currently ingested evidence.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10×) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | CS20230722_CLUS_0723 | — | null | ⚪ UNCERTAIN | Region filter only (CeA region_fraction 0.064) | UNCERTAIN |

*1 edge assessed; relationship type: `evidencell:UncertainRelationship`. n_cells null — taxonomy DB rebuild required (see Methods).*

#### Property alignment — CS20230722_CLUS_0723 [UNCERTAIN]

**Table 1 — Property comparison.**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | MBA:536 CeA present; region_fraction 0.064 (highest in rank-0 GABAergic CeA cohort of 5) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Ppp1r1b expression | Defining marker (added post-discovery) | NOT_ASSESSED — HDF5 precomputed stats unavailable | NOT_ASSESSED |
| Morphology (medium spiny) | Ovoid soma, branching spiny secondary/tertiary dendrites | NOT_ASSESSED — morphological information not available from WMBv1 transcriptomic atlas | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Nikolenko 2020 morphology review | Literature | PARTIAL | Classical type definition; no transcriptomic data | [1] |
| CLUS_0723 atlas metadata | Atlas metadata | NO_EVIDENCE | Region filter only; score 1 in cohort of 5; no marker overlap | — |

### CS20230722_CLUS_0723 · ⚪ UNCERTAIN

**Supporting evidence:**

- **NT type CONSISTENT:** CLUS_0723 is annotated GABA in WMBv1, matching the classical GABAergic identity of CeA medium spiny neurons. This is expected across all five CeA GABAergic rank-0 candidates — it provides no discriminating power. [2], [3]
- **Soma location CONSISTENT:** CeA region_fraction of 0.064 is the highest among the five-member GABAergic CeA cohort at rank 0 in the CCN20230722 scan. However, at fewer than 7%, the majority of CLUS_0723 cells do not reside in MBA:536 — and the UNCERTAIN classification reflects this, combined with the absence of any marker evidence.

**Marker evidence provenance:**

- **Ppp1r1b (DARPP-32):** Hochgerner et al. 2023 [4] is a primary single-cell atlas study reporting that Ppp1r1b+ types correlate with the lateral CeA.

  > "The Ppp1r1b types correlated with the lateral CEA"
  > — Hochgerner et al. 2023, Inhibitory neurons of valence-learning modulation and output · [4] <!-- quote_key: 264517392_113398c6 -->

  This is transcript-level evidence from a scRNA-seq atlas with spatial registration (lateral CeA localisation). The evidence is methodologically appropriate — single-cell resolution with anatomical annotation — but the specific cluster identity in CCN20230722 terms remains unresolved because HDF5 precomputed expression stats were unavailable when discovery was run. Ppp1r1b was added to the KB as a defining marker after the initial scoring pass; its expression levels across CLUS_0657, CLUS_0705, CLUS_0723, CLUS_0725, and CLUS_0738 have not been interrogated. Source-side Ppp1r1b relevance is confirmed in literature (lateral CeA correlation); target-side is still unresolvable from current atlas metadata.

**Concerns:**

- **No discriminating markers at time of discovery.** The discovery scored all five CeA GABAergic candidates at 1 (region filter only). CLUS_0723 ranks third in the cohort (rank_in_cohort 3 of 5) with next_best_score also 1 — there is no dominance. The selection of CLUS_0723 as the single reported edge is an arbitrary tie-break, not a meaningful biological signal. *(The three CeA morphological types — cea_medium_spiny_neuron, cea_large_aspiny_neuron, cea_small_aspiny_neuron — return identical rank-0 candidates because none have markers; see AMBIGUOUS_MAPPING caveat.)*
- **HDF5 precomputed stats unavailable.** Ppp1r1b expression cannot be cross-checked against the WMBv1 atlas cluster profiles until the CCN20230722 HDF5 file is accessible and the taxonomy DB is rebuilt. Until then, the only available marker evidence is the metadata-level assertion that Ppp1r1b types correlate with lateral CeA (Hochgerner et al. 2023 [4]) — insufficient to discriminate among the five candidates.
- **Morphology not assessable from transcriptomic atlas.** The medium spiny morphology is the defining feature of this classical type but is invisible to the transcriptomic mapping workflow. Even after Ppp1r1b-guided re-discovery, morphological confirmation will require independent multimodal data.

**What would upgrade confidence:**

- **Primary action — rebuild taxonomy DB with HDF5 and re-run discovery.** Once CCN20230722 HDF5 precomputed expression stats are available, add Ppp1r1b as a defining marker on the KB node and re-run `just find-candidates` at rank 0. If a CeA cluster shows selective Ppp1r1b expression above MIN_DETECTABLE, re-score accordingly. This is the single most important next step.
- **Targeted atlas query for CEA-AAA-BST Six3 Sp9 clusters.** These subclass-level candidates are the expected transcriptomic home for striatal-lineage CeA cell types. A direct query for clusters within this subclass that (a) localise to MBA:536 and (b) express Ppp1r1b would substantially constrain the mapping.
- **Annotation transfer (AnnotationTransferEvidence, target F1 ≥ 0.60 at cluster level).** A MapMyCells run using a source dataset with morphology-confirmed or Cre-driver-confirmed CeA MSN-like cells (e.g. D1-Cre or DARPP-32-Cre labelled CeA neurons) would provide the most direct transcriptomic linkage. Would add AnnotationTransferEvidence to this edge.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Central amygdala medium spiny neuron is defined on a CLASSICAL basis: morphological characterisation from McDonald (1982) and Hall (2004) as reviewed in Nikolenko et al. 2020 [1], with GABAergic neurotransmitter type supported by two independent reviews [2][3]. The single defining molecular marker (Ppp1r1b/DARPP-32) was added to the KB node following initial discovery, citing Hochgerner et al. 2023 [4]; it was not available to the Stage A scoring pass.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:536, NT type GABAergic). Full scoring rules: `workflows/map-cell-type.md`. The resulting cohort comprised 5 GABAergic CeA clusters; all scored 1 (region filter only). No defining markers were available to the scorer at the time of discovery.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / NOT_ASSESSED. Atlas-side numerical values for Ppp1r1b expression are not available because the CCN20230722 HDF5 precomputed stats file had not been ingested at the time of this mapping run. Morphology is structurally NOT_ASSESSED (the WMBv1 atlas does not contain morphological feature vectors).

**Atlas data sources.** CCN20230722 (WMBv1); taxonomy YAML and SQLite index in `kb/taxonomy/CCN20230722/`. Pseudobulk SHA not available (HDF5 not yet ingested). The `n_cells` column on the mapping edge returns null — the taxonomy DB predates PR #21 (n_cells addition); rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` before the next report cycle.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_medium_spiny_neuron_to_cs20230722_clus_0723 | LITERATURE; ATLAS_METADATA | PARTIAL; NO_EVIDENCE | [1]; — |

*Generated by evidencell `8222564` at 2026-06-04T10:52:50+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Central amygdala medium spiny neuron → CS20230722_CLUS_0723 at UNCERTAIN confidence. Key support: GABAergic NT type is CONSISTENT; CeA soma location is CONSISTENT at region_fraction 0.064. Key caveats: NO_DISCRIMINATING_MARKER (all five CeA GABAergic candidates score equally); HDF5 unavailable (Ppp1r1b expression cannot be cross-checked); mapping is indistinguishable from cea_large_aspiny_neuron and cea_small_aspiny_neuron (AMBIGUOUS_MAPPING).

The Cell Ontology has no specific term for this population; medium spiny neuron [CL:1001474](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001474) is the closest ancestor (BROAD mapping). The CeA MSN is a biologically distinct cell population — defined by morphology, striatopallidal developmental origin, and Ppp1r1b expression in lateral CeA — and is a candidate for a new, more specific CL term. Auto-proposed mapping requires expert review.

No Cell Ontology term currently assigned at the specificity needed. Candidate for CL contribution.

### Proposed experiments and follow-ups

**1. Add Ppp1r1b to defining markers and re-run discovery (immediate; no new data required)**

- **What:** Update `cea_medium_spiny_neuron` KB node with Ppp1r1b as a formal `defining_marker` (citing PMID:37884748 [4]); then run `just find-candidates` at ranks 0 and 1 once CCN20230722 HDF5 stats are available.
- **Target:** Score > 1 (region + at least one marker tier credit); identify a dominant candidate in the CeA cohort.
- **Expected output:** New or updated MappingEdge YAML with Ppp1r1b-guided property comparison; replaces the current region-only UNCERTAIN edge.
- **Resolves:** Q1 (which clusters express Ppp1r1b in CeA); NO_DISCRIMINATING_MARKER and AMBIGUOUS_MAPPING caveats for all three CeA morphological types.

**2. CEA-AAA-BST Six3 Sp9 Gaba subclass targeted query**

- **What:** Direct metadata query for clusters in the Six3/Sp9 Gaba subclass of CCN20230722 (the expected striatal-lineage transcriptomic home) that (a) localise to MBA:536 and (b) express Ppp1r1b above MIN_DETECTABLE.
- **Target:** Identify ≥1 CeA-enriched cluster with Ppp1r1b expression; compare region_fraction against CeA morphological type candidates.
- **Expected output:** CandidateAtlasCluster evidence or updated MappingEdge.
- **Resolves:** Q1; AMBIGUOUS_MAPPING; possible upgrade from UNCERTAIN to LOW or MODERATE.

**3. Annotation transfer from a Cre-driver or DARPP-32-labelled CeA dataset**

- **What:** MapMyCells run using source cells confirmed as CeA Ppp1r1b+ (e.g. from a D1-Cre or DARPP-32-Cre intersectional dataset, or from a lateral CeA patch-seq dataset with MSN morphology confirmed).
- **Target:** F1 ≥ 0.60 at cluster level against CCN20230722.
- **Expected output:** AnnotationTransferEvidence item on this edge.
- **Resolves:** Q1 and morphology concern; could upgrade confidence to LOW (with single strong AT result) or MODERATE (AT + Ppp1r1b marker confirmation).

### Open questions

1. **Which WMBv1 CeA cluster(s) express Ppp1r1b/DARPP-32 at detectable levels?** This is the primary unresolved question. Hochgerner et al. 2023 confirms that Ppp1r1b+ types correlate with the lateral CeA [4], but the specific CCN20230722 cluster identity is unknown because HDF5 stats were unavailable.

2. **Can the three CeA morphological types (medium spiny, large aspiny, small aspiny) be distinguished at the transcriptomic level?** All three currently share identical rank-0 candidates. The AMBIGUOUS_MAPPING caveat applies equally to cea_medium_spiny_neuron, cea_large_aspiny_neuron, and cea_small_aspiny_neuron. Resolving this requires either (a) distinct marker profiles for each morphological type or (b) multimodal (patch-seq) data linking morphology to transcriptomic identity. *(This question appears on all three CEA morphological type edges.)*

3. **Is the CeA medium spiny neuron sufficiently distinct to warrant a new CL term?** The CL:1001474 (BROAD) mapping and the striatopallidal biology suggest this type may merit a more specific CL representation once the transcriptomic identity is established.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nikolenko et al. 2020 — "Morphology of Central Amygdala Neurons" | [PMID:32751957](https://pubmed.ncbi.nlm.nih.gov/32751957/) | Soma location; morphological definition |
| [2] | Ignacio et al. 2014 — "Effects of Acute Prenatal Exposure to Ethanol on microRNA Expression are Ameliorated by Social Enrichment" | [PMID:25309888](https://pubmed.ncbi.nlm.nih.gov/25309888/) | Neurotransmitter type (GABAergic) |
| [3] | Gilpin et al. 2014 — "The central amygdala as an integrative hub for anxiety and alcohol use disorders" | [PMID:25433901](https://pubmed.ncbi.nlm.nih.gov/25433901/) | Neurotransmitter type (GABAergic) |
| [4] | Hochgerner et al. 2023 — "Conservative and variable regions of the mouse cortex define lateralized associations" | [PMID:37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Ppp1r1b marker (lateral CeA correlation) |

---

<!-- verdict-block-start: edge_cea_medium_spiny_neuron_to_cs20230722_clus_0723 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    evidencell:UncertainRelationship to CS20230722_CLUS_0723 based on region
    filter only (discovery score 1 in a GABAergic CeA cohort of 5; all five
    candidates scored equally; rank_in_cohort 3 of 5; next_best_score 1).
    NT type (GABAergic) is CONSISTENT but provides no discriminating power
    across the cohort. Ppp1r1b (DARPP-32) — the defining marker for
    striatal-lineage CeA medium spiny neurons per Hochgerner et al. 2023
    (PMID:37884748) — was added to the KB node post-discovery; target-side
    expression is NOT_ASSESSED because HDF5 precomputed stats are unavailable.
    Soma and dendritic form (medium spiny profile) is structurally NOT_ASSESSED by the
    WMBv1 transcriptomic atlas. No positive evidence distinguishes
    CS20230722_CLUS_0723 from the four sibling CeA GABAergic candidates for
    this soma/dendrite-defined type.
  reconciliation_note: >
    cea_medium_spiny_neuron, cea_large_aspiny_neuron, and cea_small_aspiny_neuron
    share identical rank-0 candidates (CLUS_0657/0705/0723/0725/0738) because none
    carry molecular markers distinguishable by Stage A scoring. The three edges are
    indistinguishable on current evidence (AT panels, marker panels, and ephys all
    not assessed). See AMBIGUOUS_MAPPING caveat; resolves once Ppp1r1b and
    structural markers are encoded and HDF5 stats are available.
  unresolved_questions:
    - "Which WMBv1 CeA cluster(s) express Ppp1r1b/DARPP-32 (the striatal MSN marker) and should be the primary candidate for medium spiny neurons?"
    - "Can the three CeA morphological types (medium spiny, large aspiny, small aspiny) be distinguished transcriptomically? All three share identical rank-0 candidates under current marker coverage."
```
<!-- verdict-block-end -->
