# Resolution report: thalamus_dlgn_report_ingest

- Total references (author_keys): 39. HIGH 39, MODERATE 0, UNRESOLVED 0.
- Resolution source: fetch_reference.json (`just fetch-reference` batch; ASTA MCP unavailable). All 39 corpus IDs matched one author_key by title/year/first author.
- Authors for the 24 papers new to the store: Europe PMC REST (full first+last names). 15 papers were already in the store (paper_meta ignored).
- Quotes: 138 passed to write_quote_to_refs (many repeated within extracted_quotes.json), 63 distinct quote keys: 60 new, 3 already in store. All 138 listed in run_quotes.json.
- Extra references (corpus IDs not matching an author_key): none.

## Duplicate S2 records
- Hammer et al., 2014 -> 1225644 (PMID 25011644); Hammer et al._1, 2014 -> 255985654 (same DOI 10.1186/1749-8104-9-16, no PMID).
- Seabrook et al., 2013 -> 15010690 (PMID 24359973); Seabrook et al._1, 2013 -> 255986294 (same DOI, no PMID).
- All four papers were already in the store as separate records, so no new record was created. The report's evidence quotes are not linked to a specific corpus ID in the inputs, so the plain key was assigned the PMID-bearing record and the `_1` key the DOI-only record. The `_1` quotes have ref = DOI URL. Prefer the PMID-bearing records (1225644, 15010690) when citing in KB YAML.
