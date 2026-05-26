# Entorhinal cortex layer III PCP4-positive pyramidal cell — WMBv1 (CCN20230722) Mapping Report
*2026-05-19 · Source: `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`*

## Introduction

Entorhinal cortex layer III principal neurons express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum via the temporoammonic (direct) pathway [1], forming a key hippocampal input that bypasses the trisynaptic circuit. This EC layer III → CA1/subiculum projection is thought to carry contextual and sensory information directly to the output stage of the hippocampus and plays an important role in memory consolidation. PCP4 is shared with CA2 pyramidal cells [2] and therefore identifies but does not uniquely discriminate EC layer III pyramidal cells from CA2 populations at the molecular level. The WMBv1 annotation transfer from Yao 2021 SSv4 provides strong evidence for the primary mapping to supertype 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] (F1=0.937).

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Entorhinal cortex [UBERON:0002728] layer III | |
| NT | Glutamatergic | [1] |
| Defining markers | Pcp4 (PCP4; shared with CA2 pyramidal cells) | [2][1] |
| Negative markers | — | |
| Neuropeptides | — | |
| CL term | pyramidal neuron [CL:0000598] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **EC layer III PCP4+ neurons project to CA1 and subiculum** [1]
  > Principal neurons in EC layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum
  > — Unknown 2021 · [1] <!-- quote_key: 244909998_bdbb7689 -->

  > Principal neurons in entorhinal cortex layer III express Purkinje cell protein 4 (PCP4) and project to CA1 and the subiculum (Ohara et al., 2021).
  > — Unknown 2021 · [1] <!-- quote_key: 244909998_c43772d2 -->

- **PCP4 as CA2 marker — cross-regional expression noted** [2]
  > Here we report identification of the CA2 region in the mouse by immunostaining with a Purkinje cell protein 4 (PCP4) antibody, which effectively delineates CA3/CA2 and CA2/CA1 borders and agrees well with previous cytoarchitectural definitions of CA2
  > — Unknown 2014 · [2] <!-- quote_key: 18746823_614030d2 -->

</details>

Cell Ontology mapping: pyramidal neuron [[CL:0000598](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0000598)] (BROAD). No EC layer III-specific CL term exists; CL:0000598 is the best available match. EC layer III pyramidal cells are a candidate for a dedicated CL term given their well-defined projection identity (temporoammonic pathway to CA1/subiculum).

---

## Results

One annotation-transfer run informs this node. Yao 2021 (GSE185862) 'L3 IT ENT' subclass cells (EC layer III IT projection neurons, including PCP4+ pyramidal cells projecting to CA1 and subiculum) map to WMBv1 supertype 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] with strong, high-purity results (F1=0.937, group_purity=0.888, target_purity=0.992). A secondary 10.2% of L3 IT ENT cells map to SUPT_0037, together covering 99.0% of source cells across two supertypes.

**Note on filtered AT figure:** A filtered AT figure could not be generated for this node. The source label "L3 IT ENT" is not present in the SSv4 CSV used for filtered figure generation — the SSv4 dataset (GEO:GSE185862) has very few entorhinal cortex layer III cells matching this specific label in the SSv4 CSV. No figure is embedded here.

### Mapping candidates table

| Rank | WMBv1 supertype | Cells (WMBv1) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] | 10,208 | 🟡 MODERATE | NT CONSISTENT · location CONSISTENT · Pcp4 mean=10.57 · F1=0.937 | Best candidate |
| 2 | 0037 L2/3 IT ENT Glut_5 [CS20230722_SUPT_0037] | 2,447 | 🔴 LOW | NT CONSISTENT · location CONSISTENT · Pcp4 mean=9.44 · F1=0.177 | Speculative |

Total: 2 edges; relationship PARTIAL_OVERLAP (TYPE_A_SPLITS — 88.8% + 10.2% = 99.0% of L3 IT ENT cells covered).

### Primary candidate property alignment — 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Atlas supertype | Alignment |
|---|---|---|---|
| NT type | Glutamatergic | Glutamatergic (SUBC_008 L2/3 IT ENT Glut) | CONSISTENT |
| Soma location | Entorhinal cortex [UBERON:0002728] layer III | SUPT_0036 in L2/3 IT ENT subclass; Yao 2021 'L3 IT ENT' label explicitly layer III | CONSISTENT |
| Pcp4 (defining marker) | PCP4; shared with CA2 pyramidal cells [2] | Not in atlas discriminating markers (Fermt1, Cxcl14); mean_expression=10.57 (precomputed_stats.h5) | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Yao 2021 (GSE185862) MapMyCells, L3 IT ENT (n=588) | Annotation transfer | SUPPORT | F1=0.937, group_purity=0.888, target_purity=0.992; 522/588 cells (88.8%) | at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 |

**Supporting evidence**

- **NT type — CONSISTENT.** SUPT_0036 belongs to subclass SUBC_008 L2/3 IT ENT Glut, a glutamatergic layer II–III IT subclass grouping entorhinal cortex neurons. The classical EC layer III PCP4+ pyramidal cell is glutamatergic [1].

- **Annotation transfer — SUPPORT (strong, high-purity).** MapMyCells local AT of Yao 2021 (GEO:GSE185862) 'L3 IT ENT' cells (n=588, EC layer III IT projection neurons including PCP4+ temporoammonic pathway cells): 522 (88.8%) map to SUPT_0036, F1=0.937, group_purity=0.888, target_purity=0.992. Near-perfect target purity (0.992) confirms that SUPT_0036 is populated almost exclusively by EC layer III cells. SUPT_0037 captures a further 10.2% (F1=0.177); together 99.0% of L3 IT ENT cells are covered.

- **Location — CONSISTENT.** The Yao 2021 'L3 IT ENT' subclass explicitly labels layer III cells of the entorhinal cortex [UBERON:0002728]. The WMBv1 'L2/3 IT ENT' designation groups layers II–III EC IT neurons; the near-perfect target_purity confirms SUPT_0036 is primarily populated by EC layer III cells in this dataset.

- **Marker Pcp4 — CONSISTENT.** Pcp4 mean=10.57 in SUPT_0036 (precomputed_stats.h5). Pcp4 is not among the atlas discriminating markers for SUPT_0036 (Fermt1, Cxcl14), but the quantitative value confirms active Pcp4 transcription consistent with the classical PCP4-positive identity. CA2 comparison: SUPT_0100 (CA2-FC-IG Glut_1) mean=11.26, SUPT_0101 (CA2-FC-IG Glut_2) mean=9.99, SUPT_0037 mean=9.44. Values across EC layer III and CA2 supertypes span 9.44–11.26 — Pcp4 does not discriminate between EC layer III and CA2 at atlas supertype level, consistent with its known broad expression in both populations [2].

**Concerns**

- **Pcp4 lacks discriminating power at atlas level.** Pcp4 mean expression is similarly elevated across EC layer III supertypes (SUPT_0036: 10.57; SUPT_0037: 9.44) and CA2 supertypes (SUPT_0100: 11.26; SUPT_0101: 9.99). Pcp4 alone cannot distinguish EC layer III from CA2 pyramidal cells at the transcriptomic atlas level. Additional EC layer III-specific markers are needed to achieve HIGH confidence.

- **L2/3 grouping in WMBv1.** The WMBv1 'L2/3 IT ENT' subclass does not separate layer II from layer III neurons at subclass level. SUPT_0036 is inferred to correspond predominantly to layer III cells based on the Yao 2021 AT result, but independent layer-resolved spatial validation would strengthen this.

- **TYPE_A_SPLITS — 10.2% secondary population in SUPT_0037.** The split likely reflects transcriptomic heterogeneity within the EC layer III population rather than a distinct cell class.

**What would upgrade confidence**

- Spatial transcriptomics (MERFISH or similar) confirming SUPT_0036 cells are predominantly in EC layer III rather than layer II.
- Run add-expression for EC layer III-specific markers (genes distinguishing EC layer III from CA2 beyond Pcp4) to strengthen the molecular rationale.

### Secondary candidate — 0037 L2/3 IT ENT Glut_5 [CS20230722_SUPT_0037] · 🔴 LOW

SUPT_0037 captures 10.2% of L3 IT ENT cells (n ≈ 60/588) with F1=0.177. It belongs to the same SUBC_008 L2/3 IT ENT Glut subclass as SUPT_0036 and has Pcp4 mean=9.44 (precomputed_stats.h5), consistent with the shared EC layer III Pcp4+ identity. The low F1 reflects this being a minor secondary destination. This edge likely represents transcriptomic heterogeneity at the tail of the L3 IT ENT distribution rather than a distinct biologically separable class. It is retained to provide complete coverage of the TYPE_A_SPLITS relationship.

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The EC layer III PCP4-positive pyramidal cell is defined on a CLASSICAL_MULTIMODAL basis: soma in entorhinal cortex [UBERON:0002728] layer III; glutamatergic [1]; defining marker Pcp4 (PCP4; shared with CA2 pyramidal cells, identifies but does not uniquely discriminate EC layer III) [1][2]; projects to CA1 and subiculum via the temporoammonic pathway [1].

**Atlas mapping query.** Candidate atlas clusters retrieved from WMBv1 (CCN20230722) at rank 1 (supertype) using NT type (glutamatergic) and region (entorhinal cortex) as primary filters.

**Property alignment.** Alignments graded CONSISTENT / NOT_ASSESSED. Pcp4 atlas values from precomputed_stats.h5 (supertype level); CA2 comparison values also from precomputed_stats.h5.

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse HPF SMART-Seq v4) |
| Source group | L3 IT ENT subclass (Yao 2021 Allen Institute taxonomy) |
| n cells (L3 IT ENT) | 588 |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default params, raw norm, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| n cells total | 6,398 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | No filtered AT figure available: source label "L3 IT ENT" not present in SSv4 CSV — SSv4 dataset has very few EC layer III cells matching this label in the SSv4 CSV. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes are validated against the evidencell knowledge base at write time.

*Generated by evidencell `07c6dbd` at 2026-05-19 from `kb/graphs/hippocampus/hippocampus_glutamatergic.yaml`.*

**Evidence base table.**

| Edge ID | Evidence type | Supports | Source |
|---|---|---|---|
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0036 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | SUPPORT — F1=0.937; group_purity=0.888; target_purity=0.992; 522/588 L3 IT ENT cells (88.8%) | at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 |
| edge_ec_layer3_pyramidal_cell_hippocampus_to_supt_0037 | ANNOTATION_TRANSFER (MapMyCells; GEO:GSE185862) | PARTIAL — F1=0.177; ~60/588 L3 IT ENT cells (10.2%) | at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1 |

</details>

---

## Discussion

**Primary mapping: EC layer III PCP4-positive pyramidal cell → 0036 L2/3 IT ENT Glut_4 [CS20230722_SUPT_0036] · MODERATE.** The Yao 2021 (GEO:GSE185862) annotation transfer of 588 'L3 IT ENT' cells maps 88.8% to SUPT_0036 (F1=0.937, group_purity=0.888, target_purity=0.992), providing strong, high-purity evidence. Near-perfect target_purity confirms SUPT_0036 is populated almost exclusively by EC layer III cells. Pcp4 mean=10.57 in SUPT_0036 (precomputed_stats.h5) is consistent with the classical PCP4+ identity, though Pcp4 is similarly elevated in CA2 supertypes (SUPT_0100 mean=11.26) and does not discriminate between EC layer III and CA2 at the atlas supertype level.

A secondary LOW-confidence edge to SUPT_0037 (F1=0.177, 10.2% of L3 IT ENT cells) captures the remaining EC layer III population and completes the TYPE_A_SPLITS. Together these two supertypes cover 99.0% of L3 IT ENT cells. No filtered AT figure was generated for either edge — the SSv4 dataset lacks sufficient EC layer III cells to populate the source label in the SSv4 CSV.

The L2/3 grouping in WMBv1 means that SUPT_0036 may contain a small layer II component; spatial transcriptomics would resolve this. No additional markers specific to EC layer III (vs. CA2 or EC layer II) have been assessed.

The Cell Ontology has no EC layer III-specific CL term; pyramidal neuron [CL:0000598] is used as BROAD mapping. The well-defined temporoammonic projection identity of EC layer III pyramidal cells makes them a strong candidate for a new CL term.

### Proposed experiments

1. **Spatial transcriptomics (MERFISH) validation:** confirm that SUPT_0036 cells are predominantly in EC layer III (rather than layer II) in the WMBv1 MERFISH data. This would upgrade the location assessment to CONFIRMED and provide grounds for a confidence upgrade.

2. **Add-expression for EC layer III-specific markers** (genes distinguishing EC layer III from CA2 beyond Pcp4) on SUBT_0036 and CA2 supertypes (SUPT_0100, SUPT_0101). Specific candidates from the literature or from differential expression between SUPT_0036 and CA2 supertypes would strengthen the molecular rationale.

3. **Assess SUPT_0037 vs. SUPT_0036 differential expression** to determine whether SUPT_0037 represents a molecularly distinguishable EC layer III subpopulation or sampling noise. Running add-expression for differentially expressed genes would reveal this; if SUPT_0037 is biologically distinguishable, the secondary edge could be upgraded to MODERATE.

4. **CL new term request** for "entorhinal cortex layer III pyramidal cell" (PCP4+, temporoammonic pathway to CA1/subiculum) via `workflows/cl-term-request.md`.

### Open questions

No explicit unresolved questions are recorded on these edges in the current KB entry. The implicit open questions are:

1. Does SUPT_0036 correspond predominantly to EC layer III (not layer II) cells in the WMBv1 MERFISH data? The Yao 2021 'L3 IT ENT' layer assignment provides indirect evidence, but a direct MERFISH spatial check would confirm.
2. Are there EC layer III-specific markers (beyond Pcp4) that can distinguish SUPT_0036 from CA2 supertypes (SUPT_0100, SUPT_0101) at the atlas level?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Unknown 2021 · PMID:34949991 | [34949991](https://pubmed.ncbi.nlm.nih.gov/34949991/) | neurotransmitter type; Pcp4 as EC layer III marker; temporoammonic projection |
| [2] | Unknown 2014 · PMID:24166578 | [24166578](https://pubmed.ncbi.nlm.nih.gov/24166578/) | Pcp4 marker (CA2 / EC layer III shared cross-regional expression) |
