# Medial amygdala GABAergic principal neuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The medial amygdala (MeA; [UBERON:0002892]) is a centromedial amygdala nucleus with a complex developmental history, receiving contributions from pallidal, preoptic, hypothalamic, and prethalamic eminence territories. GABAergic principal neurons are the dominant neuronal class in MeA, reflecting the nucleus's predominantly subpallial origin; mapping this heterogeneous population to the Allen CCN20230722 atlas is a prerequisite for linking classical circuit and behavioural studies to transcriptomic cell types.

### Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Medial amygdalar nucleus [UBERON:0002892] | [1], [2], [3] |
| NT type | GABAergic | [4], [5] |
| Defining markers | — (none formally characterised) | — |
| Negative markers | — | — |
| Neuropeptides | — (not formally assigned; note: Gal, Avp, Sst, Npy subpopulations described in literature) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** review, amygdala organisation and developmental origins · Vicario et al. 2016 [1]
  > the medial amygdala also includes cell subpopulations from the same origins as those in the BSTM (pallidal, preoptic, hypothalamic, prethalamic eminence)
  > — Vicario et al. 2016, Medial and extended amygdala developmental-origin cell populations · [1] <!-- quote_key: 11582390_8b546b82 -->

- **Soma location:** review, amygdala volume and anatomy · Nolan et al. 2020 [2]
  > .amygdala nuclei are commonly categorised into three groups: the deep laterobasal amygdala containing the lateral (LA) and basal nuclei; the superficial cortical-like nuclei; and centromedial amygdala containing the central (CE) and medial nuclei. (Yang et al., 2017)
  > — Nolan et al. 2020, Medial temporal lobe structures and broad cellular makeup · [2] <!-- quote_key: 222092617_b027389d -->

- **Soma location:** review, amygdala cellular organisation · Ignacio et al. 2014 [3]
  > At the cellular level, the amygdala is composed of a group of 13 sub-nuclei located in the medial temporal lobe (Price, 2003). These nuclei may be divided into four subdivisions (Sah et al., 2003): (Ethen et al., 2009) basolateral (which includes the lateral, basolateral, and basomedial nuclei), (May et al., 2009) cortical like (including nucleus of the lateral olfactory tract, bed nucleus of the accessory olfactory tract, the cortical nucleus, and the periamygdaloid cortex), (3) centromedial (central and medial nuclei, and the amygdaloid part of the bed nucleus of stria terminalis), and (4) other (which includes anterior amygdala area, the amygdalo-hippocampal area, and the intercalated nuclei)
  > — Ignacio et al. 2014, Amygdala organization and principal cellular classes · [3] <!-- quote_key: 1229611_e14a19cf -->

- **NT type:** primary circuit study, amygdala cell types · Raudales et al. 2024 [4]
  > .the former includes BLA, CoA, BMA, and MeA, while the latter includes CeA and BST.Within the amygdala nuclei, PNs are exclusively glutamatergic in BLA, CoA, BMA, exclusively GABAergic in CeA, and predominantly GABAergic in MeA and BST.In rodents, there is also a population of glutamatergic pyramidal neurons (GLU PNs, derived from third ventricle neuroepithelium) that populates the BST, MeA, and hypothalamus (García-Moreno et al., 2010)(Huilgol et al., 2016).
  > — Raudales et al. 2024, Amygdala organization and principal cellular classes · [4] <!-- quote_key: 271240390_b54d0b91 -->

- **NT type:** comparative neurobiology review · Gerlach & Wullimann 2021 [5]
  > the mammalian/rodent medial amygdala is a mosaic of GABAergic subpallial cells complemented by glutamatergic neuron types from extrinsic sources (ventral pallium, SPV, EmT).
  > — Gerlach & Wullimann 2021, Medial and extended amygdala developmental-origin cell populations · [5] <!-- quote_key: 231758452_9fd699d1 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: GABAergic neuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] (BROAD).

The Cell Ontology has no specific term for this MeA GABAergic population; CL:0011005 (GABAergic neuron) is the closest broadly applicable ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas supertype was assessed. 0256 NDB-SI-MA-STRv Lhx8 Gaba_13 [CS20230722_SUPT_0256] is the only ranked candidate at LOW confidence, representing a tentative broadMatch in a discovery context where five GABAergic supertypes at MBA:403 scored equally and no formal markers exist on the classical node to discriminate among them.

### Mapping candidates table

**4a. Candidate overview table**

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0256 NDB-SI-MA-STRv Lhx8 Gaba_13 [CS20230722_SUPT_0256] | NDB-SI-MA-STRv | 162 | 🔴 LOW | NT CONSISTENT · location APPROXIMATE | Speculative |

Note: 1 edge total; skos:broadMatch (n:m mapping context — classical node likely spans multiple supertypes).

**4b. Property alignment table — 0256 NDB-SI-MA-STRv Lhx8 Gaba_13 [CS20230722_SUPT_0256]**

**Table 1 — Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial amygdalar nucleus [UBERON:0002892] | MBA:403 Medial amygdalar nucleus (4 cells Zhuang 2023; 0 soma Yao 2024; region_fraction 0.06); dominant: Striatum MBA:477, Pallidum MBA:803 | not assessed | APPROXIMATE |
| NT type | GABAergic | GABA (subclass NDB-SI-MA-STRv Lhx8 Gaba; inferred from label) | not assessed | CONSISTENT |
| LHX8 expression | not assessed (no defining_markers on classical node) | Lhx8 DEFINING marker on CS20230722_SUPT_0256 | not assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| MERFISH atlas metadata (Zhuang 2023) | Atlas metadata | PARTIAL | 4 cells at MBA:403; region_fraction 0.06; GABAergic label consistent | atlas-internal |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### 0256 NDB-SI-MA-STRv Lhx8 Gaba_13 · 🔴 LOW

**Supporting evidence:**

- **NT type CONSISTENT:** The supertype label encodes "Gaba" and belongs to subclass NDB-SI-MA-STRv, confirming a GABAergic identity consistent with the classical node [atlas-internal]. The MeA is predominantly GABAergic, as documented in multiple classical references [4][5].
- **MeA represented in supertype label:** The subclass name "NDB-SI-MA-STRv" contains "MA" (medial amygdala), indicating that some cells in this lineage occupy MeA territory [atlas-internal].
- **MERFISH spatial data (Zhuang 2023):** 4 SUPT_0256 cells are placed in Medial amygdalar nucleus (MBA:403) by MERFISH, providing direct spatial evidence of minor MeA presence (cell_ratio 0.074) [atlas-internal].

**Marker evidence provenance:**

The classical node carries no formal defining markers. The atlas candidate (CS20230722_SUPT_0256) is defined by Lhx8 as a DEFINING marker. Classical descriptions of MeA interneurons often reference Lhx6 (a paralogue expressed in MGE-derived cells) rather than Lhx8. The relationship between Lhx6 and Lhx8 in MeA is not assessed in the gathered evidence; the alignment for the LHX8 property is therefore NOT_ASSESSED. A targeted literature search for "Lhx8 medial amygdala" versus "Lhx6 medial amygdala" would clarify whether Lhx8+ MeA cells are a genuine subpopulation or a striatopallidal contaminant from non-MeA portions of the supertype.

**Concerns:**

- **Location APPROXIMATE — MeA is peripheral in this supertype:** region_fraction = 0.06; dominant soma distribution is striatopallidal (Striatum MBA:477, Pallidum MBA:803). *(The striatopallidal regions are not directly adjacent to the medial amygdala; this is a meaningful anatomical mismatch indicating most cells of this supertype are not MeA neurons.)*
- **BROAD_CLASSICAL_NODE:** The classical node encompasses a heterogeneous population with pallidal, preoptic, hypothalamic, and prethalamic eminence developmental origins, likely corresponding to multiple atlas supertypes simultaneously.
- **DISTRIBUTED_ACROSS_SUPERTYPES:** Five GABAergic supertypes at MBA:403 scored equally in the discovery cohort (cohort score = 1, cohort_size = 5, next_best_score = 1). SUPT_0256 is ranked first by cohort order only; SUPT_0249 and SUPT_0230 are equally viable candidates.
- **Null MERFISH soma count (Yao 2024):** The Yao 2024 MERFISH dataset records 0 soma for this supertype in MeA, contrasting with the 4 cells in Zhuang 2023 — the discrepancy is unexplained and limits confidence in the spatial localisation claim.

**What would upgrade confidence:**

- **Neuropeptide marker extraction and re-discovery:** Extract neuropeptide subtype markers (Gal, Avp, Sst, Npy) from ASTA literature snippets and add them to the classical node, then re-run Stage A discovery to determine which of the 5 equally-scoring MeA GABAergic supertypes best matches each neuropeptide-defined subpopulation. This would replace the current broad node with multiple targeted nodes and allow proper subtype-level mapping.
- **Targeted literature search:** Trawl literature for Lhx8 expression in MeA versus striatopallidal territory to determine whether SUPT_0256's Lhx8 identity is congruent with MeA-resident cells or reflects striatopallidal contamination.
- **Annotation transfer (AnnotationTransferEvidence):** Run MapMyCells on a dataset containing neuropeptide-defined or Cre-driver MeA GABAergic populations to produce F1-based mapping at supertype level (target: F1 ≥ 0.50 at SUPT level for any subtype).

---

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The Medial amygdala GABAergic principal neuron is defined by NT type (GABAergic; [4][5]) and soma location (Medial amygdalar nucleus [UBERON:0002892]; [1][2][3]). No formal molecular markers are assigned; the node carries a `definition_basis: CLASSICAL`, reflecting a population defined by anatomy and neurotransmitter identity rather than transcriptomic or marker-based criteria. The `notes` field records the known heterogeneity: multiple lineage-defined subpopulations (pallidal-, preoptic-, hypothalamic-, and prethalamic-eminence-derived cells; TOH-domain Otp+ and SPV core Sim1+ lineages) distribute distinctly across medial and central extended amygdala.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**
- CCN20230722; pseudobulk path not recorded in this edge's atlas metadata item.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_medial_amygdala_gabaergic_neuron_to_cs20230722_supt_0256 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `f00d68f` at 2026-06-04T12:07:34+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Medial amygdala GABAergic principal neuron → 0256 NDB-SI-MA-STRv Lhx8 Gaba_13 [CS20230722_SUPT_0256] at LOW confidence. Key support: NT type CONSISTENT; minor MERFISH MeA presence (region_fraction 0.06). Key caveats: BROAD_CLASSICAL_NODE (heterogeneous lineage composition; no formal markers); DISTRIBUTED_ACROSS_SUPERTYPES (five equally scoring MeA GABAergic supertypes in discovery cohort).

The Cell Ontology has no specific term for this MeA GABAergic population; GABAergic neuron [[CL:0011005](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0011005)] is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

### Proposed experiments and follow-ups

**1. Neuropeptide-resolved subtype decomposition**
- **What:** Extract neuropeptide marker data (Gal, Avp, Sst, Npy) from existing ASTA literature snippets; add markers to classical node; re-run Stage A discovery.
- **Target:** Discriminate among the 5 equally-scoring MeA GABAergic supertypes by neuropeptide profile.
- **Expected output:** Multiple targeted classical nodes with formal defining markers, enabling higher-confidence mapping edges.
- **Resolves:** edge_medial_amygdala_gabaergic_neuron_to_cs20230722_supt_0256 open question Q1; reduces BROAD_CLASSICAL_NODE caveat.

**2. Targeted literature review — Lhx8 in MeA**
- **What:** Cite-traverse for "Lhx8 medial amygdala" and "Lhx6 medial amygdala" in existing ASTA corpus; supplement with database search if needed.
- **Target:** Determine whether SUPT_0256's Lhx8 identity is congruent with MeA-resident cells or reflects striatopallidal contamination.
- **Expected output:** LiteratureEvidence item on the edge; resolution of NOT_ASSESSED LHX8 marker alignment.
- **Resolves:** edge open question Q2 (Lhx8 vs. Lhx6 paralogue question).

**3. Annotation transfer**
- **What:** Run MapMyCells (CCN20230722 target) on a dataset of neuropeptide-defined or Cre-driver MeA GABAergic cells (e.g. Gal-Cre, Avp-Cre, Sst-Cre transcriptomes).
- **Target:** F1 ≥ 0.50 at SUPT level for at least one neuropeptide-defined subtype; discriminate among the 5 candidate supertypes.
- **Expected output:** AnnotationTransferEvidence items on each of the 5 candidate supertype edges.
- **Resolves:** DISTRIBUTED_ACROSS_SUPERTYPES caveat; would allow at least MODERATE confidence for the dominant neuropeptide subtype.

### Open questions

1. Which of the 5 MeA GABAergic supertypes best represents the multiple MeA subpopulations (galanin+, vasopressin+, SST+, NPY+ populations)?
2. Does Lhx8 expression in CS20230722_SUPT_0256 indicate a genuine Lhx8-expressing MeA subpopulation, or is this a striatopallidal signal in non-MeA cells?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Vicario et al. 2016 | [27160258](https://pubmed.ncbi.nlm.nih.gov/27160258/) | Soma location; MeA developmental origins |
| [2] | Nolan et al. 2020 | [33015518](https://pubmed.ncbi.nlm.nih.gov/33015518/) | Soma location; amygdala nuclei organisation |
| [3] | Ignacio et al. 2014 | [25309888](https://pubmed.ncbi.nlm.nih.gov/25309888/) | Soma location; amygdala subdivision classification |
| [4] | Raudales et al. 2024 | [39012795](https://pubmed.ncbi.nlm.nih.gov/39012795/) | NT type; MeA predominantly GABAergic |
| [5] | Gerlach & Wullimann 2021 | [33515290](https://pubmed.ncbi.nlm.nih.gov/33515290/) | NT type; MeA GABAergic subpallial identity |

---

<!-- verdict-block-start: edge_medial_amygdala_gabaergic_neuron_to_cs20230722_supt_0256 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  rationale: >
    NT type CONSISTENT (GABAergic label on CS20230722_SUPT_0256); location APPROXIMATE
    (region_fraction 0.06 at MBA:403; dominant distribution striatopallidal MBA:477/803;
    1 of 1 property comparisons assessed CONSISTENT, 1 APPROXIMATE, 1 NOT_ASSESSED).
    No defining markers on classical node; 5 equally-scoring MeA GABAergic supertypes
    in discovery cohort (score 1, cohort_size 5, next_best_score 1) — SUPT_0256
    ranked first by cohort order only. BROAD_CLASSICAL_NODE caveat applies.
  reconciliation_note: >
    skos:broadMatch is appropriate: the classical node spans multiple developmental
    lineages (pallidal, preoptic, hypothalamic, prethalamic) likely distributed across
    several supertypes. The mapping is speculative until neuropeptide subtype markers
    are added and Stage A re-run.
  lit_to_lit_edges: []
  unresolved_questions:
    - >
      Which of the 5 MeA GABAergic supertypes (CS20230722_SUPT_0256, SUPT_0249,
      SUPT_0233, SUPT_0230, SUPT_0286) best represents each neuropeptide-defined
      subpopulation (Gal+, Avp+, Sst+, Npy+)? Neuropeptide markers should be
      extracted from ASTA corpus and added to the classical node before re-running
      discovery.
    - >
      Does Lhx8 on CS20230722_SUPT_0256 reflect genuine MeA-resident Lhx8+ cells
      or striatopallidal contamination? Targeted Lhx8/Lhx6 literature check needed.
```
<!-- verdict-block-end -->
