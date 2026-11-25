"""Interim per-node snippet fetch for survey (see issue #250). Not part of src/.

Usage: python3 fetch_snippets.py <queries.json> <corpus_ids.json> <out_dir> [per_paper=15]
Calls S2 /graph/v1/snippet/search once per node (limit=1000) via curl, writes
raw_snippets/{node}.json, then trims to the top N per paper (dropping title
snippets and peer-review/reference sections) into trimmed/{node}.json.
"""
import collections
import json
import os
import re
import subprocess
import sys
import time

queries, ids, out = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])), sys.argv[3]
per_paper = int(sys.argv[4]) if len(sys.argv) > 4 else 15
paper_ids = ",".join(f"CorpusId:{i}" for i in ids)
drop_sec = re.compile(r"peer review|reviewer|references", re.I)
os.makedirs(f"{out}/raw_snippets", exist_ok=True)
os.makedirs(f"{out}/trimmed", exist_ok=True)

for node, q in queries.items():
    raw = f"{out}/raw_snippets/{node}.json"
    if not os.path.exists(raw):  # re-runs only re-trim
        # The key goes to curl on stdin as a config line, never in argv, so it
        # cannot leak into tracebacks or process listings.
        r = subprocess.run(
            ["curl", "-sS", "--fail", "--retry", "3", "--retry-all-errors", "--max-time", "120",
             "-K", "-", "-G", "-o", raw,
             "https://api.semanticscholar.org/graph/v1/snippet/search",
             "--data-urlencode", f"query={q}",
             "--data-urlencode", f"paperIds={paper_ids}",
             "--data-urlencode", "limit=1000"],
            input=f'header = "x-api-key: {os.environ["ASTA_API_KEY"]}"\n', text=True,
        )
        if r.returncode:
            sys.exit(f"{node}: curl failed with exit {r.returncode}")
        time.sleep(1.1)
    data = json.load(open(raw))["data"]
    kept, per = [], collections.Counter()
    for rank, s in enumerate(data, 1):  # API returns score-descending
        sn, cid = s["snippet"], s["paper"]["corpusId"]
        if sn.get("snippetKind") == "title" or drop_sec.search(sn.get("section") or ""):
            continue
        if per[cid] >= per_paper:
            continue
        per[cid] += 1
        kept.append({
            "corpus_id": cid, "title": s["paper"]["title"], "overall_rank": rank,
            "paper_rank": per[cid], "score": round(s["score"], 4),
            "kind": sn.get("snippetKind"), "section": sn.get("section"), "text": sn["text"],
        })
    json.dump({"node_id": node, "query": q, "per_paper": per_paper,
               "raw_count": len(data), "snippets": kept},
              open(f"{out}/trimmed/{node}.json", "w"), indent=1)
    chars = sum(len(k["text"]) for k in kept)
    print(f"{node}: raw {len(data)}, kept {len(kept)} from {len(per)} papers, ~{chars // 4} tokens")
