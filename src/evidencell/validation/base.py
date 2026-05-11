"""Base classes for evidencell validation/audit drivers.

A validation audit is a runnable comparison of evidencell's current
pipeline behaviour against an oracle (curator-supplied ground truth,
external dataset, prior published mapping, etc.). Each audit produces
a structured ``AuditRun`` artifact that lands in
``research/validation/methods_audits/<audit_id>/runs/`` and a Markdown
summary that updates the audit's README.

The base classes here establish patterns intended to minimise the
"agent inference substitutes for data lookup" failure mode:

  * Every test case carries both `expected` and `actual` dicts — the
    audit report contains raw evidence, not just verdicts.
  * Preflight assertions catch silent dropouts before the audit body
    runs (e.g. UBERON IDs that fail to resolve to MBA terms, expression
    data that wasn't loaded).
  * Run-time outcomes are stored as raw ``AuditOutcome`` objects so a
    re-analysis after the fact can reach back to the data, not just
    a summary statistic.
"""

from __future__ import annotations

import json
import subprocess
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


class AuditAssertion(Exception):
    """Raised by an audit's preflight check when a precondition is violated.

    Preflight failures stop the audit before it runs — silent dropouts
    (e.g. region filter not applied because UBERON resolution failed)
    are the failure mode this exception is meant to prevent.
    """


@dataclass
class AuditOutcome:
    """One test case's outcome with full provenance.

    The ``expected`` and ``actual`` dicts must contain enough information
    that a reviewer reading the JSON archive can audit the audit. Don't
    summarise into ``passed``/``reason`` alone; carry the raw values that
    backed the verdict.
    """

    test_id: str
    expected: dict
    actual: dict
    passed: bool
    reason: str
    notes: str = ""
    metadata: dict = field(default_factory=dict)


@dataclass
class AuditRun:
    """A complete audit run with metadata sufficient to reproduce it later.

    ``commit`` is the git HEAD at run time; ``config`` is the audit
    parameter set. ``preflight_assertions`` records the invariant checks
    that passed (or, if the run was forced past a failure, the warning
    notes). ``outcomes`` is the per-case data.
    """

    audit_id: str
    started_at: str
    finished_at: str | None
    commit: str
    config: dict
    preflight_assertions: list[dict] = field(default_factory=list)
    outcomes: list[AuditOutcome] = field(default_factory=list)
    summary_stats: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["outcomes"] = [asdict(o) for o in self.outcomes]
        return d

    def aggregate_by_reason(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for o in self.outcomes:
            out[o.reason] = out.get(o.reason, 0) + 1
        return out


def current_git_commit() -> str:
    """Return ``git rev-parse HEAD`` or 'unknown' if not in a repo."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return "unknown"


class AuditDriver(ABC):
    """Abstract base for an audit/validation driver.

    Implementations declare:

      * ``audit_id`` — slug used in output paths and the audits index.
      * ``preflight()`` — a sequence of (name, callable) invariant checks.
        Each callable raises :class:`AuditAssertion` on failure. The
        run aborts before executing test cases unless ``force_preflight``
        is set in the config.
      * ``collect_ground_truth()`` — yields the test-case dicts the audit
        will run.
      * ``run_test_case(case)`` — executes a single case, returns
        :class:`AuditOutcome`.

    The :meth:`run` method orchestrates preflight + collection + execution
    and emits the :class:`AuditRun` artifact to
    ``research/validation/methods_audits/<audit_id>/runs/<timestamp>.json``.
    """

    audit_id: str = "unnamed_audit"

    def __init__(
        self,
        config: dict | None = None,
        output_root: Path | None = None,
        force_preflight: bool = False,
    ):
        self.config = dict(config or {})
        self.force_preflight = force_preflight
        self.output_root = output_root or self._default_output_root()
        self.output_dir = self.output_root / self.audit_id
        self.runs_dir = self.output_dir / "runs"

    def _default_output_root(self) -> Path:
        # Resolved relative to repo root (evidencell.paths.repo_root)
        from evidencell.paths import repo_root
        return repo_root() / "research" / "validation" / "methods_audits"

    # ── Subclass hook points ──────────────────────────────────────────

    @abstractmethod
    def preflight(self) -> list[tuple[str, Callable[[], None]]]:
        """Return a list of (name, callable) invariant checks. Each callable
        raises :class:`AuditAssertion` on failure."""

    @abstractmethod
    def collect_ground_truth(self) -> list[dict]:
        """Return the test-case dicts the audit will iterate over."""

    @abstractmethod
    def run_test_case(self, case: dict) -> AuditOutcome:
        """Execute one test case; produce an :class:`AuditOutcome`."""

    # ── Orchestration ─────────────────────────────────────────────────

    def run(self, write_artifact: bool = True) -> AuditRun:
        """Execute the full audit: preflight, ground-truth collection,
        per-case execution, summary computation. Writes a JSON artifact
        unless ``write_artifact`` is False."""

        started_at = datetime.now(tz=timezone.utc).isoformat()
        run = AuditRun(
            audit_id=self.audit_id,
            started_at=started_at,
            finished_at=None,
            commit=current_git_commit(),
            config=self.config,
        )

        # Preflight invariants — fail loud unless force_preflight is set.
        for name, check in self.preflight():
            try:
                check()
                run.preflight_assertions.append({"name": name, "status": "pass"})
            except AuditAssertion as exc:
                if self.force_preflight:
                    run.preflight_assertions.append(
                        {"name": name, "status": "skipped", "note": str(exc)}
                    )
                else:
                    run.preflight_assertions.append(
                        {"name": name, "status": "fail", "note": str(exc)}
                    )
                    run.finished_at = datetime.now(tz=timezone.utc).isoformat()
                    if write_artifact:
                        self._write_artifact(run, suffix="_PREFLIGHT_FAILED")
                    raise

        # Ground-truth collection.
        cases = self.collect_ground_truth()
        run.config["n_cases"] = len(cases)
        if not cases:
            run.finished_at = datetime.now(tz=timezone.utc).isoformat()
            run.summary_stats = {"empty": True}
            if write_artifact:
                self._write_artifact(run, suffix="_EMPTY")
            return run

        # Per-case execution. We catch unexpected exceptions per case so
        # one bad case doesn't take out the whole audit; the case is
        # recorded with reason="error" and the exception string in notes.
        for case in cases:
            try:
                outcome = self.run_test_case(case)
            except Exception as exc:  # noqa: BLE001
                outcome = AuditOutcome(
                    test_id=str(case.get("test_id") or case.get("id") or "?"),
                    expected={},
                    actual={},
                    passed=False,
                    reason="error",
                    notes=f"{type(exc).__name__}: {exc}",
                    metadata={"case": _truncate_for_json(case)},
                )
            run.outcomes.append(outcome)

        run.finished_at = datetime.now(tz=timezone.utc).isoformat()
        run.summary_stats = self._summarise(run)

        if write_artifact:
            self._write_artifact(run)

        return run

    # ── Helpers ───────────────────────────────────────────────────────

    def _summarise(self, run: AuditRun) -> dict:
        n = len(run.outcomes)
        by_reason = run.aggregate_by_reason()
        pass_count = sum(1 for o in run.outcomes if o.passed)
        return {
            "n_cases": n,
            "pass_count": pass_count,
            "pass_rate": pass_count / n if n else None,
            "by_reason": by_reason,
        }

    def _write_artifact(self, run: AuditRun, suffix: str = "") -> Path:
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        stamp = run.started_at.replace(":", "").split(".")[0]
        path = self.runs_dir / f"{stamp}{suffix}.json"
        path.write_text(json.dumps(run.to_dict(), indent=2, default=str))
        # Also update a symlink-style "latest" pointer for easy diffing.
        latest = self.runs_dir / "latest.json"
        latest.write_text(json.dumps(run.to_dict(), indent=2, default=str))
        return path


def _truncate_for_json(obj: Any, max_chars: int = 500) -> Any:
    """Best-effort truncation of a case dict so error metadata stays small."""
    try:
        text = json.dumps(obj, default=str)
    except Exception:
        return repr(obj)[:max_chars]
    if len(text) <= max_chars:
        return obj
    return {"_truncated": True, "preview": text[:max_chars]}
