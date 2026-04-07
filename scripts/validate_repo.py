from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "current-truth.md",
    "decisions.md",
    "pending.md",
    "next-actions.md",
    "sources.md",
    "LICENSE",
    "DISCLAIMER.md",
    "updates/README.md",
    "updates/000-initial.md",
    "templates/decision-entry.md",
    "templates/pending-entry.md",
    "templates/source-entry.md",
    "templates/update-entry.md",
    "playbooks/planning.md",
    "playbooks/research.md",
    "playbooks/handoff.md",
    "playbooks/weekly-review.md",
    "adapters/chatgpt.md",
    "adapters/claude.md",
    "adapters/codex.md",
    "examples/full-session-walkthrough.md",
    "examples/report-only-output-example.md",
    "examples/first-safe-update-pass.md",
    "examples/handoff-example.md",
    "docs/first-run.md",
    "docs/model-selection.md",
    "docs/what-good-looks-like.md",
    "docs/support-positioning.md",
]

REQUIRED_EXAMPLE_FILES = [
    "examples/full-session-walkthrough.md",
    "examples/report-only-output-example.md",
    "examples/first-safe-update-pass.md",
    "examples/handoff-example.md",
]

REQUIRED_PLAYBOOK_FILES = [
    "playbooks/planning.md",
    "playbooks/research.md",
    "playbooks/handoff.md",
    "playbooks/weekly-review.md",
]

REQUIRED_ADAPTER_FILES = [
    "adapters/chatgpt.md",
    "adapters/claude.md",
    "adapters/codex.md",
]

KNOWN_PLACEHOLDER_MARKERS = [
    "TODO",
    "TBD",
    "FIXME",
    "XXX",
    "replace later",
    "lorem ipsum",
    "coming soon",
    "insert here",
    "<placeholder>",
]

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def existing_file(path: str) -> bool:
    return (ROOT / path).exists()


def is_internal_markdown_path(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return False
    return target.endswith(".md") or "/" in target or target.startswith("./") or target.startswith("../")


def validate_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not existing_file(rel):
            errors.append(f"missing required file: {rel}")


def validate_required_groups(errors: list[str]) -> None:
    for rel in REQUIRED_EXAMPLE_FILES:
        if not existing_file(rel):
            errors.append(f"missing required example file: {rel}")

    for rel in REQUIRED_PLAYBOOK_FILES:
        if not existing_file(rel):
            errors.append(f"missing required playbook file: {rel}")

    for rel in REQUIRED_ADAPTER_FILES:
        if not existing_file(rel):
            errors.append(f"missing required adapter file: {rel}")


def validate_internal_markdown_links(errors: list[str]) -> None:
    root_resolved = ROOT.resolve()
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text):
            if not is_internal_markdown_path(target):
                continue

            resolved = (md.parent / target).resolve()
            try:
                resolved.relative_to(root_resolved)
            except ValueError:
                errors.append(f"link escapes repo: {md.relative_to(ROOT)} -> {target}")
                continue

            if not resolved.exists():
                errors.append(f"broken internal link: {md.relative_to(ROOT)} -> {target}")


def validate_placeholder_markers(errors: list[str]) -> None:
    markdown_files = ROOT.rglob("*.md")
    for md in markdown_files:
        text = md.read_text(encoding="utf-8")
        lowered = text.lower()
        for marker in KNOWN_PLACEHOLDER_MARKERS:
            needle = marker.lower()
            if needle in lowered:
                errors.append(
                    f"placeholder marker '{marker}' found in {md.relative_to(ROOT)}"
                )


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    validate_required_groups(errors)
    validate_internal_markdown_links(errors)
    validate_placeholder_markers(errors)

    if errors:
        print("repo validation failed")
        for err in sorted(set(errors)):
            print(f"- {err}")
        return 1

    print("repo validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
