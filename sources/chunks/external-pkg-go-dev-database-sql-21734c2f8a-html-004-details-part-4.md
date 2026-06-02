---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/database/sql"
source_path: "sources/raw/external/pkg-go-dev-database-sql-21734c2f8a.html"
license_ref: ""
---

If n <= 0, no idle connections are retained.

The default max idle connections is currently 2. This may change in a future release.

```go
func (db *DB) SetMaxOpenConns(n int)
```

SetMaxOpenConns sets the maximum number of open connections to the database.

If MaxIdleConns is greater than 0 and the new MaxOpenConns is less than MaxIdleConns, then MaxIdleConns will be reduced to match the new MaxOpenConns limit.

If n <= 0, then there is no limit on the number of open connections. The default is 0 (unlimited).

```go
func (db *DB) Stats() DBStats
```

Stats returns database statistics.

```go
type DBStats struct {
	MaxOpenConnections int // Maximum number of open connections to the database.

// Pool Status
	OpenConnections int // The number of established connections both in use and idle.
	InUse           int // The number of connections currently in use.
	Idle            int // The number of idle connections.

// Counters
	WaitCount         int64         // The total number of connections waited for.
	WaitDuration      time.Duration // The total time blocked waiting for a new connection.
	MaxIdleClosed     int64         // The total number of connections closed due to SetMaxIdleConns.
	MaxIdleTimeClosed int64         // The total number of connections closed due to SetConnMaxIdleTime.
	MaxLifetimeClosed int64         // The total number of connections closed due to SetConnMaxLifetime.
}
```

DBStats contains database statistics.

```go
type IsolationLevel int
```

IsolationLevel is the transaction isolation level used in TxOptions.

```go
const (
	LevelDefault IsolationLevel = iota
	LevelReadUncommitted
	LevelReadCommitted
	LevelWriteCommitted
	LevelRepeatableRead
	LevelSnapshot
	LevelSerializable
	LevelLinearizable
)
```

Various isolation levels that drivers may support in DB.BeginTx. If a driver does not support a given isolation level an error may be returned.

See https://en.wikipedia.org/wiki/Isolation_(database_systems)#Isolation_levels <https://en.wikipedia.org/wiki/Isolation_%28database_systems%29#Isolation_levels>.

```go
func (i IsolationLevel) String() string
```

String returns the name of the transaction isolation level.

```go
type NamedArg struct {

// Name is the name of the parameter placeholder.
	//
	// If empty, the ordinal position in the argument list will be
	// used.
	//
	// Name must omit any symbol prefix.
	Name string

// Value is the value of the parameter.
	// It may be assigned the same value types as the query
	// arguments.
	Value any
	// contains filtered or unexported fields
}
```

A NamedArg is a named argument. NamedArg values may be used as arguments to DB.Query or DB.Exec and bind to the corresponding named parameter in the SQL statement.

For a more concise way to create NamedArg values, see the Named function.

```go
func Named(name string, value any) NamedArg
```

Named provides a more concise way to create NamedArg values.

Example usage:

```go
db.ExecContext(ctx, `
    delete from Invoice
    where
        TimeCreated < @end
        and TimeCreated >= @start;`,
    sql.Named("start", startTime),
    sql.Named("end", endTime),
)

```

```go
type Null[T any] struct {
	V     T
	Valid bool
}
```

Null represents a value that may be null. Null implements the Scanner interface so it can be used as a scan destination:

```go
var s Null[string]
err := db.QueryRow("SELECT name FROM foo WHERE id=?", id).Scan(&s)
...
if s.Valid {
   // use s.V
} else {
   // NULL value
}

```

T should be one of the types accepted by driver.Value.

```go
func (n *Null[T]) Scan(value any) error
```

```go
func (n Null[T]) Value() (driver.Value, error)
```

```go
type NullBool struct {
	Bool  bool
	Valid bool // Valid is true if Bool is not NULL
}
```

NullBool represents a bool that may be null. NullBool implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullBool) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullBool) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullByte struct {
	Byte  byte
	Valid bool // Valid is true if Byte is not NULL
}
```

NullByte represents a byte that may be null. NullByte implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullByte) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullByte) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullFloat64 struct {
	Float64 float64
	Valid   bool // Valid is true if Float64 is not NULL
}
```

NullFloat64 represents a float64 that may be null. NullFloat64 implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullFloat64) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullFloat64) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullInt16 struct {
	Int16 int16
	Valid bool // Valid is true if Int16 is not NULL
}
```

NullInt16 represents an int16 that may be null. NullInt16 implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullInt16) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullInt16) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullInt32 struct {
	Int32 int32
	Valid bool // Valid is true if Int32 is not NULL
}
```

NullInt32 represents an int32 that may be null. NullInt32 implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullInt32) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullInt32) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullInt64 struct {
	Int64 int64
	Valid bool // Valid is true if Int64 is not NULL
}
```

NullInt64 represents an int64 that may be null. NullInt64 implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullInt64) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullInt64) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullString struct {
	String string
	Valid  bool // Valid is true if String is not NULL
}
```

NullString represents a string that may be null. NullString implements the Scanner interface so it can be used as a scan destination:

```go
var s NullString
err := db.QueryRow("SELECT name FROM foo WHERE id=?", id).Scan(&s)
...
if s.Valid {
   // use s.String
} else {
   // NULL value
}

```

```go
func (ns *NullString) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (ns NullString) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type NullTime struct {
	Time  time.Time
	Valid bool // Valid is true if Time is not NULL
}
```

NullTime represents a time.Time that may be null. NullTime implements the Scanner interface so it can be used as a scan destination, similar to NullString.

```go
func (n *NullTime) Scan(value any) error
```

Scan implements the Scanner interface.

```go
func (n NullTime) Value() (driver.Value, error)
```

Value implements the driver.Valuer interface.

```go
type Out struct {

// Dest is a pointer to the value that will be set to the result of the
	// stored procedure's OUTPUT parameter.
	Dest any

// In is whether the parameter is an INOUT parameter. If so, the input value to the stored
	// procedure is the dereferenced value of Dest's pointer, which is then replaced with
	// the output value.
	In bool
	// contains filtered or unexported fields
}
```

Out may be used to retrieve OUTPUT value parameters from stored procedures.

Not all drivers and databases support OUTPUT value parameters.

Example usage:

```go
var outArg string
_, err := db.ExecContext(ctx, "ProcName", sql.Named("Arg1", sql.Out{Dest: &outArg}))

```

```go
type RawBytes []byte
```

RawBytes is a byte slice that holds a reference to memory owned by the database itself. After a Rows.Scan into a RawBytes, the slice is only valid until the next call to Rows.Next, Rows.Scan, or Rows.Close.

```go
type Result interface {
	// LastInsertId returns the integer generated by the database
	// in response to a command. Typically this will be from an
	// "auto increment" column when inserting a new row. Not all
	// databases support this feature, and the syntax of such
	// statements varies.
	LastInsertId() (int64, error)

// RowsAffected returns the number of rows affected by an
	// update, insert, or delete. Not every database or database
	// driver may support this.
	RowsAffected() (int64, error)
}
```

A Result summarizes an executed SQL command.

```go
type Row struct {
	// contains filtered or unexported fields
}
```

Row is the result of calling DB.QueryRow to select a single row.

```go
func (r *Row) Err() error
```

Err provides a way for wrapping packages to check for query errors without calling Row.Scan. Err returns the error, if any, that was encountered while running the query. If this error is not nil, this error will also be returned from Row.Scan.

```go
func (r *Row) Scan(dest ...any) error
```

Scan copies the columns from the matched row into the values pointed at by dest. See the documentation on Rows.Scan for details. If more than one row matches the query, Scan uses the first row and discards the rest. If no row matches the query, Scan returns ErrNoRows.

```go
type Rows struct {
	// contains filtered or unexported fields
}
```

Rows is the result of a query. Its cursor starts before the first row of the result set. Use Rows.Next to advance from row to row.

```go

package main

import (
	"context"
	"database/sql"
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
