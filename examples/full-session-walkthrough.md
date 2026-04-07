# Full Session Walkthrough

This is a realistic first loop that demonstrates why `aiprojectpack` prevents restart friction.

## 1) What was broken before using the repo

A small product team was using plain chat threads for release planning. After four sessions, they had the same recurring failures:
- each model restart re-interpreted goals differently
- one unresolved question about validation ownership kept getting treated as settled
- "next steps" became generic advice instead of executable tasks
- no durable record explained why prior wording decisions were made

## 2) What plain chat would likely miss

Without a durable operating surface, plain chat would likely miss:
- whether a statement belongs in `current-truth.md` or still in `pending.md`
- whether a proposed change is a bounded safe-update vs a scope shift
- the latest operational pass details that should be appended in `updates/`
- restart instructions for the next model

## 3) Exact first report-only prompt

```txt
Use this repository as the operating pack for this pass.
Read in order: README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, and sources.md.
Work in report-only mode. Do not edit files.
Return exactly:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on
```

## 4) Realistic report-only output

```txt
What is currently consistent:
- Report-only is the required first step before edits.
- Safe-update is defined as bounded and reviewable.
- Update logs are append-only and required for meaningful edit passes.

What is unresolved:
- Validation cadence and owner assignment are still open.
- Validator strictness on heading structure is undecided.
- Adapter refinements are waiting on external first-run evidence.

What should be updated first if safe-update is approved:
1) Rewrite next-actions.md items into actions with explicit outputs.
2) Append one dated update log documenting this pass.
3) Add a matching sources.md note that links evidence for any newly supported claim.

Which files were relied on:
README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, sources.md
```

## 5) Explicit safe-update approval prompt

```txt
Approved: run one bounded safe-update pass now.
Allowed edits:
- tighten current-truth.md wording for operational sharpness only
- append one new decision with reason + impact in decisions.md
- rewrite next-actions.md into fully startable tasks
- append one dated update file in updates/
Do not change scope, do not promote unresolved claims without evidence, and keep pending unresolved items visible.
Return touched files, why each edit was safe, what stayed unresolved, and the appended update log filename.
```

## 6) Explicit touched-files report (example)

```txt
Touched files:
- current-truth.md
- decisions.md
- next-actions.md
- updates/2026-04-07-operational-strength-pass.md

Why each edit was safe:
- current-truth.md: sharpened existing truths without adding unsupported claims.
- decisions.md: appended one decision entry; no prior entries rewritten.
- next-actions.md: converted abstract items into executable tasks with outputs.
- updates/2026-04-07-operational-strength-pass.md: append-only log entry for continuity.
```

## 7) Explicit update log append

A strong appended update log should contain:
- summary of what changed in this pass
- touched files list
- why edits were safe and bounded
- intentionally unresolved items
- first action for the next session

## 8) Next-session restart prompt

```txt
Resume from this repo, not from chat memory.
Read in order: README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, sources.md, then updates/2026-04-07-operational-strength-pass.md.
Start in report-only mode.
Return:
- what is currently consistent
- what is unresolved
- the highest-value safe-update if approved
- files relied on
```

## 9) What became easier because the repo existed

- restart quality improved because the next model could execute immediately without re-discovery
- unresolved items stayed visible instead of being overwritten by optimism
- safe-update scope stayed bounded and reviewable
- the update log made cross-session continuity explicit and auditable
