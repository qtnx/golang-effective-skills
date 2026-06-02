---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/text/template"
source_path: "sources/raw/external/pkg-go-dev-text-template-6ffbb3f83b.html"
license_ref: ""
---

err := tmpl.Execute(os.Stdout, nil)
	if err != nil {
		log.Fatalf("template execution: %s", err)
	}
}

```

```go
Output:
T0 invokes T1: (T1 invokes T2: (This is T2))

```

Share Format Run

This example demonstrates one way to share some templates and use them in different contexts. In this variant we add multiple driver templates by hand to an existing bundle of templates.

```go

package main

import (
	"io"
	"log"
	"os"
	"path/filepath"
	"text/template"
)

// templateFile defines the contents of a template to be stored in a file, for testing.
type templateFile struct {
	name     string
	contents string
}

func createTestDir(files []templateFile) string {
	dir, err := os.MkdirTemp("", "template")
	if err != nil {
		log.Fatal(err)
	}
	for _, file := range files {
		f, err := os.Create(filepath.Join(dir, file.name))
		if err != nil {
			log.Fatal(err)
		}
		defer f.Close()
		_, err = io.WriteString(f, file.contents)
		if err != nil {
			log.Fatal(err)
		}
	}
	return dir
}

func main() {
	// Here we create a temporary directory and populate it with our sample
	// template definition files; usually the template files would already
	// exist in some location known to the program.
	dir := createTestDir([]templateFile{
		// T1.tmpl defines a template, T1 that invokes T2.
		{"T1.tmpl", `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`},
		// T2.tmpl defines a template T2.
		{"T2.tmpl", `{{define "T2"}}This is T2{{end}}`},
	})
	// Clean up after the test; another quirk of running as an example.
	defer os.RemoveAll(dir)

// pattern is the glob pattern used to find all the template files.
	pattern := filepath.Join(dir, "*.tmpl")

// Here starts the example proper.
	// Load the helpers.
	templates := template.Must(template.ParseGlob(pattern))
	// Add one driver template to the bunch; we do this with an explicit template definition.
	_, err := templates.Parse("{{define `driver1`}}Driver 1 calls T1: ({{template `T1`}})\n{{end}}")
	if err != nil {
		log.Fatal("parsing driver1: ", err)
	}
	// Add another driver template.
	_, err = templates.Parse("{{define `driver2`}}Driver 2 calls T2: ({{template `T2`}})\n{{end}}")
	if err != nil {
		log.Fatal("parsing driver2: ", err)
	}
	// We load all the templates before execution. This package does not require
	// that behavior but html/template's escaping does, so it's a good habit.
	err = templates.ExecuteTemplate(os.Stdout, "driver1", nil)
	if err != nil {
		log.Fatalf("driver1 execution: %s", err)
	}
	err = templates.ExecuteTemplate(os.Stdout, "driver2", nil)
	if err != nil {
		log.Fatalf("driver2 execution: %s", err)
	}
}

```

```go
Output:
Driver 1 calls T1: (T1 invokes T2: (This is T2))
Driver 2 calls T2: (This is T2)

```

Share Format Run

This example demonstrates how to use "if".

```go

package main

import (
	"log"
	"os"
	"text/template"
)

func main() {
	type book struct {
		Stars float32
		Name  string
	}

tpl, err := template.New("book").Parse(`{{ if (gt .Stars 4.0) }}"{{.Name }}" is a great book.{{ else }}"{{.Name}}" is not a great book.{{ end }}`)
	if err != nil {
		log.Fatalf("failed to parse template: %s", err)
	}

b := &book{
		Stars: 4.9,
		Name:  "Good Night, Gopher",
	}
	err = tpl.Execute(os.Stdout, b)
	if err != nil {
		log.Fatalf("failed to execute template: %s", err)
	}

}

```

```go
Output:
"Good Night, Gopher" is a great book.

```

Share Format Run

This example demonstrates how to use one group of driver templates with distinct sets of helper templates.

```go

package main

import (
	"io"
	"log"
	"os"
	"path/filepath"
	"text/template"
)

// templateFile defines the contents of a template to be stored in a file, for testing.
type templateFile struct {
	name     string
	contents string
}

func createTestDir(files []templateFile) string {
	dir, err := os.MkdirTemp("", "template")
	if err != nil {
		log.Fatal(err)
	}
	for _, file := range files {
		f, err := os.Create(filepath.Join(dir, file.name))
		if err != nil {
			log.Fatal(err)
		}
		defer f.Close()
		_, err = io.WriteString(f, file.contents)
		if err != nil {
			log.Fatal(err)
		}
	}
	return dir
}

func main() {
	// Here we create a temporary directory and populate it with our sample
	// template definition files; usually the template files would already
	// exist in some location known to the program.
	dir := createTestDir([]templateFile{
		// T0.tmpl is a plain template file that just invokes T1.
		{"T0.tmpl", "T0 ({{.}} version) invokes T1: ({{template `T1`}})\n"},
		// T1.tmpl defines a template, T1 that invokes T2. Note T2 is not defined
		{"T1.tmpl", `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`},
	})
	// Clean up after the test; another quirk of running as an example.
	defer os.RemoveAll(dir)

// pattern is the glob pattern used to find all the template files.
	pattern := filepath.Join(dir, "*.tmpl")

// Here starts the example proper.
	// Load the drivers.
	drivers := template.Must(template.ParseGlob(pattern))

// We must define an implementation of the T2 template. First we clone
	// the drivers, then add a definition of T2 to the template name space.

// 1. Clone the helper set to create a new name space from which to run them.
	first, err := drivers.Clone()
	if err != nil {
		log.Fatal("cloning helpers: ", err)
	}
	// 2. Define T2, version A, and parse it.
	_, err = first.Parse("{{define `T2`}}T2, version A{{end}}")
	if err != nil {
		log.Fatal("parsing T2: ", err)
	}

// Now repeat the whole thing, using a different version of T2.
	// 1. Clone the drivers.
	second, err := drivers.Clone()
	if err != nil {
		log.Fatal("cloning drivers: ", err)
	}
	// 2. Define T2, version B, and parse it.
	_, err = second.Parse("{{define `T2`}}T2, version B{{end}}")
	if err != nil {
		log.Fatal("parsing T2: ", err)
	}

// Execute the templates in the reverse order to verify the
	// first is unaffected by the second.
	err = second.ExecuteTemplate(os.Stdout, "T0.tmpl", "second")
	if err != nil {
		log.Fatalf("second execution: %s", err)
	}
	err = first.ExecuteTemplate(os.Stdout, "T0.tmpl", "first")
	if err != nil {
		log.Fatalf("first: execution: %s", err)
	}

}

```

```go
Output:
T0 (second version) invokes T1: (T1 invokes T2: (T2, version B))
T0 (first version) invokes T1: (T1 invokes T2: (T2, version A))

```

Share Format Run

```go
func Must(t *Template, err error) *Template
```

Must is a helper that wraps a call to a function returning (*Template, error) and panics if the error is non-nil. It is intended for use in variable initializations such as

```go
var t = template.Must(template.New("name").Parse("text"))

```

```go
func New(name string) *Template
```

New allocates a new, undefined template with the given name.

```go
func ParseFS(fsys fs.FS, patterns ...string) (*Template, error)
```

ParseFS is like Template.ParseFiles or Template.ParseGlob but reads from the file system fsys instead of the host operating system's file system. It accepts a list of glob patterns (see path.Match). (Note that most file names serve as glob patterns matching only themselves.)

```go
func ParseFiles(filenames ...string) (*Template, error)
```

ParseFiles creates a new Template and parses the template definitions from the named files. The returned template's name will have the base name and parsed contents of the first file. There must be at least one file. If an error occurs, parsing stops and the returned *Template is nil.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results. For instance, ParseFiles("a/foo", "b/foo") stores "b/foo" as the template named "foo", while "a/foo" is unavailable.

```go
func ParseGlob(pattern string) (*Template, error)
```

ParseGlob creates a new Template and parses the template definitions from the files identified by the pattern. The files are matched according to the semantics of filepath.Match, and the pattern must match at least one file. The returned template will have the filepath.Base name and (parsed) contents of the first file matched by the pattern. ParseGlob is equivalent to calling ParseFiles with the list of files matched by the pattern.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

```go
func (t *Template) AddParseTree(name string, tree *parse.Tree) (*Template, error)
```

AddParseTree associates the argument parse tree with the template t, giving it the specified name. If the template has not been defined, this tree becomes its definition. If it has been defined and already has that name, the existing definition is replaced; otherwise a new template is created, defined, and returned.

```go
func (t *Template) Clone() (*Template, error)
```

Clone returns a duplicate of the template, including all associated templates. The actual representation is not copied, but the name space of associated templates is, so further calls to Template.Parse in the copy will add templates to the copy but not to the original. Clone can be used to prepare common templates and use them with variant definitions for other templates by adding the variants after the clone is made.

```go
func (t *Template) DefinedTemplates() string
```

DefinedTemplates returns a string listing the defined templates, prefixed by the string "; defined templates are: ". If there are none, it returns the empty string. For generating an error message here and in html/template.

```go
func (t *Template) Delims(left, right string) *Template
```

Delims sets the action delimiters to the specified strings, to be used in subsequent calls to Template.Parse, Template.ParseFiles, or Template.ParseGlob. Nested template definitions will inherit the settings. An empty delimiter stands for the corresponding default: {{ or }}. The return value is the template, so calls can be chained.

```go
func (t *Template) Execute(wr io.Writer, data any) error
```

Execute applies a parsed template to the specified data object, and writes the output to wr. If an error occurs executing the template or writing its output, execution stops, but partial results may already have been written to the output writer. A template may be executed safely in parallel, although if parallel executions share a Writer the output may be interleaved.

If data is a reflect.Value, the template applies to the concrete value that the reflect.Value holds, as in fmt.Print.
