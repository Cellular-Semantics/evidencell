"""Single source of truth for evidencell directory conventions.

All path logic that maps between graph YAML, references, research
artefacts, and reports lives here.
"""

from pathlib import Path
import gzip
from contextlib import contextmanager

import yaml


def repo_root() -> Path:
    """Walk up from this file to find the repo root (contains schema/)."""
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "schema").is_dir():
            return p
        p = p.parent
    raise RuntimeError("Cannot locate repo root (no schema/ directory found)")


def find_node_file(node_id: str) -> Path:
    """Return the YAML file that contains the CellTypeNode with this node_id.

    Workflows should always call this rather than constructing paths directly.
    Scans kb/graphs/ for a YAML containing the node_id.

    Raises FileNotFoundError if no YAML in the KB contains the node_id.
    """
    root = repo_root()
    kb_dir = root / "kb" / "graphs"
    if kb_dir.exists():
        for yaml_file in sorted(kb_dir.rglob("*.yaml")):
            try:
                with yaml_file.open() as fh:
                    data = yaml.safe_load(fh)
            except Exception:
                continue
            nodes = data.get("nodes", []) if isinstance(data, dict) else []
            for node in nodes:
                if isinstance(node, dict) and node.get("id") == node_id:
                    return yaml_file
    raise FileNotFoundError(
        f"Node '{node_id}' not found in any KB YAML under kb/graphs/. "
        "Check node_id spelling or run 'just qc' to validate the KB."
    )


def region_from_graph(graph_file: Path) -> str:
    """Extract region name from a KB graph path.

    kb/graphs/{region}/foo.yaml → region
    """
    parts = graph_file.resolve().parts
    for i, part in enumerate(parts):
        if part == "kb" and i + 2 < len(parts) and parts[i + 1] == "graphs":
            return parts[i + 2]
    raise ValueError(f"Cannot extract region from graph path: {graph_file}")


def refs_path_for_graph(graph_file: Path) -> Path:
    """Return the references.json path for a given graph YAML file."""
    region = region_from_graph(graph_file)
    return repo_root() / "references" / region / "references.json"


def refs_path_for_region(region: str) -> Path:
    """Return the references.json path for a named region."""
    return repo_root() / "references" / region / "references.json"


def reports_dir_for_region(region: str) -> Path:
    """Return the reports directory for a named region."""
    return repo_root() / "reports" / region


def research_dir_for_region(region: str) -> Path:
    """Return the research directory for a named region."""
    return repo_root() / "research" / region


def taxonomy_dir(taxonomy_id: str) -> Path:
    """Return the directory for a taxonomy reference store."""
    return repo_root() / "kb" / "taxonomy" / taxonomy_id


def taxonomy_db_path(taxonomy_id: str) -> Path:
    """Return the SQLite DB path for a taxonomy."""
    return taxonomy_dir(taxonomy_id) / f"{taxonomy_id}.db"


def taxonomy_yaml_path(taxonomy_id: str, level: str) -> Path:
    """Return the YAML file path for a given taxonomy level.

    Prefers `{level}.yaml.gz` when present (the large WMBv1 cluster.yaml
    is gzipped on disk to stay under GitHub's 100 MB file limit); falls
    back to the uncompressed `{level}.yaml`. Callers that read the file
    should use `open_taxonomy_yaml()` to get a transparently-decompressed
    text stream.
    """
    base = taxonomy_dir(taxonomy_id) / f"{level}.yaml"
    gz = base.with_suffix(".yaml.gz")
    if gz.exists():
        return gz
    return base


@contextmanager
def open_taxonomy_yaml(path: Path):
    """Open a taxonomy YAML file as a text stream, transparently
    gunzipping when the path ends in `.yaml.gz`. Use this for any
    read of a file returned by `taxonomy_yaml_path()` or discovered
    via a `*.yaml*` glob on `kb/taxonomy/{taxonomy_id}/`.
    """
    if str(path).endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            yield fh
    else:
        with path.open(encoding="utf-8") as fh:
            yield fh


def iter_taxonomy_level_files(taxonomy_dir_path: Path):
    """Yield the per-level taxonomy YAML files in a taxonomy directory,
    catching both `*.yaml` and `*.yaml.gz` variants. Skips
    `taxonomy_meta.yaml` and `field_mapping.yaml` (non-level config).
    """
    skip_names = {"taxonomy_meta.yaml", "taxonomy_meta.yaml.gz",
                  "field_mapping.yaml", "field_mapping.yaml.gz"}
    seen_stems: set[str] = set()
    # Prefer .gz when both forms exist (consistent with taxonomy_yaml_path).
    for ext in ("*.yaml.gz", "*.yaml"):
        for f in sorted(taxonomy_dir_path.glob(ext)):
            if f.name in skip_names:
                continue
            stem = f.name.removesuffix(".gz").removesuffix(".yaml")
            if stem in seen_stems:
                continue
            seen_stems.add(stem)
            yield f


def taxonomy_meta_path(taxonomy_id: str) -> Path:
    """Return the taxonomy_meta.yaml path for a taxonomy (written by ingest)."""
    return taxonomy_dir(taxonomy_id) / "taxonomy_meta.yaml"


def taxonomy_meta_input_path(taxonomy_id: str) -> Path:
    """Return the metadata input file path (provided by user before ingest)."""
    return repo_root() / "inputs" / "taxonomies" / f"{taxonomy_id}_meta.yaml"


def at_runs_dir() -> Path:
    """Return the annotation transfer runs directory."""
    return repo_root() / "kb" / "annotation_transfer_runs"


def at_run_index_path() -> Path:
    """Return the AT run registry index path."""
    return at_runs_dir() / "index.yaml"
