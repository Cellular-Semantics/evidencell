# Reference Resolution Report

**Run:** 20260709_cerebellum_blind_report_ingest  
**Date:** 2026-07-09  
**Region:** cerebellum_blind  
**Output:** references/cerebellum_blind/references.json

---

## Summary

| Metric | Count |
|---|---|
| Total author_keys in reference_list.json | 45 |
| Resolved HIGH | 45 |
| Resolved MODERATE | 0 |
| UNRESOLVED | 0 |
| Corpus IDs in pdf_corpus_ids.json | 46 |
| Extra references (inline citations, no quotes) | 1 |
| Quotes merged (new unique) | 85 |
| Quotes deduplicated (cross-section duplicates) | 103 |
| References entries written | 45 |

---

## Resolution Method

All 45 author_keys were resolved via the single `get_paper_batch` call against the
46 corpus IDs from `pdf_corpus_ids.json`. Matching criterion: year + first-author surname.
All matches are HIGH confidence.

No fallback searches were needed.

---

## Extra References (corpus IDs without author_key matches)

| Corpus ID | Title | Note |
|---|---|---|
| 257748826 | "Evaluation of P-gp and SGLT2 transport capacity in MPS using human iPS cell-derived proximal tubular cells" (Kawakami et al., 2022) | Unrelated paper (kidney MPS study); not in reference_list.json; likely a spurious hyperlink in the ASTA PDF. No quotes. |

Note: The pdf_corpus_ids.json contains 46 IDs. 45 map to the 45 author_keys in
reference_list.json. The 46th (257748826) is an unrelated paper with no
corresponding quotes and is logged here as an extra_reference only.

---

## Deduplication Notes

188 raw quote instances appeared in extracted_quotes.json across 45 author_keys.
Many quotes were repeated verbatim across multiple sections (e.g., the same passage
cited under "Anatomical organization and core cell types", "Functional roles and
physiology", "Connectivity and circuit motifs", and "Molecular markers, proteins,
and transgenes"). Content-hash deduplication collapsed these to 85 unique quote
entries — one canonical entry per distinct text per corpus_id, retaining the section
label from the first occurrence.

---

## Author_key → Corpus_id Mapping

| Author Key | Corpus ID | PMID | DOI |
|---|---|---|---|
| Arlt et al., 2020 | 212416931 | 32130904 | 10.1016/j.celrep.2020.02.009 |
| Auer et al., 2021 | 232102613 | 33651839 | 10.1371/journal.pone.0247801 |
| Beau et al., 2024 | 267384488 | 38352514 | 10.1101/2024.01.30.577845 |
| Briatore et al., 2010 | 1460508 | 20711348 | 10.1371/journal.pone.0012119 |
| Brown et al., 2018 | 59945454 | 30742002 | 10.1038/s41598-018-38264-1 |
| Buttermore et al., 2012 | 41293753 | 22492029 | 10.1523/JNEUROSCI.5602-11.2012 |
| Cerminara et al., 2015 | 24278908 | 25601779 | 10.1038/nrn3886 |
| Chu et al., 2012 | 3834513 | 22623975 | 10.1371/journal.pone.0037031 |
| Ding et al., 2023 | 258488886 | 37147705 | 10.1186/s13578-023-01032-4 |
| Dizon et al., 2011 | 17186992 | 21775592 | 10.1523/JNEUROSCI.1350-11.2011 |
| Filho et al., 2025 | 281405540 | 40973045 | 10.1055/s-0045-1811623 |
| Gaffield et al., 2017 | 207511102 | 28389475 | 10.1523/JNEUROSCI.0534-17.2017 |
| Halverson et al., 2022 | 247245529 | 36480240 | 10.1101/2022.03.03.482855 |
| Jahncke et al., 2024 | 268857461 | 38585758 | 10.1101/2024.03.28.587263 |
| Kamath et al., 2018 | 52897807 | 30276662 | 10.1007/s12035-018-1363-7 |
| Kim et al., 2014 | 17043664 | 24857665 | 10.1016/j.celrep.2014.04.047 |
| Kim et al., 2020 | 222815633 | 33075461 | 10.1016/j.neuroscience.2020.10.008 |
| Konno et al., 2014 | 8585958 | 24872547 | 10.1523/JNEUROSCI.0628-14.2014 |
| Kozareva et al., 2020 | 214725795 | (preprint) | 10.1101/2020.03.04.976407 |
| Lackey et al., 2023 | 262069620 | 37745401 | 10.1101/2023.09.15.557934 |
| Lackey et al., 2024 | 269458929 | 38692278 | 10.1016/j.neuron.2024.04.010 |
| Lackey et al., 2025 | 280548075 | 40777368 | 10.1101/2025.07.17.665322 |
| Lang et al., 1999 | 36404032 | 10087085 | 10.1523/JNEUROSCI.19-07-02728.1999 |
| Leto et al., 2009 | 12484440 | 19474334 | 10.1523/JNEUROSCI.0957-09.2009 |
| Leto et al., 2015 | 12596141 | 26439486 | 10.1007/s12311-015-0724-2 |
| Lin et al., 2020 | 216044470 | 32390933 | 10.3389/fneur.2020.00315 |
| Lowenstein et al., 2022 | 247317953 | 35262281 | 10.1111/febs.16426 |
| Mann-Metzer et al., 1999 | 6066223 | 10212289 | 10.1523/JNEUROSCI.19-09-03298.1999 |
| Miyazaki et al., 2021 | 239017682 | 34658339 | 10.7554/eLife.59613 |
| Nordquist et al., 1988 | 17950457 | 3199205 | 10.1523/JNEUROSCI.08-12-04780.1988 |
| Osorno et al., 2021 | 233245440 | (preprint) | 10.1101/2021.04.09.439172 |
| Osorno et al., 2022 | 248832318 | 35578131 | 10.1038/s41593-022-01057-x |
| Pilotto et al., 2023 | 259169106 | 37321222 | 10.1016/j.neuron.2023.05.016 |
| Rieubland et al., 2014 | 2011920 | 24559679 | 10.1016/j.neuron.2013.12.029 |
| Sarropoulos et al., 2021 | 237308705 | 34446581 | 10.1126/science.abg4696 |
| Schilling et al., 2008 | 14529996 | 18677503 | 10.1007/s00418-008-0483-y |
| Sillitoe et al., 2008 | 10659411 | 19150487 | 10.1016/j.neuroscience.2008.12.025 |
| Sudarov et al., 2011 | 33378607 | 21795554 | 10.1523/JNEUROSCI.0479-11.2011 |
| Wang et al., 2020 | 213840122 | 35701402 | 10.1038/s41467-022-30977-2 |
| Watson et al., 2015 | 15503971 | 26136256 | 10.1098/rsob.150056 |
| Witter et al., 2016 | 2715384 | 27346533 | 10.1016/j.neuron.2016.05.037 |
| Wu et al., 2023 | 255974302 | 36675230 | 10.3390/ijms24021718 |
| Zhang et al., 1996 | 18960178 | 8562089 | 10.1016/S0896-6273(00)80022-7 |
| Zhou et al., 2020 | 213986526 | (preprint) | 10.1101/2020.01.28.923896 |
| Zhou et al._1, 2020 | 222167171 | (eLife) | 10.7554/eLife.55569 |

**Note on Zhou 2020 disambiguation:** Two corpus IDs both map to Zhou et al. 2020
(same first author, same year). 213986526 is the bioRxiv preprint (title contains
"that are defined by"); 222167171 is the published eLife paper (title says
"defined by" without "that are"). Both are legitimate: reference_list.json
distinguishes them as `Zhou et al., 2020` and `Zhou et al._1, 2020`.
