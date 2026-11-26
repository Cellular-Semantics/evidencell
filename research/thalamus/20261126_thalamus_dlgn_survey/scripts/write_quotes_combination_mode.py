from evidencell.references import write_quote_to_refs
from pathlib import Path
import json
cat = json.load(open('research/thalamus/20261126_thalamus_dlgn_survey/paper_catalogue.json'))
papers = cat if isinstance(cat, list) else cat.get('result', [])
summ = json.load(open('research/thalamus/20261126_thalamus_dlgn_survey/all_summaries.json'))
for cid, qi in [('5326680', 0), ('4807205', 0)]:
    e = next(x for x in summ if str(x['source_corpus_id']) == cid)
    meta = next((p for p in papers if str(p.get('externalIds', {}).get('CorpusId', '')) == cid), {})
    key = write_quote_to_refs(region_dir=Path('references/thalamus'), corpus_id=cid,
        quote_text=e['quotes'][qi], section=e['quote_sections'][qi],
        source_method=e.get('source_method', 'ASTA_snippet'),
        added_by='evidence_extraction_dlgn_combination_mode_principal_neuron_20261126', paper_meta=meta)
    print(cid, key, e.get('source_method'))
