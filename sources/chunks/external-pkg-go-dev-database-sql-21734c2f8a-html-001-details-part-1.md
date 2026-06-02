---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/database/sql"
source_path: "sources/raw/external/pkg-go-dev-database-sql-21734c2f8a.html"
license_ref: ""
---

sql package - database/sql - Go Packages
## Details

-     Valid go.mod <https://cs.opensource.google/go/go/+/go1.26.3:src/go.mod> file
 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go.

-     Redistributable license
 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed.

-     Tagged version
Modules with tagged versions give importers more predictable builds.

-     Stable version
When a project reaches major version v1 it is considered stable.

-  Learn more about best practices

## Repository
   cs.opensource.google/go/go  <https://cs.opensource.google/go/go>

##   Documentation ¶

Package sql provides a generic interface around SQL (or SQL-like) databases.

The sql package must be used in conjunction with a database driver. See https://golang.org/s/sqldrivers <https://golang.org/s/sqldrivers> for a list of drivers.

Drivers that do not support context cancellation will not return until after the query is completed.

For usage examples, see the wiki page at https://golang.org/s/sqlwiki <https://golang.org/s/sqlwiki>.

```go

package main

import (
	"context"
	"database/sql"
	"flag"
	"log"
	"os"
	"os/signal"
	"time"
)

var pool *sql.DB // Database connection pool.

func main() {
	id := flag.Int64("id", 0, "person ID to find")
	dsn := flag.String("dsn", os.Getenv("DSN"), "connection data source name")
	flag.Parse()

if len(*dsn) == 0 {
		log.Fatal("missing dsn flag")
	}
	if *id == 0 {
		log.Fatal("missing person ID")
	}
	var err error

// Opening a driver typically will not attempt to connect to the database.
	pool, err = sql.Open("driver-name", *dsn)
	if err != nil {
		// This will not be a connection error, but a DSN parse error or
		// another initialization error.
		log.Fatal("unable to use data source name", err)
	}
	defer pool.Close()

pool.SetConnMaxLifetime(0)
	pool.SetMaxIdleConns(3)
	pool.SetMaxOpenConns(3)

ctx, stop := context.WithCancel(context.Background())
	defer stop()

appSignal := make(chan os.Signal, 3)
	signal.Notify(appSignal, os.Interrupt)

go func() {
		<-appSignal
		stop()
	}()

Ping(ctx)

Query(ctx, *id)
}

// Ping the database to verify DSN provided by the user is valid and the
// server accessible. If the ping fails exit the program with an error.
func Ping(ctx context.Context) {
	ctx, cancel := context.WithTimeout(ctx, 1*time.Second)
	defer cancel()

if err := pool.PingContext(ctx); err != nil {
		log.Fatalf("unable to connect to database: %v", err)
	}
}

// Query the database for the information requested and prints the results.
// If the query fails exit the program with an error.
func Query(ctx context.Context, id int64) {
	ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
	defer cancel()

var name string
	err := pool.QueryRowContext(ctx, "select p.name from people as p where p.id = :id;", sql.Named("id", id)).Scan(&name)
	if err != nil {
		log.Fatal("unable to execute search query", err)
	}
	log.Println("name=", name)
}

```

```go
Output:

```

Share Format Run

```go

package main

import (
	"context"
	"database/sql"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"time"
)

func main() {
	// Opening a driver typically will not attempt to connect to the database.
	db, err := sql.Open("driver-name", "database=test1")
	if err != nil {
		// This will not be a connection error, but a DSN parse error or
		// another initialization error.
		log.Fatal(err)
	}
	db.SetConnMaxLifetime(0)
	db.SetMaxIdleConns(50)
	db.SetMaxOpenConns(50)

s := &Service{db: db}

http.ListenAndServe(":8080", s)
}

type Service struct {
	db *sql.DB
}

func (s *Service) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	db := s.db
	switch r.URL.Path {
	default:
		http.Error(w, "not found", http.StatusNotFound)
		return
	case "/healthz":
		ctx, cancel := context.WithTimeout(r.Context(), 1*time.Second)
		defer cancel()

err := s.db.PingContext(ctx)
		if err != nil {
			http.Error(w, fmt.Sprintf("db down: %v", err), http.StatusFailedDependency)
			return
		}
		w.WriteHeader(http.StatusOK)
		return
	case "/quick-action":
		// This is a short SELECT. Use the request context as the base of
		// the context timeout.
		ctx, cancel := context.WithTimeout(r.Context(), 3*time.Second)
		defer cancel()

id := 5
		org := 10
		var name string
		err := db.QueryRowContext(ctx, `
select
	p.name
from
	people as p
	join organization as o on p.organization = o.id
where
	p.id = :id
	and o.id = :org
;`,
			sql.Named("id", id),
			sql.Named("org", org),
		).Scan(&name)
		if err != nil {
			if err == sql.ErrNoRows {
				http.Error(w, "not found", http.StatusNotFound)
				return
			}
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		io.WriteString(w, name)
		return
	case "/long-action":
		// This is a long SELECT. Use the request context as the base of
		// the context timeout, but give it some time to finish. If
		// the client cancels before the query is done the query will also
		// be canceled.
		ctx, cancel := context.WithTimeout(r.Context(), 60*time.Second)
		defer cancel()

var names []string
		rows, err := db.QueryContext(ctx, "select p.name from people as p where p.active = true;")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

for rows.Next() {
			var name string
			err = rows.Scan(&name)
			if err != nil {
				break
			}
			names = append(names, name)
		}
		// Check for errors during rows "Close".
		// This may be more important if multiple statements are executed
		// in a single batch and rows were written as well as read.
		if closeErr := rows.Close(); closeErr != nil {
			http.Error(w, closeErr.Error(), http.StatusInternalServerError)
			return
		}

// Check for row scan error.
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

// Check for errors during row iteration.
		if err = rows.Err(); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

json.NewEncoder(w).Encode(names)
		return
	case "/async-action":
		// This action has side effects that we want to preserve
		// even if the client cancels the HTTP request part way through.
		// For this we do not use the http request context as a base for
		// the timeout.
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		defer cancel()

var orderRef = "ABC123"
		tx, err := db.BeginTx(ctx, &sql.TxOptions{Isolation: sql.LevelSerializable})
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		_, err = tx.ExecContext(ctx, "stored_proc_name", orderRef)

if err != nil {
			tx.Rollback()
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		err = tx.Commit()
		if err != nil {
			http.Error(w, "action in unknown state, check state before attempting again", http.StatusInternalServerError)
			return
		}
		w.WriteHeader(http.StatusOK)
		return
	}
}

```

```go
Output:

```

Share Format Run

- Variables
-  func Drivers() []string
-  func Register(name string, driver driver.Driver)
-  type ColumnType
-
-  func (ci *ColumnType) DatabaseTypeName() string
-  func (ci *ColumnType) DecimalSize() (precision, scale int64, ok bool)
-  func (ci *ColumnType) Length() (length int64, ok bool)
-  func (ci *ColumnType) Name() string
-  func (ci *ColumnType) Nullable() (nullable, ok bool)
-  func (ci *ColumnType) ScanType() reflect.Type

-  type Conn
-
-  func (c *Conn) BeginTx(ctx context.Context, opts *TxOptions) (*Tx, error)
-  func (c *Conn) Close() error
-  func (c *Conn) ExecContext(ctx context.Context, query string, args ...any) (Result, error)
-  func (c *Conn) PingContext(ctx context.Context) error
-  func (c *Conn) PrepareContext(ctx context.Context, query string) (*Stmt, error)
-  func (c *Conn) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)
-  func (c *Conn) QueryRowContext(ctx context.Context, query string, args ...any) *Row
-  func (c *Conn) Raw(f func(driverConn any) error) (err error)

-  type DB
-
-  func Open(driverName, dataSourceName string) (*DB, error)
-  func OpenDB(c driver.Connector) *DB

-
-  func (db *DB) Begin() (*Tx, error)
-  func (db *DB) BeginTx(ctx context.Context, opts *TxOptions) (*Tx, error)
-  func (db *DB) Close() error
-  func (db *DB) Conn(ctx context.Context) (*Conn, error)
-  func (db *DB) Driver() driver.Driver
-  func (db *DB) Exec(query string, args ...any) (Result, error)
-  func (db *DB) ExecContext(ctx context.Context, query string, args ...any) (Result, error)
-  func (db *DB) Ping() error
-  func (db *DB) PingContext(ctx context.Context) error
-  func (db *DB) Prepare(query string) (*Stmt, error)
-  func (db *DB) PrepareContext(ctx context.Context, query string) (*Stmt, error)
-  func (db *DB) Query(query string, args ...any) (*Rows, error)
-  func (db *DB) QueryContext(ctx context.Context, query string, args ...any) (*Rows, error)
-  func (db *DB) QueryRow(query string, args ...any) *Row
-  func (db *DB) QueryRowContext(ctx context.Context, query string, args ...any) *Row
-  func (db *DB) SetConnMaxIdleTime(d time.Duration)
-  func (db *DB) SetConnMaxLifetime(d time.Duration)
-  func (db *DB) SetMaxIdleConns(n int)
-  func (db *DB) SetMaxOpenConns(n int)
-  func (db *DB) Stats() DBStats

-  type DBStats
-  type IsolationLevel
-
-  func (i IsolationLevel) String() string

-  type NamedArg
-
-  func Named(name string, value any) NamedArg

-  type Null
-
-  func (n *Null[T]) Scan(value any) error
-  func (n Null[T]) Value() (driver.Value, error)

-  type NullBool
-
-  func (n *NullBool) Scan(value any) error
-  func (n NullBool) Value() (driver.Value, error)

-  type NullByte
-
-  func (n *NullByte) Scan(value any) error
-  func (n NullByte) Value() (driver.Value, error)

-  type NullFloat64
-
-  func (n *NullFloat64) Scan(value any) error
-  func (n NullFloat64) Value() (driver.Value, error)

-  type NullInt16
-
-  func (n *NullInt16) Scan(value any) error
-  func (n NullInt16) Value() (driver.Value, error)

-  type NullInt32
-
-  func (n *NullInt32) Scan(value any) error
-  func (n NullInt32) Value() (driver.Value, error)

-  type NullInt64
-
-  func (n *NullInt64) Scan(value any) error
-  func (n NullInt64) Value() (driver.Value, error)

-  type NullString
-
-  func (ns *NullString) Scan(value any) error
-  func (ns NullString) Value() (driver.Value, error)

-  type NullTime
-
-  func (n *NullTime) Scan(value any) error
-  func (n NullTime) Value() (driver.Value, error)

-  type Out
-  type RawBytes
-  type Result
-  type Row
-
-  func (r *Row) Err() error
-  func (r *Row) Scan(dest ...any) error

-  type Rows
-
-  func (rs *Rows) Close() error
-  func (rs *Rows) ColumnTypes() ([]*ColumnType, error)
-  func (rs *Rows) Columns() ([]string, error)
-  func (rs *Rows) Err() error
-  func (rs *Rows) Next() bool
-  func (rs *Rows) NextResultSet() bool
-  func (rs *Rows) Scan(dest ...any) error

-  type Scanner
-  type Stmt
-
-  func (s *Stmt) Close() error
-  func (s *Stmt) Exec(args ...any) (Result, error)
-  func (s *Stmt) ExecContext(ctx context.Context, args ...any) (Result, error)
-  func (s *Stmt) Query(args ...any) (*Rows, error)
-  func (s *Stmt) QueryContext(ctx context.Context, args ...any) (*Rows, error)
-  func (s *Stmt) QueryRow(args ...any) *Row
-  func (s *Stmt) QueryRowContext(ctx context.Context, args ...any) *Row
