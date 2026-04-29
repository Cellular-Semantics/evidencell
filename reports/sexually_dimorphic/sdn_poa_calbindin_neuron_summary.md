# Sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neuron — WMBv1 Mapping Report
*draft · 2026-04-25 · Source: `kb/draft/sexually_dimorphic/20260425_sexually_dimorphic_report_ingest.yaml`*

**⚠ Draft mappings. Evidence is atlas-metadata only unless otherwise noted. All edges require expert review before use.**

---

## 1. Classical type

The **sexually dimorphic nucleus of the preoptic area (SDN-POA) calbindin neuron** is
defined by neurochemical and histological criteria: Calbindin-D28K (Calb1)
immunoreactivity in a histologically delineable subnucleus within the rodent medial
preoptic nucleus, with absence of tyrosine hydroxylase (TH) cell bodies. The structure
is male-biased in cell number and is considered the rodent homolog of the third
interstitial nucleus of the anterior hypothalamus (INAH3) in humans, with homologous
structures described in sheep, rhesus monkey, and quail.

No CL term currently exists for this population — it is a candidate for a new term.

| Property | Value | References |
|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515] (SDN-POA is a histologically defined subnucleus within MPN) | [1], [2] |
| Defining markers | Calb1 (calbindin-D28K, protein, IHC) | [2] |
| Negative markers | Th (no TH-positive cell bodies in SDN-POA) | [2] |

<details>
<summary>Literature support — expand for verbatim quotes</summary>

**[1] Negri-Cesi 2015 · PMID:26672480 — Sexually Dimorphic Brain Regions and Structures**

> The 2 best known dimorphic brain structures are the sexual dimorphic nucleus of the medial preoptic hypothalamic area (SDN-POA) in rodents, which correspond to the interstitial nucleus of the anterior hypothalamus (INAH) in humans, and the anteroventral periventricular (AVPV) nucleus. The first one controls male sex behavior and is larger in males than in females; the second one is critical for the cyclic control of ovulation and is larger in females than in males.
> — Negri-Cesi 2015, Sexually Dimorphic Brain Regions and Structures · [1] <!-- quote_key: 14863067_fa51fcf7 -->

**[2] He et al. 2013 · PMID:25206587 — Sexually Dimorphic Brain Regions and Structures**

> One of the well-defined sexually dimorphic structures in the brain is the sexually dimorphic nucleus, a cluster of cells located in the preoptic area of the hypothalamus. The rodent sexually dimorphic nucleus of the preoptic area can be delineated histologically using conventional Nissl staining or immunohistochemically using calbindin D28K immunoreactivity
> — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_d6c3a647 -->

**[2] He et al. 2013 · PMID:25206587 — Sexually Dimorphic Brain Regions and Structures (cross-species homology)**

> The sexually dimorphic nucleus has been specifically defined in the brains of human and other mammalian and non-mammalian and includes the third interstitial nucleus of the anterior hypothalamus in humans (Allen et al., 1989)(Allen et al., 1990) , the ovine sexually dimorphic nucleus in the medial preoptic area (Roselli et al., 2004) , the medial preoptic and anterior hypothalamic regions in rhesus monkeys (Byne, 1998) , a specific area in the medial preoptic nucleus in quail (Viglietti‐Panzica et al., 1986) , and the sexually dimorphic nucleus of the preoptic area in rats (Gorski et al., 1978)(Gorski et al., 1980) . The human sexually dimorphic nucleus of the preoptic area is located in the medial part of the preoptic area, between the dorsolateral supraoptic nucleus and the rostral pole of the paraventricular nucleus (Hofman et al., 1989)
> — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_1098a86b -->

**[2] He et al. 2013 · PMID:25206587 — Calbindin/TH profile of SDN-POA**

> The sexually dimorphic nucleus of the preoptic area is highlighted by calbindin-D28K immunoreactivity: no TH-positive cells were found, but fine axon-like projections/synaptic structures were seen
> — He et al. 2013, Sexually Dimorphic Brain Regions and Structures · [2] <!-- quote_key: 3481177_17d4bd9d -->

</details>

---

## 4. Mapping candidates

### 4a. Candidate overview

Two mapping edges are recorded for sdn_poa_calbindin_neuron: a supertype-level edge
to SUPT_0423 and a cluster-level edge to CLUS_1550, the only child cluster of SUPT_0423
whose primary soma is MBA:515 (MPN) and which carries an unambiguous male bias.
Both edges are LOW confidence: SDN-POA is a histologically defined subnucleus within
MPN that cannot be resolved as a distinct spatial domain in WMBv1 MERFISH data.

| Rank | WMBv1 cluster | Supertype | Cells (MERFISH) | Confidence | Key property alignment | Verdict |
|---|---|---|---|---|---|---|
| 1 | 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] | 0423 BST-MPN Six3 Nrgn Gaba_4 | n=22 MPN (also PVH n=9, PVHap n=4, Hypothalamus n=9) | 🔴 LOW | Calb1 CONSISTENT; MFR=3.35 CONSISTENT; Th DISCORDANT | Speculative |
| 2 | 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] | (self) | n=47 MPN (also BNST n=18, AHN n=46, PVN n=31) | 🔴 LOW | Calb1 CONSISTENT; Th DISCORDANT | Speculative |

2 edges total. Relationship type: PARTIAL_OVERLAP (CLUS_1550) / UNCERTAIN (SUPT_0423).

### 4b. Property alignment — primary candidate (CLUS_1550)

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Medial preoptic nucleus [MBA:515] (SDN-POA is histological subnucleus within MPN) | MBA:515 (MPN) n=47; also BNST n=18, AHN n=46, PVN n=31 | MBA:515 (MPN) n=22 (primary soma); also PVH n=9, PVHap n=4, Hypothalamus n=9 | APPROXIMATE (both levels) |
| Calb1 expression | POSITIVE (protein, primary defining marker) | precomputed mean_expression=6.42 (DEFINING_SCOPED atlas marker) | precomputed mean_expression=6.66 | CONSISTENT (both levels) |
| Th (negative marker) | ABSENT (negative marker; no TH cell bodies in SDN-POA) | precomputed mean_expression=0.99 | precomputed mean_expression=2.75 | DISCORDANT (both levels) |
| Sex ratio | male-biased (SDN-POA larger in males; classical IHC) | not available at supertype level | MFR=3.35 (CLUS_1550) — male-biased | CONSISTENT |
| Annotation transfer F1 | not applicable | NOT_ASSESSED | NOT_ASSESSED | NOT_ASSESSED |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas precomputed expression (CLUS_1550 Calb1/Th, MFR) | Atlas metadata | WEAK | Calb1=6.66; Th=2.75; MFR=3.35; MPN primary soma n=22 | atlas-internal |
| SUPT_0423 atlas metadata (Calb1/Th, MBA:515 n=47) | Atlas metadata | WEAK | Calb1=6.42 (DEFINING_SCOPED); Th=0.99; MPN n=47 | atlas-internal |

*(1 of an unreported number of child clusters of SUPT_0423 — CLUS_1550 — has MBA:515 (MPN) as primary soma and an unambiguous male-biased MFR; however, Th=2.75 at cluster level remains discordant with the classical Th NEGATIVE assertion, and the SDN-POA cytoarchitectonic zone cannot be resolved within MPN from MERFISH data alone. Best match: CLUS_1550.)*

---

## 5. Candidate paragraphs

## 1550 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_CLUS_1550] · 🔴 LOW

### Supporting evidence

- **Calb1 expression is high and concordant.** CLUS_1550 precomputed mean Calb1 = 6.66 directly matches the primary classical defining marker (calbindin-D28K immunoreactivity) [2]. This is the strongest atlas-side signal supporting the mapping.
- **MPN primary soma is confirmed.** CLUS_1550 has MBA:515 (Medial preoptic nucleus) as its primary soma annotation (n=22 cells), placing the cluster in the broader brain region in which SDN-POA is histologically defined [1], [2].
- **Sex ratio is concordant and unambiguous.** male_female_ratio = 3.35 in CLUS_1550 — clearly male-biased — directly matches the male-biased dimorphism that defines sdn_poa_calbindin_neuron [1]. CLUS_1550 is the only child cluster of SUPT_0423 with both MPN-primary soma and an unambiguous male bias.
- **Cluster was identified by targeted child-cluster analysis.** CLUS_1550 emerged from systematic inspection of SUPT_0423 child clusters for an MPN-restricted, male-biased, Calb1-high cluster — the only one matching all three filters.

### Marker evidence provenance

- **Calb1** — classical evidence is protein-level (calbindin-D28K immunohistochemistry, the histological criterion used to delineate SDN-POA from surrounding MPN) [2]. Atlas precomputed value (mean = 6.66) is transcript-based (10x Chromium). The high atlas value is consistent with the protein evidence; no data-source discrepancy. Calb1 is a DEFINING_SCOPED marker at the supertype level (mean = 6.42), confirming Calb1 as a marker shared across SUPT_0423 rather than specific to the SDN-POA subnucleus.
- **Th (negative marker)** — classical evidence is protein-level: He et al. 2013 explicitly report "no TH-positive cells were found" within the calbindin-delineated SDN-POA [2]. Atlas precomputed Th = 2.75 at CLUS_1550 (transcript-based) is non-zero and discordant with the classical NEGATIVE assertion. The discrepancy is between **classical protein-IHC negative** and **atlas transcript positive at moderate level**. Transcript-level Th may reflect cells outside the SDN-POA cytoarchitectonic zone (PVH/PVHap components of CLUS_1550), or low-abundance transcript not translated to detectable protein. This concern persists at supertype level (Th = 0.99) and is amplified at cluster level (Th = 2.75).

### Concerns

- **SDN-POA is not resolvable as a distinct spatial domain in WMBv1 MERFISH.** SDN-POA is a histologically defined subnucleus within MPN [MBA:515]; WMBv1 MERFISH registers cells to MBA:515 as a whole and cannot distinguish SDN-POA cells from other MPN Calb1+ neurons. Mapping is possible only at MPN level. *(adjacent region — could reflect registration boundary error; weak counter-evidence at the level of SDN-POA-specific identity, but the broader MPN-level placement is correct)*
- **Th = 2.75 at cluster level is discordant with the Th NEGATIVE classical assertion.** The classical negative-marker call is protein-level (no TH-positive cell bodies in SDN-POA) [2]; the atlas value is transcript-level. CLUS_1550 spans MPN, PVH, and PVHap — Th transcript signal may originate from non-MPN cells within the cluster, but this cannot be confirmed from MERFISH data alone. Spatial inspection of the Th MERFISH channel for CLUS_1550 cells assigned to MBA:515 is needed.
- **CLUS_1550 is not MPN-restricted.** The cluster spans MBA:515 (MPN) n=22, PVH n=9, PVHap n=4, and Hypothalamus n=9. The MPN-primary soma annotation (n=22) is the largest single-region count, but the cluster as a whole is multi-regional.
- **Annotation transfer NOT_ASSESSED.** No data-driven cell-level mapping of Calb1+ MPN/SDN-POA scRNA-seq cells to WMBv1 has been run; this is the most important remaining gap in the evidence base for this edge.

### What would upgrade confidence

- **MapMyCells annotation transfer** of an SDN-POA-focused or MPN Calb1+ scRNA-seq dataset against WMBv1 (see Proposed experiments) is the priority experiment. F1 ≥ 0.50 at CLUS_1550 would support upgrading to MODERATE confidence and would add `AnnotationTransferEvidence`.
- **MERFISH spatial inspection of the Th channel** for CLUS_1550 cells assigned to MBA:515 would resolve whether Th transcript signal originates from MPN cells (refuting the mapping) or from PVH/PVHap components of the cluster (preserving the mapping).
- **Sub-regional MERFISH spatial analysis** of CLUS_1550 cells within MBA:515 — testing for clustering consistent with the SDN-POA dorsomedial position — would address whether atlas data can recover the histological subnucleus despite the lack of explicit MBA-level annotation.

---

## 0423 BST-MPN Six3 Nrgn Gaba_4 [CS20230722_SUPT_0423] · 🔴 LOW

### Supporting evidence

- **Calb1 is a DEFINING_SCOPED supertype marker.** Precomputed mean Calb1 = 6.42 at SUPT_0423 directly matches the classical primary defining marker [2]. This is the strongest quantitative agreement between classical node and supertype.
- **MPN cells are present.** n = 47 cells within SUPT_0423 are labelled to Medial preoptic nucleus [MBA:515], providing a direct anatomical anchor for the broader MPN region in which SDN-POA is histologically defined [1], [2].
- **DB-score rank-1 candidate at supertype level.** SUPT_0423 was the only anatomically plausible rank-1 candidate (DB score = 1) returned by atlas-metadata candidate search for Calb1+ MPN.

### Marker evidence provenance

- **Calb1** — classical evidence is protein-level (calbindin-D28K IHC) [2]; atlas precomputed value is transcript-level (mean = 6.42, DEFINING_SCOPED). The values are concordant; specificity is reduced because Calb1 is widely expressed and is DEFINING_SCOPED rather than DEFINING — i.e. it is a defining marker only within the scope of SUPT_0423, not exclusive to it.
- **Th (negative marker)** — classical protein-IHC evidence reports no TH-positive cell bodies in SDN-POA [2]. Atlas Th = 0.99 at supertype level is low but non-zero, discordant with the classical NEGATIVE assertion. The discrepancy is amplified at child-cluster level (CLUS_1550 Th = 2.75). Th transcript signal at supertype level may reflect Th-expressing cells in BST/AHN/PVN components of SUPT_0423 rather than MPN-proper cells.

### Concerns

- **Supertype spans BST, MPN, AHN, and PVN.** SUPT_0423 covers MBA:515 (MPN, n=47), BNST (n=18), AHN (n=46), and PVN (n=31). Multiple classical types — not just SDN-POA Calb1 neurons — are expected to map to this same supertype; SDN-POA Calb1 neurons are a subset within the MPN component. *(distant regions — BST, AHN, PVN are anatomically distinct from MPN; this is a significant caveat at supertype level)*
- **Calb1 alone is insufficient to identify SDN-POA neurons specifically.** Calb1 is expressed across many brain regions and is DEFINING_SCOPED (not DEFINING) in SUPT_0423. The supertype-level Calb1 signal does not discriminate SDN-POA from other MPN Calb1+ populations or from BST/AHN/PVN Calb1+ populations within the supertype.
- **Th = 0.99 at supertype level is discordant with the Th NEGATIVE classical assertion.** Although low, this contradicts the protein-level IHC evidence [2] that no TH-positive cell bodies exist in SDN-POA. The signal may originate from non-MPN components.
- **SDN-POA is not resolvable as a subnucleus within MPN in MERFISH data.** Matching is possible only at MPN level; SDN-POA cells cannot be distinguished from other MPN Calb1 neurons.
- **Sex ratio data not available at supertype level.** Male-biased dimorphism — a defining feature of SDN-POA — cannot be assessed from supertype-level metadata. The signal is visible only in CLUS_1550 (MFR = 3.35).
- **Annotation transfer NOT_ASSESSED.**

### What would upgrade confidence

- The child-cluster inspection (proposed in this edge) has already been carried out and is captured in the CLUS_1550 edge above.
- MapMyCells annotation transfer of an SDN-POA-focused or MPN Calb1+ scRNA-seq dataset against WMBv1 — F1 ≥ 0.50 at SUPT_0423 would upgrade this edge; F1 ≥ 0.80 at CLUS_1550 level would support MODERATE confidence on the cluster edge. Expected output: `AnnotationTransferEvidence`.
- Targeted cite-traverse for studies reporting scRNA-seq of histologically delineated SDN-POA Calb1+ cells from male and female rodents could provide independent transcriptomic confirmation of the supertype assignment and address the Th discrepancy.

---

## 6. Proposed experiments

### 1. MapMyCells annotation transfer of an SDN-POA / MPN Calb1+ scRNA-seq dataset against WMBv1

**What:** Retrieve a published scRNA-seq dataset enriched for MPN Calb1+ cells, ideally a Calb1-Cre or SDN-POA-microdissected preparation from male and female rodents. Run MapMyCells against WMBv1 at cluster resolution.

**Target:** F1 ≥ 0.50 at SUPT_0423 level; F1 ≥ 0.80 at CLUS_1550 level for Calb1+ MPN cells.

**Expected output:** `AnnotationTransferEvidence` entries on both edges (edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 and edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550). Atlas: WMBv1. Tool: MapMyCells. Output format: F1 matrix per cluster, fed back as `AnnotationTransferEvidence` YAML.

**Resolves:** Open questions 1 and 3. Confirms or refutes CLUS_1550 as the correct cluster assignment. Addresses the `annotation_transfer_f1` NOT_ASSESSED gap on both edges.

### 2. MERFISH spatial inspection of the Th channel within CLUS_1550 cells at MBA:515

**What:** For CLUS_1550 cells assigned to MBA:515 in WMBv1 MERFISH data, examine the per-cell Th channel intensity. Compare to CLUS_1550 cells in PVH and PVHap.

**Target:** Determination of whether Th transcript signal in CLUS_1550 originates from the MPN component (refuting the SDN-POA mapping at cluster level) or from PVH/PVHap components (preserving the mapping by attributing Th to non-SDN-POA cells within a multi-region cluster).

**Expected output:** Curatorial note attached to the CLUS_1550 edge summarising per-region Th signal; potentially a refined `MarkerAnalysisEvidence` record.

**Resolves:** Open question 1 (Th source within CLUS_1550).

### 3. Sub-regional MERFISH spatial analysis of CLUS_1550 cells within MBA:515

**What:** Within MBA:515, test CLUS_1550 cells for sub-regional clustering consistent with the dorsomedial cytoarchitectonic position of the SDN-POA. Compare cell density and distribution between male and female samples.

**Target:** Detection of a male-biased dorsomedial sub-cluster within MBA:515 cells of CLUS_1550 — the spatial signature of SDN-POA — or formal demonstration that no such sub-cluster exists at MERFISH spatial resolution.

**Expected output:** Curatorial note or, if positive, a refined `MarkerAnalysisEvidence` / spatial-evidence record.

**Resolves:** Open question 2 (sub-regional resolution of SDN-POA within MPN).

---

## 7. Open questions

1. Do CLUS_1550 cells at MBA:515 (MPN) express Th, or does the cluster-level Th=2.75 signal originate from PVH/PVHap components of this multi-region cluster? *(Appears on the cluster edge.)*
2. Can sub-regional MERFISH spatial data distinguish SDN-POA dorsomedial cells from other MPN Calb1+ neurons within CLUS_1550? *(Appears on the cluster edge; partially shared with the supertype edge.)*
3. Do any clusters within SUPT_0423 — beyond CLUS_1550 — show peak Calb1 co-located with MBA:515 (MPN) and male-biased sex ratio consistent with SDN-POA identity? *(Appears on the supertype edge; partially addressed by the CLUS_1550 child-cluster analysis but not exhaustively surveyed.)*

---

## 8. Evidence base

| Edge ID | Evidence type | Supports |
|---|---|---|
| edge_sdn_poa_calbindin_neuron_to_cs20230722_supt_0423 | ATLAS_METADATA | WEAK — Calb1=6.42 (DEFINING_SCOPED); Th=0.99 (discordant with NEGATIVE); MBA:515 n=47; supertype spans BST/MPN/AHN/PVN |
| edge_sdn_poa_calbindin_neuron_to_cs20230722_clus_1550 | ATLAS_METADATA | WEAK — Calb1=6.66; Th=2.75 (discordant with NEGATIVE); MBA:515 primary soma n=22; MFR=3.35 (male-biased, concordant); cluster spans MPN/PVH/PVHap |

---

## 9. References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Negri-Cesi 2015 | [PMID:26672480](https://pubmed.ncbi.nlm.nih.gov/26672480/) | Soma location; SDN-POA male-biased dimorphism; INAH homology |
| [2] | He et al. 2013 | [PMID:25206587](https://pubmed.ncbi.nlm.nih.gov/25206587/) | Soma location; calbindin-D28K defining marker (IHC); Th NEGATIVE marker (no TH cell bodies); cross-species homology |
