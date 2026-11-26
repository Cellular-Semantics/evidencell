import json
from pathlib import Path
from evidencell.references import write_quote_to_refs
D = Path('research/thalamus/20261126_thalamus_dlgn_survey')
summ = json.load(open(D/'all_summaries.json'))
cat = json.load(open(D/'paper_catalogue.json'))
papers = cat if isinstance(cat, list) else cat.get('result', [])
picks = {'3598591': 1, '4601077': 1, '4807205': 2, '257758447': 0, '1639353': 2}
for e in summ:
    cid = str(e['source_corpus_id'])
    if cid not in picks: continue
    i = picks[cid]
    meta = next((p for p in papers if str(p.get('externalIds', {}).get('CorpusId', '')) == cid), {})
    key = write_quote_to_refs(region_dir=Path('references/thalamus'), corpus_id=cid,
        quote_text=e['quotes'][i], section=e['quote_sections'][i], source_method=e['source_method'],
        added_by='evidence_extraction_dlgn_direction_selective_neuron_20261126', paper_meta=meta)
    print(cid, key)
