import json
from pathlib import Path
from evidencell.references import write_quote_to_refs
S = json.load(open('research/thalamus/20261126_thalamus_dlgn_survey/all_summaries.json'))
cat = json.load(open('research/thalamus/20261126_thalamus_dlgn_survey/paper_catalogue.json'))
papers = cat if isinstance(cat, list) else cat.get('result', [])
picks = [('8247989', 1), ('4601077', 1), ('16328698', 2)]
for cid, qi in picks:
    e = next(x for x in S if str(x['source_corpus_id']) == cid)
    meta = next((p for p in papers if str(p.get('externalIds', {}).get('CorpusId', '')) == cid), {})
    key = write_quote_to_refs(region_dir=Path('references/thalamus'), corpus_id=cid,
        quote_text=e['quotes'][qi], section=e['quote_sections'][qi], source_method=e['source_method'],
        added_by='evidence_extraction_dlgn_shell_relay_neuron_20261126', paper_meta=meta)
    print(cid, key, e['quotes'][qi][:80])
