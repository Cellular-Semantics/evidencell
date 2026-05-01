# CA2 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | — | |
| Soma location | CA2 stratum pyramidale [UBERON:0014549] | [1] [2] |
| NT | glutamatergic | [3] |
| Markers | Pcp4+, Rgs14+, Amigo2+ | [4] [5] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0100 CA2-FC-IG Glut_1 [CS20230722_SUPT_0100] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0100 CA2-FC-IG Glut_1 · 🟡 MODERATE

**Supporting evidence:**

- SUPT_0100 (0100 CA2-FC-IG Glut_1) is the highest-scoring WMBv1 supertype candidate for CA2 pyramidal cells (discovery score 4). It belongs to subclass CS20230722_SUBC_025 (025 CA2-FC-IG Glut), which groups CA2 together with fasciola cinerea (FC) and indusium griseum (IG) glutamatergic cells. SUPT_0100 has 446 cells in Field CA2, pyramidal layer (MBA:446) consistent with the CA2 PC soma location. However, SUPT_0100 also has substantial cells in CA1/CA3 strata, raising the possibility that this supertype spans CA2 and transitional CA1/CA3 pyramidal cells or contains MERFISH registration noise at subfield borders. [Atlas metadata]
- MapMyCells local annotation transfer of Yao 2021 (GSE185862) mouse hippocampus SSv4 CA2-IG-FC subclass label (n=19) onto WMBv1 (CCN20230722). At SUBCLASS level: 18/19 cells (94.7%) map to SUBC_025 CA2-FC-IG Glut (F1=0.973, group_purity=1.0, target_purity=0.947). At SUPERTYPE level: 18/19 cells (94.7%) map to SUPT_0101 (CA2-FC-IG Glut_2, F1=0.947) and only 1/19 (5.3%) to SUPT_0100 (CA2-FC-IG Glut_1, F1=0.1). This result is PARTIAL because the subclass-level assignment strongly supports SUBC_025 membership, but supertype-level mapping to SUPT_0101 rather than SUPT_0100 reflects FC/IG contamination in Yao's mixed CA2-IG-FC label: SUPT_0101 is enriched for fasciola cinerea and induseum griseum cells (MERFISH data: 0 CA2 pyramidal layer cells in SUPT_0101 vs 446 in SUPT_0100). SUPT_0100 remains the correct supertype candidate for CA2 pyramidal cells based on MERFISH anatomy. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=CA2 stratum pyramidale (UBERON:0014549, compartment: SOMA) / B=Field CA2, pyramidal layer (MBA:446): 446 cells; Field CA1, stratum oriens (MBA:399): 292 cells; Field CA3, stratum oriens (MBA:486): 215 cells; Field CA3, pyramidal layer (MBA:495): 165 cells; Field CA2, stratum radiatum (MBA:454): 55 cells. CA2 pyramidal layer cells are present (446 cells) but SUPT_0100 has comparable or greater cell counts in CA1 and CA3 strata. The FC and IG component of the CA2-FC-IG subclass may drive cells to non-CA2 MERFISH regions. Classic CA2 PCs are a subset of the broader SUBC_025 population.

- SUBT_0100 name includes FC (fasciola cinerea) and IG (indusium griseum) alongside CA2. These are small CA2-adjacent structures; classical CA2 pyramidal cells are distinct from FC/IG neurons. The PARTIAL_OVERLAP relationship reflects uncertainty about whether this supertype cleanly captures CA2 PCs or conflates them with FC/IG populations.
- Annotation transfer of Yao 2021 (GSE185862) CA2-IG-FC subclass label (n=19) maps 94.7% of cells to SUPT_0101 (0101 CA2-FC-IG Glut_2, F1=0.947), not to SUPT_0100 (F1=0.1). However, SUPT_0101 MERFISH anatomy shows 0 cells in CA2 pyramidal layer (MBA:446) and is dominated by Fasciola cinerea (175 cells) and Induseum griseum (61 cells). SUPT_0100 has 106 CA2 pyramidal layer cells and 0 FC/IG cells. The AT result therefore reflects the FC/IG component of Yao's mixed CA2-IG-FC label mapping to the FC/IG-enriched atlas supertype SUPT_0101 — it does not constitute evidence that SUPT_0100 is the wrong target for CA2 pyramidal cells. A CA2-specific dataset (a CA2-specific dataset without FC/IG contamination) would be required for definitive AT.

**What would upgrade confidence:**

- *Unresolved:* Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors? FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 would clarify.

- *Proposed:* Check precomputed expression for Rgs14 and Pcp4 in SUPT_0100 via add-expression to distinguish CA2 PC subset from FC/IG contamination.

- *Proposed:* Run annotation transfer from a CA2-specific dataset (not a CA2-IG-FC mixed label) to distinguish SUPT_0100 vs SUPT_0101 correspondence for CA2 pyramidal cells proper.


---

## Proposed experiments

### 1 — Other

- Check precomputed expression for Rgs14 and Pcp4 in SUPT_0100 via add-expression to distinguish CA2 PC subset from FC/IG contamination.
- Run annotation transfer from a CA2-specific dataset (not a CA2-IG-FC mixed label) to distinguish SUPT_0100 vs SUPT_0101 correspondence for CA2 pyramidal cells proper.
*Resolves: edge_ca2_pc_hippocampus_to_supt_0100*

---

## Open questions

1. Do SUPT_0100 cells in CA1 and CA3 strata represent genuine pyramidal neurons (e.g. deep CA3c cells near CA2 border) or MERFISH registration errors? FISH validation of Rgs14 or Amigo2 in CA2 cells assigned to SUPT_0100 would clarify.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ca2_pc_hippocampus_to_supt_0100 | Atlas metadata | SUPPORT |
| edge_ca2_pc_hippocampus_to_supt_0100 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | soma location |
| [2] | Unknown 2021 · PMID:33956790 | [33956790](https://pubmed.ncbi.nlm.nih.gov/33956790/) | soma location |
| [3] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | neurotransmitter type |
| [4] | Unknown 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker |
| [5] | Unknown 2012 · PMID:22904370 | [22904370](https://pubmed.ncbi.nlm.nih.gov/22904370/) | Amigo2 marker |
