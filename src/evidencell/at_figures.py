"""Tree-style annotation transfer figures.

Renders an F1 tree figure for a MapMyCells (or other AT) run: parent
chain on the left (one lane per taxonomy rank), F1 bar plus precision /
recall as text on each node, vertical layout one panel per source group
(or pooled group).

Design points:

* **Rank-independent.** Lane order is taken from the taxonomy's
  ``level_hierarchy`` (loaded via ``taxonomy_db``). For taxonomies with
  different rank counts or names, the figure renders accordingly.
* **Parent resolution via taxonomy DB**, not name heuristics — joins each
  ``f1_matrix.csv`` row to its ``node_id`` and then walks ``parent_id``.
* **Leaf cutoff.** Drops rank-0 targets with ``n_cells / source_total <
  cutoff_pct`` (default 5%). Internal ancestors that lose all kept
  descendants are pruned too.
* **Redundant-ancestor pruning.** An internal node whose precision and
  recall match its single rendered child within ``PRUNE_TOL`` is
  collapsed away — it carries no new information.
* **Source pooling.** ``--pool srcA,srcB,...:new_name`` (repeatable)
  combines multiple source labels into one synthetic source group with
  recomputed P / R / F1.

CLI::

    python -m evidencell.at_figures RUN_ID
        [--pool srcA,srcB:NAME ...]
        [--output PATH]              # relative to run dir; default
                                     # figures/f1_heatmap.png (overwrite)
        [--cutoff FRACTION]          # default 0.05
        [--cmap NAME]                # default YlOrRd
        [--title TEXT]

The companion ``just gen-at-figure {run_id} ...`` recipe is the usual
entry point.

Supersedes the per-run ad-hoc figure scripts (e.g.
``kb/annotation_transfer_runs/at_run_*/scripts/render_f1_heatmap.py``);
those are retained in-place as historical record.
"""

from __future__ import annotations

import argparse
import csv
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import yaml
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

from .paths import repo_root


# Default tuning knobs (CLI can override cutoff)
DEFAULT_CUTOFF_PCT = 0.05
PRUNE_TOL = 0.01           # P/R difference below this counts as "same"
DEFAULT_CMAP = "YlOrRd"


# ─── Data loading ─────────────────────────────────────────────────────────────


def load_f1_matrix(run_dir: Path, csv_relpath: str = "f1_matrix.csv") -> list[dict]:
    """Read the F1 matrix CSV from an AT run directory.

    ``csv_relpath`` defaults to ``f1_matrix.csv`` but should be passed from
    the manifest's ``output.relpath`` field for runs that use a different
    output filename (e.g. ``f1_scores_best.csv``).
    """
    csv_path = run_dir / csv_relpath
    if not csv_path.exists():
        raise FileNotFoundError(
            f"F1 matrix not found at {csv_path}. Run manifest's "
            f"output.relpath may need updating, or pass --f1 explicitly."
        )
    with csv_path.open() as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        # Some runs emit `best_target` (top-hit-only) instead of `target_name`
        # (full matrix). Normalise to `target_name`.
        if "target_name" not in r and "best_target" in r:
            r["target_name"] = r["best_target"]
        r["n_cells"] = int(r["n_cells"])
        for k in ("group_purity", "target_purity", "f1"):
            r[k] = float(r[k])
    return rows


def load_manifest(run_dir: Path) -> dict:
    return yaml.safe_load((run_dir / "manifest.yaml").read_text())


def load_level_order(taxonomy_id: str) -> list[str]:
    """Return CSV-level names (lowercased) ordered coarsest → finest.

    Reads ``level_hierarchy`` from ``kb/taxonomy/{taxonomy_id}/taxonomy_meta.yaml``.
    """
    meta_path = (
        repo_root() / "kb" / "taxonomy" / taxonomy_id / "taxonomy_meta.yaml"
    )
    meta = yaml.safe_load(meta_path.read_text())
    levels = sorted(meta["level_hierarchy"], key=lambda L: -L["rank"])
    return [L["level_name"].lower() for L in levels]


# ─── Parent resolution via taxonomy DB ────────────────────────────────────────


def _open_taxonomy_db(taxonomy_id: str) -> sqlite3.Connection:
    db_path = (
        repo_root() / "kb" / "taxonomy" / taxonomy_id / f"{taxonomy_id}.db"
    )
    if not db_path.exists():
        raise FileNotFoundError(
            f"Taxonomy DB not found at {db_path}. Run "
            f"`just build-taxonomy-db {taxonomy_id}` first."
        )
    return sqlite3.connect(db_path)


def _rank_for_level(taxonomy_id: str, level_name: str) -> int:
    """Map CSV level name (lowercase) → integer rank."""
    meta_path = (
        repo_root() / "kb" / "taxonomy" / taxonomy_id / "taxonomy_meta.yaml"
    )
    meta = yaml.safe_load(meta_path.read_text())
    for L in meta["level_hierarchy"]:
        if L["level_name"].lower() == level_name.lower():
            return L["rank"]
    raise KeyError(f"level {level_name!r} not in taxonomy_meta.yaml")


def attach_node_ids(rows: list[dict], taxonomy_id: str) -> None:
    """Attach ``node_id`` (= accession) to each row by label + rank lookup.

    Mutates ``rows`` in place. Rows whose label has no DB match are left
    without a ``node_id`` and will not contribute parent edges.
    """
    conn = _open_taxonomy_db(taxonomy_id)
    cur = conn.cursor()
    # Cache (rank, label) → node_id
    cache: dict[tuple[int, str], str | None] = {}
    for r in rows:
        rank = _rank_for_level(taxonomy_id, r["level"])
        key = (rank, r["target_name"])
        if key not in cache:
            cur.execute(
                "SELECT node_id FROM nodes "
                "WHERE label = ? AND taxonomy_rank = ?",
                (r["target_name"], rank),
            )
            row = cur.fetchone()
            cache[key] = row[0] if row else None
        r["node_id"] = cache[key]
    conn.close()


def lookup_parent_chain(
    leaf_node_id: str, taxonomy_id: str
) -> dict[int, dict]:
    """Return {rank: {node_id, label}} walking from leaf to root."""
    conn = _open_taxonomy_db(taxonomy_id)
    cur = conn.cursor()
    chain: dict[int, dict] = {}
    cursor_id: str | None = leaf_node_id
    while cursor_id:
        cur.execute(
            "SELECT node_id, label, parent_id, taxonomy_rank "
            "FROM nodes WHERE node_id = ?",
            (cursor_id,),
        )
        row = cur.fetchone()
        if not row:
            break
        node_id, label, parent_id, rank = row
        chain[rank] = {"node_id": node_id, "label": label}
        cursor_id = parent_id
    conn.close()
    return chain


# ─── Source pooling ───────────────────────────────────────────────────────────


def pool_sources(
    rows: list[dict], pool_spec: dict[str, str]
) -> list[dict]:
    """Pool rows whose ``source_label`` is in ``pool_spec`` keys.

    ``pool_spec`` maps original source label → new pooled name. Returns a
    new list of rows with pooled groups carrying recomputed
    group_purity / target_purity / f1. Non-pooled rows pass through
    unchanged.
    """
    if not pool_spec:
        return list(rows)

    finest = None
    levels_in_csv = {r["level"] for r in rows}
    # Pick the level with the largest count of rows as a proxy for finest
    # (production: use load_level_order(taxonomy_id)[-1]). This is fine
    # because the caller passes a single AT run and rank-0 rows are
    # always present.
    finest = max(levels_in_csv, key=lambda L: sum(1 for r in rows if r["level"] == L))

    # Reconstruct target totals from any contributing row (target_total =
    # n_cells / target_purity when target_purity > 0).
    target_totals: dict[tuple[str, str], float] = {}
    for r in rows:
        if r["target_purity"] > 0:
            key = (r["level"], r["target_name"])
            target_totals.setdefault(key, r["n_cells"] / r["target_purity"])

    # New source-group totals: sum of n_cells at finest level across pooled inputs
    pooled_src_totals: dict[str, int] = defaultdict(int)
    for r in rows:
        new_src = pool_spec.get(r["source_label"])
        if new_src is None:
            continue
        if r["level"] == finest:
            pooled_src_totals[new_src] += r["n_cells"]

    # Aggregate pooled rows
    pool_acc: dict[tuple[str, str, str], dict] = {}
    keep: list[dict] = []
    for r in rows:
        new_src = pool_spec.get(r["source_label"])
        if new_src is None:
            keep.append(r)
            continue
        key = (new_src, r["level"], r["target_name"])
        agg = pool_acc.setdefault(
            key,
            {
                "source_label": new_src,
                "level": r["level"],
                "target_name": r["target_name"],
                "n_cells": 0,
                "node_id": r.get("node_id"),
            },
        )
        agg["n_cells"] += r["n_cells"]

    for (src, lvl, name), agg in pool_acc.items():
        src_total = pooled_src_totals[src] or 1
        t_total = target_totals.get((lvl, name)) or agg["n_cells"]
        rec = agg["n_cells"] / src_total
        prec = agg["n_cells"] / t_total if t_total else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        keep.append(
            {
                **agg,
                "group_purity": rec,
                "target_purity": prec,
                "f1": f1,
                "mean_boot": 0.0,
                "median_boot": 0.0,
            }
        )
    return keep


# ─── Rendering ────────────────────────────────────────────────────────────────


def _approx_equal(a: float, b: float, tol: float = PRUNE_TOL) -> bool:
    return abs(a - b) <= tol


def render_tree(
    rows: list[dict],
    levels: list[str],
    taxonomy_id: str,
    *,
    out_path: Path,
    title: str,
    cutoff_pct: float = DEFAULT_CUTOFF_PCT,
    cmap_name: str = DEFAULT_CMAP,
) -> Path:
    """Render the tree figure to ``out_path``. Returns the written path."""
    attach_node_ids(rows, taxonomy_id)

    by_source: dict[str, dict[str, list[dict]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for r in rows:
        by_source[r["source_label"]][r["level"]].append(r)
    source_labels = sorted(by_source.keys())
    finest = levels[-1]

    # Build per-source leaf list after cutoff
    leaves_kept: dict[str, list[dict]] = {}
    source_totals: dict[str, int] = {}
    for src in source_labels:
        leaves = by_source[src].get(finest, [])
        total = sum(r["n_cells"] for r in leaves)
        source_totals[src] = total
        cutoff_n = max(1, int(total * cutoff_pct))
        leaves_kept[src] = [r for r in leaves if r["n_cells"] >= cutoff_n]

    # Build per-leaf parent chains using the taxonomy DB
    per_leaf_chain_by_src: dict[str, list[dict[str, dict]]] = {}
    keep_node_by_src: dict[str, dict[tuple[str, str], bool]] = {}

    chain_pairs = list(zip(levels[:-1], levels[1:]))  # (parent_lvl, child_lvl)
    rank_to_level = {
        _rank_for_level(taxonomy_id, lvl): lvl for lvl in levels
    }

    for src in source_labels:
        clusters_sorted = sorted(
            leaves_kept[src], key=lambda r: -r["n_cells"]
        )
        chains: list[dict[str, dict]] = []
        for leaf in clusters_sorted:
            chain: dict[str, dict] = {finest: leaf}
            if not leaf.get("node_id"):
                chains.append(chain)
                continue
            anc = lookup_parent_chain(leaf["node_id"], taxonomy_id)
            for rank, info in anc.items():
                lvl = rank_to_level.get(rank)
                if not lvl or lvl == finest:
                    continue
                # Pull the rendered F1/P/R for that ancestor from the CSV
                # rows at this level + label, if present.
                hits = [
                    r
                    for r in by_source[src].get(lvl, [])
                    if r["target_name"] == info["label"]
                ]
                if hits:
                    chain[lvl] = hits[0]
            chains.append(chain)
        per_leaf_chain_by_src[src] = chains

        # Per-chain inactive levels: ancestor with P,R ≈ child's P,R
        inactive = [set() for _ in chains]
        for i, chain in enumerate(chains):
            for parent_lvl, child_lvl in chain_pairs:
                p = chain.get(parent_lvl)
                c = chain.get(child_lvl)
                if p is None or c is None:
                    continue
                if _approx_equal(
                    p["target_purity"], c["target_purity"]
                ) and _approx_equal(
                    p["group_purity"], c["group_purity"]
                ):
                    inactive[i].add(parent_lvl)

        # Vote: prune iff every leaf containing the parent flagged it
        votes: dict[tuple[str, str], list[bool]] = defaultdict(list)
        for i, chain in enumerate(chains):
            for lvl in levels[:-1]:
                if lvl not in chain:
                    continue
                votes[(lvl, chain[lvl]["target_name"])].append(
                    lvl in inactive[i]
                )
        keep_node_by_src[src] = {k: not all(v) for k, v in votes.items()}

    # Globally-surviving levels (finest always survives)
    surviving_levels: list[str] = []
    for lvl in levels:
        if lvl == finest:
            surviving_levels.append(lvl)
            continue
        for src in source_labels:
            survived = False
            for chain in per_leaf_chain_by_src[src]:
                if lvl in chain and keep_node_by_src[src].get(
                    (lvl, chain[lvl]["target_name"]), True
                ):
                    survived = True
                    break
            if survived:
                surviving_levels.append(lvl)
                break

    # Lane geometry — packed left in coarsest → finest order
    lane_x: dict[str, float] = {}
    lane_w: dict[str, float] = {}
    cur_x = 0.2
    for lvl in surviving_levels:
        rank_idx = levels.index(lvl)
        w = 1.5 + 0.25 * rank_idx
        lane_w[lvl] = w
        lane_x[lvl] = cur_x
        cur_x += w + 0.25
    x_max = cur_x + 0.05

    max_rows = max(len(leaves_kept[s]) for s in source_labels)
    row_height = 0.55
    panel_height = 0.6 + row_height * max(max_rows, 1)
    fig_w = min(8.3, x_max * 0.95)
    fig, axes = plt.subplots(
        len(source_labels),
        1,
        figsize=(fig_w, panel_height * len(source_labels) + 1.2),
        constrained_layout=True,
        squeeze=False,
    )

    norm = Normalize(vmin=0.0, vmax=1.0)
    cmap = plt.colormaps[cmap_name]
    f1_scalar = ScalarMappable(norm=norm, cmap=cmap)

    for src_idx, src in enumerate(source_labels):
        ax = axes[src_idx, 0]
        ax.set_xlim(-0.2, x_max)
        per_leaf_chain = per_leaf_chain_by_src[src]
        keep_node = keep_node_by_src[src]
        n_rows = max(len(per_leaf_chain), 1)
        ax.set_ylim(-1.4, n_rows - 0.5)
        ax.invert_yaxis()

        total = source_totals[src]
        kept_total = sum(c[finest]["n_cells"] for c in per_leaf_chain)
        ax.set_title(
            f"{src}  (n={total} cells; {kept_total} shown after "
            f"{int(cutoff_pct * 100)}% leaf cutoff)",
            loc="left",
            fontsize=10,
            fontweight="bold",
            pad=8,
        )

        for lvl in surviving_levels:
            ax.text(
                lane_x[lvl] + lane_w[lvl] / 2,
                -0.95,
                lvl.capitalize(),
                ha="center",
                va="center",
                fontsize=9,
                fontweight="bold",
            )

        # y-positions for kept parent nodes
        parent_y: dict[tuple[str, str], list[float]] = defaultdict(list)
        for y, chain in enumerate(per_leaf_chain):
            for lvl in surviving_levels:
                if lvl == finest or lvl not in chain:
                    continue
                key = (lvl, chain[lvl]["target_name"])
                if keep_node.get(key, True):
                    parent_y[key].append(y)
        drawn_parents = {
            k: sum(ys) / len(ys) for k, ys in parent_y.items()
        }

        rendered: set[tuple[str, str]] = set()
        for y, chain in enumerate(per_leaf_chain):
            prev_xy: tuple[float, float] | None = None
            for lvl in surviving_levels:
                row = chain.get(lvl)
                if not row:
                    continue
                key = (lvl, row["target_name"])
                if lvl != finest and not keep_node.get(key, True):
                    continue
                node_y = (
                    y if lvl == finest else drawn_parents.get(key, y)
                )
                x = lane_x[lvl]
                w = lane_w[lvl]

                if key not in rendered:
                    color = f1_scalar.to_rgba(row["f1"])
                    ax.add_patch(
                        mpatches.FancyBboxPatch(
                            (x, node_y - 0.38),
                            w,
                            0.76,
                            boxstyle="round,pad=0.02,rounding_size=0.06",
                            linewidth=0.6,
                            edgecolor="black",
                            facecolor=color,
                        )
                    )
                    name = row["target_name"]
                    max_chars = int(w * 14)
                    if len(name) > max_chars:
                        name = name[: max_chars - 1] + "…"
                    pval = row["target_purity"]
                    rval = row["group_purity"]
                    n_str = (
                        f"  n={row['n_cells']}" if lvl == finest else ""
                    )
                    label = (
                        f"{name}{n_str}\n"
                        f"F1={row['f1']:.2f}  "
                        f"(P={pval:.2f}, R={rval:.2f})"
                    )
                    text_color = (
                        "white" if row["f1"] > 0.55 else "black"
                    )
                    ax.text(
                        x + w / 2,
                        node_y,
                        label,
                        ha="center",
                        va="center",
                        fontsize=6.4,
                        color=text_color,
                    )
                    rendered.add(key)

                if prev_xy is not None:
                    px, py = prev_xy
                    ax.plot(
                        [px, x],
                        [py, node_y],
                        color="gray",
                        linewidth=0.8,
                        zorder=0,
                    )
                prev_xy = (x + w, node_y)

        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ("top", "right", "bottom", "left"):
            ax.spines[spine].set_visible(False)

    fig.suptitle(title, fontsize=10, y=1.06)
    cbar = fig.colorbar(
        f1_scalar, ax=axes.ravel().tolist(), shrink=0.5, pad=0.01
    )
    cbar.set_label("F1 (tree fill)", fontsize=9)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ─── CLI ──────────────────────────────────────────────────────────────────────


def _parse_pool_args(pool_args: Iterable[str]) -> dict[str, str]:
    """Parse ``--pool srcA,srcB:NAME`` repeats into a {src: name} dict."""
    spec: dict[str, str] = {}
    for item in pool_args:
        if ":" not in item:
            raise ValueError(
                f"--pool expects 'srcA,srcB,...:NEW_NAME', got {item!r}"
            )
        srcs, _, new = item.partition(":")
        new = new.strip()
        if not new:
            raise ValueError(f"--pool missing target name in {item!r}")
        for s in srcs.split(","):
            s = s.strip()
            if not s:
                continue
            spec[s] = new
    return spec


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="evidencell.at_figures",
        description=(
            "Render the tree-style F1 figure for an AT run. "
            "Pooling is per-invocation; call twice to write split + merged "
            "panels alongside each other."
        ),
    )
    p.add_argument("run_id", help="AT run id (subdir under kb/annotation_transfer_runs/)")
    p.add_argument(
        "--pool",
        action="append",
        default=[],
        metavar="SRC1,SRC2,...:NAME",
        help="Pool source labels into a new group (repeatable).",
    )
    p.add_argument(
        "--output",
        default="figures/f1_heatmap.png",
        help="Output path relative to the run dir (default overwrites figures/f1_heatmap.png).",
    )
    p.add_argument(
        "--cutoff", type=float, default=DEFAULT_CUTOFF_PCT,
        help=f"Leaf-cutoff fraction (default {DEFAULT_CUTOFF_PCT}).",
    )
    p.add_argument(
        "--cmap", default=DEFAULT_CMAP,
        help=f"Matplotlib colormap (default {DEFAULT_CMAP}).",
    )
    p.add_argument("--title", default=None)
    p.add_argument(
        "--f1",
        default=None,
        help=(
            "F1 matrix CSV path relative to the run dir. Defaults to "
            "manifest's output.relpath, then to 'f1_matrix.csv'."
        ),
    )
    p.add_argument(
        "--source",
        default=None,
        metavar="LABEL[,LABEL,...]",
        help=(
            "Comma-separated source_label values to keep. All other source "
            "groups are dropped before rendering. Useful for trimming "
            "multi-source AT figures down to the rows relevant to one "
            "report. Applied AFTER --pool, so the new pooled label is what "
            "you filter on."
        ),
    )
    args = p.parse_args(argv)

    run_dir = (
        repo_root() / "kb" / "annotation_transfer_runs" / args.run_id
    )
    if not run_dir.exists():
        print(f"AT run not found: {run_dir}", file=sys.stderr)
        return 2

    manifest = load_manifest(run_dir)
    taxonomy_id = manifest.get("target_taxonomy_id") or manifest.get(
        "atlas", {}
    ).get("taxonomy_id")
    if not taxonomy_id:
        print(
            f"Could not find target_taxonomy_id in {run_dir}/manifest.yaml",
            file=sys.stderr,
        )
        return 2

    f1_relpath = (
        args.f1
        or manifest.get("output", {}).get("relpath")
        or "f1_matrix.csv"
    )
    rows = load_f1_matrix(run_dir, f1_relpath)
    levels = load_level_order(taxonomy_id)
    attach_node_ids(rows, taxonomy_id)

    pool_spec = _parse_pool_args(args.pool)
    if pool_spec:
        rows = pool_sources(rows, pool_spec)

    if args.source:
        keep_labels = {s.strip() for s in args.source.split(",") if s.strip()}
        available = {r["source_label"] for r in rows}
        missing = keep_labels - available
        if missing:
            print(
                f"warning: --source labels not found in F1 matrix: "
                f"{sorted(missing)}; available: {sorted(available)}",
                file=sys.stderr,
            )
        rows = [r for r in rows if r["source_label"] in keep_labels]
        if not rows:
            print(
                f"error: no rows survive --source filter {sorted(keep_labels)}; "
                f"available source labels: {sorted(available)}",
                file=sys.stderr,
            )
            return 2

    title = args.title or (
        f"Annotation Transfer ({args.run_id} → {taxonomy_id})  "
        f"·  fill = F1 ({args.cmap})  ·  leaf cutoff "
        f"{int(args.cutoff * 100)}%"
    )

    out_path = run_dir / args.output
    written = render_tree(
        rows,
        levels,
        taxonomy_id,
        out_path=out_path,
        title=title,
        cutoff_pct=args.cutoff,
        cmap_name=args.cmap,
    )
    print(f"Wrote {written}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
