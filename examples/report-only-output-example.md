# Report-only Output Example

Use this as a quality bar for report-only responses.

## Mode
Report-only (no edits made)

## Files read
- `README.md`
- `AGENTS.md`
- `current-truth.md`
- `decisions.md`
- `pending.md`
- `next-actions.md`
- `sources.md`

## What is currently consistent
- The repository consistently positions report-only as the default mode before edits.
- Safe-update is defined as bounded, reviewable changes with explicit constraints.
- Update logs under `updates/` are treated as required continuity artifacts.

## What is unresolved
- Validation cadence and ownership are not yet decided.
- Future validator strictness around required heading structure is still open.
- Adapter refinements are waiting on external first-run evidence.

## What should be updated first if safe-update is approved
1. Rewrite any non-startable action phrasing in `next-actions.md` into executable tasks.
2. Append one dated update log capturing the safe-update outcome.
3. Add one matching evidence note in `sources.md` when an external dry run is completed.

## Files relied on
`README.md`, `AGENTS.md`, `current-truth.md`, `decisions.md`, `pending.md`, `next-actions.md`, `sources.md`
