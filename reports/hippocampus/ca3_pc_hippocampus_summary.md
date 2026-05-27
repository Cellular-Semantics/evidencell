# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-27 · Source: `kb/draft/hippocampus/hippocampus_glutamatergic.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Pyramidal layer of CA3 [UBERON:0014550] | [1][2] |
| NT | Glutamatergic | [3] |
| Defining markers | — | |
| Negative markers | — | |
| Neuropeptides | — | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0078 CA3 Glut_4 [CS20230722_SUPT_0078] | CA3 Glut | 1467 (CA3 pyramidal layer, MBA:495) | 🟡 MODERATE | Location CONSISTENT · NT CONSISTENT · AT F1=0.773 | Best candidate |

Total: 1 edge. Relationship type: TYPE_A_SPLITS (classical CA3 pyramidal cell encompasses five WMBv1 supertypes within SUBC_017; this edge targets the dominant correspondence SUPT_0078).

---

## 0078 CA3 Glut_4 [CS20230722_SUPT_0078] · 🟡 MODERATE

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0078 belongs to subclass CS20230722_SUBC_017 (017 CA3 Glut), the dedicated CA3 glutamatergic subclass in WMBv1. The classical CA3 pyramidal cell is defined as glutamatergic [3], and SUBC_017 is exclusively glutamatergic.

- **Soma location — CONSISTENT.** SUPT_0078 MERFISH anatomy is entirely CA3: pyramidal layer (MBA:495; 1467 cells), stratum oriens (MBA:486; 1381 cells), stratum radiatum (MBA:504; 945 cells), stratum lucidum (MBA:479; 868 cells), and stratum lacunosum-moleculare (MBA:471; 437 cells). All cells are within CA3 strata. No artefactual off-target regions such as lateral ventricle or alveus appear. Pyramidal layer (1467 cells) and stratum oriens (1381 cells) are the dominant compartments; MERFISH soma assignment routinely places CA3 PC soma in adjacent oriens.

- **Annotation transfer — SUPPORT.** MapMyCells local annotation transfer of Yao 2021 (GEO:GSE185862) mouse hippocampus SSv4 scRNA-seq CA3 subclass label onto WMBv1 (CCN20230722). Of 322 CA3 cells, 203 (63.0%) map to SUPT_0078 at the supertype level. F1 score = 0.773 (coverage = 0.630, purity = 1.0). Target_purity = 1.0 confirms SUPT_0078 receives only CA3 cells in this dataset. The remaining CA3 cells distribute across SUPT_0075 (16.8%), SUPT_0077 (11.5%), SUPT_0076 (6.5%), and SUPT_0079 (1.6%), consistent with TYPE_A_SPLITS: the classical CA3 pyramidal cell spans all SUBC_017 supertypes, with SUPT_0078 as the dominant correspondence.

- **Atlas metadata context.** The previous primary candidate SUPT_0075 received only 16.8% of Yao 2021 CA3 cells (F1=0.288); SUPT_0078 received 63.0% (F1=0.773), indicating it is the dominant CA3 PC supertype in the atlas. SUPT_0078 defining markers are Homer3 and Cldn22. The former claim that SUPT_0078–0079 represent mossy cell populations is not supported — SUPT_0078 anatomy is exclusively CA3 pyramidal/oriens/radiatum/lucidum/SLM strata with no hilar representation.

**Marker evidence provenance**

- **No defining markers established** for the classical CA3 pyramidal cell node at the time of this mapping. The CA3 pyramidal cell is defined primarily by anatomical location (CA3 stratum pyramidale [UBERON:0014550]) and glutamatergic NT type [3]; no specific molecular marker is listed on the classical node [1][2]. SUPT_0078 defining markers Homer3 and Cldn22 have not been compared against classical CA3 PC transcriptomics in the current evidence set. Cross-checking these atlas markers against published CA3 PC literature would strengthen the evidence base. *(Recommendation: A targeted cite-traverse for "Homer3 CA3 pyramidal" or "Cldn22 hippocampus" may identify whether these are genuinely CA3-specific markers.)*

**Concerns**

- **TYPE_A_SPLITS — incomplete representation.** WMBv1 SUBC_017 (CA3 Glut) contains five supertypes: SUPT_0075–0079. Annotation transfer (Yao 2021) confirms SUPT_0078 as the primary CA3 PC correspondence (63.0%, F1=0.773), but the remaining 37% of CA3 cells distribute across SUPT_0075 (16.8%), 0077 (11.5%), 0076 (6.5%), and 0079 (1.6%). A complete mapping requires additional edges to all five supertypes.

- **Sublayer correspondence unresolved.** SUPT_0075–0077 (CA3 Glut_1–3) collectively received 34.8% of Yao 2021 CA3 cells; their correspondence to CA3a, CA3b, or CA3c sublayers, or to other organisational principles such as proximal vs. distal mossy fiber input zones, is unresolved.

**What would upgrade confidence**

- **Annotation transfer from a CA3 sublayer-resolved dataset:** Run MapMyCells annotation transfer using a source dataset with CA3a/b/c sublayer annotations to map CA3 sublayer correspondence among SUPT_0075–0079; expected output: AnnotationTransferEvidence entries clarifying the role of SUPT_0078 vs SUPT_0075–0077 in the sublayer organisation. Expected F1 ≥ 0.70 per sublayer type at SUPERTYPE level. Resolves open question 1.

- **Additional supertype edges (SUPT_0075–0077, 0079):** Adding MappingEdge entries for the remaining CA3 Glut supertypes would accurately represent the full classical CA3 pyramidal cell population and enable confidence upgrade across the TYPE_A_SPLITS mapping.

---

## Proposed experiments

### Annotation transfer (CA3 sublayer-resolved dataset)

- **What:** MapMyCells annotation transfer to WMBv1 (CCN20230722) using a source dataset with CA3a/b/c sublayer-resolved annotations.
- **Target:** F1 ≥ 0.70 at SUPERTYPE level per CA3 sublayer class.
- **Expected output:** AnnotationTransferEvidence entries for edges to SUPT_0075, 0076, 0077, 0078, 0079; clarification of sublayer correspondence.
- **Resolves:** Open question 1 (CA3a/b/c sublayer correspondence of SUPT_0075–0077).

---

## Open questions

1. Do SUPT_0075, 0076, 0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to other organisational principles (e.g. proximal vs. distal mossy fiber input zone)?

---

## Evidence base table

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_ca3_pc_hippocampus_to_supt_0078 | ATLAS_METADATA | SUPPORT — SUPT_0078 in dedicated CA3 Glut subclass; NT CONSISTENT, all MERFISH cells in CA3 strata (1467 in pyramidal layer MBA:495) |
| edge_ca3_pc_hippocampus_to_supt_0078 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.773; purity=1.0; 63.0% of Yao 2021 CA3 cells map to SUPT_0078 |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 · PMID:27113915 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915/) | Soma location |
| [2] | Wheeler et al. 2015 · PMID:26402459 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459/) | Soma location |
| [3] | Dale et al. 2015 · PMID:26346726 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726/) | Neurotransmitter type |
