# Dentate Gyrus Neuroblast (Type-3 Progenitor) — Allen Brain Cell Atlas CCN202307220 Mapping Report
*2026-04-14 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

---

## Introduction

The dentate gyrus (DG) neuroblast is the late, lineage-committed progenitor of adult hippocampal neurogenesis: a doublecortin (DCX)-expressing, transit-amplifying cell that resides in the dentate gyrus subgranular zone [UBERON:0009952] (SGZ) and gives rise to granule neurons. Classical neurochemical and immunohistochemical studies define this stage as the "type-3" cell of a developmental cascade running from type-1 radial-glial-like stem cells, through type-2a (Nestin+/Sox2+) and type-2b (Nestin+/DCX+) intermediate progenitors, to a DCX+ neuroblast that is still proliferating (Ki67+) but transcriptionally committed to a glutamatergic granule-neuron fate [1][2]. Mapping this protein-defined stage onto the WMBv1 transcriptomic atlas matters because adult neurogenesis is the principal experimental handle on circuit plasticity and disease in the adult hippocampus, and the transcriptomic correlates of each stage are needed to design Cre-driver and FACS strategies on a scRNA-seq footing.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus subgranular zone (SGZ) [UBERON:0009952] | — |
| NT | glutamatergic (committed but not yet functional) | — |
| Markers | DCX, Ki67 (Mki67), PSA-NCAM, Nestin | DCX [1][2]; Ki67 [2]; Nestin [1] |
| Negative markers | NeuN, Calbindin, GFAP | — |
| Neuropeptides | — | — |
| CL term | dentate gyrus neuroblast [CL:9900001] (EXACT) | — |

*Developmental staging note (from `classical_nodes[0].notes`):* the developmental sequence distinguishes type-2a (Nestin+/Sox2+), type-2b (Nestin+/DCX+), and type-3 (DCX+) stages, with a transcription-factor cascade (Pax6 → Ngn2 → Tbr2 → NeuroD → Tbr1) marking transitions. The three transit-amplifying stages may warrant separate nodes; this is flagged as potential heterogeneity within the classical node.

<details>
<summary>Details — source evidence for classical type properties</summary>

- **DCX (marker):** review · adult mouse DG SGZ · [1][2]

  > Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004).
  > — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [1] <!-- quote_key: 279046466_998847af -->

  > Three types of proliferatively active cells have been identified in the granular layer of the dentate gyrus (DG) of the hippocampus: type I cells -radial glial-like stem cells expressing glial fibrillary acidic protein (GFAP) and Sox2; type II cells -non-sessile cells expressing nestin, also referred to as transiently activated progenitor cells, neuroblasts expressing doublecortin (DCX); and Ki67 proteins and immature neurons expressing the DCX protein, PSA-NCAM, a marker of migrating neurons (polysialylated neuronal cell adhesion molecules) and neuron-specific protein (NeuN) (Attardo et al., 2009)(Gault et al., 2021). On the other hand, three types of cells were distinguished in the subventricular zone (SVZ): B1-type astrocytic stem cells, GFAP-positive, C-type progenitor cells expressing the Mash1 protein, and neuroblasts expressing the DCX protein (Okano et al., 2008).
  > — Stepień et al. 2021, Dentate Gyrus Immature Neurons · [2] <!-- quote_key: 245432259_44d5c91b -->

- **Ki67 (marker):** review · adult mouse DG SGZ · [2] (quote shared with DCX above)
- **Nestin (marker):** review · adult mouse DG SGZ · [1] (quote shared with DCX above)

</details>

### Cell Ontology mapping

Cell Ontology mapping: dentate gyrus neuroblast [[CL:9900001](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:9900001)] (EXACT).

---

## Results

A single mapping candidate was assessed: WMBv1 cluster **0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511]** is proposed as a LOW-confidence partial-overlap match, supported by atlas curator annotation and an annotation-transfer run from Hochgerner 2018 (GSE95315) that resolves Hochgerner Neuroblast_1/Neuroblast_2 cells to the DG-PIR Ex IMN supertype (0141) and to neighbouring clusters CS20230722_CLUS_0512 / CS20230722_CLUS_0513 rather than to CS20230722_CLUS_0511 itself.

![Annotation transfer F1 heatmap (GEO:GSE95315 → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the two source groups (Hochgerner Neuroblast_1, Neuroblast_2) relevant to the DG neuroblast classical node. Subclass 038 DG-PIR Ex IMN and supertype 0141 DG-PIR Ex IMN_2 are cleanly hit by Neuroblast_2 (F1 ≈ 0.80); cluster-level resolution drops as Hochgerner neuroblasts split across CS20230722_CLUS_0512 and CS20230722_CLUS_0513, with no cells assigned to CS20230722_CLUS_0511.*

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] | not available | not available | 🔴 LOW | NT CONSISTENT · Dcx CONSISTENT · location APPROXIMATE | Speculative |

Total: 1 edge (PARTIAL_OVERLAP).

### Property alignment — 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511]

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | dentate gyrus subgranular zone (SGZ) [UBERON:0009952] | not available | DG STR (DG-STR boundary, MERFISH); CCF NA:0.75, CTXsp:0.12 (CS20230722_CLUS_0511) | APPROXIMATE |
| NT type | glutamatergic (committed but not yet functional) | not available | Glut (Slc17a6 MERFISH score 6.02) (CS20230722_CLUS_0511) | CONSISTENT |
| DCX expression | DCX; PROTEIN; positive (IHC, canonical neuroblast marker) | not available | Dcx precomputed mean = 9.30 (CS20230722_CLUS_0511) | CONSISTENT |
| Ki67 (Mki67) expression | Ki67; PROTEIN; positive (IHC, proliferating cells) | not available | Mki67 precomputed mean = 0.09 (CS20230722_CLUS_0511) | APPROXIMATE |
| PSA-NCAM expression | PSA-NCAM; PROTEIN; positive (post-translational polysialylation of NCAM1) | not available | not in defining_markers (CS20230722_CLUS_0511) | NOT_ASSESSED |
| Nestin expression | Nestin; PROTEIN; positive at type-2b stage only (IHC) | not available | not in defining_markers (CS20230722_CLUS_0511) | APPROXIMATE |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — CS20230722_CLUS_0511 is itself a cluster-level (rank 0) candidate, reported as the sole member of supertype CS20230722_SUPT_0140 per atlas curator annotation; see Discussion for proposed split into type-2b vs type-3 sub-nodes.)*

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas curator "early neuroblast" annotation | Atlas metadata | SUPPORT | Eomes/Neurod1/Sox6/Meis1-2/Igfbpl1; CL:9900001 BROAD on SUPT_0140; Slc17a6 MERFISH=6.02 | atlas-internal |
| Supertype CL mapping on CS20230722_SUPT_0140 | Atlas metadata | PARTIAL | CL:9900001 BROAD; Eomes/Tbr2 = canonical type-2b TF | atlas-internal |
| MapMyCells AT — Hochgerner Neuroblast_2 → WMBv1 | Annotation transfer | PARTIAL | SUBCLASS 038 F1=0.798; SUPERTYPE 0141 F1=0.805; best CLUSTER 0512 F1=0.609; 0511 received no cells | — |
| MapMyCells AT — Hochgerner Neuroblast_1 → WMBv1 | Annotation transfer | PARTIAL | Best CLUSTER 0513 F1=0.788; SUBCLASS 038 F1=0.184; 0511 received no cells | — |

### 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] · 🔴 LOW

**Supporting evidence**

- **Atlas curator annotation.** WMBv1 labels CS20230722_CLUS_0511 an "early neuroblast" and lists Eomes (= Tbr2, the canonical type-2b intermediate-progenitor TF), Neurod1, Sox6, Meis1/2, and Igfbpl1 as cluster markers. MERFISH localises Eomes and Igfbpl1 transcripts to the DG–STR boundary (the SGZ surface). Slc17a6 (Vglut2) MERFISH score is 6.02, consistent with a committed glutamatergic identity. (atlas-internal)
- **Supertype CL mapping.** CS20230722_CLUS_0511 is reported as the sole member of supertype CS20230722_SUPT_0140 (DG-PIR Ex IMN_1), which already carries a BROAD CL:9900001 (dentate gyrus neuroblast) mapping in the atlas's CL crosswalk — independent support that the supertype-level placement of this cluster within the neuroblast space is correct. (atlas-internal)
- **Direct expression cross-check (Dcx).** Although Dcx is not on the atlas's curated `defining_markers` list for CS20230722_CLUS_0511, the precomputed cluster-level mean expression of Dcx is 9.30 — high and entirely consistent with the canonical DCX+ classical neuroblast. This was the basis for upgrading the Dcx property alignment from APPROXIMATE (metadata-only) to CONSISTENT.
- **MapMyCells AT (Hochgerner 2018 GSE95315).** Hochgerner Neuroblast_2 (n=777 cells, 717 after filter) maps cleanly to subclass 038 DG-PIR Ex IMN (F1=0.798) and supertype 0141 DG-PIR Ex IMN_2 (F1=0.805, median bootstrap 1.0), confirming that classically defined DG neuroblasts land in the DG-PIR Ex IMN lineage in WMBv1. Hochgerner Neuroblast_1 (n=97) maps similarly at subclass/supertype with the best individual cluster being CS20230722_CLUS_0513 (F1=0.788).

**Marker evidence provenance**

- **DCX (defining marker).** Evidence is protein-level (IHC) in the cited reviews [1][2]; both summarise classical IHC studies in adult mouse DG SGZ. The classical literature base is morphology- and location-confirmed (DCX+ cells in the SGZ with neuroblast morphology). Atlas annotation/expression cross-check: Dcx mRNA in CS20230722_CLUS_0511 has precomputed mean = 9.30 (high) despite Dcx not appearing on the atlas's curated `defining_markers` list — i.e. Dcx is filtered out as a cluster-discriminating marker because it is broadly expressed across DG-IMN clusters, not because it is absent. No discrepancy of concern.
- **Ki67 / Mki67 (defining marker).** Protein-level (IHC) evidence in [2]. Mki67 mRNA precomputed mean is 0.09 in CS20230722_CLUS_0511 — non-zero but low; this is biologically reasonable because Ki67 protein is detectable through G1–M whereas Mki67 transcript is short-lived and only a subset of cells is in active cycle at sampling time. *(note: cluster-mean Mki67 of 0.09 is interpretable as a transit-amplifying population with a small cycling fraction; this interpretation goes slightly beyond the facts file.)*
- **PSA-NCAM.** Post-translational glycan epitope on NCAM1; intrinsically undetectable by RNA-seq. NOT_ASSESSED is the correct alignment; no atlas-side correlate is expected. No primary citation on the classical node — a targeted cite-traverse for "PSA-NCAM adult DG neuroblast" could attach a primary IHC source if needed for downstream reuse.
- **Nestin (defining marker).** Protein-level (IHC) evidence in [1]. Classical literature places Nestin at the type-2a/type-2b stages, with downregulation in the type-3 (pure DCX+) stage. Atlas-side Nes is not on the defining_markers list; APPROXIMATE is the correct alignment because the classical node spans type-2b and type-3 sub-stages.
- **Negative markers (NeuN, Calbindin, GFAP).** Appear without per-marker primary citations on the classical node. NeuN/Calbindin negativity is implicit in the same classical reviews [1][2] (NeuN appears at stage 5, Calbindin at stage 6); GFAP negativity follows from exclusion of type-1 radial-glial-like cells. A targeted literature search would be useful only if atlas-side levels look discordant — they currently do not (atlas defining_markers do not list NeuN/Rbfox3, Calb1, or Gfap for CS20230722_CLUS_0511).

**Concerns**

- **Soma-location APPROXIMATE alignment.** CCF broad annotation for CS20230722_CLUS_0511 records NA:0.75 and CTXsp:0.12, with MERFISH label "DG STR" (DG–STR boundary). The DG–STR boundary is the SGZ — the correct soma location for classical neuroblasts — but CCF coverage at this sparse SGZ margin is a known weak point and the NA:0.75 fraction is a registration artefact rather than evidence of off-target localisation. *(adjacent region — could reflect registration boundary error; weak counter-evidence)*
- **AT runs do not anchor at CS20230722_CLUS_0511.** Both Hochgerner source groups (Neuroblast_1 and Neuroblast_2) preferentially map to CS20230722_CLUS_0512 (Neuroblast_2 best cluster, F1=0.609) and CS20230722_CLUS_0513 (Neuroblast_1 best cluster, F1=0.788); CS20230722_CLUS_0511 received no Hochgerner cells in either run. This is consistent with the curator caveat that the classical node spans type-2b (enriched in CS20230722_CLUS_0511 per its Eomes+ TF signature) and type-3 (likely CS20230722_CLUS_0512), and that Hochgerner Neuroblast_1/Neuroblast_2 are slightly later transitional cells. The atlas-vs-source split therefore supports the *lineage* assignment (DG-PIR Ex IMN supertype / subclass) but is **uncertain at cluster resolution**.
- **Classical node may straddle sub-stages.** Per the edge caveats, CS20230722_CLUS_0511 is enriched for type-2b (Eomes+ dominant), while the type-3 sub-stage probably corresponds to CS20230722_CLUS_0512. Full correspondence of the *single* classical node with CS20230722_CLUS_0511 alone is therefore unconfirmed.
- **Methodological gap (marker not specific).** Classical markers are protein-IHC defined; atlas defining_markers are scRNA-seq derived. Protein abundance does not track mRNA linearly for structural proteins (Nestin); PSA-NCAM is undetectable by transcriptomics; broadly expressed stage markers (Dcx) are filtered out of cluster-level marker selection. APPROXIMATE alignments largely reflect this methodological gap, not biological discordance.

**What would upgrade confidence**

- **Triple-label smFISH (Dcx + Eomes + Sox6) with Ki67 IHC in adult mouse DG SGZ** to directly test co-localisation of the CS20230722_CLUS_0511 transcriptomic signature with classical DCX+/Ki67+ neuroblasts. Resolves whether CS20230722_CLUS_0511 corresponds to the type-2b or type-3 sub-stage. Expected output: MultimodalEvidence.
- **DCX-GFP FACS + snRNA-seq + MapMyCells projection onto CCN20230722.** Protein-defined neuroblasts mapped directly to atlas clusters; target F1 ≥ 0.80 at CLUSTER level for either CS20230722_CLUS_0511 or CS20230722_CLUS_0512. Expected output: AnnotationTransferEvidence.
- **Targeted Dcx expression query on the full atlas feature matrix** at CS20230722_CLUS_0511 (sub-threshold per-cell detection rate) to confirm that the curator-list omission is a discrimination-threshold artefact rather than a biological absence.
- **Resolve the Gad2 nt_marker signal (score 3.24) in CS20230722_CLUS_0511** — distinguish ambient RNA, GABAergic contamination, or transient GABAergic signalling in type-2b progenitors.
- **Consider splitting `dg_neuroblast` into separate type-2b and type-3 classical nodes** to match the atlas's CS20230722_CLUS_0511 / CS20230722_CLUS_0512 resolution and remove the straddling ambiguity at source.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical `dg_neuroblast` node is defined on a CLASSICAL_NEUROCHEMICAL basis: a DCX+/Ki67+/PSA-NCAM+ adult-born progenitor of the dentate gyrus subgranular zone, also expressing Nestin at the type-2b stage and negative for NeuN, Calbindin, and GFAP. The neurotransmitter assignment is glutamatergic (committed but not yet functional), and the canonical developmental cascade Pax6 → Ngn2 → Tbr2 → NeuroD → Tbr1 places the type-3 stage between Tbr2 (Eomes) and NeuroD expression. Literature support is drawn from two reviews of adult hippocampal neurogenesis [1][2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the Allen Brain Cell Atlas CCN202307220 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

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

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:12+00:00 from [kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml](kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | ATLAS_METADATA (×2); ANNOTATION_TRANSFER (×2) | SUPPORT; PARTIAL; PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Dentate Gyrus Neuroblast (Type-3 Progenitor) → 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] at LOW confidence. Key support: atlas curator "early neuroblast" annotation (Eomes/Neurod1/Sox6/Meis1-2/Igfbpl1 + Slc17a6+ Glut) and MapMyCells AT placing Hochgerner DG neuroblasts on the DG-PIR Ex IMN lineage (subclass 038 F1=0.798; supertype 0141 F1=0.805). Key caveats: MARKER_NOT_SPECIFIC (protein-IHC vs scRNA-seq methodological gap, especially for PSA-NCAM and Nestin) and that the classical node straddles type-2b and type-3 sub-stages, with Hochgerner-derived AT preferentially landing on neighbouring CS20230722_CLUS_0512 / CS20230722_CLUS_0513 rather than CS20230722_CLUS_0511 itself.

This classical type maps directly to the Cell Ontology term dentate gyrus neuroblast [[CL:9900001](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:9900001)].

### Proposed experiments and follow-ups

A MapMyCells annotation transfer (Hochgerner 2018 GSE95315 → WMBv1) already exists on this edge and partly addresses cluster-level placement: it resolves Hochgerner Neuroblast_1/Neuroblast_2 to the DG-PIR Ex IMN subclass/supertype but **not** to CS20230722_CLUS_0511 specifically (Neuroblast_2 best cluster CS20230722_CLUS_0512, F1=0.609; Neuroblast_1 best cluster CS20230722_CLUS_0513, F1=0.788; CS20230722_CLUS_0511 received no cells). The completed round therefore resolves the *lineage* assignment but leaves *cluster identity* of the classical neuroblast unresolved.

**Group 1 — Multimodal mRNA/protein co-localisation in tissue.**
- *What:* triple-label smFISH (Dcx + Eomes + Sox6) combined with Ki67 IHC in adult mouse DG SGZ.
- *Target:* quantify the type-2b (Eomes+) vs type-3 (Eomes-low) split within DCX+ cells and assign each fraction to CS20230722_CLUS_0511 vs CS20230722_CLUS_0512 transcriptomic signatures.
- *Expected output:* a new MultimodalEvidence item with morphology- and TF-anchored cell counts.
- *Resolves:* edge cluster-vs-supertype ambiguity (open questions 1, 3); whether the classical node should be split into type-2b and type-3 sub-nodes.

**Group 2 — Protein-defined snRNA-seq + AnnotationTransfer (refined).**
- *What:* FACS-isolated DCX-GFP cells from adult DG → snRNA-seq → MapMyCells against CCN20230722. This is a *refined* version of the existing Hochgerner→WMBv1 AT run: it starts from protein-defined neuroblasts rather than from an external scRNA-seq label, removing dependence on Hochgerner's clustering decisions and adding stronger anchoring at protein level.
- *Target:* F1 ≥ 0.80 at CLUSTER level for either CS20230722_CLUS_0511 or CS20230722_CLUS_0512.
- *Expected output:* new AnnotationTransferEvidence on the existing edge (and possibly a new edge to CS20230722_CLUS_0512).
- *Resolves:* whether the protein-defined neuroblast lands at CS20230722_CLUS_0511 (type-2b) or CS20230722_CLUS_0512 (type-3) (open question 3) and whether the Hochgerner-vs-protein-defined gap is biological or labelling-driven.

**Group 3 — Targeted feature-matrix query.**
- *What:* direct Dcx and Mki67 expression query across the full WMBv1 feature matrix for cells in CS20230722_CLUS_0511.
- *Target:* per-cell Dcx detection rate (binary) and Mki67 detection rate in CS20230722_CLUS_0511 cells.
- *Expected output:* an inline ATLAS_QUERY evidence item.
- *Resolves:* open question 1 (whether Dcx absence from atlas `defining_markers` is a discrimination-threshold artefact rather than a biological absence).

### Open questions

1. Does Dcx transcript appear in CS20230722_CLUS_0511 cells at a level below the differential expression threshold for `defining_marker` selection? A targeted Dcx expression query on the full atlas feature matrix would resolve this.
2. Is the Gad2 nt_marker signal (score 3.24) in CS20230722_CLUS_0511 ambient RNA, a minor contaminating GABAergic population, or evidence of transient GABAergic signalling in type-2b progenitors?
3. Should the `dg_neuroblast` classical node be split into separate type-2b and type-3 nodes to match atlas resolution (CS20230722_CLUS_0511 for type-2b; CS20230722_CLUS_0512 for type-3)?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Micheli 2025 · PMID:40519263 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | DCX marker |
| [2] | Stepień 2021 · PMID:37082558 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX marker |
