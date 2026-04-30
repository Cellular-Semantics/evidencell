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
    bars = ax.barh(y_pos, deltas, color=colours, edgecolor=edgecolours, linewidth=0.6)

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
