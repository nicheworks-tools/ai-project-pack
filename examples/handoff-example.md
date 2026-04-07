# Handoff Example

Goal: another model resumes quickly and correctly with minimal re-briefing.

## Handoff package checklist
- `current-truth.md` is current and scoped.
- `pending.md` contains unresolved items only.
- `next-actions.md` contains startable tasks only.
- latest `updates/*.md` explains last meaningful pass.

## Handoff instruction to next model

```txt
You are resuming an active aiprojectpack repository.
Read in order: README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, sources.md, then the latest relevant updates file.
Start in report-only mode and return:
- what is currently consistent
- what is unresolved
- highest-value bounded safe-update if approved
- files relied on
```

## What success looks like
- Next model does not re-open settled decisions.
- Next model does not erase unresolved items.
- Next model proposes one bounded improvement and names touched files before editing.
