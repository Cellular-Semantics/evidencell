# Trilaminar cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| Soma location | stratum oriens of hippocampus [UBERON:0014548] | [1] |
| NT | GABAergic | — |
| Markers | Pvalb+, M2R (Chrm2)+ | — |
| Negative markers | Sst− | — |

**Node notes:** Stub from cite-traverse (2026-04-10). Well-documented by the Somogyi lab (Katona et al. 2017 [1]). Long-range projection cell distinct from hippocampo-septal cell. PV+/M2R+/SOM−. Pvalb and M2R markers have no individual primary citations on this classical node entry.

**Direct expression evidence:** Precomputed WMBv1 stats for SUPT_0206 [CS20230722_SUPT_0206] confirm Pvalb (mean 8.74) and Chrm2/M2R (mean 4.52), supporting both defining markers at atlas supertype level. Sst shows low-level expression (mean 2.72) in this supertype; classical trilaminar cells are Sst-negative, which weakens its discriminating power as a strict negative marker at this resolution.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | — | 🔴 LOW | Pvalb CONSISTENT · stratum oriens CONSISTENT · M2R CONSISTENT (precomputed only) | Speculative |

1 edge total · relationship type: PARTIAL_OVERLAP.

---

## 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] · 🔴 LOW

### Supporting evidence

- **NT type: CONSISTENT.** Pvalb Gaba_2 belongs to the Pvalb Gaba subclass, confirming inhibitory GABAergic identity.
- **Soma location: CONSISTENT.** SUPT_0206 [CS20230722_SUPT_0206] is enriched in CA1 stratum oriens (493 cells) and CA3 stratum oriens (152 cells), directly matching the trilaminar cell's canonical soma location in stratum oriens [UBERON:0014548] [1].
- **Marker Pvalb: CONSISTENT.** Precomputed stats mean 8.74 in SUPT_0206 [CS20230722_SUPT_0206], consistent with PV+ immunoreactivity for trilaminar cells [1].
- **Marker M2R (Chrm2): CONSISTENT** by precomputed expression (mean 4.52), consistent with M2R immunoreactivity in PV+ interneurons documented by Katona et al. 2017 [1]. Chrm2 is absent from the SUPT_0206 defining marker list — this is a precomputed-stats-only confirmation.
- **Negative marker Sst: CONSISTENT** at the marker-list level — Sst is absent from SUPT_0206 [CS20230722_SUPT_0206] defining markers. Precomputed mean 2.72 indicates low but non-zero transcript level (see Concerns).
- **Annotation transfer (GEO:GSE185862).** MapMyCells local run, default parameters, source: Yao 2021 SSv4 Pvalb subclass (n=66 HIP cells): SUPT_0206 receives 12/66 Pvalb cells (F1=0.324, purity=0.800). PARTIAL: the SSv4 Pvalb label is a mixed population and trilaminar cell identity cannot be confirmed from this AT alone.

### Marker evidence provenance

- **Pvalb:** No dedicated primary citation on the classical node entry (refs field empty). Katona et al. 2017 [1] is the primary characterisation study. Method: IHC. Cell-type specificity based on morphological reconstruction (long-range projection soma in stratum oriens). Precomputed stats (mean 8.74) confirm atlas-side expression.
- **M2R (Chrm2):** No dedicated primary citation on the classical node entry (refs field empty). Katona et al. 2017 [1] documents M2R immunoreactivity in PV+ SO interneurons. Chrm2 is detected at mean 4.52 in SUPT_0206 from precomputed stats but does not appear in the atlas defining marker list, so the match is quantitative only and does not confirm cell-type specificity at atlas resolution.
- **Negative marker Sst:** Sst mean 2.72 in SUPT_0206 likely represents low-level transcription or heterogeneous co-expression in a subset of cells. This is below typical Sst+ interneuron supertype levels (e.g., Sst Gaba supertypes show means >10) but is not zero. The single-study provenance of the Sst-negative assertion is a gap — no independent citation is attached.
- **Annotation transfer note:** The AT best subclass-level hit is 051 Pvalb chandelier Gaba (F1=0.588, 25 cells), not a stratum oriens-enriched supertype. *(note: this likely reflects the mixed PV subtype composition of the Yao 2021 SSv4 "Pvalb" label — axo-axonic/chandelier cells are well-separated transcriptomically and may dominate the subclass-level assignment. It should not be interpreted as evidence that trilaminar cells are chandelier cells.)*

### Concerns

- **Supertype heterogeneity (AMBIGUOUS_MAPPING).** SUPT_0206 [CS20230722_SUPT_0206] is also the candidate supertype for PV basket cells, and possibly axo-axonic cells. Trilaminar cells and PV basket cells share Pvalb expression and stratum oriens soma location. No transcriptomic features distinguishing trilaminar cells from other PV+ interneurons are available in atlas metadata. This is the primary obstacle to higher-confidence mapping.
- **M2R not in atlas marker list (MARKER_NOT_SPECIFIC).** The key discriminating marker M2R (Chrm2) is absent from SUPT_0206 [CS20230722_SUPT_0206] defining markers. Long-range projection identity and the M2R signature cannot be confirmed from atlas metadata alone.
- **Long-range projection and physiology unassessable.** Trilaminar cells are classically defined not only by marker profile but by long-range projections to subiculum and medial septum and characteristic burst-firing electrophysiology [1]. Neither property is accessible from atlas metadata.
- **Low-level Sst expression (MARKER_NOT_SPECIFIC).** Sst precomputed mean 2.72. Classical trilaminar cells are Sst-negative, but low-level Sst co-expression in Pvalb interneurons is known. Does not disqualify the mapping but reduces the power of Sst negativity as a discriminating constraint.
- **Single-study provenance (SINGLE_STUDY).** Classical trilaminar cell definition rests primarily on Katona et al. 2017 [1]. Independent transcriptomic characterisation from a second group has not been published.

### What would upgrade confidence

- **Patch-seq from morphologically confirmed trilaminar cells** (identified by long-range projection to subiculum/septum) would yield a definitive transcriptomic profile and allow direct atlas cluster assignment. Expected output: AnnotationTransferEvidence or LiteratureEvidence on this edge.
- **Demonstration that Chrm2-high/Pvalb+/Sst-low cells within SUPT_0206 form a transcriptomically separable sub-cluster** would support subdivision of this supertype and provide a cluster-level mapping target.
- **Retrograde labelling from medial septum in Pvalb-Cre mice + scRNA-seq** would disambiguate trilaminar cells from hippocampo-septal cells and PV basket cells at the transcript level.

---

## Proposed experiments

### Patch-seq (morphological–transcriptomic integration)
- **What:** Record and fill trilaminar cells in acute hippocampal slices; extract cytoplasm for scRNA-seq
- **Target:** Definitive cluster assignment within WMBv1 SUPT_0206 [CS20230722_SUPT_0206] or identification of a sub-cluster
- **Expected output:** LiteratureEvidence or AnnotationTransferEvidence on this edge; Pvalb mean 8.74, Chrm2 mean 4.52 in SUPT_0206 are the expected molecular reference points
- **Resolves:** Whether trilaminar cells are separable from PV basket cells at current atlas resolution

### Retrograde tracing + single-cell transcriptomics
- **What:** Inject retrograde tracer into medial septum or subiculum; FACS-sort labelled neurons from CA1 for scRNA-seq
- **Target:** Transcriptomic identity of long-range projecting PV+ cells; comparison against WMBv1 supertype assignments
- **Expected output:** Direct evidence for trilaminar cell cluster identity; resolves trilaminar vs. hippocampo-septal ambiguity
- **Resolves:** Open question 1

### smFISH / RNAscope co-detection
- **What:** Co-detect Pvalb, Chrm2, and Sst transcripts in stratum oriens sections
- **Target:** Quantify PV+/M2R+/Sst-low fraction; compare against SUPT_0206 [CS20230722_SUPT_0206] precomputed stats
- **Expected output:** Estimate of trilaminar cell proportion among stratum oriens PV+ interneurons
- **Resolves:** Open question 4

---

## Open questions

1. Does SUPT_0206 [CS20230722_SUPT_0206] contain a transcriptomically distinct sub-population corresponding to long-range projecting PV+/M2R+ trilaminar cells, or are trilaminar cells indistinguishable from PV basket cells at current atlas resolution?
2. Is Chrm2/M2R expression sufficiently high and selective within the Pvalb subclass to serve as a transcriptomic discriminator for trilaminar cells in WMBv1?
3. What is the transcriptomic relationship between the trilaminar cell and the hippocampo-septal cell — are these separable clusters at any WMBv1 taxonomy level?
4. Can the low Sst signal (mean 2.72) in SUPT_0206 [CS20230722_SUPT_0206] be attributed to a specific sub-cluster, or is it distributed uniformly across the supertype?

---

## Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA — supertype marker and anatomy comparison | PARTIAL |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA — precomputed stats cross-check (Pvalb=8.74, Chrm2=4.52, Sst=2.72) | PARTIAL |
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ANNOTATION_TRANSFER — MapMyCells · GEO:GSE185862 · Pvalb subclass n=66 HIP cells | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | soma location; PV+/M2R+/SOM− profile; classical type definition |
