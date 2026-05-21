# Low-threshold high-Ih (LTH) cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

The low-threshold high-Ih (LTH) cell is an SST-positive GABAergic interneuron of CA1 stratum oriens, defined by physiological clustering from SST-Cre Ai14 mouse acute hippocampal slices in a single study (Hewitt et al. 2021 [1]). Its defining electrophysiological signature is strong spike frequency adaptation combined with a prominent hyperpolarisation-activated cation current (I_h). Beyond SST-Cre driver labelling and CA1 stratum oriens soma location, no molecular markers or morphological properties have been characterised, making transcriptomic identity entirely unknown and atlas mapping fully speculative.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552] | [1] |
| NT | GABAergic | — |
| Markers | Sst (defining; via SST-Cre labelling) | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — (no mapping) | — |

<details><summary>Details — source evidence for classical type properties</summary>

- **Soma location:** CA1 stratum oriens documented by Hewitt et al. 2021 [1] using physiological clustering of SST-Cre Ai14 cells in acute hippocampal slices. The LTH cluster was defined within the SST-Cre population by strong spike frequency adaptation and prominent I_h sag.
- **Sst marker:** inferred from SST-Cre Ai14 driver labelling, not from direct immunostaining or ISH of Sst transcript in morphologically identified LTH cells. The Cre driver labels all SST-expressing cells in the lineage; specificity to LTH cells versus other SST+ stratum oriens types (OLM, hippocampo-septal, oriens-oriens) is not established. No verbatim quote is available in the current evidence set.

</details>

Cell Ontology mapping: no CL term is mapped for this node. Given that the LTH cell is defined exclusively by electrophysiology with no molecular anchor beyond SST-Cre, a CL term request should be deferred until transcriptomic characterisation is available.

---

## Results

One candidate atlas supertype was assessed and eliminated as UNCERTAIN. No MODERATE or LOW edges were resolved. The primary disqualifying signals are: (1) SUPT_0219 (Sst Gaba_6) is CA3-enriched with no CA1 stratum oriens representation, while LTH cells were characterised in CA1; and (2) the LTH cell is defined exclusively by electrophysiology with no molecular identity established, making any transcriptomic supertype assignment a placeholder pending characterisation.

![Annotation transfer F1 heatmap — Yao 2021 SSv4 Sst subclass → WMBv1](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/figures/f1_for_lth_cell_hippocampus.png)

*F1 across taxonomy levels for the Yao 2021 (GEO:GSE185862) SSv4 Sst source group (n=273 HIP cells) mapped to WMBv1. SUPT_0219 (Sst Gaba_6) is the dominant Sst supertype target (F1=0.759, 161 cells, target_purity=0.964), but the CA3-enriched anatomy of SUPT_0219 is discordant with the CA1 stratum oriens location of LTH cells, and the Sst label is morphologically unresolved.*

### Candidate overview table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key alignment | Verdict |
|---|---|---|---:|---|---|---|
| — | — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | 1495 | ⚪ UNCERTAIN | Sst CONSISTENT · NT CONSISTENT · anatomy DISCORDANT (CA3-enriched, no CA1 SO) | Eliminated |

1 edge total · relationship type: UNCERTAIN.

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] — ⚪ UNCERTAIN

The primary disqualifying signals are an anatomical DISCORDANT (SUPT_0219 is CA3-enriched; LTH cells are CA1-localised) and an electrophysiology-only definition with no molecular identity established for the classical type.

**Supporting evidence**

- NT type is CONSISTENT: LTH cell is GABAergic; SUPT_0219 belongs to the Sst Gaba subclass.
- Sst marker is CONSISTENT: LTH cells are SST-Cre labelled; SUPT_0219 carries Sst as a defining marker (precomputed mean 10.17).
- Annotation transfer: MapMyCells local, Yao 2021 (GEO:GSE185862) SSv4 Sst subclass (n=273 HIP cells). SUPT_0219 is the dominant supertype target (161/273 cells, F1=0.759, target_purity=0.964). At subclass level, 053 Sst Gaba captures 265/273 cells (F1=0.983). Sst+ LTH cells in CA1 would be expected within the Sst Gaba subclass; SUPT_0219 being the dominant target is consistent with this assignment, though the anatomical mismatch undermines confidence.

**Concerns**

- DISCORDANT anatomy (primary concern): SUPT_0219 is CA3-enriched (CA3 SO: 305 cells, CA3 lucidum: 99, CA3 SR: 167, CA3 pyr: 261) with no CA1 stratum oriens representation. LTH cells were characterised exclusively in CA1 stratum oriens [UBERON:0014552] [1]. *(note: the complete absence of CA1 SO cells in SUPT_0219 is a strong counter-evidence; this is not consistent with a registration boundary artefact.)*
- ELECTROPHYSIOLOGY_ONLY_DEFINITION: LTH cell is defined exclusively by physiological clustering [1] in a single study. No morphological reconstruction or molecular markers beyond SST-Cre labelling were reported. Transcriptomic identity is entirely unknown.
- AMBIGUOUS_MAPPING: LTH cells may overlap with OLM cells (both SST+, CA1 SO soma). If LTH and OLM are transcriptomically indistinguishable, the correct supertype target would be SUPT_0216 (not SUPT_0219), as SUPT_0216 is CA1 SO-enriched and the primary OLM candidate. The current assignment to SUPT_0219 is a placeholder.
- SINGLE_STUDY: single-lab evidence from a single study [1]. Classification stability across datasets, recording conditions, and mouse ages is unknown.

**What would upgrade confidence**

- A MODERATE edge would require: (a) transcriptomic profiling (patch-seq or scRNA-seq) of physiologically identified LTH cells confirming assignment to SUPT_0219 or an alternative supertype, and (b) resolution of the anatomical discordance (revised spatial atlas data showing a CA1 SO component of SUPT_0219, or demonstration that LTH cells share the molecular profile of SUPT_0219 despite the regional bias in the atlas).
- A HIGH edge would additionally require independent replication of the LTH physiological classification and morphological confirmation distinguishing LTH from OLM cells.

## Methods

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The LTH cell is defined on a CLASSICAL_MULTIMODAL basis: soma in CA1 stratum oriens [UBERON:0014552] [1]; GABAergic neurotransmitter type; Sst marker (via SST-Cre driver) [1]. Primary characterisation from Hewitt et al. 2021 (PMID:33991454) by physiological clustering of SST-Cre Ai14 cells; no morphological reconstruction or transcriptomic profiling reported.

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
| Caveats | Yao 2021 SSv4 Sst label encompasses OLM, bistratified, hippocampo-septal, and other Sst types; LTH-specific resolution is not achievable from this morphologically unresolved source. |

**Atlas data sources.** WMBv1 (CCN20230722); precomputed expression from supertype YAML in the taxonomy reference store.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. The pre-write hook rejects any unresolvable identifier or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:26+00:00 from [kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_lth_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA; ANNOTATION_TRANSFER | WEAK; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** LTH cell → 0219 Sst Gaba_6 [CS20230722_SUPT_0219] at UNCERTAIN confidence; candidate is ELIMINATED. Key support: Sst expression is CONSISTENT (precomputed mean 10.17); SUPT_0219 is the dominant Sst annotation transfer target (F1=0.759, 161/273 cells, target_purity=0.964); both nodes are GABAergic. Key caveats: SUPT_0219 is CA3-enriched with no CA1 stratum oriens cells — a strong anatomical DISCORDANT for a type characterised exclusively in CA1 stratum oriens [1]; the LTH cell is defined solely by electrophysiology with no molecular markers beyond SST-Cre, meaning any transcriptomic supertype assignment is entirely provisional; LTH cells may be transcriptomically indistinguishable from OLM cells (both SST+/CA1 SO), which would make SUPT_0216 the correct target rather than SUPT_0219; evidence rests on a single study [1].

### Proposed experiments

**Patch-seq from physiologically identified LTH cells (highest priority).**

- Record whole-cell patch-clamp on SST-Cre Ai14 CA1 neurons; confirm LTH physiology (strong spike frequency adaptation, prominent I_h sag); harvest cell contents for scRNA-seq; apply MapMyCells to assign WMBv1 supertypes.
- Cross-check: current AT uses the bulk Sst subclass (morphologically and physiologically unresolved); LTH-specific transcriptomic identity requires patch-seq from physiologically confirmed LTH cells. This is the only experiment that can directly resolve the SUPT_0219 vs. SUPT_0216 ambiguity and the LTH vs. OLM overlap question.

**Multiplexed in situ hybridisation — Sst + Nos1 + Npy + Cck.**

- smFISH/RNAscope panel in CA1 stratum oriens to identify molecular discriminators between LTH and OLM cells. Sst/Nos1 co-expression marks canonical OLM cells; if LTH cells are Nos1-negative, they may be transcriptomically distinct from OLM and potentially mappable to a different supertype.
- Cross-check: no molecular markers beyond SST-Cre labelling are recorded for the LTH cell; this panel would establish a molecular discriminator for future annotation transfer experiments.

**Physiological replication in an independent laboratory.**

- Reproduce the LTH physiological classification in a second lab, using different recording conditions and mouse ages, to confirm the LTH cluster is a stable functional type and not a recording-condition artefact.
- Cross-check: current evidence rests on a single study [1]; replication is needed before the LTH node can be treated as a reliable classification target for transcriptomic mapping.

### Open questions

1. Does the LTH cell constitute a transcriptomically distinct type from OLM cells, or is it a physiological variant within the same transcriptomic cluster (which would make SUPT_0216 the correct supertype target)?
2. Which WMBv1 supertype corresponds to the CA1 stratum oriens Sst+ interneuron population distinct from OLM cells — SUPT_0219 (dominant Sst AT target but CA3-enriched) or another supertype?
3. Is the LTH physiological classification reproducible across independent datasets, recording conditions, and animal ages?
4. Do LTH cells express Nos1, Calb1, or other Sst-subtype discriminating markers that would distinguish them molecularly from OLM cells?
5. Could the CA3 anatomical enrichment of SUPT_0219 in the WMBv1 atlas reflect a sampling or clustering bias, and is there CA1 SO representation of SUPT_0219 not captured in current atlas metadata?

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hewitt et al. 2021 | [33991454](https://pubmed.ncbi.nlm.nih.gov/33991454/) | soma location; LTH physiological characterisation; Sst marker (via SST-Cre) |
