"""Strategy dispatcher for MapMyCells mapping.

Routes mapping requests to either the web API (GraphQL) or the local
cell_type_mapper CLI based on the taxonomy's preferred_backend setting.
The user can always override with an explicit backend choice.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

from annotation_transfer.taxonomies import TaxonomySpec, get_taxonomy


class MappingBackend(str, Enum):
    WEB = "web"
    LOCAL = "local"
    AUTO = "auto"


class MapperError(Exception):
    """Raised when MapMyCells mapping fails."""


@dataclass
class MappingResult:
    """Result of a MapMyCells mapping run."""

    backend_used: MappingBackend
    output_csv: Path
    output_json: Path | None
    n_cells_mapped: int
    subsampled_from: int | None  # original n_cells if subsampled, else None
    taxonomy: str
    algorithm: str


def resolve_backend(
    taxonomy: TaxonomySpec,
    input_h5ad: Path,
    requested: MappingBackend | None = None,
) -> MappingBackend:
    """Determine which backend to use for this mapping run.

    Priority: explicit request > taxonomy preference > auto logic.
    """
    if requested is not None and requested != MappingBackend.AUTO:
        return requested

    preferred = taxonomy.preferred_backend

    if preferred == "local":
        if taxonomy.local_stats_path and taxonomy.local_markers_path:
            return MappingBackend.LOCAL
        warnings.warn(
            f"Taxonomy {taxonomy.id} prefers local but files not downloaded. "
            f"Falling back to web.",
            stacklevel=2,
        )
        return MappingBackend.WEB

    if preferred == "web":
        if taxonomy.web_ref_id:
            return MappingBackend.WEB
        warnings.warn(
            f"Taxonomy {taxonomy.id} prefers web but has no web_ref_id. "
            f"Falling back to local.",
            stacklevel=2,
        )
        return MappingBackend.LOCAL

    # AUTO: prefer web if available, fall back to local
    if taxonomy.web_ref_id:
        return MappingBackend.WEB
    if taxonomy.local_stats_path and taxonomy.local_markers_path:
        return MappingBackend.LOCAL

    raise MapperError(
        f"Taxonomy {taxonomy.id}: neither web API nor local files available. "
        f"Run 'annotation-transfer taxonomy-setup {taxonomy.id}' first."
    )


def _count_cells(h5ad_path: Path) -> int:
    """Read cell count from h5ad metadata without loading X."""
    import h5py

    with h5py.File(h5ad_path, "r") as f:
        if "X" in f:
            x = f["X"]
            if "shape" in x.attrs:
                return int(x.attrs["shape"][0])
            if isinstance(x, h5py.Dataset):
                return int(x.shape[0])
        if "obs" in f:
            obs = f["obs"]
            if "_index" in obs:
                return int(obs["_index"].shape[0])
    return 0


def run_mapping(
    input_h5ad: Path,
    taxonomy_id: str,
    output_dir: Path,
    *,
    backend: MappingBackend | None = None,
    algorithm: str | None = None,
    max_cells_web: int = 150_000,
    subsample_col: str | None = None,
    # Local-only overrides
    precomputed_stats: Path | None = None,
    marker_genes: Path | None = None,
    taxonomy_dir: Path | None = None,
    on_status: Any | None = None,
) -> MappingResult:
    """Run MapMyCells mapping via the resolved backend.

    Parameters
    ----------
    input_h5ad
        MapMyCells-ready h5ad file.
    taxonomy_id
        Taxonomy ID (e.g. "CCN20230722").
    output_dir
        Directory for output files.
    backend
        Explicit backend choice. None = use taxonomy preference.
    algorithm
        Workflow name. None = use first algorithm in taxonomy spec.
    max_cells_web
        Max cells before subsampling for web API.
    subsample_col
        Column for stratified subsampling (web path only).
    precomputed_stats
        Override local precomputed stats path.
    marker_genes
        Override local marker genes path.
    taxonomy_dir
        Override taxonomy spec directory.
    on_status
        Optional callback for web API status updates.
    """
    kwargs = {}
    if taxonomy_dir is not None:
        kwargs["taxonomy_dir"] = taxonomy_dir
    taxonomy = get_taxonomy(taxonomy_id, **kwargs)

    if algorithm is None:
        if taxonomy.algorithms:
            algorithm = taxonomy.algorithms[0]
        else:
            algorithm = "HierarchicalAlgorithmRun"

    resolved = resolve_backend(taxonomy, input_h5ad, backend)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if resolved == MappingBackend.WEB:
        return _run_web(
            input_h5ad, taxonomy, algorithm, output_dir,
            max_cells_web=max_cells_web,
            subsample_col=subsample_col,
            on_status=on_status,
        )
    else:
        return _run_local(
            input_h5ad, taxonomy, algorithm, output_dir,
            precomputed_stats=precomputed_stats,
            marker_genes=marker_genes,
        )


def _run_web(
    input_h5ad: Path,
    taxonomy: TaxonomySpec,
    algorithm: str,
    output_dir: Path,
    *,
    max_cells_web: int,
    subsample_col: str | None,
    on_status: Any | None,
) -> MappingResult:
    from annotation_transfer.mapper_web import run_mapmycells_web

    n_cells_original = _count_cells(input_h5ad)
    actual_input = input_h5ad
    subsampled_from = None

    # Subsample if needed
    if n_cells_original > max_cells_web:
        from annotation_transfer.subsample import subsample_file

        subsampled_path = output_dir / f"subsampled_{input_h5ad.name}"
        n_kept = subsample_file(
            input_h5ad, subsampled_path,
            max_cells=max_cells_web,
            stratify_col=subsample_col,
        )
        actual_input = subsampled_path
        subsampled_from = n_cells_original
        n_cells_original = n_kept

    csv_path = run_mapmycells_web(
        actual_input, taxonomy, algorithm, output_dir,
        on_status=on_status,
    )

    return MappingResult(
        backend_used=MappingBackend.WEB,
        output_csv=csv_path,
        output_json=None,
        n_cells_mapped=n_cells_original,
        subsampled_from=subsampled_from,
        taxonomy=taxonomy.id,
        algorithm=algorithm,
    )


def _run_local(
    input_h5ad: Path,
    taxonomy: TaxonomySpec,
    algorithm: str,
    output_dir: Path,
    *,
    precomputed_stats: Path | None,
    marker_genes: Path | None,
) -> MappingResult:
    from annotation_transfer.mapper_local import run_mapmycells, extract_csv_from_json

    stats = Path(precomputed_stats) if precomputed_stats else None
    markers = Path(marker_genes) if marker_genes else None

    if stats is None and taxonomy.local_stats_path:
        stats = Path(taxonomy.local_stats_path)
    if markers is None and taxonomy.local_markers_path:
        markers = Path(taxonomy.local_markers_path)

    if stats is None or markers is None:
        raise MapperError(
            f"Local mapping requires precomputed_stats and marker_genes. "
            f"Download them with 'annotation-transfer taxonomy-setup {taxonomy.id} --download' "
            f"or provide --stats and --markers."
        )

    output_json = output_dir / "mapping_result.json"
    output_csv = output_dir / "mapping_result.csv"

    run_mapmycells(
        input_h5ad, stats, markers, output_json,
        output_csv=output_csv,
    )

    n_cells = _count_cells(input_h5ad)

    return MappingResult(
        backend_used=MappingBackend.LOCAL,
        output_csv=output_csv,
        output_json=output_json,
        n_cells_mapped=n_cells,
        subsampled_from=None,
        taxonomy=taxonomy.id,
        algorithm=algorithm,
    )
