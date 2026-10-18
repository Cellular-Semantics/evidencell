# Completing the reference-store refactor

The final round: retire the compatibility shim, and separate the QC baseline's
two populations. After this the publication-store refactor is done.

**Status:** open — shim landed with the papers/ + quotes/ split
**Owner:** unassigned
**Created:** 2026-10-18

The split from `references/{region}/references.json` to `papers/` + `quotes/`
shipped behind a compatibility shim so the change could land without touching
every consumer in one PR. Part 1 removes it — a shim with no removal plan is
just a second layout maintained forever.

Part 2 fixes something the split surfaced: the QC baseline now mixes a backlog
that should shrink with gaps that can never close, so its headline numbers no
longer mean what they appear to.

---

## Part 1 — retiring the shim

### What the shim is

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

### Work list

Consumers that still think in terms of `references.json`. Each line is one
change: take the region directory, use the narrow accessor, drop the
legacy-path round trip.

#### Code — must change

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

#### Docs — must change

`workflows/asta-report-ingest.md`, `evidence-extraction.md`, `survey.md`,
`map-cell-type.md`, `gen-report.md` all reference `references.json` by name.
These are agent-facing instructions, so a stale path here produces confidently
wrong behaviour rather than an error. **Update these in the same PR as
`paths.py`.**

#### Tests

`test_references.py`, `test_validate.py`, `test_paths.py`, `test_render.py`,
`test_hook_integration.py`, `test_qc_content.py`, `test_fetch.py`,
`test_reference_store_integrity.py` construct `references.json` fixtures.
Convert to split-layout fixtures as each consumer migrates; keep **at least
one** legacy-layout test until the shim is deleted, so dual-layout reading stays
covered while it still exists.

---

### Sequence

1. `fetch.py` → `papers/` only. Smallest, no quote access, immediate win.
2. `qc_content.py` and `validate.py` → narrow accessors. Both are already
   file-scoped in spirit.
3. `paths.py` → return region directories, **with** the workflow docs.
4. `render.py` → last; it is the heaviest consumer and the one with real
   rendering behaviour riding on it (`author_keys`, `#119`).
5. Delete `load_store()`'s legacy branch, `write_quote_to_refs()`, and
   `is_split_layout()`. `store_exists()` survives as a plain directory check.

---

### Done when

- [ ] No module outside `references.py` names `references.json`
- [ ] No caller passes a `…/references.json` path
- [ ] `write_quote_to_refs()` deleted; callers use `save_paper()` / `append_quote()`
- [ ] `load_store()` either deleted or reduced to the split layout with no
      monolith branch
- [ ] Workflow docs describe `papers/` + `quotes/`
- [ ] A fresh clone has no `references.json` anywhere

### Guardrails while the shim exists

- **New code must not call `write_quote_to_refs()`** — use `save_paper()` /
  `append_quote()`. The shim is for existing callers only.
- **Never use `refs_path.exists()`** to test for a store (see above).
- `quote_key` format is unchanged and must stay unchanged. Keys are live in KB
  YAML and reports; changing the format turns a file reorganisation into a
  corpus-wide content migration.


---

## Part 2 — split the QC baseline

`qc_content_baseline.json` currently holds 323 entries, and **241 of them can
never clear**: they are `source_document` warnings for ASTA reports that were
never committed to the repository. The remaining 82 are a genuine backlog that
should shrink to nothing.

| check | entries | clears? |
|---|---|---|
| `source_document` | **241** | **no** — the PDFs do not exist |
| `rationale_stale` | 41 | yes, on next `gen-report` |
| `source_method` | 22 | yes, curation |
| `markdown` | 8 | yes |
| `flat_citation` | 5 | yes |
| `no_refs_store` | 4 | yes, if those regions get stores |
| `run_ref` | 2 | yes (#89) |

### Why it matters

The baseline conflates *backlog that should shrink* with *accepted facts about
the world*. Three consequences:

- "0 new / 0 stale" stops being a progress signal, because 75% of the file is
  inert by construction.
- An 82-entry backlog is invisible inside a 323-line file, so nobody can tell
  at a glance whether the situation is improving.
- The stated goal — an empty baseline, at which point `--baseline` comes out of
  CI — becomes unreachable, which quietly makes the whole mechanism permanent.

### Two candidate shapes

1. **Collapse the finding.** Emit one `source_document` finding per *missing
   document* rather than per affected quote. 241 warnings become 1, and the
   `SourceDocument` record with `available: false` is already the place that
   fact is stated. Smallest change; keeps one file.

2. **Two files.** A shrinking `qc_content_baseline.json` and a separate
   `qc_known_gaps.json` for accepted-by-design absences, with the sweep
   reporting them in distinct lines. More machinery, but it makes the
   distinction explicit rather than implied.

Option 1 is probably sufficient and is strictly less code. Worth deciding on
the evidence at the time rather than now.

### Done when

- [ ] The baseline contains only findings that can actually be fixed
- [ ] Unrecoverable deepsearch documents are recorded once, not once per quote
- [ ] The sweep distinguishes "backlog remaining" from "known permanent gaps"
