# Central amygdala small aspiny neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala small aspiny neuron is one of three classical morphological cell classes
in the central nucleus of the amygdala (CeA [UBERON:0002883]), first distinguished by Cassell
and colleagues on the basis of soma size and dendritic spine density. Its defining feature —
a small soma with aspiny dendrites — is purely morphological; no molecular markers have been
identified that uniquely demarcate this class from the medium spiny and large aspiny neurons
occupying the same nucleus. Understanding how this morphological class maps to transcriptomically
defined atlas clusters is important for bridging classical CeA circuit physiology with modern
single-cell omics, but the absence of molecular anchors makes this the hardest of the three CeA
morphological types to resolve.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdala [UBERON:0002883] | [1] |
| Neurotransmitter | GABAergic | [2] |
| Defining markers | None recorded | — |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Morphology | Small soma; aspiny dendrites | [1] |
| Notes | Likely overlaps with fast-spiking internuncial neurons of CeA, though direct mapping not given | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / Morphology:** morphological description from review of CeA neuron types · [1]

  > "Morphologically, there are several types of neurons located in the central nucleus of the
  > amygdala (CeA). In the lateral sector of the central nucleus, a predominant cell type with
  > ovoid soma is located. These cells have several primary nonspiny dendrites, branching onto
  > spiny secondary and tertiary dendrite. Their axons begin branching even before leaving the
  > nucleus, which is why these cells are called \"medium spiny neurons\" (Hall, 2004)(McDonald,
  > 1982). Another type of neurons located in the central nuclei have big soma with thick aspiny
  > dendrites, branching on to secondary seldom spiny processes (McDonald, 1982)(Cassell et al.,
  > 1989) (Schiess et al., 1999). The third type of cells are small aspiny neurons (Cassell et
  > al., 1989)"
  > — Nikolenko et al. 2020, Central amygdala cell types · [1] <!-- quote_key: 220976356_f1fe3fe1 -->

- **Neurotransmitter:** CeA striatal-like GABAergic organisation described in review · [2]

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; the single edge
(edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657) carries UNCERTAIN confidence. No
CCN20230722 cluster can be meaningfully distinguished as a match for the small aspiny neuron
given the complete absence of defining molecular markers.

A complete scan of the CCN20230722 survival cohort at MBA:536 (CeA [UBERON:0002883],
GABAergic filter) returned five candidates all tied at discovery score 1 — the minimum
possible value, reflecting region and NT type match only. CS20230722_CLUS_0657 ("Vip Gaba_9")
is listed as rank 1 by cohort ordering only; it has a CeA region_fraction of 0.004 and no
expression markers matched. The Vip Gaba lineage is not expected to match a CeA small aspiny
neuron. The morphological defining property — small soma, aspiny dendrites — cannot be
assessed from WMBv1 transcriptomic metadata. The mapping is entirely uninformative.

### Mapping candidates overview

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | CS20230722_CLUS_0657 | not recorded | not recorded | ⚪ UNCERTAIN | NT CONSISTENT; location APPROXIMATE (region_fraction 0.004); morphology NOT_ASSESSED | No marker match; region_fraction 0.004 |

*1 edge assessed; all carry `evidencell:UncertainRelationship`.*

### Property alignment table — CS20230722_CLUS_0657

**Table 1 — Property comparison.**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Soma location | Central amygdala [UBERON:0002883] | MBA:536 CeA present; region_fraction 0.004 (rank 1 of 5 by ordering only) | APPROXIMATE |
| Morphology (small aspiny) | Small soma, aspiny dendrites [1] | NOT_ASSESSED — morphological information not available from WMBv1 | NOT_ASSESSED |
| Sex ratio | Not documented | Not available | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Nikolenko 2020 morphological review | Literature | PARTIAL | Type definition without transcriptomic or molecular marker information | [1] |
| WMBv1 atlas region/NT filter | Atlas metadata | NO_EVIDENCE | Region filter only; no expression markers matched; Vip Gaba lineage not expected for CeA small aspiny neuron | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

## Eliminated candidates

All five candidates in the discovery cohort scored identically (score 1 = NT type match + region
present). The "top-ranked" candidate CS20230722_CLUS_0657 is an ordering artefact, not a
biologically preferred assignment. The shared disqualifying signal across all five candidates is:

**No discriminating molecular markers available.** The classical node carries no defining
markers, no negative markers, and no neuropeptides. Discovery scores are uniformly 1 across
the entire CeA GABAergic cohort. No candidate can be advanced above the others.

Additional disqualifying detail for CS20230722_CLUS_0657:

- **Location:** region_fraction 0.004 for MBA:536. Fewer than 1% of CLUS_0657 cells localise
  to CeA in the WMBv1 MERFISH spatial registration. The Vip Gaba lineage has its primary
  distribution outside CeA; this selection reflects only that CeA cells survive the regional
  filter, not that CLUS_0657 is a CeA type. *(Very low region_fraction — strong
  counter-evidence against a biologically meaningful match.)*
- **Lineage:** "Vip Gaba_9" designation. VIP-lineage interneurons are a specific
  cortical/hippocampal interneuron class; there is no published evidence that the classical
  small aspiny neuron corresponds to the Vip Gaba transcriptomic lineage.
- **Morphology:** morphological property (small soma, aspiny dendrites) is not assessable from
  WMBv1 metadata — alignment is NOT_ASSESSED for the defining discriminating property of this
  type.
- **Identical candidate pool:** the five discovery candidates are shared with
  cea_medium_spiny_neuron and cea_large_aspiny_neuron. All three classical CeA morphological
  types are currently indistinguishable at the discovery stage.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Central amygdala small aspiny neuron is defined on a
CLASSICAL basis (definition_basis: CLASSICAL): small soma with aspiny dendrites, located in
the central amygdala [UBERON:0002883], GABAergic neurotransmitter type [2]. No defining
molecular markers, negative markers, or neuropeptides are recorded on the classical node. The
morphological description derives from a review of CeA neuron types [1]. Node notes indicate
possible overlap with fast-spiking internuncial neurons of CeA.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722
taxonomy at rank 0 (cluster) using metadata-based scoring (region match MBA:536, NT type
GABAergic). Full scoring rules: `workflows/map-cell-type.md`. The survival cohort contained
5 members; all tied at the minimum discovery score of 1.

**Property alignment.** Each defining property of the classical type was compared to the
corresponding atlas-side value via the `property_comparisons` schema, with alignments graded
CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side values came from WMBv1
metadata and MERFISH spatial registration for soma location. The morphology property is
NOT_ASSESSED because WMBv1 is a transcriptomic atlas with no soma-size or dendritic-spine
morphology data.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim
literature quotes in this report are validated against the evidencell knowledge base at write
time. Authored-prose evidence narratives are validated against their source
`evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier
or unattributed blockquote. Specific mapping limitations and caveats are documented
per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657 | LITERATURE; ATLAS_METADATA | PARTIAL; NO_EVIDENCE | [1]; atlas-internal |

*Generated by evidencell `8222564` at 2026-06-04T10:52:50+00:00 from
[kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** Central amygdala small aspiny neuron → CS20230722_CLUS_0657 at UNCERTAIN
confidence. Key support: NT type CONSISTENT (GABAergic / GABA). Key caveats:
NO_DISCRIMINATING_MARKER (no molecular markers defined; discovery score 1 for all candidates),
AMBIGUOUS_MAPPING (identical candidate pool shared with two sibling CeA morphological types).

No Cell Ontology term currently assigned. The small aspiny neuron class is a purely
morphological taxon at present; it would require at least one molecular discriminant before a
CL contribution could be drafted.

### Proposed experiments and follow-ups

**1. Patch-seq of morphologically identified small aspiny CeA neurons**
- **What:** patch-clamp recording with biocytin fill to confirm morphology (small soma, aspiny
  dendrites), followed by single-cell RNA-seq transcriptome capture
- **Target:** transcriptomic profile sufficient for MapMyCells cluster assignment in CCN20230722
- **Expected output:** AnnotationTransferEvidence linking the morphological class to a specific
  WMBv1 cluster
- **Resolves:** edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657; open question 1

**2. Candidate marker addition + rediscovery**
- **What:** add candidate interneuron markers to the classical node (e.g. Pvalb, Sst, or any
  fast-spiking marker if the type overlaps with CeA internuncial neurons) and re-run discovery
  scoring across all five CeA GABAergic rank-0 candidates
- **Target:** at least one marker that splits the five-way tie (applied_score > 1 for one or
  more candidates)
- **Expected output:** updated property_comparisons with expression-level alignments; possible
  upgrade from UNCERTAIN to LOW or MODERATE
- **Resolves:** edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657; open question 1

### Open questions

1. Do small aspiny neurons in CeA correspond to the fast-spiking internuncial class, and if so
   what molecular markers define them? *(Note: this question also applies to the sibling edges
   for cea_medium_spiny_neuron and cea_large_aspiny_neuron, which share the same candidate
   pool.)*

---

## References

| Label | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nikolenko et al. 2020 | [PMID:32751957](https://pubmed.ncbi.nlm.nih.gov/32751957/) | Soma location; morphological type definition |
| [2] | Yeh et al. 2024 | [PMID:38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | Neurotransmitter type (GABAergic) |

---

<!-- verdict-block-start: edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    No molecular markers are defined for cea_small_aspiny_neuron; discovery score = 1
    (minimum) across all 5 members of the CeA GABAergic cohort (region=MBA:536,
    nt_type=GABAergic). CS20230722_CLUS_0657 ("Vip Gaba_9") is selected by cohort
    ordering only (region_fraction 0.004; no expression markers matched).
    NT type is CONSISTENT (GABAergic / GABA); all other properties are NOT_ASSESSED
    or APPROXIMATE at best. The defining soma/dendrite property (small aspiny soma)
    cannot be assessed from WMBv1 transcriptomic metadata. The Vip Gaba lineage is
    not a biologically expected match for a CeA small aspiny neuron. Mapping is
    entirely uninformative pending molecular characterisation of this soma-defined class.
  reconciliation_note: >
    Identical candidate pool (score 1, cohort_size 5) shared with
    edge_cea_medium_spiny_neuron_to_cs20230722_clus_0657 and
    edge_cea_large_aspiny_neuron_to_cs20230722_clus_0657; all three CeA morphological
    types are currently indistinguishable without molecular markers.
  unresolved_questions:
    - >
      Do small aspiny neurons in CeA correspond to the fast-spiking internuncial class,
      and if so what molecular markers define them? Shared with sibling CeA morphological
      type edges.
```
<!-- verdict-block-end -->
