# Resolution report (20261114_thalamus_report_ingest)

Environment note: the Asta MCP tools were unavailable. Batch resolution used the Semantic Scholar Graph API /paper/batch (authors, year, ids) cross-checked against `evidencell.fetch --json` (pmid/doi). No pmid/doi discrepancies between the two sources.

- Total references: 33 author_keys; 33 corpus IDs, all matched
- HIGH: 33, MODERATE: 0, UNRESOLVED: 0
- Quotes merged: 65 new, 101 deduplicated (166 total; many quotes repeat verbatim across keys/within a key)
- Extra references (no evidence-section quotes): none
- Duplicate-key pairs map to distinct corpus IDs of the same paper (the _1 variants are the PMID-less duplicate records 255985654, 255986294, 255989565).
- 1225644 and 1898525 treated as new papers.

## Mapping
- Hammer et al., 2014 -> 1225644
- Hammer et al._1, 2014 -> 255985654
- Bickford et al., 2010 -> 23985202
- Lindstrom et al., 2010 -> 14045536
- Gamlin et al., 2018 -> 46970679
- Gamlin et al._1, 2018 -> 255989565
- Halassa et al., 2016 -> 3881295
- Su et al., 2020 -> 210870509
- Evangelio et al., 2018 -> 4792744
- Weil et al., 2022 -> 249575101
- Seabrook et al., 2013 -> 15010690
- Seabrook et al._1, 2013 -> 255986294
- Morgan et al., 2019 -> 198259790
- Antal et al., 2010 -> 11224139
- Leist et al., 2016 -> 1898525
- Halnes et al., 2011 -> 53306582
- Sanchez-Vives et al., 1996 -> 7411015
- Jager et al., 2016 -> 264044014
- Somaiya et al., 2022 -> 247085323
- Charalambakis et al., 2019 -> 73481430
- Stebbins et al., 2024 -> 271906359
- Yang et al., 2017 -> 26076888
- Errington et al., 2011 -> 13918038
- Pressler et al., 2013 -> 15874961
- Govindaiah et al., 2006 -> 11022573
- Godwin et al., 1996 -> 347964
- Crandall et al., 2012 -> 17166593
- Casale et al., 2011 -> 15995215
- Mullner et al., 2023 -> 257758447
- Krosigk et al., 1999 -> 17326929
- Whitley et al., 2025 -> 277785001
- Lorincz et al., 2009 -> 10154880
- Chattopadhyaya et al., 2004 -> 16859652
