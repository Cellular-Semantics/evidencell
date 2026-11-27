# Reference resolution report — hypothalamus PVN CRH neuron report ingest

Run ID: `20261127_hypothalamus_report_ingest`
Region: `hypothalamus`
Reference store: `references/hypothalamus/`

**Environment note**: the `mcp__Asta_semanticscholar__*` MCP server was unavailable
in this environment (did not connect). All corpus-ID resolution went through the
CLI fallback (`just fetch-reference`, i.e. `evidencell.fetch`), which resolves
offline-first (validated reference stores, cached catalogues, then the Semantic
Scholar public API).

## Summary

- Total references (author_keys in `reference_list.json`): **55**
- Total corpus IDs (`pdf_corpus_ids.json`): **55**
- Resolution confidence: **HIGH: 54**, **MODERATE: 1**, **UNRESOLVED: 0**
- Extra references (inline citations without an evidence-section quote): **0**
  (every corpus ID matched exactly one `reference_list.json` author_key)
- Quotes merged: **99 new**, **12 deduplicated** (111 `write_quote_to_refs()`
  calls total — the extracted-quotes file repeats several quotes verbatim
  across multiple report sections; the store's idempotent append collapsed
  those repeats to their existing key)

## Resolution method

1. `just fetch-reference CorpusId:<id>` resolved **43 of 55** corpus IDs directly
   (most via the Semantic Scholar public API; five — `222410534`, `255832704`,
   `4940077`, `6175788`, `8197728` — were already present in another region's
   validated reference store and resolved from there).
2. The remaining **12** corpus IDs (`207377691`, `211122949`, `260146994`,
   `260348712`, `268520959`, `278260305`, `289414326`, `290696127`,
   `292113836`, `457737`, `52881652`, `6971171`) returned `UNRESOLVED (not
   found locally or via API)` from the CLI — confirmed on a second,
   rate-limit-spaced retry, so this is a genuine gap in the public API's
   corpus-ID index, not a transient 429.

   For these 12, per the task's step 4a, I located each corpus ID's actual
   hyperlink target in the source PDF (`inputs/deepsearch/PVN_CRH_neurons.pdf`)
   using its link annotations (`https://www.semanticscholar.org/p/<id>`) and
   the citation text immediately preceding each link — e.g. `CorpusId:457737`
   sits directly under the in-text citation `(Karsten et al., 2013)` /
   *"How Does a Neuron 'know' to Modulate Its Epigenetic Machinery..."*. This
   gave an unambiguous, non-guessed candidate title/author/year for each of
   the 12 still-unmatched `reference_list.json` entries. I then searched
   Europe PMC for that exact title to obtain a candidate PMID/DOI, and
   confirmed existence via `just fetch-reference --verify-pmid <pmid>` for
   the 11 that have a PMID (all confirmed; title, authors, and year matched
   exactly). The twelfth (`Ono et al., 2026`, corpus `290696127`) is a
   bioRxiv preprint with no PMID — confirmed instead by exact title/author/DOI
   match in Europe PMC's preprint (PPR) index, hence **MODERATE** rather than
   **HIGH** confidence.
3. The CLI's `fetch-reference` output does not include full author lists (only
   title/PMID/DOI/year), so full author names for all 54 newly-added papers
   were taken from Europe PMC (`get_europepmc_paper_by_id`, `result_type=core`),
   which is the identifier-translation source the task's environment note
   permits in place of the unavailable Semantic Scholar MCP server. Older
   MEDLINE records only carry author initials (not spelled-out given names);
   those are recorded as-is (e.g. `"S M McCann"`) rather than guessed.
4. Two corpus-ID pairs in `pdf_corpus_ids.json` turned out to be duplicate
   Semantic Scholar records for the same actual paper (same DOI/PMID):
   `232240856`/`255832704` (Wang et al., 2021 — "Single-cell morphological
   characterization of CRH neurons...") and `255955325`/`778336` (Rodriguez
   et al., 2015 — "Fibroblast growth factor 8 regulates postnatal
   development..."). `reference_list.json` carries both as separate
   author_keys (`X` and `X_1`). Which specific corpus ID maps to which
   author_key was confirmed from the PDF's citation-label text next to each
   link (not assumed by list order): `255832704` → `Wang et al., 2021`,
   `232240856` → `Wang et al._1, 2021`; `255955325` → `Rodriguez et al.,
   2015`, `778336` → `Rodriguez et al._1, 2015`.

## Corrections made during this run

- The first merge pass produced an empty/default paper record for corpus
  `268520959` (`Qiu et al., 2024`) because its `paper_meta` was omitted
  from the merge script by mistake — `qc-content` caught this immediately
  (`store_schema: paper '268520959': year: Input should be a valid integer`).
  Corrected the paper record with the full resolved metadata (PMID 38498811)
  and re-ran `qc-content`: 0 errors for `references/hypothalamus`.

## Outstanding gaps (expected, not blocking)

`qc-content` reports 91 `source_document` **gaps** (not errors) for the
`hypothalamus` store — every `ASTA_REPORT`-sourced quote lacks a recorded
source PDF path. This matches the existing pattern for prior ASTA-report
ingests in other regions (e.g. `sexually_dimorphic`) and is a known,
tracked gap category in `qc_content.py`, not something this workflow step
sets.

## Verification

`just qc-content` after the merge + correction: **`references/hypothalamus
(0 error, 0 warn, 91 gap)`**.

See `run_quotes.json` for the full per-quote provenance (quote_key, corpus_id,
ref, author_key, section, text) that later workflow steps (evidence
extraction) will cite from.
