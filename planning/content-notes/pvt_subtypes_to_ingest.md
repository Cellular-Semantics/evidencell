# PVT subtype candidates — split and deferrals

Date: 2026-11-26 · Branch: `content/thalamus-pvt-subtypes` (PR #253) · Umbrella: `pvt_glutamatergic_neuron`
Source run: `research/thalamus/20261114_thalamus_pvt_report_ingest/` (PVT_Glut.pdf)

**Status.** The session stopped at a gate. The curator then approved the recommendation
("Decisions" below, option b):
- **Created:** `apvt_glutamatergic_neuron` and `ppvt_glutamatergic_neuron`. `apvt_crh_neuron` and
  `apvt_gck_neuron` were re-parented under aPVT.
- **Deferred:** PVT1–4, to a follow-up PR with the Gao 2023 AT.
- **Deferred:** PVT5.
- **Not created:** the Li 2021 projection groups and pPVT→CeA.

This file keeps the deferred and rejected candidates in enough detail to pick up later. The
umbrella node's notes ("DEFERRED SUBTYPE CANDIDATES") carry a shorter version.

## 2026-11-26 Gao AT follow-up (branch `content/thalamus-at-gao2023`): F1 gate pending

**The PVT1–5 rows below (3–7) are wrong on markers and AP position. Do not ingest them as
written.** Their quote_keys (251021326_6e3c6191, _3d4954d5, _19d51130, _6820b736, plus _815dcc71,
_17100715, _ecb498e7 and _5ed06f40) are not in the Gao 2023 eLife version of record. No 8-word
window of any of them matches the Europe PMC full text. They also contradict the paper's
Supplementary file 1c (Thy1, Cxcl14, Cbln2 and Tesc are not PVT DEGs). Details:
`research/thalamus/annotation_transfer/gao2023_pvt/README.md`.

What the paper says (verified quotes 251021326_6ecf0efa, _d84aa264, _644f9bee, _1fef2fe7,
_9034ddfa, _a12d1cda):

| cluster | ISH marker | 2nd ISH marker | position | ThalamoSeq overlap (correlation) | proposed parent |
|---|---|---|---|---|---|
| PVT1 | Esr1 | Drd2 | pPVT, across the dorso-ventral axis | PFC projectors | ppvt_glutamatergic_neuron |
| PVT2 | Col12a1 | Pde3a | ventral "edge" of pPVT | PFC projectors (largest overlap); PL retrobeads at the ventral edge partly co-localise with Col12a1 | ppvt_glutamatergic_neuron |
| PVT3 | Npffr1 | Insrr | aPVT-biased, antero-lateral | prefrontal (small) | apvt_glutamatergic_neuron |
| PVT4 | Hcrtr1 | Npsr1 | aPVT-biased, antero-medial | auditory and visual (small) | apvt_glutamatergic_neuron |
| PVT5 | Drd3 | — | pan-PVT | visual (small) | umbrella (if created) |

AT results, from derived labels (marker-set assignment; best cluster target, F1 / purity):
- PVT1 → 2621: 0.64 / 0.64.
- PVT2 → 2639: 0.71 / 0.80.
- PVT3 → 2624: 0.73 / 0.94.
- PVT4 → 2626: 0.67 / 0.87.
- PVT5 is not clean: best 2637 at 0.42 / 0.83, and the rest scattered.

The PVT1–4 nodes and the PVT5 deferral wait for curator approval at the F1 gate (PR). The
existing aPVT / pPVT / umbrella nodes cite the unverifiable keys above. Fixing them is proposed in
the same PR.

The gate was raised because:
1. The full split is 7 nodes (aPVT, pPVT, PVT1–5).
2. Type vs gradient position is unresolved. Shima 2022 reports that the four scRNA-seq types are
   continuous and that the AP axis is the largest source of variance (264359607_d839d41e). Gao 2023
   calls PVT1–5 "molecularly distinct" but organised on gradients (251021326_f573a2e9,
   251021326_ecb498e7).

All quote_keys below are in `references/thalamus/quotes/` with status `pending` (ASTA-extracted,
not yet verified against the primary text).

## Candidate table

| # | proposed id / name | defining criterion | proposed parent | likely kind | source PMID · quote_keys | overlaps siblings? | decision |
|---|---|---|---|---|---|---|---|
| 1 | `apvt_glutamatergic_neuron`: anterior PVT glutamatergic neuron | AP position: anterior PVT | `pvt_glutamatergic_neuron` | DEFINITIONAL (gradient pole) | PMID:37862168 · 264359607_d839d41e, 264359607_8626b44b; PMID:36867023 · 251021326_1e273142, 251021326_3d4954d5; PMID:28426970 · 207218608_40dbc14a | No overlap with pPVT at the poles, but Shima reports an intermediate population, so the aPVT/pPVT boundary is arbitrary | **CREATED** (2026-11-26). subtype_of the umbrella: DEFINITIONAL, MODERATE. Children: apvt_crh_neuron, apvt_gck_neuron; PVT2/4/5 to come |
| 2 | `ppvt_glutamatergic_neuron`: posterior PVT glutamatergic neuron | AP position: posterior PVT | `pvt_glutamatergic_neuron` | DEFINITIONAL (gradient pole) | PMID:37862168 · 264359607_d839d41e; PMID:36867023 · 251021326_1e273142, 251021326_3d4954d5; PMID:32958568 · 221841412_8ca731a8 | As row 1 | **CREATED** (2026-11-26). subtype_of the umbrella: DEFINITIONAL, MODERATE. PVT1 and pPVT→CeA are deferred children |
| 3 | `pvt1_gao2023_neuron`: PVT1 | snRNA-seq cluster; FISH Esr1, Col12a1, Npffr1; posterior | pPVT (row 2), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736, 251021326_19d51130 | Npffr1 is shared with PVT3, and Col12a1 is also medial with PVT3 (251021326_5ed06f40) | **DEFER** to the Gao AT follow-up (parent: ppvt_glutamatergic_neuron) |
| 4 | `pvt2_gao2023_neuron`: PVT2 | FISH Hcrtr1, Drd3, Cxcl14; anterior | aPVT (row 1), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736 | Drd3 is shared with PVT4 | **DEFER** to the Gao AT follow-up (parent: apvt_glutamatergic_neuron) |
| 5 | `pvt3_gao2023_neuron`: PVT3 | FISH Npffr1, Hs6st3, Rxfp1; middle AP, no AP bias | umbrella (it fits neither pole) | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736, 251021326_5ed06f40 | Npffr1 is shared with PVT1 | **DEFER** to the Gao AT follow-up (parent: umbrella). This is the cluster most likely to be a gradient midpoint |
| 6 | `pvt4_gao2023_neuron`: PVT4 | FISH Drd3, Cbln2, Tesc; anterior | aPVT (row 1), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736 | Drd3 is shared with PVT2 | **DEFER** to the Gao AT follow-up (parent: apvt_glutamatergic_neuron) |
| 7 | `pvt5_gao2023_neuron`: PVT5 | FISH Thy1 only; anterior | aPVT (row 1), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5 | Unclear | **DEFER.** Reconsider if the Gao AT shows a clean cluster. It has one marker and a position, and no cortical-projection data (6820b736 covers PVT1–4 only). That is close to the "name + one marker" bar |
| 8 | `pvt_nacsh_projecting_neuron` | AXON_TARGET UBERON:0012171 shell of nucleus accumbens | umbrella | DEFINITIONAL | PMID:34032911 · 235203924_e162d4d9 | Yes, heavily: most PVT neurons collateralise to the same forebrain set, whatever their target | **Defer.** Intermixed and collateralised, not a discrete population. Overlap, not containment, separates it from rows 9–11 |
| 9 | `pvt_bstdl_projecting_neuron` | AXON_TARGET UBERON:0001880 bed nucleus of stria terminalis ("BSTDL") | umbrella | DEFINITIONAL | PMID:34032911 · 235203924_e162d4d9 | Yes (as row 8) | **Defer** (as row 8) |
| 10 | `pvt_cel_projecting_neuron` | AXON_TARGET UBERON:0002883 central amygdaloid nucleus ("CeL"). Ground a more specific lateral-division term at ingest | umbrella | DEFINITIONAL | PMID:34032911 · 235203924_e162d4d9; PMID:25600269 · 4471456_71209129 | Yes (as row 8); likely overlaps row 12 | **Defer** (as row 8) |
| 11 | `pvt_dmh_projecting_neuron` | AXON_TARGET UBERON:0001934 dorsomedial nucleus of hypothalamus | umbrella | DEFINITIONAL | PMID:34032911 (no DMH quote in store); PMID:23661182 · 17237721_87fea274 (rat FG retrograde) | Yes (as row 8) | **Defer.** No Li 2021 quote in the store names DMH; the only support is a rat retrograde co-labelling statement |
| 12 | `ppvt_cea_projecting_neuron`: pPVT→CeA glutamatergic projection neuron | posterior AP position + AXON_TARGET UBERON:0002883 central amygdaloid nucleus | pPVT (row 2), else umbrella | DEFINITIONAL | PMID:32958568 · 221841412_405f324a, 221841412_8ca731a8, 221841412_9b66a251; PMID:29904149 · 49208529_0485207c | Yes, with row 10 and the collateralised NAcSh/BSTDL groups | **Defer.** It has no molecular marker; the evidence is functional (pain, rat; passive coping, mouse); and CeA-projecting cells collateralise (row 8). If created later, the parent is `ppvt_glutamatergic_neuron`, which already carries the CeA AXON_TARGET with these sources |

### Projection targets as they would be written (rows 8–12)

Each target goes in `anatomical_location` as a `compartment: AXON_TARGET` entry, and the node gets
a `subtype_of` entry with kind DEFINITIONAL (parent narrowed by projection target). The
umbrella already carries these targets with the same sources. The Li 2021 sources are tracing
studies (support SUPPORT); per `CellCompartment.AXON_TARGET`, set no WEAK flag. Note in each
subtype_of assertion that the siblings overlap: `SubtypeAssertion` makes no disjointness claim.

### AXON_TARGET entries on the aPVT/pPVT nodes (now written; kept here for reference)

- aPVT: nucleus accumbens and amygdala. Do-Monte 2017 photoinhibits aPVT projections to both
  (207218608_40dbc14a); this counts as direct evidence, SUPPORT. aPVT CRF+ to NAc is already on
  apvt_crh_neuron.
- pPVT: central amygdaloid nucleus (221841412_405f324a; 49208529_0485207c, "posterior PVT …
  PVT-to-CE projections").
- PVT1/PVT3 vs PVT2/PVT4 cortical targets (251021326_6820b736) are a correlation with ThalamoSeq,
  not tracing, so support is WEAK. Scope each entry as reported jointly ("PVT1/PVT3").

## Decisions (proposed at the gate; curator approved the recommendations 2026-11-26)

1. **aPVT/pPVT as gradient-pole nodes?** The schema allows a "one end of a gradient" narrowing
   (SubtypeKind DEFINITIONAL). Shima 2022 reports an intermediate population and continuity, so
   the nodes would be poles with an unassigned middle. Recommended: yes to aPVT and pPVT. They
   carry AP position, direct projection targets (above), aPVT ephys (207218608_40dbc14a) and
   anterior/posterior FISH markers (251021326_3d4954d5). Re-parent apvt_crh_neuron and
   apvt_gck_neuron under aPVT. Kind stays DEFINITIONAL; LOW, because glutamatergic identity is
   inferred. **Done.** aPVT and pPVT are subtype_of the umbrella as DEFINITIONAL, MODERATE.
2. **PVT1–5 as nodes?** Recommended: create PVT1–4 (four nodes: three FISH markers each, AP
   position, joint cortical-projection bias) and defer PVT5 (Thy1 only). With aPVT/pPVT that is
   6 nodes, still over 5. Options: (a) accept 6; (b) do aPVT/pPVT now and PVT1–4 in a follow-up
   PR together with Gao 2023 AT; (c) do PVT1–4 only and parent them on the umbrella.
   Recommendation: (b), because the AT run gives PVT1–4 their atlas evidence in the same PR.
3. **Primary verification.** The quotes behind Gao 2023 and Shima 2022 are pending ASTA extracts.
   Both are open access (eLife; PMID:37862168 preprint). Verify the PVT-subtype quotes against the
   primary text before writing nodes. Part 3's rule requires verified quotes for both the
   criterion and the containment. **Still open:** aPVT/pPVT were created on pending quotes,
   following the usual DRAFT-node practice. Verification belongs in evidence-extraction, and it is
   a prerequisite for the PVT1–4 follow-up.

## Follow-up checklist (deferred PVT1–4 / PVT5)

1. Verify these quotes against the Gao 2023 primary text: 251021326_6e3c6191, _3d4954d5,
   _5ed06f40, _6820b736, _19d51130, _ecb498e7 and _815dcc71. Gao 2023 is eLife and open
   access.
2. Run annotation transfer from GEO:GSE208707 (Gao 2023) to WMBv1, so each new cluster node gets
   atlas evidence.
3. Ingest PVT1–4 as NEW. Parents: PVT1 → ppvt, PVT2/PVT4 → apvt, PVT3 → umbrella. Kind EMPIRICAL
   (clustering-defined; position is a finding). Defining markers are the FISH sets in the table.
   Cortical targets are AXON_TARGET with support WEAK (correlation), scoped jointly ("PVT1/PVT3",
   "PVT2/PVT4").
4. Move the cluster markers that are now kept off the pole nodes onto the cluster nodes: Hcrtr1,
   Tesc, Cbln2 and Thy1 (aPVT); Npffr1, Hs6st3 and Rxfp1 (pPVT).
5. Remove clause (a) (and (b), if PVT5 is created) from the umbrella's "DEFERRED SUBTYPE
   CANDIDATES" notes paragraph.

## Annotation transfer (separate job, not this session)

Gao 2023 snRNA-seq is GEO:GSE208707. Nodes that could declare `at_source_sets` on it:
- PVT1–PVT5 nodes, if created: EXACT to the corresponding Gao cluster label.
- aPVT: PVT2, PVT4 and PVT5, one SUBSET row per cluster.
- pPVT: PVT1 (SUBSET).
- `pvt_glutamatergic_neuron`: PVT1–5 (SUBSET each).
`apvt_gck_neuron` and `apvt_crh_neuron` have no stated correspondence to Gao clusters, so they
get no declaration.

## Done in this branch

- `pvt_glutamatergic_neuron` subtype_of `thalamic_glutamatergic_projection_neuron`: DEFINITIONAL, HIGH.
- `apvt_glutamatergic_neuron` (NEW) subtype_of `pvt_glutamatergic_neuron`: DEFINITIONAL, MODERATE.
- `ppvt_glutamatergic_neuron` (NEW) subtype_of `pvt_glutamatergic_neuron`: DEFINITIONAL, MODERATE.
- `apvt_crh_neuron` subtype_of `apvt_glutamatergic_neuron`: DEFINITIONAL, LOW.
- `apvt_gck_neuron` subtype_of `apvt_glutamatergic_neuron`: DEFINITIONAL, LOW.
- Umbrella notes:
  - The aPVT/pPVT description was removed; it now lives on the child nodes.
  - PVT1–5, the Li 2021 groups and pPVT→CeA are still described, now with the reason each was
    deferred or not created and their quote keys.
