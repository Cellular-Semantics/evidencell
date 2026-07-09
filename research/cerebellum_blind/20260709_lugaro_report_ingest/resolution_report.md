# Reference Resolution Report
**Run:** 20260709_lugaro_report_ingest
**Date:** 2026-07-09
**References file:** references/cerebellum_blind/references.json

---

## Summary

Resolved **13/13** author_keys from `reference_list.json` using a single batch call against
`pdf_corpus_ids.json`. All corpus IDs matched an author_key by year + first-author surname.

**HIGH: 13 | MODERATE: 0 | UNRESOLVED: 0**

Merged **16 net-new quotes** (35 deduped — many quotes appeared across multiple sections in
`extracted_quotes.json` and collapsed to a single canonical entry).

Total entries in `references/cerebellum_blind/references.json` after merge: **60** (was 52).

---

## Resolution table

| author_key | corpus_id | confidence | disposition |
|---|---|---|---|
| Vicario-Abejbn et al., 1995 | 9407361 | HIGH | new entry |
| Kita et al., 2013 | 1394480 | HIGH | new entry |
| Schilling et al., 2008 | 14529996 | HIGH | merged (author_key already present, 1 new quote added) |
| Hirono et al., 2021 | 235419102 | HIGH | new entry |
| Hirono et al., 2012 | 14276970 | HIGH | merged (existing entry, 3 quotes new, 3 deduped) |
| Dieudonne et al., 2000 | 9985750 | HIGH | merged (existing entry, 0 new quotes — all text deduped) |
| Miyazaki et al., 2020 | 219105292 | HIGH | new entry (4 raw quotes → 1 unique, 3 deduped) |
| Osorno et al., 2021 | 233245440 | HIGH | merged (existing entry, 2 new quotes added) |
| Osorno et al., 2022 | 248832318 | HIGH | merged (existing entry, 3 new quotes added) |
| Schilling, 2023 | 265064966 | HIGH | new entry |
| Schilling, 2025 | 276672145 | HIGH | new entry |
| Consalez et al., 2013 | 10192571 | HIGH | new entry |
| Niewiadomska-Cimicka et al., 2020 | 233372052 | HIGH | new entry |

---

## Extra references (corpus IDs with no matching author_key)

None. All 13 corpus IDs in `pdf_corpus_ids.json` matched exactly one author_key in
`reference_list.json`.

---

## Deduplication notes

The `extracted_quotes.json` contains 13 author_keys with a total of 52 raw quote objects.
Many quotes appear verbatim under multiple section headings (e.g. the Hirono et al. 2021
abstract paragraph appears under Structure, Function, Markers, Transgenes, and Landscape
sections). Content-hash deduplication reduced these to 16 unique texts not previously
stored, while 35 were suppressed as exact duplicates.

---

## Changes to references.json

- **8 new entries added:** 9407361, 1394480, 235419102, 219105292, 265064966, 276672145, 10192571, 233372052
- **5 existing entries updated:** 14529996 (Schilling 2008), 14276970 (Hirono 2012), 9985750 (Dieudonne 2000), 233245440 (Osorno 2021), 248832318 (Osorno 2022)
- **`_meta` updated:** `last_updated_by = "20260709_lugaro_report_ingest"`, `total_entries = 60`
