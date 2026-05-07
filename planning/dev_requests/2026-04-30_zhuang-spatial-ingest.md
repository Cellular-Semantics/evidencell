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

## Status update — 2026-05-01

Zhuang-ABCA spatial counts are **already ingested in the KG** (resolved upstream
during the 2026-04 KG rebuild). The actual ingest shape is different from the
"multi-edge with `source_dataset` property" originally proposed below: edges
are **list-merged**, not multi-edged.

### Actual KG edge shape (verified 2026-05-01)

One `obsolete_some_soma_located_in` edge per (WMB cluster, MBA region) pair,
with three parallel lists carrying per-source contributions. Order is aligned
across the three lists — index `i` is one source's count + ratio + DOI:

```
(:Individual {curie: "WMB:CS20230722_CLUS_1915"})
  -[r:obsolete_some_soma_located_in {
      cell_count:           [1, 135],
      obsolete_cell_ratio:  [0.2, 0.6],
      source: ["https://doi.org/10.1038/s41586-023-06812-z",  // Zhuang 2023
               "https://doi.org/10.1038/s41586-023-06808-9"]  // Yao 2024
  }]->(:Multicellular_anatomical_structure {curie: "MBA:133"})
```

Single-source edges still wrap their values in length-1 lists. There are no
`source_dataset` / `parcellation_release` properties — only the bare DOI.
The list-merge is an artefact of the OWL-axiom → Neo4j translation in the KG
build, not a deliberate evidencell schema choice.

### evidencell handling — chosen approach

The evidencell schema and KB **do not mirror** the list-merged KG shape. Each
(cluster, region, source) tuple becomes its own `AnatomicalLocation` entry in
the taxonomy YAML, with a single `cell_count` and a single `PropertySource`
in `sources[]` carrying the DOI as `ref` and a method label derived from the
DOI ("MERFISH (Yao 2024)" / "MERFISH (Zhuang 2023)"). Same region therefore
appears multiple times under one node when multi-sourced. No schema change.

This is an explicit exception to the "no PropertySource on
ATLAS_TRANSCRIPTOMIC nodes" rule — multiple spatial studies contribute and
must stay attributable.

### Filtering caveats (still upstream KG-side)

- **Drop unassigned cells before counting.** Zhuang `parcellation_index = 0`
  is unassigned; it should not produce an edge. Substructures whose name
  contains "unassigned" or whose parent is `fiber tracts` / ventricular
  systems are coordinate-boundary artefacts (~25% of Zhuang cells in our
  spot check) — recommend filtering at ingest time, but at minimum tag them
  so downstream can ignore. evidencell trusts whatever the KG provides;
  if these reach the YAML they'll need a KG-side fix, not a downstream one.

### evidencell changes (landing on `at/zhuang-spatial-ingest`)

- `inputs/taxonomies/CCN20230722.cypher` — collect `r.source` alongside
  `r.cell_count` and `r.obsolete_cell_ratio`.
- `src/evidencell/taxonomy_db.py` — `_extract_node` expands the parallel
  count/ratio/source lists into one anat entry per source; the YAML emitter
  populates `AnatomicalLocation.sources[]` with a `PropertySource` per entry
  (`ref` = DOI, `method` from the `_SPATIAL_METHOD_BY_DOI` table).
- `tests/test_taxonomy_db.py` — adds `test_anat_multi_source_expansion`
  covering the merged-edge → per-source-AP transform.
- Reingest: `just reingest CCN20230722 inputs/taxonomies/CCN20230722.json`
  after a fresh `just fetch-taxonomy-kg` to pick up the new `source` field.
  Reingest preserves enrichments and refreshes `anatomical_location[]`.

Reports and `find_candidates` queries that read `anatomical_location[]`
will see one entry per source and can weight or display them as needed.
Callers that previously assumed one entry per region will now see
duplicates — verify before relying on count-by-region semantics.

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
| brain_cell_KG ingest | **Done upstream (2026-04 KG rebuild).** Spatial sources merged onto a single edge per (cluster, region) with parallel `cell_count` / `obsolete_cell_ratio` / `source` lists; `source` is the bare DOI. |
| `inputs/taxonomies/CCN20230722.cypher` | Anat collect extended to include `r.source`. |
| `src/evidencell/taxonomy_db.py` | `_extract_node` expands parallel lists into one entry per (region, source); YAML emitter populates `AnatomicalLocation.sources[]` with a single `PropertySource` per entry (`ref` = DOI, `method` from DOI lookup). |
| `kb/taxonomy/CCN20230722/*.yaml` | Refreshed via `just reingest`. No manual edits. |
| schema | No change. `AnatomicalLocation.sources[]` already supports per-source attribution. |
