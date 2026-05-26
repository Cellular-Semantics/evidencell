# Low-threshold high-Ih (LTH) cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum oriens of hippocampus [UBERON:0014548] (CA1) | [1] |
| NT | GABAergic | — |
| Markers | Sst+ | [1] |

**Node notes:** Stub from cite-traverse (2026-04-10). THIN EVIDENCE — single study (Hewitt et al. 2021 [1]) using physiological clustering of SST-Cre Ai14 cells in CA1 acute slices. The LTH cell is characterised by strong spike frequency adaptation and a prominent hyperpolarisation-activated cation current (I_h). No molecular markers beyond SST-Cre labelling have been reported; transcriptomic identity is entirely unknown. May overlap with oriens-oriens or other SST+ subtypes.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | — | 0219 Sst Gaba_6 [CS20230722_SUPT_0219] | — | ⚪ UNCERTAIN | Sst CONSISTENT · location DISCORDANT (CA3-enriched, no CA1 SO) | Eliminated |

1 edge total · relationship type: UNCERTAIN. No MODERATE or LOW mappings were established.

---

## Eliminated candidates

### 0219 Sst Gaba_6 [CS20230722_SUPT_0219] — ⚪ UNCERTAIN

The primary disqualifying signal is that SUPT_0219 [CS20230722_SUPT_0219] is CA3-enriched with no CA1 stratum oriens representation, while the LTH cell was characterised exclusively in CA1 stratum oriens. An additional concern is that the LTH cell is defined exclusively by electrophysiology, with no molecular identity established beyond SST-Cre driver labelling.

**Supporting evidence**

- NT type consistent: LTH cell is GABAergic; SUPT_0219 belongs to the 053 Sst Gaba subclass, confirming GABAergic identity.
- Sst marker consistent: LTH cells are SST-Cre labelled; SUPT_0219 [CS20230722_SUPT_0219] carries Sst as a defining marker (precomputed mean 10.17).
- Annotation transfer (Yao 2021, GEO:GSE185862, n=273 SSv4 Sst HIP cells): subclass-level correspondence strongly confirmed (265/273 cells to Sst Gaba subclass; F1=0.983). At supertype level, SUPT_0219 was the dominant target (161/273 cells, F1=0.759, purity=0.964).

**Marker evidence provenance**

- **Sst (via SST-Cre Ai14):** SST-Cre labels a broad population of Sst interneurons across all hippocampal Sst subtypes. No single-cell transcriptomics, ISH, or quantitative gene-expression measurement was performed on LTH cells specifically. The Sst marker assignment reflects Cre-driver breadth, not confirmed high-level Sst expression at single-cell resolution.
- **Annotation transfer source (GEO:GSE185862):** Heterogeneous Sst interneuron population. Supertype-level F1=0.759 and group purity=0.626 confirm SUPT_0219 as the plurality target but not dominant. Subtype resolution requires a source dataset with morphologically or physiologically identified Sst interneuron labels.

**Concerns**

- **Discordant anatomy (primary concern — DISCORDANT).** SUPT_0219 [CS20230722_SUPT_0219] is CA3-enriched: 305 CA3 stratum oriens cells, no CA1 stratum oriens. LTH cells were characterised exclusively in CA1 stratum oriens [UBERON:0014548]. *(note: CA3 and CA1 are adjacent hippocampal subfields, but the complete absence of CA1 SO cells in SUPT_0219 is a stronger counter-evidence than a mere registration boundary error would produce.)*
- **Electrophysiology-only definition (ELECTROPHYSIOLOGY_ONLY_DEFINITION).** LTH cell is defined solely by physiological clustering in a single study. No morphological reconstruction or molecular profiling beyond SST-Cre labelling was performed. Whether the LTH type constitutes a transcriptomically distinct entity is entirely unknown.
- **Potential OLM overlap (AMBIGUOUS_MAPPING).** LTH cells share key features with OLM cells (SST+, CA1 stratum oriens soma). If LTH and OLM cells are transcriptomically indistinguishable, the correct supertype target would be SUPT_0216 [CS20230722_SUPT_0219 notes reference SUPT_0216] rather than SUPT_0219. The current assignment to SUPT_0219 is a placeholder pending molecular characterisation.
- **Single-study, single-lab evidence (SINGLE_STUDY).** Classification stability across datasets, recording conditions, and mouse ages is unknown.
- **Mixed annotation transfer source.** AT group purity 0.626 at supertype level confirms Yao 2021 Sst HIP cells are heterogeneous at supertype level.

**What would upgrade confidence**

- A MODERATE edge would require: (a) transcriptomic profiling (Patch-seq or scRNA-seq) of physiologically identified LTH cells confirming assignment to SUPT_0219, and (b) resolution of the anatomical discordance — either by revised spatial atlas data showing SUPT_0219 in CA1 SO, or by demonstrating that LTH cells share the molecular profile of SUPT_0219 despite the regional bias.
- A HIGH edge would additionally require independent replication of the LTH physiological classification and morphological confirmation distinguishing LTH from OLM cells.

---

## Proposed experiments

### Patch-seq (highest priority)
- **What:** Patch-seq on physiologically identified LTH cells in SST-Cre Ai14 CA1 acute slices: record whole-cell patch-clamp, confirm LTH physiology (strong spike-frequency adaptation + prominent I_h sag), harvest cell contents for scRNA-seq
- **Target:** Direct transcriptomic assignment to WMBv1 supertypes; resolve SUPT_0219 [CS20230722_SUPT_0219] vs. SUPT_0216 ambiguity
- **Expected output:** AnnotationTransferEvidence on this edge (or a revised edge to the correct supertype)
- **Resolves:** Open questions 1, 2

### Multiplex in situ hybridisation
- **What:** smFISH/RNAscope panel in CA1 stratum oriens using Sst, Nos1, Calb1, Npy, Cck; Sst/Nos1 co-expression marks OLM cells; differential expression would provide a molecular discriminator for LTH cells
- **Target:** Identify a molecular signature distinguishing LTH from OLM cells in CA1 SO tissue
- **Expected output:** LiteratureEvidence identifying discriminating markers for LTH cells; informs whether SUPT_0219 or SUPT_0216 better captures LTH cells
- **Resolves:** Open question 4

### Physiological replication
- **What:** Independent physiological classification (second lab, different recording conditions, adult vs. juvenile mice) to confirm the LTH cluster is a stable functional type
- **Target:** Reproducibility of LTH classification
- **Expected output:** Stabilised classical node definition for LTH cell; independent study citation
- **Resolves:** Open question 3

---

## Open questions

1. Does the LTH cell constitute a transcriptomically distinct type, or is it a physiological variant within an existing Sst interneuron type such as OLM?
2. Which WMBv1 supertype corresponds to the CA1 stratum oriens Sst interneuron population: SUPT_0219 [CS20230722_SUPT_0219] (CA3-enriched in the atlas) or SUPT_0216 (OLM-associated)?
3. Is the LTH physiological classification reproducible across independent datasets, recording conditions, and animal ages?
4. Do LTH cells express Nos1, Calb1, or other Sst-subtype discriminators that would distinguish them molecularly from OLM cells?
5. Could the CA3 anatomical enrichment of SUPT_0219 [CS20230722_SUPT_0219] in the WMBv1 atlas reflect a sampling or clustering bias rather than true anatomical restriction?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_lth_cell_hippocampus_to_CS20230722_SUPT_0219 | ATLAS_METADATA — supertype marker and anatomy comparison | WEAK |
| edge_lth_cell_hippocampus_to_CS20230722_SUPT_0219 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Sst subclass n=273 HIP cells | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Hewitt et al. 2021 | [33991454](https://pubmed.ncbi.nlm.nih.gov/33991454/) | soma location; LTH physiological characterisation |
