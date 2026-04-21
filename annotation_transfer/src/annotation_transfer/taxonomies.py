"""Registry of MapMyCells taxonomies and their configurations.

Each taxonomy has both web API identifiers (for the BKP GraphQL endpoint)
and optional local file paths (for cell_type_mapper CLI execution).
Taxonomy specs are persisted as YAML so backend preferences survive
across sessions.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

import yaml

# Default directory for persisted taxonomy specs
DEFAULT_TAXONOMY_DIR = Path("annotation_transfer/taxonomies")

# S3 base URL for Allen Brain Cell Atlas taxonomy files
_S3_BASE = "https://allen-brain-cell-atlas.s3.us-west-2.amazonaws.com"


@dataclass
class TaxonomySpec:
    """Configuration for a MapMyCells reference taxonomy."""

    id: str
    name: str
    species: str
    # Web API identifiers (from getWorkflowNames GraphQL query)
    web_available: bool = True
    web_ref_id: str | None = None  # e.g. "10xGene"
    web_display_name: str | None = None
    algorithms: list[str] = field(default_factory=list)
    # Local file paths (None until downloaded)
    local_stats_path: str | None = None
    local_markers_path: str | None = None
    # S3 URLs for downloading taxonomy files
    stats_s3_url: str | None = None
    markers_s3_url: str | None = None
    # CLI command variant for local execution
    local_cli_variant: str = "from_specified_markers"
    # User's preferred backend
    preferred_backend: str = "auto"  # "local" | "web" | "auto"


# Built-in taxonomy definitions with known S3 URLs and web IDs.
_BUILTIN_TAXONOMIES: dict[str, TaxonomySpec] = {
    "CCN20230722": TaxonomySpec(
        id="CCN20230722",
        name="Whole Mouse Brain (Yao 2023)",
        species="mouse",
        web_ref_id="10xGene",
        web_display_name="10x Whole Mouse Brain (CCN20230722)",
        algorithms=["HierarchicalAlgorithmRun", "CorrelationAlgorithmRun"],
        stats_s3_url=f"{_S3_BASE}/mapmycells/WMB-10X/20240831/precomputed_stats_ABC_revision_230821.h5",
        markers_s3_url=f"{_S3_BASE}/mapmycells/WMB-10X/20240831/mouse_markers_230821.json",
        local_cli_variant="from_specified_markers",
    ),
    "CCN202210140": TaxonomySpec(
        id="CCN202210140",
        name="Whole Human Brain (Siletti)",
        species="human",
        web_ref_id="10x_whole_human_brain",
        web_display_name="10x Whole Human Brain (CCN202210140)",
        algorithms=["CorrelationAlgorithmRun", "HierarchicalAlgorithmRun_Siletti"],
        stats_s3_url=f"{_S3_BASE}/mapmycells/WHB-10Xv3/20240831/precomputed_stats.siletti.training.h5",
        markers_s3_url=f"{_S3_BASE}/mapmycells/WHB-10Xv3/20240831/query_markers.n10.20240221800.json",
        local_cli_variant="from_specified_markers",
    ),
    "CCN20230505": TaxonomySpec(
        id="CCN20230505",
        name="Human MTG SEA-AD",
        species="human",
        web_ref_id="10x-Human-MTG-SEA-AD",
        web_display_name="10x Human MTG SEA-AD (CCN20230505)",
        algorithms=[
            "SEA-AD_CorrelationAlgorithmRun",
            "SEA-AD_HierarchicalAlgorithmRun",
            "DeepGenerativeMapping",
        ],
        stats_s3_url=f"{_S3_BASE}/mapmycells/SEAAD/20240831/precomputed_stats.20231120.sea_ad.MTG.h5",
        markers_s3_url=None,  # uses on-the-fly markers
        local_cli_variant="map_to_on_the_fly_markers",
    ),
    "CCN20250428": TaxonomySpec(
        id="CCN20250428",
        name="Consensus Basal Ganglia",
        species="mouse",
        web_ref_id="HMBA-BG-taxonomy-CCN20250428",
        web_display_name="Consensus Basal Ganglia Taxonomy (CCN20250428)",
        algorithms=["HierarchicalAlgorithmRun", "CorrelationAlgorithmRun"],
        stats_s3_url=None,
        markers_s3_url=None,
    ),
}


class TaxonomyError(Exception):
    """Raised for taxonomy registry errors."""


def _spec_path(taxonomy_id: str, taxonomy_dir: Path) -> Path:
    return taxonomy_dir / f"{taxonomy_id}.yaml"


def list_taxonomies(
    *, taxonomy_dir: Path = DEFAULT_TAXONOMY_DIR,
) -> list[TaxonomySpec]:
    """Return all known taxonomies (built-in + any persisted overrides)."""
    specs: dict[str, TaxonomySpec] = dict(_BUILTIN_TAXONOMIES)
    if taxonomy_dir.exists():
        for p in taxonomy_dir.glob("*.yaml"):
            spec = _load_spec_file(p)
            specs[spec.id] = spec
    return list(specs.values())


def get_taxonomy(
    taxonomy_id: str,
    *,
    taxonomy_dir: Path = DEFAULT_TAXONOMY_DIR,
) -> TaxonomySpec:
    """Look up a taxonomy by ID. Persisted spec takes precedence over built-in."""
    spec_file = _spec_path(taxonomy_id, taxonomy_dir)
    if spec_file.exists():
        return _load_spec_file(spec_file)
    if taxonomy_id in _BUILTIN_TAXONOMIES:
        return _BUILTIN_TAXONOMIES[taxonomy_id]
    raise TaxonomyError(
        f"Unknown taxonomy '{taxonomy_id}'. "
        f"Known: {', '.join(sorted(_BUILTIN_TAXONOMIES))}"
    )


def save_taxonomy(
    spec: TaxonomySpec,
    *,
    taxonomy_dir: Path = DEFAULT_TAXONOMY_DIR,
) -> Path:
    """Persist a taxonomy spec to YAML."""
    taxonomy_dir.mkdir(parents=True, exist_ok=True)
    path = _spec_path(spec.id, taxonomy_dir)
    data = asdict(spec)
    with open(path, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)
    return path


# Standard relative paths (from repo root) for downloaded taxonomy files.
# Mirroring the conf/mba/ pattern: large, gitignored, re-fetchable.
_MMC_BASE = Path("conf/mapmycells")


def mapmycells_dir(taxonomy_id: str) -> Path:
    """Return the standard directory for a taxonomy's MapMyCells files."""
    return _MMC_BASE / taxonomy_id


def download_taxonomy_files(
    spec: TaxonomySpec,
    dest_dir: Path | None = None,
) -> tuple[Path, Path | None]:
    """Download MapMyCells stats and (optionally) marker files for a taxonomy.

    Files are placed in dest_dir (default: conf/mapmycells/{taxonomy_id}/) with
    generic names: precomputed_stats.h5 and marker_genes.json.

    Returns (stats_path, markers_path).  markers_path is None if the taxonomy
    has no markers_s3_url (e.g. SEA-AD uses on-the-fly markers).
    """
    import urllib.request

    if dest_dir is None:
        dest_dir = mapmycells_dir(spec.id)
    dest_dir.mkdir(parents=True, exist_ok=True)

    stats_path: Path | None = None
    if spec.stats_s3_url:
        stats_path = dest_dir / "precomputed_stats.h5"
        if stats_path.exists():
            print(f"  Stats already present: {stats_path} — skipping.")
        else:
            print(f"  Downloading stats → {stats_path}")
            print(f"    URL: {spec.stats_s3_url}")
            urllib.request.urlretrieve(spec.stats_s3_url, stats_path)
            print(f"    Done ({stats_path.stat().st_size // (1024**2):,} MB)")
    else:
        print(f"  No stats_s3_url for {spec.id} — skipping stats download.")

    markers_path: Path | None = None
    if spec.markers_s3_url:
        markers_path = dest_dir / "marker_genes.json"
        if markers_path.exists():
            print(f"  Markers already present: {markers_path} — skipping.")
        else:
            print(f"  Downloading markers → {markers_path}")
            print(f"    URL: {spec.markers_s3_url}")
            urllib.request.urlretrieve(spec.markers_s3_url, markers_path)
            print(f"    Done ({markers_path.stat().st_size // 1024:,} KB)")

    return stats_path, markers_path  # type: ignore[return-value]


def _load_spec_file(path: Path) -> TaxonomySpec:
    with open(path) as f:
        data: dict[str, Any] = yaml.safe_load(f)
    return TaxonomySpec(**data)


def resource_check_for_download(
    taxonomy: TaxonomySpec,
) -> dict[str, Any]:
    """Check whether local resources are sufficient to download + run locally.

    Returns a dict with: can_download, available_disk_gb, est_download_gb,
    available_ram_gb, est_ram_gb, recommendation.
    """
    import psutil

    available_ram_gb = psutil.virtual_memory().available / (1024**3)
    # Taxonomy files are typically 2-5 GB total
    est_download_gb = 5.0

    disk_usage = shutil.disk_usage(Path.home())
    available_disk_gb = disk_usage.free / (1024**3)

    # Conservative: need ~16 GB RAM for local mapping, ~10 GB disk
    can_run_local = available_ram_gb >= 16.0
    can_download = available_disk_gb >= 10.0

    if can_run_local and can_download:
        recommendation = "local"
    elif can_download:
        recommendation = "auto"  # can download but RAM may be tight
    else:
        recommendation = "web"

    return {
        "can_download": can_download,
        "can_run_local": can_run_local,
        "available_disk_gb": round(available_disk_gb, 1),
        "est_download_gb": est_download_gb,
        "available_ram_gb": round(available_ram_gb, 1),
        "recommendation": recommendation,
    }
