"""
Integration tests: all KB YAML examples pass linkml-validate and structural checks.

These tests treat the draft KB files as the canonical test fixtures for the schema.
A failure here means either the schema changed in a breaking way or a KB file regressed.
"""

from pathlib import Path
import subprocess
import yaml
import pytest
from evidencell.validate import structural_checks

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "schema" / "celltype_mapping.yaml"
DRAFT_DIR = REPO_ROOT / "kb" / "draft"
CANONICAL_DIR = REPO_ROOT / "kb" / "mappings"


def _find_yaml_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(directory.rglob("*.yaml"))


draft_files = _find_yaml_files(DRAFT_DIR)
canonical_files = _find_yaml_files(CANONICAL_DIR)
all_kb_files = draft_files + canonical_files


# ── linkml-validate ───────────────────────────────────────────────────────────

@pytest.mark.parametrize("kb_file", all_kb_files, ids=[f.name for f in all_kb_files])
def test_linkml_validate(kb_file: Path):
    """Every KB YAML file must conform to the LinkML schema."""
    result = subprocess.run(
        [
            "uv", "run", "linkml-validate",
            "--schema", str(SCHEMA),
            "--target-class", "CellTypeMappingGraph",
            str(kb_file),
        ],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    output = (result.stdout + result.stderr).strip()
    assert result.returncode == 0, (
        f"linkml-validate failed for {kb_file.name}:\n{output}"
    )


# ── structural checks ─────────────────────────────────────────────────────────

@pytest.mark.parametrize("kb_file", all_kb_files, ids=[f.name for f in all_kb_files])
def test_structural_checks(kb_file: Path):
    """Every KB YAML file must pass the structural integrity checks."""
    doc = yaml.safe_load(kb_file.read_text(encoding="utf-8"))
    assert isinstance(doc, dict), f"{kb_file.name}: YAML root must be a mapping"
    errors = structural_checks(doc)
    assert errors == [], (
        f"Structural errors in {kb_file.name}:\n" + "\n".join(f"  - {e}" for e in errors)
    )


# ── YAML parsability ──────────────────────────────────────────────────────────

@pytest.mark.parametrize("kb_file", all_kb_files, ids=[f.name for f in all_kb_files])
def test_yaml_parseable(kb_file: Path):
    """Every KB YAML file must parse without errors."""
    try:
        doc = yaml.safe_load(kb_file.read_text(encoding="utf-8"))
        assert doc is not None, f"{kb_file.name}: file is empty"
    except yaml.YAMLError as exc:
        pytest.fail(f"YAML parse error in {kb_file.name}: {exc}")


# ── Schema present ────────────────────────────────────────────────────────────

def test_schema_exists():
    """The LinkML schema file must exist."""
    assert SCHEMA.exists(), f"Schema not found at {SCHEMA}"


def test_at_least_one_kb_file():
    """There must be at least one KB YAML file to test against."""
    assert len(all_kb_files) > 0, (
        f"No KB YAML files found in {DRAFT_DIR} or {CANONICAL_DIR}"
    )
