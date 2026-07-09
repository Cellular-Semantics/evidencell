"""Mapping census (R2.Q2): tally edge confidence tiers by region across kb/graphs/**.

Counts one row per MappingEdge that carries a `confidence:` field.
Demo files (basename starting with '_') are tallied separately and excluded
from the headline totals.
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[5]
GRAPHS = ROOT / "kb" / "graphs"
TIERS = ["HIGH", "MODERATE", "LOW", "UNCERTAIN", "REFUTED", "CANDIDATE"]

by_region = defaultdict(Counter)
demo = Counter()
total = Counter()

for f in sorted(GRAPHS.rglob("*.yaml")):
    region = f.relative_to(GRAPHS).parts[0]
    is_demo = f.name.startswith("_")
    try:
        doc = yaml.safe_load(f.read_text()) or {}
    except Exception as e:  # noqa
        print(f"PARSE ERROR {f}: {e}", file=sys.stderr)
        continue
    for edge in doc.get("edges", []) or []:
        if not isinstance(edge, dict):
            continue
        conf = edge.get("confidence")
        if conf is None:
            continue
        if is_demo:
            demo[conf] += 1
        else:
            by_region[region][conf] += 1
            total[conf] += 1

def fmt_row(label, counter):
    cells = "  ".join(f"{t}={counter.get(t,0)}" for t in TIERS if counter.get(t, 0))
    n = sum(counter.values())
    return f"{label:<20} N={n:<4} {cells}"

print("=== Mapping census by region (demo files excluded) ===")
for region in sorted(by_region):
    print(fmt_row(region, by_region[region]))
print("-" * 60)
print(fmt_row("TOTAL", total))
print()
print(f"Regions: {len(by_region)}")
print(f"Total mappings (confidence-bearing edges): {sum(total.values())}")
print()
if demo:
    print("=== Demo files (_*.yaml), excluded from totals ===")
    print(fmt_row("demo", demo))

# machine-readable
import json
out = {
    "by_region": {r: dict(c) for r, c in by_region.items()},
    "total": dict(total),
    "demo_excluded": dict(demo),
    "n_regions": len(by_region),
    "n_mappings": sum(total.values()),
}
(Path(__file__).parent.parent / "census.json").write_text(json.dumps(out, indent=2))
print("\nWrote census.json")
