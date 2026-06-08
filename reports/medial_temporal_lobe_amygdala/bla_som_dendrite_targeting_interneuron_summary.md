# Basolateral amygdala somatostatin-positive dendrite-targeting interneuron — CCN20230722 Mapping Report
*2026-06-04 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The basolateral amygdala (BLA) somatostatin-positive dendrite-targeting interneuron is a GABAergic interneuron of the basolateral amygdaloid complex characterised by co-expression of somatostatin (Sst) and calbindin (Calb1), and by a preferential axonal targeting of dendritic shafts and spines on principal cells rather than somata or axon initial segments. This class comprises an estimated 10–16% of all GABAergic neurons in the lateral and basal amygdala (LA/BA), placing it among the larger inhibitory populations in this structure. Mapping this type to the CCN20230722 atlas is important for connecting classical neuroanatomical literature with transcriptomic taxonomy and enabling downstream annotation-transfer experiments.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | [1] |
| NT type | GABAergic | [1], [2] |
| Defining markers | Calb1 | [1] |
| Neuropeptides | Sst | [1], [3] |
| Notes | Estimated 10–16% of GABAergic cells in LA/BA; distinct from somatostatin/nNOS-expressing GABAergic projection neurons | — |

<details>
<summary>### Details — source evidence for classical type properties</summary>

- **Soma location / NT type / Calb1 / Sst:** literature synthesis · mouse and rat BLA · [1]

  > The cell types in all of these amygdalar nuclei are similar, but they have been studied primarily in the basolateral amygdala. The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982(McDonald, , 1985(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003Millhouse and DeOlmos, 1983;Fuller et al., 1987;Carlsen and Heimer, 1988;McDonald and Augustine, 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;
  > — McDonald et al. 2012, Classical neuron classes across amygdala subdivisions · [1] <!-- quote_key: 11544073_94689603 -->

- **NT type:** review, species not specified · [2]

- **Sst neuropeptide:** neurochemical classification, mouse BLA · [3]

  > One commonly adopted method segregates IN subpopulations based on neurochemical content, including expression of Ca 2+ - binding proteins [e.g., parvalbumin (PV); (McDonald et al., 2001)(McDonald et al., 2001)] and neuropeptides such as somatostatin (SOM), neuropeptide Y (NPY), and cholecystokinin (CCK; Mascagni and McDonald, 2003;(Kepecs et al., 2014)
  > — Rovira-Esteban et al. 2019, Basolateral amygdala and corticobasal cell types · [3] <!-- quote_key: 204835327_bf931431 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_0765 is the primary mapping at LOW confidence. The candidate is tied with CLUS_0774 in discovery score; a second parallel edge is required before confidence can be elevated.

### Mapping candidates table

**4a. Candidate overview table**

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | CS20230722_CLUS_0765 | — | — | 🔴 LOW | Calb1 CONSISTENT · Sst CONSISTENT | skos:broadMatch |

*1 edge assessed; relationship: skos:broadMatch (tied score — see caveats).*

Note: `n_cells` is null for this edge — the taxonomy DB pre-dates the n_cells column (PR #21). Rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` to populate.

**4b. Property alignment — CS20230722_CLUS_0765**

**Table 1 — Property comparison**

| Property | Classical | Best cluster | Alignment |
|---|---|---|---|
| Soma location | Basolateral amygdala [UBERON:0002887] | MBA:295 BLA: 43 cells, cell_ratio 0.289 (Yao 2024); 65 cells, cell_ratio 0.214 (Zhuang 2023). Also BMA/BLA-ant/BLA-post; cortical subplate carries majority of cluster cells. | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Calb1 expression | Calb1 — defining marker | Calb1 precomputed mean_expression 9.57 (cohort 96.5th pct; tier 2; applied_score 2.0) | CONSISTENT |
| Sst neuropeptide | Sst — neuropeptide | Sst NEUROPEPTIDE (expression_score 11.9); precomputed mean 11.92 (cohort 96.7th pct; tier 2). Cluster named "0765 Sst Gaba_2". | CONSISTENT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Vereczki 2021 EM dendrite-targeting | Literature | SUPPORT | EM confirms SST+ terminals preferentially contact dendritic shafts in mouse LA/BA | [4] |
| McDonald 2012 BLA interneuron classes | Literature | SUPPORT | SST+/Calb1+ interneurons estimated 10–16% of GABAergic cells; distinct class from PV and CCK basket cells | [1] |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### CS20230722_CLUS_0765 · 🔴 LOW

**Supporting evidence**

- **Calb1 CONSISTENT:** The precomputed mean expression of Calb1 for CS20230722_CLUS_0765 is 9.57 (96.5th cohort percentile among the 5-member GABAergic/MBA:295 survival cohort; tier 2; applied_score 2.0 via EXPRESSION source). This places the cluster among the highest Calb1 expressors in the regional GABAergic cohort and is consistent with the classical SOM+/CB+ subpopulation described by McDonald [1].

- **Sst CONSISTENT:** Sst precomputed mean is 11.92 (96.7th cohort percentile; tier 2; applied_score 2.0 via EXPRESSION source). The cluster is named "0765 Sst Gaba_2" in the CCN20230722 taxonomy, and Sst carries a NEUROPEPTIDE annotation (expression_score 11.9). Both are fully consistent with the classical neuropeptide identity [1], [3].

- **Soma location CONSISTENT:** MERFISH spatial registration places CS20230722_CLUS_0765 cells in MBA:295 (BLA) with cell_ratio 0.289 in Yao 2024 and 0.214 in Zhuang 2023. Although the cortical subplate carries the majority of cluster cells and additional cells fall in BMA/BLA-ant/BLA-post, the BLA representation at these ratios is consistent with the classical type's soma location [1].

- **NT type CONSISTENT:** The atlas annotates CS20230722_CLUS_0765 as GABA, consistent with the classical GABAergic assignment [1], [2].

- **EM morphology — dendrite targeting:** Vereczki et al. 2021 used correlated electron microscopy in mouse LA/BA to confirm that SST+ inhibitory axon terminals preferentially target dendritic shafts, providing the primary morphological anchor for the dendrite-targeting classification [4].

  > SST+ inhibitory cells target predominantly the dendritic shaft and to a lesser extent, the spines of principal cells
  > — Vereczki et al. 2021, Discussion · [4] <!-- quote_key: 232283078_bd1f3975 -->

- **Classical interneuron class description:**

  > The cell types in all of these amygdalar nuclei are similar, but they have been studied primarily in the basolateral amygdala. The principal neurons in the CBL are pyramidal-like projection neurons with spiny dendrites that utilize glutamate as an excitatory neurotransmitter, whereas most non-pyramidal neurons in the CBL are spine-sparse interneurons that utilize GABA as an inhibitory neurotransmitter (McDonald, 1982(McDonald, , 1985(McDonald, , 1992a(McDonald, ,b, 1996(McDonald, , 2003Millhouse and DeOlmos, 1983;Fuller et al., 1987;Carlsen and Heimer, 1988;McDonald and Augustine, 1993). Dual-labeling immunohistochemical studies in the basolateral amygdala suggest that the CBL contains at least four distinct subpopulations of GABAergic non-pyramidal neurons that can be distinguished on the basis of their content of calcium-binding proteins and peptides. These subpopulations are: (1) PV+/CB+ neurons, (2) SOM+/CB+ neurons, (3) large multipolar cholecystokinin+ neurons that are often CB+, and (4) small bipolar and bitufted interneurons that exhibit extensive colocalization of calretinin, cholecystokinin, and vasoactive intestinal peptide (Kemppainen and Pitkänen, 2000;McDonald and Betette, 2001;Mascagni, 2001, 2002;
  > — McDonald et al. 2012, Classical neuron classes across amygdala subdivisions · [1] <!-- quote_key: 11544073_94689603 -->

**Marker evidence provenance**

- **Calb1 (defining marker):** Evidence is protein-level (immunohistochemistry, dual-labeling IHC studies) from McDonald [1]. The original studies were performed on BLA populations identified as SOM+/CB+ interneurons; cell-type identity was based on neurochemical co-labeling rather than morphological reconstruction of individual cells. Atlas-side expression (mean 9.57; cohort 96.5th pct) is robust and corroborates the marker assignment. No discrepancy between annotation and precomputed expression.

- **Sst (neuropeptide):** Evidence is protein-level (immunohistochemistry) from McDonald [1] and additionally supported by Rovira-Esteban et al. 2019 [3] via neurochemical classification. The cluster carries a NEUROPEPTIDE annotation and high precomputed Sst expression (mean 11.92), so there is no annotation/expression discrepancy. Both literature and atlas metadata are concordant.

  *(note: The defining marker Calb1 as listed refers to calbindin-D28k/CB; in the McDonald [1] text this population is described as SOM+/CB+. The atlas precomputed Calb1 value at 9.57 is the highest in the 5-member regional cohort, supporting specificity. The Calb1 evidence is primarily protein-level; transcript-level cross-validation from ISH or scRNA-seq in BLA would strengthen this.)*

**Concerns**

- **TIED_CANDIDATES:** CS20230722_CLUS_0765 and CS20230722_CLUS_0774 (Sst Gaba_3, parent SUPT_0216) both achieved a discovery score of 5 in the 5-member GABAergic/MBA:295 survival cohort. The cohort was exhausted (score 5, next_best_score 5, rank_in_cohort 1 in a cohort of size 5). A parallel edge to CLUS_0774 has not yet been constructed; until that edge is assessed, the single-edge evidence is insufficient to select CLUS_0765 as the unique match. This is the primary reason for LOW rather than MODERATE confidence.

- **MORPHOLOGY_NOT_RESOLVABLE:** Dendritic-shaft targeting, the key morphological property distinguishing this type from other BLA SST+ interneurons, cannot be resolved from transcriptomics alone. The atlas provides no morphological annotations at cluster level. Patch-seq or correlated EM with transcriptomic readout is required to link the morphological classification definitively to an atlas cluster.

- **AT_ABSENT:** No annotation-transfer evidence is available for this edge. Confidence is accordingly capped at LOW per the rubric (single evidence type, indirect convergence).

- **Region fraction in boundary band:** `region_fraction` = 0.289 for Yao 2024 (0.214 for Zhuang 2023). Both values are below 0.30, placing them at the lower edge of the boundary band. The cortical subplate carries the majority of this cluster's cells, which warrants noting in the context of a type defined as being in the BLA proper; however, BLA and cortical subplate are developmentally related (both are part of the pallial amygdala), so this may reflect registration boundary overlap rather than a true mismatch.

**What would upgrade confidence**

- **Construct a parallel edge to CLUS_0774** (same methodology as the present edge): resolves the TIED_CANDIDATES caveat. If one cluster is more strongly enriched in BLA-proper cells or shows better co-expression of Calb1 and Sst at single-cell resolution, confidence on the winning edge could reach MODERATE.
- **Annotation transfer (AnnotationTransferEvidence, target: F1 ≥ 0.60 at CLUSTER level):** Run MapMyCells or a patch-seq bridging analysis using a Sst+ BLA interneuron reference dataset. Would differentiate CLUS_0765 vs CLUS_0774 and provide the experimental anchor missing from the current evidence base.
- **smFISH:** Targeted smFISH with Sst + Calb1 + Cort + Ano2 in mouse BLA with dendritic synapse localisation would simultaneously confirm the dendrite-targeting morphology and assess co-expression of additional markers high in CLUS_0765 (NPY, Pnoc, Cort, Ano2), potentially resolving the CLUS_0765 vs CLUS_0774 question. Expected output: direct LiteratureEvidence or a new MarkerAnalysisEvidence item.
- **Patch-seq in BLA SST+ interneurons:** Would link morpho-electrophysiological identity (dendrite-targeting class, firing pattern) to a transcriptomic cluster with single-cell resolution. Expected output: AnnotationTransferEvidence or BulkCorrelationEvidence anchored to a characterised reference.
- **Targeted literature search for Calb1 specificity in BLA SST+ interneurons:** Current Calb1 evidence is protein-level IHC from pooled SOM+/CB+ populations without individual cell reconstruction. A cite-traverse for "calbindin somatostatin basolateral amygdala interneuron" may identify primary studies that confirmed the co-expression with morphological verification, strengthening the marker evidence chain.

---

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The classical node `bla_som_dendrite_targeting_interneuron` is defined under `CLASSICAL` definition basis. The type is a GABAergic non-pyramidal interneuron of the basolateral amygdaloid complex characterised by co-expression of Calb1 (calbindin-D28k) as a defining marker [1] and Sst (somatostatin) as a neuropeptide [1], [3]. Soma location is the basolateral amygdala [UBERON:0002887] [1]. The type is estimated to comprise 10–16% of GABAergic cells in LA/BA and is distinct from somatostatin/nNOS-expressing GABAergic projection neurons. NT type is GABAergic [1], [2].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Atlas data sources.**

| Atlas | Taxonomy ID | Notes |
|---|---|---|
| CCN20230722 | CCN20230722 | Candidate query at ranks 0 and 1 |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_bla_som_dendrite_targeting_interneuron_to_cs20230722_clus_0765 | LITERATURE; LITERATURE | SUPPORT; SUPPORT | [4], [1] |

*Generated by evidencell `8222564` at 2026-06-04T10:52:47+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Basolateral amygdala somatostatin-positive dendrite-targeting interneuron → CS20230722_CLUS_0765 at LOW confidence. Key support: LiteratureEvidence (EM dendrite-targeting morphology [4]; BLA SST+/Calb1+ class characterisation [1]) and CONSISTENT precomputed expression of both Calb1 (mean 9.57; cohort 96.5th pct) and Sst (mean 11.92; cohort 96.7th pct). Key caveats: TIED_CANDIDATES (CLUS_0765 and CLUS_0774 both score 5/5 in the 5-member regional GABAergic cohort; no tie-breaking evidence available); MORPHOLOGY_NOT_RESOLVABLE (dendrite-targeting cannot be confirmed from transcriptomics alone); AT_ABSENT (no annotation-transfer evidence).

No Cell Ontology term currently assigned. This type represents a candidate for CL contribution as a BLA-specific somatostatin/calbindin dendrite-targeting interneuron distinct from hippocampal or cortical Sst+ counterparts.

### Proposed experiments and follow-ups

**1. Construct parallel edge to CLUS_0774**
- **What:** Property comparison mapping (same pipeline as current edge)
- **Target:** Determine which of CLUS_0765 / CLUS_0774 better matches classical BLA SST+ dendrite-targeting interneuron
- **Expected output:** MappingEdge YAML for CLUS_0774; resolution of TIED_CANDIDATES caveat
- **Resolves:** Q1 (Do CLUS_0765 and CLUS_0774 represent genuinely distinct SST subtypes in BLA?)

**2. Annotation transfer**
- **What:** MapMyCells or patch-seq AT against CCN20230722 using a Sst+ BLA interneuron scRNA-seq reference dataset
- **Target:** F1 ≥ 0.60 at CLUSTER level for CLUS_0765 or CLUS_0774
- **Expected output:** AnnotationTransferEvidence items on both edges; would upgrade LOW → MODERATE if F1 threshold met and TIED_CANDIDATES resolved
- **Resolves:** AT_ABSENT caveat; provides experimental anchor for predicate selection

**3. smFISH panel in mouse BLA**
- **What:** Multiplexed smFISH (Sst, Calb1, Cort, Ano2, NPY/Npy) with dendritic synapse localisation markers in mouse BLA
- **Target:** Quantify co-expression rates and axon-terminal targeting patterns at single-cell resolution
- **Expected output:** LiteratureEvidence or MarkerAnalysisEvidence; resolves MORPHOLOGY_NOT_RESOLVABLE; may also resolve CLUS_0765 vs CLUS_0774 by differential co-expression of Cort/Ano2/NPY
- **Resolves:** MORPHOLOGY_NOT_RESOLVABLE caveat; Q2 (co-expression of NPY, PNOC, Cort, Ano2 in dendrite-targeting class)

**4. Patch-seq in BLA SST+ interneurons**
- **What:** Patch-seq combining electrophysiology, morphological reconstruction, and single-cell transcriptomics in mouse BLA SST+ interneurons
- **Target:** Assign patch-seq profiles to CCN20230722 clusters at leaf level
- **Expected output:** AnnotationTransferEvidence or BulkCorrelationEvidence linking morpho-electrophysiological dendrite-targeting class to a specific cluster
- **Resolves:** MORPHOLOGY_NOT_RESOLVABLE caveat; Q1 (CLUS_0765 vs CLUS_0774)

**5. Targeted literature search — Calb1 specificity**
- **What:** Cite-traverse for "calbindin somatostatin basolateral amygdala interneuron" to identify primary studies with morphological verification of co-expression
- **Target:** At least one primary study confirming Calb1 in morphology-identified BLA SST+ dendrite-targeting cells
- **Expected output:** LiteratureEvidence item strengthening Calb1 as a verified defining marker
- **Resolves:** Weak marker evidence provenance for Calb1 (currently protein-level pooled IHC without individual cell reconstruction)

### Open questions

1. Do CS20230722_CLUS_0765 and CLUS_0774 (Sst Gaba_3, parent SUPT_0216) represent genuinely distinct SST subtypes in BLA, or are they transcriptomic sub-clusters of a single classical type? *(applies to edge_bla_som_dendrite_targeting_interneuron_to_cs20230722_clus_0765)*
2. Does the BLA SST+ dendrite-targeting class co-express NPY, PNOC, Cort, and Ano2 — all reported as high in CLUS_0765 — and can these markers serve as distinguishing features between CLUS_0765 and CLUS_0774? *(applies to edge_bla_som_dendrite_targeting_interneuron_to_cs20230722_clus_0765)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | McDonald et al. 2012 · PMID:22837739 | [22837739](https://pubmed.ncbi.nlm.nih.gov/22837739/) | Soma location, NT type, Calb1 defining marker, Sst neuropeptide, BLA interneuron class characterisation |
| [2] | Perumal & Sah 2021 · PMID:33994955 | [33994955](https://pubmed.ncbi.nlm.nih.gov/33994955/) | Neurotransmitter type |
| [3] | Rovira-Esteban et al. 2019 · PMID:31636080 | [31636080](https://pubmed.ncbi.nlm.nih.gov/31636080/) | Sst neuropeptide |
| [4] | Vereczki et al. 2021 · PMID:33837051 | [33837051](https://pubmed.ncbi.nlm.nih.gov/33837051/) | EM confirmation of SST+ axon terminals targeting dendritic shafts in mouse LA/BA |

---

<!-- verdict-block-start: edge_bla_som_dendrite_targeting_interneuron_to_cs20230722_clus_0765 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.32
  rationale: >
    `marker_Calb1` CONSISTENT (precomputed mean 9.57; cohort 96.5th pct) and
    `neuropeptide_Sst` CONSISTENT (precomputed mean 11.92; cohort 96.7th pct) in
    CS20230722_CLUS_0765; LiteratureEvidence (LITERATURE evidence items) anchor the SST+/Calb1+ identity. However, CLUS_0774 (Sst Gaba_3)
    scores equally in the 5-member GABAergic MBA:295 cohort (score 5,
    next_best_score 5), no AT evidence is available, and
    dendrite-targeting axonal pattern is not resolvable from transcriptomics.
    2 of 2 markers CONSISTENT; broadMatch reflects unresolved 1:n ambiguity
    with CLUS_0774.
  reconciliation_note: >
    TIED_CANDIDATES: CLUS_0765 and CLUS_0774 both score 5 in the 5-member
    GABAergic/MBA:295 cohort. A parallel edge to CLUS_0774 is required before
    a closeMatch or narrowMatch predicate can be justified. broadMatch is
    appropriate given current evidence.
  unresolved_questions:
    - "Do CLUS_0765 and CLUS_0774 represent genuinely distinct SST subtypes in BLA? Requires parallel edge construction and patch-seq."
    - "Does the BLA SST+ dendrite-targeting class co-express NPY, PNOC, Cort, and Ano2 (all high in CLUS_0765)? Targeted smFISH or patch-seq needed."
```
<!-- verdict-block-end -->
