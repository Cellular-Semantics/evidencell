"""Programmatic figure generation for paper-style mapping reports.

Figures are deterministic outputs: same inputs → same hash → same filename.
Each figure is committed alongside the report it accompanies, with a
sidecar `.meta.yaml` carrying provenance (render timestamp, evidencell
commit, input hash, parameters, caption).

The content-hashed filename is the report-figure sync mechanism: if the
underlying data changes, the hash changes, the filename changes, and the
old report's `![caption](figures/foo_a3f72b.png)` reference becomes a
visibly broken link rather than a silent stale visual.

See `planning/paper_style_reports_review_addendum.md` §4 for design rationale.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import yaml


__all__ = [
    "render_top_n_hits_figure",
    "render_anat_heatmap_figure",
]


def _content_hash(payload: dict[str, Any]) -> str:
    """SHA-256 short hash (8 chars) of canonical JSON of the payload.

    Same dict → same hash. Used to stamp figure filenames so that a change
    in input data or rendering parameters produces a new filename.
    """
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:8]


def render_top_n_hits_figure(
    hits: list[dict],
    out_dir: Path,
    node_id: str,
    contrast_id: str,
    *,
    caption: str | None = None,
    framework_version: str = "",
    figure_kind: str = "delta_ranked_bar",
) -> tuple[Path, Path]:
    """Render a horizontal bar chart of top-N hits ranked by δ.

    The target row (hit['is_target'] == True) is highlighted. Outputs:
      out_dir/{node_id}_{short_contrast}_{sha8}.png
      out_dir/{node_id}_{short_contrast}_{sha8}.meta.yaml

    Returns (png_path, meta_path).

    `hits` is the list produced by `render._top_n_hits_for_contrast`:
    each row carries cluster_id, label, parent_supertype, mfr, top_anat,
    delta, is_target.

    Side-effect free if the file already exists with the matching content
    hash — this lets the renderer regenerate facts cheaply when nothing
    has changed.
    """
    import matplotlib
    matplotlib.use("Agg")  # no display backend; safe in CI / headless
    import matplotlib.pyplot as plt

    if not hits:
        raise ValueError("Cannot render figure for empty hits list")

    short_contrast = contrast_id.removeprefix("corr_")
    payload = {
        "node_id": node_id,
        "contrast_id": contrast_id,
        "figure_kind": figure_kind,
        "hits": hits,
    }
    sha8 = _content_hash(payload)
    out_dir.mkdir(parents=True, exist_ok=True)
    png_path = out_dir / f"{node_id}_{short_contrast}_{sha8}.png"
    meta_path = out_dir / f"{node_id}_{short_contrast}_{sha8}.meta.yaml"

    if png_path.exists() and meta_path.exists():
        return png_path, meta_path

    # Plot — ranks 1..N from top to bottom so rank 1 is at the top.
    n = len(hits)
    deltas = []
    labels = []
    is_target = []
    for h in hits:
        try:
            deltas.append(float(h.get("delta", 0.0)))
        except (TypeError, ValueError):
            deltas.append(0.0)
        cid = h.get("cluster_id", "")
        # Strip the standard CCN prefix to keep labels short for the figure
        cid_short = cid.replace("CS20230722_", "")
        lab = h.get("label", "")
        # Trim long labels
        lab_short = lab if len(lab) <= 36 else lab[:33] + "…"
        labels.append(f"{h.get('rank', '')}  {cid_short}  {lab_short}")
        is_target.append(bool(h.get("is_target", False)))

    fig, ax = plt.subplots(figsize=(7.5, 0.45 * n + 0.8))
    y_pos = list(range(n - 1, -1, -1))  # rank 1 at top
    colours = ["#1f77b4" if not t else "#d62728" for t in is_target]
    edgecolours = ["#11425c" if not t else "#7a1f1f" for t in is_target]
    ax.barh(y_pos, deltas, color=colours, edgecolor=edgecolours, linewidth=0.6)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel(r"$\delta$ (rank-correlation differential)", fontsize=9)
    title = caption or f"Top {n} clusters by {short_contrast}"
    ax.set_title(title, fontsize=10, loc="left")
    ax.tick_params(axis="x", labelsize=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle=":", alpha=0.5)
    if any(is_target):
        # Compact legend explaining the highlight colour
        from matplotlib.patches import Patch
        ax.legend(
            handles=[Patch(facecolor="#d62728", label="target match")],
            loc="lower right", fontsize=8, frameon=False,
        )
    fig.tight_layout()
    fig.savefig(png_path, dpi=180)
    plt.close(fig)

    # Sidecar metadata for audit
    from datetime import datetime, timezone
    meta = {
        "figure_kind": figure_kind,
        "node_id": node_id,
        "contrast_id": contrast_id,
        "inputs_sha": sha8,
        "n_hits": n,
        "rendered_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "framework_version": framework_version,
        "caption": caption or title,
        "renderer": "evidencell.figures.render_top_n_hits_figure",
    }
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False), encoding="utf-8")

    return png_path, meta_path


def render_anat_heatmap_figure(
    rows: list[dict],
    out_dir: Path,
    node_id: str,
    *,
    taxonomy_id: str,
    metric: str,
    cutoff: float,
    vmax: float,
    caption: str | None = None,
    framework_version: str = "",
) -> tuple[Path, Path]:
    """Render an anatomy-ontology heat-map as an indented coloured tree PNG.

    `rows` is the DFS-flattened tree from
    `evidencell.anat_heatmap.flatten_tree`: each row has ``depth``, ``anat_id``,
    ``label``, ``value``. Each region is drawn as a coloured swatch (value →
    `evidencell.anat_heatmap.RAMP` bucket) at an x-offset set by its depth, with
    the percentage inside the swatch and the region label to its right.

    Outputs (content-hashed for report-sync, like `render_top_n_hits_figure`):
      out_dir/{node_id}_anat_{metric}_{sha8}.png
      out_dir/{node_id}_anat_{metric}_{sha8}.meta.yaml

    Returns (png_path, meta_path). No-op if a file with the matching content
    hash already exists.
    """
    import matplotlib
    matplotlib.use("Agg")  # no display backend; safe in CI / headless
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    from evidencell.anat_heatmap import RAMP, bucket_index

    if not rows:
        raise ValueError("Cannot render anat heat-map for empty rows list")

    payload = {
        "node_id": node_id,
        "taxonomy_id": taxonomy_id,
        "metric": metric,
        "cutoff": cutoff,
        "vmax": vmax,
        "rows": rows,
    }
    sha8 = _content_hash(payload)
    safe_metric = metric.replace("/", "_")
    out_dir.mkdir(parents=True, exist_ok=True)
    png_path = out_dir / f"{node_id}_anat_{safe_metric}_{sha8}.png"
    meta_path = out_dir / f"{node_id}_anat_{safe_metric}_{sha8}.meta.yaml"

    if png_path.exists() and meta_path.exists():
        return png_path, meta_path

    n = len(rows)
    max_depth = max(r["depth"] for r in rows)
    indent = 0.28            # x units per depth level
    chip_w = 1.3             # swatch width in x units
    label_gap = 0.12

    # Width grows with deepest indent + longest label; height with row count.
    longest_label = max(len(r["label"]) for r in rows)
    fig_w = 3.0 + indent * max_depth + chip_w + 0.075 * longest_label
    fig_h = 0.30 * n + 0.7
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))

    for i, row in enumerate(rows):
        y = n - 1 - i        # row 0 at the top
        x0 = row["depth"] * indent
        idx = bucket_index(row["value"], vmax, len(RAMP))
        r, g, b = RAMP[idx]
        face = (r / 255, g / 255, b / 255)
        text_col = "black" if idx >= 5 else "white"
        # Faint indentation guides connecting nesting levels.
        for d in range(row["depth"]):
            ax.plot(
                [d * indent + chip_w * 0.04] * 2,
                [y - 0.5, y + 0.5],
                color="#cccccc", linewidth=0.5, zorder=0,
            )
        ax.add_patch(
            Rectangle(
                (x0, y - 0.36), chip_w, 0.72,
                facecolor=face, edgecolor="#33333344", linewidth=0.4, zorder=2,
            )
        )
        ax.text(
            x0 + chip_w / 2, y, f"{row['value'] * 100:.1f}%",
            ha="center", va="center", fontsize=7.5, color=text_col, zorder=3,
        )
        ax.text(
            x0 + chip_w + label_gap, y, row["label"],
            ha="left", va="center", fontsize=8, color="#222222", zorder=3,
        )

    ax.set_xlim(-0.1, indent * max_depth + chip_w + label_gap + 0.075 * longest_label + 0.5)
    ax.set_ylim(-0.7, n)
    ax.axis("off")
    title = caption or (
        f"{node_id} — soma distribution ({metric} ≥ {cutoff * 100:.0f}%)"
    )
    ax.set_title(title, fontsize=10, loc="left")
    fig.tight_layout()
    fig.savefig(png_path, dpi=180, bbox_inches="tight")
    plt.close(fig)

    from datetime import datetime, timezone
    meta = {
        "figure_kind": "anat_heatmap",
        "node_id": node_id,
        "taxonomy_id": taxonomy_id,
        "metric": metric,
        "cutoff": cutoff,
        "vmax": vmax,
        "inputs_sha": sha8,
        "n_rows": n,
        "rendered_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "framework_version": framework_version,
        "caption": caption or title,
        "renderer": "evidencell.figures.render_anat_heatmap_figure",
    }
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False), encoding="utf-8")

    return png_path, meta_path
