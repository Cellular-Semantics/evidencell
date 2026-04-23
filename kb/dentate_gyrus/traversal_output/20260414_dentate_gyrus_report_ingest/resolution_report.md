# Reference Resolution Report

**Run ID:** 20260414_dentate_gyrus_report_ingest
**Region:** dentate_gyrus
**Date:** 2026-04-14
**Output:** kb/draft/dentate_gyrus/references.json

---

## Summary

| Metric | Count |
|--------|-------|
| Total references in reference_list.json | 22 |
| Corpus IDs in pdf_corpus_ids.json | 22 |
| Resolved HIGH confidence | 22 |
| Resolved MODERATE confidence | 0 |
| UNRESOLVED | 0 |
| Quotes merged (new) | 39 |
| Quotes deduplicated | 8 |
| Extra references (inline citations without evidence quotes) | 0 |

---

## Resolution Details

All 22 author_keys in reference_list.json were matched to corpus IDs via year + first-author surname matching. All matches are HIGH confidence.

| Author Key | Corpus ID | DOI | PMID | Confidence |
|------------|-----------|-----|------|------------|
| Attardo et al., 2009 | 7393550 | 10.1093/cercor/bhp100 | 19482889 | HIGH |
| Bartkowska et al., 2022 | 252063749 | 10.3390/cells11172735 | 36078144 | HIGH |
| Coviello et al., 2021 | 235300723 | 10.3390/ijms22115733 | 34072166 | HIGH |
| Dayer et al., 2005 | 15994456 | 10.1083/jcb.200407053 | 15684031 | HIGH |
| Delgado-Garcia, 2016 | 54603778 | 10.23937/2469-570X/1410039 | — | HIGH |
| Doetsch et al., 1997 | 2281064 | 10.1523/JNEUROSCI.17-13-05046.1997 | 9185542 | HIGH |
| Gomez-Climent et al., 2008 | 25925289 | 10.1093/cercor/bhm255 | 18245040 | HIGH |
| Groen et al., 2021 | 233432690 | 10.3389/fnana.2021.656882 | 33994960 | HIGH |
| Hodge et al., 2008 | 15727849 | 10.1523/JNEUROSCI.4280-07.2008 | 18385329 | HIGH |
| Hussain et al., 2023 | 258927570 | 10.4103/1673-5374.375317 | 37488837 | HIGH |
| Merz et al., 2013 | 14598082 | 10.1371/journal.pone.0062693 | 23667508 | HIGH |
| Micheli et al., 2025 | 279046466 | 10.3389/fcell.2025.1605116 | 40519263 | HIGH |
| Regalado-Santiago et al., 2016 | 14221248 | 10.1155/2016/1513285 | 26880934 | HIGH |
| Rotheneichner et al., 2018 | 13799502 | 10.1093/cercor/bhy087 | 29688272 | HIGH |
| Stepien, 2021 | 245432259 | 10.5114/ppn.2021.111950 | 37082558 | HIGH |
| Stoll, 2014 | 8479504 | 10.1186/2052-8426-2-12 | 26056581 | HIGH |
| Tanaka et al., 2019 | 148569364 | 10.2131/jts.44.357 | 31068541 | HIGH |
| Vangeneugden et al., 2015 | 625292 | 10.3389/fnins.2015.00110 | 25954142 | HIGH |
| Velusamy et al., 2017 | 13752593 | 10.1155/2017/3279061 | 28168008 | HIGH |
| Vik-Mo et al., 2012 | 10712122 | 10.5772/29754 | — | HIGH |
| Yang et al., 2015 | 7440369 | 10.3389/fnana.2015.00109 | 26321922 | HIGH |
| Zhao et al., 2006 | 18166210 | 10.1523/JNEUROSCI.3648-05.2006 | 16399667 | HIGH |

---

## Quote Merge Details

- **Raw quotes in extracted_quotes.json:** 47
- **Stored in references.json:** 39 (new)
- **Deduplicated:** 8 — these were identical text strings from the same corpus ID appearing under multiple section labels in the source report (e.g., the same passage quoted in both "Dentate Gyrus Immature Neurons" and "Olfactory Bulb Immature Neurons" sections). The content-hash key `{corpus_id}_{sha256[:8]}` identifies duplicates; only the first occurrence was stored.

Quote keys use format: `{corpus_id}_{sha256[:8]}` where sha256 is computed over whitespace-normalized lowercase text.

All stored quotes have:
- `status: pending`
- `claims: []` (to be populated in Step 3b)
- `source_method: asta_report`
- `added_by: 20260414_dentate_gyrus_report_ingest`

---

## Extra References

None. All 22 corpus IDs from pdf_corpus_ids.json mapped 1:1 to author_keys in reference_list.json. No inline-citation-only corpus IDs were detected.

---

## Notes

- CorpusID 235300723 (Coviello et al., 2021) was initially rate-limited by the Semantic Scholar API during batch resolution. It was successfully resolved on a final retry: title "PSA Depletion Induces the Differentiation of Immature Neurons in the Piriform Cortex of Adult Mice", year 2021, first author Simona Coviello. Match confirmed HIGH confidence.
- The Semantic Scholar public API (unauthenticated) was used for all lookups due to MCP tool unavailability in this environment. Rate limiting required sequential fetching with backoff (1–20s delays).
