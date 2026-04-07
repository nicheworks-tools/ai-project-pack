# Decisions

Append-only decision ledger. Add new entries at the bottom.

### 2026-04-07 — Keep report-only as default operating mode
- Decision: every new session must begin with a report-only pass before any file edits.
- Reason: this prevents accidental scope drift and creates a review checkpoint.
- Impact: edits become explicit second-step actions rather than silent first-step changes.

### 2026-04-07 — Require update-log append for meaningful edit passes
- Decision: each safe-update or handoff pass must append a dated file under `updates/`.
- Reason: session continuity depends on visible historical context, not hidden chat history.
- Impact: model handoff and restart quality improve; auditability is preserved.

### 2026-04-07 — Preserve public-facing scope while improving operational density
- Decision: strengthen content quality and coherence in-place without reducing file structure or README scope.
- Reason: users need a shippable operating pack, not a trimmed template.
- Impact: repository remains substantial, practical, and immediately useful on first run.

### 2026-04-07 — Raise examples/playbooks/adapters to operational-quality baseline
- Decision: strengthen priority examples, playbooks, and adapters with concrete prompts, outputs, failure modes, and touched-files discipline.
- Reason: first-time users need immediately executable patterns, not instructional abstraction.
- Impact: first-run trust improves and model-to-model restart becomes faster and less error-prone.
