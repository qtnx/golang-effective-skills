# Examples

Use these as calibration snippets before changing error behavior.

## Error Strings

```go
var ErrMissingUser = errors.New("Missing User.")
```

```go
var ErrMissingUser = errors.New("missing user")
```

## Log Once

```go
if err := loadUser(id); err != nil {
	log.Printf("load user: %v", err)
	return fmt.Errorf("load user: %w", err)
}
```

Prefer returning context and logging at the boundary that handles the failure:

```go
if err := loadUser(id); err != nil {
	return fmt.Errorf("load user %q: %w", id, err)
}
```

## Wrap Intentionally

```go
return fmt.Errorf("load config: %w", os.ErrNotExist)
```

Use `%w` only when callers should be able to inspect the wrapped error with
`errors.Is` or `errors.As`.

## Avoid Panic for Runtime Failure

```go
func load(id string) *User {
	user, err := repo.Load(id)
	if err != nil {
		panic(err)
	}
	return user
}
```

```go
func load(id string) (*User, error) {
	user, err := repo.Load(id)
	if err != nil {
		return nil, fmt.Errorf("load user %q: %w", id, err)
	}
	return user, nil
}
```
