#!/usr/bin/env python3
"""Extract Markdown and HTML headings from the source corpus."""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path


MARKDOWN_HEADING = re.compile(r"^(#{1,4})\s+(.+?)\s*$")


class HeadingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self._current: tuple[int, int] | None = None
        self._parts: list[str] = []
        self.headings: list[tuple[int, int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if re.fullmatch(r"h[1-4]", tag):
            level = int(tag[1])
            line, _ = self.getpos()
            self._current = (level, line)
            self._parts = []

    def handle_data(self, data: str) -> None:
        if self._current:
            self._parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self._current:
            self._parts.append(html.unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        if self._current:
            self._parts.append(html.unescape(f"&#{name};"))

    def handle_endtag(self, tag: str) -> None:
        if self._current and re.fullmatch(r"h[1-4]", tag):
            level, line = self._current
            text = re.sub(r"\s+", " ", "".join(self._parts)).strip()
            if text:
                self.headings.append((line, level, text))
            self._current = None
            self._parts = []


def markdown_headings(path: Path) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        match = MARKDOWN_HEADING.match(line)
        if match:
            level = len(match.group(1))
            text = re.sub(r"\s+", " ", match.group(2)).strip()
            headings.append((line_no, level, text))
    return headings


def html_headings(path: Path) -> list[tuple[int, int, str]]:
    parser = HeadingParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser.headings


def iter_source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".html"}:
            continue
        if path.name.endswith(".headers.txt"):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Source corpus root")
    args = parser.parse_args()

    for path in iter_source_files(args.root):
        headings = html_headings(path) if path.suffix.lower() == ".html" else markdown_headings(path)
        for line_no, level, text in headings:
            print(f"{path}:{line_no}:h{level}:{text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
