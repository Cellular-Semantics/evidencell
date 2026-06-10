# Central amygdala GABAergic projection neuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala GABAergic projection neuron (CeA-GP) is a long-range inhibitory neuron projecting from the central amygdala to downstream targets. Classical defining markers include GBX1, TH, and NR4A2, distinguishing it from local CeA interneurons. This cell type is implicated in fear expression and modulation of downstream autonomic and behavioural responses.

---

## Results

One candidate atlas supertype was assessed: CS20230722_SUPT_0249, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-25-Lhx8-Th to CS20230722_SUPT_0249 with F1=0.86 at SUBCLASS and F1=0.57 at SUPERTYPE level. All three classical markers are NOT_ASSESSED in the atlas.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_SUPT_0249 | 🔴 LOW | AT F1=0.86 (SUBCLASS) · markers all NOT_ASSESSED | `skos:broadMatch` |

#### Property alignment — CS20230722_SUPT_0249 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| GBX1 expression | GBX1 — positive | not in precomputed data | NOT_ASSESSED |
| TH expression | TH — positive | not in precomputed data | NOT_ASSESSED |
| NR4A2 expression | NR4A2 — positive | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-25-Lhx8-Th, n=50) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

Subclass AT F1=0.86 is strong, but the supertype-level F1 (0.57) is moderate, and the edge targets SUPT_0249 rather than a subclass. All three defining markers (GBX1, TH, NR4A2) are NOT_ASSESSED because precomputed expression data for these genes is unavailable for this atlas cluster. Marker validation is required to strengthen this mapping. The broadMatch is appropriate given the coarse resolution of the AT at the supertype level.

---

<!-- verdict-block-start: edge_central_amygdala_gabaergic_projection_neuron_to_cs20230722_supt_0249 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.38
  rationale: >
    GABA-25-Lhx8-Th maps with F1=0.86 (SUBCLASS) and F1=0.57 (SUPERTYPE)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_SUPT_0249; 0 of 3 markers CONSISTENT (marker_GBX1,
    marker_TH, marker_NR4A2 all NOT_ASSESSED). AT provides molecular
    anchor at subclass but supertype-level F1 is moderate; marker
    validation required.
  unresolved_questions:
    - "Can GBX1, TH, or NR4A2 expression be confirmed in CS20230722_SUPT_0249 from precomputed stats or in-situ data?"
    - "Does GABA-25-Lhx8-Th specifically capture long-range CeA projection neurons, or does it mix with local CeA interneurons?"
```
<!-- verdict-block-end -->
