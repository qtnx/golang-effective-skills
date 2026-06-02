---
source_name: "Google Go Style Guide"
source_url: "https://google.github.io/styleguide/go/"
source_path: "sources/raw/google-go-styleguide/decisions.md"
license_ref: "sources/licenses/google-styleguide-LICENSE.txt"
---

### Conditionals and loops

An `if` statement should not be line broken; multi-line `if` clauses can lead to
[indentation confusion](#indentation-confusion).

```go
// Bad:
// The second if statement is aligned with the code within the if block, causing
// indentation confusion.
if db.CurrentStatusIs(db.InTransaction) &&
    db.ValuesEqual(db.TransactionKey(), row.Key()) {
    return db.Errorf(db.TransactionError, "query failed: row (%v): key does not match transaction key", row)
}
```

If the short-circuit behavior is not required, the boolean operands can be
extracted directly:

```go
// Good:
inTransaction := db.CurrentStatusIs(db.InTransaction)
keysMatch := db.ValuesEqual(db.TransactionKey(), row.Key())
if inTransaction && keysMatch {
    return db.Error(db.TransactionError, "query failed: row (%v): key does not match transaction key", row)
}
```

There may also be other locals that can be extracted, especially if the
conditional is already repetitive:

```go
// Good:
uid := user.GetUniqueUserID()
if db.UserIsAdmin(uid) || db.UserHasPermission(uid, perms.ViewServerConfig) || db.UserHasPermission(uid, perms.CreateGroup) {
    // ...
}
```

```go
// Bad:
if db.UserIsAdmin(user.GetUniqueUserID()) || db.UserHasPermission(user.GetUniqueUserID(), perms.ViewServerConfig) || db.UserHasPermission(user.GetUniqueUserID(), perms.CreateGroup) {
    // ...
}
```

`if` statements that contain closures or multi-line struct literals should
ensure that the [braces match](#literal-matching-braces) to avoid
[indentation confusion](#indentation-confusion).

```go
// Good:
if err := db.RunInTransaction(func(tx *db.TX) error {
    return tx.Execute(userUpdate, x, y, z)
}); err != nil {
    return fmt.Errorf("user update failed: %s", err)
}
```

```go
// Good:
if _, err := client.Update(ctx, &upb.UserUpdateRequest{
    ID:   userID,
    User: user,
}); err != nil {
    return fmt.Errorf("user update failed: %s", err)
}
```

Similarly, don't try inserting artificial linebreaks into `for` statements. You
can always let the line simply be long if there is no elegant way to refactor
it:

```go
// Good:
for i, max := 0, collection.Size(); i < max && !collection.HasPendingWriters(); i++ {
    // ...
}
```

Often, though, there is:

```go
// Good:
for i, max := 0, collection.Size(); i < max; i++ {
    if collection.HasPendingWriters() {
        break
    }
    // ...
}
```

`switch` and `case` statements should also remain on a single line.

```go
// Good:
switch good := db.TransactionStatus(); good {
case db.TransactionStarting, db.TransactionActive, db.TransactionWaiting:
    // ...
case db.TransactionCommitted, db.NoTransaction:
    // ...
default:
    // ...
}
```

```go
// Bad:
switch bad := db.TransactionStatus(); bad {
case db.TransactionStarting,
    db.TransactionActive,
    db.TransactionWaiting:
    // ...
case db.TransactionCommitted,
    db.NoTransaction:
    // ...
default:
    // ...
}
```

If the line is excessively long, indent all cases and separate them with a blank
line to avoid [indentation confusion](#indentation-confusion):

```go
// Good:
switch db.TransactionStatus() {
case
    db.TransactionStarting,
    db.TransactionActive,
    db.TransactionWaiting,
    db.TransactionCommitted:

    // ...
case db.NoTransaction:
    // ...
default:
    // ...
}
```

In conditionals comparing a variable to a constant, place the variable value on
the left hand side of the equality operator:

```go
// Good:
if result == "foo" {
  // ...
}
```

Instead of the less clear phrasing where the constant comes first
(["Yoda style conditionals"](https://en.wikipedia.org/wiki/Yoda_conditions)):

```go
// Bad:
if "foo" == result {
  // ...
}
```

<a id="copying"></a>
