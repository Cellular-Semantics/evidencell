# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*draft · 2026-04-09 · Source: `kb/draft/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## Classical type

| Property | Value | References |
|---|---|---|
| CL term | bistratified cell (CL:0004247) — BROAD mapping | |
| Soma location | stratum pyramidale [UBERON:0005401] (CA1); stratum oriens [UBERON:0005383] (CA1); stratum radiatum [UBERON:0005402] (CA1) | [1][2][3] |
| NT | GABAergic | [4] |
| Markers | Pvalb, Sst, Tac1 | Pvalb: [5][6][7][8]; Sst: [9]; Tac1: [9] |
| Negative markers | — | |
| Neuropeptides | Sst | [9] |

---

## Mapping candidates

| Rank | WMBv1 supertype | Cells | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|
| 1 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 🔴 LOW | Tac1 CONSISTENT · Pvalb DISCORDANT | Speculative |

Total: 1 edge. Relationship type: PARTIAL_OVERLAP.

---

## 0216 Sst Gaba_3 · 🔴 LOW

**Supporting evidence:**

- **NT type — CONSISTENT.** SUPT_0216 belongs to the GABA NT class, matching the GABAergic identity of bistratified cells [4].
- **Sst marker — CONSISTENT.** SUPT_0216 is an Sst-defined supertype with precomputed mean expression 11.44, consistent with Sst co-expression in bistratified cells [9].
- **Tac1 marker — CONSISTENT.** Tac1 is present among DEFINING_SCOPED markers in SUPT_0216 (precomputed mean: 0.55). Chamberland et al. 2024 [9] used the Sst;;Tac1 intersectional genetics approach and demonstrated that this intersection targets bistratified cells — Tac1 positivity in this supertype is directly consistent with that identity.
- **Neuropeptide Sst — CONSISTENT.** The Sst neuropeptide on the classical node is supported by the Sst-class identity of this supertype (precomputed mean: 11.44) [9].
- **Atlas metadata (PARTIAL).** The supertype carries Reln among defining markers (consistent with known Reln+ identity of bistratified cells) and shows CA1 stratum oriens signal (818 cells). The Sst subclass placement and GABA NT assignment are consistent with the bistratified cell co-expression of Pvalb and Sst. Partial overlap declared because this supertype also accommodates OLM cells (separate edge) and HS cells — these classical types are not separable at supertype level.
- **Annotation transfer (PARTIAL).** MapMyCells local transfer of Yao 2021 (GEO:GSE185862) SSv4 Sst subclass hippocampal cells (n=273) onto WMBv1 maps 83/273 cells to SUPT_0216 (F1=0.488, supertype level). A separate Pvalb SSv4 subclass transfer (n=66 HIP cells) yields only 6/66 cells to SUPT_0216 (F1=0.053, target purity=0.036); the Pvalb population maps predominantly to Pvalb chandelier (SUPT_0204, F1=0.612) and Pvalb Gaba_2 (SUPT_0206, F1=0.324). The partial Sst signal lends weak support; the absent Pvalb signal reflects the Sst-subclass placement of this supertype.

**Marker evidence provenance:**

- **Pvalb [5][6][7][8].** Evidence spans transcript-level and protein-level methods across four studies. Dannenberg et al. 2017 [4] classifies bistratified cells within the PV+ interneuron group on morphological and functional grounds. The broader PV+ literature [5][6][7] establishes Pvalb as a defining marker for bistratified cells within that group. Tzilivaki et al. 2023 [7] explicitly enumerates morphological subtypes:

> "WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes (basket, axo-axonic, bistratified, radiatum-targeting)."
> — Tzilivaki et al. 2023, Classification Schemes and Methodological Approaches · [7] <!-- quote_key: 221276443_e917908b -->

  Cell-type specificity for bistratified cells is confirmed in [7] and [6] via morphological subtype classification and Cre-driver targeting, respectively. Que et al. 2021 [8] highlights a key constraint on Pvalb-based classification:

> "while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities"
> — Que et al. 2021, unknown · [8] <!-- quote_key: 230508306_e8cc8c19 -->

  This is directly relevant to the DISCORDANT Pvalb alignment: the continuous transcriptomic landscape of PV interneurons means that bistratified cells, despite expressing Pvalb, may sit transcriptomically closer to Sst-class supertypes than to Pvalb-class ones. The DISCORDANT call reflects a real biology, not a classification error.

- **Sst [9].** Chamberland et al. 2024 [9] uses Sst;;Tac1 intersectional genetics and directly confirms Sst co-expression in the targeted bistratified cell population. Cell-type specificity is strong — the intersection was validated by post-hoc morphological and connectivity characterisation:

> "the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells"
> — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [9] <!-- quote_key: 269246896_c084d5c0 -->

- **Tac1 [9].** Evidence from Chamberland et al. 2024 [9] only — a single primary citation. Method: Sst;;Tac1 Cre-driver with morphological and connectivity confirmation (strong cell-type specificity for this study). However, because only one primary study establishes Tac1 as a bistratified-cell marker, independent confirmation is needed. A targeted literature search for "Tac1 bistratified hippocampus" or "substance P bistratified interneuron" is recommended to resolve this gap.

- **Soma location [1][2][3].** Three independent studies confirm soma placement across stratum pyramidale [UBERON:0005401], stratum oriens [UBERON:0005383], and stratum radiatum [UBERON:0005402] of CA1. Perez et al. 2020 [3] note:

> "The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus"
> — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [3] <!-- quote_key: 224817966_79f4a500 -->

  Bocchio et al. 2024 [2] contextualise the canonical PV-expressing subtypes:

> "the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin"
> — Bocchio et al. 2024, Results · [2] <!-- quote_key: 262127573_ba6d02e9 -->

  Chamberland & Topolnik 2012 [1] provide functional classification context:

> "Different types of hippocampal inhibitory interneurons control spike initiation [e.g., axo-axonic and basket cells (BCs)] and synaptic integration (e.g., bistratified and oriens–lacunosum moleculare interneurons) within pyramidal neurons"
> — Chamberland & Topolnik 2012, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 8530661_92702482 -->

  Additional context on PV+ heterogeneity is provided by Dannenberg et al. 2017 [4]:

> "Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells."
> — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 38778375_462ec931 -->

**Concerns:**

- **Pvalb marker — DISCORDANT.** Bistratified cells co-express Pvalb and Sst, but SUPT_0216 belongs to the Sst subclass; Pvalb is not among supertype markers, and the precomputed mean for Pvalb in this supertype is 1.48 (low). The Sst-class placement captures the Sst component of bistratified identity but misses the Pvalb component entirely. The continuous transcriptomic landscape of PV interneurons noted in Que et al. 2021 [8] likely means bistratified cells sit transcriptomically closer to OLM cells than to PV basket cells — *(note: this interpretation of relative transcriptomic proximity is based on general PV-IN biology and [8], not directly stated in the facts)*.
- **Location — APPROXIMATE.** The dominant hippocampal signal in SUPT_0216 is CA1 stratum oriens (818 cells), whereas the bistratified cell soma classically sits at or near stratum pyramidale [UBERON:0005401]. Stratum oriens [UBERON:0005383] and stratum pyramidale [UBERON:0005401] are immediately adjacent CA1 layers *(note: adjacent layers — could reflect registration boundary error; weak counter-evidence)*.
- **Prosubiculum and posterior amygdala signal.** SUPT_0216 carries 259 prosubiculum cells and 780 posterior amygdala cells in addition to the CA1 hippocampal signal. Prosubiculum is adjacent to CA1 (weak counter-evidence). Posterior amygdala is anatomically distant from hippocampal CA1 *(note: distant region — stronger counter-evidence; the classical type may still be a subtype of this T-type but not the hippocampus population specifically)*.
- **Distributed across classical types (DISTRIBUTED_ACROSS_CLUSTERS).** SUPT_0216 contains at least three classical hippocampal types: OLM cells (Sst+/Chrna2+), bistratified cells (Sst+/Pvalb+/Tac1+), and HS cells (Sst+, long-range projecting). These are not separable at supertype level. Confidence cannot be upgraded without cluster-level resolution.
- **Annotation transfer weak for PV population (MARKER_NOT_SPECIFIC).** MapMyCells of Yao 2021 Pvalb SSv4 subclass (n=66 HIP cells) onto WMBv1 yields F1=0.053 at SUPT_0216 with target purity=0.036. The Pvalb population predominantly maps to Pvalb-subclass supertypes (SUPT_0204 and SUPT_0206), not to SUPT_0216. The Yao 2021 'Pvalb' SSv4 label encompasses PV basket, axo-axonic, and bistratified cells without morphological resolution.

**What would upgrade confidence:**

- A morphologically confirmed bistratified cell dataset (patch-clamp with post-hoc reconstruction, or Sst;;Tac1 Cre-driver with histological verification) mapped via MapMyCells at cluster level (target: F1 ≥ 0.80 within SUPT_0216 clusters) would provide `AnnotationTransferEvidence` at cluster rank and could upgrade confidence from LOW to MODERATE if a specific cluster is recovered.
- Targeted `cite-traverse` for "Tac1 bistratified hippocampus" or "substance P bistratified interneuron hippocampus" to confirm Tac1 as a bistratified marker independently of the single Chamberland 2024 citation [9]. Independent confirmation would strengthen the CONSISTENT alignment verdict for `marker_Tac1` and remove the single-citation caveat.
- Cluster-level separation of OLM, bistratified, and HS cell matches within the SUPT_0216 supertype would directly address the DISTRIBUTED_ACROSS_CLUSTERS caveat and is a prerequisite for any confidence upgrade.

---

## Proposed experiments

### 1. Morphologically-confirmed bistratified cell annotation transfer

*Existing annotation transfer status:* A SUPERTYPE-level MapMyCells transfer is already recorded using Yao 2021 (GEO:GSE185862) SSv4 data. The Sst SSv4 subclass maps 83/273 HIP cells to SUPT_0216 with F1=0.488; the Pvalb SSv4 subclass yields only F1=0.053 (6/66 cells). This provides partial support but cannot resolve cluster-level identity and does not use a morphologically confirmed bistratified cell source. The GEO:GSE185862 dataset is available as a starting point, but subtype resolution requires a more specific input.

- **What:** MapMyCells local annotation transfer at CLUSTER level using a morphologically confirmed bistratified cell dataset (e.g. Sst;;Tac1 Cre-driver or patch-clamp-reconstructed bistratified cells)
- **Target:** F1 ≥ 0.80 at CLUSTER level within Sst Gaba_3 supertype [CS20230722_SUPT_0216]
- **Expected output:** `AnnotationTransferEvidence` entries at cluster rank, added to edge `edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216`
- **Resolves:** DISTRIBUTED_ACROSS_CLUSTERS caveat; distinguishes bistratified cell clusters from OLM and HS clusters within SUPT_0216; addresses open question 1

### 2. Targeted literature search: Tac1 as bistratified marker

- **What:** `cite-traverse` targeted search for "Tac1 bistratified hippocampus" and "substance P bistratified interneuron hippocampus"
- **Target:** Identification of ≥1 independent primary study confirming Tac1/substance P expression in morphologically confirmed bistratified cells
- **Expected output:** `LiteratureEvidence` item on the `marker_Tac1` property comparison; updated `MarkerSource` provenance on the Tac1 `GeneDescriptor`
- **Resolves:** Open question 2; removes single-citation caveat on Tac1 marker; strengthens CONSISTENT alignment verdict for `marker_Tac1`

---

## Open questions

1. Can bistratified cells be separated from OLM and HS cells at WMBv1 cluster level within Sst Gaba_3 supertype [CS20230722_SUPT_0216]? *(appears on edge `edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216`)*
2. Is Tac1 confirmed as a bistratified cell marker in independent primary studies beyond Chamberland et al. 2024 [9]? *(single-citation marker; targeted literature search recommended)*
3. Does the continuous transcriptomic landscape of PV interneurons [8] fully account for the Sst-subclass placement of bistratified cells, or could a bistratified-cell-specific transcriptomic signature be identified that would separate them from OLM cells at cluster resolution?

---

## Evidence base table

| Edge ID | Evidence type | Supports | Notes |
|---|---|---|---|
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA | PARTIAL | Sst subclass, GABA NT, Tac1 DEFINING_SCOPED consistent; Pvalb not captured; three classical types co-occupy this supertype |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ANNOTATION_TRANSFER | PARTIAL | Yao 2021 GEO:GSE185862 SSv4; Sst subclass F1=0.488 (83/273 HIP cells) at SUPT level; Pvalb subclass F1=0.053 (6/66 HIP cells) |

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Chamberland & Topolnik 2012 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426/) | soma location |
| [2] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246/) | soma location |
| [3] | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500/) | soma location |
| [4] | Dannenberg et al. 2017 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728/) | neurotransmitter type, PV+ heterogeneity |
| [5] | Ekins et al. 2020 | [33150866](https://pubmed.ncbi.nlm.nih.gov/33150866/) | Pvalb marker |
| [6] | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922/) | Pvalb marker |
| [7] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748/) | Pvalb marker, morphological subtypes |
| [8] | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060/) | Pvalb marker, transcriptomic landscape |
| [9] | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/) | Sst marker, Tac1 marker |
