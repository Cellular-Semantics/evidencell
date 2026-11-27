# Reference resolution report — hypothalamus, 20261127_hypothalamus_report_ingest

## Method

The `Asta_semanticscholar` MCP server was unavailable in this session (no
tools exposed). Resolution was performed entirely via the `just
fetch-reference` CLI fallback, which resolves offline-first against
`references/**/papers/*.json` and falls back to the public Semantic Scholar
API. All 57 corpus IDs in `pdf_corpus_ids.json` resolved successfully: 6 from
the existing reference stores (`source: "references"`) and 51 from the
public S2 API (`source: "api"`). The raw output is
`fetch_reference_raw.json`.

Because the CLI path does not return full author lists, every paper record
written this run carries reduced identity metadata: `author_keys` (taken
directly from the matched `reference_list.json` entry) but `authors: []`
(no full author names). This is the degraded mode specified for this run,
not a data-quality defect.

Each of the 57 `author_key` entries in `reference_list.json` was matched to
a `corpus_id` in `fetch_reference_raw.json` by year + first-author surname
(parsed from the `author_key` string) and confirmed by title similarity.
All 57 matched cleanly as the same paper (title strings were effectively
identical, modulo Unicode punctuation normalisation such as curly quotes/
hyphens).

One pair of ambiguous duplicates: `Song et al., 2015` and `Song et al._1,
2015` share an identical title, year, and DOI
(`10.1186/s13041-015-0106-1` — "The role of orexin in post-stroke
inflammation, cognitive decline, and depression") but resolved to two
distinct corpus IDs (`16791178` and `255981136`) in `fetch_reference_raw.json`
— i.e. the ASTA report (or S2) produced two separate corpus records for what
is the same real paper. Title/year alone cannot disambiguate which corpus_id
belongs to which author_key suffix, so the two were assigned in the order
they appear in `pdf_corpus_ids.json` / `reference_list.json`
(`Song et al., 2015` → `16791178`, the one source `"references"` already
had; `Song et al._1, 2015` → `255981136`, from the API). This is a
pre-existing duplication in the input data, not something resolved further
here.

## Summary

- Total `author_key` entries in `reference_list.json`: **57**
- Total corpus IDs in `pdf_corpus_ids.json`: **57**
- Resolved: **57/57**
  - HIGH confidence: **57**
  - MODERATE confidence: **0**
  - UNRESOLVED: **0**
- Extra references (corpus_ids with no matching `author_key`, i.e. inline
  citations only): **0** — every corpus_id in `fetch_reference_raw.json` was
  consumed by a `reference_list.json` entry.
- Unresolved `author_key`s (no corpus_id match): **0**

## Quotes merged

- Total quote entries in `extracted_quotes.json` passed to
  `write_quote_to_refs()`: **142**
- New quotes written to the store this run: **113**
- Deduplicated (quote_key already present — either from a prior run/
  pre-existing store content, or a repeat passage inside this run's
  `extracted_quotes.json`, e.g. the same evidence sentence filed under both
  "Structure, location, and abundance" and "Markers and their
  anatomical/modal context" for the same paper): **29**
- New paper records created in `references/hypothalamus/papers/`: **54**.
  Only 3 of the 57 papers already had a file in `references/hypothalamus/
  papers/`: `10721050` (Mickelsen et al., 2017), `17964183` (Goforth et al.,
  2014), `195878681` (Schiffino et al., 2019). The other 3 of the 6 that
  resolved with `source: "references"` — `16724939` (Peyron et al., 1998),
  `49903082` (Giardino et al., 2018), `73728732` (Mickelsen et al., 2019) —
  were found by `fetch-reference`'s offline-first glob in *other* regions'
  stores (`references/thalamus/`, `references/sexually_dimorphic/`) and did
  not yet exist in `references/hypothalamus/`, so new paper records were
  created for them here.

All 142 quotes carry a non-null `ref`: 137 resolve to `PMID:<digits>`, 5
resolve to a DOI URL (no PMID available for these papers): `Cruz et al.,
2018`, `Devere et al., 2026`, `Pol, 1999`, `Reghunandanan, 2024`, `Song et
al._1, 2015`.

No quotes were left unmerged — every `author_key` in `extracted_quotes.json`
resolved to a corpus_id with HIGH confidence, so there is no "unresolved —
quotes not merged" section this run.

See `run_quotes.json` for the full per-quote mapping (quote_key, corpus_id,
ref, author_key, section, text).
