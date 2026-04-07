# Claude Adapter

## Best fit
Use Claude when evidence quality and claim classification are the highest priority.

## Distinct operating bias
Evidence-first structure with explicit buckets:
- **Supported**
- **Inferred**
- **Unresolved**

## Read first
- `README.md`
- `AGENTS.md`
- `sources.md`
- `current-truth.md`
- `pending.md`

## Source-task workflow
1. Label each consequential claim as supported, inferred, or unresolved.
2. Create source tasks for any inferred claim that might become consequential.
3. Update `sources.md` before promoting supported claims into `current-truth.md`.
4. Keep unresolved claims visible in `pending.md` until evidence is sufficient.

## Short realistic output example
- Supported: update logs are append-only continuity artifacts required after meaningful passes.
- Inferred: current adapter guidance could improve once external first-run evidence is collected.
- Unresolved: validator cadence owner is still undefined.
- Source task: run one external dry run, append evidence in `updates/`, and link it under secondary sources.

## Failure mode: blending inference into support
Do not treat plausible interpretation as evidence. If a claim lacks traceable support, keep it inferred or unresolved.
