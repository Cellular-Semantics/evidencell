"""
KB example tests.

Two tiers:
  canonical (kb/mappings/)  — strict: linkml-validate + structural_checks.
                              Failures here mean a schema change broke a graduated KB file.
  draft (kb/draft/)         — lenient: YAML parseability only.
                              Draft files are WIP; schema conformance is checked at commit
                              time via `just qc-draft`, not here.

This split means `just test` never fails because of an in-progress KB file.
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


# ── Schema present ────────────────────────────────────────────────────────────

def test_schema_exists():
    """The LinkML schema file must exist."""
    assert SCHEMA.exists(), f"Schema not found at {SCHEMA}"


# ── Canonical files: strict validation ────────────────────────────────────────
# kb/mappings/ files have graduated from draft; they must always be schema-valid.

@pytest.mark.parametrize(
    "kb_file", canonical_files, ids=[f.name for f in canonical_files]
)
def test_linkml_validate_canonical(kb_file: Path):
    """Canonical KB files must conform to the LinkML schema."""
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


@pytest.mark.parametrize(
    "kb_file", canonical_files, ids=[f.name for f in canonical_files]
)
def test_structural_checks_canonical(kb_file: Path):
    """Canonical KB files must pass structural integrity checks."""
    doc = yaml.safe_load(kb_file.read_text(encoding="utf-8"))
    assert isinstance(doc, dict), f"{kb_file.name}: YAML root must be a mapping"
    errors = structural_checks(doc)
    assert errors == [], (
        f"Structural errors in {kb_file.name}:\n" + "\n".join(f"  - {e}" for e in errors)
    )


# ── Draft files: YAML parseability only ───────────────────────────────────────
# Draft files are WIP. We only check they are valid YAML — schema conformance is
# the job of `just qc-draft` and the pre-edit hook, not the test suite.

@pytest.mark.parametrize(
    "kb_file", draft_files, ids=[f.name for f in draft_files]
)
def test_yaml_parseable_draft(kb_file: Path):
    """Draft KB files must at least be parseable YAML (catches syntax errors early)."""
    try:
        doc = yaml.safe_load(kb_file.read_text(encoding="utf-8"))
        assert doc is not None, f"{kb_file.name}: file is empty"
    except yaml.YAMLError as exc:
        pytest.fail(f"YAML parse error in {kb_file.name}: {exc}")
