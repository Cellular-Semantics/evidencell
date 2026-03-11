#!/usr/bin/env python3
"""
PreToolUse hook: validates kb/mappings/**/*.yaml BEFORE edits are applied.

1. Intercepts Edit/Write/MultiEdit calls targeting kb/mappings/**/*.yaml
2. Simulates the resulting file content (no disk write until validated)
3. Runs `just validate <temp_file>` on the simulated result
4. Returns exit code 2 to BLOCK the edit if validation fails

Exit code 2 blocks the operation in PreToolUse hooks.
https://docs.claude.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

import sys
import json
import subprocess
import tempfile
from pathlib import Path


def simulate_edit(file_path: Path, old_string: str, new_string: str) -> str:
    if not file_path.exists():
        sys.exit(0)  # Let Claude Code handle missing file
    content = file_path.read_text()
    if old_string not in content:
        sys.exit(0)  # Let Claude Code handle this
    return content.replace(old_string, new_string, 1)


def simulate_write(content: str) -> str:
    return content


def simulate_multi_edit(file_path: Path, edits: list) -> str:
    if not file_path.exists():
        sys.exit(0)
    content = file_path.read_text()
    for edit in edits:
        old_string = edit.get("old_string", "")
        new_string = edit.get("new_string", "")
        if old_string and old_string in content:
            content = content.replace(old_string, new_string, 1)
    return content


def validate_content(content: str, original_path: Path, project_root: Path) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir) / original_path.name
        temp_path.write_text(content)
        result = subprocess.run(
            ["just", "validate", str(temp_path)],
            capture_output=True,
            text=True,
            cwd=project_root,
        )
        return result.returncode == 0, result.stdout + result.stderr


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

    # Intercept all KB YAML files: kb/mappings/**/*.yaml and kb/draft/**/*.yaml
    if "/kb/" not in str(file_path) or file_path.suffix != ".yaml":
        sys.exit(0)

    project_root = Path(__file__).parent.parent.parent

    if tool_name == "Edit":
        simulated = simulate_edit(file_path, tool_input.get("old_string", ""), tool_input.get("new_string", ""))
    elif tool_name == "Write":
        simulated = simulate_write(tool_input.get("content", ""))
    elif tool_name == "MultiEdit":
        simulated = simulate_multi_edit(file_path, tool_input.get("edits", []))
    else:
        sys.exit(0)

    success, output = validate_content(simulated, file_path, project_root)

    print("\n" + "=" * 60, file=sys.stderr)
    print(f"Pre-Edit Validation: {file_path.name}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    if output.strip():
        print(output.strip(), file=sys.stderr)

    if not success:
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
