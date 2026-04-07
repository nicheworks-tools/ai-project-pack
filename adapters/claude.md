# Claude Adapter

## Best fit
Use Claude when evidence quality, synthesis, and claim hygiene are the top priority.

## Operating bias
Separate evidence states explicitly: supported vs inferred vs unresolved.

## Read first
- `README.md`
- `AGENTS.md`
- `sources.md`
- `current-truth.md`
- `pending.md`

## Preferred response structure
- **Supported:** directly supported by a recorded source.
- **Inferred:** reasonable interpretation, not yet source-backed.
- **Unresolved:** requires confirmation or new evidence.
- **Source tasks:** concrete evidence-collection actions.

## Good mini-example
- Supported: update log append is required for meaningful edit passes.
- Inferred: adapter wording may benefit from first-run user data.
- Unresolved: validation cadence ownership.
- Source task: capture one external dry-run report and log in `updates/` + `sources.md`.

## Failure mode to avoid
Merging inferred claims into supported claims without explicit evidence.
