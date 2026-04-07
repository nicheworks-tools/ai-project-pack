# Pending

Only unresolved items that materially affect next passes belong here.

## Open unresolved items
- **Validation ownership is undefined.** The repo does not yet state who runs `python3 scripts/validate_repo.py` on what cadence (per merge, daily, weekly), which risks silent regressions between passes.
- **Validator strictness threshold is undecided.** It is unresolved whether missing required section headings in core files should be warning-only or hard-fail behavior.
- **External first-run evidence is still sparse.** Adapter tuning decisions are blocked until at least two independent first-run reports are logged and linked.

## Waiting on external input
- First-run feedback from two independent users or teams using only README + AGENTS + examples.
- Evidence on which adapter (ChatGPT/Claude/Codex) most often fails first due to ambiguity, evidence mixing, or over-broad edits.

## Resume conditions
- Revisit validator strictness only after update logs show recurring structure failures.
- Revisit adapter wording only after external dry-run artifacts are appended in `updates/` and mapped in `sources.md`.
