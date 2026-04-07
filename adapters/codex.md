# Codex Adapter

## Best fit
Use Codex when repository edits must be precise, bounded, and reviewable.

## Operating bias
Repo-edit discipline with explicit touched-files reporting.

## Read first
- `README.md`
- `AGENTS.md`
- `current-truth.md`
- `decisions.md`
- `pending.md`
- `next-actions.md`

## Required edit workflow
1. Perform report-only analysis first.
2. Confirm bounded safe-update scope.
3. Edit minimum necessary files.
4. Append one dated update log under `updates/`.
5. Return touched files + why each change was safe + what remained unresolved.

## Good mini-example
Touched files:
- `next-actions.md` — converted vague items into startable actions.
- `updates/2026-04-07-safe-update.md` — appended pass summary.

Why safe:
- no scope or assumption change
- unresolved items preserved
- append-only history maintained

## Failure mode to avoid
Large multi-file rewrites that hide the purpose and safety of the update.
