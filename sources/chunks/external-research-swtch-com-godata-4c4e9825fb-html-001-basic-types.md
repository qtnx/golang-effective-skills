---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/godata"
source_path: "sources/raw/external/research-swtch-com-godata-4c4e9825fb.html"
license_ref: ""
---

# Go Data Structures   Russ Cox

research!rsc: Go Data Structures
# Go Data Structures   Russ Cox
 November 24, 2009
 _research.swtch.com/godata_
  Posted on Tuesday, November 24, 2009.
When explaining Go to new programmers, I've found that it often helps to explain what Go values look like in memory, to build the right intuition about which operations are expensive and which are not. This post is about basic types, structs, arrays, and slices.
## Basic types

Let's start with some simple examples:

The variable `i` has type `int`, represented in memory as a single 32-bit word. (All these pictures show a 32-bit memory layout; in the current implementations, only the pointer gets bigger on a 64-bit machine—`int` is still 32 bits—though an implementation could choose to use 64 bits instead.)

The variable `j` has type `int32`, because of the explicit conversion. Even though `i` and `j` have the same memory layout, they have different types: the assignment `i = j` is a type error and must be written with an explicit conversion: `i = int(j)`.

The variable `f` has type `float`, which the current implementations represent as a 32-bit floating-point value. It has the same memory footprint as the `int32` but a different internal layout.
