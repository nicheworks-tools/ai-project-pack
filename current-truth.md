# Current Truth

## Operating status (as of 2026-04-07)
`aiprojectpack` is a public, single-repo operating pack that is actively maintained for real AI-assisted project continuity.

## Stable operating contract
- Every pass starts in **report-only** mode before edits.
- Safe-update passes are bounded, reviewable, and scope-preserving.
- Meaningful safe-update and handoff passes append exactly one dated log in `updates/`.
- Unresolved items remain explicit in `pending.md` until evidence or a decision resolves them.

## What is now operationally strong
- Core file roles are differentiated and cross-referenced (`current-truth`, `decisions`, `pending`, `next-actions`, `sources`).
- Examples now show end-to-end first-loop behavior (report-only, approval, bounded edits, touched-files reporting, update-log append, restart prompt).
- Playbooks and adapters provide model-specific and mode-specific execution guidance rather than generic templates.

## Guardrails that remain non-negotiable
- Keep public-facing posture; do not label the repo as draft/internal/incomplete.
- Preserve single-repo concept and current file structure.
- Prefer append over rewrite for historical artifacts (`decisions.md`, `updates/`).
- Do not promote evidence-weak claims into truth.
