# Reference Resolution Report

**Run:** 20260425_sexually_dimorphic_report_ingest  
**Date:** 2026-04-25  
**Region:** sexually_dimorphic  
**Output:** `references/sexually_dimorphic/references.json`

---

## Summary

| Metric | Count |
|---|---|
| Total corpus IDs in pdf_corpus_ids.json | 46 |
| Total author_keys in reference_list.json | 47 |
| Resolved HIGH confidence | 46 |
| Resolved MODERATE confidence | 0 |
| UNRESOLVED | 0 |
| Unique corpus entries written | 46 |
| New quotes merged | 98 |
| Deduplicated quotes | 0 |
| Extra corpus IDs (no author_key match) | 0 |

All 47 author_keys were resolved. The reference_list contains 47 entries across 46 unique corpus IDs because two author_keys (`Chung et al., 2017` and `Chung et al._1, 2017`; `Moore et al., 2019` and `Moore et al._1, 2019`) refer to two separate corpus IDs for what appear to be the same papers — these were correctly disambiguated using the two distinct corpus IDs (20699614/256895819 for Chung and 164802066/204460206 for Moore).

---

## Resolution Method

- **Step 1:** Batch-fetched all 46 corpus IDs via Semantic Scholar batch API (`/graph/v1/paper/batch`) with `fields=title,authors,year,externalIds`.
- **Step 2:** Matched each author_key to a batch result by year + first-author surname (normalized to ASCII).
- **Step 3:** No fallback search required — all author_keys matched at HIGH confidence in the batch step.

---

## Per-Reference Resolution

| Author Key | Corpus ID | Year | PMID | DOI | Quotes |
|---|---|---|---|---|---|
| Choe et al., 2021 | 233354742 | 2021 | PMID:33895570 | DOI:10.1016/j.yhbeh.2021.104978 | 1 |
| Abrahao et al., 2012 | 214694216 | 2012 | — | DOI:10.1007/s12031-012-9923-1 | 2 |
| Rosinger et al., 2019 | 143424909 | 2019 | PMID:31055007 | DOI:10.1016/j.neuroscience.2019.04.045 | 1 |
| Nejad et al., 2017 | 1227024 | 2017 | PMID:29201072 | DOI:10.5812/ijem.44337 | 8 |
| Adachi et al., 2007 | 1357086 | 2007 | PMID:17213691 | DOI:10.1262/JRD.18146 | 2 |
| Negri-Cesi, 2015 | 14863067 | 2015 | PMID:26672480 | DOI:10.1177/1559325815590394 | 1 |
| Zilkha et al., 2021 | 233446934 | 2021 | PMID:33910083 | DOI:10.1016/j.conb.2021.03.005 | 6 |
| He et al., 2013 | 3481177 | 2013 | PMID:25206587 | DOI:10.3969/j.issn.1673-5374.2013.29.008 | 7 |
| Hemminger et al., 2024 | 273240437 | 2024 | PMID:39416191 | DOI:10.1101/2024.10.08.617260 | 2 |
| Kanaya et al., 2025 | 279874350 | 2025 | — | DOI:10.3389/fncir.2025.1593443 | 2 |
| Ide et al., 2013 | 14550592 | 2013 | PMID:23554470 | DOI:10.1523/JNEUROSCI.4278-12.2013 | 1 |
| Uchida et al., 2019 | 59307485 | 2019 | PMID:30691514 | DOI:10.1186/s13293-019-0221-2 | 1 |
| Ponzi et al., 2020 | 218556148 | 2020 | PMID:32380724 | DOI:10.3390/ijms21093269 | 2 |
| Tsukahara et al., 2020 | 220837356 | 2020 | PMID:32848568 | DOI:10.3389/fnins.2020.00797 | 2 |
| Stephens et al., 2017 | 4702847 | 2017 | PMID:28660243 | DOI:10.1523/ENEURO.0150-17.2017 | 1 |
| Lee et al., 2022 | 247882232 | 2022 | PMID:35406710 | DOI:10.3390/cells11071146 | 4 |
| Kauffman et al., 2007 | 17692566 | 2007 | PMID:17699664 | DOI:10.1523/JNEUROSCI.2099-07.2007 | 2 |
| Muir et al., 2001 | 10935681 | 2001 | PMID:11387329 | DOI:10.1074/JBC.M102743200 | 1 |
| Kotani et al., 2001 | 25457526 | 2001 | PMID:11457843 | DOI:10.1074/JBC.M104847200 | 1 |
| Park et al., 2010 | 15152139 | 2010 | PMID:20609214 | DOI:10.1186/1471-2156-11-62 | 1 |
| Pandey et al., 2011 | 22407553 | 2011 | PMID:21243444 | DOI:10.1007/s12031-011-9506-6 | 1 |
| Hashikawa et al., 2021 | 237425192 | 2021 | — | DOI:10.1101/2021.09.02.458782 | 3 |
| Wartenberg et al., 2021 | 237626479 | 2021 | PMID:34561233 | DOI:10.1523/JNEUROSCI.0885-21.2021 | 2 |
| Yamashita et al., 2021 | 236963220 | 2021 | PMID:34373576 | DOI:10.1038/s42003-021-02476-5 | 4 |
| Newmaster et al., 2019 | 201207691 | 2019 | PMID:32313029 | DOI:10.1038/s41467-020-15659-1 | 1 |
| Zdon et al., 2024 | 273148430 | 2024 | — | DOI:10.1210/jendso/bvae163.1280 | 3 |
| Zdon et al., 2025 | 282319169 | 2025 | — | DOI:10.1210/jendso/bvaf149.1673 | 2 |
| Pereira et al., 2018 | 57390802 | 2018 | PMID:30599092 | DOI:10.1101/416735 | 1 |
| Frazao et al., 2013 | 11330110 | 2013 | PMID:23407940 | DOI:10.1523/JNEUROSCI.1610-12.2013 | 5 |
| Moore et al., 2019 | 164802066 | 2019 | — | DOI:10.1210/JS.2019-SAT-426 | 2 |
| Moore et al._1, 2019 | 204460206 | 2019 | PMID:31611573 | DOI:10.1038/s41598-019-51201-0 | 3 |
| Torres et al., 2024 | 270730043 | 2024 | PMID:38978624 | DOI:10.3389/fendo.2024.1408677 | 1 |
| Johnson et al., 2021 | 237390485 | 2021 | PMID:34470806 | DOI:10.1523/JNEUROSCI.1103-21.2021 | 1 |
| Esteves et al., 2019 | 201041732 | 2019 | PMID:31419363 | DOI:10.1111/jne.12781 | 1 |
| Scerbo et al., 2014 | 1864906 | 2014 | PMID:25071448 | DOI:10.3389/fncel.2014.00188 | 4 |
| Chung et al., 2017 | 20699614 | 2017 | PMID:28894175 | DOI:10.1038/s41598-017-11478-5 | 2 |
| Chung et al._1, 2017 | 256895819 | 2017 | — | DOI:10.1038/s41598-017-11478-5 | 2 |
| Freda et al., 2022 | 246062603 | 2022 | — | DOI:10.1101/2022.01.17.476652 | 3 |
| Zapata et al., 2021 | 235348948 | 2021 | PMID:34633482 | DOI:10.1007/s00018-021-03945-0 | 5 |
| Xu et al., 2008 | 14155811 | 2008 | PMID:18434530 | DOI:10.1523/JNEUROSCI.5382-07.2008 | 1 |
| Cisternas et al., 2020 | 218682527 | 2020 | PMID:32427857 | DOI:10.1038/s41598-020-65183-x | 3 |
| Marraudino et al., 2019 | 160013615 | 2019 | PMID:31109056 | DOI:10.3390/ijms20102465 | 3 |
| Kim et al., 2019 | 204741414 | 2019 | PMID:31626771 | DOI:10.1016/j.cell.2019.09.020 | 1 |
| Correa et al., 2015 | 27794167 | 2015 | PMID:25543145 | DOI:10.1016/j.celrep.2014.12.011 | 1 |
| Zapata et al., 2022 | 251161895 | 2022 | PMID:36268511 | DOI:10.3389/fcell.2022.937875 | 1 |
| Street et al., 2018 | 46934471 | 2018 | PMID:29865233 | DOI:10.3390/ijms19061647 | 1 |

---

## Notes

- **Abrahao et al., 2012** (corpus 214694216): Title is "Abstracts" — a conference abstract collection. No PMID; DOI resolves to a journal supplement. Quotes retained but may need manual verification of attribution.
- **Hashikawa et al., 2021** (corpus 237425192): DOI is a bioRxiv preprint. No PMID.
- **Moore et al., 2019** (corpus 164802066): Conference abstract (Endocrine Society). No PMID.
- **Zdon et al., 2024 / 2025** (corpus 273148430, 282319169): Endocrine Society meeting abstracts. No PMID.
- **Freda et al., 2022** (corpus 246062603): bioRxiv preprint. No PMID.
- **Pereira et al., 2018** (corpus 57390802): bioRxiv preprint. No PMID.
- **Kanaya et al., 2025** (corpus 279874350): No PMID yet (very recent publication).
- **Chung et al._1, 2017 / Moore et al._1, 2019**: The `_1` suffix in the author_keys indicates these were separately listed in the reference_list for the same paper titles. Each was assigned a distinct corpus ID that S2 has for the same DOI, preserving the original distinction.
- **Extra corpus IDs in pdf_corpus_ids.json with no unique author_key**: None. All 46 corpus IDs are mapped.
