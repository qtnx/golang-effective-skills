---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/database/sql"
source_path: "sources/raw/external/pkg-go-dev-database-sql-21734c2f8a.html"
license_ref: ""
---

```go
func (tx *Tx) Exec(query string, args ...any) (Result, error)
```

Exec executes a query that doesn't return rows. For example: an INSERT and UPDATE.

Exec uses context.Background internally; to specify the context, use Tx.ExecContext.

```go
func (tx *Tx) ExecContext(ctx context.Context, query string, args ...any) (Result, error)
```

ExecContext executes a query that doesn't return rows. For example: an INSERT and UPDATE.

```go

package main

import (
	"context"
	"database/sql"
	"log"
)

var (
	ctx context.Context
	db  *sql.DB
)

func main() {
	tx, err := db.BeginTx(ctx, &sql.TxOptions{Isolation: sql.LevelSerializable})
	if err != nil {
		log.Fatal(err)
	}
	id := 37
	_, execErr := tx.ExecContext(ctx, "UPDATE users SET status = ? WHERE id = ?", "paid", id)
	if execErr != nil {
		if rollbackErr := tx.Rollback(); rollbackErr != nil {
			log.Fatalf("update failed: %v, unable to rollback: %v\n", execErr, rollbackErr)
		}
		log.Fatalf("update failed: %v", execErr)
	}
	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (tx *Tx) Prepare(query string) (*Stmt, error)
```

Prepare creates a prepared statement for use within a transaction.

The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.

To use an existing prepared statement on this transaction, see Tx.Stmt.

Prepare uses context.Background internally; to specify the context, use Tx.PrepareContext.

```go

package main

import (
	"context"
	"database/sql"
	"log"
)

var db *sql.DB

func main() {
	projects := []struct {
		mascot  string
		release int
	}{
		{"tux", 1991},
		{"duke", 1996},
		{"gopher", 2009},
		{"moby dock", 2013},
	}

tx, err := db.Begin()
	if err != nil {
		log.Fatal(err)
	}
	defer tx.Rollback() // The rollback will be ignored if the tx has been committed later in the function.

stmt, err := tx.Prepare("INSERT INTO projects(id, mascot, release, category) VALUES( ?, ?, ?, ? )")
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close() // Prepared statements take up server resources and should be closed after use.

for id, project := range projects {
		if _, err := stmt.Exec(id+1, project.mascot, project.release, "open source"); err != nil {
			log.Fatal(err)
		}
	}
	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (tx *Tx) PrepareContext(ctx context.Context, query string) (*Stmt, error)
```

PrepareContext creates a prepared statement for use within a transaction.

The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.

To use an existing prepared statement on this transaction, see Tx.Stmt.

The provided context will be used for the preparation of the context, not for the execution of the returned statement. The returned statement will run in the transaction context.

```go
func (tx *Tx) Query(query string, args ...any) (*Rows, error)
```

Query executes a query that returns rows, typically a SELECT.

Query uses context.Background internally; to specify the context, use Tx.QueryContext.

```go
func (tx *Tx) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)
```

QueryContext executes a query that returns rows, typically a SELECT.

```go
func (tx *Tx) QueryRow(query string, args ...any) *Row
```

QueryRow executes a query that is expected to return at most one row. QueryRow always returns a non-nil value. Errors are deferred until Row's Scan method is called. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, the *Row.Scan scans the first selected row and discards the rest.

QueryRow uses context.Background internally; to specify the context, use Tx.QueryRowContext.

```go
func (tx *Tx) QueryRowContext(ctx context.Context, query string, args ...any) *Row
```

QueryRowContext executes a query that is expected to return at most one row. QueryRowContext always returns a non-nil value. Errors are deferred until Row's Scan method is called. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, the *Row.Scan scans the first selected row and discards the rest.

```go
func (tx *Tx) Rollback() error
```

Rollback aborts the transaction.

```go

package main

import (
	"context"
	"database/sql"
	"log"
)

var (
	ctx context.Context
	db  *sql.DB
)

func main() {
	tx, err := db.BeginTx(ctx, &sql.TxOptions{Isolation: sql.LevelSerializable})
	if err != nil {
		log.Fatal(err)
	}
	id := 53
	_, err = tx.ExecContext(ctx, "UPDATE drivers SET status = ? WHERE id = ?;", "assigned", id)
	if err != nil {
		if rollbackErr := tx.Rollback(); rollbackErr != nil {
			log.Fatalf("update drivers: unable to rollback: %v", rollbackErr)
		}
		log.Fatal(err)
	}
	_, err = tx.ExecContext(ctx, "UPDATE pickups SET driver_id = $1;", id)
	if err != nil {
		if rollbackErr := tx.Rollback(); rollbackErr != nil {
			log.Fatalf("update failed: %v, unable to back: %v", err, rollbackErr)
		}
		log.Fatal(err)
	}
	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (tx *Tx) Stmt(stmt *Stmt) *Stmt
```

Stmt returns a transaction-specific prepared statement from an existing statement.

Example:

```go
updateMoney, err := db.Prepare("UPDATE balance SET money=money+? WHERE id=?")
...
tx, err := db.Begin()
...
res, err := tx.Stmt(updateMoney).Exec(123.45, 98293203)

```

The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.

Stmt uses context.Background internally; to specify the context, use Tx.StmtContext.

```go
func (tx *Tx) StmtContext(ctx context.Context, stmt *Stmt) *Stmt
```

StmtContext returns a transaction-specific prepared statement from an existing statement.

Example:

```go
updateMoney, err := db.Prepare("UPDATE balance SET money=money+? WHERE id=?")
...
tx, err := db.Begin()
...
res, err := tx.StmtContext(ctx, updateMoney).Exec(123.45, 98293203)

```

The provided context is used for the preparation of the statement, not for the execution of the statement.

The returned statement operates within the transaction and will be closed when the transaction has been committed or rolled back.

```go
type TxOptions struct {
	// Isolation is the transaction isolation level.
	// If zero, the driver or database's default level is used.
	Isolation IsolationLevel
	ReadOnly  bool
}
```

TxOptions holds the transaction options to be used in DB.BeginTx.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql>

- convert.go <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql/convert.go>
- ctxutil.go <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql/ctxutil.go>
- sql.go <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql/sql.go>

##   Directories ¶
    Show internal   Expand all

driver
 Package driver defines interfaces to be implemented by database drivers as used by package sql.

Package driver defines interfaces to be implemented by database drivers as used by package sql.

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
