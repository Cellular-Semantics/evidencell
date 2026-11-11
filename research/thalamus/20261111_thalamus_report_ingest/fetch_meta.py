import json,urllib.request
ids=json.load(open('pdf_corpus_ids.json'))
req=urllib.request.Request("https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,authors,year,externalIds",data=json.dumps({"ids":["CorpusId:"+i for i in ids]}).encode(),headers={"Content-Type":"application/json"})
d=json.load(urllib.request.urlopen(req,timeout=60))
json.dump(d,open('batch_result.json','w'),indent=1)
print(len(d),sum(x is None for x in d))
