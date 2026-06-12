# Uncertain Reference Resolution Report

**Run date:** 2026-06-12
**Added by:** 20260612_uncertain_report_ingest
**References file:** references/medial_temporal_lobe_amygdala/references.json

---

## Summary

| Metric | Count |
|--------|-------|
| Total references in this PDF | 12 |
| HIGH confidence | 12 |
| MODERATE confidence | 0 |
| UNRESOLVED | 0 |
| Papers already in references.json (deduplicated by corpus_id) | 4 |
| New papers added | 8 |
| Quotes merged — new | 13 |
| Quotes merged — deduplicated (key already existed) | 2 |
| Extra references (corpus IDs without evidence-section quotes) | 0 |

---

## Resolution method

Semantic Scholar batch and search APIs returned HTTP 403 for all calls. All references were resolved via PubMed (mcp__claude_ai_PubMed) by title+author+year search followed by metadata retrieval. All 12 references were matched with HIGH confidence (year + first-author surname confirmed against PubMed records).

---

## Papers already in references.json (no new entry created)

| Corpus ID | Author key | Notes |
|-----------|------------|-------|
| 252477669 | Hu et al., 2022 | Both uncertain quotes already present (keys 252477669_715ad4e2, 252477669_f2902c46) — 0 new quotes merged |
| 221366115 | Sarowar et al., 2020 | 1 new quote merged (key 221366115_197a5821, section "Introduction/Background") |
| 232283078 | Vereczki et al., 2021 | 1 new quote merged (key 232283078_00bb8003, long abstract, section "Introduction/Background") |
| 264517392 | Hochgerner et al., 2023 | 1 new quote merged (key 264517392_57886ed9, abstract text, section "Introduction/Background"); the duplicate-section copy resolved to the same key and was not added twice |

---

## New papers added (8)

| Corpus ID | Author key | PMID | DOI | Quotes added |
|-----------|------------|------|-----|--------------|
| 17223544 | Waclaw et al., 2010 | 20484636 | 10.1523/JNEUROSCI.5772-09.2010 | 1 |
| 3103554 | Chung et al., 2016 | 27053114 | 10.1038/srep23757 | 1 |
| 280092907 | Paul et al., 2025 | 40686779 | 10.1016/j.ynpai.2025.100190 | 1 |
| 281382725 | Totty et al., 2025 | 40961182 | 10.1126/sciadv.adw1029 | 1 |
| 4940771 | Cardenas et al., 2019 | 31193505 | 10.1016/j.ynstr.2019.100163 | 1 |
| 104297085 | McCullough et al., 2016 | 27767183 | 10.1038/ncomms13149 | 3 |
| 17860491 | Flores et al., 2017 | 28453642 | 10.1093/ijnp/pyx029 | 1 |
| 250411527 | Page et al., 2022 | 35841648 | 10.1016/j.dcn.2022.101133 | 1 |

**Note on Totty et al.:** Corpus 273531817 (Totty et al., 2024 preprint, already in references.json) and corpus 281382725 (Totty et al., 2025, published Science Advances paper) are distinct entries — the 2025 paper is the peer-reviewed version of the preprint with a different corpus ID, title punctuation, and DOI.

---

## Quote deduplication detail

- **Waclaw et al., 2010** (17223544): The identical quote text appeared in two sections ("Introduction/Background" and "Central amygdala large aspiny and small aspiny neurons") → same content hash → 1 entry stored.
- **Chung et al., 2016** (3103554): Same as above, identical text in two sections → 1 entry stored.
- **Paul et al., 2025** (280092907): Same as above → 1 entry stored.
- **Hu et al., 2022** (252477669): Both quotes already present in references.json → 0 new entries.

Total deduplicated (skipped): 5 quote instances → 2 unique keys not added (3 cross-section duplicates collapsed to 1 each = 3 instances saved; 2 Hu quotes already existed = 2 instances saved; net new unique quote entries = 13).

---

## Extra references

None. All 12 corpus IDs from uncertain_pdf_corpus_ids.json are matched to author_keys in uncertain_reference_list.json and carry evidence-section quotes in uncertain_extracted_quotes.json.

---

## Final state of references.json

- **Total papers:** 87 (was 79)
- **Total quotes:** 211 (was 198)
- **_meta.last_updated:** 2026-06-12T00:00:00.000000+00:00
- **_meta.last_updated_by:** 20260612_uncertain_report_ingest
