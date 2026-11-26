import json
from pathlib import Path
from evidencell.references import write_quote_to_refs
D = 'research/thalamus/20261126_thalamus_dlgn_survey'
summ = json.load(open(f'{D}/all_summaries.json'))
cat = json.load(open(f'{D}/paper_catalogue.json'))
papers = cat if isinstance(cat, list) else cat.get('result', [])
picks = [(0, 2), (9, 1), (23, 1), (4, 0)]
for i, qi in picks:
    e = summ[i]
    cid = str(e['source_corpus_id'])
    meta = next((p for p in papers if str(p.get('externalIds', {}).get('CorpusId', '')) == cid), {})
    key = write_quote_to_refs(region_dir=Path('references/thalamus'), corpus_id=cid,
        quote_text=e['quotes'][qi], section=e['quote_sections'][qi], source_method=e['source_method'],
        added_by='evidence_extraction_dlgn_x_like_relay_cell_20261126', paper_meta=meta)
    print(i, cid, key)
