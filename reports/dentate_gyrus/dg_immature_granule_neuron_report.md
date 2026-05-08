# Dentate Gyrus Immature Granule Neuron — Allen Brain Cell Atlas CCN202307220 Mapping Report
*draft · 2026-04-14 · Source: `kb/draft/dentate_gyrus/20260414_dentate_gyrus_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

**CL term:** immature dentate gyrus granule neuron (CL:9900002) — EXACT mapping

| Property | Value | References |
|---|---|---|
| Soma location | dentate gyrus granule cell layer [UBERON:0005381]; specifically the inner granule cell layer (GCL), into which postmitotic cells migrate from the SGZ | [1], [2] |
| Neurotransmitter | Glutamatergic | [3], [4] |
| Defining markers | DCX (doublecortin), NeuN (RBFOX3), PSA-NCAM, Tis21 (BTG2) | [5], [6], [7] |
| Negative markers | Calbindin (absent at this stage; acquired upon terminal maturation) | — |
| Neuropeptides | None documented | — |

**Stage context.** Immature granule neurons correspond to stage 5 of adult hippocampal neurogenesis: postmitotic cells that co-express DCX and NeuN but have not yet acquired Calbindin. They have migrated from the subgranular zone (SGZ) into the inner granule cell layer [UBERON:0005381], where they begin axonal outgrowth toward CA3 (reaching it by approximately 10–11 days) and develop dendritic spines over the first weeks of maturation. Tis21 (Btg2) re-appears during this postmitotic phase, distinguishing it from progenitor stages [7]. The presence of Tbr1 — a canonical postmitotic transcription factor — marks the definitive transition from neuroblast to immature granule neuron [8].

The stage-5 definition from Micheli et al. 2025 [5]:

> "Neural stem cells (NSCs) progressively develop into proliferating neural progenitor cells (NPCs), designated as type-2a (Nestin + / Sox2 + ), type-2b cells (expressing Nestin and doublecortin: Nestin + /DCX + ) and neuroblasts (type-3, DCX + ) (Filippov et al., 2003) (Fukuda et al., 2003)(Kronenberg et al., 2003)(Steiner et al., 2006). Neuroblasts progress toward immature postmitotic granule neurons co-expressing DCX and NeuN (stage 5), and eventually become terminally differentiated neurons (stage 6) expressing calbindin and NeuN (Brandt et al., 2003)Steiner et al., 2004)."
> — Micheli et al. 2025, Dentate Gyrus Immature Neurons · [5] <!-- quote_key: 279046466_998847af -->

The immature neuron protein marker profile from Stepień et al. 2021 [6]:

> "Three types of proliferatively active cells have been identified in the granular layer of the dentate gyrus (DG) of the hippocampus: type I cells -radial glial-like stem cells expressing glial fibrillary acidic protein (GFAP) and Sox2; type II cells -non-sessile cells expressing nestin, also referred to as transiently activated progenitor cells, neuroblasts expressing doublecortin (DCX); and Ki67 proteins and immature neurons expressing the DCX protein, PSA-NCAM, a marker of migrating neurons (polysialylated neuronal cell adhesion molecules) and neuron-specific protein (NeuN) (Attardo et al., 2009)(Gault et al., 2021). On the other hand, three types of cells were distinguished in the subventricular zone (SVZ): B1-type astrocytic stem cells, GFAP-positive, C-type progenitor cells expressing the Mash1 protein, and neuroblasts expressing the DCX protein (Okano et al., 2008)."
> — Stepień et al. 2021, Dentate Gyrus Immature Neurons · [6] <!-- quote_key: 245432259_44d5c91b -->

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] | DG-PIR Ex IMN_2 | n/a | 🔴 LOW | Tbr1+ / Calb1− postmitotic | Speculative |
| 2 | 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515] | DG-PIR Ex IMN_2 | n/a | 🔴 LOW | Tbr1+ / Calb1− postmitotic | Speculative |

**Total:** 2 edges. Relationship type: TYPE_A_SPLITS — the classical type distributes across both clusters; neither cluster alone fully represents the immature granule neuron stage.

---

## 0514 DG-PIR Ex IMN_2 [CS20230722_CLUS_0514] · 🔴 LOW

### Supporting evidence

- **EXACT CL:9900002 in atlas metadata.** The Allen Brain Cell Atlas CCN202307220 assigns immature dentate gyrus granule neuron (CL:9900002) to cluster [CS20230722_CLUS_0514] with an EXACT match; the curator annotation reads "late neuroblast/immature granule cell." Discovery composite score: 0.82.
- **Tbr1 transcription factor marks the postmitotic transition.** Tbr1 is present as a defining TF marker of cluster [CS20230722_CLUS_0514]. Hodge et al. 2008 [8] established experimentally that Tbr1 expression is restricted to postmitotic granule cells and is never detected in progenitors — Tbr1 did not colocalize with nestin-GFP in any proliferating cell, confirming its postmitotic specificity.

- **Calbindin absence is consistent with pre-terminal identity.** Cluster [CS20230722_CLUS_0514] lacks Calb1 (Calbindin) from its defining markers, consistent with stage 5 (DCX+/NeuN+/Calbindin−) rather than terminal stage 6, per Micheli et al. 2025 [5].
- **Additional TF markers and spatial validation.** Cluster [CS20230722_CLUS_0514] carries the core signature Prox1+/Emx2+/Igfbpl1+, MERFISH-validated in the DGdo,me (dentate gyrus dorsal/medial blade) spatial context, which corresponds to the classical inner GCL [UBERON:0005381]. MERFISH hippocampal probability HIP:0.98.
- **Glutamatergic NT is CONSISTENT.** Both the classical type (glutamatergic, [3], [4]) and the atlas cluster (Glut by direct assignment) align on neurotransmitter identity.
- **Tis21 re-expression in postmitotic DG neurons is consistent.** Attardo et al. 2009 showed that Tis21 is re-expressed in maturing postmitotic neurons and proposed this marks functional integration [7]:

> "During embryonic cortical development, expression of Tis21 is associated with cell cycle lengthening and neurogenic divisions of progenitor cells. We here investigated if the expression pattern of Tis21 also correlates with the generation of new neurons in the adult hippocampus. We used Tis21 knock-in mice expressing green fluorescent protein (GFP) and studied Tis21-GFP expression together with markers of adult hippocampal neurogenesis in newly generated cells. We found that Tis21-GFP 1) was absent from the radial glia–like putative stem cells (type-1 cells), 2) first appeared in transient amplifying progenitor cells (type-2 and 3 cells), 3) did not colocalize with markers of early postmitotic maturation stage, 4) was expressed again in maturing neurons, and 5) finally decreased in mature granule cells. Our data show that, in the course of adult neurogenesis, Tis21 is expressed in a phase additional to the one of the embryonic neurogenesis. This additional phase of expression might be associated with a new and different function of Tis21 than during embryonic brain development, where no Tis21 is expressed in mature neurons. We hypothesize that this function is related to the final functional integration of the newborn neurons. Tis21 can thus serve as new marker for key stages of adult neurogenesis."
> — Attardo et al. 2009, Dentate Gyrus Immature Neurons · [7] <!-- quote_key: 7393550_b2644450 -->

### Concerns

- **DCX protein not in atlas defining_markers (APPROXIMATE).** The classical stage-5 identity is defined by DCX protein positivity, but DCX does not appear in the cluster's ranked scRNA-seq markers. This is an expected methodological gap: Dcx mRNA is broadly expressed across the DG-PIR Ex IMN subclass and is filtered out during cluster-level marker selection. The curator annotation "late neuroblast/immature granule cell" is compatible with DCX+ protein status, but direct confirmation is lacking.
- **NeuN (RBFOX3) not in atlas defining_markers (APPROXIMATE).** Rbfox3 is non-discriminating at this cluster level in the atlas. Tbr1 TF presence makes NeuN+ status biologically expected, but is not directly confirmed.
- **PSA-NCAM not assessable (NOT_ASSESSED).** PSA-NCAM is a post-translational glycan epitope intrinsically undetectable by RNA-seq. This gap is methodological, not biological.
- **Tis21 (Btg2) not in atlas defining_markers (APPROXIMATE).** Btg2 may be broadly expressed or below the cluster-level marker ranking threshold. No direct conflict, but the alignment is indirect.
- **Protein-to-mRNA general caveat.** Atlas defining_markers are derived from scRNA-seq; protein abundance does not track mRNA linearly for structural proteins. All APPROXIMATE alignments reflect this methodological gap, not biological discordance.
- **Gad1 nt_marker signal in cluster 0514 (score 5.56).** A Gad1 signal is present at cluster level. This is unexplained and may reflect: (a) transient GABAergic depolarisation signalling known in immature granule neurons, (b) doublet artefact, or (c) cluster contamination. This warrants investigation before the edge is accepted.
- **TYPE_A_SPLITS caveat.** The classical immature granule neuron type is distributed across two clusters — [CS20230722_CLUS_0514] and [CS20230722_CLUS_0515] — both carrying EXACT CL:9900002. Neither cluster alone fully represents the classical type.
- **Pending literature evidence.** Twelve proposed literature evidence items are pending review and attachment to this edge and its companion edge to [CS20230722_CLUS_0515].

### What would upgrade confidence

- Co-stain of anti-DCX + anti-Tbr1 on adult mouse DG to confirm that Tbr1+ inner-GCL cells are also DCX+/NeuN+ at protein level, directly bridging the atlas TF profile and the classical stage-5 definition.
- Query of the full Allen Brain Cell Atlas CCN202307220 feature matrix for Dcx, Rbfox3, and Btg2 in clusters 0514 and 0515 to check whether these transcripts are present below the marker ranking threshold.
- Resolution of the Gad1 signal: targeted smFISH or patch-seq to determine whether GABAergic markers reflect transient physiology, doublets, or contamination.

---

## 0515 DG-PIR Ex IMN_2 [CS20230722_CLUS_0515] · 🔴 LOW

### Supporting evidence

- **EXACT CL:9900002 in atlas metadata.** Cluster [CS20230722_CLUS_0515] carries an EXACT CL:9900002 assignment, with curator annotation "late neuroblast." Discovery composite score: 0.82. MERFISH hippocampal probability HIP:1.0 (perfect allocation).
- **Identical core TF profile to cluster 0514.** Tbr1+/Prox1+/Emx2+/Igfbpl1+ is present, providing the same postmitotic bridge via Hodge et al. 2008 [8] (see Supporting evidence for cluster 0514). MERFISH validation places this cluster in DGdo,me, overlapping the classical inner GCL [UBERON:0005381].
- **Calbindin absence is consistent with pre-terminal identity** (same argument as cluster 0514; [5]).
- **Additional markers Bcl11b, Cd24a, Fam163a (MERFISH) and scoped marker Rarb.** Retinoic acid receptor beta (Rarb) distinguishes cluster [CS20230722_CLUS_0515] within the subclass; Bcl11b is a transcription factor associated with neuronal maturation. These may indicate a distinct maturational sub-stage or transcriptional state relative to cluster 0514.
- **Glutamatergic NT inherited from parent class.** Glut assignment for cluster [CS20230722_CLUS_0515] is by parent-class inheritance (no direct cluster-level assignment). This is consistent with the classical glutamatergic identity [3], [4], though the evidence is weaker than for cluster 0514.
- **Tis21 re-expression consistent** (same reasoning as cluster 0514; [7]).

### Concerns

- **DCX, NeuN, PSA-NCAM, Tis21 APPROXIMATE or NOT_ASSESSED** (same methodological caveats as cluster 0514 apply in full; see above).
- **NT type not directly assigned at cluster level.** Cluster [CS20230722_CLUS_0515] has no direct cluster-level nt_type_combo_label; glutamatergic identity is inherited from the parent class. This is weaker NT evidence than the direct Glut assignment in cluster 0514.
- **Gad1 signal in cluster 0515 (score 3.67).** The same Gad1 nt_marker signal is present (lower than in cluster 0514 at score 5.56), raising the same interpretive ambiguity. *(note: if cluster 0515 has a lower Gad1 score than cluster 0514, it may represent a later maturational state with waning GABAergic signalling — but this is speculative.)*
- **Biological basis for the 0514/0515 split is unresolved.** Rarb and Bcl11b/Cd24a/Fam163a distinguish cluster 0515 from cluster 0514, but whether this reflects a maturational sub-stage, sex composition, circadian/activity-dependent state, or technical stratification is unknown.
- **TYPE_A_SPLITS and pending evidence** caveats identical to cluster 0514 (see above).

### What would upgrade confidence

- RNA velocity or pseudotime analysis on the DG-PIR Ex IMN_2 supertype (clusters 0512–0515) to determine the ordering of clusters along the neuroblast-to-immature-GN differentiation axis, and to determine whether cluster 0515 precedes or follows cluster 0514.
- Targeted smFISH for Tbr1, Rarb, Bcl11b, and Dcx in adult DG to determine whether Rarb+/Bcl11b+ cells form a distinct subpopulation within the inner GCL and whether they are spatially segregated from Rarb− cells.
- Direct cluster-level NT assignment for cluster 0515 to strengthen glutamatergic evidence.

---

## Eliminated candidates

No edges were assessed as UNCERTAIN in this facts file. Both candidate edges are LOW confidence.

---

## Proposed experiments

### 1. Protein co-localisation (IHC/IF)

**What:** Anti-DCX + anti-Tbr1 co-immunostaining on adult mouse coronal DG sections.
**Target:** Confirm that Tbr1+ cells in the inner GCL [UBERON:0005381] are also DCX+/NeuN+ at protein level in the same spatial region validated by MERFISH.
**Expected output:** Protein-level CONSISTENT alignment for the DCX and NeuN properties currently scored APPROXIMATE; would upgrade APPROXIMATE to CONSISTENT for both clusters.
**Resolves:** Marker alignment uncertainty for DCX and NeuN in edges to both [CS20230722_CLUS_0514] and [CS20230722_CLUS_0515]; addresses the core protein-to-mRNA gap.

### 2. Atlas feature matrix query (bioinformatic)

**What:** Query the full Allen Brain Cell Atlas CCN202307220 gene expression matrix for Dcx, Rbfox3 (NeuN), and Btg2 (Tis21) in clusters 0514 and 0515.
**Target:** Determine whether these transcripts are present at sub-threshold expression levels not captured by cluster-defining marker selection.
**Expected output:** Sub-threshold expression data; would either confirm expected co-expression (strengthening APPROXIMATE alignments) or reveal absence (requiring re-evaluation of stage identity).
**Resolves:** DCX, NeuN, and Tis21 APPROXIMATE alignments for both edges.

### 3. Pseudotime / RNA velocity (bioinformatic)

**What:** RNA velocity or pseudotime trajectory analysis on the DG-PIR Ex IMN_2 supertype, encompassing clusters 0512–0515.
**Target:** Establish the relative ordering of clusters 0514 and 0515 along the neuroblast-to-immature-GN differentiation axis.
**Expected output:** Directed trajectory placing clusters in maturational sequence; would clarify whether cluster 0515 is earlier or later than cluster 0514, and whether both correspond to the same classical stage or adjacent stages.
**Resolves:** The biological basis of the 0514/0515 split; the question of whether Gad1 signal diminishes with maturation.

### 4. Spatial transcriptomics (smFISH / MERFISH follow-up)

**What:** Targeted smFISH panel for Tbr1, Rarb, Bcl11b, and Dcx in adult mouse DG.
**Target:** Determine whether Rarb+/Bcl11b+ cells are spatially segregated from Rarb− cells within the inner GCL.
**Expected output:** Spatial map of marker co-expression within [UBERON:0005381]; would characterise whether clusters 0514 and 0515 correspond to spatially distinguishable subpopulations.
**Resolves:** The biological basis of the 0514/0515 split; Rarb as a distinguishing marker for cluster 0515.

### 5. Electrophysiology / patch-seq (Gad1 signal)

**What:** Patch-seq or targeted smFISH for Gad1 alongside Tbr1 and Dcx in inner GCL cells.
**Target:** Determine whether Gad1 signal in clusters 0514/0515 reflects transient physiological GABAergic activity, doublets, or contamination.
**Expected output:** Clarification of GABAergic co-expression status; if transient physiology, consistent with published accounts of GABA depolarisation in immature granule neurons.
**Resolves:** Unresolved question about Gad1 nt_marker signal in both clusters.

---

## Open questions

1. What is the biological basis for the two-cluster split between [CS20230722_CLUS_0514] and [CS20230722_CLUS_0515] at the immature GN stage? Possibilities include: maturational sub-stage, sex composition, or circadian/activity-dependent transcriptional state.
2. Does Dcx mRNA appear in clusters 0514/0515 below the atlas marker ranking threshold? A targeted query on the full atlas feature matrix would resolve the DCX alignment.
3. Why does cluster 0514 show a Gad1 nt_marker signal (score 5.56)? Transient GABAergic signalling in immature granule neurons, doublet artefact, or contamination?
4. What distinguishes cluster 0515 from cluster 0514 biologically? Rarb (retinoic acid receptor beta, scoped in 0515) and Bcl11b/Cd24a/Fam163a MERFISH markers may mark a later maturational sub-stage or sex-biased transcriptional state.
5. Is the Gad1 nt_marker signal in cluster 0515 (score 3.67) the same transient GABAergic signal as in cluster 0514 (score 5.56), and does the lower score in cluster 0515 indicate a more advanced maturational state?

---

## Evidence base

| Edge | Evidence type | Supports | Source |
|---|---|---|---|
| → [CS20230722_CLUS_0514] | ATLAS_METADATA | SUPPORT | Atlas; CL:9900002 EXACT; Tbr1/Prox1/Emx2/Igfbpl1; DGdo,me HIP:0.98; Glut; no Calb1 |
| → [CS20230722_CLUS_0514] | LITERATURE (review) | SUPPORT | Micheli 2025 [5]: stage-5 definition DCX+/NeuN+/Calb1− |
| → [CS20230722_CLUS_0514] | LITERATURE (experimental) | SUPPORT | Hodge 2008 [8]: Tbr1 postmitotic specificity |
| → [CS20230722_CLUS_0514] | LITERATURE (experimental) | SUPPORT | Attardo 2009 [7]: Tis21 postmitotic re-expression |
| → [CS20230722_CLUS_0515] | ATLAS_METADATA | SUPPORT | Atlas; CL:9900002 EXACT; Tbr1/Prox1/Emx2/Igfbpl1; Rarb/Bcl11b/Cd24a/Fam163a; DGdo,me HIP:1.0; Glut (inherited) |
| → [CS20230722_CLUS_0515] | LITERATURE (review) | SUPPORT | Micheli 2025 [5]: stage-5 definition DCX+/NeuN+/Calb1− |
| → [CS20230722_CLUS_0515] | LITERATURE (experimental) | SUPPORT | Hodge 2008 [8]: Tbr1 postmitotic specificity |
| → [CS20230722_CLUS_0515] | LITERATURE (experimental) | SUPPORT | Attardo 2009 [7]: Tis21 postmitotic re-expression |

All atlas metadata evidence is from Allen Brain Cell Atlas CCN202307220 (atlas metadata, not literature). Literature items are individually cited above.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Velusamy 2017 | [28168008](https://pubmed.ncbi.nlm.nih.gov/28168008/) | Soma location — inner granule cell layer |
| [2] | Regalado-Santiago 2016 | [26880934](https://pubmed.ncbi.nlm.nih.gov/26880934/) | Soma location — inner granule cell layer |
| [3] | Stoll 2014 | [26056581](https://pubmed.ncbi.nlm.nih.gov/26056581/) | Neurotransmitter type — glutamatergic |
| [4] | Vangeneugden 2015 | [25954142](https://pubmed.ncbi.nlm.nih.gov/25954142/) | Neurotransmitter type — glutamatergic |
| [5] | Micheli 2025 | [40519263](https://pubmed.ncbi.nlm.nih.gov/40519263/) | Stage-5 definition: DCX+/NeuN+/Calbindin− (immature GN); stage-6 Calbindin+ (mature GN) |
| [6] | Stepień 2021 | [37082558](https://pubmed.ncbi.nlm.nih.gov/37082558/) | DCX and PSA-NCAM markers; NeuN immature neuron marker |
| [7] | Attardo 2009 | [19482889](https://pubmed.ncbi.nlm.nih.gov/19482889/) | Tis21 re-expression in postmitotic maturing adult DG neurons |
| [8] | Hodge 2008 | [18385329](https://pubmed.ncbi.nlm.nih.gov/18385329/) | Tbr1 onset marks postmitotic transition from neuroblast to immature granule neuron |
