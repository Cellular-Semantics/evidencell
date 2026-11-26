"""How much would evidence-extraction's 'skip refs already on the node' rule drop?

Usage: uv run python skip_analysis.py <survey_dir>
For each node: summary entries, papers, papers already cited on the node (would be
skipped), and quotes not already in the reference store (new text).
"""
import glob
import json
import re
import sys

import yaml

D = sys.argv[1]
papers = {}
for f in glob.glob("references/thalamus/papers/*.json"):
    p = json.load(open(f))
    papers[p["corpus_id"]] = p
store = set()
for f in glob.glob("references/thalamus/quotes/*.json"):
    for q in json.load(open(f)).values() if isinstance(json.load(open(f)), dict) else []:
        store.add(re.sub(r"\s+", " ", q.get("text", "").lower()).strip())


def ref_of(cid):
    p = papers.get(str(cid), {})
    if p.get("pmid"):
        return f"PMID:{p['pmid']}"
    if p.get("doi"):
        return f"https://doi.org/{p['doi']}"
    return f"CorpusId:{cid}"


def refs_on(obj, out):
    if isinstance(obj, dict):
        if "ref" in obj and "quote_key" in obj:
            out.add(obj["ref"])
        for v in obj.values():
            refs_on(v, out)
    elif isinstance(obj, list):
        for v in obj:
            refs_on(v, out)
    return out


print("node\tentries\tpapers\tH\tpapers_already_cited(skipped)\tH_skipped\tnew_quotes\tnew_quotes_in_skipped_papers")
for f in sorted(glob.glob(f"{D}/summaries/*.json")):
    nid = f.split("/")[-1][:-5]
    node = yaml.safe_load(open(f"kb/graphs/thalamus/{nid}.yaml"))["nodes"][0]
    existing = refs_on(node, set())
    ents = json.load(open(f))
    pids = {str(e["source_corpus_id"]) for e in ents}
    skipped = {c for c in pids if ref_of(c) in existing}
    high = {str(e["source_corpus_id"]) for e in ents if e["node_relevance"] == "HIGH"}
    newq = [(str(e["source_corpus_id"]), q) for e in ents for q in e["quotes"]
            if re.sub(r"\s+", " ", q.lower()).strip() not in store]
    print(f"{nid}\t{len(ents)}\t{len(pids)}\t{len(high)}\t{len(skipped)}\t{len(high & skipped)}\t"
          f"{len(newq)}\t{sum(c in skipped for c, _ in newq)}")
