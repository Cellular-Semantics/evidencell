# Pyramidale-lacunosum moleculare (P-LM) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | stratum pyramidale [UBERON:0005401] | — |
| Neurotransmitter | GABAergic | — |
| Defining markers | Sst | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — | — |

**Thin evidence note:** The P-LM cell is described in a single study (Oliva et al. 2000 [1]). It has not been transcriptomically characterised as an independent type. The P-LM and R-LM cells were identified together in the same study and may not be separable at the transcriptomic level; both are Sst+ and differ only in soma laminar position (stratum pyramidale vs stratum oriens respectively).

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype accession | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0219 Sst Gaba_6 | CS20230722_SUPT_0219 | — | ⚪ UNCERTAIN | SST+/GABAergic consistent; anatomy DISCORDANT (CA3-enriched, no CA1) | Eliminated |

**Total edges:** 1 · Relationship type: UNCERTAIN

*(note: No MODERATE or LOW edges were generated for this cell type. The single candidate is classified UNCERTAIN and appears in the Eliminated candidates section below.)*

---

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] · ⚪ UNCERTAIN

**Supporting evidence**

- SST subclass identity is consistent: the P-LM cell expresses Sst [1] and 0219 Sst Gaba_6 [CS20230722_SUPT_0219] belongs to the WMBv1 Sst Gaba subclass with Sst as a defining marker (precomputed mean expression: 10.17).
- GABAergic neurotransmitter type is consistent across both nodes: the classical type is GABAergic; the atlas supertype belongs to the GABA (Sst Gaba) subclass.
- Annotation transfer of Yao 2021 SSv4 hippocampal Sst cells (GEO:GSE185862, n=273 HIP cells) onto WMBv1 places 0219 Sst Gaba_6 [CS20230722_SUPT_0219] as the dominant supertype target (F1=0.759; 161/273 cells). At subclass level, the 053 Sst Gaba subclass captures 265/273 cells with F1=0.983, confirming robust subclass-level coherence for hippocampal Sst interneurons.

**Marker evidence provenance**

- Sst marker for the P-LM cell: single immunohistochemical study (Oliva et al. 2000 [1]). No quantitative transcriptomic data exist for this classical type specifically.
- Sst expression in the atlas supertype: precomputed HDF5 stats from WMBv1 CCN20230722; Sst is a defining marker for this supertype with a mean expression of 10.17.
- Annotation transfer source: Yao 2021 SSv4 patch-seq dataset (GEO:GSE185862), hippocampal Sst subclass cells (n=273). This dataset pools multiple Sst interneuron subtypes (OLM, bistratified, hippocampo-septal, oriens-oriens, and others) and does not provide morphologically identified P-LM-specific labels; subtype resolution is therefore not achievable from this source alone.

**Concerns**

- DISCORDANT anatomy (primary concern): 0219 Sst Gaba_6 [CS20230722_SUPT_0219] is predominantly represented in CA3 in atlas metadata (CA3 SO: 305 cells, CA3 lucidum: 99, CA3 SR: 167, CA3 pyr: 261) with no CA1 pyramidal layer representation. The P-LM cell is a CA1 type with its soma in stratum pyramidale [UBERON:0005401]. This anatomical mismatch is the primary reason for UNCERTAIN classification.
- A CA1-enriched Sst supertype (e.g., SUPT_0216) may be a more appropriate candidate, but the distinctive soma position in stratum pyramidale rather than stratum oriens was the basis for separating the P-LM cell from the R-LM cell as a distinct mapping target.
- SINGLE_STUDY caveat: the P-LM cell is described in a single study [1] and has not been independently replicated in transcriptomic datasets.
- AMBIGUOUS_MAPPING: P-LM and R-LM cells were identified in the same study and differ only in soma laminar position. Whether they constitute distinct transcriptomic types or represent a single type with variable soma placement is unknown; if the latter, they would map to the same atlas supertype and should not be treated as separate nodes.
- Annotation transfer F1=0.759 at supertype level reflects mixture of multiple Sst interneuron subtypes in the source dataset, not P-LM-specific signal.

**What would upgrade confidence**

- A transcriptomic dataset with morphologically identified P-LM cell labels (patch-seq with post-hoc morphological reconstruction, or retrograde labelling from stratum lacunosum-moleculare combined with single-cell RNA-seq) would enable direct supertype assignment.
- MERFISH or spatial transcriptomics data resolving Sst+ interneurons by soma layer in CA1 would clarify whether a distinct atlas cluster occupies the stratum pyramidale niche.
- Explicit comparison of CA1-enriched Sst supertypes in WMBv1 (particularly SUPT_0216) as alternative candidates, using atlas metadata for soma-layer distribution, could identify a better-fitting target.
- Clarification of whether P-LM and R-LM cells share a transcriptomic identity would resolve the ambiguous mapping caveat and determine whether both nodes should point to the same atlas supertype.

---

## Proposed experiments

No structured proposed experiments were recorded in the source facts for this cell type. The following are inferred from the concerns and open questions.

**Morphology-coupled transcriptomics**

- Patch-seq of CA1 Sst+ interneurons with soma confirmed in stratum pyramidale, with post-hoc morphological reconstruction to verify P-LM identity (axon projecting to stratum lacunosum-moleculare).
- Retrograde labelling from stratum lacunosum-moleculare to enrich for P-LM and R-LM cells, followed by single-cell RNA-seq, to test whether the two types are transcriptomically distinct.

**Spatial transcriptomics**

- MERFISH or SLIDE-seq profiling of hippocampal CA1 to map Sst+ interneurons by soma layer (stratum oriens vs stratum pyramidale) and assign WMBv1 supertype identities.

**Comparative atlas analysis**

- Systematic comparison of WMBv1 Sst supertypes for CA1 soma-layer enrichment, with explicit focus on SUPT_0216 and neighbouring supertypes, to identify any candidate with CA1 stratum pyramidale representation.

---

## Open questions

1. Do P-LM and R-LM cells constitute transcriptomically distinct types, or do they represent a single Sst interneuron type with variable soma laminar position across CA1 strata?
2. Which WMBv1 supertype, if any, is enriched in CA1 stratum pyramidale among Sst+ interneurons — and does SUPT_0216 fit better than SUPT_0219?
3. Is the P-LM cell consistently present across individual animals and preparations, or is it a morphological variant captured only under specific labelling conditions in the original study?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_p_lm_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA, ANNOTATION_TRANSFER | WEAK / PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Oliva et al. 2000 | [10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/) | Sst marker |
