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
MIN_CHUNK_WORDS = 120
MAX_CHUNK_WORDS = 1600
VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


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
    "external": SourceInfo(
        "External Linked Documentation",
        "",
        "",
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
        tag = tag.lower()
        attrs_map = {key.lower(): value for key, value in attrs}
        if self._skip_depth:
            if tag not in VOID_TAGS:
                self._skip_depth += 1
            return
        if self._should_skip(tag, attrs_map):
            self._skip_depth += 1
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
        tag = tag.lower()
        if self._skip_depth:
            self._skip_depth -= 1
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
            href = self._link_href.pop()
            if href and href.startswith(("http://", "https://")):
                self.parts.append(f" <{href}>")

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

    def _should_skip(self, tag: str, attrs_map: dict[str, str | None]) -> bool:
        if tag in {"script", "style", "nav", "header", "footer"}:
            return True
        marker = " ".join(
            value or ""
            for key, value in attrs_map.items()
            if key in {"id", "class", "role", "aria-label"}
        ).lower()
        skip_markers = {
            "breadcrumb",
            "cookie",
            "drawer",
            "footer",
            "header",
            "menu",
            "navigation",
            "search",
            "sidebar",
            "skip",
            "social",
            "topbar",
        }
        return any(item in marker for item in skip_markers)

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
    if "external" in path.parts:
        text = path.read_text(encoding="utf-8", errors="replace")[:2000]
        name_match = re.search(r'^source_name:\s*"([^"]+)"', text, flags=re.MULTILINE)
        url_match = re.search(r'^source_url:\s*"([^"]+)"', text, flags=re.MULTILINE)
        return SourceInfo(
            name_match.group(1) if name_match else "External Linked Documentation",
            url_match.group(1) if url_match else "",
            "",
        )
    for key, info in SOURCE_INFO.items():
        if key in path.parts:
            return info
    return SourceInfo("Unknown", "", "")


def normalize(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = strip_frontmatter(text)
    if path.suffix.lower() == ".html":
        parser = MarkdownHTMLParser()
        parser.feed(text)
        text = parser.markdown()
    else:
        text = text if text.endswith("\n") else text + "\n"
    return clean_markdown(text)


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.DOTALL)


def clean_markdown(markdown: str) -> str:
    markdown = strip_frontmatter(markdown)
    markdown = re.sub(r"<!--.*?-->", "", markdown, flags=re.DOTALL)
    markdown = re.sub(r"\{%\s*raw\s*%\}|\{%\s*endraw\s*%\}", "", markdown)
    markdown = re.sub(r"^\s*\[Overview\].*$", "", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"^\s*https://google\.github\.io/styleguide/go/\S*\s*$", "", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", re.sub(r"^---.*?---", "", text, flags=re.DOTALL)))


def split_chunks(markdown: str) -> list[tuple[str, str]]:
    lines = markdown.splitlines()
    top_sections = split_by_heading_level(lines, 2)
    if len(top_sections) <= 1:
        top_sections = split_by_heading_level(lines, 1)

    chunks: list[tuple[str, str]] = []
    current_h1 = next((m.group(2).strip() for line in lines if (m := HEADING_RE.match(line)) and len(m.group(1)) == 1), "")

    for title, body_lines in top_sections:
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        if is_low_value_title(title):
            continue
        if word_count(body) > MAX_CHUNK_WORDS:
            sub_sections = split_by_heading_level(body_lines, 3)
            if len(sub_sections) > 1:
                parent_heading = body_lines[0] if body_lines and HEADING_RE.match(body_lines[0]) else ""
                for sub_title, sub_lines in sub_sections:
                    sub_body = "\n".join(sub_lines).strip()
                    if is_low_value_title(sub_title):
                        continue
                    if parent_heading and not sub_body.startswith(parent_heading):
                        sub_body = parent_heading + "\n\n" + sub_body
                    chunks.append((sub_title, sub_body + "\n"))
                continue
        if current_h1 and not body.startswith("# "):
            body = f"# {current_h1}\n\n{body}"
        chunks.append((title, body + "\n"))

    return merge_small_chunks(chunks)


def is_low_value_title(title: str) -> bool:
    normalized = slugify(title)
    return normalized in {
        "additional-navigation",
        "also-in-this-series",
        "archive",
        "breadcrumbs",
        "contents",
        "elsewhere",
        "footer",
        "links",
        "navigation",
        "next",
        "previous",
        "related",
        "related-posts",
        "see-also",
        "share",
        "social",
    }


def preamble_title(lines: list[str]) -> str:
    for line in lines:
        cleaned = re.sub(r"\s+", " ", line.strip(" #")).strip()
        if cleaned:
            return cleaned[:100]
    return "overview"


def split_by_heading_level(lines: list[str], level: int) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    preamble: list[str] = []
    current_title = ""
    current: list[str] = []

    for line in lines:
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == level:
            if current:
                sections.append((current_title, current))
                current = []
            elif preamble and not sections:
                if word_count("\n".join(preamble)) >= MIN_CHUNK_WORDS:
                    sections.append((preamble_title(preamble), preamble))
                else:
                    current = preamble[:]
                preamble = []
            current_title = match.group(2).strip()
            current.append(line)
        elif current:
            current.append(line)
        elif line.strip():
            preamble.append(line)

    if current:
        sections.append((current_title or "overview", current))
    elif preamble:
        sections.append(("overview", preamble))
    return sections


def merge_small_chunks(chunks: list[tuple[str, str]]) -> list[tuple[str, str]]:
    merged: list[tuple[str, str]] = []
    pending_title = ""
    pending_body = ""

    for title, body in chunks:
        if not pending_body:
            pending_title, pending_body = title, body
            continue
        if word_count(pending_body) < MIN_CHUNK_WORDS:
            pending_title = pending_title if pending_title != "overview" else title
            pending_body = pending_body.rstrip() + "\n\n" + body
        else:
            merged.append((pending_title, pending_body))
            pending_title, pending_body = title, body

    if pending_body:
        if merged and word_count(pending_body) < MIN_CHUNK_WORDS:
            prev_title, prev_body = merged[-1]
            merged[-1] = (prev_title, prev_body.rstrip() + "\n\n" + pending_body)
        else:
            merged.append((pending_title, pending_body))

    sized: list[tuple[str, str]] = []
    for title, body in merged:
        if word_count(body) < MIN_CHUNK_WORDS:
            continue
        sized.extend(split_oversized_chunk(title, body))
    return merge_tiny_split_tails(sized)


def split_oversized_chunk(title: str, body: str) -> list[tuple[str, str]]:
    if word_count(body) <= MAX_CHUNK_WORDS:
        return [(title, body.strip() + "\n")]

    heading = ""
    lines = body.splitlines()
    if lines and HEADING_RE.match(lines[0]):
        heading = lines[0]
        body = "\n".join(lines[1:]).strip()
    limit = max(MIN_CHUNK_WORDS, MAX_CHUNK_WORDS - word_count(heading))

    paragraphs = re.split(r"\n{2,}", body)
    chunks: list[tuple[str, str]] = []
    current: list[str] = []
    current_words = 0
    part = 1

    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        for block in split_large_block(paragraph, limit):
            paragraph_words = word_count(block)
            if current and current_words + paragraph_words > limit:
                chunk_body = "\n\n".join(current).strip()
                if heading:
                    chunk_body = f"{heading}\n\n{chunk_body}"
                chunks.append((f"{title} part {part}", chunk_body + "\n"))
                part += 1
                current = []
                current_words = 0
            current.append(block)
            current_words += paragraph_words

    if current:
        chunk_body = "\n\n".join(current).strip()
        if heading:
            chunk_body = f"{heading}\n\n{chunk_body}"
        chunks.append((f"{title} part {part}" if part > 1 else title, chunk_body + "\n"))

    return chunks


def split_large_block(block: str, max_words: int = MAX_CHUNK_WORDS) -> list[str]:
    if word_count(block) <= max_words:
        return [block]

    pieces: list[str] = []
    current: list[str] = []
    current_words = 0

    for line in block.splitlines():
        line_words = word_count(line)
        if line_words > max_words:
            words = line.split()
            for start in range(0, len(words), max_words):
                if current:
                    pieces.append("\n".join(current).strip())
                    current = []
                    current_words = 0
                pieces.append(" ".join(words[start : start + max_words]))
            continue
        if current and current_words + line_words > max_words:
            chunk_body = "\n\n".join(current).strip()
            pieces.append(chunk_body)
            current = []
            current_words = 0
        current.append(line)
        current_words += line_words

    if current:
        pieces.append("\n".join(current).strip())

    return [piece for piece in pieces if piece]


def merge_tiny_split_tails(chunks: list[tuple[str, str]]) -> list[tuple[str, str]]:
    merged: list[tuple[str, str]] = []
    for title, body in chunks:
        if merged and word_count(body) < MIN_CHUNK_WORDS:
            prev_title, prev_body = merged[-1]
            if word_count(prev_body) + word_count(body) <= MAX_CHUNK_WORDS:
                merged[-1] = (prev_title, prev_body.rstrip() + "\n\n" + body)
                continue
        if word_count(body) >= MIN_CHUNK_WORDS:
            merged.append((title, body))
    return merged


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
    all_files: list[Path] = []
    for path in raw_root.rglob("*"):
        if not path.is_file():
            continue
        if path.name.endswith(".headers.txt") or path.name == "headers.txt":
            continue
        if path.suffix.lower() in {".md", ".html"}:
            all_files.append(path)

    # Prefer canonical Markdown where both rendered HTML and Markdown source exist.
    selected: list[Path] = []
    for path in sorted(all_files):
        if "google-go-styleguide" in path.parts and path.suffix.lower() == ".html":
            md_peer = path.with_suffix(".md")
            if md_peer.exists():
                continue
        if "uber-go-guide" in path.parts and path.suffix.lower() == ".html":
            continue
        selected.append(path)
    return selected


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
