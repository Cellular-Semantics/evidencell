# Reference resolution report — hypothalamus 20261127 report ingest

## Tool substitution note

`mcp__Asta_semanticscholar__*` MCP tools were unavailable in this environment
(confirmed by the orchestrator before dispatch). All corpus ID resolution below
used the CLI fallback `just fetch-reference --json CorpusId:NNN ...`
(`src/evidencell/fetch.py`), which resolves offline-first against
`references/**/papers/*.json` and `research/**/paper_catalogue*.json`, falling
back to the keyless Semantic Scholar batch API for anything not already known
locally. Author lists are not returned by this tool (the `Resolution`
dataclass carries only `pmid`/`doi`/`title`/`year`/`source`), so full author
names for papers newly entering the hypothalamus store were obtained from
Europe PMC (`mcp__artl-mcp__get_europepmc_paper_by_id`, keyed by the PMID or
DOI the fetch tool returned) and normalised to `"First Last"` strings — the
canonical shape `references._normalise_authors()` expects.

## Resolution summary

- Total references in `reference_list.json`: **28**
- Resolved via `just fetch-reference` (PMID and/or DOI confirmed): **28/28**
- `resolution_confidence`: **HIGH: 28**, MODERATE: 0, UNRESOLVED: 0

The Semantic Scholar keyless API is heavily rate-limited and returned
transient failures (429s) on a majority-first pass; every corpus ID was
retried individually (up to 6 attempts, 3s backoff) and all 28 eventually
resolved with either a PMID or a DOI. No reference needed the PMID-verification
fallback (`--verify-pmid`), and no identifier was guessed from memory.

## Matching corpus IDs to author_keys

Matching was done on title (case-sensitive where it disambiguated) + year,
since `just fetch-reference` does not return author surnames. Two pairs of
author_keys in `reference_list.json` share an identical-looking title and
needed individual judgement:

- **`Massa et al., 2023`** (Title Case: "Feeding Neurons Integrate Metabolic
  and Reproductive States in Mice") and **`Massa et al._1, 2023`** (lowercase:
  "Feeding neurons integrate metabolic and reproductive states in mice") are
  two genuinely distinct Europe PMC/PubMed records: the bioRxiv preprint
  (corpus `263827506`, PMID 36747631, DOI `10.1101/2023.01.25.525595`) and its
  published iScience version (corpus `256305361`, PMID 37817932, DOI
  `10.1016/j.isci.2023.107918`, "Update of" the preprint per Europe PMC's
  `commentCorrectionList`). Matched on exact title casing, each kept as its
  own paper record.
- **`Sokolowski et al., 2016`** and **`Sokolowski et al._1, 2016`** share an
  *exactly identical* title string and year. Resolution to corpus `9550590`
  (PMID 27209204) and `255977286` (no PMID) returned the **same DOI**
  (`10.1186/s13064-016-0067-9`) — i.e. these are two duplicate Semantic
  Scholar records for one physical paper (the scenario `fetch.py`'s docstring
  explicitly calls out: "S2 can hold more than one record for the same paper
  ... Prefer the record carrying the PubMed crosslink."). Both author_keys
  were therefore consolidated onto the single canonical PMID-bearing record,
  corpus `9550590` — avoiding a duplicate `papers/9550590.json` /
  `papers/255977286.json` pair for the same publication. All 8 quotes
  attributed to either author_key were written against corpus `9550590`.

No corpus ID failed to match an author_key, so there are **no
`extra_references`** (inline citations without an evidence-section author_key)
from this run.

## Reference store merge

27 distinct corpus IDs were written via `evidencell.references.write_quote_to_refs`
(28 author_keys map onto 27 corpus IDs because of the Sokolowski consolidation
above). 5 of those corpus IDs already existed in `references/hypothalamus/papers/`
from prior ingests (`27794167` Correa 2014, `204741414` Kim 2019, `233329194`
Affinati 2021, `246907354` Naito 2022, `255457408` Lopez-Gonzalez 2023) —
their titles were sanity-checked against the expected `reference_list.json`
titles before merging and matched; `paper_meta` for these was passed but
ignored per the write-once identity rule. The remaining 22 corpus IDs were new
to the store and had full `paper_meta` (including authors, from Europe PMC)
attached at creation.

- Quotes merged: **97 total** passed to `write_quote_to_refs`
  (**45 new**, **52 deduplicated** — already present, idempotent no-ops).
  The high dedup count reflects both repeat citations of the same passage
  across different report sections (quote_key hashes text only, not section)
  and prior partial ingest activity already present in the store.
- `just qc-content` was run after the merge: `references/hypothalamus` reports
  **0 error, 0 warn** (60 informational gaps, e.g. missing `source_document`
  on ASTA_REPORT quotes — expected and non-blocking). No new errors were
  introduced anywhere in the sweep by this merge.

See `run_quotes.json` for the per-quote record (quote_key, corpus_id, ref,
author_key, section, text) covering all 97 quotes processed this run.
