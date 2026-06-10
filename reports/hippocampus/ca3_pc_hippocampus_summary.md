# CA3 pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-27 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

---

## Introduction

CA3 pyramidal cells are the principal glutamatergic neurons of hippocampal area CA3 and form the main excitatory relay of the trisynaptic circuit, receiving mossy-fiber input from dentate granule cells onto thorny excrescences of proximal apical dendrites and projecting via Schaffer collaterals to CA1 [1][3]. The dense recurrent collateral network of CA3 underlies pattern-completion memory models and lets single CA3 neurons act as hub neurons. No molecular marker exclusively specific to CA3 has been established in classical literature; thorny-excrescence morphology and mossy-fiber innervation remain the primary defining criteria. Several glutamate receptor subunits and a vesicular glutamate transporter are nonetheless robustly expressed in CA3 pyramidal cells: AMPA receptor subunits Gria1 and Gria2 [4], the group I metabotropic glutamate receptor Grm1 (mGluR1) [7], the vesicular glutamate transporter Slc17a7 (vGLUT1) [7], the cell-adhesion molecule Nptn (neuroplastin) [8], and the gap-junction connexin Gjd2 (Cx36) [6].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA3 [UBERON:0014550]; hippocampus stratum radiatum [UBERON:0005372] (apical/basal dendritic field); CA1 stratum radiatum [UBERON:0014554] (Schaffer collateral projection target) | [1][2][3][4] |
| NT | glutamatergic | [5][6][1] |
| Markers | Gria1, Gria2 [4]; Grm1, Slc17a7 [7]; Nptn [8]; Gjd2 [6] | [4][7][8][6] |
| Negative markers | (none recorded) | — |
| Neuropeptides | (none recorded) | — |
| CL term | hippocampal pyramidal neuron [CL:1001571] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** review/synthesis · whole-genome bulk RNA-seq of CA3 pyramidal cells · [1]
  > we used next-generation RNA sequencing (RNA-seq) to produce a quantitative, whole genome characterization of gene expression for the major excitatory neuronal classes of the hippocampus; namely, granule cells and mossy cells of the dentate gyrus, and pyramidal cells of areas CA3, CA2, and CA1
  > — Cembrowski et al. 2016, abstract · [1] <!-- quote_key: 4875295_4a456257 -->
- **Soma location:** knowledge-base compilation · rodent hippocampal formation · [2]
  > Hippocampome.org is a comprehensive knowledge base of neuron types in the rodent hippocampal formation (dentate gyrus, CA3, CA2, CA1, subiculum, and entorhinal cortex)
  > — Wheeler et al. 2015, abstract · [2] <!-- quote_key: 631148_edb9eac6 -->
- **Soma location:** review · principal-cell circuit organisation · [3]
  > The hippocampal formation consists of GCs in the dentate gyrus and pyramidal cells in the CA1 and CA3 areas
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 7458943_d6507595 -->
- **Soma location:** review · trisynaptic-circuit anatomy · [3]
  > The principal cells are interconnected by glutamatergic synapses, forming the "trisynaptic pathway" (Andersen et al., 1971)(Storm- Mathisen, 1977). The GCs of the dentate gyrus receive excitatory glutamatergic input from layer II pyramidal cells of the entorhinal cortex (Steward et al., 1976)) and project to CA3 pyramidal cells. From there, they project to CA1 cells, which in turn project to the subiculum and back to the entorhinal cortex (Andersen et al., 1971)(Amaral et al., 1990). The GCs show highly conserved properties across species (Seress et al., 1990) and are born continuously throughout life (Altman et al., 1990), a feature that may be related to their role in memory formation (Schmidt-Hieber et al., 2004). There are approximately one million GCs within the rat dentate gyrus, all projecting thin unmyelinated axons into the stratum lucidum of the CA3, adjacent to the cell body layer.
  > — Munster-Wandowski et al. 2013, Major Glutamatergic Cell Types in Hippocampal Subfields · [3] <!-- quote_key: 7458943_efa15be5 -->
- **Soma location / Gria1, Gria2 markers:** immunohistochemistry · CA3 stratum pyramidale / stratum radiatum / stratum oriens · [4]
  > The GluA1 receptor subunit displayed diffuse staining within the str. radiatum and str. oriens, with marked immunoreactivity localized to cellular processes within the str. pyramidale of the CA3 (Figure 2). Isolated localization to pyramidal cell bodies can be seen through all three layers of the CA3, although mainly concentrated within the str. pyramidale. The CA1 showed strong dense immunoreactivity within the str. oriens and str. radiatum, with relatively decreased staining within the str. pyramidale cells. Within the DG, immunoreactivity was diffuse within the str. moleculare, with staining localized to cellular bodies within the str. granulosum. In particular, the hilus displayed neuronal body staining, with otherwise weak diffuse immunoreactivity
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [4] <!-- quote_key: 210181642_7ac40176 -->
  > GluA2 showed diffuse uniform staining within the str. radiatum and str. oriens of the CA3, with greater localization to neuronal bodies within the str. pyramidale (Figures 4Ba-f). The CA1 region exhibited similar staining patterns, localized to the cell bodies within the str. pyramidale, with diffuse staining throughout the str. oriens and str. radiatum (Figure 4A). In addition, immunoreactivity was localized to dendritic processes within the str. radiatum. Immunoreactivity within the DG was more diffuse within the str. moleculare, in contrast to the str. granulosum, which displayed more localized labeling surrounding cell bodies (Figure 4C). Labeling was also strong surrounding some neuronal cell bodies within the hilar region.
  > — Yeung et al. 2020, Synaptic Properties and Neurotransmitter Systems · [4] <!-- quote_key: 210181642_88f001b0 -->
- **NT (glutamatergic):** review · hippocampal-circuit neurotransmission · [5]
  > There are 2 types of principal cells in the hippocampal circuit: glutamatergic pyramidal cells in the Ammon's horn and subiculum regions, and glutamatergic granule cells in the DG (Figure 1). They generally have excitatory effects on the neurons to which they send axon terminals including other glutamatergic and GABAergic, as well monoaminergic [5-HT, norepinephrine (NE), dopamine (DA)], cholinergic, and histaminergic (HA) cells.
  > — Dale et al. 2015, Major Glutamatergic Cell Types in Hippocampal Subfields · [5] <!-- quote_key: 2281033_5b9805ff -->
- **NT (glutamatergic):** bulk RNA-seq, cell-population scope · CA3 pyramidal cells · [1]
  > The hippocampus is grossly comprised of five excitatory cell populations; namely, granule and mossy cells of the dentate gyrus (DG), and pyramidal cells of CA3, CA2, and CA1.
  > — Cembrowski et al. 2016, Major Glutamatergic Cell Types in Hippocampal Subfields · [1] <!-- quote_key: 4875295_002a714a -->
- **Grm1 / Slc17a7 markers:** review · rat hippocampal subfield expression · [7]
  > Metabotropic glutamate receptor 1 (mGluR1) is mainly expressed in granule cells and CA3 pyramidal neurons while mGluR5 is highly expressed in all subfields of the rat hippocampus (Fotuhi et al., 1994)
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [7] <!-- quote_key: 14854554_b6a5ffa0 -->
  > From the three known vesicular glutamate transporters (vGLUT1-3), vGLUT1 is the main subtype expressed in the hippocampus (Fremeau et al., 2004). It packs glutamate into synaptic vesicles of the glutamatergic axon terminals.
  > — Sarvari et al. 2016, Synaptic Properties and Neurotransmitter Systems · [7] <!-- quote_key: 14854554_ed1bdc00 -->
- **Nptn marker:** transcript-level identification of human Nptn-positive glutamatergic neurons across hippocampal subfields · [8]
  > unequivocally identified hNp65-positive glutamatergic neurons are granular neurons of DG, pyramidal neurons of CA1, CA2-3, subiculum, and layers II, IV, and V of the entorhinal cortex. Further direct visual inspection using a bright-field microscope confirmed that the hNp65 expression in major areas/ layers of the glutamatergic pathways within the entorhinal cortex and hippocampus (Supplementary Table 1) is very similar to its reported expression in mouse and rat (Beesley et al., 2014)(Smalla et al., 2000) (Herrera-Molina et al., 2014)(Bernstein et al., 2007)(Langnaese et al., 1997)
  > — Herrera-Molina et al. 2017, Specialized Glutamatergic Populations · [8] <!-- quote_key: 3288675_37ad1c13 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] (BROAD).

**Proposed CL term:** *CA3 pyramidal cell* (SUBMITTED) — see [obophenotype/cell-ontology#3653](https://github.com/obophenotype/cell-ontology/issues/3653).

---

## Results

Annotation transfer of Yao 2021 mouse hippocampal SMART-Seq v4 CA3-labelled cells onto the WMBv1 (CCN20230722) taxonomy combined with concordant MERFISH soma location supports a broadMatch from CA3 pyramidal cell to supertype 0078 CA3 Glut_4 [CS20230722_SUPT_0078] (F1=0.77 at supertype; see figure and property comparison table). Source CA3 cells distribute across all five CS20230722_SUBC_017 supertypes (SUPT_0078 63%, SUPT_0075 17%, SUPT_0077 12%, SUPT_0076 7%, SUPT_0079 2%), so the broadMatch sits at supertype rather than 1:1; the AT-best within-supertype cluster is 0315 CA3 Glut_4 [CS20230722_CLUS_0315] (F1=0.70) but is not currently represented as an edge in this graph.

![Filtered AT figure for CA3 pyramidal cell](figures/f1_for_ca3_pc_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GSE185862) CA3 source group (n=322 cells) mapped onto WMBv1 (CCN20230722). Nodes are coloured by F1 with **Purity** (Pur) and **Coverage** (Cov) shown inline. Coverage = fraction of source cells landing on this target; Purity = fraction of target cells from the source group. With a single source group, Purity is 1.0 at every target and only Coverage discriminates. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution. Subclass-level mapping to 017 CA3 Glut is essentially complete (F1=0.99); supertype-level resolves a dominant 0078 CA3 Glut_4 with substantial scatter across the four sibling supertypes; cluster-level scatter within SUPT_0078 leaves CLUS_0315 as the best cluster.*

### 0078 CA3 Glut_4 [CS20230722_SUPT_0078] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | pyramidal layer of CA3 [UBERON:0014550] | Hippocampal formation [MBA:1089] count_100um=9204 [painted]; Field CA3 [MBA:463] count_100um=9164 [painted]; Field CA3, pyramidal layer [MBA:495] count_100um=8918 [painted] | not assessed (no cluster-level edge in graph) | CONSISTENT |
| NT type | glutamatergic | not asserted | not assessed | NOT_ASSESSED |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| WMBv1 atlas curation of SUBC_017 CA3 Glut | Atlas metadata | SUPPORT | SUBC_017 dedicated CA3 glutamatergic subclass; SUPT_0078 MERFISH overwhelmingly in CA3 pyramidal layer | atlas-internal |
| Yao 2021 MapMyCells AT (GEO:GSE185862 → WMBv1) | Annotation transfer | SUPPORT | F1=0.77 at supertype (Cov=0.63, Pur=1.00; n=198) | atlas-internal |

**Supporting evidence.**

- WMBv1 atlas curation places SUPT_0078 inside the dedicated CA3 glutamatergic subclass 017 CA3 Glut; SUPT_0078 MERFISH counts localise overwhelmingly to Field CA3, pyramidal layer [MBA:495] (8918 of 9204 hippocampal counts), and the broader CA3 pyramidal-cell population spans the full SUBC_017 supertype range. *(note: SUPT_0078 is the dominant CA3-pyramidal-cell supertype in this atlas; the four sibling supertypes within SUBC_017 collectively absorb the remaining 37% of Yao 2021 CA3 cells.)*
- Yao 2021 MapMyCells annotation transfer maps 203 of 322 source CA3 cells (63.0%) onto SUPT_0078, with purity 1.0 (the supertype receives only CA3 cells in this dataset); cluster-level transfer continues to scatter within SUPT_0078, with 0315 CA3 Glut_4 [CS20230722_CLUS_0315] as the best within-supertype cluster (F1=0.70).
- Subclass-level transfer is essentially complete: 320 of 322 source CA3 cells map to subclass 017 CA3 Glut (F1=0.99). The drop from subclass to supertype is the scatter across SUPT_0075–0079.

**Marker evidence provenance.**

- **Gria1 / Gria2:** Yeung et al. 2020 immunohistochemistry [4] shows GluA1 and GluA2 protein in CA3 stratum pyramidale, stratum radiatum, and stratum oriens; both subunits are expressed broadly across hippocampal pyramidal subfields and are not unique discriminators of CA3. No transcript-level cross-check is recorded on the candidate atlas node, so atlas-side concordance is not directly assessed.
- **Grm1 (mGluR1):** Sarvari et al. 2016 [7] is a review citing Fotuhi et al. 1994 for transcript/protein localisation of Grm1 to granule cells and CA3 pyramidal neurons in rat hippocampus. The primary citation is upstream of [7]; a targeted literature search for the original Fotuhi reference would anchor Grm1 to a primary study.
- **Slc17a7 (vGLUT1):** Sarvari et al. 2016 [7] cites Fremeau et al. 2004 for vGLUT1 as the principal hippocampal vesicular glutamate transporter; vGLUT1 marks all hippocampal glutamatergic neurons and is not a CA3-specific discriminator.
- **Nptn (neuroplastin / hNp65):** Herrera-Molina et al. 2017 [8] identifies hNp65 in glutamatergic neurons across DG granule cells, CA1/CA2-3 pyramidal cells, subiculum, and entorhinal cortex layers II/IV/V; broad glutamatergic expression rather than CA3-specific.
- **Gjd2 (Cx36):** marker citation is the doi.org/10.3389/fnana.2012.00013 review [6]; Cx36 marks gap-junctional coupling on CA3 pyramidal dendrites but is not CA3-specific.
- Atlas annotation/expression discrepancy check is not informative here: the candidate edge's `property_comparisons` carry no transcript-level expression rows for Gria1/Gria2/Grm1/Slc17a7/Nptn/Gjd2 on SUPT_0078. The defining markers are all broad glutamatergic / hippocampal-pyramidal markers; none is expected to discriminate among SUBC_017 supertypes.

**Concerns.**

- Source CA3 cells distribute across all five SUBC_017 supertypes — SUPT_0078 is the dominant but not exclusive correspondence (AMBIGUOUS_MAPPING).
- Annotation transfer evidence is from a single source dataset (Yao 2021 GSE185862 SSv4); independent replication on a second CA3-resolved dataset is not yet available (SINGLE_DATASET).
- Best supportable resolution is supertype CS20230722_SUPT_0078 (F1=0.77); cluster-level transfer best target CS20230722_CLUS_0315 is not currently represented as an edge in this graph (TAXONOMY_LEVEL_MISMATCH).
- All defining markers on the classical node are broad glutamatergic / hippocampal-pyramidal markers (Gria1/2, Grm1, Slc17a7, Nptn, Gjd2). None is established as a CA3-specific transcript-level discriminator and none is assessed against atlas-side precomputed expression on SUPT_0078.

**What would upgrade confidence.**

- Annotation transfer from a CA3-sublayer-resolved dataset (CA3a / CA3b / CA3c, or proximodistal labels) onto WMBv1 CCN20230722 via MapMyCells, with target F1 ≥ 0.80 at supertype for each sublayer source group; expected output `AnnotationTransferEvidence` on edges to SUPT_0075 / 0076 / 0077 / 0078 / 0079 to test whether the four sibling supertypes correspond to CA3a/b/c sublayers or to a proximodistal mossy-fiber input axis.
- Emit an edge to CLUS_0315 so the within-supertype best-cluster correspondence is recorded, and resolve the duplicate `edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078` (legacy/fresh-emit collision).
- Targeted literature trawls to anchor Grm1 to the Fotuhi et al. 1994 primary citation and to test whether any marker on the classical node discriminates within SUBC_017 supertypes (likely a primary-literature gap rather than an experiment).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0078 CA3 Glut_4 [CS20230722_SUPT_0078]` | — | 2147 | 🟡 MODERATE | Yao 2021 AT F1=0.77 to supertype; SUBC_017 CA3 Glut; MERFISH CA3 pyramidal layer | Primary |
| `0297 CA3 Glut_1 [CS20230722_CLUS_0297]` | 0075 CA3 Glut_1 | 199 | ⚪ UNCERTAIN | Parent SUPT_0075 only 17% of Yao 2021 CA3 cohort | Eliminated (minor share of CA3 cohort) |
| `0300 CA3 Glut_1 [CS20230722_CLUS_0300]` | 0075 CA3 Glut_1 | 60 | ⚪ UNCERTAIN | Low cluster cell count (60); parent SUPT_0075 minor share | Eliminated (low cell count) |
| `0301 CA3 Glut_1 [CS20230722_CLUS_0301]` | 0075 CA3 Glut_1 | 101 | ⚪ UNCERTAIN | MERFISH split across Field CA3 / Field CA1 | Eliminated (CA3/CA1 boundary) |
| `0303 CA3 Glut_2 [CS20230722_CLUS_0303]` | 0076 CA3 Glut_2 | 164 | ⚪ UNCERTAIN | Parent SUPT_0076 only 7% of Yao 2021 CA3 cohort | Eliminated (minor share of CA3 cohort) |
| `0309 CA3 Glut_3 [CS20230722_CLUS_0309]` | 0077 CA3 Glut_3 | 246 | ⚪ UNCERTAIN | Parent SUPT_0077 only 12% of Yao 2021 CA3 cohort | Eliminated (minor share of CA3 cohort) |
| `0075 CA3 Glut_1 [CS20230722_SUPT_0075]` | — | 763 | ⚪ UNCERTAIN | Minor share of Yao 2021 CA3 cohort (17%) | Eliminated (minor share of CA3 cohort) |
| `0076 CA3 Glut_2 [CS20230722_SUPT_0076]` | — | 962 | ⚪ UNCERTAIN | Minor share of Yao 2021 CA3 cohort (7%) | Eliminated (minor share of CA3 cohort) |
| `0077 CA3 Glut_3 [CS20230722_SUPT_0077]` | — | 1039 | ⚪ UNCERTAIN | Minor share of Yao 2021 CA3 cohort (12%) | Eliminated (minor share of CA3 cohort) |
| `0078 CA3 Glut_4 [CS20230722_SUPT_0078]` | — | 2147 | ⚪ UNCERTAIN | Duplicate of primary edge; legacy/fresh-emit ID collision | Eliminated (duplicate edge) |
| `0079 CA3 Glut_5 [CS20230722_SUPT_0079]` | — | 318 | 🔴 REFUTED | MERFISH somata in dentate gyrus polymorph layer (hilus) | Eliminated (wrong anatomy — hilus) |

</details>

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** CA3 pyramidal cells (definition_basis CLASSICAL_MULTIMODAL) are defined by their soma in the pyramidal layer of CA3 [UBERON:0014550] with apical / basal dendrites in stratum radiatum and stratum oriens, axonal projection via Schaffer collaterals into CA1 stratum radiatum [UBERON:0014554], and glutamatergic identity [1][3][5][6]. The recorded defining markers are AMPA-receptor subunits Gria1 and Gria2 [4], group I metabotropic glutamate receptor Grm1 and vesicular glutamate transporter Slc17a7 [7], the cell-adhesion molecule Nptn [8], and the gap-junction connexin Gjd2 [6]. None of these is uniquely specific to CA3; thorny excrescences and mossy-fiber innervation remain the morphological hallmarks.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 (GSE185862) mouse hippocampal formation SMART-Seq v4 cell type labels (Allen Institute taxonomy): Astro, CA1-ProS, CA2-IG-FC, CA3, DG, L2/3 IT ENTl, L2/3 IT RHP, L6 CT CTX, L6b CTX, Lamp5, Micro-PVM, NP SUB, Oligo, Pvalb, SUB-ProS, Sncg, Sst, Sst Chodl, Vip.) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells (default parameters) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `b95d284` at 2026-06-10T13:04:42+00:00 from [kb/graphs/hippocampus/hippocampus_glutamatergic.yaml](kb/graphs/hippocampus/hippocampus_glutamatergic.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_ca3_pc_hippocampus_to_supt_0078 | ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; SUPPORT | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0297 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0300 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0301 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0303 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0309 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0075 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0076 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0077 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0079 | ATLAS_METADATA | PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** CA3 pyramidal cell → 0078 CA3 Glut_4 [CS20230722_SUPT_0078] at MODERATE confidence. Key support: WMBv1 atlas curation (SUBC_017 CA3 Glut; MERFISH soma in CA3 pyramidal layer) and Yao 2021 MapMyCells annotation transfer (F1=0.77 at supertype, 63% of source CA3 cells, purity 1.0). Key caveats: AMBIGUOUS_MAPPING (source CA3 cells scatter across all five SUBC_017 supertypes); SINGLE_DATASET (Yao 2021 alone, no independent replication); TAXONOMY_LEVEL_MISMATCH (the cluster-level AT best target CLUS_0315 is not represented as an edge). The Cell Ontology has no specific term for this population; hippocampal pyramidal neuron [[CL:1001571](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001571)] is the closest ancestor. CA3 pyramidal cells are a subpopulation of hippocampal pyramidal neurons; CL:1001571 covers all hippocampal pyramidal neurons without anatomical resolution to individual subfields. No CA3-specific CL term currently exists. A new CL term for *CA3 pyramidal cell* has been submitted ([obophenotype/cell-ontology#3653](https://github.com/obophenotype/cell-ontology/issues/3653)).

### Proposed experiments and follow-ups

Yao 2021 MapMyCells AT already resolves the subclass-level mapping (SUBC_017 CA3 Glut, F1=0.99) and identifies SUPT_0078 as the dominant CA3 supertype (F1=0.77, 63% of source CA3 cells); it does not resolve the within-subclass scatter across SUPT_0075–0079, and a refined experiment is warranted.

- **What:** annotation transfer of a CA3-sublayer-resolved dataset (CA3a / CA3b / CA3c, or proximodistal mossy-fiber input zone labels) onto WMBv1 CCN20230722 via MapMyCells.
  - **Target:** F1 ≥ 0.80 at supertype level for each sublayer source group.
  - **Expected output:** `AnnotationTransferEvidence` on edges to CS20230722_SUPT_0075 / 0076 / 0077 / 0078 / 0079.
  - **Resolves:** open questions 1–2; would test whether the four sibling supertypes correspond to CA3a/b/c sublayers or to a different organisational axis (proximodistal mossy-fiber input zone).
- **What:** curator removal of the duplicate edge `edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078` (legacy/fresh-emit ID collision on taxonomy_type CS20230722_SUPT_0078); emit a fresh edge to CS20230722_CLUS_0315 so the within-supertype best-cluster correspondence (cluster-level AT F1=0.70) is recorded.
  - **Resolves:** open questions 3–4.
- **What:** targeted literature trawl to anchor Grm1 to the Fotuhi et al. 1994 primary citation (referenced upstream of Sarvari et al. 2016) and to test whether any of the recorded markers (Gria1, Gria2, Grm1, Slc17a7, Nptn, Gjd2) has been established as a transcript-level discriminator within SUBC_017 supertypes.
  - **Resolves:** marker-provenance gaps noted in the primary candidate section.

### Open questions

1. Do CS20230722_SUPT_0075, CS20230722_SUPT_0076, CS20230722_SUPT_0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to another organisational axis (proximodistal mossy-fiber input zone)?
2. Pioneer early-generated CA3 glutamatergic neurons (Marissal et al., 2012) form a morpho-functionally distinct subpopulation with persistent features into adulthood — likely a separable subtype not currently resolved within SUBC_017.
3. Curator removal of the duplicate edge `edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078` (legacy/fresh-emit ID collision on taxonomy_type CS20230722_SUPT_0078).
4. Should an edge be emitted to CS20230722_CLUS_0315 (cluster-level AT best target, F1=0.70) so the within-supertype best-cluster correspondence is recorded?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Cembrowski et al. 2016 | [27113915](https://pubmed.ncbi.nlm.nih.gov/27113915) | soma location |
| [2] | Wheeler et al. 2015 | [26402459](https://pubmed.ncbi.nlm.nih.gov/26402459) | soma location |
| [3] | Munster-Wandowski et al. 2013 | [24319410](https://pubmed.ncbi.nlm.nih.gov/24319410) | soma location |
| [4] | Yeung et al. 2020 | [32009891](https://pubmed.ncbi.nlm.nih.gov/32009891) | soma location |
| [5] | Dale et al. 2015 | [26346726](https://pubmed.ncbi.nlm.nih.gov/26346726) | neurotransmitter type |
| [6] | https://doi.org/10.3389/fnana.2012.00013 | — | neurotransmitter type |
| [7] | Sarvari et al. 2016 | [27375434](https://pubmed.ncbi.nlm.nih.gov/27375434) | Grm1 marker |
| [8] | Herrera-Molina et al. 2017 | [28779130](https://pubmed.ncbi.nlm.nih.gov/28779130) | Nptn marker |

---

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_supt_0078 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.65
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Annotation transfer of Yao 2021 GSE185862 CA3-labelled cells
    onto WMBv1  lands F1=0.99
    at subclass CS20230722_SUBC_017 and F1=0.77 at supertype CS20230722_SUPT_0078
    (Cov=0.63, Pur=1.00, n=198); MERFISH soma localisation places SUPT_0078
    overwhelmingly in Field CA3, pyramidal layer (region_fraction_100um: 0.969).
    Source CA3 cells scatter across all five CS20230722_SUBC_017 supertypes
    (SUPT_0078 63%, SUPT_0075 17%, SUPT_0077 12%, SUPT_0076 7%, SUPT_0079 2%),
    so the supportable mapping is at supertype rather than 1:1. The cluster-level
    best target CS20230722_CLUS_0315 (F1=0.77) is not currently an edge in this
    graph.
  reconciliation_note: >
    Within-subclass scatter across SUPT_0075-0079 is unresolved; sublayer-resolved
    annotation transfer needed to test correspondence to CA3a/b/c or proximodistal
    mossy-fiber input axis.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Yao 2021 source CA3 cells distribute across all five CS20230722_SUBC_017
        supertypes (SUPT_0078 63.0%, SUPT_0075 16.8%, SUPT_0077 11.5%, SUPT_0076
        6.5%, SUPT_0079 1.6%); CS20230722_SUPT_0078 is the dominant correspondence
        but not 1:1.
    - caveat_type: SINGLE_DATASET
      description: >
        Annotation transfer evidence comes from a single source dataset (Yao 2021
        GSE185862); independent replication on a second CA3-resolved dataset is not
        yet available.
    - caveat_type: TAXONOMY_LEVEL_MISMATCH
      description: >
        Best supportable resolution is supertype CS20230722_SUPT_0078 (F1=0.77);
        cluster-level transfer best target is CS20230722_CLUS_0315 (F1=0.77),
        which is not currently represented as an edge in this graph.
  proposed_experiments:
    - >
      Annotation transfer from a CA3-sublayer-resolved dataset (CA3a / CA3b / CA3c,
      or proximodistal labels) onto WMBv1 CCN20230722; target F1 >= 0.80 at supertype
      for each sublayer source group; expected output AnnotationTransferEvidence on
      edges to CS20230722_SUPT_0075 / 0076 / 0077 / 0078 / 0079.
    - >
      Emit a fresh edge to CS20230722_CLUS_0315 (cluster-level annotation transfer
      best target, F1=0.77 in) so
      the within-supertype best-cluster correspondence is recorded.
  unresolved_questions:
    - Do CS20230722_SUPT_0075, CS20230722_SUPT_0076, CS20230722_SUPT_0077 correspond to CA3a, CA3b, CA3c sublayers respectively, or to a proximodistal mossy-fiber input axis?
    - Pioneer early-generated CA3 glutamatergic neurons (Marissal et al. 2012) form a morpho-functionally distinct subpopulation likely separable from the main CA3 supertypes; not yet resolved within SUBC_017.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0297 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0297 sits within parent supertype CS20230722_SUPT_0075,
    which captures only 16.8% of Yao 2021 CA3 source cells in; cluster-level annotation transfer
    evidence is not recorded on this edge and the within-subclass scatter is
    unresolved.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0300 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0300 carries only 60 atlas cells (below the
    robustness margin); parent supertype CS20230722_SUPT_0075 captures only
    16.8% of Yao 2021 CA3 cells in
    and cluster-level annotation transfer is not recorded.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0301 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0301 MERFISH counts split between Field CA3
    [MBA:463] and Field CA1 [MBA:382] (region_fraction_100um: 0.628, strict
    region_fraction: 0.259), suggesting a CA3/CA1 boundary population rather
    than a clean CA3 pyramidal cluster.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0303 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0303 sits within parent supertype CS20230722_SUPT_0076,
    which captures only 6.5% of Yao 2021 CA3 source cells in; cluster-level annotation transfer
    evidence is not recorded on this edge.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_CLUS_0309 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_CLUS_0309 sits within parent supertype CS20230722_SUPT_0077,
    which captures only 11.5% of Yao 2021 CA3 source cells in; cluster-level annotation transfer
    evidence is not recorded on this edge.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0075 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.25
  rationale: >
    [tier:CUT] CS20230722_SUPT_0075 captures only 16.8% of Yao 2021 CA3 source
    cells in; minor share of
    the CA3 cohort with no recorded basis for preferring it over the dominant
    SUPT_0078.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0076 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0076 captures only 6.5% of Yao 2021 CA3 source
    cells in; minor share of
    the CA3 cohort.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0077 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.2
  rationale: >
    [tier:CUT] CS20230722_SUPT_0077 captures only 11.5% of Yao 2021 CA3 source
    cells in; minor share of
    the CA3 cohort.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] Duplicate edge — legacy/fresh-emit ID collision on taxonomy_type
    CS20230722_SUPT_0078; the substantive verdict for CS20230722_SUPT_0078 lives
    on edge_ca3_pc_hippocampus_to_supt_0078.
  caveats:
    - caveat_type: OTHER
      description: >
        Duplicate edge — legacy/fresh-emit ID collision on taxonomy_type
        CS20230722_SUPT_0078; substantive record lives on
        edge_ca3_pc_hippocampus_to_supt_0078.
  unresolved_questions:
    - Curator removal of duplicate edge edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0078.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_ca3_pc_hippocampus_to_CS20230722_SUPT_0079 -->
```yaml
verdict:
  confidence: REFUTED
  confidence_score: 0.05
  rationale: >
    [tier:CUT] CS20230722_SUPT_0079 MERFISH somata localise predominantly to
    Dentate gyrus, polymorph layer [MBA:10704] (count_100um=1524 of 1619
    hippocampal counts; region_fraction_100um: 0.581, strict region_fraction:
    0.181), consistent with hilar mossy-cell rather than CA3 pyramidal-cell
    identity.
  caveats:
    - caveat_type: DISCORDANT_ANATOMY
      description: >
        CS20230722_SUPT_0079 MERFISH somata localise to the dentate gyrus
        polymorph layer (MBA:10704), not to the CA3 pyramidal layer; consistent
        with hilar mossy-cell rather than CA3 pyramidal-cell identity.
```
<!-- verdict-block-end -->
