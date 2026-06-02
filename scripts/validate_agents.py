#!/usr/bin/env python3
"""Validate root-level special agent profiles."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_KEYS = {"name", "description", "model"}
ALLOWED_KEYS = REQUIRED_KEYS
NAME_RE = re.compile(r"^[a-z0-9-]+$")


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
    key: str | None = None

    for line in lines[1:end]:
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if key == "description":
                values[key] = (values.get(key, "") + "\n" + line.strip()).strip()
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        raw_key, raw_value = line.split(":", 1)
        key = raw_key.strip()
        value = raw_value.strip().strip('"')
        if value == "|":
            value = ""
        values[key] = value

    extra = set(values) - ALLOWED_KEYS
    missing = REQUIRED_KEYS - set(values)
    if extra:
        errors.append(f"frontmatter has unsupported keys: {', '.join(sorted(extra))}")
    if missing:
        errors.append(f"frontmatter missing required keys: {', '.join(sorted(missing))}")
    return values, errors


def validate_agent(path: Path) -> list[str]:
    values, errors = parse_frontmatter(path)

    name = values.get("name", "")
    if name:
        if not NAME_RE.fullmatch(name):
            errors.append("name must contain only lowercase letters, digits, and hyphens")
        if path.stem != name:
            errors.append(f"name must match filename stem {path.stem!r}")

    description = values.get("description", "")
    if len(description) < 80:
        errors.append("description is too short to describe trigger behavior")

    if values.get("model") != "inherit":
        errors.append("model must be inherit")

    body = path.read_text(encoding="utf-8").split("---", 2)[-1].strip()
    if len(body.splitlines()) < 20:
        errors.append("agent body is too short to be useful")

    return [f"{path}: {error}" for error in errors]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("agents_dir", type=Path)
    args = parser.parse_args()

    if not args.agents_dir.exists():
        print(f"{args.agents_dir}: directory does not exist", file=sys.stderr)
        return 1

    agent_files = sorted(args.agents_dir.glob("*.md"))
    if not agent_files:
        print(f"{args.agents_dir}: no agent profiles found", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in agent_files:
        errors.extend(validate_agent(path))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(agent_files)} agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
