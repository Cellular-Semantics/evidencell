# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

## Introduction

Hippocampal bistratified cells are a fast-spiking GABAergic interneuron subtype of the CA1 microcircuit whose axon ramifies in both stratum oriens and stratum radiatum, where it co-targets the basal and apical dendrites of pyramidal neurons. They are a major Pvalb-expressing population, distinguished from cortical-style basket cells partly by their Sst and Tac1 co-expression — a combination recently exploited by intersectional genetics to target them selectively [9].

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum pyramidale [UBERON:0014548], CA1 stratum oriens [UBERON:0014552], CA1 stratum radiatum [UBERON:0014554] | [1][2][3] |
| Neurotransmitter | GABAergic | [4] |
| Defining markers | Pvalb, Sst, Tac1 | Pvalb [5][6][7][8]; Sst, Tac1 [9] |
| Neuropeptides | Sst | [9] |
| Definition basis | CLASSICAL_MULTIMODAL | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Neurotransmitter:** review · GABAergic · [4]
  > Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
  > — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 38778375_462ec931 -->
- **Pvalb marker:** review / experimental · mouse hippocampus · [5][6][7][8]
  > WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes (basket, axo-axonic, bistratified, radiatum-targeting).
  > — Ekins et al. 2020, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 221276443_e917908b -->
  > while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities
  > — Que et al. 2021 · [8] <!-- quote_key: 230508306_e8cc8c19 -->
- **Sst, Tac1 markers / Sst neuropeptide:** intersectional genetics · mouse · [9]
  > the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [9] <!-- quote_key: 269246896_c084d5c0 -->
- **Soma location:** review / atlas reconstruction · mouse hippocampus · [1][2][3]
  > Different types of hippocampal inhibitory interneurons control spike initiation [e.g., axo-axonic and basket cells (BCs)] and synaptic integration (e.g., bistratified and oriens–lacunosum moleculare interneurons) within pyramidal neurons
  > — Chamberland & Topolnik 2012, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 8530661_92702482 -->
  > the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin
  > — Bocchio et al. 2024, Results · [2] <!-- quote_key: 262127573_ba6d02e9 -->
  > The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus
  > — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [3] <!-- quote_key: 224817966_79f4a500 -->

</details>

Cell Ontology mapping: bistratified cell [[CL:0004247](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)] (BROAD).

---

## Results

Morphologically identified PV bistratified cells (Que 2021 patch-seq [8]) and Chamberland's in-silico Sst::Tac1 subfamily (Harris 2018 [9]) jointly resolve the canonical hippocampal bistratified mapping to the supertype 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] and, within it, to the cluster 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] (see figure and property comparison tables). The supertype is shared with PV basket cells (CLUS_0739), but cluster-level annotation transfer cleanly separates BIC from BC within it.

![Filtered AT figure for Bistratified cell (Que 2021 BIC → WMBv1)](figures/f1_for_bistratified_cell_hippocampus.png)

*F1 across taxonomy levels for the Que 2021 PV bistratified cohort (BIC = hBIC + vBIC, n=20 morphologically identified cells). Coverage = fraction of source-group cells landing on the target; Purity = fraction of target cells from the source group. With a single source group plotted, Purity differentiates by how many other source labels also land on the target — here Purity rises sharply from class/subclass (~0.22) to cluster (Pur=0.70 at CLUS_0737), reflecting BC cells siphoning off to CLUS_0739 at finer resolution and leaving CLUS_0737 enriched for BIC. F1 ≥ 0.5 at a level indicates a clean mapping at that resolution; cluster-level F1=0.80 is the headline result.*

![Filtered AT figure for Bistratified cell (Chamberland Sst_Tac1 → WMBv1)](figures/f1_for_bistratified_cell_hippocampus_chamberland.png)

*F1 across taxonomy levels for the Chamberland per-cluster Sst_Tac1 subfamily (n=168 Harris 2018 cells labelled by gene-pair rules applied to cluster-mean expression). As before, Pur = Purity (fraction of target cells from this source); Cov = Coverage (fraction of source cells on this target). The Sst_Tac1 label maps preferentially to the Pvalb branch — subclass 052 Pvalb Gaba (F1=0.578) → supertype 0206 Pvalb Gaba_2 (F1=0.566) → cluster 0737 Pvalb Gaba_2 (Pur=0.939) — recapitulating the Sst-Pvalb transcriptomic continuum reported for bistratified cells in Chamberland et al. 2024 Fig 6 [9].*

### 0737 Pvalb Gaba_2 · 🟡 MODERATE

This is the primary atlas landing site for canonical PV bistratified cells. The cluster sits in the Pvalb Gaba subclass and shows a CA1 soma distribution dominated by stratum oriens (614 painted cells in MBA:399 of 995 hippocampal-formation cells), with substantial stratum radiatum representation — the bilaminar SO + SR pattern that defines bistratified axonal territory. Atlas neuropeptide and marker expression aligns with the classical profile: Pvalb (val 8.27, cohort percentile 0.956), Sst (4.39, 0.706), Tac1 (7.26, 0.956); both Sst and Tac1 are annotated NEUROPEPTIDE at atlas level. See property comparison table and Evidence support table below.

**Table 1 — Property comparison (CLUS_0737)**

| Property | Classical | Supertype (0206) | Best cluster (0737) | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum pyramidale / oriens / radiatum [UBERON:0014548/52/54] | 668 cells in Field CA1 [MBA:382] (region_fraction_100um 0.224) | CA1 SO 614, CA1 SR / SP secondary | APPROXIMATE |
| NT type | GABAergic | not asserted at supertype | GABA | CONSISTENT |
| Pvalb expression | defining marker | 8.74 (cohort 0.968) | 8.27 (cohort 0.956) | CONSISTENT |
| Sst expression | defining marker / neuropeptide | 2.72 (cohort 0.774) | 4.39 (cohort 0.706); atlas NEUROPEPTIDE | CONSISTENT |
| Tac1 expression | defining marker | 5.36 (cohort 0.935) | 7.26 (cohort 0.956); atlas NEUROPEPTIDE | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support (CLUS_0737)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (CA1 SO+SR; Pvalb/Sst/Tac1 NP profile) | Atlas metadata | SUPPORT | bilaminar SO+SR; Cort 8.0, Tac1 7.3, Sst 4.4 | atlas-internal |
| Que 2021 BIC patch-seq AT | Annotation transfer | SUPPORT | F1=0.80, Pur=0.70, Cov=0.94 (n=16/20) | [8] |
| Chamberland Sst_Tac1 per-cluster AT | Annotation transfer | PARTIAL | cluster Pur=0.94; subclass F1=0.58 | [9] |

**Marker evidence provenance.**
- **Pvalb (defining):** transcript-level (cluster mean 8.27, cohort percentile 0.956) and protein-level confirmation in the source literature ([5][6][7][8]). Que 2021 [8] specifically patch-clamped morphologically identified BIC cells and recovered Pvalb transcripts — direct evidence at the right cell type.
- **Sst, Tac1 (defining + Sst neuropeptide):** transcript-level on the cluster (Sst 4.39, Tac1 7.26) and an annotated atlas NEUROPEPTIDE category for both. The biological anchor is Chamberland 2024 [9], where the Sst::Tac1 intersection selectively labelled bistratified cells with confirmed fast-spiking targets — direct evidence at the right cell type via intersectional driver.
- No marker provenance gaps were flagged; both lit anchors confirm cell identity through morphology / connectivity, not by appeal to the same marker that defines the cluster.

**Concerns.**
- **Location APPROXIMATE** (boundary scatter — `region_fraction_100um: 0.224`; could reflect MERFISH registration error or genuine spread into adjacent CA1 strata; weak counter-evidence).
- DISTRIBUTED_ACROSS_CLUSTERS caveat on the edge: an Sst-dominant bistratified subpopulation may distribute toward SUPT_0216 Sst Gaba_3 rather than to CLUS_0737. The cluster captures the Pvalb-primary bistratified population; an Sst-dominant Pvalb-low fraction would not be represented here.
- Que 2021 input was TPM-rounded pseudo-counts (no raw counts available for the patch-seq dataset); robustness to raw-counts normalisation is unverified.
- Age mismatch: Que 2021 spans P10–P77 (mean ~P30) against adult WMBv1; partly mitigated by Que's own finding of high cross-age transcriptomic similarity in morphologically defined PV-IN types.

**What would upgrade confidence.**
- Replicate Que 2021 BIC → CLUS_0737 (F1 ≥ 0.80) with an independent morphologically confirmed PV bistratified patch-seq dataset, ideally from adult mice with raw counts.
- Test robustness of CLUS_0737 assignment to raw-counts vs. TPM-pseudo-counts normalisation on GSE142546.
- Targeted intersectional scRNA-seq (Sst-Cre × Tac1-Flp × Pvalb-negative) to test whether a Sst-dominant Pvalb-low bistratified subpopulation exists and whether it routes to CLUS_0737 or to a Sst Gaba_3 cluster.

### 0206 Pvalb Gaba_2 · 🟡 MODERATE

The supertype is the natural Pvalb-subclass parent that absorbs morphologically identified BIC cells before they resolve at cluster level. 18/20 Que 2021 BIC cells map here (coverage 0.900, F1 0.375); the supertype-level F1 is depressed because the supertype also contains PV basket cells (CLUS_0739) and the BIC pool is small relative to the cohort. See property comparison and Evidence support tables below. *(1 of 2 morphological subtypes — bistratified — concentrate in CLUS_0737 within this supertype; the remainder (basket) routes to CLUS_0739. Best match: CLUS_0737.)*

**Table 1 — Property comparison (SUPT_0206)**

| Property | Classical | Supertype (0206) | Best cluster (0737) | Alignment |
|---|---|---|---|---|
| Soma location | CA1 stratum pyramidale / oriens / radiatum | Field CA1 [MBA:382] count_100um=922 (region_fraction_100um 0.160) | CA1 SO 614 / CA1 SR (CLUS_0737) | APPROXIMATE |
| NT type | GABAergic | not asserted | GABA (at cluster) | NOT_ASSESSED at supertype; CONSISTENT at cluster |
| Pvalb expression | defining marker | 8.74 (cohort 0.968) | 8.27 (cohort 0.956) | CONSISTENT |
| Sst expression | defining marker / neuropeptide | 2.72 (cohort 0.774) | 4.39 (cohort 0.706) | CONSISTENT |
| Tac1 expression | defining marker | 5.36 (cohort 0.935) | 7.26 (cohort 0.956) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support (SUPT_0206)**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata (dominant hippocampal Pvalb supertype; CLUS_0737 child bilaminar) | Atlas metadata | PARTIAL | child-coverage 1.000 for Pvalb/Sst/Tac1 | atlas-internal |
| Que 2021 BIC patch-seq AT (supertype level) | Annotation transfer | SUPPORT | F1=0.375, Cov=0.90 (18/20) | [8] |

**Marker evidence provenance.**
- Pvalb, Sst, Tac1 all show child-cluster coverage 1.000 at the supertype level, i.e. all five SUPT_0206 child clusters express each marker above the percentile threshold — supertype-level marker concordance is broad, not specific to bistratified.
- No marker-concordance circularity (the supertype name "Pvalb Gaba_2" matches the Pvalb defining marker, but Pvalb is anchored to primary patch-seq + intersectional studies [5][6][7][8], not nominal).

**Concerns.**
- Location APPROXIMATE (boundary scatter — `region_fraction_100um: 0.160`; weak counter-evidence; supertype contains substantial cortical-subplate adjacency).
- DISTRIBUTED_ACROSS_CLUSTERS caveat: SUPT_0206 contains both PV basket cells (CLUS_0739) and PV bistratified cells (CLUS_0737). The supertype is not specific to bistratified at this resolution — the child-cluster split is where the morphological identity resolves.

**What would upgrade confidence.**
- Determine whether SUPT_0206 carries morphologically informative substructure beyond the BC/BIC cluster-level split — e.g. whether axo-axonic cells also route into this supertype (Que 2021 AAC n=6 is uninformative; a larger AAC dataset would resolve this).

<details>
<summary>Candidates audited (full top-K)</summary>

| WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key evidence | Verdict |
|---|---|---:|---|---|---|
| `0737 Pvalb Gaba_2 [CS20230722_CLUS_0737]` | 0206 Pvalb Gaba_2 | 170 | 🟡 MODERATE | Que 2021 BIC AT F1=0.80; bilaminar SO+SR | Primary |
| `0206 Pvalb Gaba_2 [CS20230722_SUPT_0206]` | — | 650 | 🟡 MODERATE | dominant hippocampal Pvalb supertype; BIC Cov=0.90 | Supports broader mapping |
| `0216 Sst Gaba_3 [CS20230722_SUPT_0216]` | — | 2004 | 🔴 LOW | no BIC AT signal; only Sst-co-expression signal | Eliminated (Que 2021 BIC routes to Pvalb supertype, not Sst Gaba_3) |
| `0739 Pvalb Gaba_2 [CS20230722_CLUS_0739]` | 0206 Pvalb Gaba_2 | 55 | ⚪ UNCERTAIN | sibling of CLUS_0737; absorbs BC, not BIC | Eliminated (basket cell sibling cluster) |
| `0732 Pvalb chandelier Gaba_1 [CS20230722_CLUS_0732]` | 0204 Pvalb chandelier Gaba_1 | 309 | ⚪ UNCERTAIN | chandelier supertype; low Sst | Eliminated (chandelier identity, not bistratified) |
| `0768 Sst Gaba_3 [CS20230722_CLUS_0768]` | 0216 Sst Gaba_3 | 66 | ⚪ UNCERTAIN | Tac1 only 0.15 (cohort 0.338); no BIC AT | Eliminated (Tac1 low; no BIC AT signal) |
| `0772 Sst Gaba_3 [CS20230722_CLUS_0772]` | 0216 Sst Gaba_3 | 190 | ⚪ UNCERTAIN | Pvalb 0.34; Tac1 0.14; no BIC AT | Eliminated (Pvalb and Tac1 both low) |
| `0212 Pvalb Gaba_8 [CS20230722_SUPT_0212]` | — | 7777 | ⚪ UNCERTAIN | location DISCORDANT — isocortex-dominant | Eliminated (no hippocampal cells) |
| `0196 RHP-COA Ndnf Gaba_4 [CS20230722_SUPT_0196]` | — | 167 | ⚪ UNCERTAIN | Ndnf supertype; CA3-biased; no BIC AT | Eliminated (wrong subclass) |
| `0219 Sst Gaba_6 [CS20230722_SUPT_0219]` | — | 725 | ⚪ UNCERTAIN | Sst supertype; no BIC AT; CA3-biased | Eliminated (wrong subclass; no BIC AT signal) |

</details>

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Bistratified cell is defined here by the convergence of Pvalb [5][6][7][8], Sst and Tac1 [9] markers on a fast-spiking CA1 GABAergic interneuron [4] with soma in CA1 stratum pyramidale / oriens / radiatum [1][2][3]. `definition_basis` = CLASSICAL_MULTIMODAL.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH spatial registration for soma location.

**Annotation transfer — Que 2021 (`at_run_20260508_que2021_pvin_mmc_wmbv1`).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (BIC = hBIC + vBIC) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 88 (filtered to 88) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Caveats | Patch-seq with morphologically confirmed PV subtypes. TPM rounded to integer pseudo-counts (raw counts unavailable). Age range P10–P77, mean ~P30 vs adult WMBv1. AAC n=6 uninformative. BC/BIC separate cleanly within SUPT_0206 (BC→CLUS_0739 F1=0.827; BIC→CLUS_0737 F1=0.800). |

**Annotation transfer — Chamberland subfamily on Harris 2018 (`at_run_20260512_chamberland_subfamily_mmc_wmbv1`).**

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Sst_Tac1 Chamberland per-cluster subfamily label) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| F1 matrix | `f1_matrix_chamberland_by_class.csv` |
| Caveats | Per-cluster derivation is the primary (dropout-robust) result. Sst::Tac1 → Pvalb subclass (subclass-level recall 0.78) surfaces transcriptomic Sst-Pvalb continuity for bistratified types. |

**Annotation transfer — Yao 2021 SSv4 (`at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1`).** Used as a negative control for the Sst-Gaba_3 alternative hypothesis. Yao SSv4 "Pvalb" subclass (n=66 HIP cells) maps predominantly to SUPT_0204 Pvalb chandelier (F1=0.612) and SUPT_0206 Pvalb Gaba_2 (F1=0.324), with only 6/66 cells reaching SUPT_0216 Sst Gaba_3 (F1=0.053) — i.e. there is no Pvalb-labelled signal supporting SUPT_0216 as a bistratified target.

</details>

---

## Discussion

**Best candidate + caveats.** The strongest call is a cluster-level `skos:closeMatch` from the classical bistratified cell to CLUS_0737 Pvalb Gaba_2, with the parent supertype SUPT_0206 carrying a `skos:closeMatch` that absorbs both bistratified (CLUS_0737) and basket (CLUS_0739) populations. The MODERATE rating reflects three factors: (i) Que 2021 BIC n=20 is small and from juvenile-skewed animals; (ii) Sst-co-expressing bistratified cells may partly route into the Sst Gaba_3 supertype rather than into SUPT_0206 (the DISTRIBUTED_ACROSS_CLUSTERS caveat); (iii) atlas marker concordance at the supertype is broad and non-specific to bistratified identity. The CL mapping is `BROAD` because CL:0004247 (bistratified cell) is a retinal-focused term — the hippocampal Pvalb/Sst/Tac1+ bistratified interneuron with axon in SO and SR has no dedicated CL term, and the broad mapping is a placeholder pending a new-term request.

**SUPT_0216 reframing.** The earlier SUPT_0216 Sst Gaba_3 edge is retained as LOW-confidence speculative, representing only a candidate Sst-dominant bistratified subpopulation. Que 2021 morphologically identified BIC cells show no transcriptomic mapping to any Sst supertype, ruling out SUPT_0216 as the primary atlas target for canonical PV bistratified cells. Resolution of this question requires a Sst-Cre × Tac1-Flp × Pvalb-negative intersectional dataset.

---

## References

- [1] Chamberland & Topolnik 2012 · PMID:23162426 — soma location
- [2] Bocchio et al. 2024 · PMID:39401246 — soma location
- [3] Perez et al. 2020 · PMID:33404500 — soma location
- [4] Dannenberg et al. 2017 · PMID:29321728 — neurotransmitter type
- [5] Ekins et al. 2020 · PMID:33150866 — Pvalb marker
- [6] Chamberland et al. 2023 · PMID:37162922 — Pvalb marker
- [7] Tzilivaki et al. 2023 · PMID:37467748 — Pvalb marker
- [8] Que et al. 2021 · PMID:33398060 — Pvalb marker; patch-seq BIC dataset (GSE142546)
- [9] Chamberland et al. 2024 · PMID:38640347 — Sst, Tac1 markers; Sst::Tac1 intersectional genetics

---

<!-- VERDICT BLOCKS (audit metadata; not user-facing) -->

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737
confidence: MODERATE
relationship: skos:closeMatch
mapping_cardinality: "1:1"
rationale: |
  [tier:STRONGEST] Cluster-level mapping for canonical PV bistratified cell.
  Que 2021 patch-seq morphologically identified BIC cells (n=20) map to
  CLUS_0737 with F1=0.80, Purity=0.696, Coverage=0.941; sibling cluster
  CLUS_0739 absorbs BC cells. Bilaminar CA1 SO + SR soma distribution
  matches bistratified axonal territory. Atlas Pvalb/Sst/Tac1 expression
  aligns with the classical Pvalb/Sst/Tac1+ profile (Chamberland 2024
  Sst::Tac1 intersectional targeting). Chamberland per-cluster Sst_Tac1
  AT confirms CLUS_0737 specificity (cluster purity 0.939).
caveats:
  - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
    description: |
      Sst-dominant Pvalb-low bistratified subpopulation, if it exists,
      may route toward SUPT_0216 Sst Gaba_3 rather than to CLUS_0737.
  - caveat_type: SINGLE_STUDY
    description: |
      Cluster-level F1=0.80 derives from a single patch-seq dataset
      (Que 2021, n=20 BIC cells); independent morphologically confirmed
      replication is outstanding.
proposed_experiments:
  - Independent morphologically confirmed PV bistratified patch-seq
    dataset from adult mice with raw counts, to test reproducibility
    of the CLUS_0737 mapping.
  - Robustness check of CLUS_0737 assignment under raw-counts vs
    TPM-pseudo-counts normalisation on GSE142546.
  - Sst-Cre x Tac1-Flp x Pvalb-negative intersectional scRNA-seq with
    morphology recovery, to test for a Sst-dominant bistratified
    subpopulation and its atlas routing.
unresolved_questions:
  - Whether a Sst-dominant Pvalb-low bistratified subpopulation exists
    and routes to CLUS_0737 or to a Sst Gaba_3 child cluster.
reconciliation_note: |
  Paired with edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206
  as the parent supertype absorbing both bistratified (this cluster)
  and basket (sibling CLUS_0739) populations.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206
confidence: MODERATE
relationship: skos:closeMatch
mapping_cardinality: "1:n"
rationale: |
  [tier:NEXT] Parent Pvalb supertype absorbing morphologically
  identified BIC cells (Que 2021: 18/20 BIC cells, Coverage=0.90)
  before they resolve at cluster level. Supertype-level F1=0.375 is
  depressed by the supertype also containing PV basket cells (CLUS_0739).
  All defining markers (Pvalb, Sst, Tac1) show child-cluster coverage
  1.000 across the supertype, but the bistratified-specific signal is
  at cluster level (CLUS_0737), not supertype.
caveats:
  - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
    description: |
      Supertype contains both PV bistratified (CLUS_0737) and PV
      basket (CLUS_0739) cells; not specific to bistratified at
      supertype resolution.
proposed_experiments:
  - Test whether SUPT_0206 carries morphologically informative
    substructure beyond the BC/BIC cluster split (e.g. AAC routing,
    pending a larger axo-axonic dataset; Que 2021 AAC n=6 is
    uninformative).
unresolved_questions:
  - Whether SUPT_0206 provides further morphological substructure
    beyond the CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.
reconciliation_note: |
  Paired with edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737
  as the best-child mapping within this supertype.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216
confidence: LOW
relationship: skos:closeMatch
mapping_cardinality: "1:n"
rationale: |
  [tier:WEAKEST] Speculative edge representing a candidate
  Sst-dominant Pvalb-low bistratified subpopulation. Que 2021
  morphologically identified BIC cells show no AT signal to any Sst
  supertype (0/20 BIC cells route here; all route to SUPT_0206
  Pvalb Gaba_2). Support rests on Sst marker co-expression and
  Chamberland 2024 Sst::Tac1 intersectional targeting alone, not on
  direct cluster annotation transfer from morphologically identified
  BIC cells. Sst Gaba_3 supertype is shared with OLM and HS cells
  per the olm_cell_ca1 edge.
caveats:
  - caveat_type: DISTRIBUTED_ACROSS_CLUSTERS
    description: |
      Sst Gaba_3 supertype contains OLM, bistratified, and HS cells;
      not separable at supertype level.
  - caveat_type: MARKER_NOT_SPECIFIC
    description: |
      Pvalb co-expression (defining for bistratified) is not captured
      at the Sst supertype level; the candidate subpopulation would
      be Pvalb-low.
proposed_experiments:
  - Sst-Cre x Tac1-Flp x Pvalb-negative intersectional scRNA-seq with
    morphology recovery, to test for a distinct Sst-dominant
    bistratified subpopulation and its supertype routing.
unresolved_questions:
  - Does a Sst-dominant Pvalb-low bistratified subpopulation exist,
    and if so does it map to CS20230722_SUPT_0216 specifically?
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0739
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0739
confidence: LOW
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Sibling cluster of CLUS_0737 within SUPT_0206; Que 2021
  patch-seq AT routes morphologically identified basket cells (BC)
  preferentially to CLUS_0739 (F1=0.827), while bistratified (BIC)
  cells route to CLUS_0737. CLUS_0739 is the PV basket cluster, not
  bistratified.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0732
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0732
confidence: LOW
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Cluster sits in the Pvalb chandelier supertype
  (SUPT_0204), not in Pvalb Gaba_2; chandelier identity, not
  bistratified. Sst is low (cohort percentile 0.191).
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0768
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0768
confidence: LOW
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Sst Gaba_3 child cluster; Tac1 is low (val 0.15, cohort
  percentile 0.338), inconsistent with the classical Sst+Tac1+
  bistratified profile, and no Que 2021 BIC AT signal lands here.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0772
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0772
confidence: LOW
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Sst Gaba_3 child cluster; Pvalb is low (0.34) and Tac1
  is low (0.14), inconsistent with the classical Pvalb+Sst+Tac1+
  bistratified profile, and no Que 2021 BIC AT signal lands here.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0212
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0212
confidence: REFUTED
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Location DISCORDANT: SUPT_0212 is isocortex-dominant
  (Isocortex MBA:315 count_100um=6762; hippocampal formation only
  2349), region_fraction_100um=0.019. No hippocampal-targeted
  bistratified signal can be attributed to this supertype.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0196
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0196
confidence: LOW
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Ndnf-subclass supertype (RHP-COA Ndnf Gaba_4); wrong
  subclass for a Pvalb-defined bistratified cell. CA3-biased
  location; no Que 2021 BIC AT signal lands here.
```

```yaml
# Verdict block for edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0219
edge_id: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0219
confidence: LOW
relationship: evidencell:UncertainRelationship
rationale: |
  [tier:CUT] Sst Gaba_6 supertype; CA3-biased location
  (region_fraction_100um=0.110); no Que 2021 BIC AT signal here.
  The dominant Sst-SSv4 target in the Yao 2021 run but unrelated to
  the canonical PV bistratified mapping.
```
