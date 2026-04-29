# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report

*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA3 (UBERON:0014550; *CA3 stratum pyramidale*) | [1], [2] |
| Neurotransmitter | Glutamatergic | [3] |
| Defining markers | — | — |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — | — |

> "There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1). They generally have excitatory effects on the neurons to which they send axon terminals including other glutamatergic and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine (DA)], cholinergic, and histaminergic (HA) cells."
> <!-- quote_key: 2281033_5b9805ff -->
> *— Dale et al. 2015 · PMID:26346726*

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_SUPT_0078 | 0078 CA3 Glut_4 | — | 🟡 MODERATE | NT consistent; anatomy CA3-exclusive; AT F1 = 0.773 | Best candidate |

---

## 0078 CA3 Glut_4 (CS20230722_SUPT_0078) · 🟡 MODERATE

### Supporting evidence

**Atlas metadata.** SUPT_0078 belongs to subclass CS20230722_SUBC_017 (017 CA3 Glut), the dedicated WMBv1 CA3 glutamatergic subclass. The subclass contains five supertypes (SUPT_0075–0079). SUPT_0078 MERFISH anatomy is restricted to CA3 strata: pyramidal layer (1,467 cells), stratum oriens (1,381), stratum radiatum (945), stratum lucidum (868), and stratum lacunosum-moleculare (437). No off-target regions are detected, in contrast to SUPT_0075, which showed lateral ventricle and alveus entries. Defining markers for SUPT_0078 are Homer3 and Cldn22.

Neurotransmitter type is consistent: both the classical CA3 pyramidal cell [3] and SUBC_017 (017 CA3 Glut) are glutamatergic.

**Annotation transfer.** MapMyCells local annotation transfer of the Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq dataset onto WMBv1 (CCN20230722) at the supertype level: of 322 CA3-labelled cells, 203 (63.0%) mapped to SUPT_0078, yielding F1 = 0.773 (group_purity = 0.630, target_purity = 1.0). The target_purity of 1.0 confirms that SUPT_0078 receives only CA3 cells in this dataset, establishing high specificity. The remaining 34.8% of CA3 cells distributed across SUPT_0075 (16.8%), SUPT_0077 (11.5%), SUPT_0076 (6.5%), and SUPT_0079 (1.6%), consistent with a TYPE_A_SPLITS relationship: the classical CA3 pyramidal cell type spans the entire CA3 Glut subclass, with SUPT_0078 as the dominant correspondence.

### Marker evidence provenance

No defining markers are currently recorded on the classical CA3 pyramidal cell node. SUPT_0078 atlas markers (Homer3, Cldn22) are derived from atlas metadata and have not yet been validated against primary literature sources for this node.

### Concerns

- **AMBIGUOUS_MAPPING.** WMBv1 SUBC_017 (CA3 Glut) contains five supertypes (SUPT_0075–0079). While SUPT_0078 is the dominant AT correspondence (63.0%, F1 = 0.773), the remaining 34.8% of Yao 2021 CA3 cells distribute across the other four supertypes. The sublayer correspondence of SUPT_0075–0077 (CA3 Glut_1–3) to CA3a/b/c remains unresolved; these may represent sublayer-specific populations or other organisational principles (e.g. proximal vs. distal mossy fibre input zone).
- The classical node currently carries no defining transcriptomic markers, limiting the depth of property comparison to anatomy and NT type.
- Cell counts for SUPT_0078 are not available from atlas metadata in this draft.

### What would upgrade confidence

- Populating defining markers on the classical CA3 pyramidal cell node from primary transcriptomic literature would enable direct marker-level comparison with SUPT_0078 atlas markers (Homer3, Cldn22) and the other CA3 Glut supertypes.
- Annotation transfer from a CA3 sublayer-resolved dataset (e.g. distinguishing CA3a, CA3b, CA3c) would clarify the spatial correspondence of SUPT_0075–0077 relative to SUPT_0078 and resolve whether the split reflects sublayer organisation.

---

## Proposed experiments

### Transcriptomics / single-cell

- Run annotation transfer from a CA3 sublayer-resolved dataset to map CA3a/b/c correspondence among SUPT_0075–0077 and clarify the role of SUPT_0078 vs. SUPT_0075–0077 in the sublayer organisation.

---

## Open questions

1. Do SUPT_0075, 0076, 0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to other organisational principles (e.g. proximal vs. distal mossy fibre input zone)?

---

## Evidence base

| Source | Type | Used for |
|---|---|---|
| Cembrowski et al. 2016 · PMID:27113915 | RNA-seq (mouse hippocampus) | Soma location |
| Wheeler et al. 2015 · PMID:26402459 | Knowledge base (Hippocampome.org) | Soma location |
| Dale et al. 2015 · PMID:26346726 | Review / synthesis | Neurotransmitter type |
| Yao 2021 · GEO:GSE185862 | AT source dataset (SSv4 scRNA-seq, mouse hippocampus) | Annotation transfer |
| WMBv1 CCN20230722 | Atlas metadata | Candidate supertype identification, MERFISH anatomy |

---

## References

1. Cembrowski et al. 2016 · PMID:27113915 · DOI:10.7554/eLife.14997
2. Wheeler et al. 2015 · PMID:26402459 · DOI:10.7554/eLife.09960
3. Dale et al. 2015 · PMID:26346726 · DOI:10.1017/S1092852915000425
