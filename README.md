# aiprojectpack

A single text-first repository that an AI reads first, updates carefully, and uses to keep long-running work coherent.

`aiprojectpack` is for work that breaks when context stays trapped in chat: product planning, OSS release prep, research-heavy implementation, and model-to-model handoff. It separates **current truth**, **decisions**, **pending items**, **next actions**, and **sources** into stable files so each session starts from an operating surface instead of reconstruction.

This is not magic memory. It is a reviewable operating repo.

## Start here

Read in this order:

1. `README.md`
2. `AGENTS.md`
3. `current-truth.md`
4. `decisions.md`
5. `pending.md`
6. `next-actions.md`
7. `sources.md` if claims need evidence
8. one relevant playbook under `playbooks/`
9. one relevant adapter under `adapters/`
10. the latest relevant log under `updates/`

## First run

1. Copy this repo.
2. Replace the example content in the five core files with your own project state.
3. Start with this prompt in **report-only** mode:

```txt
Use this repository as the project operating pack.
Read README.md, AGENTS.md, current-truth.md, decisions.md, pending.md, next-actions.md, and sources.md in that order.
Work in report-only mode. Do not edit files. Return:
- what is currently consistent
- what is unresolved
- what should be updated first if safe-update is approved
- which files you relied on
```

4. If the report is bounded and sensible, move to **safe-update** with this prompt:

```txt
Apply only safe updates.
List touched files and why each change is safe.
Append one new file under updates/ describing the pass.
Do not rewrite broad sections for style.
```

## Modes

### Report-only
Read, evaluate, and propose. Do not edit files.

### Safe-update
Make only small reviewable changes such as:
- tightening `current-truth.md` without changing scope
- appending one real decision to `decisions.md`
- moving one resolved pending item with a logged reason
- rewriting `next-actions.md` into smaller concrete actions
- appending a dated file under `updates/`

### Handoff
Prepare the repo so another model or person can restart work fast.

### Review
Check whether current truth, decisions, pending items, next actions, and update history still agree.

## Files that matter most

- `current-truth.md`: what is true now
- `decisions.md`: what is decided and why
- `pending.md`: what is still unresolved
- `next-actions.md`: what to do next
- `sources.md`: where important claims came from
- `updates/`: what changed on each meaningful pass

## Included guidance

- `playbooks/planning.md`
- `playbooks/handoff.md`
- `playbooks/weekly-review.md`
- `adapters/chatgpt.md`
- `adapters/claude.md`
- `adapters/codex.md`
- `docs/first-run.md`
- `docs/model-selection.md`
- `docs/what-good-looks-like.md`

## Worked examples

- `examples/full-session-walkthrough.md` — one complete first loop
- `examples/report-only-output-example.md` — a good report-only response shape
- `examples/first-safe-update-pass.md` — one bounded safe-update
- `examples/handoff-example.md` — one clean handoff

## Validation

Run:

```bash
python3 scripts/validate_repo.py
```

It checks required files and common local markdown link mistakes.

## Non-goals

- hidden memory
- autonomous project management
- automatic factual truth
- broad platform features
- replacing review with convenience

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

Use at your own risk. Review AI output before relying on it. See [DISCLAIMER.md](DISCLAIMER.md).
