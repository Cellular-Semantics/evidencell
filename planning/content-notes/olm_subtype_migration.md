# OLM subtype migration — post-#37 curation task

**Depends on:** [#37](https://github.com/Cellular-Semantics/evidencell/issues/37) landing
(`proposed_subtypes[]` on `CellTypeNode`, `marker_role` or `subtype_markers` field)

**Companion to:** `planning/content-notes/olm_definition_history.md`

Once #37 is implemented, the OLM KB needs a targeted curation pass to migrate
subtype information currently held in free-text notes and planning files into
the new structured schema slots. This file tracks what needs moving and where
it currently lives.

---

## What needs to migrate

### 1. `proposed_subtypes[]` on `olm_hippocampus` node

Two subtypes to add (both from Chamberland 2024, PMID:38640347):

| Subtype id | Name | Key markers | Source | Candidate atlas node |
|---|---|---|---|---|
| `olm_chrna2` | Chrna2-OLM | Sst+, Chrna2+ | Leão 2012, Chamberland 2024 | CS20230722_CLUS_0771 (Harris+Chamberland AT F1=0.65) |
| `olm_ndnf` | Ndnf::Nkx2-1-OLM | Sst+, Ndnf+ | Chamberland 2024 | unresolved (AT signal unclear; see AT run README) |

Winterer 2019 subtypes (operational, not transcriptomic):

| Subtype id | Name | Cre line | Notes |
|---|---|---|---|
| `olm_sst_cre` | Sst-Cre-OLM | Sst-Cre | Likely overlaps Chrna2-OLM; Chrna2 detection 26% |
| `olm_htr3a_cre` | Htr3a-Cre-OLM | Htr3a-Cre | Possibly POA origin; Chrna2 detection 43%; may overlap Ndnf-OLM |

The Winterer Cre-line subtypes and Chamberland transcriptomic subtypes are not 1:1
equivalents and should probably be cross-referenced in subtype notes rather than
collapsed. The Winterer AT run combined both subtypes — a split-by-Cre-line re-run
is a proposed experiment on the CLUS_0771 edge.

### 2. `Chrna2` demotion from `defining_markers`

Current state: Chrna2 is in `defining_markers` on `olm_hippocampus` (Leão 2012,
Nichol 2018, Thulin 2025 citations). Under the adopted definition (2) (Sst-multimodal),
Chrna2 is a subtype marker for Chrna2-OLM, not a type-level defining marker.

Action: move Chrna2 sources to `proposed_subtypes[olm_chrna2].subtype_markers[]`.
Retain Sst and Grm1 as type-level defining markers.

Requires `marker_role` extension or new `subtype_markers` field (part of #37 scope).

### 3. Per-subtype Chrna2 detection rates

Currently in: `hippocampus_OLM.yaml`, `defining_markers[Chrna2].sources[].notes`
> "Htr3a-OLM 43% vs Sst-OLM 26%. Consistent with scattered Chrna2 at Sst Gaba_3
> supertype level in WMBv1."

Migrate to: `proposed_subtypes[olm_chrna2].notes` or as a `PropertySource` on the
subtype's Chrna2 marker entry (whichever the #37 schema supports).

### 4. Ndnf tension with existing negative_markers

The Winterer enrichment notes added Ndnf as a **negative marker** on `olm_hippocampus`
(from the Sst-Cre-OLM characterisation in GSE124847). Chamberland 2024 defines
Ndnf::Nkx2-1-OLM as an OLM subtype that IS Ndnf+.

These are not contradictory if Ndnf-negative applies to Sst-Cre-enriched cells only.
Resolution: Ndnf negative marker should gain a scope qualifier ("Sst-Cre-OLM subset")
and a cross-reference to the Ndnf-OLM proposed subtype. The contradiction should be
surfaced explicitly, not silently inherited.

See also: `kb/annotation_transfer_runs/at_run_20260506_harris_chamberland_mmc_wmbv1/README.md`
§ Caveats — Ndnf::Nkx2-1-OLM is honest-negative in the Harris+Chamberland AT run.

### 5. Thulin 2025 three-subcluster structure

Currently in: `olm_hippocampus.notes` (free text)
> "Thulin et al. (2025) identify three Sst/Pnoc subclusters with differential
> dorsal-ventral connectivity."

Action: once `proposed_subtypes[]` exists, evaluate whether the Thulin subclusters
(PMID:40757734) warrant additional entries or are better held as `notes` on the
`olm_chrna2` subtype (Pnoc is enriched in the Chrna2-OLM fraction per the AT run).

### 6. Edge caveat reframing (already partially done in current map-cell-type re-run)

After #37 lands and proposed_subtypes are populated, review all edges in
`hippocampus_OLM.yaml` where Chrna2-DISCORDANT caveats were reframed as
"not Chrna2-OLM, Sst-OLM not excluded". These can be tightened to reference
the specific subtype id (e.g. `not olm_chrna2; candidate for olm_ndnf`).

---

## Sources to mine (content currently in non-YAML locations)

| Location | What it contains | Priority |
|---|---|---|
| `planning/content-notes/olm_definition_history.md` | Three-definitions framing, subtype implications | HIGH — primary reference |
| `planning/content-notes/winterer_enrichment_notes.md` | Sst-Cre vs Htr3a-Cre subtype data, per-subtype Chrna2 rates | HIGH |
| `kb/annotation_transfer_runs/at_run_20260506_harris_chamberland_mmc_wmbv1/README.md` | Chamberland four-subfamily AT results, Ndnf honest-negative | HIGH |
| `kb/annotation_transfer_runs/at_run_20260506_harris_chamberland_mmc_wmbv1/manifest.yaml` | Per-cluster F1 headline results | HIGH |
| `hippocampus_OLM.yaml` edge caveats | Subtype framing in existing DISCORDANT notes | MEDIUM — review in-place |
| `hippocampus_OLM.yaml` olm_hippocampus.notes | Heterogeneity paragraph | MEDIUM |

---

## Sequencing

1. **#37 lands** — schema adds `proposed_subtypes[]` and marker_role or subtype_markers
2. **Run this migration pass** — populate proposed_subtypes on olm_hippocampus;
   demote Chrna2; resolve Ndnf tension; tighten edge caveats
3. **Re-run gen-report for OLM** — the report Introduction should surface both subtypes
   once the schema slot is populated (requires gen-report.md update, per paper-style
   reports addendum §6.1 pattern)
4. **Consider split Winterer AT run** — Sst-Cre cells vs Htr3a-Cre cells separately
   against WMBv1; this is a proposed experiment already on the CLUS_0771 edge and
   would directly test the mixed-signal hypothesis
