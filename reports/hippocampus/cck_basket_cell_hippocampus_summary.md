# Cholecystokinin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `/Users/ar38/Documents/GitHub/evidencell/kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | basket cell (CL:0000118) — BROAD mapping | — |
| Soma location | stratum pyramidale [UBERON:0005401] (CA1 stratum pyramidale) | [1][2][3][4] |
| Neurotransmitter | GABAergic | [3] |
| Defining markers | Cck, Cnr1, Vglut3 | [5][2][4][6][7] (Cck); [5] (Cnr1); unsourced (Vglut3) |
| Negative markers | Pvalb | — |
| Neuropeptides | Cck | [5] |

**Notes from curation record:** CCK cells are remarkably diverse, extending beyond the Sncg transcriptomic class. Activity is thought to inversely scale with PV cell activity. CCK+ basket cells have never been observed to receive direct monosynaptic excitation from local CA1 pyramidal cells.

---

## Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | Vip Gaba | — | ⚪ UNCERTAIN | NT consistent; Cck/Cnr1 absent from supertype markers | Eliminated |

**Total:** 1 edge · relationship type: UNCERTAIN.

---

## Eliminated candidates

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · ⚪ UNCERTAIN

This candidate was identified by location overlap in CA1 and GABA neurotransmitter type, but was eliminated at the supertype level because the three canonical CCK basket cell markers (Cck, Cnr1, Vglut3) are all absent from the atlas supertype metadata.

**Supporting evidence:**

- Neurotransmitter type is CONSISTENT: the atlas supertype is classified as GABA, matching the GABAergic identity of CCK basket cells [atlas metadata].
- Hippocampal spatial distribution is broadly present in this supertype: CA1 SO (24 cells), CA1 pyramidal layer (11 cells), CA1 SR (26 cells), CA3 SO (25 cells), CA3 pyramidal layer (23 cells), CA3 SR (17 cells). The presence of cells in perisomatic positions (pyramidal layers) is compatible with basket cell morphology. *(note: perisomatic targeting is a defining anatomical feature of basket cells; somatic inhibition in stratum pyramidale is the hallmark of this cell class.)*
- Absence of Pvalb in the supertype marker set is CONSISTENT with CCK basket cell identity: PV basket cells and CCK basket cells are the two canonical perisomatic inhibitory populations and are mutually exclusive at the marker level. Precomputed expression stats confirm very low Pvalb expression in this supertype (mean: 0.09).
- Cnr1 precomputed expression mean (10.58) in this supertype is notably elevated — the highest of any marker assessed — which provides a tentative signal consistent with CCK basket cell identity, even though Cnr1 is not listed among the atlas supertype's defining markers.

**Marker evidence provenance:**

- **Cck** (defining marker and neuropeptide): Multi-source evidence at both protein and transcript levels. Protein level: Katona et al. 1999 [5] confirmed CCK+ identity in basket cells by co-immunostaining with CB1 receptor and morphological characterisation (basket cell terminals surrounding pyramidal somata and proximal dendrites). 85.6% of CB1-positive interneurons were CCK+, and 96.9% of all CCK+ interneurons expressed CB1, establishing a near-complete co-identity between CCK and CB1 in this population [5]. Transcript level: Fuzik et al. 2015 [7], Fasano et al. 2017 [2], Contreras et al. 2019 [4], and Huang et al. 2014 [6] all cite CCK as a defining transcript marker. In the atlas supertype [CS20230722_SUPT_0179], Cck is not listed as a defining marker and the precomputed expression mean is 1.36 — low. Source-side evidence for Cck is well-established; target-side expression is not corroborated by supertype metadata.
- **Cnr1** (defining marker): Evidence is protein level (IHC), with high morphological specificity — Katona et al. 1999 [5] localised CB1/Cnr1 to CCK-positive basket cell terminals surrounding pyramidal somata, and demonstrated absence from PV basket terminals in identical locations. This co-localisation study directly confirmed CCK basket cell identity by co-staining. Precomputed expression stats for the atlas supertype show a mean of 10.58 for Cnr1 — the strongest expression signal of any assessed marker — yet Cnr1 is not named in the supertype's defining markers. This discrepancy may reflect atlas marker selection criteria (e.g. Cnr1 is broadly expressed in CGE interneurons and therefore not discriminative at the supertype level), but it cannot be resolved without cluster-level transcriptomic data.
- **Vglut3** (defining marker): Listed in the curation record without a source citation. This is an unsourced marker. Precomputed expression stats show a mean of 0.42 in this supertype. *(note: Vglut3 expression in hippocampal interneurons is documented in the literature and is most commonly associated with CCK-expressing interneurons, particularly those with axon-initial-segment-targeting or dendrite-targeting morphology rather than classical basket cell morphology — this distinction matters for interpreting whether Vglut3 is appropriate as a CCK basket cell marker specifically.)* A source citation is required before this marker can be used in property comparisons.
- **Pvalb** (negative marker): Unsourced as a negative marker in the curation record. Pvalb negativity in CCK basket cells is well-established contextually: Katona et al. 1999 [5] explicitly showed that CB1-positive (CCK) basket cell terminals are in locations where PV basket terminals are CB1-negative, establishing mutual exclusivity at the level of terminal identity. Whissell et al. 2015 [3] and Rivera et al. 2014 [1] are cited for soma location rather than Pvalb negativity. A direct citation for Pvalb as a negative marker would strengthen the classical node definition. Precomputed expression stats confirm a mean of 0.09 in this atlas supertype, consistent with expectation for a non-PV population.

**Concerns:**

- The atlas supertype identity is "Vip Gaba" — this is the primary reason for elimination. CCK basket cells in hippocampus are CGE-derived (as are Vip interneurons) and a subset may co-express Vip, but the defining transcriptomic identity of hippocampal CCK basket cells is not expected to be Vip-primary. Mapping to a Vip-defined supertype implies either (a) this supertype contains a mixed CGE population with CCK basket cells as a minor component, or (b) the Vip subclass captures a CCK-expressing CGE interneuron subtype that classical morphological literature has not distinguished from the Vip population.
- Cck is absent from the supertype's defining marker list (precomputed mean 1.36), making it impossible to confirm Cck identity from atlas metadata alone. This is the single most critical unresolved alignment gap.
- Cnr1 is absent from the supertype's defining marker list despite a high precomputed mean (10.58). This discrepancy is noted but cannot be resolved at the supertype level.
- Vglut3 is neither confirmed by the atlas (precomputed mean 0.42; not in defining markers) nor properly sourced on the classical node. Both gaps must be addressed before this marker can inform mapping decisions.
- Cell counts for this supertype in CA1 pyramidal layer (11 cells) are sparse relative to other hippocampal compartments, raising the question of whether basket cell soma positions are underrepresented within this larger, more dispersed supertype.
- The entire mapping rests on location overlap and inferred CGE origin. Without Cck or Cnr1 in the atlas supertype's named markers, this is a circumstantial candidate only.

**What would upgrade confidence:**

- Patch-seq or multiplexed single-cell RNA-seq of morphologically or physiologically identified CCK basket cells in CA1, with explicit Cck, Cnr1, and Vip co-expression data, would allow direct comparison to the atlas supertype marker profile and could reveal whether CCK basket cells map to a specific cluster within the Vip Gaba supertype.
- Cluster-level (rather than supertype-level) transcriptomic data for individual clusters within Vip Gaba [CS20230722_SUPT_0179] may reveal whether one or more child clusters show elevated Cck and Cnr1 simultaneously — this would enable re-evaluation at higher resolution.
- IHC co-localisation of Vip and CCK in identified basket cells (morphological confirmation) would establish whether the Vip Gaba supertype is a plausible transcriptomic home for CCK basket cells, or whether CCK basket cells form a separate transcriptomic identity.
- A source citation for Vglut3 as a CCK basket cell marker would strengthen the classical node definition and allow meaningful comparison to atlas precomputed expression (currently 0.42).

---

## Proposed experiments

### Transcriptomics / patch-seq
- Patch-seq of physiologically characterised CCK basket cells in CA1 to determine whether they map to the Vip Gaba supertype or to a distinct transcriptomic cluster with high Cck and Cnr1 expression.
- Single-cell RNA-seq with explicit readout of Cck, Cnr1, Vip, and Vglut3 co-expression in CA1 stratum pyramidale cells to test whether CCK basket cells form a distinct transcriptomic identity separate from the core Vip interneuron population.

### Immunohistochemistry / protein-level validation
- IHC co-staining of Vip and CCK (or CB1/Cnr1) in CA1 to quantify what fraction of CCK-positive basket cells co-express Vip — this would directly test the plausibility of the Vip Gaba subclass assignment.
- Targeted IHC for Vglut3 in morphologically confirmed CCK basket cells (e.g. cells reconstructed after patch-clamp to confirm basket cell morphology) to validate or refute the unsourced Vglut3 marker listing.

### Atlas resolution
- Query child clusters within the WMBv1 Vip Gaba supertype [CS20230722_SUPT_0179] for Cck and Cnr1 expression statistics to identify whether any cluster-level population shows the expected CCK basket cell marker combination at higher specificity.

---

## Open questions

1. Do CCK basket cells in hippocampus form a coherent transcriptomic cluster in WMBv1, or are they distributed across multiple supertypes (e.g. Vip Gaba, Sncg, or other CGE-derived classes)? The diversity of CCK interneurons noted in the curation record makes this an important unresolved question.
2. What fraction of CCK+ perisomatic interneurons in CA1 co-express Vip? Is Vip co-expression a consistent feature of CCK basket cells or a marker of a morphologically distinct subpopulation?
3. Is Vglut3 a reliable marker of CCK basket cells specifically, or does it mark a broader or different CCK interneuron subtype (e.g. axon-initial-segment-targeting interneurons)? What is the supporting citation?
4. Why is Cnr1 not listed as a defining marker in the Vip Gaba atlas supertype despite a high precomputed mean (10.58)? Does this reflect atlas marker selection criteria, or does it suggest Cnr1 is broadly expressed across multiple CGE-derived supertypes and therefore not discriminative?
5. Are the sparse cell counts for this supertype in CA1 pyramidal layer (11 cells) an artefact of sampling density in the WMBv1 dataset, or do they indicate that basket cell soma positions are genuinely underrepresented within this atlas supertype?

---

## Evidence base table

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | PARTIAL |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Rivera et al. 2014 | [25018703](https://pubmed.ncbi.nlm.nih.gov/25018703/) | Soma location |
| [2] | Fasano et al. 2017 | [28559797](https://pubmed.ncbi.nlm.nih.gov/28559797/) | Soma location; Cck marker |
| [3] | Whissell et al. 2015 | [26441554](https://pubmed.ncbi.nlm.nih.gov/26441554/) | Soma location; GABAergic NT |
| [4] | Contreras et al. 2019 | [31297048](https://pubmed.ncbi.nlm.nih.gov/31297048/) | Soma location; Cck marker |
| [5] | Katona et al. 1999 | [10341254](https://pubmed.ncbi.nlm.nih.gov/10341254/) | Cck marker; Cnr1 marker; Cck neuropeptide |
| [6] | Huang et al. 2014 | [24533597](https://pubmed.ncbi.nlm.nih.gov/24533597/) | Cck marker |
| [7] | Fuzik et al. 2015 | [26689544](https://pubmed.ncbi.nlm.nih.gov/26689544/) | Cck marker |
