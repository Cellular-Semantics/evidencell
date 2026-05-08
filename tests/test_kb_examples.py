"""
KB example tests.

All cell-type graphs in `kb/graphs/` must conform to the LinkML schema and
pass structural integrity checks. The quality gate is `just qc` + human PR
review; there is no separate draft/canonical tier.
"""

from pathlib import Path
import subprocess
import yaml
import pytest
from evidencell.validate import structural_checks

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "schema" / "celltype_mapping.yaml"
KB_GRAPHS_DIR = REPO_ROOT / "kb" / "graphs"


def _find_yaml_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(directory.rglob("*.yaml"))


kb_files = _find_yaml_files(KB_GRAPHS_DIR)


# ── Schema present ────────────────────────────────────────────────────────────

def test_schema_exists():
    """The LinkML schema file must exist."""
    assert SCHEMA.exists(), f"Schema not found at {SCHEMA}"


# ── KB files: strict validation ───────────────────────────────────────────────

@pytest.mark.parametrize(
    "kb_file", kb_files, ids=[f.name for f in kb_files]
)
def test_linkml_validate(kb_file: Path):
    """KB graph files must conform to the LinkML schema."""
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
    "kb_file", kb_files, ids=[f.name for f in kb_files]
)
def test_structural_checks(kb_file: Path):
    """KB graph files must pass structural integrity checks."""
    doc = yaml.safe_load(kb_file.read_text(encoding="utf-8"))
    assert isinstance(doc, dict), f"{kb_file.name}: YAML root must be a mapping"
    errors = structural_checks(doc)
    assert errors == [], (
        f"Structural errors in {kb_file.name}:\n" + "\n".join(f"  - {e}" for e in errors)
    )
