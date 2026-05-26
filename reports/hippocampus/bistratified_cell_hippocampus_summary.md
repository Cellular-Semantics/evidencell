# Bistratified cell — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

The hippocampal bistratified cell is a classical, morphologically defined CA1
GABAergic interneuron whose axon ramifies bilaminarly in stratum oriens and
stratum radiatum, where it inhibits the dendrites of CA1 pyramidal cells [1, 2].
It belongs to the parvalbumin-expressing (PV) interneuron family and co-expresses
Pvalb, Sst and Tac1 [4, 5, 6, 7, 8, 9]. Because bistratified cells share a
PV/Sst molecular profile with neighbouring populations (basket, axo-axonic, OLM),
their unambiguous placement within a transcriptomic taxonomy has long been an
open question — and bistratified cells therefore serve as a stress test of
whether transcriptomic atlas clusters resolve PV-IN morphological subtypes.

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | pyramidal layer of CA1 [UBERON:0014548] (axon extends into CA1 stratum oriens [UBERON:0014552] and CA1 stratum radiatum [UBERON:0014554]) | [1, 2, 3] |
| Neurotransmitter | GABAergic | [4] |
| Defining markers | Pvalb [5, 6, 7, 8]; Sst [9]; Tac1 [9] | [5–9] |
| Neuropeptides | Sst | [9] |
| Cell Ontology | bistratified cell [CL:0004247] (BROAD; retinal-focused term, no dedicated hippocampal CL term) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** Chamberland & Topolnik 2012 review · [1]
  > The hippocampal cells they most resemble, Basket-bistratified, HS and OLM interneurons, have their somata in the stratum pyramidale (sp) of the hippocampus
  > — Perez et al. 2020, Identification of cell types based on the somatic transcriptome · [3] <!-- quote_key: 224817966_79f4a500 -->
  > the most representative ones, the PV-expressing basket and bistratified cells, the NOS-expressing ivy cells and 2 types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin
  > — Bocchio et al. 2024, Results · [2] <!-- quote_key: 262127573_ba6d02e9 -->
- **Neurotransmitter (GABA):** Dannenberg et al. 2017 · [4]
  > Interneurons expressing the calcium binding protein parvalbumin (PV) make up approximately 40% of all GABAergic interneurons. However, this is a heterogeneous group of functionally distinct interneuron subtypes. For example, in the hippocampus alone, there are at least three functionally and morphologically distinct populations of PV + expressing interneurons, namely basket, axo-axonic and bistratified cells. Fast spiking interneurons in the hippocampus and neocortex are often PV + positive and target the soma of pyramidal cells.
  > — Dannenberg et al. 2017, Classification Schemes and Methodological Approaches · [4] <!-- quote_key: 38778375_462ec931 -->
- **Pvalb marker:** Ekins et al. 2020 · [5]; Chamberland et al. 2023 · [6]; Tzilivaki et al. 2023 · [7]; Que et al. 2021 · [8]
  > WT PV+INTs consist of two physiological subtypes (80% fast-spiking (FS), 20% non-fast-spiking (NFS)) and four morphological subtypes (basket, axo-axonic, bistratified, radiatum-targeting).
  > — Ekins et al. 2020, Classification Schemes and Methodological Approaches · [5] <!-- quote_key: 221276443_e917908b -->
  > while PV-INs differ in anatomy and in vivo activity, their continuous transcriptomic and homogenous biophysical landscapes are not predictive of these distinct identities
  > — Que et al. 2021 · [8] <!-- quote_key: 230508306_e8cc8c19 -->
- **Sst / Tac1 markers and neuropeptide:** Chamberland et al. 2024 · [9]
  > the Sst;;Tac1 intersection targeted a population of bistratified cells that overwhelmingly targeted fast-spiking interneurons. In contrast, the Ndnf;;Nkx2-1 intersection revealed a population of oriens lacunosum-moleculare interneurons that selectively targeted CA1 pyramidal cells
  > — Chamberland et al. 2024, Transcriptomic Interneuron Classifications · [9] <!-- quote_key: 269246896_c084d5c0 -->
- **Electrophysiology / morphology context:** Chamberland & Topolnik 2012 · [1]
  > Different types of hippocampal inhibitory interneurons control spike initiation [e.g., axo-axonic and basket cells (BCs)] and synaptic integration (e.g., bistratified and oriens–lacunosum moleculare interneurons) within pyramidal neurons
  > — Chamberland & Topolnik 2012, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 8530661_92702482 -->

</details>

### Cell Ontology mapping

**Cell Ontology mapping:** bistratified cell [[CL:0004247](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)] (BROAD).

The CL term is retinal-focused; the hippocampal Pvalb/Sst/Tac1+ bistratified
cell with axons in CA1 SO and SR has no dedicated CL term and is a candidate
for a new term. Mapping notes are surfaced again in the Discussion.

---

## Results

Three candidate atlas edges were assessed against the bistratified-cell
classical node. The primary mapping is **CLUS_0737 (0737 Pvalb Gaba_2)** at
MODERATE confidence — the sole WMBv1 cluster whose MERFISH bilaminar CA1
SO + CA1 SR distribution and Pvalb/Sst/Tac1 marker profile align with the
classical morphological definition, and the cluster recipient of 16/17
morphologically labelled Que 2021 BIC patch-seq cells reaching cluster
resolution. The parent supertype SUPT_0206 (Pvalb Gaba_2) is co-assigned at
MODERATE confidence; SUPT_0216 (Sst Gaba_3) is retained at LOW confidence
to represent any Sst-dominant bistratified subpopulation that would not
be captured under the canonical PV branch.

### Annotation-transfer overview figure (Que 2021 patch-seq, BIC)

![Filtered AT figure for bistratified cells (Que 2021 BIC)](figures/f1_for_bistratified_cell_hippocampus.png)

*F1 across taxonomy levels for the single source group relevant to the
classical bistratified cell — Que 2021 patch-seq BIC (pooled hBIC + vBIC,
n=20 morphologically confirmed cells; CS20230722). Each panel row is a
source-cell group; nodes are coloured by F1 with **Purity** (Pur) and
**Coverage** (Cov) shown inline. Coverage = fraction of source-group cells
landing on this target; Purity = fraction of this target's cells coming
from the source group. With a single source group in the figure, Coverage
discriminates the landing site while Purity reports the target cluster's
contamination by other PV morphological types. F1 ≥ 0.5 at a level
indicates a clean mapping at that resolution. The cluster-level landing
site CS20230722_CLUS_0737 reaches F1=0.80 (Cov=0.94, Pur=0.70) — the
strongest BIC signal in WMBv1.*

The cluster-level F1 jump from 0.38 at supertype to 0.80 at cluster
reflects that the supertype SUPT_0206 pools BIC and basket (BC)
morphologies; only at cluster resolution do BC (→ CLUS_0739, F1=0.83 in
the companion analysis reported in the run caveats) and BIC
(→ CLUS_0737) separate cleanly.

### Mapping candidates

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|:--:|---|---|--:|:--:|---|---|
| 1 | 0737 Pvalb Gaba_2 [CS20230722_CLUS_0737] | 0206 Pvalb Gaba_2 | 1312 | 🟡 MODERATE | Bilaminar CA1 SO+SR CONSISTENT · Pvalb/Sst/Tac1 CONSISTENT | Best candidate |
| 2 | 0206 Pvalb Gaba_2 [CS20230722_SUPT_0206] | — | 2860 | 🟡 MODERATE | Pvalb subclass CONSISTENT · pools BC + BIC | Best candidate (supertype) |
| 3 | 0216 Sst Gaba_3 [CS20230722_SUPT_0216] | — | 2712 | 🔴 LOW | Sst/Tac1 CONSISTENT · Pvalb DISCORDANT · location APPROXIMATE | Speculative |

Total: 3 edges on this node; all `evidencell:PartialOverlapMatch`.

### Primary candidate — CLUS_0737 (Pvalb Gaba_2)

**Table 1 — Property comparison (CLUS_0737 and parent SUPT_0206).**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | GABA | CONSISTENT |
| Soma / axon location | CA1 stratum oriens [UBERON:0014552] + CA1 stratum radiatum [UBERON:0014554] (axonal bilamina) | not separable (pools BC + BIC) | CLUS_0737: CA1 SO (361), CA1 SR (72), CA3 SO (72) — bilaminar | CONSISTENT |
| Pvalb expression | defining marker | Pvalb subclass; CLUS_0739 MERFISH: Pvalb present | Pvalb subclass; CLUS_0737 scoped marker Ednra (Pvalb not in CLUS_0737 MERFISH panel but present in parent subclass) | CONSISTENT |
| Sst expression | co-expressed | NP: Sst:4.4 (CLUS_0737) | NP: Sst:4.4 (CLUS_0737) | CONSISTENT |
| Tac1 expression | co-expressed (Sst;;Tac1 intersection targets BIC) | NP: Tac1:7.3 (CLUS_0737) | NP: Tac1:7.3 (CLUS_0737) | CONSISTENT |
| Sex ratio | not documented | not available | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support (all items on CLUS_0737 + SUPT_0206 edges).**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| SUPT_0206 atlas metadata | Atlas metadata | PARTIAL | Pvalb supertype; contains CLUS_0737 (BIC) and CLUS_0739 (BC) | atlas-internal |
| Que 2021 patch-seq AT → SUPT_0206 | Annotation transfer | SUPPORT | F1=0.38 (Cov=0.90, Pur=0.24); 18/20 BIC cells land on SUPT_0206 | atlas-internal |
| CLUS_0737 atlas metadata | Atlas metadata | SUPPORT | Bilaminar CA1 SO (361)+SR (72); NP Tac1:7.3, Sst:4.4, Cort:8.0 | atlas-internal |
| Que 2021 patch-seq AT → CLUS_0737 | Annotation transfer | SUPPORT | F1=0.80 (Cov=0.94, Pur=0.70); 16/17 cluster-resolved BIC at CLUS_0737 | atlas-internal |
| Chamberland Sst_Tac1 in-silico AT → CLUS_0737 | Annotation transfer | PARTIAL | Cluster F1=0.47 (Cov=0.31, Pur=0.94); confirms landing site | atlas-internal |

*(BIC/BC cluster separation within SUPT_0206 is recovered only at cluster
resolution: of 17 morphologically confirmed BIC cells reaching the right
lineage at cluster level, 16 concentrate at CLUS_0737, while sibling
CLUS_0739 is the preferred landing site for BC cells. Best match: CLUS_0737.)*

### 0737 Pvalb Gaba_2 · 🟡 MODERATE

**Supporting evidence**

- WMBv1 MERFISH for CLUS_0737 shows the largest CA1 stratum oriens cell
  count of any Pvalb cluster (361 cells) together with a substantive CA1
  stratum radiatum component (72 cells) — the bilaminar SO + SR axon
  territory that defines the bistratified morphological type [atlas-internal].
- CLUS_0737 neuropeptide stats list Tac1:7.3, Sst:4.4 and Cort:8.0,
  directly consistent with the Pvalb+/Sst+/Tac1+ co-expression that
  Chamberland et al. 2024 used to target bistratified cells via the
  Sst;;Tac1 intersection [9].
- Que 2021 (GSE142546) morphologically confirmed PV bistratified cells
  (pooled hBIC + vBIC patch-seq, n=20) map to CLUS_0737 at F1=0.80
  (Cov=0.94, Pur=0.70), with 16 of 17 cluster-resolved cells landing on
  CLUS_0737 (`at_run_20260508_que2021_pvin_mmc_wmbv1`). This is the
  strongest cluster-level AT signal for bistratified identity in WMBv1
  and is the primary quantitative anchor of this mapping.
- Sibling CLUS_0739 is the preferred BC (basket) landing site in the
  same run (F1=0.83 reported in the run caveats), demonstrating that
  BC and BIC morphological types separate cleanly at cluster resolution
  within SUPT_0206 even though they share Pvalb subclass identity.
- Independent in-silico support: Chamberland 2024 Sst_Tac1 per-cluster
  labels (Harris 2018 cells re-aggregated by Chamberland gene-pair rules,
  n=126 cells reaching Pvalb subclass) land on CLUS_0737 with cluster-
  level Pur=0.94 (Cov=0.31, F1=0.47) in
  `at_run_20260512_chamberland_subfamily_mmc_wmbv1` — high purity confirms
  CLUS_0737 as the specific Sst+Tac1+ landing site within the Pvalb
  branch, consistent with the Sst–Pvalb transcriptomic continuity
  reported for bistratified cells in Chamberland 2024 [9].

**Marker evidence provenance**

- **Pvalb:** confirmed at the patch-seq level by Que et al. 2021 in
  morphologically reconstructed BIC cells [8] and in genetically targeted
  Pvalb-Cre populations by Ekins et al. 2020 [5], Tzilivaki et al. 2023
  [7] and Chamberland et al. 2023 [6] — protein- and transcript-level
  evidence converge. CLUS_0737 itself does not list Pvalb in its MERFISH
  scoped marker panel (it lists Ednra), but Pvalb is the defining marker
  of the parent subclass (Pvalb Gaba) and the patch-seq mapping anchors
  CLUS_0737 to Pvalb+ morphology directly.
- **Sst, Tac1:** Chamberland et al. 2024 [9] established the
  Sst;;Tac1 intersection as a bistratified-cell driver in a morphology-
  confirmed cohort. The CLUS_0737 NP profile (Sst:4.4, Tac1:7.3) is
  directly consistent.
- No marker provenance gaps that warrant a targeted cite-traverse.

**Concerns**

- AT F1=0.80 is good but not high (≥0.90); n_cells_mapped at cluster
  level is 16/20 (4 cells did not reach cluster resolution), and the
  Que 2021 dataset is the only morphology-confirmed PV-IN scRNA-seq
  source currently available — replication is missing.
- Que 2021 input was TPM rounded to integer pseudo-counts (raw counts
  not available for patch-seq); robustness of the CLUS_0737 assignment
  to a true raw-counts re-run is untested.
- Age skew: Que 2021 cohort spans P10–P77 with mean ~P30 (juvenile),
  while WMBv1 reference is adult. Que et al. found high transcriptomic
  similarity of morphological types across age, but a fully adult PV-IN
  patch-seq replication remains desirable.
- The supertype SUPT_0206 pools BC (CLUS_0739) and BIC (CLUS_0737) — at
  supertype level Pvalb morphological types are not separable
  (caveat `DISTRIBUTED_ACROSS_CLUSTERS`).

**What would upgrade confidence**

- A second morphologically confirmed PV-IN scRNA-seq dataset (patch-seq
  or sorted) with adult mice, mapped onto WMBv1 via MapMyCells.
  Expected output: `AnnotationTransferEvidence` reaching F1 ≥ 0.80 at
  CLUSTER level for BIC → CLUS_0737. Resolves open question 1.
- Raw-counts re-run of GSE142546 (if available) confirming CLUS_0737
  assignment is robust to TPM-vs-counts normalisation. Resolves open
  question 2.

### 0206 Pvalb Gaba_2 · 🟡 MODERATE

**Supporting evidence**

- SUPT_0206 is the dominant hippocampal Pvalb supertype and the primary
  atlas branch for canonical PV interneurons of the hippocampus —
  Pvalb is the defining marker of bistratified cells, and the child
  CLUS_0737 carries the bilaminar CA1 SO + SR signature [atlas-internal].
- Que 2021 BIC patch-seq AT places 18/20 BIC cells onto SUPT_0206
  (F1=0.38, Cov=0.90, Pur=0.24 — purity is low because SUPT_0206 also
  contains BC cells from CLUS_0739) (`at_run_20260508_que2021_pvin_mmc_wmbv1`).
- Together with the CLUS_0737 signal, this places bistratified cells
  unambiguously on the PV branch and within Pvalb Gaba_2.

**Concerns**

- Caveat `DISTRIBUTED_ACROSS_CLUSTERS`: SUPT_0206 contains both PV
  basket cells (CLUS_0739) and PV bistratified cells (CLUS_0737); not
  separable at supertype level. This is a normal consequence of the
  atlas hierarchy rather than a defect of the mapping — the cluster-level
  edge resolves it.

**What would upgrade confidence**

- Whether SUPT_0206 contains any morphologically informative
  substructure beyond the BC/BIC cluster-level split is an open question
  (open question 3). Resolves only by deeper subtype analysis (patch-seq
  + transcriptomic clustering at finer resolution).

### 0216 Sst Gaba_3 · 🔴 LOW

This edge is retained to represent a hypothetical Sst-dominant,
Pvalb-low bistratified subpopulation. It is **not** the primary atlas
target for canonical bistratified cells.

**Supporting evidence**

- SUPT_0216 carries Sst as a subclass-defining marker (precomputed
  mean 11.44) and Tac1 in DEFINING_SCOPED markers (precomputed mean
  0.55), both consistent with the Sst;;Tac1 marker logic Chamberland et
  al. used to target bistratified cells [9] [atlas-internal].

![Filtered AT figure for Yao 2021 Pvalb subclass (HIP cells)](figures/f1_for_bistratified_cell_hippocampus_yao_pvalb.png)

*As before, Pur = Purity (fraction of target cells from this source);
Cov = Coverage (fraction of source cells on this target). Yao 2021
(GSE185862) SSv4 'Pvalb' HIP cells (n=66) — a label that mixes PV basket,
axo-axonic and bistratified subtypes. The Pvalb subclass label maps
predominantly to PV chandelier supertype CS20230722_SUPT_0204
(F1=0.61, Pur=1.0, Cov=0.44) and the edge metrics record only 6/66
Pvalb cells reaching CS20230722_SUPT_0216 (Sst Gaba_3) in
`at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1` — a weak signal consistent
with Sst co-expression in a bistratified subset rather than a primary
target.*

**Concerns**

- The Que 2021 morphology-confirmed BIC cohort shows zero mapping to
  any Sst supertype — 18/20 BIC cells land on SUPT_0206 and 16/17 on
  CLUS_0737. The Sst supertype is not the canonical landing site.
- `marker_Pvalb` is DISCORDANT: SUPT_0216 is in the Sst subclass; Pvalb
  is not listed in supertype markers and the precomputed Pvalb mean is
  1.48 — the PV component of bistratified identity is not captured here.
- Location is APPROXIMATE: the dominant MBA signal on SUPT_0216 is
  CA1 stratum oriens (MBA:399, 818 cells) with no pyramidal-layer
  listing, whereas canonical bistratified somata sit in/near stratum
  pyramidale. *(note: CA1 SO is adjacent to stratum pyramidale, so the
  location mismatch is geometrically modest — but combined with the
  Pvalb discordance it is a real signal that this is not the primary
  bistratified target.)*
- Caveat `DISTRIBUTED_ACROSS_CLUSTERS`: SUPT_0216 simultaneously
  contains OLM cells (Sst+/Chrna2+), bistratified cells (in this
  Sst-dominant reading) and HS cells — none separable at supertype level.

**What would upgrade confidence (or downgrade further)**

- A Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq +
  morphology dataset would test whether a Sst-dominant bistratified
  subpopulation exists at all and, if so, whether it maps to SUPT_0216
  specifically. Resolves open question 4. Without such a dataset, this
  edge remains a placeholder for an unobserved subpopulation; an
  alternative outcome is REFUTED (no Sst-dominant bistratified
  subpopulation exists and the edge should be removed).

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The bistratified cell is a `CLASSICAL_MULTIMODAL`
classical node whose defining markers Pvalb [5, 6, 7, 8], Sst [9] and Tac1 [9],
GABAergic NT [4] and CA1 stratum pyramidale / oriens / radiatum location
[1, 2, 3] derive from morphology- and genetics-anchored literature. The
electrophysiology / morphology context is set by Chamberland & Topolnik 2012
[1], Dannenberg et al. 2017 [4] and Ekins et al. 2020 [5]: bistratified cells
sit alongside basket and axo-axonic cells within the PV-IN family but are
distinguished by their bilaminar dendritic-targeting axon arbor in CA1 SO
and SR.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the
WMBv1 taxonomy (CCN20230722) at ranks 0 (cluster) and 1 (supertype) using
metadata-based scoring (region match, NT type, defining markers, sex bias
when applicable). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was
compared to the corresponding atlas-side value via the `property_comparisons`
schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT /
NOT_ASSESSED. Atlas-side numerical values came from precomputed expression on
the cluster (cluster.yaml in the taxonomy reference store) and from MERFISH
spatial registration for soma location.

**Annotation transfer.**

*Run `at_run_20260508_que2021_pvin_mmc_wmbv1` (Que 2021 patch-seq, primary).*

| Field | Value |
|---|---|
| Source dataset | GEO:GSE142546 (Que 2021 patch-seq PV interneurons; BIC = hBIC + vBIC, n=20) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.0 |
| n cells | 88 (filtered to 88) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/manifest.yaml) |
| Script (external) | README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_aggregated_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_que2021_pvin_mmc_wmbv1/f1_scores_aggregated_best.csv) |
| Caveats | TPM input used as pseudo-counts; cohort P10–P77 (mean ~P30) juvenile, WMBv1 adult; AAC n=6 is uninformative. Headline finding: BC and BIC separate cleanly within SUPT_0206 at cluster level — BC → CLUS_0739 (F1=0.83), BIC → CLUS_0737 (F1=0.80). |

*Run `at_run_20260512_chamberland_subfamily_mmc_wmbv1` (in-silico
Chamberland subfamily, secondary).*

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Harris 2018 re-aggregated under Chamberland 2024 gene-pair subfamily rules; Sst_Tac1 label is the bistratified proxy) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_chamberland_subfamily_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Per-cluster derivation is the primary result (dropout-robust); per-cell labels subject to scRNA-seq dropout. Sst_Tac1 label is in-silico from Harris cluster-mean expression, not morphologically confirmed. |

*Run `at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1` (Yao 2021 SSv4 HPF, context).*

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Yao 2021 SSv4 mouse HPF, Pvalb subclass n=66 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | SSv4 'Pvalb' label is the subclass — it pools BC, AAC and BIC morphologies and so cannot resolve bistratified cells specifically. Used here only as context for the SUPT_0216 edge. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. Authored-prose evidence narratives are validated
against their source `evidence_items[*].explanation` fields. The pre-write hook
rejects any unresolvable identifier or unattributed blockquote. Specific
mapping limitations and caveats are documented per-candidate in the Discussion
section.

*Generated by evidencell `50602e9` at 2026-05-26T12:00:33+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

<details>
<summary>Evidence base table</summary>

| Edge ID | Evidence types | Supports | Source |
| --- | --- | --- | --- |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 | ATLAS_METADATA; ANNOTATION_TRANSFER | PARTIAL; SUPPORT | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 | ATLAS_METADATA; ANNOTATION_TRANSFER (×2) | SUPPORT; SUPPORT; PARTIAL | atlas-internal |
| edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 | ATLAS_METADATA; ANNOTATION_TRANSFER (×2) | PARTIAL; PARTIAL; PARTIAL | atlas-internal |

</details>

</details>

---

## Discussion

**Primary mapping:** Bistratified cell → 0737 Pvalb Gaba_2
[CS20230722_CLUS_0737] at MODERATE confidence. Key support: Que 2021 patch-seq
annotation transfer (F1=0.80 at cluster level, 16/17 morphologically confirmed
BIC cells reaching cluster resolution; corroborated by Chamberland Sst_Tac1
in-silico AT, cluster Pur=0.94) plus WMBv1 MERFISH bilaminar CA1 SO+SR cell
distribution and an Sst/Tac1+ neuropeptide profile consistent with Chamberland
et al. 2024 Sst;;Tac1 bistratified genetics. Key caveats:
`DISTRIBUTED_ACROSS_CLUSTERS` (the parent SUPT_0206 also contains PV basket
cells in CLUS_0739, so resolution requires cluster level) and a single
morphology-confirmed AT cohort (juvenile-skewed Que 2021 patch-seq) without
independent replication.

The Cell Ontology has no specific term for the hippocampal Pvalb/Sst/Tac1+
bistratified interneuron; **bistratified cell** [[CL:0004247](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:0004247)]
is a BROAD ancestor whose definition is retinal-focused. CL:0004247 is retained
as the closest available term; a dedicated CL term for the hippocampal
bistratified cell would be a candidate addition.

### Proposed experiments and follow-ups

- **Replication patch-seq / morphology-confirmed scRNA-seq.** A second
  morphologically reconstructed PV-IN dataset in adult mice, mapped by
  MapMyCells to WMBv1. Target: F1 ≥ 0.80 at CLUSTER level for BIC → CLUS_0737.
  Expected output: a second `AnnotationTransferEvidence` item replicating the
  Que 2021 signal. Resolves open question 1 (single-cohort dependence) and
  open question 2 (age-skew robustness).
- **Raw-counts re-mapping of GSE142546 (if upstream raw counts become
  available).** Target: confirm CLUS_0737 assignment is invariant to TPM-vs-
  counts normalisation. Expected output: an `AnnotationTransferEvidence` item
  whose CLUS_0737 F1 is within ±0.05 of the present 0.80. Resolves open
  question 2.
- **Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology.**
  Test whether a Sst-dominant, Pvalb-low bistratified subpopulation exists at
  all. Expected output: either a new `AnnotationTransferEvidence` supporting
  the SUPT_0216 edge with F1 ≥ 0.50, or refutation of the edge. Resolves open
  question 4.
- **Sub-supertype resolution within SUPT_0206 beyond the BC/BIC cluster
  split.** Look for morphologically informative substructure (radiatum-
  targeting, axo-axonic-like) within the SUPT_0206 → CLUS_0737 / CLUS_0739 /
  others tree. Resolves open question 3.

### Open questions

1. Independent replication of Que 2021 BIC → CLUS_0737 F1=0.80 with a
   morphologically confirmed PV bistratified scRNA-seq dataset.
2. Robustness of CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts
   normalisation in GEO:GSE142546.
3. Whether SUPT_0206 provides morphologically informative substructure
   beyond the CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.
4. Whether a Sst-dominant, Pvalb-low bistratified subpopulation exists, and
   if so whether it maps to CS20230722_SUPT_0216 specifically — a question
   that requires a Sst-Cre × Tac1-Flp × Pvalb-negative intersectional
   scRNA-seq + morphology dataset.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| 1 | Chamberland & Topolnik 2012 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426) | Soma location, ephys/morphology context |
| 2 | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | Soma location |
| 3 | Perez et al. 2020 | [33404500](https://pubmed.ncbi.nlm.nih.gov/33404500) | Soma location |
| 4 | Dannenberg et al. 2017 | [29321728](https://pubmed.ncbi.nlm.nih.gov/29321728) | Neurotransmitter type |
| 5 | Ekins et al. 2020 | [33150866](https://pubmed.ncbi.nlm.nih.gov/33150866) | Pvalb marker |
| 6 | Chamberland et al. 2023 | [37162922](https://pubmed.ncbi.nlm.nih.gov/37162922) | Pvalb marker |
| 7 | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Pvalb marker |
| 8 | Que et al. 2021 | [33398060](https://pubmed.ncbi.nlm.nih.gov/33398060) | Pvalb marker; patch-seq BIC source |
| 9 | Chamberland et al. 2024 | [38640347](https://pubmed.ncbi.nlm.nih.gov/38640347) | Sst, Tac1 markers; Sst;;Tac1 bistratified genetics |

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_CLUS_0737 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.72
  rationale: >
    Que 2021 patch-seq BIC (hBIC + vBIC, n=20) lands on CS20230722_CLUS_0737
    at F1=0.80 in at_run_20260508_que2021_pvin_mmc_wmbv1, the strongest
    cluster-level signal in WMBv1, supported independently by Chamberland
    Sst_Tac1 in-silico AT in at_run_20260512_chamberland_subfamily_mmc_wmbv1
    (CS20230722_CLUS_0737 cluster Pur=0.94). 3 of 3 markers CONSISTENT
    (Pvalb, Sst, Tac1) anchored in patch-seq, MERFISH and scRNA-seq
    modalities, alongside CONSISTENT NT and bilaminar CA1 SO+SR location.
    Replication and a raw-counts re-run remain caveats.
  unresolved_questions:
    - Replication of Que 2021 BIC → CS20230722_CLUS_0737 F1=0.80 with an independent morphologically confirmed PV bistratified scRNA-seq dataset.
    - Robustness of CS20230722_CLUS_0737 assignment to raw-counts vs TPM-pseudo-counts normalization in GEO:GSE142546.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0206 -->
```yaml
verdict:
  confidence: MODERATE
  confidence_score: 0.62
  rationale: >
    Que 2021 patch-seq BIC maps to CS20230722_SUPT_0206 at F1=0.38 with
    coverage 0.90 (18/20 cells) in at_run_20260508_que2021_pvin_mmc_wmbv1;
    the low supertype F1 reflects pooling of BC and BIC morphologies within
    SUPT_0206 rather than a weakness of the assignment — cluster-level
    resolution at CS20230722_CLUS_0737 recovers the BIC landing site
    cleanly. 3 of 3 markers CONSISTENT (Pvalb, Sst, Tac1) supported
    by scRNA-seq and immunohistochemistry; NT and Pvalb subclass also
    CONSISTENT.
  unresolved_questions:
    - Whether CS20230722_SUPT_0206 provides morphologically informative substructure beyond the CS20230722_CLUS_0737 / CLUS_0739 BIC/BC cluster-level split.
```
<!-- verdict-block-end -->

<!-- verdict-block-start: edge_bistratified_cell_hippocampus_to_CS20230722_SUPT_0216 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.22
  rationale: >
    Morphologically confirmed Que 2021 BIC patch-seq shows zero mapping to
    any Sst supertype in at_run_20260508_que2021_pvin_mmc_wmbv1 — 18/20
    cells land on CS20230722_SUPT_0206 and 16/17 cluster-resolved cells
    on CS20230722_CLUS_0737. Yao 2021 SSv4 Pvalb-subclass cells map only
    6/66 to CS20230722_SUPT_0216 in
    at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1. 3 of 4 markers CONSISTENT
    (Sst, Tac1, Gad1 by scRNA-seq); Pvalb DISCORDANT (Sst subclass, atlas
    Pvalb mean 1.48); location APPROXIMATE (CA1 SO, not stratum pyramidale).
    Edge retained as placeholder for a hypothetical Sst-dominant,
    Pvalb-low bistratified subpopulation not yet observed in any
    morphology-confirmed dataset.
  unresolved_questions:
    - Does a Sst-dominant Pvalb-low bistratified subpopulation exist, and if so does it map to CS20230722_SUPT_0216 specifically? Requires a Sst-Cre × Tac1-Flp × Pvalb-negative intersectional scRNA-seq + morphology dataset.
```
<!-- verdict-block-end -->
