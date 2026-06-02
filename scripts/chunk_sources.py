#!/usr/bin/env python3
"""Normalize and chunk the Go source corpus for targeted agent grounding."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")


@dataclass(frozen=True)
class SourceInfo:
    name: str
    url: str
    license_ref: str


SOURCE_INFO = {
    "google-go-styleguide": SourceInfo(
        "Google Go Style Guide",
        "https://google.github.io/styleguide/go/",
        "sources/licenses/google-styleguide-LICENSE.txt",
    ),
    "effective-go": SourceInfo(
        "Effective Go",
        "https://go.dev/doc/effective_go",
        "sources/licenses/go-LICENSE.txt",
    ),
    "uber-go-guide": SourceInfo(
        "Uber Go Style Guide",
        "https://github.com/uber-go/guide/blob/master/style.md",
        "sources/licenses/uber-go-guide-LICENSE.txt",
    ),
}


class MarkdownHTMLParser(HTMLParser):
    """Small HTML-to-Markdown converter for source chunking."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.parts: list[str] = []
        self._heading: int | None = None
        self._pre = False
        self._skip_depth = 0
        self._link_href: list[str | None] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag in {"script", "style", "nav", "header", "footer"}:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if re.fullmatch(r"h[1-4]", tag):
            self._heading = int(tag[1])
            self.parts.append("\n" + "#" * self._heading + " ")
        elif tag == "p":
            self.parts.append("\n")
        elif tag in {"br"}:
            self.parts.append("\n")
        elif tag in {"pre"}:
            self._pre = True
            self.parts.append("\n```go\n")
        elif tag in {"li"}:
            self.parts.append("\n- ")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("_")
        elif tag == "code" and not self._pre:
            self.parts.append("`")
        elif tag == "a":
            self._link_href.append(attrs_map.get("href"))

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav", "header", "footer"} and self._skip_depth:
            self._skip_depth -= 1
            return
        if self._skip_depth:
            return
        if re.fullmatch(r"h[1-4]", tag):
            self._heading = None
            self.parts.append("\n")
        elif tag in {"p", "ul", "ol", "div", "section"}:
            self.parts.append("\n")
        elif tag == "pre":
            self._pre = False
            self.parts.append("\n```\n")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("_")
        elif tag == "code" and not self._pre:
            self.parts.append("`")
        elif tag == "a" and self._link_href:
            self._link_href.pop()

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        text = html.unescape(data)
        if self._pre:
            self.parts.append(text)
        else:
            self.parts.append(re.sub(r"\s+", " ", text))

    def handle_entityref(self, name: str) -> None:
        if not self._skip_depth:
            self.parts.append(html.unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        if not self._skip_depth:
            self.parts.append(html.unescape(f"&#{name};"))

    def markdown(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "section"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_info(path: Path) -> SourceInfo:
    for key, info in SOURCE_INFO.items():
        if key in path.parts:
            return info
    return SourceInfo("Unknown", "", "")


def normalize(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() == ".html":
        parser = MarkdownHTMLParser()
        parser.feed(text)
        return parser.markdown()
    return text if text.endswith("\n") else text + "\n"


def split_chunks(markdown: str) -> list[tuple[str, str]]:
    lines = markdown.splitlines()
    chunks: list[tuple[str, list[str]]] = []
    current_title = "overview"
    current: list[str] = []

    for line in lines:
        match = HEADING_RE.match(line)
        if match:
            if current:
                chunks.append((current_title, current))
            current_title = match.group(2).strip()
            current = [line]
        else:
            current.append(line)

    if current:
        chunks.append((current_title, current))

    return [(title, "\n".join(body).strip() + "\n") for title, body in chunks if "\n".join(body).strip()]


def write_chunk(path: Path, content: str, source_path: Path, info: SourceInfo) -> None:
    header = (
        "---\n"
        f'source_name: "{info.name}"\n'
        f'source_url: "{info.url}"\n'
        f'source_path: "{source_path.as_posix()}"\n'
        f'license_ref: "{info.license_ref}"\n'
        "---\n\n"
    )
    path.write_text(header + content, encoding="utf-8")


def iter_source_files(raw_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in raw_root.rglob("*"):
        if not path.is_file():
            continue
        if path.name.endswith(".headers.txt") or path.name == "headers.txt":
            continue
        if path.suffix.lower() in {".md", ".html"}:
            files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raw_root", type=Path)
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()

    normalized_dir = args.output_root / "normalized"
    chunks_dir = args.output_root / "chunks"
    shutil.rmtree(normalized_dir, ignore_errors=True)
    shutil.rmtree(chunks_dir, ignore_errors=True)
    normalized_dir.mkdir(parents=True, exist_ok=True)
    chunks_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, object] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "raw_root": args.raw_root.as_posix(),
        "sources": [],
        "chunks": [],
    }

    used_names: dict[str, int] = {}
    for source in iter_source_files(args.raw_root):
        info = source_info(source)
        normalized = normalize(source)
        source_slug = slugify("-".join(source.relative_to(args.raw_root).parts))
        normalized_path = normalized_dir / f"{source_slug}.md"
        normalized_path.write_text(normalized, encoding="utf-8")

        source_entry = {
            "source_path": source.as_posix(),
            "normalized_path": normalized_path.as_posix(),
            "source_name": info.name,
            "source_url": info.url,
            "sha256": sha256(source),
        }
        manifest["sources"].append(source_entry)

        for index, (title, content) in enumerate(split_chunks(normalized), 1):
            base = f"{source_slug}-{index:03d}-{slugify(title)}"
            count = used_names.get(base, 0)
            used_names[base] = count + 1
            chunk_name = f"{base}.md" if count == 0 else f"{base}-{count + 1}.md"
            chunk_path = chunks_dir / chunk_name
            write_chunk(chunk_path, content, source, info)
            manifest["chunks"].append(
                {
                    "chunk_path": chunk_path.as_posix(),
                    "source_path": source.as_posix(),
                    "title": title,
                }
            )

    manifest["source_count"] = len(manifest["sources"])
    manifest["chunk_count"] = len(manifest["chunks"])
    (args.output_root / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {manifest['source_count']} normalized sources and {manifest['chunk_count']} chunks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
