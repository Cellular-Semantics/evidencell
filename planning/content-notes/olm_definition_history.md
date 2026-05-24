# OLM definition history — note for the redrafted OLM mapping report

*Captured 2026-05-06 during the OLM mapping refresh + Harris/Chamberland reanalysis sessions. Material for the OLM redraft scheduled for week 3–4 post-conference (see ROADMAP / [#37](https://github.com/Cellular-Semantics/evidencell/issues/37) prerequisite).*

The OLM (oriens-lacunosum-moleculare) interneuron has been defined three different ways across the literature, and the definitions do not pick out the same set of cells. The redrafted report should open with an explicit Definitions paragraph naming all three and stating which one the framework adopts.

## Three definitions

**1. Morphological (the original).** Cajal/McBain/Sik/Maccaferri/Lacaille era. An OLM cell is one whose soma sits in stratum oriens, dendrites are horizontal in oriens, and axon projects vertically through the layers to ramify in stratum lacunosum-moleculare. No molecular criteria. Broadest definition. Citations on the OLM classical node: Zemankovics et al. 2010 ([PMID 20421280](https://pubmed.ncbi.nlm.nih.gov/20421280/)), Tecuatl et al. 2020 ([PMID 33361464](https://pubmed.ncbi.nlm.nih.gov/33361464/)).

**2. Sst-era multimodal.** Late 1990s through mid-2010s. Adds a molecular requirement: Sst+. So "Sst+ stratum oriens neuron with OLM morphology". Still includes most morphologically-defined OLMs because Sst is broadly expressed across the population, but excludes any non-Sst horizontal-cell types. Citations: Hooft et al. 2000 ([PMID 10804195](https://pubmed.ncbi.nlm.nih.gov/10804195/)), Oliva et al. 2000 ([PMID 10777798](https://pubmed.ncbi.nlm.nih.gov/10777798/)).

**3. Chrna2-as-precise-marker.** Leão et al. 2012 ([PMID 23042082](https://pubmed.ncbi.nlm.nih.gov/23042082/)) introduces Chrna2-Cre as "a precise molecular marker for a population of hippocampal GABAergic interneurons known as oriens lacunosum-moleculare cells". This becomes the dominant operational definition in subsequent functional and connectivity studies (Mikulovic 2015, Hilscher 2019 [PMID 31301163](https://pubmed.ncbi.nlm.nih.gov/31301163/), Nichol 2018 [PMID 29487503](https://pubmed.ncbi.nlm.nih.gov/29487503/), Thulin 2025 [PMID 40757734](https://pubmed.ncbi.nlm.nih.gov/40757734/)) because the transgenic line is the experimental handle. In effect: OLM = Chrna2-Cre+ stratum oriens cell.

## What Chamberland 2024 changes

Chamberland et al. 2024 ([PMID 38640347](https://pubmed.ncbi.nlm.nih.gov/38640347/)) demonstrate that **Chrna2-Cre targets only one of at least two morphologically-OLM Sst+ subfamilies**: Chrna2-OLM and Ndnf::Nkx2-1-OLM are both OLMs by morphology, both Sst+, but only the first is Chrna2+. The two subfamilies differ in:

- **Postsynaptic target preference.** Ndnf::Nkx2-1-OLM preferentially targets CA1 pyramidal cells over fast-spiking interneurons; Chrna2-OLM lacks this preference.
- **Axonal projection.** Ndnf::Nkx2-1-OLM projects to both stratum oriens AND lacunosum-moleculare. Chrna2-OLM projects almost exclusively to lacunosum-moleculare.

Under definition (1) — morphological — there are two OLM subtypes. Under definition (3) — Chrna2-as-precise-marker — only Chrna2-OLM is "really" OLM and the Ndnf-OLM is something else (or simply was never on the radar of studies using Chrna2-Cre as the OLM handle). Definition (2) sits in the middle and is consistent with the multi-subfamily reading.

## Implications for the OLM classical node

The current OLM classical node carries `Chrna2` in `defining_markers`, citing Leão 2012, Nichol 2018, and Winterer 2019 (i.e. the Chrna2-as-precise-marker tradition). The classical type table at the top of the report effectively encodes definition (3). Under Chamberland's reading this is **biologically wrong**: it elevates a subset marker to a defining marker, and consequently treats CLUS_0768 (Ndnf-OLM, Chrna2 mostly absent) as having a *defining marker discordance* when in fact CLUS_0768 is plausibly an OLM under the morphological definition that Chrna2 was always intended to operationalise.

Three concrete redraft changes follow:

1. **Open the Introduction with an explicit Definitions paragraph** that names the three definitions and states which one this report adopts. Recommendation: definition (1), morphological, with Sst+ as an additional necessary condition (i.e. definition (2)). This is what Chamberland 2024 implicitly uses and what cleanly accommodates the subfamily structure.

2. **Demote `Chrna2` from `defining_markers` to a `subtype_markers` field** (or add a `marker_role` enum on existing `defining_markers[*]` with values like DEFINING / SUBTYPE_DEFINING / NEGATIVE). The Leão 2012, Nichol 2018, and Thulin 2025 citations would land on `subtype_markers` rather than `defining_markers`. Schema dependency: [#37](https://github.com/Cellular-Semantics/evidencell/issues/37) covers this with the proposed `proposed_subtypes[]` slot; a separate small `marker_role` extension may be needed if the demotion is to `defining_markers[*].marker_role` rather than a new field.

3. **Add `proposed_subtypes[]`** (the slot proposed in [#37](https://github.com/Cellular-Semantics/evidencell/issues/37)) populated with `OLM_Chrna2` and `OLM_Ndnf::Nkx2-1`, each with its own marker signature and candidate atlas cluster — and explicitly cite Leão 2012 (for the Chrna2-OLM subtype, *not* the OLM type as a whole) and Chamberland 2024 (for the formal split).

The downstream consequences propagate to many edges. Currently several "Chrna2 DISCORDANT" caveats are used to *eliminate* candidate clusters (Sst Gaba_6 trio, CLUS_0769); these would be reframed as "Chrna2 absent therefore not Chrna2-OLM, but Sst-OLM-by-morphology not ruled out at this evidence level". Some eliminations probably stand on other grounds (Sst Gaba_6 amygdala spread, CA3-restricted distribution); others may shift status.

## Why this matters as a paper-level point

The OLM case is a useful illustrative for the framework because it shows the framework dealing honestly with **definitional drift in the literature** — a fundamental issue for any cell-type knowledge base that the static-ontology approach cannot represent. The schema additions in [#37](https://github.com/Cellular-Semantics/evidencell/issues/37) plus a `marker_role` enum would let the framework hold "the literature has used Chrna2 in three different ways: as a marker for the whole population, as a marker for one subset, as a Cre-driver experimental handle" as structured data rather than as free-text caveats. Worth a paragraph or a slide in the conference talk and a substantial section in the planned preprint/journal submission.

## Provenance

Captured from the BICAN agentic framework planning chat session, 2026-05-05 to 2026-05-06. Discussion threads:

- Three-definitions framing emerged when reviewing the Chamberland 2024 finding's implications for the OLM classical type table.
- Chamberland subfamily assignment to WMBv1 child clusters confirmed independently by both target-side marker overlay (this session) and source-side annotation transfer with per-cluster labels ([`at_run_20260506_harris_chamberland_mmc_wmbv1`](../../kb/annotation_transfer_runs/at_run_20260506_harris_chamberland_mmc_wmbv1/)).
- Redraft scheduled for week 3–4 post-conference, after [#37](https://github.com/Cellular-Semantics/evidencell/issues/37) (schema), [#32](https://github.com/Cellular-Semantics/evidencell/issues/32) (AT registry), [#34](https://github.com/Cellular-Semantics/evidencell/issues/34) (find-candidates scoring) land.
