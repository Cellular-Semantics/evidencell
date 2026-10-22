"""Canonical writer for KB graph YAML.

Several call sites write KB YAML today with differing serialiser settings, and
**none of them validates before writing**. None passes through the PreToolUse
hook either -- that hook only intercepts the Write/Edit tools, so a programmatic
write lands unchecked. That is the gap this module closes: ``write_kb_yaml`` is
the one place that decides how generated KB YAML is serialised and the one place
that validates first. It fails closed -- a document that does not validate is
not written.

Scope note: this writer is for **generated** documents (the component splitter,
emitters). It serialises via PyYAML and therefore drops YAML comments, which
CLAUDE.md explicitly permits ("Reserve comments for transient developer-facing
hints that are acceptable to lose"). For *in-place edits* of an existing
curated file, prefer the ruamel round-trip dumper used by
``refresh_predicates`` -- it preserves comments and authored quoting, which a
re-serialise cannot.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path
from typing import Any

import yaml

# Pinned serialisation. Changing any of these reflows every KB file, so treat
# them as a format version, not as tuning knobs.
#   sort_keys=False        -- preserve authored key order; alphabetising a
#                             CellTypeNode destroys its readability
#   allow_unicode=True     -- author names and quotes contain non-ASCII
#   default_flow_style=False -- block style throughout; no inline {a: 1}
#   width=100              -- stable line wrapping, so diffs track real edits
CANONICAL_DUMP_KWARGS: dict[str, Any] = {
    "sort_keys": False,
    "allow_unicode": True,
    "default_flow_style": False,
    "width": 100,
}


class KbValidationError(RuntimeError):
    """A KB document failed schema validation and was not written."""


def canonical_yaml(doc: Any) -> str:
    """Serialise `doc` as canonical KB YAML."""
    return yaml.dump(doc, **CANONICAL_DUMP_KWARGS)


def validate_kb_doc(doc: Any, *, target_class: str | None = None) -> list[str]:
    """Return schema-validation messages for `doc`. Empty means valid.

    Raises KbValidationError if the schema cannot be loaded at all -- an
    unavailable validator must not read as "valid".
    """
    from evidencell.paths import repo_root

    schema = repo_root() / "schema" / "celltype_mapping.yaml"
    try:
        from linkml.validator import Validator
        from linkml.validator.plugins import JsonschemaValidationPlugin

        # Plugins must be passed explicitly -- a Validator with none returns zero
        # results for every input (see validate_batch for the upstream detail),
        # which would make this "validate before writing" a no-op.
        validator = Validator(
            str(schema),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        )
    except Exception as exc:  # pragma: no cover - environment failure
        raise KbValidationError(
            f"Cannot load schema {schema} to validate before writing: {exc}"
        ) from exc
    report = validator.validate(doc, target_class=target_class)
    return [r.message for r in report.results]


def write_kb_yaml(
    path: Path,
    doc: Any,
    *,
    validate: bool = True,
    target_class: str | None = None,
) -> Path:
    """Write `doc` to `path` as canonical KB YAML, validating first.

    The write is atomic -- the document is validated and serialised in full
    before anything touches `path`, so a validation failure cannot leave a
    partially-written or invalid file behind.

    Pass ``validate=False`` only for documents that are deliberately not
    whole-schema instances (fragments, test fixtures).
    """
    path = Path(path)
    if validate:
        messages = validate_kb_doc(doc, target_class=target_class)
        if messages:
            joined = "\n  ".join(messages)
            raise KbValidationError(
                f"Refusing to write schema-invalid KB YAML to {path}:\n  {joined}"
            )

    text = canonical_yaml(doc)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except Exception:
        Path(tmp).unlink(missing_ok=True)
        raise
    return path


def usable_sqlite(db_path: Path) -> bool:
    """True if `db_path` is a non-empty file that sqlite can read.

    `sqlite3.connect(path)` *creates* an empty database when the file is
    absent, so any code that guards a lookup with `db_path.exists()` and then
    connects will, on its first miss, leave a 0-byte file behind -- after which
    every later `exists()` guard passes and the lookup raises "no such table"
    instead of degrading gracefully. Guard with this instead of `exists()`.
    """
    try:
        return db_path.is_file() and db_path.stat().st_size > 0
    except OSError:
        return False


def connect_readonly(db_path: Path):
    """Open `db_path` read-only, or return None if it is missing or empty.

    Read-only mode means a missing file raises rather than being created, so a
    graceful-degradation path can never poison later guards (see
    `usable_sqlite`).
    """
    import sqlite3

    if not usable_sqlite(db_path):
        return None
    try:
        return sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    except sqlite3.Error:
        return None
