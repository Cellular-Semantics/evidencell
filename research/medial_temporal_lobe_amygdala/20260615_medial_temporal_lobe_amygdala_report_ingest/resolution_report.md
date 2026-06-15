# Reference Resolution Report

**Run ID:** 20260615_medial_temporal_lobe_amygdala_report_ingest  
**Date:** 2026-06-15  
**References file:** references/medial_temporal_lobe_amygdala/references.json

---

## Summary

| Metric | Count |
|---|---|
| Total references in reference_list.json | 12 |
| HIGH confidence resolutions | 12 |
| MODERATE confidence resolutions | 0 |
| UNRESOLVED | 0 |
| New quotes merged | 2 |
| Duplicate quotes skipped | 20 |
| Extra references (no extracted quotes) | 0 |

---

## Resolution Details

All 12 corpus IDs from `pdf_corpus_ids.json` were already present in `references.json`
with correct author_key mappings. No new paper lookups were needed.

| author_key | corpus_id | confidence |
|---|---|---|
| Hu et al., 2022 | 252477669 | HIGH (pre-existing) |
| Waclaw et al., 2010 | 17223544 | HIGH (pre-existing) |
| Chung et al., 2016 | 3103554 | HIGH (pre-existing) |
| Paul et al., 2025 | 280092907 | HIGH (pre-existing) |
| Vereczki et al., 2021 | 232283078 | HIGH (pre-existing) |
| Sarowar et al., 2020 | 221366115 | HIGH (pre-existing) |
| Hochgerner et al., 2023 | 264517392 | HIGH (pre-existing) |
| Totty et al., 2025 | 281382725 | HIGH (pre-existing) |
| Cardenas et al., 2019 | 4940771 | HIGH (pre-existing) |
| McCullough et al., 2016 | 104297085 | HIGH (pre-existing) |
| Flores et al., 2017 | 17860491 | HIGH (pre-existing) |
| Page et al., 2022 | 250411527 | HIGH (pre-existing) |

---

## Quotes Merged

### New quotes added (2)

Both new quotes are for **McCullough et al., 2016** (corpus_id: 104297085), in section
`Basal amygdala fear neurons and extinction neurons`. They are near-duplicates of
previously ingested quotes (keys `104297085_cb656278` and `104297085_20a79f85`) with
minor Unicode apostrophe differences (curly vs straight quotes), which produce different
content hashes. The new keys are:

- `104297085_d5c2e82a` — "Here we demonstrate a comprehensive workflow..." (curly quotes)
- `104297085_2747518b` — ".These experiments identify and validate Ntsr2..." (curly quotes)

### Duplicates skipped (20)

All other 20 quote instances were exact content-hash matches to existing quotes and were
correctly skipped.

---

## Extra References

None. All 12 corpus IDs had corresponding extracted quotes.

---

## Notes

- The batch API (mcp__Asta_semanticscholar__get_paper_batch) returned HTTP 403; resolution
  was confirmed by checking existing entries in references.json directly.
- The near-duplicate McCullough quotes arise from Unicode normalisation differences in the
  source text. They are stored as separate entries per the content-hash protocol and do not
  indicate an error.
