# Amygdala Intercalated Cell — CCN20230722 Mapping Report

## Introduction

The amygdala intercalated cell (ITC) is a GABAergic neuron residing in the intercalated cell masses (ICMs) — small, densely packed clusters positioned at the interface between the basolateral amygdala (BLA) and the central amygdala (CeA). A single mapping edge was evaluated against the CCN20230722 whole-brain transcriptomic atlas, testing the hypothesis that this classically-defined cell type corresponds to supertype CS20230722_SUPT_0235 (0235 STR Prox1 Lhx6 Gaba_3) on the basis of shared GABAergic identity and a shared subpallial (MGE) developmental lineage.

---

## Classical Node Properties

| Property | Value | Source(s) |
|---|---|---|
| Node ID | `amygdala_intercalated_cell` | — |
| Definition basis | CLASSICAL | — |
| Neurotransmitter | GABAergic | Veinante et al. 2013 [3]; Pitkānen & Amaral 1994 [4] |
| Soma location | UBERON:0002884 — amygdala intercalated nuclei (BLA–CeA interface) | Ignacio et al. 2014 [1]; Nardelli et al. 2024 [2]; Veinante et al. 2013 [3] |
| Morphology | Small clusters of densely packed neurons (intercalated cell masses) | Veinante et al. 2013 [3] |
| Defining markers (formal) | None encoded | — |
| Neuropeptides | None encoded | — |
| CL mapping | None assigned | — |
| Subtypes | None detailed in this report | — |

**Note on markers.** ITC-associated markers (TSHZ1, FOXP2, DRD1, TACR3, NTS) are present in the literature and referenced in mapping evidence snippets but were not formally extracted as `defining_markers` on this classical node. This is a known gap that limits marker-level comparison with atlas clusters (see Unresolved Questions below).

---

## Mapping Results

### Edge: `amygdala_intercalated_cell` → CS20230722_SUPT_0235

**Atlas supertype:** 0235 STR Prox1 Lhx6 Gaba_3 (`CS20230722_SUPT_0235`)  
**Relationship:** `skos:broadMatch`  
**Supertype cell count:** 146 cells  
**ITC region fraction:** 0.022 (MERFISH Zhuang 2023, MBA:1105; ~2% of supertype)  
**Overall confidence:** LOW

#### Property Comparisons

| Property | Classical node value | Atlas supertype value | Alignment |
|---|---|---|---|
| Neurotransmitter type | GABAergic | GABAergic (subclass STR Prox1 Lhx6 Gaba; high Gad1/Gad2 in cluster precomputed data) | CONSISTENT |
| Soma location | UBERON:0002884 — intercalated amygdalar nuclei (BLA–CeA interface) | MBA:1105 Intercalated amygdalar nucleus: 6 cells (region fraction 0.024, Zhuang 2023); 3 cells (region fraction 0.27, Yao 2024). Dominant regions: Striatum (MBA:477), Cortical subplate (MBA:703); BLA-anterior (MBA:303) also present | APPROXIMATE |
| Marker profile (TSHZ1 / FOXP2) | Referenced in literature as ITC markers; not formally encoded as defining_markers | Atlas defining markers are Gna14, Car4, Daam2 — not known ITC markers | NOT ASSESSED |

**ATLAS_METADATA evidence (PMID:37915112):** MERFISH data (Zhuang 2023) places a minor SUPT_0235 contingent at MBA:1105 (6 cells, region fraction 0.024) and BLA-adjacent MBA:303 (65 cells). ITC location is confirmed within the supertype, but is quantitatively minor; the supertype is predominantly distributed across striatum and cortical subplate.

> "In some regions, such as the intercalated nuclei, virtually all of the resident neurons appeared to be GABAergic"
> <!-- quote_key: 14068807_9efc175b -->
> — Pitkānen & Amaral 1994 (PMID:8158266)

**LITERATURE evidence (PMID:38567489) [5]:** ITC cells share a Prox1+/Lhx6+ developmental lineage reflecting a subpallial MGE origin, consistent with the STR Prox1 Lhx6 Gaba subclass lineage of SUPT_0235. This provides biological plausibility for the `broadMatch` relationship, despite the supertype not being ITC-selective.

#### Caveats

1. **Broad atlas supertype.** SUPT_0235 (STR Prox1 Lhx6 Gaba_3) has its majority of cells in Striatum and Cortical subplate; the intercalated amygdalar nucleus (MBA:1105) accounts for only ~2% of the supertype. The supertype is not ITC-selective and spans a wide range of subpallial GABAergic cell populations.

2. **Missing classical markers.** No `defining_markers` are encoded on the `amygdala_intercalated_cell` classical node. ITC-specific markers (TSHZ1, FOXP2, DRD1, TACR3, NTS) are present in the literature and referenced in mapping evidence but were not formally extracted. Without a defined marker profile, a marker-level comparison against atlas clusters is not possible.

#### Unresolved Questions

- Is there a more ITC-specific cluster within subclass SUBC_054 (STR Prox1 Lhx6 Gaba) that is concentrated at MBA:1105?
- Do TSHZ1/FOXP2 selectively mark a cluster within SUBC_054, or a different subclass (e.g. CEA-AAA-BST)?
- Should CEA-AAA-BST Six3 Sp9 Gaba candidates (SUPT_0379, SUPT_0377) be evaluated as alternative or parallel ITC hypotheses?

---

## Verdict

**Confidence:** LOW  
**Confidence score:** 0.15  
**Relationship:** `skos:broadMatch`

**Rationale.** The single mapping edge to CS20230722_SUPT_0235 satisfies only weak criteria. Neurotransmitter type (GABAergic) is consistent across both nodes [3][4], and a shared subpallial Prox1+/Lhx6+ MGE lineage provides developmental plausibility (PMID:38567489 [5]). However, the atlas supertype is broadly distributed across striatum and cortical subplate, with ITC cells (MBA:1105) comprising only approximately 2% of the supertype cell count (region fraction 0.022, MERFISH Zhuang 2023, PMID:37915112). Critically, the classical node carries no formal `defining_markers`, precluding any marker-level evidence for or against the match. Atlas defining markers (Gna14, Car4, Daam2) are not known ITC markers. The combination of a non-ITC-selective supertype distribution and absent marker evidence is insufficient to support a confidence level above LOW. A `broadMatch` to the STR Prox1 Lhx6 Gaba subclass lineage is biologically reasonable but does not resolve the ITC at sub-supertype resolution.

---

## Discussion

The intercalated cell masses are morphologically well-defined — small, densely packed clusters of GABAergic neurons at the BLA–CeA interface:

> ". In addition to the four groups, a few nuclei of the amygdala remain unclassified, among them the intercalated cell masses which are small clusters of densely packed GABAergic neurons (Palomares-Castillo et al., 2012)."
> <!-- quote_key: 15449738_a21bd562 -->
> — Veinante et al. 2013 (PMID:25408902)

Their anatomical position is consistently described as distinct from the canonical amygdala subdivisions:

> "At the cellular level, the amygdala is composed of a group of 13 sub-nuclei located in the medial temporal lobe [...] (4) other (which includes anterior amygdala area, the amygdalo-hippocampal area, and the intercalated nuclei)"
> <!-- quote_key: 1229611_e14a19cf -->
> — Ignacio et al. 2014 (PMID:25309888)

> ". Anatomically the amygdala is composed of three major nuclear groups [...] To this canonical classification, other amygdaloid nuclei must be added, such as the anterior amygdaloid area, the amygdalohippocampal area, and the intercalated cells."
> <!-- quote_key: 270614391_b0af02da -->
> — Nardelli et al. 2024 (PMID:39130512)

Despite this clear classical identity, the present mapping is limited by the absence of a formal marker panel on the classical node. The ITC literature describes distinctive molecular markers — most prominently TSHZ1 and FOXP2, as well as DRD1, TACR3, and NTS — that would permit targeted cluster-level interrogation of the atlas. These were observed in evidence snippets during mapping but not formally extracted into the KB.

The CCN20230722 atlas contains the STR Prox1 Lhx6 Gaba subclass (SUBC_054), which includes SUPT_0235 and several other supertypes with documented presence at MBA:1105. An ITC-specific cluster likely exists within this subclass or, alternatively, within the CEA-AAA-BST Six3 Sp9 Gaba subclass. Resolving the mapping requires: (1) formally encoding ITC marker genes on the classical node, and (2) re-running the `map-cell-type` workflow at cluster level within SUBC_054.

**Proposed experiments:**

1. Extract ITC marker genes (TSHZ1, FOXP2, DRD1, TACR3, NTS) from primary literature, add as `defining_markers` on the `amygdala_intercalated_cell` classical node, then re-run `map-cell-type` to test whether a specific cluster in SUBC_054 selectively expresses this profile.
2. Assess CEA-AAA-BST Six3 Sp9 Gaba candidates (SUPT_0379, SUPT_0377) as parallel ITC mapping hypotheses.

---

## References

| Label | Citation | PMID |
|---|---|---|
| [1] | Ignacio et al. 2014 — "Effects of Acute Prenatal Exposure to Ethanol on microRNA Expression are Ameliorated by Social Enrichment" | PMID:25309888 |
| [2] | Nardelli et al. 2024 — "Pain in Parkinson's disease: a neuroanatomy-based approach" | PMID:39130512 |
| [3] | Veinante et al. 2013 — "The amygdala between sensation and affect: a role in pain" | PMID:25408902 |
| [4] | Pitkānen & Amaral 1994 — "The distribution of GABAergic cells, fibers, and terminals in the monkey amygdaloid complex" | PMID:8158266 |
| [5] | PMID:38567489 — ITC Prox1+/Lhx6+ lineage (subpallial MGE origin) | PMID:38567489 |
| [atlas] | Zhuang 2023 — MERFISH whole-brain atlas (CCN20230722) | PMID:37915112 |
