---
source_name: "External Linked Documentation"
source_url: "https://go.dev/doc/fuzz"
source_path: "sources/raw/external/go-dev-doc-fuzz-ee5f17aa89.html"
license_ref: ""
---

# Go Fuzzing

## Corpus file format

Corpus files are encoded in a special format. This is the same format for both the seed corpus, and the generated corpus.

Below is an example of a corpus file:

```go
go test fuzz v1
[]byte("hello\\xbd\\xb2=\\xbc ⌘")
int64(572293)

```

The first line is used to inform the fuzzing engine of the file’s encoding version. Although no future versions of the encoding format are currently planned, the design must support this possibility.

Each of the lines following are the values that make up the corpus entry, and can be copied directly into Go code if desired.

In the example above, we have a `[]byte` followed by an `int64`. These types must match the fuzzing arguments exactly, in that order. A fuzz target for these types would look like this:

```go
f.Fuzz(func(*testing.T, []byte, int64) {})

```

The easiest way to specify your own seed corpus values is to use the `(*testing.F).Add` method. In the example above, that would look like this:

```go
f.Add([]byte("hello\\xbd\\xb2=\\xbc ⌘"), int64(572293))

```

However, you may have large binary files that you’d prefer not to copy as code into your test, and instead remain as individual seed corpus entries in the testdata/fuzz/{FuzzTestName} directory. The `file2fuzz` <https://pkg.go.dev/golang.org/x/tools/cmd/file2fuzz> tool at golang.org/x/tools/cmd/file2fuzz can be used to convert these binary files to corpus files encoded for `[]byte`.

To use this tool:

```go
$ go install golang.org/x/tools/cmd/file2fuzz@latest
$ file2fuzz -h

```
