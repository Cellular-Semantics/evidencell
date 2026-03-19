#!/usr/bin/env python3
"""
PreToolUse hook: validates kb/mappings/**/*.yaml BEFORE edits are applied.

1. Intercepts Edit/Write/MultiEdit calls targeting kb/**/*.yaml
2. Simulates the resulting file content (no disk write until validated)
3. Runs linkml-validate via validate.py AND structural_checks
4. Returns exit code 2 to BLOCK the edit if either check fails

Exit code 2 blocks the operation in PreToolUse hooks.
https://docs.claude.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

import sys
import json
from pathlib import Path

# Add project src/ to path so we can import evidencell.validate
_project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_project_root / "src"))

import yaml  # noqa: E402
from evidencell.validate import simulate_edit, structural_checks, linkml_validate  # noqa: E402


def main():
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    if tool_name not in ["Write", "Edit", "MultiEdit"]:
        sys.exit(0)

    file_path_str = tool_input.get("file_path", "")
    if not file_path_str:
        sys.exit(0)

    file_path = Path(file_path_str)

    # Only intercept KB YAML files
    if "/kb/" not in str(file_path) or file_path.suffix != ".yaml":
        sys.exit(0)

    schema_path = _project_root / "schema" / "celltype_mapping.yaml"

    # Simulate the post-edit content using validate.py
    simulated = simulate_edit(tool_name, tool_input, file_path)

    print("\n" + "=" * 60, file=sys.stderr)
    print(f"Pre-Edit Validation: {file_path.name}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    errors_found = False

    # 1. Structural integrity checks (fast, no subprocess)
    try:
        doc = yaml.safe_load(simulated)
        if isinstance(doc, dict):
            struct_errors = structural_checks(doc)
            if struct_errors:
                print("Structural errors:", file=sys.stderr)
                for e in struct_errors:
                    print(f"  - {e}", file=sys.stderr)
                errors_found = True
    except yaml.YAMLError as exc:
        print(f"YAML parse error: {exc}", file=sys.stderr)
        errors_found = True

    # 2. LinkML schema validation (subprocess)
    ok, output = linkml_validate(simulated, schema_path, file_path.name)
    if output.strip():
        print(output.strip(), file=sys.stderr)
    if not ok:
        errors_found = True

    if errors_found:
        print("=" * 60, file=sys.stderr)
        print("BLOCKING EDIT: Validation failed", file=sys.stderr)
        print("Fix the issues above before proceeding.", file=sys.stderr)
        print("=" * 60 + "\n", file=sys.stderr)
        sys.exit(2)

    print("Validation passed - allowing edit", file=sys.stderr)
    print("=" * 60 + "\n", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
