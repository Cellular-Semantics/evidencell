"""Tests for the canonical KB writer and sqlite guards."""

import pytest
import yaml

from evidencell.kb_io import (
    KbValidationError,
    canonical_yaml,
    connect_readonly,
    usable_sqlite,
    validate_kb_doc,
    write_kb_yaml,
)

VALID_DOC = {
    "name": "test",
    "target_atlas": "WMBv1",
    "nodes": [
        {"id": "a", "name": "a", "definition_basis": "CLASSICAL_MULTIMODAL"},
    ],
    "edges": [],
}


def test_canonical_yaml_preserves_key_order():
    text = canonical_yaml({"zebra": 1, "apple": 2})
    assert text.index("zebra") < text.index("apple")


def test_canonical_yaml_keeps_unicode_unescaped():
    assert "Müller" in canonical_yaml({"name": "Müller"})


def test_validator_actually_validates():
    """Guard against the fails-open trap.

    linkml's Validator.iter_results_from_source short-circuits with
    `if not self._validation_plugins: return []`, so a Validator built without
    an explicit plugin list reports *every* instance as valid. This test fails
    if that explicit plugin list is ever dropped.
    """
    messages = validate_kb_doc(
        {"nodes": [{"id": "x", "definition_basis": "NOT_A_BASIS"}]}
    )
    assert messages, "invalid document reported as valid -- validator is a no-op"
    assert any("NOT_A_BASIS" in m for m in messages)


def test_valid_document_has_no_messages():
    assert validate_kb_doc(VALID_DOC) == []


def test_write_refuses_invalid_and_leaves_no_file(tmp_path):
    target = tmp_path / "out.yaml"
    with pytest.raises(KbValidationError):
        write_kb_yaml(target, {"nodes": [{"id": "x", "definition_basis": "NOPE"}]})
    assert not target.exists()


def test_write_does_not_clobber_on_validation_failure(tmp_path):
    target = tmp_path / "out.yaml"
    write_kb_yaml(target, VALID_DOC)
    original = target.read_text(encoding="utf-8")
    with pytest.raises(KbValidationError):
        write_kb_yaml(target, {"nodes": [{"id": "x", "definition_basis": "NOPE"}]})
    assert target.read_text(encoding="utf-8") == original


def test_write_round_trips(tmp_path):
    target = tmp_path / "out.yaml"
    write_kb_yaml(target, VALID_DOC)
    assert yaml.safe_load(target.read_text(encoding="utf-8")) == VALID_DOC


def test_write_leaves_no_temp_files(tmp_path):
    write_kb_yaml(tmp_path / "out.yaml", VALID_DOC)
    assert [p.name for p in tmp_path.iterdir()] == ["out.yaml"]


def test_usable_sqlite_rejects_empty_file(tmp_path):
    """A 0-byte DB must not read as usable.

    sqlite3.connect() creates an empty file on a miss, so `exists()` guards
    pass forever after and the next query raises "no such table".
    """
    empty = tmp_path / "empty.db"
    empty.touch()
    assert empty.exists()
    assert not usable_sqlite(empty)


def test_usable_sqlite_rejects_missing_file(tmp_path):
    assert not usable_sqlite(tmp_path / "nope.db")


def test_connect_readonly_never_creates_a_file(tmp_path):
    missing = tmp_path / "nope.db"
    assert connect_readonly(missing) is None
    assert not missing.exists(), "connect_readonly created the database"
