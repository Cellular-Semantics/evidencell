# entorhinal cortex layer III PCP4-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | pyramidal neuron (CL:0000598) | |
| Soma location | entorhinal cortex layer III [UBERON:0001905] |  |
| NT | glutamatergic | [1] |
| Markers | Pcp4+ | [2] [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0036 L2/3 IT ENT Glut_4 · 🟡 MODERATE

**Supporting evidence:**

- Annotation transfer of Yao 2021 (GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722) via local MapMyCells. Yao 2021 'L3 IT ENT' subclass cells (n=588), representing entorhinal cortex layer III IT projection neurons (including PCP4+ pyramidal cells projecting to CA1 and subiculum via the temporoammonic pathway), map to SUPT_0036 (L2/3 IT ENT Glut_4) with group_purity=0.888 and F1=0.937. This is a strong, high-purity mapping. SUPT_0037 (L2/3 IT ENT Glut_5) accounts for a further 10.2% of L3 IT ENT cells. Together SUPT_0036+0037 cover 99.0% of L3 IT ENT cells. [Annotation transfer]

**Concerns:**

- SUPT_0036 and SUPT_0037 together capture 99.0% of Yao 2021 L3 IT ENT cells. The classical ec_layer3_pyramidal_cell (Pcp4+) may TYPE_A_SPLITS across these two supertypes. SUPT_0036 is the dominant target (F1=0.937); a secondary edge to SUPT_0037 (F1=0.177, due to lower group purity) would complete the mapping.

**What would upgrade confidence:**

- *Unresolved:* Does PCP4 expression pattern in WMBv1 distinguish SUPT_0036 (EC layer III) from SUPT_0100/0101 (CA2-FC-IG) supertypes? This would confirm the PCP4 marker is not confounded across atlas types.

- *Proposed:* Add edge to SUPT_0037 (L2/3 IT ENT Glut_5) as secondary EC layer III mapping. Add-expression for Pcp4 in SUBC_008 (L2/3 IT ENT) supertypes.


---

## Proposed experiments

### 1 — Other

- Add edge to SUPT_0037 (L2/3 IT ENT Glut_5) as secondary EC layer III mapping. Add-expression for Pcp4 in SUBC_008 (L2/3 IT ENT) supertypes.
*Resolves: edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0036*

---

## Open questions

1. Does PCP4 expression pattern in WMBv1 distinguish SUPT_0036 (EC layer III) from SUPT_0100/0101 (CA2-FC-IG) supertypes? This would confirm the PCP4 marker is not confounded across atlas types.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0036 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | neurotransmitter type |
| [2] | Unknown 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker |
