# Handoff Playbook

## When to use
Use when transferring execution to another model or maintainer and restart speed matters.

## What to read first
1. `current-truth.md`
2. `decisions.md`
3. `pending.md`
4. `next-actions.md`
5. latest relevant `updates/*.md`

## Likely files to update
- `next-actions.md` (remove ambiguity before handoff)
- `pending.md` (ensure unresolved blockers are explicit)
- `updates/<date>-handoff.md`

## Handoff procedure
1. Confirm unresolved items are still visible in `pending.md`.
2. Ensure `next-actions.md` tasks are startable without reinterpretation.
3. Append a handoff update log with stable state, unresolved state, and first next action.
4. Provide exact restart instruction that enforces read order and report-only first.

## Good mini-example
"Append `updates/2026-04-07-handoff.md` listing stable constraints, unresolved validator-owner decision, and first next action: run report-only and propose one bounded safe-update option."

## Bad mini-example
"Tell the next model to continue from chat history" (loses auditable continuity and breaks restart reliability).

## Minimum handoff quality bar
A handoff is acceptable only if:
- unresolved items remain explicit and unpromoted
- latest update file states touched files and why edits were safe
- restart instruction is copy/paste ready
- next action is concrete and file-targeted
