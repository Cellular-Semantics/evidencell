"""Phase 2 PR2 — post-cutover assertions.

PR1 introduced a back-compat shim (``src/evidencell/_mapping_compat.py``)
that read both old (``type_a``/``type_b``/ALL_CAPS-relationship-values)
and new (``lit_type``/``taxonomy_type``/CURIE-relationship-values)
MappingEdge shapes. PR2 sweeps every KB edge into the new shape and
deletes the shim. These tests guarantee that nothing in ``src/``
still imports the shim and that the schema's deprecated entries are
gone — the post-cutover state is locked in.

If a future curator regresses any of these invariants, this file is
the first failing test.
"""

from __future__ import annotations

import yaml

from evidencell.paths import repo_root


# ──────────────────────────────────────────────────────────────────
# Shim is gone
# ──────────────────────────────────────────────────────────────────


def test_mapping_compat_module_deleted():
    """The PR1 back-compat shim no longer exists in src/."""
    path = repo_root() / "src" / "evidencell" / "_mapping_compat.py"
    assert not path.exists(), (
        "src/evidencell/_mapping_compat.py should have been deleted in PR2 "
        "(KB sweep + back-compat removal)."
    )


def test_no_src_imports_of_mapping_compat():
    """No production module imports the deleted shim."""
    src_root = repo_root() / "src" / "evidencell"
    offenders: list[str] = []
    for py in src_root.rglob("*.py"):
        text = py.read_text(encoding="utf-8")
        if "_mapping_compat" in text:
            offenders.append(str(py.relative_to(repo_root())))
    assert not offenders, (
        "Found stale references to the deleted compat shim in: "
        + ", ".join(offenders)
    )


# ──────────────────────────────────────────────────────────────────
# Schema has shed its deprecated entries
# ──────────────────────────────────────────────────────────────────


def _load_schema() -> dict:
    schema_path = repo_root() / "schema" / "celltype_mapping.yaml"
    with schema_path.open() as fh:
        return yaml.safe_load(fh)


def test_mapping_edge_drops_deprecated_aliases():
    """MappingEdge no longer carries the deprecated `type_a` / `type_b`
    slot aliases. The new `lit_type` / `taxonomy_type` slots are
    required."""
    schema = _load_schema()
    attrs = schema["classes"]["MappingEdge"]["attributes"]
    assert "type_a" not in attrs, "Deprecated `type_a` slot still present."
    assert "type_b" not in attrs, "Deprecated `type_b` slot still present."
    assert attrs["lit_type"].get("required") is True
    assert attrs["taxonomy_type"].get("required") is True


def test_mapping_relationship_drops_deprecated_values():
    """MappingRelationship enum no longer carries the deprecated
    ALL_CAPS values (EQUIVALENT, TYPE_A_SPLITS, …). Only the CURIE
    values survive."""
    schema = _load_schema()
    perms = schema["enums"]["MappingRelationship"]["permissible_values"]
    deprecated = {
        "EQUIVALENT", "PARTIAL_OVERLAP", "CROSS_CUTTING",
        "TYPE_A_SPLITS", "TYPE_A_MERGES", "SUBSET", "SUPERSET",
        "NO_CORRESPONDENCE", "UNCERTAIN", "CANDIDATE_SYNONYM",
        "OVERLAPS",
    }
    still_present = deprecated & set(perms.keys())
    assert not still_present, (
        f"Deprecated MappingRelationship values still in schema: "
        f"{sorted(still_present)}"
    )

    # Sanity check: the canonical CURIE values are present.
    expected = {
        "skos:exactMatch", "skos:closeMatch",
        "skos:broadMatch", "skos:narrowMatch",
        "evidencell:PartialOverlapMatch", "evidencell:CrossCuttingMatch",
        "evidencell:NoCorrespondence", "evidencell:UncertainRelationship",
    }
    missing = expected - set(perms.keys())
    assert not missing, (
        f"Expected MappingRelationship values absent from schema: "
        f"{sorted(missing)}"
    )


# ──────────────────────────────────────────────────────────────────
# KB graphs use only the new shape
# ──────────────────────────────────────────────────────────────────


def _iter_edges():
    graphs = repo_root() / "kb" / "graphs"
    for path in sorted(graphs.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        for edge in doc.get("edges") or []:
            if isinstance(edge, dict):
                yield path, edge


def test_no_kb_edge_uses_old_field_names():
    offenders: list[str] = []
    for path, edge in _iter_edges():
        if "type_a" in edge or "type_b" in edge:
            offenders.append(
                f"{path.relative_to(repo_root())}::{edge.get('id', '<unnamed>')}"
            )
    assert not offenders, (
        f"{len(offenders)} KB edges still use deprecated `type_a` / `type_b`:"
        f" {offenders[:5]}{'…' if len(offenders) > 5 else ''}"
    )


def test_no_kb_edge_uses_old_relationship_values():
    deprecated = {
        "EQUIVALENT", "PARTIAL_OVERLAP", "CROSS_CUTTING",
        "TYPE_A_SPLITS", "TYPE_A_MERGES", "SUBSET", "SUPERSET",
        "NO_CORRESPONDENCE", "UNCERTAIN", "CANDIDATE_SYNONYM",
        "OVERLAPS",
    }
    offenders: list[str] = []
    for path, edge in _iter_edges():
        rel = edge.get("relationship")
        if rel in deprecated:
            offenders.append(
                f"{path.relative_to(repo_root())}::{edge.get('id', '<unnamed>')}={rel}"
            )
    assert not offenders, (
        f"{len(offenders)} KB edges still use deprecated relationship "
        f"values: {offenders[:5]}{'…' if len(offenders) > 5 else ''}"
    )


def test_every_kb_edge_has_mapping_justification():
    """Phase 2 PR2 sweep populated `mapping_justification` on every
    edge. New edges going forward must continue to set it."""
    missing: list[str] = []
    for path, edge in _iter_edges():
        if not edge.get("mapping_justification"):
            missing.append(
                f"{path.relative_to(repo_root())}::{edge.get('id', '<unnamed>')}"
            )
    assert not missing, (
        f"{len(missing)} KB edges lack mapping_justification: "
        f"{missing[:5]}{'…' if len(missing) > 5 else ''}"
    )
