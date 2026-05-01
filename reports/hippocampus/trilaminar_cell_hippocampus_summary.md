# Trilaminar cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Stratum oriens of hippocampus [UBERON:0014548] | [1] |
| Neurotransmitter | GABAergic | — |
| Defining markers | Pvalb, M2R (Chrm2) | — |
| Negative markers | Sst | — |
| Neuropeptides | None documented | — |
| CL term | — | — |

**Direct expression evidence:** Precomputed WMBv1 stats for supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] confirm Pvalb expression (mean 8.74) and Chrm2/M2R detection (mean 4.52), supporting both defining markers at the atlas supertype level. Sst shows low-level expression (mean 2.72) in this supertype; classical trilaminar cells are defined as Sst-negative, which weakens its discriminating power as a strict negative marker at this resolution.

**Node notes:** Stub from cite-traverse (2026-04-10). Well-documented by Somogyi lab (Katona et al. 2017) [1]. Long-range projection cell distinct from hippocampo-septal cell. PV+/M2R+/SOM−.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | — | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | — | 🔴 LOW | GABAergic; Pvalb+; stratum oriens [UBERON:0014548] enrichment | Speculative |

**Total edges:** 1. Relationship type: PARTIAL_OVERLAP.

*(note: No cluster-level (rank 0) edge was resolved. The mapping is to a supertype that contains multiple PV+ interneuron subtypes including PV basket and axo-axonic cells.)*

---

## 0206 Pvalb Gaba_2 · 🔴 LOW

**Supporting evidence**

- NT type: GABAergic — CONSISTENT. The Pvalb Gaba_2 supertype belongs to the Pvalb Gaba subclass, confirming inhibitory identity.
- Soma location: CONSISTENT — 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] is enriched in CA1 stratum oriens (493 cells) and CA3 stratum oriens (152 cells), directly matching the trilaminar cell's canonical soma location in stratum oriens [UBERON:0014548] [1].
- Marker Pvalb: CONSISTENT — precomputed stats mean 8.74 in SUPT_0206, consistent with PV+ immunoreactivity described for trilaminar cells [1].
- Marker M2R (Chrm2): CONSISTENT by precomputed expression (mean 4.52 in SUPT_0206), though Chrm2 is absent from the SUPT_0206 defining marker list. Detection is from precomputed stats only and is not validated as an atlas-level discriminating marker.
- Negative marker Sst: CONSISTENT at the marker-list level — Sst is absent from SUPT_0206 defining markers. Precomputed mean 2.72 indicates low but detectable transcript level (see Concerns).
- Annotation transfer (MapMyCells; local run, default parameters; source: Yao 2021 SSv4 Pvalb subclass, GEO:GSE185862, n=66 HIP cells): SUPT_0206 receives 12/66 Pvalb cells (F1=0.324, target purity=0.800). The PV+ population partially assigning to SUPT_0206 is consistent with the trilaminar cell's Pvalb identity, though this is a weak and indirect signal given the mixed-subtype composition of the source label.

**Marker evidence provenance**

- Pvalb and Chrm2/M2R expression values are atlas precomputed stats (atlas re-analysis method); these are supertype-level means and do not resolve cell-type heterogeneity within the supertype.
- M2R (Chrm2) is detected at mean 4.52 in SUPT_0206. This is consistent with M2R immunoreactivity in PV+ interneurons documented by Katona et al. 2017 [1]. However, Chrm2 does not appear in the atlas marker list for this supertype, so the match is quantitative only and does not confirm cell-type specificity.
- Sst mean 2.72 in SUPT_0206 likely represents a mixture of low-level transcription and genuine co-expression in a subset of cells within the supertype. This level is below what is typically observed in dedicated Sst+ interneuron supertypes, but is not zero.
- The annotation transfer best subclass-level hit is the 051 Pvalb chandelier Gaba subclass (F1=0.588, group purity=0.417, 25 cells), not a stratum oriens-enriched supertype. *(note: this likely reflects the mixed PV subtype composition of the Yao 2021 SSv4 "Pvalb" label — axo-axonic/chandelier cells are well-separated transcriptomically and may dominate the subclass-level assignment. It should not be interpreted as evidence that trilaminar cells are chandelier cells.)*

**Concerns**

- **Supertype heterogeneity (AMBIGUOUS_MAPPING):** SUPT_0206 (Pvalb Gaba_2) is the same supertype assigned to PV basket cells and possibly axo-axonic cells. Trilaminar cells and PV basket cells share Pvalb expression and stratum oriens soma location. No transcriptomic features distinguishing trilaminar cells from other PV+ interneurons are available in atlas metadata. This is the primary obstacle to a higher-confidence mapping.
- **M2R not in atlas marker list (MARKER_NOT_SPECIFIC):** The key discriminating marker M2R (Chrm2) is absent from SUPT_0206 defining markers. Long-range projection identity and the M2R signature that distinguishes trilaminar cells from other PV+ interneurons cannot be confirmed from atlas metadata alone.
- **Long-range projection and physiology unassessable:** The trilaminar cell is classically defined not only by its marker profile but by long-range projections to subiculum and medial septum and a characteristic burst-firing electrophysiological pattern [1]. Neither property is accessible from the WMBv1 atlas metadata.
- **Low-level Sst expression (MARKER_NOT_SPECIFIC):** Sst precomputed mean 2.72 in SUPT_0206. Classical trilaminar cells are Sst-negative, but low-level Sst co-expression in Pvalb interneurons is documented across studies. This does not disqualify the mapping but reduces the power of Sst negativity as a discriminating constraint.
- **Single-study provenance (SINGLE_STUDY):** The classical trilaminar cell definition rests primarily on Katona et al. 2017 [1] (Somogyi lab). Independent transcriptomic characterisation of morphologically identified trilaminar cells from a second group has not been published.
- **Annotation transfer ambiguity:** The source dataset (Yao 2021 SSv4 "Pvalb" subclass, GEO:GSE185862) is a mixed population encompassing PV basket, axo-axonic, bistratified, and potentially trilaminar cells. Subtype resolution from this AT is not achievable without morphological or long-range projection metadata in the source dataset.

**What would upgrade confidence**

- Patch-seq from morphologically confirmed trilaminar cells (identified by long-range projection to subiculum/septum) would yield a definitive transcriptomic profile and allow direct atlas cluster assignment.
- Demonstration that Chrm2-high / Pvalb+ / Sst-low cells within SUPT_0206 form a transcriptomically separable sub-cluster would support subdivision of this supertype.
- A retrograde-labelling experiment from medial septum in Pvalb-Cre mice combined with scRNA-seq would allow disambiguation of trilaminar cells from hippocampo-septal cells and PV basket cells at the transcript level.
- Confirmation that SUPT_0206 or a sub-cluster thereof contains cells with burst-firing physiology (via multimodal atlas or electrophysiology co-registration) would add a corroborating functional constraint.

---

## Eliminated candidates

No UNCERTAIN-confidence edges are present for this node. The single LOW edge to 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] represents the most parsimonious supertype match available given the Pvalb+/Sst−/stratum oriens profile.

---

## Proposed experiments

No proposed experiments are formally recorded in the facts file for this node. The following are inferred from unresolved caveats.

**Patch-seq (morphological–transcriptomic integration)**
- Record from and fill trilaminar cells in acute hippocampal slices; extract cytoplasm for scRNA-seq.
- Expected output: definitive cluster assignment within WMBv1 SUPT_0206 or identification of a sub-cluster.
- Cross-check with: Pvalb mean 8.74, Chrm2 mean 4.52 in SUPT_0206; stratum oriens enrichment [1].

**Retrograde tracing + single-cell transcriptomics**
- Inject retrograde tracer into medial septum or subiculum; FACS-sort labelled neurons from CA1 for scRNA-seq.
- Expected output: transcriptomic identity of long-range projecting PV+ cells; direct comparison against WMBv1 supertype assignments.
- Cross-check with: hippocampo-septal cell (separate node) to resolve trilaminar vs. hippocampo-septal identity.

**smFISH / RNAscope co-detection**
- Co-detect Pvalb, Chrm2, and Sst transcripts in stratum oriens sections to quantify the PV+/M2R+/Sst-low fraction.
- Expected output: estimate of the trilaminar cell proportion among stratum oriens PV+ interneurons; direct comparison against SUPT_0206 precomputed stats.

---

## Open questions

1. Does SUPT_0206 (Pvalb Gaba_2) contain a transcriptomically distinct sub-population corresponding to long-range projecting PV+/M2R+ trilaminar cells, or are trilaminar cells indistinguishable from PV basket cells at current atlas resolution?
2. Is Chrm2/M2R expression sufficiently high and selective within the Pvalb subclass to serve as a transcriptomic discriminator for trilaminar cells in WMBv1?
3. What is the transcriptomic relationship between the trilaminar cell and the hippocampo-septal cell — are these separable at the WMBv1 cluster level, and do they map to different supertypes?
4. Can the low Sst signal (mean 2.72) in SUPT_0206 be attributed to a specific sub-cluster, or is it distributed uniformly across the supertype?

---

## Evidence base

| Edge ID | Evidence types | Supports |
|---|---|---|
| edge_trilaminar_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA (×2), ANNOTATION_TRANSFER | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Katona et al. 2017 | [27997999](https://pubmed.ncbi.nlm.nih.gov/27997999/) | Soma location (stratum oriens); classical type definition; PV+/M2R+/SOM− profile |
