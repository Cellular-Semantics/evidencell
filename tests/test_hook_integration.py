"""Integration tests for the pre-edit validation hook.

Runs validate_mapping_hook.py as a subprocess to verify exit codes:
  0 → edit allowed
  2 → edit blocked

Tests 1–4 are fast (structural checks only; no linkml-validate subprocess called).
Test 5 is marked @pytest.mark.integration (calls linkml-validate with the real schema).
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

HOOK = (
    Path(__file__).parent.parent / ".claude" / "hooks" / "validate_mapping_hook.py"
)
SCHEMA = Path(__file__).parent.parent / "schema" / "celltype_mapping.yaml"
VALID_KB_FIXTURE = (
    Path(__file__).parent.parent / "kb" / "draft" / "BG" / "GPi_shell_neuron.yaml"
)

# A KB path the hook will intercept (must contain '/kb/' and end in '.yaml')
_FAKE_KB_PATH = "/project/kb/draft/test_hook.yaml"

# Minimal structurally-valid KB YAML (passes structural_checks; not full schema)
_MINIMAL_VALID_YAML = """\
nodes:
  - id: type_a
    name: Type A
  - id: type_b
    name: Type B
edges:
  - id: edge_1
    type_a: type_a
    type_b: type_b
    evidence:
      - corpus_id: "12345"
        snippet: "These cells express parvalbumin and are found in layer IV."
"""


def _run_hook(payload: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
    )


def _write_payload(content: str, file_path: str = _FAKE_KB_PATH) -> dict:
    return {
        "tool_name": "Write",
        "tool_input": {"file_path": file_path, "content": content},
    }


# ── Fast tests (no linkml-validate subprocess) ────────────────────────────────


def test_non_kb_path_passes_through():
    """Hook must exit 0 and skip validation for non-KB files."""
    payload = _write_payload("anything: here", file_path="/project/src/foo.yaml")
    r = _run_hook(payload)
    assert r.returncode == 0, f"Expected 0, got {r.returncode}\n{r.stderr}"


def test_non_yaml_path_passes_through():
    """Hook must exit 0 and skip validation for non-.yaml KB paths."""
    payload = _write_payload("whatever", file_path="/project/kb/mappings/foo.json")
    r = _run_hook(payload)
    assert r.returncode == 0, f"Expected 0, got {r.returncode}\n{r.stderr}"


def test_non_edit_tool_passes_through():
    """Hook must exit 0 for tool names that are not Write/Edit/MultiEdit."""
    payload = {"tool_name": "Read", "tool_input": {"file_path": _FAKE_KB_PATH}}
    r = _run_hook(payload)
    assert r.returncode == 0, f"Expected 0, got {r.returncode}\n{r.stderr}"


def test_empty_evidence_list_blocked():
    """Edge with empty evidence list must be blocked (exit 2)."""
    bad_yaml = """\
nodes:
  - id: type_a
    name: Type A
  - id: type_b
    name: Type B
edges:
  - id: edge_1
    type_a: type_a
    type_b: type_b
    evidence: []
"""
    r = _run_hook(_write_payload(bad_yaml))
    assert r.returncode == 2, (
        f"Expected exit 2 for empty evidence, got {r.returncode}\n{r.stderr}"
    )


def test_placeholder_snippet_blocked():
    """Edge with a placeholder snippet must be blocked (exit 2)."""
    bad_yaml = """\
nodes:
  - id: type_a
    name: Type A
  - id: type_b
    name: Type B
edges:
  - id: edge_1
    type_a: type_a
    type_b: type_b
    evidence:
      - corpus_id: "12345"
        snippet: "TODO: add snippet"
"""
    r = _run_hook(_write_payload(bad_yaml))
    assert r.returncode == 2, (
        f"Expected exit 2 for placeholder snippet, got {r.returncode}\n{r.stderr}"
    )


def test_dangling_edge_reference_blocked():
    """Edge referencing a non-existent node must be blocked (exit 2)."""
    bad_yaml = """\
nodes:
  - id: type_a
    name: Type A
edges:
  - id: edge_1
    type_a: type_a
    type_b: NONEXISTENT
    evidence:
      - corpus_id: "12345"
        snippet: "Some real text."
"""
    r = _run_hook(_write_payload(bad_yaml))
    assert r.returncode == 2, (
        f"Expected exit 2 for dangling edge reference, got {r.returncode}\n{r.stderr}"
    )


def test_invalid_yaml_syntax_blocked():
    """Syntactically invalid YAML must be blocked (exit 2)."""
    bad_yaml = "nodes: [\nunclosed bracket"
    r = _run_hook(_write_payload(bad_yaml))
    assert r.returncode == 2, (
        f"Expected exit 2 for invalid YAML syntax, got {r.returncode}\n{r.stderr}"
    )


# ── Quote key and PMID provenance checks ─────────────────────────────────────


def _make_refs_and_yaml(tmp_path: Path, yaml_content: str) -> tuple[str, dict]:
    """Create a kb/draft/ dir with references.json; return file_path string + payload."""
    kb_dir = tmp_path / "kb" / "draft"
    kb_dir.mkdir(parents=True)
    refs = {
        "201041756": {
            "corpus_id": "201041756",
            "pmid": "31420995",
            "doi": "10.1111/ejn.14606",
            "quotes": {
                "201041756_aabb1234": {"text": "OLM cells express Sst.", "claims": ["sst_positive"]},
            },
        }
    }
    (kb_dir / "references.json").write_text(json.dumps(refs))
    yaml_path = kb_dir / "test.yaml"
    yaml_path.write_text(yaml_content)
    return str(yaml_path), _write_payload(yaml_content, file_path=str(yaml_path))


def test_missing_quote_key_blocked(tmp_path: Path):
    """A quote_key not in references.json must block the write (exit 2)."""
    yaml_content = """\
nodes:
  - id: type_a
    name: Type A
    defining_markers:
      - symbol: Sst
        sources:
          - ref: "PMID:31420995"
            quote_key: "INVENTED_KEY_deadbeef00"
  - id: type_b
    name: Type B
edges:
  - id: edge_1
    type_a: type_a
    type_b: type_b
    evidence:
      - corpus_id: "12345"
        snippet: "Real text."
"""
    _, payload = _make_refs_and_yaml(tmp_path, yaml_content)
    r = _run_hook(payload)
    assert r.returncode == 2, f"Expected exit 2 for missing quote_key, got {r.returncode}\n{r.stderr}"


def test_hallucinated_pmid_ref_blocked(tmp_path: Path):
    """A PMID: ref not in references.json must block the write (exit 2)."""
    yaml_content = """\
nodes:
  - id: type_a
    name: Type A
    defining_markers:
      - symbol: FakeMarker
        sources:
          - ref: "PMID:00000001"
  - id: type_b
    name: Type B
edges:
  - id: edge_1
    type_a: type_a
    type_b: type_b
    evidence:
      - corpus_id: "12345"
        snippet: "Real text."
"""
    _, payload = _make_refs_and_yaml(tmp_path, yaml_content)
    r = _run_hook(payload)
    assert r.returncode == 2, (
        f"Expected exit 2 for hallucinated PMID, got {r.returncode}\n{r.stderr}"
    )


# ── Integration test (calls linkml-validate subprocess) ───────────────────────


@pytest.mark.integration
def test_valid_kb_file_passes():
    """A known-good KB file must be allowed through the full validation stack.

    Calls linkml-validate with the real schema. Requires schema and all deps installed.
    """
    if not SCHEMA.exists():
        pytest.skip("Schema file not found — run from evidencell/ root")
    if not VALID_KB_FIXTURE.exists():
        pytest.skip(f"Fixture file not found: {VALID_KB_FIXTURE}")

    content = VALID_KB_FIXTURE.read_text()
    r = _run_hook(_write_payload(content))
    assert r.returncode == 0, (
        f"Expected exit 0 for valid KB file, got {r.returncode}\n{r.stderr}"
    )
