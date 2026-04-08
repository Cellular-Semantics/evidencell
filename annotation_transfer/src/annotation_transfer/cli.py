"""CLI entry points for the annotation transfer pipeline.

Usage:
    annotation-transfer convert INPUT OUTPUT [--cluster-col COL --cluster-value VAL --label-col COL]
    annotation-transfer score MMC_CSV LABELS_JSON OUTPUT [--threshold 0.8]
    annotation-transfer map INPUT STATS MARKERS OUTPUT_JSON [--csv PATH]
    annotation-transfer preflight FILE
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def cmd_convert(args: argparse.Namespace) -> None:
    import anndata as ad
    from annotation_transfer.convert import prepare_for_mapmycells, save_source_labels
    from annotation_transfer.preflight import preflight_gate

    preflight_gate(args.input, auto_approve=args.yes)

    adata = ad.read_h5ad(args.input)
    labels = prepare_for_mapmycells(
        adata,
        args.output,
        cluster_col=args.cluster_col,
        cluster_value=args.cluster_value,
        label_col=args.label_col,
    )

    if labels:
        labels_path = args.output.with_suffix(".labels.json")
        save_source_labels(labels, labels_path)
        print(f"Source labels: {labels_path} ({len(labels)} cells)")

    print(f"MapMyCells-ready: {args.output}")


def cmd_score(args: argparse.Namespace) -> None:
    from annotation_transfer.convert import load_source_labels
    from annotation_transfer.score import compute_f1_matrix, best_mappings

    labels = load_source_labels(args.labels)
    f1_df = compute_f1_matrix(
        args.mmc_csv,
        labels,
        threshold=args.threshold,
    )

    f1_df.to_csv(args.output, index=False)
    print(f"F1 matrix: {args.output} ({len(f1_df)} rows)")

    best = best_mappings(f1_df)
    best_path = args.output.with_name(args.output.stem + "_best.csv")
    best.to_csv(best_path, index=False)
    print(f"Best mappings: {best_path}")

    # Print summary
    print("\n--- Best mappings ---")
    for label in best["source_label"].unique():
        print(f"\n== {label} ==")
        subset = best[best["source_label"] == label]
        print(
            subset[["level", "best_target", "group_purity", "target_purity", "f1", "n_cells"]]
            .to_string(index=False)
        )


def cmd_map(args: argparse.Namespace) -> None:
    from annotation_transfer.mapper import run_mapmycells

    csv_path = args.csv if args.csv else args.output_json.with_suffix(".csv")
    run_mapmycells(
        args.input,
        args.precomputed_stats,
        args.marker_genes,
        args.output_json,
        output_csv=csv_path,
    )
    print(f"MapMyCells result: {args.output_json}")
    print(f"MapMyCells CSV:    {csv_path}")


def cmd_preflight(args: argparse.Namespace) -> None:
    from annotation_transfer.preflight import check_resources

    report = check_resources(args.file)
    print(report.summary())
    sys.exit(0 if report.fits else 1)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="annotation-transfer",
        description="Annotation transfer pipeline: convert, map, score.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # convert
    p_conv = sub.add_parser("convert", help="Convert h5ad to MapMyCells-ready format")
    p_conv.add_argument("input", type=Path, help="Input h5ad file")
    p_conv.add_argument("output", type=Path, help="Output MapMyCells-ready h5ad")
    p_conv.add_argument("--cluster-col", help="obs column to slice on")
    p_conv.add_argument("--cluster-value", help="Value to filter cluster-col")
    p_conv.add_argument("--label-col", help="obs column for source labels (default: cluster-col)")
    p_conv.add_argument("-y", "--yes", action="store_true", help="Skip preflight confirmation")

    # score
    p_score = sub.add_parser("score", help="Compute F1 matrix from MapMyCells output")
    p_score.add_argument("mmc_csv", type=Path, help="MapMyCells output CSV")
    p_score.add_argument("labels", type=Path, help="Source labels JSON")
    p_score.add_argument("output", type=Path, help="Output F1 matrix CSV")
    p_score.add_argument("--threshold", type=float, default=0.8, help="Bootstrap threshold")

    # map
    p_map = sub.add_parser("map", help="Run MapMyCells (requires cell_type_mapper)")
    p_map.add_argument("input", type=Path, help="MapMyCells-ready h5ad")
    p_map.add_argument("precomputed_stats", type=Path, help="Taxonomy precomputed stats HDF5")
    p_map.add_argument("marker_genes", type=Path, help="Marker genes JSON")
    p_map.add_argument("output_json", type=Path, help="Output extended JSON")
    p_map.add_argument("--csv", type=Path, help="Also write CSV output")

    # preflight
    p_pre = sub.add_parser("preflight", help="Check if dataset fits in memory")
    p_pre.add_argument("file", type=Path, help="Dataset file or mtx directory")

    args = parser.parse_args(argv)

    handlers = {
        "convert": cmd_convert,
        "score": cmd_score,
        "map": cmd_map,
        "preflight": cmd_preflight,
    }
    handlers[args.command](args)


if __name__ == "__main__":
    main()
