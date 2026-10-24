"""Split a multi-type KB graph file into one file per connected component.

The split unit is **not** the classical type. Non-atlas nodes joined by
lit-to-lit edges form one indivisible unit: in cerebellum a classical type maps
to a PRIOR_TRANSCRIPTOMIC node (a T-type from a published study that is not one
of our reference taxonomies), which in turn maps to an atlas cluster, e.g.

    classical_candelabrum -> pli1_osorno -> wmb_cluster_5178

Splitting per classical type would break that chain, because
`validate.structural_checks` requires both endpoints of every edge to resolve to
a node in the same document.

Each emitted file contains:
  * the component's non-atlas nodes, verbatim;
  * thin stubs for whatever the component's edges point at;
  * the component's edges.

Nodes referenced by no edge at all cannot belong to any component. They are
reported, never silently dropped -- a component splitter that quietly discards
unreferenced nodes loses curated content with no diff to show for it.

Serialisation goes through ruamel round-trip rather than `kb_io.write_kb_yaml`
so that curatorial YAML comments survive the split. The document header comment
is shared provenance (curator, date, source analysis) and is copied to every
output file.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

ATLAS_BASIS = "ATLAS_TRANSCRIPTOMIC"

# Relations that order two lit types by breadth. `A --broadMatch--> B` means B is
# the broader thing; `A --narrowMatch--> B` means A is. Used only to name a
# multi-node component after its most general member.
_BROADER_IS_TARGET = "skos:broadMatch"
_BROADER_IS_SOURCE = "skos:narrowMatch"

# Fields a thin atlas stub may carry (CLAUDE.md: taxonomy YAML is canonical for
# atlas properties). The splitter copies stubs verbatim rather than trimming to
# this set -- stripping anatomical_location is a report-content change and
# belongs to its own change, not to a layout change.
STUB_FIELDS = ("id", "name", "definition_basis", "taxonomy_id", "cell_set_accession")

# Document-level keys carried into every component file.
DOC_KEYS = (
    "name", "description", "brain_region", "source_atlas", "target_atlas",
    "species", "creation_date",
)


def _yaml() -> YAML:
    y = YAML()
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    y.width = 4096
    return y


@dataclass
class Component:
    """One indivisible split unit."""

    representative: str
    node_ids: list[str] = field(default_factory=list)
    edge_ids: list[str] = field(default_factory=list)


@dataclass
class SplitPlan:
    source: Path
    components: list[Component] = field(default_factory=list)
    orphan_atlas: list[str] = field(default_factory=list)

    @property
    def is_noop(self) -> bool:
        """True when splitting this file would produce nothing useful.

        Either it is already exactly one whole component -- splitting would
        only rename it, losing the header provenance for no gain -- or it has
        no components at all (a stub dump or a crosswalk), in which case there
        is nothing to split.

        Note there is no `orphan_non_atlas`: every non-atlas node is placed in
        a component by construction, including edgeless ones, which become
        single-node components. Unmapped literature types therefore always
        survive the split.
        """
        if not self.components:
            return True
        return len(self.components) == 1 and not self.orphan_atlas


def is_stub(node: dict) -> bool:
    return node.get("definition_basis") == ATLAS_BASIS


def plan_split(doc: dict, source: Path) -> SplitPlan:
    """Compute components without writing anything."""
    nodes = {n["id"]: n for n in doc.get("nodes") or [] if n.get("id")}
    edges = [e for e in doc.get("edges") or [] if isinstance(e, dict)]
    non_atlas = {i for i, n in nodes.items() if not is_stub(n)}

    parent = {i: i for i in non_atlas}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge in edges:
        a, b = edge.get("lit_type"), edge.get("taxonomy_type")
        if a in non_atlas and b in non_atlas:
            parent[find(a)] = find(b)

    groups: dict[str, list[str]] = {}
    for node_id in sorted(non_atlas):
        groups.setdefault(find(node_id), []).append(node_id)

    plan = SplitPlan(source=source)
    referenced: set[str] = set()
    for members in sorted(groups.values(), key=lambda m: sorted(m)[0]):
        members = sorted(members)
        member_set = set(members)
        comp_edges = [
            e for e in edges
            if e.get("lit_type") in member_set or e.get("taxonomy_type") in member_set
        ]
        representative = _representative(members, comp_edges)
        for edge in comp_edges:
            referenced.update(
                x for x in (edge.get("lit_type"), edge.get("taxonomy_type")) if x
            )
        plan.components.append(
            Component(
                representative=representative,
                node_ids=members,
                edge_ids=[e.get("id", "") for e in comp_edges],
            )
        )

    for node_id, node in nodes.items():
        if node_id not in referenced and is_stub(node):
            plan.orphan_atlas.append(node_id)

    plan.orphan_atlas.sort()
    return plan


def _representative(members: list[str], comp_edges: list[dict]) -> str:
    """Name a component after its most general member.

    A multi-node component is a general type plus its subtypes -- O-LM with the
    two Chamberland transgene-defined subfamilies, say. Naming the file after
    whichever member sorts first would call that file
    `chrna2_olm_subfamily_chamberland.yaml`, which misrepresents what it holds.

    Breadth comes from the component's own broad/narrow edges. If exactly one
    member has nothing broader than it, that member names the file; otherwise
    (no breadth edges, or several roots) fall back to alphabetical, which is
    stable and arbitrary rather than misleading.
    """
    member_set = set(members)
    has_broader: set[str] = set()
    for edge in comp_edges:
        a, b = edge.get("lit_type"), edge.get("taxonomy_type")
        if a not in member_set or b not in member_set:
            continue
        rel = edge.get("relationship")
        if rel == _BROADER_IS_TARGET:
            has_broader.add(a)
        elif rel == _BROADER_IS_SOURCE:
            has_broader.add(b)
    roots = [m for m in members if m not in has_broader]
    return roots[0] if len(roots) == 1 else members[0]


def build_component_doc(doc: dict, component: Component) -> CommentedMap:
    """Assemble one component's document, preserving node/edge comments."""
    nodes = {n["id"]: n for n in doc.get("nodes") or [] if n.get("id")}
    edges = {e.get("id"): e for e in doc.get("edges") or [] if isinstance(e, dict)}

    member_set = set(component.node_ids)
    comp_edges = [edges[eid] for eid in component.edge_ids if eid in edges]

    # Stub targets, in first-reference order so the file reads in edge order.
    stub_ids: list[str] = []
    for edge in comp_edges:
        for endpoint in (edge.get("lit_type"), edge.get("taxonomy_type")):
            if (
                endpoint
                and endpoint not in member_set
                and endpoint not in stub_ids
                and endpoint in nodes
            ):
                stub_ids.append(endpoint)

    out = CommentedMap()
    for key in DOC_KEYS:
        if key in doc:
            out[key] = doc[key]

    out_nodes = CommentedSeq()
    for node_id in component.node_ids:
        out_nodes.append(nodes[node_id])
    for node_id in stub_ids:
        out_nodes.append(nodes[node_id])
    out["nodes"] = out_nodes

    out_edges = CommentedSeq()
    for edge in comp_edges:
        out_edges.append(edge)
    out["edges"] = out_edges
    return out


def verify_conservation(doc: dict, plan: SplitPlan) -> list[str]:
    """Check every node and edge survives the split. Returns problem strings.

    Run before writing anything. The reference-store migration taught this the
    hard way: a splitter that writes first and verifies after can leave a
    proven-wrong split shadowing an intact original.
    """
    problems: list[str] = []
    src_nodes = {n["id"] for n in doc.get("nodes") or [] if n.get("id")}
    src_edges = {e.get("id") for e in doc.get("edges") or [] if isinstance(e, dict)}

    out_nodes: set[str] = set()
    out_edges: set[str] = set()
    for component in plan.components:
        out_doc = build_component_doc(doc, component)
        out_nodes.update(n["id"] for n in out_doc["nodes"] if n.get("id"))
        out_edges.update(e.get("id") for e in out_doc["edges"] if isinstance(e, dict))

    missing_edges = src_edges - out_edges
    if missing_edges:
        problems.append(f"edges lost: {sorted(missing_edges)}")

    missing_nodes = src_nodes - out_nodes - set(plan.orphan_atlas)
    if missing_nodes:
        problems.append(f"nodes lost: {sorted(missing_nodes)}")

    # Every emitted edge endpoint must resolve within its own document, or
    # validate.structural_checks will reject the file.
    for component in plan.components:
        out_doc = build_component_doc(doc, component)
        ids = {n["id"] for n in out_doc["nodes"] if n.get("id")}
        for edge in out_doc["edges"]:
            for endpoint in (edge.get("lit_type"), edge.get("taxonomy_type")):
                if endpoint and endpoint not in ids:
                    problems.append(
                        f"{component.representative}: edge {edge.get('id')} endpoint "
                        f"'{endpoint}' does not resolve in-document"
                    )
    return problems


def split_file(
    source: Path,
    *,
    dry_run: bool = True,
    out_dir: Path | None = None,
) -> SplitPlan:
    """Split `source` into one file per component under `out_dir`.

    Refuses to proceed if any component file would collide with another, or if
    an output path already exists.
    """
    y = _yaml()
    with source.open(encoding="utf-8") as fh:
        doc = y.load(fh)

    plan = plan_split(doc, source)
    out_dir = out_dir or source.parent

    targets = {c.representative: out_dir / f"{c.representative}.yaml" for c in plan.components}
    if len(set(targets.values())) != len(targets):
        raise ValueError(f"Component filenames collide under {out_dir}")

    problems = verify_conservation(doc, plan)
    if problems:
        raise ValueError(
            f"Refusing to split {source} -- content would not be preserved:\n  "
            + "\n  ".join(problems)
        )

    if dry_run:
        return plan

    if plan.is_noop:
        return plan

    existing = [p for p in targets.values() if p.exists() and p != source]
    if existing:
        raise FileExistsError(
            "Refusing to overwrite: " + ", ".join(str(p) for p in existing)
        )

    # Preserve the file header comment -- shared provenance for every component.
    header = getattr(doc.ca, "comment", None)

    out_dir.mkdir(parents=True, exist_ok=True)
    for component in plan.components:
        out_doc = build_component_doc(doc, component)
        if header is not None:
            out_doc.ca.comment = header
        with targets[component.representative].open("w", encoding="utf-8") as fh:
            y.dump(out_doc, fh)
    return plan


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m evidencell.split_graph",
        description="Split a KB graph file into one file per connected component.",
    )
    parser.add_argument("graph_file", type=Path)
    parser.add_argument("--out-dir", type=Path, default=None)
    parser.add_argument(
        "--apply", action="store_true",
        help="Write the component files. Without this, only the plan is printed.",
    )
    args = parser.parse_args(argv)

    try:
        plan = split_file(args.graph_file, dry_run=not args.apply, out_dir=args.out_dir)
    except (ValueError, FileExistsError, OSError) as exc:
        # A refused split is an expected outcome for a curator running this,
        # not a crash. Print the reason, not a traceback.
        print(f"split-graph: {exc}", file=sys.stderr)
        return 1

    print(f"{plan.source}: {len(plan.components)} component(s)")
    if not plan.components:
        print("  no components (no non-atlas nodes) -- nothing to split, file left as is")
    elif plan.is_noop:
        print("  already a single whole component -- no split needed, file left as is")
    for component in plan.components:
        print(
            f"  {component.representative}.yaml"
            f"  nodes={component.node_ids}"
            f"  edges={len(component.edge_ids)}"
        )
    if plan.orphan_atlas:
        print(f"  !! {len(plan.orphan_atlas)} atlas stub(s) referenced by no edge "
              f"-- NOT emitted: {plan.orphan_atlas}")
    if not args.apply:
        print("  (dry run -- pass --apply to write)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
