# Paralaminar/Ventral Amygdala Immature Excitatory Neuron — CCN20230722 Mapping Report

## Introduction

The paralaminar/ventral amygdala immature excitatory neuron is a prolonged-immaturity neuronal
population documented in the adult human and non-human primate amygdala and adjacent medial
temporal lobe cortices. Its defining biological feature — and the primary obstacle to atlas
mapping — is that it has no established mouse homolog. Cross-species single-nucleus RNA
sequencing across human, macaque, rat, and mouse amygdala (Yu et al. 2023 · PMID:36788214)
identifies a neuronal cluster with high expression of immature markers (SOX11, BCL2) exclusively
in humans and macaques; this cluster is explicitly absent from mouse datasets. As a consequence,
no cluster in the Allen Mouse Brain Cell Atlas (CCN20230722 / WMBv1), which was derived entirely
from adult mouse tissue, can constitute a true biological equivalent. The mapping edge recorded
here documents the closest surviving candidate by regional and neurotransmitter filter only; it
carries no claim of biological homology.

---

## Classical Node

| Field | Value |
|---|---|
| **Node ID** | `paralaminar_immature_neuron` |
| **Name** | Paralaminar/ventral amygdala immature excitatory neuron |
| **Definition basis** | CLASSICAL |
| **CL mapping** | CL:4042028 (BROAD; auto-proposed, requires expert review) |
| **Neurotransmitter** | Glutamatergic (inferred from CL:4042028 context; no explicit NT block) |
| **Soma location** | Paralaminar nucleus (UBERON:0002887); extends to ventral amygdala, anterior entorhinal cortex, and perirhinal cortex layer II \[1\]\[2\]\[3\] |
| **Defining markers** | DCX, BCL2, NCAM1, RBFOX3, TUBB3, VIM, NES, MKI67, SP8, NR2F2, PROX1 \[1\]\[2\] |
| **Negative markers** | NKX2-1 \[1\] |
| **Notes** | Spans a continuum from progenitor-like (Ki-67+ VIM+ NES+) to postmitotic immature neurons (DCX+ BCL2+ NeuN+); also includes a clustered BCL2+ population in piriform cortex |

**References**

- \[1\] Sorrells et al. 2019 · PMID:31227709
- \[2\] Chareyron et al. 2021 · PMID:34206571
- \[3\] Villard et al. 2023 · PMID:37337377

---

## Mapping Results

**Edge:** `edge_paralaminar_immature_neuron_to_cs20230722_supt_0005`
**Relationship type:** `evidencell:UncertainRelationship`
**Atlas candidate:** CS20230722_SUPT_0005 — "0005 IT EP-CLA Glut_3" (n = 798 cells)

This candidate was retrieved as the closest atlas type by regional proximity (BLA-adjacent;
region_fraction 0.042 in MBA:295) and inferred glutamatergic neurotransmitter type. It is
ranked 1 of 5 in the regional survival cohort but shares a discovery score of 1 with all
cohort members, indicating no candidate distinguishes itself as a strong match.

### Property comparisons

| Property | Classical node (A) | Atlas candidate B — CS20230722_SUPT_0005 | Alignment |
|---|---|---|---|
| **NT type** | Glutamatergic (inferred from CL:4042028) | Glut (inferred from "IT EP-CLA Glut" parent label) | APPROXIMATE — both inferred from context, neither explicitly recorded |
| **Soma location** | Paralaminar nucleus (UBERON:0002887); primate-specific zone adjacent to amygdala | Cortical subplate MBA:703 dominant (~55%); minor BLA-adjacent signal (MBA:295 region_fraction 0.042) | **DISCORDANT** — paralaminar nucleus has no direct CCF equivalent; atlas type is distributed across EP/CLA/cortical subplate territory |
| **DCX expression** | Defining marker (protein; neuroblast immaturity marker) \[1\]\[2\] | Not present in atlas metadata; absent from adult mouse transcriptomic types by definition | **DISCORDANT** — DCX marks migrating/immature neurons and is not expressed in adult mouse IT neurons |
| **BCL2 expression** | Defining marker (anti-apoptotic; marks paralaminar immature state) \[1\]\[2\] | Not present in atlas metadata | NOT ASSESSED |

### Evidence items

- **ATLAS_METADATA (AGAINST):** Cross-species snRNA-seq (Yu et al. 2023 · PMID:36788214)
  identifies paralaminar neurons as a primate-enriched cluster with high SOX11 and BCL2
  expression, explicitly absent from mouse datasets. This evidence actively argues against
  biological equivalence to any adult mouse atlas type.

### Caveats

1. **SPECIES_BARRIER:** Paralaminar immature neuron is a primate-enriched type with no
   established mouse homolog. WMBv1 is derived from adult mouse. This mapping has no
   biological support; it records only the closest type by regional/NT filter in the absence
   of a true homolog.
2. **MARKER_INCOMPATIBILITY:** Classical defining markers (DCX, VIM, NES, MKI67, BCL2) are
   immaturity/progenitor-state markers absent from adult mouse transcriptomic atlases. No
   precomputed expression comparison is possible.

---

## Verdict

| Field | Value |
|---|---|
| **Relationship** | evidencell:UncertainRelationship |
| **Confidence** | UNCERTAIN |
| **Confidence score** | 0.07 |
| **Atlas candidate** | CS20230722_SUPT_0005 (IT EP-CLA Glut_3) |

**Rationale:** Confidence is set to UNCERTAIN (score 0.07) for three compounding reasons.
First, cross-species snRNA-seq (Yu et al. 2023 · PMID:36788214) explicitly identifies the
paralaminar population as absent from mouse datasets, removing any principled basis for
mapping to WMBv1. Second, the location comparison is DISCORDANT: the paralaminar nucleus is
a primate-specific anatomical structure with no CCF equivalent, while the surviving atlas
candidate (CS20230722_SUPT_0005) is primarily distributed in cortical subplate and endopiriform
territory. Third, the key defining markers (DCX, VIM, NES, MKI67) are markers of neuronal
immaturity that are, by definition, absent from mature adult mouse atlas types, making direct
molecular comparison impossible. The surviving edge is retained as a placeholder to document
the best available regional/NT approximation; it should not be interpreted as biological
equivalence.

---

## Discussion

### Biological context

The paralaminar nucleus hosts a population of neurons that remain in an immature transcriptomic
and morphological state well into human adulthood, and possibly throughout life. Sorrells et al.
(2019; PMID:31227709) showed that in high-proliferative paralaminar regions, Ki-67+ cells
co-express SP8 and COUP-TFII (NR2F2) — transcription factors characteristic of caudal ganglionic
eminence (CGE) progenitors — while displaying a dense field of VIM+ NES+ progenitor-like and
DCX+ PSA-NCAM+ neuroblast-like cells, with few NKX2-1+ medial ganglionic eminence-derived cells.
This positions the paralaminar nucleus as a CGE-affiliated delayed-maturation zone.

Chareyron et al. (2021; PMID:34206571) extended this picture to non-human primates, demonstrating
that the BCL2+ NeuN+ immature neuron population is not confined to the paralaminar nucleus but
forms a continuous stream from the lateral ventricle SVZ through the paralaminar nucleus and into
the anterior entorhinal and perirhinal cortices. Villard et al. (2023; PMID:37337377) further
confirmed BCL2+ immature neuron populations in the ventromedial amygdala and temporal cortex of
adult primates across multiple studies.

Critically, Yu et al. (2023; PMID:36788214) profiled amygdala cell types in human, macaque, rat,
and mouse using single-nucleus transcriptomics and found that the SOX11+ BCL2+ immature neuron
cluster is present in primates only. Mouse amygdala contains no equivalent transcriptomic state.
This cross-species negative finding is the principal evidence driving the UNCERTAIN mapping and
the SPECIES_BARRIER caveat.

### Key unresolved questions

1. Does any cross-species scRNA-seq dataset contain a mouse cluster partially matching the
   DCX+/BCL2+/PROX1+ paralaminar population, even transiently during development?
2. Would targeted re-analysis of WMBv1 restricted to the endopiriform nucleus (MBA:942) reveal
   a closer candidate than the cortical subplate-dominant CS20230722_SUPT_0005?

### Recommended experiment

**Map published human paralaminar snRNA-seq data to WMBv1 using MapMyCells.** Data from Sorrells
et al. (2019; PMID:31227709) or Caglayan et al. (2023) provide snRNA-seq profiles from the human
paralaminar nucleus. Projecting these onto WMBv1 via MapMyCells would reveal whether any mouse
atlas cluster captures even a partial transcriptomic signature — or whether the query cells fall
uniformly into a low-confidence catch-all state, formally confirming the absence of a mouse
homolog. A complementary experiment — IHC for DCX, BCL2, and NES in adult mouse amygdala —
would formally confirm at the protein level the absence of a paralaminar-equivalent population
in rodent.
