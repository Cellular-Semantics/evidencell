# Reference resolution report — sexually_dimorphic general_survey (2026-11-25)

**Tool availability note:** `mcp__Asta_semanticscholar__*` tools were not
available in this environment (confirmed absent, not merely still
connecting). Per the workflow's documented fallback, all 56 corpus IDs were
resolved with the CLI tool `just fetch-reference` (batched, `--json`), which
resolves offline-first via the local reference stores / paper catalogues and
falls back to the Semantic Scholar API, never guessing a PMID/DOI.

## Resolution summary

- Total references (author_keys in `reference_list.json`): 56
- Corpus IDs in `pdf_corpus_ids.json`: 56
- Resolved via `just fetch-reference`: 56 / 56
- HIGH confidence: 56
- MODERATE confidence: 0
- UNRESOLVED: 0

Every corpus ID matched exactly one `author_key` by year + first-author
surname (title strings from the resolver and from `reference_list.json` are
effectively identical for all 56, which made the match unambiguous).

### Duplicate-paper edge case: Morales-Delgado et al., 2013

`reference_list.json` contains two distinct author_keys for the same title —
"Regionalized differentiation of CRH, TRH, and GHRH peptidergic neurons in
the mouse hypothalamus" — `Morales-Delgado et al., 2013` and
`Morales-Delgado et al._1, 2013` (an artefact of the extraction step treating
two separate in-document citations of the same paper as two entries). The two
remaining unassigned corpus IDs, `9614413` and `253974358`, both resolved to
the **same DOI** (`10.1007/s00429-013-0554-2`), confirming they are two
different Semantic Scholar corpus records for one physical paper (a common
duplicate-indexing situation). Since the task's matching rule (year + first
author) does not disambiguate between them, they were assigned
deterministically: the PMID-bearing record (`9614413`, PMID 24337236) to the
plain `Morales-Delgado et al., 2013` key, and the DOI-only record
(`253974358`) to the `_1` key. Both are written to the store as **separate
paper records** (the store is keyed by corpus_id), so this paper now has two
`papers/*.json` entries for the same work — flagged here for a possible
future consolidation decision, not resolved further in this run.

### Papers with no PMID (DOI-only resolution)

Six papers resolved via DOI only (preprints / conference abstracts not yet
indexed with a PMID in Semantic Scholar or Europe PMC at reference-store
query time):

| corpus_id | author_key | DOI |
|---|---|---|
| 214721986 | Saucisse et al., 2020 | 10.1101/2020.03.25.007765 |
| 218608339 | Kim, 2020 | 10.1210/jendso/bvaa046.1237 |
| 218686941 | Mickelsen et al., 2020 | 10.1101/2020.05.14.096818 |
| 219535578 | Zhang et al., 2020 | 10.1101/2020.06.01.125054 |
| 253974358 | Morales-Delgado et al._1, 2013 | 10.1007/s00429-013-0554-2 |
| 255832704 | Wang et al., 2021 | 10.1186/s12915-021-00973-x |

These quotes carry `ref: "https://doi.org/<doi>"` in `run_quotes.json` and
cannot be cited by PMID in KB YAML (only by DOI, via whichever citation form
the schema accepts for DOI-only sources).

### Author metadata

`just fetch-reference` does not surface full author lists (only
pmid/doi/title/year/source). Full author name lists for all 56 `paper_meta`
records were obtained from Europe PMC (`EXT_ID:<pmid> AND SRC:MED` when a
PMID was available, else `DOI:<doi>`) — the same public, keyless service the
codebase's own `verify_pmid()` helper already uses, and a read-only lookup
that introduces no fabricated data. All 56 resolved on the first or second
attempt; none required a guess.

### extra_references

None. All 56 corpus IDs in `pdf_corpus_ids.json` matched an `author_key` in
`reference_list.json` 1:1 (after resolving the Morales-Delgado duplicate
above); there were no leftover inline-citation-only corpus IDs.

## Quotes merged

- Quotes passed to `write_quote_to_refs()`: 176 (one call per quote, across
  all 56 papers)
- New quote records: 98
- Deduplicated (identical quote already present from an earlier
  `sexually_dimorphic` ingest run): 78

The reference store already held 81 papers / quotes from two earlier runs
(`20260425_sexually_dimorphic_report_ingest`,
`20260911_sexually_dimorphic_report_ingest`). After this run:
`references/sexually_dimorphic/papers/` and `.../quotes/` each hold 134
entries (81 pre-existing + 53 newly created by this run; 3 of this run's 56
papers — corpus IDs 204741414, 218528429, 221402501 — already existed as
paper records from an earlier run, so only their `quotes/*.json` files grew).

`just qc-content` was run after the merge and reports **0 errors, 0
warnings** for `references/sexually_dimorphic` (56 informational "gap"
findings, all `source_document` — expected, since `write_quote_to_refs()`
does not take a `source_document` parameter and none of the other
`sexually_dimorphic` quotes from prior runs record one either). No write
dropped a paper or quote, edited a paper's identity, or produced a mismatched
quote key.

## Outputs

- `run_quotes.json` — 176 entries, one per quote written this run
  (`quote_key`, `corpus_id`, `ref`, `author_key`, `section`, `text`)
- Reference store updates: `references/sexually_dimorphic/papers/*.json`
  (53 new) and `references/sexually_dimorphic/quotes/*.json` (53 new + 3
  appended-to)
