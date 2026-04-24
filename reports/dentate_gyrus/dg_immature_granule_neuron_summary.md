# Dentate Gyrus Immature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*Draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | immature dentate gyrus granule neuron (CL:9900002) | |
| Soma location | inner granule cell layer (GCL) [UBERON:0005381] | [1] [2] |
| NT | glutamatergic | [3] [4] |
| Markers | DCX+, NeuN+, PSA-NCAM+, Tis21+ | [5] [6] [7] |
| Negative | Calbindin− | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] |  | — | 🔴 LOW | Speculative |
| 2 | 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515] |  | — | 🔴 LOW | Speculative |

All edges: `TYPE_A_SPLITS`

---

## 0514 DG-PIR Ex IMN_2 · 🔴 LOW

**Supporting evidence:**

- EXACT CL:9900002 (immature dentate gyrus granule neuron) in atlas; curator annotation 'late neuroblast/immature granule cell'. TF markers: Tbr1 (canonical postmitotic TF; Hodge et al. 2008), Prox1, Emx2 (MERFISH), Igfbpl1 (MERFISH), Ccbe1 (scoped). Anatomy: DGdo,me HIP:0.98. NT: Glut. No Calbindin (Calb1) — consistent with immature (not mature) stage. Discovery composite score 0.82. [Atlas metadata]
- Establishes stage-5 definition (DCX+/NeuN+/Calbindin−). Absence of Calbindin from cluster defining_markers is consistent with pre-terminal immature identity. [Literature] [5]
- Tbr1 onset marks postmitotic transition from neuroblast to immature granule neuron. Tbr1 present as TF marker; bridges atlas TF evidence to classical postmitotic immature granule neuron stage. [Literature] [8]
- Confirms Tis21 re-expression in postmitotic adult DG neurons. Consistent with postmitotic Tbr1+ identity of this cluster. [Literature] [7]
- MapMyCells transfer of Hochgerner 2018 Granule-immature cells (n=1333; GSE95315) to WMBv1. The majority map to 037 DG Glut (F1=0.566 subclass) and best cluster 0507 DG Glut_2 (F1=0.510), consistent with an immature granule neuron identity. A minority (27 cells, 2%) map to cluster 0514 DG-PIR Ex IMN_2 (F1=0.211), suggesting overlap with a transitional neuroblast-like population. Weak PARTIAL support for 0514; the dominant atlas representation is the DG Glut lineage (0506/0507). [Annotation transfer]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (RBFOX3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.35. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- **marker_Tis21** (APPROXIMATE): A=Tis21 (Btg2); PROTEIN; positive (postmitotic re-expression in adult DG) / B=not in atlas defining_markers; precomputed stats Btg2 mean = 0.0193 (near-zero). Btg2 (Tis21) mRNA near-zero in precomputed stats; IHC may detect transiently accumulated protein not captured by scRNAseq; APPROXIMATE retained pending further resolution
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: dg_immature_granule_neuron maps across two clusters: CS20230722_CLUS_0514 (this edge) and CS20230722_CLUS_0515. Both carry EXACT CL:9900002 and share the Tbr1+/Prox1+/Emx2+/Igfbpl1+ core TF profile. Neither cluster alone fully represents the classical type.
- 12 proposed literature evidence items (proposed_evidence_dg_immature_granule_neuron.yaml) are pending review and attachment to this edge and its companion to CS20230722_CLUS_0515. Items above are the most load-bearing.

**What would upgrade confidence:**

- *Unresolved:* What is the biological basis for the two-cluster split (0514 vs 0515) at the immature GN stage? Possibilities: maturational sub-stage, sex composition, or circadian/activity-dependent transcriptional state.
- *Unresolved:* Does Dcx mRNA appear in clusters 0514/0515 below the atlas marker ranking threshold? A targeted query on the full atlas feature matrix would resolve the DCX alignment.
- *Unresolved:* Why does cluster 0514 show a Gad1 nt_marker signal (score 5.56)? Transient GABAergic signalling in immature granule neurons, doublet artefact, or contamination?
- *Proposed:* Anti-DCX and anti-Tbr1 co-stain on adult mouse DG to confirm Tbr1+ inner-GCL cells are also DCX+/NeuN+ at protein level, bridging atlas TF and classical profiles.
- *Proposed:* Query full Allen Brain Cell Atlas CCN202307220 feature matrix for Dcx, Rbfox3, Btg2 in clusters 0514/0515 to check expression below the marker ranking threshold.

---

## 0515 DG-PIR Ex IMN_2 · 🔴 LOW

**Supporting evidence:**

- EXACT CL:9900002 in atlas; curator annotation 'late neuroblast'. Core TF profile identical to cluster 0514 (Tbr1+/Prox1+/Emx2+/Igfbpl1+). Scoped marker Rarb (distinctive within subclass). Additional MERFISH markers: Bcl11b, Cd24a, Fam163a. Anatomy: DGdo,me HIP:1.0 (perfect hippocampal allocation). NT: NA at cluster level, Glut by parent-class inheritance. Discovery composite score 0.82. [Atlas metadata]
- Establishes stage-5 definition (DCX+/NeuN+/Calbindin−). Absence of Calbindin from cluster defining_markers is consistent with pre-terminal immature identity. [Literature] [5]
- Tbr1 onset marks postmitotic transition from neuroblast to immature granule neuron. Tbr1 present as TF marker; bridges atlas TF evidence to classical postmitotic immature granule neuron stage. [Literature] [8]
- Confirms Tis21 re-expression in postmitotic adult DG neurons. Consistent with postmitotic Tbr1+ identity of this cluster. [Literature] [7]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (RBFOX3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.30. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- **marker_Tis21** (APPROXIMATE): A=Tis21 (Btg2); PROTEIN; positive (postmitotic re-expression in adult DG) / B=not in atlas defining_markers; precomputed stats Btg2 mean = 0.0000 (near-zero). Btg2 (Tis21) mRNA near-zero in precomputed stats; IHC may detect transiently accumulated protein not captured by scRNAseq; APPROXIMATE retained pending further resolution
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS companion to edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514. Both clusters carry EXACT CL:9900002 and share the same core TF profile. The biological basis for the intra-stage split is unresolved; Rarb and Bcl11b/Cd24a distinguish 0515 from 0514.
- NT type not directly assigned at cluster level (nt_type_combo_label: null); glutamatergic by parent class inheritance. Direct cluster-level assignment would strengthen the NT evidence.

**What would upgrade confidence:**

- *Unresolved:* What distinguishes cluster 0515 from 0514 biologically? Rarb (retinoic acid receptor beta, scoped in 0515) and Bcl11b/Cd24a/Fam163a MERFISH markers may mark a later maturational sub-stage or sex-biased transcriptional state.
- *Unresolved:* Is the Gad1 nt_marker signal (score 3.67) the same transient GABAergic signal as in 0514 (score 5.56), potentially indicating 0515 is at an earlier maturational state?
- *Proposed:* RNA velocity or pseudotime analysis on the DG-PIR Ex IMN_2 supertype (clusters 0512–0515) to determine cluster ordering along the neuroblast-to-immature-GN axis.
- *Proposed:* Targeted smFISH for Tbr1, Rarb, Bcl11b, and Dcx in adult DG to characterise whether Rarb+/Bcl11b+ cells form a distinct subpopulation within the inner GCL.

---

## Proposed experiments

### 1 — Other

- Anti-DCX and anti-Tbr1 co-stain on adult mouse DG to confirm Tbr1+ inner-GCL cells are also DCX+/NeuN+ at protein level, bridging atlas TF and classical profiles.
- Query full Allen Brain Cell Atlas CCN202307220 feature matrix for Dcx, Rbfox3, Btg2 in clusters 0514/0515 to check expression below the marker ranking threshold.
- RNA velocity or pseudotime analysis on the DG-PIR Ex IMN_2 supertype (clusters 0512–0515) to determine cluster ordering along the neuroblast-to-immature-GN axis.
- Targeted smFISH for Tbr1, Rarb, Bcl11b, and Dcx in adult DG to characterise whether Rarb+/Bcl11b+ cells form a distinct subpopulation within the inner GCL.
*Resolves: edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514, edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515*

---

## Open questions

1. What is the biological basis for the two-cluster split (0514 vs 0515) at the immature GN stage? Possibilities: maturational sub-stage, sex composition, or circadian/activity-dependent transcriptional state.
2. Does Dcx mRNA appear in clusters 0514/0515 below the atlas marker ranking threshold? A targeted query on the full atlas feature matrix would resolve the DCX alignment.
3. Why does cluster 0514 show a Gad1 nt_marker signal (score 5.56)? Transient GABAergic signalling in immature granule neurons, doublet artefact, or contamination?
4. What distinguishes cluster 0515 from 0514 biologically? Rarb (retinoic acid receptor beta, scoped in 0515) and Bcl11b/Cd24a/Fam163a MERFISH markers may mark a later maturational sub-stage or sex-biased transcriptional state.
5. Is the Gad1 nt_marker signal (score 3.67) the same transient GABAergic signal as in 0514 (score 5.56), potentially indicating 0515 is at an earlier maturational state?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | Atlas metadata | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | Literature [5] | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | Literature [8] | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | Literature [7] | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0514 | Annotation transfer | PARTIAL |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | Atlas metadata | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | Literature [5] | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | Literature [8] | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | Literature [7] | SUPPORT |
| edge_dg_immature_granule_neuron_to_CS20230722_CLUS_0515 | Annotation transfer | NO_EVIDENCE |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:28168008 | [28168008](https://pubmed.ncbi.nlm.nih.gov/28168008/) | soma location |
| [2] | PMID:26880934 | [26880934](https://pubmed.ncbi.nlm.nih.gov/26880934/) | soma location |
| [3] | PMID:26056581 | [26056581](https://pubmed.ncbi.nlm.nih.gov/26056581/) | neurotransmitter type |
| [4] | PMID:25954142 | [25954142](https://pubmed.ncbi.nlm.nih.gov/25954142/) | neurotransmitter type |
| [5] | PMID:40519263 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | DCX marker |
| [6] | PMID:37082558 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX marker |
| [7] | PMID:19482889 | [19482889](https://pubmed.ncbi.nlm.nih.gov/19482889/) | Tis21 marker |
| [8] | PMID:18385329 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Tbr1 onset marks postmitotic transition from neuroblast to immature granule neur |
