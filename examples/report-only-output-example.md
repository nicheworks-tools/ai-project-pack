# Report-only Output Example

Use this as the quality bar for a report-only response.

## Mode
Report-only (no edits performed)

## Files read
- `README.md`
- `AGENTS.md`
- `current-truth.md`
- `decisions.md`
- `pending.md`
- `next-actions.md`
- `sources.md`
- latest relevant `updates/*.md`

## Example output

```txt
What is currently consistent:
- Repository posture is public-facing and not marked as internal/incomplete.
- Operating model remains stable: report-only first, bounded safe-update second.
- Append-only update logging is required for meaningful safe-update and handoff passes.
- Core file roles are distinct (truth, decisions, unresolved, next actions, sources).

What is unresolved:
- No documented owner/cadence yet for routine validator execution.
- No decision yet on whether validation should enforce heading-structure minimums.
- Adapter wording improvements still depend on external first-run evidence.

What should be updated first if safe-update is approved:
1) Tighten next-actions.md so each item has an observable output artifact.
2) Append one dated update log documenting exactly what changed and what remained unresolved.
3) Add or update one sources.md entry that records evidence quality for any promoted claim.

Which files were relied on:
README.md; AGENTS.md; current-truth.md; decisions.md; pending.md; next-actions.md; sources.md; updates/000-initial.md
```

## Why this output is operationally credible
- It distinguishes stable operating facts from unresolved decisions.
- It proposes bounded edits before touching files.
- It cites exactly which repository artifacts informed the report.
