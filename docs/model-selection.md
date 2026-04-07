# Model Selection

Choose the model/tool based on task shape, then still start in report-only mode.

## Start with ChatGPT when
- the problem statement is ambiguous
- stakeholders use inconsistent language
- you need clear option framing before edits

See: `adapters/chatgpt.md`.

## Start with Claude when
- evidence quality determines correctness
- you need supported/inferred/unresolved separation
- research synthesis quality matters most

See: `adapters/claude.md`.

## Start with Codex when
- you need direct repo edits with strict discipline
- touched-file accountability matters
- safe-update bounds must be enforced in implementation

See: `adapters/codex.md`.

## Practical default
If unsure, run report-only with whichever model is available, then select the adapter style for the safe-update pass.
