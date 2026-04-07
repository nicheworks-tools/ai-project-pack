# Full Session Walkthrough

## Before the repo
Plain chat had the release goal, unresolved naming, and one unverified benchmark claim mixed together. A new session would likely treat all three as equally stable.

## Initial state
- `../current-truth.md` says the goal is the first narrow public release.
- `../pending.md` shows one unresolved naming choice and one source verification task.
- `../next-actions.md` is still too generic.

## First prompt
```txt
Use this repository as the project operating pack.
Read README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, and sources.md.
Work in report-only mode. Do not edit files.
Return what is currently consistent, what is unresolved, and what should be updated first if safe-update is approved.
```

## Good report-only response
- Consistent: the release is intentionally narrow and feature expansion is deferred.
- Unresolved: naming is not final; benchmark wording still needs source verification.
- First safe updates: tighten `next-actions.md`; add a dated update log after edits.

## Safe-update approval
```txt
Apply only safe updates.
Tighten next-actions.md and add one dated update log.
Do not resolve naming or promote benchmark wording into current truth.
List touched files and why each change is safe.
```

## Touched files
- `../next-actions.md` — vague actions replaced with three concrete actions
- `../updates/2026-04-07-session.md` — logged what changed and what stayed unresolved

## Why this was safe
- scope did not change
- unresolved items stayed in `../pending.md`
- no claim moved into truth without evidence
