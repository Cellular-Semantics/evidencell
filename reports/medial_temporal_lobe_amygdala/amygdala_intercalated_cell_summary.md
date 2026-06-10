# Amygdala intercalated cell — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The amygdala intercalated cell (ITC) is a GABAergic inhibitory neuron forming the intercalated cell masses (ICMs) between the BLA and CeA. ITCs express the transcription factor Foxp2, dopamine receptor D1 (Drd1), and mu-opioid receptor (Oprm1) as defining markers, distinguishing them from all other amygdala GABAergic subtypes. ITCs gate information flow from BLA to CeA and are critical for fear extinction. Their distinctive marker profile (Foxp2+ / Drd1+ / Oprm1+) makes them one of the most molecularly distinct amygdala cell types.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0998, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-3-Foxp2_Col6a1 to CS20230722_CLUS_0998 with F1=0.56 at CLASS and F1=0.10 at SUBCLASS level (PARTIAL support). All three defining markers are CONSISTENT.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0998 | 🔴 LOW | Foxp2 CONSISTENT · Drd1 CONSISTENT · Oprm1 CONSISTENT · AT F1=0.56 (CLASS) | `skos:broadMatch` |

#### Property alignment — CS20230722_CLUS_0998 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Foxp2 expression | Foxp2 — defining TF | Foxp2 CONSISTENT | CONSISTENT |
| Drd1 expression | Drd1 — positive | Drd1 CONSISTENT | CONSISTENT |
| Oprm1 expression | Oprm1 — positive | Oprm1 CONSISTENT | CONSISTENT |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-3-Foxp2_Col6a1, n=165) | ANNOTATION_TRANSFER | PARTIAL |

---

## Discussion

All three distinctive ITC markers are CONSISTENT, providing strong molecular evidence. However, AT mapping only reaches CLASS level with meaningful F1 (0.56); subclass F1=0.10 is very weak, indicating the AT does not resolve to the specific cluster. The PARTIAL support on the AT evidence reflects this limited resolution. The strong marker convergence provides biological credibility for the broadMatch, but cluster-level AT resolution is needed to upgrade confidence. A dedicated ITC dataset or re-analysis of the Hochgerner data targeting Foxp2+ cells specifically would strengthen this mapping.

---

<!-- verdict-block-start: edge_amygdala_intercalated_cell_to_cs20230722_clus_0998 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.42
  rationale: >
    GABA-3-Foxp2_Col6a1 maps with F1=0.56 (CLASS) and F1=0.10 (SUBCLASS)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0998 (PARTIAL); 3 of 3 markers CONSISTENT
    (marker_Foxp2, marker_Drd1, marker_Oprm1). Strong marker convergence
    but AT resolves only to CLASS level; broadMatch retained pending
    cluster-level AT resolution.
  unresolved_questions:
    - "Can a dedicated ITC-enriched dataset resolve GABA-3-Foxp2_Col6a1 to CS20230722_CLUS_0998 at cluster level (F1 ≥ 0.70)?"
    - "Are there additional clusters within the Foxp2+ class that also correspond to ITC subtypes (dorsal vs. ventral ICMs)?"
```
<!-- verdict-block-end -->
