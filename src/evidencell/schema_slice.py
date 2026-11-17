"""
schema_slice — render the schema slice an ingest agent needs for one phase.

Slots an ingest agent fills carry two annotations (#202):
`ingest_question` (the question whose answer fills the slot) and
`ingest_phase` (identity | properties). This module renders, for one phase,
each such slot's question, description, range and allowed values, plus the
shape of every class those slots reach. Workflow prompts include this output
instead of hand-written field lists, so the field guidance an agent reads
cannot drift from the schema.

Usage:
    uv run python -m evidencell.schema_slice <phase> [--class CellTypeNode] [--schema PATH]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from linkml_runtime.linkml_model.meta import SlotDefinition  # type: ignore[import-untyped]
from linkml_runtime.utils.schemaview import SchemaView  # type: ignore[import-untyped]

from evidencell.paths import repo_root

PHASES = ("identity", "properties")
DEFAULT_SCHEMA = "schema/celltype_mapping.yaml"


def _ann(slot: SlotDefinition, tag: str) -> str | None:
    ann = slot.annotations or {}
    return str(ann[tag].value) if tag in ann else None


def _flat(text: str | None) -> str:
    return " ".join((text or "").split())


def _cardinality(slot: SlotDefinition) -> str:
    bits = ["required" if slot.required else "optional"]
    bits.append("list" if slot.multivalued else "single value")
    return ", ".join(bits)


def phase_slots(sv: SchemaView, cls: str, phase: str) -> list[SlotDefinition]:
    """Induced slots of `cls` tagged with `phase`, in schema order."""
    return [s for s in sv.class_induced_slots(cls) if _ann(s, "ingest_phase") == phase]


def _enum_lines(sv: SchemaView, enum: str) -> list[str]:
    out = []
    for name, pv in (sv.get_enum(enum).permissible_values or {}).items():
        desc = _flat(pv.description)
        out.append(f"  - `{name}`" + (f": {desc}" if desc else ""))
    return out


def _reachable_classes(sv: SchemaView, roots: list[str], skip: set[str]) -> list[str]:
    """Classes reachable from `roots` through slot ranges, breadth-first."""
    seen: list[str] = []
    queue = [r for r in roots if r not in skip]
    while queue:
        cls = queue.pop(0)
        if cls in seen:
            continue
        seen.append(cls)
        for s in sv.class_induced_slots(cls):
            if s.range in sv.all_classes() and s.range not in skip and s.range not in seen:
                queue.append(s.range)
    return seen


def _shape(sv: SchemaView, cls: str, phase: str) -> list[str]:
    lines = [f"### {cls}", ""]
    if desc := _flat(sv.get_class(cls).description):
        lines += [desc, ""]
    for s in sv.class_induced_slots(cls):
        rng = s.range or "string"
        line = f"- `{s.name}` ({_cardinality(s)}; {rng})"
        if d := _flat(s.description):
            line += f": {d}"
        lines.append(line)
        if _ann(s, "ingest_phase") == phase and (q := _ann(s, "ingest_question")):
            lines.append(f"  - **Question:** {_flat(q)}")
        if rng in sv.all_enums():
            lines += _enum_lines(sv, rng)
    return lines + [""]


def render_slice(phase: str, cls: str = "CellTypeNode",
                 schema: Path | None = None) -> str:
    """Markdown slice for `phase`: questions on `cls`, then reachable class shapes."""
    if phase not in PHASES:
        raise ValueError(f"phase must be one of {PHASES}, not '{phase}'")
    sv = SchemaView(str(schema or repo_root() / DEFAULT_SCHEMA))
    slots = phase_slots(sv, cls, phase)
    if not slots:
        raise ValueError(f"no {cls} slots carry ingest_phase: {phase}")

    lines = [f"## {cls} fields: {phase} phase", ""]
    for s in slots:
        rng = s.range or "string"
        lines += [f"### `{s.name}`", "",
                  f"**Question:** {_flat(_ann(s, 'ingest_question'))}", "",
                  f"Range: {rng} ({_cardinality(s)})", ""]
        if d := _flat(s.description):
            lines += [d, ""]
        if rng in sv.all_enums():
            lines += ["Allowed values:"] + _enum_lines(sv, rng) + [""]

    roots = [s.range for s in slots if s.range in sv.all_classes()]
    shapes = _reachable_classes(sv, roots, skip={cls})
    if shapes:
        lines += ["## Shapes of the classes these fields use", ""]
        for c in shapes:
            lines += _shape(sv, c, phase)
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(prog="python -m evidencell.schema_slice",
                                 description=__doc__.split("\n\n")[0].strip())
    ap.add_argument("phase", choices=PHASES)
    ap.add_argument("--class", dest="cls", default="CellTypeNode")
    ap.add_argument("--schema", type=Path, default=None)
    args = ap.parse_args()
    try:
        print(render_slice(args.phase, args.cls, args.schema), end="")
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
