"""Per-node evidence metrics for the survey trial (before/after comparison).

Usage: uv run python node_metrics.py <git-rev or WORKTREE> <node_id> ...
Counts, per node: property fields filled, PropertySource/MarkerSource entries,
distinct refs and quote keys cited, and markers with a gene ID.
"""
import subprocess
import sys

import yaml

PROPS = ["anatomical_location", "nt_type", "morphology", "electrophysiology",
         "defining_markers", "negative_markers", "neuropeptides", "synonyms"]


def sources(obj):
    """Yield every dict in obj that carries a quote_key."""
    if isinstance(obj, dict):
        if "quote_key" in obj:
            yield obj
        for v in obj.values():
            yield from sources(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from sources(v)


rev, nodes = sys.argv[1], sys.argv[2:]
print("node\tfields\tsources\trefs\tquote_keys\tmarkers_w_gene")
for nid in nodes:
    path = f"kb/graphs/thalamus/{nid}.yaml"
    text = open(path).read() if rev == "WORKTREE" else subprocess.run(
        ["git", "show", f"{rev}:{path}"], capture_output=True, text=True, check=True).stdout
    node = yaml.safe_load(text)["nodes"][0]
    fields = sum(1 for p in PROPS if node.get(p))
    src = [s for p in PROPS for s in sources(node.get(p))]
    markers = [m for p in ("defining_markers", "negative_markers", "neuropeptides")
               for m in node.get(p) or [] if m.get("ncbi_gene_id")]
    print(f"{nid}\t{fields}\t{len(src)}\t{len({s.get('ref') for s in src})}\t"
          f"{len({s['quote_key'] for s in src})}\t{len(markers)}")
