# Chamberland 2024 subfamily nodes — merge into general hippocampus GABAergic graph

## What landed (2026-05-12, Phase 2 C3)

`kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml` was
created as a *separate* graph containing four Chamberland 2024
functional Sst-IN subfamily nodes + their WMBv1 mapping edges:

- `chrna2_olm_subfamily_chamberland` → CLUS_0771 (F1 0.65)
- `ndnf_nkx2_1_olm_subfamily_chamberland` → SUPT_0216 (LOW, fragmented)
- `sst_nos1_subfamily_chamberland` → CLUS_0859 Sst Chodl Gaba_4 (F1 0.97)
- `sst_tac1_subfamily_chamberland` → SUBC_052 Pvalb Gaba (F1 0.58)

AT evidence cites
`at_run_20260512_chamberland_subfamily_mmc_wmbv1`.

## Why this is a stop-gap, not the final shape

The Chamberland subfamilies overlap heavily with **existing
classical types** in
`kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`:

| Chamberland subfamily | Likely classical counterpart |
|---|---|
| Chrna2-IN | `olm_cell_ca1` (Chrna2-Cre is the canonical OLM marker) |
| Ndnf::Nkx2-1-IN | `olm_cell_ca1` or `oriens_oriens_cell_hippocampus` (OLM-like targeting CA1 pyramidals) |
| Sst::Nos1-IN (long-range) | `hippocampo_septal_cell_ca1`, `lth_cell_hippocampus` (long-range Sst types) |
| Sst::Tac1-IN (bistratified-like) | `bistratified_cell_hippocampus` (Sst-positive bistratified) |

Putting these in a separate graph forces cross-graph reasoning to
state the (subfamily ↔ classical-type) relationship. Users (you)
have expressed preference to **merge into the general hippocampus
graph** so that:

1. Cross-mapping edges between Chamberland subfamilies and the
   morphologically-defined classical types can be expressed as
   normal `MappingEdge` entries (both nodes in the same graph).
2. The graph file becomes the single discoverable place for
   "hippocampal GABAergic cell types" rather than a scatter of
   per-source graphs.
3. The query / reporting code that walks one graph at a time
   captures the full local cell-type lattice without needing a
   cross-graph join layer.

## Proposed merge

1. Move the four Chamberland subfamily nodes (and the WMBv1 atlas
   stubs they reference) into
   `kb/graphs/hippocampus/hippocampus_GABAergic_interneurons.yaml`.
2. Add MappingEdge entries linking each Chamberland subfamily to its
   classical counterpart(s):
   - `chrna2_olm_subfamily_chamberland` ↔ `olm_cell_ca1` —
     relationship `BROAD_MATCH` (Chrna2-IN is a subset of canonical
     OLM defined by Chrna2-Cre intersection); evidence
     ATLAS_METADATA + Chamberland 2024 quote.
   - `ndnf_nkx2_1_olm_subfamily_chamberland` ↔ `olm_cell_ca1` —
     relationship `BROAD_MATCH` or `PARTIAL_OVERLAP`
     (Ndnf::Nkx2-1-IN is OLM-like; weak transcriptomic mapping).
   - `sst_nos1_subfamily_chamberland` ↔ `hippocampo_septal_cell_ca1`
     and/or `lth_cell_hippocampus` — relationship `EQUIVALENT` or
     `PARTIAL_OVERLAP` depending on how Sst::Nos1 maps to back-
     projection vs theta-rhythmically-firing long-range types.
   - `sst_tac1_subfamily_chamberland` ↔ `bistratified_cell_hippocampus`
     — relationship `PARTIAL_OVERLAP` (Sst::Tac1 targets fast-spiking
     interneurons; bistratified targets pyramidal dendrites in both
     SO and SR — overlap is partial, Chamberland's intersection
     captures a functional subset).
3. Migrate the 4 AT-evidence edges (Chrna2 → CLUS_0771, etc.) into
   the merged graph too — they're already referenced by accession
   so the move is mechanical.
4. Delete `kb/graphs/hippocampus/hippocampus_chamberland_subfamilies.yaml`
   after the merge.

## Open questions to resolve at merge time

- **Naming.** Keep the verbose `*_chamberland_subfamily_*` ids, or
  shorten? They need to stay unique within the merged graph but
  shouldn't be ugly.
- **Anatomy.** Currently all four subfamily nodes set
  `name_in_source: "CA1 stratum oriens"` for UBERON resolution
  reasons (audit preflight expects an MBA-resolvable name).
  Chamberland 2024 actually localises Chrna2 and Ndnf::Nkx2-1
  deeper in O/A than Sst::Tac1 (quote `269246896_1b1ebab4`).
  Express the depth difference via `name_in_source` synonyms,
  per-compartment annotation, or a `notes` field on each node?
- **CL terms.** None of the four subfamilies have a CL term yet.
  Chrna2-OLM, Ndnf-OLM, and the long-range Sst types might warrant
  CL new-term requests; the Sst::Tac1 ↔ bistratified mapping might
  resolve to an existing CL term. Use `cl-term-request` workflow.

## Tags

`#chamberland2024` `#hippocampus` `#graph-merge` `#follow-up-from-phase2-c3`
