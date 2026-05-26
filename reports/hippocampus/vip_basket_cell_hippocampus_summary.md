# VIP-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | stratum pyramidale [UBERON:0014548] |  |
| NT | GABAergic |  |
| Markers | Vip+ |  |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] |  | 215 |  |  |

All edges: `evidencell:UncertainRelationship`

---

## 0179 Vip Gaba_7 · 

*`CS20230722_SUPT_0179` · 215 cells (10x)*

**Supporting evidence:**

- Vip Gaba_7 supertype has Vip as a defining marker, consistent with the VIP+ basket cell marker profile. Atlas anatomy includes CA1 pyramidal layer (11 cells) and CA1 stratum oriens (24 cells), partially consistent with a perisomatic-targeting cell soma in stratum pyramidale. However, SUPT_0179 has limited CA1 representation and is primarily a CA3-enriched supertype (CA3 pyr 23, CA3 SO 25, CA3 SR 17, CA3 lucidum 11). Vip Gaba_7 is also the candidate supertype for IS interneurons (interneuron-selective VIP+ types), making this assignment uncertain without functional/morphological data. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) SSv4 Vip subclass (n=476 HIP cells) onto WMBv1. Vip cells map strongly to SUBC_046 (F1=0.969) at SUBCLASS level. At SUPERTYPE level, SUPT_0179 (Vip Gaba_7) is the second-strongest target (F1=0.379, 96 cells, purity=0.970), alongside SUPT_0177 (Vip Gaba_5, F1=0.397). The Vip population is distributed across many supertypes; SUPT_0179 being a prominent target is consistent with the VIP basket correspondence but does not discriminate basket from IS cells. Yao 2021 SSv4 'Vip' subclass (n=476 HIP cells) encompasses VIP basket, IS cells, and other VIP interneuron subtypes; subtype resolution requires a dataset with morphologically identified VIP-IN labels. [Annotation transfer]

**Concerns:**

- **location_stratum_pyramidale** (APPROXIMATE): A=stratum pyramidale (SOMA) / B=CA1 pyramidal layer (11 cells); CA3 pyramidal layer (23 cells). CA1 pyramidal layer present but low cell count. CA3-enriched overall. Stratum oriens cells (CA1 SO 24) may represent a different VIP type.

- SUPT_0179 (Vip Gaba_7) is also the candidate supertype for IS interneurons (calretinin/VIP+ interneuron-selective cells described in Tyan et al. 2014). VIP basket cells (perisomatic to pyramidal cells) and IS interneurons (targeting other interneurons) are functionally distinct but share VIP expression. Without additional markers (e.g., Cnr1 for basket identity, Calb2 for IS identity) this mapping cannot be resolved from atlas metadata.
- VIP basket cell described in a single primary study (Tyan et al. 2014, PMID:24671999). Thin evidence base.
- CA1 pyramidal layer representation in SUPT_0179 is very low (11 cells).

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | Atlas metadata | PARTIAL |
| edge_vip_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
