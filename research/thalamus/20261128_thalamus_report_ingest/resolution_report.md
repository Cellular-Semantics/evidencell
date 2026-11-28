# Resolution report

Method: Asta MCP unavailable; CLI fallback used (`just fetch-reference CorpusId:NNN`, offline store first, then Semantic Scholar API). Full author lists for 6 new papers came from Europe PMC (REST search by PMID/DOI), since fetch-reference returns no authors. No search fallbacks needed.

- Total references: 12 (12 corpus IDs, all matched on normalised title + year/first author)
- HIGH: 12, MODERATE: 0, UNRESOLVED: 0
- Extra references (corpus IDs with no author_key): none
- Notes: Laliberte et al., 2026 is a bioRxiv preprint (no PMID; DOI 10.64898/2026.08.31.748331, ref given as DOI URL). Juavinett et al. is year 2019 in Semantic Scholar, 2020 in Europe PMC (kept 2019, matching author_key).
- New paper records: 14280583, 195771773, 256505257, 276403731, 291827425, 293845523. Existing: 13741105, 23594973, 249575101, 254404676, 275580744, 4792744.
- Quotes: 16 distinct quotes passed to write_quote_to_refs (8 in-run exact duplicates dropped before writing); 15 new, 1 already in store.
