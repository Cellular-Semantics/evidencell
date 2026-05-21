# Pyramidale-lacunosum moleculare (P-LM) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The pyramidale-lacunosum moleculare (P-LM) cell is an SST-positive GABAergic interneuron of the hippocampus with soma in CA1 stratum pyramidale and axon targeting stratum lacunosum-moleculare, identified together with the R-LM cell by Oliva et al. 2000 [1] using the GIN transgenic reporter. The P-LM cell has not been transcriptomically characterised; its defining difference from the R-LM cell is soma laminar position (stratum pyramidale vs. stratum oriens), and whether these two populations constitute transcriptomically distinct types or a single type with variable soma placement remains an open question.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] | — |
| NT | GABAergic | — |
| Markers | Sst (defining) | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — (no mapping) | — |

<details><summary>Details — source evidence for classical type properties</summary>

- **Soma location:** stratum pyramidale location based on the original characterisation study (Oliva et al. 2000 [1]); no formal location references are indexed in the facts file beyond the Sst marker citation. The stratum pyramidale soma location is the key morphological distinction from the R-LM cell.
- **Sst marker:** GIN transgenic reporter labelling at protein/reporter level in Oliva et al. 2000 [1]. Specificity to P-LM cells versus other SST+ hippocampal types is not established at transcriptomic resolution. No verbatim quote is available in the current evidence set.

</details>

Cell Ontology mapping: no CL term is mapped for this node. Given the thin evidence base and uncertain transcriptomic identity, a CL term request should be deferred until morpho-transcriptomic validation is available.

---

## Results

One candidate atlas supertype was assessed and eliminated as UNCERTAIN. No MODERATE or LOW edges were resolved. The primary disqualifying signal is a strong anatomical discordance: the proposed candidate supertype (SUPT_0219, Sst Gaba_6) is CA3-enriched with no CA1 pyramidal layer representation, while the P-LM cell is a CA1 type with soma in stratum pyramidale.

![Annotation transfer F1 heatmap — Yao 2021 SSv4 Sst subclass → WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_p_lm_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) SSv4 Sst source group (n=273 HIP cells) mapped to WMBv1. The Sst subclass maps cleanly at subclass level (F1=0.983); SUPT_0219 (Sst Gaba_6) is the dominant supertype target (F1=0.759, 161 cells, group_purity=0.626), but anatomical mismatch with the P-LM cell's CA1 soma location makes this supertype an imperfect candidate.*

### Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | 1495 | ⚪ UNCERTAIN | Sst CONSISTENT · NT CONSISTENT · anatomy DISCORDANT (CA3-enriched, no CA1) | Eliminated |

1 edge total · relationship type: UNCERTAIN.

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] — ⚪ UNCERTAIN

The primary disqualifying signal is an anatomical DISCORDANT: SUPT_0219 is predominantly CA3-enriched with no CA1 pyramidal layer representation, whereas the P-LM cell is a CA1 type with soma in stratum pyramidale.

**Supporting evidence**

- SST subclass identity is CONSISTENT: P-LM cell expresses Sst [1]; SUPT_0219 belongs to the Sst Gaba subclass with Sst as a defining marker (precomputed mean 10.17).
- GABAergic NT type is CONSISTENT across both nodes.
- Annotation transfer: MapMyCells local, Yao 2021 (GEO:GSE185862) SSv4 Sst subclass (n=273 HIP cells). SUPT_0219 is the dominant supertype target (F1=0.759, 161/273 cells, target_purity=0.964). At subclass level, 053 Sst Gaba captures 265/273 cells (F1=0.983). P-LM cells as Sst+ interneurons would be expected within the Sst Gaba subclass; SUPT_0219 being the dominant target is consistent with P-LM assignment pending resolution of the anatomical discordance.

**Concerns**

- DISCORDANT anatomy (primary concern): SUPT_0219 is predominantly CA3 (CA3 SO: 305 cells, CA3 lucidum: 99, CA3 SR: 167, CA3 pyr: 261) with no CA1 pyramidal layer representation. The P-LM cell is a CA1 type described in stratum pyramidale. *(note: the complete absence of CA1 pyramidal layer cells in SUPT_0219 is the primary evidence against this supertype as the P-LM correspondent; it is not a minor registration artefact.)*
- SINGLE_STUDY: P-LM cell described in a single study [1]. Not transcriptomically characterised. May be the same transcriptomic type as R-LM cells.
- AMBIGUOUS_MAPPING: P-LM and R-LM were identified in the same study and differ only in soma laminar position. Whether they constitute distinct transcriptomic types or a single type with variable soma placement is unknown. If they are the same type, the R-LM edge candidate supertype (SUPT_0216, CA1 SO-enriched) may be a better fit for both.

**What would upgrade confidence**

- A transcriptomic dataset with morphologically identified P-LM cell labels (patch-seq with post-hoc reconstruction, or retrograde labelling from stratum lacunosum-moleculare followed by scRNA-seq of CA1 stratum pyramidale neurons) to enable direct supertype assignment.
- MERFISH or spatial transcriptomics data resolving Sst+ interneurons by soma layer in CA1 to determine whether a distinct atlas cluster occupies the stratum pyramidale niche and which supertype it corresponds to.
- Explicit comparison of CA1-enriched Sst supertypes in WMBv1 (particularly SUPT_0216, which is CA1 SO-enriched) as alternative candidates — if P-LM and R-LM are the same type, SUPT_0216 may be the correct target regardless of the stratum pyramidale soma position reported for P-LM.

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The P-LM cell is defined on a CLASSICAL_MULTIMODAL basis: soma in the pyramidal layer of CA1 [UBERON:0014548]; GABAergic neurotransmitter type; defining marker Sst [1]. Primary characterisation from Oliva et al. 2000 (PMID:10777798); no subsequent transcriptomic characterisation is recorded.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at rank 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Numerical values from precomputed expression on the supertype in the taxonomy reference store.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 mouse hippocampal formation SMART-Seq v4) |
| Source cluster label | Sst (n=273 HIP cells; morphologically unresolved) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398; Sst subclass n=273 |
| Run record | `kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/` |
| Code reference | https://github.com/AllenInstitute/cell_type_mapper |
| F1 matrix | `f1_scores_best.csv` |
| Caveats | Yao 2021 SSv4 Sst label encompasses OLM, bistratified, hippocampo-septal, and other Sst types; P-LM-specific resolution is not achievable from this morphologically unresolved source. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed expression from supertype YAML in the taxonomy reference store.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:26+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA; ANNOTATION_TRANSFER | WEAK; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** P-LM cell → 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at UNCERTAIN confidence; candidate is ELIMINATED. Key support: Sst expression is CONSISTENT (precomputed mean 10.17); SUPT_0219 is the dominant Sst annotation transfer target (F1=0.759, 161/273 cells); both nodes are GABAergic. Key caveats: SUPT_0219 is a CA3-enriched supertype (CA3 SO: 305 cells, CA3 pyr: 261 cells, CA3 SR: 167 cells) with no CA1 pyramidal layer representation — a strong anatomical DISCORDANT against a CA1-localised type with soma in stratum pyramidale; the P-LM cell was described in a single study [1] with no subsequent transcriptomic characterisation; whether P-LM and R-LM cells are transcriptomically distinct is unknown; if they are the same type, the CA1 stratum oriens-enriched SUPT_0216 (primary OLM/R-LM candidate) may be the correct target for both.

### Proposed experiments

**Morphology-coupled transcriptomics.**

- Patch-seq of CA1 Sst+ interneurons with soma confirmed in stratum pyramidale; post-hoc morphological reconstruction to verify P-LM identity (axon to stratum lacunosum-moleculare); retrograde labelling from SLM to enrich for P-LM and R-LM cells followed by scRNA-seq.
- Cross-check: current AT uses the bulk Sst subclass (morphologically unresolved); direct cluster assignment requires a morphologically confirmed P-LM labelled reference. This is the primary bottleneck and would also resolve the P-LM vs. R-LM identity question.

**Spatial transcriptomics.**

- MERFISH or SLIDE-seq of hippocampal CA1 to map Sst+ interneurons by soma layer (stratum oriens vs. stratum pyramidale) and assign WMBv1 supertype identities. Identify atlas clusters enriched in CA1 stratum pyramidale among Sst+ interneurons.
- Cross-check: SUPT_0219 has no CA1 pyramidal layer cells in atlas metadata; spatial data would reveal whether any WMBv1 supertype occupies this niche and inform whether the P-LM node requires a supertype re-assignment.

**Comparison of P-LM and R-LM transcriptomic profiles.**

- Isolate CA1 stratum pyramidale vs. stratum oriens GIN+ cells by layer-selective dissection or laminar patch-seq, then compare transcriptomes. A null result (no significant DEGs) would indicate P-LM and R-LM are the same transcriptomic type and should share a mapping edge.
- Cross-check: the single-study provenance [1] and identical morphological characterisation of both types motivates this comparison before either node advances beyond UNCERTAIN confidence.

### Open questions

1. Do P-LM and R-LM cells constitute transcriptomically distinct types, or are they a single Sst interneuron type with variable soma laminar position?
2. Which WMBv1 supertype, if any, is enriched in CA1 stratum pyramidale among Sst+ interneurons — and does SUPT_0216 (CA1 SO-enriched) fit better than SUPT_0219 (CA3-enriched) for the P-LM cell?
3. Is the P-LM cell consistently identifiable across individual animals and preparations, or is it a morphological variant captured only under specific labelling conditions in the original study [1]?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst defining marker; classical characterisation |
