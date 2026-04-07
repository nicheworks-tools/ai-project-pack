# Sources

Track evidence for consequential claims. Do not blur evidence strength.

## Primary sources (highest confidence)
- Repository files under version control: `README.md`, `AGENTS.md`, core files, examples, playbooks, adapters, docs, templates, and `updates/` logs.
- Validator output from `python3 scripts/validate_repo.py` run against the current commit.
- Explicit decisions recorded in append-only `decisions.md` entries.

## Secondary sources (useful but confirmable)
- External first-run walkthrough notes that reference exact repository files or update logs.
- Comparative model-run notes (ChatGPT/Claude/Codex) that document repeat failure patterns with artifacts.
- Community feedback issues/discussions that include reproducible steps.

## Internal notes (not sufficient alone)
- Maintainer intuition about clarity gaps.
- Single-session observations without reproducible artifacts.
- Draft hypotheses about future improvements.

## Promotion rule
A claim may move into `current-truth.md` only when backed by primary evidence, or by secondary evidence strong enough to be independently verified. If evidence is weaker, keep the claim inferred or unresolved in `pending.md`.
