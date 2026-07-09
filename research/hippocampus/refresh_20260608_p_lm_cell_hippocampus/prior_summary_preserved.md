# Pyramidale-lacunosum moleculare (P-LM) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum pyramidale [UBERON:0005401] | — |
| NT | GABAergic | — |
| Markers | Sst+ | [1] |

**Node notes:** Stub from cite-traverse (2026-04-10). THIN EVIDENCE — described in one study (Oliva et al. 2000 [1]). The P-LM and R-LM cells were identified together in the same study and differ only in soma laminar position (stratum pyramidale vs. stratum oriens respectively). Whether they constitute distinct transcriptomic types or a single type with variable soma placement is unknown.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | ⚪ UNCERTAIN | SST+/GABAergic CONSISTENT · anatomy DISCORDANT (CA3-enriched, no CA1) | Eliminated |

1 edge total · relationship type: UNCERTAIN. No MODERATE or LOW edges are present.

---

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] — ⚪ UNCERTAIN

The primary disqualifying signal is a strong anatomical DISCORDANT: SUPT_0219 [CS20230722_SUPT_0219] is predominantly CA3-enriched with no CA1 pyramidal layer representation, whereas the P-LM cell is a CA1 type with soma in stratum pyramidale.

**Supporting evidence**

- SST subclass identity consistent: P-LM cell expresses Sst [1]; SUPT_0219 [CS20230722_SUPT_0219] belongs to the Sst Gaba subclass with Sst as a defining marker (precomputed mean 10.17).
- GABAergic NT type consistent across both nodes.
- Annotation transfer (Yao 2021 SSv4 hippocampal Sst cells, GEO:GSE185862, n=273 HIP cells) onto WMBv1 places SUPT_0219 [CS20230722_SUPT_0219] as the dominant supertype target (F1=0.759, 161/273 cells). At subclass level, 053 Sst Gaba captures 265/273 cells with F1=0.983, confirming robust subclass-level coherence for hippocampal Sst interneurons.

**Marker evidence provenance**

- **Sst:** Single immunohistochemical study (Oliva et al. 2000 [1]). No quantitative transcriptomic data exist for P-LM cells specifically.
- **Sst in atlas:** Precomputed HDF5 stats from WMBv1 CCN20230722; Sst is a defining marker for SUPT_0219 [CS20230722_SUPT_0219] with mean expression 10.17.
- **Annotation transfer source (GEO:GSE185862):** Yao 2021 SSv4 Sst subclass is a mixed population (OLM, bistratified, hippocampo-septal, oriens-oriens, and others) without P-LM-specific labels. Subtype resolution is not achievable from this source alone.

**Concerns**

- **DISCORDANT anatomy (primary concern).** SUPT_0219 [CS20230722_SUPT_0219] is predominantly represented in CA3 (CA3 SO: 305 cells, CA3 lucidum: 99, CA3 SR: 167, CA3 pyr: 261) with no CA1 pyramidal layer representation. The P-LM cell is a CA1 type with soma in stratum pyramidale [UBERON:0005401]. *(note: CA3 is adjacent to CA1 in the hippocampal trisynaptic circuit, but the complete absence of CA1 pyramidal layer cells in SUPT_0219 is a strong counter-evidence; this is not a registration boundary artefact.)*
- **SINGLE_STUDY.** P-LM cell described in a single study [1] and has not been independently replicated in transcriptomic datasets.
- **AMBIGUOUS_MAPPING.** P-LM and R-LM were identified in the same study and differ only in soma laminar position. If they are the same transcriptomic type, both should map to the same atlas supertype and should not be treated as separate nodes.
- **Annotation transfer F1=0.759 at supertype level** reflects mixture of multiple Sst interneuron subtypes, not P-LM-specific signal.

**What would upgrade confidence**

- A transcriptomic dataset with morphologically identified P-LM cell labels (patch-seq with post-hoc reconstruction, or retrograde labelling from stratum lacunosum-moleculare + scRNA-seq) would enable direct supertype assignment.
- MERFISH or spatial transcriptomics data resolving Sst+ interneurons by soma layer in CA1 would clarify whether a distinct atlas cluster occupies the stratum pyramidale niche.
- Explicit comparison of CA1-enriched Sst supertypes in WMBv1 (particularly SUPT_0216) as alternative candidates — a CA1-enriched Sst supertype may be a better fit even if the P-LM soma is in stratum pyramidale rather than stratum oriens.
- Clarification of whether P-LM and R-LM cells share a transcriptomic identity would resolve the ambiguous mapping caveat and determine whether both nodes should point to the same atlas supertype.

---

## Proposed experiments

### Morphology-coupled transcriptomics
- **What:** Patch-seq of CA1 Sst+ interneurons with soma confirmed in stratum pyramidale; post-hoc morphological reconstruction to verify P-LM identity (axon to stratum lacunosum-moleculare); retrograde labelling from SLM to enrich for P-LM and R-LM cells + scRNA-seq
- **Target:** Test whether P-LM and R-LM are transcriptomically distinct; determine correct WMBv1 supertype assignment
- **Expected output:** AnnotationTransferEvidence on this edge; or evidence that P-LM and R-LM share a transcriptomic identity warranting node merger
- **Resolves:** Open questions 1 and 2

### Spatial transcriptomics
- **What:** MERFISH or SLIDE-seq of hippocampal CA1 to map Sst+ interneurons by soma layer (stratum oriens vs. stratum pyramidale) and assign WMBv1 supertype identities
- **Target:** Identify atlas clusters enriched in CA1 stratum pyramidale among Sst+ interneurons
- **Expected output:** Spatial validation of a P-LM-consistent cluster; informs whether SUPT_0219 or SUPT_0216 has any CA1 SP Sst+ representation
- **Resolves:** Open question 2

---

## Open questions

1. Do P-LM and R-LM cells constitute transcriptomically distinct types, or do they represent a single Sst interneuron type with variable soma laminar position across CA1 strata?
2. Which WMBv1 supertype, if any, is enriched in CA1 stratum pyramidale among Sst+ interneurons — and does SUPT_0216 fit better than SUPT_0219 [CS20230722_SUPT_0219]?
3. Is the P-LM cell consistently present across individual animals and preparations, or is it a morphological variant captured only under specific labelling conditions in the original study?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA — supertype marker and anatomy comparison | WEAK |
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Sst subclass n=273 HIP cells | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst marker |
