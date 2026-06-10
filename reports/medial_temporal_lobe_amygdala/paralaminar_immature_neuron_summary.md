# Paralaminar/ventral amygdala immature excitatory neuron — CCN20230722 Mapping Report
*2026-06-10 · Source: `kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml`*

---

## Introduction

The paralaminar/ventral amygdala immature excitatory neuron is a distinctive population of cells residing in the paralaminar nucleus [UBERON:0002887] and adjacent ventral amygdala of adult humans and non-human primates. These cells are characterised by an arrested or protracted developmental state, occupying a continuum from Ki-67⁺ vimentin⁺ nestin⁺ cycling progenitors to DCX⁺ Bcl-2⁺ NeuN⁺ postmitotic immature neurons. Their persistence into adulthood — in a zone contiguous with the medial temporal lobe germinal subventricular zone — raises fundamental questions about delayed neurogenesis in the primate brain and points to a biological niche with no established rodent counterpart. Mapping this classical type to the Allen CCN20230722 whole-mouse-brain atlas (WMBv1) is important for clarifying the taxonomic scope of the paralaminar population and for evaluating whether any functional or transcriptomic homolog exists in the mouse that could serve as an experimental model.

### Classical type properties

| Property | Value | References |
|---|---|---|
| Soma location | Paralaminar nucleus [UBERON:0002887]; ventral amygdala, anterior entorhinal cortex, perirhinal cortex layer II | [1], [2], [3] |
| NT type | Glutamatergic (inferred; no explicit NT block recorded) | — |
| Defining markers | Dcx, Bcl2, Ncam1, Rbfox3, Tubb3, Vim, Nes, Mki67, Sp8, Nr2f2, Prox1 | [1], [2] |
| Negative markers | Nkx2-1 | [1] |
| Neuropeptides | None documented | — |

<details>
<summary>Details — source evidence for classical type properties</summary>

- **Soma location (paralaminar nucleus / CGE-adjacent zone):** immunohistochemistry for Ki-67, SP8, COUP-TFII (Nr2f2), and PROX1 in human temporal lobe · Sorrells et al. 2019 · [1]

  > The PL develops next to the CGE which is highly proliferative in humans (Hansen et al., 2013) . To determine whether the PL forms from progenitors in the CGE we immunostained the human temporal lobe for Ki-67 to label dividing cells, and for transcription factors expressed in the CGE (SP8, COUP-TFII, and PROX1) (Ma et al., 2013)(Hansen et al., 2013)(Miyoshi et al., 2015)(Rubin et al., 2013)
  > — Sorrells et al. 2019, Non-neuronal and immature neuron populations · [1] <!-- quote_key: 195246702_dd079f9e -->

- **Soma location (ventral amygdala / SVZ continuum / perirhinal cortex):** immunohistochemistry for DCX and Bcl-2 in post-mortem human and non-human primate tissue · Chareyron et al. 2021 · [2]

  > Our current findings demonstrate that the population of immature neurons found in the ventral amygdala is not an isolated population but may be part of a larger group of Bcl-2-positive and NeuN-positive cells that extends from the SVZ of the lateral ventricle to the paralaminar nucleus and some cortical areas within the medial temporal lobe. The presence of these immature neurons in the ventral amygdala, anterior entorhinal cortex and layer II of the perirhinal cortex can be observed on coronal or sagittal sections of the temporal lobe labeled with DCX or Bcl-2 markers (Bernier et al., 2002)(Fudge, 2004)(0).
  > — Chareyron et al. 2021, Non-neuronal and immature neuron populations · [2] <!-- quote_key: 235715856_1045f5c1 -->

- **Soma location (ventromedial amygdala and temporal cortex in adult primates):** immunohistochemistry for Bcl-2 · Villard et al. 2023 · [3]

  > populations of immature neurons expressing the anti-apoptosis Bcl2 protein have been observed in several regions of the adult mammalian brain, including the ventromedial amygdala and the temporal cortex in humans and non-human primates (Bernier et al., 2002)(Bernier et al., 1998)(Fudge, 2004)(Yachnis et al., 2000)
  > — Villard et al. 2023, Non-neuronal and immature neuron populations · [3] <!-- quote_key: 259201574_70036ef8 -->

- **Defining markers (Ki-67, Sp8, Nr2f2/COUP-TFII, Vim, Nes, Dcx, Ncam1) and negative marker (Nkx2-1):** immunohistochemistry in human temporal lobe · Sorrells et al. 2019 · [1]

  > Regions with high Ki-67 + cell density contained many SP8 + COUP-TFII + cells, few NKX2.1 + cells that would be likely be medial ganglionic eminence-derived, and a dense field of vimentin + nestin + cells and DCX + PSA-NCAM + cells (Fig. 1f, g)
  > — Sorrells et al. 2019, Non-neuronal and immature neuron populations · [1] <!-- quote_key: 195246702_302eefd5 -->

</details>

### Cell Ontology mapping

Cell Ontology mapping: immature neuron [[CL:4042028](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042028)] (BROAD).

The Cell Ontology has no specific term for the primate paralaminar population; immature neuron [CL:4042028] is the closest ancestor. This mapping is auto-proposed by asta-report-ingest and requires expert review. This type is a strong candidate for a new CL term request capturing the primate-specific CGE-derived adult paralaminar immature neuron (see Discussion).

---

## Results

One candidate atlas supertype was assessed; **no atlas cluster in WMBv1 (CCN20230722) constitutes a biologically supported mapping for this classical type.** The single edge is UNCERTAIN, driven by a fundamental species barrier: paralaminar immature neurons are a primate-enriched population whose defining markers (Dcx, Vim, Nes, Mki67, Bcl2) are immaturity and progenitor-state proteins absent from adult mouse transcriptomic atlases by definition.

**Primary null finding.** Cross-species snRNA-seq evidence identifies the paralaminar population as a primate-enriched cluster (high SOX11 and BCL2 expression) explicitly absent from mouse datasets. WMBv1 is derived entirely from adult mouse brain. The single retrieved candidate — CS20230722_SUPT_0005 (0005 IT EP-CLA Glut_3) — represents only the closest survivor in a regional/NT filter scan; it does not constitute biological equivalence.

*(No annotation-transfer runs are present for this node — figure generation skipped.)*

### Mapping candidates overview

| Rank | WMBv1 supertype | Cells (10x) | Confidence | Key property alignment | Verdict |
|---:|---|---:|---|---|---|
| — | 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] | 798 | ⚪ UNCERTAIN | Location DISCORDANT · Dcx DISCORDANT | Eliminated (species barrier) |

*1 edge assessed. Relationship type: evidencell:UncertainRelationship.*

---

## Eliminated candidates

All edges are UNCERTAIN. The shared primary disqualifying signal is the **SPECIES_BARRIER**: paralaminar immature neurons are a primate-enriched type with no established mouse homolog, and their complete defining marker panel is categorically absent from adult mouse transcriptomic atlases.

### 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] · ⚪ UNCERTAIN

**Atlas supertype:** 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005]; 798 cells (10x scRNA-seq).

**Disqualifying evidence:**

- **Species barrier (primary disqualification).** Atlas metadata evidence (cross-species snRNA-seq, atlas-internal) identifies paralaminar neurons as a primate-enriched cluster characterised by high SOX11 and BCL2 expression, explicitly absent from mouse datasets. This evidence argues directly against biological equivalence to any adult mouse atlas type. The ATLAS_METADATA item supports = AGAINST.

- **Dcx: DISCORDANT.** Dcx is the canonical marker of migrating/immature neurons in all vertebrates and is not expressed in mature adult neurons. It is definitionally absent from any adult mouse transcriptomic type; the atlas metadata confirms no Dcx signal. This is not a graded discordance but a categorical incompatibility arising from the maturation state difference.

- **Soma location: DISCORDANT.** The paralaminar nucleus [UBERON:0002887] is a primate-specific anatomical zone adjacent to the basolateral amygdala, without a direct CCF mouse equivalent. CS20230722_SUPT_0005 is distributed primarily in cortical subplate (MBA:703; ~55%), with only minor BLA-adjacent presence (MBA:295; region_fraction = 0.042). *(note: the cortical subplate/endopiriform/claustrum territory occupied by this atlas supertype is anatomically distant from a primate paralaminar zone in both evolutionary and functional terms — the IT EP-CLA Glut population is an adult corticothalamic/claustral type, not a developmental transitional type.)*

- **NT type: APPROXIMATE only.** Both classical-side and atlas-side NT annotations are inferred from context (CL mapping lineage and parent subclass label, respectively) rather than from recorded NT data. This provides weak supporting signal at best, not corroboration.

- **Bcl2: NOT_ASSESSED.** Bcl2 is a core defining marker of the paralaminar immature state. Atlas metadata for CS20230722_SUPT_0005 carries no Bcl2 expression information; direct molecular comparison is not possible.

- **Marker incompatibility (systemic).** All 11 classical defining markers (Dcx, Vim, Nes, Mki67, Bcl2, Sp8, Nr2f2, Prox1, Ncam1, Rbfox3, Tubb3) are immaturity or progenitor-state markers. Precomputed expression comparison with any adult mouse atlas cluster is structurally impossible. This is a categorical biological boundary, not a data gap.

**Counter-evidence strength:** Strong. Disqualification rests on cross-species transcriptomic data confirming primate-specificity, compounded by discordant location and marker incompatibility across all defining properties.

*(Child-cluster breakdown not assessed — see proposed experiments.)*

---

### Methods

<details>
<summary>Data sources, analyses, and reproducibility receipts</summary>

**Classical type definition.** The paralaminar/ventral amygdala immature excitatory neuron is defined on a CLASSICAL basis, grounded in immunohistochemical characterisation of human and non-human primate post-mortem tissue. Defining markers include Dcx, Bcl2, Ncam1, Rbfox3, Tubb3, Vim, Nes, Mki67, Sp8, Nr2f2, and Prox1 [1], [2]. The negative marker Nkx2-1 excludes medial ganglionic eminence (MGE) origin, consistent with CGE derivation [1]. Soma location is the paralaminar nucleus [UBERON:0002887], extending through the ventral amygdala, anterior entorhinal cortex, and perirhinal cortex layer II [1], [2], [3]. The population spans a continuum from progenitor-like (Ki-67⁺ vimentin⁺ nestin⁺) to postmitotic immature neurons (DCX⁺ Bcl-2⁺ NeuN⁺) and includes a clustered Bcl-2⁺ population in piriform cortex.

**Atlas mapping query.** Candidate atlas clusters were retrieved from the CCN20230722 taxonomy at ranks 0 (cluster) and 1 (supertype) using metadata-based scoring (region match, NT type, defining markers, sex bias when applicable). Full scoring rules: `workflows/map-cell-type.md`. The survival cohort was restricted to region MBA:295 (5 members); CS20230722_SUPT_0005 ranked 1 of 5 with discovery score = 1, equal to next-best score = 1, indicating no candidate distinguishes itself as a strong match.

**Property alignment.** Each defining property of the classical type was compared to the corresponding atlas-side value via the `property_comparisons` schema, with alignments graded CONSISTENT / APPROXIMATE / DISCORDANT / NOT_ASSESSED. Atlas-side values were drawn from atlas metadata. No precomputed expression comparison was possible for any defining marker because all are immaturity/progenitor-state proteins categorically absent from adult mouse transcriptomic profiles.

**Anti-hallucination.** All citations, atlas accessions, ontology CURIEs, and verbatim literature quotes in this report are validated against the evidencell knowledge base at write time. Authored-prose evidence narratives are validated against their source `evidence_items[*].explanation` fields. The pre-write hook rejects any unresolvable identifier or unattributed blockquote. Specific mapping limitations and caveats are documented per-candidate in the Discussion section.

**Evidence base table**

| Edge ID | Evidence types | Supports | Source |
|---|---|---|---|
| edge_paralaminar_immature_neuron_to_cs20230722_supt_0005 | ATLAS_METADATA | AGAINST | — |

*Generated by evidencell `f1aa396` at 2026-06-10T14:09:31+00:00 from [kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml](../../kb/graphs/medial_temporal_lobe_amygdala/20260528_medial_temporal_lobe_amygdala_report_ingest.yaml).*

</details>

---

## Discussion

### Best candidate + caveats summary

**Primary mapping:** Paralaminar/ventral amygdala immature excitatory neuron → 0005 IT EP-CLA Glut_3 [CS20230722_SUPT_0005] at UNCERTAIN confidence. Key support: none — no biological equivalence is claimed; the edge documents the closest regional/NT survivor only. Key caveats: SPECIES_BARRIER (primate-enriched type absent from mouse datasets); MARKER_INCOMPATIBILITY (all defining markers are immaturity/progenitor-state proteins absent from adult mouse transcriptomics).

The Cell Ontology has no specific term for this population; immature neuron [[CL:4042028](https://www.ebi.ac.uk/ols4/ontologies/cl/classes?obo_id=CL:4042028)] is the closest ancestor. The mapping is auto-proposed and requires expert review. This classical type is a strong candidate for a dedicated new CL term request that would specifically capture the primate paralaminar/ventral amygdala adult immature neuron, distinguishing it from generic developmental immature neurons and from other BCL2⁺ adult populations (see proposed experiments).

### Proposed experiments and follow-ups

**Annotation transfer — cross-species human → mouse atlas**

MapMyCells annotation transfer has not been run for this node (no `annotation_transfer_runs` present in methods_summary). Running cross-species AT would directly address both open questions.

- **What:** Map published human paralaminar nucleus snRNA-seq data (Sorrells et al. 2019, PMID:31227709, or Caglayan et al. 2023) to WMBv1 using MapMyCells in cross-species mode.
- **Target:** Identify any mouse atlas supertype with F1 ≥ 0.40 at rank 1 (lower threshold is appropriate given known species divergence; F1 ≥ 0.40 would indicate partial transcriptomic capture worth investigating).
- **Expected output:** AnnotationTransferEvidence item on edge_paralaminar_immature_neuron_to_cs20230722_supt_0005. If any supertype reaches F1 ≥ 0.40, upgrade edge confidence to LOW with `skos:broadMatch`; if cells fall uniformly into catch-all states, formally confirm absence of a mouse homolog.
- **Resolves:** Q1 and Q2 below.

**IHC in adult mouse amygdala**

- **What:** Immunohistochemistry for DCX, BCL2, and NES in adult mouse amygdala and endopiriform nucleus (MBA:942) sections.
- **Target:** Detect or formally exclude any DCX⁺ population in adult mouse amygdala at protein level.
- **Expected output:** LiteratureEvidence or direct lab data confirming or refuting SPECIES_BARRIER at the protein level.
- **Resolves:** Q1 (whether any mouse cluster partially matches the DCX⁺/BCL2⁺/PROX1⁺ paralaminar profile).

**Targeted endopiriform nucleus atlas query**

- **What:** Re-run the atlas mapping query restricted to MBA:942 (endopiriform nucleus) rather than MBA:295 (BLA), to test whether a closer regional candidate exists in deep piriform layers adjacent to the claustrum.
- **Target:** Any candidate with region_fraction > 0.20 in MBA:942 and composite marker score > 1.
- **Expected output:** New ATLAS_QUERY evidence item; potentially a second UNCERTAIN edge in a more anatomically proximate territory than IT EP-CLA Glut_3.
- **Resolves:** Q2 (whether MBA:942 reveals a closer candidate).

**CL new term request**

- **What:** Draft and submit a new Cell Ontology term request for the primate paralaminar/ventral amygdala adult immature neuron, using `workflows/cl-term-request.md`.
- **Target:** A specific CL term capturing the Sp8⁺/Nr2f2⁺/Prox1⁺ CGE-derived immature neuron persisting in the adult primate amygdala/medial temporal lobe.
- **Expected output:** GitHub issue to the CL tracker; `proposed_cl_term` populated on the KB node.
- **Resolves:** Ontology placement independent of atlas mapping outcome.

### Open questions

1. Does any cross-species scRNA-seq dataset contain a mouse cluster partially matching the DCX⁺/BCL2⁺/PROX1⁺ paralaminar population? *(from edge_paralaminar_immature_neuron_to_cs20230722_supt_0005)*
2. Would targeted re-analysis of WMBv1 in endopiriform nucleus (MBA:942) reveal a closer candidate? *(from edge_paralaminar_immature_neuron_to_cs20230722_supt_0005)*

---

## References

| # | Citation | PMID | Used for |
|---|---|---|---|
| [1] | Sorrells et al. 2019 | [31227709](https://pubmed.ncbi.nlm.nih.gov/31227709/) | Soma location, defining markers, negative markers |
| [2] | Chareyron et al. 2021 | [34206571](https://pubmed.ncbi.nlm.nih.gov/34206571/) | Soma location, defining markers |
| [3] | Villard et al. 2023 | [37337377](https://pubmed.ncbi.nlm.nih.gov/37337377/) | Soma location |

---

<!-- verdict-block-start: edge_paralaminar_immature_neuron_to_cs20230722_supt_0005 -->
```yaml
verdict:
  confidence: UNCERTAIN
  confidence_score: 0.05
  rationale: >
    Paralaminar immature neurons are a primate-enriched type (SPECIES_BARRIER caveat);
    atlas-internal metadata evidence confirms absence from mouse datasets,
    removing any basis for biological equivalence to adult mouse atlas types.
    CS20230722_SUPT_0005 (0005 IT EP-CLA Glut_3, 798 cells) is the sole survivor
    in a 5-member MBA:295 cohort (discovery score 1, rank 1 of 5, next-best score 1)
    but shows marker_DCX DISCORDANT and location_soma DISCORDANT; marker_BCL2
    NOT_ASSESSED. All 11 defining markers are immaturity/progenitor-state proteins
    absent from adult mouse transcriptomics; no precomputed expression comparison
    or annotation-transfer F1 is available. Edge retained as placeholder only.
  reconciliation_note: >
    No pool-candidate indistinguishability applies (pool_candidates empty).
    UNCERTAIN confidence reflects an absolute species barrier, not a graded
    evidence gap. Upgrading would require cross-species MapMyCells AT with
    F1 >= 0.40 at rank 1, or IHC confirming a DCX+ population in adult mouse
    amygdala.
  unresolved_questions:
    - "Does any cross-species scRNA-seq dataset contain a mouse cluster partially matching the DCX+/BCL2+/PROX1+ paralaminar population?"
    - "Would targeted re-analysis of WMBv1 in endopiriform nucleus (MBA:942) reveal a closer candidate?"
```
<!-- verdict-block-end -->
