# Dentate Gyrus Mature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**WARNING: Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | Granule cell layer (GCL) of dentate gyrus of hippocampal formation [UBERON:0001885] | [1] |
| Neurotransmitter | Glutamatergic | [2][3] |
| Markers | Calbindin (Calb1); NeuN (Rbfox3) | [4] |
| Markers (cont.) | Tbr1 | [5] |
| Negative markers | DCX; Nestin; PSA-NCAM | — |
| CL term | dentate gyrus granule cell (CL:2000089); EXACT | — |
| Electrophysiology class | Repetitive action potential firing; plateau ~140 Hz; Vth ~−39.6 to −45.8 mV; Cm 99.2 pF; tau_m 33.7 ms; Vrest −74.8 mV (adult mouse C57BL/6). Larger Cm and longer tau_m than immature adult-born granule cells. Fully synaptically integrated by 4 weeks post-birth. | — |

**Morphology note.** Terminally differentiated granule neurons (stage 6) populating the granule cell layer. Fully elaborated dendritic arbor and complete axonal projections to CA3. Receive primary glutamatergic afferents from entorhinal cortex and project mossy fiber axons to inhibitory interneurons and pyramidal cells of area CA3.

---

## Mapping candidates

All nine edges share the same relationship type: **TYPE_A_SPLITS** — the classical type CL:2000089 (dentate gyrus granule cell) is distributed across nine atlas clusters representing topographic (dorsal/ventral/posterior GCL) and neuropeptide/functional variants. No single atlas cluster captures the full classical type; all nine clusters together constitute it.

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0506 DG Glut_2 [CS20230722_CLUS_0506] | DG Glut | — | 🔴 LOW | NT consistent; soma DG do (dorsal outer GCL) consistent; Calbindin/NeuN/Tbr1 APPROXIMATE (protein-transcriptome gap) | Speculative |
| 2 | 0503 DG Glut_1 [CS20230722_CLUS_0503] | DG Glut | — | 🔴 LOW | NT consistent; soma DG ve (ventral GCL) consistent; Calbindin/NeuN/Tbr1 APPROXIMATE | Speculative |
| 3 | 0507 DG Glut_2 [CS20230722_CLUS_0507] | DG Glut | — | 🔴 LOW | NT consistent; soma DG do (dorsal outer GCL) consistent; Calbindin/NeuN/Tbr1 APPROXIMATE | Speculative |
| 4 | 0502 DG Glut_1 [CS20230722_CLUS_0502] | DG Glut | — | 🔴 LOW | NT consistent; soma DG ve (ventral GCL) consistent; registration uncertainty noted | Speculative |
| 5 | 0505 DG Glut_2 [CS20230722_CLUS_0505] | DG Glut | — | 🔴 LOW | NT consistent; soma DG do (dorsal outer GCL) consistent; no neuropeptides | Speculative |
| 6 | 0508 DG Glut_3 [CS20230722_CLUS_0508] | DG Glut | — | 🔴 LOW | NT consistent; soma DG do (dorsal outer GCL) consistent; Egr2/Egr4 TF markers | Speculative |
| 7 | 0504 DG Glut_1 [CS20230722_CLUS_0504] | DG Glut | — | 🔴 LOW | NT consistent; soma DG ve (ventral GCL) consistent; registration uncertainty noted | Speculative |
| 8 | 0510 DG Glut_4 [CS20230722_CLUS_0510] | DG Glut | — | 🔴 LOW | NT consistent; soma DG po (posterior GCL) consistent | Speculative |
| 9 | 0509 DG Glut_3 [CS20230722_CLUS_0509] | DG Glut | — | 🔴 LOW | NT consistent; soma DG do (dorsal outer GCL) consistent; stress-response TF markers (Atf3, Cebpb) | Speculative |

**Total: 9 edges; all TYPE_A_SPLITS (one classical type maps to multiple atlas clusters).** No UNCERTAIN edges were generated for this classical type.

---

## Candidate paragraphs

All nine candidate clusters share the same structural logic: they belong to the DG Glut subclass, carry an EXACT CL:2000089 mapping at the subclass level, and their separation into nine clusters reflects topographic position and neuropeptide co-expression rather than distinct cell type identity. Because all edges are LOW confidence with no MODERATE or UNCERTAIN edges, each is addressed below. The core evidence and concerns are largely shared; per-cluster distinctions are noted where they differ.

---

## 0506 DG Glut_2 [CS20230722_CLUS_0506] — dorsal outer GCL, Cck+

**Supporting evidence**

- Atlas metadata places this cluster within the DG Glut subclass, which carries a CL:2000089 EXACT mapping. Discovery composite score: 0.69 (highest of the nine clusters). [ATLAS_METADATA]
- Core transcription factors Glis3, Neurod2, Prox1, and St18 define the mature granule identity in the atlas; Glis3 and Neurod2 in particular are shared across all DG Glut clusters as the transcriptomic surrogate of the mature granule state.
- Literature establishes that stage-6 terminally differentiated neurons express calbindin and NeuN and are DCX-negative [4]; absence of DCX/Eomes and presence of Glis3/Neurod2 in this cluster is consistent with that terminal state.
- Tbr1 marks postmitotic granule cells exclusively, not progenitors [5]; DG Glut clusters represent the Tbr1+ postmitotic stage even though Tbr1 is not a cluster-level discriminating marker in the atlas.
- Glutamatergic neurotransmitter type is consistent: classical type is glutamatergic [2][3]; atlas cluster is in the Glut subclass (Slc17a7/vGLUT1 marker).
- Soma location is consistent: classical GCL [UBERON:0001885] maps to DG do (dorsal outer GCL) in the atlas (HIP allocation 0.99).
- Neuropeptide Cck is expressed in this cluster.

**Concerns**

- Calbindin (Calb1), NeuN (Rbfox3), and Tbr1 are all APPROXIMATE alignments, not CONSISTENT. These markers are defined by protein IHC in the classical literature; they are absent from the atlas defining_markers because (1) protein abundance does not track mRNA linearly for structural/calcium-binding proteins; (2) Rbfox3 and Tbr1 are broadly expressed across mature neurons and are filtered out in cluster-level differential expression; (3) PSA-NCAM (negative marker) is a post-translational glycan epitope invisible to transcriptomics. These are methodological gaps, not biological discordances.
- The full classical type (CL:2000089) is split across nine clusters. This cluster represents only the dorsal outer GCL subpopulation.
- Whether Cck co-expression defines a stable functional subtype of mature granule neuron or reflects a transient, activity-dependent state is unresolved.

**What would upgrade confidence**

- MERFISH or smFISH co-labelling for Calb1 together with cluster-specific markers (Glis3, Prox1, St18) in adult mouse DG would confirm Calb1 mRNA expression in cells belonging to this cluster.
- IHC co-labelling of Calbindin protein with MERFISH-validated spatial markers for the DG do (dorsal outer GCL) would directly link the protein marker to the transcriptomic cluster.

---

## 0503 DG Glut_1 [CS20230722_CLUS_0503] — ventral GCL, Cck+ Grp+

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.68. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Hey2 — consistent with mature granule transcriptional identity.
- Stage-6 mature identity (DCX−/NeuN+/Calbindin+) is supported by literature [4]; Tbr1+ postmitotic identity supported by [5].
- NT consistent: Glut (Slc17a7/vGLUT1) [2][3].
- Soma: DG ve (ventral GCL); HIP allocation 0.93 — consistent with GCL [UBERON:0001885].
- Neuropeptides Cck and Grp expressed.

**Concerns**

- Same protein-transcriptome gap as all DG Glut clusters: Calbindin, NeuN, Tbr1 absent from atlas defining_markers (methodological, not biological).
- Cluster covers only the ventral GCL subpopulation of the classical type.
- Whether the Cck + Grp co-expression profile defines a stable subtype or an activity-dependent state is unresolved.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Prox1, Hey2 in adult mouse DG to confirm Calb1 expression in ventral GCL cells of this cluster.
- IHC for Calbindin protein co-registered with MERFISH spatial data for DG ve [UBERON:0001885].

---

## 0507 DG Glut_2 [CS20230722_CLUS_0507] — dorsal outer GCL, Cck+ Pdyn+

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.67. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Neurod2, St18 — shared mature granule core.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; soma DG do (dorsal outer GCL) HIP:0.98, consistent with GCL [UBERON:0001885].
- Neuropeptides Cck and Pdyn co-expressed.

**Concerns**

- Same protein-transcriptome gap applies.
- Covers only the dorsal outer GCL subpopulation.
- Pdyn co-expression: whether this indicates a stable enkephalinergic-variant granule neuron subtype or activity-dependent peptide induction is unresolved.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Neurod2, St18 in adult DG to confirm cluster identity in DG do cells.
- IHC for Calbindin protein in DG do with MERFISH-validated spatial markers.

---

## 0502 DG Glut_1 [CS20230722_CLUS_0502] — ventral GCL, Grp+ Cck+ (registration uncertainty)

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.64. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Rfx2, Lhx9 — expanded mature granule TF set.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; anatomical_location field specifies DG ve (ventral GCL), HIP:0.74 — consistent with GCL [UBERON:0001885].
- Neuropeptides Grp and Cck expressed.

**Concerns**

- Same protein-transcriptome gap applies.
- CCF broad annotation for this cluster includes MEA and sAMY, reflecting ventral hippocampal registration ambiguity *(note: the authoritative anatomical_location field specifies DG ve; CCF broad ambiguity does not alter the soma location claim, but independent spatial validation is warranted)*.
- Lower HIP allocation (0.74 vs. 0.93–0.99 for dorsal clusters) makes this ventral cluster more susceptible to registration error.
- Covers only the ventral GCL subpopulation.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Prox1, Rfx2, Lhx9 in adult DG to confirm expression in DG ve cells.
- IHC for Calbindin protein in DG ve with MERFISH spatial validation — particularly important given CCF registration ambiguity.

---

## 0505 DG Glut_2 [CS20230722_CLUS_0505] — dorsal outer GCL, no neuropeptides

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.63. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Neurod2, St18 — shared mature granule core.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; soma DG do (dorsal outer GCL) HIP:0.99, consistent with GCL [UBERON:0001885].
- No neuropeptide co-expression detected — this cluster may represent the "baseline" dorsal granule neuron without peptide co-expression.

**Concerns**

- Same protein-transcriptome gap applies.
- Covers only the dorsal outer GCL subpopulation.
- Absence of neuropeptide co-expression may distinguish this cluster from 0506 and 0507, but whether this is a stable subtype or reflects sampling or detection limits is unresolved.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Neurod2, St18 in adult DG, with confirmatory negative staining for Cck and Pdyn in the same cells.
- IHC for Calbindin protein in DG do with MERFISH spatial markers.

---

## 0508 DG Glut_3 [CS20230722_CLUS_0508] — dorsal outer GCL, Cck+ Pdyn+, Egr2/Egr4+

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.63. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Egr2, Egr4 — the Egr2/Egr4 combination is distinctive within the DG Glut subclass.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; soma DG do (dorsal outer GCL) HIP:0.96, consistent with GCL [UBERON:0001885].
- Neuropeptides Cck and Pdyn co-expressed.

**Concerns**

- Same protein-transcriptome gap applies.
- Egr2 and Egr4 are activity-regulated transcription factors; their prominence as cluster-defining markers raises the possibility that this cluster captures an activity state rather than a constitutively distinct subtype *(note: interpretation of Egr-high clusters as activity-dependent states vs. stable subtypes requires functional validation)*.
- Covers only the dorsal outer GCL subpopulation.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Egr2, Egr4 in resting vs. stimulated adult mice to test whether Egr2/Egr4 expression is constitutive or activity-induced.
- IHC for Calbindin protein in DG do with MERFISH spatial validation.

---

## 0504 DG Glut_1 [CS20230722_CLUS_0504] — ventral GCL, Grp+ Penk+ Cck+ Cartpt+ (registration uncertainty)

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.62. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Prox1, Nr4a3, Egr3, Rorb — richest neuropeptide and TF diversity in the ventral clusters.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; anatomical_location field specifies DG ve (ventral GCL), HIP:0.69 — consistent with GCL [UBERON:0001885].
- Four neuropeptides co-expressed: Grp, Penk, Cck, Cartpt — the most neuropeptide-rich cluster in this group.

**Concerns**

- Same protein-transcriptome gap applies.
- CCF broad annotation includes sAMY:0.2 — this is the lowest HIP allocation of all nine clusters (0.69), making ventral registration ambiguity most pronounced here *(note: the authoritative anatomical_location field specifies DG ve; the sAMY CCF annotation may reflect registration boundary error at the ventral hippocampal tip, but independent spatial validation is particularly warranted for this cluster)*.
- The extensive neuropeptide co-expression profile (four peptides) could reflect either a genuinely distinct ventral granule neuron subtype or a superposition of activity states captured during atlas sampling.
- Nr4a3, Egr3, and Rorb alongside Glis3/Prox1 suggest a transcriptionally distinct ventral identity; Neurod2 is notably absent from the defining marker set for this cluster.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Prox1, Nr4a3, Rorb in adult DG to confirm expression in DG ve cells.
- IHC for Calbindin protein in DG ve with MERFISH spatial validation — critical for this cluster given registration uncertainty.
- Targeted validation to exclude sAMY contamination: double FISH for DG ve markers and sAMY markers on the same tissue sections.

---

## 0510 DG Glut_4 [CS20230722_CLUS_0510] — posterior GCL, Cck+ Grp+ Pdyn+

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.62. [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, St18, Lhx9, Nr2f2 — the posterior GCL cluster has a distinctive TF combination that does not include Neurod2 or Prox1 as primary markers.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; soma DG po (posterior GCL) HIP:0.99, consistent with GCL [UBERON:0001885].
- Three neuropeptides co-expressed: Cck, Grp, Pdyn.

**Concerns**

- Same protein-transcriptome gap applies.
- This is the only cluster assigned to the posterior GCL (DG po) subregion. Posterior DG is less studied than dorsal or ventral; whether a distinct TF program (Lhx9, Nr2f2) in DG po granule neurons is a genuine topographic specialisation requires validation *(note: neuroanatomical interpretation of "posterior" vs. "dorsal" GCL position in the CCF framework warrants expert review)*.
- Three-peptide profile (Cck, Grp, Pdyn) is notable but its stability vs. activity-dependence is unresolved.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 with Glis3, Lhx9, Nr2f2, St18 in adult DG with explicit posterior section sampling to confirm DG po localization.
- IHC for Calbindin protein in DG po with MERFISH-validated markers.

---

## 0509 DG Glut_3 [CS20230722_CLUS_0509] — dorsal outer GCL, Cck+ Pdyn+ Npy+, stress-response TFs

**Supporting evidence**

- Atlas metadata: DG Glut subclass, CL:2000089 EXACT. Discovery composite score: 0.59 (lowest of the nine clusters). [ATLAS_METADATA]
- Core TF/MERFISH markers: Glis3, Neurod2, Atf3, Bhlhe41, Cebpb — the combination of Atf3 (stress-response TF) and Cebpb (C/EBPbeta, inflammatory/stress TF) alongside the mature granule core is distinctive.
- Stage-6 identity by literature [4]; Tbr1+ postmitotic state [5].
- NT consistent [2][3]; soma DG do (dorsal outer GCL) HIP:0.96, consistent with GCL [UBERON:0001885].
- Three neuropeptides: Cck, Pdyn, Npy.

**Concerns**

- Same protein-transcriptome gap applies.
- Atf3 and Cebpb are canonical immediate-early/stress-response genes strongly induced by cellular stress, inflammation, or neural activity. Their prominence as cluster-defining markers raises serious concern that this cluster captures a stress or damage state of mature granule neurons rather than a constitutively distinct subtype *(note: the presence of stress-response TFs as cluster-defining markers is the most significant biological concern for this edge; lowest discovery composite score also reflects greater uncertainty)*.
- Npy co-expression is also associated with stress and neuroinflammatory responses in hippocampal granule neurons.
- Covers the dorsal outer GCL subpopulation but has the lowest composite score of the nine clusters.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1, Glis3, Atf3, and Cebpb in adult DG tissue collected under controlled baseline conditions (minimising handling/stress-induced gene expression) vs. after a defined stressor — to determine whether Atf3/Cebpb expression is constitutive in a granule neuron subset or stress-induced.
- IHC for Calbindin protein in DG do with MERFISH spatial markers.
- Single-cell ATAC-seq to determine whether Atf3/Cebpb target loci are constitutively accessible in this cluster or only opened by stimulus.

---

## Proposed experiments

All experiments below are derived from unresolved questions and proposed experiments across all nine edges.

### MERFISH / smFISH — Calb1 co-localisation

| What | Target | Expected output | Resolves |
|---|---|---|---|
| MERFISH or smFISH co-labelling for Calb1 + Glis3 + cluster-specific TF markers (St18, Prox1, Hey2, Rfx2, Lhx9, Nr4a3, Rorb, Egr2, Egr4, Bhlhe41, Atf3, Nr2f2) | Adult mouse DG (all GCL subregions: dorsal outer, ventral, posterior) | Confirm or refute Calb1 mRNA expression within cells belonging to each of the nine DG Glut clusters | Whether Calb1 mRNA is detectable below atlas threshold, or calbindin protein accumulates via post-transcriptional regulation |

### IHC spatial validation — Calbindin protein

| What | Target | Expected output | Resolves |
|---|---|---|---|
| IHC co-labelling of Calbindin protein with MERFISH-validated spatial markers per GCL subregion (DG do, DG ve, DG po) | Adult mouse DG sections covering all three GCL topographic zones | Spatial overlap of Calbindin protein with each cluster's MERFISH marker profile | Protein-transcriptome gap for the cardinal mature marker; confirms cluster-to-protein-identity correspondence |

### Activity vs. constitutive state — stress-response TF clusters

| What | Target | Expected output | Resolves |
|---|---|---|---|
| MERFISH/smFISH for Atf3, Cebpb, Glis3, and Calb1 in baseline vs. acute stress conditions | Adult mouse DG, controlled handling + acute stressor | Whether Atf3/Cebpb expression is constitutive in a granule neuron subset or induced by stress | Whether cluster 0509 [CS20230722_CLUS_0509] represents a stable subtype or a stress state |

### Activity vs. constitutive state — Egr2/Egr4 clusters

| What | Target | Expected output | Resolves |
|---|---|---|---|
| MERFISH/smFISH for Egr2, Egr4, Glis3, and Calb1 in resting vs. stimulated adult mice | Adult mouse DG, resting vs. novelty/exploration paradigm | Whether Egr2/Egr4 expression is constitutive in a granule neuron subset or activity-induced | Whether cluster 0508 [CS20230722_CLUS_0508] represents a stable subtype or an activity state |

### Spatial validation — CCF registration at ventral hippocampus

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Double FISH for DG ve markers (Glis3 + Prox1 + Rfx2/Nr4a3) and sAMY markers on same tissue sections at the ventral hippocampal tip | Ventral hippocampal–amygdaloid border in adult mouse | Exclusion or confirmation of sAMY contamination in ventral DG clusters | CCF registration ambiguity for clusters 0502 [CS20230722_CLUS_0502] and 0504 [CS20230722_CLUS_0504] |

### Neuropeptide subtype stability

| What | Target | Expected output | Resolves |
|---|---|---|---|
| Single-cell RNA-seq or spatial transcriptomics in animals with varied behavioural histories (home cage, enriched environment, fear conditioning) | Adult mouse DG | Whether neuropeptide co-expression profiles (Cck, Grp, Pdyn, Penk, Cartpt, Npy) are stable across conditions or shift with experience | Whether neuropeptide-defined cluster identities represent stable mature granule neuron subtypes or transient activity-dependent states (applicable to all nine clusters) |

---

## Open questions

1. Is Calb1 mRNA expressed but below atlas detection threshold in all nine DG Glut clusters, or does calbindin protein accumulate via post-transcriptional regulation in terminally differentiated granule neurons?

2. Do the distinct neuropeptide profiles (Cck in 0506; Cck/Grp in 0503; Cck/Pdyn in 0507 and 0508; Grp/Cck in 0502; no peptides in 0505; Grp/Penk/Cck/Cartpt in 0504; Cck/Grp/Pdyn in 0510; Cck/Pdyn/Npy in 0509) reflect stable functional subtypes of mature granule neurons or transient, activity-dependent states?

3. Do clusters 0509 [CS20230722_CLUS_0509] (Atf3+/Cebpb+) and 0508 [CS20230722_CLUS_0508] (Egr2+/Egr4+) represent constitutively distinct mature granule neuron subtypes, or do they capture stress- and activity-dependent transcriptional states respectively?

4. Is the CCF registration ambiguity for ventral GCL clusters 0502 [CS20230722_CLUS_0502] (HIP:0.74, MEA/sAMY overlap) and 0504 [CS20230722_CLUS_0504] (HIP:0.69, sAMY:0.2) biologically meaningful (i.e., do some cells of these clusters genuinely reside in medial amygdaloid or striatal amygdaloid areas) or is it solely a registration artefact?

5. Does the posterior GCL cluster 0510 [CS20230722_CLUS_0510] — with a TF profile (Lhx9, Nr2f2, St18) distinct from dorsal and ventral clusters — represent a genuinely topographically specialised mature granule neuron identity, or is the posterior GCL classification a subdivision of dorsal DG that does not map to a distinct cell type?

6. Why is Neurod2 absent from the defining marker set of cluster 0504 [CS20230722_CLUS_0504], the only ventral cluster lacking it as a primary TF marker, given that Neurod2 is shared across all other DG Glut clusters as a core mature granule marker?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | ATLAS_METADATA; LITERATURE [4]; LITERATURE [5] | SUPPORT x 3 |

---

## References

[1] Tanaka 2019 · PMID:[31068541](https://pubmed.ncbi.nlm.nih.gov/31068541/) · DOI:10.2131/jts.44.357 · *Used for: soma location*

[2] Stoll 2014 · PMID:[26056581](https://pubmed.ncbi.nlm.nih.gov/26056581/) · DOI:10.1186/2052-8426-2-12 · *Used for: neurotransmitter type*

[3] Vangeneugden 2015 · PMID:[25954142](https://pubmed.ncbi.nlm.nih.gov/25954142/) · DOI:10.3389/fnins.2015.00110 · *Used for: neurotransmitter type*

[4] Micheli 2025 · PMID:[40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) · DOI:10.3389/fcell.2025.1605116 · *Used for: Calbindin marker; stage-6 mature identity definition*

[5] Hodge 2008 · PMID:[18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) · DOI:10.1523/JNEUROSCI.4280-07.2008 · *Used for: Tbr1 marker (postmitotic granule cells)*
