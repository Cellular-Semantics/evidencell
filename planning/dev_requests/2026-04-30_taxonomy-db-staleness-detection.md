# Dev request: detect stale taxonomy DB during gen-facts / render

**Date:** 2026-04-30
**Status:** **CLOSED 2026-05-01** — landed on branch `regen-sexually-dimorphic-paper-style`. `taxonomy_db._SCHEMA_HASH` + `_meta.schema_hash` row at build time, `taxonomy_db.taxonomy_db_freshness(taxonomy_id)` and the path-explicit `_freshness_at(db_path, yaml_dir)`, render.py emits a single stderr WARNING per taxonomy_id per process when stale. Six unit tests cover fresh / missing-DB / missing-hash / hash-mismatch / yaml-newer / recovers-after-rebuild.
**Severity:** Medium — silent data dropping; user-discoverable only by spot-check.

---

## Problem

The cell-counts PR (#21) added `TaxonomyNode.n_cells`, ingested 10x per-node
counts from the rebuilt KG into `kb/taxonomy/{taxonomy_id}/cluster.yaml` etc.,
and updated `render._node_b_info` to populate `facts.edges[*].n_cells` from
the SQLite reference DB. The renderer's candidate-overview column was
renamed `Cells` → `Cells (10x)`.

But the SQLite DB at `kb/taxonomy/{taxonomy_id}/{taxonomy_id}.db` is built
once via `just build-taxonomy-db {id}` and not auto-refreshed when:
- the schema gains a new column (n_cells, future additions)
- the YAML files are re-ingested with new fields

The DB is gitignored; on a fresh checkout someone must rebuild manually. The
renderer's lookup is best-effort (intentional — supports test fixtures and
fresh checkouts) and falls back to None when the column doesn't exist.

**Observed failure mode:** all sexually_dimorphic reports rendered for weeks
showed `Cells = blank` (or stale "Cells (MERFISH)") with no error. The fix
was a one-line `just build-taxonomy-db CCN20230722`, but the staleness was
invisible until a curator noticed.

## Proposed fix

`taxonomy_db.py` should expose a freshness check. Two complementary surfaces:

1. **Hash-based:** at build time, write a sentinel record `_meta.schema_hash`
   into the DB (SHA of the schema's `nodes` CREATE TABLE statement). At
   query time, compare against the current schema. Mismatch → emit a warning
   + rebuild command.
2. **mtime-based:** compare DB mtime vs the newest `kb/taxonomy/{id}/*.yaml`
   mtime. Source-newer-than-DB → emit warning.

Wire into `render.py`'s TaxonomyDB cache opener:
- If freshness check fails, log a single `WARNING: taxonomy DB stale at
  {db_path}; run: just build-taxonomy-db {taxonomy_id}` to stderr at the
  start of `gen-facts` (once per render call, not per-edge).
- Don't auto-rebuild — explicit is better than implicit for KB integrity
  (DB rebuilds touch derived data and we want the curator to know it
  happened).

## Verification

- Add a `taxonomy_db.is_stale(taxonomy_id) -> tuple[bool, list[str]]`
  function returning (is_stale, reasons).
- Unit test against a fixture DB built with one schema then queried after a
  schema mtime change.
- Integration: rename `n_cells` to `n_cells_v2` in the schema; confirm
  next `gen-facts` warns about DB staleness; confirm rebuild fixes it.

## Out of scope

- Auto-rebuild on stale detection (deliberate).
- Cross-taxonomy freshness (single-taxonomy is enough for now).
- Hash of YAML contents (mtime is enough; cheap; mtime-equal-but-content-
  different is rare and harmless).
