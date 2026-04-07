# Research Playbook

## When to use
Use when a claim could change `current-truth.md`, influence a decision, or alter public-facing guidance.

## What to read first
1. `sources.md` (current evidence map)
2. `current-truth.md` (claims already promoted)
3. `pending.md` (unresolved evidence-dependent items)
4. latest relevant `updates/*.md` (recent evidence activity)

## Likely files to update
- `sources.md` (add or strengthen evidence entries)
- `pending.md` (keep unresolved evidence gaps visible)
- `current-truth.md` (only for supported claims)
- `decisions.md` (append when evidence changes a consequential direction)
- `updates/<date>-research-pass.md`

## Evidence hygiene rules
- Supported claims require traceable primary or high-quality secondary evidence.
- Inferred claims may guide next research tasks but must not be promoted into truth.
- Unresolved claims stay in `pending.md` with explicit evidence gaps.

## Supported-claim example
"`scripts/validate_repo.py` checks required files, internal markdown links, and placeholder markers" is supported by direct review of the validator script and can be recorded in `current-truth.md`.

## Inferred-but-not-promoted example
"External teams will likely need stricter section enforcement" is a plausible inference, but it stays unresolved until evidence from real user runs is logged in `updates/` and linked in `sources.md`.

## Bad example (incorrect promotion)
"One team member said weekly reviews felt optional, so weekly review cadence is no longer needed" is weak evidence and must not be promoted into `current-truth.md` or `decisions.md` without stronger support.

## Output quality check before edits
If you cannot clearly label each consequential claim as supported, inferred, or unresolved, stop and keep the claim unresolved.
