# Reference resolution report — sexually_dimorphic (2026-09-11)

Run ID: `20260911_sexually_dimorphic_report_ingest`

## Resolution summary

- Total author_keys in `reference_list.json`: 35
- Resolved via single `get_paper_batch` call (all 35 corpus IDs from `pdf_corpus_ids.json`): **35/35**
- HIGH confidence: 35
- MODERATE confidence: 0
- UNRESOLVED: 0

No fallback title/author search was needed — every corpus ID in `pdf_corpus_ids.json` matched
exactly one `author_key` in `reference_list.json` on year + first-author surname, and every
`author_key` found a match. There were no extra (inline-citation-only) corpus IDs left over.

## Quotes merged

- New quote entries added: 63
- Duplicates skipped (quote text already present): 11 — all under corpus ID `1832035`
  (Kim et al., 2013), which already existed in `references.json` from a prior ingest run
  and shared one anti-anxiety-focused source quote with this run's evidence extraction.
- Content-hashed quote keys (`{corpus_id}_{sha256[:8]}`) generated for every new quote;
  no key collisions encountered.

## Entries

- Pre-existing entries in `references/sexually_dimorphic/references.json`: 46
- New entries added: 34
- Total after merge: 80
- All 46 pre-existing `corpus_id` keys preserved (verified by set-containment check
  after write).

## Data-shape normalisation (pre-existing entries)

All 46 pre-existing entries in `references.json` were written in a non-conformant shape
by an earlier ingest run (see `planning/asta_ingest_lessons_sexually_dimorphic.md` §1-2
and `planning/minirefs_author_rendering_fix.md`):

- `authors` stored as a single comma-joined string with a trailing `et al.` (46/46 entries)
- `doi` stored with a `DOI:` prefix (46/46 entries)

Per the field-shape contract in this step, these 46 entries were normalised in place
during the merge (no quotes or corpus IDs were removed):

- `authors` → `list[str]` of full names (comma-split, trailing "et al." stripped)
- `doi` → bare path (leading `DOI:` prefix stripped)
- `pmid` already bare digits on all pre-existing entries (no change needed)

Post-write verification confirmed:
- File parses as valid JSON
- Zero entries have `authors` as a string
- Zero entries retain a `DOI:` or `PMID:` prefix
- All 46 pre-existing `corpus_id` keys still present

## Extra references (inline citations, not evidence-section papers)

None. All 35 corpus IDs in `pdf_corpus_ids.json` matched an `author_key` in
`reference_list.json`.

## Field shape used for new entries

Each new entry follows the step 5c1 contract exactly:

```json
{
  "corpus_id": "<digits-only>",
  "author_keys": ["Last et al., YYYY"],
  "title": "<paper title>",
  "year": <int>,
  "authors": ["First Author", "Second Author", ...],
  "pmid": "<digits-only>",
  "doi": "<bare path>",
  "resolution_confidence": "HIGH",
  "quotes": { "<corpus_id>_<hash>": { "text": ..., "section": ..., "claims": [], "source_method": "asta_report", "status": "pending", "added_by": "20260911_sexually_dimorphic_report_ingest" } }
}
```
