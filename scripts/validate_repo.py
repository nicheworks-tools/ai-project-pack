from __future__ import annotations
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    'README.md', 'AGENTS.md', 'current-truth.md', 'decisions.md', 'pending.md',
    'next-actions.md', 'sources.md', 'LICENSE', 'DISCLAIMER.md',
    'updates/README.md', 'updates/000-initial.md',
    'templates/decision-entry.md', 'templates/pending-entry.md',
    'templates/source-entry.md', 'templates/update-entry.md',
    'playbooks/planning.md', 'playbooks/handoff.md', 'playbooks/weekly-review.md',
    'adapters/chatgpt.md', 'adapters/claude.md', 'adapters/codex.md',
    'examples/full-session-walkthrough.md', 'examples/report-only-output-example.md',
    'examples/first-safe-update-pass.md', 'examples/handoff-example.md',
    'docs/first-run.md', 'docs/model-selection.md', 'docs/what-good-looks-like.md',
]

LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')

errors = []
for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f'missing required file: {rel}')

for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    for target in LINK_RE.findall(text):
        if target.startswith('http://') or target.startswith('https://') or target.startswith('#'):
            continue
        resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except Exception:
            errors.append(f'link escapes repo: {md.relative_to(ROOT)} -> {target}')
            continue
        if not resolved.exists():
            errors.append(f'broken link: {md.relative_to(ROOT)} -> {target}')

if errors:
    print('repo validation failed')
    for e in errors:
        print('-', e)
    sys.exit(1)

print('repo validation passed')
