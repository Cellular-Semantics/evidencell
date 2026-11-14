# Resolution report: 20261112_thalamus_igl_report_ingest

- Total references: 14; resolved 14/14 via one get_paper_batch call.
- HIGH: 14, MODERATE: 0, UNRESOLVED: 0 (no search fallback needed).
- Extra references (corpus IDs with no author_key): none.
- Quotes: 65 write_quote_to_refs calls (all 14 papers) yielding 24 distinct quote keys.
  The same passage appears under several sections, so repeat calls are deduplicated by the
  store (idempotent). All 14 papers were new to the store (script: merge_refs.py).
- Notes: "Blasiak et al., 2013" -> CorpusId 25997395 (Differential firing pattern...);
  "Blasiak et al._1, 2013" -> 36406110 (Relaxin-3...). Gouwens 2020 is a bioRxiv preprint (no PMID).
