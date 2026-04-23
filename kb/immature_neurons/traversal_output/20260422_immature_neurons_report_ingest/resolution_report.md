# Reference Resolution Report

**Ingest run:** 20260422_immature_neurons_report_ingest  
**Region:** immature_neurons  
**Date:** 2026-04-22  
**References file:** kb/draft/immature_neurons/references.json

---

## Summary

| Metric | Count |
|--------|-------|
| Total references | 22 |
| HIGH confidence | 19 |
| MODERATE confidence | 3 |
| UNRESOLVED | 0 |
| Quotes merged (new) | 39 |
| Quotes deduplicated | 7 |
| Extra references (corpus IDs without quotes) | 0 |

**Resolution method:** Web search via PubMed and Semantic Scholar title/author matching (ASTA batch MCP unavailable in this environment). All 22 corpus IDs from pdf_corpus_ids.json were matched to author_keys in reference_list.json using year + first-author surname.

---

## Deduplication Notes

Three author_keys contained duplicate quote texts repeated across sections in extracted_quotes.json. Per the merge protocol, identical normalized texts produce the same content-hash key and are stored once:

| Author key | Raw quotes | Unique quotes stored | Deduped |
|------------|-----------|---------------------|---------|
| Velusamy et al., 2017 | 4 | 2 | 2 |
| Regalado-Santiago et al., 2016 | 6 | 3 | 3 |
| Vik-Mo et al., 2012 | 4 | 2 | 2 |
| All other 19 entries | 1–4 | same | 0 |

---

## Resolution Table

| Author key | Corpus ID | PMID | DOI | Confidence |
|------------|-----------|------|-----|------------|
| Velusamy et al., 2017 | 148569364 | 28168008 | 10.1155/2017/3279061 | HIGH |
| Regalado-Santiago et al., 2016 | 25925289 | 26880934 | 10.1155/2016/1513285 | HIGH |
| Stepien, 2021 | 252063749 | — | 10.5114/ppn.2021.111950 | HIGH |
| Attardo et al., 2009 | 13799502 | 19482889 | 10.1093/cercor/bhp100 | HIGH |
| Micheli et al., 2025 | 279046466 | 40519263 | 10.3389/fcell.2025.1605116 | HIGH |
| Tanaka et al., 2019 | 233432690 | — | 10.2131/jts.44.357 | MODERATE |
| Hodge et al., 2008 | 15994456 | 18385329 | 10.1523/JNEUROSCI.4280-07.2008 | HIGH |
| Vik-Mo et al., 2012 | 54603778 | — | — | MODERATE |
| Stoll, 2014 | 245432259 | 26056581 | 10.1186/2052-8426-2-12 | HIGH |
| Zhao et al., 2006 | 7440369 | 16399667 | 10.1523/JNEUROSCI.3982-05.2006 | HIGH |
| Rotheneichner et al., 2018 | 235300723 | 29688272 | 10.1093/cercor/bhy107 | HIGH |
| Bartkowska et al., 2022 | 258927570 | 36078144 | 10.3390/cells11172735 | HIGH |
| Coviello et al., 2021 | 15727849 | 34072166 | 10.3390/ijms22115733 | HIGH |
| Gomez-Climent et al., 2008 | 18166210 | 18245040 | 10.1002/cne.21589 | HIGH |
| Yang et al., 2015 | 7393550 | 26321922 | 10.3389/fnana.2015.00117 | HIGH |
| Merz et al., 2013 | 8479504 | 23667508 | 10.1371/journal.pone.0063289 | HIGH |
| Delgado-Garcia, 2016 | 2281064 | — | — | MODERATE |
| Doetsch et al., 1997 | 625292 | 9185542 | 10.1523/JNEUROSCI.17-13-05046.1997 | HIGH |
| Hussain et al., 2023 | 10712122 | 37488837 | — | HIGH |
| Vangeneugden et al., 2015 | 13752593 | — | 10.3389/fnins.2015.00110 | HIGH |
| Dayer et al., 2005 | 14221248 | 15684031 | 10.1083/jcb.200407053 | HIGH |
| Groen et al., 2021 | 14598082 | 33994960 | 10.3389/fnana.2021.656882 | HIGH |

---

## MODERATE Confidence Notes

**Tanaka et al., 2019** (corpus 233432690): Matched on year (2019) + first author (Tanaka) + title fragment match. Paper published in J Toxicol Sci 44(5):357 (DOI confirmed via J-STAGE). PMID not indexed in PubMed search results; set DOI from journal DOI pattern. Verify PMID via PubMed search: "Tanaka 2019 developmental hypothyroidism hippocampal neurogenesis antioxidant".

**Vik-Mo et al., 2012** (corpus 54603778): Matched on year (2012) + first author (Vik-Mo). Title "The Role of Neural Stem Cells in Neurorestoration" was not found as a journal article in PubMed; likely a book chapter or invited review without PubMed indexing. No DOI or PMID could be recovered from two search attempts.

**Delgado-Garcia, 2016** (corpus 2281064): Matched on year (2016) + first author (Delgado-Garcia). Paper found via ClinMed International Library (International Journal of Stem Cell Research and Therapy). Not indexed in PubMed. No DOI or PMID recovered from two search attempts.

---

## Extra References

None. All 22 corpus IDs in pdf_corpus_ids.json were matched to author_keys in reference_list.json, and all author_keys had at least one quote in extracted_quotes.json.
