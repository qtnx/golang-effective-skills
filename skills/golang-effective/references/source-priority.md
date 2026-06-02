# Source Priority

Use this precedence when guidance conflicts:

1. User request and repository-specific style.
2. Go compiler, `gofmt`, `go test`, `go vet`, race detector, and project tooling.
3. Go language spec and current Go docs.
4. Effective Go as baseline idiom.
5. Google Go Style Guide decisions for normative style questions.
6. Uber Go Style Guide for pragmatic service/application code conventions.
7. Local consistency in the touched package.

Effective Go remains useful for core idiom, but it is not a complete modern
guide for modules, generics, or current ecosystem conventions.
