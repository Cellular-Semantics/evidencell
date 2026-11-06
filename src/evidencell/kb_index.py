"""In-memory index over every mapping graph under kb/graphs.

The files stay the edit surface; this is a query surface derived from them.
See planning/kb_index_plan.md for the design and phasing.

Three invariants:

1. **Read-only.** Writes go to files and the index is rebuilt; nothing writes
   through it. Records hold the parsed dicts themselves, shared across every
   caller in the process -- treat them as immutable, and copy before editing.
2. **Fail closed.** A file under kb/graphs that will not parse, or whose
   top level is not a mapping, raises KbIndexError naming it. An index built
   from the files that happened to parse would answer as if it had seen them
   all.
3. **Provenance on nodes and edges.** Every record carries its source file.
   Today every edge sits in its lit endpoint's file because
   validate.structural_checks requires in-document endpoints; that is
   enforced, not chosen, so edge provenance is recorded rather than inferred.

The index is rebuilt whenever the set of files or any file's mtime changes,
so it cannot be stale relative to the files it was built from.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from evidencell import paths


class KbIndexError(RuntimeError):
    """A kb/graphs file could not be indexed, so the index cannot be trusted."""


@dataclass(frozen=True)
class NodeRecord:
    node: dict[str, Any]
    source_file: Path
    is_stub: bool


@dataclass(frozen=True)
class EdgeRecord:
    edge: dict[str, Any]
    source_file: Path


@dataclass
class KbIndex:
    # Ids map to lists: atlas stubs legitimately repeat across files, and a
    # duplicated canonical definition must stay visible so callers can reject it.
    nodes: dict[str, list[NodeRecord]] = field(default_factory=dict)
    edges: dict[str, list[EdgeRecord]] = field(default_factory=dict)
    by_lit: dict[str, list[str]] = field(default_factory=dict)
    by_region: dict[str, list[str]] = field(default_factory=dict)
    stubs_by_accession: dict[str, list[NodeRecord]] = field(default_factory=dict)
    files: tuple[Path, ...] = ()


def is_stub(node: dict[str, Any]) -> bool:
    """True for a local placeholder whose real record lives elsewhere.

    Two kinds exist only so edge endpoints resolve in-document (see
    validate.structural_checks): an atlas stub, recognisable from
    definition_basis ATLAS_TRANSCRIPTOMIC because canonical atlas data lives in
    kb/taxonomy/, and a lit stub, which carries its type's real
    definition_basis and so must declare itself with `reference_stub`.
    """
    return bool(node.get("reference_stub")) or node.get("definition_basis") == paths.ATLAS_BASIS


# (stamp, index); stamp is the kb dir plus (path, mtime_ns) for every file.
_CACHE: tuple[tuple, KbIndex] | None = None


def clear_cache() -> None:
    global _CACHE
    _CACHE = None


def _kb_dir() -> Path:
    # Looked up through the module so tests can monkeypatch paths.repo_root.
    return paths.repo_root() / "kb" / "graphs"


def get_index() -> KbIndex:
    """Return the index for the current state of kb/graphs, rebuilding if needed."""
    global _CACHE
    kb_dir = _kb_dir()
    files = sorted(kb_dir.rglob("*.yaml")) if kb_dir.exists() else []
    stamp = (str(kb_dir), tuple((str(f), f.stat().st_mtime_ns) for f in files))
    if _CACHE is not None and _CACHE[0] == stamp:
        return _CACHE[1]
    index = _build(kb_dir, files)
    _CACHE = (stamp, index)
    return index


def _load(yaml_file: Path) -> dict[str, Any]:
    try:
        with yaml_file.open() as fh:
            data = yaml.safe_load(fh)
    except Exception as exc:
        raise KbIndexError(f"Cannot parse KB graph file {yaml_file}: {exc}") from exc
    if not isinstance(data, dict):
        raise KbIndexError(
            f"KB graph file {yaml_file} does not hold a mapping at the top level "
            f"(got {type(data).__name__})."
        )
    return data


def _build(kb_dir: Path, files: list[Path]) -> KbIndex:
    index = KbIndex(files=tuple(files))
    stubs: dict[str, list[NodeRecord]] = {}
    for yaml_file in files:
        data = _load(yaml_file)
        region = yaml_file.relative_to(kb_dir).parts[0]
        # Malformed entries (non-dict, missing id) are skipped rather than
        # raised: they cannot be addressed by id, and structural_checks owns them.
        for node in data.get("nodes") or []:
            if not isinstance(node, dict) or not node.get("id"):
                continue
            record = NodeRecord(node, yaml_file, is_stub(node))
            if record.is_stub:
                stubs.setdefault(node["id"], []).append(record)
                accession = node.get("cell_set_accession")
                if accession:
                    index.stubs_by_accession.setdefault(accession, []).append(record)
            else:
                index.nodes.setdefault(node["id"], []).append(record)
                region_ids = index.by_region.setdefault(region, [])
                if node["id"] not in region_ids:
                    region_ids.append(node["id"])
        for edge in data.get("edges") or []:
            if not isinstance(edge, dict) or not edge.get("id"):
                continue
            index.edges.setdefault(edge["id"], []).append(EdgeRecord(edge, yaml_file))
            lit = edge.get("lit_type")
            if lit:
                index.by_lit.setdefault(lit, []).append(edge["id"])
    # Canonical definitions first, then stubs, each in sorted-file order:
    # callers that take the first match must never get a stub when a real
    # definition exists.
    for node_id, records in stubs.items():
        index.nodes.setdefault(node_id, []).extend(records)
    return index
