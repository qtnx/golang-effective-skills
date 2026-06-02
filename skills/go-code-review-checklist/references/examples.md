# Examples

Use these to calibrate severity and finding shape.

## Correctness Finding

```go
for _, id := range ids {
	go func() {
		user, err := store.Get(id)
		...
	}()
}
return names, nil
```

Review finding:

```text
- [P1] path/to/file.go:12 - Function returns before goroutines finish
  The caller can observe an incomplete result because the goroutines append
  after the function has already returned. Wait for the work to finish and
  propagate errors, or make the function synchronous.
```

## Style Finding

```text
- [P2] path/to/file.go:8 - Comment repeats the function name
  The comment does not add behavior or rationale. Replace it with the contract
  callers need, or remove it if the function is unexported and obvious.
```

## Source-Backed Review Flow

1. Classify the finding: style, naming/API, errors/panics, tests, or broader
   correctness.
2. Load the matching task skill.
3. Read that skill's checklist and examples.
4. If the claim depends on published guidance, read the task skill's
   `references/source-map.md` and then the relevant `sources/chunks/...` files.
