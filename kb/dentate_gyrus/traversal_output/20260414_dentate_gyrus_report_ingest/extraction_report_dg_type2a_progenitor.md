# Extraction report: dg_type2a_progenitor

- Extraction date: 2026-04-22
- Node: dg_type2a_progenitor (Dentate Gyrus Type-2a Neural Progenitor, CL:9900003)
- Node context: Nestin+/Sox2+ amplifying progenitor in SGZ, DCX−, GFAP−, non-radial,
  actively proliferating (Ki67+), glutamatergic (lineage-committed), no synaptic
  integration.
- Source summaries: `all_summaries.json`
- Excluded corpus IDs (per orchestrator): 14221248, 252063749, 7440369, 13752593

## Summary

- Total non-excluded summaries reviewed: 13 (12 with quotes; 1 empty CorpusId:148569364).
- Proposed evidence items: 12 (1 per summary with non-empty quotes, excluding
  CorpusId:148569364 which has no extractable quotes).
- Support distribution: 2 SUPPORT, 10 PARTIAL, 0 REFUTE.
- PARTIAL dominates, as expected per the orchestrator note — most papers describe
  the broader NSC → neuroblast → immature → mature lineage rather than type-2a
  specifically.

## Target-field coverage

| Target field            | Items | Notes                                                                                                  |
|-------------------------|-------|--------------------------------------------------------------------------------------------------------|
| defining_markers        | 4     | Nestin+/Sox2+ type-2a named explicitly only in Micheli 2025; others support the broader type-2/IPC pattern. |
| morphology_notes        | 4     | Clustered SGZ location (Hodge 2008 SUPPORT); other items speak to broader lineage morphology / timing. |
| negative_markers        | 3     | DCX status of type-2a (DCX−) inferred from DCX's canonical assignment to immature neurons/neuroblasts. |
| nt_type                 | 1     | Glutamatergic identity of DG lineage (Dayer 2005 cross-regional).                                      |
| anatomical_location     | 0     | SGZ location is implied in multiple items (Hodge 2008, Stepien 2021) but no snippet addresses it alone. |
| electrophysiology_class | 0     | Per node context, type-2a has no synaptic integration; ephys is not a defined field for this node.     |

## Papers that characterise type-2a specifically

Only one summary names type-2a with its Nestin+/Sox2+ marker signature explicitly:

- **CorpusId:279046466 (Micheli 2025, PMID:40519263)** — Directly names "type-2a
  (Nestin+/Sox2+)" and places it in the sequential marker progression through
  type-2b (Nestin+/DCX+) and neuroblasts (type-3, DCX+). This is the single most
  informative item for the node and is the only direct SUPPORT for
  defining_markers of type-2a.

- **CorpusId:15727849 (Hodge 2008, PMID:18385329)** — Characterises Tbr2+ cells
  in the SGZ with morphology consistent with "type-2 progenitors" (96.76% of
  nestin-GFP+, Tbr2+ double-labelled cells) and notes clustering in SGZ near
  type-1 nestin-GFP+ cells. Addresses type-2 IPCs directly but does not
  disambiguate type-2a vs type-2b; classified as SUPPORT for morphology_notes.

## Papers that mention the lineage broadly

All remaining 10 non-excluded summaries describe DG neurogenesis in passing
or characterise neighbouring stages (neuroblast, immature granule neuron) and
therefore contribute only PARTIAL evidence to type-2a:

- **CorpusId:7393550 (Attardo 2009, PMID:19482889)** — Tis21 in postmitotic
  neurons; type-2 progenitors mentioned in context but not marker-characterised.
- **CorpusId:245432259 (Stepien 2021, PMID:37082558)** — Lists "type II cells —
  non-sessile cells expressing nestin" without disambiguating 2a/2b.
- **CorpusId:258927570 (Hussain 2023, PMID:37488837)** — Broad lineage
  description, no type-2a-specific content.
- **CorpusId:14598082 (Merz 2013, PMID:23667508)** — Canonical DCX assignment
  to immature neurons implies DCX− status for earlier progenitors.
- **CorpusId:8479504 (Stoll 2014, PMID:26056581)** — Describes B/C/A-type cells
  but in SVZ context (GFAP+Nestin+Dcx−, GFAP−Nestin+Dcx+); parallels to DG
  type-1/2a/2b are partial at best.
- **CorpusId:235300723 (Coviello 2021, PMID:34072166)** — Piriform cortex
  immature neurons; only tangentially relevant to DG type-2a.
- **CorpusId:13799502 (Rotheneichner 2018, PMID:29688272)** — Piriform cortex
  CaMKII acquisition; glutamatergic lineage context.
- **CorpusId:233432690 (Groen 2021, PMID:33994960)** — DCX+/Ki67+/PCNA+
  proliferative cells; supports DCX+ proliferating stages but not type-2a
  (DCX−) directly.
- **CorpusId:15994456 (Dayer 2005, PMID:15684031)** — Calretinin→calbindin
  switch in DG granule cells; relevant to nt_type via glutamatergic granule
  lineage, but does not mention type-2a.
- **CorpusId:625292 (Vangeneugden 2015, DOI:10.3389/fnins.2015.00110)** —
  Olfactory bulb granule cells; morphology/integration timing cross-regional
  only.

## Key finding: the type-2a characterisation gap

There is a clear asymmetry between the number of papers that cite the standard
Kempermann-style type-2a/2b/type-3 classification (essentially one summary in
this set: Micheli 2025) and the number of papers that mention the adult DG
lineage in passing (all the rest). Hodge 2008 is the only primary-study summary
in this set that provides histological/marker data specifically addressing
"type-2" progenitors (as a class) — and even then, it does not disambiguate
2a from 2b on the Nestin+DCX− vs Nestin+DCX+ axis.

Consequences for the KB:

- The defining_markers field for dg_type2a_progenitor (Nestin+, Sox2+) is
  supported primarily by a single review (Micheli 2025). Any downstream
  confidence scoring should weight accordingly.
- The negative_markers field (DCX−, GFAP−) is not directly evidenced by any
  summary in this set; the DCX− status is inferred from the canonical DCX
  assignment to type-2b/neuroblast/immature stages (Merz 2013, Stepien 2021,
  Groen 2021). Expert review is required to confirm whether this inferential
  support is acceptable or whether primary literature specifically
  distinguishing type-2a DCX− from type-2b DCX+ should be added to the
  discovery set.
- No summary in this set addresses the "non-radial, horizontally oriented"
  morphology detail of the node context. This is a concrete morphology_notes
  gap that would benefit from targeted retrieval (e.g., Filippov/Fukuda/
  Kronenberg/Kempermann primary literature).
- No summary addresses anatomical_location for type-2a specifically (SGZ
  location is only implied).
- The node context states "No synaptic integration" for type-2a; no
  ephys/electrophysiology_class evidence is appropriate and none was proposed.

## Provenance and next steps

- All snippets are verbatim substrings of the `quotes` field for their source
  summary; snippet selection was guided by relevance to Nestin+/Sox2+/DCX−
  amplifying progenitor identity rather than to downstream neuroblast/immature
  content.
- Items are PROPOSED; expert curator must review each for:
  - Appropriateness of target_field assignment.
  - Adequacy of the SUPPORT/PARTIAL designation (especially the 10 PARTIAL
    items, which a curator may prefer to reclassify as out-of-scope rather
    than as weak evidence for type-2a).
  - Whether the inferred DCX−/GFAP− negative_markers support is acceptable
    without a primary source that directly reports it.
- Recommended follow-up retrieval for type-2a-specific primary sources:
  Kempermann 2004, Filippov 2003, Fukuda 2003, Kronenberg 2003 — all
  commonly cited for the 2a/2b distinction and not represented in this
  summary set.
