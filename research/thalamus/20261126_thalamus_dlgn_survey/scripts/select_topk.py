"""Merge raw snippet files, filter, keep top-K high-confidence snippets per paper."""
import json, sys, glob, re
raw, out = sys.argv[1], sys.argv[2]
K, FLOOR, FALLBACK_FLOOR = 3, 0.50, 0.40
BAD_SECTION = re.compile(r"peer review|reviewer|references", re.I)
snips = {}
for f in sorted(glob.glob(raw + "/*.json")):
    d = json.load(open(f)); q = f.split("/")[-1][:-5]
    for s in d["response"]["data"]:
        sn = s["snippet"]; cid = s["paper"]["corpusId"]
        if sn.get("snippetKind") == "title" or BAD_SECTION.search(sn.get("section") or ""):
            continue
        e = snips.setdefault((cid, sn["text"]), {
            "source_corpus_id": cid, "source_title": s["paper"]["title"],
            "snippet_kind": sn.get("snippetKind"), "section": sn.get("section") or "unknown",
            "text": sn["text"], "query_scores": {}})
        e["query_scores"][q] = round(s["score"], 4)
by_paper = {}
for e in snips.values():
    e["snippet_score"] = max(e["query_scores"].values())
    by_paper.setdefault(e["source_corpus_id"], []).append(e)
selected, low_only = [], []
for cid, es in by_paper.items():
    es.sort(key=lambda e: (-e["snippet_score"], e["snippet_kind"] != "body"))
    keep = [e for e in es if e["snippet_score"] >= FLOOR][:K]
    if not keep and es[0]["snippet_score"] >= FALLBACK_FLOOR:
        keep = es[:1]
    if not keep:
        low_only.append({"source_corpus_id": cid, "best_score": es[0]["snippet_score"]})
    selected.extend(keep)
selected.sort(key=lambda e: -e["snippet_score"])
json.dump({"params": {"K": K, "floor": FLOOR, "fallback_floor": FALLBACK_FLOOR},
           "snippets": selected, "below_floor_papers": low_only},
          open(out, "w"), indent=1)
print(len(snips), "filtered unique;", len(selected), "selected from", len({e['source_corpus_id'] for e in selected}), "papers;", len(low_only), "below floor:", low_only)
