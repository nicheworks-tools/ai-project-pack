# AGENTS

Use this repository as the operating surface for long-running AI-assisted project work.

## Required read order

Always read in this order unless the user explicitly overrides it:

1. `README.md`
2. `AGENTS.md`
3. `current-truth.md`
4. `decisions.md`
5. `pending.md`
6. `next-actions.md`
7. `sources.md` (when evidence matters)
8. one relevant file under `playbooks/`
9. one relevant file under `adapters/`
10. latest relevant file under `updates/`

## Default mode: report-only

Default to **report-only**.
Do not edit files unless the user explicitly approves **safe-update** or requests a **handoff pass**.

### Report-only output contract

Return exactly:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on

## Safe-update contract (bounded changes only)

A safe-update is a small, reviewable edit that improves operational clarity without changing scope.

### Good safe-update examples

- tighten wording in `current-truth.md` without promoting unresolved claims
- append one real decision in `decisions.md` with reason + impact
- move one resolved item in `pending.md` and log why
- rewrite `next-actions.md` into concrete startable tasks
- add one source to `sources.md` with type and relevance
- append one dated update file under `updates/`

### Bad safe-update examples

- changing project scope or release goals without approval
- turning unresolved items into truth without source support
- deleting history to make files look cleaner
- broad rewrites across many files for style only
- inventing sources or references
- changing legal, financial, security, or production assumptions without explicit direction

## Handoff contract

When asked for handoff:
- keep unresolved items visible
- ensure next actions are startable without reinterpretation
- append one dated update log for the handoff pass
- include a touched-files report

## Required reporting for any edit pass

For safe-update or handoff passes, always return:
- touched files
- why each change was safe
- what intentionally stayed unresolved
- which update log file was appended

## Stop conditions (require confirmation)

Stop and request confirmation if any apply:
- scope would materially change
- unresolved claims would need promotion into truth
- source-backed claims are missing evidence
- an existing decision would need to be overturned
- requested edits conflict with this contract

## Update style

- prefer append over rewrite
- prefer one bounded change over broad cleanup
- preserve explicit uncertainty
- optimize for restart speed by another model
