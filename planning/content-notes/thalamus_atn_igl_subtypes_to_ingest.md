# ATN and IGL subtype candidates: split and deferrals

Date: 2026-11-26 · Branch: `content/thalamus-atn-igl-subtype-of` (PR #261)
Umbrellas: `anterior_thalamic_nucleus_excitatory_neuron` (children AD / AV / AM),
`igl_gabaergic_neuron`, `lgv_igl_gabaergic_neuron`
Source runs:
- `research/thalamus/20261115_thalamus_atn_report_ingest/` (ATN_Glut.pdf)
- `research/thalamus/20261112_thalamus_igl_report_ingest/` (IGL.pdf)

**Status: stopped at the [GATE]. No nodes created.** Two problems block it.

1. **The ATN subtype evidence fails primary verification (provenance problem).** The
   AD1–2 / AV1–3 / AM1–3 / ADP / AMd / AMv / AMdc / AMV scheme and its markers (Tnnt1, Col5a1,
   Cacna2d1, Calb1) rest on quotes stored under corpus 279797062. The store resolves that corpus
   to Hintiryan et al. 2025, *Distinct subnetworks of the mouse anterior thalamic nuclei*
   (Nat Commun; PMID:40593635; PMC12216302; open access).

   **Check against the full text (Europe PMC).** Only 1 of the 10 stored quotes is in that paper:
   279797062_33751aaa, from the abstract. These nine are not:
   `_049553b3 _79c8b7ec _289edc65 _d062691f _228b8f25 _6369b05f _9833fcee _de94e1f6 _7b604467`

   In the full text:
   - none of the type names AD1/AV1/AMdc/ADP appear (the only string hits are citation
     artefacts such as "AV16,18");
   - none of the genes Tnnt1, Col5a1, Cacna2d1, Pvalb or C1ql2 appear;
   - the word "glutamatergic" does not appear.

   The paper's own units are different. They are connectivity-defined **domains**, found by
   aggregating tracer labelling on a spatial grid and running Louvain community detection:
   AD.medial / AD.lateral; AV.dorsal / lateral / medial / medial tip; AMd sub-domains; AMv. It
   has no molecular data. All ten quotes carry one section label ("Shared cellular properties of
   excitatory projection neurons across ATN"), which is not a section of the paper. So the ASTA
   report probably attributed text from another source to this corpus ID. That source is
   unidentified; Europe PMC searches on Tnnt1 / Col5a1 / Cacna2d1 / AMdc + ATN found nothing. A
   Research Square preprint with the same title (doi 10.21203/rs.3.rs-4356188/v1) has no full
   text in Europe PMC and could not be checked.

   **Part 3 requires verified quotes for both the criterion and the containment. No ATN
   candidate below meets that.**
2. **Type vs gradient is unresolved anyway.** Kapustina et al. 2024 report "graded spatial
   variation along the dorsomedial-ventrolateral axis for all individual nuclei of the ATN"
   (268122794_e9176ba6), with AV inputs and proteins covarying along it. The published Hintiryan
   domains are positional subdivisions found by grid-based community detection, not
   per-cell clustering. Its Discussion describes "minor spillover across border regions".
   Whether the domains are cell types or parcels of a continuum is a curator decision.

**Effect on Part 1 (fixed in this PR).** Part 1 had cited 279797062_9833fcee (ATN →
thalamic_glutamatergic_projection_neuron) and 279797062_79c8b7ec (AD/AV/AM → ATN). Both sources
are removed:
- ATN → parent now cites Kapustina 268122794_5c2e793b and the Clascá review 23594973_a7fbdba3.
- AD/AV/AM → ATN cite Kapustina 268122794_e9176ba6 and the verified Hintiryan abstract sentence
  279797062_33751aaa.

**Pre-existing KB content (not changed here).** These existing assertions on the AD / AV / AM
/ ATN nodes cite the unsupported keys:
- AD Pvalb, AV C1ql2 / Bdnf, AM Rspo2 / Tnnt1 markers (`_7b604467`, `_289edc65`);
- the ATN morphology (`_6369b05f`);
- ATN / AD / AV / AM nt_type sources (`_9833fcee`);
- several anatomy and morphology sources (`_79c8b7ec`, `_049553b3`);
- the "SUBTYPES NOTED" paragraphs.

They need a follow-up: find the true source of these quotes, or replace and remove them. This
PR is scoped to subtype_of, and the reference store is additive-only while other thalamus
branches are open, so I didn't edit them here.

Anatomy terms follow the 2026-11-26 curator decision: MBA for rodent nodes, UBERON only where MBA
has no term at the right granularity.

## Candidate table: ATN

All ATN rows are mouse. "Unverified" means the only quote supporting the row is one of the nine
keys above.

| # | proposed id / name | defining criterion | proposed parent | likely kind | source · quote_keys | overlaps siblings? | decision |
|---|---|---|---|---|---|---|---|
| 1 | `ad1_anterodorsal_projection_neuron`: AD1 | position: dorsolateral AD. Projection: postsubiculum, VISl / VISli, mammillary body | `anterodorsal_thalamic_nucleus_excitatory_neuron` | DEFINITIONAL (subregion + target) | unverified: 279797062_049553b3, _79c8b7ec, _de94e1f6 | On Kapustina's within-AD DM–VL gradient; shares targets with AD2 | **DEFER.** The quotes aren't in PMID:40593635. The nearest published unit is the "AD.lateral" domain |
| 2 | `ad2_anterodorsal_projection_neuron`: AD2 | position: ventromedial AD. Projection: RSP, visual, postsubiculum, mammillary body | as row 1 | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | As row 1 | **DEFER.** As row 1 (nearest: "AD.medial") |
| 3 | `av1_anteroventral_projection_neuron`: AV1 | position: dorsomedial AV. Projection: PL, ACA, anterior RSP | `anteroventral_thalamic_nucleus_excitatory_neuron` | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | Likely overlaps the AVDM input subregion (row 15); on AV's DM–VL gradient | **DEFER.** Unverified; AV is where Kapustina's gradients are strongest |
| 4 | `av2_anteroventral_projection_neuron`: AV2 | position: ventrolateral AV. Projection: RSPv, ventral visual stream | as row 3 | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | Likely overlaps AVVL (row 15) | **DEFER.** As row 3 |
| 5 | `av3_anteroventral_projection_neuron`: AV3 | position: dorsolateral AV. Projection: prefrontal + visual | as row 3 | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | Unclear | **DEFER.** As row 3 |
| 6 | `am1_anteromedial_projection_neuron`: AM1 | throughout AM. Projection: ACA + RSP. No marker | `anteromedial_thalamic_nucleus_excitatory_neuron` | DEFINITIONAL (target only) | unverified: _049553b3, _79c8b7ec, _d062691f | Shares targets with AM3 | **DEFER.** Unverified, and no marker or subregion |
| 7 | `am2_anteromedial_projection_neuron`: AM2 | position: ventrolateral AM ("all portions" in _049553b3). Projection: prefrontal, prostriata, ventral visual | as row 6 | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | Unclear | **DEFER.** Unverified; the two quotes disagree on its position |
| 8 | `am3_tnnt1_anteromedial_projection_neuron`: AM3 | throughout the principal AM. Marker: Tnnt1. Projection: prefrontal, ACA, RSP | as row 6 | EMPIRICAL | unverified: _049553b3, _79c8b7ec, _289edc65 | Shares Tnnt1 with AMdc | **DEFER.** Would meet the bar if a verified source is found. Tnnt1 does not appear in PMID:40593635 |
| 9 | `adp_anteromedial_projection_neuron`: ADP | position: dorsal aspect of posterior AM. Marker: Cacna2d1. Projection: PL, ACA, visual | as row 6 | EMPIRICAL | unverified: _049553b3, _79c8b7ec, _289edc65 | None reported | **DEFER.** As row 8 |
| 10 | `amd_anteromedial_projection_neuron`: AMd | position: dorsal middle AM (MBA:1096 "Anteromedial nucleus, dorsal part"). Projection: ACA, visual | as row 6 | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | Unclear | **DEFER.** Unverified. The published paper does use "AMd" (with sub-domains): a possible verified route via a new primary quote |
| 11 | `amv_anteromedial_projection_neuron`: AMv | position: ventral middle AM (MBA:1104 "Anteromedial nucleus, ventral part"). Projection: PL, ACA | as row 6 | DEFINITIONAL | unverified: _049553b3, _79c8b7ec | Unclear | **DEFER.** As row 10 ("AMv" is a published domain) |
| 12 | `amdc_tnnt1_anteromedial_projection_neuron`: AMdc | position: rostral AM dorsal cap. Marker: Tnnt1. Projection: PL, ACA | as row 6 | EMPIRICAL | unverified: _049553b3, _79c8b7ec, _289edc65 | Shares Tnnt1 with AM3 | **DEFER.** As row 8 |
| 13 | `amv_border_col5a1_anteromedial_projection_neuron`: AMV | position: caudal ventral border of AM. Marker: Col5a1. Projection: ORBv / ORBvl, AI, ENT | as row 6 | EMPIRICAL | unverified: _049553b3, _79c8b7ec, _289edc65 | None reported | **DEFER.** As row 8 |
| 14 | Calb1+ AM type (unnamed) | marker: Calb1 only | as row 6 | EMPIRICAL | unverified: _289edc65 | Unstated | **DEFER.** A name plus one marker, and unverified |
| 15 | AVDM / AVVL input subregions | AV subregion defined by afferent input (ACA → AVDM) | AV | DEFINITIONAL | PMID:32964131 · 221820655_439b9d6b (rat, review) | Overlaps AV1/AV2 | **Not created.** Input-defined subregions, not cell populations. Gradient context on AV |
| 16 | Grp_KH288-Cre+ AV subset | BAC Cre line: subset of AV, none in AD | AV | EMPIRICAL | PMID:30858601 · 73729161_fddda88d | Unknown | **DEFER.** Transgene label only (a name plus one transgene) |
| 17 | AV single-axon type 1 / type 2 (rat) | granular-RSC arbor: layer Ia only vs also layers III/IV | AV | EMPIRICAL | PMID:22013412 · 903275_698804ed | Unknown relation to AV2 | **DEFER.** One rat single-axon study; axon classes without soma position or marker |
| 18 | AM transcriptomic subdomains (THALMANAC) | MERFISH supertypes within AM | AM | EMPIRICAL | https://doi.org/10.1101/2025.09.30.679413 · 282311854_6f08b319, _83c180d9 | Likely overlaps rows 6–13 | **DEFER.** No subdomain or marker is named in the quotes. Better handled as an atlas correspondence via map-cell-type |
| 18b | Hintiryan 2025 published connectivity domains (AD.medial / AD.lateral; AV.dorsal / lateral / medial / medial tip; AMd sub-domains; AMv) | position + brain-wide input/output pattern, from grid-based Louvain community detection on tracer labelling | AD / AV / AM | DEFINITIONAL (subregion) | PMID:40593635 · no quotes in the store yet (new primary quotes needed) | Domains tile each nucleus; "minor spillover across border regions" | **DEFER (gate).** Type vs parcel is a curator call. If accepted, these would replace rows 1–13 as the verified scheme. Needs new primary quotes (additive) |

### Projection targets as they would be written

For any ATN projection-defined node created later: `anatomical_location`,
`compartment: AXON_TARGET`, cited to a verified quote.

| target in source | term | note |
|---|---|---|
| postsubiculum | MBA:1037 Postsubiculum | |
| lateral / laterointermediate visual area | MBA:409 Lateral visual area; MBA:312782574 Laterointermediate area | "laterodorsal visual area" has no MBA term |
| mammillary regions | MBA:331 Mammillary body | |
| retrosplenial | MBA:254 Retrosplenial area | granular RSC → MBA:886 Retrosplenial area, ventral part |
| prelimbic | MBA:972 Prelimbic area | |
| anterior cingulate | MBA:31 Anterior cingulate area | |
| visual | MBA:669 Visual areas | give the "ventral visual stream" in name_in_source |
| prefrontal | UBERON:0000451 prefrontal cortex | MBA has no whole-PFC term |
| prostriata | none | not in MBA. Not MBA:484682470 Prosubiculum |
| ventral orbital | MBA:738 Orbital area, ventral part / MBA:746 ventrolateral part | |
| agranular insular | MBA:95 Agranular insular area | |
| entorhinal | MBA:909 Entorhinal area | |
| contralateral IGL (IGL rows) | MBA:27 Intergeniculate leaflet of the lateral geniculate complex | |
| SCN (IGL rows) | MBA:286 Suprachiasmatic nucleus | |

## Candidate table: IGL / LGv

The IGL evidence is rat. The vLGN nodes from #235 cover the LGv side (vLGNe, vLGNi,
SC-projecting, local interneuron, Sox14, and LHb-, LPBN- and reuniens-projecting).
`igl_npy_geniculohypothalamic_neuron` belongs to evidencell_1.

| # | proposed id / name | defining criterion | proposed parent | likely kind | source · quote_keys | overlaps siblings? | decision |
|---|---|---|---|---|---|---|---|
| 19 | Thankachan Type I: NPY-lacking, light-sustained IGL/VLG neuron | NPY absent (juxtacellular label). Sustained activation by retinal illumination | `lgv_igl_gabaergic_neuron` (spans IGL/VLG) | EMPIRICAL | PMID:16207879 · 9130790_8fa09d39 (pending) | May overlap the ENK class (also NPY-negative) and the third cell group | **DEFER.** One study; the criterion is a functional response plus an absent marker, and it crosses the IGL/VLG boundary |
| 20 | Thankachan Type III: NPY-recipient, light-on / dark-silent neuron | patchy, internalised NPY. Sustained light activation, silent in dark | `lgv_igl_gabaergic_neuron` | EMPIRICAL | PMID:16207879 · 9130790_8fa09d39 | Unknown relation to ENK | **DEFER.** As row 19 |
| 21 | Thankachan Type II | strong somatic NPY | — | — | PMID:16207879 · 9130790_8fa09d39 | Likely the same population as igl_npy | **Not a new node.** A possible ENRICH of igl_npy, for evidencell_1 |
| 22 | IGL "third cell group" of unknown transmitter | none given | unclear (GABAergic identity unknown) | — | PMID:23432696 · 36406110_2999c838 | Unknown | **Not created.** No defining property |

## Decisions for the curator (the gate)

1. **Provenance of corpus 279797062's quotes.** Find where the nine unsupported quotes come
   from. They could be the Research Square preprint, or another paper misattributed by ASTA.
   - Is the source a different paper? Then file its quotes under the right corpus ID and repoint
     the KB citations.
   - Is there no source? Then remove the dependent marker, NT, morphology and SUBTYPES NOTED
     assertions on the ATN / AD / AV / AM nodes.
   - Recommended: a dedicated follow-up content PR, after the open thalamus branches merge
     (the reference store is additive-only until then).
2. **Hintiryan published domains (row 18b): cell types or positional parcels?** They come from
   tracer-grid community detection, not per-cell data, and lie on Kapustina's gradients.
   Recommended: treat them as parcels for now (do not create). Revisit if the curator wants
   DEFINITIONAL subregion nodes.
3. **IGL.** Nothing to create (rows 19–22). Pass Thankachan Type II to evidencell_1.

## Follow-up checklist

1. Resolve decision 1 before any ATN subtype work.
2. If subtype nodes are approved later, follow `workflows/asta-report-ingest.md` from Step 3
   in `research/thalamus/20261115_thalamus_atn_report_ingest/`. First rebuild
   `run_quotes.json` and `ingest_plan.yaml` there; they predate the current workflow.
3. When a child node exists, remove its entry from the AD / AV / AM "SUBTYPES NOTED" notes.
   Leave the deferred ones with their reason.
4. AT: Kapustina GSE227627 has no per-cell cluster labels, so it can't supply child-level AT.
