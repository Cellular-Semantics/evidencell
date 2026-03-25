"""Smoke tests for external CLI tool interfaces.

These tests verify that the subprocess invocations used in the justfile
are syntactically correct and that expected subcommands / flags exist.
They call --help only: no KB data, no network, no OAK databases required.
Total run time is a few seconds.

If 'uv run <tool>' fails because the tool is not installed, the test is
skipped rather than failed, so a fresh env without optional deps doesn't
block everything.

Regression catalogue
--------------------
- linkml-term-validator: must use 'validate' subcommand
    Bug: `linkml-term-validator --config ...` → "No such option: --config"
    Fix: `linkml-term-validator validate --config ...`
"""

import subprocess

import pytest


def _uv_run_help(*extra: str) -> subprocess.CompletedProcess:
    """Run `uv run <extra> --help` and return the completed process."""
    cmd = ["uv", "run", *extra, "--help"]
    return subprocess.run(cmd, capture_output=True, text=True)


def _require(result: subprocess.CompletedProcess, tool: str) -> None:
    """Skip if the tool is not installed (returncode 127 = command not found)."""
    if result.returncode == 127:
        pytest.skip(f"{tool} not installed in this environment")


# ── linkml-validate ───────────────────────────────────────────────────────────


def test_linkml_validate_help():
    """linkml-validate must accept --help without error."""
    r = _uv_run_help("linkml-validate")
    _require(r, "linkml-validate")
    assert r.returncode == 0, (
        f"linkml-validate --help failed (rc={r.returncode}):\n{r.stderr}"
    )


def test_linkml_validate_accepts_schema_flag():
    """linkml-validate must advertise a -s / --schema flag."""
    r = _uv_run_help("linkml-validate")
    _require(r, "linkml-validate")
    combined = r.stdout + r.stderr
    assert "-s" in combined or "--schema" in combined, (
        "'-s/--schema' flag not found in linkml-validate --help.\n"
        "The justfile validate recipe uses: linkml-validate -s <schema> <file>"
    )


# ── linkml-term-validator ─────────────────────────────────────────────────────


def test_linkml_term_validator_has_validate_subcommand():
    """linkml-term-validator must expose a 'validate' subcommand.

    Regression: previously the justfile called
        linkml-term-validator --config ... --schema ... <dir>
    which fails with "No such option: --config".
    Correct invocation:
        linkml-term-validator validate --config ... --schema ... <dir>
    """
    r = _uv_run_help("linkml-term-validator", "validate")
    _require(r, "linkml-term-validator")
    assert r.returncode == 0, (
        f"'linkml-term-validator validate --help' failed (rc={r.returncode}).\n"
        f"stderr: {r.stderr}\n"
        "Did the CLI interface change? Update the validate-terms recipe in justfile."
    )


def test_linkml_term_validator_validate_accepts_config():
    """linkml-term-validator validate must accept --config flag."""
    r = _uv_run_help("linkml-term-validator", "validate")
    _require(r, "linkml-term-validator")
    combined = r.stdout + r.stderr
    assert "--config" in combined, (
        "'--config' not found in linkml-term-validator validate --help.\n"
        "The justfile validate-terms recipe uses --config <oak_config.yaml>."
    )


def test_linkml_term_validator_validate_accepts_schema():
    """linkml-term-validator validate must accept --schema flag."""
    r = _uv_run_help("linkml-term-validator", "validate")
    _require(r, "linkml-term-validator")
    combined = r.stdout + r.stderr
    assert "--schema" in combined, (
        "'--schema' not found in linkml-term-validator validate --help.\n"
        "The justfile validate-terms recipe uses --schema <schema.yaml>."
    )


# ── runoak (OAK) ──────────────────────────────────────────────────────────────


def test_runoak_help():
    """runoak must be importable / callable — used by validate-terms indirectly."""
    r = _uv_run_help("runoak")
    _require(r, "runoak")
    # runoak --help exits 0
    assert r.returncode == 0, (
        f"runoak --help failed (rc={r.returncode}):\n{r.stderr}"
    )
