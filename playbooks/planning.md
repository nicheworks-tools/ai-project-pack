# Planning Playbook

## When to use
Use this playbook when execution has stalled because priorities are unclear, actions are vague, or current tasks do not map to visible outputs.

## What to read first
1. `current-truth.md` (what is actually stable now)
2. `pending.md` (what still blocks progress)
3. `next-actions.md` (whether actions are startable)
4. latest relevant `updates/*.md` (what changed most recently)

## Likely files to update
- `next-actions.md` (primary output)
- `pending.md` (if an item is clarified or split)
- `decisions.md` (append only if planning creates a consequential choice)
- `updates/<date>-planning-pass.md`

## Planning procedure (bounded)
1. List up to three concrete outcomes needed this cycle.
2. Map each outcome to one owner-like action statement (even if owner is "next model").
3. Require each action to name a deliverable artifact (file update, log entry, evidence link).
4. Move anything not startable back to `pending.md` as unresolved.
5. Append an update log summarizing what changed and why it was safe.

## Good mini-example
- Weak action: "Improve handoff quality."
- Strong action: "Run one model-to-model restart simulation, record restart misses in `updates/2026-04-07-handoff-sim.md`, and add any persistent blockers to `pending.md`."

## Bad mini-example / failure mode
"Rewrite planning, handoff, and research docs for consistency" (broad, not bounded, and no observable output).

## How planning should sharpen `next-actions.md`
A sharpened `next-actions.md` should:
- start with verbs (`Run`, `Append`, `Record`, `Update`)
- include exactly what file/artifact will change
- include completion evidence (e.g., "contains X section" or "links Y source")
- avoid umbrella language like "improve", "enhance", or "refine" without output criteria
