# Dentate Gyrus Immature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*2026-04-14 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

---

## Introduction

The dentate gyrus immature granule neuron is a postmitotic, synaptically integrating stage of adult hippocampal neurogenesis, classically defined by co-expression of doublecortin (DCX) and NeuN prior to the acquisition of calbindin that marks terminal granule cell maturation [3][4]. New granule cells in the dentate gyrus differentiate into glutamatergic neurons and receive primary glutamatergic afferents from entorhinal cortex [1][2]. Mapping this transient developmental stage to the WMBv1 transcriptomic atlas is important because it places a classically IHC-defined population into the same reference frame as terminally differentiated granule cells and earlier neuroblast stages, enabling lineage-aware analyses.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus granule cell layer (inner GCL) [UBERON:0005381] | — |
| NT | glutamatergic | [1], [2] |
| Markers | DCX, NeuN, PSA-NCAM, Tis21 | [3], [4], [5] |
| Negative markers | Calbindin | [3] |
| CL term | immature dentate gyrus granule neuron [CL:9900002] (EXACT) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **NT type (glutamatergic in DG):** LITERATURE · [2]
  > new immature neurons are continuously produced and then migrate out to their respective target circuits, differentiating either into glutamatergic neurons (dentate gyrus) or into mostly GABAergic interneurons called granule cells in the olfactory bulb
  > — Vangeneugden et al. 2015, Olfactory Bulb Immature Neurons · [2] <!-- quote_key: 625292_ff3f8b1d -->
- **NT type (glutamatergic afferents / DG context):** LITERATURE · [1]
  > In the adult dentate gyrus, cells proliferate in the inner granule cell layer, and migrate radially outward as they differentiate (Zhao et al., 2006). New granule cells in hippocampal dentate gyrus receive primary glutamatergic afferents from entorhinal cortex and project axons to inhibitory interneurons and pyramidal cells of area CA3
  > — Stoll et al. 2014, Dentate Gyrus Immature Neurons · [1] <!-- quote_key: 8479504_1542ed61 -->
- **DCX / NeuN / Calbindin− (stage-5 definition):** LITERATURE · [3]
  > Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004).
  > — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [3] <!-- quote_key: 279046466_998847af -->
- **DCX / PSA-NCAM / NeuN (immature neuron protein markers):** LITERATURE · [4]
  > Three types of proliferatively active cells have been identified in the granular layer of the dentate gyrus (DG) of the hippocampus: type I cells -radial glial-like stem cells expressing glial fibrillary acidic protein (GFAP) and Sox2; type II cells -non-sessile cells expressing nestin, also referred to as transiently activated progenitor cells, neuroblasts expressing doublecortin (DCX); and Ki67 proteins and immature neurons expressing the DCX protein, PSA-NCAM, a marker of migrating neurons (polysialylated neuronal cell adhesion molecules) and neuron-specific protein (NeuN) (Attardo et al., 2009)(Gault et al., 2021). On the other hand, three types of cells were distinguished in the subventricular zone (SVZ): B1-type astrocytic stem cells, GFAP-positive, C-type progenitor cells expressing the Mash1 protein, and neuroblasts expressing the DCX protein (Okano et al., 2008).
  > — Stepień et al. 2021, Dentate Gyrus Immature Neurons · [4] <!-- quote_key: 245432259_44d5c91b -->
- **Tis21 re-expression in postmitotic phase:** LITERATURE · [5]
  > During embryonic cortical development, expression of Tis21 is associated with cell cycle lengthening and neurogenic divisions of progenitor cells. We here investigated if the expression pattern of Tis21 also correlates with the generation of new neurons in the adult hippocampus. We used Tis21 knock-in mice expressing green fluorescent protein (GFP) and studied Tis21-GFP expression together with markers of adult hippocampal neurogenesis in newly generated cells. We found that Tis21-GFP 1) was absent from the radial glia–like putative stem cells (type-1 cells), 2) first appeared in transient amplifying progenitor cells (type-2 and 3 cells), 3) did not colocalize with markers of early postmitotic maturation stage, 4) was expressed again in maturing neurons, and 5) finally decreased in mature granule cells. Our data show that, in the course of adult neurogenesis, Tis21 is expressed in a phase additional to the one of the embryonic neurogenesis. This additional phase of expression might be associated with a new and different function of Tis21 than during embryonic brain development, where no Tis21 is expressed in mature neurons. We hypothesize that this function is related to the final functional integration of the newborn neurons. Tis21 can thus serve as new marker for key stages of adult neurogenesis.
  > — Attardo et al. 2009, Dentate Gyrus Immature Neurons · [5] <!-- quote_key: 7393550_b2644450 -->
- **Tbr1 onset (bridges atlas TF marker to classical postmitotic stage):** LITERATURE (EXPERIMENTAL) · [6]

</details>

### Cell Ontology mapping

Cell Ontology mapping: immature dentate gyrus granule neuron [[CL:9900002](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:9900002)] (EXACT).

---

## Results

Two atlas clusters within the DG-PIR Ex IMN_2 supertype carry an EXACT CL:9900002 annotation and are assessed here as a `TYPE_A_SPLITS` mapping: cluster 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] and cluster 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515]. Both are at LOW confidence; annotation transfer of Hochgerner 2018 Granule-immature cells provides partial support for 0514 and no support for 0515 (which preferentially attracts Hochgerner Neuroblast_2 cells).

![Annotation transfer F1 heatmap (GEO:GSE95315 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Hochgerner 2018 Granule-immature source group mapped to WMBv1. The best mapping is at SUBCLASS rank to 037 DG Glut (F1=0.566); the best cluster-level hit is 0507 DG Glut_2 (F1=0.510), not the IMN_2 clusters. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.*

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] | DG-PIR Ex IMN_2 | — | 🔴 LOW | NT CONSISTENT · Location CONSISTENT · Dcx CONSISTENT (mRNA high) | Speculative |
| 2 | 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515] | DG-PIR Ex IMN_2 | — | 🔴 LOW | NT CONSISTENT · Location CONSISTENT · AT NO_EVIDENCE | Speculative |

Total edges: 2 (relationship: TYPE_A_SPLITS).

### 0514 DG-PIR Ex IMN_2 · 🔴 LOW

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | not available | Glut (CS20230722_CLUS_0514) | CONSISTENT |
| Soma location | inner granule cell layer (GCL) [UBERON:0005381] | not available | DGdo,me (dentate gyrus dorsal/medial blade); HIP:0.98 | CONSISTENT |
| DCX expression | DCX; PROTEIN; positive (defining) | not available | Dcx mean = 8.79 (CS20230722_CLUS_0514) | CONSISTENT |
| NeuN (Rbfox3) expression | NeuN; PROTEIN; positive | not available | Rbfox3 mean = 0.35 (CS20230722_CLUS_0514) | APPROXIMATE |
| PSA-NCAM | PSA-NCAM; PROTEIN; positive | not available | not in defining_markers | NOT_ASSESSED |
| Tis21 (Btg2) | Tis21; PROTEIN; positive | not available | Btg2 mean = 0.0193 (CS20230722_CLUS_0514) | APPROXIMATE |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — this is a cluster-level edge.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata for 0514 | Atlas metadata | SUPPORT | EXACT CL:9900002; Tbr1+/Prox1+/Emx2+/Igfbpl1+; DGdo,me HIP:0.98; composite score 0.82 | atlas-internal |
| Micheli 2025 stage-5 definition | Literature | SUPPORT | DCX+/NeuN+/Calbindin− postmitotic immature stage | [3] |
| Hodge 2008 Tbr1 onset | Literature | SUPPORT | Tbr1 marks postmitotic transition from neuroblast | [6] |
| Attardo 2009 Tis21 re-expression | Literature | SUPPORT | Tis21 reappears in maturing postmitotic adult DG neurons | [5] |
| Hochgerner 2018 → WMBv1 (MapMyCells) | Annotation transfer | PARTIAL | F1=0.211 at 0514 (27 cells, 2%); subclass F1=0.566 (037 DG Glut) | — |

**Supporting evidence**

- Cluster 0514 carries an **EXACT CL:9900002** annotation in WMBv1 metadata with a coherent TF marker profile (Tbr1, Prox1, Emx2, Igfbpl1; Ccbe1 scoped), MERFISH anatomy DGdo,me at HIP:0.98, glutamatergic NT, and no Calbindin — collectively consistent with a postmitotic but pre-terminal immature granule neuron stage.
- **Stage-5 literature [3]** anchors the DCX+/NeuN+/Calbindin− definition that the atlas annotation tracks at the transcriptional level.
- **Tbr1 onset [6]** is the bridge between atlas TF evidence and classical postmitotic immature identity: Tbr1 is observed only in postmitotic granule cells and never co-localises with nestin-GFP.
- **Tis21 re-expression [5]** in postmitotic adult DG neurons is consistent with the postmitotic Tbr1+ identity of this cluster.
- **MapMyCells AT** of Hochgerner 2018 Granule-immature cells assigns 27 of 1333 cells (~2%) to cluster 0514 at F1=0.211, with the majority routed to the DG Glut lineage (037 DG Glut, F1=0.566; best cluster 0507 DG Glut_2, F1=0.510). This provides weak PARTIAL support for 0514 as a transitional neuroblast-like population within the broader immature granule neuron envelope.

**Marker evidence provenance**

- **DCX**: protein-level marker [3][4]; absent from atlas `defining_markers` but precomputed Dcx mRNA mean = 8.79 in 0514 — high expression confirms the marker at the transcript level. The discordance with the atlas marker list is a marker-ranking artefact (Dcx is broadly expressed across the IMN class and so is filtered out of cluster-distinguishing markers), not a biological discordance. Alignment upgraded to CONSISTENT.
- **NeuN (Rbfox3)**: protein-level postmitotic marker [3][4]; precomputed Rbfox3 mRNA mean = 0.35 in 0514. APPROXIMATE retained — scRNA-seq sensitivity for nuclear protein mRNA is lower than IHC for the protein itself.
- **PSA-NCAM**: a post-translational glycan epitope on NCAM1 — intrinsically undetectable by scRNA-seq. NOT_ASSESSED is correct; this is a methodological gap not a discordance [4].
- **Tis21 (Btg2)**: Btg2 precomputed mean = 0.0193 in 0514 — near-zero. ⚠ The classical evidence [5] is GFP-knock-in reporter and IHC, capturing transiently accumulated protein; absence of detectable mRNA at single-cell resolution may reflect a brief transcriptional pulse not captured by snapshot scRNA-seq. APPROXIMATE retained.
- **Calbindin (Calb1)** as a negative marker is consistent — Calbindin is absent from the 0514 defining markers, matching the pre-terminal stage definition.

**Concerns**

- The atlas-side AT data show that the Hochgerner 2018 Granule-immature reference cells map dominantly to the DG Glut lineage (037 DG Glut subclass; best cluster 0507 DG Glut_2), not to the IMN_2 supertype. Only ~2% of cells route to 0514. *(note: this suggests that the bulk of Hochgerner's "Granule-immature" population corresponds transcriptionally to early mature granule neurons (DG Glut_2) rather than to the Tbr1+/Igfbpl1+ IMN_2 stage — interpretation beyond the facts.)*
- The TYPE_A_SPLITS relationship across 0514/0515 means neither cluster alone fully represents the classical type [DISTRIBUTED_ACROSS_CLUSTERS caveat].
- Atlas marker list does not include DCX, NeuN, PSA-NCAM, or Tis21 [MARKER_NOT_SPECIFIC caveat — protein-level markers and post-translational glycan epitopes are not directly comparable to scRNA-seq marker selection].
- 12 proposed literature evidence items are pending attachment to this edge [OTHER caveat].
- An unexplained Gad1 nt_marker signal (score 5.56) at cluster 0514 raises the possibility of transient GABAergic transcriptional state, doublet artefact, or contamination — currently unresolved.

**What would upgrade confidence**

- RNA velocity / pseudotime on the DG-PIR Ex IMN_2 supertype (clusters 0512–0515) to determine ordering along the neuroblast → immature GN axis. Expected output: interpretive evidence informing the TYPE_A_SPLITS interpretation.
- Targeted query of the full Allen Brain Cell Atlas CCN202307220 feature matrix for Dcx, Rbfox3, Btg2 in 0514/0515 below the marker ranking threshold. Expected output: AtlasQueryEvidence resolving marker provenance.
- Anti-DCX / anti-Tbr1 IHC co-stain in adult DG to confirm Tbr1+ inner-GCL cells are also DCX+/NeuN+ at protein level. Expected output: LiteratureEvidence bridging atlas TF and classical profiles.
- Refined annotation transfer using a source dataset that explicitly separates a Tbr1+ immature stage from later DG Glut maturation (Hochgerner 2018 "Granule-immature" is a single combined label). Target: F1 ≥ 0.5 at CLUSTER level for the Tbr1+ subset.

### 0515 DG-PIR Ex IMN_2 · 🔴 LOW

**Property comparison**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic | not available | Glut (inherited; cluster-level NA) (CS20230722_CLUS_0515) | CONSISTENT |
| Soma location | inner granule cell layer (GCL) [UBERON:0005381] | not available | DGdo,me (dentate gyrus dorsal/medial blade); HIP:1.0 | CONSISTENT |
| DCX expression | DCX; PROTEIN; positive (defining) | not available | Dcx mean = 8.78 (CS20230722_CLUS_0515) | CONSISTENT |
| NeuN (Rbfox3) expression | NeuN; PROTEIN; positive | not available | Rbfox3 mean = 0.30 (CS20230722_CLUS_0515) | APPROXIMATE |
| PSA-NCAM | PSA-NCAM; PROTEIN; positive | not available | not in defining_markers | NOT_ASSESSED |
| Tis21 (Btg2) | Tis21; PROTEIN; positive | not available | Btg2 mean = 0.0000 (CS20230722_CLUS_0515) | APPROXIMATE |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — this is a cluster-level edge.)*

**Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata for 0515 | Atlas metadata | SUPPORT | EXACT CL:9900002; same core TF profile as 0514; Rarb scoped; DGdo,me HIP:1.0; composite score 0.82 | atlas-internal |
| Micheli 2025 stage-5 definition | Literature | SUPPORT | DCX+/NeuN+/Calbindin− postmitotic immature stage | [3] |
| Hodge 2008 Tbr1 onset | Literature | SUPPORT | Tbr1 marks postmitotic transition from neuroblast | [6] |
| Attardo 2009 Tis21 re-expression | Literature | SUPPORT | Tis21 reappears in maturing postmitotic adult DG neurons | [5] |
| Hochgerner 2018 → WMBv1 (MapMyCells) | Annotation transfer | NO_EVIDENCE | F1=0.0 at 0515 for Granule-immature; cluster preferentially receives Hochgerner Neuroblast_2 (F1=0.483) | — |

**Supporting evidence**

- Cluster 0515 carries an **EXACT CL:9900002** annotation in WMBv1 metadata, with a core TF profile (Tbr1, Prox1, Emx2, Igfbpl1) identical to 0514. Scoped marker **Rarb** (retinoic acid receptor beta) plus MERFISH markers Bcl11b, Cd24a, and Fam163a distinguish it from 0514. Anatomy DGdo,me at HIP:1.0 (perfect hippocampal allocation).
- The same stage-5, Tbr1, and Tis21 literature [3][5][6] apply to the CL annotation.

**Marker evidence provenance**

- Marker provenance for DCX, NeuN, PSA-NCAM, Tis21, and Calbindin follows the same pattern as 0514. Dcx mRNA is high (mean = 8.78); Rbfox3 mRNA is low (mean = 0.30); Btg2 mRNA is essentially zero (mean = 0.0000); PSA-NCAM is untestable by RNA-seq.
- *(note: the Btg2 = 0.0000 reading in 0515 is more striking than the 0.0193 in 0514 — interpretation: this argues that 0515 is at a different point in the maturation trajectory than 0514, possibly later than the classical Tis21+ phase.)* Combined with the AT result (no Granule-immature mapping, but strong Neuroblast_2 mapping), 0515 is more consistent with a *late neuroblast* stage than with a true immature granule neuron stage.

**Concerns**

- **AT NO_EVIDENCE**: Hochgerner 2018 Granule-immature cells do not map to 0515 (F1=0.0). Instead, cluster 0515 is preferentially occupied by Hochgerner **Neuroblast_2** cells (F1=0.483, target_purity=1.0 — all 0515-mapped cells derive from Neuroblast_2). *(note: this is moderately strong counter-evidence that 0515 is not the immature granule neuron stage but a later neuroblast stage — interpretation beyond the facts.)*
- **NT prediction uncertain** [NT_PREDICTION_UNCERTAIN caveat]: glutamatergic identity inherited from parent class (cluster-level nt_type_combo_label is null).
- TYPE_A_SPLITS companion to 0514 [DISTRIBUTED_ACROSS_CLUSTERS caveat]; both share EXACT CL:9900002 but biological basis for the split is unresolved.
- Btg2 (Tis21) mRNA = 0.0 — even by the IHC vs scRNA-seq sensitivity argument that rescues 0514's near-zero reading, complete absence is harder to reconcile [MARKER_NOT_SPECIFIC caveat].
- A Gad1 nt_marker signal (score 3.67) at 0515 mirrors the same uninterpreted GABAergic signature as in 0514.

**What would upgrade confidence**

- Same RNA velocity / pseudotime analysis on the supertype (proposed for 0514) would resolve whether 0515 is upstream or downstream of 0514 along the neuroblast → immature GN axis. *(note: if upstream, this would justify reclassifying 0515 as a late neuroblast and removing it from this mapping.)*
- Targeted smFISH for Tbr1, Rarb, Bcl11b, and Dcx in adult DG to characterise whether Rarb+/Bcl11b+ cells form a distinct subpopulation within the inner GCL.
- A refined cite-traverse or AT using a dataset that distinguishes late neuroblast (Tbr1+/DCX+/Btg2−) from immature granule (Tbr1+/DCX+/Btg2+) cells would either upgrade 0515 to a separate `dg_late_neuroblast` mapping or downgrade this edge to UNCERTAIN.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** `dg_immature_granule_neuron` is annotated with `definition_basis: CLASSICAL_NEUROCHEMICAL`. The classical type is defined by protein-level markers DCX, NeuN, PSA-NCAM, and Tis21 [3][4][5], with Calbindin as a negative marker [3], soma located in the inner granule cell layer (UBERON:0005381), and glutamatergic neurotransmission [1][2]. Tbr1 onset marks the postmitotic transition from neuroblast to immature granule neuron [6], bridging atlas-side TF evidence to the classical IHC-defined stage.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the Allen Brain Cell Atlas CCN202307220 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (Hochgerner 2018 mouse DG scRNA-seq cell type labels: Granule-mature, Granule-immature, Mossy-Cyp26b1, Mossy-Adcyap1, Mossy-Klk8, Neuroblast 1, Neuroblast 2, Cajal-Retzius, GABA-Cnr1, GABA-Lhx6, Astrocytes) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations). 2 genes unmapped. Per-cell labels aggregated by source_cluster_label and target taxonomy level for F1 scoring. |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 2934 (filtered to 2934) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/f1_scores_best.csv) |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Results section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:12+00:00 from [kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml](kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | ATLAS_METADATA; LITERATURE×3; ANNOTATION_TRANSFER | SUPPORT×4; PARTIAL | atlas-internal, [3], [5], [6] |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | ATLAS_METADATA; LITERATURE×3; ANNOTATION_TRANSFER | SUPPORT×4; NO_EVIDENCE | atlas-internal, [3], [5], [6] |

</details>

---

## Discussion

**Primary mapping:** Dentate Gyrus Immature Granule Neuron → 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] at LOW confidence (with TYPE_A_SPLITS companion 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515]). Key support: EXACT CL:9900002 atlas annotation with coherent Tbr1+/Prox1+/Emx2+/Igfbpl1+ TF profile and stage-5 DCX+/NeuN+/Calbindin− literature [3][5][6]; weak PARTIAL annotation-transfer support for 0514. Key caveats: MARKER_NOT_SPECIFIC (classical IHC markers vs scRNA-seq marker selection) and DISTRIBUTED_ACROSS_CLUSTERS (TYPE_A_SPLITS across 0514/0515 with unresolved biological basis). This classical type maps directly to the Cell Ontology term immature dentate gyrus granule neuron [[CL:9900002](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:9900002)].

*(note: the AT data add an important qualification — the bulk of Hochgerner 2018 "Granule-immature" cells map to the DG Glut lineage (037 DG Glut subclass), not to the IMN_2 supertype. This is consistent with the IMN_2 supertype (and CL:9900002) corresponding to a narrower, earlier postmitotic window than the Hochgerner clustering captured — and with cluster 0515 representing a late neuroblast rather than a true immature granule neuron, since 0515 preferentially attracts Hochgerner Neuroblast_2.)*

### Proposed experiments and follow-ups

The Hochgerner 2018 AT (run `at_run_20260427_hochgerner2018_dg_mmc_wmbv1`) has already been completed and is the source of the PARTIAL / NO_EVIDENCE AT items above. A *refined* AT with a source dataset that explicitly separates Tbr1+ immature from earlier neuroblast and from DG Glut early-mature stages would still add value.

1. **Refined annotation transfer.**
   - *What*: MapMyCells transfer using a source dataset with explicit Tbr1+ / Btg2+ / Calbindin− gating (e.g. a marker-based subset of an existing adult DG scRNA-seq study).
   - *Target*: F1 ≥ 0.5 at CLUSTER level for the Tbr1+ subset to CS20230722_CLUS_0514.
   - *Expected output*: AnnotationTransferEvidence resolving whether IMN_2 is the correct atlas placement for the strict CL:9900002 definition.
   - *Resolves*: open questions 1, 4.

2. **Atlas feature-matrix query for sub-marker expression.**
   - *What*: Targeted query on the full Allen Brain Cell Atlas CCN202307220 feature matrix for Dcx, Rbfox3, Btg2 in clusters 0514/0515 below the marker-ranking threshold.
   - *Target*: confirm Dcx mRNA detection rate in 0514/0515 and quantify Btg2 expression heterogeneity within 0515.
   - *Expected output*: AtlasQueryEvidence resolving the marker-list discordance.
   - *Resolves*: open question 2.

3. **IHC co-stain to bridge atlas TF and classical IHC profiles.**
   - *What*: Anti-DCX and anti-Tbr1 (with anti-Calbindin counter) co-stain on adult mouse DG.
   - *Target*: ≥80% of Tbr1+ inner-GCL cells also DCX+ and Calbindin−.
   - *Expected output*: LiteratureEvidence (new publication) or direct experimental evidence.
   - *Resolves*: open question 3.

4. **Pseudotime / RNA velocity on the IMN_2 supertype.**
   - *What*: RNA velocity / pseudotime on clusters 0512–0515.
   - *Target*: ordered trajectory placing 0515 upstream or downstream of 0514.
   - *Expected output*: interpretive evidence (not a schema-defined EvidenceItem type).
   - *Resolves*: open questions 1, 5.

5. **smFISH validation of distinguishing markers.**
   - *What*: smFISH for Tbr1, Rarb, Bcl11b, Dcx in adult DG.
   - *Target*: spatial / cellular co-occurrence of Rarb+/Bcl11b+ cells within Tbr1+ inner-GCL cells.
   - *Expected output*: LiteratureEvidence on the biological basis of the 0514/0515 split.
   - *Resolves*: open question 5.

### Open questions

1. What is the biological basis for the two-cluster split (0514 vs 0515) at the immature GN stage? Possibilities: maturational sub-stage, sex composition, or circadian/activity-dependent transcriptional state. (Both edges.)
2. Does Dcx mRNA appear in clusters 0514/0515 below the atlas marker ranking threshold? A targeted query on the full atlas feature matrix would resolve the DCX alignment.
3. Are Tbr1+ inner-GCL cells in adult DG confirmed DCX+/NeuN+ at the protein level by IHC co-stain?
4. Is cluster 0515 better classified as a late neuroblast (per AT result showing Hochgerner Neuroblast_2 → 0515 at F1=0.483, target_purity=1.0) than as an immature granule neuron?
5. What distinguishes 0515 from 0514 biologically — does Rarb (retinoic acid receptor beta, scoped in 0515) plus Bcl11b/Cd24a/Fam163a MERFISH markers mark a later maturational sub-stage, a sex-biased transcriptional state, or a separate late-neuroblast identity? Why do both clusters show an unexplained Gad1 nt_marker signal (0514 score 5.56; 0515 score 3.67)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Stoll 2014 | [26056581](https://pubmed.ncbi.nlm.nih.gov/26056581/) | neurotransmitter type |
| [2] | Vangeneugden 2015 | [25954142](https://pubmed.ncbi.nlm.nih.gov/25954142/) | neurotransmitter type |
| [3] | Micheli 2025 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | DCX marker; stage-5 definition |
| [4] | Stepień 2021 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX, PSA-NCAM, NeuN markers |
| [5] | Attardo 2009 | [19482889](https://pubmed.ncbi.nlm.nih.gov/19482889/) | Tis21 marker; postmitotic re-expression |
| [6] | Hodge 2008 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Tbr1 postmitotic onset |
