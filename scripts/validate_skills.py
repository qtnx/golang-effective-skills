#!/usr/bin/env python3
"""Validate Codex skill folders in this repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ALLOWED_FRONTMATTER_KEYS = {"name", "description"}
BANNED_SKILL_FILES = {
    "README.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "CHANGELOG.md",
}
REFERENCE_RE = re.compile(r"(?:references/|\.?/references/)([A-Za-z0-9._/-]+\.md)")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["frontmatter must start on the first line with ---"]

    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, ["frontmatter must end with ---"]

    values: dict[str, str] = {}
    errors: list[str] = []
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"')
        values[key] = value

    extra = set(values) - ALLOWED_FRONTMATTER_KEYS
    missing = ALLOWED_FRONTMATTER_KEYS - set(values)
    if extra:
        errors.append(f"frontmatter has unsupported keys: {', '.join(sorted(extra))}")
    if missing:
        errors.append(f"frontmatter missing required keys: {', '.join(sorted(missing))}")
    return values, errors


def referenced_files(skill_md: Path) -> set[Path]:
    text = skill_md.read_text(encoding="utf-8")
    skill_dir = skill_md.parent
    return {skill_dir / "references" / match.group(1).split("references/")[-1] for match in REFERENCE_RE.finditer(text)}


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    values, frontmatter_errors = parse_frontmatter(skill_md)
    errors.extend(f"{skill_md}: {error}" for error in frontmatter_errors)

    if values.get("name") and values["name"] != skill_dir.name:
        errors.append(f"{skill_md}: name must match folder name {skill_dir.name!r}")
    if values.get("description") and len(values["description"]) < 40:
        errors.append(f"{skill_md}: description is too short to trigger reliably")

    body_lines = skill_md.read_text(encoding="utf-8").splitlines()
    if len(body_lines) > 150:
        errors.append(f"{skill_md}: expected <= 150 lines, got {len(body_lines)}")

    agents_file = skill_dir / "agents" / "openai.yaml"
    if not agents_file.exists():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")
    else:
        agents_text = agents_file.read_text(encoding="utf-8")
        if values.get("name") and f"${values['name']}" not in agents_text:
            errors.append(f"{agents_file}: default prompt should mention ${values['name']}")

    references_dir = skill_dir / "references"
    if not references_dir.exists():
        errors.append(f"{skill_dir}: missing references/ directory")

    for ref in referenced_files(skill_md):
        if not ref.exists():
            errors.append(f"{skill_md}: referenced file does not exist: {ref}")

    for path in skill_dir.rglob("*"):
        if path.is_file() and path.name in BANNED_SKILL_FILES:
            errors.append(f"{path}: public docs do not belong inside skill folders")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills_dir", type=Path)
    args = parser.parse_args()

    if not args.skills_dir.exists():
        print(f"{args.skills_dir}: directory does not exist", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in args.skills_dir.iterdir() if path.is_dir())
    if not skill_dirs:
        print(f"{args.skills_dir}: no skill directories found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
