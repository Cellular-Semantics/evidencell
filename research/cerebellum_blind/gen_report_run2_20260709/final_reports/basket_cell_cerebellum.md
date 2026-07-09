# Cerebellar basket cell (molecular layer interneuron) — WMBv1 (CCN20230722) Mapping Report
*2026-07-09 · Source: `kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml`*

---

## Introduction

Cerebellar basket cells are GABAergic interneurons of the molecular layer of the cerebellar cortex [UBERON:0002974] that provide perisomatic and axon-initial-segment inhibition onto Purkinje cells [1][2][3][4]. They are classically distinguished from stellate cells by soma position in the lower third of the molecular layer and by the formation of perisomatic basket terminals and specialised pinceau synapses at the Purkinje cell axon initial segment — a basket-stellate division that has long been debated, as morphological variation suggests these two types may form a continuum [1][2][4]. Mapping basket cells onto the WMBv1 transcriptomic atlas is complicated by this morphological continuum: at the transcriptomic level, basket cells (source cluster MLI1_1) and stellate cells (MLI1_2) both resolve to the same WMBv1 cluster, a cross-cutting relationship that the AT evidence narrates directly and honestly.

**Location note.** WMBv1 location data derives from MERFISH spatial registration and records **soma position** only. Axonal and dendritic projection targets — including the pinceau at the Purkinje cell axon initial segment — are not reflected in atlas cluster location fields and are not used in mapping assessments. All region fraction values in this report are lower-bound estimates because the canonical rollup rows include non-painted CCF2020 descendants whose cells are uncounted.

### Classical type summary

| Property | Value | References |
|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] (inner/lower third); cerebellar cortex [UBERON:0002129] (coarse query) | [1][2][3][4] |
| Neurotransmitter | GABAergic | [5] |
| Defining markers | Pvalb, RORa, HCN1, Kcna1, Grid1 | [6][2][7][8][7][9] |
| Negative markers | Calb1 | [6] |
| Cell Ontology | cerebellar basket cell [CL:2000027] (EXACT) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** immunostaining · Wang & Lefebvre 2022 [1]
- **Soma location:** morphological classification · Brown et al. 2018 [2]
  > The distribution of reporter expression in stellate versus basket cells was validated by RAR-related orphan receptor alpha (RORα) expression (Fig. 2c, per condition: N = 3, n = 9), which also marks molecular layer interneurons and Purkinje cells (Maricich et al., 1999)(Hamilton et al., 1996)(Ino, 2004)(Sillitoe et al., 2008)
  > — Brown et al. 2018, Anatomical organization and core cell types · [2] <!-- quote_key: 59945454_b21703e0 -->
- **Soma location:** immunostaining · Miyazaki et al. 2021 [3]
  > lower MLIs or basket cells (ΔMLI), that is, PV-labeled somata in the lower ML VIAAT-labeled presynaptic terminals around PC somata, and PV/VIAAT-labeled pinceau formation at the base of PC somata
  > — Miyazaki et al. 2021, Results · [3] <!-- quote_key: 239017682_320a7a9b -->
- **Soma location:** review · Filho et al. 2025 [4]
  > basket and stellate cells refine Purkinje cell output through somatic and dendritic inhibition, respectively.
  > — Filho et al. 2025, CEREBELLAR CYTOARCHITECTURE · [4] <!-- quote_key: 281405540_ab65a557 -->
- **Neurotransmitter (GABAergic):** Briatore et al. 2010 [5]
  > Stellate and basket cells are the only ML interneurons (MLIs) known to use GABA as a neurotransmitter (Shepherd, 1974). They are distinguished by their position in the upper and lower ML and by their axonal distribution [1,3], although intermediate forms have been described, raising the possibility that MLIs represent a continuum that varies gradually (Sultan et al., 1998)(Schilling et al., 2008).
  > — Briatore et al. 2010, Anatomical organization and core cell types · [5] <!-- quote_key: 1460508_88d765d5 -->
- **Pvalb (defining marker):** immunostaining · Buttermore et al. 2012 [6]
  > We performed immunostaining of wild-type cerebellar sections against parvalbumin (Parv) to label both Purkinje neurons and molecular layer interneurons, including basket neurons (Bastianelli, 2008). We also immunostained for Calb as a specific marker for Purkinje neurons (Nordquist et al., 1988), pNfl as a marker for basket neuron collaterals, and potassium channels (K V 1.2) to label the core of the pinceau formed by basket axon terminals that target the Purkinje AIS. As shown in Figure 1, coimmunostaining against Parv and Calb at P10 shows Parv expression in basket neurons (b) (Fig. 1 Aa,b) in the vicinity of the Purkinje neurons. Note that Parv is also expressed in Purkinje neurons (Fig. 1 Ab, merged yellow color), but Calb is not expressed in basket neurons
  > — Buttermore et al. 2012, Anatomical organization and core cell types · [6] <!-- quote_key: 41293753_2d217397 -->
- **RORa (defining marker):** immunostaining · Brown et al. 2018 [2] — see RORa quote above.
- **HCN1, Kcna1 (defining markers):** Wang & Lefebvre 2022 [1]; preprints [7][8]
  > Basket cells form dense inhibitory plexuses that wrap Purkinje cell somata and terminate as pinceaux at the initial segment of axons. Here, we demonstrate that HCN1, Kv1.1, PSD95 and GAD67 unexpectedly mark patterns of basket cell pinceaux that map onto Purkinje cell functional zones.
  > — Wang & Lefebvre 2022, Connectivity and circuit motifs · [1] <!-- quote_key: 222167171_a9c43f32 -->
- **Grid1 (defining marker):** immunostaining/electrophysiology · Konno et al. 2014 [9]
  > In the cerebellar cortex, GluD1 mRNA was expressed at the highest level in molecular layer interneurons and its immunoreactivity was concentrated at PF synapses on interneuron somata.
  > — Konno et al. 2014, Functional roles and physiology · [9] <!-- quote_key: 8585958_c30f821f -->
- **Calb1 (negative marker):** immunostaining · Buttermore et al. 2012 [6] — see Pvalb quote above; Calb not expressed in basket neurons but expressed in Purkinje neurons.

</details>

### Cell Ontology mapping

Cell Ontology mapping: cerebellar basket cell [[CL:2000027](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:2000027)] (EXACT).

---

## Results

Annotation-transfer evidence from Kozareva et al. 2021 basket-cell source nuclei (MLI1_1; GEO:GSE165371) and marker alignment support mapping cerebellar basket cells to the supertype 1149 CBX MLI Megf11 Gaba_1 [CS20230722_SUPT_1149], with the single child cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] as the best cluster-level target (F1=0.51 at cluster; see property comparison tables). A critical caveat shapes this mapping: MLI1_1 (basket) and MLI1_2 (stellate) both transfer predominantly to CLUS_5188 with nearly identical coverage (~1.0) but low purity for each source (~0.34 for basket), indicating that WMBv1 does not resolve the basket–stellate transcriptomic boundary at the cluster level — a well-documented biological feature of cerebellar MLI organisation.

*(No filtered AT figure was generated in this run; embed a node-scoped figure using `just gen-at-figure at_run_20260709_kozareva_cerebellum_mmc_wmbv1 --source MLI1_1` when pipeline tooling is available.)*

---

### 1149 CBX MLI Megf11 Gaba_1 [CS20230722_SUPT_1149] · 🟡 MODERATE

**Table 1 — Property comparison (supertype)**

| Property | Classical | Supertype [CS20230722_SUPT_1149] | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | no atlas anat data (supertype lacks MERFISH registration rows) | NOT_ASSESSED |
| NT type | GABAergic | not asserted at supertype level | NOT_ASSESSED |
| Pvalb expression | defining marker | 10.51; cohort_pct 0.973; child-coverage 1.000 | CONSISTENT |
| RORa expression | defining marker | no atlas expression data | NOT_ASSESSED |
| HCN1 expression | defining marker | no atlas expression data | NOT_ASSESSED |
| Kcna1 expression | defining marker | 5.82; cohort_pct 0.945; child-coverage 1.000 | CONSISTENT |
| Grid1 expression | defining marker | 8.96; cohort_pct 0.955; child-coverage 1.000 | CONSISTENT |
| Calb1 (negative) | ABSENT | 0.31; cohort_pct 0.355 | DISCORDANT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node metadata | Atlas metadata | PARTIAL | region data absent at supertype level | atlas-internal |
| MapMyCells AT (MLI1_1) | Annotation transfer | PARTIAL | F1=0.50 at supertype level (`at_run_20260709_kozareva_cerebellum_mmc_wmbv1`) | atlas-internal |

*(Child-cluster breakdown: CLUS_5188 is the sole resolved cluster within this supertype in the top-K set; Calb1 DISCORDANT on both. Child-cluster breakdown across all supertype members not assessed — see proposed experiments.)*

Marker expression alignment and annotation-transfer evidence from Kozareva et al. 2021 mouse cerebellar snRNA-seq basket-cell nuclei (MLI1_1, n=10,998 source cells; `at_run_20260709_kozareva_cerebellum_mmc_wmbv1`) supports mapping cerebellar basket cells to the supertype 1149 CBX MLI Megf11 Gaba_1 [CS20230722_SUPT_1149] at MODERATE confidence (see property comparison table). Coverage of MLI1_1 source cells is essentially complete at supertype level (0.999), confirming that virtually all basket-source nuclei land within this lineage. Three of five assessed markers are CONSISTENT with the basket-cell profile: Pvalb (cohort pct 0.973, child-coverage 1.000), Kcna1 (cohort pct 0.945, child-coverage 1.000), and Grid1 (cohort pct 0.955, child-coverage 1.000). The Calb1 negative-marker comparison is DISCORDANT (mean 0.31, cohort pct 0.355), and RORa and HCN1 are NOT_ASSESSED (absent from precomputed atlas expression data).

The mapping is at supertype level rather than cluster level because the transcriptomic cluster 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] is shared between basket (MLI1_1) and stellate (MLI1_2) source groups: both transfer there with near-complete coverage but low purity (~0.34 each), reflecting the well-established biological continuum between basket and stellate cells in the cerebellar molecular layer. The supportable mapping is therefore at supertype breadth, with CLUS_5188 named as the best cluster correspondence despite the cross-cutting biology.

**Marker evidence notes:**

- **Pvalb:** Protein-level evidence from immunostaining on morphologically identified basket cells (Buttermore et al. 2012 [6]; Miyazaki et al. 2021 [3]). Atlas precomputed expression at SUPT_1149 is high (10.51, cohort pct 0.973), confirming transcript-level consistency. Evidence quality: strong.
- **RORa:** Protein-level (immunostaining) in Brown et al. 2018 [2]; absent from atlas precomputed expression — NOT_ASSESSED at atlas level. This is a methodological gap (precomputed stats do not include RORa for this cluster lineage), not a contradiction.
- **HCN1:** Documented via pinceau immunostaining (Wang & Lefebvre 2022 [1]; preprints [7][8]); absent from atlas precomputed expression — NOT_ASSESSED. Same methodological gap as RORa.
- **Kcna1:** Kv1.1 protein evidence co-localised with HCN1 at basket cell pinceaux (Wang & Lefebvre 2022 [1]); atlas expression CONSISTENT (5.82, cohort pct 0.945).
- **Grid1:** GluD1 mRNA in molecular layer interneurons (Konno et al. 2014 [9]); atlas expression CONSISTENT (8.96, cohort pct 0.955).
- **Calb1 (negative marker):** Immunostaining on identified basket cells shows Calb1 absent in basket neurons but present in Purkinje neurons (Buttermore et al. 2012 [6]). The DISCORDANT atlas value (0.31, cohort pct 0.355) is low in absolute terms but above MIN_DETECTABLE. *(note: the classical Calb1-absence evidence comes from a basket + Purkinje preparation at P10; MLI1 cluster Calb1 could reflect contaminating Purkinje transcripts in the snRNA-seq preparation, or low-level Calb1 in a basket-cell subpopulation not sampled by early-postnatal immunostaining — this warrants investigation but does not by itself refute the mapping.)*

**Concerns:**

- Calb1 DISCORDANT: atlas mean 0.31 at SUPT_1149 (cohort pct 0.355), above MIN_DETECTABLE. The classical literature is clear that basket cells do not express Calb1 at the protein level; the atlas-side mean expression warrants investigation (snRNA-seq contamination, subpopulation heterogeneity, or developmental timing). This is the primary unresolved counter-evidence.
- RORa and HCN1 are NOT_ASSESSED — the atlas lacks precomputed expression for these basket-cell discriminators, leaving a significant marker-evidence gap that cannot be resolved from current atlas metadata alone.
- Region data absent at supertype level: SUPT_1149 lacks MERFISH-derived soma-location rows in the atlas, so the cerebellar-cortex molecular-layer specificity cannot be confirmed from atlas metadata at this resolution tier. Child cluster CLUS_5188 provides this (region_fraction_100um=0.841).

**What would upgrade confidence:**

- Direct annotation-transfer using a basket-cell-specific snRNA-seq or patch-seq dataset where cells were morphologically confirmed as basket cells (pinceaux identified) before sequencing — this would allow distinguishing basket from stellate within the MLI1 cluster and substantially improve purity.
- Precomputed expression for RORa, HCN1 in the WMBv1 reference could resolve the two currently NOT_ASSESSED markers.
- Investigation of the Calb1 discrepancy: Is the atlas-side mean driven by a minority of cells? A single-cell-level query of Calb1 expression within CLUS_5188 would clarify.

---

### 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] · 🟡 MODERATE

**Table 1 — Property comparison (cluster)**

| Property | Classical | Cluster [CS20230722_CLUS_5188] | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512] (region_fraction_100um=0.841; lower_bound) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Pvalb expression | defining marker | 11.12; cohort_pct 0.995 | CONSISTENT |
| RORa expression | defining marker | no atlas expression data | NOT_ASSESSED |
| HCN1 expression | defining marker | no atlas expression data | NOT_ASSESSED |
| Kcna1 expression | defining marker | 6.47; cohort_pct 0.946 | CONSISTENT |
| Grid1 expression | defining marker | 9.85; cohort_pct 0.989 | CONSISTENT |
| Calb1 (negative) | ABSENT | 0.18; cohort_pct 0.277 | DISCORDANT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.841 (lower_bound); strict=0.720 | atlas-internal |
| MapMyCells AT (MLI1_1) | Annotation transfer | PARTIAL | F1=0.51 at cluster level (`at_run_20260709_kozareva_cerebellum_mmc_wmbv1`) | atlas-internal |

*(Concordance: 3 of 5 assessed markers CONSISTENT (Pvalb, Kcna1, Grid1), 1 DISCORDANT (Calb1), 2 NOT_ASSESSED (RORa, HCN1). The cross-cutting biology — basket+stellate sharing this cluster — is the central structural caveat.)*

Annotation-transfer evidence from Kozareva et al. 2021 basket-cell (MLI1_1) source nuclei and marker expression alignment support a cluster-level correspondence to 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence, with the important qualification that this cluster is transcriptomically shared between basket (MLI1_1) and stellate (MLI1_2) cell types. The AT result (F1=0.51 at cluster; coverage=0.999; purity=0.34) documents both the specific assignment of basket-source nuclei to this cluster and the limitation: because stellate-source nuclei (MLI1_2) also transfer to CLUS_5188 at comparable coverage, purity is ~0.34 rather than the >0.75 that would be expected from a fully discriminating mapping. This reflects the transcriptomic reality of cerebellar MLI biology: basket and stellate cells share a common transcriptomic identity at the resolution WMBv1 provides, consistent with the morphological-continuum literature [1][5].

Three of five assessed markers are CONSISTENT: Pvalb (11.12, cohort pct 0.995 — the highest-ranked marker in the cohort), Kcna1 (6.47, cohort pct 0.946), and Grid1 (9.85, cohort pct 0.989). NT type (GABA) and soma location in the cerebellum (region_fraction_100um=0.841, lower_bound) are CONSISTENT. Calb1 is DISCORDANT (0.18, cohort pct 0.277, above MIN_DETECTABLE). RORa and HCN1 are NOT_ASSESSED.

**Concerns:**

- **Cross-cutting mapping (primary structural caveat):** MLI1_1 (basket) and MLI1_2 (stellate) both assign to CLUS_5188 with near-identical coverage but purity ~0.34 each. This is not a mapping failure — it accurately reflects the literature consensus that basket and stellate cells occupy overlapping transcriptomic space at current atlas resolution. The mapping is to be read as a cross-cutting correspondence at cluster level: both basket and stellate classical types share this cluster. The supertype-level mapping (SUPT_1149) carries the same cross-cutting property.
- **Calb1 DISCORDANT:** mean 0.18 (cohort pct 0.277) in CLUS_5188. At cluster level the value is slightly lower than at the supertype mean (0.31), but remains above MIN_DETECTABLE. *(note: could reflect contaminating Purkinje snRNA-seq nuclei or a basket-cell subpopulation — requires single-cell investigation.)*
- **Region_fraction_100um is a lower-bound floor:** true cerebellar fraction may be higher; the value (0.841) already strongly supports cerebellar localisation.

**What would upgrade confidence:**

- A basket-cell-specific dataset (morphologically confirmed) would resolve purity and allow a direct 1:1 mapping rather than a cross-cutting call. This is the single most impactful follow-up experiment.
- Precomputed expression for RORa and HCN1 at CLUS_5188 would allow two currently unassessed markers to contribute to the alignment.

---

### 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] · 🔴 LOW

**Table 1 — Property comparison (supertype)**

| Property | Classical | Supertype [CS20230722_SUPT_1151] | Alignment |
|---|---|---|---|
| Soma location | Molecular layer of cerebellar cortex [UBERON:0002974] | Cerebellum [MBA:512] (region_fraction_100um=0.851; lower_bound) | CONSISTENT |
| NT type | GABAergic | not asserted | NOT_ASSESSED |
| Pvalb expression | defining marker | 11.33; cohort_pct 0.991; child-coverage 1.000 | CONSISTENT |
| RORa expression | defining marker | no atlas expression data | NOT_ASSESSED |
| HCN1 expression | defining marker | no atlas expression data | NOT_ASSESSED |
| Kcna1 expression | defining marker | 7.23; cohort_pct 0.973; child-coverage 1.000 | CONSISTENT |
| Grid1 expression | defining marker | 1.39; cohort_pct 0.191; child-coverage 1.000 | APPROXIMATE |
| Calb1 (negative) | ABSENT | 0.09; cohort_pct 0.073 | CONSISTENT |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas node metadata | Atlas metadata | PARTIAL | region_fraction_100um=0.851 (lower_bound); strict=0.723 | atlas-internal |
| MapMyCells AT (MLI1_1) | Annotation transfer | PARTIAL | Best F1 0.39 at class level only (`at_run_20260709_kozareva_cerebellum_mmc_wmbv1`) | atlas-internal |

*(Child-cluster breakdown not assessed in the top-K set — see proposed experiments.)*

Atlas metadata and marker expression support supertype 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] as a secondary candidate for cerebellar basket cell at LOW confidence. Pvalb is strongly CONSISTENT (11.33, cohort pct 0.991, child-coverage 1.000) and Kcna1 CONSISTENT (7.23, cohort pct 0.973), and Calb1 is appropriately absent (0.09, cohort pct 0.073 — CONSISTENT). The cerebellar soma location is confirmed (region_fraction_100um=0.851, lower_bound). However, the AT evidence provides only class-level resolution (best F1=0.39 at the 28 CB GABA class) — the MLI1_1 source does not transfer to this supertype's lineage at subclass or higher resolution, indicating that the atlas' transcriptomic assignment of MLI1_1 basket cells does not place them in the SUPT_1151 lineage. Grid1 is APPROXIMATE (1.39, cohort pct 0.191), substantially lower than the primary candidate SUPT_1149 (8.96). This supertype carries the "Cdh22" name rather than "Megf11", suggesting a distinct molecular identity from the primary candidate lineage.

**Concerns:**

- AT evidence resolves only to class level — no basket-source cells land in SUPT_1151 or its lineage at supertype or cluster resolution. This is a strong negative AT signal: the basket-cell transcriptome predominantly assigns to the Megf11 lineage, not the Cdh22 lineage.
- Grid1 is low (1.39 mean, cohort pct 0.191) relative to classical expectation; APPROXIMATE alignment reflects real expression but at below-median cohort specificity.
- NT type not asserted at supertype level — limits property alignment.

**What would upgrade confidence:**

- If a basket-cell-specific dataset transferred with high F1 to SUPT_1151 (rather than SUPT_1149), this candidate would warrant re-evaluation. At present, the AT evidence actively distinguishes SUPT_1151 from the primary hit.
- Targeted literature search for "Cdh22 cerebellar interneuron" to determine whether this lineage has been characterised in the classical literature.

---

<details>
<summary>### Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| 1149 CBX MLI Megf11 Gaba_1 [CS20230722_SUPT_1149] | — (is supertype) | — | 🟡 MODERATE | Pvalb/Kcna1/Grid1 CONSISTENT; AT coverage 0.999 at supertype | Primary (supertype broadMatch) |
| 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] | 1149 CBX MLI Megf11 Gaba_1 | 31,095 | 🟡 MODERATE | AT F1=0.51 at cluster; basket+stellate cross-cutting (purity ~0.34) | Secondary (best cluster, cross-cutting) |
| 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] | — (is supertype) | 13,098 | 🔴 LOW | Pvalb/Kcna1 CONSISTENT; AT class-level only; Grid1 low (1.39) | Tertiary (secondary MLI supertype) |
| 5185 CB PLI Gly-Gaba_4 [CS20230722_CLUS_5185] | 1147 CB PLI Gly-Gaba_4 | 442 | — | PLI type; AT class-level only | Eliminated (PLI cell type, not basket) |
| 5178 CB PLI Gly-Gaba_1 [CS20230722_CLUS_5178] | 1144 CB PLI Gly-Gaba_1 | 3,066 | — | PLI type; Calb1 DISCORDANT; AT class-level only | Eliminated (PLI cell type, not basket) |
| 5184 CB PLI Gly-Gaba_3 [CS20230722_CLUS_5184] | 1146 CB PLI Gly-Gaba_3 | 69 | — | PLI type; n=69 cells; AT class-level only | Eliminated (PLI cell type; very small cluster) |
| 5267 OPC NN_1 [CS20230722_CLUS_5267] | 1179 OPC NN_1 | 210 | — | Non-neuronal; midbrain/pons location (region_fraction_100um=0.135); no AT transfer | Eliminated (wrong class, wrong region) |
| 1147 CB PLI Gly-Gaba_4 [CS20230722_SUPT_1147] | — (is supertype) | 442 | — | PLI supertype; AT class-level only | Eliminated (PLI supertype, not basket) |
| 1144 CB PLI Gly-Gaba_1 [CS20230722_SUPT_1144] | — (is supertype) | 3,646 | — | PLI supertype; Calb1 DISCORDANT; AT class-level only | Eliminated (PLI supertype, not basket) |
| 1150 CBX MLI Megf11 Gaba_2 [CS20230722_SUPT_1150] | — (is supertype) | 370 | — | Sibling MLI supertype; Grid1 low (4.18, 23.6th pct); Calb1 DISCORDANT; AT subclass-level only | Eliminated (sibling MLI supertype; inferior marker profile) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The cerebellar basket cell is defined on a CLASSICAL_MULTIMODAL basis: GABAergic neurotransmitter type confirmed by immunostaining [5]; Pvalb as a defining marker at both protein and transcript levels [6][3]; RORa as a marker validated in Cre-line reporter mice [2]; HCN1 and Kv1.1 (Kcna1) marking basket cell pinceaux via immunostaining [1][7][8]; Grid1 (GluD1) expressed at highest level in molecular layer interneurons [9]; Calb1 as a negative marker (absent in basket cells, positive in Purkinje cells; [6]). Soma location in the lower molecular layer of the cerebellar cortex is established by multiple independent studies [1][2][3][4].

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 (CCN20230722) taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer.**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE165371 (MLI1_1 — basket cells per Kozareva et al. 2021 / Osorno et al. 2022) |
| Source species | NCBITaxon:10090 (mouse) |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper 1.7.1, default parameters, 100 bootstrap iterations) |
| Tool version | cell_type_mapper 1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 45,555 (all interneurons; no post-filter) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260709_kozareva_cerebellum_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Same-species (mouse) snRNA-seq → WMBv1. MLI1_1 (basket) and MLI1_2 (stellate) both map to CLUS_5188 with high coverage but MLI1_1 purity ~0.34 — basket+stellate share the MLI1 transcriptomic cluster. BKP web backend unavailable (HTTP 400) at run time; local backend used. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source evidence_items fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table:**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1149 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5188 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1151 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5178 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5184 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_CLUS_5267 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; NO_EVIDENCE | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1144 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |
| edge_basket_cell_cerebellum_to_CS20230722_SUPT_1150 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; PARTIAL | atlas-internal |

*Generated by evidencell `f4ce9b9` at 2026-07-09T18:53:50+00:00 from [kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml](kb/graphs/cerebellum_blind/20260709_cerebellum_blind_run2.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Cerebellar basket cell (molecular layer interneuron) → 1149 CBX MLI Megf11 Gaba_1 [CS20230722_SUPT_1149] and 5188 CBX MLI Megf11 Gaba_1 [CS20230722_CLUS_5188] at MODERATE confidence. Key support: marker alignment (Pvalb/Kcna1/Grid1 CONSISTENT), annotation-transfer coverage from Kozareva et al. 2021 basket-source nuclei (coverage ~1.0 at supertype and cluster). Key caveat: cross-cutting biology — MLI1_1 (basket) and MLI1_2 (stellate) both map to CLUS_5188 with high coverage but low purity (~0.34), reflecting the morphological-continuum nature of cerebellar molecular layer interneurons and the inability of WMBv1 to resolve basket from stellate at the cluster level. A second caveat is the Calb1 DISCORDANT signal at SUPT_1149 and CLUS_5188 (above MIN_DETECTABLE), which conflicts with protein-level evidence of Calb1 absence in basket cells.

The Cell Ontology maps this classical type directly to cerebellar basket cell [[CL:2000027](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:2000027)] (EXACT).

The cross-cutting nature of the mapping at WMBv1 cluster resolution means the same atlas cluster (CLUS_5188) receives basket and stellate cell mappings simultaneously. This is biologically correct — it captures the transcriptomic reality — but it means the basket cell mapping cannot be read as a clean 1:1 correspondence at cluster level. The supertype mapping (SUPT_1149) is the broadest defensible resolution.

### Proposed experiments and follow-ups

1. **Basket-cell-specific annotation transfer** (highest priority): Retrieve a dataset where basket cells were identified by morphological criteria (pinceau immunostaining for Kv1.1/HCN1, or biocytin fill) before or after single-cell sequencing. Run MapMyCells against WMBv1 (CCN20230722). Target: F1 ≥ 0.75 at cluster level with purity > 0.75 — this would distinguish basket from stellate within the MLI1 transcriptomic cluster and allow a 1:1 assignment rather than a cross-cutting call. Expected output: AnnotationTransferEvidence on the surviving edges.

2. **Calb1 expression investigation**: Query single-cell Calb1 expression within CLUS_5188 to determine whether the mean (0.18 at cluster; 0.31 at supertype) is driven by a minority of cells with high expression (contaminating non-basket nuclei) or by low-level expression across the cluster. If the former, the mapping remains sound and the Calb1 discordance reflects snRNA-seq preparation noise rather than biology.

3. **Precomputed expression for RORa and HCN1**: If these markers can be added to the WMBv1 precomputed expression store for the CBX MLI lineage, the two currently NOT_ASSESSED comparisons would contribute to alignment scoring.

4. **Secondary candidate investigation (SUPT_1151)**: Determine whether the 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] lineage represents a distinct interneuron population or a transcriptomic sister clade of the basket/stellate pool. A targeted literature search for "Cdh22 cerebellar interneuron" or "Cdh22 molecular layer interneuron" may resolve this without new experiments.

### Open questions

1. Does WMBv1 resolve basket cells from stellate cells at any taxonomy level? The current evidence (AT purity ~0.34 for each source group at cluster) suggests no, consistent with the Kozareva et al. 2021 transcriptomic analysis. Future atlas iterations with higher resolution may separate these.
2. Is the Calb1 mean expression at CLUS_5188 (0.18) and SUPT_1149 (0.31) biologically real (basket-cell Calb1 in a subpopulation) or a technical artefact of snRNA-seq nuclear preparation? The classical immunostaining evidence (Buttermore et al. 2012 [6]) is unambiguous at the protein level in P10 mouse tissue.
3. What is the biological identity of the 1151 CBX MLI Cdh22 Gaba_1 [CS20230722_SUPT_1151] lineage relative to the basket/stellate MLI types? Its distinct Grid1 expression (1.39 vs 8.96 at SUPT_1149) and separate Cdh22 name marker suggest a genuinely distinct molecular subpopulation.
4. Are the PLI-lineage clusters (5178, 5185, 5184 and their supertypes) in the candidate set a scoring artefact (Pvalb cross-reactivity) or do they represent a genuine ambiguity at the basket cell / PLI boundary? *(note: PLI cells — candelabrum, globular, Lugaro — are a distinct cerebellar interneuron class not basket cells by any classical definition. Their presence in the top-K likely reflects Pvalb expression shared across cerebellar interneurons and should be addressed by stricter marker-combination filtering in future runs.)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Wang & Lefebvre 2022 | [35701402](https://pubmed.ncbi.nlm.nih.gov/35701402/) | Soma location, HCN1/Kcna1 markers |
| [2] | Brown et al. 2018 | [30742002](https://pubmed.ncbi.nlm.nih.gov/30742002/) | Soma location, RORa marker |
| [3] | Miyazaki et al. 2021 | [34658339](https://pubmed.ncbi.nlm.nih.gov/34658339/) | Soma location, Pvalb marker |
| [4] | Filho et al. 2025 | [40973045](https://pubmed.ncbi.nlm.nih.gov/40973045/) | Soma location |
| [5] | Briatore et al. 2010 | [20711348](https://pubmed.ncbi.nlm.nih.gov/20711348/) | Neurotransmitter type |
| [6] | Buttermore et al. 2012 | [22492029](https://pubmed.ncbi.nlm.nih.gov/22492029/) | Pvalb marker, Calb1 negative marker |
| [7] | https://doi.org/10.7554/eLife.55569 | — | HCN1, Kcna1 markers |
| [8] | https://doi.org/10.1101/2020.01.28.923896 | — | HCN1 marker |
| [9] | Konno et al. 2014 | [24872547](https://pubmed.ncbi.nlm.nih.gov/24872547/) | Grid1 marker |

---

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1149 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.55
  relationship: skos:broadMatch
  mapping_cardinality: "1:n"
  mapping_justification: semapv:CompositeMatching
  rationale: >
    [tier:STRONGEST] Pvalb (CONSISTENT; cohort_pct 0.973), Kcna1 (CONSISTENT; cohort_pct 0.945), Grid1 (CONSISTENT; cohort_pct 0.955) all align at CS20230722_SUPT_1149 with child-coverage 1.000 across all three markers; 3 of 5 assessed markers CONSISTENT. AT coverage of MLI1_1 basket-source cells at CS20230722_SUPT_1149 is 0.999 in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (F1=0.50 at supertype level), confirming basket nuclei land within this lineage. Cross-cutting biology (basket MLI1_1 and stellate MLI1_2 both mapping to the CS20230722_CLUS_5188 child with purity ~0.34 each) motivates broadMatch rather than closeMatch — the supertype is the broadest defensible resolution. Calb1 DISCORDANT (val=0.31, cohort_pct 0.355) is unresolved counter-evidence. Region data absent at supertype level (lacks MERFISH rows); child cluster provides cerebellar confirmation.
  reconciliation_note: >
    Paired with edge_basket_cell_cerebellum_to_CS20230722_CLUS_5188 (best child cluster): basket and stellate source groups (MLI1_1, MLI1_2 from at_run_20260709_kozareva_cerebellum_mmc_wmbv1) both map to CS20230722_CLUS_5188 with coverage ~1.0 but purity ~0.34 each, reflecting basket+stellate cross-cutting at WMBv1 cluster resolution. CS20230722_SUPT_1149 is the broadMatch parent; CS20230722_CLUS_5188 is the best-cluster child.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        AT purity for MLI1_1 (basket) at CS20230722_CLUS_5188 is ~0.34 because MLI1_2 (stellate) also maps there with comparable coverage. This cross-cutting biology reflects the basket-stellate morphological continuum and prevents a 1:1 mapping at cluster resolution. broadMatch at supertype level is the supported call.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        Region data absent at supertype level; child cluster CS20230722_CLUS_5188 provides cerebellar molecular layer confirmation (region_fraction_100um=0.841, lower_bound rollup).
  proposed_experiments:
    - >
      Retrieve a basket-cell-specific snRNA-seq dataset where cells were morphologically confirmed (Kv1.1/HCN1 pinceau immunostaining or intracellular dye fill) before or after sequencing, run annotation transfer against WMBv1 CCN20230722 targeting source label against CS20230722_SUPT_1149 and its children. Target: cluster-level F1 ≥ 0.75 with purity > 0.75. Expected output: AnnotationTransferEvidence resolving the cross-cutting call or upgrading confidence.
    - >
      Query single-cell Calb1 expression within CS20230722_CLUS_5188 to determine whether the mean (0.31 at CS20230722_SUPT_1149) is driven by minority contaminating nuclei or represents a basket-cell subpopulation. Resolve DISCORDANT Calb1 counter-evidence.
    - >
      Add RORa and HCN1 to the WMBv1 precomputed expression store for the CBX MLI lineage to convert two NOT_ASSESSED marker comparisons to assessable alignments.
  unresolved_questions:
    - >
      Does WMBv1 resolve basket cells from stellate cells at any taxonomy level? Current AT evidence (purity ~0.34 for each source group at cluster) suggests no. Future atlas iterations may separate these.
    - >
      Is Calb1 mean expression at CS20230722_SUPT_1149 (0.31) biologically real (basket-cell Calb1 subpopulation) or a snRNA-seq artefact?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5188 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.52
  relationship: evidencell:CrossCuttingMatch
  mapping_cardinality: "n:1"
  mapping_justification: semapv:CompositeMatching
  rationale: >
    [tier:NEXT] Pvalb CONSISTENT (val=11.12; cohort_pct 0.995), Kcna1 CONSISTENT (val=6.47; cohort_pct 0.946), Grid1 CONSISTENT (val=9.85; cohort_pct 0.989); 3 of 5 assessed markers CONSISTENT. Location: region_fraction_100um=0.841 (lower_bound), CONSISTENT with molecular layer cerebellar cortex. NT GABA CONSISTENT. AT F1=0.51 at cluster level (coverage=0.999, purity=0.34) in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 — purity is low because MLI1_2 (stellate) also maps to CS20230722_CLUS_5188 with comparable coverage. Cross-cutting: both basket (MLI1_1) and stellate (MLI1_2) map to this cluster; n:1 cardinality. Calb1 DISCORDANT (val=0.18, cohort_pct 0.277) is unresolved counter-evidence.
  reconciliation_note: >
    Paired with edge_basket_cell_cerebellum_to_CS20230722_SUPT_1149 (parent supertype broadMatch). CS20230722_CLUS_5188 is the best cluster-level target but the cross-cutting MLI1 biology means this is not a clean 1:1 mapping. CrossCuttingMatch is used because both basket_cell_cerebellum and stellate_cell_cerebellum map to this cluster with indistinguishable transcriptomic coverage.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        MLI1_1 (basket) and MLI1_2 (stellate) both map to CS20230722_CLUS_5188 with coverage ~1.0 and purity ~0.34 each in at_run_20260709_kozareva_cerebellum_mmc_wmbv1. WMBv1 does not resolve basket from stellate at cluster resolution. This is a known biological feature of cerebellar MLI transcriptomics, not a pipeline failure.
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        region_fraction_100um=0.841 is a lower_bound estimate — CCF2020 non-painted descendants not counted in rollup. True cerebellar fraction may be higher.
  proposed_experiments:
    - >
      Retrieve a morphologically confirmed basket-cell dataset (Kv1.1/HCN1 pinceau staining or intracellular dye fill), run annotation transfer against WMBv1 CCN20230722 with CS20230722_CLUS_5188 as target. Target: purity > 0.75 and F1 ≥ 0.75 at cluster level. This would resolve CrossCuttingMatch to closeMatch if stellate cells do not map there at comparable purity under a morphology-filtered source.
    - >
      Query single-cell Calb1 within CS20230722_CLUS_5188; determine whether the DISCORDANT mean (0.18) is a minority-cell effect.
  unresolved_questions:
    - >
      Is the basket+stellate cross-cutting at CS20230722_CLUS_5188 resolvable at any WMBv1 taxonomy level, or is basket-stellate separation fundamentally below WMBv1's transcriptomic resolution?
    - >
      Is Calb1 expression (0.18) in CS20230722_CLUS_5188 a technical artefact or a genuine basket-cell subpopulation signal?
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1151 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  relationship: skos:closeMatch
  mapping_cardinality: "1:1"
  mapping_justification: semapv:CompositeMatching
  rationale: >
    [tier:WEAKEST] Pvalb CONSISTENT (val=11.33; cohort_pct 0.991; child-coverage 1.000), Kcna1 CONSISTENT (val=7.23; cohort_pct 0.973; child-coverage 1.000), Calb1 CONSISTENT (val=0.09; cohort_pct 0.073); 3 of 5 assessed markers CONSISTENT (including Calb1 absence). Region CONSISTENT (region_fraction_100um=0.851; lower_bound). Grid1 APPROXIMATE (val=1.39; cohort_pct 0.191). However, AT resolves only to class level (best F1=0.39 at class) in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 — MLI1_1 basket-source cells do not transfer to the CS20230722_SUPT_1151 lineage at subclass or supertype resolution, indicating the primary basket transcriptome assigns elsewhere. LOW confidence because AT class-level only and the basket AT signal actively prefers the CS20230722_SUPT_1149 lineage.
  reconciliation_note: >
    Secondary candidate to edge_basket_cell_cerebellum_to_CS20230722_SUPT_1149 (primary). Marker profile is partially supportive but AT evidence does not land in this lineage at subclass+ resolution; Cdh22-named supertype may represent a distinct cerebellar interneuron subpopulation from the MLI1 basket/stellate types.
  caveats:
    - caveat_type: AMBIGUOUS_MAPPING
      description: >
        AT evidence resolves only to class level for this candidate; the basket-source AT signal (MLI1_1) does not reach CS20230722_SUPT_1151 or its children at subclass or finer resolution. This distinguishes CS20230722_SUPT_1151 from CS20230722_SUPT_1149 (which receives AT coverage ~1.0 at supertype level).
    - caveat_type: MERFISH_REGISTRATION_UNCERTAINTY
      description: >
        region_fraction_100um=0.851 is a lower_bound estimate.
  proposed_experiments:
    - >
      Determine whether the Cdh22 lineage (CS20230722_SUPT_1151 and children) represents a distinct cerebellar interneuron population from the basket/stellate MLI1 types. A targeted literature search for "Cdh22 cerebellar interneuron" or targeted annotation-transfer from a basket-cell-specific dataset would resolve this.
  unresolved_questions:
    - >
      What is the biological identity of the 1151 CBX MLI Cdh22 Gaba_1 lineage relative to basket and stellate cells? Its distinct Grid1 expression (1.39 vs 8.96 at CS20230722_SUPT_1149) and separate Cdh22 name marker suggest a genuinely distinct subpopulation.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5185 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] PLI-lineage cluster (CB PLI Gly-Gaba_4); AT resolves only to class level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (best F1=0.39). Not an MLI basket-cell lineage. Eliminated on cell-type identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5178 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] PLI-lineage cluster (CB PLI Gly-Gaba_1); AT resolves only to class level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (best F1=0.39). Calb1 DISCORDANT (val=0.27). Not an MLI basket-cell lineage. Eliminated on cell-type identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5184 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.08
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] PLI-lineage cluster (CB PLI Gly-Gaba_3); n=69 cells (very small cluster); AT resolves only to class level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (best F1=0.39). Eliminated on cell-type identity and cluster size.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_CLUS_5267 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Non-neuronal cluster (OPC NN_1); primary soma location in Midbrain and Pons (region_fraction_100um=0.135); AT: NO_EVIDENCE — MLI1_1 source cells do not transfer to this lineage in at_run_20260709_kozareva_cerebellum_mmc_wmbv1. Eliminated on wrong cell class and wrong region.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1147 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] PLI supertype (CB PLI Gly-Gaba_4); AT resolves only to class level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (best F1=0.39). Not an MLI basket-cell lineage. Eliminated on cell-type identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1144 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.10
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] PLI supertype (CB PLI Gly-Gaba_1); AT resolves only to class level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (best F1=0.39). Calb1 DISCORDANT (val=0.17, cohort_pct 0.182). Not an MLI basket-cell lineage. Eliminated on cell-type identity.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_basket_cell_cerebellum_to_CS20230722_SUPT_1150 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.15
  relationship: evidencell:UncertainRelationship
  rationale: >
    [tier:CUT] Sibling MLI Megf11 supertype (CBX MLI Megf11 Gaba_2); Grid1 APPROXIMATE (val=4.18; cohort_pct 0.236) — substantially lower than primary candidate CS20230722_SUPT_1149 (val=8.96); Calb1 DISCORDANT (val=0.20, cohort_pct 0.218); AT resolves only to subclass level in at_run_20260709_kozareva_cerebellum_mmc_wmbv1 (best F1=0.50 at subclass, not reaching this supertype specifically). n=370 cells. Eliminated in favour of CS20230722_SUPT_1149 as the better-supported sibling.
```
<!-- verdict-block-end -->
