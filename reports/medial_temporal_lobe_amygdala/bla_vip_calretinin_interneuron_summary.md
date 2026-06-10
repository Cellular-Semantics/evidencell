# BLA VIP/calretinin interneuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala VIP/calretinin interneuron is an interneuron-selective GABAergic interneuron defined by co-expression of VIP (vasoactive intestinal peptide) and calretinin (Calb2), often also expressing CCK. Vereczki et al. 2021 estimated VIP and/or calretinin-expressing interneuron-selective cells constitute 29–38% of GABAergic cells in the LA/BA, making this the most abundant interneuron class. These cells preferentially inhibit other interneurons (disinhibition circuit). The defining marker profile includes Calb2, VIP, and CCK with absence of Pvalb and Sst.

---

## Results

One candidate atlas cluster was assessed: CS20230722_CLUS_0628, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps GABA-51-Vip-Crh to CS20230722_CLUS_0628 with F1=0.65 at SUBCLASS and F1=0.54 at CLUSTER level. Two of five markers are CONSISTENT.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_CLUS_0628 | 🔴 LOW | Calb2 CONSISTENT · VIP CONSISTENT · CCK APPROXIMATE · AT F1=0.54 (CLUSTER) | `skos:broadMatch` |

#### Property alignment — CS20230722_CLUS_0628 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | GABAergic | GABA | CONSISTENT |
| Calb2 expression | Calb2 — positive | Calb2 CONSISTENT | CONSISTENT |
| VIP expression | VIP — positive | VIP CONSISTENT | CONSISTENT |
| CCK expression | CCK — associated | CCK APPROXIMATE | APPROXIMATE |
| Pvalb (negative) | absent | not in precomputed data | NOT_ASSESSED |
| Sst (negative) | absent | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (GABA-51-Vip-Crh, n=72) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

Two core markers (Calb2, VIP) are CONSISTENT and CCK is APPROXIMATE. However, cluster-level AT F1=0.54 is moderate, and this is a heterogeneous classical type (29–38% of GABAergic cells) likely spanning multiple atlas clusters. The broadMatch predicate reflects this heterogeneity. Upgrading requires either splitting the classical type into subtypes or providing additional marker data to identify a specific cluster anchor.

---

<!-- verdict-block-start: edge_bla_vip_calretinin_interneuron_to_cs20230722_clus_0628 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.38
  rationale: >
    GABA-51-Vip-Crh maps with F1=0.65 (SUBCLASS) and F1=0.54 (CLUSTER)
    in `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_CLUS_0628; 2 of 5 markers CONSISTENT (marker_Calb2,
    neuropeptide_Vip CONSISTENT; neuropeptide_Cck APPROXIMATE;
    negative_marker_Pvalb, negative_marker_Sst NOT_ASSESSED).
    Moderate AT; heterogeneous classical type likely spans multiple
    clusters; broadMatch retained.
  unresolved_questions:
    - "Does the VIP/calretinin BLA population span multiple atlas clusters, and if so, which clusters correspond to the interneuron-selective subtype?"
    - "Can Pvalb and Sst absence be confirmed in CS20230722_CLUS_0628 from precomputed data?"
```
<!-- verdict-block-end -->
