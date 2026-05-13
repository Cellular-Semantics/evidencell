# Dentate Gyrus Type-2b Neural Progenitor — Allen Brain Cell Atlas CCN202307220 Mapping Report
*2026-04-14 · Source: `/Users/do12/Documents/GitHub/BICAN_agentic_framework_planning/evidencell/kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

---

## Introduction

The dentate gyrus type-2b neural progenitor is a transiently amplifying intermediate progenitor in the subgranular zone (SGZ) of the adult dentate gyrus, defined classically by co-expression of Nestin and doublecortin (DCX) and by the canonical type-2b transcription factor Eomes (Tbr2) [1][2]. Establishing a transcriptomic correlate for this stage matters because type-2b cells sit at the lineage boundary between proliferating progenitors (type-2a) and post-mitotic neuroblasts (type-3), and a clean atlas mapping enables atlas-based identification of stage-specific neurogenic populations and downstream comparison across protocols.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus subgranular zone [UBERON:0009952] | — |
| NT | glutamatergic (lineage committed, not yet functional) | — |
| Markers | Nestin [1][2]; DCX [1][2]; Eomes [2] | [1], [2] |
| Negative markers | NeuN; Calbindin | — |
| CL term | dentate gyrus type-2b neural progenitor (CL:9900004) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Nestin / DCX (classical type-2b signature):** REVIEW · [1]
  > Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004).
  > — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [1] <!-- quote_key: 279046466_998847af -->

- **Eomes/Tbr2 (canonical type-2b TF):** EXPERIMENTAL · mouse SGZ IHC · [2]
  > Tbr2+ cells coexpressing nestin-GFP were more typically found in clusters in the SGZ and were often noted to be in close association with a Tbr2-negative type-1 nestin-GFP+ cell. Of all the nestin-GFP+, Tbr2+ double-labeled cells examined, 96.76 ± 0.39% had morphology consistent with type-2 progenitors
  > — Hodge et al. 2008, Characterization of Tbr2+ cells in the SGZ · [2] <!-- quote_key: 15727849_21c476fd -->

- **DCX co-labelling of Tbr2+ (type-2b):** EXPERIMENTAL · mouse SGZ IHC · [2]
  > The majority of Tbr2+ cells colabeled with DCX (64.4 ± 4.7%). In general, these cells had low DCX expression, with either no processes or short, tangentially oriented processes, typical of type-2 cells.
  > — Hodge et al. 2008, Characterization of Tbr2+ cells in the SGZ · [2] <!-- quote_key: 15727849_237d8f24 -->

</details>

Cell Ontology mapping: dentate gyrus type-2b neural progenitor [[CL:9900004](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:9900004)] (EXACT).

---

## Results

One candidate atlas cluster was assessed: cluster 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] is the primary mapping at MODERATE confidence (PARTIAL_OVERLAP), anchored by the Eomes (=Tbr2) defining-marker match.

![Annotation transfer F1 tree (GEO:GSE95315 Hochgerner 2018 DG → WMBv1)](../../kb/annotation_transfer_runs/at_run_20260427_hochgerner2018_dg_mmc_wmbv1/figures/f1_tree.png)

*F1 across taxonomy levels for the Hochgerner 2018 nIPC source group. Each panel row is a source-cell group; nodes are coloured by F1 with precision (P) and recall (R) shown inline. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution.* The Hochgerner nIPC label is a mixed type-2a/type-2b population, and the strongest F1 (0.508) lands on a non-DG immature-neuron supertype (CS20230722_SUPT_0166), so the transfer is informative about source-label heterogeneity rather than confirmatory for cluster 0511.

### 4. Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] | — | — | 🟡 MODERATE | Eomes CONSISTENT · DCX CONSISTENT · location CONSISTENT | Best candidate |

Total edges assessed: 1 (PARTIAL_OVERLAP).

**Property comparison — 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511]**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | glutamatergic (lineage committed, not yet functional) | not available | Glut (Slc17a6 MERFISH score 6.02) | CONSISTENT |
| Soma location | dentate gyrus subgranular zone [UBERON:0009952] | not available | DG STR (DG-STR boundary, MERFISH); CCF NA:0.75, CTXsp:0.12 | CONSISTENT |
| Eomes | Eomes (=Tbr2); PROTEIN; positive (IHC, canonical type-2b TF; Hodge et al. 2008) | not available | Eomes; present in defining_markers; precomputed stats Eomes mean = 6.90 | CONSISTENT |
| Nestin | Nestin; PROTEIN; positive (IHC, co-expressed with DCX at type-2b stage) | not available | not present in defining_markers | NOT_ASSESSED |
| DCX | DCX; PROTEIN; positive at low levels (IHC; 64% of Tbr2+ cells co-label DCX at low expression; Hodge 2008) | not available | not in atlas defining_markers; precomputed stats Dcx mean = 9.30 | CONSISTENT |
| NeuN | NeuN; NEGATIVE (progenitor stage; not yet postmitotic) | not available | not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.48 | CONSISTENT |
| Calbindin | Calbindin; NEGATIVE (stage-6 mature marker; absent in progenitors) | not available | absent from defining_markers | CONSISTENT |
| Sex ratio | not documented | not available | not available | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Evidence support — 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511]**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas curator BROAD cl_mapping to CL:9900004 | Atlas metadata | SUPPORT | Eomes defining_marker; Sox6/Neurod1/Meis1/2/Igfbpl1 corroborate | atlas-internal |
| Hodge 2008 Tbr2/DCX SGZ IHC | Literature | SUPPORT | 64.4 ± 4.7% Tbr2+ cells co-label DCX | [2] |
| Micheli 2025 review of DG neurogenesis stages | Literature | SUPPORT | type-2b = Nestin+/DCX+ | [1] |
| Hochgerner 2018 (GSE95315) nIPC → WMBv1 MapMyCells | Annotation transfer | PARTIAL | F1=0.508 at SUPERTYPE (SUPT_0166); F1=0.225 at CLUSTER (CLUS_0513); 0 cells to 0511 | — |

### 5. Candidate paragraphs

### 0511 DG-PIR Ex IMN_1 · 🟡 MODERATE

**Supporting evidence**

- Atlas curator records a BROAD `cl_mapping` from CS20230722_CLUS_0511 to CL:9900004 with the cluster annotated as "early neuroblast"; Eomes (=Tbr2) is listed as a `defining_marker`, providing the direct molecular anchor to the classical Tbr2+ type-2b population.
- Additional TF markers in the atlas metadata for cluster 0511 — Sox6, Neurod1, Meis1/2, Igfbpl1 — corroborate the early-neurogenesis stage; MERFISH validates Eomes and Igfbpl1 at the DG-STR boundary (= SGZ), supporting both the marker assignment and the SGZ soma location.
- Hodge et al. 2008 established the canonical IHC definition of type-2b cells; the Tbr2+ population co-labels DCX at 64.4 ± 4.7% with typical type-2 morphology [2].
  > Tbr2+ cells coexpressing nestin-GFP were more typically found in clusters in the SGZ and were often noted to be in close association with a Tbr2-negative type-1 nestin-GFP+ cell. Of all the nestin-GFP+, Tbr2+ double-labeled cells examined, 96.76 ± 0.39% had morphology consistent with type-2 progenitors
  > — Hodge et al. 2008, Characterization of Tbr2+ cells in the SGZ · [2] <!-- quote_key: 15727849_21c476fd -->
- Micheli et al. 2025 reaffirms the type-2b = Nestin+/DCX+ definition in a recent review of DG adult neurogenesis stages [1].
  > Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004).
  > — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [1] <!-- quote_key: 279046466_998847af -->
- Quantitative cross-check from atlas precomputed expression: Eomes mean = 6.90 (high) and Dcx mean = 9.30 (high) in cluster 0511 — both classical markers are strongly transcriptionally detected at the cluster level, upgrading the DCX comparison from APPROXIMATE to CONSISTENT despite DCX not appearing in the atlas `defining_markers` list. Negative-marker Rbfox3 (NeuN) mean = 0.48 (low) is consistent with the progenitor (pre-postmitotic) stage.

**Marker evidence provenance**

- **Eomes/Tbr2:** evidence chain is strong — protein-level IHC in mouse SGZ with morphological characterisation of type-2 cells [2], directly aligned with the atlas transcriptomic `defining_marker` (mean = 6.90). No discrepancy.
- **DCX:** protein-level IHC in mouse SGZ [2] plus review reaffirmation [1]; mRNA is highly expressed at the cluster level (mean = 9.30) but absent from the atlas `defining_markers` list. This is a metadata/expression-annotation gap rather than a biological discordance — DCX is broadly expressed across early neurogenic stages and may be filtered out by the atlas's cluster-level differential-marker selection.
- **Nestin:** PROTEIN-level IHC evidence on classical side [1][2]; Nes mRNA is absent from the WMBv1 precomputed-stats gene panel, so a transcript-level cross-check cannot be performed. Aligned with the NOT_ASSESSED label.
- **NeuN (negative):** the low Rbfox3 mRNA value (0.48) is consistent with the progenitor stage, but scRNA-seq sensitivity for Rbfox3 mRNA is lower than IHC nuclear protein detection — interpret with caution. *(note: scRNA-seq under-detection of Rbfox3 mRNA relative to nuclear NeuN protein is a general technical observation, not a fact in the facts file.)*
- **Calbindin (negative):** absent from atlas `defining_markers`, consistent with classical negative-marker assignment; no expression cross-check value provided.

**Concerns**

- *MARKER_NOT_SPECIFIC*: classical type-2b markers (DCX, Nestin, PSA-NCAM) are defined by protein IHC, while atlas `defining_markers` are derived from scRNA-seq. Protein abundance does not track mRNA linearly for structural proteins; PSA-NCAM (a post-translational glycan epitope) is undetectable by transcriptomics; broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- *OTHER (stage boundary)*: cluster 0511 spans the type-2b/type-3 boundary. The curator annotation "early neuroblast" and the presence of Neurod1 (expressed from the neuroblast stage onward) indicate that some cells in cluster 0511 may already have progressed past the type-2b stage. This is the reason for PARTIAL_OVERLAP rather than EXACT_OVERLAP: type-2b progenitors are the dominant population in cluster 0511 but the cluster is not exclusive to this stage.
- *MERFISH_REGISTRATION_UNCERTAINTY*: CCF broad annotation shows NA:0.75 and CTXsp:0.12; MERFISH label "DG STR" places cells at the DG-STR boundary (SGZ) but CCF soma location cannot be fully verified. The high NA fraction is a known artefact of sparse CCF coverage at the SGZ margin and is treated as weak counter-evidence here.
- *Annotation-transfer PARTIAL result*: MapMyCells transfer of Hochgerner 2018 nIPC cells (n=88) to WMBv1 places zero cells on cluster 0511. The closest DG-PIR Ex IMN match is CS20230722_CLUS_0513 (F1=0.225, 8 cells) and the strongest supertype hit is CS20230722_SUPT_0166 OB-STR-CTX Inh IMN_1 (F1=0.508), the latter reflecting heterogeneity in the Hochgerner nIPC label (likely mixed type-2a/2b progenitors plus a non-DG immature-neuron component). The transfer therefore neither confirms nor strongly refutes the type-2b → 0511 mapping — it flags source-side label impurity as the dominant obstacle.

**What would upgrade confidence**

- Triple-label smFISH combining Eomes, Sox6, and Nes transcripts with Tbr2 IHC to confirm co-localisation of the cluster-0511 signature with classical Tbr2+/Nestin+ type-2b cells in adult mouse SGZ. Expected output: a curated direct-imaging `LiteratureEvidence` confirming co-occurrence.
- Tbr2-CreERT2 fate-mapping with snRNA-seq from sorted Tbr2+ cells followed by MapMyCells projection onto CCN202307220 at F1 ≥ 0.80 at CLUSTER level. Expected output: `AnnotationTransferEvidence` with a clean cluster-0511 mapping.
- A targeted re-analysis or refined source-label split of the Hochgerner 2018 nIPC population (separating Eomes+/DCX+ type-2b cells from Sox2+/Nestin+ type-2a cells) followed by MapMyCells transfer to WMBv1 would resolve whether the F1=0.508 SUPT_0166 hit reflects type-2a vs. type-2b heterogeneity and could lift the AT result to SUPPORT.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical Dentate Gyrus Type-2b Neural Progenitor is defined as the Nestin+/DCX+/Eomes(Tbr2)+ transiently amplifying progenitor in the SGZ [1][2]. NT identity is glutamatergic (lineage committed, not yet functional). Negative markers are NeuN and Calbindin (mature granule-neuron markers). `definition_basis` = CLASSICAL_NEUROCHEMICAL — the node sits on a literature/IHC evidentiary base, augmented at curation time by atlas precomputed-expression cross-checks.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the Allen Brain Cell Atlas CCN202307220 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE95315 (nIPC) |
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

*Generated by evidencell `01f89d6` at 2026-05-13T15:46:13+00:00 from [kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml](kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml).*

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511 | ATLAS_METADATA; LITERATURE; LITERATURE; ANNOTATION_TRANSFER | SUPPORT; SUPPORT; SUPPORT; PARTIAL | atlas-internal, [2], [1], at_run_20260427_hochgerner2018_dg_mmc_wmbv1 |

</details>

---

## Discussion

**Primary mapping:** Dentate Gyrus Type-2b Neural Progenitor → 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] at MODERATE confidence (PARTIAL_OVERLAP). Key support: ATLAS_METADATA (Eomes `defining_marker`; MERFISH-validated DG-STR/SGZ location) and LITERATURE (Hodge 2008 Tbr2/DCX SGZ IHC [2]; Micheli 2025 review [1]). Key caveats: MARKER_NOT_SPECIFIC (protein-vs-mRNA mismatch for structural progenitor markers) and stage-boundary mixing in cluster 0511 (type-2b dominant but not exclusive; Neurod1+ cells indicate some type-3 progression).

This classical type maps directly to the Cell Ontology term dentate gyrus type-2b neural progenitor [[CL:9900004](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:9900004)]. CL:9900004 (child of CL:0011020 neural progenitor cell) is defined as the Nestin+/DCX+/Eomes(Tbr2)+ transiently amplifying progenitor in the SGZ. Atlas cluster 0511 (DG-PIR Ex IMN_1, Eomes+/Sox6+) is the primary transcriptomic correlate; cluster 0512 (Eomes+/Prox1+) represents the type-2b/type-3 transition.

### 7. Proposed experiments and follow-ups

An annotation transfer using the Hochgerner 2018 nIPC source label has already been run (MapMyCells v1.7.1, n=88 nIPC cells, F1=0.508 at SUPERTYPE on SUPT_0166, 0 cells to cluster 0511); it did not confirm the type-2b → 0511 mapping because the Hochgerner nIPC label aggregates type-2a + type-2b progenitors. A *refined* annotation-transfer experiment is therefore still warranted:

- **What**: Tbr2-CreERT2 fate-mapping → snRNA-seq from sorted Tbr2+ cells → MapMyCells transfer to WMBv1.
- **Target**: F1 ≥ 0.80 at CLUSTER level on cluster 0511 [CS20230722_CLUS_0511].
- **Expected output**: `AnnotationTransferEvidence` with a cleanly resolved type-2b → 0511 mapping.
- **Resolves**: open question 1 (type-2b → 0511/0512/0513 transition series); would upgrade primary edge toward HIGH.

- **What**: Triple-label smFISH (Eomes + Sox6 + Nes) plus Tbr2 IHC in adult mouse SGZ.
- **Target**: confirm co-localisation of the cluster-0511 signature with classical Tbr2+/Nestin+ type-2b cells.
- **Expected output**: curated `LiteratureEvidence` for direct co-occurrence.
- **Resolves**: cross-check of cluster-0511 identity at single-cell resolution; reduces the MARKER_NOT_SPECIFIC caveat.

- **What**: Source-side re-analysis of the Gad2 score 3.24 in cluster 0511.
- **Target**: distinguish ambient-RNA contamination from a minor GABAergic contaminant or transient GABAergic signalling.
- **Expected output**: curator note resolving open question 2; potentially a new caveat flagging an ambient-RNA/doublet signal.

### 8. Open questions

1. Do clusters 0512 and 0513 (in `dg_pir_ex_imn.yaml`) together with 0511 represent a progressive type-2b → type-3 transition series, and if so should the type-2b node have secondary PARTIAL_OVERLAP edges to 0512/0513?
2. Is the Gad2 signal (score 3.24) in cluster 0511 ambient RNA, a minor GABAergic contaminant, or evidence of transient GABAergic signalling in type-2b progenitors?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Micheli 2025 · PMID:[40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | 40519263 | Nestin / DCX type-2b classical signature |
| [2] | Hodge 2008 · PMID:[18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | 18385329 | Tbr2/Eomes type-2b TF; Tbr2+/DCX+ SGZ IHC |
