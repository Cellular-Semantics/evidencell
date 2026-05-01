# Dev request: Ingest Zhuang ABCA spatial counts into brain_cell_KG

**Date:** 2026-04-30
**Blocked step:** Mapping decisions for low-MERFISH-coverage clusters in `workflows/map-cell-type.md` (in particular the `arpv_kiss` → `CS20230722_CLUS_1915` line of work, where Yao MERFISH gives only 5 cells / 3 regions for the candidate cluster — too sparse for a confident region-based call).
**Severity:** Medium — unblocks per-cluster region-distribution evidence for any cluster with sparse Yao MERFISH coverage, which is a meaningful fraction of the WMBv1 taxonomy (especially rare hypothalamic / preoptic / brainstem types).
**Owner of upstream change:** brain_cell_KG team (this is a KG ingest, not an evidencell code change).

---

## What is missing

The KG currently exposes one `obsolete_some_soma_located_in` edge per
(WMB cluster, MBA region) pair, populated from the **Yao 2024 MERFISH
summary**. There is no second source of per-cluster spatial counts. For
clusters with low Yao MERFISH coverage we have no fallback.

The Zhuang lab's MERFISH atlas (joint with Zeng/Yao 2024, released as
Zhuang-ABCA-1..4 on the Allen Brain Cell Atlas portal) provides an
independent set of cells assigned to the *same* WMBv1 clusters, and on a
finer parcellation. For at least one cluster we've spot-checked:

| Cluster | Yao MERFISH cells | Zhuang cells | Yao regions | Zhuang regions (specific) |
|---|---:|---:|---:|---:|
| CS20230722_CLUS_1915 (PVpo-VMPO-MPN Hmx2 Gaba_5) | 5 | 225 | 3 | 5 specific + edge artefacts |

Zhuang adds biologically meaningful regions Yao didn't catch (e.g. **MPN**
26 cells, **PS** 1 cell), and reinforces existing ones by 100× (PVpo: 1 → 135).

## What needs to change (in brain_cell_KG)

Ingest Zhuang-ABCA-1..4 spatial data the same way Yao MERFISH was ingested:
add `obsolete_some_soma_located_in` edges from `(WMB:cluster)` to `(MBA:region)`
with per-edge counts, **plus a source attribution property** so the two
sources stay distinguishable.

### Proposed edge shape

```
(node:Individual {curie: "WMB:CS20230722_CLUS_1915"})
  -[r:obsolete_some_soma_located_in {
      cell_count: 135,
      cell_ratio: 0.6,                        // cells in this region / total cells of this cluster in this dataset
      source_dataset: "Zhuang-ABCA-1",        // or "Yao-MERFISH" for existing edges
      parcellation_release: "Allen-CCF-2020/20230630",
      source_doi: "10.1038/s41586-023-06808-9"  // confirm with Zhuang team
  }]->
(anat:Multicellular_anatomical_structure {curie: "MBA:133"})
```

Key requirements:

- **Multi-edge per (cluster, region) pair.** A cluster + region can have
  one edge from Yao and one from each Zhuang dataset. Don't union them
  upstream — keep attributable.
- **Backfill `source_dataset` on existing Yao edges** (e.g.
  `source_dataset: "Yao-MERFISH"`) so consumers can filter / weight.
- **Drop unassigned cells before counting.** Zhuang `parcellation_index = 0`
  is unassigned; it should not produce an edge. Substructures whose name
  contains "unassigned" or whose parent is `fiber tracts` / ventricular
  systems are coordinate-boundary artefacts (~25% of Zhuang cells in our
  spot check) — recommend filtering at ingest time, but at minimum tag them
  so downstream can ignore.
- **One `cell_ratio` per source per cluster.** Compute as
  `count / total_cells_for_cluster_in_dataset` so Zhuang ratios are
  comparable across datasets but not directly to Yao.

### What evidencell needs after the KG change

Minimal:

- `inputs/taxonomies/CCN20230722.cypher` — extend the anat collect to
  capture `r.source_dataset` (and optionally `r.parcellation_release`,
  `r.source_doi`):
  ```cypher
  collect({cell_count: r.cell_count, cell_ratio: r.obsolete_cell_ratio,
           anat_label: anat.label, anat_id: anat.curie,
           source_dataset: r.source_dataset}) AS anat
  ```
- `src/evidencell/taxonomy_db.py` — extend `_extract_node` anat block to
  pass `source_dataset` through to `AnatomicalLocation.sources[].method`
  (or a similar slot). The schema already supports per-source attribution
  on `AnatomicalLocation` via the `sources` list — no schema change needed.
- Reingest: `just reingest CCN20230722 inputs/taxonomies/CCN20230722.json`
  (the recently-merged work on the `cell_counts` branch already preserves
  enrichments and refreshes `anatomical_location[]` from KG).

Reports and `find_candidates` queries that read `anatomical_location[]`
will see all sources and can weight or display them as needed; no caller
change strictly required.

## What was tried

Streaming spike, no abc_atlas_access library required (everything is CSV
on `https://allen-brain-cell-atlas.s3.us-west-2.amazonaws.com/`):

- Filter `Zhuang-ABCA-N/.../cell_metadata_with_cluster_annotation.csv` by
  `cluster` column starting with `"<cluster_number> "` — yields cell_label set.
- Look up `parcellation_index` per cell_label in
  `Zhuang-ABCA-N-CCF/.../ccf_coordinates.csv`.
- Resolve `parcellation_index → MBA: identifier` via Allen-CCF-2020
  parcellation lookup tables (small).

Full details (URLs, column schemas, join recipe, reference Python
implementation) in [`scratch/zhuang_spike/README.md`](../../scratch/zhuang_spike/README.md)
and [`scratch/zhuang_spike/spike.py`](../../scratch/zhuang_spike/spike.py).

The spike confirms the data is rich enough to be worth the upstream
ingest work. The numbers for CS20230722_CLUS_1915 are above; equivalent
boosts are expected for other low-MERFISH-coverage clusters in the
preoptic / brainstem / rare-NT subclasses.

## Proposed surface

| Layer | Change |
|---|---|
| brain_cell_KG ingest | Add Zhuang-ABCA-1..4 spatial CSVs as a parallel source to Yao MERFISH. Multi-edge per (cluster, region) with `source_dataset`, `parcellation_release`, `source_doi` properties. Backfill `source_dataset` on existing Yao edges. |
| `inputs/taxonomies/CCN20230722.cypher` | Extend anat collect to include `source_dataset`. |
| `src/evidencell/taxonomy_db.py` | Pass `source_dataset` through to `AnatomicalLocation.sources[].method` (or equivalent slot). |
| `kb/taxonomy/CCN20230722/*.yaml` | Refreshed via `just reingest`. No manual edits. |
| schema | No change. `AnatomicalLocation.sources[]` already supports per-source attribution. |
