"""
Post a drafted CL new term request markdown file to the obophenotype/cell-ontology
GitHub repo as a new issue.

Two-stage gate:
  1. Without --confirm, prints title + body preview and exits (the default).
  2. With --confirm, posts via `gh issue create`, using GH_TOKEN sourced from
     the CELLSEM_GH_TOKEN environment variable.

Usage:
    python -m evidencell.cl_post {ntr_md_file}              # preview only
    python -m evidencell.cl_post {ntr_md_file} --confirm    # post for real
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

CL_REPO = "obophenotype/cell-ontology"
ISSUE_LABEL = "new term request"


def _split_title_body(md_text: str) -> tuple[str, str]:
    """
    First top-level `# Title` line becomes the issue title (without the `# `).
    Everything after that line is the body. Title MUST be on the first
    non-blank line; otherwise the file is rejected as malformed.
    """
    lines = md_text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if not line.startswith("# "):
            raise ValueError(
                f"NTR file must start with a '# Title' heading; first non-blank line was: {line!r}"
            )
        title = line[2:].strip()
        body = "\n".join(lines[i + 1 :]).lstrip("\n")
        return title, body
    raise ValueError("NTR file is empty.")


def post(ntr_path: Path, confirm: bool) -> int:
    if not ntr_path.is_file():
        print(f"ERROR: file not found: {ntr_path}", file=sys.stderr)
        return 2

    title, body = _split_title_body(ntr_path.read_text())

    print(f"Repo:   {CL_REPO}")
    print(f"Label:  {ISSUE_LABEL}")
    print(f"Title:  {title}")
    print("Body preview (first 40 lines):")
    print("─" * 60)
    for line in body.splitlines()[:40]:
        print(line)
    print("─" * 60)

    if not confirm:
        print()
        print("Preview only. Re-run with --confirm to post the issue.")
        return 0

    if shutil.which("gh") is None:
        print("ERROR: `gh` CLI not found on PATH.", file=sys.stderr)
        return 3

    token = os.environ.get("CELLSEM_GH_TOKEN")
    if not token:
        print(
            "ERROR: CELLSEM_GH_TOKEN is not set in the environment. "
            "Configure it via .claude/settings.local.json or your shell.",
            file=sys.stderr,
        )
        return 4

    env = os.environ.copy()
    env["GH_TOKEN"] = token

    cmd = [
        "gh", "issue", "create",
        "--repo", CL_REPO,
        "--title", title,
        "--body", body,
        "--label", ISSUE_LABEL,
    ]
    print(f"Posting to {CL_REPO}…")
    result = subprocess.run(cmd, env=env)
    return result.returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ntr_path", type=Path, help="Path to NTR markdown file")
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Actually post the issue. Without this flag, prints a preview only.",
    )
    args = parser.parse_args(argv)
    return post(args.ntr_path, args.confirm)


if __name__ == "__main__":
    sys.exit(main())
