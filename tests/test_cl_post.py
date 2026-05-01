"""Unit tests for evidencell.cl_post — preview/post gating for CL NTR issues."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest

from evidencell import cl_post


def _write_ntr(tmp_path: Path, body: str = "Body line one.\nBody line two.\n") -> Path:
    f = tmp_path / "ntr.md"
    f.write_text(f"# CL new term request: foo cell\n\n{body}")
    return f


def test_split_title_body(tmp_path: Path) -> None:
    f = _write_ntr(tmp_path)
    title, body = cl_post._split_title_body(f.read_text())
    assert title == "CL new term request: foo cell"
    assert "Body line one." in body
    assert not body.startswith("\n")


def test_split_title_body_rejects_no_heading() -> None:
    with pytest.raises(ValueError, match="must start with"):
        cl_post._split_title_body("not a heading\nstill not\n")


def test_split_title_body_rejects_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        cl_post._split_title_body("")


def test_post_missing_file(tmp_path, capsys) -> None:
    rc = cl_post.post(tmp_path / "does_not_exist.md", confirm=False)
    assert rc == 2


def test_post_preview_only_does_not_call_gh(tmp_path, capsys) -> None:
    f = _write_ntr(tmp_path)
    with patch("evidencell.cl_post.subprocess.run") as run, \
         patch("evidencell.cl_post.shutil.which", return_value="/usr/bin/gh"):
        rc = cl_post.post(f, confirm=False)
    assert rc == 0
    run.assert_not_called()
    out = capsys.readouterr().out
    assert "Preview only" in out
    assert "CL new term request: foo cell" in out


def test_post_confirm_requires_gh(tmp_path, capsys) -> None:
    f = _write_ntr(tmp_path)
    with patch("evidencell.cl_post.shutil.which", return_value=None):
        rc = cl_post.post(f, confirm=True)
    assert rc == 3


def test_post_confirm_requires_token(tmp_path, monkeypatch) -> None:
    f = _write_ntr(tmp_path)
    monkeypatch.delenv("CELLSEM_GH_TOKEN", raising=False)
    with patch("evidencell.cl_post.shutil.which", return_value="/usr/bin/gh"):
        rc = cl_post.post(f, confirm=True)
    assert rc == 4


def test_post_confirm_invokes_gh_with_token(tmp_path, monkeypatch) -> None:
    f = _write_ntr(tmp_path)
    monkeypatch.setenv("CELLSEM_GH_TOKEN", "tok-xyz")

    captured = {}

    def fake_run(cmd, env=None):  # noqa: ANN001
        captured["cmd"] = cmd
        captured["env"] = env
        class R:
            returncode = 0
        return R()

    with patch("evidencell.cl_post.shutil.which", return_value="/usr/bin/gh"), \
         patch("evidencell.cl_post.subprocess.run", side_effect=fake_run):
        rc = cl_post.post(f, confirm=True)

    assert rc == 0
    cmd = captured["cmd"]
    assert cmd[:3] == ["gh", "issue", "create"]
    assert "--repo" in cmd and cl_post.CL_REPO in cmd
    assert "--label" in cmd and cl_post.ISSUE_LABEL in cmd
    title_idx = cmd.index("--title") + 1
    assert cmd[title_idx] == "CL new term request: foo cell"
    assert captured["env"]["GH_TOKEN"] == "tok-xyz"
