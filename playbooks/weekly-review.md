# Weekly Review Playbook

## When to use
Use on a weekly cadence (or fixed interval) to detect drift across core operating files.

## What to read first
1. `current-truth.md`
2. `decisions.md`
3. `pending.md`
4. `next-actions.md`
5. recent `updates/*.md`

## Likely files to update
- `current-truth.md` (tighten wording if stale or ambiguous)
- `pending.md` (remove resolved items, clarify unresolved blockers)
- `next-actions.md` (replace stale tasks with startable ones)
- `sources.md` (link fresh evidence referenced in review)
- `updates/<date>-weekly-review.md`

## Drift symptoms to look for
- `next-actions.md` items without observable outputs
- claims in `current-truth.md` that are no longer source-backed
- decisions being implied in other files but missing from `decisions.md`
- unresolved blockers disappearing from `pending.md` without evidence or decision
- update logs missing after meaningful safe-update or handoff passes

## Good mini-example
"During weekly review, move one resolved blocker out of `pending.md`, add one new unresolved evidence gap, and append `updates/2026-04-07-weekly-review.md` documenting both moves."

## Bad mini-example
"Reformat all files for tone consistency" (creates churn, hides operational signal, and does not reduce drift).
