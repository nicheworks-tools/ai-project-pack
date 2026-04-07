# Codex Adapter

## Best fit
Use Codex when repository edits must be precise, bounded, and auditable.

## Distinct operating bias
Report-only first, then minimal edits with strict touched-files discipline.

## Read first
- `README.md`
- `AGENTS.md`
- `current-truth.md`
- `decisions.md`
- `pending.md`
- `next-actions.md`

## Required workflow
1. Run report-only analysis and state unresolved items before edits.
2. Confirm bounded safe-update scope and expected touched files.
3. Edit only the minimum set of files needed.
4. Append one dated update log in `updates/`.
5. Return touched files, safety rationale per file, and unresolved items that remained.

## Strong mini-example (touched files + why safe)
Touched files:
- `next-actions.md` — rewrote vague tasks into startable actions with explicit outputs.
- `decisions.md` — appended one decision entry; no existing entry changed.
- `updates/2026-04-07-operational-strength-pass.md` — append-only summary for restart continuity.

Why safe:
- no scope change
- no unresolved claim promoted without evidence
- changes are reviewable and tied to explicit artifacts

## Failure mode: broad rewrites that hide intent
Avoid sweeping multi-file rewrites that make it hard to review what changed and why the pass was safe.
