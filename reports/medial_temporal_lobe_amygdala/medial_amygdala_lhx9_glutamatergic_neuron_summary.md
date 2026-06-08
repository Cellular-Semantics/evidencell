# Medial amygdala Lhx9+ ventral pallial-derived glutamatergic neuron — CCN20230722 Mapping Report
*2026-06-05 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The medial amygdala Lhx9+ ventral pallial-derived glutamatergic neuron is a minor, developmentally distinctive subpopulation within the medial amygdalar nucleus [UBERON:0002892]. Unlike the predominant GABAergic subpallial cells of the medial amygdala, these neurons derive from the ventral pallium and express the LIM-homeodomain transcription factor LHX9, which differentially marks the efferent projections regulating reproductive versus defensive behaviours [4]. Establishing which WMBv1 atlas cluster(s) capture this population is important for anchoring this developmentally defined subtype to the CCN20230722 transcriptomic taxonomy.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Medial amygdalar nucleus [UBERON:0002892] | [1] |
| NT type | Glutamatergic | [2][3] |
| Defining markers | Lhx9 | [1][4] |
| Negative markers | — | |
| Neuropeptides | — | |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Cross-species genoarchitecture of the extended amygdala; comparative developmental-origin mapping in avian and mammalian species · [1]
  > In addition to these cells, the medial amygdala includes a minor subpopulation of Lhx9 cells of ventral pallial origin
  > — Vicario et al. 2016, Medial and extended amygdala developmental-origin cell populations · [1] <!-- quote_key: 11582390_e268c719 -->

- **NT type (glutamatergic):** Review of mammalian/rodent medial amygdala mosaic composition; comparative neuroanatomy · [2]
  > the mammalian/rodent medial amygdala is a mosaic of GABAergic subpallial cells complemented by glutamatergic neuron types from extrinsic sources (ventral pallium, SPV, EmT).
  > — Gerlach & Wullimann 2021, Medial and extended amygdala developmental-origin cell populations · [2] <!-- quote_key: 231758452_9fd699d1 -->

- **NT type (glutamatergic; independent corroboration):** Amygdala principal neuron circuit review covering NT identity across amygdala nuclei · [3]
  > .the former includes BLA, CoA, BMA, and MeA, while the latter includes CeA and BST.Within the amygdala nuclei, PNs are exclusively glutamatergic in BLA, CoA, BMA, exclusively GABAergic in CeA, and predominantly GABAergic in MeA and BST.In rodents, there is also a population of glutamatergic pyramidal neurons (GLU PNs, derived from third ventricle neuroepithelium) that populates the BST, MeA, and hypothalamus (García-Moreno et al., 2010)(Huilgol et al., 2016).
  > — Raudales et al. 2024, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 271240390_b54d0b91 -->

- **Defining marker (Lhx9):** Sonic hedgehog fate-mapping study in mouse medial amygdala; Shh-Cre lineage tracing · [4]
  > the anatomical segregation of efferent projections that regulate reproductive or defensive behaviors is differentially marked by the LIM-containing homeodomain genes Lhx6 and Lhx9
  > — Carney et al. 2010, Background · [4] <!-- quote_key: 627853_c6aafc07 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: glutamatergic neuron [[CL:0000679](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000679)] (BROAD).

The Cell Ontology has no specific term for this population; CL:0000679 (glutamatergic neuron) is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas supertype was assessed; 0057 MEA Slc17a7 Glut_3 [CS20230722_SUPT_0057] is the proposed mapping at LOW confidence with a `skos:broadMatch` (1:n) relationship. The mapping rests solely on NT type and soma location concordance: the classical defining marker LHX9 is absent from SUPT_0057 atlas metadata and cannot be assessed — this is the direct reason broadMatch rather than exactMatch is the appropriate predicate.

### Mapping candidates table

**4a. Candidate overview**

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0057 MEA Slc17a7 Glut_3 [CS20230722_SUPT_0057] | 3,748 | 🔴 LOW | NT CONSISTENT · LHX9 NOT_ASSESSED | broadMatch 1:n |

*1 edge assessed; relationship type: `skos:broadMatch` (1:n).*

**4b. Property alignment — 0057 MEA Slc17a7 Glut_3 [CS20230722_SUPT_0057]**

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | Glutamatergic | Glut (Slc17a7 subclass) | not assessed | CONSISTENT |
| Soma location | Medial amygdalar nucleus [UBERON:0002892] | MBA:403 Medial amygdalar nucleus (region_fraction 0.588; SELF evidence; both Zhuang 2023 and Yao 2024 MERFISH) | not assessed | CONSISTENT |
| Lhx9 expression | Defining marker (TRANSCRIPT; fate-mapping Shh-Cre lineage tracing) | not present in atlas metadata (Trabd2b, Zic5, Dab1, Ntf3, Rassf3, Krt12); no precomputed expression data | not assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Zhuang 2023 MERFISH spatial placement | Atlas metadata | SUPPORT | MBA:403 cell_ratio 0.399; Slc17a7 subclass confirms glutamatergic identity | atlas-internal |
| Yao 2024 MERFISH spatial placement | Atlas metadata | SUPPORT | MBA:403 cell_ratio 0.619; glutamatergic assignment consistent with classical NT | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

### 0057 MEA Slc17a7 Glut_3 [CS20230722_SUPT_0057] · 🔴 LOW

**Why broadMatch, not exactMatch.** The classical definition of the medial amygdala Lhx9+ glutamatergic neuron rests on the defining marker LHX9, established by Shh-Cre fate-mapping [4] and comparative genoarchitecture [1]. CS20230722_SUPT_0057 carries six defining markers in the CCN20230722 atlas metadata (Trabd2b, Zic5, Dab1, Ntf3, Rassf3, Krt12); LHX9 is absent from this list, and no precomputed expression data is available for LHX9 at SUPT_0057 (local_stats: None). Without atlas-side LHX9 signal it is not possible to confirm that SUPT_0057 captures the Lhx9+ ventral pallial subpopulation specifically, rather than one of the other four MEA Slc17a7 Glut supertypes. Concordance on NT type and soma location alone is insufficient for exactMatch or closeMatch under the 2026-05-26 predicate rubric; `skos:broadMatch` (1:n) is assigned because SUPT_0057 is likely broader than this single minor subpopulation and may subsume multiple developmentally distinct MEA glutamatergic populations.

**Supporting evidence:**

- **NT type CONSISTENT.** Slc17a7 (VGLUT1) subclass assignment in CCN20230722 confirms SUPT_0057 as glutamatergic, concordant with the classical type's glutamatergic identity supported by two independent literature sources [2][3].
- **Soma location CONSISTENT.** MERFISH spatial data from Zhuang 2023 places CS20230722_SUPT_0057 predominantly in Medial amygdalar nucleus (MBA:403; cell_ratio 0.399); Yao 2024 MERFISH confirms the placement (cell_ratio 0.619), giving a combined region_fraction of 0.588. Among the five MEA Slc17a7 Glut supertypes in the discovery cohort (size 5; filters: region=MBA:403, nt_type=Glutamatergic), SUPT_0057 ranks first by region_fraction. Stage A discovery score = 1, tied with all cohort members at next_best_score = 1 — the cohort is differentiated only by region_fraction, not by marker evidence.

**Marker evidence provenance:**

- **Lhx9 (defining marker):** Evidence is transcript-level, from Shh-Cre lineage tracing in mouse medial amygdala [4] and cross-species comparative genoarchitecture [1]. No precomputed expression data for LHX9 is available at SUPT_0057, and LHX9 is absent from the CCN20230722 atlas metadata for this node. This is the single most consequential evidence gap: without LHX9 expression data across the five MEA Slc17a7 Glut supertypes, it is not possible to determine whether SUPT_0057 or a sibling supertype specifically hosts the Lhx9+ population. A targeted literature search for "Lhx9 medial amygdala mouse" or "LHX9 MEA single-cell" may surface existing transcript-level data that would resolve this without new experiments.

**Concerns:**

- **LHX9 NOT_ASSESSED (primary concern).** The classical defining marker LHX9 is absent from SUPT_0057 atlas metadata and no precomputed expression data is available. The mapping cannot be confirmed or refuted on marker grounds. This is the direct basis for the `skos:broadMatch` predicate rather than exactMatch or closeMatch.
- **Cohort tied on discovery score.** Stage A score = 1, tied across all five MEA Glutamatergic supertypes (next_best_score = 1, cohort_size = 5). SUPT_0057 is selected by highest region_fraction (0.588) alone — marker differentiation within the cohort is zero.
- **1:n cardinality.** The broadMatch 1:n reflects the possibility that multiple classical subtypes of MEA glutamatergic neurons (Lhx9+, EmT-derived, SPV-derived) are collapsed within SUPT_0057 or distributed across the five MEA Slc17a7 Glut supertypes. The Lhx9+ population is explicitly described as "a minor subpopulation" within the medial amygdala [1], making it unlikely to dominate a supertype of 3,748 cells without admixture.

**What would upgrade confidence:**

1. **Precomputed expression query for LHX9 across MEA Glut supertypes** — identifying which of the five supertypes expresses LHX9 above background would provide ATLAS_METADATA evidence; if SUPT_0057 is the highest-expressing, confidence upgrades to MODERATE (closeMatch with marker alignment) or higher.
2. **LHX9-ISH co-staining with SUPT_0057 defining markers (Trabd2b, Zic5, Dab1, Ntf3)** in mouse medial amygdala — direct co-expression test; if positive, LiteratureEvidence with marker_LHX9 CONSISTENT is added, supporting a closeMatch at MODERATE confidence.
3. **Targeted literature search** for "Lhx9 medial amygdala mouse transcriptomics" or "LHX9 MEA scRNA-seq" — may surface already-published data resolving LHX9 atlas distribution.
4. **Annotation transfer using a Lhx9+ fate-mapped or Lhx9-enriched MEA dataset** (if available in public repositories) against CCN20230722 at CLUSTER level — target F1 ≥ 0.75 to reach MODERATE confidence; would add AnnotationTransferEvidence to the KB.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The medial amygdala Lhx9+ ventral pallial-derived glutamatergic neuron is defined on the basis of CLASSICAL evidence: glutamatergic NT type [2][3], soma location in medial amygdalar nucleus [UBERON:0002892] [1], and the LIM-homeodomain transcription factor Lhx9 as a defining marker [1][4]. Definition basis: CLASSICAL. The primary marker evidence derives from Shh-Cre lineage tracing in mouse (Carney et al. 2010 [4]) and comparative genoarchitecture in bird and mammal (Vicario et al. 2016 [1]). The node note records that this is one of several extrinsic glutamatergic populations (ventral pallium, SPV, EmT-derived) contributing to the medial/extended amygdala.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**

| Atlas | Taxonomy ID | Notes |
|---|---|---|
| CCN20230722 | CCN20230722 | WMBv1; MERFISH spatial data from Zhuang 2023 (PMID:37915112) and Yao 2024 (PMID:37914271) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_medial_amygdala_lhx9_glutamatergic_neuron_to_cs20230722_supt_0057 | ATLAS_METADATA; ATLAS_METADATA | SUPPORT; SUPPORT | atlas-internal |

*Generated by evidencell `6a99d26` at 2026-06-05T13:57:40+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Medial amygdala Lhx9+ ventral pallial-derived glutamatergic neuron → 0057 MEA Slc17a7 Glut_3 [CS20230722_SUPT_0057] at LOW confidence. Key support: ATLAS_METADATA (MERFISH soma location CONSISTENT; NT type CONSISTENT). Key caveats: MARKER_NOT_ASSESSED (LHX9 absent from SUPT_0057 atlas metadata; no precomputed expression data available); cohort of 5 MEA Glutamatergic supertypes tied on discovery score — SUPT_0057 selected by highest region_fraction (0.588) alone.

The Cell Ontology has no specific term for this population; CL:0000679 (glutamatergic neuron) [[CL:0000679](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000679)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

**Predicate rationale.** The 2026-05-26 predicate rubric assigns `skos:broadMatch` when the atlas taxonomy_type is broader than the classical type. SUPT_0057 is the most MeA-enriched of the five MEA Slc17a7 Glut supertypes (region_fraction 0.588), but without LHX9 expression data it cannot be distinguished from the other four supertypes on the defining marker dimension. A prior run incorrectly assigned `skos:exactMatch` to this edge; this has been corrected to `skos:broadMatch` (1:n). The correction is warranted because: (1) the defining marker LHX9 is NOT_ASSESSED on the atlas side — it is absent from SUPT_0057 metadata and no precomputed expression data is available; (2) concordance on NT type and soma location alone does not meet the exactMatch threshold under the rubric (which requires clean 1:1 with no major unresolved contradictions); and (3) SUPT_0057 at 3,748 cells is very likely broader than the "minor subpopulation" [1] of Lhx9+ neurons in the medial amygdala.

### Proposed experiments and follow-ups

**1. Precomputed expression query for LHX9 across MEA Glut supertypes**
- **What:** Query precomputed expression stats for LHX9 across all five MEA Slc17a7 Glut supertypes (SUPT_0055–0057 and siblings) in CCN20230722.
- **Target:** Identify which supertype(s) show LHX9 mean expression ≥ MIN_DETECTABLE.
- **Expected output:** ATLAS_METADATA evidence item with marker_LHX9 alignment (CONSISTENT, APPROXIMATE, or DISCORDANT) added to the KB edge. If SUPT_0057 is the highest-expressing, supports narrowing to closeMatch.
- **Resolves:** Unresolved question 1; primary bottleneck for predicate correction and confidence upgrade.

**2. LHX9-ISH co-staining with SUPT_0057 defining markers**
- **What:** ISH co-staining of Lhx9 with SUPT_0057 defining markers (Trabd2b, Zic5, Dab1, Ntf3) in mouse medial amygdala sections.
- **Target:** Co-expression confirmed at single-cell level in medial amygdalar nucleus [UBERON:0002892].
- **Expected output:** LiteratureEvidence (marker_LHX9 CONSISTENT) added to KB edge; predicate could be narrowed to closeMatch, confidence upgraded to MODERATE.
- **Resolves:** Unresolved question 1.

**3. Targeted literature search**
- **What:** Cite-traverse or snippet search for "Lhx9 medial amygdala mouse transcriptomics" / "LHX9 MEA scRNA-seq" / "ventral pallial MEA neurons single-cell".
- **Target:** Any published dataset reporting LHX9 expression in MEA glutamatergic neurons.
- **Expected output:** LiteratureEvidence items; could provide marker alignment without new experiments.
- **Resolves:** Unresolved question 1.

**4. Annotation transfer using a Lhx9+ fate-mapped MEA dataset (if available)**
- **What:** MapMyCells annotation transfer of a Lhx9-Cre fate-mapped or Lhx9-enriched MEA dataset against CCN20230722 at CLUSTER level.
- **Target:** F1 ≥ 0.75 at CLUSTER level.
- **Expected output:** AnnotationTransferEvidence; would resolve cardinality, identify the best child cluster, and potentially support upgrade to MODERATE or HIGH confidence.
- **Resolves:** Unresolved question 1; would resolve 1:n cardinality.

### Open questions

1. Which of the five MEA Slc17a7 Glut supertypes (SUPT_0055–0057 and siblings) in CCN20230722 specifically corresponds to Lhx9+ ventral pallial-derived neurons? LHX9 expression data across these supertypes is needed to distinguish the candidates.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vicario et al. 2016 | [27160258](https://pubmed.ncbi.nlm.nih.gov/27160258/) | soma location; Lhx9 defining marker |
| [2] | Gerlach & Wullimann 2021 | [33515290](https://pubmed.ncbi.nlm.nih.gov/33515290/) | NT type |
| [3] | Raudales et al. 2024 | [39012795](https://pubmed.ncbi.nlm.nih.gov/39012795/) | NT type |
| [4] | Carney et al. 2010 | [20507551](https://pubmed.ncbi.nlm.nih.gov/20507551/) | Lhx9 defining marker |

---

<!-- verdict-block-start: edge_medial_amygdala_lhx9_glutamatergic_neuron_to_cs20230722_supt_0057 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.20
  rationale: >
    NT type CONSISTENT (Slc17a7/Glut subclass) and location_medial_amygdala CONSISTENT
    (region_fraction 0.588; CS20230722_SUPT_0057 ranks 1 of 5 in MBA:403 Glutamatergic
    cohort by region_fraction). Predicate is skos:broadMatch (1:n) because marker_LHX9
    is NOT_ASSESSED: LHX9 is absent from CS20230722_SUPT_0057 atlas metadata (defining
    markers: Trabd2b, Zic5, Dab1, Ntf3, Rassf3, Krt12) and no precomputed expression
    data is available. NT+location CONSISTENT alone is insufficient for exactMatch under
    the 2026-05-26 rubric; broadMatch reflects that SUPT_0057 likely encompasses multiple
    MEA glutamatergic populations beyond the Lhx9+ minor subpopulation.
  reconciliation_note: >
    Edge was previously marked skos:exactMatch in error. Corrected to skos:broadMatch 1:n
    per 2026-05-26 rubric: the classical defining marker LHX9 is NOT_ASSESSED on
    CS20230722_SUPT_0057 (absent from atlas metadata; no precomputed expression available).
    Concordance on NT+location alone does not meet exactMatch threshold. The five MEA
    Slc17a7 Glut supertypes are indistinguishable in Stage A discovery (all tied at
    score 1, cohort_size 5); SUPT_0057 selected by region_fraction 0.588 only.
  unresolved_questions:
    - "Which of 5 MEA Slc17a7 Glut supertypes (SUPT_0055-0057 and siblings) specifically corresponds to Lhx9+ ventral pallial-derived neurons? LHX9 expression data is needed."
```
<!-- verdict-block-end -->
