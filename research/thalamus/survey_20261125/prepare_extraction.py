"""Merge per-node summaries to one entry per paper; write paper_catalogue.json.

Usage: python3 prepare_extraction.py <survey_dir> <refs_dir>
Some survey subagents wrote one entry per snippet. Merge them per corpus_id:
highest node_relevance wins, quotes are unioned (order kept, max 5), summaries joined.
paper_catalogue.json uses the externalIds shape evidence-extraction.md reads.
"""
import glob
import json
import os
import sys

D, R = sys.argv[1], sys.argv[2]
RANK = {"HIGH": 0, "MODERATE": 1, "LOW": 2}

os.makedirs(f"{D}/summaries_merged", exist_ok=True)
for f in sorted(glob.glob(f"{D}/summaries/*.json")):
    merged = {}
    for e in json.load(open(f)):
        cid = str(e["source_corpus_id"])
        m = merged.get(cid)
        if m is None:
            merged[cid] = dict(e, quotes=list(e["quotes"]),
                               synonyms_found=list(e.get("synonyms_found") or []))
            continue
        if RANK[e["node_relevance"]] < RANK[m["node_relevance"]]:
            m["node_relevance"], m["node_relevance_reason"] = e["node_relevance"], e["node_relevance_reason"]
        m["quotes"] += [q for q in e["quotes"] if q not in m["quotes"]]
        m["summary"] += " " + e["summary"]
        m["synonyms_found"] += e.get("synonyms_found") or []
    out = sorted(merged.values(), key=lambda e: RANK[e["node_relevance"]])
    for e in out:
        e["quotes"] = e["quotes"][:5]
    json.dump(out, open(f"{D}/summaries_merged/{os.path.basename(f)}", "w"), indent=1)
    print(f"{os.path.basename(f)[:-5]}: {len(out)} papers, {sum(len(e['quotes']) for e in out)} quotes")

cat = []
for f in sorted(glob.glob(f"{R}/papers/*.json")):
    p = json.load(open(f))
    ext = {"CorpusId": p["corpus_id"]}
    if p.get("pmid"):
        ext["PubMed"] = p["pmid"]
    if p.get("doi"):
        ext["DOI"] = p["doi"]
    cat.append({"externalIds": ext, "title": p.get("title"), "year": p.get("year"),
                "authors": p.get("authors"), "author_keys": p.get("author_keys")})
json.dump(cat, open(f"{D}/paper_catalogue.json", "w"), indent=1)
print(f"paper_catalogue.json: {len(cat)} papers")
