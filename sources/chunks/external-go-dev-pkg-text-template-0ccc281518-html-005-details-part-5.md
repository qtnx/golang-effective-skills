---
source_name: "External Linked Documentation"
source_url: "https://go.dev/pkg/text/template/"
source_path: "sources/raw/external/go-dev-pkg-text-template-0ccc281518.html"
license_ref: ""
---

```go
func (t *Template) ExecuteTemplate(wr io.Writer, name string, data any) error
```

ExecuteTemplate applies the template associated with t that has the given name to the specified data object and writes the output to wr. If an error occurs executing the template or writing its output, execution stops, but partial results may already have been written to the output writer. A template may be executed safely in parallel, although if parallel executions share a Writer the output may be interleaved.

```go
func (t *Template) Funcs(funcMap FuncMap) *Template
```

Funcs adds the elements of the argument map to the template's function map. It must be called before the template is parsed. It panics if a value in the map is not a function with appropriate return type or if the name cannot be used syntactically as a function in a template. It is legal to overwrite elements of the map. The return value is the template, so calls can be chained.

```go
func (t *Template) Lookup(name string) *Template
```

Lookup returns the template with the given name that is associated with t. It returns nil if there is no such template or the template has no definition.

```go
func (t *Template) Name() string
```

Name returns the name of the template.

```go
func (t *Template) New(name string) *Template
```

New allocates a new, undefined template associated with the given one and with the same delimiters. The association, which is transitive, allows one template to invoke another with a {{template}} action.

Because associated templates share underlying data, template construction cannot be done safely in parallel. Once the templates are constructed, they can be executed in parallel.

```go
func (t *Template) Option(opt ...string) *Template
```

Option sets options for the template. Options are described by strings, either a simple string or "key=value". There can be at most one equals sign in an option string. If the option string is unrecognized or otherwise invalid, Option panics.

Known options:

missingkey: Control the behavior during execution if a map is indexed with a key that is not present in the map.

```go
"missingkey=default" or "missingkey=invalid"
	The default behavior: Do nothing and continue execution.
	If printed, the result of the index operation is the string
	"<no value>".
"missingkey=zero"
	The operation returns the zero value for the map type's element.
"missingkey=error"
	Execution stops immediately with an error.

```

```go
func (t *Template) Parse(text string) (*Template, error)
```

Parse parses text as a template body for t. Named template definitions ({{define ...}} or {{block ...}} statements) in text define additional templates associated with t and are removed from the definition of t itself.

Templates can be redefined in successive calls to Parse. A template definition with a body containing only white space and comments is considered empty and will not replace an existing template's body. This allows using Parse to add new named template definitions without overwriting the main template body.

```go
func (t *Template) ParseFS(fsys fs.FS, patterns ...string) (*Template, error)
```

ParseFS is like Template.ParseFiles or Template.ParseGlob but reads from the file system fsys instead of the host operating system's file system. It accepts a list of glob patterns (see path.Match). (Note that most file names serve as glob patterns matching only themselves.)

```go
func (t *Template) ParseFiles(filenames ...string) (*Template, error)
```

ParseFiles parses the named files and associates the resulting templates with t. If an error occurs, parsing stops and the returned template is nil; otherwise it is t. There must be at least one file. Since the templates created by ParseFiles are named by the base (see filepath.Base) names of the argument files, t should usually have the name of one of the (base) names of the files. If it does not, depending on t's contents before calling ParseFiles, t.Execute may fail. In that case use t.ExecuteTemplate to execute a valid template.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

```go
func (t *Template) ParseGlob(pattern string) (*Template, error)
```

ParseGlob parses the template definitions in the files identified by the pattern and associates the resulting templates with t. The files are matched according to the semantics of filepath.Match, and the pattern must match at least one file. ParseGlob is equivalent to calling Template.ParseFiles with the list of files matched by the pattern.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

```go
func (t *Template) Templates() []*Template
```

Templates returns a slice of defined templates associated with t.

##   Source Files ¶
 View all Source files <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template>

- doc.go <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template/doc.go>
- exec.go <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template/exec.go>
- funcs.go <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template/funcs.go>
- helper.go <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template/helper.go>
- option.go <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template/option.go>
- template.go <https://cs.opensource.google/go/go/+/go1.26.3:src/text/template/template.go>

##   Directories ¶
    Show internal   Expand all

parse
 Package parse builds parse trees for templates as defined by text/template and html/template.

Package parse builds parse trees for templates as defined by text/template and html/template.

Click to show internal directories.
  Click to hide internal directories.

Close

**?** : This menu   **/** : Search site   **f** or **F** : Jump to   **y** or **Y**  : Canonical URL
  Close
