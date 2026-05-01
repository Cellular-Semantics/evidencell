# Low-threshold high-Ih (LTH) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Stratum oriens of hippocampus [UBERON:0014548] (CA1 stratum oriens) | [1] |
| Neurotransmitter | GABAergic | — |
| Defining markers | Sst | [1] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| CL term | — | — |

**Evidence note:** This node is a thin-evidence stub derived from a single study (Hewitt et al. 2021 [1]) using physiological clustering of SST-Cre Ai14 cells in CA1 acute slices. The LTH cell is characterised by strong spike frequency adaptation and a prominent hyperpolarisation-activated cation current (I_h). No molecular markers beyond SST-Cre labelling have been reported; transcriptomic identity is entirely unknown.

---

## Mapping candidates

| Rank | WMBv1 supertype | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | *(no MODERATE or LOW edges)* | — | — | — | — | — |

**Total edges:** 1 (UNCERTAIN). No MODERATE or LOW mappings were established for the LTH cell. The single edge to SUPT_0219 is eliminated primarily on anatomical grounds. See Eliminated candidates below.

---

## Eliminated candidates

### 0219 Sst Gaba\_6 [CS20230722\_SUPT\_0219] · ⚪ UNCERTAIN

**Supporting evidence**

- Neurotransmitter type is consistent: LTH cell is GABAergic; SUPT\_0219 belongs to the 053 Sst Gaba subclass [CS20230722\_SUBC\_053], confirming GABAergic identity across both nodes.
- Sst marker is consistent: LTH cells are SST-Cre labelled; SUPT\_0219 carries Sst as a defining marker with a high precomputed mean expression of 10.17.
- MapMyCells annotation transfer (Yao 2021, GEO:GSE185862, n=273 SSv4 Sst HIP cells) confirms strong subclass-level correspondence: 265/273 cells mapped to the Sst Gaba subclass (F1=0.983, group purity=0.989, target purity=0.978). At supertype level, SUPT\_0219 was the dominant target for these HIP Sst cells (161/273 cells, F1=0.759, group purity=0.626, target purity=0.964).

**Marker evidence provenance**

- SST-Cre Ai14 driver (Hewitt et al. 2021 [1]): SST-Cre labels a broad population of Sst interneurons across all hippocampal Sst subtypes (OLM, bistratified, oriens-oriens, hippocampo-septal, and others). No single-cell transcriptomics, in situ hybridisation, or quantitative gene-expression measurement was performed on LTH cells specifically. The Sst marker assignment reflects Cre-driver breadth, not confirmed high-level Sst expression at the single-cell resolution.
- The Yao 2021 source dataset (GEO:GSE185862, SSv4 Sst subclass, n=273 HIP cells) is a heterogeneous Sst interneuron population. The supertype-level F1 of 0.759 and group purity of 0.626 indicate that Sst HIP cells are distributed across multiple supertypes — SUPT\_0219 is the plurality target but not dominant for the full mixed Sst population. Subtype resolution would require a source dataset with morphologically or physiologically identified Sst interneuron labels.

**Concerns**

- **Discordant anatomy (primary concern):** SUPT\_0219 is CA3-enriched in the WMBv1 atlas (305 CA3 stratum oriens cells assigned); no CA1 stratum oriens cells are present in SUPT\_0219. LTH cells were characterised exclusively in CA1 stratum oriens. This regional mismatch is the principal reason the edge is classified as UNCERTAIN rather than LOW or MODERATE.
- **Electrophysiology-only definition:** The LTH cell is defined solely by physiological clustering in a single study. No morphological reconstruction or molecular profiling beyond SST-Cre labelling was performed. Whether the LTH type constitutes a transcriptomically distinct entity — rather than a physiological state, a high-I_h variant, or a recording artifact — is unresolved.
- **Potential OLM overlap:** LTH cells share key features with OLM cells (SST+, CA1 stratum oriens soma, horizontal morphology implied by CA1 SO location). If LTH and OLM cells are transcriptomically indistinguishable, the correct supertype target would be SUPT\_0216 (OLM-associated) rather than SUPT\_0219. The current assignment to SUPT\_0219 is a placeholder pending molecular characterisation.
- **Single-study, single-lab evidence:** The LTH classification has not been reproduced in independent physiological characterisation studies. Classification stability across datasets, recording conditions, and mouse ages is unknown.
- **Mixed annotation-transfer source:** The AT group purity of 0.626 at supertype level confirms that Yao 2021 Sst HIP cells are heterogeneous at the supertype level. The AT result supports SUPT\_0219 as a major Sst HIP supertype generally, but does not provide evidence specific to LTH cells.

**What would upgrade confidence**

- A MODERATE edge would require at minimum: (a) transcriptomic profiling (Patch-seq or scRNA-seq) of physiologically identified LTH cells confirming assignment to SUPT\_0219, and (b) resolution of the anatomical discordancy (CA1 vs. CA3) — either by revised MERFISH/spatial atlas data showing SUPT\_0219 in CA1 SO, or by demonstrating that LTH cells share the molecular profile of SUPT\_0219 despite the regional bias.
- A HIGH edge would additionally require independent replication of the LTH physiological classification in a second study, and morphological confirmation distinguishing LTH from OLM cells.

---

## Proposed experiments

### Patch-seq (highest priority)

- **Patch-seq on physiologically identified LTH cells** in SST-Cre Ai14 CA1 acute slices: record whole-cell patch-clamp, confirm LTH physiology (strong spike-frequency adaptation + prominent I_h sag), then harvest cell contents for scRNA-seq. Direct transcriptomic assignment to WMBv1 supertypes would resolve SUPT\_0219 vs. SUPT\_0216 ambiguity with a single experiment type.

### Multiplex in situ hybridisation

- **smFISH/RNAscope panel in CA1 stratum oriens** using: *Sst*, *Nos1*, *Calb1*, *Npy*, *Cck*. Sst/Nos1 co-expression marks OLM cells; differential expression of *Npy* or *Calb1* relative to OLM would provide a potential molecular discriminator for LTH cells in tissue without requiring electrophysiology.

### Physiological replication

- **Independent physiological classification** (second lab, different recording conditions, adult vs. juvenile mice) to confirm the LTH cluster is a stable, reproducible functional type rather than a physiological outlier or classification artifact.

### OLM comparison

- **Parallel recording of LTH and morphologically reconstructed OLM cells** in the same preparation to quantify I_h magnitude and spike-frequency adaptation differences and establish a quantitative electrophysiological boundary between the two types, enabling future Patch-seq experiments to unambiguously assign cells.

---

## Open questions

1. Does the LTH cell constitute a transcriptomically distinct type, or is it a physiological variant (e.g. high-I_h state) within an existing Sst interneuron type such as OLM?
2. Which WMBv1 supertype corresponds to the CA1 stratum oriens Sst interneuron population: SUPT\_0219 (CA3-enriched in the atlas) or SUPT\_0216 (OLM-associated)?
3. Is the LTH physiological classification reproducible across independent datasets, recording conditions, and animal ages?
4. Do LTH cells express Nos1, Calb1, or other Sst-subtype discriminators that would distinguish them molecularly from OLM cells and permit atlas assignment without Patch-seq?
5. Could the CA3 anatomical enrichment of SUPT\_0219 in the WMBv1 atlas reflect a sampling or clustering bias, rather than a true anatomical restriction, and might SUPT\_0219 cells occur at lower frequency in CA1 SO?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge\_lth\_cell\_hippocampus\_to\_CS20230722\_SUPT\_0219 | ATLAS\_METADATA, ANNOTATION\_TRANSFER | WEAK / PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hewitt et al. 2021 | [33991454](https://pubmed.ncbi.nlm.nih.gov/33991454/) | Soma location |
