# Full Session Walkthrough

This walkthrough demonstrates immediate operational value on day one.

## 1) Before using the repo

A team working on an AI-assisted release process had three recurring failures:
- each new chat session reconstructed context differently
- unresolved issues were accidentally treated as settled
- “next steps” were broad suggestions instead of startable actions

## 2) What plain chat would miss

Without a durable repo surface, plain chat often misses:
- whether a claim is current truth vs unresolved
- why a previous decision was made
- what changed in the last meaningful pass
- which tasks are actually startable now

## 3) First report-only pass

### Prompt used

```txt
Use this repository as the operating pack.
Read README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, and sources.md in that order.
Work in report-only mode. Do not edit files.
Return:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on
```

### Example report-only result (abridged)

- Consistent: report-only default, bounded safe-update model, and append-only updates are aligned across README and AGENTS.
- Unresolved: validation cadence/ownership and stricter heading enforcement are still open.
- First safe updates: tighten one action list and append one update log with observed friction.
- Files relied on: README, AGENTS, current-truth, decisions, pending, next-actions, sources.

## 4) Safe-update approval

### Approval prompt

```txt
Apply one bounded safe-update pass.
Allowed scope:
- refine next-actions.md to make every item startable
- append one dated update in updates/
Do not change project scope or resolve pending items without evidence.
Return touched files, why safe, and what remains unresolved.
```

## 5) Touched files

- `next-actions.md` — replaced abstract tasks with concrete steps and observable outputs.
- `updates/2026-04-07-*.md` — appended pass log for continuity.

## 6) Update log entry (shape)

A good update entry includes:
- what changed
- what stayed unresolved
- why edits were safe
- what the next model should do first

## 7) Next-session restart

At restart, the next model reads the standard order and latest update, then can answer quickly:
- what is stable
- what is still open
- what to do next without reinterpretation

That is the core value: less reconstruction, faster safe progress.
