# Resolution report

- Total references: 48 (reference_list.json); corpus IDs from PDF: 48
- Resolved via batch (Semantic Scholar graph API batch endpoint; the Asta MCP tool was not exposed in this session): 48/48
- HIGH: 48, MODERATE: 0, UNRESOLVED: 0
- Matches on year + first-author surname, then title for disambiguation.
- Duplicate corpus records for the same paper (each has its own author_key and papers/ record):
  Sellers et al., 2014 (13962500) / Sellers et al._1, 2014 (255982651);
  Hammer et al., 2014 (1225644) / Hammer et al._1, 2014 (255985654).
- 5 papers have no PMID in Semantic Scholar (DOI-only or none); pmid left empty.
- Quotes merged: 84 new, 19 deduplicated (identical text, same key, no-op).
- Extra references (corpus IDs with no author_key): none.
- Raw batch response: s2_batch.json; author_key to corpus/PMID/DOI map: resolved_map.json.
