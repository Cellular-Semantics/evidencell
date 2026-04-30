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

def _target_class_for_kb_path(file_path: Path) -> str | None:
    """
    Pick the LinkML target_class for a KB YAML file by its location.

    Returns None if the file is in a path with no schema class (validation skipped).
    """
    parts = file_path.parts
    try:
        kb_idx = parts.index("kb")
    except ValueError:
        return "CellTypeMappingGraph"

    sub = parts[kb_idx + 1] if kb_idx + 1 < len(parts) else ""
    name = file_path.name

    if sub == "datasets":
        return "BulkDataset"
    if sub == "correlation_runs":
        if name == "manifest.yaml":
            return "CorrelationRun"
        return None
    if sub == "annotation_transfer_runs":
        if name == "manifest.yaml":
            return "AnnotationTransferRun"
        return None
    if sub == "taxonomy":
        if name in {"cluster.yaml", "supertype.yaml", "subclass.yaml",
                    "class.yaml", "neurotransmitter.yaml"}:
            return "TaxonomyNodeList"
        return None
    return "CellTypeMappingGraph"


def linkml_validate(
    content: str,
    schema_path: Path,
    original_name: str = "input.yaml",
    file_path: Path | None = None,
) -> tuple[bool, str]:
    """
    Validate YAML content against a LinkML schema.

    Writes content to a temp file and runs linkml-validate as a subprocess.
    The target_class is chosen by file_path location when provided; defaults
    to CellTypeMappingGraph otherwise.

    Returns (passed: bool, output_text: str).
    """
    if not schema_path.exists():
        return True, f"(schema not found at {schema_path} — linkml-validate skipped)"

    if file_path is not None:
        target_class = _target_class_for_kb_path(file_path)
        if target_class is None:
            return True, f"(no schema class for {file_path} — linkml-validate skipped)"
    else:
        target_class = "CellTypeMappingGraph"

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir) / original_name
        tmp.write_text(content, encoding="utf-8")

        result = subprocess.run(
            [
                "uv", "run", "linkml-validate",
                "--schema", str(schema_path),
                "--target-class", target_class,
                str(tmp),
            ],
            capture_output=True,
            text=True,
            cwd=schema_path.parent.parent,  # project root (schema is at root/schema/...)
        )
        output = (result.stdout + result.stderr).strip()
        return result.returncode == 0, output


# ── Markdown annotation parsing ────────────────────────────────────────────────

# Blockquote attribution line: starts with `> —` (em-dash)
_MD_ATTRIBUTION_RE = re.compile(r"^>\s*[—–-]")
# Hidden quote key annotation: <!-- quote_key: X -->
_MD_QUOTE_KEY_RE = re.compile(r"<!--\s*quote_key:\s*(\S+)\s*-->")
# Ontology CURIEs: [PREFIX:digits]  e.g. [UBERON:0014548]
_MD_CURIE_RE = re.compile(r"\[([A-Z]+:\d+)\]")
# Atlas cluster accessions: [CS...] (upper-alpha-numeric + underscore)
_MD_ACCESSION_RE = re.compile(r"\[(CS[A-Z0-9_]+)\]")
# PMID from pubmed hyperlink in reference table: [digits](https://pubmed...)
_MD_PMID_RE = re.compile(r"\[(\d{7,9})\]\(https://pubmed")
# Numbered reference label at the start of a references-table row:
# `| [3] | Author 2024 | ... |`
_MD_REF_TABLE_LABEL_RE = re.compile(r"^\|\s*\[(\d+)\]\s*\|")
# Numbered reference cite anywhere in text: `[3]`. Used to detect attributions
# like `> — Knoedler et al. 2022 · [3]`. Distinct from CURIE and accession
# patterns above.
_MD_NUMBERED_REF_CITE_RE = re.compile(r"\[(\d+)\]")


def parse_md_annotations(text: str) -> dict:
    """
    Parse machine-readable annotations embedded in a Markdown report.

    A blockquote block is considered validly annotated if EITHER:
      (a) it contains a `<!-- quote_key: X -->` annotation (verbatim-quote
          path; X is validated against references.json), OR
      (b) it carries an attribution line `> — ...` containing a numbered
          reference cite `[N]` where N matches a row in the report's
          References table (authored-prose path; trades text-content
          validation for visible numbered-ref provenance).

    Blocks meeting neither criterion are flagged in `unannotated_blockquotes`.

    Returns a dict with:
      quote_keys             — list of quote_key values from <!-- quote_key: X --> on > lines
      unannotated_blockquotes— blockquote blocks with no acceptable attribution
                               (represented by first content line of each block)
      curie_ids              — list of [PREFIX:digits] CURIEs found anywhere in text
      accessions             — list of [CS...] atlas accessions found anywhere
      pmids                  — list of PMIDs from PubMed hyperlinks in reference table
      ref_table_labels       — set of numbered ref labels declared in the References table
    """
    quote_keys: list[str] = []
    unannotated_blockquotes: list[str] = []
    curie_ids: list[str] = []
    accessions: list[str] = []
    pmids: list[str] = []
    ref_table_labels: set[str] = set()

    lines = text.splitlines()

    # Pass 1a: extract CURIEs, accessions, PMIDs from every line; collect
    # numbered ref labels from any `| [N] | ... |` table row (typically the
    # References table at the bottom of the report).
    for line in lines:
        curie_ids.extend(_MD_CURIE_RE.findall(line))
        accessions.extend(_MD_ACCESSION_RE.findall(line))
        pmids.extend(_MD_PMID_RE.findall(line))
        m = _MD_REF_TABLE_LABEL_RE.match(line)
        if m:
            ref_table_labels.add(m.group(1))

    # Pass 2: blockquote blocks — check for an acceptable annotation
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith(">"):
            # Collect entire contiguous blockquote block
            block_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block_lines.append(lines[i].strip())
                i += 1

            # Extract all quote keys from the block (path (a))
            block_has_key = False
            for bl in block_lines:
                qk_match = _MD_QUOTE_KEY_RE.search(bl)
                if qk_match:
                    quote_keys.append(qk_match.group(1))
                    block_has_key = True

            # If no quote_key, look for a numbered-ref cite on the
            # attribution line(s) (path (b)).
            block_has_numbered_ref = False
            if not block_has_key:
                for bl in block_lines:
                    if not _MD_ATTRIBUTION_RE.match(bl):
                        continue
                    nums = _MD_NUMBERED_REF_CITE_RE.findall(bl)
                    if any(n in ref_table_labels for n in nums):
                        block_has_numbered_ref = True
                        break

            # Flag if neither annotation form is present
            if not block_has_key and not block_has_numbered_ref:
                representative = next(
                    (bl for bl in block_lines if not _MD_ATTRIBUTION_RE.match(bl)),
                    block_lines[0],
                )
                unannotated_blockquotes.append(representative)
        else:
            i += 1

    return {
        "quote_keys": quote_keys,
        "unannotated_blockquotes": unannotated_blockquotes,
        "curie_ids": curie_ids,
        "accessions": accessions,
        "pmids": pmids,
        "ref_table_labels": ref_table_labels,
    }


def check_md_ids(
    annotations: dict,
    refs_path: Path,
    kb_nodes: dict | None = None,
) -> list[str]:
    """
    Validate machine-readable annotations extracted by parse_md_annotations().

    Checks performed (silently skipped when the backing cache does not exist):
      1. Unannotated blockquotes — always an error
      2. quote_keys — existence in references.json
      3. pmids — existence in references.json
      4. curie_ids — if term_index.json exists beside refs_path
      5. accessions — if kb_nodes dict provided
      6. gene_symbols — (reserved; not yet implemented)

    Returns list of error strings; empty = OK.
    """
    errors: list[str] = []

    # 1. Unannotated blockquotes — unconditional
    for line in annotations.get("unannotated_blockquotes", []):
        errors.append(
            f"Unannotated blockquote (missing '<!-- quote_key: X -->' annotation): {line[:80]}"
        )

    # Load references.json once if it exists
    refs: dict | None = None
    if refs_path.exists():
        try:
            refs = json.loads(refs_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            errors.append(f"Could not read {refs_path.name} — ensure it is valid JSON")

    if refs is not None:
        # Build lookup sets
        known_quote_keys: set[str] = set()
        known_pmids: set[str] = set()
        known_dois: set[str] = set()
        for entry in refs.values():
            if not isinstance(entry, dict):
                continue
            known_quote_keys.update(entry.get("quotes", {}).keys())
            if pmid := entry.get("pmid"):
                known_pmids.add(str(pmid))
            if doi := entry.get("doi"):
                known_dois.add(doi.lower())

        # 2. quote_keys
        for qk in annotations.get("quote_keys", []):
            if qk not in known_quote_keys:
                errors.append(
                    f"quote_key '{qk}' not found in {refs_path.name}. "
                    "Add the quote through the validated ingest path before referencing it."
                )

        # 3. pmids
        for pmid in annotations.get("pmids", []):
            if pmid not in known_pmids:
                errors.append(
                    f"PMID '{pmid}' not found in {refs_path.name}. "
                    "Add the reference through the validated ingest path first."
                )

    # 4. curie_ids — checked against term_index.json if present
    term_index_path = refs_path.parent / "term_index.json"
    if term_index_path.exists() and annotations.get("curie_ids"):
        try:
            term_index: dict = json.loads(term_index_path.read_text(encoding="utf-8"))
            for curie in annotations["curie_ids"]:
                if curie not in term_index:
                    errors.append(
                        f"Ontology term '{curie}' not found in term_index.json. "
                        "Verify the term with runoak before using it."
                    )
        except (json.JSONDecodeError, OSError):
            pass  # Corrupt index — skip silently; not a report author's fault

    # 5. accessions — checked against kb_nodes if provided
    if kb_nodes is not None:
        for acc in annotations.get("accessions", []):
            if acc not in kb_nodes:
                errors.append(
                    f"Atlas accession '{acc}' not found in KB nodes. "
                    "Check the accession against the taxonomy."
                )

    return errors
