"""
schema_subset — the part of the schema an ingest agent needs, as LinkML YAML.

Writing a node file needs CellTypeMappingGraph's header, CellTypeNode, and
every class and enum they depend on: slot ranges, any_of / exactly_one_of
ranges, binding ranges (the ontology-term enums such as AnatomyTerm), and
parent classes and mixins. This module collects that set and writes it out
as a sub-schema, copying each definition verbatim from the source YAML, so
an agent reads the same descriptions, constraints and `ingest_phase`
annotations the validator uses. Comments in the source are not carried.

Graph slots no ingest step writes (OMIT) are dropped, with everything only
they reach. The result is itself a valid schema; tests load it and validate
the KB's nodes against it, so an incomplete subset fails CI.

Usage:
    uv run python -m evidencell.schema_subset [--schema PATH] [-o OUT]
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

from evidencell.paths import repo_root

DEFAULT_SCHEMA = "schema/celltype_mapping.yaml"
ROOTS = ("CellTypeMappingGraph",)
OMIT: dict[str, frozenset[str]] = {
    "CellTypeMappingGraph": frozenset({"edges", "annotation_transfer_datasets"}),
}
PHASES = ("identity", "classification", "properties")
HEADER_KEYS = ("id", "name", "description", "prefixes", "imports", "default_range")


def reachable(sv: SchemaView, roots: tuple[str, ...] = ROOTS,
              omit: dict[str, frozenset[str]] = OMIT) -> tuple[set[str], set[str]]:
    """Classes and enums reachable from `roots`, skipping slots in `omit`."""
    all_classes, all_enums = set(sv.all_classes()), set(sv.all_enums())
    classes: set[str] = set()
    enums: set[str] = set()
    queue = list(roots)
    while queue:
        cls = queue.pop()
        if cls in classes:
            continue
        classes.add(cls)
        refs = list(sv.class_ancestors(cls))
        for slot in sv.class_induced_slots(cls):
            if slot.name in omit.get(cls, ()):
                continue
            refs.append(slot.range)
            refs += [x.range for x in (slot.any_of or []) + (slot.exactly_one_of or [])]
            refs += [b.range for b in (slot.bindings or [])]
        for ref in refs:
            if ref in all_classes:
                queue.append(ref)
            elif ref in all_enums:
                enums.add(ref)
    return classes, enums


def build_subset(schema: Path | None = None) -> dict[str, Any]:
    """The sub-schema as a dict, definitions in source order."""
    path = schema or repo_root() / DEFAULT_SCHEMA
    raw = yaml.safe_load(path.read_text())
    if raw.get("slots") or raw.get("types"):
        # Everything is declared as class attributes today; top-level slots or
        # types would need collecting too.
        raise ValueError(f"{path}: top-level slots/types are not supported")
    classes, enums = reachable(SchemaView(str(path)))
    out: dict[str, Any] = {k: raw[k] for k in HEADER_KEYS if k in raw}
    out["id"] = f"{raw['id']}/ingest-subset"
    out["name"] = f"{raw['name']}_ingest_subset"
    out["enums"] = {n: d for n, d in raw["enums"].items() if n in enums}
    out["classes"] = {}
    for name, defn in raw["classes"].items():
        if name not in classes:
            continue
        if name in OMIT:
            defn = dict(defn)
            defn["attributes"] = {k: v for k, v in defn["attributes"].items()
                                  if k not in OMIT[name]}
        out["classes"][name] = defn
    return out


class _Dumper(yaml.SafeDumper):
    pass


def _str(dumper: yaml.SafeDumper, value: str) -> yaml.ScalarNode:
    # Multi-line descriptions stay readable blocks rather than escaped strings.
    style = "|" if "\n" in value.rstrip("\n") else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _str)


def render_subset(schema: Path | None = None) -> str:
    source = (schema or Path(DEFAULT_SCHEMA)).as_posix()
    head = (f"# Generated from {source} by `just schema-subset`. Do not edit.\n"
            "# The classes and enums needed to write a node file.\n")
    return head + yaml.dump(build_subset(schema), Dumper=_Dumper, sort_keys=False,
                            allow_unicode=True, width=88)


def main() -> None:
    ap = argparse.ArgumentParser(prog="python -m evidencell.schema_subset",
                                 description=__doc__.split("\n\n")[0].strip())
    ap.add_argument("--schema", type=Path, default=None)
    ap.add_argument("-o", "--output", type=Path, default=None)
    args = ap.parse_args()
    text = render_subset(args.schema)
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
