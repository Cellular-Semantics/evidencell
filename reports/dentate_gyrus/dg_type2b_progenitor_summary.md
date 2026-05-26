# Dentate Gyrus Type-2b Neural Progenitor — Allen Brain Cell Atlas CCN202307220 Mapping Report
*2026-04-14 · Source: `/Users/do12/Documents/GitHub/evidencell/kb/graphs/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus type-2b neural progenitor (CL:9900004) | |
| Soma location | subgranular zone (SGZ) [UBERON:0009952] |  |
| NT | glutamatergic (lineage committed, not yet functional) |  |
| Markers | Nestin+, DCX+, Eomes+ | [1] [2] |
| Negative | NeuN−, Calbindin− | |

---

## Cell Ontology mapping

Dentate Gyrus Type-2b Neural Progenitor is mapped to **dentate gyrus type-2b neural progenitor (CL:9900004)** as an **exact match** in the Cell Ontology (skos:exactMatch); the existing CL term covers this type.

*Mapping notes:* CL:9900004 (dentate gyrus type-2b neural progenitor, child of CL:0011020 neural progenitor cell) is an exact match — defined as the Nestin+/DCX+/ Eomes(Tbr2)+ transiently amplifying progenitor in the SGZ. Atlas cluster 0511 (DG-PIR Ex IMN_1, Eomes+/Sox6+) is the primary transcriptomic correlate; cluster 0512 (Eomes+/Prox1+) represents the type-2b/type-3 transition.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Verdict |
|---|---|---|---|---|---|
| — | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] |  | — |  |  |

All edges: `skos:closeMatch`

---

## 0511 DG-PIR Ex IMN_1 · 

*`CS20230722_CLUS_0511`*

**Supporting evidence:**

- Atlas curator cl_mapping on CS20230722_CLUS_0511: BROAD CL:9900004 (dentate gyrus type-2b neural progenitor), annotated as "early neuroblast". Eomes (=Tbr2) is a defining_marker, directly matching the canonical type-2b molecular identity. Additional TF markers Sox6, Neurod1, Meis1/2, Igfbpl1 corroborate the early neurogenesis stage. MERFISH validates Eomes and Igfbpl1 at DG-STR (SGZ). NT: Slc17a6 (Glut). [Atlas metadata]
- Hodge et al. 2008 established Tbr2/Eomes as the canonical type-2b marker. The Eomes+ defining_marker in cluster 0511 is the direct transcriptomic correlate of the IHC-defined Tbr2+ type-2b population. [Literature] [2]
- Confirms the classical type-2b signature (Nestin+/DCX+/Eomes+) that cluster 0511 anchors transcriptomically via Eomes. [Literature] [1]
- MapMyCells transfer of Hochgerner 2018 nIPC cells (n=88; GSE95315) to WMBv1. Cluster 0511 receives no nIPC cells. Closest DG-PIR Ex IMN match: cluster 0513 (F1=0.225, 8 cells). Strongest supertype hit is 0166 OB-STR-CTX Inh IMN_1 (F1=0.508), reflecting heterogeneity in the Hochgerner nIPC label (likely mixed type-2a/2b progenitors). Transfer neither confirms nor strongly refutes the type2b → 0511 mapping. [Annotation transfer]

**Concerns:**

- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- Cluster 0511 spans the type-2b/type-3 boundary. The curator annotation "early neuroblast" and the presence of Neurod1 (expressed from the neuroblast stage onward) indicate that some cells in this cluster may have already progressed past the type-2b stage. PARTIAL_OVERLAP reflects that type-2b progenitors are the dominant population but the cluster is not exclusive to this stage.
- CCF broad annotation shows NA:0.75 and CTXsp:0.12. MERFISH label 'DG STR' places cells at the DG-STR boundary (SGZ), but CCF soma location cannot be fully verified. The high NA fraction is a known artefact of sparse CCF coverage at the SGZ margin.
- [AUTO_REPREDICATED_2026_05_26] Predicate auto-migrated from deprecated evidencell:PartialOverlapMatch to skos:closeMatch by `refresh_predicates.py`. Rule: rule-3b: F1=0.059 ≤ 0.75, existing caveats → closeMatch. Curator review recommended.

**What would upgrade confidence:**

- *Unresolved:* Do clusters 0512 and 0513 (in dg_pir_ex_imn.yaml) together with 0511 represent a progressive type-2b to type-3 transition series, and if so should the type-2b node have secondary PARTIAL_OVERLAP edges to 0512/0513?
- *Unresolved:* Is the Gad2 signal (score 3.24) in cluster 0511 ambient RNA, a minor GABAergic contaminant, or evidence of transient GABAergic signalling in type-2b progenitors?
- *Proposed:* Triple-label smFISH combining Eomes, Sox6, and Nes transcripts with Tbr2 IHC to confirm co-localisation of cluster 0511 signature with classical Tbr2+/Nestin+ type-2b cells in adult mouse SGZ.
- *Proposed:* Tbr2-CreERT2 fate-mapping with snRNA-seq from sorted Tbr2+ cells followed by MapMyCells projection onto CCN202307220 to assign IHC-defined type-2b cells to specific atlas clusters.

---

## Proposed experiments

### 1 — Other

- Triple-label smFISH combining Eomes, Sox6, and Nes transcripts with Tbr2 IHC to confirm co-localisation of cluster 0511 signature with classical Tbr2+/Nestin+ type-2b cells in adult mouse SGZ.
*Resolves: edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511*

### 2 — MapMyCells / annotation transfer

- Tbr2-CreERT2 fate-mapping with snRNA-seq from sorted Tbr2+ cells followed by MapMyCells projection onto CCN202307220 to assign IHC-defined type-2b cells to specific atlas clusters.
*Resolves: edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511*

---

## Open questions

1. Do clusters 0512 and 0513 (in dg_pir_ex_imn.yaml) together with 0511 represent a progressive type-2b to type-3 transition series, and if so should the type-2b node have secondary PARTIAL_OVERLAP edges to 0512/0513?
2. Is the Gad2 signal (score 3.24) in cluster 0511 ambient RNA, a minor GABAergic contaminant, or evidence of transient GABAergic signalling in type-2b progenitors?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511 | Atlas metadata | SUPPORT |
| edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511 | Literature [2] | SUPPORT |
| edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511 | Literature [1] | SUPPORT |
| edge_dg_type2b_progenitor_to_CS20230722_CLUS_0511 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Micheli 2025 · PMID:40519263 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | Nestin marker |
| [2] | Hodge 2008 · PMID:18385329 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Nestin marker |
