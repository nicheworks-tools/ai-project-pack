# First Run

This page defines what success and failure look like in your first loop.

## First-loop success path
1. Read `README.md` and `AGENTS.md`.
2. Run one report-only pass (no edits).
3. Approve one bounded safe-update.
4. Append one dated update log under `updates/`.
5. Confirm unresolved items remain visible.

## What success looks like
- You can point to exactly what is consistent right now.
- You can point to exactly what is unresolved right now.
- You made small, reviewable edits only.
- Another model can restart using the repo without chat reconstruction.

## What failure looks like
- First pass edits files without explicit safe-update approval.
- Unresolved items disappear instead of being tracked.
- `next-actions.md` contains non-startable advice.
- No update log captures what changed.

## Quick recovery if first loop failed
- Re-run report-only and compare with current files.
- Reintroduce unresolved items in `pending.md` if they were dropped.
- Append a corrective update entry documenting the recovery.
