# Examples

Use these as calibration snippets before editing or reviewing style.

## Comment Repeats Code

```go
// total returns total.
func total(items []int) int { ... }
```

Prefer a comment only when it adds contract, invariant, or rationale:

```go
// total ignores negative items because refunds are handled separately.
func total(items []int) int { ... }
```

## Flatten Control Flow

```go
if count == 0 {
	return "none"
} else {
	return "some"
}
```

```go
if count == 0 {
	return "none"
}
return "some"
```

## Name Intermediate Values

```go
return strings.TrimSpace(strings.ToLower(input)) == "enabled"
```

```go
normalized := strings.ToLower(strings.TrimSpace(input))
return normalized == "enabled"
```
