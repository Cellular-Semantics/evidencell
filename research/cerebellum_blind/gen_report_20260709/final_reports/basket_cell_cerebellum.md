# Cerebellar basket cell (molecular layer interneuron) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml`*

---

## Introduction

Cerebellar basket cells are GABAergic interneurons of the molecular layer whose axons form dense perisomatic plexuses — the basket formations — around Purkinje cell somata, and specialised pinceaux at the Purkinje cell axon initial segment [1][2][3][4]. They are born earlier than stellate cells during development, populate the inner third of the molecular layer [UBERON:0002974], and are distinguished from stellate cells both by their position in the layer and by the characteristic axonal architecture [5]. The basket-stellate distinction has long been debated: morphological variation across the depth of the molecular layer suggests the two populations may form a continuous spectrum rather than two discrete types, and basket cells are not perfectly resolved by current transcriptomic atlases [1][2][5]. The mapping reported here reflects this limitation — the evidence is based on atlas metadata alone and the available transcriptomic clusters likely represent molecular-layer interneuron (MLI) diversity that does not cleanly partition along basket/stellate lines.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] (inner/lower third); cerebellar cortex [UBERON:0002129] | [1][2][3][4] |
| Neurotransmitter | GABAergic | [5] |
| Defining markers | Pvalb, RORa, HCN1, Kcna1, Grid1 | [6][2][7][8][7][9] |
| Negative markers | Calb1 | [6] |
| Neuropeptides | — | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Immunostaining for PV (parvalbumin) and VIAAT-labelled presynaptic terminals around Purkinje cell somata; pinceau at Purkinje cell axon initial segment · [3]

  > lower MLIs or basket cells (ΔMLI), that is, PV-labeled somata in the lower ML VIAAT-labeled presynaptic terminals around PC somata, and PV/VIAAT-labeled pinceau formation at the base of PC somata
  > — Miyazaki et al. 2021, Results · [3] <!-- quote_key: 239017682_320a7a9b -->

- **Soma location:** Morphological review — basket cells born earlier, populate lower third of molecular layer and form basket terminals around Purkinje cell somata · [1]

  > The cerebellar molecular layer interneurons (MLIs) derive from a common progenitor pool and form compact morphologies 30, (Sotelo, 2015) . MLIs encompass an anatomically and functionally diverse population that provides the complement of dendritic-, somatic-, and axon initial segment-targeting inhibition onto principal Purkinje cells. MLIs are classically divided based on morphological features into the basket cells and stellate cells 30 . Basket cells (BCs) are born earlier, populate the lower third of the molecular layer (ML) and form a series of perisomatic basket terminals that enwrap the cell bodies of Purkinje cells. Some BC terminals further specialize into 'pinceaux' formations that align the Purkinje cell axon initial segment (Sotelo, 2015)(Buttermore et al., 2012) . By contrast, later-born stellate cells (SCs) integrate into the upper molecular layer where their axons innervate Purkinje cell dendrites. The basket-stellate cell division has long been debated due to the morphological variation that suggests MLIs form one continuously varying population (Abend, 2016)(Sotelo, 2015)(Rakić, 1972)(Paula-Barbosa et al., 1983)(Rieubland et al., 2014) (Sultan et al., 1998) . How MLI diversity arises during development is not known
  > — Wang & Lefebvre 2020, Anatomical organization and core cell types · [1] <!-- quote_key: 213840122_c2acdac4 -->

- **Soma location:** Basket axons form the basket formation and pinceaux around Purkinje cell axon initial segments · [2]

  > The axons of several basket cells converge on single Purkinje cell somata to form the basket 34 . Basket cell axons extend further to form specialized pinceaux synapses around the axon initial segments of Purkinje cells 34,(Ango et al., 2004)(Sotelo, 2008)
  > — Brown et al. 2018, Anatomical organization and core cell types · [2] <!-- quote_key: 59945454_09563575 -->

- **Soma location + general MLI description:** Stellate and basket cells — sole GABA-using MLIs; basket cells target Purkinje soma/AIS, stellate cells target dendrites · [5]

  > . Stellate and basket cells are the only ML interneurons (MLIs) known to use GABA as a neurotransmitter (Shepherd, 1974). They are distinguished by their position in the upper and lower ML and by their axonal distribution [1,3], although intermediate forms have been described, raising the possibility that MLIs represent a continuum that varies gradually (Sultan et al., 1998)(Schilling et al., 2008). Basket cell axons, in particular, surround the cell bodies of Purkinje cells and also form a characteristic plexus around the axon initial segment, whereas stellate cells make synapses exclusively on the dendritic arbor.
  > — Briatore et al. 2010, Anatomical organization and core cell types · [5] <!-- quote_key: 1460508_88d765d5 -->

- **Neurotransmitter:** GABAergic (same quote as soma location above) · [5]

- **Pvalb (defining marker):** Immunostaining — Parv labels basket neurons in the vicinity of Purkinje cells; Calb not expressed in basket neurons · [6]

  > .We performed immunostaining of wild-type cerebellar sections against parvalbumin (Parv) to label both Purkinje neurons and molecular layer interneurons, including basket neurons (Bastianelli, 2008). We also immunostained for Calb as a specific marker for Purkinje neurons (Nordquist et al., 1988), pNfl as a marker for basket neuron collaterals, and potassium channels (K V 1.2) to label the core of the pinceau formed by basket axon terminals that target the Purkinje AIS. As shown in Figure 1, coimmunostaining against Parv and Calb at P10 shows Parv expression in basket neurons (b) (Fig. 1 Aa,b) in the vicinity of the Purkinje neurons. Note that Parv is also expressed in Purkinje neurons (Fig. 1 Ab, merged yellow color), but Calb is not expressed in basket neurons
  > — Buttermore et al. 2012, Anatomical organization and core cell types · [6] <!-- quote_key: 41293753_2d217397 -->

- **RORa (defining marker):** RORa expression validated the basket/stellate reporter distribution · [2]

  > The distribution of reporter expression in stellate versus basket cells was validated by RAR-related orphan receptor alpha (RORα) expression (Fig. 2c, per condition: N = 3, n = 9), which also marks molecular layer interneurons and Purkinje cells (Maricich et al., 1999)(Hamilton et al., 1996)(Ino, 2004)(Sillitoe et al., 2008)
  > — Brown et al. 2018, Anatomical organization and core cell types · [2] <!-- quote_key: 59945454_b21703e0 -->

- **HCN1, Kcna1 (defining markers):** HCN1, Kv1.1 (Kcna1), PSD95, GAD67 mark basket cell pinceaux in functional zones; genetic tracing with Ascl1CreERT2 · [7][8]

  > Basket cells form dense inhibitory plexuses that wrap Purkinje cell somata and terminate as pinceaux at the initial segment of axons. Here, we demonstrate that HCN1, Kv1.1, PSD95 and GAD67 unexpectedly mark patterns of basket cell pinceaux that map onto Purkinje cell functional zones. Using cell-specific genetic tracing with an Ascl1CreERT2 mouse conditional allele, we reveal that basket cell zones comprise different sizes of pinceaux
  > — Wang & Lefebvre 2020, Connectivity and circuit motifs · [7] <!-- quote_key: 222167171_a9c43f32 -->

- **Grid1 (defining marker):** GluD1 (Grid1) expressed at highest level in molecular layer interneurons; GluD1 knockout reduces interneuron connectivity and number · [9]

  > In the cerebellar cortex, GluD1 mRNA was expressed at the highest level in molecular layer interneurons and its immunoreactivity was concentrated at PF synapses on interneuron somata. In GluD1-knock-out mice, the density of PF synapses on interneuron somata was significantly reduced and the size and number of interneurons were significantly diminished. Therefore, GluD1 is common to GluD2 in expression at PF synapses, but distinct from GluD2 in neuronal expression in the cerebellar cortex; that is, GluD1 in interneurons and GluD2 in PCs. Furthermore, GluD1 regulates the connectivity of PF–interneuron synapses and promotes the differentiation and/or survival of molecular layer interneurons.
  > — Konno et al. 2014, Functional roles and physiology · [9] <!-- quote_key: 8585958_c30f821f -->

- **Calb1 (negative marker):** Calb is not expressed in basket neurons; Calb is a specific marker for Purkinje neurons (Buttermore et al. 2012) · [6]

</details>

### Cell Ontology mapping

Cell Ontology mapping: cerebellar basket cell [[CL:2000027](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:2000027)] (EXACT).

---

## Results

Atlas metadata supports mapping of the cerebellar basket cell to the supertype 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] as the primary transcriptomic candidate, with high Pvalb and Kcna1 expression in the 99th percentile of the GABAergic cerebellar cohort, clean Calb1 negativity, and strong cerebellar cortex localisation (see property comparison table below). A secondary cluster-level candidate, 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185], carries the cleanest overall marker profile at cluster resolution but represents a small population (442 cells) with boundary-range cerebellar signal. Both candidates are assessed at LOW confidence given the metadata-only evidence base and the known imperfect correspondence between basket/stellate morphological identity and current WMBv1 transcriptomic cluster labels; annotation-transfer experiments from a basket-cell-targeted source are the primary route to a definitive call.

### 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Supertype (SUPT_1151) | Best cluster | Alignment |
|---|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] count_100um=21,084 (painted); Ansiform lobule; Crus 1 | Not assessed at cluster level in this edge | CONSISTENT |
| NT type | GABAergic | Not asserted at supertype | — | NOT_ASSESSED |
| Pvalb expression | Defining marker | Mean 11.33; cohort-pct 0.991; child-cluster coverage 1.000 | — | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | — | NOT_ASSESSED |
| HCN1 expression | Defining marker | No atlas expression data | — | NOT_ASSESSED |
| Kcna1 expression | Defining marker | Mean 7.23; cohort-pct 0.973; child-cluster coverage 1.000 | — | CONSISTENT |
| Grid1 expression | Defining marker | Mean 1.39; cohort-pct 0.191; child-cluster coverage 1.000 | — | APPROXIMATE |
| Calb1 | Absent (negative marker) | Mean 0.09; cohort-pct 0.073; child-cluster coverage 1.000 | — | CONSISTENT |
| Sex ratio | Not documented | Not available at supertype level | — | NOT_ASSESSED |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: SUPT_1151 cerebellar location + marker expression | Atlas metadata | PARTIAL | region_fraction_100um=0.851; Pvalb 11.33, Kcna1 7.23; child-coverage 1.000 | atlas-internal |

**Supporting evidence:**
- Pvalb expression at mean 11.33, 99.1st percentile of the 50-member GABAergic cerebellar cohort, with full child-cluster coverage (1.000): the Pvalb signal is consistent across every child cluster under this supertype, matching the classical definition established by immunostaining of basket neurons [6].
- Kcna1 (Kv1.1) expression at mean 7.23, 97.3rd percentile, full child-coverage (1.000): consistent with the literature identifying Kv1.1 as a basket cell pinceau marker in cerebellar functional zones [7][8].
- Calb1 mean 0.09, below the MIN_DETECTABLE threshold (0.1), 7.3rd percentile, full child-coverage (1.000): clean absence consistent with the classical negative marker established by Buttermore et al. 2012 [6].
- Soma location: 85.1% of cells fall within 100 µm of the cerebellar MBA region (region_fraction_100um: 0.851; lower-bound rollup). Localisation is CONSISTENT with cerebellar cortex.
- Supertype name "CBX MLI" (cerebellar cortex molecular layer interneuron) is anatomically aligned with the classical soma location in the molecular layer of cerebellar cortex [UBERON:0002974].

**Marker evidence provenance:**
- **Pvalb:** Evidence is immunofluorescence/immunostaining from Buttermore et al. 2012 [6] on morphologically identifiable basket neurons in wild-type cerebellar sections. Cell-type identity confirmed by anatomical position (vicinity of Purkinje neurons) and co-staining with pNfl (basket neuron collateral marker) and Kv1.2 (pinceau marker). Evidence is protein-level; atlas-side value is transcript-level precomputed mean expression. The high mean (11.33) strongly supports cross-modality concordance. Note: Pvalb is also expressed in Purkinje cells (which are positive for Calb1); the clean Calb1 absence on SUPT_1151 helps distinguish from a Purkinje-cell contamination scenario.
- **RORa:** Marker established by Brown et al. 2018 [2] using a reporter line — validated at transcript/reporter level in molecular layer interneurons and Purkinje cells. Not available in WMBv1 precomputed stats for this supertype — cannot assess atlas-side concordance. Gap in evidence.
- **HCN1:** Literature established at protein level by immunostaining of basket cell pinceau structures [7][8]. Gene absent from WMBv1 precomputed stats for this supertype — NOT_ASSESSED. ⚠ Gap: HCN1 is a pinceau-enriched marker and may be expressed at low levels in cell bodies while being concentrated in axonal terminations; soma-level transcript expression may not reflect pinceau protein abundance.
- **Kcna1:** Established by Zhou et al. (preprint) at protein level in basket cell pinceaux [7][8]. Present in atlas at transcript level (mean 7.23, pct 0.973). Cross-modality concordance is plausible; same caveat as HCN1 applies regarding pinceau-enriched distribution.
- **Grid1:** Established by Konno et al. 2014 [9] at mRNA level (highest in MLI) and protein level (PF synapses on interneuron somata). The atlas APPROXIMATE alignment (mean 1.39, 19.1st percentile) is notably low for a gene described as most highly expressed in MLIs. This discrepancy may reflect: (a) Atlas-level averaging across supertype diluting a cluster-specific signal; (b) The Konno 2014 finding covering all MLIs (basket + stellate combined) while SUPT_1151 may correspond to only one subtype; (c) Gene-level normalisation differences between datasets. Flag for investigation.
- **Calb1 (negative):** Immunostaining evidence [6] — Calb is not expressed in basket neurons; in the atlas, Calb1=0.09 is below detection threshold. Cross-modality CONSISTENT. Importantly, Calb1 is a defining Purkinje cell marker, so its absence helps rule out Purkinje cell contamination of this cluster.

**Concerns:**
- Grid1 APPROXIMATE on SUPT_1151 (mean 1.39, 19.1st percentile). The literature (Konno 2014 [9]) establishes Grid1 as the MLI-enriched paralogue in cerebellar cortex. The low supertype-level mean is an unexplained gap; without cluster-level breakdown it is unclear whether this reflects supertype averaging or a genuine marker difference. *(note: SUPT_1151's children likely include both basket-enriched and stellate-enriched clusters; Grid1 distribution across children is unknown from current data.)*
- NT type not asserted at supertype level — the GABA identity of this supertype's cells cannot be confirmed from available atlas metadata. Given the cerebellar MLI biology, GABAergic identity is expected, but cannot be confirmed without supertype-level NT annotation.
- Location rollup is a lower-bound (region_count_completeness: lower_bound) — the region_fraction_100um value of 0.851 is a floor, with non-painted CCF2020 descendants uncounted. True fraction is at least 0.851.
- No annotation transfer data available. This is the primary gap: without a basket-cell-targeted source dataset mapped onto WMBv1, we cannot determine whether basket cells specifically map to SUPT_1151, to a subset of its children, or are distributed across multiple MLI supertypes.
- The basket-stellate morphological continuum [1][2][5] means that even with AT evidence, a clean 1:1 mapping to a single transcriptomic cluster may not be achievable at current atlas resolution.

**What would upgrade confidence:**
- Annotation-transfer experiment using a basket-cell-targeted source (e.g. morphologically confirmed basket cells from patch-seq, or Pvalb-Cre / Ascl1CreERT2 driver lines with morphology confirmation), mapped to WMBv1 via MapMyCells, targeting F1 ≥ 0.75 at SUPT or CLUSTER level — would add AnnotationTransferEvidence and allow predicate commitment.
- Literature trawl for "RORa basket cell cerebellum" and "HCN1 transcript cerebellar interneuron" to anchor the RORa and HCN1 markers with transcript-level primary data, and to check whether atlas-side absence for these genes is real or a dataset gap.
- Cluster-level breakdown of Grid1 expression across SUPT_1151 children — available if taxonomy YAML is extended or with direct query of atlas expression data.

---

### 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Cluster (CLUS_5185) | Supertype (SUPT_1147) | Alignment |
|---|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] count_100um=297 (painted); cerebellum related fiber tracts; arbor vitae | — | CONSISTENT |
| NT type | GABAergic | GABA | — | CONSISTENT |
| Pvalb expression | Defining marker | Mean 10.40; cohort-pct 0.978 | — | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | — | NOT_ASSESSED |
| HCN1 expression | Defining marker | No atlas expression data | — | NOT_ASSESSED |
| Kcna1 expression | Defining marker | Mean 4.43; cohort-pct 0.897 | — | CONSISTENT |
| Grid1 expression | Defining marker | Mean 5.49; cohort-pct 0.332 | — | APPROXIMATE |
| Calb1 | Absent (negative marker) | Mean 0.04; cohort-pct 0.071 | — | CONSISTENT |
| Sex ratio | Not documented | Not available | — | NOT_ASSESSED |

*(Child-cluster breakdown not applicable — this is a cluster-level node.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: CLUS_5185 cerebellar location + marker expression | Atlas metadata | PARTIAL | region_fraction_100um=0.525; Pvalb 10.40, Kcna1 4.43; Calb1 0.04 | atlas-internal |

**Supporting evidence:**
- CLUS_5185 (5185 CB PLI Gly-Gaba_4) carries NT annotation "GABA" — directly CONSISTENT with the classical GABAergic identity [5]. This is the only cluster in the top candidates with a cluster-level NT assertion matching the classical type.
- Pvalb at mean 10.40 (97.8th percentile of the 50-member GABAergic cerebellar cohort): strongly CONSISTENT with the Buttermore et al. 2012 immunostaining evidence [6].
- Kcna1 at mean 4.43 (89.7th percentile): CONSISTENT with the basket cell pinceau literature [7][8].
- Calb1 at mean 0.04, 7.1st percentile: the cleanest Calb1 absence among all cluster-level candidates assessed. CONSISTENT with classical negative marker [6].
- Location: region_fraction_100um=0.525 (lower_bound rollup). The value is a floor and reflects boundary scatter — the cluster is in cerebellar cortex territory but with registration imprecision at the boundary with related fiber tracts (cerebellum related fiber tracts; arbor vitae). *(note: boundary scatter is expected for a laminar type like basket cells, which sit at the interface of the molecular layer and deeper structures.)*
- The "CB PLI" designation in the cluster name plausibly reflects "Purkinje layer interneuron" (PLI), consistent with basket cells, which are perisomatic inhibitors of the Purkinje cell layer. Co-designation "Gly-Gaba" suggests glycine co-release — a feature reported in a subset of cerebellar interneurons, though not a defining characteristic of the classical basket cell definition in the facts available here.

**Marker evidence provenance:**
- **Pvalb, Calb1 (negative):** Same immunostaining provenance as for SUPT_1151 [6]. At cluster level, the precomputed expression values are derived from a single cluster rather than averaged across children, making them more specific but based on fewer cells (n=442).
- **Kcna1:** Same literature provenance [7][8]. Kcna1 value (4.43) is lower at cluster level than in SUPT_1151 (7.23 as supertype mean); this is consistent with CLUS_5185 representing a more specific and potentially smaller basket cell subpopulation with different pinceau density or maturation.
- **Grid1:** APPROXIMATE (mean 5.49, 33.2nd percentile). Same interpretation as SUPT_1151 — the Konno 2014 [9] mRNA evidence predicts higher MLI expression. The moderate expression here may reflect the "CB PLI" subgroup being distinct from the MLI bulk measured by Konno et al.
- **RORa, HCN1:** Not available in atlas precomputed stats — same gaps as SUPT_1151.
- ⚠ **Marker concordance note:** The supertype for this cluster (SUPT_1147: 1147 CB PLI Gly-Gaba_4) shares the same cell population (n_cells = 442 at both cluster and supertype, reflecting a 1-child supertype). The supertype-level edge (edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147) is therefore informationally near-identical to the cluster-level edge. These two edges carry the same cells; the cluster edge is preferred here for specificity.

**Concerns:**
- Location boundary scatter: region_fraction_100um=0.525 (lower_bound) places approximately 47.5% of this cluster outside the cerebellar region (or uncounted due to non-painted descendants). This is moderate uncertainty — the cluster is genuinely in the cerebellum but with significant boundary signal in fiber tracts and arbor vitae. *(note: arbor vitae is the white matter of the cerebellum; MERFISH soma registration near the molecular-layer/white-matter boundary can produce this pattern.)*
- Very small cluster (n=442 cells in the atlas). Small clusters are more susceptible to composition artefacts.
- No NT assertion at supertype level for SUPT_1147 (though cluster-level GABA annotation is present).
- Same general limitations as SUPT_1151: no AT data; basket/stellate morphological distinction not resolvable from transcriptomic data alone; RORa/HCN1 not assessable.

**What would upgrade confidence:**
- Same annotation-transfer experiment as for SUPT_1151 (morphologically confirmed basket cells → MapMyCells → WMBv1), now checking whether the basket-cell source maps specifically to CLUS_5185 / SUPT_1147 or to the CBX MLI supertypes.
- Confirmation of Kcna1 and Grid1 at transcript level in morphologically confirmed basket cells to anchor these markers with direct evidence.

---

### 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] · 🔴 LOW

**Table 1 — Property comparison**

| Property | Classical | Cluster (CLUS_5188) | Supertype (SUPT_1149) | Alignment |
|---|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974]; cerebellar cortex [UBERON:0002129] | Cerebellum [MBA:512] count_100um=84,424 (painted); Ansiform lobule; Simple lobule | — | CONSISTENT |
| NT type | GABAergic | GABA | — | CONSISTENT |
| Pvalb expression | Defining marker | Mean 11.12; cohort-pct 0.995 | — | CONSISTENT |
| RORa expression | Defining marker | No atlas expression data | — | NOT_ASSESSED |
| HCN1 expression | Defining marker | No atlas expression data | — | NOT_ASSESSED |
| Kcna1 expression | Defining marker | Mean 6.47; cohort-pct 0.946 | — | CONSISTENT |
| Grid1 expression | Defining marker | Mean 9.85; cohort-pct 0.989 | — | CONSISTENT |
| Calb1 | Absent (negative marker) | Mean 0.18; cohort-pct 0.277 | — | DISCORDANT |
| Sex ratio | Not documented | Not available | — | NOT_ASSESSED |

*(Child-cluster breakdown not applicable — this is a cluster-level node.)*

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: CLUS_5188 cerebellar location + marker expression | Atlas metadata | PARTIAL | region_fraction_100um=0.841; Pvalb 11.12 (pct 0.995), Grid1 9.85 (pct 0.989); Calb1 DISCORDANT | atlas-internal |

**Supporting evidence:**
- Pvalb at mean 11.12, 99.5th percentile — the highest Pvalb among all cluster-level candidates, strongly CONSISTENT with classical basket cell identity [6].
- Grid1 at mean 9.85, 98.9th percentile — the only candidate with a fully CONSISTENT Grid1 alignment. This is the most direct match to the Konno 2014 [9] finding that GluD1 mRNA is highest in molecular layer interneurons.
- Kcna1 at mean 6.47, 94.6th percentile: CONSISTENT with pinceau marker literature [7][8].
- Soma location: 84.1% of cells within 100 µm of cerebellar region (lower_bound; true fraction ≥ 0.841). Localisation clearly cerebellar cortex, with lobule-level detail (Ansiform lobule, Simple lobule).
- "CBX MLI" cluster name designates cerebellar cortex molecular layer interneuron — appropriate anatomical match.

**Marker evidence provenance:**
- **Pvalb, Grid1, Kcna1:** Cross-modality concordance is strongest here for these three markers. The Megf11 designation (MEGF11 = Multiple EGF Like Domains 11) suggests a marker distinguishing this cluster from the "Cdh22" supertype SUPT_1151; Megf11 biology in cerebellar interneurons is not described in the gathered literature.
- ⚠ **Calb1 DISCORDANT:** The classical negative marker is present at mean 0.18, 27.7th percentile — above the MIN_DETECTABLE threshold. Buttermore et al. 2012 [6] clearly establishes Calb1 absence in basket neurons (and Calb1 as a Purkinje cell marker). A Calb1 mean of 0.18 in this cluster is a genuine counter-signal. Possible interpretations: (a) the cluster contains a mixture of basket cells and a Calb1-expressing population (stellate cells occasionally express low Calb1, or contamination with Purkinje cell transcripts in MERFISH); (b) this cluster corresponds primarily to stellate cells, which occupy the upper molecular layer and may have low Calb1 expression; (c) the threshold between undetectable and low-level Calb1 in cerebellar interneurons is not well established at transcript level — the Buttermore evidence is protein-level. A targeted literature search for "Calb1 stellate basket cerebellum transcript" may resolve whether 0.18 is within the basket cell biological range.

**Concerns:**
- Calb1 DISCORDANT (mean 0.18) is the primary concern. Given that Calb1 is a defining positive marker for Purkinje cells and a classical negative marker for basket cells, any detectable Calb1 expression on a candidate cluster is counter-evidence. This does not eliminate CLUS_5188 (the literature evidence for the negative marker is protein-level; transcript-level may differ), but it reduces confidence and warrants investigation.
- "Megf11" in the cluster name is unattributed in the gathered literature — no primary study is available in the facts file establishing what Megf11 marks in cerebellar MLIs, and whether Megf11+ cells are basket cells, stellate cells, or both.
- Same general limitations: no AT data; RORa/HCN1 not assessable.

**What would upgrade confidence:**
- Targeted literature trawl: "Calb1 basket cell cerebellum transcript" and "Megf11 cerebellar interneuron" to resolve whether low Calb1 is biologically compatible with basket cell identity at the transcript level, and to characterise the Megf11-positive population.
- Annotation-transfer experiment (same design as above) — if basket-cell-targeted source cells map to CLUS_5188, the Calb1 discordance would need to be explained or accepted as a known subpopulation feature.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — (supertype node) | 13,098 | 🔴 LOW | Pvalb 11.33 (pct 0.991); Kcna1 7.23 (pct 0.973); Calb1 CONSISTENT; rf100=0.851 | Primary |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | 🔴 LOW | Cleanest Calb1 absence (0.04); GABA NT; Pvalb 10.40; rf100=0.525 | Secondary |
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🔴 LOW | Grid1 9.85 (pct 0.989); Pvalb 11.12; Calb1 DISCORDANT (0.18) | Supports broader mapping — Calb1 discordant |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | ⚪ UNCERTAIN | — | Eliminated (Calb1 DISCORDANT — val 0.27) |
| 5184 CB PLI Gly-Gaba_3 [CS20230722_CLUS_5184] | 1146 CB PLI Gly-Gaba_3 | 69 | ⚪ UNCERTAIN | — | Eliminated (very small cluster; Pvalb low) |
| 5267 OPC NN_1 [CS20230722_CLUS_5267] | 1179 OPC NN_1 | 210 | ⚪ UNCERTAIN | — | Eliminated (non-neuronal OPC class; wrong region) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — (supertype node) | 442 | ⚪ UNCERTAIN | — | Eliminated (same cells as CLUS_5185; cluster edge preferred) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — (supertype node) | 3,646 | ⚪ UNCERTAIN | — | Eliminated (Calb1 DISCORDANT — val 0.17) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — (supertype node) | 370 | ⚪ UNCERTAIN | — | Eliminated (Calb1 DISCORDANT — val 0.20) |
| 1115 CBN Dmbx1 Gaba_1 [CS20230722_SUPT_1115] | — (supertype node) | 3,641 | ⚪ UNCERTAIN | — | Eliminated (cerebellar nuclei, not cortex; rf100=0.136) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Cerebellar basket cell (molecular layer interneuron) is defined on a CLASSICAL_MULTIMODAL basis: GABAergic interneuron of the inner molecular layer [UBERON:0002974] of cerebellar cortex [UBERON:0002129], with defining markers Pvalb [6], RORa [2], HCN1 [7][8], Kcna1 [7], and Grid1 [9], and negative marker Calb1 [6]. Soma location and morphological definition derive from multiple sources [1][2][3][4]. The basket-stellate distinction is a morphological continuum and does not map cleanly onto current transcriptomic atlas divisions.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table (audit):**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5184 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5267 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA | PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1115 | ATLAS_METADATA | PARTIAL | atlas-internal |

*Generated by evidencell `8e05bb5` at 2026-07-09T13:25:34+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml](kb/graphs/cerebellum_blind/20260709_cerebellum_blind_report_ingest.yaml).*

</details>

---

## Discussion

**Primary mapping:** Cerebellar basket cell (molecular layer interneuron) → 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] at LOW confidence. Key support: high Pvalb (99.1st percentile) and Kcna1 (97.3rd percentile) with full child-cluster coverage; clean Calb1 negativity; strong cerebellar localisation (region_fraction_100um: 0.851). Key caveats: atlas metadata only (no annotation-transfer evidence); NT type not asserted at supertype level; Grid1 unexpectedly low (19.1st percentile); the basket/stellate morphological distinction is not resolved by current atlas transcriptomic clusters.

This classical type maps directly to the Cell Ontology term cerebellar basket cell [[CL:2000027](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:2000027)].

A secondary cluster-level candidate, 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185], provides complementary evidence at cluster resolution: it shares the Pvalb/Kcna1 marker profile, carries a direct GABA NT annotation, and has the cleanest Calb1 absence of all assessed candidates (mean 0.04). Its small size (442 cells) and boundary-range cerebellar localisation (region_fraction_100um: 0.525) make it a secondary rather than primary call.

A third candidate, 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188], has the strongest Grid1 alignment of all assessed clusters and very high Pvalb — but the Calb1 DISCORDANT signal (mean 0.18) introduces counter-evidence that is not resolvable from current data. It is included here as a weaker secondary candidate where the Calb1 discordance warrants investigation before further commitment.

The primary limitation of all three calls is the single-evidence-type basis: atlas metadata scores gene co-expression but cannot confirm cell-type identity, morphological class, or axonal organisation. The basket/stellate morphological continuum is a known complication — the WMBv1 "MLI" clusters may represent transcriptomic divisions orthogonal to the basket/stellate morphological axis, with each transcriptomic cluster containing both basket-like and stellate-like cells.

### Proposed experiments and follow-ups

1. **Annotation transfer from morphologically confirmed basket cells to WMBv1.**
   - **What:** MapMyCells (hierarchical mapping) using a source dataset containing morphologically verified basket cells (post-hoc fill after patch-clamp, or Ascl1-CreERT2 / Pvalb-Cre driver-line cells with morphology confirmation).
   - **Target:** F1 ≥ 0.75 at SUPT level, F1 ≥ 0.60 at CLUS level.
   - **Expected output:** AnnotationTransferEvidence entries on candidate edges.
   - **Resolves:** Ambiguity between SUPT_1151, CLUS_5185, CLUS_5188; determines whether basket cells are transcriptomically distinct from stellate cells in WMBv1.

2. **Targeted literature search for Calb1 at transcript level in cerebellar MLIs.**
   - **What:** Cite-traverse search on "Calb1 calbindin basket stellate cerebellum transcript scRNA-seq"; assess whether any published scRNA-seq of cerebellar MLIs shows a Calb1-expressing interneuron subtype.
   - **Expected output:** LiteratureEvidence entries on CLUS_5188 (and on SUPT_1150 / SUPT_1144 if resolved as basket-like); potential revision of the negative-marker status.
   - **Resolves:** Whether Calb1 DISCORDANT on CLUS_5188 is biologically plausible or disqualifying.

3. **Targeted literature search for RORa, HCN1, and Megf11 in cerebellar MLIs at transcript level.**
   - **What:** Cite-traverse search for "RORa cerebellar basket interneuron transcript", "HCN1 cerebellar interneuron mRNA", "Megf11 cerebellar interneuron".
   - **Expected output:** LiteratureEvidence entries potentially enabling NOT_ASSESSED → CONSISTENT/DISCORDANT resolution for RORa and HCN1; characterisation of the Megf11+ cluster.
   - **Resolves:** Two of five defining markers currently not assessable; Megf11 cluster identity.

4. **Grid1 cluster-level breakdown for SUPT_1151.**
   - **What:** Query atlas taxonomy DB or precomputed stats for Grid1 expression across child clusters of SUPT_1151 (1151 CBX MLI Cdh22 Gaba_1).
   - **Expected output:** Identification of which children carry the Grid1 signal; may point to a specific child cluster as the basket-cell-enriched node.
   - **Resolves:** Whether the APPROXIMATE Grid1 alignment at supertype level hides a CONSISTENT child cluster.

### Open questions

1. Do basket cells and stellate cells form transcriptomically distinct populations in WMBv1, or do they map to the same MLI clusters regardless of morphological identity? The classical literature [1][2][5] repeatedly notes a basket-stellate morphological continuum; current atlas metadata cannot resolve this.
2. Is the Calb1 DISCORDANT signal on CLUS_5188 (mean 0.18) within the biological range for basket cells at transcript level, or does it indicate this cluster corresponds primarily to a different MLI subtype (possibly stellate cells or a mixed population)?
3. Does the "CB PLI" (Purkinje Layer Interneuron) designation in the WMBv1 cluster names correspond specifically to basket cells (perisomatic inhibitors), and is the "CBX MLI" designation inclusive of both basket and stellate cells?
4. What is the biological significance of the Gly-Gaba co-designation in "CB PLI Gly-Gaba" clusters? Glycine co-release in basket cells has not been characterised in the gathered literature.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wang & Lefebvre 2020 | [35701402](https://pubmed.ncbi.nlm.nih.gov/35701402/) | Soma location, basket-stellate morphology |
| [2] | Brown et al. 2018 | [30742002](https://pubmed.ncbi.nlm.nih.gov/30742002/) | Soma location, RORa marker |
| [3] | Miyazaki et al. 2021 | [34658339](https://pubmed.ncbi.nlm.nih.gov/34658339/) | Soma location |
| [4] | Filho et al. 2025 | [40973045](https://pubmed.ncbi.nlm.nih.gov/40973045/) | Soma location |
| [5] | Briatore et al. 2010 | [20711348](https://pubmed.ncbi.nlm.nih.gov/20711348/) | Neurotransmitter type |
| [6] | Buttermore et al. 2012 | [22492029](https://pubmed.ncbi.nlm.nih.gov/22492029/) | Pvalb marker, Calb1 negative marker |
| [7] | Zhou et al. (eLife preprint) | — | HCN1, Kcna1 markers |
| [8] | Zhou et al. (bioRxiv preprint) | — | HCN1, Kcna1 markers |
| [9] | Konno et al. 2014 | [24872547](https://pubmed.ncbi.nlm.nih.gov/24872547/) | Grid1 marker |

---

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.35
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:STRONGEST] Metadata-only evidence: Pvalb=11.33 (cohort-pct 0.991; child-coverage
    1.000) and Kcna1=7.23 (cohort-pct 0.973; child-coverage 1.000) are highly consistent
    with the classical basket cell marker profile across all children of CS20230722_SUPT_1151;
    Calb1=0.09 (below MIN_DETECTABLE; child-coverage 1.000) is consistent with the classical
    negative marker. Grid1=1.39 (cohort-pct 0.191) is APPROXIMATE — lower than expected
    given MLI-enriched expression in Konno 2014. NT type not asserted at supertype level.
    No annotation-transfer evidence available. LOW confidence reflects single ATLAS_METADATA
    evidence item and absence of AT or literature evidence on this edge; predicate left as
    UncertainRelationship pending AT data.
  reconciliation_note: >
    SUPT_1151 (CBX MLI Cdh22 Gaba_1) is the top supertype candidate (discovery score 9,
    rank 1/50 in GABAergic cerebellar cohort). Cluster-level children not in edge set.
    Relationship to basket cell biology at supertype level uncertain — the basket/stellate
    morphological continuum predicts AT scatter across MLI supertypes. Paired secondary
    candidate: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185 at cluster level.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup — region_fraction_100um=0.851 is a
        floor; non-painted CCF2020 descendants present and uncounted.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Basket/stellate morphological continuum not resolved by transcriptomic data.
        Atlas MLI clusters may contain both basket and stellate cells. NT type not asserted
        at supertype level. No annotation-transfer or literature evidence on this edge.
  proposed_experiments:
    - >
      Annotation transfer from morphologically confirmed basket cells (post-hoc fill after
      patch-clamp or Ascl1-CreERT2/Pvalb-Cre driver lines) to WMBv1,
      targeting F1 >= 0.75 at SUPT level; would add AnnotationTransferEvidence.
    - >
      Query Atlas taxonomy DB for Grid1 expression across child clusters of CS20230722_SUPT_1151
      to determine whether APPROXIMATE supertype alignment conceals a CONSISTENT child cluster.
    - >
      Literature trawl for RORa, HCN1, and Megf11 in cerebellar MLIs at transcript level;
      would convert NOT_ASSESSED property comparisons to scored alignments.
  unresolved_questions:
    - >
      Does CS20230722_SUPT_1151 (CBX MLI Cdh22 Gaba_1) contain basket cells, stellate cells,
      or both? Annotation transfer from morphologically confirmed basket cells required to resolve.
    - >
      Why is Grid1 expression low (cohort-pct 0.191) on CS20230722_SUPT_1151 given the Konno
      2014 MLI-enriched expression finding? May reflect supertype averaging masking a
      child-cluster-specific signal.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.30
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:NEXT] Metadata-only evidence: Pvalb=10.40 (cohort-pct 0.978), Kcna1=4.43
    (cohort-pct 0.897), Calb1=0.04 (below MIN_DETECTABLE; cohort-pct 0.071) — cleanest
    Calb1 absence among cluster-level candidates. NT annotation GABA (CONSISTENT). 
    Grid1=5.49 (cohort-pct 0.332) APPROXIMATE. Location region_fraction_100um=0.525
    (lower_bound; boundary scatter with fiber tracts). Small cluster (n=442). 
    LOW confidence: single ATLAS_METADATA evidence item; no AT or literature evidence
    on edge. Predicate left as UncertainRelationship pending AT data.
  reconciliation_note: >
    CS20230722_CLUS_5185 is the cluster-level child of CS20230722_SUPT_1147 (1147 CB PLI
    Gly-Gaba_4; same 442 cells at both ranks — 1-child supertype). Cluster edge preferred
    over the supertype edge (edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147) for
    specificity. Companion supertype-level candidate is CS20230722_SUPT_1151.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup — region_fraction_100um=0.525 is a floor.
        Boundary scatter into cerebellum related fiber tracts and arbor vitae present.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Small cluster (n=442). Basket/stellate distinction not resolvable from metadata alone.
        No AT or literature evidence on this edge.
  proposed_experiments:
    - >
      Annotation transfer from morphologically confirmed basket cells to WMBv1, checking
      whether source cells land on CS20230722_CLUS_5185/SUPT_1147 or on CBX MLI supertypes.
    - >
      Literature trawl for Kcna1 and Grid1 at transcript level in morphologically confirmed
      basket cells; would provide primary transcript-level evidence for these markers.
  unresolved_questions:
    - >
      Does the "CB PLI Gly-Gaba" cluster designation map specifically to basket cells
      (perisomatic inhibitors) versus other Purkinje-layer interneuron types? The Gly-Gaba
      co-designation (glycine co-release) has not been characterised in the gathered literature.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.22
  relationship: evidencell:UncertainRelationship
  mapping_justification: semapv:ManualMappingCuration
  rationale: >
    [tier:WEAKEST] Metadata-only evidence: Pvalb=11.12 (cohort-pct 0.995) and Grid1=9.85
    (cohort-pct 0.989) are CONSISTENT — the strongest Grid1 alignment of all assessed
    clusters, matching Konno 2014 MLI-enriched expression. Kcna1=6.47 (cohort-pct 0.946)
    CONSISTENT. However, Calb1=0.18 (cohort-pct 0.277) is DISCORDANT — the classical
    negative marker is present above MIN_DETECTABLE. Location region_fraction_100um=0.841
    (lower_bound). LOW confidence: Calb1 DISCORDANT counter-evidence; single ATLAS_METADATA
    item; no AT or literature evidence. Predicate left as UncertainRelationship.
  reconciliation_note: >
    CS20230722_CLUS_5188 (CBX MLI Megf11 Gaba_1) has the strongest Grid1 and Pvalb signals
    but is downranked by the Calb1 DISCORDANT comparison (val=0.18 vs threshold 0.1).
    The Megf11 marker is uncharacterised in the gathered literature. Basket vs. stellate
    assignment for this cluster requires AT evidence or targeted literature.
  caveats:
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region signal driven by lower_bound rollup — region_fraction_100um=0.841 is a floor.
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        Calb1=0.18 is DISCORDANT against classical negative marker. Megf11 cluster identity
        unknown from gathered literature. Basket/stellate distinction not resolvable from
        metadata alone.
  proposed_experiments:
    - >
      Literature trawl for Calb1 at transcript level in cerebellar MLI subtypes to determine
      whether Calb1 mean 0.18 is within biological range for basket cells, or indicative of
      stellate cell or mixed composition.
    - >
      Literature trawl for Megf11 in cerebellar molecular layer interneurons to characterise
      the Megf11+ cluster identity (basket vs. stellate vs. mixed).
    - >
      Annotation transfer from morphologically confirmed basket cells to resolve whether
      CS20230722_CLUS_5188 receives basket-cell AT signal despite the Calb1 discordance.
  unresolved_questions:
    - >
      Is Calb1=0.18 on CS20230722_CLUS_5188 within biological range for basket cells at
      transcript level, or does it indicate this cluster corresponds primarily to stellate
      cells or a mixed population? Trawl literature for Calb1 transcript data in cerebellar
      MLI subtypes.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Calb1=0.27 (cohort-pct 0.435) DISCORDANT — the strongest Calb1 signal
    among all assessed candidates, clearly above MIN_DETECTABLE; disqualifying against
    classical negative marker. Pvalb and Kcna1 are consistent but the Calb1
    counter-evidence is decisive in the absence of any AT or literature data on this edge.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5184 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.08
  rationale: >
    [tier:CUT] Very small cluster (n=69 cells); Pvalb=1.56 (cohort-pct 0.772) is 
    notably lower than other cerebellar GABAergic candidates, suggesting weaker marker
    expression. Calb1=0.00 CONSISTENT and Grid1=8.20 (pct 0.652) CONSISTENT are
    positive signals but insufficient to compensate given small cell count and lower
    Pvalb. Single ATLAS_METADATA evidence item.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5267 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.02
  rationale: >
    [tier:CUT] Cluster name "OPC NN_1" indicates oligodendrocyte precursor cell —
    a non-neuronal cell type inconsistent with the classical basket cell definition.
    NT type not asserted (vs. classical GABAergic). Location APPROXIMATE with
    region_fraction_100um=0.135 (primarily midbrain and pons, not cerebellum).
    Pvalb=0.32 is low. Multiple lines of evidence against basket cell identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.15
  rationale: >
    [tier:CUT] CS20230722_SUPT_1147 (1147 CB PLI Gly-Gaba_4) is the single-child
    supertype of CS20230722_CLUS_5185, containing the same 442 cells. The cluster-level
    edge (edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185) is preferred for
    specificity and is carried as a secondary survivor. This supertype edge is
    informationally redundant with the cluster edge; retaining both would create a
    confusing duplication.
  unresolved_questions:
    - >
      Curator should consider removing edge edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147
      as redundant with the cluster-level edge edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185
      (same 442 cells; 1-child supertype).
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Calb1=0.17 (cohort-pct 0.182) DISCORDANT — above MIN_DETECTABLE;
    counter-evidence against classical negative marker. CS20230722_SUPT_1144 is the
    supertype of CS20230722_CLUS_5178 (which itself was cut for stronger Calb1=0.27
    DISCORDANT). Low Calb1 expected for basket cells is not met at this supertype.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.10
  rationale: >
    [tier:CUT] Calb1=0.20 (cohort-pct 0.218) DISCORDANT — above MIN_DETECTABLE.
    Despite strong Pvalb (10.71, pct 0.982, DEFINING atlas category) and reasonable
    Kcna1 (5.40, pct 0.909), the Calb1 counter-evidence and lower discovery score
    (rank 4/50 at supertype level) place this candidate below threshold in the absence
    of any AT or literature evidence.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1115 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.04
  rationale: >
    [tier:CUT] CS20230722_SUPT_1115 (1115 CBN Dmbx1 Gaba_1) — "CBN" designates
    cerebellar nuclei, not cerebellar cortex. Location APPROXIMATE with
    region_fraction_100um=0.136 (the smallest cerebellar proximity fraction among all
    supertype candidates). NT type not asserted. Classical basket cells reside in the
    molecular layer of cerebellar cortex, not in the deep cerebellar nuclei. Wrong
    subregion disqualifies this candidate.
```
<!-- verdict-block-end -->
