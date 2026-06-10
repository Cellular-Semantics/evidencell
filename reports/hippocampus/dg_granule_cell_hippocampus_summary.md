# Dentate gyrus granule cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

Dentate gyrus (DG) granule cells are the densely packed glutamatergic principal neurons of the DG granule cell layer; their unmyelinated axons (mossy fibers) project into the stratum lucidum of CA3 and form the first leg of the classical hippocampal trisynaptic circuit, carrying excitatory input from layer II of entorhinal cortex onward to CA3 pyramidal cells [1][5][7]. The population is continuously renewed in adult animals, with newly generated cells passing through an immature stage before integrating into the mature circuit, and dorsal versus ventral granule cells are reported to differ in functional properties [2][5][6]. Mapping the classical granule cell onto the WMBv1 taxonomy is consequential both for anchoring DG-focused functional studies in a reference cell-type framework and for resolving how the atlas's several DG Glut supertypes relate to mature versus immature granule populations.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Dentate gyrus granule cell layer [UBERON:0005381]; mossy-fiber projection target: CA3 pyramidal layer [UBERON:0014550] | [1][2][3][4][5][6] |
| NT | Glutamatergic (with mixed VGLUT1/VGLUT2/VGAT co-release at juvenile mossy-fiber terminals) | [1][5][6][7][8] |
| Defining markers | Prox1, C1ql2, Slc17a7 (VGLUT1), Gria1 (GluA1), Gria2 (GluA2), Grm1 (mGluR1), Nptn (neuroplastin Np65) | [2][9][10][11][12] |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** mossy-fiber circuit description (Munster-Wandowski et al. 2013) · [1]
  > The hippocampal mossy fibers (MFs), the axons of the granule cells (GCs) of the dentate gyrus, innervate mossy cells and interneurons in the hilus on their way to CA3 where they innervate interneurons and pyramidal cells
  > — Munster-Wandowski et al. 2013, abstract · [1] <!-- quote_key: 7458943_e2eed73d -->
- **Soma location:** trisynaptic-circuit description (Yau et al. 2015) · [3]
  > These principal cells are interconnected through glutamatergic synapses that form the classical trisynaptic pathway, where dentate granule cells receive input from entorhinal cortex and project to CA3 pyramidal cells, which then connect to CA1 pyramidal cells (Munster-Wandowski et al., 2013)(Yau et al., 2015).
  > — Yau et al. 2015, Classical Hippocampal Circuit Organization · [3] <!-- quote_key: 1705399_6ee6563e -->
- **NT type:** mossy-fiber co-release (Pedroni et al. 2014) · [6]
  > Granule cells (GCs) in the dentate gyrus are crucial for transferring information from the entorhinal cortex to the hippocampus proper where they integrate the classical excitatory trisynaptic circuit (McBain, 2008). Although primarily glutamatergic, the axons of GCs, the mossy fibers (MFs), contain GABA, its synthesizing enzyme glutamic acid decarboxylase (Schwarzer et al., 1995)(Sloviter et al., 1996) and the vesicular GABA transporter VIAAT (Zander et al., 2010). In addition, immunogold experiments have demonstrated the presence of both AMPA and GABA A receptors, co-localized on MF terminals in close spatial relation with synaptic vesicles (Bergersen et al., 2003). All these pieces of evidence suggest that MF-cornu ammon (CA3) synapses can use GABA as a neurotransmitter since they posses all the machinery for synthesizing, storing, releasing, and sensing it
  > — Pedroni et al. 2014, Developmental and Temporal Characteristics · [6] <!-- quote_key: 11333153_7e2a7ff8 -->
- **NT type:** mossy-fiber VGLUT1/VGLUT2/VGAT coexistence (Zander et al. 2010) · [8]
  > VGLUT1, VGLUT2, and VGAT coexist in mossy fiber terminals of the h
  > — Zander et al. 2010, abstract · [8] <!-- quote_key: 539922_281341b3 -->
- **NT type:** transient GABAergic phenotype before glutamatergic integration (Pedroni et al. 2014) · [6]
  > immediately after birth, GCs exhibit a clear GABAergic phenotype. Only later they integrate the classical glutamatergic trisynaptic hippocampal circuit
  > — Pedroni et al. 2014, abstract · [6] <!-- quote_key: 11333153_3bc75fe5 -->
- **NT type:** quantitative RNA-seq of major excitatory hippocampal classes (Cembrowski et al. 2016) · [7]
  > we used next-generation RNA sequencing (RNA-seq) to produce a quantitative, whole genome characterization of gene expression for the major excitatory neuronal classes of the hippocampus; namely, granule cells and mossy cells of the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
  > — Cembrowski et al. 2016, abstract · [7] <!-- quote_key: 4875295_4a456257 -->
- **Prox1 / Slc17a7 marker:** vGLUT1 as principal hippocampal VGLUT (Sarvari et al. 2016) · [9]
  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [9] <!-- quote_key: 14854554_ed1bdc00 -->
- **Grm1 marker:** mGluR1 restricted to granule cells and CA3 pyramidal neurons (Sarvari et al. 2016) · [9]
  > Metabotropic glutamate receptor 1 (mGluR1) is mainly expressed in granule cells and CA3 pyramidal neurons while mGluR5 is highly expressed in all subfields of the rat hippocampus (Fotuhi et al., 1994)
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [9] <!-- quote_key: 14854554_b6a5ffa0 -->
- **C1ql2 marker:** restricted to DG granule cells within hippocampus (D et al. 2018) · [10]
  > the expression of Sema5B and C1ql2 is restricted to dentate granule cells within the hippocampus
  > — D et al. 2018, discussion · [10] <!-- quote_key: 5895709_81a3d36b -->
- **Gria1 marker:** developmental onset in granule cells (Hagihara et al. 2011) · [2]
  > granule cells begin to profoundly express GluR1 at around 3 weeks after cell division
  > — Hagihara et al. 2011, Developmental and Temporal Characteristics · [2] <!-- quote_key: 16383828_dc4eb8fc -->
- **Gria1 / Gria2 marker:** GluA1/GluA2 immunoreactivity in DG granule cell bodies (Yeung et al. 2020) · [11]
  > The GluA1 receptor subunit displayed diffuse staining within the str. radiatum and str. oriens, with marked immunoreactivity localized to cellular processes within the str. pyramidale of the CA3 (Figure 2). Isolated localization to pyramidal cell bodies can be seen through all three layers of the CA3, although mainly concentrated within the str. pyramidale. The CA1 showed strong dense immunoreactivity within the str. oriens and str. radiatum, with relatively decreased staining within the str. pyramidale cells. Within the DG, immunoreactivity was diffuse within the str. moleculare, with staining localized to cellular bodies within the str. granulosum. In particular, the hilus displayed neuronal body staining, with otherwise weak diffuse immunoreactivity
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [11] <!-- quote_key: 210181642_7ac40176 -->
- **Nptn marker:** Np65 localized to DG granule cell layer (Herrera-Molina et al. 2017) · [12]
  > unequivocally identified hNp65-positive glutamatergic neurons are granular neurons of DG, pyramidal neurons of CA1, CA2-3, subiculum, and layers II, IV, and V of the entorhinal cortex. Further direct visual inspection using a bright-field microscope confirmed that the hNp65 expression in major areas/ layers of the glutamatergic pathways within the entorhinal cortex and hippocampus (Supplementary Table 1) is very similar to its reported expression in mouse and rat (Beesley et al., 2014)(Smalla et al., 2000) (Herrera-Molina et al., 2014)(Bernstein et al., 2007)(Langnaese et al., 1997)
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [12] <!-- quote_key: 3288675_37ad1c13 -->

</details>

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

Annotation transfer of an independent mouse DG scRNA-seq dataset (Hochgerner 2018, GSE95315) onto WMBv1 places mature and immature granule cell labels predominantly on the DG Glut supertype 0137 DG Glut_2 [CS20230722_SUPT_0137] (supertype F1=0.584 / 0.601 for mature / immature; subclass-level coverage 0.988 onto the DG Glut subclass; see figure and Table 1). Cluster-level mass scatters within supertype 0137 across child clusters, with the in-graph cluster candidate 0505 DG Glut_2 [CS20230722_CLUS_0505] supported by atlas-side marker concordance (Prox1, C1ql2) rather than by direct AT, which actually peaks on sibling clusters 0506 / 0507 — see Discussion.

![Filtered AT figure for Dentate gyrus granule cell](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the two Hochgerner 2018 source groups relevant to DG granule cells (Granule-mature, n=487 source cells reaching subclass; Granule-immature, n=383 source cells reaching subclass). Each panel row is a source-cell group; nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source-group cells landing on this target; Purity = fraction of this target's cells coming from the source group. With multiple source groups in the figure, Purity differentiates them; with a single pooled source, Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. Both source labels converge on the DG Glut subclass and on 0137 DG Glut_2 at supertype; at cluster level the mature label peaks on 0506 DG Glut_2 (F1=0.690) and the immature label on 0507 DG Glut_2 (F1=0.720), with 0505 DG Glut_2 not the top cluster for either source group.*

The mature- and immature-granule labels converge on the same DG Glut subclass and supertype, while diverging at cluster level — a pattern consistent with the developmental cohort structure reported for granule cells, where adult-born immature cells form a distinct functional subpopulation that integrates into the granule layer over weeks.

### 0137 DG Glut_2 [CS20230722_SUPT_0137] · 🟡 MODERATE

**Property alignment (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus granule cell layer [UBERON:0005381] | 47167 painted cells in Dentate gyrus, granule cell layer [MBA:632]; region_fraction_100um=0.991 | 12273 painted cells in MBA:632 (0505 DG Glut_2); region_fraction_100um=0.991 | CONSISTENT |
| NT type | glutamatergic | not asserted on supertype | Glut (0505 DG Glut_2) | SUPT: NOT_ASSESSED; CLUS: CONSISTENT |
| Prox1 expression | defining marker | 8.59 (cohort_pct 0.853; child-coverage 1.000) | 8.38 (0505 DG Glut_2; cohort_pct 0.818) | CONSISTENT |
| C1ql2 expression | defining marker | 5.77 (cohort_pct 0.912; child-coverage 1.000) | 7.38 (0505 DG Glut_2; cohort_pct 0.982) | CONSISTENT |

*(All 5 child clusters of supertype 0137 carry Prox1 and C1ql2 above cohort-50th-percentile (child-coverage 1.000 for both markers); the supertype is uniformly granule-marker-positive. Best AT-supported child is 0506 / 0507; the in-graph child-cluster edge is 0505 — see Concerns.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Hochgerner 2018 MapMyCells AT | Annotation transfer | SUPPORT | F1=0.584 (mature) / 0.601 (immature) at supertype; subclass coverage 0.988 onto DG Glut | atlas-internal |
| Atlas spatial / marker metadata | Atlas metadata | SUPPORT | 7199 cells in MBA:632; defining markers Dsp/Kcnh3/Syndig1 (atlas-side) | atlas-internal |

**Supporting evidence**

- Direct annotation-transfer evidence from an independent DG scRNA-seq dataset (Hochgerner 2018, GSE95315, n=870 cells from Granule-mature + Granule-immature labels): both labels map predominantly onto supertype 0137 DG Glut_2 with supertype F1=0.584 / 0.601, and onto the parent DG Glut subclass with coverage 0.988 (mature) / 0.888 (immature). This is the strongest available link between the classical type and a WMBv1 supertype.
- Atlas spatial registration places 7199 supertype cells in the dentate gyrus granule cell layer [MBA:632], 6636 in the molecular layer, and 3067 in the polymorph layer — a soma-position pattern consistent with classical granule cells (region_fraction_100um = 0.991, region_evidence = SELF).
- Atlas-side precomputed expression confirms the classical defining markers on the supertype: Prox1 mean = 8.59 (cohort percentile 0.853, child-coverage 1.000) and C1ql2 mean = 5.77 (cohort percentile 0.912, child-coverage 1.000). C1ql2 in particular is reported as DG-granule-restricted within hippocampus [10].

**Marker evidence provenance**

- **Prox1:** transcript-level marker with a primary hippocampal expression study cited [9]; consistent expression on the supertype (val=8.59) and uniformly above the cohort 50th percentile across all 5 child clusters.
- **C1ql2:** transcript-level marker with a primary citation specifically restricting C1ql2 to DG granule cells within hippocampus [10]; supertype mean (5.77) is at cohort percentile 0.912.
- **Slc17a7 / Gria1 / Gria2 / Grm1 / Nptn:** included in the classical defining marker list but not yet present as `property_comparisons` rows on this edge; their target-side values are not represented in the current YAML and therefore cannot be cross-checked here. Adding precomputed expression for these markers across the DG Glut supertypes would strengthen the call (see proposed experiments).
- The atlas-side defining markers Dsp, Kcnh3, Syndig1 are not on the classical defining-marker list, so the two marker sets do not directly cross-check at the moment; targeted classical-side curation of these atlas-defining genes would help.

**Concerns**

- AT support is robust but partial: supertype F1=0.584 reflects scatter of granule-label cells across sibling DG Glut supertypes (0136, 0138) and into the immature-granule supertype 0141 (AMBIGUOUS_MAPPING caveat). At cluster level the AT signal is not exclusive — see the 0505 paragraph.
- Atlas-side defining markers on this supertype (Dsp, Kcnh3, Syndig1) have not yet been compared against classical granule cell transcriptomics (TAXONOMY_LEVEL_MISMATCH caveat); the cluster-level call within the supertype rests on atlas-side marker concordance rather than direct AT.

**What would upgrade confidence**

- Add `PrecomputedExpression` entries for Slc17a7, Gria1, Gria2, Grm1, and Nptn on the DG Glut supertypes (0136 through 0139) to discriminate them via the full classical defining-marker panel (`AtlasMetadataEvidence`).
- Run MapMyCells from an independent adult mouse DG granule cell scRNA-seq dataset onto WMBv1 (target F1 ≥ 0.75 at supertype) to cross-validate the supertype call (`AnnotationTransferEvidence`).
- Resolve whether the DG Glut supertypes 0136 / 0137 / 0138 reflect functionally distinct granule cell cohorts (e.g. dorsal vs ventral, or developmental age cohorts).

### 0505 DG Glut_2 [CS20230722_CLUS_0505] · 🟡 MODERATE

**Property alignment (Table 1).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus granule cell layer [UBERON:0005381] | 47167 cells in MBA:632 (parent supertype 0137); region_fraction_100um=0.991 | 12273 cells in MBA:632 (0505); region_fraction_100um=0.991 | CONSISTENT |
| NT type | glutamatergic | not asserted on parent supertype 0137 | Glut (0505) | CONSISTENT |
| Prox1 expression | defining marker | 8.59 (parent supertype 0137; cohort_pct 0.853) | 8.38 (0505; cohort_pct 0.818) | CONSISTENT |
| C1ql2 expression | defining marker | 5.77 (parent supertype 0137; cohort_pct 0.912) | 7.38 (0505; cohort_pct 0.982) | CONSISTENT |

*(Of the 5 children of the parent supertype 0137, cluster 0505 sits at the high end of the C1ql2 distribution at cluster level (val=7.38, cohort_pct 0.982); however the AT-best children are cluster 0506 (F1=0.690 for the Granule-mature label) and cluster 0507 (F1=0.720 for the Granule-immature label), not 0505 — best cluster on AT is not yet in graph edges.)*

**Evidence support (Table 2).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression | Atlas metadata | PARTIAL | Prox1=8.38, C1ql2=7.38; region_fraction_100um=0.991 | atlas-internal |

**Supporting evidence**

- Cluster 0505 DG Glut_2 sits within supertype 0137 DG Glut_2, inheriting the supertype-level AT support indirectly.
- Atlas-side marker concordance is strong: Prox1 mean = 8.38 (cohort percentile 0.818) and C1ql2 mean = 7.38 (cohort percentile 0.982). C1ql2 in particular places this cluster at the high end of the DG granule cohort distribution.
- Spatial registration: 12273 painted cells of cluster 0505 fall in Dentate gyrus, granule cell layer [MBA:632] (region_fraction_100um = 0.991, region_evidence = SELF).

**Marker evidence provenance**

- See the supertype 0137 marker provenance — the same classical-marker portfolio applies. Cluster 0505 is the highest C1ql2-expressing child of supertype 0137 in the precomputed-stats cohort.

**Concerns**

- The cluster-level call is supported by atlas-side marker concordance rather than by direct AT: the Hochgerner Granule-mature and Granule-immature labels peak at cluster level on cluster 0506 (F1=0.690, mature) and cluster 0507 (F1=0.720, immature) — both siblings of cluster 0505 within the parent supertype 0137 — not on cluster 0505 itself (TAXONOMY_LEVEL_MISMATCH caveat). Neither sibling is currently a top-K edge in this graph, so this cluster-level mapping is the best available in-graph proxy but is not the AT-preferred child.
- Cluster-level marker comparison relies on a single atlas precomputed-expression cohort (CCN20230722); independent transcriptomic replication of the Prox1 / C1ql2 child-cluster ranking is not yet available (SINGLE_DATASET caveat).

**What would upgrade confidence**

- Re-emit Stage B to add the AT-preferred sibling clusters 0506 and 0507 to the top-K, then re-run AT scoring against the Hochgerner Granule-mature and Granule-immature labels (target F1 ≥ 0.7 at cluster level) (`AnnotationTransferEvidence`).
- Add precomputed expression for Slc17a7, Gria1, Gria2, Grm1, and Nptn on clusters 0505, 0506, and 0507 for direct marker comparison across the AT-preferred children of supertype 0137 (`AtlasMetadataEvidence`).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0137 DG Glut_2 [CS20230722_SUPT_0137]` | — | 74950 | 🟡 MODERATE | Hochgerner AT F1=0.584/0.601 to supertype; Prox1+C1ql2 child-coverage 1.000 | Primary |
| `0505 DG Glut_2 [CS20230722_CLUS_0505]` | `0137 DG Glut_2 [CS20230722_SUPT_0137]` | 20503 | 🟡 MODERATE | Prox1=8.38, C1ql2=7.38 (cohort_pct 0.982); within supertype 0137 | Secondary (best in-graph cluster within supertype 0137) |
| `0510 DG Glut_4 [CS20230722_CLUS_0510]` | `0139 DG Glut_4 [CS20230722_SUPT_0139]` | 5166 | 🔴 LOW | Prox1+C1ql2 high but wrong DG Glut supertype | Eliminated (AT peaks on supertype 0137) |
| `0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514]` | `0141 DG-PIR Ex IMN_2 [CS20230722_SUPT_0141]` | 408 | 🔴 LOW | Immature-neuron supertype; C1ql2 low (0.47) | Eliminated (immature-neuron supertype) |
| `0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515]` | `0141 DG-PIR Ex IMN_2 [CS20230722_SUPT_0141]` | 511 | 🔴 LOW | Immature-neuron supertype; C1ql2 low (0.38) | Eliminated (immature-neuron supertype) |
| `0316 CA3 Glut_5 [CS20230722_CLUS_0316]` | `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` | 202 | 🔴 LOW | CA3 supertype; Prox1=0.23, C1ql2=0.29 | Eliminated (CA3 not DG) |
| `0141 DG-PIR Ex IMN_2 [CS20230722_SUPT_0141]` | — | 1200 | 🔴 LOW | Immature-neuron supertype; C1ql2 child-coverage 0.500 | Eliminated (immature-neuron supertype) |
| `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` | — | 318 | 🔴 LOW | CA3 supertype; Prox1+C1ql2 near zero | Eliminated (CA3 not DG) |
| `0139 DG Glut_4 [CS20230722_SUPT_0139]` | — | 5166 | 🔴 LOW | DG Glut sibling of supertype 0137; AT peaks elsewhere | Eliminated (AT peaks on supertype 0137) |
| `0138 DG Glut_3 [CS20230722_SUPT_0138]` | — | 964 | 🔴 LOW | DG Glut sibling of supertype 0137; AT peaks elsewhere | Eliminated (AT peaks on supertype 0137) |
| `0137 DG Glut_2 [CS20230722_SUPT_0137]` (duplicate) | — | 74950 | 🔴 LOW | Duplicate edge to the same supertype accession (only `discovery_score` evidence) | Eliminated (duplicate edge — see unresolved questions) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The dentate gyrus granule cell is curated as a `CLASSICAL_MULTIMODAL` classical node: glutamatergic with developmentally transient GABAergic / mixed-transmitter phenotype at mossy-fiber terminals [6][7][8]; defining markers Prox1, C1ql2, Slc17a7 (VGLUT1), Gria1 (GluA1), Gria2 (GluA2), Grm1 (mGluR1), and Nptn (Np65) [2][9][10][11][12]; soma in the dentate gyrus granule cell layer [UBERON:0005381] with mossy-fiber projection target in the CA3 pyramidal layer [UBERON:0014550] [1][3][4][5][6].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018; cluster labels: Granule-mature / Granule-immature) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (precomputed_stats CCN20230722) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 2934 (filtered to 2934) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | — |

</details>

---

## Discussion

The primary mapping is to supertype 0137 DG Glut_2 [CS20230722_SUPT_0137] at MODERATE confidence (skos:broadMatch; mapping_cardinality 1:n). The supertype is the unambiguous AT-best supertype for both mature and immature granule cell labels from an independent DG scRNA-seq dataset, sits in the dentate gyrus granule cell layer, and carries the classical defining markers Prox1 and C1ql2 above their cohort 50th percentiles in every child cluster.

Cluster-level resolution is less clean. Within supertype 0137, the in-graph cluster candidate 0505 DG Glut_2 [CS20230722_CLUS_0505] is the highest C1ql2-expressing child, but Hochgerner Granule-mature peaks at cluster level on cluster 0506 (F1=0.690) and Granule-immature on cluster 0507 (F1=0.720). Neither sibling is currently a top-K edge in this graph. The MODERATE cluster-level mapping to 0505 should therefore be treated as a marker-based placeholder pending re-emission of the top-K to include 0506 and 0507, and direct AT scoring against them.

The mature- and immature-granule labels converge at subclass and supertype but diverge at cluster level — consistent with the well-described developmental cohort structure of granule cells, where adult-born immature granule neurons (which may correspond in part to the WMBv1 immature-neuron supertype 0141 DG-PIR Ex IMN_2 [CS20230722_SUPT_0141]) integrate over weeks into the mature granule population. The atlas placement of immature granule cells across supertype 0141 versus supertype 0137 is itself a biological question worth follow-up.

A duplicate edge to the same supertype 0137 accession exists in the graph (a LOW-confidence stub from Stage A emit, alongside the substantive MODERATE edge with full AT + atlas-marker evidence). The substantive edge is the authoritative one; the duplicate is flagged for curator removal.

---

## References

[1] Munster-Wandowski et al. 2013 · PMID:24319410
[2] Hagihara et al. 2011 · PMID:21927594
[3] Yau et al. 2015 · PMID:26380120
[4] https://doi.org/10.1038/s41598-017-11268-z
[5] Scharfman & Myers 2013 · PMID:23420672
[6] Pedroni et al. 2014 · PMID:24592213
[7] Cembrowski et al. 2016 · PMID:27113915
[8] Zander et al. 2010 · PMID:20519538
[9] Sarvari et al. 2016 · PMID:27375434
[10] D et al. 2018 · PMID:29674952
[11] Yeung et al. 2020 · PMID:32009891
[12] Herrera-Molina et al. 2017 · PMID:28779130

---

## Verdict blocks (machine-readable; not rendered in user-facing report)

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_supt_0137 -->
```yaml
verdict:
  node_b_accession: CS20230722_SUPT_0137
  confidence: MODERATE
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  rationale: '[tier:STRONGEST] Direct annotation-transfer evidence from an independent

    mouse DG scRNA-seq dataset (Hochgerner 2018, GSE95315) places both

    Granule-mature and Granule-immature labels predominantly on this

    supertype (supertype F1=0.58 / 0.601; subclass coverage onto

    the DG Glut subclass = 0.988 / 0.888). Atlas-side spatial registration

    and precomputed expression confirm dentate gyrus granule cell layer

    soma location and concordance with the classical defining markers

    Prox1 (val=8.59, child-coverage 1.000) and C1ql2 (val=5.77,

    child-coverage 1.000). Supertype mapping is the supportable level;

    cluster-level resolution requires re-emission with the AT-preferred

    sibling children.

    '
  caveats:
  - caveat_type: AMBIGUOUS_MAPPING
    description: 'Granule-mature and Granule-immature scatter across DG Glut sibling

      supertypes (0136 through 0139) and to the immature-neuron

      supertype 0141; 0137 is dominant at F1=0.58 but not exclusive.

      '
  - caveat_type: TAXONOMY_LEVEL_MISMATCH
    description: 'Cluster-level call within this supertype rests on atlas-side

      marker concordance rather than direct annotation-transfer

      evidence; AT-preferred children at cluster level (Granule-mature

      peaking on 0506, Granule-immature on 0507) are not currently

      top-K edges in this graph.

      '
  proposed_experiments:
  - Run annotation transfer from an independent adult mouse dentate gyrus granule cell scRNA-seq dataset onto WMBv1 (target F1 >= 0.75 at supertype) to cross-validate the supertype call.
  - Add precomputed expression for Slc17a7, Gria1, Gria2, Grm1, and Nptn on the DG Glut supertypes 0136 through 0139 to discriminate them via the full classical defining-marker panel.
  unresolved_questions:
  - Do supertypes 0136, 0137, and 0138 correspond to functionally distinct granule cell populations (dorsal vs ventral, or developmental cohorts)?
  - How does the adult-born immature granule cell population (supertype 0141) relate to the classical dentate gyrus granule cell definition?
  reconciliation_note: 'Paired with cluster-level edge

    edge_dg_granule_cell_hippocampus_to_CS20230722_CLUS_0505 as the

    supertype + best-in-graph-child-within-supertype mapping; the

    annotation-transfer-preferred children (cluster 0506 and cluster 0507)

    are not currently in top-K and should be added.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_CLUS_0505 -->
```yaml
verdict:
  node_b_accession: CS20230722_CLUS_0505
  confidence: MODERATE
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  rationale: '[tier:NEXT] Cluster lies within the supertype 0137 (the

    annotation-transfer-best supertype) and carries the classical

    defining markers Prox1 (val=8.38, cohort_pct 0.818) and C1ql2

    (val=7.38, cohort_pct 0.982) — the latter at the high end of the

    DG-granule cohort distribution. Spatial registration places

    12273 painted cells in MBA:632 (region_fraction_100um=0.991,

    region_evidence=SELF). This is the best in-graph cluster proxy

    pending re-emission of the AT-preferred sibling children.

    '
  caveats:
  - caveat_type: TAXONOMY_LEVEL_MISMATCH
    description: 'Cluster-level call rests on atlas-side marker concordance;

      direct annotation-transfer evidence supports the supertype

      0137 at supertype level but peaks on sibling clusters at

      cluster level (Granule-mature on 0506, F1 (on the paired supertype edge);

      Granule-immature on 0507, F1 (on the paired supertype edge)) rather than on this

      cluster 0505.

      '
  - caveat_type: SINGLE_DATASET
    description: 'Cluster-level marker comparison relies on a single atlas

      precomputed-expression cohort (CCN20230722); independent

      transcriptomic replication of the Prox1 / C1ql2 child-cluster

      ranking is not yet available.

      '
  proposed_experiments:
  - Re-emit top-K to include the AT-preferred sibling clusters 0506 and 0507 and run annotation transfer against the Hochgerner Granule-mature and Granule-immature labels (target F1 >= 0.7 at cluster level).
  - Add precomputed expression for Slc17a7, Gria1, Gria2, Grm1, and Nptn on clusters 0505, 0506, and 0507 for direct marker comparison across the annotation-transfer-preferred children of supertype 0137.
  unresolved_questions:
  - Are clusters 0506 and 0507 the appropriate cluster-level mapping for mature and immature granule cells rather than cluster 0505?
  reconciliation_note: 'Paired with supertype edge

    edge_dg_granule_cell_hippocampus_to_supt_0137 as the

    best-in-graph-child-within-supertype side of a supertype + cluster

    mapping.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_CLUS_0510 -->
```yaml
verdict:
  node_b_accession: CS20230722_CLUS_0510
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] Wrong DG Glut supertype — annotation-transfer peaks on

    the supertype 0137, not on the parent supertype 0139 of this

    cluster.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_CLUS_0514 -->
```yaml
verdict:
  node_b_accession: CS20230722_CLUS_0514
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] Parent supertype 0141 is the immature-neuron supertype

    (DG-PIR Ex IMN_2); C1ql2 expression (val=0.47) is well below the

    DG granule profile, so this cluster does not match mature granule

    cells.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_CLUS_0515 -->
```yaml
verdict:
  node_b_accession: CS20230722_CLUS_0515
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] Parent supertype 0141 is the immature-neuron supertype

    (DG-PIR Ex IMN_2); C1ql2 expression (val=0.38) is well below the

    DG granule profile.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_CLUS_0316 -->
```yaml
verdict:
  node_b_accession: CS20230722_CLUS_0316
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] CA3 cluster (parent supertype 0079, CA3 Glut_5); soma

    in CA3 not dentate gyrus (strict region_fraction 0.044), and

    Prox1 (val=0.23) and C1ql2 (val=0.29) are near zero.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_SUPT_0141 -->
```yaml
verdict:
  node_b_accession: CS20230722_SUPT_0141
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] Immature-neuron supertype (DG-PIR Ex IMN_2); C1ql2

    child-coverage 0.500 and supertype-level C1ql2 (val=0.25) are

    below the DG granule profile. Possible match for the adult-born

    immature granule cell subpopulation rather than the classical

    mature dentate gyrus granule cell defined here.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_SUPT_0079 -->
```yaml
verdict:
  node_b_accession: CS20230722_SUPT_0079
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] CA3 supertype (CA3 Glut_5); strict region_fraction in

    DG granule cell layer is 0.091 (most cells in CA3 polymorph

    layer), Prox1 (val=0.29) and C1ql2 (val=0.29) are near zero.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_SUPT_0139 -->
```yaml
verdict:
  node_b_accession: CS20230722_SUPT_0139
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] DG Glut sibling of the supertype 0137;

    annotation-transfer peaks on the supertype 0137, not here.

    Markers Prox1 and C1ql2 are high (cohort_pct 0.912 and 0.941) but

    do not discriminate the DG Glut supertypes — supertype

    assignment is driven by annotation-transfer.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_SUPT_0138 -->
```yaml
verdict:
  node_b_accession: CS20230722_SUPT_0138
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] DG Glut sibling of the supertype 0137;

    annotation-transfer peaks on the supertype 0137, not here.

    Markers Prox1 and C1ql2 are above cohort 50th percentile but do

    not discriminate the DG Glut supertypes.

    '
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_dg_granule_cell_hippocampus_to_CS20230722_SUPT_0137 -->
```yaml
verdict:
  node_b_accession: CS20230722_SUPT_0137
  confidence: LOW
  relationship: evidencell:UncertainRelationship
  rationale: '[tier:CUT] Duplicate edge targeting the same supertype accession

    (0137) as the substantive MODERATE edge

    edge_dg_granule_cell_hippocampus_to_supt_0137; this duplicate

    carries only discovery_score / stub property_comparison evidence

    and should be removed by curator.

    '
  unresolved_questions:
  - Curator removal of duplicate edge edge_dg_granule_cell_hippocampus_to_CS20230722_SUPT_0137 — legacy/fresh-emit ID collision on taxonomy_type 0137.
```
<!-- verdict-block-end -->
