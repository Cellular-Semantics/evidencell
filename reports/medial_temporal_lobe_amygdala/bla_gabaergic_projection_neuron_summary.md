# Basolateral amygdala GABAergic projection neuron (SST/nNOS) — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) GABAergic projection neuron (SST/nNOS) is a rare long-range inhibitory cell type co-expressing somatostatin (Sst) and neuronal nitric oxide synthase (Nos1/nNOS), constituting approximately 5.5–8% of GABAergic neurons in the lateral and basal amygdala [1]. Unlike the majority of BLA interneurons, which are strictly local, this type bears a long-range axon projecting beyond the amygdala — making it functionally distinct from dendrite-targeting Sst+ interneurons. McDonald et al. 2012 [2] demonstrated that SOM+ long-range non-pyramidal (LRNP) neurons in the BLA project to distal targets including the basal forebrain, while McDonald & Mott 2016 [3] synthesise the broader evidence for long-range GABAergic amygdalo-hippocampal circuit connections. Mapping this type to the CCN20230722 atlas provides an entry point for understanding whether the SST+/nNOS+ projection identity corresponds to a defined transcriptomic cluster or is a functional specialisation within the broader Sst Chodl family.

### Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1], [2] |
| NT type | GABAergic | [3], [1] |
| Defining markers | Sst, Nos1 | [1] |
| Negative markers | Pvalb | [1] |
| Neuropeptides | Sst | [1] |
| Definition basis | CLASSICAL | — |

Notes: Distinct from local SOM dendrite-targeting interneurons by virtue of projection axon and nNOS co-expression; estimated 5.5–8% of BLA GABAergic cells.

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location / NT type / defining markers Sst and Nos1 / neuropeptide Sst / negative marker Pvalb:** asta_report synthesis · mouse BLA stereological quantification · [1]

  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 232283078_d4238834 -->

- **Soma location (LRNP projection evidence):** asta_snippet · rat amygdala-to-basal forebrain retrograde tracing + SOM immunolabeling · [2]

  > a subpopulation of non-pyramidal SOM+ neurons, termed 'long-range non-pyramidal neurons' (LRNP neurons), in the external capsule, basolateral amygdala, and cortical and medial amygdalar nuclei were FG+
  > — McDonald et al. 2012, abstract · [2] <!-- quote_key: 11544073_bef58c1f -->

- **NT type (long-range GABAergic projection):** asta_report · amygdalo-hippocampal literature review · [3]

  > The amygdalar nuclear complex and hippocampal/parahippocampal region are key components of the limbic system that play a critical role in emotional learning and memory. This Review discusses what is currently known about the neuroanatomy and neurotransmitters involved in amygdalo‐hippocampal interconnections, their functional roles in learning and memory, and their involvement in mnemonic dysfunctions associated with neuropsychiatric and neurological diseases. Tract tracing studies have shown that the interconnections between discrete amygdalar nuclei and distinct layers of individual hippocampal/parahippocampal regions are robust and complex. Although it is well established that glutamatergic pyramidal cells in the amygdala and hippocampal region are the major players mediating interconnections between these regions, recent studies suggest that long‐range GABAergic projection neurons are also involved. Whereas neuroanatomical studies indicate that the amygdala only has direct interconnections with the ventral hippocampal region, electrophysiological studies and behavioral studies investigating fear conditioning and extinction, as well as amygdalar modulation of hippocampal‐dependent mnemonic functions, suggest that the amygdala interacts with dorsal hippocampal regions via relays in the parahippocampal cortices. Possible pathways for these indirect interconnections, based on evidence from previous tract tracing studies, are discussed in this Review. Finally, memory disorders associated with dysfunction or damage to the amygdala, hippocampal region, and/or their interconnections are discussed in relation to Alzheimer's disease, posttraumatic stress disorder (PTSD), and temporal lobe epilepsy. © 2016 Wiley Periodicals, Inc.
  > — McDonald & Mott 2016, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 3460849_57002ff6 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; 0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850] in supertype 0239 Sst Chodl Gaba_2 is the primary mapping at LOW confidence (skos:broadMatch 1:n; all three marker comparisons CONSISTENT; no annotation transfer).

### 4a. Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---|---:|---|---|---|
| 1 | 0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850] | 0239 Sst Chodl Gaba_2 | 407 | 🔴 LOW | Sst CONSISTENT · Nos1 CONSISTENT · Pvalb absent CONSISTENT | broadMatch 1:n; 3 of 3 markers CONSISTENT; no AT |

Note: 1 edge assessed; relationship skos:broadMatch (1:n).

### 4b. Property alignment table — 0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850]

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | not available | MBA:295 BLA present; region_fraction 0.015 | CONSISTENT |
| NT type | GABAergic | not available | GABA | CONSISTENT |
| Sst expression | defining marker | not available | precomputed mean 12.23 (99.6th pct; tier 2) | CONSISTENT |
| Nos1 expression | defining marker (nNOS) | not available | precomputed mean 12.1 (tier 2); canonical Sst Chodl family | CONSISTENT |
| Pvalb (negative marker) | negative marker | not available | val 0.0 (0th pct; effectively absent) | CONSISTENT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki et al. 2021 ASTA report | Literature | SUPPORT | SST+/nNOS+ projection neurons estimated 5.5–8% of BLA GABAergic cells; long-range projecting | [1] |
| CLUS_0850 atlas metadata | Atlas metadata | SUPPORT | Sst 99.6th pct, Nos1 tier-2, Pvalb 0.0; three Sst Chodl clusters (0850/0858/0860) score equally (score 6) | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### 0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850] · 🔴 LOW

**Supporting evidence:**

- Atlas metadata for [CS20230722_CLUS_0850] shows all three marker and negative-marker property comparisons CONSISTENT: Sst precomputed mean 12.23 (99.6th percentile in the BLA GABAergic survival cohort of 5 clusters), Nos1 precomputed mean 12.1 (tier 2), and Pvalb val 0.0 (absent). The Sst Chodl cluster family is the canonical Sst+/Nos1+ GABAergic type in CCN20230722. Three Sst Chodl clusters (CLUS_0850, CLUS_0858, CLUS_0860) score equally (score 6 of 6). [atlas-internal]

- Vereczki et al. 2021 [1] establishes the SST+/nNOS+ BLA projection neuron as a distinct subtype comprising 5.5–8% of BLA GABAergic cells, with co-expression of somatostatin and nNOS as definitive markers:

  > we estimated that the following cell types together compose the vast majority of GABAergic cells in the LA and BA: axo-axonic cells (5.5%-6%), basket cells expressing parvalbumin (17%-20%) or cholecystokinin (7%-9%), dendrite-targeting inhibitory cells expressing somatostatin (10%-16%), NPY-containing neurogliaform cells (14%-15%), VIP and/or calretinin-expressing interneuron-selective interneurons (29%-38%), and GABAergic projection neurons expressing somatostatin and neuronal nitric oxide synthase (5.5%-8%). Our results show that these amygdalar nuclei contain all major GABAergic neuron types as found in other cortical regions.
  > — Vereczki et al. 2021, Basolateral amygdala neuronal subtypes · [1] <!-- quote_key: 232283078_d4238834 -->

- McDonald et al. 2012 [2] confirms the long-range projection identity in rat BLA, demonstrating that SOM+ non-pyramidal LRNP neurons in the BLA and related nuclei project to basal forebrain:

  > a subpopulation of non-pyramidal SOM+ neurons, termed 'long-range non-pyramidal neurons' (LRNP neurons), in the external capsule, basolateral amygdala, and cortical and medial amygdalar nuclei were FG+
  > — McDonald et al. 2012, abstract · [2] <!-- quote_key: 11544073_bef58c1f -->

- Stage A discovery: CLUS_0850 ranked 1st within the BLA GABAergic cohort (cohort_size = 5, score = 6, next_best_score = 6). Sst contributed applied_score 2.0 (pct 0.996), Nos1 contributed applied_score 2.0 (pct 0.996), and absence of Pvalb contributed applied_score 1.0. *(note: the cohort is small (n=5) and all three Sst Chodl clusters are tied at the top; dominance should be read in the context of this small cohort size.)*

**Marker evidence provenance:**

- **Sst (defining marker and neuropeptide):** Evidence is from the Vereczki et al. 2021 asta_report synthesis [1], scope "marker synthesis from ASTA report," in mouse BLA with stereological quantification of major GABAergic subtypes. Atlas-side: Sst precomputed mean 12.23 at 99.6th percentile within the BLA GABAergic cohort — strong concordance. No atlas annotation vs. expression discrepancy detected.
- **Nos1 (defining marker / nNOS):** Evidence from Vereczki et al. 2021 [1]. Atlas-side: Nos1 mean 12.1 (tier 2). The Sst Chodl cluster family is described as the canonical Sst+/Nos1+ type in CCN20230722 taxonomy metadata. Note that CLUS_0850, CLUS_0858, and CLUS_0860 all score equally on Sst+Nos1 — the Nos1 tier-2 signal does not discriminate among the three Sst Chodl clusters at rank-0.
- **Pvalb (negative marker):** Pvalb val 0.0 (0th percentile) is CONSISTENT with the classical Pvalb-negativity. Vereczki et al. 2021 [1] establishes PVALB+ and non-PVALB populations as non-overlapping GABAergic subsets in mouse BLA. No discrepancy.

**Concerns:**

- **DISTRIBUTED_ACROSS_CLUSTERS (1:n ambiguity):** CLUS_0850, CLUS_0858, and CLUS_0860 all score 6 on the Sst+Nos1 composite. The 1:n broadMatch cardinality reflects this: atlas metadata alone cannot identify which Sst Chodl cluster best corresponds to the BLA SST+/nNOS+ projection neuron. The classical type's key functional feature (long-range projection axon) is not reflected in atlas transcriptomic metadata.
- **No annotation transfer (AT) evidence.** LOW confidence is primarily driven by the absence of any cell-level experiment directly linking labeled SST+/nNOS+ BLA projection neurons to an atlas cluster. Without AT, it is not possible to confirm that the Sst Chodl transcriptomic identity is causally linked to the projection phenotype.
- Region_fraction for [CS20230722_CLUS_0850] in MBA:295 is 0.015 (property comparison). *(note: low region_fraction is expected for a long-range projection neuron whose soma may span multiple amygdalar subregions; this is not a strong counter-indicator given the documented BLA soma location.)*

**What would upgrade confidence:**

1. **Annotation transfer using a projection-neuron–labelled dataset:** Retrograde labeling of BLA SST/nNOS projection neurons followed by single-nucleus profiling and MapMyCells annotation to CCN20230722 would add `AnnotationTransferEvidence`. F1 ≥ 0.50 at CLUSTER level on one of the three Sst Chodl clusters would upgrade to MODERATE and resolve the 1:n ambiguity. This directly addresses open question 1.
2. **Retrograde tracing + SST/NOS1 intersectional labeling:** Confirms that the Sst+/Nos1+ BLA population is the long-range projecting subtype and not shared with local dendrite-targeting interneurons. Would add `LiteratureEvidence` corroborating the broadMatch predicate.
3. **Targeted literature search:** "Sst Chodl long-range BLA projection" or "nNOS Sst amygdala mouse single-cell" may surface published transcriptomic characterisation, adding `LiteratureEvidence` without new experiments.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Basolateral amygdala GABAergic projection neuron (SST/nNOS) is defined on a `CLASSICAL` definition basis. Defining markers are Sst and Nos1 [1]; neuropeptide is Sst [1]; negative marker is Pvalb [1]; soma location is basolateral amygdala [UBERON:0002887] [1], [2]; NT type is GABAergic [3], [1]. Vereczki et al. 2021 [1] provides the primary quantitative census of BLA GABAergic subtypes and establishes SST+/nNOS+ co-expression as the defining molecular signature. McDonald et al. 2012 [2] demonstrates long-range projection identity via retrograde tracing in rat BLA. McDonald & Mott 2016 [3] synthesises amygdalo-hippocampal interconnection evidence including long-range GABAergic projections.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**
- Atlas: CCN20230722; taxonomy_id: CCN20230722; pseudobulk source: taxonomy reference store (precomputed stats).

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `c4efa0e` at 2026-06-05T13:42:48+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_gabaergic_projection_neuron_to_cs20230722_clus_0850 | LITERATURE; ATLAS_METADATA | SUPPORT; SUPPORT | [1]; atlas-internal |

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala GABAergic projection neuron (SST/nNOS) → 0850 Sst Chodl Gaba_2 [CS20230722_CLUS_0850] at LOW confidence. Key support: atlas metadata with 3 of 3 marker/negative-marker comparisons CONSISTENT (Sst 99.6th pct, Nos1 tier-2, Pvalb absent), corroborated by literature (Vereczki et al. 2021 [1]). Key caveats: 1:n ambiguity across three equally-scoring Sst Chodl clusters (CLUS_0850, CLUS_0858, CLUS_0860); no annotation transfer evidence available.

No Cell Ontology term currently assigned. This rare long-range GABAergic projection type, co-defined by SST and nNOS co-expression, has no matching CL term and is a candidate for a new CL contribution once the mapping is resolved.

### Proposed experiments and follow-ups

**1. Annotation transfer (projection-neuron labelled dataset)**
- **What:** Single-nucleus or single-cell transcriptomics on retrogradely labeled BLA SST/nNOS projection neurons, followed by MapMyCells annotation transfer to CCN20230722.
- **Target:** F1 ≥ 0.50 at CLUSTER level on one of the three Sst Chodl clusters.
- **Expected output:** `AnnotationTransferEvidence` on `edge_bla_gabaergic_projection_neuron_to_cs20230722_clus_0850`; potential upgrade to MODERATE and resolution of 1:n ambiguity.
- **Resolves:** Open question 1 (do Sst Chodl clusters correspond to the long-range projecting SST/nNOS population?); identifies which of CLUS_0850/0858/0860 is the best specific match.

**2. Retrograde tracing + SST/NOS1 intersectional labeling**
- **What:** Combinatorial retrograde tracing from BLA projection targets combined with SST and nNOS co-detection in mouse BLA, with cell-density quantification.
- **Target:** Confirm that retrograde-labeled neurons are SST+/NOS1+ and Pvalb-negative.
- **Expected output:** `LiteratureEvidence` corroborating the broadMatch predicate and projection identity.
- **Resolves:** Whether the BLA SST/nNOS cell type is a single transcriptomic entity or contains projection-target-specific subpopulations; whether local SST interneurons share the same transcriptomic cluster.

**3. Targeted literature search**
- **What:** Cite-traverse for "Sst Chodl long-range BLA projection" or "nNOS Sst amygdala mouse single-cell transcriptomics."
- **Target:** Identify any published single-cell or spatial characterisation of SST+/nNOS+ projection neurons in mouse BLA cross-referenced to WMBv1 or CCN20230722.
- **Expected output:** Additional `LiteratureEvidence`; possibly data enabling direct atlas comparison without new experiments.
- **Resolves:** Source-side expression evidence gap.

### Open questions

1. Do Sst Chodl clusters (CLUS_0850, CLUS_0858, CLUS_0860) in the BLA correspond specifically to the long-range projecting SST/nNOS population, or does the Sst Chodl transcriptomic type also encompass local SST interneurons? (`edge_bla_gabaergic_projection_neuron_to_cs20230722_clus_0850`)
2. Which of the three equally-scoring Sst Chodl clusters best represents the BLA SST/nNOS projection neuron — does projection target identity map to distinct rank-0 clusters within the Sst Chodl family? (`edge_bla_gabaergic_projection_neuron_to_cs20230722_clus_0850`)

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vereczki et al. 2021 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | soma location, NT type, defining markers, neuropeptides, negative markers |
| [2] | McDonald et al. 2012 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | soma location |
| [3] | McDonald & Mott 2016 | [26876924](https://pubmed.ncbi.nlm.nih.gov/26876924/) | neurotransmitter type |

---

<!-- verdict-block-start: edge_bla_gabaergic_projection_neuron_to_cs20230722_clus_0850 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    3 of 3 markers CONSISTENT (marker_Sst: precomputed mean 12.23 at 99.6th pct; marker_Nos1: precomputed mean 12.1 tier-2; negative_marker_Pvalb: val 0.0) anchors broadMatch to CS20230722_CLUS_0850. LOW confidence: no AT evidence; DISTRIBUTED_ACROSS_CLUSTERS caveat — CLUS_0850, CLUS_0858, and CLUS_0860 score equally (score 6 in BLA GABAergic cohort of 5).
  reconciliation_note: ""
  lit_to_lit_edges: []
  unresolved_questions:
    - "Which of CLUS_0850, CLUS_0858, CLUS_0860 best represents the BLA long-range SST/nNOS projection neuron — retrograde tracing plus atlas cross-reference needed to discriminate."
```
<!-- verdict-block-end -->
