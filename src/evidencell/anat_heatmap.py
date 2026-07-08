"""Heat-map of a taxonomy node's anatomical-location distribution, painted
onto the brain anatomy ontology hierarchy.

For one taxonomy node (cluster/supertype accession) this reads the per-region
soma distribution from the taxonomy SQLite index (`anat` table), prunes the
anatomy ontology tree (`anat_hierarchy` / `anat_terms`) down to the regions
that clear a cutoff plus the ancestors needed to connect them, and renders the
tree with each region coloured by its metric value.

The core logic is factored into pure functions (aggregation, pruning, root
finding, colour bucketing, tree rendering) so it can be unit-tested without a
database and so a non-ANSI renderer can be slotted in for report figures later.

CLI:

    python -m evidencell.anat_heatmap NODE_ID TAXONOMY_ID [--cutoff 0.05]
        [--metric cell_ratio|ratio_in_or_near_100um] [--root MBA:567]

The anatomy ontology is the one baked into the taxonomy's `anat_hierarchy` /
`anat_terms` tables at DB-build time; `--root` selects where rendering starts
(e.g. `MBA:567` Cerebrum to drop the universal brain scaffold).
"""

from __future__ import annotations

import sqlite3
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from evidencell.paths import taxonomy_db_path

__all__ = [
    "RAMP",
    "METRIC_COLUMNS",
    "AnatGraph",
    "HeatmapTree",
    "aggregate_metric",
    "prune_to_connected",
    "ancestors_of",
    "find_roots",
    "prune",
    "count_rows",
    "node_depths",
    "bucket_index",
    "flatten_tree",
    "render_lines",
    "load_anat_graph",
    "summarize_distribution",
    "suggest_cutoff",
    "build_heatmap_tree",
    "build_heatmap",
    "main",
]

# Metric columns selectable from the `anat` table. cell_ratio is soma strictly
# in region; ratio_in_or_near_100um is the softer "in or within 100µm" variant.
METRIC_COLUMNS = ("cell_ratio", "ratio_in_or_near_100um")

# Default figure row budget. The CLI applies this guard by default so a
# broadly-distributed type can never render a giant figure by accident; pass
# `--max-rows 0` to opt out. The library functions keep max_rows=None
# (unlimited) so programmatic callers stay explicit.
DEFAULT_MAX_ROWS = 28

# Colour ramp: viridis-ish steps as truecolor RGB, low → high.
RAMP: list[tuple[int, int, int]] = [
    (40, 40, 80),     # very low
    (60, 60, 140),
    (40, 110, 170),
    (50, 160, 160),
    (90, 200, 120),
    (200, 210, 60),
    (240, 160, 40),
    (230, 90, 40),
    (180, 30, 40),    # highest
]

_RESET = "\x1b[0m"
_GAMMA = 0.6  # <1 expands contrast at the low end of the ramp


# ── pure logic ───────────────────────────────────────────────────────────────


def aggregate_metric(
    rows: list[tuple[str, str, float | None]],
) -> tuple[dict[str, float], dict[str, str]]:
    """Aggregate per-region metric values, taking the max over duplicate edges.

    `rows` is an iterable of ``(anat_id, anat_label, value)``. A single
    (node, region) pair can appear on multiple edges; we keep the maximum
    value seen and the last non-empty label.

    Returns ``(values, labels)`` where ``values`` maps anat_id → max value
    (regions with only NULL values are omitted) and ``labels`` maps anat_id →
    label.
    """
    values: dict[str, float] = {}
    labels: dict[str, str] = {}
    for anat_id, label, value in rows:
        if label:
            labels[anat_id] = label
        if value is not None:
            values[anat_id] = max(values.get(anat_id, 0.0), float(value))
    return values, labels


def prune_to_connected(
    present: set[str], parents: dict[str, set[str]]
) -> set[str]:
    """Expand `present` upward to include every ancestor needed to connect it.

    Walks parent links from each present node until no new ancestors are
    found. The returned set is closed under "parent of a kept node".
    """
    keep = set(present)
    frontier = set(present)
    while frontier:
        nxt: set[str] = set()
        for node in frontier:
            for parent in parents.get(node, ()):
                if parent not in keep:
                    keep.add(parent)
                    nxt.add(parent)
        frontier = nxt
    return keep


def find_roots(keep: set[str], parents: dict[str, set[str]]) -> set[str]:
    """Roots of the pruned forest: kept nodes with no kept parent."""
    return {n for n in keep if not (parents.get(n, set()) & keep)}


def ancestors_of(node: str, parents: dict[str, set[str]]) -> set[str]:
    """All proper ancestors of `node` reachable via parent links.

    Used to drop the universal scaffold above a chosen `--root`: a region
    whose only path to the natural root runs through the scaffold becomes a
    new root once the scaffold is removed, so genuine off-root branches still
    render while the scaffold above `root` does not duplicate `root`'s subtree.
    """
    seen: set[str] = set()
    frontier = set(parents.get(node, ()))
    while frontier:
        nxt: set[str] = set()
        for n in frontier:
            if n not in seen:
                seen.add(n)
                nxt |= parents.get(n, set())
        frontier = nxt
    return seen


def prune(
    values: dict[str, float],
    children: dict[str, set[str]],
    parents: dict[str, set[str]],
    cutoff: float,
    root: str | None = None,
) -> tuple[list[str], set[str]]:
    """Prune the anatomy graph to regions clearing `cutoff` + connectors.

    Pure counterpart of the pruning inside `build_heatmap_tree`: returns
    ``(ordered_roots, keep)``. ``ordered_roots`` is empty (and ``keep`` empty)
    when no region clears the cutoff. When `root` is given and kept, its proper
    ancestors are dropped so its subtree renders once.
    """
    present = {a for a, v in values.items() if v >= cutoff}
    if not present:
        return [], set()
    keep = prune_to_connected(present, parents)
    if root and root in keep:
        keep -= ancestors_of(root, parents)
    all_roots = find_roots(keep, parents)
    ordered: list[str] = []
    if root and root in keep:
        ordered.append(root)
    for r in sorted(all_roots - set(ordered), key=lambda x: -values.get(x, 0.0)):
        ordered.append(r)
    return ordered, keep


def count_rows(
    roots: list[str], children: dict[str, set[str]], keep: set[str]
) -> int:
    """Number of rows a pruned forest renders to (one per kept node reached)."""
    seen: set[str] = set()
    stack = list(roots)
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(children.get(node, set()) & keep)
    return len(seen)


def node_depths(
    keep: set[str], parents: dict[str, set[str]]
) -> dict[str, int]:
    """Depth (shortest hops to a kept root) for each kept node."""
    depth: dict[str, int] = {}

    def of(n: str, stack: frozenset[str]) -> int:
        if n in depth:
            return depth[n]
        kept_parents = (parents.get(n, set()) & keep) - stack
        if not kept_parents:
            depth[n] = 0
        else:
            depth[n] = 1 + min(of(p, stack | {n}) for p in kept_parents)
        return depth[n]

    for n in keep:
        of(n, frozenset())
    return depth


def bucket_index(val: float, vmax: float, n: int = len(RAMP), gamma: float = _GAMMA) -> int:
    """Map a value in [0, vmax] onto a ramp bucket index in [0, n-1].

    Non-positive values or a non-positive vmax bucket to 0 (lowest). A gamma
    < 1 expands contrast at the low end so small regions remain distinguishable.
    """
    if vmax <= 0 or val <= 0:
        return 0
    return min(n - 1, int((val / vmax) ** gamma * (n - 1)))


@dataclass
class AnatGraph:
    """Loaded anatomy data for one node, independent of any cutoff.

    Separating the DB load from pruning lets `summarize_distribution` trial
    several cutoffs without re-querying the DB.
    """

    node_id: str
    metric: str
    values: dict[str, float]   # anat_id → max metric value (measured regions)
    labels: dict[str, str]
    children: dict[str, set[str]]
    parents: dict[str, set[str]]


@dataclass
class HeatmapTree:
    """Structured result of pruning the anatomy tree for one node.

    Carries everything a renderer (ANSI or figure) needs without touching the
    DB again. `roots` is the render order (chosen root first, then off-root
    branches by descending value).
    """

    node_id: str
    metric: str
    cutoff: float
    roots: list[str]
    children: dict[str, set[str]]
    keep: set[str]
    values: dict[str, float]
    labels: dict[str, str]
    vmax: float


def flatten_tree(tree: HeatmapTree) -> list[dict]:
    """DFS-flatten a HeatmapTree into render rows (same order as the ANSI walk).

    Each row is ``{"depth", "anat_id", "label", "value"}``. Children are
    ordered by descending value, matching `render_lines`.
    """
    rows: list[dict] = []

    def walk(aid: str, depth: int) -> None:
        rows.append(
            {
                "depth": depth,
                "anat_id": aid,
                "label": tree.labels.get(aid, aid),
                "value": tree.values.get(aid, 0.0),
            }
        )
        kids = sorted(
            tree.children.get(aid, set()) & tree.keep,
            key=lambda k: -tree.values.get(k, 0.0),
        )
        for kid in kids:
            walk(kid, depth + 1)

    for root in tree.roots:
        walk(root, 0)
    return rows


def _ansi_chip(value: float, vmax: float, text: str) -> str:
    """An ANSI truecolor swatch wrapping `text`, coloured by `value`."""
    idx = bucket_index(value, vmax)
    r, g, b = RAMP[idx]
    fg = "0;0;0" if idx >= 5 else "230;230;230"
    return f"\x1b[48;2;{r};{g};{b}m\x1b[38;2;{fg}m{text}{_RESET}"


def render_lines(
    roots: list[str],
    children: dict[str, set[str]],
    keep: set[str],
    values: dict[str, float],
    labels: dict[str, str],
    *,
    vmax: float,
    secondary_metric: dict[str, float] | None = None,
) -> list[str]:
    """Render the pruned tree as ANSI lines, one per kept node.

    Children are sorted by descending metric value. `secondary_metric`, when
    given, is appended in parentheses (e.g. the 100µm-soft ratio alongside the
    strict ratio).
    """
    lines: list[str] = []

    def label_of(aid: str) -> str:
        return labels.get(aid, aid)

    def walk(aid: str, prefix: str, is_last: bool) -> None:
        connector = "└─ " if is_last else "├─ "
        val = values.get(aid, 0.0)
        chip = _ansi_chip(val, vmax, f" {val * 100:5.1f}% ")
        line = f"{prefix}{connector}{chip} {label_of(aid)}"
        if secondary_metric is not None:
            line += f"  (alt {secondary_metric.get(aid, 0.0):.2f})"
        lines.append(line)
        nxt_prefix = prefix + ("   " if is_last else "│  ")
        kids = sorted(
            children.get(aid, set()) & keep,
            key=lambda k: -values.get(k, 0.0),
        )
        for i, kid in enumerate(kids):
            walk(kid, nxt_prefix, i == len(kids) - 1)

    for i, root in enumerate(roots):
        walk(root, "", i == len(roots) - 1)
    return lines


def legend_line(vmax: float) -> str:
    """A one-line ANSI colour legend keyed to the ramp / vmax."""
    parts = ["legend (% cells): "]
    n = len(RAMP)
    for i, (r, g, b) in enumerate(RAMP):
        fg = "0;0;0" if i >= 5 else "230;230;230"
        edge = (i / (n - 1)) ** (1 / _GAMMA) * vmax * 100
        parts.append(
            f"\x1b[48;2;{r};{g};{b}m\x1b[38;2;{fg}m {edge:4.0f} {_RESET}"
        )
    return "".join(parts)


# ── DB access ────────────────────────────────────────────────────────────────


def _table_columns(con: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in con.execute(f"PRAGMA table_info({table})")}


def _load_node_metric(
    con: sqlite3.Connection, node_id: str, metric: str
) -> tuple[dict[str, float], dict[str, str]]:
    cols = _table_columns(con, "anat")
    if metric not in cols:
        available = sorted(cols & set(METRIC_COLUMNS))
        raise ValueError(
            f"metric column {metric!r} is not in the `anat` table "
            f"(available: {available or 'none'}). The taxonomy DB may predate "
            f"this column; rebuild it with `just build-taxonomy-db <id>`."
        )
    rows = con.execute(
        f"SELECT anat_id, anat_label, {metric} FROM anat WHERE node_id = ?",
        (node_id,),
    ).fetchall()
    return aggregate_metric(rows)


def _load_hierarchy(
    con: sqlite3.Connection,
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    children: dict[str, set[str]] = defaultdict(set)
    parents: dict[str, set[str]] = defaultdict(set)
    for parent_id, child_id in con.execute(
        "SELECT parent_id, child_id FROM anat_hierarchy"
    ):
        children[parent_id].add(child_id)
        parents[child_id].add(parent_id)
    return children, parents


def _load_term_labels(con: sqlite3.Connection) -> dict[str, str]:
    try:
        return {
            aid: label
            for aid, label in con.execute(
                "SELECT anat_id, label FROM anat_terms"
            )
        }
    except sqlite3.OperationalError:
        return {}


def load_anat_graph(
    db_path: Path, node_id: str, *, metric: str = "cell_ratio"
) -> AnatGraph:
    """Load the per-node anat values, labels, and the ontology hierarchy.

    Raises ValueError if the metric column is absent from the DB or the node
    has no anat rows for the chosen metric.
    """
    con = sqlite3.connect(db_path)
    try:
        values, labels = _load_node_metric(con, node_id, metric)
        if not values:
            raise ValueError(
                f"no `{metric}` values for node {node_id!r} in {db_path} "
                f"(check the accession and that the DB is freshly built)."
            )
        children, parents = _load_hierarchy(con)
        # anat_terms gives labels for ancestor scaffold nodes not on the node's
        # own edges; node labels (from `anat`) take precedence.
        term_labels = _load_term_labels(con)
        labels = {**term_labels, **labels}
    finally:
        con.close()
    return AnatGraph(
        node_id=node_id,
        metric=metric,
        values=values,
        labels=labels,
        children=children,
        parents=parents,
    )


# Cutoffs trialled (descending) when summarising breadth / picking a row budget.
_CANDIDATE_CUTOFFS = (0.5, 0.25, 0.10, 0.05, 0.02)


def summarize_distribution(
    graph: AnatGraph,
    *,
    root: str | None = None,
    max_rows: int = 28,
    candidate_cutoffs: tuple[float, ...] = _CANDIDATE_CUTOFFS,
) -> dict:
    """Describe how concentrated/dispersed a node's soma distribution is.

    Returns a JSON-able dict an agent can read *without* rendering a figure, to
    decide whether a heat-map is informative for identity and at what cutoff:

    - `max_region` / `finest_dominant_region` — where the cells concentrate;
      a deep region holding the majority means a focal, discriminating type,
      while only shallow (large-region) majorities mean a broad type whose
      fine localisation is not identity-informative.
    - `region_counts` — measured regions at increasing cutoffs (a high count at
      a low cutoff signals broad dispersal).
    - `figure_rows_by_cutoff` / `recommended_cutoff` — keep the figure within a
      `max_rows` budget; `recommended_cutoff` is the most detailed cutoff that
      still fits.
    """
    values = graph.values
    fixed_cutoffs = (0.05, 0.10, 0.25, 0.50)

    top_id = max(values, key=lambda k: values[k])
    region_counts = {
        f"{c:.2f}": sum(1 for v in values.values() if v >= c)
        for c in fixed_cutoffs
    }

    # Finest (deepest) region whose ratio ≥ 0.5 — a focal-localisation signal.
    keep_all = set(values)
    depths = node_depths(keep_all, graph.parents)
    dominant = [(depths.get(a, 0), values[a], a) for a in values if values[a] >= 0.5]
    finest_dominant = max(dominant) if dominant else None

    rows_by_cutoff: dict[str, int] = {}
    for c in candidate_cutoffs:
        roots, keep = prune(values, graph.children, graph.parents, c, root)
        rows_by_cutoff[f"{c:.2f}"] = count_rows(roots, graph.children, keep)

    # Recommended: most detailed (lowest) cutoff whose figure fits the budget.
    recommended = max(candidate_cutoffs)
    for c in sorted(candidate_cutoffs):
        if rows_by_cutoff[f"{c:.2f}"] <= max_rows:
            recommended = c
            break

    return {
        "node_id": graph.node_id,
        "metric": graph.metric,
        "n_measured_regions": len(values),
        "max_region": {
            "id": top_id, "label": graph.labels.get(top_id, top_id),
            "ratio": round(values[top_id], 4),
        },
        "finest_dominant_region": (
            None if finest_dominant is None else {
                "id": finest_dominant[2],
                "label": graph.labels.get(finest_dominant[2], finest_dominant[2]),
                "ratio": round(finest_dominant[1], 4),
                "depth": finest_dominant[0],
            }
        ),
        "region_counts": region_counts,
        "figure_rows_by_cutoff": rows_by_cutoff,
        "recommended_cutoff": recommended,
        "recommended_rows": rows_by_cutoff[f"{recommended:.2f}"],
        "max_rows_budget": max_rows,
    }


def suggest_cutoff(
    graph: AnatGraph,
    *,
    root: str | None = None,
    max_rows: int = 28,
    candidate_cutoffs: tuple[float, ...] = _CANDIDATE_CUTOFFS,
) -> float:
    """The most detailed cutoff keeping the figure within `max_rows`."""
    summary = summarize_distribution(
        graph, root=root, max_rows=max_rows, candidate_cutoffs=candidate_cutoffs
    )
    return summary["recommended_cutoff"]


def build_heatmap_tree(
    db_path: Path,
    node_id: str,
    *,
    metric: str = "cell_ratio",
    cutoff: float = 0.05,
    root: str | None = None,
    max_rows: int | None = None,
) -> HeatmapTree:
    """Load and prune the anatomy tree for one node into a HeatmapTree.

    Raises ValueError if the node has no anat rows for the chosen metric, if the
    metric column is absent from the DB, if no region clears the cutoff, or if
    `max_rows` is set and the pruned tree exceeds it (a too-low cutoff for a
    broadly-distributed type — raise rather than emit a giant figure).
    """
    graph = load_anat_graph(db_path, node_id, metric=metric)
    ordered, keep = prune(graph.values, graph.children, graph.parents, cutoff, root)
    if not ordered:
        raise ValueError(
            f"no regions clear cutoff {cutoff} for node {node_id!r} "
            f"(max {metric} = {max(graph.values.values()):.3f})."
        )

    n_rows = count_rows(ordered, graph.children, keep)
    if max_rows is not None and n_rows > max_rows:
        raise ValueError(
            f"pruned tree has {n_rows} rows (> max_rows {max_rows}) for node "
            f"{node_id!r} at cutoff {cutoff} — this type is broadly distributed; "
            f"raise --cutoff (see `summarize_distribution` for a recommendation) "
            f"or accept that fine soma localisation is not identity-informative."
        )

    return HeatmapTree(
        node_id=node_id,
        metric=metric,
        cutoff=cutoff,
        roots=ordered,
        children=graph.children,
        keep=keep,
        values=graph.values,
        labels=graph.labels,
        vmax=max(graph.values.values()),
    )


def build_heatmap(
    db_path: Path,
    node_id: str,
    *,
    metric: str = "cell_ratio",
    cutoff: float = 0.05,
    root: str | None = None,
) -> list[str]:
    """Build the heat-map for one node as ANSI text lines."""
    tree = build_heatmap_tree(
        db_path, node_id, metric=metric, cutoff=cutoff, root=root
    )
    header = (
        f"{tree.node_id} — anatomy heat-map "
        f"({tree.metric} ≥ {tree.cutoff * 100:.0f}%)"
    )
    return [header, "", legend_line(tree.vmax), ""] + render_lines(
        tree.roots,
        tree.children,
        tree.keep,
        tree.values,
        tree.labels,
        vmax=tree.vmax,
    )


# ── CLI ──────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        prog="python -m evidencell.anat_heatmap",
        description=(
            "Render an ANSI heat-map of a taxonomy node's anatomical-location "
            "distribution painted onto the brain anatomy ontology hierarchy."
        ),
    )
    parser.add_argument("node_id", help="Taxonomy cluster/supertype accession.")
    parser.add_argument(
        "taxonomy_id",
        help="Taxonomy id; resolves the SQLite DB path under kb/taxonomy/.",
    )
    parser.add_argument(
        "--cutoff",
        type=float,
        default=0.05,
        help="Metric threshold for a region to be shown. Default 0.05 (5%%).",
    )
    parser.add_argument(
        "--metric",
        choices=METRIC_COLUMNS,
        default="cell_ratio",
        help="anat column to colour by. Default cell_ratio.",
    )
    parser.add_argument(
        "--root",
        default=None,
        help="Ontology node to start rendering from (e.g. MBA:567 Cerebrum).",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=None,
        help="Override the taxonomy DB path (default: derived from taxonomy_id).",
    )
    parser.add_argument(
        "--figure-dir",
        type=Path,
        default=None,
        help=(
            "Render a PNG report figure (+ .meta.yaml sidecar) into this "
            "directory instead of printing ANSI. Filename is content-hashed."
        ),
    )
    parser.add_argument(
        "--caption",
        default=None,
        help="Caption/title override for the PNG figure.",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=DEFAULT_MAX_ROWS,
        help=(
            f"Refuse to render if the pruned tree exceeds this many rows "
            f"(guards against giant figures for broadly-distributed types). "
            f"Default {DEFAULT_MAX_ROWS}; pass 0 to disable the guard."
        ),
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help=(
            "Emit distribution-breadth JSON (max/finest region, region counts, "
            "rows-by-cutoff, recommended cutoff) instead of rendering. Use this "
            "to decide whether a heat-map is informative and at what cutoff."
        ),
    )
    args = parser.parse_args(argv)

    db_path = args.db or taxonomy_db_path(args.taxonomy_id)
    if not db_path.exists():
        parser.error(f"taxonomy DB not found: {db_path}")

    if args.summary:
        import json

        try:
            graph = load_anat_graph(db_path, args.node_id, metric=args.metric)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        # Summary always needs a positive budget to recommend a cutoff; a
        # disabled guard (0) falls back to the default budget for the advice.
        summary = summarize_distribution(
            graph,
            root=args.root,
            max_rows=args.max_rows if args.max_rows > 0 else DEFAULT_MAX_ROWS,
        )
        print(json.dumps(summary, indent=2))
        return 0

    if args.figure_dir is not None:
        from evidencell.figures import render_anat_heatmap_figure

        try:
            tree = build_heatmap_tree(
                db_path,
                args.node_id,
                metric=args.metric,
                cutoff=args.cutoff,
                root=args.root,
                max_rows=args.max_rows if args.max_rows > 0 else None,
            )
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        png_path, meta_path = render_anat_heatmap_figure(
            flatten_tree(tree),
            args.figure_dir,
            args.node_id,
            taxonomy_id=args.taxonomy_id,
            metric=args.metric,
            cutoff=args.cutoff,
            vmax=tree.vmax,
            caption=args.caption,
        )
        print(png_path)
        print(meta_path)
        return 0

    try:
        lines = build_heatmap(
            db_path,
            args.node_id,
            metric=args.metric,
            cutoff=args.cutoff,
            root=args.root,
        )
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
