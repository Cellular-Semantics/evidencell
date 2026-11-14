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
    Path(__file__).parent.parent / "kb" / "graphs" / "BG" / "classical_gpi_shell.yaml"
)

# A KB path the hook will intercept (must contain '/kb/' and end in '.yaml')
_FAKE_KB_PATH = "/project/kb/graphs/test_hook.yaml"

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
    payload = _write_payload("whatever", file_path="/project/kb/graphs/foo.json")
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


def _split(region_dir, store):
    """Write a store in the split layout from a legacy-shaped dict."""
    (region_dir / "papers").mkdir(parents=True, exist_ok=True)
    (region_dir / "quotes").mkdir(parents=True, exist_ok=True)
    for cid, entry in store.items():
        if not isinstance(entry, dict):
            continue
        paper = {k: v for k, v in entry.items() if k != "quotes"}
        paper.setdefault("corpus_id", cid)
        (region_dir / "papers" / f"{cid}.json").write_text(json.dumps(paper))
        (region_dir / "quotes" / f"{cid}.json").write_text(
            json.dumps(entry.get("quotes") or {}))


def _make_refs_and_yaml(tmp_path: Path, yaml_content: str) -> tuple[str, dict]:
    """Create kb/graphs/{region}/ with YAML plus a split reference store."""
    region = "test_region"
    kb_dir = tmp_path / "kb" / "graphs" / region
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
    _split(refs_dir, refs)
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
    """Create reports/{region}/ plus a split reference store; return payload."""
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
    _split(refs_dir, refs)
    md_path = reports_dir / "test_report.md"
    md_path.write_text(md_content)
    return _write_payload(md_content, file_path=str(md_path))


def test_md_non_report_path_passes(tmp_path: Path):
    """A .md file NOT in a reports/ subdir must pass through (exit 0)."""
    md_path = tmp_path / "kb" / "graphs" / "notes.md"
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


def test_curation_blocks_workflows_write_for_untrusted_user():
    """Untrusted user writing under workflows/ must be blocked (exit 2).

    Workflows define the curation process (gates, sequencing, subagent
    prompts); they are maintainer artifacts, not curator-editable.
    """
    payload = _write_payload(
        "# edited orchestrator\n",
        file_path="/project/workflows/evidence-extraction.md",
    )
    r = _run_hook(payload, user="")
    assert r.returncode == 2, (
        f"Expected exit 2 for workflows/ write, got {r.returncode}\n{r.stderr}"
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


# ── Term-reference validation ──────────────────────────────────────────────────


def _run_hook_with_env(
    payload: dict,
    extra_env: dict[str, str],
    user: str | None = "dosumis@gmail.com",
) -> subprocess.CompletedProcess:
    """Run the hook with extra env vars (e.g. EVIDENCELL_SKIP_TERM_CHECK=1)."""
    env = os.environ.copy()
    if user is not None:
        env["EVIDENCELL_HOOK_USER"] = user
    env.update(extra_env)
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        env=env,
    )


def test_term_check_bypass_env_short_circuits():
    """EVIDENCELL_SKIP_TERM_CHECK=1 prints a bypass notice and skips term validation.

    Structural checks still run, so a structurally-valid YAML should pass even
    if the term check would have rejected it.
    """
    payload = _write_payload(_MINIMAL_VALID_YAML)
    r = _run_hook_with_env(payload, {"EVIDENCELL_SKIP_TERM_CHECK": "1"})
    # Hook should print the bypass notice
    assert "bypassed" in r.stderr.lower() or "term check" in r.stderr.lower()
    # And should not have invoked validate_terms (no "term check skipped: OAK" message)
    # We do *not* assert exit code here because LinkML schema check may still
    # fire and either pass or skip; this test isolates the bypass path.


def test_term_check_skipped_when_oak_dbs_missing(tmp_path: Path, monkeypatch):
    """Soft-skip path: when no OAK DBs are cached, the hook still allows the
    write but emits the informational `[term check skipped: ...]` message.

    Exercised by pointing PYSTOW_HOME at an empty tmp dir so the semsql
    lookup finds no DB files.
    """
    payload = _write_payload(_MINIMAL_VALID_YAML)
    # Empty pystow home → no .data/semsql/sqlite/*.db files
    fake_home = tmp_path / "pystow_home"
    fake_home.mkdir()
    r = _run_hook_with_env(payload, {"PYSTOW_HOME": str(fake_home)})
    # The skipped message should appear (assuming conf/oak_config.yaml is
    # present in the project — it is, so the function gets past the first
    # short-circuit and into the missing-DB branch).
    assert (
        "term check skipped" in r.stderr.lower()
        or "fetch-oak-dbs" in r.stderr.lower()
    )


def _oak_dbs_ready() -> tuple[bool, str]:
    """Check whether the local OAK DBs needed for binding validation are
    cached. Returns (ready, missing_description).
    """
    import pystow
    project_root = Path(__file__).parent.parent
    missing: list[str] = []
    for name in ("cl", "uberon"):
        if not pystow.join("oaklib", name=f"{name}.db").exists():
            missing.append(name)
    for fname in ("taxslim.obo", "mbao.obo"):
        if not (project_root / "conf" / "oak_dbs" / fname).exists():
            missing.append(fname)
    return (not missing), ", ".join(missing)


@pytest.mark.integration
@pytest.mark.parametrize(
    "real_curie,bad_curie,expect_substr",
    [
        # CL slot: cl_mapping.cl_term — bogus ID should fail the CLClassTerm binding.
        ("CL:4310096", "CL:9999999999", "CL:9999999999"),
        # NCBITaxon slot: species — bogus ID should fail NCBITaxonClassTerm.
        ("NCBITaxon:9443", "NCBITaxon:9999999999", "NCBITaxon:9999999999"),
        # Anatomy slot: brain_region — bogus UBERON should fail AnatomyTerm.
        # Use the brain_region CURIE actually present in the fixture (DHBA:10344).
        ("DHBA:10344", "UBERON:9999999999", "UBERON:9999999999"),
    ],
    ids=["bogus_CL", "bogus_NCBITaxon", "bogus_UBERON"],
)
def test_term_check_rejects_bad_curie(real_curie: str, bad_curie: str, expect_substr: str):
    """End-to-end: when OAK DBs are warm, the hook blocks writes containing
    a CURIE that doesn't resolve in the bound ontology. Marked integration
    because it requires CL + UBERON semsql DBs cached locally plus the
    NCBITaxon / MBA file-adapter OBOs fetched by `just fetch-oak-dbs`.
    """
    if not SCHEMA.exists():
        pytest.skip("Schema file not found — run from evidencell/ root")
    if not VALID_KB_FIXTURE.exists():
        pytest.skip(f"Fixture file not found: {VALID_KB_FIXTURE}")
    ready, missing = _oak_dbs_ready()
    if not ready:
        pytest.skip(f"OAK DBs missing: {missing}; run `just fetch-oak-dbs`")

    content = VALID_KB_FIXTURE.read_text()
    if real_curie not in content:
        pytest.skip(f"Fixture does not contain expected real CURIE {real_curie}")
    bad_content = content.replace(real_curie, bad_curie)

    r = _run_hook(_write_payload(bad_content))
    assert r.returncode == 2, (
        f"Expected exit 2 for bogus CURIE {bad_curie}, got {r.returncode}\n{r.stderr}"
    )
    assert expect_substr in r.stderr, (
        f"Expected stderr to mention {expect_substr}, got:\n{r.stderr}"
    )


@pytest.mark.integration
def test_term_check_rejects_label_mismatch():
    """An OntologyTerm whose label disagrees with OAK's canonical fires a
    BindingValidationPlugin label_mismatch and is reported (exit non-zero).
    """
    if not SCHEMA.exists():
        pytest.skip("Schema file not found — run from evidencell/ root")
    if not VALID_KB_FIXTURE.exists():
        pytest.skip(f"Fixture file not found: {VALID_KB_FIXTURE}")
    ready, missing = _oak_dbs_ready()
    if not ready:
        pytest.skip(f"OAK DBs missing: {missing}; run `just fetch-oak-dbs`")

    content = VALID_KB_FIXTURE.read_text()
    # Swap the canonical species label "Primates" for a wrong one while
    # leaving NCBITaxon:9443 in place — exactly the wrong-name-for-right-ID
    # hallucination shape.
    bad_content = content.replace(
        "{id: NCBITaxon:9443, label: Primates, name_in_source: Primates}",
        "{id: NCBITaxon:9443, label: Rodentia, name_in_source: Primates}",
    )
    if bad_content == content:
        pytest.skip("Fixture did not contain expected NCBITaxon Primates triple")

    r = _run_hook(_write_payload(bad_content))
    assert r.returncode == 2, (
        f"Expected exit 2 for label mismatch, got {r.returncode}\n{r.stderr}"
    )
    assert "Label mismatch" in r.stderr or "label" in r.stderr.lower(), (
        f"Expected stderr to mention label mismatch, got:\n{r.stderr}"
    )


# ── Reference-store writes: split layout (issue #168) ─────────────────────────
#
# Each file under references/{region}/{papers,quotes}/ is validated against its
# own schema class. The regression this guards: the hook used to rebuild the
# retired monolith shape from a quotes file alone and then fail every quotes
# write on the paper fields the quotes file never carried.

from evidencell.references import compute_quote_key  # noqa: E402

_CID = "10060696"
_PAPER = {
    "corpus_id": _CID,
    "title": "A paper",
    "year": 2015,
    "authors": ["A. Author", "B. Author"],
    "author_keys": ["Author et al., 2015"],
    "doi": "10.1000/x",
    "pmid": "12345678",
    "resolution_confidence": "HIGH",
}


def _quote(text: str, **over) -> tuple[str, dict]:
    q = {"text": text, "section": "Results", "claims": [], "status": "pending"}
    q.update(over)
    return compute_quote_key(_CID, text), q


def _refs_region(tmp_path: Path, *, paper: dict | None = _PAPER, quotes: dict | None = None):
    """Create references/{region}/ with an optional paper + quotes file for _CID."""
    region_dir = tmp_path / "references" / "test_region"
    (region_dir / "papers").mkdir(parents=True)
    (region_dir / "quotes").mkdir(parents=True)
    if paper is not None:
        (region_dir / "papers" / f"{_CID}.json").write_text(json.dumps(paper))
    if quotes is None:
        k, q = _quote("These cells express parvalbumin.")
        quotes = {k: q}
    (region_dir / "quotes" / f"{_CID}.json").write_text(json.dumps(quotes))
    return region_dir, quotes


def _hook_write(path: Path, payload: dict) -> subprocess.CompletedProcess:
    return _run_hook(_write_payload(json.dumps(payload, indent=2), file_path=str(path)))


def test_refs_unchanged_quotes_rewrite_passes(tmp_path: Path):
    """Regression for #168: a no-op rewrite of quotes/{cid}.json must pass clean."""
    region_dir, quotes = _refs_region(tmp_path)
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", quotes)
    assert r.returncode == 0, r.stderr
    assert "Field required" not in r.stderr
    assert "WARNING" not in r.stderr


def test_refs_claims_only_edit_passes(tmp_path: Path):
    region_dir, quotes = _refs_region(tmp_path)
    new = json.loads(json.dumps(quotes))
    next(iter(new.values()))["claims"] = ["defining_markers"]
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", new)
    assert r.returncode == 0, r.stderr
    assert "WARNING" not in r.stderr


def test_refs_quotes_write_with_missing_paper_warns_but_passes(tmp_path: Path):
    region_dir, quotes = _refs_region(tmp_path, paper=None)
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", quotes)
    assert r.returncode == 0, r.stderr
    assert "WARNING" in r.stderr
    assert "no paper record" in r.stderr
    assert "load_store()" in r.stderr
    assert f"just fetch-reference CorpusId:{_CID}" in r.stderr


def test_refs_quotes_write_with_invalid_paper_warns_naming_field(tmp_path: Path):
    bad_paper = dict(_PAPER, year=None)
    region_dir, quotes = _refs_region(tmp_path, paper=bad_paper)
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", quotes)
    assert r.returncode == 0, r.stderr
    assert "WARNING" in r.stderr
    assert "year" in r.stderr
    assert f"just fetch-reference CorpusId:{_CID}" in r.stderr


def test_refs_quotes_text_change_without_rekey_blocked(tmp_path: Path):
    region_dir, quotes = _refs_region(tmp_path)
    new = json.loads(json.dumps(quotes))
    next(iter(new.values()))["text"] = "These cells express somatostatin."
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", new)
    assert r.returncode == 2
    assert "does not match its text" in r.stderr


def test_refs_quotes_text_change_with_rekey_blocked_as_removal(tmp_path: Path):
    """Re-keying is just drop + add; the drop is what the guard sees."""
    region_dir, quotes = _refs_region(tmp_path)
    k, q = _quote("These cells express somatostatin.")
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", {k: q})
    assert r.returncode == 2
    assert "would be removed" in r.stderr


def test_refs_quotes_drop_key_blocked(tmp_path: Path):
    k1, q1 = _quote("First passage.")
    k2, q2 = _quote("Second passage.")
    region_dir, _ = _refs_region(tmp_path, quotes={k1: q1, k2: q2})
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", {k1: q1})
    assert r.returncode == 2
    assert "would be removed" in r.stderr


def test_refs_quotes_add_key_passes(tmp_path: Path):
    region_dir, quotes = _refs_region(tmp_path)
    k2, q2 = _quote("Second passage.")
    r = _hook_write(region_dir / "quotes" / f"{_CID}.json", {**quotes, k2: q2})
    assert r.returncode == 0, r.stderr


def test_refs_quotes_non_object_blocked(tmp_path: Path):
    region_dir, _ = _refs_region(tmp_path)
    r = _run_hook(_write_payload("[]", file_path=str(region_dir / "quotes" / f"{_CID}.json")))
    assert r.returncode == 2


def test_refs_paper_title_change_blocked(tmp_path: Path):
    region_dir, _ = _refs_region(tmp_path)
    r = _hook_write(region_dir / "papers" / f"{_CID}.json", dict(_PAPER, title="Other"))
    assert r.returncode == 2
    assert "identity field 'title'" in r.stderr


def test_refs_paper_authors_change_blocked(tmp_path: Path):
    region_dir, _ = _refs_region(tmp_path)
    r = _hook_write(region_dir / "papers" / f"{_CID}.json", dict(_PAPER, authors=["Z. Other"]))
    assert r.returncode == 2
    assert "identity field 'authors'" in r.stderr


def test_refs_paper_add_missing_venue_passes(tmp_path: Path):
    region_dir, _ = _refs_region(tmp_path)
    r = _hook_write(region_dir / "papers" / f"{_CID}.json", dict(_PAPER, venue="J. Neurosci."))
    assert r.returncode == 0, r.stderr


def test_refs_paper_repair_fills_absent_identity_field(tmp_path: Path):
    """The follow-up repair after a quotes-write warning: filling a missing
    year on an incomplete record is allowed; it is not an identity change."""
    incomplete = {k: v for k, v in _PAPER.items() if k != "year"}
    region_dir, _ = _refs_region(tmp_path, paper=incomplete)
    r = _hook_write(region_dir / "papers" / f"{_CID}.json", _PAPER)
    assert r.returncode == 0, r.stderr


def test_refs_paper_missing_authors_blocked(tmp_path: Path):
    region_dir, _ = _refs_region(tmp_path)
    bad = {k: v for k, v in _PAPER.items() if k != "authors"}
    r = _hook_write(region_dir / "papers" / f"{_CID}.json", bad)
    assert r.returncode == 2
    assert "authors" in r.stderr


def test_refs_paper_corpus_id_stem_mismatch_blocked(tmp_path: Path):
    region_dir, _ = _refs_region(tmp_path)
    r = _hook_write(region_dir / "papers" / "99999.json", _PAPER)
    assert r.returncode == 2
