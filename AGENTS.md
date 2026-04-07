# AGENTS

Use this repository as the operating surface for long-running work.

## Read order

Always read in this order unless the user says otherwise:

1. `README.md`
2. `AGENTS.md`
3. `current-truth.md`
4. `decisions.md`
5. `pending.md`
6. `next-actions.md`
7. `sources.md` when evidence matters
8. one relevant file under `playbooks/`
9. one relevant file under `adapters/`
10. the latest relevant file under `updates/`

## Default mode

Default to **report-only**.
Do not edit files unless the user explicitly asks for a safe-update or handoff pass.

## What counts as safe-update

Usually safe:
- tightening wording in `current-truth.md` without changing project scope
- appending one real decision to `decisions.md`
- moving one resolved item in `pending.md` with a logged reason
- rewriting `next-actions.md` into smaller concrete actions
- adding one source to `sources.md`
- appending one dated update log under `updates/`

Not safe by default:
- changing product scope
- turning unresolved claims into truth
- removing history for neatness
- rewriting whole files because a cleaner structure seems nicer
- inventing sources
- changing legal, financial, or production assumptions

## Output contract

In report-only mode return:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on

In safe-update mode return:
- touched files
- why each change was safe
- what intentionally stayed unresolved
- which new update log was added

## Stop conditions

Stop and ask for confirmation if:
- scope would materially change
- an unresolved claim would need promotion into truth
- a source-backed claim is missing evidence
- an old decision would need to be overturned

## Update style

Prefer append over rewrite.
Prefer one bounded change over broad cleanup.
Prefer explicit uncertainty over polished certainty.
