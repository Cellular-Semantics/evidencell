# Retiring the reference-store compat shim

**Status:** open — shim landed with the papers/ + quotes/ split
**Owner:** unassigned
**Created:** 2026-10-18

The split from `references/{region}/references.json` to `papers/` + `quotes/`
shipped behind a compatibility shim so the change could land without touching
every consumer in one PR. This is the plan to remove it. It exists because a
shim with no removal plan is just a second layout maintained forever.

---

## What the shim is

Three functions in `src/evidencell/references.py` accept the *old* path
(`references/{region}/references.json`) and transparently serve the *new*
layout:

| Function | What it hides |
|---|---|
| `load_store(refs_path)` | Reads either layout, returns the legacy single-dict shape |
| `store_exists(refs_path)` | True for either layout — replaces bare `refs_path.exists()` |
| `write_quote_to_refs(refs_path, …)` | Routes to `save_paper()` + `append_quote()` when split |

`load_store()` reassembles the monolith's exact in-memory shape
(`{corpus_id: {...paper..., "quotes": {...}}}`), so every reader kept working
unchanged. That reassembly is the cost: each call globs and parses the whole
region. Fine at 270 papers; it is the thing to delete, not to optimise.

**`store_exists()` is load-bearing beyond convenience.** Every provenance check
returns `[]` when the store is missing, so a bare `refs_path.exists()` against
the split layout silently disables the entire anti-hallucination guard for the
region. Any new reader must use `store_exists()`, never `Path.exists()`.

---

## Work list

Consumers that still think in terms of `references.json`. Each line is one
change: take the region directory, use the narrow accessor, drop the
legacy-path round trip.

### Code — must change

| File | Current | Target |
|---|---|---|
| `src/evidencell/validate.py` | `load_store(refs_path)` in 4 checks | take a region dir; for quote-key checks read only `quotes/{cid}.json` |
| `src/evidencell/render.py` | `load_store()` for the whole region | needs identity for citation rendering + quotes for blockquotes — likely the last to migrate |
| `src/evidencell/qc_content.py` | `load_store()` per store | read `papers/` for identity checks, `quotes/` for integrity |
| `src/evidencell/fetch.py` | `load_store()` to build the resolver index | read `papers/` only — it never needs quote text |
| `src/evidencell/paths.py` | `refs_path_for_graph/region` return `…/references.json` | return the region **directory** |
| `.claude/hooks/validate_mapping_hook.py` | builds a store-shaped view from the written file | already file-scoped; drop the legacy-monolith branch |

`fetch.py` is the easiest and most valuable first move: it reads 270 identity
records to answer "what PMID is this corpus ID", and currently parses every
quote in the repo to do it.

### Docs — must change

`workflows/asta-report-ingest.md`, `evidence-extraction.md`, `survey.md`,
`map-cell-type.md`, `gen-report.md` all reference `references.json` by name.
These are agent-facing instructions, so a stale path here produces confidently
wrong behaviour rather than an error. **Update these in the same PR as
`paths.py`.**

### Tests

`test_references.py`, `test_validate.py`, `test_paths.py`, `test_render.py`,
`test_hook_integration.py`, `test_qc_content.py`, `test_fetch.py`,
`test_reference_store_integrity.py` construct `references.json` fixtures.
Convert to split-layout fixtures as each consumer migrates; keep **at least
one** legacy-layout test until the shim is deleted, so dual-layout reading stays
covered while it still exists.

---

## Sequence

1. `fetch.py` → `papers/` only. Smallest, no quote access, immediate win.
2. `qc_content.py` and `validate.py` → narrow accessors. Both are already
   file-scoped in spirit.
3. `paths.py` → return region directories, **with** the workflow docs.
4. `render.py` → last; it is the heaviest consumer and the one with real
   rendering behaviour riding on it (`author_keys`, `#119`).
5. Delete `load_store()`'s legacy branch, `write_quote_to_refs()`, and
   `is_split_layout()`. `store_exists()` survives as a plain directory check.

---

## Done when

- [ ] No module outside `references.py` names `references.json`
- [ ] No caller passes a `…/references.json` path
- [ ] `write_quote_to_refs()` deleted; callers use `save_paper()` / `append_quote()`
- [ ] `load_store()` either deleted or reduced to the split layout with no
      monolith branch
- [ ] Workflow docs describe `papers/` + `quotes/`
- [ ] A fresh clone has no `references.json` anywhere

## Guardrails while the shim exists

- **New code must not call `write_quote_to_refs()`** — use `save_paper()` /
  `append_quote()`. The shim is for existing callers only.
- **Never use `refs_path.exists()`** to test for a store (see above).
- `quote_key` format is unchanged and must stay unchanged. Keys are live in KB
  YAML and reports; changing the format turns a file reorganisation into a
  corpus-wide content migration.
