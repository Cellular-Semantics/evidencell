# Reference Resolution Report

**Run:** 20260709_globular_report_ingest  
**Date:** 2026-07-09  
**References file:** references/cerebellum_blind/references.json

---

## Summary

| Metric | Count |
|---|---|
| Corpus IDs in pdf_corpus_ids.json | 28 |
| Author keys in reference_list.json | 28 |
| Resolved HIGH | 28 |
| Resolved MODERATE | 0 |
| UNRESOLVED | 0 |
| Extra references (corpus IDs unmatched to any author_key) | 0 |
| Quotes merged — new | 33 |
| Quotes merged — deduped (already present) | 15 |
| New reference entries created | 7 |
| Total entries in references.json after merge | 52 |

---

## Resolution method

All 28 corpus IDs were resolved in a single batch call to
`get_paper_batch`. All matched to an author_key in reference_list.json
by year + first-author surname — confidence HIGH throughout. No fallback
searches were needed.

---

## Matched corpus IDs (HIGH)

| corpus_id | Author key | Already in refs? |
|---|---|---|
| 12484440 | Leto et al., 2009 | yes |
| 12596141 | Leto et al., 2015 | yes |
| 14276970 | Hirono et al., 2012 | **new** |
| 14529996 | Schilling et al., 2008 | yes |
| 15503971 | Watson et al., 2015 | yes |
| 17950457 | Nordquist et al., 1988 | yes |
| 18075937 | Ruigrok et al., 2011 | **new** |
| 18960178 | Zhang et al., 1996 | yes |
| 2011920 | Rieubland et al., 2014 | yes |
| 214725795 | Kozareva et al., 2020 | yes |
| 222815633 | Kim et al., 2020 | yes |
| 233245440 | Osorno et al., 2021 | yes |
| 237197775 | Farini et al., 2021 | **new** |
| 247317953 | Lowenstein et al., 2022 | yes |
| 248832318 | Osorno et al., 2022 | yes |
| 256266268 | Hernandez-Perez et al., 2023 | **new** |
| 258488886 | Ding et al., 2023 | yes |
| 268857461 | Jahncke et al., 2024 | yes |
| 269458929 | Lackey et al., 2024 | yes |
| 280548075 | Lackey et al., 2025 | yes |
| 281405540 | Filho et al., 2025 | yes |
| 33378607 | Sudarov et al., 2011 | yes |
| 41293753 | Buttermore et al., 2012 | yes |
| 52897807 | Kamath et al., 2018 | yes |
| 59340086 | Peng et al., 2019 | **new** |
| 59945454 | Brown et al., 2018 | yes |
| 608385 | Englund et al., 2006 | **new** |
| 9985750 | Dieudonne et al., 2000 | **new** |

---

## New entries created

| corpus_id | Author key | PMID | DOI |
|---|---|---|---|
| 14276970 | Hirono et al., 2012 | 22235322 | 10.1371/journal.pone.0029663 |
| 18075937 | Ruigrok et al., 2011 | 21228180 | 10.1523/JNEUROSCI.1959-10.2011 |
| 237197775 | Farini et al., 2021 | 34406416 | 10.1007/s00018-021-03911-w |
| 256266268 | Hernandez-Perez et al., 2023 | — | 10.3390/anatomia2010005 |
| 59340086 | Peng et al., 2019 | 30690467 | 10.1093/jmcb/mjy089 |
| 608385 | Englund et al., 2006 | 16957075 | 10.1523/JNEUROSCI.1610-06.2006 |
| 9985750 | Dieudonne et al., 2000 | 10684885 | 10.1523/JNEUROSCI.20-05-01837.2000 |

---

## Deduplication detail

15 quotes were skipped because their content-hashed key already existed in
references.json (from earlier cerebellum_blind ingest runs). Affected entries
(existing refs with overlapping quotes): Leto et al. 2009/2015, Watson et al.
2015, Schilling et al. 2008, Nordquist et al. 1988, Zhang et al. 1996,
Rieubland et al. 2014, Kozareva et al. 2020, Kim et al. 2020, Lowenstein et
al. 2022, Osorno et al. 2021/2022, Jahncke et al. 2024, Lackey et al.
2024/2025, Brown et al. 2018, Buttermore et al. 2012, Kamath et al. 2018,
Ding et al. 2023, Filho et al. 2025.

---

## Extra references

None — every corpus ID in pdf_corpus_ids.json matched an author_key.
