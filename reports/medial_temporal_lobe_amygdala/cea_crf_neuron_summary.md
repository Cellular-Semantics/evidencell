# Central amygdala corticotropin-releasing factor (CRF) neuron — CCN20230722 Mapping Report
*2026-06-11 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

Corticotropin-releasing factor (CRF) neurons of the central amygdala (CeA) are GABAergic inhibitory neurons that express the neuropeptide Crh (CRF/CRH) and contribute to CeA output circuits mediating fear, stress, and autonomic responses. Alongside the PKC-δ (Prkcd) and somatostatin (Sst/SOM) populations, CRF neurons constitute one of three classical neuropeptide-defined CeA cell classes identified in rodent studies and confirmed in other species [1]. Because the CeA is the principal output nucleus of the amygdaloid complex, establishing the correspondence between CRF neurons and single-cell transcriptomic atlas clusters is essential for translating circuit-level findings to human disease. This report documents a mapping to SUPT_0393 ("CEA-BST Rai14 Pdyn Crh Gaba_2"), which carries Crh as an explicit defining feature and resides in the correct CEA-BST developmental lineage.

### Classical type description

| Property | Value | References |
|---|---|---|
| Cell type name | Central amygdala corticotropin-releasing factor (CRF) neuron | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | [1] |
| Soma location | central amygdala [UBERON:0002883] | [1] |
| Defining markers | None recorded | — |
| Negative markers | None recorded | — |
| Neuropeptides | Crh | [1] |
| Morphology | Not recorded | — |
| Electrophysiology | Not recorded | — |
| Notes | Often partially overlaps with other neuropeptide-defined CeA populations; not exhaustively characterized here. | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Neurotransmitter (GABAergic):** asta_report synthesis · amygdala literature synthesis · [1]

- **Soma location (central amygdala [UBERON:0002883]):** asta_report synthesis · CeA neuropeptide neuron classification · [1]
  > .It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice.
  > — Yeh et al. 2024, Central amygdala cell types · [1] <!-- quote_key: 267685584_daaf5612 -->

- **Neuropeptide Crh:** asta_report synthesis · amygdala literature synthesis · [1]
  > .It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice.
  > — Yeh et al. 2024, Central amygdala cell types · [1] <!-- quote_key: 267685584_daaf5612 -->

</details>

### Cell Ontology mapping

No Cell Ontology term currently covers this type — candidate for a new CL term.

---

## Results

One candidate atlas supertype was assessed; CS20230722_SUPT_0393 ("CEA-BST Rai14 Pdyn Crh Gaba_2") is the primary mapping at LOW confidence, reflecting strong Crh neuropeptide alignment and correct CEA-BST lineage, but confounded by AGAINST annotation-transfer evidence: GABA-13-Adora2a-Crh (the Hochgerner 2023 source type) maps to STR D2 Gaba_5 (SUPT_0278, F1=0.800 at supertype level) rather than SUPT_0393, suggesting that Adora2a co-expression drives the AT signal away from the expected CeA target.

### Mapping candidates table

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|---|---|---|
| 1 | CS20230722_SUPT_0393 (CEA-BST Rai14 Pdyn Crh Gaba_2) | 278 | 🔴 LOW | Crh CONSISTENT · NT CONSISTENT | broadMatch; AT AGAINST |

*1 edge assessed; relationship type: skos:broadMatch.*

### Property alignment table — CS20230722_SUPT_0393

**Table 1 — Property comparison**

| Property | Classical | Supertype (SUPT_0393) | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | central amygdala [UBERON:0002883] | MBA:536 CeA present; SUPT_0393 "CEA-BST Rai14 Pdyn Crh Gaba_2" region_fraction 0.034 (rank-1 cohort); CEA-BST lineage confirms amygdalar context | not assessed | CONSISTENT |
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Crh (neuropeptide) | Crh — defining neuropeptide | Crh is an explicit defining marker in the supertype label "CEA-BST Rai14 Pdyn Crh Gaba_2"; precomputed mean_expression 7.96 (CeA GABAergic rank-1 cohort 99.4th pct; tier 2; highest Crh expression among all candidates) | not assessed | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yeh 2024 CeA neuropeptide classification | Literature | SUPPORT | CRF identified as CeA neuropeptide marker alongside PKC-δ and SOM | [1] |
| Atlas metadata — SUPT_0393 Crh/Pdyn expression | Atlas metadata | SUPPORT | Crh mean 7.96; 99.4th pct CeA GABAergic rank-1 cohort; CEA-BST lineage | atlas-internal |
| Hochgerner 2023 AT — GABA-13-Adora2a-Crh | Annotation transfer | AGAINST | GABA-13 maps to SUPT_0278 STR D2 (F1=0.800 at supertype), not SUPT_0393; Adora2a co-expression drives STR D2 signal | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### CS20230722_SUPT_0393 (CEA-BST Rai14 Pdyn Crh Gaba_2) · 🔴 LOW

**Supporting evidence:**

- **Crh neuropeptide alignment (CONSISTENT):** SUPT_0393 carries Crh as an explicit named feature in its label "CEA-BST Rai14 Pdyn Crh Gaba_2". Precomputed mean_expression for Crh = 7.96, placing it at the 99.4th percentile of the CeA GABAergic rank-1 survival cohort (n=5; filtered to MBA:536 + GABAergic). This is the highest Crh expression of any candidate in the cohort. The Stage A discovery score was 3 (rank 5 of 5 in the 5-member cohort; the low cohort rank reflects region_fraction 0.034 which is modest), driven entirely by Crh (`applied_score: 2.0` from cohort-pct 0.994 of 5). *(Note: the cohort has only 5 members; percentile values reflect intra-cohort rank only.)*

- **CEA-BST lineage (CONSISTENT):** The "CEA-BST" lineage label correctly places this supertype in the central extended amygdala developmental context. Co-expression of Pdyn (dynorphin) is biologically consistent with known co-expression of dynorphin in CeA lateral subdivision CRF neurons. *(note: Pdyn co-expression with Crh in CeA is a neuroanatomical inference; the current facts file does not carry a primary citation directly confirming co-expression in confirmed-identity CRF+ CeA neurons.)*

- **NT type (CONSISTENT):** SUPT_0393 is designated GABA, consistent with the classical GABAergic identity of CeA CRF neurons [1].

- **Literature support:** Yeh et al. 2024 identifies CRF as one of three canonical CeA neuropeptide populations (alongside PKC-δ/Prkcd and SOM/Sst), confirmed in human amygdala. This directly supports Crh as the defining neuropeptide for this classical type.
  > .It revealed distinct PKC-δ, SOM, and CRF neuronal populations similar to those in mice.
  > — Yeh et al. 2024, Central amygdala cell types · [1] <!-- quote_key: 267685584_daaf5612 -->

**Marker evidence provenance:**

- **Crh (neuropeptide):** Evidence is transcript-level via asta_report synthesis from Yeh et al. 2024 [1]. The study synthesises prior literature affirming CRF as a canonical CeA marker in both mouse and human, rather than providing primary single-cell characterisation of morphologically or electrophysiologically confirmed CRF+ CeA neurons. No IHC or morphological confirmation of the specific CRF+ population is recorded in the current facts file. The atlas-side Crh expression value (mean 7.96; tier 2 = reliably expressed) at SUPT_0393 provides strong cohort-relative specificity (99.4th percentile; highest of any candidate). *(note: absence of a primary morphology- or electrophysiology-confirmed study means the classical node rests on literature synthesis rather than direct cell-type confirmation; a targeted literature search for "Crh CeA single-cell scRNA-seq" may identify stronger primary evidence.)*

**Concerns:**

- **AT AGAINST — Adora2a co-expression in GABA-13:** The Hochgerner 2023 source type GABA-13-Adora2a-Crh maps to SUPT_0278 "STR D2 Gaba_5" (F1=0.800 at supertype level) rather than SUPT_0393. Adora2a is a D2 dopamine receptor-associated adenosine receptor expressed in striatal MSN-like cells; its co-expression in GABA-13 likely drives the STR D2 mapping. This may indicate GABA-13 represents a D2-lineage subset of CeA Crh-expressing neurons rather than the canonical Crh-only CeA CRF population. An Adora2a-negative Crh+ population matching SUPT_0393 may exist but is not captured by the available Hochgerner source types.

- **TAXONOMY_LEVEL_MISMATCH:** SUPT_0393 is assessed only at supertype level (rank 1). CeA region_fraction = 0.034 at supertype level — the "CEA-BST" label encompasses both CeA and BST; WMBv1 spatial data may primarily sample BST for this supertype. Individual clusters within SUPT_0393 and their CeA-specific fractions are unassessed.

- **DISTRIBUTED_ACROSS_CLUSTERS:** Mapping is at supertype level; CeM vs CeL CRF subtypes may correspond to different clusters within SUPT_0393, but this is unassessed.

- **Single neuropeptide marker:** No defining molecular markers beyond Crh are recorded on the classical node. The mapping rests entirely on Crh expression correspondence.

**What would upgrade confidence:**

1. **MapMyCells with a Crh+/Adora2a− source dataset (AnnotationTransferEvidence):** The key issue is that GABA-13 co-expresses Adora2a, which is not expected for the canonical CeA CRF population. A source type enriched for Adora2a-negative Crh+ CeA cells (e.g. from CRH-Cre+ intersectional strategy, or a CeA-focused atlas with richer cell-type resolution) would allow a cleaner AT run against WMBv1. Target: F1 ≥ 0.60 at supertype level for SUPT_0393; this would resolve the AT AGAINST concern (Q1).
2. **Cre-dependent scRNA-seq of CRH-Cre+ CeA neurons mapped to WMBv1:** Cluster-level assignment of the majority (>70%) of CRH-Cre+ cells to SUPT_0393 or its child clusters would confirm identity and resolve 1:n cardinality. Expected output: AnnotationTransferEvidence resolving both Q1 and Q2.
3. **Dual ISH for Crh + Pdyn in mouse CeA:** Fluorescent ISH confirming Pdyn/Crh co-expression would provide direct molecular support for the link to the SUPT_0393 supertype label "CEA-BST Rai14 Pdyn Crh Gaba_2". Expected output: LiteratureEvidence.
4. **Targeted literature search:** A cite-traverse for "CRF CeA single-cell transcriptomics" or "Crh amygdala scRNA-seq" may identify published datasets directly assigning CRF+ CeA cells to WMBv1 clusters, strengthening the currently single-reference evidence base.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The central amygdala corticotropin-releasing factor (CRF) neuron is defined on a CLASSICAL basis: GABAergic neurotransmitter type [1], soma location in the central amygdala [UBERON:0002883] [1], and Crh as the sole neuropeptide marker [1]. No defining molecular markers beyond Crh and no morphological or electrophysiological class are recorded. The definition derives from literature synthesis (asta_report method) via Yeh et al. 2024.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) and rank 1 (supertype) using metadata-based scoring (region match MBA:536, NT type GABAergic, neuropeptide Crh). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the supertype (supertype.yaml in the taxonomy reference store).

**Annotation transfer.** Annotation transfer was performed using MapMyCells (cell_type_mapper v1.7.1) against WMBv1 (CCN20230722). Source dataset: Hochgerner et al. 2023 (ArrayExpress:E-MTAB-12096; naive neuronal cells only; n=7,777 after filtering). Source type assessed for this edge: GABA-13-Adora2a-Crh (n=16 cells). Result: AGAINST — maps to SUPT_0278 STR D2 Gaba_5 (F1=0.800 at supertype), not SUPT_0393.

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 (GABA-13-Adora2a-Crh) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, 100 bootstrap iterations) |
| Bootstrap threshold | 0.7 |
| n cells | 55,514 (filtered to 7,777) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Source labels are transcriptomically-defined types; GABA-13 co-expresses Adora2a (D2 MSN marker), which may not represent the canonical Crh-only CeA CRF population. Fear-conditioned cells excluded to avoid transcriptional-state confounds. Gene symbols matched against WMBv1 marker genes. |

**Atlas data sources.**
- Atlas: CCN20230722 (WMBv1); taxonomy_id: CCN20230722.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_crf_neuron_to_cs20230722_supt_0393 | LITERATURE; ATLAS_METADATA; ANNOTATION_TRANSFER | SUPPORT; SUPPORT; AGAINST | [1]; atlas-internal; — |

*Generated by evidencell `8d79cdb` at 2026-06-11T09:44:19+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Central amygdala corticotropin-releasing factor (CRF) neuron → CS20230722_SUPT_0393 (CEA-BST Rai14 Pdyn Crh Gaba_2) at LOW confidence. Key support: Crh precomputed mean expression 7.96 at the 99.4th percentile of the CeA GABAergic rank-1 cohort (CONSISTENT) and NT type CONSISTENT (GABAergic). Key caveats: ANNOTATION_TRANSFER AGAINST — GABA-13-Adora2a-Crh maps to STR D2 Gaba_5 (SUPT_0278, F1=0.800 at supertype level), not SUPT_0393; Adora2a co-expression in GABA-13 likely drives the STR D2 signal and the canonical Crh-only CeA CRF population is not captured by the available Hochgerner source types.

No Cell Ontology term currently assigned. Candidate for CL contribution (no existing CL term covers CRF-defined CeA neurons specifically).

### Proposed experiments and follow-ups

Annotation transfer has been performed once (Hochgerner 2023, `at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1`), but returned AGAINST due to Adora2a co-expression in the available source type GABA-13-Adora2a-Crh. This resolves the question of whether this run supports the mapping (it does not), but leaves open whether the canonical Adora2a-negative Crh+ population would map correctly. Refined experiments are therefore still needed.

**1. MapMyCells with an Adora2a-negative CRH+ source dataset**
- **What:** Apply MapMyCells (cell_type_mapper v1.7.1) against WMBv1 (CCN20230722) using a source population enriched for Adora2a-negative Crh+ CeA neurons — e.g. from CRH-Cre intersectional profiling, or from a CeA-resolved dataset with sufficient Crh+ cell coverage.
- **Target:** F1 ≥ 0.60 at supertype level for CS20230722_SUPT_0393.
- **Expected output:** AnnotationTransferEvidence on edge_cea_crf_neuron_to_cs20230722_supt_0393.
- **Resolves:** AT AGAINST concern (Q1); discriminates canonical CRF population from the Adora2a co-expressing subset.

**2. Cre-dependent scRNA-seq of CRH-Cre+ CeA neurons**
- **What:** scRNA-seq of CRH-Cre+ CeA neurons with WMBv1 cluster assignment via MapMyCells at cluster level (rank 0).
- **Target:** Majority (>70%) of CRH-Cre+ cells assigned to SUPT_0393 or its child clusters.
- **Expected output:** AnnotationTransferEvidence; resolves 1:n cardinality.
- **Resolves:** Q1 (distinct class vs. Adora2a-driven subset) and Q2 (CeM vs. CeL CRF neuron resolution); DISTRIBUTED_ACROSS_CLUSTERS caveat.

**3. Dual ISH for Crh + Pdyn in mouse CeA**
- **What:** Fluorescent ISH for Crh and Pdyn co-expression in mouse CeA sections.
- **Target:** Confirm co-expression expected from SUPT_0393 label "CEA-BST Rai14 Pdyn Crh Gaba_2".
- **Expected output:** LiteratureEvidence supporting the Pdyn/Crh co-expression link.
- **Resolves:** Molecular link between classical Crh+ CeA neurons and the Pdyn co-expressing SUPT_0393 supertype.

**4. Targeted literature search**
- **What:** Cite-traverse for "CRF CeA single-cell transcriptomics" or "Crh amygdala scRNA-seq" to identify published datasets assigning CRF+ CeA cells to WMBv1 clusters.
- **Target:** At least one primary study with cell-type-confirmed CRF+ CeA neurons and transcriptomic profiling.
- **Expected output:** LiteratureEvidence entry with primary citation on the classical node.
- **Resolves:** Weak evidence provenance for Crh (currently rests on a single review-level reference).

### Open questions

1. Does the canonical (Adora2a-negative) CeA CRF population correspond to SUPT_0393 or a sibling CEA-BST supertype? The AT evidence shows that the Adora2a-Crh co-expressing GABA-13 type maps to STR D2, not CEA-BST. *(On: edge_cea_crf_neuron_to_cs20230722_supt_0393.)*

2. Which WMBv1 cluster(s) within SUPT_0393 correspond to CeM CRF projection neurons vs CeL CRF interneurons? The CeA subdivision distinction is not resolved at supertype level. *(On: edge_cea_crf_neuron_to_cs20230722_supt_0393.)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Yeh et al. 2024 | [PMID:38419794](https://pubmed.ncbi.nlm.nih.gov/38419794/) | NT type, soma location, neuropeptide Crh; CRF identified as canonical CeA neuropeptide population alongside PKC-δ and SOM |

---

<!-- verdict-block-start: edge_cea_crf_neuron_to_cs20230722_supt_0393 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.2
  rationale: >
    skos:broadMatch to CS20230722_SUPT_0393 "CEA-BST Rai14 Pdyn Crh Gaba_2":
    neuropeptide_Crh CONSISTENT (mean_expression 7.96; 99.4th pct of CeA GABAergic
    rank-1 cohort of 5 — highest Crh of any candidate; applied_score 2.0 from
    cohort-pct 0.994). NT type (GABA) and soma location (MBA:536, region_fraction
    0.034, CEA-BST lineage) are both CONSISTENT. However, ANNOTATION_TRANSFER is
    AGAINST: GABA-13-Adora2a-Crh (source_cluster_label in
    at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1) maps to SUPT_0278 STR D2
    Gaba_5, not SUPT_0393. Adora2a
    co-expression in GABA-13 likely drives the STR D2 signal; the canonical
    Adora2a-negative Crh+ CeA population is not captured by the available Hochgerner
    source types. No defining markers beyond Crh are recorded; mapping assessed at
    supertype level only. LOW confidence: single neuropeptide marker alignment with
    AGAINST AT evidence from a confounded source type.
  unresolved_questions:
    - Does the canonical (Adora2a-negative) CeA CRF population correspond to SUPT_0393 or a sibling CEA-BST supertype?
    - Which WMBv1 cluster(s) within SUPT_0393 correspond to CeM CRF projection neurons vs CeL CRF interneurons?
```
<!-- verdict-block-end -->
