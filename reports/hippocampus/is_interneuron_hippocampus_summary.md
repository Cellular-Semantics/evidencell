# Interneuron-specific (IS) interneuron — WMBv1 (CCN20230722) Mapping Report
*2026-04-09 · Source: `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`*

---

## Introduction

Interneuron-specific (IS) interneurons are GABAergic cells in hippocampal CA1
whose defining functional property is selective innervation of other GABAergic
interneurons rather than pyramidal cells — a disinhibitory motif that amplifies
the activity of pyramidal-cell networks by suppressing their inhibitory inputs.
Three subtypes are recognised: IS-1 (calretinin+/VIP−), IS-2 (VIP+), and IS-3
(calretinin+/VIP+) [1][2].

> "The so-called interneuron-specific (IS) cells were identified based on direct ultrastructural evidence that some calretinin (CR)- expressing or vasoactive intestinal polypeptide (VIP)-expressing GABAergic cells in the CA1 area of the hippocampus contact interneurons selectively. IS cells were further subdivided into three subtypes with distinct anatomical and neurochemical features."
> — Tyan et al. 2014, Classical Functional and Morphological Interneuron Types · [1] <!-- quote_key: 23480858_1f4801fb -->

> "Freund and colleagues first characterized IS interneurons and showed that these cells express calretinin (CR) (IS-1), VIP (IS-2), or both (IS-3)"
> — Tzilivaki et al. 2023, Transcriptomic Interneuron Classifications · [2] <!-- quote_key: 259953057_10f139f9 -->

### Classical type table

| Property | Value | References |
|---|---|---|
| Soma location | CA1 stratum oriens [UBERON:0014552]; CA1 stratum radiatum [UBERON:0014554]; CA1 stratum lacunosum moleculare [UBERON:0014557] | [1] |
| NT | GABAergic | — |
| Markers | Calb2 (calretinin), Vip | [1][2][3][4] |
| Neuropeptides | Vip | [2] |
| CL term | VIP GABAergic interneuron [CL:4023016] (BROAD) | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location and IS cell definition:** direct ultrastructural evidence in CA1 · [1]

- **IS-1/2/3 subtype scheme:** [2]

- **Bocchio et al. 2024 context:** sampling of IS subtypes in CA1 pyramidal layer · [4]
  > "This mouse line allows for a large sampling from diverse interneuron subtypes in the CA1 pyramidal layer, including the most representative ones (Bezaire et al., 2013), the PV-expressing basket and bistratified cells (Klausberger et al., 2008), the NOS- expressing ivy cells (14381729) and two types of interneuron-selective interneurons (ISI 1 and 3) that express calretinin (Klausberger et al., 2008)(Topolnik et al., 2022)"
  > — Bocchio et al. 2024, Classical Functional and Morphological Interneuron Types · [4] <!-- quote_key: 262127573_d140faf4 -->

</details>

Cell Ontology mapping: VIP GABAergic interneuron [[CL:4023016](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4023016)] (BROAD). CL:4023016 captures the VIP+ subset (IS-2 and IS-3) but not IS-1 (CR+/VIP−). The defining functional feature — selective interneuron targeting for disinhibition — is not encoded in any current CL term.

---

## Results

One MODERATE candidate atlas mapping was assessed. 0179 Vip Gaba_7
[CS20230722_SUPT_0179] is the primary mapping target based on confirmed
Vip and Calb2 expression, multi-laminar CA1 anatomical distribution, and
two independent annotation-transfer runs. Evidence is PARTIAL because the
Yao 2021 source label pools IS and non-IS VIP interneurons, and the IS-1
subtype (VIP−/CR+) cannot map to a Vip-defined supertype.

### Mapping candidates table

| Rank | WMBv1 cluster | Supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---|---|---|-:|----|---|---|
| 1 | — | 0179 Vip Gaba_7 [CS20230722_SUPT_0179] | 215 | 🟡 MODERATE | Vip CONSISTENT · Calb2 CONSISTENT · multi-laminar CA1 CONSISTENT | Best candidate |

Total: 1 edge (MODERATE); relationship type: PARTIAL_OVERLAP.

### Primary candidate property alignment — 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · 🟡 MODERATE

**Table 1 — Property comparison.**

| Property | Classical | Supertype | Best cluster | Alignment |
|---|---|---|---|---|
| NT type | GABAergic | GABA | — | CONSISTENT |
| Soma location — SO | CA1 stratum oriens [UBERON:0014552] | CA1 SO: 24 cells | — | CONSISTENT |
| Soma location — SR | CA1 stratum radiatum [UBERON:0014554] | CA1 SR: 26 cells | — | CONSISTENT |
| Soma location — SLM | CA1 stratum lacunosum-moleculare [UBERON:0014557] | not in top locations | — | NOT_ASSESSED |
| Vip expression | defining marker (IHC/transgenic) | Vip — DEFINING marker; precomputed mean 6.82 | — | CONSISTENT |
| Calb2 expression | defining marker (IHC) | not listed in atlas markers; precomputed mean 6.78 | — | CONSISTENT |
| Vip neuropeptide | present | precomputed mean 6.82 | — | CONSISTENT |

**Table 2 — Evidence support.**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Atlas metadata: Vip, multi-laminar CA1 anatomy | ATLAS_METADATA | PARTIAL | CA1 SO/SR present; additional defining markers Qrfpr/Stk32a/Igfbp4 without IS correspondence | atlas-internal |
| Precomputed stats: Calb2=6.78, Vip=6.82 | ATLAS_METADATA | SUPPORT | Both defining markers confirmed | atlas-internal |
| Yao 2021 SSv4 Vip → WMBv1 AT | ANNOTATION_TRANSFER | PARTIAL | SUPT_0179 F1=0.379 (96/476 cells); Vip subclass F1=0.969; dispersed across 10+ supertypes | GEO:GSE185862 |
| Harris 2018 Calb2.Vip.Igfbp4 → SUPT_0179 | ANNOTATION_TRANSFER | PARTIAL | SUPT_0179 F1=0.612 (26 cells, 57.8% of class); group_purity=0.578 | GEO:GSE99888 |

### 0179 Vip Gaba_7 [CS20230722_SUPT_0179] · 🟡 MODERATE

**Supporting evidence**

- Both defining markers are strongly confirmed by precomputed stats: Vip mean=6.82 (DEFINING marker, CONSISTENT) and Calb2 mean=6.78 (CONSISTENT, though Calb2 is absent from the atlas supertype's named markers). NT type is GABAergic (CONSISTENT with GABA atlas).
- Atlas metadata records SUPT_0179 cells in CA1 stratum oriens (24 cells; CONSISTENT) and CA1 stratum radiatum (26 cells; CONSISTENT), matching two of the three classical IS soma locations cited by Tyan et al. 2014 [1].
- Yao 2021 (GEO:GSE185862) SSv4 Vip hippocampal cells (n=476) map very strongly to the Vip Gaba subclass at subclass level (F1=0.969, 463/476 cells), confirming VIP-family identity. At supertype level, 0179 Vip Gaba_7 [CS20230722_SUPT_0179] receives 96 cells (F1=0.379, target_purity=0.970), ranking second to 0177 Vip Gaba_5 (101 cells, F1=0.397). The broad Vip dispersal across 10+ supertypes is consistent with the known heterogeneity of VIP interneurons (IS-1/2/3 plus VIP basket cells).
- Harris 2018 (GEO:GSE99888) Class Calb2.Vip.Igfbp4 (Calb2+/Vip+/Igfbp4+ CA1 interneurons, n=98 cells) maps entirely to Vip Gaba subclass (100% recall) and 57.8% to 0179 Vip Gaba_7 [CS20230722_SUPT_0179] (F1=0.612, 26/45 cells). The complete recall at SUBCLASS confirms Vip family assignment; the modest concentration at SUPT_0179 provides partial additional corroboration.

**Marker evidence provenance**

- **Calb2 (calretinin):** Protein-level (IHC) evidence from Tyan et al. 2014 [1] (direct ultrastructural identification in CA1) and Chamberland & Topolnik 2012 [3] (review). Tzilivaki et al. 2023 [2] provides transcriptomic context. Data discrepancy: Calb2 is not listed as a defining marker of SUPT_0179 in atlas metadata, yet precomputed stats return a mean of 6.78 — both values are recorded. Calb2 may be expressed at variable levels across multiple Vip supertypes rather than being specific to SUPT_0179.
- **Vip:** IHC and transgenic reporter-level evidence from Tzilivaki et al. 2023 [2] and Bocchio et al. 2024 [4]. Bocchio et al. 2024 [4] used a Vip-IRES-Cre driver in CA1, providing direct targeting of VIP-expressing cells in the appropriate context. Vip is a DEFINING marker of SUPT_0179 with precomputed mean=6.82 — no discrepancy.

**Concerns**

- **IS-1 subtype not captured.** IS-1 cells are VIP−/CR+ and would not map to a Vip supertype. This edge represents only IS-2 (VIP+) and IS-3 (VIP+/CR+). A Calb2+/Vip-negative supertype candidate for IS-1 has not been identified in this mapping graph.
- **VIP basket cells co-occur (MARKER_NOT_SPECIFIC).** Hippocampal VIP interneurons include VIP basket cells in addition to IS cells. SUPT_0179 may encompass both perisomatic VIP basket cells and disinhibitory IS cells. The interneuron-specific targeting feature of IS cells is not resolvable from transcriptomic metadata alone.
- **Stratum lacunosum-moleculare NOT_ASSESSED.** SLM [UBERON:0014557] is listed as a classical IS soma location [1] but is not recorded among the top-count anatomical locations for SUPT_0179.
- **Additional atlas defining markers without IS correspondence.** Qrfpr, Stk32a, and Igfbp4 are additional defining markers of SUPT_0179; none appears in the classical IS literature surveyed.
- **AT is not IS-cell-specific.** The Yao 2021 SSv4 source label pools IS cells and all other VIP interneuron types without discriminating labels. F1=0.969 at subclass confirms VIP family membership but does not provide IS-specific evidence.

**What would upgrade confidence**

- IS-cell-specific annotation transfer: a dataset with morphologically identified IS cells (IS-1, IS-2, IS-3 individually) mapped via MapMyCells onto WMBv1. Target: F1 ≥ 0.80 at SUPERTYPE. Expected output: AnnotationTransferEvidence discriminating IS cells from VIP basket cells within the Vip Gaba clade.
- IS-1 candidate identification: `just find-candidates` query on WMBv1 filtered for Calb2 expression + hippocampal anatomy + GABAergic NT, excluding Vip-defining supertypes. Expected output: a new LOW or MODERATE edge for IS-1 (CR+/VIP−) in this graph.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** IS interneurons are defined on a CLASSICAL_MULTIMODAL
basis: soma in CA1 stratum oriens [UBERON:0014552], stratum radiatum [UBERON:0014554],
and stratum lacunosum-moleculare [UBERON:0014557] [1]; GABAergic; defining markers
Calb2 and Vip [1][2][3][4]; neuropeptide Vip [2]. Three subtypes (IS-1, IS-2, IS-3)
are recognised. This edge covers IS-2 and IS-3 only (VIP+); IS-1 has no current
mapping edge.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the WMBv1
taxonomy (CCN20230722) at rank 1 (supertype) using metadata-based scoring. Full
scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property was compared to atlas values with
alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED.

**Annotation transfer.**

Run 1 — Yao 2021 SSv4 hippocampal formation → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE185862 (Vip; n=476 HIP cells) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722) |
| Method | MapMyCells local (cell_type_mapper, default parameters, raw normalization, 100 bootstrap iterations) |
| Tool version | cell_type_mapper |
| Bootstrap threshold | 0.0 |
| n cells total | 6398 (filtered to 6398) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_scores_best.csv`](../../kb/annotation_transfer_runs/at_run_20260508_yao2021_hpf_ssv4_mmc_wmbv1/f1_scores_best.csv) |
| Caveats | Yao 2021 SSv4 Vip label pools IS and non-IS VIP types; IS-specific resolution unavailable. |

Run 2 — Harris 2018 (GSE99888) published Class labels → WMBv1:

| Field | Value |
|---|---|
| Source dataset | GEO:GSE99888 (Calb2.Vip.Igfbp4 class; n=98 cells from 3663 total) |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells (cell_type_mapper v1.7.1, default parameters, raw normalization, bootstrap_iteration=100) |
| Tool version | cell_type_mapper v1.7.1 |
| Bootstrap threshold | 0.8 |
| n cells total | 3663 (filtered to 3663) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/manifest.yaml) |
| Script (external) | ../at_run_20260506_harris_chamberland_mmc_wmbv1/README.md |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| F1 matrix | [`f1_matrix_harris_class.csv`](../../kb/annotation_transfer_runs/at_run_20260512_harris_class_mmc_wmbv1/f1_matrix_harris_class.csv) |
| Caveats | Harris 2018 Calb2.Vip.Igfbp4 class is not specifically IS-labelled; provides PARTIAL corroboration that Calb2+/Vip+ cells map to SUPT_0179. |

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and
verbatim literature quotes in this report are validated against the evidencell
knowledge base at write time. The pre-write hook rejects any unresolvable identifier
or unattributed blockquote.

*Generated by evidencell `07c6dbd` at 2026-05-19T10:45:25+00:00 from
[kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml](kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml).*

**Evidence base table.**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_is_interneuron_hippocampus_to_CS20230722_SUPT_0179 | ATLAS_METADATA ×2; ANNOTATION_TRANSFER ×2 | PARTIAL; SUPPORT; PARTIAL; PARTIAL | atlas-internal |

</details>

---

## Discussion

**Primary mapping:** Interneuron-specific interneuron → 0179 Vip Gaba_7 [CS20230722_SUPT_0179] at MODERATE confidence. Key support: both defining markers confirmed by precomputed stats (Calb2=6.78, Vip=6.82); multi-laminar CA1 distribution matching IS soma locations; Yao 2021 subclass F1=0.969 confirming VIP family; Harris 2018 Calb2.Vip.Igfbp4 class F1=0.612 at SUPT_0179. Key caveats: the classical IS node covers three subtypes — this edge covers IS-2 and IS-3 (VIP+) only, with IS-1 (CR+/VIP−) having no current mapping; VIP basket cells co-occur in SUPT_0179 and cannot be discriminated from IS cells by transcriptomics alone; the disinhibitory circuit function of IS cells has no transcriptomic correlate at supertype resolution.

The Cell Ontology BROAD mapping to CL:4023016 (VIP GABAergic interneuron) captures the VIP+ subset (IS-2 and IS-3) but omits IS-1 (CR+/VIP−) and does not encode the IS-defining functional property of selective interneuron targeting. A dedicated IS cell CL term would be valuable for capturing the full IS population and the disinhibitory motif.

### Proposed experiments

**IS-cell-specific annotation transfer**

- Obtain a dataset with morphologically or physiologically confirmed IS cell labels (IS-1, IS-2, IS-3 individually identified by their target specificity in CA1), run MapMyCells onto WMBv1. Target: F1 ≥ 0.80 at SUPERTYPE for each IS subtype. Expected output: AnnotationTransferEvidence discriminating IS cells from VIP basket cells and from other VIP interneuron subtypes. This is the most informative single experiment for this node.

**IS-1 candidate identification**

- `just find-candidates` query on WMBv1 filtered for Calb2 expression + hippocampal anatomy + GABAergic NT, excluding Vip-defining supertypes. Target: identify ≥1 candidate supertype with Calb2 as defining or high-expression marker and no Vip. Expected output: a new LOW or MODERATE mapping edge for IS-1 (CR+/VIP−) in this graph. Resolves: open question 2.

**Targeted cite-traverse for Calb2 / IS marker specificity**

- Cite-traverse for "calretinin interneuron-specific hippocampus" and "IS-1 interneuron calretinin CA1" to confirm Calb2/calretinin as a marker specifically for morphology-confirmed IS cells (rather than calretinin-positive interneurons broadly). Expected output: strengthened LiteratureEvidence for the Calb2 marker attribution.

### Open questions

1. Can WMBv1 supertypes discriminate IS cells from VIP basket cells based on transcriptomic signature alone? The disinhibitory connectivity motif of IS cells may not have a distinctive transcriptomic correlate at supertype resolution.
2. Which WMBv1 supertype(s) contain IS-1 (CR+/VIP−) cells? A Calb2+/Vip-negative supertype with hippocampal anatomy has not yet been identified in this mapping.
3. Does the Calb2 atlas-detected expression (precomputed mean=6.78 at SUPT_0179) reflect IS-1/IS-3 cells specifically, or is it broadly expressed across the Vip Gaba clade?
4. What are the functional roles of Qrfpr, Stk32a, and Igfbp4 — the additional atlas-defining markers of SUPT_0179 — in IS cell identity?
5. Does stratum lacunosum-moleculare represent a genuine IS soma location, or is it sparse/transient? It is listed in the classical node [1] but is not among the top anatomical counts in SUPT_0179.

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Tyan et al. 2014 | [24671999](https://pubmed.ncbi.nlm.nih.gov/24671999) | soma location; IS cell definition |
| [2] | Tzilivaki et al. 2023 | [37467748](https://pubmed.ncbi.nlm.nih.gov/37467748) | Calb2 marker; Vip marker; IS subtype scheme |
| [3] | Chamberland & Topolnik 2012 | [23162426](https://pubmed.ncbi.nlm.nih.gov/23162426) | Calb2 marker |
| [4] | Bocchio et al. 2024 | [39401246](https://pubmed.ncbi.nlm.nih.gov/39401246) | Vip marker |
