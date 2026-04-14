# Reference Resolution Report

**Ingest run:** 20260409_hippocampus_report_ingest  
**Region:** hippocampus  
**Date:** 2026-04-09  
**Output file:** kb/draft/hippocampus/references.json

---

## Summary

| Metric | Count |
|--------|-------|
| Total author_keys in reference_list.json | 49 |
| Resolved HIGH confidence | 49 |
| Resolved MODERATE confidence | 0 |
| UNRESOLVED | 0 |
| Extra corpus IDs (no matching author_key) | 0 |

All 49 author_keys resolved with **HIGH** confidence via year + first-author surname match against the Semantic Scholar batch API result.

No fallback searches were needed.

---

## Resolution Method

**Step 1 — Batch API call:** All 49 corpus IDs from `pdf_corpus_ids.json` were resolved in a single POST to the Semantic Scholar batch endpoint (`/graph/v1/paper/batch`), retrieving `title, authors, year, externalIds` for each.

**Step 2 — Matching:** Each batch result was matched to an `author_key` in `reference_list.json` by `(year, first_author_surname)`. All 49 matched unambiguously:

- No duplicate `(year, surname)` collisions requiring disambiguation
- The two Chamberland 2023 / 2024 entries matched to distinct corpus IDs (258397933 and 269246896 respectively) by year
- The two Huang 2014 / 2023 entries matched to distinct corpus IDs (10835885 and 260033122 respectively) by year

---

## Quotes Merged

| Metric | Count |
|--------|-------|
| New quotes added | 93 |
| Deduplicated (already present) | 39 |
| References already in references.json (merged) | 2 |
| New references added | 47 |

**Deduplicated quotes note:** 39 quotes were skipped because their normalized text hash already existed in the store or the exact text was already present in the corpus entry. These came from quote text that was duplicated across sections in `extracted_quotes.json` (e.g. Ekins et al. 2020 had identical text in three sections; only the first occurrence per unique text was stored).

**Merged entries** (corpus IDs already present in references.json from a prior ingest):
- `234597703` — Hewitt et al., 2021 (1 pre-existing quote; 2 new quotes added)
- `6652630` — Hooft et al., 2000 (4 pre-existing quotes; 1 new quote added)

---

## Extra References

None. All 49 corpus IDs from `pdf_corpus_ids.json` were matched to author_keys in `reference_list.json`.

---

## references.json State After Ingest

- Total entries (excluding `_meta`): 82
- `_meta.last_updated`: 2026-04-09T12:22:59
- `_meta.last_updated_by`: 20260409_hippocampus_report_ingest
