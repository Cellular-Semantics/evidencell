# Minirefs author rendering — bug + fix plan

**Filed**: 2026-04-28
**Scope**: `#gen-report` · `#asta-ingest`
**Status**: Layers 1 + 3 (Option A) landed on branch `sexually_dimorophic_neurons`, 2026-04-28. Layer 2 deliberately skipped (anti-hallucination contamination rule prohibits direct references.json edits; Layer 1 produces correct output without one).

## Relationship to the broader references-store work

This is **the third instance of one underlying bug**: the
`asta-report-ingest` Step 2 subagent writes `references.json` entries directly
from a free-form prose prompt, without typed schemas or helper functions, so
field shapes drift from what the rest of the system expects.

Prior instances, captured in
[planning/asta_ingest_lessons_sexually_dimorphic.md](planning/asta_ingest_lessons_sexually_dimorphic.md):

| # | Field | Wrong shape | Expected | Detected by |
|---|---|---|---|---|
| §1 | `pmid` | `"PMID:29201072"` | bare digits `"29201072"` | KB validation hook (every PMID cite rejected) |
| §2 | `doi` | `"DOI:10.1007/..."` | bare path `"10.1007/..."` | latent — only avoided because all KB DOI refs used `https://doi.org/` form |
| §3 (new) | `authors` | comma-joined string with `et al.` suffix | `list[str]` of full names | renderer output (`"S et al. YYYY"` in minirefs) |

All three patched as one-off data fixes. None of them surfaced in tests
because the Step 2 writer has no schema validation on the way out and no
fixture coverage on the way in.

The relevant longer-term planning doc is
[planning/schema_self_contained_references.md](planning/schema_self_contained_references.md),
which proposes:

- Demote `references.json` to a research artifact under `research/{region}/`
  (Phase D).
- Move cited-paper metadata into an inline `PublicationReference` schema class
  on `CellTypeMappingGraph` (Phase A) — `authors: multivalued: true`, i.e.
  `list[str]`, schema-validated at write time.
- Read snippets from inline `evidence.snippet` rather than via `quote_key`
  → `references.json` lookup (Phase C).

If that migration lands, the renderer no longer reads `authors` from
`references.json` at all — it reads from a LinkML-validated
`PublicationReference` on the graph, where the wrong shape can't be written
in the first place. **Layer 1 of the fix below becomes moot post-migration;
Layers 2 and 3 are still needed because the bulk quote store survives in
`research/` and continues to be written by ASTA ingest.**

## Recommended ordering

1. **Layer 1 first** (defensive renderer) — small, recovers existing reports,
   no coupling to other work.
2. **Layer 3 next** (route ASTA-ingest writes through `references.py` helpers
   or a typed CLI) — addresses the class of bug, not just `authors`. This is
   the structural fix that should have happened after lesson §1; doing it now
   prevents instance §4.
3. **Layer 2** (one-shot data migration) — only useful for the existing
   sexually_dimorphic store. Optional if Layer 1 is in place and the data is
   small enough that re-rendering produces correct output anyway.
4. **Self-contained references migration** ([schema_self_contained_references.md](planning/schema_self_contained_references.md))
   — the structural endgame. Layer 3's typed writer plugs into Phase D's
   research-artifact bulk store unchanged.

Layers 1–3 should not block the schema migration and vice versa; they cost
about a day total and unblock current report rendering.

## Symptom

Recent `gen-report` outputs show citation tables with the author surname
collapsed to a single letter:

```
[1]  S et al. 2017   PMID:29201072   Soma location, Kiss1, Esr1
[2]  S et al. 2007   PMID:17213691   Soma location, Kiss1, Esr1, GnRH/LH surge
[3]  S et al. 2017   PMID:28660243   Soma location, NT type, Kiss1+Th, sex dimorphism
```

Same problem on the per-quote `— Author et al. YYYY` lines and on drill-down
report titles / filenames.

Confirmed in
[reports/sexually_dimorphic/avpv_kiss1_neuron_summary.md](reports/sexually_dimorphic/avpv_kiss1_neuron_summary.md)
and other 2026-04-25 sexually_dimorphic reports.

## Root cause

Two-part defect — bad data plus a renderer that doesn't validate its input.

### 1. `references.json` `authors` field type is inconsistent across regions

Authoritative shape (from
[src/evidencell/references.py:154](src/evidencell/references.py#L154) via
`_normalise_authors()`): `list[str]` of full names.

Observed:

| Region | `authors` type | Example |
|---|---|---|
| `references/hippocampus/references.json` | `list[str]` ✅ | `["Iris Oren", "Wiebke Nissen", "D. Kullmann", "P. Somogyi", "K. Lamsa"]` |
| `references/sexually_dimorphic/references.json` | `str` ❌ (all 46 entries) | `"Shannon B. Z. Stephens, Melvin L. Rouse, K. Tolson, R. Liaw, Ruby A Parra, Navi Chahal et al."` |

The sexually_dimorphic file was written by the resolution subagent step in
[workflows/asta-report-ingest.md](workflows/asta-report-ingest.md) (step 5,
"Merge into references/{region}/references.json"). The orchestrator instructs
the subagent to write entries directly without going through
`_build_paper_entry()` / `_normalise_authors()`. The subagent received author
lists from
`mcp__Asta_semanticscholar__get_paper_batch(fields="title,authors,year,externalIds")`
(which returns `[{authorId, name}, ...]`) and chose to flatten the list to a
comma-joined string with an `et al.` suffix when serialising.

### 2. Renderers index `authors[0]` without type checking

[src/evidencell/render.py](src/evidencell/render.py) treats `authors` as a list
in three places:

| Line | Use |
|---|---|
| [render.py:139–152](src/evidencell/render.py#L139-L152) | `_format_citation_line()` — minirefs table + `— Author et al. YYYY` lines |
| [render.py:932–941](src/evidencell/render.py#L932-L941) | drill-down `# Evidence Drill-down: …` heading |
| [render.py:1319–1322](src/evidencell/render.py#L1319-L1322) | drill-down output filename |

When `authors` is a string, `authors[0]` is the first character (`"S"`),
`.split()[-1]` returns `"S"`, and the citation collapses to `"S et al. YYYY"`.

`_normalise_authors()` itself has the same blind spot — its `for a in authors`
loop iterates characters when handed a string (each `isinstance(a, str)` is
true), so the resulting list would be a list of characters, not a single name.

## Fix plan

Three independent layers — each safe in isolation, all three desirable.

### Layer 1: harden the renderer (defensive read)

Add a single helper in `render.py`:

```python
def _coerce_authors(authors) -> list[str]:
    """Return a list of full-name strings regardless of input shape.
    Accepts: list[str], list[dict] (Semantic Scholar shape), comma-joined str,
    or empty/None. Strips a trailing ' et al.' / ' et al' if present on a
    string input."""
```

Call it at the three sites above. The string-input branch should split on
`,`, strip whitespace, and drop a trailing `et al.` token. This recovers
correct rendering for the existing sexually_dimorphic reports without any
data migration.

Keep behaviour identical for the canonical `list[str]` shape.

### Layer 2: normalise existing references.json files (data migration)

One-shot script (suggested location: `scripts/migrate_authors_field.py` or as
a `taxonomy_ops.py`-style subcommand) that:

1. Walks `references/*/references.json`.
2. For each entry whose `authors` is a string: splits on `,`, strips an
   `et al.` suffix, writes back as `list[str]`.
3. Skips entries already in canonical shape.
4. Updates `_meta.last_updated` / `last_updated_by`.

Audit-only first pass (`--dry-run`) before any write.

### Layer 3: prevent the bad shape from being written again

Two viable surfaces; pick one.

**Option A — fix the orchestrator prompt.** Update
[workflows/asta-report-ingest.md](workflows/asta-report-ingest.md) step 5
to spell out the `authors` field shape: `list[str]`, full names, no
`et al.` suffix. Show one good entry and one bad entry inline. Cheapest fix;
relies on the subagent following instructions.

**Option B — make the writer go through `_build_paper_entry()`.** Have the
subagent call a CLI (e.g. `just merge-references {payload.json}`) that uses
`references.py` helpers, so `_normalise_authors()` runs unconditionally.
Higher up-front cost but eliminates the class of bug for any future
references.json writer (cite-traverse, evidence-extraction, manual edits).

Recommendation: **Option B**, since a similar bug will recur on the next
free-form `references.json` write path otherwise. Option A as a stopgap if B
is not in scope this round.

While at this surface, also fix `_normalise_authors()` to accept a
comma-joined string (mirror the `_coerce_authors` rule from Layer 1) so the
helper is correct in isolation.

## Test coverage to add

- Unit test: `_coerce_authors()` over list[str], list[dict], string with
  `et al.` suffix, string without suffix, empty list, `None`.
- Unit test: `_format_citation_line()` produces `"Stephens et al. 2017 · PMID:…"`
  for a string-form `authors` entry (regression guard for Layer 1).
- Integration test: render a fixture node from a graph whose references.json
  has a string-form `authors` entry; assert no `"S et al."` in output.
- If Layer 2 migration script lands: a fixture references.json with mixed
  shapes; assert the script normalises in place idempotently.

## Out of scope

- Fixing the rendered reports themselves — once the renderer is fixed and the
  data is migrated, regenerating the reports via `gen-report` produces correct
  citations. No edits to existing `*_summary.md` / `*_facts.json` are needed.
- Author-name disambiguation, ORCID resolution, or "et al."-threshold tuning
  (currently 3+ authors → `Last et al.`).

## References

Code:
- [src/evidencell/render.py:139-158](src/evidencell/render.py#L139-L158) — `_format_citation_line()`
- [src/evidencell/render.py:925-943](src/evidencell/render.py#L925-L943) — drill-down heading
- [src/evidencell/references.py:121-170](src/evidencell/references.py#L121-L170) — `_build_paper_entry()` + `_normalise_authors()`
- [workflows/asta-report-ingest.md](workflows/asta-report-ingest.md) — step 5, references.json merge

Data examples:
- [reports/sexually_dimorphic/avpv_kiss1_neuron_summary.md](reports/sexually_dimorphic/avpv_kiss1_neuron_summary.md) — bad output
- [references/sexually_dimorphic/references.json](references/sexually_dimorphic/references.json) — bad data
- [references/hippocampus/references.json](references/hippocampus/references.json) — correct data

Related planning:
- [planning/asta_ingest_lessons_sexually_dimorphic.md](planning/asta_ingest_lessons_sexually_dimorphic.md) — §1 PMID prefix bug, §2 DOI prefix bug; same writer, same class of issue
- [planning/schema_self_contained_references.md](planning/schema_self_contained_references.md) — long-term plan that supersedes Layer 1 and reframes Layer 3 as the writer for a `research/`-tier bulk store
