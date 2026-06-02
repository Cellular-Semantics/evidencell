# Reference Resolution Report

**Run ID:** 20260528_medial_temporal_lobe_amygdala_report_ingest  
**Region:** medial_temporal_lobe_amygdala  
**Date:** 2026-05-28

---

## Summary

| Metric | Value |
|---|---|
| Total references | 44 |
| HIGH confidence | 44 |
| MODERATE confidence | 0 |
| UNRESOLVED | 0 |
| Quotes merged (new) | 57 |
| Quotes deduplicated | 0 |
| Extra references | 0 |

---

## Resolution method

All 44 corpus IDs from `pdf_corpus_ids.json` were resolved in a single batch call to
`get_paper_batch` with `fields=title,authors,year,externalIds`. Every corpus ID
matched exactly one author_key in `reference_list.json` by year + first-author surname.
No fallback searches were required.

---

## Resolved references (44 / 44 HIGH)

| author_key | corpus_id | PMID | DOI |
|---|---|---|---|
| Preston et al., 2002 | 16969256 | 12359830 | 10.1101/LM.54702 |
| Heckers, 2000 | 5246583 | 22033839 | 10.31887/DCNS.2000.2.3/sheckers |
| Juran et al., 2016 | 2088724 | 26779109 | 10.3389/fpsyg.2015.02015 |
| Nolan et al., 2020 | 222092617 | 33015518 | 10.1177/2470547020944553 |
| Kiernan, 2012 | 5837589 | 22934160 | 10.1155/2012/176157 |
| Ruiz-Rizzo et al., 2019 | 195404074 | 31783114 | 10.1101/659854 |
| Yousuf et al., 2021 | 237541151 | 34537382 | 10.1016/j.neuroimage.2021.118563 |
| Poggi et al., 2024 | 269255369 | 38712320 | 10.1093/braincomms/fcae140 |
| Yang et al., 2017 | 1397717 | 29163066 | 10.3389/fncir.2017.00086 |
| Pitkanen et al., 1994 | 14068807 | 8158266 | 10.1523/JNEUROSCI.14-04-02200.1994 |
| Ignacio et al., 2014 | 1229611 | 25309888 | 10.3389/fped.2014.00103 |
| Nardelli et al., 2024 | 270614391 | 39130512 | 10.1093/braincomms/fcae210 |
| Pitkanen et al., 1997 | 10539464 | 9364666 | 10.1016/S0166-2236(97)01125-9 |
| Porcaro et al., 2023 | 256859534 | 36831071 | 10.3390/biomedicines11020535 |
| Kinkead et al., 2023 | 258718681 | 37265841 | 10.3389/fphys.2023.1183933 |
| Veinante et al., 2013 | 15449738 | 25408902 | 10.1186/2049-9256-1-9 |
| Polepalli et al., 2020 | 220930580 | 32802405 | 10.1038/s41539-020-0071-z |
| Perumal et al., 2021 | 233450033 | 33994955 | 10.3389/fncir.2021.633235 |
| Cutsuridis et al., 2017 | 2026905 | 28428747 | 10.3389/fnsys.2017.00019 |
| Loonen et al., 2016 | 18703800 | 27920666 | 10.3389/fnins.2016.00539 |
| McDonald et al., 2016 | 3460849 | 26876924 | 10.1002/jnr.23709 |
| Raudales et al., 2024 | 271240390 | 39012795 | 10.7554/eLife.93481 |
| Huilgol et al., 2016 | 9742927 | 26994098 | 10.1007/s00018-016-2172-7 |
| McDonald et al., 2012 | 11544073 | 22837739 | 10.3389/fncir.2012.00046 |
| Woodruff et al., 2007 | 161407 | 17234587 | 10.1523/JNEUROSCI.3686-06.2007 |
| Unal et al., 2020 | 212579559 | 32144495 | 10.1007/s00429-020-02051-4 |
| Nishijo et al., 1988 | 18678121 | 3193170 | 10.1523/JNEUROSCI.08-10-03556.1988 |
| Vereczki et al., 2021 | 232283078 | 33837051 | 10.1101/2021.03.15.435365 |
| Vicario et al., 2014 | 10856039 | 25309337 | 10.3389/fnana.2014.00090 |
| Garcia-Calero et al., 2020 | 226283312 | 33240050 | 10.3389/fnana.2020.590011 |
| Vicario et al., 2016 | 11582390 | 27160258 | 10.1007/s00429-016-1229-6 |
| Gerlach et al., 2021 | 231758452 | 33515290 | 10.1007/s00441-020-03378-4 |
| Metwalli et al., 2022 | 248700803 | 35645737 | 10.3389/fnana.2022.883537 |
| Ignacio et al., 2025 | 278095530 | 40294707 | 10.1016/j.yfrne.2025.101190 |
| Sorrells et al., 2019 | 195246702 | 31227709 | 10.1038/s41467-019-10765-1 |
| Hansen et al., 2013 | 8042525 | 24097039 | 10.1038/nn.3541 |
| Rubin et al., 2013 | 17126269 | 24155945 | 10.1371/journal.pone.0077339 |
| Miyoshi et al., 2015 | 8070111 | 26377473 | 10.1523/JNEUROSCI.1164-15.2015 |
| Chareyron et al., 2021 | 235715856 | 34206571 | 10.3390/ijms22136691 |
| Villard et al., 2023 | 259201574 | 37337377 | 10.1002/hipo.23567 |
| Bernier et al., 1998 | 15638357 | 9502809 | 10.1523/JNEUROSCI.18-07-02486.1998 |
| Hochgerner et al., 2023 | 264517392 | 37884748 | 10.1038/s41593-023-01469-3 |
| Carrere et al., 2015 | 14375617 | 25852499 | 10.3389/fnsys.2015.00041 |
| Mackay et al., 2024 | 272553238 | 39256373 | 10.1038/s41467-024-52295-5 |

---

## Extra references

None. All 44 corpus IDs in `pdf_corpus_ids.json` matched an author_key in
`reference_list.json`.

---

## Quote merge details

57 quotes from `extracted_quotes.json` were merged into
`references/medial_temporal_lobe_amygdala/references.json`.
0 quotes were deduplicated (all were new).

Quote keys were generated using content-hash:
`sha256(normalized_text)[:8]` prefixed with corpus_id.

---

## Output

- **references.json:** `references/medial_temporal_lobe_amygdala/references.json`
- **Entries:** 44 (all HIGH confidence)
- **Total quotes stored:** 57
