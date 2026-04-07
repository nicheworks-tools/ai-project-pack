# ChatGPT Adapter

## Best fit
Use ChatGPT when you need strong ambiguity reduction and option framing before any file edits.

## Distinct operating bias
Clarification-first workflow: reduce interpretation risk before touching repository files.

## Read first
- `README.md`
- `AGENTS.md`
- `current-truth.md`
- `pending.md`
- `next-actions.md`

## Clarification-first workflow
1. Restate the request in operational terms (scope, constraints, expected outputs).
2. Surface ambiguity as explicit options with tradeoffs.
3. Recommend one bounded option.
4. Wait for explicit option approval before editing.

## Short good opening response example
"I can run this as a bounded safe-update. I see two valid paths: (A) strengthen examples + playbooks only, or (B) include core-file tightening and update log append. I recommend B because it improves first-run usability while keeping scope stable. Confirm B and I will list touched files before edits."

## Failure mode: editing too early
Starting edits before options are confirmed often causes silent scope drift and rework. If ambiguity exists, stop and resolve it first.
