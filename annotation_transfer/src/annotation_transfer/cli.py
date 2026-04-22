"""CLI entry points for the annotation transfer pipeline.

Usage:
    annotation-transfer convert INPUT OUTPUT [--cluster-col COL --cluster-value VAL --label-col COL]
    annotation-transfer map INPUT TAXONOMY OUTPUT_DIR [--backend web|local|auto --algorithm ALG]
    annotation-transfer map-local INPUT STATS MARKERS OUTPUT_JSON [--csv PATH]
    annotation-transfer score MMC_CSV LABELS_JSON OUTPUT [--threshold 0.8]
    annotation-transfer subsample INPUT OUTPUT [--max-cells N --stratify-col COL]
    annotation-transfer taxonomy-setup TAXONOMY_ID [--web/--no-web --download/--no-download]
    annotation-transfer taxonomy-list
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


def cmd_map(args: argparse.Namespace) -> None:
    """New taxonomy-aware mapping command."""
    from annotation_transfer.mapper import run_mapping, MappingBackend

    backend = None
    if args.backend:
        backend = MappingBackend(args.backend)

    def on_status(status: dict) -> None:
        ws = status.get("workflowStatus", "")
        als = status.get("algorithmStatus", "")
        eta = status.get("ETA", "")
        print(f"  Status: workflow={ws} algorithm={als} ETA={eta}")

    result = run_mapping(
        args.input,
        args.taxonomy,
        args.output_dir,
        backend=backend,
        algorithm=args.algorithm,
        max_cells_web=args.max_cells,
        subsample_col=args.subsample_col,
        on_status=on_status,
    )

    print(f"Backend: {result.backend_used.value}")
    print(f"Output CSV: {result.output_csv}")
    if result.output_json:
        print(f"Output JSON: {result.output_json}")
    print(f"Cells mapped: {result.n_cells_mapped}")
    if result.subsampled_from:
        print(f"Subsampled from: {result.subsampled_from}")


def cmd_map_local(args: argparse.Namespace) -> None:
    """Backward-compatible local mapping (old interface)."""
    from annotation_transfer.mapper_local import run_mapmycells

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


def cmd_subsample(args: argparse.Namespace) -> None:
    from annotation_transfer.subsample import subsample_file

    n_kept = subsample_file(
        args.input,
        args.output,
        max_cells=args.max_cells,
        stratify_col=args.stratify_col,
        seed=args.seed,
    )
    print(f"Subsampled: {args.input} → {args.output} ({n_kept} cells)")


def cmd_taxonomy_setup(args: argparse.Namespace) -> None:
    from annotation_transfer.taxonomies import (
        get_taxonomy, save_taxonomy, resource_check_for_download, TaxonomyError,
    )

    try:
        spec = get_taxonomy(args.taxonomy_id)
    except TaxonomyError:
        print(f"Unknown taxonomy: {args.taxonomy_id}")
        sys.exit(1)

    print(f"Taxonomy: {spec.name} ({spec.id})")
    print(f"Species:  {spec.species}")
    print(f"Web ID:   {spec.web_ref_id or '(none)'}")

    # Set web availability
    if args.web is not None:
        spec.web_available = args.web

    # Resource check + download
    if args.download:
        from annotation_transfer.taxonomies import download_taxonomy_files, resource_check_for_download
        report = resource_check_for_download(spec)
        print(f"\nResource check:")
        print(f"  Available RAM:  {report['available_ram_gb']} GB")
        print(f"  Available disk: {report['available_disk_gb']} GB")
        print(f"  Recommendation: {report['recommendation']}")

        if not report["can_download"]:
            print("Insufficient disk space for download.")
            spec.preferred_backend = "web"
        else:
            stats_path, markers_path = download_taxonomy_files(spec)
            if stats_path:
                spec.local_stats_path = str(stats_path)
            if markers_path:
                spec.local_markers_path = str(markers_path)
            spec.preferred_backend = report["recommendation"]
    elif args.web is False:
        spec.preferred_backend = "local"
    elif spec.web_ref_id:
        spec.preferred_backend = "auto"

    path = save_taxonomy(spec)
    print(f"\nSaved: {path}")
    print(f"Preferred backend: {spec.preferred_backend}")


def cmd_taxonomy_list(args: argparse.Namespace) -> None:
    from annotation_transfer.taxonomies import list_taxonomies

    specs = list_taxonomies()
    for s in specs:
        web = f"web={s.web_ref_id}" if s.web_ref_id else "web=N/A"
        local = "local=yes" if s.local_stats_path else "local=no"
        print(f"  {s.id:20s}  {s.name:40s}  {web:30s}  {local}  pref={s.preferred_backend}")


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

    # map (new: taxonomy-aware)
    p_map = sub.add_parser("map", help="Run MapMyCells (web API or local)")
    p_map.add_argument("input", type=Path, help="MapMyCells-ready h5ad or CSV")
    p_map.add_argument("taxonomy", help="Taxonomy ID (e.g. CCN20230722)")
    p_map.add_argument("output_dir", type=Path, help="Output directory")
    p_map.add_argument("--backend", choices=["web", "local", "auto"], help="Force backend")
    p_map.add_argument("--algorithm", help="Mapping algorithm workflow name")
    p_map.add_argument("--max-cells", type=int, default=150_000, help="Max cells for web API")
    p_map.add_argument("--subsample-col", help="Column for stratified subsampling")

    # map-local (backward-compatible)
    p_mapl = sub.add_parser("map-local", help="Run MapMyCells locally (requires cell_type_mapper)")
    p_mapl.add_argument("input", type=Path, help="MapMyCells-ready h5ad")
    p_mapl.add_argument("precomputed_stats", type=Path, help="Taxonomy precomputed stats HDF5")
    p_mapl.add_argument("marker_genes", type=Path, help="Marker genes JSON")
    p_mapl.add_argument("output_json", type=Path, help="Output extended JSON")
    p_mapl.add_argument("--csv", type=Path, help="Also write CSV output")

    # score
    p_score = sub.add_parser("score", help="Compute F1 matrix from MapMyCells output")
    p_score.add_argument("mmc_csv", type=Path, help="MapMyCells output CSV")
    p_score.add_argument("labels", type=Path, help="Source labels JSON")
    p_score.add_argument("output", type=Path, help="Output F1 matrix CSV")
    p_score.add_argument("--threshold", type=float, default=0.8, help="Bootstrap threshold")

    # subsample
    p_sub = sub.add_parser("subsample", help="Subsample h5ad for web API limits")
    p_sub.add_argument("input", type=Path, help="Input h5ad file")
    p_sub.add_argument("output", type=Path, help="Output subsampled h5ad")
    p_sub.add_argument("--max-cells", type=int, default=150_000, help="Maximum cells")
    p_sub.add_argument("--stratify-col", help="Column for stratified sampling")
    p_sub.add_argument("--seed", type=int, default=42, help="Random seed")

    # taxonomy-setup
    p_tax = sub.add_parser("taxonomy-setup", help="Configure a taxonomy for mapping")
    p_tax.add_argument("taxonomy_id", help="Taxonomy ID (e.g. CCN20230722)")
    p_tax.add_argument("--web", action="store_true", default=None, dest="web",
                        help="This taxonomy is available on MapMyCells web")
    p_tax.add_argument("--no-web", action="store_false", dest="web",
                        help="This taxonomy is NOT on MapMyCells web")
    p_tax.add_argument("--download", action="store_true", default=False,
                        help="Download taxonomy files for local execution")
    p_tax.add_argument("--no-download", action="store_false", dest="download")

    # taxonomy-list
    sub.add_parser("taxonomy-list", help="List known taxonomies")

    # preflight
    p_pre = sub.add_parser("preflight", help="Check if dataset fits in memory")
    p_pre.add_argument("file", type=Path, help="Dataset file or mtx directory")

    args = parser.parse_args(argv)

    handlers = {
        "convert": cmd_convert,
        "map": cmd_map,
        "map-local": cmd_map_local,
        "score": cmd_score,
        "subsample": cmd_subsample,
        "taxonomy-setup": cmd_taxonomy_setup,
        "taxonomy-list": cmd_taxonomy_list,
        "preflight": cmd_preflight,
    }
    handlers[args.command](args)


if __name__ == "__main__":
    main()
