# Handoff Example

This example demonstrates a high-quality model-to-model restart package.

## Handoff package checklist

Before handoff, verify all of the following:
- `current-truth.md` reflects only currently supported and in-scope truths.
- `decisions.md` has append-only entries for consequential choices made this pass.
- `pending.md` clearly lists unresolved items that materially affect next passes.
- `next-actions.md` contains startable actions with observable outputs.
- `sources.md` separates primary, secondary, and internal notes clearly.
- latest `updates/*.md` includes summary, touched files, safe rationale, unresolved, and next action.

## Exact restart instruction for the next model

```txt
You are continuing aiprojectpack from repository state, not chat memory.
Read in order: README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, sources.md, then updates/2026-04-07-operational-strength-pass.md.
Start in report-only mode and return exactly:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on
Do not reopen settled decisions unless new evidence is provided.
```

## What success looks like
- restart report matches existing truth/decision boundaries without reinterpretation
- unresolved items remain unresolved and visible
- first proposed safe-update is bounded and names touched files before edits
- no session time is spent rediscovering basic operating context

## What must not be rediscovered
- default mode is report-only
- safe-update must be bounded and reviewable
- updates are append-only continuity artifacts
- unresolved claims require evidence before promotion

## How unresolved items remain visible
- unresolved items remain in `pending.md` until evidence or a decision resolves them
- update logs explicitly repeat unresolved items that still block progress
- report-only outputs always include unresolved state before suggesting edits
