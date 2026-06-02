---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/database/sql"
source_path: "sources/raw/external/pkg-go-dev-database-sql-21734c2f8a.html"
license_ref: ""
---

names := make([]string, 0)
	for rows.Next() {
		var name string
		if err := rows.Scan(&name); err != nil {
			log.Fatal(err)
		}
		names = append(names, name)
	}
	// Check for errors from iterating over rows.
	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
	log.Printf("%s are %d years old", strings.Join(names, ", "), age)
}

```

```go
Output:

```

Share Format Run

```go
func (rs *Rows) Close() error
```

Close closes the Rows, preventing further enumeration. If Rows.Next is called and returns false and there are no further result sets, the Rows are closed automatically and it will suffice to check the result of Rows.Err. Close is idempotent and does not affect the result of Rows.Err.

```go
func (rs *Rows) ColumnTypes() ([]*ColumnType, error)
```

ColumnTypes returns column information such as column type, length, and nullable. Some information may not be available from some drivers.

```go
func (rs *Rows) Columns() ([]string, error)
```

Columns returns the column names. Columns returns an error if the rows are closed.

```go
func (rs *Rows) Err() error
```

Err returns the error, if any, that was encountered during iteration. Err may be called after an explicit or implicit Rows.Close.

```go
func (rs *Rows) Next() bool
```

Next prepares the next result row for reading with the Rows.Scan method. It returns true on success, or false if there is no next result row or an error happened while preparing it. Rows.Err should be consulted to distinguish between the two cases.

Every call to Rows.Scan, even the first one, must be preceded by a call to Rows.Next.

```go
func (rs *Rows) NextResultSet() bool
```

NextResultSet prepares the next result set for reading. It reports whether there is further result sets, or false if there is no further result set or if there is an error advancing to it. The Rows.Err method should be consulted to distinguish between the two cases.

After calling NextResultSet, the Rows.Next method should always be called before scanning. If there are further result sets they may not have rows in the result set.

```go
func (rs *Rows) Scan(dest ...any) error
```

Scan copies the columns in the current row into the values pointed at by dest. The number of values in dest must be the same as the number of columns in Rows.

Scan converts columns read from the database into the following common Go types and special types provided by the sql package:

```go
*string
*[]byte
*int, *int8, *int16, *int32, *int64
*uint, *uint8, *uint16, *uint32, *uint64
*bool
*float32, *float64
*interface{}
*RawBytes
*Rows (cursor value)
any type implementing Scanner (see Scanner docs)

```

In the most simple case, if the type of the value from the source column is an integer, bool or string type T and dest is of type *T, Scan simply assigns the value through the pointer.

Scan also converts between string and numeric types, as long as no information would be lost. While Scan stringifies all numbers scanned from numeric database columns into *string, scans into numeric types are checked for overflow. For example, a float64 with value 300 or a string with value "300" can scan into a uint16, but not into a uint8, though float64(255) or "255" can scan into a uint8. One exception is that scans of some float64 numbers to strings may lose information when stringifying. In general, scan floating point columns into *float64.

If a dest argument has type *[]byte, Scan saves in that argument a copy of the corresponding data. The copy is owned by the caller and can be modified and held indefinitely. The copy can be avoided by using an argument of type *RawBytes instead; see the documentation for RawBytes for restrictions on its use.

If an argument has type *interface{}, Scan copies the value provided by the underlying driver without conversion. When scanning from a source value of type []byte to *interface{}, a copy of the slice is made and the caller owns the result.

Source values of type time.Time may be scanned into values of type *time.Time, *interface{}, *string, or *[]byte. When converting to the latter two, time.RFC3339Nano is used.

Source values of type bool may be scanned into types *bool, *interface{}, *string, *[]byte, or *RawBytes.

For scanning into *bool, the source may be true, false, 1, 0, or string inputs parseable by strconv.ParseBool.

Scan can also convert a cursor returned from a query, such as "select cursor(select * from my_table) from dual", into a *Rows value that can itself be scanned from. The parent select query will close any cursor *Rows if the parent *Rows is closed.

If any of the first arguments implementing Scanner returns an error, that error will be wrapped in the returned error.

```go
type Scanner interface {
	// Scan assigns a value from a database driver.
	//
	// The src value will be of one of the following types:
	//
	//    int64
	//    float64
	//    bool
	//    []byte
	//    string
	//    time.Time
	//    nil - for NULL values
	//
	// An error should be returned if the value cannot be stored
	// without loss of information.
	//
	// Reference types such as []byte are only valid until the next call to Scan
	// and should not be retained. Their underlying memory is owned by the driver.
	// If retention is necessary, copy their values before the next call to Scan.
	Scan(src any) error
}
```

Scanner is an interface used by Rows.Scan.

```go
type Stmt struct {
	// contains filtered or unexported fields
}
```

Stmt is a prepared statement. A Stmt is safe for concurrent use by multiple goroutines.

If a Stmt is prepared on a Tx or Conn, it will be bound to a single underlying connection forever. If the Tx or Conn closes, the Stmt will become unusable and all operations will return an error. If a Stmt is prepared on a DB, it will remain usable for the lifetime of the DB. When the Stmt needs to execute on a new underlying connection, it will prepare itself on the new connection automatically.

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
	// In normal use, create one Stmt when your process starts.
	stmt, err := db.PrepareContext(ctx, "SELECT username FROM users WHERE id = ?")
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close()

// Then reuse it each time you need to issue the query.
	id := 43
	var username string
	err = stmt.QueryRowContext(ctx, id).Scan(&username)
	switch {
	case err == sql.ErrNoRows:
		log.Fatalf("no user with id %d", id)
	case err != nil:
		log.Fatal(err)
	default:
		log.Printf("username is %s\n", username)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (s *Stmt) Close() error
```

Close closes the statement.

```go
func (s *Stmt) Exec(args ...any) (Result, error)
```

Exec executes a prepared statement with the given arguments and returns a Result summarizing the effect of the statement.

Exec uses context.Background internally; to specify the context, use Stmt.ExecContext.

```go
func (s *Stmt) ExecContext(ctx context.Context, args ...any) (Result, error)
```

ExecContext executes a prepared statement with the given arguments and returns a Result summarizing the effect of the statement.

```go
func (s *Stmt) Query(args ...any) (*Rows, error)
```

Query executes a prepared query statement with the given arguments and returns the query results as a *Rows.

Query uses context.Background internally; to specify the context, use Stmt.QueryContext.

```go
func (s *Stmt) QueryContext(ctx context.Context, args ...any) (*Rows, error)
```

QueryContext executes a prepared query statement with the given arguments and returns the query results as a *Rows.

```go
func (s *Stmt) QueryRow(args ...any) *Row
```

QueryRow executes a prepared query statement with the given arguments. If an error occurs during the execution of the statement, that error will be returned by a call to Scan on the returned *Row, which is always non-nil. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, the *Row.Scan scans the first selected row and discards the rest.

Example usage:

```go
var name string
err := nameByUseridStmt.QueryRow(id).Scan(&name)

```

QueryRow uses context.Background internally; to specify the context, use Stmt.QueryRowContext.

```go
func (s *Stmt) QueryRowContext(ctx context.Context, args ...any) *Row
```

QueryRowContext executes a prepared query statement with the given arguments. If an error occurs during the execution of the statement, that error will be returned by a call to Scan on the returned *Row, which is always non-nil. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, the *Row.Scan scans the first selected row and discards the rest.

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
	// In normal use, create one Stmt when your process starts.
	stmt, err := db.PrepareContext(ctx, "SELECT username FROM users WHERE id = ?")
	if err != nil {
		log.Fatal(err)
	}
	defer stmt.Close()

// Then reuse it each time you need to issue the query.
	id := 43
	var username string
	err = stmt.QueryRowContext(ctx, id).Scan(&username)
	switch {
	case err == sql.ErrNoRows:
		log.Fatalf("no user with id %d", id)
	case err != nil:
		log.Fatal(err)
	default:
		log.Printf("username is %s\n", username)
	}
}

```

```go
Output:

```

Share Format Run

```go
type Tx struct {
	// contains filtered or unexported fields
}
```

Tx is an in-progress database transaction.

A transaction must end with a call to Tx.Commit or Tx.Rollback.

After a call to Tx.Commit or Tx.Rollback, all operations on the transaction fail with ErrTxDone.

The statements prepared for a transaction by calling the transaction's Tx.Prepare or Tx.Stmt methods are closed by the call to Tx.Commit or Tx.Rollback.

```go
func (tx *Tx) Commit() error
```

Commit commits the transaction.
