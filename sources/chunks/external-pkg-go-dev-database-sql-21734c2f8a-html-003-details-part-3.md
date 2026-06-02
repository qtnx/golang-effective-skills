---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/database/sql"
source_path: "sources/raw/external/pkg-go-dev-database-sql-21734c2f8a.html"
license_ref: ""
---

The provided context is used until the transaction is committed or rolled back. If the context is canceled, the sql package will roll back the transaction. Tx.Commit will return an error if the context provided to BeginTx is canceled.

The provided TxOptions is optional and may be nil if defaults should be used. If a non-default isolation level is used that the driver doesn't support, an error will be returned.

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
	_, execErr := tx.Exec(`UPDATE users SET status = ? WHERE id = ?`, "paid", id)
	if execErr != nil {
		_ = tx.Rollback()
		log.Fatal(execErr)
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
func (db *DB) Close() error
```

Close closes the database and prevents new queries from starting. Close then waits for all queries that have started processing on the server to finish.

It is rare to Close a DB, as the DB handle is meant to be long-lived and shared between many goroutines.

```go
func (db *DB) Conn(ctx context.Context) (*Conn, error)
```

Conn returns a single connection by either opening a new connection or returning an existing connection from the connection pool. Conn will block until either a connection is returned or ctx is canceled. Queries run on the same Conn will be run in the same database session.

Every Conn must be returned to the database pool after use by calling Conn.Close.

```go
func (db *DB) Driver() driver.Driver
```

Driver returns the database's underlying driver.

```go
func (db *DB) Exec(query string, args ...any) (Result, error)
```

Exec executes a query without returning any rows. The args are for any placeholder parameters in the query.

Exec uses context.Background internally; to specify the context, use DB.ExecContext.

```go
func (db *DB) ExecContext(ctx context.Context, query string, args ...any) (Result, error)
```

ExecContext executes a query without returning any rows. The args are for any placeholder parameters in the query.

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
	id := 47
	result, err := db.ExecContext(ctx, "UPDATE balances SET balance = balance + 10 WHERE user_id = ?", id)
	if err != nil {
		log.Fatal(err)
	}
	rows, err := result.RowsAffected()
	if err != nil {
		log.Fatal(err)
	}
	if rows != 1 {
		log.Fatalf("expected to affect 1 row, affected %d", rows)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (db *DB) Ping() error
```

Ping verifies a connection to the database is still alive, establishing a connection if necessary.

Ping uses context.Background internally; to specify the context, use DB.PingContext.

```go
func (db *DB) PingContext(ctx context.Context) error
```

PingContext verifies a connection to the database is still alive, establishing a connection if necessary.

```go

package main

import (
	"context"
	"database/sql"
	"log"
	"time"
)

var (
	ctx context.Context
	db  *sql.DB
)

func main() {
	// Ping and PingContext may be used to determine if communication with
	// the database server is still possible.
	//
	// When used in a command line application Ping may be used to establish
	// that further queries are possible; that the provided DSN is valid.
	//
	// When used in long running service Ping may be part of the health
	// checking system.

ctx, cancel := context.WithTimeout(ctx, 1*time.Second)
	defer cancel()

status := "up"
	if err := db.PingContext(ctx); err != nil {
		status = "down"
	}
	log.Println(status)
}

```

```go
Output:

```

Share Format Run

```go
func (db *DB) Prepare(query string) (*Stmt, error)
```

Prepare creates a prepared statement for later queries or executions. Multiple queries or executions may be run concurrently from the returned statement. The caller must call the statement's *Stmt.Close method when the statement is no longer needed.

Prepare uses context.Background internally; to specify the context, use DB.PrepareContext.

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

stmt, err := db.Prepare("INSERT INTO projects(id, mascot, release, category) VALUES( ?, ?, ?, ? )")
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close() // Prepared statements take up server resources and should be closed after use.

for id, project := range projects {
		if _, err := stmt.Exec(id+1, project.mascot, project.release, "open source"); err != nil {
			log.Fatal(err)
		}
	}
}

```

```go
Output:

```

Share Format Run

```go
func (db *DB) PrepareContext(ctx context.Context, query string) (*Stmt, error)
```

PrepareContext creates a prepared statement for later queries or executions. Multiple queries or executions may be run concurrently from the returned statement. The caller must call the statement's *Stmt.Close method when the statement is no longer needed.

The provided context is used for the preparation of the statement, not for the execution of the statement.

```go
func (db *DB) Query(query string, args ...any) (*Rows, error)
```

Query executes a query that returns rows, typically a SELECT. The args are for any placeholder parameters in the query.

Query uses context.Background internally; to specify the context, use DB.QueryContext.

```go

package main

import (
	"context"
	"database/sql"
	"log"
)

var db *sql.DB

func main() {
	age := 27
	q := `
create temp table uid (id bigint); -- Create temp table for queries.
insert into uid
select id from users where age < ?; -- Populate temp table.

-- First result set.
select
	users.id, name
from
	users
	join uid on users.id = uid.id
;

-- Second result set.
select
	ur.user, ur.role
from
	user_roles as ur
	join uid on uid.id = ur.user
;
	`
	rows, err := db.Query(q, age)
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

for rows.Next() {
		var (
			id   int64
			name string
		)
		if err := rows.Scan(&id, &name); err != nil {
			log.Fatal(err)
		}
		log.Printf("id %d name is %s\n", id, name)
	}
	if !rows.NextResultSet() {
		log.Fatalf("expected more result sets: %v", rows.Err())
	}
	var roleMap = map[int64]string{
		1: "user",
		2: "admin",
		3: "gopher",
	}
	for rows.Next() {
		var (
			id   int64
			role int64
		)
		if err := rows.Scan(&id, &role); err != nil {
			log.Fatal(err)
		}
		log.Printf("id %d has role %s\n", id, roleMap[role])
	}
	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (db *DB) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)
```

QueryContext executes a query that returns rows, typically a SELECT. The args are for any placeholder parameters in the query.

```go

package main

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"strings"
)

var (
	ctx context.Context
	db  *sql.DB
)

func main() {
	age := 27
	rows, err := db.QueryContext(ctx, "SELECT name FROM users WHERE age=?", age)
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()
	names := make([]string, 0)

for rows.Next() {
		var name string
		if err := rows.Scan(&name); err != nil {
			// Check for a scan error.
			// Query rows will be closed with defer.
			log.Fatal(err)
		}
		names = append(names, name)
	}
	// If the database is being written to ensure to check for Close
	// errors that may be returned from the driver. The query may
	// encounter an auto-commit error and be forced to rollback changes.
	rerr := rows.Close()
	if rerr != nil {
		log.Fatal(rerr)
	}

// Rows.Err will report the last error encountered by Rows.Scan.
	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s are %d years old", strings.Join(names, ", "), age)
}

```

```go
Output:

```

Share Format Run

```go
func (db *DB) QueryRow(query string, args ...any) *Row
```

QueryRow executes a query that is expected to return at most one row. QueryRow always returns a non-nil value. Errors are deferred until Row's Scan method is called. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, *Row.Scan scans the first selected row and discards the rest.

QueryRow uses context.Background internally; to specify the context, use DB.QueryRowContext.

```go
func (db *DB) QueryRowContext(ctx context.Context, query string, args ...any) *Row
```

QueryRowContext executes a query that is expected to return at most one row. QueryRowContext always returns a non-nil value. Errors are deferred until Row's Scan method is called. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, *Row.Scan scans the first selected row and discards the rest.

```go

package main

import (
	"context"
	"database/sql"
	"log"
	"time"
)

var (
	ctx context.Context
	db  *sql.DB
)

func main() {
	id := 123
	var username string
	var created time.Time
	err := db.QueryRowContext(ctx, "SELECT username, created_at FROM users WHERE id=?", id).Scan(&username, &created)
	switch {
	case err == sql.ErrNoRows:
		log.Printf("no user with id %d\n", id)
	case err != nil:
		log.Fatalf("query error: %v\n", err)
	default:
		log.Printf("username is %q, account created on %s\n", username, created)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (db *DB) SetConnMaxIdleTime(d time.Duration)
```

SetConnMaxIdleTime sets the maximum amount of time a connection may be idle.

Expired connections may be closed lazily before reuse.

If d <= 0, connections are not closed due to a connection's idle time.

```go
func (db *DB) SetConnMaxLifetime(d time.Duration)
```

SetConnMaxLifetime sets the maximum amount of time a connection may be reused.

Expired connections may be closed lazily before reuse.

If d <= 0, connections are not closed due to a connection's age.

```go
func (db *DB) SetMaxIdleConns(n int)
```

SetMaxIdleConns sets the maximum number of connections in the idle connection pool.

If MaxOpenConns is greater than 0 but less than the new MaxIdleConns, then the new MaxIdleConns will be reduced to match the MaxOpenConns limit.
