import json,re,unicodedata
from pathlib import Path
from evidencell.references import write_quote_to_refs
RUN="20261111_thalamus_report_ingest"
D="research/thalamus/20261111_thalamus_report_ingest/"
refl=json.load(open(D+'reference_list.json'))
batch=json.load(open(D+'batch_result.json'))
quotes=json.load(open(D+'extracted_quotes.json'))
def norm(s): return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
def surname(k): return norm(k.split(' et al')[0].split(',')[0].strip().split()[-1])
used=set(); res={}
for r in refl:
    ys=int(r['year']); sn=surname(r['author_key']); hit=None
    for b in batch:
        if b['paperId'] in used: continue
        if b['year']==ys and norm(b['authors'][0]['name']).split()[-1]==sn and norm(b['title'])[:40]==norm(r['title'])[:40]:
            hit=b;break
    if hit: used.add(hit['paperId']); res[r['author_key']]=hit
unmatched=[r['author_key'] for r in refl if r['author_key'] not in res]
extra=[b['externalIds']['CorpusId'] for b in batch if b['paperId'] not in used]
new=dup=0; report=[]
store=Path("references/thalamus")
for ak,hit in res.items():
    ex=hit['externalIds']; names=list(dict.fromkeys(a['name'] for a in hit['authors']))
    meta={"corpus_id":str(ex['CorpusId']),"author_keys":[ak],"title":hit['title'],"year":hit['year'],"authors":names,"resolution_confidence":"HIGH"}
    if ex.get('PubMed'): meta['pmid']=str(ex['PubMed'])
    if ex.get('DOI'): meta['doi']=ex['DOI']
    for q in quotes.get(ak,{}).get('quotes',[]):
        qf=sorted(store.glob(f"quotes/{meta['corpus_id']}.json")) 
        before=qf[0].read_text() if qf else ''
        k=write_quote_to_refs(store,meta['corpus_id'],q['text'],q.get('section',''),"ASTA_REPORT",RUN,paper_meta=meta)
        if k in before: dup+=1
        else: new+=1
print("matched",len(res),"unmatched",unmatched,"extra",extra,"new",new,"dup",dup)
json.dump({"matched":{k:v['externalIds']['CorpusId'] for k,v in res.items()},"unmatched":unmatched,"extra":extra,"new":new,"dup":dup},open(D+'resolution.json','w'),indent=1)
