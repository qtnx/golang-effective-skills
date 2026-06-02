---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/database/sql"
source_path: "sources/raw/external/pkg-go-dev-database-sql-21734c2f8a.html"
license_ref: ""
---

-  type Tx
-
-  func (tx *Tx) Commit() error
-  func (tx *Tx) Exec(query string, args ...any) (Result, error)
-  func (tx *Tx) ExecContext(ctx context.Context, query string, args ...any) (Result, error)
-  func (tx *Tx) Prepare(query string) (*Stmt, error)
-  func (tx *Tx) PrepareContext(ctx context.Context, query string) (*Stmt, error)
-  func (tx *Tx) Query(query string, args ...any) (*Rows, error)
-  func (tx *Tx) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)
-  func (tx *Tx) QueryRow(query string, args ...any) *Row
-  func (tx *Tx) QueryRowContext(ctx context.Context, query string, args ...any) *Row
-  func (tx *Tx) Rollback() error
-  func (tx *Tx) Stmt(stmt *Stmt) *Stmt
-  func (tx *Tx) StmtContext(ctx context.Context, stmt *Stmt) *Stmt

-  type TxOptions

- Package (OpenDBCLI)
- Package (OpenDBService)
- Conn.ExecContext
- DB.BeginTx
- DB.ExecContext
- DB.PingContext
- DB.Prepare
- DB.Query (MultipleResultSets)
- DB.QueryContext
- DB.QueryRowContext
- Rows
- Stmt
- Stmt.QueryRowContext
- Tx.ExecContext
- Tx.Prepare
- Tx.Rollback

This section is empty.

View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql/sql.go;l=1936>
```go
var ErrConnDone = errors.New("sql: connection is already closed")
```

ErrConnDone is returned by any operation that is performed on a connection that has already been returned to the connection pool.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql/sql.go;l=493>
```go
var ErrNoRows = errors.New("sql: no rows in result set")
```

ErrNoRows is returned by Row.Scan when DB.QueryRow doesn't return a row. In such a case, QueryRow returns a placeholder *Row value that defers this error until a Scan.
  View Source <https://cs.opensource.google/go/go/+/go1.26.3:src/database/sql/sql.go;l=2230>
```go
var ErrTxDone = errors.New("sql: transaction has already been committed or rolled back")
```

ErrTxDone is returned by any operation that is performed on a transaction that has already been committed or rolled back.

```go
func Drivers() []string
```

Drivers returns a sorted list of the names of the registered drivers.

```go
func Register(name string, driver driver.Driver)
```

Register makes a database driver available by the provided name. If Register is called twice with the same name or if driver is nil, it panics.

```go
type ColumnType struct {
	// contains filtered or unexported fields
}
```

ColumnType contains the name and type of a column.

```go
func (ci *ColumnType) DatabaseTypeName() string
```

DatabaseTypeName returns the database system name of the column type. If an empty string is returned, then the driver type name is not supported. Consult your driver documentation for a list of driver data types. ColumnType.Length specifiers are not included. Common type names include "VARCHAR", "TEXT", "NVARCHAR", "DECIMAL", "BOOL", "INT", and "BIGINT".

```go
func (ci *ColumnType) DecimalSize() (precision, scale int64, ok bool)
```

DecimalSize returns the scale and precision of a decimal type. If not applicable or if not supported ok is false.

```go
func (ci *ColumnType) Length() (length int64, ok bool)
```

Length returns the column type length for variable length column types such as text and binary field types. If the type length is unbounded the value will be math.MaxInt64 (any database limits will still apply). If the column type is not variable length, such as an int, or if not supported by the driver ok is false.

```go
func (ci *ColumnType) Name() string
```

Name returns the name or alias of the column.

```go
func (ci *ColumnType) Nullable() (nullable, ok bool)
```

Nullable reports whether the column may be null. If a driver does not support this property ok will be false.

```go
func (ci *ColumnType) ScanType() reflect.Type
```

ScanType returns a Go type suitable for scanning into using Rows.Scan. If a driver does not support this property ScanType will return the type of an empty interface.

```go
type Conn struct {
	// contains filtered or unexported fields
}
```

Conn represents a single database connection rather than a pool of database connections. Prefer running queries from DB unless there is a specific need for a continuous single database connection.

A Conn must call Conn.Close to return the connection to the database pool and may do so concurrently with a running query.

After a call to Conn.Close, all operations on the connection fail with ErrConnDone.

```go
func (c *Conn) BeginTx(ctx context.Context, opts *TxOptions) (*Tx, error)
```

BeginTx starts a transaction.

The provided context is used until the transaction is committed or rolled back. If the context is canceled, the sql package will roll back the transaction. Tx.Commit will return an error if the context provided to BeginTx is canceled.

The provided TxOptions is optional and may be nil if defaults should be used. If a non-default isolation level is used that the driver doesn't support, an error will be returned.

```go
func (c *Conn) Close() error
```

Close returns the connection to the connection pool. All operations after a Close will return with ErrConnDone. Close is safe to call concurrently with other operations and will block until all other operations finish. It may be useful to first cancel any used context and then call close directly after.

```go
func (c *Conn) ExecContext(ctx context.Context, query string, args ...any) (Result, error)
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
	// A *DB is a pool of connections. Call Conn to reserve a connection for
	// exclusive use.
	conn, err := db.Conn(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close() // Return the connection to the pool.
	id := 41
	result, err := conn.ExecContext(ctx, `UPDATE balances SET balance = balance + 10 WHERE user_id = ?;`, id)
	if err != nil {
		log.Fatal(err)
	}
	rows, err := result.RowsAffected()
	if err != nil {
		log.Fatal(err)
	}
	if rows != 1 {
		log.Fatalf("expected single row affected, got %d rows affected", rows)
	}
}

```

```go
Output:

```

Share Format Run

```go
func (c *Conn) PingContext(ctx context.Context) error
```

PingContext verifies the connection to the database is still alive.

```go
func (c *Conn) PrepareContext(ctx context.Context, query string) (*Stmt, error)
```

PrepareContext creates a prepared statement for later queries or executions. Multiple queries or executions may be run concurrently from the returned statement. The caller must call the statement's *Stmt.Close method when the statement is no longer needed.

The provided context is used for the preparation of the statement, not for the execution of the statement.

```go
func (c *Conn) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)
```

QueryContext executes a query that returns rows, typically a SELECT. The args are for any placeholder parameters in the query.

```go
func (c *Conn) QueryRowContext(ctx context.Context, query string, args ...any) *Row
```

QueryRowContext executes a query that is expected to return at most one row. QueryRowContext always returns a non-nil value. Errors are deferred until the *Row.Scan method is called. If the query selects no rows, the *Row.Scan will return ErrNoRows. Otherwise, the *Row.Scan scans the first selected row and discards the rest.

```go
func (c *Conn) Raw(f func(driverConn any) error) (err error)
```

Raw executes f exposing the underlying driver connection for the duration of f. The driverConn must not be used outside of f.

Once f returns and err is not driver.ErrBadConn, the Conn will continue to be usable until Conn.Close is called.

```go
type DB struct {
	// contains filtered or unexported fields
}
```

DB is a database handle representing a pool of zero or more underlying connections. It's safe for concurrent use by multiple goroutines.

The sql package creates and frees connections automatically; it also maintains a free pool of idle connections. If the database has a concept of per-connection state, such state can be reliably observed within a transaction (Tx) or connection (Conn). Once DB.Begin is called, the returned Tx is bound to a single connection. Once Tx.Commit or Tx.Rollback is called on the transaction, that transaction's connection is returned to DB's idle connection pool. The pool size can be controlled with DB.SetMaxIdleConns.

```go
func Open(driverName, dataSourceName string) (*DB, error)
```

Open opens a database specified by its database driver name and a driver-specific data source name, usually consisting of at least a database name and connection information.

Most users will open a database via a driver-specific connection helper function that returns a *DB. No database drivers are included in the Go standard library. See https://golang.org/s/sqldrivers <https://golang.org/s/sqldrivers> for a list of third-party drivers.

Open may just validate its arguments without creating a connection to the database. To verify that the data source name is valid, call DB.Ping.

The returned DB is safe for concurrent use by multiple goroutines and maintains its own pool of idle connections. Thus, the Open function should be called just once. It is rarely necessary to close a DB.

```go
func OpenDB(c driver.Connector) *DB
```

OpenDB opens a database using a driver.Connector, allowing drivers to bypass a string based data source name.

Most users will open a database via a driver-specific connection helper function that returns a *DB. No database drivers are included in the Go standard library. See https://golang.org/s/sqldrivers <https://golang.org/s/sqldrivers> for a list of third-party drivers.

OpenDB may just validate its arguments without creating a connection to the database. To verify that the data source name is valid, call DB.Ping.

The returned DB is safe for concurrent use by multiple goroutines and maintains its own pool of idle connections. Thus, the OpenDB function should be called just once. It is rarely necessary to close a DB.

```go
func (db *DB) Begin() (*Tx, error)
```

Begin starts a transaction. The default isolation level is dependent on the driver.

Begin uses context.Background internally; to specify the context, use DB.BeginTx.

```go
func (db *DB) BeginTx(ctx context.Context, opts *TxOptions) (*Tx, error)
```

BeginTx starts a transaction.
