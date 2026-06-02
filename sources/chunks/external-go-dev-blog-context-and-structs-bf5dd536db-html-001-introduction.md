---
source_name: "External Linked Documentation"
source_url: "https://go.dev/blog/context-and-structs"
source_path: "sources/raw/external/go-dev-blog-context-and-structs-bf5dd536db.html"
license_ref: ""
---

# The Go Blog

Contexts and structs - The Go Programming Language
# The Go Blog
# Contexts and structs
 Jean Barkhuysen, Matt T. Proud
 24 February 2021
## Introduction

In many Go APIs, especially modern ones, the first argument to functions and methods is often `context.Context`. Context provides a means of transmitting deadlines, caller cancellations, and other request-scoped values across API boundaries and between processes. It is often used when a library interacts — directly or transitively — with remote servers, such as databases, APIs, and the like.

The documentation for context states:

Contexts should not be stored inside a struct type, but instead passed to each function that needs it.

This article expands on that advice with reasons and examples describing why it’s important to pass Context rather than store it in another type. It also highlights a rare case where storing Context in a struct type may make sense, and how to do so safely.
