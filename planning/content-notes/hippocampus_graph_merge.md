# Hippocampus graph merge plan

## Current state (2026-04-14)

Two draft graphs in `kb/draft/hippocampus/`:

| File | Classical types | Atlas stubs | Edges | Evidence depth |
|---|---|---|---|---|
| `hippocampus_OLM.yaml` | 1 (OLM) | 61 WMBv1 | Yes | Deep — cite-traverse + evidence extraction complete |
| `hippocampus_GABAergic_interneurons.yaml` | 15 GABAergic types | 0 | None | Shallow — ASTA report synthesis only, no primary lit verification |

## Overlap

OLM appears in both files:
- `hippocampus_OLM.yaml`: `olm_hippocampus` — fully researched, edges + evidence
- `hippocampus_GABAergic_interneurons.yaml`: `olm_cell_ca1` — stub from ASTA report

## Merge plan

Once the other classical types in `hippocampus_GABAergic_interneurons.yaml` gain edges
and evidence (via cite-traverse + evidence-extraction), merge both into a single
`hippocampus_WMBv1.yaml` (or keep the classical-type naming if atlas stubs move to a
separate reference DB per M8).

At merge time:
- Deduplicate OLM: keep the deeply researched version from `hippocampus_OLM.yaml`
- Reconcile node IDs (`olm_hippocampus` vs `olm_cell_ca1`)
- Merge atlas stubs (the 61 WMBv1 stubs serve all classical types in the region)
- Verify no duplicate edges

Not urgent — keep separate until at least 2-3 more types have edges.
