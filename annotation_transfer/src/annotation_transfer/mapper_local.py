"""Thin wrapper around the cell_type_mapper CLI for running MapMyCells.

The cell_type_mapper package (https://github.com/AllenInstitute/cell_type_mapper)
is an optional dependency. Install with:
    uv pip install "cell_type_mapper @ git+https://github.com/AllenInstitute/cell_type_mapper"

This module wraps the CLI rather than the Python API because the CLI
is the documented, stable interface.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


class MapperError(Exception):
    """Raised when MapMyCells mapping fails."""


def run_mapmycells(
    input_h5ad: Path,
    precomputed_stats: Path,
    marker_genes: Path,
    output_json: Path,
    *,
    output_csv: Path | None = None,
    log_path: Path | None = None,
) -> Path:
    """Run MapMyCells via the cell_type_mapper CLI.

    Parameters
    ----------
    input_h5ad
        MapMyCells-ready h5ad file (output of convert.prepare_for_mapmycells).
    precomputed_stats
        Path to the precomputed taxonomy stats HDF5 file (e.g., WMB Yao 2023).
    marker_genes
        Path to the marker genes JSON file for the target taxonomy.
    output_json
        Where to write the extended JSON result.
    output_csv
        Optional path for simplified CSV output.
    log_path
        Optional path for log messages.

    Returns
    -------
    Path to the output JSON file.

    Raises
    ------
    MapperError
        If the cell_type_mapper CLI is not installed or the mapping fails.
    """
    cmd = [
        sys.executable, "-m", "cell_type_mapper.cli.from_specified_markers",
        "--query_path", str(input_h5ad),
        "--precomputed_stats.path", str(precomputed_stats),
        "--query_markers.serialized_lookup", str(marker_genes),
        "--extended_result_path", str(output_json),
        "--type_assignment.normalization", "raw",
    ]

    if output_csv is not None:
        cmd.extend(["--csv_result_path", str(output_csv)])
    if log_path is not None:
        cmd.extend(["--log_path", str(log_path)])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        raise MapperError(
            "cell_type_mapper is not installed. Install with:\n"
            '  uv pip install "cell_type_mapper @ '
            'git+https://github.com/AllenInstitute/cell_type_mapper"'
        )

    if result.returncode != 0:
        raise MapperError(
            f"MapMyCells failed (exit {result.returncode}):\n"
            f"stdout: {result.stdout[-500:] if result.stdout else '(empty)'}\n"
            f"stderr: {result.stderr[-500:] if result.stderr else '(empty)'}"
        )

    return output_json


def extract_csv_from_json(json_path: Path, csv_path: Path) -> Path:
    """Extract a flat CSV from MapMyCells extended JSON output.

    Useful when MapMyCells was run without --csv_result_path.
    Produces the same columns as the native CSV output.
    """
    with open(json_path) as f:
        data = json.load(f)

    results = data.get("results", [])
    if not results:
        raise MapperError(f"No results found in {json_path}")

    import pandas as pd

    rows = []
    for cell in results:
        row = {"cell_id": cell["cell_id"]}
        for level in cell.get("assignments", []):
            name = level["level"]
            row[f"{name}_name"] = level.get("assignment", "")
            row[f"{name}_bootstrapping_probability"] = level.get(
                "bootstrapping_probability", 0.0
            )
            if "alias" in level:
                row[f"{name}_alias"] = level["alias"]
        rows.append(row)

    pd.DataFrame(rows).to_csv(csv_path, index=False)
    return csv_path
