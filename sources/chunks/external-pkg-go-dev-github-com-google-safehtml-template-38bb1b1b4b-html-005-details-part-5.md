---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/safehtml/template"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-safehtml-template-38bb1b1b4b.html"
license_ref: ""
---

ExecuteToHTML applies a parsed template to the specified data object, returning the output as a safehtml.HTML value. A template may be executed safely in parallel.

```go
func (t *Template) Funcs(funcMap FuncMap) *Template
```

Funcs adds the elements of the argument map to the template's function map. It must be called before the template is parsed. It panics if a value in the map is not a function with appropriate return type. However, it is legal to overwrite elements of the map. The return value is the template, so calls can be chained.

```go
func (t *Template) Lookup(name string) *Template
```

Lookup returns the template with the given name that is associated with t, or nil if there is no such template.

```go
func (t *Template) Name() string
```

Name returns the name of the template.

```go
func (t *Template) New(name string) *Template
```

New allocates a new HTML template associated with the given one and with the same delimiters. The association, which is transitive, allows one template to invoke another with a {{template}} action.

If a template with the given name already exists, the new HTML template will replace it. The existing template will be reset and disassociated with t.

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
func (t *Template) Parse(text stringConstant) (*Template, error)
```

Parse parses text as a template body for t. Named template definitions ({{define ...}} or {{block ...}} statements) in text define additional templates associated with t and are removed from the definition of t itself.

Templates can be redefined in successive calls to Parse, before the first use of Execute on t or any associated template. A template definition with a body containing only white space and comments is considered empty and will not replace an existing template's body. This allows using Parse to add new named template definitions without overwriting the main template body.

To guarantee that the template body is never controlled by an attacker, text must be an untyped string constant, which is always under programmer control.

```go
func (t *Template) ParseFS(tfs TrustedFS, patterns ...string) (*Template, error)
```

ParseFS is like ParseFiles or ParseGlob but reads from the TrustedFS instead of the host operating system's file system. It accepts a list of glob patterns. (Note that most file names serve as glob patterns matching only themselves.)

The same behaviors listed for ParseFiles() apply to ParseFS too (e.g. using the base name of the file as the template name).

```go
func (t *Template) ParseFiles(filenames ...stringConstant) (*Template, error)
```

ParseFiles parses the named files and associates the resulting templates with t. If an error occurs, parsing stops and the returned template is nil; otherwise it is t. There must be at least one file.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseFiles returns an error if t or any associated template has already been executed.

To guarantee that filepaths, and thus template bodies, are never controlled by an attacker, filenames must be untyped string constants, which are always under programmer control.

```go
func (t *Template) ParseFilesFromTrustedSources(filenames ...TrustedSource) (*Template, error)
```

ParseFilesFromTrustedSources parses the named files and associates the resulting templates with t. If an error occurs, parsing stops and the returned template is nil; otherwise it is t. There must be at least one file.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseFilesFromTrustedSources returns an error if t or any associated template has already been executed.

To guarantee that filepaths, and thus template bodies, are never controlled by an attacker, filenames must be trusted sources, which are always under programmer or application control.

```go
func (t *Template) ParseFromTrustedTemplate(tmpl TrustedTemplate) (*Template, error)
```

ParseFromTrustedTemplate parses tmpl as a template body for t. Named template definitions ({{define ...}} or {{block ...}} statements) in text define additional templates associated with t and are removed from the definition of t itself.

Templates can be redefined in successive calls to ParseFromTrustedTemplate, before the first use of Execute on t or any associated template. A template definition with a body containing only white space and comments is considered empty and will not replace an existing template's body. This allows using ParseFromTrustedTemplate to add new named template definitions without overwriting the main template body.

To guarantee that the template body is never controlled by an attacker, tmpl is a TrustedTemplate, which is always under programmer control.

```go
func (t *Template) ParseGlob(pattern stringConstant) (*Template, error)
```

ParseGlob parses the template definitions in the files identified by the pattern and associates the resulting templates with t. The pattern is processed by filepath.Glob and must match at least one file. ParseGlob is equivalent to calling t.ParseFiles with the list of files matched by the pattern.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseGlob returns an error if t or any associated template has already been executed.

To guarantee that the pattern, and thus the template bodies, is never controlled by an attacker, pattern must be an untyped string constant, which is always under programmer control.

```go
func (t *Template) ParseGlobFromTrustedSource(pattern TrustedSource) (*Template, error)
```

ParseGlobFromTrustedSource parses the template definitions in the files identified by the pattern and associates the resulting templates with t. The pattern is processed by filepath.Glob and must match at least one file. ParseGlob is equivalent to calling t.ParseFiles with the list of files matched by the pattern.

When parsing multiple files with the same name in different directories, the last one mentioned will be the one that results.

ParseGlobFromTrustedSource returns an error if t or any associated template has already been executed.

To guarantee that the pattern, and thus the template bodies, is never controlled by an attacker, pattern must be a trusted source, which is always under programmer or application control.

```go
func (t *Template) Templates() []*Template
```

Templates returns a slice of the templates associated with t, including t itself.

```go
type TrustedFS struct {
	// contains filtered or unexported fields
}
```

A TrustedFS is an immutable type referencing a filesystem (fs.FS) under application control.

In order to ensure that an attacker cannot influence the TrustedFS value, a TrustedFS can be instantiated in only two ways. One way is from an embed.FS with TrustedFSFromEmbed. It is assumed that embedded filesystems are under the programmer's control. The other way is from a TrustedSource using TrustedFSFromTrustedSource, in which case the guarantees and caveats of TrustedSource apply.

```go
func TrustedFSFromEmbed(fsys embed.FS) TrustedFS
```

TrustedFSFromEmbed constructs a TrustedFS from an embed.FS.

```go
func TrustedFSFromTrustedSource(ts TrustedSource) TrustedFS
```

TrustedFSFromTrustedSource constructs a TrustedFS from the string in the TrustedSource, which should refer to a directory.

```go
func (tf TrustedFS) Sub(dir TrustedSource) (TrustedFS, error)
```

Sub returns a TrustedFS at a subdirectory of the receiver. It works by calling fs.Sub on the receiver's fs.FS.

```go
type TrustedSource struct {
	// contains filtered or unexported fields
}
```

A TrustedSource is an immutable string-like type referencing trusted template files under application control. It can be passed to template-parsing functions and methods to safely load templates without the risk of untrusted template execution.

In order to ensure that an attacker cannot influence the TrustedSource value, a TrustedSource can be instantiated only from untyped string constants, command-line flags, and other application-controlled strings, but never from arbitrary string values potentially representing untrusted user input.

Note that TrustedSource's constructors cannot truly guarantee that the templates it references are not attacker-controlled; it can guarantee only that the path to the template itself is under application control. Users of these constructors must ensure themselves that TrustedSource never references attacker-controlled files or directories that contain such files.

```go
func TrustedSourceFromConstant(src stringConstant) TrustedSource
```

TrustedSourceFromConstant constructs a TrustedSource with its underlying src set to the given src, which must be an untyped string constant.

No runtime validation or sanitization is performed on src; being under application control, it is simply assumed to comply with the TrustedSource type contract.

```go
func TrustedSourceFromConstantDir(dir stringConstant, src TrustedSource, filename string) (TrustedSource, error)
```

TrustedSourceFromConstantDir constructs a TrustedSource calling path/filepath.Join on an application-controlled directory path, which must be an untyped string constant, a TrustedSource, and a dynamic filename. It returns an error if filename contains filepath or list separators, since this might cause the resulting path to reference a file outside of the given directory.

dir or src may be empty if either of these path segments are not required.

```go
func TrustedSourceFromEnvVar(key stringConstant) TrustedSource
```

TrustedSourceFromEnvVar is a wrapper around os.Getenv that returns a TrustedSource containing the value of the environment variable named by the key. It returns the value, which will be empty if the variable is not present. To distinguish between an empty value and an unset value, use os.LookupEnv.

In a server setting, environment variables are part of the application's deployment configuration and are hence considered application-controlled.
