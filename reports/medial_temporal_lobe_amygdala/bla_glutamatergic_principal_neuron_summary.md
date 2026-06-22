# Basolateral amygdala glutamatergic principal neuron — CCN20230722 Mapping Report
*2026-06-22 · Source: `/Users/andrea/Documents/GitHub/evidencell/kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Glutamatergic principal neurons constitute the dominant excitatory cell class of the basolateral amygdala (BLA), accounting for approximately 70–85% of the neuronal population in the lateral and basal nuclei [1][5][6][7][8][9]. The BLA is a cortical-like structure in which these projection cells bear pyramidal morphology with spiny dendrites and release glutamate via vesicular glutamate transporter type 1 (VGluT1/Slc17a7) [7][8][9]. Mapping these neurons to a reference single-cell transcriptomic atlas is essential for integrating the rich physiological, connectivity, and behavioural literature on BLA principal cells with high-resolution molecular taxonomy and, ultimately, for enabling cross-study comparisons of circuit-level findings.

> "Based on the cell types, their connectivity features, and developmental characteristics, the BLA is a cortical structure. Accordingly, glutamatergic excitatory projection cells expressing vesicular glutamate transporter type 1 (VGluT1; (Andrási et al., 2017) are the most numerous neurons in this amygdala region (80-85%; (Vereczki et al., 2021). The dendrites of the principal cells (PC) are densely decorated with spines and their axon arborizes within the nucleus, giving rise to local collaterals, but they also project to other amygdala regions and remote cortical and/or subcortical areas (Sah et al., 2003)."
> — Hájos 2021, Classical neuron classes across amygdala subdivisions · [7] <!-- quote_key: 235382885_2970aa11 -->

### Cell Ontology mapping

The classical node carries a broad match to **CL:0000598** (pyramidal neuron) — this term is broader than the BLA principal neuron concept and has been auto-proposed pending expert review. No Cell Ontology term currently covers the BLA glutamatergic principal neuron specifically — this type is a candidate for a new CL term.

---

### Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] (lateral and basal nuclei) | [1][2][3][4] |
| Neurotransmitter | Glutamatergic | [5][1][6] |
| Defining markers | Slc17a7 (VGluT1), Camk2a | [7][8][9][7][8] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | CL:0000598 (broad match; requires review) | — |

<details>
<summary>Per-property literature support</summary>

**Soma location.** The BLA comprises the lateral and basolateral (basal) nuclei together, occupying the deep laterobasal group of the amygdaloid complex [1][2][3][4]. Multiple reviews describe the lateral and basal nuclei as the core of the BLA [1][2].

**Neurotransmitter.** Approximately 70–85% of BLA neurons are glutamatergic principal cells; GABAergic interneurons constitute the remainder [5][6]. The BLA is explicitly a cortical-like structure containing "glutamatergic pyramidal neurons and GABAergic interneurons" [6].

> "In the basolateral group, approximately 70% of neurons are thought to be glutamatergic (pyramidal, spiny, or class I neurons)."
> — Ignacio et al. 2014, Amygdala organization and principal cellular classes · [5] <!-- quote_key: 1229611_70584dfd -->

> "It is a cortical-like structure and contains glutamatergic pyramidal neurons and GABAergic interneurons."
> — Polepalli et al. 2020, Amygdala organization and principal cellular classes · [6] <!-- quote_key: 220930580_130f4111 -->

**Slc17a7 (VGluT1).** BLA principal cells express vesicular glutamate transporter type 1 (VGluT1/Slc17a7), the defining transcript-level marker of cortical-type glutamatergic neurons and the basis for distinguishing them from VGluT2-expressing populations [7][8][9]. Hájos 2021 directly attributes VGluT1 expression to BLA excitatory projection cells [7].

**Camk2a.** Calcium/calmodulin-dependent protein kinase II alpha (CaMKII-alpha) is a classical marker of cortical-type excitatory neurons; its expression in BLA principal cells parallels its well-established role in cortical pyramidal neurons and has been used as a positive cell-type marker in BLA optogenetic studies [7][8].

**Morphology (contextual).** BLA principal cells resemble cortical pyramidal neurons: spiny dendrites with pyramidal-like soma geometry in most, though lateral amygdala glutamatergic neurons can lack a clear apical/basal dendritic polarity. *(note: morphological heterogeneity between LA and BA subdivision principal cells is well established.)*

> "Its main nuclei, the lateral and the basolateral nuclei are known as the basolateral amygdala (BLA) and mostly contain projection neurons of pyramidal type, synthesizing glutamate."
> — Veinante et al. 2013, Amygdala organization and principal cellular classes · [1] <!-- quote_key: 15449738_4bbaac69 -->

**Notes.** The classical node notes capture an important heterogeneity: dendritic field extent varies (small vs. large neurons), and the type is referred to in the literature variably as pyramidal, spiny, or class I neurons. This population-level heterogeneity predicts atlas-side distribution across multiple supertypes rather than concentration in a single cluster.

</details>

---

## Results

Atlas metadata places three dedicated LA-BLA-BMA-PA Glut supertypes (0064, 0065, 0061) within BLA territory with high region fractions and consistent Slc17a7 and Camk2a expression, collectively providing the best molecular and spatial match to the classical BLA glutamatergic principal neuron. No single supertype captures the full population; the classical type distributes across at least three to four atlas supertypes within the same subclass, consistent with the known morphological and projection-target heterogeneity of BLA principal cells.

### Property alignment — 0064 LA-BLA-BMA-PA Glut_5 [CS20230722_SUPT_0064] · MODERATE

**Table 1 — Property comparison**

| Property | Classical node | Atlas supertype 0064 | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glut (LA-BLA-BMA-PA Glut subclass) | CONSISTENT |
| Soma location | Basolateral amygdala [UBERON:0002887] | Cortical subplate [MBA:703] / Basolateral amygdalar nucleus [MBA:295] / BLA anterior [MBA:303]; region_fraction_100um = 0.881 | CONSISTENT |
| Slc17a7 | Defining marker | val = 10.00; cohort_pct = 0.895 | CONSISTENT |
| Camk2a | Defining marker | val = 9.99; cohort_pct = 0.684 | CONSISTENT |

**Table 2 — Evidence support**

| Evidence type | Direction | Summary |
|---|---|---|
| ATLAS_METADATA (Zhuang/Yao) | PARTIAL | region_fraction_100um = 0.881 (highest in BLA Glut cohort); strict region_fraction = 0.716 |
| Precomputed expression | CONSISTENT | Slc17a7 val 10.00 (90th cohort percentile); Camk2a val 9.99 (68th cohort percentile) |

**Subcluster concordance note.** Supertype 0064 (1,803 cells) belongs to the LA-BLA-BMA-PA Glut subclass. Its high region_fraction_100um of 0.881 indicates that approximately 88% of cells painted within a 100 µm radius fall in BLA territory, making it the most BLA-enriched supertype in the cohort. Precomputed Slc17a7 expression at the 90th cohort percentile is the strongest Slc17a7 signal among all BLA Glut candidates, consistent with the transcript-level identity of BLA VGluT1+ principal cells. The spread across Cortical subplate [MBA:703], Basolateral amygdalar nucleus [MBA:295], and BLA anterior [MBA:303] reflects the known anterior-posterior extent of the BLA.

**Supporting evidence**
- Both defining markers (Slc17a7, Camk2a) are CONSISTENT with high cohort-relative expression values, satisfying the transcript-level marker expectation for BLA VGluT1+ principal neurons.
- Region fraction is the highest of any BLA Glut supertype in the atlas — SUPT_0064 is the most spatially BLA-specific candidate assessed.
- NT type (Glut) is unambiguous and consistent.
- 1,803 cells provide a robust, well-sampled supertype.

**Concerns**
- Evidence rests on atlas metadata alone; no annotation transfer data are available for this edge.
- NT type on node_b is not formally asserted in the taxonomy YAML (noted as "not asserted" in structured comparison), relying on the supertype naming convention.
- Absence of cluster-level marker data (no precomputed_expression for individual clusters within this supertype) means within-supertype heterogeneity in marker expression cannot be resolved.
- The classical BLA principal neuron population almost certainly distributes across multiple supertypes (see SUPT_0065 and SUPT_0061 below), so the 1:1 framing underestimates mapping complexity.

**What would upgrade confidence.** Annotation transfer using a dataset with well-characterised BLA principal neurons (e.g. a patch-seq dataset from BLA, or a dataset from a Camk2a-Cre × glutamatergic reporter line) targeting these supertypes directly would provide direct evidence. Precomputed expression at the cluster level within SUPT_0064 for Slc17a7 and Camk2a would confirm whether marker enrichment is uniform or concentrated in specific sub-clusters.

---

### 0065 LA-BLA-BMA-PA Glut_6 [CS20230722_SUPT_0065] · MODERATE

**Supporting evidence**
- Slc17a7 val = 9.69 (cohort_pct 0.763) — CONSISTENT; Camk2a val = 10.16 (cohort_pct 0.789) — the highest Camk2a value of any candidate assessed, consistent with a CaMKII-alpha-positive excitatory population.
- region_fraction_100um = 0.719; strict region_fraction = 0.485, placing the majority of cells within BLA territory.
- Primary MERFISH location shows Cortical subplate [MBA:703], Basolateral amygdalar nucleus [MBA:295], and Lateral amygdalar nucleus [MBA:131] — spatially appropriate for a BLA/LA principal neuron population.
- 1,025 cells; a moderately sized supertype.

**Concerns**
- Atlas metadata only; no annotation transfer evidence.
- Both Slc17a7 and Camk2a cohort percentiles are high but slightly below SUPT_0064, consistent with SUPT_0065 representing a partially distinct BLA or LA-enriched subpopulation.
- The prominence of Lateral amygdalar nucleus [MBA:131] in the location profile suggests this supertype may preferentially represent the LA subdivision rather than the basal amygdala proper.
- NT type similarly not formally asserted in the taxonomy YAML.

**What would upgrade confidence.** Direct annotation transfer from a BLA-specific transcriptomic dataset; resolution of within-supertype cluster composition relative to LA versus BA anatomical subdivision.

---

### 0061 LA-BLA-BMA-PA Glut_2 [CS20230722_SUPT_0061] · MODERATE

**Supporting evidence**
- region_fraction_100um = 0.766 (strong BLA enrichment); Slc17a7 cohort_pct = 0.526 (CONSISTENT); Camk2a cohort_pct = 0.526 (CONSISTENT).
- Largest cell count of the three primary BLA supertypes at 6,385 cells, suggesting SUPT_0061 captures a substantial fraction of the atlas BLA Glut population.
- Location profile includes Basolateral amygdalar nucleus, posterior part [MBA:311] — consistent with the posterior BLA subdivision where principal cells are prominent.

**Concerns**
- Atlas metadata only; no annotation transfer.
- Slc17a7 and Camk2a cohort percentiles (0.526) are at the cohort median rather than distinctly elevated, making marker confirmation less decisive than for SUPT_0064.
- The large cell count may reflect inclusion of neurons from BMA and PA territories (the supertype spans LA-BLA-BMA-PA), reducing BLA specificity compared to SUPT_0064.

**What would upgrade confidence.** Annotation transfer; subdivision-level expression data to determine whether Slc17a7 expression is uniformly distributed or concentrated in the BLA-fraction cells.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| Rank | Atlas target | Accession | Region fraction (100um / strict) | Slc17a7 (cohort_pct) | Camk2a (cohort_pct) | AT F1 | Verdict |
|---|---|---|---|---|---|---|---|
| 1 (rank1 cohort) | 0064 LA-BLA-BMA-PA Glut_5 | CS20230722_SUPT_0064 | 0.881 / 0.716 | 10.00 (0.895) | 9.99 (0.684) | — | **Primary candidate** |
| 2 (rank1 cohort) | 0065 LA-BLA-BMA-PA Glut_6 | CS20230722_SUPT_0065 | 0.719 / 0.485 | 9.69 (0.763) | 10.16 (0.789) | — | **Primary candidate** |
| 3 (rank1 cohort) | 0061 LA-BLA-BMA-PA Glut_2 | CS20230722_SUPT_0061 | 0.766 / 0.541 | 9.46 (0.526) | 9.79 (0.526) | — | **Primary candidate** |
| 4 (rank1 cohort) | 0063 LA-BLA-BMA-PA Glut_4 | CS20230722_SUPT_0063 | 0.634 / 0.328 | 9.06 (0.316) | 9.96 (0.658) | — | Eliminated (Slc17a7 below cohort median) |
| 5 (rank1, old) | 0005 IT EP-CLA Glut_3 | CS20230722_SUPT_0005 | 0.042–0.080 / low | — | — | SUPT F1=0.30 (3 cells) | Eliminated (wrong primary region; cortical/claustral type) |
| 6 (rank0 cohort) | 0018 IT EP-CLA Glut_3 | CS20230722_CLUS_0018 | 0.296 / 0.166 | — | — | CLUS F1=0.40 (2 cells) | Eliminated (child of cortical SUPT_0005; low BLA fraction) |
| 7 (rank0 cohort) | 0201 MEA Slc17a7 Glut_2 | CS20230722_CLUS_0201 | 0.621 / 0.345 | — | — | — | Eliminated (MEA supertype, not BLA) |
| 8 (rank0 cohort) | 0241 LA-BLA-BMA-PA Glut_4 | CS20230722_CLUS_0241 | 0.651 / 0.281 | — | — | — | Eliminated (cluster-level; no marker data; SUPT_0063 level preferred) |
| 9 (rank0 cohort) | 0142 L2/3 IT PIR-ENTl Glut_1 | CS20230722_CLUS_0142 | 0.646 / 0.384 | — | — | — | Eliminated (piriform/entorhinal type; not BLA) |
| 10 (rank0 cohort) | 0204 MEA Slc17a7 Glut_2 | CS20230722_CLUS_0204 | 0.245 / 0.132 | — | — | — | Eliminated (MEA type; low BLA fraction) |

</details>

---

## Methods

<details>
<summary>Methods detail</summary>

### Classical type definition

The BLA glutamatergic principal neuron is defined classically by soma location within the lateral and basal nuclei of the amygdala [UBERON:0002887], glutamatergic neurotransmitter identity, and expression of Slc17a7 (VGluT1) and Camk2a as molecular markers [7][8][9]. The type encompasses the heterogeneous population of pyramidal-like and non-pyramidal spiny excitatory neurons (class I neurons) that constitute approximately 70–85% of BLA neurons [5][6]. Morphological heterogeneity in dendritic field extent between small and large neurons, and between LA and BA subdivision neurons, is acknowledged.

### Atlas mapping query

Candidate atlas supertypes were identified by querying the CCN20230722 taxonomy for neurons meeting BLA region membership (MBA:295) and glutamatergic neurotransmitter identity. A cohort of 10 nodes was scored at both supertype (rank 1) and cluster (rank 0) levels. Discovery scores were based on region enrichment and precomputed marker expression for Slc17a7 and Camk2a where available.

### Property alignment

Two defining markers were assessed: Slc17a7 and Camk2a. Precomputed expression values (mean log-normalised counts from WMBv1 precomputed stats) were available for SUPT_0063, 0064, 0065, and 0061. Cohort percentiles were computed across the BLA Glut supertype cohort (n = 10). CONSISTENT was assigned where val was present and cohort percentile ≥ 0.5; APPROXIMATE where cohort percentile was between 0.25 and 0.5; NOT_ASSESSED where expression data were absent. NT type alignment was assessed by prefix match to the supertype name.

### Annotation transfer

One annotation transfer run was performed: **at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1** using MapMyCells local (cell_type_mapper v1.7.1). Input dataset: Hochgerner 2023 (ArrayExpress:E-MTAB-12096), naive neuronal cells only (fear-conditioned cells excluded), 7,777 cells after filtering from 55,514 total. Method: raw normalisation, 100 bootstrap iterations, bootstrap threshold 0.7. Source cluster VGLUT2-23-Nov_Gpr83 (3 cells mapped) produced low F1 scores across levels (class F1 = 0.002; subclass F1 = 0.21; supertype F1 = 0.30 to SUPT_0005; cluster F1 = 0.40 to CLUS_0018). These results did not meaningfully constrain the BLA-specific supertype candidates (SUPT_0061–0065) because the Hochgerner 2023 dataset likely underrepresents excitatory BLA principal neurons (42 VGLUT2 types vs 56 GABA types in the published taxonomy; source labels are Zeisel-style transcriptomic types, not classical morpho-electrophysiological types). The AT evidence is therefore uninformative for distinguishing among LA-BLA-BMA-PA supertypes and is not used in the primary confidence assessment.

### Atlas data sources

- MERFISH spatial data: Zhuang 2023 (PMID:37915112) and Yao 2024, as reported in CCN20230722 precomputed statistics.
- Precomputed expression: WMBv1 precomputed stats (atlas_pseudobulk_sha: b21ca985652fb25f9608f99005139a40757133a76fbe845ae5b175c5c26a447b).

### Anti-hallucination

All quote_keys, PMIDs, and accessions cited in this report have been verified against `references/medial_temporal_lobe_amygdala/references.json` and the facts file. No accessions or identifiers have been introduced from sources outside the facts file. Atlas accessions are cited only where they appear in `facts.edges`.

### Reproducibility

Facts file generated: 2026-06-22T11:48:12+00:00. Framework version: 11e0b89. KB graph: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`.

### Evidence base

| Edge | Evidence types | AT runs | Marker assessment |
|---|---|---|---|
| SUPT_0064 | ATLAS_METADATA (PARTIAL) | None | 2 of 2 CONSISTENT |
| SUPT_0065 | ATLAS_METADATA (PARTIAL) | None | 2 of 2 CONSISTENT |
| SUPT_0061 | ATLAS_METADATA (PARTIAL) | None | 2 of 2 CONSISTENT |
| SUPT_0063 | ATLAS_METADATA (PARTIAL) | None | 1 CONSISTENT, 1 APPROXIMATE |
| SUPT_0005 | ATLAS_METADATA (SUPPORT + AGAINST), ANNOTATION_TRANSFER (PARTIAL) | at_run_20260609 | 0 of 2 ASSESSED |
| CLUS_0018 | ATLAS_METADATA (PARTIAL), ANNOTATION_TRANSFER (PARTIAL) | at_run_20260609 | 0 of 2 ASSESSED |
| CLUS_0201, 0204, 0241, 0142 | ATLAS_METADATA (PARTIAL) | None | 0 of 2 ASSESSED |

</details>

---

## Discussion

### Best candidate and caveats

**Primary mapping:** Basolateral amygdala glutamatergic principal neuron maps most broadly to the LA-BLA-BMA-PA Glut subclass of CCN20230722, with the individual supertype 0064 LA-BLA-BMA-PA Glut_5 [CS20230722_SUPT_0064] providing the strongest single-candidate alignment: the highest BLA region fraction in the cohort (region_fraction_100um = 0.881), Slc17a7 expression at the 90th cohort percentile, and consistent Camk2a expression. However, the classical BLA principal neuron is a broad, heterogeneous population, and the atlas distributes it across at least three additional high-BLA-fraction supertypes (SUPT_0065, SUPT_0061, and to a lesser degree SUPT_0063). The overall mapping is therefore better described as 1:n (one classical type → multiple atlas supertypes), with SUPT_0064 as the best individual representative.

Evidence is currently limited to atlas metadata (region fraction and precomputed expression); no annotation transfer experiment using a well-characterised BLA excitatory cell dataset constrains the supertype-level attribution. This limits confidence to MODERATE for all individual supertype candidates.

### Proposed experiments and follow-ups

1. **Annotation transfer with a BLA-targeted excitatory cell dataset.** A dataset in which BLA principal neurons are labelled by a Camk2a-Cre or Slc17a7-Cre driver, or from a patch-seq study with morphological recovery, would enable direct AT mapping to SUPT_0061–0065 and resolve which supertypes receive the strongest signal. The Hochgerner 2023 dataset used in this run is not suitable for this purpose given its sparse VGLUT2 excitatory cell representation.

2. **Precomputed expression at the cluster level within SUPT_0064 and SUPT_0065.** Slc17a7 and Camk2a values are available at the supertype level; cluster-level values would reveal whether marker enrichment is uniform (supporting a single-population interpretation) or heterogeneous (supporting further subdivision).

3. **Hypothesis-mode assessment of SUPT_0061 and SUPT_0063.** These two supertypes share the LA-BLA-BMA-PA supertype group but were not included in the original rank-1 discovery run. Formal property comparison including anatomy sub-region (LA vs. BA vs. BMA) would clarify whether they represent anterior, posterior, or subdivision-specific BLA populations.

4. **Resolve the SUPT_0005 / CLUS_0018 IT EP-CLA signal.** The single AT experiment mapped VGLUT2-23-Nov_Gpr83 (3 cells) to SUPT_0005/CLUS_0018 (IT EP-CLA Glut subclass) with low F1. This may reflect a cortical-like BLA subpopulation that is homologous to claustrum or endopiriform neurons — a possibility raised by the defining markers of SUPT_0005 (Abca8a, Npsr1, Adam33). Investigation of whether these IT EP-CLA cells mark a specific BLA subpopulation (possibly the anterior BLA neurons projecting to prefrontal cortex) would clarify whether a secondary cross-class edge is warranted.

### Open questions

1. Does the atlas separate the lateral (LA) and basal (BA) amygdala principal neuron populations into distinct supertypes within the LA-BLA-BMA-PA Glut group? The location profiles suggest LA cells may concentrate in SUPT_0065 (which shows prominent Lateral amygdalar nucleus [MBA:131] signal) while BA cells are more prominent in SUPT_0064. This subdivision-level resolution has functional relevance (LA is the primary sensory input nucleus; BA is the primary projection nucleus to central amygdala and striatum).

2. Is VGLUT2-23-Nov_Gpr83 (Hochgerner 2023) a genuine BLA principal neuron type or a misclassified / non-BLA excitatory type? Its mapping to the IT EP-CLA Glut subclass rather than the LA-BLA-BMA-PA Glut subclass raises this question. Resolution requires cell-type tracing in the Hochgerner 2023 dataset against BLA anatomical markers.

3. Does a cortical-type BLA subpopulation (IT EP-CLA) exist within the BLA, distinct from the classical principal neuron? Such cells have been proposed on developmental grounds (pallial amygdala divisions expressing Slc17a6 vs. Slc17a7) [9]. The finding from Fernández et al. 2025 that differential Slc17a6/Slc17a7 expression distinguishes BLA sub-domains at a coarse molecular level would predict that SUPT_0005 and related IT EP-CLA supertypes capture this minority population.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Veinante et al. 2013 | 25408902 | Soma location; NT type; morphology |
| [2] | Raudales et al. 2024 | 39012795 | Soma location; amygdala subdivision |
| [3] | Nolan et al. 2020 | 33015518 | Soma location |
| [4] | Zhu et al. 2025 | 40352758 | Soma location |
| [5] | Ignacio et al. 2014 | 25309888 | NT type; morphology; proportion |
| [6] | Polepalli et al. 2020 | 32802405 | NT type; morphology |
| [7] | Hájos 2021 | 34177472 | Slc17a7 marker; NT type |
| [8] | Wilson et al. 2015 | 26844236 | Slc17a7 marker; Camk2a marker |
| [9] | Fernández et al. 2025 | 40867603 | Slc17a7 marker; Slc17a6/Slc17a7 domain distinction |

---

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_SUPT_0064 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:CompositeMatching
  rationale: >
    [tier:STRONGEST] SUPT_0064 (LA-BLA-BMA-PA Glut_5) shows the highest BLA region_fraction_100um
    (0.881) and top-decile Slc17a7 expression (cohort_pct 0.895) among all BLA Glut candidates,
    with Camk2a also CONSISTENT; atlas metadata alone supports this mapping pending annotation
    transfer. The classical BLA glutamatergic principal neuron maps to multiple LA-BLA-BMA-PA Glut
    supertypes (1:n); SUPT_0064 is the best individual representative.
  reconciliation_note: >
    The BLA glutamatergic principal neuron population distributes across at least SUPT_0061,
    SUPT_0063, SUPT_0064, and SUPT_0065 in the atlas. No single supertype captures the full
    classical type. SUPT_0064 is the strongest individual candidate by both region fraction and
    Slc17a7 expression, but sister supertypes should be considered jointly in any downstream
    analysis. Annotation transfer from a BLA-targeted excitatory dataset is the priority experiment
    to resolve this 1:n ambiguity.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        Evidence is limited to atlas metadata (region fraction and precomputed expression); no
        annotation transfer experiment using a well-characterised BLA principal neuron dataset is
        available for this edge, limiting confidence to MODERATE.
    - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
      description: >
        The classical type population is broader than any single supertype; SUPT_0064 captures a
        portion of the BLA Glut population alongside SUPT_0061, 0063, and 0065. The 1:n mapping
        cardinality is the more accurate representation.
  proposed_experiments:
    - >
      Annotation transfer using a BLA excitatory cell dataset (e.g. Camk2a-Cre or Slc17a7-Cre
      driver line scRNA-seq from BLA) to SUPT_0061–0065 to directly determine which supertypes
      receive the strongest mapping signal.
    - >
      Precomputed expression at the cluster level within SUPT_0064 for Slc17a7 and Camk2a to
      confirm whether marker enrichment is uniform across this supertype or concentrated in
      specific sub-clusters.
  unresolved_questions:
    - >
      Does SUPT_0064 predominantly represent BA (basal amygdala) principal neurons, while SUPT_0065
      represents LA (lateral amygdala) principal neurons? The location profiles suggest this
      subdivision, which has functional implications.
    - >
      Are there precomputed expression values at cluster level within SUPT_0064 for Slc17a7 and
      Camk2a that would confirm within-supertype homogeneity?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_SUPT_0065 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.50
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:CompositeMatching
  rationale: >
    [tier:NEXT] SUPT_0065 (LA-BLA-BMA-PA Glut_6) shows strong Camk2a expression (cohort_pct 0.789,
    highest in cohort) and consistent Slc17a7 (cohort_pct 0.763), with region_fraction_100um 0.719
    placing most cells in BLA territory; atlas metadata supports a BLA principal neuron identity
    as part of the 1:n mapping alongside SUPT_0064.
  reconciliation_note: >
    Paired with SUPT_0064 as a co-primary candidate within the 1:n mapping. The LA prominence
    in the location profile (Lateral amygdalar nucleus [MBA:131] as third-highest count) suggests
    SUPT_0065 may preferentially represent LA rather than BA subdivision principal neurons,
    potentially complementing SUPT_0064. See SUPT_0064 reconciliation_note for shared context.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        Atlas metadata only; no annotation transfer. NT type on node_b is not formally asserted
        in the taxonomy YAML.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Lateral amygdalar nucleus [MBA:131] features prominently in the location profile; SUPT_0065
        may skew toward LA rather than BA subdivision, meaning it may not cover the full BLA
        principal neuron spatial extent.
  proposed_experiments:
    - >
      Annotation transfer from BLA-targeted excitatory cell dataset to SUPT_0065 alongside SUPT_0064
      to resolve LA vs. BA subdivision attribution.
    - >
      Comparison of defining cluster-level markers of SUPT_0065 vs. SUPT_0064 to determine whether
      the two supertypes differ in any molecular feature that maps to a known BLA principal
      neuron subtype distinction (e.g. projection target, firing pattern).
  unresolved_questions:
    - >
      Is SUPT_0065 specifically the LA subdivision principal neuron counterpart of SUPT_0064 (BA
      subdivision), or do the two supertypes overlap in the same nuclei and reflect a purely
      molecular subdivision without anatomical correspondence?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_SUPT_0061 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.45
  relationship: skos:closeMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:CompositeMatching
  rationale: >
    [tier:NEXT] SUPT_0061 (LA-BLA-BMA-PA Glut_2) has the largest cell count (6,385) and strong
    BLA region fraction (region_fraction_100um 0.766), with both Slc17a7 and Camk2a at cohort
    median (cohort_pct 0.526); the large cell population suggests it captures a substantial portion
    of the BLA Glut atlas representation, consistent with the classical type's numerical dominance.
  reconciliation_note: >
    Median-level cohort percentiles for both markers reduce differentiation from non-BLA Glut
    supertypes; the large cell count and high region fraction are the primary supporting signals.
    Part of the 1:n mapping alongside SUPT_0064 and SUPT_0065.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        Atlas metadata only; no annotation transfer. Marker expression cohort percentiles (0.526)
        are at the cohort median rather than distinctly elevated.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Posterior BLA location profile (BLA posterior [MBA:311] prominent) suggests SUPT_0061
        may skew toward posterior BA neurons. The large cell count may also reflect inclusion of
        BMA and PA neurons (the supertype spans LA-BLA-BMA-PA).
  proposed_experiments:
    - >
      Annotation transfer from BLA excitatory dataset to SUPT_0061 to determine whether this
      large supertype maps specifically to BLA principal neurons or receives signal from multiple
      amygdala subdivisions.
  unresolved_questions:
    - >
      Does the large cell count of SUPT_0061 (6,385) reflect a genuinely abundant BLA principal
      neuron subtype, or does it arise from the supertype spanning multiple amygdala subdivisions
      (LA, BLA, BMA, PA) with heterogeneous cell type composition?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_SUPT_0063 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] SUPT_0063 (LA-BLA-BMA-PA Glut_4) has Slc17a7 at cohort_pct 0.316 (APPROXIMATE,
    below cohort median) with strict region_fraction 0.328, making it the weakest of the four
    BLA Glut supertypes; insufficient evidence to assign a confident mapping above the 1:n parent.
  caveats:
    - caveat_type: SINGLE_DATASET
      description: >
        Atlas metadata only; Slc17a7 expression below cohort median reduces confidence in a
        VGluT1-positive BLA principal neuron identity for this supertype.
  proposed_experiments:
    - >
      Precomputed expression for Slc17a7 and Camk2a at cluster level within SUPT_0063 to determine
      whether the low cohort percentile reflects within-supertype heterogeneity or genuine
      lower Slc17a7 expression.
  unresolved_questions:
    - >
      Does SUPT_0063 represent a BMA-enriched or PA-enriched subpopulation of the LA-BLA-BMA-PA
      Glut group (its location profile shows Basomedial amygdalar nucleus [MBA:319] as third-
      highest location count), reducing its relevance to the BLA-specific classical type?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] SUPT_0005 (IT EP-CLA Glut_3) is a cortical/claustral supertype whose primary
    location is Cortical subplate and Olfactory areas; BLA cells represent only 4–8% of this
    supertype, and AT evidence (F1=0.30 at supertype, 3 cells mapped) is too weak and from
    too small a cell count to support a meaningful mapping.
  unresolved_questions:
    - >
      Does SUPT_0005 mark a genuine IT EP-CLA homologous subpopulation within BLA (anterior
      BLA neurons projecting to prefrontal cortex)? This would constitute a separate, minor
      edge rather than a match to the dominant BLA principal neuron.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_CLUS_0018 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] CLUS_0018 (IT EP-CLA Glut_3 cluster) is the best-F1 child of SUPT_0005 from the
    AT run (F1=0.40, 2 cells); BLA region fraction is low (0.296/0.166) and the cortical/claustral
    supertype context makes this an unlikely match to the dominant BLA principal neuron population.
  unresolved_questions:
    - >
      Curator should confirm removal or retention of this cluster-level edge — it duplicates
      the SUPT_0005 cortical-lineage story at cluster resolution without adding discriminating
      evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_CLUS_0201 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:NoCorrespondence
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] CLUS_0201 belongs to supertype 0056 MEA Slc17a7 Glut_2 (medial amygdala),
    not the BLA; Slc17a7 name inclusion in the supertype reflects medial amygdala Slc17a7+
    neurons which are a distinct population from BLA principal neurons.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_CLUS_0241 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  relationship: evidencell:UncertainRelationship
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] CLUS_0241 is a cluster within SUPT_0063 (LA-BLA-BMA-PA Glut_4); cluster-level
    assessment is premature without marker data, and the parent supertype SUPT_0063 is already
    weakly supported; no additional evidence justifies a cluster-level mapping at this stage.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_CLUS_0142 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:NoCorrespondence
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] CLUS_0142 (L2/3 IT PIR-ENTl Glut_1) belongs to the piriform/entorhinal cortex
    lineage, not BLA; presence of BLA cells in the 100 µm painted region reflects spatial
    proximity, not genuine cell type correspondence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bla_glutamatergic_principal_neuron_to_CS20230722_CLUS_0204 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.05
  relationship: evidencell:NoCorrespondence
  mapping_cardinality: "1:n"
  mapping_justification: semapv:UnspecifiedMatching
  rationale: >
    [tier:CUT] CLUS_0204 belongs to supertype 0056 MEA Slc17a7 Glut_2 (medial amygdala);
    region_fraction_100um of 0.245 is low and the top painted location is Cortical subplate
    [MBA:703] with Striatum [MBA:477] second — inconsistent with BLA principal neuron identity.
```
<!-- verdict-block-end -->
