# Central amygdala medium spiny neuron — CCN20230722 Mapping Report
*2026-06-09 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml`*

---

## Introduction

The central amygdala medium spiny neuron (CeA MSN) is a morphologically distinctive GABAergic cell type defined by its ovoid soma, primary non-spiny dendrites that branch into spiny secondary and tertiary processes — a morphology closely paralleling that of striatal medium spiny neurons and consistent with the CeA's striatopallidal-like developmental origin [1]. Ppp1r1b (DARPP-32), a phosphoprotein enriched in striatal MSNs, has been reported to correlate with lateral CeA types [4], making it a candidate defining molecular marker. CeA MSNs are the predominant cell type of the lateral CeA and constitute the major GABAergic output population. This report documents a remap from the prior CLUS_0723 (Lamp5 Gaba_4) assignment to CLUS_1344 ("CEA-BST Six3 Cyp26b1 Gaba_5"), supported by annotation-transfer evidence from Hochgerner 2023 source type GABA-11-Adora2a-Id4.

### Classical type description

| Property | Value | References |
|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | [1] |
| Neurotransmitter | GABAergic | [2], [3] |
| Defining markers | Ppp1r1b (DARPP-32) | [4] |
| Negative markers | — | — |
| Neuropeptides | — | — |
| Morphology | Ovoid soma; primary non-spiny dendrites; spiny secondary and tertiary dendrites; medium spiny profile | [1] |
| Definition basis | CLASSICAL | — |
| Notes | Striatum-like morphology consistent with CeA's striatopallidal-like organization. | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location:** morphological description · reviewed in Nikolenko et al. 2020 · [1]
  > "Morphologically, there are several types of neurons located in the central nucleus of the amygdala (CeA). In the lateral sector of the central nucleus, a predominant cell type with ovoid soma is located. These cells have several primary nonspiny dendrites, branching onto spiny secondary and tertiary dendrite. Their axons begin branching even before leaving the nucleus, which is why these cells are called \"medium spiny neurons\" (Hall, 2004)(McDonald, 1982). Another type of neurons located in the central nuclei have big soma with thick aspiny dendrites, branching on to secondary seldom spiny processes (McDonald, 1982)(Cassell et al., 1989) (Schiess et al., 1999). The third type of cells are small aspiny neurons (Cassell et al., 1989)"
  > — Nikolenko et al. 2020, Central amygdala cell types · [1] <!-- quote_key: 220976356_f1fe3fe1 -->

- **Neurotransmitter (GABAergic):** review of amygdala neuron classification · [2]
  > "Neuronal types differ considerably among the subdivisions of the amygdala (Sah et al., 2003). In the basolateral group, approximately 70% of neurons are thought to be glutamatergic (pyramidal, spiny, or class I neurons). This division also contains interneurons such as GABAergic nonspiny stellate cells of the cortex (called S cells, stellate, or class II neurons). In contrast, within the central nucleus, the majority of cells are thought to be GABAergic."
  > — Ignacio et al. 2014, Classical neuron classes across amygdala subdivisions · [2] <!-- quote_key: 1229611_f7a0a034 -->

- **Neurotransmitter (GABAergic):** CeA as primarily GABAergic output nucleus · [3]
  > "The central amygdala (CeA) plays a central role in physiological and behavioral responses to fearful stimuli, stressful stimuli, and drug-related stimuli. The CeA receives dense inputs from cortical regions, is the major output region of the amygdala, is primarily GABAergic (inhibitory), and expresses high levels of pro- and anti-stress peptides."
  > — Gilpin et al. 2014, Central amygdala cell types · [3] <!-- quote_key: 442779_deea5502 -->

- **Defining marker — Ppp1r1b:** single-cell atlas characterisation of CeA Ppp1r1b+ types · [4]
  > "The Ppp1r1b types correlated with the lateral CEA"
  > — Hochgerner et al. 2023, Inhibitory neurons of valence-learning modulation and output · [4] <!-- quote_key: 264517392_113398c6 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: medium spiny neuron [[CL:1001474](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001474)] (BROAD).

The Cell Ontology has no specific term for a CeA-restricted medium spiny neuron population; CL:1001474 is the closest ancestor. Auto-proposed by asta-report-ingest; requires expert review.

---

## Results

One candidate atlas cluster was assessed; CS20230722_CLUS_1344 ("CEA-BST Six3 Cyp26b1 Gaba_5") is the primary mapping at LOW confidence. Annotation-transfer evidence from Hochgerner 2023 source type GABA-11-Adora2a-Id4 provides PARTIAL support (F1=0.677 at cluster level, purity=0.933), confirming that cells of this transcriptomic type — isolated from CeA tissue — preferentially map to CLUS_1344. However, only 53% of GABA-11 cells reach CLUS_1344 (recall=0.532), with the remainder splitting to STR D2 (SUPT_0274). A secondary Drd1+ source group (GABA-14-Drd1-Scn4b) maps instead to STR D1 Gaba (F1=0.710 at subclass level), revealing 1:n heterogeneity: the classical "medium spiny" morphotype encompasses at least two transcriptomically distinct populations.

### Mapping candidates table

| Rank | WMBv1 cluster | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|---|---|---|
| 1 | CS20230722_CLUS_1344 (CEA-BST Six3 Cyp26b1 Gaba_5) | not assessed | 🔴 LOW | AT PARTIAL F1=0.677 · CEA-BST lineage CONSISTENT | broadMatch; 1:n heterogeneity |

*1 edge assessed; relationship type: skos:broadMatch. n_cells null — taxonomy DB rebuild required (see Methods).*

### Property alignment table — CS20230722_CLUS_1344

**Table 1 — Property comparison**

| Property | Classical | Best cluster (CLUS_1344) | Alignment |
|---|---|---|---|
| Soma location | Central amygdaloid nucleus [UBERON:0002883] | MBA:536 AT maps CeA-isolated cells to CLUS_1344 "CEA-BST Six3 Cyp26b1 Gaba_5"; Six3/Cyp26b1 mark the central extended amygdala lineage; WMBv1 region_fraction not in CeA survival cohort (cluster may be sampled primarily in BST by atlas) | CONSISTENT |
| NT type | GABAergic | GABA | CONSISTENT |
| Morphology (medium spiny) | Ovoid soma, spiny secondary/tertiary dendrites | NOT_ASSESSED — morphological information not available from WMBv1 transcriptomic atlas | NOT_ASSESSED |
| Ppp1r1b (DARPP-32) | Defining marker; correlated with lateral CEA [4] | NOT_ASSESSED — Ppp1r1b expression in CLUS_1344 not confirmed from available precomputed expression data | NOT_ASSESSED |
| Sex ratio | not documented | not assessed | NOT_ASSESSED |

**Table 2 — Evidence support**

| Evidence | Type | Supports | Headline | Source |
|---|---|---|---|---|
| Nikolenko 2020 morphology review | Literature | PARTIAL | Classical type definition (morphology); no transcriptomic mapping | [1] |
| CLUS_1344 atlas metadata — CEA-BST lineage | Atlas metadata | PARTIAL | Six3/Cyp26b1 mark CeA/AAA/BST identity; 42/45 cells from GABA-11 (purity 0.933); absent from CeA rank-0 cohort | atlas-internal |
| Hochgerner 2023 AT — GABA-11-Adora2a-Id4 | Annotation transfer | PARTIAL | F1=0.677 at cluster; purity=0.933; recall=0.532; remainder split to STR D2 | — |
| Hochgerner 2023 AT — GABA-14-Drd1-Scn4b | Annotation transfer | AGAINST | Drd1+ subset maps to STR D1 Gaba subclass (F1=0.710); distinct from CLUS_1344 | — |

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### CS20230722_CLUS_1344 (CEA-BST Six3 Cyp26b1 Gaba_5) · 🔴 LOW

**Supporting evidence:**

- **AT PARTIAL — GABA-11-Adora2a-Id4 (F1=0.677, purity=0.933):** In the Hochgerner 2023 MapMyCells run (at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1), source type GABA-11-Adora2a-Id4 (n=79 cells, CeA-isolated naive neurons) maps to CLUS_1344 at cluster level with F1=0.677 and purity=0.933. High purity (0.933) confirms that the majority of CLUS_1344 cells in the WMBv1 reference come from the GABA-11 transcriptomic type, establishing a genuine identity link. The partial recall (0.532) means that about half the GABA-11 source cells reach CLUS_1344 while the remainder split to STR D2 (SUPT_0274) — consistent with a transcriptomically heterogeneous source type spanning CeA-BST and striatal lineages. 42 of 45 CLUS_1344 cells matching GABA-11 (purity 0.933) is a strong compositional signal at cluster level.

- **CEA-BST lineage (CONSISTENT):** CLUS_1344 "CEA-BST Six3 Cyp26b1 Gaba_5" resides in the central extended amygdala lineage defined by Six3 and Cyp26b1 transcription factors, which mark CeA/AAA/BST identity. The source cells (GABA-11) were isolated from CeA tissue in the Hochgerner 2023 study, confirming that this transcriptomic type is present in CeA-dissected material. *(Note: WMBv1 may primarily sample CLUS_1344 cells from BST rather than CeA in the atlas — low CeA region_fraction in the rank-0 survival cohort suggests this; however, the CeA origin of the source cells argues for CeA presence.)*

- **NT type (CONSISTENT):** CLUS_1344 is designated GABA, consistent with the classical GABAergic identity of CeA medium spiny neurons [2][3].

- **Literature morphology anchor:** Nikolenko et al. 2020 [1] describes the medium spiny neuron as the predominant lateral CeA cell type with ovoid soma and branching spiny secondary dendrites — establishing the morphological class. Hochgerner et al. 2023 [4] reports that Ppp1r1b+ types correlate with the lateral CEA, providing indirect molecular evidence that DARPP-32-expressing cells (the expected marker for striatal MSN-like types) are present in the lateral CeA subdivision.

  > "The Ppp1r1b types correlated with the lateral CEA"
  > — Hochgerner et al. 2023, Inhibitory neurons of valence-learning modulation and output · [4] <!-- quote_key: 264517392_113398c6 -->

**Marker evidence provenance:**

- **Ppp1r1b (DARPP-32):** Hochgerner et al. 2023 [4] provides transcript-level evidence from a scRNA-seq atlas with spatial registration confirming lateral CeA localisation of Ppp1r1b+ types. The evidence is methodologically appropriate but the specific CCN20230722 cluster identity of the Ppp1r1b+ lateral CeA types has not been confirmed from available precomputed expression data for CLUS_1344. Source-side Ppp1r1b relevance is established; target-side (CLUS_1344 expression level) is NOT_ASSESSED.

  ⚠ **Atlas annotation/expression gap:** Ppp1r1b expression in CLUS_1344 cannot be confirmed or refuted from the currently available precomputed expression data. Until HDF5 stats are queried for CLUS_1344 Ppp1r1b levels, the defining marker remains unverified on the target side. This is a notable gap — DARPP-32 is the classical morphological marker linking CeA MSNs to the striatal lineage, and its absence or presence in CLUS_1344 would substantially change the confidence assessment.

**Concerns:**

- **NO_DISCRIMINATING_MARKER:** Ppp1r1b (DARPP-32) expression in CLUS_1344 is NOT_ASSESSED. The classical MSN marker remains unverified on the target side, limiting discrimination from other CeA GABAergic clusters.

- **TAXONOMY_LEVEL_MISMATCH:** CLUS_1344 does not appear in the WMBv1 CeA rank-0 survival cohort (filtered to MBA:536 + GABAergic), suggesting primary atlas sampling in BST rather than CeA. However, Hochgerner source cells were CeA-isolated, supporting CeA presence of this type. The low WMBv1 CeA region_fraction does not negate the AT result — it means the atlas registration undersamples this cluster in CeA relative to BST.

- **DISTRIBUTED_ACROSS_CLUSTERS (1:n heterogeneity):** Drd1+ CeA MSN subset GABA-14-Drd1-Scn4b (n=29 cells) maps to STR D1 Gaba (F1=0.710 at subclass level), not CLUS_1344. This confirms that the classical "medium spiny" morphotype encompasses at least two transcriptomically distinct populations: (a) the Adora2a+Id4 CEA-BST lineage (→ CLUS_1344) and (b) the Drd1+ striatal D1 lineage. The broadMatch predicate correctly signals this 1:n situation.

**What would upgrade confidence:**

1. **Ppp1r1b expression query for CLUS_1344 (ATLAS_QUERY, no new data required once HDF5 available):** Query CCN20230722 precomputed expression for Ppp1r1b in CLUS_1344. If expression is above MIN_DETECTABLE, this would directly link the DARPP-32 lateral CeA marker to the AT-supported cluster and upgrade confidence to MODERATE. Expected output: ATLAS_QUERY evidence item.

2. **ISH for Ppp1r1b and Six3/Sp9 in mouse CeA (LiteratureEvidence):** Co-expression ISH to verify that DARPP-32+ cells in lateral CeA express Six3/Sp9 (the lineage markers of CLUS_1344). Would link the classical DARPP-32 morphological marker to the CEA-BST Six3 transcriptomic lineage. Expected output: LiteratureEvidence confirming marker correspondence.

3. **Patch-seq of morphologically confirmed CeA MSNs (AnnotationTransferEvidence):** Profile morphologically identified CeA MSNs (ovoid soma + spiny dendrites confirmed by biocytin fill) with single-cell transcriptomics and map to WMBv1. Would determine whether Adora2a+Id4 and Drd1+ subtypes correspond to distinct morphologies or both exhibit the medium spiny profile. Expected output: AnnotationTransferEvidence resolving Q2.

---

## Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** Central amygdala medium spiny neuron is defined on a CLASSICAL basis: morphological characterisation from McDonald (1982) and Hall (2004) as reviewed in Nikolenko et al. 2020 [1], with GABAergic neurotransmitter type supported by two independent reviews [2][3]. The defining molecular marker Ppp1r1b/DARPP-32 cites Hochgerner et al. 2023 [4] (lateral CeA correlation). This edge was established in hypothesis mode, remapping from the prior CLUS_0723 (Lamp5 Gaba_4) assignment to CLUS_1344 (CEA-BST Six3 Cyp26b1 Gaba_5) based on AT evidence from the Hochgerner 2023 MapMyCells run.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at rank 0 (cluster) using metadata-based scoring. This edge was the product of hypothesis-mode mapping guided by AT evidence (GABA-11-Adora2a-Id4 → CLUS_1344). Full scoring rules: `workflows/map-cell-type.md`.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / NOT_ASSESSED. Atlas-side morphological features are structurally NOT_ASSESSED; Ppp1r1b expression is NOT_ASSESSED pending HDF5 stats.

**Annotation transfer.** Annotation transfer was performed using MapMyCells (cell_type_mapper v1.7.1) against WMBv1 (CCN20230722). Source dataset: Hochgerner et al. 2023 (ArrayExpress:E-MTAB-12096; naive neuronal cells only; n=7,777 after filtering). Two source types were assessed for this edge: GABA-11-Adora2a-Id4 (n=79 cells; PARTIAL, F1=0.677, purity=0.933) and GABA-14-Drd1-Scn4b (n=29 cells; AGAINST, maps to STR D1 subclass F1=0.710).

| Field | Value |
|---|---|
| Source dataset | ArrayExpress:E-MTAB-12096 |
| Source species | NCBITaxon:10090 |
| Target atlas | WMBv1 (CCN20230722; SHA-256: b21ca985) |
| Method | MapMyCells local (cell_type_mapper v1.7.1, raw normalization) |
| Bootstrap threshold | 0.7 |
| n cells | 55,514 (filtered to 7,777) |
| Run record | [`kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml`](../../kb/annotation_transfer_runs/at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1/manifest.yaml) |
| Code reference | [https://github.com/AllenInstitute/cell_type_mapper](https://github.com/AllenInstitute/cell_type_mapper) |
| Caveats | Source labels are transcriptomically-defined types; matching to KB classical nodes requires a mapping step based on shared molecular markers. Fear-conditioned cells excluded. GABA-11 co-expresses Adora2a (D2 MSN marker); GABA-14 co-expresses Drd1 (D1 MSN marker). |

**Atlas data sources.** CCN20230722 (WMBv1); taxonomy YAML and SQLite index in `kb/taxonomy/CCN20230722/`. n_cells null — taxonomy DB predates PR #21; rebuild with `just build-taxonomy-db CCN20230722` and re-run `just gen-facts` before next report cycle.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_cea_medium_spiny_neuron_to_cs20230722_clus_1344 | LITERATURE; ATLAS_METADATA; ANNOTATION_TRANSFER; ANNOTATION_TRANSFER | PARTIAL; PARTIAL; PARTIAL; AGAINST | [1]; atlas-internal; —; — |

*Generated by evidencell `1e06776` at 2026-06-09T10:54:03+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats

**Primary mapping:** Central amygdala medium spiny neuron → CS20230722_CLUS_1344 (CEA-BST Six3 Cyp26b1 Gaba_5) at LOW confidence. Key support: ANNOTATION_TRANSFER PARTIAL — GABA-11-Adora2a-Id4 maps to CLUS_1344 with F1=0.677 (purity=0.933) in at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1; CEA-BST lineage CONSISTENT with CeA developmental origin. Key caveats: DISTRIBUTED_ACROSS_CLUSTERS — Drd1+ MSN subset (GABA-14) maps to STR D1 lineage (AGAINST); Ppp1r1b expression in CLUS_1344 NOT_ASSESSED (NO_DISCRIMINATING_MARKER); morphology not assessable from transcriptomic atlas.

The Cell Ontology has no specific term for CeA-restricted medium spiny neurons; medium spiny neuron [CL:1001474](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:1001474) is the closest ancestor (BROAD mapping). Auto-proposed mapping requires expert review.

### Proposed experiments and follow-ups

The Hochgerner 2023 AT run (at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1) has already been performed and provides PARTIAL evidence. The remaining experiments address what the completed AT run did not resolve: (a) Ppp1r1b marker confirmation, and (b) the D1/D2-lineage heterogeneity of the morphological MSN class.

**1. Ppp1r1b expression query for CLUS_1344 (immediate; no new experiments)**
- **What:** Query CCN20230722 precomputed expression (HDF5 stats) for Ppp1r1b in CLUS_1344 once stats are available.
- **Target:** Expression above MIN_DETECTABLE (> 0.5) would confirm the classical DARPP-32 marker.
- **Expected output:** ATLAS_QUERY evidence item added to edge_cea_medium_spiny_neuron_to_cs20230722_clus_1344.
- **Resolves:** NO_DISCRIMINATING_MARKER caveat; would upgrade to MODERATE confidence if Ppp1r1b is confirmed.

**2. ISH for Ppp1r1b and Six3 co-expression in mouse CeA**
- **What:** Fluorescent ISH for Ppp1r1b and Six3 (lineage marker of CLUS_1344) in mouse lateral CeA.
- **Target:** Confirm Ppp1r1b+/Six3+ co-expressing cell population in lateral CeA.
- **Expected output:** LiteratureEvidence linking DARPP-32 morphological marker to CEA-BST Six3 transcriptomic lineage.
- **Resolves:** Q1 (Ppp1r1b/CLUS_1344 link); NO_DISCRIMINATING_MARKER caveat.

**3. Patch-seq of morphologically confirmed CeA MSNs**
- **What:** Profile morphologically identified CeA MSNs (biocytin fill confirming ovoid soma + spiny dendrites) with single-cell transcriptomics; map to WMBv1 via MapMyCells.
- **Target:** F1 ≥ 0.60 at cluster level for CLUS_1344; determine whether Adora2a+ and Drd1+ subtypes share the medium spiny morphology.
- **Expected output:** AnnotationTransferEvidence on this edge; possible new edges for Drd1+ MSN subtype.
- **Resolves:** Q2 (morphological heterogeneity of MSN class); DISTRIBUTED_ACROSS_CLUSTERS caveat; TAXONOMY_LEVEL_MISMATCH (confirms CeA-specific sampling).

### Open questions

1. Does CLUS_1344 express Ppp1r1b/DARPP-32? Confirming this marker would elevate confidence from LOW to MODERATE and directly link the classical morphological marker to the AT-supported transcriptomic cluster. *(On: edge_cea_medium_spiny_neuron_to_cs20230722_clus_1344.)*

2. Are the Adora2a+Id4 (CEA-BST Six3, → CLUS_1344) and Drd1+ (STR D1 lineage, → SUPT_0269/0271) MSN subsets morphologically distinct, or do both exhibit the classical medium spiny profile? The AT evidence reveals two transcriptomically distinct populations within the morphological MSN class — their morphological relationship is unresolved. *(On: edge_cea_medium_spiny_neuron_to_cs20230722_clus_1344.)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Nikolenko et al. 2020 | [PMID:32751957](https://pubmed.ncbi.nlm.nih.gov/32751957/) | Soma location; morphological definition of CeA MSN |
| [2] | Ignacio et al. 2014 | [PMID:25309888](https://pubmed.ncbi.nlm.nih.gov/25309888/) | Neurotransmitter type (GABAergic, CeA majority) |
| [3] | Gilpin et al. 2014 | [PMID:25433901](https://pubmed.ncbi.nlm.nih.gov/25433901/) | Neurotransmitter type (CeA primarily GABAergic) |
| [4] | Hochgerner et al. 2023 | [PMID:37884748](https://pubmed.ncbi.nlm.nih.gov/37884748/) | Ppp1r1b marker (lateral CeA correlation); AT source dataset |

---

<!-- verdict-block-start: edge_cea_medium_spiny_neuron_to_cs20230722_clus_1344 -->
```yaml
verdict:
  confidence: LOW
  confidence_score: 0.25
  rationale: >
    skos:broadMatch to CS20230722_CLUS_1344 "CEA-BST Six3 Cyp26b1 Gaba_5":
    ANNOTATION_TRANSFER PARTIAL from GABA-11-Adora2a-Id4 in
    at_run_20260609_hochgerner2023_amygdala_mmc_wmbv1 (best_f1_score 0.677 at
    cluster level, purity=0.933, 42/45 CLUS_1344 cells from GABA-11). CEA-BST
    Six3 lineage is CONSISTENT with CeA developmental origin; NT type (GABA)
    CONSISTENT; soma location CONSISTENT (CeA-isolated source cells). However,
    recall=0.532 — only 53% of GABA-11 cells reach CLUS_1344, remainder split
    to STR D2 (SUPT_0274). Secondary source GABA-14-Drd1-Scn4b (n=29 cells)
    maps to STR D1 Gaba subclass (best_f1_score 0.710), confirming 1:n
    heterogeneity: the classical medium spiny morphotype encompasses at least
    two transcriptomically distinct populations. Ppp1r1b (DARPP-32) expression
    in CLUS_1344 is NOT_ASSESSED (no precomputed stats available). LOW
    confidence: PARTIAL AT support with confirmed 1:n heterogeneity and
    unverified defining marker.
  reconciliation_note: >
    Re-mapped from CLUS_0723 (Lamp5 Gaba_4) after hypothesis-mode map-cell-type
    analysis. CLUS_0723 had no AT support and was an arbitrary region-filter
    selection; CLUS_1344 is supported by AT evidence (GABA-11 purity=0.933) and
    correct CEA-BST lineage. Drd1+ MSN subset (GABA-14) maps to STR D1 lineage,
    distinct from CLUS_1344 — 1:n heterogeneity confirmed; broadMatch predicate
    reflects this.
  unresolved_questions:
    - Does CLUS_1344 express Ppp1r1b/DARPP-32? Confirming this marker would elevate confidence.
    - Are the Adora2a+Id4 (CEA-BST Six3) and Drd1+ (STR D1) MSN subsets distinct functional populations, or morphologically indistinguishable medium spiny neurons?
```
<!-- verdict-block-end -->
