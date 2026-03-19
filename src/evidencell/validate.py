# validate.py — structural validation logic for KB YAML files
#
# Wraps linkml-validate and provides structural integrity checks.
# Imported by .claude/hooks/check_mapping_edit.py and by pytest.
# Will grow in M2+ to include snippet provenance checks.

from __future__ import annotations

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
