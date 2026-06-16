# Basal amygdala extinction neuron — CCN20230722 Mapping Report
*2026-06-16 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Within the basal nucleus of the amygdala, principal glutamatergic neurons segregate into two functionally distinct, non-overlapping populations: fear neurons, which respond to the conditioned stimulus, and extinction neurons, which become active only after repeated presentations of the conditioned stimulus without reinforcement [1]. Extinction neurons are distinguished by reciprocal connectivity with the medial prefrontal cortex (mPFC), a property absent from fear neurons, and by their molecular identity as *Thy1*-expressing, *Ntsr2*-positive BLA principal cells [2, 3].

### Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdaloid complex [UBERON:0002887] | [1][2][3] |
| Neurotransmitter | Glutamatergic | [4][5] |
| Defining markers | Ntsr2, Dkk3, Rspo2, Wnt7a, Thy1 | [3] |
| Negative markers | — | — |
| Neuropeptides | — | — |

<details>
<summary>Per-property literature support</summary>

**Soma location.** Extinction neurons reside in the basal nucleus of the amygdala, as established through in vivo electrophysiology and anatomical tracing studies. Carrere & Alexandre [1] place both fear and extinction neurons in the basal amygdala nucleus; Cardenas et al. [2] confirm that both populations are BLA principal neurons projecting to mPFC; McCullough et al. [3] validate the *Thy1*/*Ntsr2* population within the BLA through transgenic labelling.

**Neurotransmitter type.** Glutamatergic identity is inferred from the classification of extinction neurons as BLA principal neurons, which are predominantly glutamatergic [4, 5]. Hochgerner et al. [4] provide single-cell transcriptomic evidence for the VGLUT1 (*Slc17a7*) identity of BLA excitatory types; Totty et al. [5] confirm glutamatergic neuron diversity in the primate BLA, including cross-species conservation.

**Defining markers.** McCullough et al. [3] used RNA sequencing of behaviourally characterised *Thy1*-labelled Fear-Off neurons to identify *Ntsr2*, *Dkk3*, *Rspo2*, and *Wnt7a* as genes strongly upregulated in this population; *Ntsr2*-expressing BLA neurons were validated as a putative Fear-Off population by immunohistochemistry and optogenetic silencing.

</details>

---

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

**Null result headline.** The CCN20230722 atlas does not currently provide expression data for four of the five defining markers of basal amygdala extinction neurons (Ntsr2, Rspo2, Wnt7a, Thy1 are absent from precomputed expression in all surveyed clusters). Without annotation transfer evidence and with marker cross-checks limited to *Dkk3* alone, no candidate cluster can be assigned a confidence level above UNCERTAIN at this time. The candidates presented below represent the best available matches given this constraint; they narrow the search space and should direct future annotation-transfer experiments.

The three leading candidates all belong to glutamatergic supertypes within the lateral–basolateral–basomedial–posterior amygdala (LA-BLA-BMA-PA) grouping, consistent with the basal nucleus location of the classical type [1, 2, 3].

### Table 1 — Property comparison: 0245 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0245]

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glut (prefix match) | CONSISTENT |
| Soma location | BLA [UBERON:0002887] | Cortical subplate [MBA:703], Basolateral amygdalar nucleus [MBA:295], Basolateral amygdalar nucleus [MBA:295] (top-3 by cell count within 100 µm) | CONSISTENT |
| Dkk3 expression | Defining marker | 7.78 (cohort percentile 0.968) | CONSISTENT |
| Ntsr2 expression | Defining marker | No atlas data | NOT ASSESSED |
| Rspo2 expression | Defining marker | No atlas data | NOT ASSESSED |
| Wnt7a expression | Defining marker | No atlas data | NOT ASSESSED |
| Thy1 expression | Defining marker | No atlas data | NOT ASSESSED |

### Table 2 — Evidence support: 0245 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0245]

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.703; Dkk3 at 96.8th percentile in cohort | CCN20230722 |

### Table 3 — Property comparison: 0250 LA-BLA-BMA-PA Glut_6 [CS20230722_CLUS_0250]

| Property | Classical | Atlas cluster | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Glut (prefix match) | CONSISTENT |
| Soma location | BLA [UBERON:0002887] | Cortical subplate [MBA:703], Basolateral amygdalar nucleus [MBA:295], Basolateral amygdalar nucleus, anterior part [MBA:303] | CONSISTENT |
| Dkk3 expression | Defining marker | 8.81 (cohort percentile 0.989) | CONSISTENT |
| Ntsr2 expression | Defining marker | No atlas data | NOT ASSESSED |
| Rspo2 expression | Defining marker | No atlas data | NOT ASSESSED |
| Wnt7a expression | Defining marker | No atlas data | NOT ASSESSED |
| Thy1 expression | Defining marker | No atlas data | NOT ASSESSED |

### Table 4 — Evidence support: 0250 LA-BLA-BMA-PA Glut_6 [CS20230722_CLUS_0250]

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.764; Dkk3 at 98.9th percentile in cohort | CCN20230722 |

### Table 5 — Property comparison: 0064 LA-BLA-BMA-PA Glut_5 [CS20230722_SUPT_0064]

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| Neurotransmitter | Glutamatergic | Not asserted at supertype level | NOT ASSESSED |
| Soma location | BLA [UBERON:0002887] | Cortical subplate [MBA:703], Basolateral amygdalar nucleus [MBA:295], Basolateral amygdalar nucleus, anterior part [MBA:303] | CONSISTENT |
| Dkk3 expression | Defining marker | 5.47 (cohort percentile 0.816; child-cluster coverage 1.000) | CONSISTENT |
| Ntsr2 expression | Defining marker | No atlas data | NOT ASSESSED |
| Rspo2 expression | Defining marker | No atlas data | NOT ASSESSED |
| Wnt7a expression | Defining marker | No atlas data | NOT ASSESSED |
| Thy1 expression | Defining marker | No atlas data | NOT ASSESSED |

### Table 6 — Evidence support: 0064 LA-BLA-BMA-PA Glut_5 [CS20230722_SUPT_0064]

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata | ATLAS_METADATA | PARTIAL | region_fraction_100um=0.881; Dkk3 at 81.6th percentile, present in all child clusters | CCN20230722 |

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster / supertype | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---|---|---|---|
| 0245 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0245] | 0064 LA-BLA-BMA-PA Glut_5 | 1093 | ⚪ UNCERTAIN | Dkk3 pct 0.968; region_fraction_100um 0.703 | See below |
| 0248 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0248] | 0064 LA-BLA-BMA-PA Glut_5 | 254 | ⚪ UNCERTAIN | Dkk3 pct 0.677; region_fraction_100um 0.828 | Eliminated: Dkk3 expression lower than 0245 and 0250; insufficient to distinguish |
| 0250 LA-BLA-BMA-PA Glut_6 [CS20230722_CLUS_0250] | 0065 LA-BLA-BMA-PA Glut_6 | 96 | ⚪ UNCERTAIN | Dkk3 pct 0.989; region_fraction_100um 0.764 | See below |
| 0064 LA-BLA-BMA-PA Glut_5 [CS20230722_SUPT_0064] | — (supertype) | 1803 | ⚪ UNCERTAIN | Dkk3 pct 0.816; region_fraction_100um 0.881; all child clusters covered | See below |
| 0065 LA-BLA-BMA-PA Glut_6 [CS20230722_SUPT_0065] | — (supertype) | 1025 | ⚪ UNCERTAIN | Dkk3 pct 0.868; region_fraction_100um 0.719 | Eliminated: supertype-level only; no NT assertion; less specific than best child cluster 0250 |
| 0063 LA-BLA-BMA-PA Glut_4 [CS20230722_SUPT_0063] | — (supertype) | 2700 | ⚪ UNCERTAIN | Dkk3 pct 0.316 (APPROXIMATE); region_fraction_100um 0.634 | Eliminated: Dkk3 expression at 31.6th percentile, below expected enrichment threshold |
| 0061 LA-BLA-BMA-PA Glut_2 [CS20230722_SUPT_0061] | — (supertype) | 6385 | ⚪ UNCERTAIN | Dkk3 pct 0.632; region_fraction_100um 0.766 | Eliminated: broad supertype with moderate Dkk3; no specificity advantage over better cluster-level candidates |
| 0142 L2/3 IT PIR-ENTl Glut_1 [CS20230722_CLUS_0142] | 0039 L2/3 IT PIR-ENTl Glut_1 | 595 | ⚪ UNCERTAIN | Dkk3 pct 0.591; region primarily piriform/entorhinal | Eliminated: wrong anatomical context — cluster localises to piriform cortex and entorhinal cortex, not BLA |
| 0201 MEA Slc17a7 Glut_2 [CS20230722_CLUS_0201] | 0056 MEA Slc17a7 Glut_2 | 341 | ⚪ UNCERTAIN | Dkk3 pct 0.054; region medial amygdala | Eliminated: medial amygdalar nucleus, not basolateral; Dkk3 at 5.4th percentile |
| 0007 L5/6 IT TPE-ENT Glut_1 [CS20230722_SUPT_0007] | — (supertype) | 2080 | ⚪ UNCERTAIN | Dkk3 pct 0.895; region_fraction_100um 0.112 | Eliminated: region fraction in amygdala is 11.2% — primary distribution is isocortex and entorhinal cortex, not BLA |

</details>

---

### 0245 LA-BLA-BMA-PA Glut_5 · ⚪ UNCERTAIN

Atlas atlas metadata places cluster [CS20230722_CLUS_0245] in the Basolateral amygdalar nucleus [MBA:295], with 70.3% of cells within 100 µm of this region (strict fraction 42.1%). The cluster belongs to supertype 0064 LA-BLA-BMA-PA Glut_5, encompassing glutamatergic neurons across the lateral, basal, basomedial, and posterior amygdala — a grouping consistent with the basal nucleus location of the classical type.

**Supporting evidence**
- Cluster location falls within the Basolateral amygdalar nucleus [MBA:295] (region_fraction_100um = 0.703), consistent with the established basal amygdala locus of extinction neurons [1][2][3].
- *Dkk3* expression is 7.78 (cohort percentile 0.968) — the highest within-BLA-glutamatergic Glut_5 cluster, consistent with McCullough et al.'s identification of *Dkk3* as one of the genes most strongly upregulated in the *Thy1*-expressing Fear-Off population of the BLA [3].

**Marker evidence provenance**
- *Dkk3* was identified by RNA sequencing of behaviourally characterised, optogenetically validated Fear-Off neurons (McCullough et al. 2016 [3]); the approach used Thy1-eNpHR, Thy1-Cre, and Thy1-eYFP lines with post-hoc bulk RNA-seq, providing transcriptomic rather than single-cell resolution.
- *Ntsr2*, *Rspo2*, *Wnt7a*, and *Thy1* — the four other defining markers — are absent from atlas precomputed expression for this cluster; marker cross-check for these genes is not possible without running annotation transfer against a dataset that includes them.
- ⚠ Atlas annotation/expression discrepancy: *Ntsr2* is stated as defining in the classical node based on McCullough et al. [3] but is unavailable in the WMBv1 precomputed expression store for this cluster; the extent to which *Ntsr2* would differentiate among LA-BLA-BMA-PA Glut supertypes is unknown.

**Concerns**
- Only one of five defining markers can be assessed against the atlas; the mapping rests on *Dkk3* alone.
- The Glut_5 supertype encompasses multiple distinct cluster-level populations (including 0245 and 0248), raising the possibility that the classical type spans more than one atlas cluster, or maps to a minor subpopulation not clearly resolved at this resolution.
- Strict region fraction (0.421) indicates that fewer than half of the cells in this cluster fall strictly within the basolateral amygdala annotation boundary; the broader cortical subplate (MBA:703) accounts for the majority of painted cells.

**What would upgrade confidence**
- Annotation transfer using a dataset containing the extinction neuron marker panel (*Ntsr2*, *Rspo2*, *Wnt7a*, *Thy1*) against the WMBv1 taxonomy, in particular against *Thy1*-Cre or *Ntsr2*-Cre targeted single-cell data.
- Integration of *Ntsr2* precomputed expression into the WMBv1 taxonomy reference store.
- In situ validation (e.g., FISH or spatial transcriptomics) confirming co-expression of *Ntsr2*, *Dkk3*, and *Rspo2* in cells falling within atlas cluster 0245 [CS20230722_CLUS_0245] boundaries.

---

### 0250 LA-BLA-BMA-PA Glut_6 · ⚪ UNCERTAIN

Cluster [CS20230722_CLUS_0250] is a small cluster (96 cells) in the Glut_6 supertype, with a high BLA region fraction (region_fraction_100um = 0.764, strict = 0.620) and the highest *Dkk3* expression among all surveyed BLA glutamatergic clusters (8.81; cohort percentile 0.989). Its supertype (0065 LA-BLA-BMA-PA Glut_6 [CS20230722_SUPT_0065]) is distinct from the Glut_5 supertype containing 0245.

**Supporting evidence**
- *Dkk3* expression at cohort percentile 0.989 is the strongest signal in the entire BLA glutamatergic cohort, suggesting this cluster is unusually enriched for one of the key extinction neuron markers [3].
- Location is consistent with the basal amygdala: the top-3 100 µm region fractions are Cortical subplate [MBA:703], Basolateral amygdalar nucleus [MBA:295], and Basolateral amygdalar nucleus, anterior part [MBA:303].

**Marker evidence provenance**
- Same limitations as 0245: *Dkk3* is the only assessable marker; *Ntsr2*, *Rspo2*, *Wnt7a*, and *Thy1* lack precomputed atlas expression for this cluster.
- ⚠ The very small cell count (n = 96) raises the possibility that this cluster may represent a subpopulation, a technical artefact, or a rare cell state rather than a discrete cell type at the resolution of the classical type.

**Concerns**
- n = 96 is substantially smaller than cluster 0245 (n = 1,093); whether this reflects genuine biological rarity or a clustering artefact is unknown.
- Belongs to a different Glut supertype (Glut_6 vs. Glut_5) than cluster 0245, indicating meaningful transcriptomic distance; whether both supertypes could correspond to the same classical type is not resolvable without broader marker data.
- Single-marker evidence (*Dkk3* only); all other defining markers not assessed.

**What would upgrade confidence**
- Annotation transfer targeting *Thy1*-labelled or *Ntsr2*-expressing BLA Fear-Off neuron data.
- Multiplexed FISH in the basal amygdala confirming whether cells at the 0250 spatial locus co-express *Ntsr2* and *Dkk3*.
- Examination of whether the Glut_5 and Glut_6 supertypes represent a single continuous cell population or genuinely distinct entities, using trajectory or pseudotime analysis.

---

### 0064 LA-BLA-BMA-PA Glut_5 · ⚪ UNCERTAIN

Supertype [CS20230722_SUPT_0064] (n = 1,803 cells) encompasses the cluster-level Glut_5 population of the LA-BLA-BMA-PA grouping, including cluster 0245. It has the highest BLA region fraction among all supertype-level candidates (region_fraction_100um = 0.881; strict = 0.716), and *Dkk3* expression at cohort percentile 0.816 with child-cluster coverage of 1.000, indicating uniform *Dkk3* enrichment across all constituent clusters.

**Supporting evidence**
- BLA localisation is the most coherent among all supertype candidates: 88.1% of cells within 100 µm of the basolateral amygdalar nucleus.
- Uniform *Dkk3* enrichment across all child clusters (coverage 1.000) means the defining marker signal is not restricted to one child cluster, consistent with *Dkk3* being a genuine feature of the supertype rather than a cluster-specific outlier.

**Subcluster concordance note.** Within supertype 0064, cluster 0245 shows substantially higher *Dkk3* expression (7.78; pct 0.968) than cluster 0248 (4.98; pct 0.677), suggesting the extinction neuron signal may be concentrated in the 0245 cluster if the classical type is biologically more discrete. A broadMatch to the supertype is more appropriate here than an exactMatch, given the heterogeneity visible at cluster level.

**Marker evidence provenance**
- Supertype-level NT is not asserted in the CCN20230722 taxonomy (NOT ASSESSED); glutamatergic identity of the classical node must be inferred from the cluster-level Glut designation of child clusters.
- ⚠ NT alignment is not formally confirmed at supertype level; curators should verify that all child clusters are annotated as glutamatergic before upgrading this edge.

**Concerns**
- Supertype-level edges reflect a broader relationship than cluster-level; a 1:n cardinality is implied.
- *Dkk3* coverage is uniform but expression value is lower than in cluster 0245 or 0250, reflecting aggregation across child clusters.
- All four remaining defining markers (Ntsr2, Rspo2, Wnt7a, Thy1) are absent from precomputed expression.

**What would upgrade confidence**
- Resolution of the cluster-level assignment (0245 vs. 0248) through annotation transfer or spatial validation.
- Addition of *Ntsr2*, *Rspo2*, *Wnt7a*, and *Thy1* to the WMBv1 precomputed expression store for this supertype.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The basal amygdala extinction neuron is defined as a glutamatergic principal neuron of the basal nucleus of the amygdala [UBERON:0002887], characterised by *Thy1*/*Ntsr2* expression, reciprocal mPFC connectivity, and selective activation during fear extinction. Definition follows McCullough et al. 2016 (PMID:27767183), Cardenas et al. 2019 (PMID:31193505), and Carrere & Alexandre 2015 (PMID:25852499).

**Atlas mapping query.** Candidate atlas nodes were drawn from CCN20230722 (Allen Brain Cell Atlas WMBv1). The candidate set was retrieved at rank 0 (cluster) and rank 1 (supertype) by querying for glutamatergic cell types within the basolateral amygdalar nucleus [MBA:295] region. Five cluster-level and five supertype-level candidates were returned (cohort size = 5 at each rank).

**Property alignment.** Neurotransmitter type was assessed by prefix matching against atlas NT annotations. Anatomical location was assessed against region fraction metrics (region_fraction_100um and strict region_fraction). Marker alignment was assessed using precomputed expression values from the WMBv1 expression store where available; genes absent from the store are recorded as NOT_ASSESSED.

**Annotation transfer.** No annotation transfer runs were performed for this node. A MapMyCells-based annotation transfer experiment is proposed as a follow-up (see Discussion).

**Atlas data sources.** CCN20230722 (Allen Brain Cell Atlas WMBv1); region annotations from Allen Mouse Brain Atlas (MBA) ontology.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0245 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0248 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0250 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0064 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0065 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0063 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0061 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0142 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0201 | ATLAS_METADATA | PARTIAL | CCN20230722 |
| edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0007 | ATLAS_METADATA | PARTIAL | CCN20230722 |

*Generated by evidencell `a4a555f` at 2026-06-16T11:53:30+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate and caveats summary

**Primary mapping:** Basal amygdala extinction neuron → 0245 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0245] at UNCERTAIN confidence. The mapping is supported by consistent BLA localisation and elevated *Dkk3* expression (96.8th percentile in the BLA glutamatergic cohort), but rests on a single marker of five defined for the classical type. Cluster 0250 [CS20230722_CLUS_0250] offers an even stronger *Dkk3* signal (98.9th percentile) in a smaller cluster, and may warrant equal priority in follow-up experiments. Supertype 0064 [CS20230722_SUPT_0064] represents the broader grouping if the classical type proves to be distributed across multiple Glut_5 child clusters.

The key limitation is not inherent ambiguity between atlas clusters but the absence of four of five defining markers from atlas precomputed expression. Resolution depends on adding *Ntsr2*, *Rspo2*, *Wnt7a*, and *Thy1* expression to the taxonomy reference store or running annotation transfer against a behaviourally characterised Fear-Off cell dataset.

*(note: The mapping of this node stands in explicit contrast to the basal amygdala fear neuron, which is its functional counterpart in the same nucleus. If a confident mapping is established for fear neurons in the same LA-BLA-BMA-PA Glut supertype, the extinction neuron mapping can be assessed by examining whether the two classical types occupy distinct atlas clusters within that supertype.)*

### Proposed experiments

1. Run annotation transfer (MapMyCells) against a dataset derived from *Thy1*-Cre or *Ntsr2*-Cre BLA Fear-Off neurons, comparing source labels to CCN20230722 at cluster resolution for clusters 0245 [CS20230722_CLUS_0245] and 0250 [CS20230722_CLUS_0250].
2. Add *Ntsr2*, *Rspo2*, *Wnt7a*, and *Thy1* precomputed expression to the WMBv1 taxonomy reference store using `just add-expression`, then re-run the mapping to assess whether these markers discriminate between Glut_5 and Glut_6 supertypes.
3. Apply multiplexed FISH (e.g., RNAscope) for *Ntsr2*, *Dkk3*, and *Rspo2* in basal amygdala sections to confirm whether cells at the spatial locus of cluster 0245 co-express all three markers.
4. Examine whether the *Thy1*-eNpHR/Cre/eYFP-labelled Fear-Off population of McCullough et al. [3] maps preferentially to the Glut_5 vs. Glut_6 supertype using published snRNA-seq datasets from the basolateral amygdala.

### Open questions

1. Does the basal amygdala extinction neuron correspond to one atlas cluster (most likely 0245 or 0250) or span multiple Glut_5/Glut_6 clusters?
2. What is the *Ntsr2* expression profile across LA-BLA-BMA-PA glutamatergic supertypes in WMBv1 — is it enriched in Glut_5, Glut_6, or both?
3. Are *Rspo2*, *Wnt7a*, and *Thy1* present in WMBv1 precomputed expression for any BLA glutamatergic cluster, and if so, do they converge on the same cluster as *Dkk3*?
4. Is there a distinct atlas cluster that corresponds to the complementary fear neuron population, and does it neighbour the extinction neuron cluster within the Glut_5 or Glut_6 supertype?

---

## References

[1] Carrere & Alexandre 2015 · PMID:25852499 · DOI:10.3389/fnsys.2015.00041
[2] Cardenas et al. 2019 · PMID:31193505 · DOI:10.1016/j.ynstr.2019.100163
[3] McCullough et al. 2016 · PMID:27767183 · DOI:10.1038/ncomms13149
[4] Hochgerner et al. 2023 · PMID:37884748 · DOI:10.1038/s41593-023-01469-3
[5] Totty et al. 2025 · PMID:40961182 · DOI:10.1126/sciadv.adw1029

---

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0245 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Cluster 0245 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0245] is the
    top-ranked BLA glutamatergic cluster; Dkk3 expression is at the 96.8th cohort
    percentile (val=7.78) and region_fraction_100um=0.703 is consistent with the basal
    amygdala location of the classical type. However, only 1 of 5 defining markers is
    assessable in the atlas; Ntsr2, Rspo2, Wnt7a, and Thy1 all lack precomputed
    expression data, precluding a confident mapping at this time.
  reconciliation_note: >
    Annotation transfer against Thy1-Cre or Ntsr2-Cre BLA Fear-Off neuron data is the
    primary path to upgrading confidence. Adding Ntsr2 precomputed expression to the
    taxonomy reference store would allow direct marker cross-check against all candidate
    clusters.
  caveats:
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Four of five defining markers (Ntsr2, Rspo2, Wnt7a, Thy1) are absent from
        WMBv1 precomputed expression for this cluster; the mapping rests on Dkk3 alone.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Strict region fraction is 0.421; fewer than half of cluster cells fall within
        the canonical basolateral amygdala annotation boundary.
  proposed_experiments:
    - Annotation transfer using Thy1-Cre or Ntsr2-Cre BLA Fear-Off neuron
      source data to assess F1 against cluster 0245 [CS20230722_CLUS_0245].
    - Add Ntsr2, Rspo2, Wnt7a, Thy1 precomputed expression to WMBv1 reference store
      using just add-expression, then re-score this edge.
    - Multiplexed FISH for Ntsr2 + Dkk3 + Rspo2 in basal amygdala to confirm
      co-expression in cells at the 0245 spatial locus.
  unresolved_questions:
    - Whether the extinction neuron maps to a single cluster (0245) or is distributed
      across multiple Glut_5 child clusters within supertype 0064.
    - Whether Ntsr2 expression in WMBv1 is enriched in the Glut_5 vs. Glut_6 supertype.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0248 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Cluster 0248 LA-BLA-BMA-PA Glut_5 [CS20230722_CLUS_0248] shows consistent
    BLA localisation (region_fraction_100um=0.828) and Dkk3 expression at the 67.7th
    cohort percentile (val=4.98), but is ranked below 0245 and 0250 on both Dkk3
    enrichment and discovery score; insufficient to warrant a distinct full assessment.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0250 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.23
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Cluster 0250 LA-BLA-BMA-PA Glut_6 [CS20230722_CLUS_0250] has the
    highest Dkk3 expression of any surveyed BLA glutamatergic cluster (val=8.81;
    cohort percentile 0.989) and a consistent BLA location (region_fraction_100um=0.764).
    Its small cell count (n=96) and membership in a different supertype (Glut_6 vs. Glut_5)
    from the primary candidate 0245 introduce uncertainty; all four remaining defining
    markers are not assessable.
  caveats:
    - caveat_type: LOW_CELL_COUNT
      description: >
        Only 96 cells; may represent a rare cell state or technical artefact rather than
        a discrete cell type.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Belongs to Glut_6 supertype rather than Glut_5; whether both supertypes could
        represent the same classical type is unresolved.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Ntsr2, Rspo2, Wnt7a, and Thy1 absent from precomputed expression for this cluster.
  proposed_experiments:
    - Annotation transfer using Fear-Off neuron source data to compare F1 between clusters
      0245 and 0250 at cluster resolution.
    - Spatial transcriptomics to determine whether Ntsr2+ Dkk3+ cells at the basal amygdala
      locus align with the 0250 cluster spatial footprint.
  unresolved_questions:
    - Whether Glut_5 and Glut_6 supertypes represent genuinely distinct cell populations
      or a continuum within the basal amygdala glutamatergic compartment.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0142 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Cluster 0142 L2/3 IT PIR-ENTl Glut_1 [CS20230722_CLUS_0142] localises
    primarily to piriform cortex and entorhinal cortex (strict region_fraction=0.384 in
    basolateral amygdala), not the basal nucleus; anatomical context is incompatible with
    the classical type definition.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_CLUS_0201 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.03
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Cluster 0201 MEA Slc17a7 Glut_2 [CS20230722_CLUS_0201] is a medial
    amygdalar nucleus cluster; Dkk3 expression is at the 5.4th cohort percentile
    (val=0.59), and strict region_fraction in BLA is only 0.345. Incompatible with
    the basal amygdala location and marker profile of the classical type.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0065 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Supertype 0065 LA-BLA-BMA-PA Glut_6 [CS20230722_SUPT_0065] contains
    cluster 0250 as its best child; a supertype-level edge is less specific and not
    preferred over the cluster-level 0250 edge given no additional evidence at supertype
    resolution. NT not asserted at supertype level.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0064 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.20
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:WEAKEST] Supertype 0064 LA-BLA-BMA-PA Glut_5 [CS20230722_SUPT_0064] has the
    highest BLA region fraction of all candidates (region_fraction_100um=0.881) and
    uniform Dkk3 enrichment across all child clusters (val=5.47; cohort percentile 0.816;
    child-cluster coverage 1.000), consistent with the extinction neuron marker profile.
    A broadMatch relationship is more appropriate than exactMatch because the supertype
    encompasses at least two child clusters with distinct Dkk3 levels, and NT is not
    asserted at supertype level.
  reconciliation_note: >
    If annotation transfer resolves the extinction neuron to a specific child cluster
    within this supertype (most likely 0245), this supertype edge should be demoted to
    a secondary record.
  caveats:
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        The supertype encompasses clusters with substantially different Dkk3 enrichment
        (0245 at pct 0.968 vs. 0248 at pct 0.677), suggesting internal heterogeneity.
    - caveat_type: NT_PREDICTION_UNCERTAIN
      description: >
        NT identity is not formally asserted at supertype level in CCN20230722.
    - caveat_type: NO_DISCRIMINATING_MARKER
      description: >
        Ntsr2, Rspo2, Wnt7a, and Thy1 absent from precomputed expression at supertype level.
  proposed_experiments:
    - Annotation transfer to resolve cluster-level identity within this supertype.
    - Add Ntsr2 precomputed expression to supertype-level taxonomy nodes to enable
      marker cross-check.
  unresolved_questions:
    - Whether the extinction neuron corresponds to one (0245) or multiple child clusters
      within this supertype.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0063 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Supertype 0063 LA-BLA-BMA-PA Glut_4 [CS20230722_SUPT_0063] shows only
    APPROXIMATE Dkk3 alignment (val=2.01; cohort percentile 0.316) and a low strict
    region fraction (0.328); inconsistent with the extinction neuron marker profile.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0061 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Supertype 0061 LA-BLA-BMA-PA Glut_2 [CS20230722_SUPT_0061] is a large,
    broad supertype (n=6,385) with moderate Dkk3 enrichment (cohort percentile 0.632);
    no specificity advantage over cluster-level candidates 0245 or 0250, and NT is not
    asserted at supertype level.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basal_amygdala_extinction_neuron_to_CS20230722_SUPT_0007 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.02
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:1"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:CUT] Supertype 0007 L5/6 IT TPE-ENT Glut_1 [CS20230722_SUPT_0007] localises
    predominantly to isocortex and entorhinal cortex (region_fraction_100um=0.112 in
    the BLA region); anatomical context is incompatible with the basal amygdala classical
    type despite elevated Dkk3 expression (cohort percentile 0.895 in its own regional
    context).
```
<!-- verdict-block-end -->
