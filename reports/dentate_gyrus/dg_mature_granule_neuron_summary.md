# Dentate Gyrus Mature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*Draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

> ⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted.
> All edges require expert review before use.

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus granule cell (CL:2000089) | |
| Soma location | granule cell layer (GCL) [UBERON:0001885] | [1] |
| NT | glutamatergic | [2] [3] |
| Markers | Calbindin+, NeuN+, Tbr1+ | [4] [5] |
| Negative | DCX−, Nestin−, PSA-NCAM− | |

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Verdict |
|---|---|---|---|---|---|
| 1 | 0506 DG Glut_2 [CS20230722_CLUS_0506] |  | — | 🟡 MODERATE | Best candidate |
| 2 | 0503 DG Glut_1 [CS20230722_CLUS_0503] |  | — | 🔴 LOW | Speculative |
| 3 | 0507 DG Glut_2 [CS20230722_CLUS_0507] |  | — | 🔴 LOW | Speculative |
| 4 | 0502 DG Glut_1 [CS20230722_CLUS_0502] |  | — | 🔴 LOW | Speculative |
| 5 | 0505 DG Glut_2 [CS20230722_CLUS_0505] |  | — | 🔴 LOW | Speculative |
| 6 | 0508 DG Glut_3 [CS20230722_CLUS_0508] |  | — | 🔴 LOW | Speculative |
| 7 | 0504 DG Glut_1 [CS20230722_CLUS_0504] |  | — | 🔴 LOW | Speculative |
| 8 | 0510 DG Glut_4 [CS20230722_CLUS_0510] |  | — | 🔴 LOW | Speculative |
| 9 | 0509 DG Glut_3 [CS20230722_CLUS_0509] |  | — | 🔴 LOW | Speculative |

All edges: `TYPE_A_SPLITS`

---

## 0506 DG Glut_2 · 🟡 MODERATE

**Supporting evidence:**

- Cluster CS20230722_CLUS_0506 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.69. Core TF/MERFISH markers: Glis3, Neurod2, Prox1, St18. Neuropeptides: Cck. Soma: DG do (dorsal outer GCL) (HIP:0.99). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]
- MapMyCells transfer of Hochgerner 2018 Granule-mature cells (n=1712; GSE95315) to WMBv1. Cluster 0506 DG Glut_2 is the best cluster match (F1=0.665, group_purity=0.833, target_purity=0.553). Subclass 037 DG Glut achieves F1=0.711 (group_purity=0.980). High group purity (83% of confident cluster-level cells map to 0506) confirms this as the primary atlas correlate of mature granule neurons in Hochgerner 2018. [Annotation transfer]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.25. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0506 covers the DG do (dorsal outer GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0506, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Cck) in cluster CS20230722_CLUS_0506 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0506.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG do (dorsal outer GCL) region to confirm spatial overlap.

---

## 0503 DG Glut_1 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0503 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.68. Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Hey2. Neuropeptides: Cck, Grp. Soma: DG ve (ventral GCL) (HIP:0.93). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.84. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0503 covers the DG ve (ventral GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0503, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Cck, Grp) in cluster CS20230722_CLUS_0503 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0503.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG ve (ventral GCL) region to confirm spatial overlap.

---

## 0507 DG Glut_2 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0507 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.67. Core TF/MERFISH markers: Glis3, Neurod2, St18. Neuropeptides: Cck, Pdyn. Soma: DG do (dorsal outer GCL) (HIP:0.98). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]
- MapMyCells transfer of Hochgerner 2018 Granule-mature cells (n=1712; GSE95315) to WMBv1. Cluster 0507 DG Glut_2 receives 7 cells from Granule-mature (F1=0.068, group_purity=0.053). Very weak PARTIAL support; dominant mapping is to 0506 (F1=0.665). [Annotation transfer]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.17. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0507 covers the DG do (dorsal outer GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0507, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Cck, Pdyn) in cluster CS20230722_CLUS_0507 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0507.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG do (dorsal outer GCL) region to confirm spatial overlap.

---

## 0502 DG Glut_1 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0502 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.64. Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Rfx2, Lhx9. Neuropeptides: Grp, Cck. Soma: DG ve (ventral GCL) (HIP:0.74). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.91. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0502 covers the DG ve (ventral GCL) subpopulation. All nine clusters together constitute the full classical type.
- CCF broad includes MEA and sAMY; ventral hippocampal registration ambiguity; anatomical_location field authoritatively specifies DG ve. The authoritative anatomical_location field specifies the correct DG assignment; CCF broad annotation ambiguity does not alter the soma location claim.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0502, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Grp, Cck) in cluster CS20230722_CLUS_0502 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0502.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG ve (ventral GCL) region to confirm spatial overlap.

---

## 0505 DG Glut_2 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0505 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.63. Core TF/MERFISH markers: Glis3, Neurod2, St18. Neuropeptides: none. Soma: DG do (dorsal outer GCL) (HIP:0.99). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.16. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0505 covers the DG do (dorsal outer GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0505, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (none) in cluster CS20230722_CLUS_0505 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0505.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG do (dorsal outer GCL) region to confirm spatial overlap.

---

## 0508 DG Glut_3 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0508 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.63. Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Egr2, Egr4. Neuropeptides: Cck, Pdyn. Soma: DG do (dorsal outer GCL) (HIP:0.96). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.76. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0508 covers the DG do (dorsal outer GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0508, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Cck, Pdyn) in cluster CS20230722_CLUS_0508 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0508.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG do (dorsal outer GCL) region to confirm spatial overlap.

---

## 0504 DG Glut_1 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0504 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.62. Core TF/MERFISH markers: Glis3, Prox1, Nr4a3, Egr3, Rorb. Neuropeptides: Grp, Penk, Cck, Cartpt. Soma: DG ve (ventral GCL) (HIP:0.69). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.39. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0504 covers the DG ve (ventral GCL) subpopulation. All nine clusters together constitute the full classical type.
- CCF broad includes sAMY:0.2; ventral hippocampal registration ambiguity. The authoritative anatomical_location field specifies the correct DG assignment; CCF broad annotation ambiguity does not alter the soma location claim.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0504, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Grp, Penk, Cck, Cartpt) in cluster CS20230722_CLUS_0504 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0504.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG ve (ventral GCL) region to confirm spatial overlap.

---

## 0510 DG Glut_4 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0510 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.62. Core TF/MERFISH markers: Glis3, St18, Lhx9, Nr2f2. Neuropeptides: Cck, Grp, Pdyn. Soma: DG po (posterior GCL) (HIP:0.99). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.32. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0510 covers the DG po (posterior GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0510, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Cck, Grp, Pdyn) in cluster CS20230722_CLUS_0510 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0510.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG po (posterior GCL) region to confirm spatial overlap.

---

## 0509 DG Glut_3 · 🔴 LOW

**Supporting evidence:**

- Cluster CS20230722_CLUS_0509 is within the DG Glut subclass (CL:2000089 EXACT mapping). Discovery composite score 0.59. Core TF/MERFISH markers: Glis3, Neurod2, Atf3, Bhlhe41, Cebpb. Neuropeptides: Cck, Pdyn, Npy. Soma: DG do (dorsal outer GCL) (HIP:0.96). All DG Glut clusters share Glis3/Neurod2/Slc17a7 mature granule core; classical protein markers Calbindin/NeuN/Tbr1 absent from atlas — protein-transcriptome gap. [Atlas metadata]
- Establishes stage-6 mature identity as DCX−/NeuN+/Calbindin+. DG Glut clusters collectively represent this terminal state; absence of DCX/Eomes and presence of mature TF core (Glis3, Neurod2) distinguishes them from upstream neuroblast and immature GN clusters. [Literature] [4]
- Confirms Tbr1 marks terminally differentiated postmitotic granule cells. DG Glut clusters represent the Tbr1+ mature stage even though Tbr1 does not appear as a cluster-distinguishing marker. [Literature] [5]
- MapMyCells transfer of Hochgerner 2018 Granule-mature cells (n=1712; GSE95315) to WMBv1. Cluster 0509 DG Glut_3 receives 12 cells from Granule-mature (F1=0.167, group_purity=0.091, target_purity=1.0). Low group purity; 0509 is not a dominant target. Weak PARTIAL support. [Annotation transfer]

**Concerns:**

- **marker_NeuN** (APPROXIMATE): A=NeuN (Rbfox3); PROTEIN; positive (postmitotic marker) / B=not in atlas defining_markers; precomputed stats Rbfox3 mean = 0.30. Rbfox3 mRNA present but low (scRNAseq sensitivity < IHC nuclear protein); APPROXIMATE retained
- Classical markers are defined by protein IHC (DCX, Ki67, PSA-NCAM, Nestin for neuroblast; DCX, NeuN, PSA-NCAM, Tis21 for immature GN; Calbindin, NeuN, Tbr1 for mature GN). Atlas defining_markers are derived from scRNA-seq: (1) protein abundance does not track mRNA linearly for structural proteins; (2) PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics; (3) broadly expressed stage markers are filtered out in cluster-level marker selection. APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- TYPE_A_SPLITS: CL:2000089 (mature granule neuron) is split across nine DG Glut clusters (0502-0510) representing topographic variants (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. Cluster CS20230722_CLUS_0509 covers the DG do (dorsal outer GCL) subpopulation. All nine clusters together constitute the full classical type.

**What would upgrade confidence:**

- *Unresolved:* Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0509, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
- *Unresolved:* Do the distinct neuropeptide profiles (Cck, Pdyn, Npy) in cluster CS20230722_CLUS_0509 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
- *Proposed:* MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0509.
- *Proposed:* IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG do (dorsal outer GCL) region to confirm spatial overlap.

---

## Proposed experiments

### 1 — MERFISH / spatial transcriptomics

- MERFISH or smFISH co-labelling for Calb1, Glis3, and Glis3 in adult mouse DG to confirm Calb1 expression within cells mapping to CS20230722_CLUS_0506.
- IHC co-labelling of Calbindin protein with MERFISH-validated markers for the DG do (dorsal outer GCL) region to confirm spatial overlap.
*Resolves: edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510, edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509*

---

## Open questions

1. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0506, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
2. Do the distinct neuropeptide profiles (Cck) in cluster CS20230722_CLUS_0506 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
3. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0503, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
4. Do the distinct neuropeptide profiles (Cck, Grp) in cluster CS20230722_CLUS_0503 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
5. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0507, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
6. Do the distinct neuropeptide profiles (Cck, Pdyn) in cluster CS20230722_CLUS_0507 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
7. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0502, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
8. Do the distinct neuropeptide profiles (Grp, Cck) in cluster CS20230722_CLUS_0502 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
9. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0505, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
10. Do the distinct neuropeptide profiles (none) in cluster CS20230722_CLUS_0505 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
11. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0508, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
12. Do the distinct neuropeptide profiles (Cck, Pdyn) in cluster CS20230722_CLUS_0508 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
13. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0504, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
14. Do the distinct neuropeptide profiles (Grp, Penk, Cck, Cartpt) in cluster CS20230722_CLUS_0504 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
15. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0510, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
16. Do the distinct neuropeptide profiles (Cck, Grp, Pdyn) in cluster CS20230722_CLUS_0510 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?
17. Is Calb1 mRNA expressed but below atlas detection threshold in CS20230722_CLUS_0509, or does calbindin protein arise via post-transcriptional regulation? MERFISH or smFISH with Calb1 probe would resolve this.
18. Do the distinct neuropeptide profiles (Cck, Pdyn, Npy) in cluster CS20230722_CLUS_0509 reflect stable functional subtypes of mature granule neurons or transient activity-dependent states?

---

## Evidence base

| Edge | Evidence types | Supports |
|---|---|---|
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | Annotation transfer | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | Annotation transfer | NO_EVIDENCE |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | Annotation transfer | PARTIAL |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | Annotation transfer | NO_EVIDENCE |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | Annotation transfer | NO_EVIDENCE |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | Annotation transfer | NO_EVIDENCE |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | Annotation transfer | NO_EVIDENCE |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | Annotation transfer | NO_EVIDENCE |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | Atlas metadata | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | Literature [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | Literature [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | Annotation transfer | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | PMID:31068541 | [31068541](https://pubmed.ncbi.nlm.nih.gov/31068541/) | soma location |
| [2] | PMID:26056581 | [26056581](https://pubmed.ncbi.nlm.nih.gov/26056581/) | neurotransmitter type |
| [3] | PMID:25954142 | [25954142](https://pubmed.ncbi.nlm.nih.gov/25954142/) | neurotransmitter type |
| [4] | PMID:40519263 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | Calbindin marker |
| [5] | PMID:18385329 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Tbr1 marker |
