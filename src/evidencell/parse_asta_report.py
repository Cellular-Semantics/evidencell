"""
parse_asta_report.py — support utilities for the asta-report-ingest orchestrator.

Does NOT parse PDFs. The orchestrator's parsing subagent reads the PDF natively
and writes YAML/JSON; this module handles the deterministic post-processing:

  - resolve_references(): replace UNRESOLVED:{key} tokens with real IDs
  - build_resolution_report(): human-readable summary of resolution quality
  - extract_cl_seeds(): pull CL definition reference IDs for cite-traverse seeds

CLI usage:
  uv run python -m evidencell.parse_asta_report resolve <yaml_file> <resolution_map.json>
  uv run python -m evidencell.parse_asta_report report <resolution_map.json>
  uv run python -m evidencell.parse_asta_report cl-seeds <cl_mappings.json>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Core functions
# ---------------------------------------------------------------------------

UNRESOLVED_PATTERN = re.compile(r'UNRESOLVED:([^"\'>\n]+)')


def resolve_references(yaml_str: str, resolution_map: dict[str, Any]) -> str:
    """Replace ``UNRESOLVED:{author_key}`` tokens in a YAML string.

    For each token, looks up the author_key in *resolution_map*.  If a
    ``pmid`` is present it substitutes ``PMID:{pmid}``; if only a ``doi``
    is present it substitutes ``DOI:{doi}``; if only a ``corpus_id`` is
    present it substitutes ``CorpusId:{corpus_id}``; otherwise leaves the
    token unchanged (so unresolved items remain visible for the human gate).

    Args:
        yaml_str: Raw YAML text containing ``UNRESOLVED:{key}`` tokens.
        resolution_map: Mapping of author_key → resolution dict with optional
            keys ``pmid``, ``doi``, ``corpus_id``, ``resolution_confidence``.

    Returns:
        YAML string with tokens replaced where possible.
    """

    def _replace(match: re.Match) -> str:
        key = match.group(1)
        entry = resolution_map.get(key, {})
        if entry.get("pmid"):
            return f"PMID:{entry['pmid']}"
        if entry.get("doi"):
            return f"DOI:{entry['doi']}"
        if entry.get("corpus_id"):
            return f"CorpusId:{entry['corpus_id']}"
        return match.group(0)  # leave unchanged

    return UNRESOLVED_PATTERN.sub(_replace, yaml_str)


def build_resolution_report(resolution_map: dict[str, Any]) -> str:
    """Build a human-readable Markdown summary of reference resolution quality.

    Args:
        resolution_map: Mapping of author_key → resolution dict with keys:
            ``resolution_confidence`` (HIGH/MODERATE/LOW/UNRESOLVED),
            ``title`` (optional), ``year`` (optional), ``quote_count`` (optional).

    Returns:
        Markdown string suitable for display at the human review gate.
    """
    counts: dict[str, int] = {"HIGH": 0, "MODERATE": 0, "LOW": 0, "UNRESOLVED": 0}
    unresolved: list[str] = []

    for key, entry in resolution_map.items():
        conf = entry.get("resolution_confidence", "UNRESOLVED").upper()
        if conf not in counts:
            conf = "UNRESOLVED"
        counts[conf] += 1
        if conf == "UNRESOLVED":
            unresolved.append(key)

    total = sum(counts.values())
    resolved = total - counts["UNRESOLVED"]
    pct = int(resolved / total * 100) if total else 0

    lines = [
        "## Reference Resolution Report",
        "",
        f"**Total references**: {total}  "
        f"**Resolved**: {resolved} ({pct}%)  "
        f"**Unresolved**: {counts['UNRESOLVED']}",
        "",
        "| Confidence | Count |",
        "|---|---|",
    ]
    for level in ("HIGH", "MODERATE", "LOW", "UNRESOLVED"):
        lines.append(f"| {level} | {counts[level]} |")

    if unresolved:
        lines += [
            "",
            "### Unresolved references",
            "These could not be matched to a corpus ID. "
            "Add `corpus_id` / `pmid` / `doi` manually or drop them.",
            "",
        ]
        for key in unresolved:
            entry = resolution_map.get(key, {})
            title_hint = entry.get("title_fragment", "")
            year = entry.get("year", "")
            hint = f" — {title_hint} ({year})" if title_hint else ""
            lines.append(f"- `{key}`{hint}")

    return "\n".join(lines)


def extract_cl_seeds(cl_mappings: dict[str, Any]) -> list[str]:
    """Extract CL definition reference IDs for use as additional cite-traverse seeds.

    CL terms carry definition references (PMIDs/DOIs) curated from the literature.
    These are valuable seed papers that complement the ASTA report's reference list.

    Args:
        cl_mappings: Mapping of node_id → CL mapping dict with optional key
            ``definition_references`` (list of PMID/DOI strings).

    Returns:
        Deduplicated list of reference ID strings (e.g. ``["PMID:1234", ...]``).
    """
    seen: set[str] = set()
    seeds: list[str] = []
    for entry in cl_mappings.values():
        for ref in entry.get("definition_references", []):
            if ref and ref not in seen:
                seen.add(ref)
                seeds.append(ref)
    return seeds


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cmd_resolve(args: list[str]) -> None:
    if len(args) < 2:
        print("Usage: parse_asta_report resolve <yaml_file> <resolution_map.json>",
              file=sys.stderr)
        sys.exit(1)
    yaml_path = Path(args[0])
    map_path = Path(args[1])
    if not yaml_path.exists():
        print(f"Error: {yaml_path} not found", file=sys.stderr)
        sys.exit(1)
    if not map_path.exists():
        print(f"Error: {map_path} not found", file=sys.stderr)
        sys.exit(1)
    resolution_map = json.loads(map_path.read_text())
    yaml_str = yaml_path.read_text()
    print(resolve_references(yaml_str, resolution_map), end="")


def _cmd_report(args: list[str]) -> None:
    if len(args) < 1:
        print("Usage: parse_asta_report report <resolution_map.json>", file=sys.stderr)
        sys.exit(1)
    map_path = Path(args[0])
    if not map_path.exists():
        print(f"Error: {map_path} not found", file=sys.stderr)
        sys.exit(1)
    resolution_map = json.loads(map_path.read_text())
    print(build_resolution_report(resolution_map))


def _cmd_cl_seeds(args: list[str]) -> None:
    if len(args) < 1:
        print("Usage: parse_asta_report cl-seeds <cl_mappings.json>", file=sys.stderr)
        sys.exit(1)
    cl_path = Path(args[0])
    if not cl_path.exists():
        print(f"Error: {cl_path} not found", file=sys.stderr)
        sys.exit(1)
    cl_mappings = json.loads(cl_path.read_text())
    seeds = extract_cl_seeds(cl_mappings)
    print(json.dumps(seeds, indent=2))


def main() -> None:
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        sys.exit(0)
    cmd = argv[0]
    rest = argv[1:]
    if cmd == "resolve":
        _cmd_resolve(rest)
    elif cmd == "report":
        _cmd_report(rest)
    elif cmd == "cl-seeds":
        _cmd_cl_seeds(rest)
    else:
        print(f"Unknown command: {cmd}\nCommands: resolve, report, cl-seeds",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
