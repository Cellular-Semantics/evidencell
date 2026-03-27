# validate.py — structural validation logic for KB YAML files
#
# Wraps linkml-validate and provides structural integrity checks.
# Imported by .claude/hooks/validate_mapping_hook.py and by pytest.

from __future__ import annotations

import json
import re
import subprocess
import tempfile
from pathlib import Path

# ── Constants ──────────────────────────────────────────────────────────────────

# Snippet values that look like placeholders rather than real verbatim text
PLACEHOLDER_SNIPPETS: frozenset[str] = frozenset(
    {"TODO", "ADD SNIPPET", "PLACEHOLDER", "TBD", "...", "FIXME"}
)


# ── Structural checks ──────────────────────────────────────────────────────────

def structural_checks(doc: dict) -> list[str]:
    """
    Validate graph integrity beyond what LinkML checks.

    Checks:
    - No duplicate node IDs
    - Edge type_a / type_b reference existing node IDs
    - Each edge has at least one evidence item
    - No empty or placeholder snippet values in LiteratureEvidence
    - Terminal nodes (is_terminal=true) have cell_set_accession populated

    Returns a list of error strings; empty list = OK.
    """
    errors: list[str] = []
    nodes = doc.get("nodes") or []
    edges = doc.get("edges") or []

    # Build node ID index; check for duplicates
    node_ids: dict[str, dict] = {}
    for node in nodes:
        nid = node.get("id")
        if not nid:
            continue
        if nid in node_ids:
            errors.append(f"Duplicate node id: '{nid}'")
        else:
            node_ids[nid] = node

    for edge in edges:
        eid = edge.get("id", "<unnamed edge>")

        # Endpoint references
        for ref_field in ("type_a", "type_b"):
            ref = edge.get(ref_field)
            if ref and ref not in node_ids:
                errors.append(
                    f"Edge '{eid}': {ref_field}='{ref}' does not match any node id. "
                    f"Known ids: {sorted(node_ids)}"
                )

        # Evidence list presence
        evidence = edge.get("evidence")
        if not isinstance(evidence, list) or len(evidence) == 0:
            errors.append(
                f"Edge '{eid}': 'evidence' must be a non-empty list (min 1 item required)"
            )
            continue

        # Snippet quality checks on each evidence item
        for ev in evidence:
            if not isinstance(ev, dict):
                continue
            snippet = ev.get("snippet")
            if snippet is None:
                continue  # Not a LiteratureEvidence, or snippet not yet added
            stripped = str(snippet).strip()
            if stripped == "":
                errors.append(
                    f"Edge '{eid}': evidence has an empty 'snippet'. "
                    "Must be verbatim text copied from the cited paper."
                )
            elif stripped.upper() in PLACEHOLDER_SNIPPETS or stripped.upper().startswith("TODO"):
                errors.append(
                    f"Edge '{eid}': snippet looks like a placeholder: '{stripped}'. "
                    "Replace with an exact substring from the cited paper."
                )

    # Terminal nodes must have cell_set_accession
    for node in nodes:
        if node.get("is_terminal") is True and not node.get("cell_set_accession"):
            errors.append(
                f"Node '{node.get('id')}': is_terminal=true but "
                "cell_set_accession is missing or empty"
            )

    return errors


# ── Quote key provenance check ─────────────────────────────────────────────────

def _collect_quote_keys(obj: object, result: list[str] | None = None) -> list[str]:
    """Recursively collect all 'quote_key' values from a nested dict/list."""
    if result is None:
        result = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "quote_key" and isinstance(v, str) and v:
                result.append(v)
            else:
                _collect_quote_keys(v, result)
    elif isinstance(obj, list):
        for item in obj:
            _collect_quote_keys(item, result)
    return result


def check_quote_keys(doc: dict, refs_path: Path) -> list[str]:
    """
    Check that every quote_key value in the YAML exists in references.json.

    Returns a list of error strings; empty = OK.
    Skips silently if references.json does not exist (fresh graph with no refs yet).
    """
    if not refs_path.exists():
        return []

    try:
        refs: dict = json.loads(refs_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return [f"Could not read {refs_path.name} — ensure it is valid JSON"]

    # Build a flat set of all known quote keys across all corpus entries
    known: set[str] = set()
    for entry in refs.values():
        if isinstance(entry, dict):
            known.update(entry.get("quotes", {}).keys())

    errors: list[str] = []
    for qk in _collect_quote_keys(doc):
        if qk not in known:
            errors.append(
                f"quote_key '{qk}' not found in {refs_path.name}. "
                "Add the quote through the validated ingest path before referencing it."
            )
    return errors


# ── Reference PMID/DOI check ───────────────────────────────────────────────────

# Matches ref: values that carry a PMID or DOI identifier
_PMID_RE = re.compile(r"^PMID:(\d+)$", re.IGNORECASE)
_DOI_RE = re.compile(r"^DOI:(.+)$", re.IGNORECASE)


def _collect_refs(obj: object, result: list[str] | None = None) -> list[str]:
    """Recursively collect all 'ref' string values from a nested dict/list."""
    if result is None:
        result = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "ref" and isinstance(v, str) and v:
                result.append(v)
            else:
                _collect_refs(v, result)
    elif isinstance(obj, list):
        for item in obj:
            _collect_refs(item, result)
    return result


def check_ref_pmids(doc: dict, refs_path: Path) -> list[str]:
    """
    Check that every PMID: or DOI: ref cited in the YAML has an entry in references.json.

    This prevents hallucinated PMIDs from being committed: if an agent invents a
    citation, the PMID will not be present in the validated references store.

    Skips silently if references.json does not exist.
    """
    if not refs_path.exists():
        return []

    try:
        refs: dict = json.loads(refs_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []  # Already flagged by check_quote_keys if called first

    # Build lookup sets from references.json
    known_pmids: set[str] = set()
    known_dois: set[str] = set()
    for entry in refs.values():
        if not isinstance(entry, dict):
            continue
        if pmid := entry.get("pmid"):
            known_pmids.add(str(pmid))
        if doi := entry.get("doi"):
            known_dois.add(doi.lower())

    errors: list[str] = []
    for ref in _collect_refs(doc):
        m = _PMID_RE.match(ref.strip())
        if m:
            pmid = m.group(1)
            if pmid not in known_pmids:
                errors.append(
                    f"ref 'PMID:{pmid}' not found in {refs_path.name}. "
                    "Add the reference through the validated ingest path first."
                )
            continue
        m = _DOI_RE.match(ref.strip())
        if m:
            doi = m.group(1).lower()
            if doi not in known_dois:
                errors.append(
                    f"ref 'DOI:{m.group(1)}' not found in {refs_path.name}. "
                    "Add the reference through the validated ingest path first."
                )

    return errors


# ── Edit simulation ────────────────────────────────────────────────────────────

def simulate_edit(tool_name: str, tool_input: dict, file_path: Path) -> str:
    """
    Return the content a file would have after a proposed Claude Code edit tool call.

    Supports Write, Edit, and MultiEdit.
    """
    if tool_name == "Write":
        return tool_input.get("content", "")

    current = file_path.read_text(encoding="utf-8") if file_path.exists() else ""

    if tool_name == "Edit":
        old = tool_input.get("old_string", "")
        new = tool_input.get("new_string", "")
        replace_all = tool_input.get("replace_all", False)
        if old in current:
            return current.replace(old, new) if replace_all else current.replace(old, new, 1)

    elif tool_name == "MultiEdit":
        for edit in tool_input.get("edits", []):
            old = edit.get("old_string", "")
            new = edit.get("new_string", "")
            replace_all = edit.get("replace_all", False)
            if old in current:
                current = current.replace(old, new) if replace_all else current.replace(old, new, 1)

    return current


# ── LinkML schema validation (subprocess) ──────────────────────────────────────

def linkml_validate(content: str, schema_path: Path, original_name: str = "input.yaml") -> tuple[bool, str]:
    """
    Validate YAML content against a LinkML schema.

    Writes content to a temp file and runs linkml-validate as a subprocess.
    Returns (passed: bool, output_text: str).
    """
    if not schema_path.exists():
        return True, f"(schema not found at {schema_path} — linkml-validate skipped)"

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir) / original_name
        tmp.write_text(content, encoding="utf-8")

        result = subprocess.run(
            [
                "uv", "run", "linkml-validate",
                "--schema", str(schema_path),
                "--target-class", "CellTypeMappingGraph",
                str(tmp),
            ],
            capture_output=True,
            text=True,
            cwd=schema_path.parent.parent,  # project root (schema is at root/schema/...)
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode == 0, output
