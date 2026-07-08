"""Tests for the anat_heatmap module.

Tier: fast (pure logic + a tiny temp SQLite fixture; no network/OAK/real DB).
"""

import re
import sqlite3

import pytest

from evidencell.anat_heatmap import (
    DEFAULT_MAX_ROWS,
    METRIC_COLUMNS,
    RAMP,
    HeatmapTree,
    aggregate_metric,
    ancestors_of,
    bucket_index,
    build_heatmap,
    build_heatmap_tree,
    count_rows,
    find_roots,
    flatten_tree,
    load_anat_graph,
    main,
    node_depths,
    prune,
    prune_to_connected,
    render_lines,
    suggest_cutoff,
    summarize_distribution,
)

_ANSI = re.compile(r"\x1b\[[0-9;]*m")


def _strip(s: str) -> str:
    return _ANSI.sub("", s)


# ── aggregate_metric ──────────────────────────────────────────────────────────


def test_aggregate_takes_max_over_duplicate_edges():
    rows = [
        ("MBA:754", "Olfactory tubercle", 0.20),
        ("MBA:754", "Olfactory tubercle", 0.35),  # duplicate edge, higher
        ("MBA:477", "Striatum", 0.10),
    ]
    values, labels = aggregate_metric(rows)
    assert values == {"MBA:754": 0.35, "MBA:477": 0.10}
    assert labels["MBA:754"] == "Olfactory tubercle"


def test_aggregate_skips_null_values_but_keeps_label():
    rows = [("MBA:754", "Olfactory tubercle", None)]
    values, labels = aggregate_metric(rows)
    assert values == {}
    assert labels == {"MBA:754": "Olfactory tubercle"}


# ── prune_to_connected ────────────────────────────────────────────────────────


def _toy_parents():
    # 567 (Cerebrum) ─ 698 (Olf areas) ─ 754 (Olf tubercle)
    #               └─ 477 (Striatum)  ─ 754 also? keep simple: single parent
    return {
        "MBA:754": {"MBA:698"},
        "MBA:698": {"MBA:567"},
        "MBA:477": {"MBA:567"},
        "MBA:567": set(),
    }


def test_prune_adds_connecting_ancestors():
    parents = _toy_parents()
    keep = prune_to_connected({"MBA:754"}, parents)
    assert keep == {"MBA:754", "MBA:698", "MBA:567"}


def test_prune_present_with_no_parents_is_its_own_keep():
    keep = prune_to_connected({"MBA:567"}, _toy_parents())
    assert keep == {"MBA:567"}


def test_find_roots_picks_topmost_kept_nodes():
    parents = _toy_parents()
    keep = prune_to_connected({"MBA:754", "MBA:477"}, parents)
    assert find_roots(keep, parents) == {"MBA:567"}


def test_ancestors_of_walks_to_top():
    parents = _toy_parents()
    assert ancestors_of("MBA:754", parents) == {"MBA:698", "MBA:567"}
    assert ancestors_of("MBA:567", parents) == set()


# ── bucket_index ──────────────────────────────────────────────────────────────


def test_bucket_index_endpoints_and_floor():
    n = len(RAMP)
    assert bucket_index(0.0, 1.0) == 0          # zero floors to lowest
    assert bucket_index(-1.0, 1.0) == 0          # negative floors to lowest
    assert bucket_index(1.0, 1.0) == n - 1       # max hits top bucket
    assert bucket_index(0.5, 0.0) == 0           # vmax<=0 floors to lowest


def test_bucket_index_monotonic_non_decreasing():
    vmax = 1.0
    seq = [bucket_index(v / 10, vmax) for v in range(0, 11)]
    assert seq == sorted(seq)
    assert seq[0] == 0 and seq[-1] == len(RAMP) - 1


# ── render_lines ──────────────────────────────────────────────────────────────


def test_render_sorts_children_by_descending_value_and_shows_pct():
    children = {"MBA:567": {"MBA:698", "MBA:477"}}
    keep = {"MBA:567", "MBA:698", "MBA:477"}
    values = {"MBA:567": 0.5, "MBA:698": 0.35, "MBA:477": 0.10}
    labels = {
        "MBA:567": "Cerebrum",
        "MBA:698": "Olfactory areas",
        "MBA:477": "Striatum",
    }
    lines = render_lines(["MBA:567"], children, keep, values, labels, vmax=0.5)
    plain = [_strip(line) for line in lines]
    # Root first, then higher-value child before lower-value child.
    assert "Cerebrum" in plain[0]
    assert "Olfactory areas" in plain[1]
    assert "Striatum" in plain[2]
    assert "35.0%" in plain[1] and "10.0%" in plain[2]


# ── build_heatmap (temp SQLite fixture) ───────────────────────────────────────


def _make_db(path, *, metric_col="cell_ratio", with_terms=True):
    con = sqlite3.connect(path)
    con.executescript(
        f"""
        CREATE TABLE anat (
          node_id    TEXT NOT NULL,
          anat_id    TEXT NOT NULL,
          anat_label TEXT NOT NULL,
          cell_count INTEGER,
          {metric_col} REAL
        );
        CREATE TABLE anat_hierarchy (
          parent_id TEXT NOT NULL,
          child_id  TEXT NOT NULL,
          PRIMARY KEY (parent_id, child_id)
        );
        """
    )
    if with_terms:
        con.executescript(
            """
            CREATE TABLE anat_terms (
              anat_id   TEXT PRIMARY KEY,
              label     TEXT NOT NULL,
              uberon_id TEXT
            );
            """
        )
        con.executemany(
            "INSERT INTO anat_terms VALUES (?,?,?)",
            [
                ("MBA:997", "brain", None),
                ("MBA:567", "Cerebrum", None),
                ("MBA:698", "Olfactory areas", None),
                ("MBA:754", "Olfactory tubercle", None),
                ("MBA:477", "Striatum", None),
                ("MBA:1009", "fiber tracts", None),
            ],
        )
    con.executemany(
        f"INSERT INTO anat (node_id, anat_id, anat_label, cell_count, {metric_col}) "
        f"VALUES (?,?,?,?,?)",
        [
            ("N1", "MBA:997", "brain", 100, 0.99),  # scaffold above Cerebrum
            ("N1", "MBA:567", "Cerebrum", 96, 0.96),  # scaffold above Cerebrum
            ("N1", "MBA:754", "Olfactory tubercle", 47, 0.35),
            ("N1", "MBA:754", "Olfactory tubercle", 51, 0.40),  # dup edge, max wins
            ("N1", "MBA:477", "Striatum", 39, 0.08),
            ("N1", "MBA:961", "Piriform area", 1, 0.01),  # below 5% cutoff
            ("N1", "MBA:1009", "fiber tracts", 10, 0.10),  # off-root branch
        ],
    )
    con.executemany(
        "INSERT INTO anat_hierarchy VALUES (?,?)",
        [
            ("MBA:997", "MBA:567"),    # brain → Cerebrum (scaffold)
            ("MBA:997", "MBA:1009"),   # brain → fiber tracts (off-root sibling)
            ("MBA:567", "MBA:698"),
            ("MBA:567", "MBA:477"),
            ("MBA:698", "MBA:754"),
            ("MBA:698", "MBA:961"),
        ],
    )
    con.commit()
    con.close()


def test_build_heatmap_prunes_below_cutoff_and_connects_ancestors(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    lines = build_heatmap(db, "N1", metric="cell_ratio", cutoff=0.05, root="MBA:567")
    plain = "\n".join(_strip(line) for line in lines)
    # Header + present regions + connecting ancestors shown.
    assert "Olfactory tubercle" in plain  # 0.40 ≥ cutoff
    assert "Striatum" in plain            # 0.08 ≥ cutoff
    assert "Cerebrum" in plain            # connecting ancestor
    assert "Olfactory areas" in plain     # connecting ancestor of tubercle
    # Below-cutoff region (and its non-connecting role) dropped.
    assert "Piriform area" not in plain
    # Dup-edge max aggregation reflected in the percentage.
    assert "40.0%" in plain


def test_build_heatmap_root_drops_scaffold_but_keeps_off_root_branch(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    lines = build_heatmap(db, "N1", cutoff=0.05, root="MBA:567")
    plain = [_strip(line) for line in lines]
    body = "\n".join(plain)
    # Scaffold above the chosen root is dropped (no duplicate Cerebrum subtree).
    assert "brain" not in body
    # Cerebrum appears exactly once, as a render root.
    assert sum(1 for line in plain if "Cerebrum" in line) == 1
    # The off-root branch (fiber tracts, ≥ cutoff, not under Cerebrum) survives
    # as its own root.
    assert "fiber tracts" in body


def test_build_heatmap_missing_metric_column_errors(tmp_path):
    db = tmp_path / "old.db"
    _make_db(db, metric_col="cell_ratio")  # no ratio_in_or_near_100um column
    with pytest.raises(ValueError, match="ratio_in_or_near_100um"):
        build_heatmap(db, "N1", metric="ratio_in_or_near_100um")


def test_build_heatmap_unknown_node_errors(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    with pytest.raises(ValueError, match="no `cell_ratio` values"):
        build_heatmap(db, "NOPE")


def test_build_heatmap_all_below_cutoff_errors(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    with pytest.raises(ValueError, match="no regions clear cutoff"):
        build_heatmap(db, "N1", cutoff=1.0)


def test_metric_columns_match_documented_set():
    assert METRIC_COLUMNS == ("cell_ratio", "ratio_in_or_near_100um")


# ── flatten_tree / build_heatmap_tree ─────────────────────────────────────────


def _toy_tree():
    return HeatmapTree(
        node_id="N1",
        metric="cell_ratio",
        cutoff=0.05,
        roots=["MBA:567"],
        children={"MBA:567": {"MBA:698", "MBA:477"}, "MBA:698": {"MBA:754"}},
        keep={"MBA:567", "MBA:698", "MBA:477", "MBA:754"},
        values={"MBA:567": 0.9, "MBA:698": 0.4, "MBA:477": 0.6, "MBA:754": 0.3},
        labels={
            "MBA:567": "Cerebrum",
            "MBA:698": "Olfactory areas",
            "MBA:477": "Striatum",
            "MBA:754": "Olfactory tubercle",
        },
        vmax=0.9,
    )


def test_flatten_tree_is_dfs_with_depth_and_value_sort():
    rows = flatten_tree(_toy_tree())
    seq = [(r["depth"], r["label"]) for r in rows]
    # Root, then higher-value child (Striatum 0.6) before lower (Olf areas 0.4),
    # and Olf areas' child nested one level deeper.
    assert seq == [
        (0, "Cerebrum"),
        (1, "Striatum"),
        (1, "Olfactory areas"),
        (2, "Olfactory tubercle"),
    ]


def test_build_heatmap_tree_shapes_match_ansi_path(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    tree = build_heatmap_tree(db, "N1", cutoff=0.05, root="MBA:567")
    assert tree.roots[0] == "MBA:567"
    assert "MBA:997" not in tree.keep  # scaffold dropped
    assert tree.vmax == max(tree.values.values())
    rows = flatten_tree(tree)
    labels = [r["label"] for r in rows]
    assert "Cerebrum" in labels and "fiber tracts" in labels


# ── prune / count_rows / node_depths ──────────────────────────────────────────


def test_prune_returns_empty_when_nothing_clears_cutoff():
    values = {"MBA:754": 0.02, "MBA:477": 0.01}
    roots, keep = prune(values, {}, _toy_parents(), cutoff=0.05)
    assert roots == [] and keep == set()


def test_count_rows_counts_reachable_kept_nodes():
    children = {"MBA:567": {"MBA:698", "MBA:477"}, "MBA:698": {"MBA:754"}}
    keep = {"MBA:567", "MBA:698", "MBA:477", "MBA:754"}
    assert count_rows(["MBA:567"], children, keep) == 4


def test_node_depths_shortest_hops_to_root():
    parents = _toy_parents()
    keep = {"MBA:567", "MBA:698", "MBA:754", "MBA:477"}
    depths = node_depths(keep, parents)
    assert depths["MBA:567"] == 0
    assert depths["MBA:698"] == 1
    assert depths["MBA:754"] == 2
    assert depths["MBA:477"] == 1


# ── summarize_distribution / suggest_cutoff ───────────────────────────────────


def test_summarize_reports_breadth_and_recommends_cutoff(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    graph = load_anat_graph(db, "N1")
    summary = summarize_distribution(graph, root="MBA:567", max_rows=28)
    assert summary["node_id"] == "N1"
    assert summary["max_region"]["id"] == "MBA:997"  # brain, 0.99 (overall max)
    # region counts increase as the cutoff falls.
    counts = summary["region_counts"]
    assert counts["0.50"] <= counts["0.05"]
    # recommended cutoff fits the row budget.
    assert summary["recommended_rows"] <= 28
    assert summary["recommended_cutoff"] in (0.5, 0.25, 0.10, 0.05, 0.02)


def test_summarize_finest_dominant_region_prefers_deeper(tmp_path):
    # Cerebrum (depth 0) and Striatum (depth 2) both ≥ 0.5; deeper wins.
    db = tmp_path / "tax.db"
    con = sqlite3.connect(db)
    con.executescript(
        """
        CREATE TABLE anat (node_id TEXT, anat_id TEXT, anat_label TEXT,
                           cell_count INTEGER, cell_ratio REAL);
        CREATE TABLE anat_hierarchy (parent_id TEXT, child_id TEXT,
                                     PRIMARY KEY(parent_id, child_id));
        """
    )
    con.executemany(
        "INSERT INTO anat VALUES (?,?,?,?,?)",
        [
            ("N1", "MBA:997", "brain", 100, 0.99),
            ("N1", "MBA:567", "Cerebrum", 90, 0.90),
            ("N1", "MBA:477", "Striatum", 60, 0.60),
        ],
    )
    con.executemany(
        "INSERT INTO anat_hierarchy VALUES (?,?)",
        [("MBA:997", "MBA:567"), ("MBA:567", "MBA:477")],
    )
    con.commit()
    con.close()
    graph = load_anat_graph(db, "N1")
    summary = summarize_distribution(graph)
    assert summary["finest_dominant_region"]["id"] == "MBA:477"  # deepest ≥0.5
    assert summary["finest_dominant_region"]["depth"] == 2


def test_suggest_cutoff_tightens_when_budget_small(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    graph = load_anat_graph(db, "N1")
    loose = suggest_cutoff(graph, root="MBA:567", max_rows=100)
    tight = suggest_cutoff(graph, root="MBA:567", max_rows=2)
    # A smaller row budget forces an equal-or-higher cutoff.
    assert tight >= loose


def test_build_heatmap_tree_max_rows_guard_errors(tmp_path):
    db = tmp_path / "tax.db"
    _make_db(db)
    with pytest.raises(ValueError, match="broadly distributed"):
        build_heatmap_tree(db, "N1", cutoff=0.05, root="MBA:567", max_rows=1)


# ── CLI default guard (broadly-distributed types) ─────────────────────────────


def _make_broad_db(path, *, n_regions=40):
    """A DB whose node spreads over many regions, each clearing a 5% cutoff —
    a broadly-distributed type that must trip the default row-budget guard."""
    con = sqlite3.connect(path)
    con.executescript(
        """
        CREATE TABLE anat (node_id TEXT, anat_id TEXT, anat_label TEXT,
                           cell_count INTEGER, cell_ratio REAL);
        CREATE TABLE anat_hierarchy (parent_id TEXT, child_id TEXT,
                                     PRIMARY KEY(parent_id, child_id));
        """
    )
    anat = [("N1", "MBA:567", "Cerebrum", 100, 0.90)]
    hier = []
    for i in range(n_regions):
        aid = f"MBA:{2000 + i}"
        anat.append(("N1", aid, f"region {i}", 10, 0.10))
        hier.append(("MBA:567", aid))
    con.executemany("INSERT INTO anat VALUES (?,?,?,?,?)", anat)
    con.executemany("INSERT INTO anat_hierarchy VALUES (?,?)", hier)
    con.commit()
    con.close()


def test_default_max_rows_guard_is_on(tmp_path):
    # The library constant and the CLI default agree; the guard is a real budget.
    assert DEFAULT_MAX_ROWS == 28


def test_cli_figure_refuses_broad_type_by_default(tmp_path):
    pytest.importorskip("matplotlib")
    db = tmp_path / "broad.db"
    _make_broad_db(db)
    figs = tmp_path / "figs"
    # No --max-rows: the default guard must fire and no figure may be written.
    rc = main(
        ["N1", "CCN20230722", "--db", str(db), "--root", "MBA:567",
         "--figure-dir", str(figs)]
    )
    assert rc == 1
    assert not figs.exists() or not list(figs.glob("*.png"))


def test_cli_figure_max_rows_zero_disables_guard(tmp_path):
    pytest.importorskip("matplotlib")
    db = tmp_path / "broad.db"
    _make_broad_db(db)
    figs = tmp_path / "figs"
    rc = main(
        ["N1", "CCN20230722", "--db", str(db), "--root", "MBA:567",
         "--figure-dir", str(figs), "--max-rows", "0"]
    )
    assert rc == 0
    assert list(figs.glob("*.png"))


# ── figure renderer ───────────────────────────────────────────────────────────


def test_render_anat_heatmap_figure_writes_png_and_sidecar(tmp_path):
    pytest.importorskip("matplotlib")
    from evidencell.figures import render_anat_heatmap_figure

    rows = flatten_tree(_toy_tree())
    out = tmp_path / "figs"
    png, meta = render_anat_heatmap_figure(
        rows, out, "N1",
        taxonomy_id="CCN20230722", metric="cell_ratio", cutoff=0.05, vmax=0.9,
    )
    assert png.exists() and png.suffix == ".png"
    assert meta.exists()
    body = meta.read_text(encoding="utf-8")
    assert "figure_kind: anat_heatmap" in body
    assert "renderer: evidencell.figures.render_anat_heatmap_figure" in body
    # Content-hash naming: same inputs → same filename, second call is a no-op.
    png2, meta2 = render_anat_heatmap_figure(
        rows, out, "N1",
        taxonomy_id="CCN20230722", metric="cell_ratio", cutoff=0.05, vmax=0.9,
    )
    assert png2 == png and meta2 == meta


def test_render_anat_heatmap_figure_empty_rows_errors(tmp_path):
    pytest.importorskip("matplotlib")
    from evidencell.figures import render_anat_heatmap_figure

    with pytest.raises(ValueError, match="empty rows"):
        render_anat_heatmap_figure(
            [], tmp_path, "N1",
            taxonomy_id="CCN20230722", metric="cell_ratio", cutoff=0.05, vmax=1.0,
        )
