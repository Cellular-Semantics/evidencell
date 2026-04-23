"""Integration tests for the pre-edit validation hook.

Runs validate_mapping_hook.py as a subprocess to verify exit codes:
  0 → edit allowed
  2 → edit blocked

Tests 1–4 are fast (structural checks only; no linkml-validate subprocess called).
Test 5 is marked @pytest.mark.integration (calls linkml-validate with the real schema).
"""

import json
import os
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


def _run_hook(
    payload: dict, user: str | None = "dosumis@gmail.com"
) -> subprocess.CompletedProcess:
    """Run the hook subprocess.

    `user` controls the curation-mode gate:
      - default "dosumis@gmail.com" — trusted; curation gate bypassed (mirrors dev use)
      - ""                          — untrusted with no git email; gate active
      - "other@example.com"         — untrusted with a non-trusted email; gate active
      - None                        — ambient: fall through to real `git config user.email`
    """
    env = os.environ.copy()
    if user is not None:
        env["EVIDENCELL_HOOK_USER"] = user
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env=env,
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
    """Create kb/draft/{region}/ with YAML + references/{region}/references.json."""
    region = "test_region"
    kb_dir = tmp_path / "kb" / "draft" / region
    kb_dir.mkdir(parents=True)
    refs_dir = tmp_path / "references" / region
    refs_dir.mkdir(parents=True)
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
    (refs_dir / "references.json").write_text(json.dumps(refs))
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


# ── Markdown report hook tests ────────────────────────────────────────────────


def _make_refs_and_md(tmp_path: Path, md_content: str) -> dict:
    """Create reports/{region}/ dir with references/{region}/references.json; return payload."""
    region = "test_region"
    reports_dir = tmp_path / "reports" / region
    reports_dir.mkdir(parents=True)
    refs_dir = tmp_path / "references" / region
    refs_dir.mkdir(parents=True)
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
    (refs_dir / "references.json").write_text(json.dumps(refs))
    md_path = reports_dir / "test_report.md"
    md_path.write_text(md_content)
    return _write_payload(md_content, file_path=str(md_path))


def test_md_non_report_path_passes(tmp_path: Path):
    """A .md file NOT in a reports/ subdir must pass through (exit 0)."""
    md_path = tmp_path / "kb" / "draft" / "notes.md"
    md_path.parent.mkdir(parents=True)
    md_path.write_text("# Just some notes\n")
    payload = _write_payload("# Just some notes\n", file_path=str(md_path))
    r = _run_hook(payload)
    assert r.returncode == 0, f"Expected 0 for non-report md, got {r.returncode}\n{r.stderr}"


def test_md_report_unannotated_blockquote_blocked(tmp_path: Path):
    """A .md report with a bare blockquote (no quote_key comment) must be blocked (exit 2)."""
    md_content = """\
# Test Report

> This blockquote has no annotation.
"""
    payload = _make_refs_and_md(tmp_path, md_content)
    r = _run_hook(payload)
    assert r.returncode == 2, (
        f"Expected exit 2 for unannotated blockquote, got {r.returncode}\n{r.stderr}"
    )


def test_md_report_bad_quote_key_blocked(tmp_path: Path):
    """A .md report with a quote_key not in references.json must be blocked (exit 2)."""
    md_content = """\
# Test Report

> Some text.
> — Author et al. 2020, §1 · [1] <!-- quote_key: INVENTED_KEY_deadbeef -->
"""
    payload = _make_refs_and_md(tmp_path, md_content)
    r = _run_hook(payload)
    assert r.returncode == 2, (
        f"Expected exit 2 for bad quote_key in md, got {r.returncode}\n{r.stderr}"
    )


def test_md_report_valid_annotation_passes(tmp_path: Path):
    """A .md report with all valid annotations must pass (exit 0)."""
    md_content = """\
# Test Report

> OLM cells express Sst.
> — Winterer et al. 2019, Results §3.3 · [1] <!-- quote_key: 201041756_aabb1234 -->
"""
    payload = _make_refs_and_md(tmp_path, md_content)
    r = _run_hook(payload)
    assert r.returncode == 0, (
        f"Expected exit 0 for valid md report, got {r.returncode}\n{r.stderr}"
    )


# ── Curation-mode gate tests ──────────────────────────────────────────────────


def test_curation_blocks_src_write_for_untrusted_user():
    """Untrusted user writing to src/ must be blocked (exit 2)."""
    payload = _write_payload(
        "print('hi')\n", file_path="/project/src/evidencell/foo.py"
    )
    r = _run_hook(payload, user="")
    assert r.returncode == 2, (
        f"Expected exit 2 for src/ write, got {r.returncode}\n{r.stderr}"
    )
    assert "curation mode" in r.stderr.lower()
    assert "src/" in r.stderr


def test_curation_blocks_schema_write_for_untrusted_user():
    """Untrusted user writing to schema/ must be blocked (exit 2) with schema note."""
    payload = _write_payload(
        "id: https://w3id.org/example\n",
        file_path="/project/schema/celltype_mapping.yaml",
    )
    r = _run_hook(payload, user="")
    assert r.returncode == 2, (
        f"Expected exit 2 for schema/ write, got {r.returncode}\n{r.stderr}"
    )
    assert "SCHEMA NOTE" in r.stderr, (
        f"Expected schema-edit guidance in stderr, got:\n{r.stderr}"
    )


def test_curation_blocks_justfile_write_for_untrusted_user():
    """Untrusted user writing to justfile must be blocked (exit 2)."""
    payload = _write_payload(
        "foo:\n\techo hi\n", file_path="/project/justfile"
    )
    r = _run_hook(payload, user="")
    assert r.returncode == 2, (
        f"Expected exit 2 for justfile write, got {r.returncode}\n{r.stderr}"
    )


def test_curation_blocks_dot_claude_write_for_untrusted_user():
    """Untrusted user writing under .claude/ must be blocked (exit 2).

    Covers the self-modification bypass: editing the hook itself, settings,
    or skills to disable or evade the curation-mode gate.
    """
    for path in (
        "/project/.claude/hooks/validate_mapping_hook.py",
        "/project/.claude/settings.json",
        "/project/.claude/skills/some_skill.md",
    ):
        payload = _write_payload("x\n", file_path=path)
        r = _run_hook(payload, user="")
        assert r.returncode == 2, (
            f"Expected exit 2 for {path}, got {r.returncode}\n{r.stderr}"
        )


def test_curation_allows_untrusted_non_blocked_write():
    """Untrusted user writing to a path outside the blocked zones passes through."""
    payload = _write_payload(
        "# just notes\n", file_path="/project/docs/foo.md"
    )
    r = _run_hook(payload, user="")
    assert r.returncode == 0, (
        f"Expected exit 0 for non-blocked path, got {r.returncode}\n{r.stderr}"
    )


def test_curation_trusted_user_allowed_src_write():
    """Trusted user writing to src/ must pass the curation gate (exit 0)."""
    payload = _write_payload(
        "print('hi')\n", file_path="/project/src/evidencell/foo.py"
    )
    r = _run_hook(payload, user="dosumis@gmail.com")
    assert r.returncode == 0, (
        f"Expected exit 0 for trusted src write, got {r.returncode}\n{r.stderr}"
    )


def test_curation_non_trusted_email_still_blocked():
    """A non-trusted git email must still be treated as untrusted."""
    payload = _write_payload(
        "print('hi')\n", file_path="/project/src/evidencell/foo.py"
    )
    r = _run_hook(payload, user="stranger@example.com")
    assert r.returncode == 2, (
        f"Expected exit 2 for non-trusted email, got {r.returncode}\n{r.stderr}"
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
