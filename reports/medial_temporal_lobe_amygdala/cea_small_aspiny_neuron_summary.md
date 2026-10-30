# Central amygdala small aspiny neuron — CCN20230722 Mapping Report
*2026-06-15 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala small aspiny neuron is one of three classical morphological cell types identified within the central nucleus of the amygdala [UBERON:0002883] [1][2]. It is defined by a small soma and aspiny dendrites, distinguishing it from the medium spiny neuron — the predominant CeA output cell — and from the large aspiny neuron with its thick, sparsely branching processes [1]. Like all central amygdala neurons, it is GABAergic [3][4][5][6][7], consistent with the striatum-like organisation of the CeA. The mapping report below describes the current state of atlas evidence for this type: the type lacks defined molecular markers and cannot currently be assigned to any CCN20230722 cluster with biological support.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdala [UBERON:0002883] | [1][2] |
| NT type | GABAergic | [3][4][2][5][6][7] |
| Defining markers | None defined | — |
| Negative markers | None defined | — |
| Neuropeptides | None defined | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / morphology:** Nikolenko et al. 2020 · [1]
  > Morphologically, there are several types of neurons located in the central nucleus of the amygdala (CeA). In the lateral sector of the central nucleus, a predominant cell type with ovoid soma is located. These cells have several primary nonspiny dendrites, branching onto spiny secondary and tertiary dendrite. Their axons begin branching even before leaving the nucleus, which is why these cells are called "medium spiny neurons" (Hall, 2004)(McDonald, 1982). Another type of neurons located in the central nuclei have big soma with thick aspiny dendrites, branching on to secondary seldom spiny processes (McDonald, 1982)(Cassell et al., 1989) (Schiess et al., 1999). The third type of cells are small aspiny neurons (Cassell et al., 1989)
  > — Nikolenko et al. 2020, Central amygdala cell types · [1] <!-- quote_key: 220976356_f1fe3fe1 -->

- **NT type — GABAergic identity:** Multiple sources confirm that CeA neurons are predominantly GABAergic · [2][3][4][5][6][7].

  Waclaw et al. 2010 · [2]:
  > The LA and BLA represent the input to the amygdala and exhibit cortex-like characteristics with a majority of glutamatergic projection neurons (Davis et al., 2000). Conversely, the CA contains striatum-like GABAergic projection neurons and represents the major output of the amygdala (McDonald, 1982)(Davis et al., 2000).
  > — Waclaw et al. 2010, Introduction/Background · [2] <!-- quote_key: 17223544_4fda1404 -->

  Sarowar & Grabrucker 2020 · [4]:
  > The majority of BLA neurons are spiny glutamatergic neurons (with a minority of GABAergic interneurons) (Spampanato et al., 2011). CEl and CEm mainly contain GABAergic neurons.
  > — Sarowar & Grabrucker 2020, Introduction/Background · [4] <!-- quote_key: 221366115_197a5821 -->

  Paul et al. 2025 · [5]:
  > While the CeA consists of mostly inhibitory neurons (McDonald, 2003). A recent study reported that all the analyzed CeA neurons robustly clustered to GABA markers.
  > — Paul et al. 2025, Introduction/Background · [5] <!-- quote_key: 280092907_397d9bdc -->

  Chung et al. 2016 · [6]:
  > The basolateral nucleus of the amygdala (BLA) is highly enriched in glutamatergic principal neurons and is required for associative learning. The central nucleus of the amygdala (CeA) primarily consists of GABAergic medium spiny neurons and controls the processing and expression of emotion.
  > — Chung et al. 2016, Introduction/Background · [6] <!-- quote_key: 3103554_aec310ea -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

A complete scan of CCN20230722 at rank 0 (cluster level) restricted to the central amygdala [UBERON:0002883] and GABAergic neurotransmitter type (MBA:536; 5-member GABAergic cohort) confirmed that no cluster can be distinguished as a molecular correlate of the small aspiny CeA neuron. All five candidates in the survival cohort received identical discovery scores (score = 1; all tied at rank 1 of 5), driven entirely by the region filter — no expression markers contributed. The top-ranked candidate, 0657 Vip Gaba_9 [CS20230722_CLUS_0657], is not biologically expected to correspond to a CeA small aspiny neuron *(note: Vip-lineage GABAergic clusters are cortical/pallial interneuron types, inconsistent with the striatal-like GABAergic composition of the CeA; flagged in the ATLAS_METADATA evidence item for this edge.)*. The absence of any defining molecular markers on the classical type precludes any biologically meaningful assignment at this stage.

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 0657 Vip Gaba_9 [CS20230722_CLUS_0657] | 0181 Vip Gaba_9 | 310 | ⚪ UNCERTAIN | No markers; arbitrary region filter only | Eliminated (no molecular markers) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The central amygdala small aspiny neuron is defined on a CLASSICAL (morphological) basis: small soma with aspiny dendrites, as described in Cassell et al. 1989 and reviewed in Nikolenko et al. 2020 [1]. The node is GABAergic [2][3][4][5][6][7]. No molecular markers, neuropeptides, or transcription factors are defined on this node; the definition basis is purely morphological. The KB notes flag potential overlap with fast-spiking internuncial neurons of the CeA, though no direct mapping has been established.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657 | LITERATURE; ATLAS_METADATA | PARTIAL; NO_EVIDENCE | [1]; — |

*Generated by evidencell `bfdb7f1` at 2026-06-15T10:48:33+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Central amygdala small aspiny neuron → no supportable atlas assignment at this stage. The only candidate edge — to 0657 Vip Gaba_9 [CS20230722_CLUS_0657] — is held at UNCERTAIN confidence and carries no positive supporting evidence; the Vip Gaba lineage is not consistent with a CeA small aspiny neuron, and the candidate emerged only from an uninformative region filter (all five GABAergic CeA cohort members scored identically). Key caveats: (1) no molecular markers are defined for this classical type, making any atlas assignment biologically ungrounded; (2) the three classical CeA morphological types (medium spiny, large aspiny, small aspiny) are currently indistinguishable without molecular discriminators.

No Cell Ontology term is currently assigned. The type is a candidate for a CL contribution once molecular markers are established.

### Proposed experiments and follow-ups

**1. Patch-seq of morphologically identified small aspiny CeA neurons**

- **What:** Patch-clamp recording with morphological recovery (biocytin fill) followed by single-cell RNA sequencing to obtain transcriptomes from morphologically confirmed small aspiny cells.
- **Target:** Direct cluster assignment via MapMyCells at F1 ≥ 0.70 at cluster level.
- **Expected output:** AnnotationTransferEvidence items on the edge; candidate molecular markers to populate `defining_markers` on the KB node.
- **Resolves:** Q1 (molecular identity of small aspiny class); enables re-running discovery with expression-level filtering.

**2. Candidate marker addition + re-run discovery**

- **What:** Literature search for candidate interneuron markers (e.g. Pvalb, Sst, Calb2, Nos1) in CeA small-cell populations; add confirmed markers to `cea_small_aspiny_neuron` and re-run `just find-candidates`.
- **Target:** Survival cohort with at least one marker contributing expression-level signal (applied_score ≥ 0.5).
- **Expected output:** Updated classical node YAML; re-run facts extraction and atlas candidate query.
- **Resolves:** Marker gap; enables meaningful candidate ranking.

**3. Targeted literature search for fast-spiking / internuncial CeA neurons**

- **What:** Cite-traverse for "small aspiny CeA interneuron", "fast-spiking CeA interneuron", "CeA internuncial neuron" to identify primary studies with molecular or transcriptomic characterisation.
- **Target:** At least one primary citation anchoring a marker to morphology-confirmed small aspiny cells.
- **Expected output:** LiteratureEvidence items on the node; candidate markers for Step 2 above.
- **Resolves:** Upstream curation gap; the existing evidence base (morphological class description only) is insufficient for transcriptomic mapping.

### Open questions

1. Do small aspiny neurons in the CeA correspond to the fast-spiking internuncial class, and if so what molecular markers define them? *(Shared with sibling CeA morphological type edges: cea_medium_spiny_neuron, cea_large_aspiny_neuron.)*
2. Are the three classical CeA morphological types (medium spiny, large aspiny, small aspiny) distinguishable at the single-cell transcriptomic level, or do they map onto the same molecular clusters?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nikolenko et al. 2020 | [32751957](https://pubmed.ncbi.nlm.nih.gov/32751957/) | Soma location; morphological class definition |
| [2] | Waclaw et al. 2010 | [20484636](https://pubmed.ncbi.nlm.nih.gov/20484636/) | Soma location; NT type (GABAergic) |
| [3] | Yeh et al. 2024 | [38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | NT type |
| [4] | Sarowar & Grabrucker 2020 | [32858950](https://pubmed.ncbi.nlm.nih.gov/32858950/) | NT type |
| [5] | Paul et al. 2025 | [40686779](https://pubmed.ncbi.nlm.nih.gov/40686779/) | NT type |
| [6] | Chung et al. 2016 | [27053114](https://pubmed.ncbi.nlm.nih.gov/27053114/) | NT type |
| [7] | Hochgerner et al. 2023 | [37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | NT type |

---

<!-- verdict-block-start: edge_cea_small_aspiny_neuron_to_cs20230722_clus_0657 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.0
  rationale: >
    [tier:CUT] No molecular markers defined for cea_small_aspiny_neuron; all five
    GABAergic CeA cohort members (rank 0) scored identically (score=1, rank 1/5),
    rendering the candidate selection biologically uninformative. CS20230722_CLUS_0657
    (Vip Gaba lineage) is not expected to correspond to a CeA small aspiny neuron;
    atlas_metadata evidence is explicitly NO_EVIDENCE. Location comparison is
    APPROXIMATE (region_fraction 0.004; very low CeA representation). Soma-type
    alignment is NOT_ASSESSED. No AnnotationTransferEvidence available.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        No molecular markers are defined for cea_small_aspiny_neuron. Discovery returned
        score 1 for all five candidates in the GABAergic CeA cohort. No expression-level
        signal contributed to candidate ranking; the mapping is entirely uninformative.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Identical candidate pool to cea_medium_spiny_neuron and cea_large_aspiny_neuron;
        the three classical CeA soma-type classes are indistinguishable at the atlas
        query stage without molecular discriminators.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region fraction of 0.004 for the top candidate; may reflect misregistration
        or extremely sparse CeA representation. Not a biologically meaningful match.
  proposed_experiments:
    - >
      Single-cell transcriptomics of small aspiny CeA neurons identified by soma size
      and aspiny dendritic architecture, with post-recording cellular labeling for
      cell-type confirmation, to obtain transcriptomes for CCN20230722 cluster
      assignment; target F1 ≥ 0.70 at cluster level.
    - >
      Add candidate interneuron markers (Pvalb, Sst, Calb2, Nos1) to
      cea_small_aspiny_neuron after targeted literature search and re-run discovery
      to obtain expression-level candidate ranking.
  unresolved_questions:
    - >
      Do small aspiny neurons in CeA correspond to the fast-spiking internuncial class,
      and if so what molecular markers define them? Shared with sibling CeA soma-type
      edges.
    - >
      Are the three classical CeA soma-type classes (medium spiny, large aspiny,
      small aspiny) distinguishable at the single-cell transcriptomic level, or do
      they map onto the same molecular clusters?
```
<!-- verdict-block-end -->
