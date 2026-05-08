# Resolution Report

**Run ID:** 20260427_hippocampus_glutamatergic_report_ingest
**Date:** 2026-04-27
**Region:** hippocampus
**References file:** references/hippocampus/references.json

---

## Summary

| Metric | Count |
|--------|-------|
| Total references in pdf_corpus_ids.json | 39 |
| Total author_keys in reference_list.json | 39 |
| Resolved HIGH | 39 |
| Resolved MODERATE | 0 |
| UNRESOLVED | 0 |
| Extra corpus IDs (no author_key match) | 0 |

**All 39/39 corpus IDs resolved to author_keys at HIGH confidence** (year + first author surname match).

---

## Quote Merge

| Metric | Count |
|--------|-------|
| Quotes new (added) | 81 |
| Quotes deduplicated (skipped — key already present) | 0 |
| New corpus entries created | 37 |
| Existing corpus entries merged into | 2 |

### Merged entries (corpus IDs pre-existing from prior ingest)

| Corpus ID | Author key | Pre-existing quotes | New quotes added |
|-----------|-----------|---------------------|-----------------|
| 21358766 | Muller et al., 2017 | 2 (status: validated, added_by: 20260324_hippocampus_report_ingest) | 2 |
| 393787 | Ceranik et al., 1997 | 2 (status: validated, added_by: 20260324_hippocampus_report_ingest) | 2 |

In both cases the author_key was already present in the existing entry's `author_keys` list, so no duplicate was appended.

---

## Resolution Details

All matches made via batch API call to Semantic Scholar (`/graph/v1/paper/batch`) with `CorpusId:` prefixed IDs, requesting `title,authors,year,externalIds`. Match criterion: year equality + normalized first-author surname match (accent-stripped, lowercased). Compound surnames (e.g. "De Cegli" → "cegli", "Munster-Wandowski" → "munster-wandowski") handled via normalization.

| Corpus ID | Author Key | Match basis |
|-----------|------------|-------------|
| 10060696 | Naumann et al., 2015 | year=2015, surname=naumann |
| 10808330 | Manent et al., 2006 | year=2006, surname=manent |
| 1115431 | Hamzei-Sichani et al., 2012 | year=2012, surname=hamzei-sichani |
| 11290620 | Scharfman et al., 2013 | year=2013, surname=scharfman |
| 11333153 | Pedroni et al., 2014 | year=2014, surname=pedroni |
| 13358368 | Cegli et al., 2012 | year=2012, surname=cegli (from "De Cegli") |
| 13657743 | Scharfman et al., 2015 | year=2015, surname=scharfman |
| 14854554 | Sarvari et al., 2016 | year=2016, surname=sarvari (accent-stripped) |
| 15354140 | Jabs et al., 2005 | year=2005, surname=jabs |
| 15897856 | Huh et al., 2010 | year=2010, surname=huh |
| 16383828 | Hagihara et al., 2011 | year=2011, surname=hagihara |
| 1705399 | Yau et al., 2015 | year=2015, surname=yau |
| 1711204 | Puighermanal et al., 2016 | year=2016, surname=puighermanal |
| 20157937 | Langnaese et al., 1997 | year=1997, surname=langnaese |
| 205599726 | Sah et al., 2017 | year=2017, surname=sah |
| 210181642 | Yeung et al., 2020 | year=2020, surname=yeung |
| 212418354 | Senova et al., 2020 | year=2020, surname=senova |
| 21358766 | Muller et al., 2017 | year=2017, surname=muller (accent-stripped from Müller) |
| 222135486 | Martin-Belmonte et al., 2020 | year=2020, surname=martin-belmonte (accent-stripped) |
| 2281033 | Dale et al., 2015 | year=2015, surname=dale |
| 231953329 | Botterill et al., 2021 | year=2021, surname=botterill |
| 235678538 | Fredes et al., 2021 | year=2021, surname=fredes |
| 252086716 | Mancini et al., 2022 | year=2022, surname=mancini |
| 2565845 | Anstotz et al., 2015 | year=2015, surname=anstotz |
| 260336826 | Godino et al., 2023 | year=2023, surname=godino |
| 280332787 | Komaki et al., 2025 | year=2025, surname=komaki |
| 3153294 | Marissal et al., 2012 | year=2012, surname=marissal |
| 3288675 | Herrera-Molina et al., 2017 | year=2017, surname=herrera-molina |
| 34872919 | Herrera-Molina et al., 2014 | year=2014, surname=herrera-molina |
| 3583187 | Sun et al., 2017 | year=2017, surname=sun |
| 393787 | Ceranik et al., 1997 | year=1997, surname=ceranik |
| 4875295 | Cembrowski et al., 2016 | year=2016, surname=cembrowski |
| 502543 | Kirson et al., 2000 | year=2000, surname=kirson |
| 539922 | Zander et al., 2010 | year=2010, surname=zander |
| 5468451 | Siegel et al., 1995 | year=1995, surname=siegel |
| 631148 | Wheeler et al., 2015 | year=2015, surname=wheeler |
| 7165380 | Quattrocolo et al., 2014 | year=2014, surname=quattrocolo |
| 7458943 | Munster-Wandowski et al., 2013 | year=2013, surname=munster-wandowski (from Münster-Wandowski) |
| 7981953 | Yu et al., 2014 | year=2014, surname=yu |

---

## Extra References

None. All 39 corpus IDs in pdf_corpus_ids.json matched an author_key in reference_list.json.

---

## No Fallback Searches Required

All references resolved in the initial batch. No MODERATE or UNRESOLVED entries.
