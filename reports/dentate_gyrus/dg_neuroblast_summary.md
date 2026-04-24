# Dentate Gyrus Neuroblast (Type-3 Progenitor) — Allen Brain Cell Atlas CCN202307220 Mapping Report
*Draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus neuroblast (CL:9900001) | |
| Soma location | subgranular zone (SGZ) [UBERON:0009952] | [1] [2] |
| NT | glutamatergic (committed but not yet functional) |  |
| Markers | DCX+, Ki67+, PSA-NCAM+, Nestin+ | [3] [4] |
| Negative | NeuN−, Calbindin−, GFAP− | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0511 DG-PIR Ex IMN_1 [CS20230722_CLUS_0511] |  | — | 🔴 LOW | Speculative |

All edges: `PARTIAL_OVERLAP`

---

## 0511 DG-PIR Ex IMN_1 · 🔴 LOW

**Supporting evidence:**

- Atlas curator annotation: 'early neuroblast'. TF markers Eomes (=Tbr2, canonical type-2b progenitor TF; Hodge et al. 2008), Neurod1, Sox6, Meis1/2, Igfbpl1. CL:9900001 (BROAD) on parent supertype CS20230722_SUPT_0140. NT: Slc17a6 MERFISH score 6.02 (Glut). MERFISH validates Eomes and Igfbpl1 at DG-STR boundary (SGZ). [Atlas metadata]
- Cluster is the sole member of supertype CS20230722_SUPT_0140 (DG-PIR Ex IMN_1), which carries CL:9900001 (dentate gyrus neuroblast) BROAD mapping. The Eomes/Tbr2 TF signature is the canonical marker for the type-2b intermediate progenitor stage. [Atlas metadata]
- MapMyCells transfer of Hochgerner 2018 Neuroblast_2 cells (n=777; GSE95315) to WMBv1. Subclass 038 DG-PIR Ex IMN (F1=0.798) and supertype 0141 DG-PIR Ex IMN_2 (F1=0.805) are strongly supported, confirming the DG-PIR Ex IMN lineage. At cluster level the best match is 0512 DG-PIR Ex IMN_2 (F1=0.609); cluster 0511 received no cells. Neuroblast_2 may represent a slightly later transitional stage (0512/0515) rather than the 0511 sub-stage. PARTIAL support for the lineage; cluster assignment uncertain. [Annotation transfer]
- MapMyCells transfer of Hochgerner 2018 Neuroblast_1 cells (n=97; GSE95315) to WMBv1. Best cluster is 0513 DG-PIR Ex IMN_2 (F1=0.788, group_purity=0.75, target_purity=0.83). Cluster 0511 received no cells. Combined with Neuroblast_2 mapping to 0512, the transfer resolves Hochgerner neuroblasts primarily to clusters 0512 and 0513. PARTIAL support at the DG-PIR Ex IMN lineage level. [Annotation transfer]

**Concerns:**

- **location_soma** (APPROXIMATE): A=UBERON:0009952 dentate gyrus subgranular zone (SGZ) / B=DG STR (DG-STR boundary, MERFISH); CCF NA:0.75, CTXsp:0.12. MERFISH validates Eomes/Igfbpl1 at DG-STR (SGZ) boundary. CCF NA:0.75 is a known registration artefact at the sparse SGZ margin.
- **marker_Ki67** (APPROXIMATE): A=Ki67 (Mki67); PROTEIN; positive (IHC, proliferating cells) / B=not in atlas defining_markers; precomputed stats Mki67 mean = 0.09. Low but non-zero Mki67 mRNA; consistent with a small fraction of cycling progenitors in this cluster
- **marker_Nestin** (APPROXIMATE): A=Nestin; PROTEIN; positive at type-2b stage only (IHC) / B=not present in defining_markers. Nestin/Nes is downregulated at the type-3 stage; absence is partly consistent with type-2b enrichment in this cluster (Eomes/Tbr2+ TF present).
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- CCF broad annotation shows NA:0.75 and CTXsp:0.12. MERFISH label 'DG STR' places cells at the DG-STR boundary (SGZ), but CCF-level soma location cannot be fully verified. The high NA fraction is a known artefact of sparse CCF coverage at the SGZ margin.
- The classical dg_neuroblast node spans type-2b (Nestin+/DCX+/Eomes+) and type-3 (DCX+/Eomes-low) sub-stages. Cluster 0511 is enriched for type-2b (Eomes+ dominant). Full correspondence with the type-3 sub-stage is unconfirmed; cluster 0512 is a secondary candidate for the type-3 transition.

**What would upgrade confidence:**

- *Unresolved:* Does Dcx transcript appear in cluster 0511 cells at a level below the differential expression threshold for defining_marker selection? A targeted Dcx expression query on the full atlas feature matrix would resolve this.
- *Unresolved:* Is the Gad2 nt_marker signal (score 3.24) in cluster 0511 ambient RNA, a minor contaminating GABAergic population, or evidence of transient GABAergic signalling in type-2b progenitors?
- *Unresolved:* Should the dg_neuroblast classical node be split into separate type-2b and type-3 nodes to match atlas resolution (cluster 0511 for type-2b; cluster 0512 for type-3)?
- *Proposed:* Triple-label smFISH combining Dcx, Eomes, and Sox6 transcripts with Ki67 IHC in adult mouse DG to directly test co-localisation of atlas cluster 0511 signature with classical DCX+/Ki67+ neuroblasts in the SGZ.
- *Proposed:* DCX-GFP sorted cells from adult DG followed by snRNA-seq and MapMyCells projection onto CCN202307220 to assign protein-defined neuroblasts to specific atlas clusters.

---

## Proposed experiments

### 1 — Other

- Triple-label smFISH combining Dcx, Eomes, and Sox6 transcripts with Ki67 IHC in adult mouse DG to directly test co-localisation of atlas cluster 0511 signature with classical DCX+/Ki67+ neuroblasts in the SGZ.
*Resolves: edge_dg_neuroblast_to_CS20230722_CLUS_0511*

### 2 — MapMyCells / annotation transfer

- DCX-GFP sorted cells from adult DG followed by snRNA-seq and MapMyCells projection onto CCN202307220 to assign protein-defined neuroblasts to specific atlas clusters.
*Resolves: edge_dg_neuroblast_to_CS20230722_CLUS_0511*

---

## Open questions

1. Does Dcx transcript appear in cluster 0511 cells at a level below the differential expression threshold for defining_marker selection? A targeted Dcx expression query on the full atlas feature matrix would resolve this.
2. Is the Gad2 nt_marker signal (score 3.24) in cluster 0511 ambient RNA, a minor contaminating GABAergic population, or evidence of transient GABAergic signalling in type-2b progenitors?
3. Should the dg_neuroblast classical node be split into separate type-2b and type-3 nodes to match atlas resolution (cluster 0511 for type-2b; cluster 0512 for type-3)?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | Atlas metadata | SUPPORT |
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | Atlas metadata | PARTIAL |
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | Annotation transfer | PARTIAL |
| edge_dg_neuroblast_to_CS20230722_CLUS_0511 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:28168008 | [28168008](https://pubmed.ncbi.nlm.nih.gov/28168008/) | soma location |
| [2] | PMID:18385329 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | soma location |
| [3] | PMID:40519263 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | DCX marker |
| [4] | PMID:37082558 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX marker |
