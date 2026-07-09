# Blinding state — cerebellum_blind run

**STATUS: blinding NOT currently active — ground-truth graphs are restored.**

The blind pipeline has not started its answer-sensitive steps yet (we paused before
Step 1b to reconnect MCP servers). To keep the working tree clean and safe across a
Claude Code restart, the two curator ground-truth graphs have been **restored** to
`kb/graphs/cerebellum/` (working tree == git HEAD, `git status` clean).

The scoring answer key is fully captured in `answer_key.json` (does not depend on the
graph files staying moved), so re-quarantining is a cheap, repeatable first step of the
run — see RESUME.md § "Re-quarantine".

## What must be blinded during the run

Before any answer-sensitive step (Step 1b onward of the discovery arm, and the whole
mapping arm), move these two files out of the writable KB so no pipeline step can read
the answer:

- `kb/graphs/cerebellum/CB_MLI_types.yaml`
- `kb/graphs/cerebellum/CB_PLI_types.yaml`

These are the ONLY pre-existing mention of the WMB target clusters or the
Kozareva/Osorno PMIDs in the writable test surface (verified 2026-07-09). No
`references/cerebellum*/` store exists; the June refresh `research/cerebellum/` dirs
contain no answer.

## Re-quarantine procedure (first step on resume)

```bash
QUAR="$SCRATCHPAD/cerebellum_quarantine"   # $SCRATCHPAD = the NEW session's scratchpad
mkdir -p "$QUAR"
mv kb/graphs/cerebellum/CB_MLI_types.yaml "$QUAR/"
mv kb/graphs/cerebellum/CB_PLI_types.yaml "$QUAR/"
git status --short kb/graphs/cerebellum/   # will show 2x ' D' — EXPECTED during run, do NOT commit
```

## Restore procedure (before ANY commit, and at end of experiment)

```bash
git checkout -- kb/graphs/cerebellum/CB_MLI_types.yaml kb/graphs/cerebellum/CB_PLI_types.yaml
git status --short kb/graphs/cerebellum/   # must be clean
```

(Using `git checkout` restores from HEAD, so it works even if the scratchpad quarantine
copy was lost to a restart. The originals are safe in git.)

## Never commit

- The quarantine deletion of the two ground-truth graphs.
- Any `kb/graphs/cerebellum_blind/**` or `references/cerebellum_blind/**` produced by the
  blind run (throwaway).
- Only `research/validation/methods_audits/cerebellum_blind/**` gets committed.
