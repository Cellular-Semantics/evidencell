# entorhinal cortex layer II stellate cell — WMBv1 (CCN20230722) Mapping Report
*Draft · 2026-04-27 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | glutamatergic neuron (CL:0000679) | |
| Soma location | entorhinal cortex layer II [UBERON:0001905] | [1] [2] [3] [4] [5] [6] [7] |
| NT | glutamatergic | [4] |
| Markers | Reln+ | [1] |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0042 L2/3 IT PIR-ENTl Glut_4 [CS20230722_SUPT_0042] |  | — | 🟡 MODERATE | Best candidate |

All edges: `PARTIAL_OVERLAP`

---

## 0042 L2/3 IT PIR-ENTl Glut_4 · 🟡 MODERATE

**Supporting evidence:**

- Annotation transfer of Yao 2021 (GSE185862) SSv4 hippocampal cells onto WMBv1 (CCN20230722) via local MapMyCells. Yao 2021 'L2 IT ENTl' subclass cells (n=180), representing lateral entorhinal cortex layer II IT neurons, map to SUPT_0042 (L2/3 IT PIR-ENTl Glut_4) with group_purity=0.956 and F1=0.964. The near-perfect F1 indicates SUPT_0042 is a highly specific match for lateral EC layer II cells. The Yao 2021 'L2 IT ENTl' subclass corresponds to the population containing reelin-positive stellate cells — the dominant excitatory neuron type in lateral EC layer II. The 'PIR-ENTl' designation in the supertype name reflects the shared transcriptomic signature between piriform cortex and lateral entorhinal cortex layer II populations. [Annotation transfer]

**Concerns:**

- **location** (APPROXIMATE): A=entorhinal cortex layer II (UBERON:0001905, compartment: SOMA) / B=SUPT_0042 in PIR-ENTl subclass; MERFISH assignment not assessed. The SUBC_009 (L2/3 IT PIR-ENTl Glut) subclass spans both lateral entorhinal cortex and piriform cortex, reflecting a shared transcriptomic signature. EC layer II stellate cells are in entorhinal cortex; any PIR component in SUPT_0042 may represent piriform layer II neurons with similar molecular profiles.

- The 'L2 IT ENTl' Yao 2021 subclass may include both Reln+ stellate cells and minor non-stellate populations in lateral EC layer II. The classical ec_layer2_stellate_cell is specifically Reln+; the Yao 2021 subclass may contain a small Reln- fraction. This does not substantially affect the mapping given the extremely high purity (F1=0.964). The 'PIR' component of the SUPT_0042 name warrants investigation to confirm EC vs. piriform contribution.

**What would upgrade confidence:**

- *Unresolved:* Does SUPT_0042 expression include a significant piriform cortex component in the WMBv1 MERFISH data, or is the PIR-ENTl designation primarily driven by transcriptomic similarity rather than spatial overlap?

- *Unresolved:* Is Reln expressed in SUPT_0042 at the level expected for stellate cells? Running add-expression for Reln on CCN20230722 precomputed stats would confirm.

- *Proposed:* Run add-expression for Reln and Calb1 on CCN20230722 to distinguish SUPT_0042 (Reln+, stellate) from SUPT_0052 (potentially Calb1+, pyramidal) at the atlas level.


---

## Proposed experiments

### 1 — Other

- Run add-expression for Reln and Calb1 on CCN20230722 to distinguish SUPT_0042 (Reln+, stellate) from SUPT_0052 (potentially Calb1+, pyramidal) at the atlas level.
*Resolves: edge_ec_layer2_stellate_cell_hippocampus_to_supt_0042*

---

## Open questions

1. Does SUPT_0042 expression include a significant piriform cortex component in the WMBv1 MERFISH data, or is the PIR-ENTl designation primarily driven by transcriptomic similarity rather than spatial overlap?
2. Is Reln expressed in SUPT_0042 at the level expected for stellate cells? Running add-expression for Reln on CCN20230722 precomputed stats would confirm.

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_ec_layer2_stellate_cell_hippocampus_to_supt_0042 | Annotation transfer | SUPPORT |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Naumann et al. 2015 · PMID:26223342 | [26223342](https://pubmed.ncbi.nlm.nih.gov/26223342/) | soma location |
| [2] | Unknown 2016 · PMID:26711115 | [26711115](https://pubmed.ncbi.nlm.nih.gov/26711115/) | soma location |
| [3] | Unknown 2010 · PMID:20512133 | [20512133](https://pubmed.ncbi.nlm.nih.gov/20512133/) | soma location |
| [4] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | soma location |
| [5] | Unknown 2023 · PMID:37219048 | [37219048](https://pubmed.ncbi.nlm.nih.gov/37219048/) | soma location |
| [6] | Unknown 2018 · PMID:29665671 | [29665671](https://pubmed.ncbi.nlm.nih.gov/29665671/) | soma location |
| [7] | Unknown 2018 · PMID:30209250 | [30209250](https://pubmed.ncbi.nlm.nih.gov/30209250/) | soma location |
