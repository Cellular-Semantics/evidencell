# Reference Resolution Report

**Run ID:** 20260528_amygdala_report_ingest  
**Region:** medial_temporal_lobe_amygdala  
**Date:** 2026-05-28  
**References file:** references/medial_temporal_lobe_amygdala/references.json

---

## Summary

| Metric | Count |
|---|---|
| Total author_keys in reference_list | 45 |
| Resolved (HIGH) | 45 |
| Resolved (MODERATE) | 0 |
| UNRESOLVED | 0 |
| Extra corpus IDs (batch but no author_key) | 0 |
| New quotes merged | 74 |
| Deduplicated quotes (already existed) | 5 |
| New reference entries added | 35 |
| Existing entries updated (author_key or quotes merged) | 10 |
| Total references in store after merge | 79 |

---

## Resolution method

All 45 author_keys were resolved in a single `get_paper_batch` call against 45 corpus IDs from `pdf_corpus_ids.json`. Matching used first-author surname + year, with Unicode accent normalization (NFD → ASCII) to handle names such as Pitkänen, Paré, Hájos, Andrási, and Fernández. No fallback searches were required.

---

## HIGH confidence matches (45/45)

| author_key | corpus_id | PMID | DOI |
|---|---|---|---|
| Veinante et al., 2013 | 15449738 | 25408902 | 10.1186/2049-9256-1-9 |
| Pineda et al., 2021 | 244936719 | — | 10.3390/metabo11120837 |
| Aerts et al., 2021 | 244956947 | 34955766 | 10.3389/fnana.2021.786679 |
| Hu et al., 2022 | 252477669 | 36232376 | 10.3390/ijms231911076 |
| Bzdok et al., 2012 | 19021055 | 22806915 | 10.1002/hbm.22138 |
| Wilson et al., 2015 | 31039293 | 26844236 | 10.1016/j.ynstr.2015.06.001 |
| Zhu et al., 2025 | 278109019 | 40352758 | 10.3389/fncir.2025.1575232 |
| Porcaro et al., 2023 | 256859534 | 36831071 | 10.3390/biomedicines11020535 |
| Chareyron et al., 2011 | 16013850 | 21618234 | 10.1002/cne.22677 |
| Carney et al., 2010 | 627853 | 20507551 | 10.1186/1749-8104-5-14 |
| McDonald et al., 2012 | 11544073 | 22837739 | 10.3389/fncir.2012.00046 |
| Pare et al., 1996 | 17655278 | 8627370 | 10.1523/JNEUROSCI.16-10-03334.1996 |
| McDonald, 2024 | 268497805 | 38491847 | 10.1002/jnr.25318 |
| Ignacio et al., 2014 | 1229611 | 25309888 | 10.3389/fped.2014.00103 |
| Perumal et al., 2021 | 233450033 | 33994955 | 10.3389/fncir.2021.633235 |
| Hajos, 2021 | 235382885 | 34177472 | 10.3389/fncir.2021.687257 |
| Vereczki et al., 2021 | 232283078 | 33837051 | 10.1101/2021.03.15.435365 |
| Andrasi et al., 2017 | 13486665 | 28542195 | 10.1371/journal.pbio.2001421 |
| Sarowar et al., 2020 | 221366115 | 32858950 | 10.3390/cells9091972 |
| Zhang et al., 2021 | 230972365 | 33691931 | 10.1016/j.biopsych.2020.12.026 |
| Raudales et al., 2024 | 271240390 | 39012795 | 10.7554/eLife.93481 |
| Woodruff et al., 2007 | 161407 | 17234587 | 10.1523/JNEUROSCI.3686-06.2007 |
| Washburn et al., 1992 | 6078957 | 1403101 | 10.1523/JNEUROSCI.12-10-04066.1992 |
| Niimi et al., 2012 | 15738241 | 22960119 | 10.1016/j.brainres.2012.08.050 |
| Vereczki et al., 2016 | 16327247 | 27013983 | 10.3389/fnana.2016.00020 |
| Rovira-Esteban et al., 2019 | 204835327 | 31636080 | 10.1523/ENEURO.0220-19.2019 |
| Bienvenu et al., 2012 | 10647550 | 22726836 | 10.1016/j.neuron.2012.04.022 |
| Yeh et al., 2024 | 267685584 | 38419794 | 10.3389/fnmol.2024.1364268 |
| Adke et al., 2019 | 209598438 | 33188006 | 10.1523/ENEURO.0402-20.2020 |
| Gilpin et al., 2014 | 442779 | 25433901 | 10.1016/j.biopsych.2014.09.008 |
| Nisbett et al., 2025 | 280558687 | 40780965 | 10.1523/ENEURO.0059-25.2025 |
| Haubensak et al., 2010 | 2270983 | 21068836 | 10.1038/nature09553 |
| Li et al., 2013 | 10650261 | 23354330 | 10.1038/nn.3322 |
| Nikolenko et al., 2020 | 220976356 | 32751957 | 10.3390/brainsci10080502 |
| O'Leary et al., 2022 | 253356112 | 36425768 | 10.1016/j.isci.2022.105497 |
| Fernandez et al., 2025 | 280713728 | 40867603 | 10.3390/biom15081160 |
| Totty et al., 2024 | 273531817 | 39463931 | 10.1101/2024.10.18.618721 |
| McDonald, 2020 | 216417665 | 34220399 | 10.1016/b978-0-12-815134-1.00001-5 |
| Hochgerner et al., 2022 | 253206255 | — | 10.1101/2022.10.25.513733 |
| Hochgerner et al., 2023 | 264517392 | 37884748 | 10.1038/s41593-023-01469-3 |
| Pitkanen et al., 1997 | 10539464 | 9364666 | 10.1016/S0166-2236(97)01125-9 |
| Yu et al., 2023 | 256832817 | 36788214 | 10.1038/s41421-022-00506-y |
| Gui et al., 2025 | 275818530 | 39843917 | 10.1038/s41398-025-03223-8 |
| Zhou et al., 2023 | 263704470 | 37798411 | 10.1038/s41593-023-01452-y |
| Beyeler et al., 2020 | 216440056 | 32792868 | 10.1016/b978-0-12-815134-1.00003-9 |

---

## Deduplicated quotes (5)

The following quote keys were already present in the references store and were skipped:

- `1229611_e14a19cf` (Ignacio et al., 2014 — "Classical neuron classes across amygdala subdivisions" section; pre-existing from the earlier MTL ingest with section "Amygdala organization and principal cellular classes")
- `1229611_70584dfd` (Ignacio et al., 2014 — second quote; same paper, pre-existing)
- `15449738_4bbaac69` (Veinante et al., 2013 — BLA pyramidal neurons quote; pre-existing)
- `15449738_a21bd562` (Veinante et al., 2013 — intercalated cell masses quote; pre-existing)
- `232283078_d4238834` (Vereczki et al., 2021 — GABAergic cell type proportions quote; pre-existing from Basolateral amygdala neuronal subtypes section; new ingest added a second instance under "Classical neuron classes across amygdala subdivisions")

Note: The Vereczki et al., 2021 quote appears identically in two sections of `extracted_quotes.json`; only the first instance was stored.

---

## Notes

- `Pineda et al., 2021` (corpus_id 244936719) has no PMID in Semantic Scholar; DOI only.
- `Hochgerner et al., 2022` (corpus_id 253206255) is a preprint (bioRxiv); no PMID.
- 10 existing entries were updated: `1229611`, `11544073`, `15449738`, `161407`, `232283078`, `233450033`, `256859534`, `264517392`, `271240390`, `10539464`. Author keys already present were not duplicated; new quotes were appended.
