# Medial amygdala Lhx9+ ventral pallial-derived glutamatergic neuron — CCN20230722 Mapping Report

*2026-06-02 · Source: kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml*

---

## Introduction

The medial amygdala (MeA) is a predominantly GABAergic, subpallially derived structure, but it harbours a subset of glutamatergic neurons derived from extrinsic sources including the ventral pallium. Among these, a minor Lhx9-expressing subpopulation with ventral pallial origin has been identified and distinguished from the dominant subpallial GABAergic contingent on developmental and molecular grounds. Mapping this population to the CCN20230722 (Allen Brain Cell Atlas) mouse taxonomy is important for anchoring a molecularly defined developmental fate to a transcriptomically characterised supertype, enabling cross-species comparison of amygdala circuit organisation.

---

## Classical Node Properties

| Property | Value | Source(s) |
|---|---|---|
| Neurotransmitter type | Glutamatergic | Gerlach & Wullimann 2021 [2]; Raudales et al. 2024 [3] |
| Soma location | Medial amygdala (UBERON:0002892) | Vicario et al. 2016 [1] |
| Defining markers | LHX9 (positive) | Vicario et al. 2016 [1]; Carney et al. 2010 [4] |
| Negative markers | None recorded | — |
| Neuropeptides | None recorded | — |
| Morphology | Not characterised | — |
| Electrophysiology | Not characterised | — |
| CL mapping | CL:0000679 (BROAD; requires expert review) | Auto-proposed by asta-report-ingest |
| Notes | One of several extrinsic glutamatergic populations (ventral pallium, SPV, EmT-derived) contributing to medial/extended amygdala | — |

---

## Mapping Results

### Edge: medial_amygdala_lhx9_glutamatergic_neuron → CS20230722_SUPT_0057 (0057 MEA Slc17a7 Glut_3)

**Relationship:** `skos:exactMatch`
**Atlas node:** CS20230722_SUPT_0057 · 0057 MEA Slc17a7 Glut_3 · n = 3,748 cells

#### Property Comparisons

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glut (Slc17a7 subclass) | CONSISTENT |
| Location | UBERON:0002892 medial amygdala | MBA:403 Medial amygdalar nucleus (region_fraction 0.588; SELF evidence; both Zhuang 2023 and Yao 2024 MERFISH) | CONSISTENT |
| Marker: LHX9 | LHX9 defining marker (TRANSCRIPT; fate-mapping / Shh-Cre lineage tracing) | Not present in atlas node defining markers (Trabd2b, Zic5, Dab1, Ntf3, Rassf3, Krt12); no precomputed expression data available | NOT_ASSESSED |

#### Evidence Items

1. **ATLAS_METADATA** — SUPPORT  
   MERFISH spatial data (Zhuang 2023, PMID:37915112) places CS20230722_SUPT_0057 predominantly in Medial amygdalar nucleus (MBA:403; cell_ratio 0.399), consistent with the classical medial amygdala location. The Slc17a7 subclass assignment confirms glutamatergic identity. [ATLAS_METADATA]

2. **ATLAS_METADATA** — SUPPORT  
   Corroborating MERFISH data (Yao 2024, PMID:37914271) confirms SUPT_0057 in Medial amygdalar nucleus (MBA:403; cell_ratio 0.619). Glutamatergic assignment is consistent with the classical NT type. [ATLAS_METADATA]

#### Supporting Literature

The classical node is defined by convergent evidence from three sources:

> "In addition to these cells, the medial amygdala includes a minor subpopulation of Lhx9 cells of ventral pallial origin" <!-- quote_key: 11582390_e268c719 -->

> "the mammalian/rodent medial amygdala is a mosaic of GABAergic subpallial cells complemented by glutamatergic neuron types from extrinsic sources (ventral pallium, SPV, EmT)." <!-- quote_key: 231758452_9fd699d1 -->

> "Within the amygdala nuclei, PNs are exclusively glutamatergic in BLA, CoA, BMA, exclusively GABAergic in CeA, and predominantly GABAergic in MeA and BST. In rodents, there is also a population of glutamatergic pyramidal neurons (GLU PNs, derived from third ventricle neuroepithelium) that populates the BST, MeA, and hypothalamus." <!-- quote_key: 271240390_b54d0b91 -->

The role of Lhx9 in delineating efferent projection streams in the medial amygdala is further supported by:

> "the anatomical segregation of efferent projections that regulate reproductive or defensive behaviors is differentially marked by the LIM-containing homeodomain genes Lhx6 and Lhx9" <!-- quote_key: 627853_c6aafc07 -->

#### Caveats

- **MARKER_NOT_ASSESSED**: The classical defining marker LHX9 is absent from the atlas node metadata for CS20230722_SUPT_0057, and no precomputed expression data are available to test co-expression. The mapping therefore rests entirely on region and NT type concordance. Among the five MEA Slc17a7 Glut supertypes (SUPT_0055–0057 and siblings), SUPT_0057 has the highest medial amygdala region fraction (0.588), making it the top-ranked candidate, but this priority is circumstantial rather than marker-confirmed.

#### Unresolved Questions

- Which of the five MEA Slc17a7 Glut supertypes (SUPT_0055–0057 and siblings) specifically corresponds to Lhx9+ ventral pallial-derived neurons? LHX9 expression data are needed to resolve this.

#### Proposed Experiments

1. Run Lhx9-ISH co-stained with MERFISH probes for SUPT_0057 defining markers (Trabd2b, Zic5, Dab1, Ntf3) in mouse medial amygdala to directly test co-expression.
2. Obtain precomputed expression for CCN20230722 and query LHX9 across all five MEA Slc17a7 Glut supertypes to identify the best-matching candidate transcriptomically.

---

## Verdict

### Edge: medial_amygdala_lhx9_glutamatergic_neuron → CS20230722_SUPT_0057

**Confidence: LOW**  
**Confidence score: 0.40**

**Rationale:** SUPT_0057 (0057 MEA Slc17a7 Glut_3) is concordant with the classical node on both NT type (glutamatergic) and location (MBA:403 Medial amygdalar nucleus, region_fraction 0.588 across two independent MERFISH datasets), and ranks first among the five MEA glutamatergic supertypes by medial amygdala enrichment. However, the defining marker LHX9 is absent from atlas node metadata and no precomputed expression data are available, so the marker dimension cannot be assessed. No annotation transfer evidence exists. Confidence would be upgraded to MODERATE if LHX9 expression is confirmed in SUPT_0057 across the CCN20230722 atlas; HIGH would require quantitative F1 from an annotation transfer experiment or direct ISH co-localisation of LHX9 with SUPT_0057 defining markers.

---

```yaml
# Verdict write-back block — paste into MappingEdge in KB YAML
# Edge ID: edge_medial_amygdala_lhx9_glutamatergic_neuron_to_cs20230722_supt_0057
confidence: LOW
confidence_score: 0.40
rationale: >
  SUPT_0057 (0057 MEA Slc17a7 Glut_3) is concordant with the classical node on
  NT type (Glutamatergic / Glut) and location (MBA:403 Medial amygdalar nucleus,
  region_fraction 0.588 across two independent MERFISH datasets — Zhuang 2023 and
  Yao 2024), and ranks first among the five MEA Slc17a7 Glut supertypes by medial
  amygdala enrichment. However, the classical defining marker LHX9 is absent from
  atlas node metadata and no precomputed expression data are available, leaving the
  marker dimension NOT_ASSESSED. No annotation transfer evidence exists.
  Confidence would be upgraded to MODERATE if LHX9 expression is confirmed in
  SUPT_0057; HIGH would additionally require annotation transfer F1 > 0.75 or
  direct ISH co-localisation of LHX9 with SUPT_0057 defining markers in mouse
  medial amygdala.
rationale_generated_at: "2026-06-02"
report_path: reports/medial_temporal_lobe_amygdala/medial_amygdala_lhx9_glutamatergic_neuron_summary.md
```

---

## Discussion

The Lhx9+ glutamatergic neuron of the medial amygdala is a well-documented but numerically minor population that is distinguished from the dominant subpallial GABAergic contingent by both developmental origin (ventral pallium) and the expression of the LIM-homeodomain transcription factor Lhx9. Literature evidence consistently places these cells in the medial amygdala, where they contribute to a mosaic of glutamatergic types also including neurons derived from the subparaventricular zone (SPV) and the embryonic tegmental area (EmT). The functional significance of Lhx9 expression — specifically its role in segregating efferent projections controlling reproductive versus defensive behaviours — adds biological weight to the distinction, suggesting this population may correspond to a circuit-relevant node rather than a transitional developmental artefact.

The match to CS20230722_SUPT_0057 is currently supported only by spatial and NT type concordance. SUPT_0057 is the most MeA-enriched of the five MEA Slc17a7 Glut supertypes and therefore represents the most parsimonious candidate, but the five supertypes are not yet distinguished at the marker level within this analysis. It is plausible that one or more of the other four MEA Slc17a7 Glut supertypes corresponds more precisely to the Lhx9+ population, or that these supertypes collectively represent a mixture of developmentally distinct glutamatergic lineages (ventral pallial, SPV, EmT) that the atlas has not yet resolved at higher transcriptomic granularity. The cluster level (below supertype) may ultimately provide better resolution if Lhx9 or allied transcription factors (e.g. Lhx6, Nr2f2) mark distinct sub-populations within the MeA glutamatergic supertype hierarchy.

Two experiments would substantially resolve the current uncertainty. First, querying precomputed expression for LHX9 across all CCN20230722 MEA Glut supertypes would identify whether SUPT_0057 is indeed the Lhx9-enriched candidate or whether a sibling supertype scores higher. Second, multiplexed ISH or smFISH combining Lhx9 with the defining markers of SUPT_0057 (Trabd2b, Zic5, Dab1, Ntf3, Rassf3, Krt12) in mouse medial amygdala sections would provide direct co-expression evidence. If Lhx9 co-localises with SUPT_0057 markers, the mapping confidence would be upgraded to MODERATE; additional annotation transfer experiments could then push it to HIGH.

---

## References

| Label | Citation | PMID | DOI |
|---|---|---|---|
| [1] | Vicario et al. 2016 | 27160258 | 10.1007/s00429-016-1229-6 |
| [2] | Gerlach & Wullimann 2021 | 33515290 | 10.1007/s00441-020-03378-4 |
| [3] | Raudales et al. 2024 | 39012795 | 10.7554/eLife.93481 |
| [4] | Carney et al. 2010 | 20507551 | 10.1186/1749-8104-5-14 |
| — | Zhuang 2023 (MERFISH atlas) | 37915112 | — |
| — | Yao 2024 (MERFISH atlas) | 37914271 | — |
