# Resolution report — arc_aromatase (sexually_dimorphic)

Run: `20261125_sexually_dimorphic_report_ingest` / `arc_aromatase`

## Tool availability

`mcp__Asta_semanticscholar__*` tools were not available in this environment
(confirmed absent before starting). Used the CLI fallback instead:

- Corpus ID → pmid/doi/title/year: one batched `just fetch-reference
  CorpusId:<id> ... --json` call covering all 19 corpus IDs
  (`src/evidencell/fetch` — offline-first via references/research
  catalogues, falling back to the Semantic Scholar API for IDs not already
  known; 18/19 came back `"source": "api"`, 1 from `"source": "references"`).
- Full author lists: one `mcp__artl-mcp__get_europepmc_paper_by_id` call per
  PMID (19 calls; 3 needed a retry after an empty first response, which then
  returned the expected metadata). Author full names were built from each
  `authorList.author[].firstName` + `lastName`.

## Reference resolution

Total references in `reference_list.json`: **19**
Total corpus IDs in `pdf_corpus_ids.json`: **19**

| Confidence | Count |
|---|---|
| HIGH | 19 |
| MODERATE | 0 |
| UNRESOLVED | 0 |

All 19 corpus IDs resolved to exactly one `reference_list.json` author_key
each, matched on year + title (titles matched the fetched title verbatim or
near-verbatim — punctuation/em-dash differences only). No step 4 Europe PMC
title-search fallback was needed; `get_europepmc_paper_by_id` by PMID was
sufficient to confirm identity and pull full author lists for every
reference.

One cosmetic note: `reference_list.json`'s author_key `"C et al., 2019"`
(for PMID 31420539, "Single cell transcriptome analysis of developing
arcuate nucleus neurons uncovers their key developmental regulators") appears
to be a corrupted/truncated first-author surname from the source report —
the actual first author is Huisman (Huisman C, Cho H, Brock O, et al.). The
paper record was written with the correct `author_keys: ["Huisman et al.,
2019"]`; `run_quotes.json` below still carries the original `"C et al.,
2019"` string in its `author_key` field for traceability back to
`reference_list.json`/`extracted_quotes.json`.

### Extra references

None — all 19 corpus IDs matched a `reference_list.json` entry; none were
left over as `extra_references`.

## Quotes merged

- Quotes passed to `write_quote_to_refs()` this run: **91** (one call per
  `extracted_quotes.json` entry, several papers' quotes recur verbatim
  across multiple section labels in the source report).
- Unique quote_keys produced: **40** (content-hash dedup over the 91 calls:
  identical quote text under different section headers hashes to the same
  key, so the second+ call for that text was a no-op against the store).
- Of those 40, **0 were already present** in the store from the sibling
  `general_survey` run or any prior commit — confirmed by diffing against
  the papers/quotes files that existed before this run (3 papers — Lam et
  al. 2017 / corpus 13728181, Wartenberg et al. 2021 / corpus 237626479,
  Moffitt et al. 2018 / corpus 53566396 — were already present as paper
  records from the sibling run or an earlier commit, each carrying quotes
  from that prior ingest; this run added quotes alongside them without
  touching the pre-existing ones). All 40 unique quote_keys this run
  produced are new entries in `quotes/{corpus_id}.json`.
- So: **40 new** quotes merged, **51 deduplicated** (within-run,
  same-text-different-section repeats).
- 16 of the 19 papers were newly created `papers/{corpus_id}.json` records
  by this run; 3 (listed above) already existed.

## Files written

- `references/sexually_dimorphic/papers/{corpus_id}.json` — 16 new paper
  records (see list above for the 3 pre-existing ones this run added quotes
  to without touching their paper identity).
- `references/sexually_dimorphic/quotes/{corpus_id}.json` — 40 new quote
  records across 19 papers.
- `run_quotes.json` — 91 entries, one per `write_quote_to_refs()` call this
  run made (including the within-run duplicates, each still showing its
  resolved `quote_key`).
