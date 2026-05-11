# Cholecystokinin-positive basket cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | basket cell (CL:0000118) — BROAD mapping | — |
| Soma location | Stratum pyramidale [UBERON:0005401] (CA1) | [1] [2] [3] [4] |
| Neurotransmitter | GABAergic | [3] |
| Defining markers | Cck, Cnr1, Vglut3 | Cck: [5] [2] [4] [6] [7]; Cnr1: [5]; Vglut3: unsourced |
| Negative markers | Pvalb | — |
| Neuropeptides | Cck | [5] |

> "Most CB + 1 terminals surrounding the somata and proximal dendrites of pyramidal neurons were cholecystokinin + (CCK) GABAergic interneurons (basket cells) and, to a lower extent, calbindin D-28k + GABAergic interneurons (Katona et al., 1999) (Marsicano et al., 1999)(Tsou et al., 1999). However, parvalbumin + GABAergic interneuron terminals localized in pyramidal cell layers were negative for CB 1 (Katona et al., 1999)(Marsicano et al., 1999)"
> — Rivera et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 10540334_418c51dd -->

> "To understand the functional significance and mechanisms of action in the CNS of endogenous and exogenous cannabinoids, it is crucial to identify the neural elements that serve as the structural substrate of these actions. We used a recently developed antibody against the CB1 cannabinoid receptor to study this question in hippocampal networks. Interneurons with features typical of basket cells showed a selective, intense staining for CB1 in all hippocampal subfields and layers. Most of them (85.6%) contained cholecystokinin (CCK), which corresponded to 96.9% of all CCK-positive interneurons, whereas only 4.6% of the parvalbumin (PV)- containing basket cells expressed CB1. Accordingly, electron microscopy revealed that CB1-immunoreactive axon terminals of CCK- containing basket cells surrounded the somata and proximal dendrites of pyramidal neurons, whereas PV-positive basket cell terminals in similar locations were negative for CB1. The synthetic cannabinoid agonist WIN 55,212-2 (0.01–3 μm) reduced dose- dependently the electrical field stimulation-induced [3H]GABA release from superfused hippocampal slices, with an EC50 value of 0.041 μm. Inhibition of GABA release by WIN 55,212-2 was not mediated by inhibition of glutamatergic transmission because the WIN 55,212-2 effect was not reduced by the glutamate blockers AP5 and CNQX. In contrast, the CB1 cannabinoid receptor antagonist SR 141716A (1 μm) prevented this effect, whereas by itself it did not change the outflow of [3H]GABA. These results suggest that cannabinoid-mediated modulation of hippocampal interneuron networks operate largely via presynaptic receptors on CCK-immunoreactive basket cell terminals. Reduction of GABA release from these terminals is the likely mechanism by which both endogenous and exogenous CB1 ligands interfere with hippocampal network oscillations and associated cognitive functions."
> — Katona et al. 1999, Classical Functional and Morphological Interneuron Types · [5] <!-- quote_key: 480205_62cd73ae -->

> "Cholecystokinin (CCK)- and parvalbumin (PV)-expressing neurons constitute the two major populations of perisomatic GABAergic neurons in the cortex and the hippocampus. As CCK- and PV-GABA neurons differ in an array of morphological, biochemical and electrophysiological features, it has been proposed that they form distinct inhibitory ensembles which differentially contribute to network oscillations and behavior. However, the relationship and balance between CCK- and PV-GABA neurons in the inhibitory networks of the brain is currently unclear as the distribution of these cells has never been compared on a large scale. Here, we systemically investigated the distribution of CCK- and PV-GABA cells across a wide number of discrete forebrain regions using an intersectional genetic approach. Our analysis revealed several novel trends in the distribution of these cells. While PV-GABA cells were more abundant overall, CCK-GABA cells outnumbered PV-GABA cells in several subregions of the hippocampus, medial prefrontal cortex and ventrolateral temporal cortex. Interestingly, CCK-GABA cells were relatively more abundant in secondary/ association areas of the cortex (V2, S2, M2, and AudD/AudV) than they were in corresponding primary areas (V1, S1, M1, and Aud1). The reverse trend was observed for PV-GABA cells. Our findings suggest that the balance between CCK- and PV-GABA cells in a given cortical region is related to the type of processing that area performs; inhibitory networks in the secondary cortex tend to favor the inclusion of CCK-GABA cells more than networks in the primary cortex. The intersectional genetic labeling approach employed in the current study expands upon the ability to study molecularly defined subsets of GABAergic neurons. This technique can be applied to the investigation of neuropathologies which involve disruptions to the GABAergic system, including schizophrenia, stress, maternal immune activation and autism."
> — Contreras et al. 2019, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 16859318_009e9f36 -->

**Notes.** CCK cells are remarkably diverse, extending beyond the Sncg transcriptomic class. Activity is thought to inversely scale with PV cell activity. CCK+ basket cells have never been observed to receive direct monosynaptic excitation from local CA1 pyramidal cells.

---

## Mapping candidates

| Rank | WMBv1 cluster / supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] | 1,723 | 🟠 LOW | CGE-derived; Cck.Cxcl14.Vip AT F1=0.768, gp=0.951 (PARTIAL); Cck/Cnr1 absent from supertype markers | Best current candidate |
| — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | — | ⚪ UNCERTAIN | NT CONSISTENT; Cck/Cnr1 absent from supertype markers; contradicted by SUPT_0187 AT | Eliminated |

Total: 2 edges.

---

## 0187 Sncg Gaba_3 [CS20230722_SUPT_0187] · 🟠 LOW

### Supporting evidence

- **Annotation transfer (GEO:GSE99888, Cck.Cxcl14.Vip — PARTIAL).** Harris 2018 Class Cck.Cxcl14.Vip (CCK+/Cxcl14+/Vip+ CA1 inhibitory cluster, n=72 cells in the 3,663-cell dataset) maps to [CS20230722_SUPT_0187] Sncg Gaba_3 with F1=0.768 and group_purity=0.951 at SUPERTYPE level. Group_purity=0.951 means 95.1% of the Cck.Cxcl14.Vip Harris cells concentrate at a single supertype — a strong directional signal. This is the CCK-expressing Harris cluster with the strongest directional signal to any single WMBv1 supertype. Consistent with Fuzik et al. 2015 (PMID:26689544) and Saunders et al. 2024 (PMID:38840081) classifying CCK+ cells within the Sncg transcriptomic class.

**Concerns and caveats:**

- **Source label not morphologically confirmed.** Cck.Cxcl14.Vip is a Harris 2018 Class label (n=72 cells), not labelled by basket cell morphology or electrophysiology. The mapping reflects the transcriptomic destination of Cck+/Cxcl14+/Vip+ CA1 cells in an unbiased CA1 interneuron dataset. Whether these cells are CCK basket cells specifically (versus other Cck+ interneuron morphotypes) is not established by this AT run alone.
- **Marker discordance at supertype.** Cck and Cnr1 (canonical CCK basket cell markers) are not listed as defining markers of SUPT_0187 in atlas metadata. This limits confidence in the mapping from atlas-metadata evidence alone; the AT evidence is the primary support.
- **Sncg vs. Vip contradiction.** The existing UNCERTAIN edge (to Vip Gaba_7) was based on atlas metadata from a location+GABA match with Cnr1 signal. The Harris AT data redirects to the Sncg class instead — consistent with CCK interneurons being classified within the Sncg transcriptomic clade in recent atlas analyses. The SUPT_0179 edge should be considered superseded by this AT-supported result, but the Vip Gaba_7 edge is retained pending expert review.

**What would upgrade confidence:**

- Patch-seq or multiplexed single-cell RNA-seq of morphologically confirmed CCK basket cells in CA1, with explicit mapping onto WMBv1. Target: F1 ≥ 0.70 at CLUSTER level within SUPT_0187 or a child cluster. Would distinguish basket cell morphotype from other Cck+ CGE interneuron types.
- Cluster-level AT using a Cck-Cre or Cnr1-Cre CA1 dataset to resolve which SUPT_0187 child clusters carry CCK basket cell identity.

---

## Eliminated candidates

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · ⚪ UNCERTAIN

This candidate was identified by location overlap in CA1 and GABA neurotransmitter type, but was eliminated at the supertype level because the three canonical CCK basket cell markers (Cck, Cnr1, Vglut3) are all absent from the atlas supertype metadata.

**Supporting evidence**

- Neurotransmitter type is CONSISTENT: the atlas supertype is classified as GABA, matching the GABAergic identity of CCK basket cells [atlas metadata].
- Hippocampal spatial distribution is broadly present: CA1 SO (24 cells), CA1 pyramidal layer (11 cells), CA1 SR (26 cells), CA3 SO (25 cells), CA3 pyramidal layer (23 cells), CA3 SR (17 cells). Perisomatic locations (pyramidal layers) are compatible with basket cell morphology. *(note: perisomatic targeting is a defining anatomical feature of basket cells; somatic inhibition in stratum pyramidale is the hallmark of this cell class.)*
- Absence of Pvalb in the supertype marker set is CONSISTENT with CCK basket cell identity: PV basket cells and CCK basket cells are the two canonical perisomatic inhibitory populations and are mutually exclusive at the marker level. Precomputed expression stats confirm very low Pvalb expression (mean: 0.09).
- Cnr1 precomputed expression mean (10.58) is notably elevated — the highest of any marker assessed — providing a tentative signal consistent with CCK basket cell identity, even though Cnr1 is not listed among the atlas supertype's defining markers.

**Marker evidence provenance**

- **Cck** (defining marker and neuropeptide): Multi-source evidence at both protein and transcript levels. Katona et al. 1999 [5] confirmed CCK+ identity in basket cells by co-immunostaining with CB1 receptor and morphological characterisation. 85.6% of CB1-positive interneurons were CCK+, and 96.9% of all CCK+ interneurons expressed CB1, establishing a near-complete co-identity between CCK and CB1. Fasano et al. 2017 [2], Contreras et al. 2019 [4], Huang et al. 2014 [6], and Fuzik et al. 2015 [7] provide additional transcript-level support. In the atlas supertype [CS20230722_SUPT_0179], Cck is not listed as a defining marker and the precomputed expression mean is 1.36 — low. Source-side evidence for Cck is well-established; target-side expression is not corroborated by supertype metadata.
- **Cnr1** (defining marker): Evidence is protein level (IHC) from Katona et al. 1999 [5], which localised CB1/Cnr1 to CCK-positive basket cell terminals and demonstrated absence from PV basket terminals. Precomputed expression stats show a mean of 10.58 for Cnr1 — the strongest expression signal of any assessed marker — yet Cnr1 is not named in the supertype's defining markers. This discrepancy may reflect atlas marker selection criteria but cannot be resolved without cluster-level data.
- **Vglut3** (defining marker): Listed in the curation record without a source citation. Precomputed expression stats show a mean of 0.42 in this supertype. *(note: Vglut3 expression in hippocampal interneurons is documented in the literature and is most commonly associated with CCK-expressing interneurons, but the specific association with classical basket cell morphology requires a direct source citation before this marker can inform property comparisons.)*
- **Pvalb** (negative marker): Unsourced as a negative marker in the curation record. Katona et al. 1999 [5] showed that CB1-positive (CCK) basket cell terminals are in locations where PV basket terminals are CB1-negative, establishing mutual exclusivity. Precomputed expression stats confirm a mean of 0.09, consistent with expectation for a non-PV population.

**Concerns**

- The atlas supertype identity is "Vip Gaba" — this is the primary reason for elimination. CCK basket cells in hippocampus are CGE-derived (as are Vip interneurons) and a subset may co-express Vip, but the defining transcriptomic identity of hippocampal CCK basket cells is not expected to be Vip-primary. Mapping to a Vip-defined supertype implies either (a) this supertype contains a mixed CGE population with CCK basket cells as a minor component, or (b) the Vip subclass captures a CCK-expressing CGE interneuron subtype that classical morphological literature has not distinguished from the Vip population.
- Cck is absent from the supertype's defining marker list (precomputed mean 1.36), making it impossible to confirm Cck identity from atlas metadata alone.
- Cnr1 is absent from the supertype's defining marker list despite a high precomputed mean (10.58). This discrepancy is noted but cannot be resolved at the supertype level.
- Vglut3 is neither confirmed by the atlas (precomputed mean 0.42; not in defining markers) nor properly sourced on the classical node. Both gaps must be addressed before this marker can inform mapping decisions.
- Cell counts for this supertype in CA1 pyramidal layer (11 cells) are sparse relative to other hippocampal compartments.
- The entire mapping rests on location overlap and inferred CGE origin. Without Cck or Cnr1 in the atlas supertype's named markers, this is a circumstantial candidate only.

**What would upgrade confidence**

- Patch-seq or multiplexed single-cell RNA-seq of morphologically or physiologically identified CCK basket cells in CA1, with explicit Cck, Cnr1, and Vip co-expression data, would allow direct comparison to the atlas supertype marker profile and could reveal whether CCK basket cells map to a specific cluster within the Vip Gaba supertype.
- Cluster-level transcriptomic data for individual clusters within Vip Gaba [CS20230722_SUPT_0179] may reveal whether one or more child clusters show elevated Cck and Cnr1 simultaneously — enabling re-evaluation at higher resolution.
- IHC co-localisation of Vip and CCK in identified basket cells would establish whether the Vip Gaba supertype is a plausible transcriptomic home for CCK basket cells.
- A source citation for Vglut3 as a CCK basket cell marker would strengthen the classical node definition and allow meaningful comparison to atlas precomputed expression (currently 0.42).

---

## Proposed experiments

### Transcriptomics / patch-seq

- Patch-seq of physiologically characterised CCK basket cells in CA1 to determine whether they map to the Vip Gaba supertype or to a distinct transcriptomic cluster with high Cck and Cnr1 expression.
- Single-cell RNA-seq with explicit readout of Cck, Cnr1, Vip, and Vglut3 co-expression in CA1 stratum pyramidale cells to test whether CCK basket cells form a distinct transcriptomic identity separate from the core Vip interneuron population.

### Immunohistochemistry / protein-level validation

- IHC co-staining of Vip and CCK (or CB1/Cnr1) in CA1 to quantify what fraction of CCK-positive basket cells co-express Vip.
- Targeted IHC for Vglut3 in morphologically confirmed CCK basket cells to validate or refute the unsourced Vglut3 marker listing.

### Atlas resolution

- Query child clusters within WMBv1 Vip Gaba supertype [CS20230722_SUPT_0179] for Cck and Cnr1 expression statistics to identify whether any cluster-level population shows the expected CCK basket cell marker combination at higher specificity.

---

## Open questions

1. Do CCK basket cells in hippocampus form a coherent transcriptomic cluster in WMBv1, or are they distributed across multiple supertypes (e.g. Vip Gaba, Sncg, or other CGE-derived classes)?
2. What fraction of CCK+ perisomatic interneurons in CA1 co-express Vip? Is Vip co-expression a consistent feature of CCK basket cells or a marker of a morphologically distinct subpopulation?
3. Is Vglut3 a reliable marker of CCK basket cells specifically, or does it mark a broader or different CCK interneuron subtype? What is the supporting citation?
4. Why is Cnr1 not listed as a defining marker in the Vip Gaba atlas supertype despite a high precomputed mean (10.58)? Does this reflect atlas marker selection criteria, or does it suggest Cnr1 is broadly expressed across multiple CGE-derived supertypes and therefore not discriminative?
5. Are the sparse cell counts for this supertype in CA1 pyramidal layer (11 cells) an artefact of sampling density in the WMBv1 dataset, or do they indicate that basket cell soma positions are genuinely underrepresented within this atlas supertype?

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0187 | ANNOTATION_TRANSFER (GEO:GSE99888, Cck.Cxcl14.Vip, SUPERTYPE F1=0.768, gp=0.951) | PARTIAL | Strong directional signal; source label not morphologically confirmed |
| edge_cck_basket_cell_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA | PARTIAL | NT consistent; Cck/Cnr1/Vglut3 all absent from supertype markers; Vip subclass identity unexpected; superseded by SUPT_0187 AT |

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
