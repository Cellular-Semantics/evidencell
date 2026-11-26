# PVT subtype candidates — split proposal (GATE)

Date: 2026-11-26 · Branch: `content/thalamus-pvt-subtypes` · Umbrella: `pvt_glutamatergic_neuron`
Source run: `research/thalamus/20261114_thalamus_pvt_report_ingest/` (PVT_Glut.pdf)

Status: **stopped at [GATE], no new nodes created.** Two gate conditions hold:

1. The proposed split is 7 nodes (aPVT, pPVT, PVT1–5), more than the cap of 5.
2. Type vs gradient position is unresolved. Shima 2022 reports that the four scRNA-seq types are
   continuous and that the AP axis is the largest source of variance (264359607_d839d41e). Gao 2023
   calls PVT1–5 "molecularly distinct" but organised on gradients (251021326_f573a2e9,
   251021326_ecb498e7).

The curator should decide on the questions under "Decisions needed" below. Then continue the PVT
ingest from `workflows/asta-report-ingest.md` Step 3 (identity + subtype_of), then Step 4 and
Step 5, in the 2026-11-14 run dir.

All quote_keys below are in `references/thalamus/quotes/` with status `pending` (ASTA-extracted,
not yet verified against the primary text).

## Candidate table

| # | proposed id / name | defining criterion | proposed parent | likely kind | source PMID · quote_keys | overlaps siblings? | decision |
|---|---|---|---|---|---|---|---|
| 1 | `apvt_glutamatergic_neuron`: anterior PVT glutamatergic neuron | AP position: anterior PVT | `pvt_glutamatergic_neuron` | DEFINITIONAL (gradient pole) | PMID:37862168 · 264359607_d839d41e, 264359607_8626b44b; PMID:36867023 · 251021326_1e273142, 251021326_3d4954d5; PMID:28426970 · 207218608_40dbc14a | No overlap with pPVT at the poles, but Shima reports an intermediate population, so the aPVT/pPVT boundary is arbitrary | **GATE.** Likeliest to qualify. It would take apvt_crh_neuron and apvt_gck_neuron as children, plus PVT2/4/5 |
| 2 | `ppvt_glutamatergic_neuron`: posterior PVT glutamatergic neuron | AP position: posterior PVT | `pvt_glutamatergic_neuron` | DEFINITIONAL (gradient pole) | PMID:37862168 · 264359607_d839d41e; PMID:36867023 · 251021326_1e273142, 251021326_3d4954d5; PMID:32958568 · 221841412_8ca731a8 | As row 1 | **GATE.** Pair with row 1. It would take PVT1 and pPVT→CeA as children |
| 3 | `pvt1_gao2023_neuron`: PVT1 | snRNA-seq cluster; FISH Esr1, Col12a1, Npffr1; posterior | pPVT (row 2), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736, 251021326_19d51130 | Npffr1 is shared with PVT3, and Col12a1 is also medial with PVT3 (251021326_5ed06f40) | **GATE** |
| 4 | `pvt2_gao2023_neuron`: PVT2 | FISH Hcrtr1, Drd3, Cxcl14; anterior | aPVT (row 1), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736 | Drd3 is shared with PVT4 | **GATE** |
| 5 | `pvt3_gao2023_neuron`: PVT3 | FISH Npffr1, Hs6st3, Rxfp1; middle AP, no AP bias | umbrella (it fits neither pole) | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736, 251021326_5ed06f40 | Npffr1 is shared with PVT1 | **GATE.** This is the cluster most likely to be a gradient midpoint |
| 6 | `pvt4_gao2023_neuron`: PVT4 | FISH Drd3, Cbln2, Tesc; anterior | aPVT (row 1), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5, 251021326_6820b736 | Drd3 is shared with PVT2 | **GATE** |
| 7 | `pvt5_gao2023_neuron`: PVT5 | FISH Thy1 only; anterior | aPVT (row 1), else umbrella | EMPIRICAL | PMID:36867023 · 251021326_6e3c6191, 251021326_3d4954d5 | Unclear | **GATE, lean defer.** It has one marker and a position, and no cortical-projection data (6820b736 covers PVT1–4 only). That is close to the "name + one marker" bar |
| 8 | `pvt_nacsh_projecting_neuron` | AXON_TARGET UBERON:0012171 shell of nucleus accumbens | umbrella | DEFINITIONAL | PMID:34032911 · 235203924_e162d4d9 | Yes, heavily: most PVT neurons collateralise to the same forebrain set, whatever their target | **Defer.** Intermixed and collateralised, not a discrete population. Overlap, not containment, separates it from rows 9–11 |
| 9 | `pvt_bstdl_projecting_neuron` | AXON_TARGET UBERON:0001880 bed nucleus of stria terminalis ("BSTDL") | umbrella | DEFINITIONAL | PMID:34032911 · 235203924_e162d4d9 | Yes (as row 8) | **Defer** (as row 8) |
| 10 | `pvt_cel_projecting_neuron` | AXON_TARGET UBERON:0002883 central amygdaloid nucleus ("CeL"). Ground a more specific lateral-division term at ingest | umbrella | DEFINITIONAL | PMID:34032911 · 235203924_e162d4d9; PMID:25600269 · 4471456_71209129 | Yes (as row 8); likely overlaps row 12 | **Defer** (as row 8) |
| 11 | `pvt_dmh_projecting_neuron` | AXON_TARGET UBERON:0001934 dorsomedial nucleus of hypothalamus | umbrella | DEFINITIONAL | PMID:34032911 (no DMH quote in store); PMID:23661182 · 17237721_87fea274 (rat FG retrograde) | Yes (as row 8) | **Defer.** No Li 2021 quote in the store names DMH; the only support is a rat retrograde co-labelling statement |
| 12 | `ppvt_cea_projecting_neuron`: pPVT→CeA glutamatergic projection neuron | posterior AP position + AXON_TARGET UBERON:0002883 central amygdaloid nucleus | pPVT (row 2), else umbrella | DEFINITIONAL | PMID:32958568 · 221841412_405f324a, 221841412_8ca731a8, 221841412_9b66a251; PMID:29904149 · 49208529_0485207c | Yes, with row 10 and the collateralised NAcSh/BSTDL groups | **Defer.** It has no molecular marker; the evidence is functional (pain, rat; passive coping, mouse); its parent, pPVT, is itself gated; and CeA-projecting cells collateralise (row 8) |

### Projection targets as they would be written (rows 8–12)

Each target goes in `anatomical_location` as a `compartment: AXON_TARGET` entry, and the node gets
a `subtype_of` entry with kind DEFINITIONAL (parent narrowed by projection target). The
umbrella already carries these targets with the same sources. The Li 2021 sources are tracing
studies (support SUPPORT); per `CellCompartment.AXON_TARGET`, set no WEAK flag. Note in each
subtype_of assertion that the siblings overlap: `SubtypeAssertion` makes no disjointness claim.

### Further AXON_TARGET entries for the aPVT/pPVT nodes (if created)

- aPVT: nucleus accumbens and amygdala. Do-Monte 2017 photoinhibits aPVT projections to both
  (207218608_40dbc14a); this counts as direct evidence, SUPPORT. aPVT CRF+ to NAc is already on
  apvt_crh_neuron.
- pPVT: central amygdaloid nucleus (221841412_405f324a; 49208529_0485207c, "posterior PVT …
  PVT-to-CE projections").
- PVT1/PVT3 vs PVT2/PVT4 cortical targets (251021326_6820b736) are a correlation with ThalamoSeq,
  not tracing, so support is WEAK. Scope each entry as reported jointly ("PVT1/PVT3").

## Decisions needed (curator)

1. **aPVT/pPVT as gradient-pole nodes?** The schema allows a "one end of a gradient" narrowing
   (SubtypeKind DEFINITIONAL). Shima 2022 reports an intermediate population and continuity, so
   the nodes would be poles with an unassigned middle. Recommended: yes to aPVT and pPVT. They
   carry AP position, direct projection targets (above), aPVT ephys (207218608_40dbc14a) and
   anterior/posterior FISH markers (251021326_3d4954d5). Re-parent apvt_crh_neuron and
   apvt_gck_neuron under aPVT. Kind stays DEFINITIONAL; LOW, because glutamatergic identity is
   inferred.
2. **PVT1–5 as nodes?** Recommended: create PVT1–4 (four nodes: three FISH markers each, AP
   position, joint cortical-projection bias) and defer PVT5 (Thy1 only). With aPVT/pPVT that is
   6 nodes, still over 5. Options: (a) accept 6; (b) do aPVT/pPVT now and PVT1–4 in a follow-up
   PR together with Gao 2023 AT; (c) do PVT1–4 only and parent them on the umbrella.
   Recommendation: (b), because the AT run gives PVT1–4 their atlas evidence in the same PR.
3. **Primary verification.** The quotes behind Gao 2023 and Shima 2022 are pending ASTA extracts.
   Both are open access (eLife; PMID:37862168 preprint). Verify the PVT-subtype quotes against the
   primary text before writing nodes. Part 3's rule requires verified quotes for both the
   criterion and the containment.

## Annotation transfer (separate job, not this session)

Gao 2023 snRNA-seq is GEO:GSE208707. Nodes that could declare `at_source_sets` on it:
- PVT1–PVT5 nodes, if created: EXACT to the corresponding Gao cluster label.
- aPVT: PVT2, PVT4 and PVT5, one SUBSET row per cluster.
- pPVT: PVT1 (SUBSET).
- `pvt_glutamatergic_neuron`: PVT1–5 (SUBSET each).
`apvt_gck_neuron` and `apvt_crh_neuron` have no stated correspondence to Gao clusters, so they
get no declaration.

## Done in this branch (Part 1)

- `pvt_glutamatergic_neuron` subtype_of `thalamic_glutamatergic_projection_neuron`: DEFINITIONAL, HIGH.
- `apvt_crh_neuron` subtype_of `pvt_glutamatergic_neuron`: DEFINITIONAL, LOW.
- `apvt_gck_neuron` subtype_of `pvt_glutamatergic_neuron`: DEFINITIONAL, LOW.
- The umbrella's subtype paragraph still describes PVT1–5, aPVT/pPVT, the Li 2021 groups and
  pPVT→CeA, because none of them is a node yet.
