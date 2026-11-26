"""Write chosen quotes for dlgn_relay_neuron evidence extraction; print keys."""
import json
from pathlib import Path
from evidencell.references import write_quote_to_refs

D = Path('research/thalamus/20261126_thalamus_dlgn_survey')
S = json.load(open(D / 'all_summaries.json'))
cat = json.load(open(D / 'paper_catalogue.json'))
meta = {str(p['externalIds'].get('CorpusId')): p for p in cat}

# (summary index, quote index, optional exact substring override)
PICKS = {
    'A': (0, 2, None), 'B': (1, 0, None), 'C': (2, 2, None), 'D': (3, 0, None),
    'F': (5, 2, None), 'G': (7, 1, None), 'H': (9, 0, None), 'I': (14, 0, None),
    'J': (15, 2, None), 'M': (18, 2, None), 'N': (19, 2, None), 'O': (20, 0, None),
    'P': (21, 1, None), 'Q': (23, 1, None),
    'R': (30, 0, 'Thalamocortical neurons in the dorsal lateral geniculate nucleus (dLGN) transfer visual information from retina to primary visual cortex'),
    'S': (31, 0, None), 'T': (33, 0, None),
}
out = {}
for tag, (i, qi, sub) in PICKS.items():
    e = S[i]
    q = e['quotes'][qi]
    text = sub if sub else q
    assert text in q
    sec = e.get('quote_sections', [e.get('section')] * 3)[qi]
    cid = e['source_corpus_id']
    key = write_quote_to_refs(region_dir=Path('references/thalamus'), corpus_id=cid,
        quote_text=text, section=sec, source_method=e['source_method'],
        added_by='evidence_extraction_dlgn_relay_neuron_20261126', paper_meta=meta.get(cid, {}))
    out[tag] = {'cid': cid, 'key': key, 'ext': meta[cid]['externalIds']}
    print(tag, cid, key, meta[cid]['externalIds'].get('PubMed'))
json.dump(out, open(D / 'scripts' / 'ee_keys_dlgn_relay_neuron.json', 'w'), indent=1)
