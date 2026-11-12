# Resolution report: 20261111_thalamus_report_ingest (region: thalamus)

- Total references: 26 (26 corpus IDs from pdf_corpus_ids.json)
- Resolved via get_paper_batch (year + first-author surname + title): 26/26
- HIGH: 26, MODERATE: 0, UNRESOLVED: 0
- Extra references (corpus IDs with no author_key): none
- Quotes: 174 extracted; 61 new written to references/thalamus/, 113 deduplicated (identical text already present)
- Notes: "Sun et al., 2025" maps to the bioRxiv preprint (CorpusId 279620506) and "Sun et al., 2026" to the Nature Methods version (291337338). Phillips 2017 and 2018 share DOI 10.1101/241315 in Semantic Scholar (two distinct corpus records); stored as returned.
- Scripts: fetch_meta.py, merge_refs.py; raw metadata in batch_result.json; summary in resolution.json.
