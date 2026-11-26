"""Fetch S2 snippet-search results for a fixed corpus, one file per query.

Usage: python s2_snippets.py CORPUS_IDS_JSON OUT_DIR
Reads ASTA_API_KEY from the environment; never prints it.
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

QUERIES = {
    "q01_relay_identity": "dLGN thalamocortical relay neuron glutamatergic projection to primary visual cortex",
    "q02_ephys": "relay neuron burst firing T-type calcium low-threshold spike tonic mode intrinsic membrane properties",
    "q03_morphology": "relay cell dendritic morphology soma size dendritic arbor reconstruction",
    "q04_xyw": "X-like Y-like W-like relay cells morphological classes mouse dLGN",
    "q05_core_shell": "dLGN shell core calbindin parvalbumin relay neurons superficial layers V1",
    "q06_convergence": "retinal ganglion cell convergence relay mode combination mode binocular rabies tracing",
    "q07_ds": "direction selective orientation selective dLGN neurons shell",
    "q08_axon_targets": "thalamocortical axons layer 4 layer 1 V1 relay neuron projection",
    "q09_markers": "dLGN relay neuron marker gene expression transcriptomic",
    "q10_inputs": "retinogeniculate synapse corticothalamic input relay neuron",
    "q11_development": "development of dLGN relay neurons eye-specific segregation",
    "q12_interneuron_contrast": "relay neurons versus local interneurons dLGN GABA",
}

LIMIT = 100


def fetch(query, paper_ids, key):
    params = urllib.parse.urlencode(
        {"query": query, "paperIds": ",".join(paper_ids), "limit": LIMIT}
    )
    req = urllib.request.Request(
        "https://api.semanticscholar.org/graph/v1/snippet/search?" + params,
        headers={"x-api-key": key},
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise


def main():
    corpus_ids = json.load(open(sys.argv[1]))
    out = Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    key = os.environ["ASTA_API_KEY"]
    paper_ids = [f"CorpusId:{c}" for c in corpus_ids]
    for name, q in QUERIES.items():
        data = fetch(q, paper_ids, key)
        (out / f"{name}.json").write_text(
            json.dumps({"query": q, "response": data}, indent=1)
        )
        print(name, len(data.get("data", [])))
        time.sleep(1.1)


if __name__ == "__main__":
    main()
