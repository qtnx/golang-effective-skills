---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/comment"
source_path: "sources/raw/external/go-dev-doc-comment-d01a1d6946.html"
license_ref: ""
---

## Syntax
Go doc comments are written in a simple syntax that supports paragraphs, headings, links, lists, and preformatted code blocks. To keep comments lightweight and readable in source files, there is no support for complex features like font changes or raw HTML. Markdown aficionados can view the syntax as a simplified subset of Markdown.
The standard formatter gofmt reformats doc comments to use a canonical formatting for each of these features. Gofmt aims for readability and user control over how comments are written in source code but will adjust presentation to make the semantic meaning of a particular comment clearer, analogous to reformatting `1+2 * 3` to `1 + 2*3` in ordinary source code.
Gofmt removes leading and trailing blank lines in doc comments. If all lines in a doc comment begin with the same sequence of spaces and tabs, gofmt removes that prefix.
