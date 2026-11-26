# Resolution report: 20261125_thalamus_lgv_report_ingest

Substitute used: Asta_semanticscholar MCP unavailable. Corpus IDs resolved with
`uv run python -m evidencell.fetch --json CorpusId...` (all 26 in one call; offline store first, then
Semantic Scholar API), then author lists (and PMIDs where blank) filled from Europe PMC REST
(same source as artl-mcp `search_europepmc_papers`; direct REST used because of 7-60 s latency/retries).
No search fallback (step 4) was needed.

## Counts
- Total references (author_keys): 26; pdf_corpus_ids: 26
- HIGH: 26, MODERATE: 0, UNRESOLVED: 0
- Matching by normalised title + year (+/-1) against fetch results.
- Quotes passed to write_quote_to_refs: 80 -> 53 unique quote keys (27 repeats of identical text within a paper
  across sections). Of the 53 unique, 50 new and 3 already in the store (corpus 255989565, 46970679, 3881295).
  Deduplicated total: 30 (27 in-run + 3 pre-existing).

## Notes / flags
- Duplicate corpus IDs for the same paper (same DOI): Gamlin et al., 2018 / "Gamlin et al._1, 2018" ->
  46970679 (PMID 29875009) and 255989565 (no PMID from fetch; PMID taken from the same DOI);
  Hammer et al., 2014 / "_1" -> 1225644 (PMID 25011644) and 255985654 (PMID from same DOI).
  The assignment of base vs "_1" key to each corpus ID is arbitrary (identical titles).
- Some metadata is preprint-DOI based: Somaiya 2022 (bioRxiv DOI, PMID 36342840), Munoz-Castaneda 2025 (bioRxiv DOI, PMID 40166303).
- Author names are Europe PMC firstName + lastName (e.g. Guido 2018 lists 1 author, Oh 2014 34).
- Ribak et al., 1975 resolved to 6613291 (PMID 1174957).
- extra_references (corpus IDs not matching an author_key): none.
