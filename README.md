# ai　project　pack

`aiprojectpack` is a public, single-repository operating pack for AI-assisted development.
It gives every model session the same durable operating surface so work can continue safely across restarts, people, and models.

The pack is designed for teams that want **real continuity**, not chat-history luck:
- a current operating truth
- explicit decisions with reasons
- visible unresolved items
- concrete next actions
- source-aware claims
- append-only update logs

Useful immediately is the baseline; stronger over time is the result of consistent use.

## Who this is for

Use this repo when project quality drops because context keeps resetting between AI sessions.
Typical fits:
- product and technical planning with iterative AI support
- research-heavy implementation where evidence quality matters
- OSS release preparation with model handoff across sessions
- mixed human + AI teams that need auditable changes

## Repository operating model

`aiprojectpack` has two core operating modes and two support modes:

- **Report-only (default):** read and report; no file edits
- **Safe-update (bounded):** small, reviewable edits only
- **Handoff:** prepare the repo for fast transfer to another model/person
- **Weekly review:** reduce drift and keep files coherent

This is intentionally not autonomous memory or autonomous project management. It is a transparent operating surface.

## Read order (every session)

Read in this exact order unless the user says otherwise:

1. `README.md`
2. `AGENTS.md`
3. `current-truth.md`
4. `decisions.md`
5. `pending.md`
6. `next-actions.md`
7. `sources.md` (when evidence matters)
8. one relevant file in `playbooks/`
9. one relevant file in `adapters/`
10. latest relevant file in `updates/`

## First-use flow (unmistakable)

### 1) First report-only pass

Start with this prompt:

```txt
Use this repository as the operating pack.
Read README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, and sources.md in that order.
Work in report-only mode. Do not edit files.
Return:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on
```

Expected result: you get a bounded, reviewable status report before any repo edits.

### 2) First bounded safe-update pass

Only after approving the report, run:

```txt
Apply one bounded safe-update pass.
Allowed scope:
- tighten wording in current-truth.md without changing scope
- append one decision in decisions.md
- rewrite next-actions.md into concrete startable actions
- append one dated update log in updates/
Do not resolve unresolved claims without evidence.
Return touched files and why each change was safe.
```

Expected result: small, high-value edits with a clear audit trail.

### 3) Append update log and hand off

Require a dated update file in `updates/` for each meaningful safe-update or handoff pass.
This is what enables fast restart by another model.

## Core files (living operating files)

- `current-truth.md` — what is true now and in scope
- `decisions.md` — append-only decisions, reasons, and impact
- `pending.md` — unresolved items that still matter
- `next-actions.md` — concrete startable actions only
- `sources.md` — evidence map (primary / secondary / internal notes)
- `updates/` — append-only change log of meaningful passes

## Examples (read in this order)

1. [`examples/full-session-walkthrough.md`](examples/full-session-walkthrough.md)
2. [`examples/report-only-output-example.md`](examples/report-only-output-example.md)
3. [`examples/first-safe-update-pass.md`](examples/first-safe-update-pass.md)
4. [`examples/handoff-example.md`](examples/handoff-example.md)

## Playbooks

- [`playbooks/planning.md`](playbooks/planning.md)
- [`playbooks/research.md`](playbooks/research.md)
- [`playbooks/handoff.md`](playbooks/handoff.md)
- [`playbooks/weekly-review.md`](playbooks/weekly-review.md)

## Model adapters

- [`adapters/chatgpt.md`](adapters/chatgpt.md)
- [`adapters/claude.md`](adapters/claude.md)
- [`adapters/codex.md`](adapters/codex.md)

## Supporting docs

- [`docs/first-run.md`](docs/first-run.md)
- [`docs/model-selection.md`](docs/model-selection.md)
- [`docs/what-good-looks-like.md`](docs/what-good-looks-like.md)
- [`docs/support-positioning.md`](docs/support-positioning.md)

## Validation

Run:

```bash
python3 scripts/validate_repo.py
```

Validation checks required files, internal markdown references, known placeholder markers, and required examples/playbooks/adapters.

## Public support positioning

This repository is maintained as a practical public operating pack. Support is centered on operational clarity: coherent docs, reliable examples, safe-update discipline, and validation quality. See [`docs/support-positioning.md`](docs/support-positioning.md).

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

Use responsibly and review outputs before relying on them. See [DISCLAIMER.md](DISCLAIMER.md).
