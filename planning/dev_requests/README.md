# planning/dev_requests/ — historical archive

> **As of 2026-05-01, dev requests are filed as GitHub issues on
> [`Cellular-Semantics/evidencell`](https://github.com/Cellular-Semantics/evidencell/issues),
> not as markdown files in this directory.**
>
> See `CLAUDE_dev.md` § *Dev request workflow* for the filing pattern,
> required body sections, and how PRs close issues via `Closes #N`.

This directory retains the markdown reports filed up to 2026-04-30 as a
historical record. Do not delete them; commit messages and PRs may
reference them.

## When to file (current workflow)

File a GitHub issue when any of the following is true during curation:

- A workflow step calls a function or recipe that does not exist, or that
  exists but does not accept the needed arguments.
- A KB validation error reveals a real gap in the schema (not a data-level
  fix). Schema edits must never be attempted directly in a curation session.
- A planned ingest, mapping, or reporting step is impossible given current
  tooling and would require new code to proceed.
- An orchestrator's instructions conflict with the state of the code or repo.

Do **not** file an issue for data-level fixes, normal validation failures
that a content correction resolves, or ambiguity that human review can
answer in the current session.

## Filing pattern

```bash
GH_TOKEN="$CELLSEM_GH_TOKEN" gh issue create \
  --repo Cellular-Semantics/evidencell \
  --title "{short description}" \
  --body "$(cat <<'EOF'
## Goal
...

## Scope
...

## Proposed surface
...
EOF
)"
```

Required body sections: **Goal**, **Scope**, **Proposed surface**. Add
**Open questions** and **Out of scope** when relevant.

## Lifecycle

1. **Filed** — issue opened on `Cellular-Semantics/evidencell`.
2. **Triaged** — labelled / assigned in a later dev-mode session.
3. **Resolved** — PR with `Closes #N` lands on `main`; issue auto-closes.
   The closed issue thread is the historical record.
