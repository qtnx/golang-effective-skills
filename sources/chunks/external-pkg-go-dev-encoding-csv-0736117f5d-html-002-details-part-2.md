---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/encoding/csv"
source_path: "sources/raw/external/pkg-go-dev-encoding-csv-0736117f5d.html"
license_ref: ""
---

# lines beginning with a # character are ignored

// Write any buffered data to the underlying writer (standard output).
	w.Flush()

if err := w.Error(); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:
first_name,last_name,username
Rob,Pike,rob
Ken,Thompson,ken
Robert,Griesemer,gri

```

Share Format Run

```go
func NewWriter(w io.Writer) *Writer
```

NewWriter returns a new Writer that writes to w.

```go
func (w *Writer) Error() error
```

Error reports any error that has occurred during a previous Writer.Write or Writer.Flush.

```go
func (w *Writer) Flush()
```

Flush writes any buffered data to the underlying io.Writer. To check if an error occurred during Flush, call Writer.Error.

```go
func (w *Writer) Write(record []string) error
```

Write writes a single CSV record to w along with any necessary quoting. A record is a slice of strings with each string being one field. Writes are buffered, so Writer.Flush must eventually be called to ensure that the record is written to the underlying io.Writer.

```go
func (w *Writer) WriteAll(records [][]string) error
```

WriteAll writes multiple CSV records to w using Writer.Write and then calls Writer.Flush, returning any error from the Flush.

```go

package main

import (
	"encoding/csv"
	"log"
	"os"
)

func main() {
	records := [][]string{
		{"first_name", "last_name", "username"},
		{"Rob", "Pike", "rob"},
		{"Ken", "Thompson", "ken"},
		{"Robert", "Griesemer", "gri"},
	}

w := csv.NewWriter(os.Stdout)
	w.WriteAll(records) // calls Flush internally

if err := w.Error(); err != nil {
		log.Fatalln("error writing csv:", err)
	}
}

```

```go
Output:
first_name,last_name,username
Rob,Pike,rob
Ken,Thompson,ken
Robert,Griesemer,gri

```

Share Format Run

# lines beginning with a # character are ignored

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv>

- reader.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv/reader.go>
- writer.go <https://cs.opensource.google/go/go/+/go1.26.3:src/encoding/csv/writer.go>

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
