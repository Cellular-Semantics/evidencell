# Reference resolution report — hypothalamus (20261127_hypothalamus_report_ingest)

## Tooling note

The `Asta_semanticscholar` MCP server was **not connected** in this session. The
documented CLI fallback was used instead:

1. `uv run python -m evidencell.fetch --json {corpus_ids...}` — batch-resolved all
   corpus IDs offline-first (references/ store → research/ catalogues → live
   Semantic Scholar API).
2. `mcp__artl-mcp__get_europepmc_paper_by_id` (Europe PMC) with each paper's PMID
   (or DOI when no PMID was available) — fetched full author lists.

The title-fragment search fallback (which depended on the unavailable Asta
search tool) was **skipped** this run, per the task's substitute-pipeline
instructions. It was not needed: all 19 corpus IDs resolved cleanly via step 1
and step 2 above.

## Resolution summary

- Total references in `reference_list.json`: **19**
- Resolved via `evidencell.fetch` (corpus ID → PMID/DOI/title/year): **19/19**
- Author lists fetched via artl-mcp / Europe PMC: **19/19**
- **HIGH** confidence (PMID or DOI + full author list): **19**
- **MODERATE**: 0
- **UNRESOLVED**: 0

Two papers are preprints with no PubMed record (DOI used as the identifier
instead of PMID):
- `Zhang et al., 2020` — corpus 219535578, bioRxiv DOI `10.1101/2020.06.01.125054`
  (published version exists, PMID 33887179, Cell Stem Cell 2021, but the
  ASTA-cited corpus ID is the preprint; PMID left blank per the preprint
  record actually in hand).
- `Locarno et al., 2026` — corpus 290474742, bioRxiv DOI `10.64898/2026.07.16.737908`.

All 19 corpus IDs matched 1:1 to the 19 `author_key` entries in
`reference_list.json` by year + first-author surname. No `extra_references`
(no corpus ID was left over after matching reference-list entries, and no
author_key in reference_list.json was left unmatched after the batch).

## Quote merge summary

- Quotes passed to `write_quote_to_refs()`: **52** (deduplicated from 132 raw
  entries in `extracted_quotes.json`, where the same quote text recurs under
  several different report-section buckets for a paper — one call was made
  per unique `(corpus_id, quote_text)` pair, using the first section label
  encountered for that text)
- New quote keys written this run: **52**
- Deduplicated against quotes already in the store: **0** (all 52 unique
  quotes were new to the store)
- Papers newly created in the store this run: **17**
- Papers already present in the store (quotes appended, identity untouched):
  **2** — `Romanov et al., 2020` (corpus 218528429) and `Lim et al., 2025`
  (corpus 276213069). Existing paper identity records matched the
  freshly-resolved metadata exactly; `paper_meta` was ignored for these two
  per the write-once identity contract.

See `run_quotes.json` for the full per-quote record (quote_key, corpus_id,
ref, author_key, section, text) and `references/hypothalamus/` for the
updated store.
