"""Single source of truth for evidencell directory conventions.

All path logic that maps between graph YAML, references, research
artefacts, and reports lives here.
"""

from pathlib import Path
import gzip
from contextlib import contextmanager



def repo_root() -> Path:
    """Walk up from this file to find the repo root (contains schema/)."""
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "schema").is_dir():
            return p
        p = p.parent
    raise RuntimeError("Cannot locate repo root (no schema/ directory found)")


ATLAS_BASIS = "ATLAS_TRANSCRIPTOMIC"


class AmbiguousNodeError(RuntimeError):
    """A node_id is canonically defined in more than one KB graph file."""


def find_node_file(node_id: str) -> Path:
    """Return the YAML file that canonically defines this node_id.

    Workflows should always call this rather than constructing paths directly.

    A node_id defined canonically in exactly one file resolves to that file,
    even if atlas stubs for the same id exist elsewhere. An id that appears
    only as a stub resolves to the first such file.

    Raises FileNotFoundError if no YAML under kb/graphs/ defines the id,
    AmbiguousNodeError if more than one file canonically defines it, and
    kb_index.KbIndexError if any file under kb/graphs/ cannot be parsed.
    """
    # Imported here: kb_index imports this module for repo_root and ATLAS_BASIS.
    from evidencell.kb_index import get_index

    matches = [(r.source_file, r.is_stub) for r in get_index().nodes.get(node_id, [])]
    if not matches:
        raise FileNotFoundError(
            f"Node '{node_id}' not found in any KB YAML under kb/graphs/. "
            "Check node_id spelling or run 'just qc' to validate the KB."
        )
    root = repo_root()
    # dict.fromkeys dedupes while keeping order: a node id repeated *within*
    # one file is an intra-file duplicate, which validate.structural_checks
    # owns. Without this it would be reported here as "defined in 2 files:
    # a.yaml, a.yaml".
    canonical = list(dict.fromkeys(path for path, is_stub in matches if not is_stub))
    if len(canonical) > 1:
        listed = ", ".join(str(p.relative_to(root)) for p in canonical)
        raise AmbiguousNodeError(
            f"Node '{node_id}' is canonically defined in {len(canonical)} files: "
            f"{listed}. Exactly one file must define it; resolve the duplicate "
            "before continuing."
        )
    return canonical[0] if canonical else matches[0][0]


def region_from_graph(graph_file: Path) -> str:
    """Extract region name from a KB graph path.

    kb/graphs/{region}/foo.yaml → region
    """
    parts = graph_file.resolve().parts
    for i, part in enumerate(parts):
        if part == "kb" and i + 2 < len(parts) and parts[i + 1] == "graphs":
            return parts[i + 2]
    raise ValueError(f"Cannot extract region from graph path: {graph_file}")


def refs_dir_for_graph(graph_file: Path) -> Path:
    """Return the reference-store directory for a given graph YAML file.

    The store is a directory (papers/ + quotes/ + sources/), not a file. Use
    `references.load_papers()` / `load_quotes()` to read it, and
    `references.store_exists()` — never `Path.exists()` — to test for it.
    """
    return refs_dir_for_region(region_from_graph(graph_file))


def refs_dir_for_region(region: str) -> Path:
    """Return the reference-store directory for a named region."""
    return repo_root() / "references" / region


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
