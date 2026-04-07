# Current Truth

## Project snapshot
`aiprojectpack` is a public single-repo operating pack for AI-assisted development.
The repository is used as a durable operating surface to avoid session-reset drift.
The published package includes core operating files, examples, playbooks, adapters, docs, templates, and validation.

## Near-term goal
Ship a coherent first public version that is immediately usable by first-time users following only `README.md` + `AGENTS.md`.

## Fixed constraints
- Keep repository public-facing and production-credible.
- Do not mark as draft/WIP/incomplete/internal.
- Preserve single-repo concept, report-only default, and bounded safe-update behavior.
- Do not shrink file structure or remove substantive sections to hide inconsistency.

## Current state
- Core structure is present and validated by `scripts/validate_repo.py`.
- Operating guidance exists across README, AGENTS, examples, playbooks, adapters, and docs.
- Remaining risk is operational drift if future updates skip bounded-edit discipline and update-log appends.

## Immediate focus
Keep future changes bounded and evidence-aware so the pack remains coherent as a living operating tool.
