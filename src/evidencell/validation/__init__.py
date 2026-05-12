"""evidencell validation/audit framework.

See ``workflows/validation/`` for orchestrator docs describing when and
how to run each audit. See ``research/validation/methods_audits/`` for
run history, findings, and decisions informed.

Public API:

    AuditDriver, AuditOutcome, AuditRun, AuditAssertion
        Base classes for implementing new audits. Subclasses live next
        to these (e.g. ``at_blind.ATBlindAudit``).

To add a new audit:
  1. Implement an ``AuditDriver`` subclass in this package.
  2. Add a CLI subcommand in ``__main__``.
  3. Add a ``justfile`` recipe ``just validate-<audit-id>``.
  4. Add a workflow doc at ``workflows/validation/<audit-id>.md``.
  5. Add a findings doc at
     ``research/validation/methods_audits/<audit-id>/README.md``.
"""

from .at_blind import ATBlindAudit
from .base import AuditAssertion, AuditDriver, AuditOutcome, AuditRun

__all__ = [
    "ATBlindAudit",
    "AuditAssertion",
    "AuditDriver",
    "AuditOutcome",
    "AuditRun",
]
