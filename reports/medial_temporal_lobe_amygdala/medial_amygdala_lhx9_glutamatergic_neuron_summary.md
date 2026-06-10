# Medial amygdala Lhx9 glutamatergic neuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The medial amygdala Lhx9 glutamatergic neuron is a glutamatergic cell type defined by expression of the LIM homeobox transcription factor Lhx9. This type resides in the medial amygdala (MEA) and plays roles in social and reproductive behaviour circuits. LHX9 is used as a defining transcription factor marker, distinguishing this type from other MEA glutamatergic neurons.

---

## Results

One candidate atlas supertype was assessed: CS20230722_SUPT_0057, carrying a `skos:broadMatch` at LOW confidence. MapMyCells annotation transfer (Hochgerner et al. 2023; `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`) maps VGLUT1-25-Plcxd3_Reln to CS20230722_SUPT_0057 with F1=0.60 at SUPERTYPE level. The defining marker LHX9 is NOT_ASSESSED.

### Mapping candidates table

| Rank | WMBv1 target | Confidence | Key alignment | Verdict |
|---|---|---|---|---|
| 1 | CS20230722_SUPT_0057 | 🔴 LOW | AT F1=0.60 (SUPERTYPE) · LHX9 NOT_ASSESSED | `skos:broadMatch` |

#### Property alignment — CS20230722_SUPT_0057 · 🔴 LOW

| Property | Classical | Atlas | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glutamatergic | CONSISTENT |
| LHX9 expression | LHX9 — defining TF | not in precomputed data | NOT_ASSESSED |

**Evidence support**

| Evidence | Type | Supports |
|---|---|---|
| WMBv1 atlas metadata | ATLAS_METADATA | SUPPORT |
| Hochgerner 2023 MapMyCells AT (VGLUT1-25-Plcxd3_Reln, n=164) | ANNOTATION_TRANSFER | SUPPORT |

---

## Discussion

Supertype AT F1=0.60 provides moderate evidence. LHX9 is NOT_ASSESSED in the precomputed atlas data, preventing marker-level validation. The atlas label "MEA Slc17a7 Glut_3" is consistent with MEA glutamatergic identity. Upgrading confidence requires LHX9 expression data for SUPT_0057 or targeted literature linking Lhx9 expression to this specific atlas supertype.

---

<!-- verdict-block-start: edge_medial_amygdala_lhx9_glutamatergic_neuron_to_cs20230722_supt_0057 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.38
  rationale: >
    VGLUT1-25-Plcxd3_Reln maps with F1=0.60 (SUPERTYPE) in
    `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1` to
    CS20230722_SUPT_0057; 0 of 1 markers CONSISTENT (marker_LHX9
    NOT_ASSESSED). Moderate AT support at supertype level; no marker
    validation possible from available precomputed data.
  unresolved_questions:
    - "Can LHX9 expression be confirmed in CS20230722_SUPT_0057 from RNA-seq or in-situ data?"
    - "Does VGLUT1-25-Plcxd3_Reln specifically correspond to Lhx9+ MEA neurons, or is it a broader MEA glutamatergic cluster?"
```
<!-- verdict-block-end -->
