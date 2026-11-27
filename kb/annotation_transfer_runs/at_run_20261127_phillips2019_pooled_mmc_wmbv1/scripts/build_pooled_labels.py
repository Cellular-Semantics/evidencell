"""Derive the pooled "all cortex-projecting" label scheme for Phillips 2019 cells.

Reads the published projection-system label JSON of
at_run_20261115_phillips2019_projection_mmc_wmbv1 (metadata column
`Projection`; 20 is_ODC cells already dropped) and writes {cell: label} with
every cell given one label. Every cell in GEO:GSE133912 was retrogradely
labelled from one of five cortical areas (visual, motor, prefrontal, auditory,
somatosensory) and sorted, so the pool is fixed by the experiment, not by any
WMBv1 mapping output. No WMBv1 output is read.

Usage:
    python -I build_pooled_labels.py LABELS_PROJECTION_JSON OUT_JSON
"""

import json
import sys

SYSTEMS = {"Visual", "Motor", "Prefrontal", "Auditory", "Somatosensory"}
POOLED_LABEL = "cortex-projecting TC (all 5 systems)"


def main(src: str, dst: str) -> None:
    with open(src) as fh:
        published = json.load(fh)
    unexpected = set(published.values()) - SYSTEMS
    if unexpected:
        raise SystemExit(f"unexpected Projection labels: {sorted(unexpected)}")
    derived = {cell: POOLED_LABEL for cell in published}
    with open(dst, "w") as fh:
        json.dump(derived, fh, indent=0)
        fh.write("\n")
    print(f"{POOLED_LABEL}: {len(derived)}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
