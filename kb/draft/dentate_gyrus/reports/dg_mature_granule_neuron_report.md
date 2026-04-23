# Dentate Gyrus Mature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | dentate gyrus granule cell (CL:2000089) · EXACT | — |
| Soma location | dentate gyrus of hippocampal formation [UBERON:0001885] — granule cell layer (GCL) | [1] |
| Neurotransmitter | Glutamatergic | [2] [3] |
| Defining markers | Calbindin, NeuN | [4] |
| Defining markers | Tbr1 | [5] |
| Negative markers | DCX, Nestin, PSA-NCAM | — |
| Neuropeptides | None documented | — |

**Morphology.** Terminally differentiated granule neurons (stage 6) populating the granule cell layer. Fully elaborated dendritic arbor and complete axonal projections to CA3. Receive primary glutamatergic afferents from entorhinal cortex and project mossy fiber axons to inhibitory interneurons and pyramidal cells of area CA3.

**Electrophysiology.** Fully synaptically integrated; functionally mature with established input from entorhinal cortex and output to CA3.

**Notes.** Terminal differentiation endpoint of the adult neurogenesis lineage in the dentate gyrus. Tis21 expression decreases in mature granule cells compared to the maturing stage. No subtypes are discussed in this report.

---

## Mapping candidates

All nine edges carry a TYPE_A_SPLITS relationship: the classical type dentate gyrus granule cell (CL:2000089) is distributed across nine DG Glut clusters (0502–0510) representing topographic variants of the granule cell layer (dorsal outer, ventral, posterior) and neuropeptide/functional variants. No single cluster captures the full classical type; the nine clusters collectively constitute the mapping.

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0506 DG Glut_2 [CS20230722_CLUS_0506] | DG Glut | — | 🔴 LOW | NT + GCL location (DG do, dorsal outer) | Speculative |
| 2 | 0503 DG Glut_1 [CS20230722_CLUS_0503] | DG Glut | — | 🔴 LOW | NT + GCL location (DG ve, ventral) | Speculative |
| 3 | 0507 DG Glut_2 [CS20230722_CLUS_0507] | DG Glut | — | 🔴 LOW | NT + GCL location (DG do, dorsal outer) | Speculative |
| 4 | 0502 DG Glut_1 [CS20230722_CLUS_0502] | DG Glut | — | 🔴 LOW | NT + GCL location (DG ve, ventral) | Speculative |
| 5 | 0505 DG Glut_2 [CS20230722_CLUS_0505] | DG Glut | — | 🔴 LOW | NT + GCL location (DG do, dorsal outer) | Speculative |
| 6 | 0508 DG Glut_3 [CS20230722_CLUS_0508] | DG Glut | — | 🔴 LOW | NT + GCL location (DG do, dorsal outer) | Speculative |
| 7 | 0504 DG Glut_1 [CS20230722_CLUS_0504] | DG Glut | — | 🔴 LOW | NT + GCL location (DG ve, ventral) | Speculative |
| 8 | 0510 DG Glut_4 [CS20230722_CLUS_0510] | DG Glut | — | 🔴 LOW | NT + GCL location (DG po, posterior) | Speculative |
| 9 | 0509 DG Glut_3 [CS20230722_CLUS_0509] | DG Glut | — | 🔴 LOW | NT + GCL location (DG do, dorsal outer) | Speculative |

Total: 9 edges. Relationship type: TYPE_A_SPLITS. The classical type splits across all nine DG Glut clusters collectively. Cell counts are not available in the atlas metadata ingested here.

---

## Candidate paragraphs

### A note on the shared evidence structure

All nine clusters are members of the DG Glut subclass and carry the same atlas subclass-level CL:2000089 EXACT mapping. Their supporting evidence and concerns are substantially identical at the level of neurotransmitter type, soma compartment, and the protein-transcriptome marker gap. Cluster-specific differences lie in (a) GCL topographic subdivision (dorsal outer, ventral, posterior), (b) TF and MERFISH marker combinations, (c) neuropeptide co-expression, and (d) composite discovery score. Differences are highlighted under each cluster section below.

---

## 0506 DG Glut_2 [CS20230722_CLUS_0506] · 🔴 LOW

Composite discovery score: 0.69. Topographic position: DG do (dorsal outer GCL). Core TF/MERFISH markers: Glis3, Neurod2, Prox1, St18. Neuropeptides: Cck.

**Supporting evidence**

- The cluster belongs to the DG Glut subclass, which carries an EXACT mapping to CL:2000089. Neurotransmitter type is glutamatergic, consistent with Slc17a7/vGLUT1 expression in the atlas, matching the classical type [2] [3].
- Soma position is assigned to the DG do (dorsal outer GCL) — a subdivision of the granule cell layer of dentate gyrus of hippocampal formation [UBERON:0001885] — consistent with the known GCL location of mature granule neurons [1].
- Core TF markers Glis3, Neurod2, Prox1, and St18 are transcriptional correlates of the mature granule identity at the atlas level, representing the cluster-level surrogate for the classical postmitotic TF cascade. The absence of DCX and Eomes from the cluster's marker set is consistent with stage-6 (mature) rather than stage-5 (immature) identity [4].
- Literature confirms that terminally differentiated neurons (stage 6) express calbindin and NeuN [4]. The DG Glut clusters represent this terminal state collectively.
- Tbr1 marks postmitotic granule cells and not progenitors [5]. The DG Glut clusters occupy the Tbr1+ stage even though Tbr1 is non-discriminating at cluster level.

**Concerns**

- Calbindin (Calb1 protein) is the cardinal mature granule neuron marker but does not appear in the cluster's defining_markers list. Calb1 mRNA may be present below the atlas detection threshold, or calbindin protein may accumulate via post-transcriptional regulation in terminally differentiated cells. The atlas subclass mapping notes assert calbindin expression for DG Glut broadly, but this gap — APPROXIMATE alignment — requires direct verification. *(note: this is a methodological gap between protein IHC and scRNA-seq, not evidence of biological discordance.)*
- NeuN (Rbfox3) and Tbr1 are broadly expressed in mature neurons and are filtered out by the atlas differential expression framework as non-discriminating at cluster level; their absence from defining_markers does not imply absence of expression.
- PSA-NCAM is a post-translational glycan epitope undetectable by transcriptomics, so its negative status cannot be confirmed from atlas data.
- This cluster covers only the DG do (dorsal outer GCL) subpopulation. It is one component of a nine-way split; confidence cannot exceed LOW for any individual cluster in the absence of additional direct evidence.
- Neuropeptide Cck is expressed in this cluster. Whether this reflects a stable functional subtype of mature granule neurons or a transient activity-dependent state is unresolved.

**What would upgrade confidence**

- MERFISH or smFISH with Calb1, Glis3, and Neurod2 probes in adult mouse DG to confirm that Calb1 mRNA co-localises with cells mapping to this cluster.
- IHC co-labelling of Calbindin protein with atlas-validated markers in the DG do (dorsal outer GCL) zone to confirm spatial correspondence.
- Determining whether the Cck neuropeptide profile represents a stable cell state or an activity-dependent signature (e.g. activity-state comparison by scRNA-seq or FISH under different behavioural paradigms).

---

## 0503 DG Glut_1 [CS20230722_CLUS_0503] · 🔴 LOW

Composite discovery score: 0.68. Topographic position: DG ve (ventral GCL). Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Hey2. Neuropeptides: Cck, Grp.

**Supporting evidence**

- DG Glut subclass carries EXACT mapping to CL:2000089; glutamatergic NT type (Slc17a7/vGLUT1) is consistent with the classical type [2] [3].
- Soma assigned to DG ve (ventral GCL), a subdivision of dentate gyrus of hippocampal formation [UBERON:0001885]; consistent with GCL location of mature granule neurons [1].
- Core TFs Glis3, Neurod2, Prox1, Hey2 represent the atlas-level transcriptional correlates of mature granule identity. Absence of DCX/Eomes is consistent with stage-6 identity [4].
- Stage-6 calbindin/NeuN expression confirmed by literature [4]; Tbr1 marks postmitotic granule cells [5].

**Concerns**

- Calbindin/NeuN/Tbr1 absent from defining_markers: same protein–transcriptome gap as 0506. APPROXIMATE alignment on all three markers [4] [5].
- Neuropeptides Cck and Grp — whether these reflect stable subtypes or activity-dependent states is unresolved.
- One component of the nine-way split; low individual-cluster confidence.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG ve (ventral GCL) region, confirming Calb1 co-localisation with the cluster marker signature.
- IHC co-labelling of Calbindin protein with MERFISH-validated markers in the ventral GCL zone.
- Characterisation of Grp and Cck expression as stable vs. activity-dependent cell states.

---

## 0507 DG Glut_2 [CS20230722_CLUS_0507] · 🔴 LOW

Composite discovery score: 0.67. Topographic position: DG do (dorsal outer GCL). Core TF/MERFISH markers: Glis3, Neurod2, St18. Neuropeptides: Cck, Pdyn.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent with classical type [2] [3].
- Soma in DG do (dorsal outer GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3, Neurod2, St18 serve as mature-granule transcriptional surrogates; DCX/Eomes absent, consistent with stage-6 status [4].
- Stage-6 marker evidence from literature [4] [5].

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- Neuropeptides Cck and Pdyn: stable subtype vs. activity-dependent state unresolved.
- One of nine clusters; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG do (dorsal outer GCL) region.
- IHC co-labelling of Calbindin protein with MERFISH markers in the dorsal outer GCL zone.
- Resolving whether Pdyn co-expression defines a constitutive functional state or a transient signature.

---

## 0502 DG Glut_1 [CS20230722_CLUS_0502] · 🔴 LOW

Composite discovery score: 0.64. Topographic position: DG ve (ventral GCL). Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Rfx2, Lhx9. Neuropeptides: Grp, Cck.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent [2] [3].
- Soma in DG ve (ventral GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3, Neurod2, Prox1, Rfx2, Lhx9 as mature-granule transcriptional surrogates; consistent with stage-6 [4].
- Stage-6 marker evidence from literature [4] [5].

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- An additional caveat applies specifically to this cluster: the CCF broad annotation includes MEA and sAMY, indicating ventral hippocampal registration ambiguity. The authoritative anatomical_location field specifies DG ve; the CCF broad ambiguity does not alter the soma location claim, but represents a registration uncertainty at the cluster level. *(note: this caveat is specific to 0502 among the ventral clusters.)*
- Neuropeptides Grp and Cck: stable subtype vs. activity-dependent state unresolved.
- One of nine clusters; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG ve (ventral GCL) region, ideally with landmarks to distinguish DG from adjacent amygdalar nuclei.
- IHC co-labelling of Calbindin in ventral GCL with regional landmarks confirming DG identity.
- Spatial registration refinement to reduce the CCF broad ambiguity for ventral hippocampal clusters.

---

## 0505 DG Glut_2 [CS20230722_CLUS_0505] · 🔴 LOW

Composite discovery score: 0.63. Topographic position: DG do (dorsal outer GCL). Core TF/MERFISH markers: Glis3, Neurod2, St18. Neuropeptides: none.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent [2] [3].
- Soma in DG do (dorsal outer GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3, Neurod2, St18 as mature-granule surrogates; DCX/Eomes absent, consistent with stage-6 [4].
- Stage-6 marker evidence from literature [4] [5].
- *(note: this cluster is the only one among the nine with no detected neuropeptide co-expression, which may make it the most transcriptomically canonical granule cell variant in the atlas.)*

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- The absence of neuropeptide expression does not resolve whether the cluster is a distinct stable subtype or simply reflects a low-expression state.
- One of nine clusters; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG do (dorsal outer GCL).
- IHC co-labelling of Calbindin protein with MERFISH-validated markers in the dorsal outer GCL zone.
- Determining whether the absence of neuropeptide detection reflects genuine absence, lower expression below threshold, or a distinct cell state.

---

## 0508 DG Glut_3 [CS20230722_CLUS_0508] · 🔴 LOW

Composite discovery score: 0.63. Topographic position: DG do (dorsal outer GCL). Core TF/MERFISH markers: Glis3, Neurod2, Prox1, Egr2, Egr4. Neuropeptides: Cck, Pdyn.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent [2] [3].
- Soma in DG do (dorsal outer GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3, Neurod2, Prox1, Egr2, Egr4 as mature-granule surrogates; consistent with stage-6 [4].
- Stage-6 marker evidence from literature [4] [5].
- *(note: the presence of Egr2 and Egr4 — activity-regulated transcription factors — may indicate that this cluster captures a more activity-responsive state of mature granule neurons.)*

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- Neuropeptides Cck and Pdyn: whether these reflect stable subtypes or activity-dependent signatures is unresolved.
- One of nine clusters; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG do (dorsal outer GCL).
- IHC co-labelling of Calbindin protein with MERFISH markers in the dorsal outer GCL zone.
- Functional experiments (e.g. activity manipulation) to determine whether Egr2/Egr4 and Pdyn expression are constitutive or activity-induced in mature granule neurons.

---

## 0504 DG Glut_1 [CS20230722_CLUS_0504] · 🔴 LOW

Composite discovery score: 0.62. Topographic position: DG ve (ventral GCL). Core TF/MERFISH markers: Glis3, Prox1, Nr4a3, Egr3, Rorb. Neuropeptides: Grp, Penk, Cck, Cartpt.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent [2] [3].
- Soma in DG ve (ventral GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3, Prox1, Nr4a3, Egr3, Rorb as mature-granule surrogates; consistent with stage-6 [4].
- Stage-6 marker evidence from literature [4] [5].
- *(note: this cluster has the richest neuropeptide co-expression profile of the nine (Grp, Penk, Cck, Cartpt), suggesting it may represent a distinctly ventral-biased, neuropeptide-enriched mature granule neuron variant.)*

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- A registration uncertainty caveat applies: CCF broad annotation includes sAMY:0.2, indicating ventral hippocampal registration ambiguity. The authoritative anatomical_location field specifies DG ve.
- Neuropeptides Grp, Penk, Cck, Cartpt: whether this multi-peptide profile reflects stable functional subtyping or activity-dependent regulation is unresolved.
- One of nine clusters; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG ve (ventral GCL) with regional landmarks.
- IHC co-labelling of Calbindin protein with MERFISH markers in the ventral GCL, with spatial landmarks to resolve the sAMY registration ambiguity.
- Characterisation of Penk and Cartpt neuropeptide profiles as stable vs. activity-regulated in mature ventral granule neurons.

---

## 0510 DG Glut_4 [CS20230722_CLUS_0510] · 🔴 LOW

Composite discovery score: 0.62. Topographic position: DG po (posterior GCL). Core TF/MERFISH markers: Glis3, St18, Lhx9, Nr2f2. Neuropeptides: Cck, Grp, Pdyn.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent [2] [3].
- Soma in DG po (posterior GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3, St18, Lhx9, Nr2f2 as mature-granule surrogates; consistent with stage-6 [4].
- Stage-6 marker evidence from literature [4] [5].
- *(note: this is the only cluster assigned to the posterior GCL, making it the sole representative of the posterior topographic axis within the nine-way split.)*

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- Neuropeptides Cck, Grp, and Pdyn: stable subtype vs. activity-dependent state unresolved.
- One of nine clusters; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1 and Glis3 in DG po (posterior GCL), which has been less extensively studied than dorsal or ventral GCL.
- IHC co-labelling of Calbindin protein with MERFISH-validated markers in the posterior GCL zone.
- Resolving whether the distinctive posterior TF signature (Lhx9, Nr2f2) reflects a stable positional identity or temporal variation.

---

## 0509 DG Glut_3 [CS20230722_CLUS_0509] · 🔴 LOW

Composite discovery score: 0.59. Topographic position: DG do (dorsal outer GCL). Core TF/MERFISH markers: Glis3, Neurod2, Atf3, Bhlhe41, Cebpb. Neuropeptides: Cck, Pdyn, Npy.

**Supporting evidence**

- DG Glut subclass; EXACT CL:2000089 mapping; glutamatergic NT consistent [2] [3].
- Soma in DG do (dorsal outer GCL), dentate gyrus of hippocampal formation [UBERON:0001885] [1].
- TFs Glis3 and Neurod2 provide the mature-granule core identity; consistent with stage-6 [4].
- Stage-6 marker evidence from literature [4] [5].
- *(note: this cluster has the lowest composite discovery score of the nine (0.59). The presence of Atf3, Bhlhe41, and Cebpb — stress-responsive and circadian transcription factors — as cluster-distinguishing markers may indicate an activity- or stress-responsive mature granule neuron state, which would explain the lower discovery score relative to constitutively marked clusters.)*

**Concerns**

- Calbindin/NeuN/Tbr1 protein–transcriptome gap; APPROXIMATE alignment [4] [5].
- Atf3, Bhlhe41, and Cebpb are known stress/activity-regulated TFs; their prominence as defining markers raises the question of whether this cluster captures a distinct cell state or a transient activation programme within otherwise mature granule neurons.
- Neuropeptides Cck, Pdyn, and Npy: stable subtype vs. activity-dependent state unresolved. The three-peptide co-expression profile is notable.
- One of nine clusters; lowest individual composite score; individual confidence cannot exceed LOW.

**What would upgrade confidence**

- MERFISH/smFISH for Calb1, Glis3, and Atf3 in DG do (dorsal outer GCL) to confirm whether the Atf3+ signature co-localises with calbindin-positive mature granule neurons.
- Activity or stress perturbation experiments to determine whether Atf3/Bhlhe41/Cebpb markers are constitutive or induced in mature granule neurons.
- IHC co-labelling of Calbindin protein with MERFISH markers in the dorsal outer GCL zone.

---

## Proposed experiments

Because this mapping is a TYPE_A_SPLITS across nine clusters, the experiments described below are designed to validate the collective mapping. No single experiment resolves only one cluster; results should be interpreted across the whole set. Cross-check against existing atlas metadata and published spatial data before initiating new experiments.

### Spatial transcriptomics (MERFISH / smFISH)

- **What:** MERFISH or smFISH panel co-labelling Calb1, Glis3, Neurod2, and selected cluster-specific TF markers (e.g. Hey2 for 0503, Egr2/Egr4 for 0508, Lhx9/Nr2f2 for 0510) in adult mouse DG sections.
- **Target:** Confirm Calb1 mRNA co-localisation with Glis3+ cells across dorsal outer, ventral, and posterior GCL subdivisions. Quantitative threshold: the majority of Glis3+/Neurod2+ cells should be Calb1+ in at least dorsal and ventral compartments.
- **Expected output:** Spatial map resolving Calb1 expression within each topographic GCL subdivision; establishes whether the protein–transcriptome gap for Calb1 is attributable to detection sensitivity or genuine transcriptional absence.
- **Resolves:** Calb1 APPROXIMATE alignment on all nine edges; distinguishes protein–transcriptome gap from biological discordance.

### Protein immunohistochemistry

- **What:** IHC co-labelling of Calbindin protein with MERFISH-validated cluster markers (e.g. anti-Glis3 or anti-Prox1) in adult mouse DG.
- **Target:** Confirm that Calbindin+ cells in GCL subdivisions (dorsal outer, ventral, posterior) carry the transcriptional TF signatures present in each cluster.
- **Expected output:** Establishes protein-level correspondence between atlas cluster TF markers and classical Calbindin positivity. Resolves the marker gap for NeuN and Calbindin simultaneously if Rbfox3 antibody is included in the panel.
- **Resolves:** Calbindin and NeuN APPROXIMATE alignments; provides IHC-level evidence to upgrade edge confidence.

### Regional landmark controls for ventral GCL clusters

- **What:** For clusters 0502 [CS20230722_CLUS_0502] and 0504 [CS20230722_CLUS_0504], apply spatial methods that include anatomical landmarks distinguishing DG ventral GCL from adjacent medial amygdalar area (MEA) and striato-amygdaloid transition area (sAMY).
- **Target:** Confirm that Glis3+/Neurod2+/Calb1+ cells are located within the hippocampal formation boundary, not in amygdalar tissue.
- **Expected output:** Resolves CCF broad registration ambiguity for ventral clusters; provides spatial confirmation of DG identity.
- **Resolves:** MERFISH_REGISTRATION_UNCERTAINTY caveat for edges to 0502 [CS20230722_CLUS_0502] and 0504 [CS20230722_CLUS_0504].

### Activity-state characterisation

- **What:** Parallel scRNA-seq or snRNA-seq from adult DG under baseline, high-activity (voluntary wheel running), and stress conditions, with cluster identity inferred from the atlas marker gene set.
- **Target:** Determine whether clusters 0508 [CS20230722_CLUS_0508] (Egr2/Egr4/Pdyn), 0509 [CS20230722_CLUS_0509] (Atf3/Bhlhe41/Cebpb/Npy), and 0504 [CS20230722_CLUS_0504] (Grp/Penk/Cck/Cartpt) shift in proportion or marker intensity across conditions.
- **Expected output:** Evidence that neuropeptide-enriched and stress-TF-positive clusters reflect stable constitutive cell states vs. activity-induced transient states.
- **Resolves:** Unresolved questions about neuropeptide profiles across all nine clusters; particularly pressing for 0509 [CS20230722_CLUS_0509].

---

## Open questions

Deduplicated and consolidated across all nine edges. Questions appearing on multiple edges are noted.

1. **Calb1 mRNA detection gap (all 9 edges).** Is Calb1 mRNA expressed but below the atlas detection threshold in each DG Glut cluster, or does calbindin protein accumulate through post-transcriptional regulation in terminally differentiated granule neurons? MERFISH or smFISH with a Calb1 probe would resolve this for each GCL topographic subdivision.

2. **Neuropeptide profiles as stable subtypes vs. transient states (all 9 edges).** The nine clusters collectively express a range of neuropeptide combinations: Cck alone (0506), Cck+Grp (0503), Cck+Pdyn (0507, 0508), Grp+Cck (0502), none (0505), Grp+Penk+Cck+Cartpt (0504), Cck+Grp+Pdyn (0510), Cck+Pdyn+Npy (0509). Do these profiles represent stable, heritable functional subtypes of mature granule neurons, or do they reflect transient activity-dependent transcriptional states?

3. **Activity- and stress-responsive TF signatures (0508, 0509).** Cluster 0508 [CS20230722_CLUS_0508] shows Egr2 and Egr4 as defining markers; cluster 0509 [CS20230722_CLUS_0509] shows Atf3, Bhlhe41, and Cebpb. These are known activity-regulated and stress-responsive TFs. Are these clusters constitutive mature granule neuron states, or do they capture a subset of mature neurons in an activity-engaged or stressed state at the time of tissue collection?

4. **Ventral GCL registration ambiguity (0502, 0504).** CCF broad annotations for clusters 0502 [CS20230722_CLUS_0502] and 0504 [CS20230722_CLUS_0504] include contributions from MEA and sAMY. Although the authoritative anatomical_location field specifies DG ve for both, spatial validation is needed to confirm hippocampal identity of cells in these clusters.

5. **Posterior GCL representation (0510).** Cluster 0510 [CS20230722_CLUS_0510] is the sole cluster assigned to the posterior GCL. Is the posterior GCL genuinely represented by a single cluster in the atlas, or are additional posterior clusters present at a finer resolution not captured at the cluster level assessed here?

6. **Protein-level Tbr1 expression in DG Glut clusters (all 9 edges).** Tbr1 is confirmed as a postmitotic granule cell marker [5] but is absent from atlas defining_markers across all nine clusters. Would targeted Tbr1 IHC in DG Glut cluster-validated cells confirm the expected Tbr1+ status, and does this validate the indirect evidence that these clusters represent the Tbr1+ mature stage?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0506 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0503 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0507 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0502 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0505 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0508 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0504 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0510 | LITERATURE [5] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | ATLAS_METADATA | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | LITERATURE [4] | SUPPORT |
| edge_dg_mature_granule_neuron_to_CS20230722_CLUS_0509 | LITERATURE [5] | SUPPORT |

No evidence items with REFUTE or PARTIAL support are present in the facts file. All 27 evidence items are SUPPORT.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tanaka 2019 | PMID:31068541 | Soma location (granule cell layer) |
| [2] | Stoll 2014 | PMID:26056581 | Neurotransmitter type (glutamatergic) |
| [3] | Vangeneugden 2015 | PMID:25954142 | Neurotransmitter type (glutamatergic) |
| [4] | Micheli 2025 | PMID:40519263 | Stage-6 mature granule neuron markers (Calbindin, NeuN); neurogenesis lineage staging |
| [5] | Hodge 2008 | PMID:18385329 | Tbr1 as postmitotic granule cell marker |
