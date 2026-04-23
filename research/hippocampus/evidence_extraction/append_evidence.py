#!/usr/bin/env python3
"""Append proposed evidence items into the KB YAML for hippocampal GABAergic interneurons."""

import yaml
from pathlib import Path

EVIDENCE_FILE = Path(__file__).parent / "proposed_evidence_all.yaml"
KB_FILE = Path(__file__).parent.parent / "20260409_hippocampus_report_ingest.yaml"
SOURCE_TAG = "cite_traverse_2026_04_10"


def make_source_entry(item: dict) -> dict:
    """Build a source dict from a proposed evidence item."""
    return {
        "ref": item["reference"],
        "snippet": item["snippet"],
        "support": item["support"],
        "source": SOURCE_TAG,
    }


def append_to_marker_sources(node: dict, field_name: str, source_entry: dict) -> bool:
    """Append source to the first marker in defining_markers or negative_markers that has a sources list.
    If none have sources, append to the first marker (creating the sources list)."""
    markers = node.get(field_name, [])
    if not markers:
        return False

    # Try to find a marker that already has a sources list
    for marker in markers:
        if isinstance(marker, dict) and "sources" in marker and isinstance(marker["sources"], list):
            marker["sources"].append(source_entry)
            return True

    # Fall back to first marker, creating sources list
    if isinstance(markers[0], dict):
        if "sources" not in markers[0]:
            markers[0]["sources"] = []
        markers[0]["sources"].append(source_entry)
        return True

    return False


def append_evidence(kb: dict, item: dict) -> str:
    """Append one evidence item to the correct node/field. Returns status string."""
    node_id = item["node_id"]
    target = item["target_field"]
    source_entry = make_source_entry(item)

    # Find node
    node = None
    for n in kb["nodes"]:
        if n["id"] == node_id:
            node = n
            break
    if node is None:
        return f"SKIP: node '{node_id}' not found"

    if target == "anatomical_location":
        # Append source to all anatomical_location entries (v0.8.0: nested sources)
        locs = node.get("anatomical_location", [])
        if not locs:
            return f"SKIP: node '{node_id}' has no anatomical_location entries"
        for loc in locs:
            if "sources" not in loc:
                loc["sources"] = []
            loc["sources"].append(source_entry)
        return "OK: anatomical_location[].sources"

    elif target == "nt_type":
        nt = node.get("nt_type")
        if not nt or not isinstance(nt, dict):
            return f"SKIP: node '{node_id}' has no nt_type dict"
        if "sources" not in nt:
            nt["sources"] = []
        nt["sources"].append(source_entry)
        return "OK: nt_type.sources"

    elif target in ("electrophysiology_class", "electrophysiology"):
        ephys = node.get("electrophysiology")
        if not ephys or not isinstance(ephys, dict):
            return f"SKIP: node '{node_id}' has no electrophysiology object"
        if "sources" not in ephys:
            ephys["sources"] = []
        ephys["sources"].append(source_entry)
        return "OK: electrophysiology.sources"

    elif target in ("morphology_notes", "morphology"):
        morph = node.get("morphology")
        if not morph or not isinstance(morph, dict):
            return f"SKIP: node '{node_id}' has no morphology object"
        if "sources" not in morph:
            morph["sources"] = []
        morph["sources"].append(source_entry)
        return "OK: morphology.sources"

    elif target == "defining_markers":
        ok = append_to_marker_sources(node, "defining_markers", source_entry)
        if ok:
            return "OK: defining_markers[].sources"
        return f"SKIP: node '{node_id}' has no defining_markers to attach to"

    elif target == "negative_markers":
        ok = append_to_marker_sources(node, "negative_markers", source_entry)
        if ok:
            return "OK: negative_markers[].sources"
        return f"SKIP: node '{node_id}' has no negative_markers to attach to"

    elif target in ("colocated_types", "other"):
        # Append to notes
        note_text = f"[{SOURCE_TAG}] {item['reference']}: {item['snippet']}"
        existing = node.get("notes", "") or ""
        if existing and not existing.endswith("\n"):
            existing += "\n"
        node["notes"] = existing + note_text + "\n"
        return f"OK: notes ({target})"

    else:
        return f"SKIP: unknown target_field '{target}'"


def main():
    # Load evidence
    with open(EVIDENCE_FILE) as f:
        evidence_items = yaml.safe_load(f)

    # Load KB
    with open(KB_FILE) as f:
        kb = yaml.safe_load(f)

    # Process
    counts: dict[str, int] = {}
    skipped: list[str] = []

    for i, item in enumerate(evidence_items):
        status = append_evidence(kb, item)
        nid = item["node_id"]
        if status.startswith("OK"):
            counts[nid] = counts.get(nid, 0) + 1
        else:
            skipped.append(f"  Item {i+1} ({nid}, {item['target_field']}): {status}")

    # Summary
    print(f"Total evidence items: {len(evidence_items)}")
    print(f"Successfully appended: {sum(counts.values())}")
    print(f"Skipped: {len(skipped)}")
    print()
    print("Per-node counts:")
    for nid, c in sorted(counts.items()):
        print(f"  {nid}: {c}")

    if skipped:
        print()
        print("Skipped items:")
        for s in skipped:
            print(s)

    # Write
    # Use a custom representer for multiline strings
    class LiteralStr(str):
        pass

    def literal_representer(dumper, data):
        if "\n" in data:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    yaml.add_representer(str, literal_representer)

    with open(KB_FILE, "w") as f:
        yaml.dump(kb, f, default_flow_style=False, allow_unicode=True, width=120, sort_keys=False)

    print(f"\nWrote updated KB to: {KB_FILE}")


if __name__ == "__main__":
    main()
