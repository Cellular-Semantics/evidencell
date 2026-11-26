"""Print evidence-extraction NODE_CONTEXT for one node."""
import sys, yaml
from evidencell.paths import find_node_file

def refs(o, acc):
    if isinstance(o, dict):
        if isinstance(o.get("ref"), str): acc.add(o["ref"])
        for v in o.values(): refs(v, acc)
    elif isinstance(o, list):
        for v in o: refs(v, acc)

nid = sys.argv[1]
f = find_node_file(nid)
node = [x for x in yaml.safe_load(open(f))["nodes"] if x["id"] == nid][0]
mk = [g.get("symbol") or g.get("name_in_source") for g in node.get("defining_markers") or []]
loc = []
for a in node.get("anatomical_location") or []:
    t = a.get("term") if isinstance(a.get("term"), dict) else {}
    loc.append(f'{a.get("label") or a.get("name_in_source")} ({a.get("compartment", "?")})')
acc = set(); refs(node, acc)
print(f"""Node:            {node['name']} ({nid})
Definition:      {node.get('definition_basis')}
Species:         {(node.get('species') or {}).get('label')}
Markers:         {', '.join(map(str, mk)) or 'none recorded'}
Location:        {'; '.join(loc) or 'none recorded'}
NT type:         {(node.get('nt_type') or {}).get('name_in_source') or 'unknown'}
Existing refs:   {', '.join(sorted(acc)) or 'none'}
KB_FILE:         {f}""")
