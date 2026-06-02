---
source_name: "Effective Go"
source_url: "https://go.dev/doc/effective_go"
source_path: "sources/raw/effective-go/effective_go.html"
license_ref: "sources/licenses/go-LICENSE.txt"
---

# Effective Go

Effective Go - The Go Programming Language
# Effective Go
  **Note:** This document was written for Go's release in 2009 and is not actively updated. While it remains a good guide for using the core language, it does not cover significant changes to the language (generics), ecosystem (modules), or libraries added since. See issue 28782 for context. For a complete list of changes, see the release notes.
## Introduction

 Go is an open-source programming language that focuses on simplicity, reliability, and efficiency, specifically designed to make it easy to build software at scale. Although it borrows ideas from existing languages, it has unusual properties that make effective Go programs different in character from programs written in its relatives. A straightforward translation of a C++ or Java program into Go is unlikely to produce a satisfactory result—Java programs are written in Java, not Go. On the other hand, thinking about the problem from a Go perspective could produce a successful but quite different program. In other words, to write Go well, it's important to understand its properties and idioms. It's also important to know the established conventions for programming in Go, such as naming, formatting, program construction, and so on, so that programs you write will be easy for other Go programmers to understand.

 This document gives tips for writing clear, idiomatic Go code. It augments the language specification, the Tour of Go, and How to Write Go Code, all of which you should read first.

### Examples

 The Go package sources are intended to serve not only as the core library but also as examples of how to use the language. Moreover, many of the packages contain working, self-contained executable examples you can run directly from the go.dev web site, such as this one (if necessary, click on the word "Example" to open it up). If you have a question about how to approach a problem or how something might be implemented, the documentation, code and examples in the library can provide answers, ideas and background.
