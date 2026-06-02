---
source_name: "External Linked Documentation"
source_url: "https://pkg.go.dev/github.com/google/safehtml/template"
source_path: "sources/raw/external/pkg-go-dev-github-com-google-safehtml-template-38bb1b1b4b.html"
license_ref: ""
---

// ErrEndContext: "... ends in a non-text context: ..."
	// Examples:
	//   <div
	//   <div title="no close quote>
	//   <script>f()
	// Discussion:
	//   Executed templates should produce a DocumentFragment of HTML.
	//   Templates that end without closing tags will trigger this error.
	//   Templates that should not be used in an HTML context or that
	//   produce incomplete Fragments should not be executed directly.
	//
	//   {{define "main"}} <script>{{template "helper"}}</script> {{end}}
	//   {{define "helper"}} document.write(' <div title=" ') {{end}}
	//
	//   "helper" does not produce a valid document fragment, so should
	//   not be Executed directly.
	ErrEndContext

// ErrNoSuchTemplate: "no such template ..."
	// Examples:
	//   {{define "main"}}<div {{template "attrs"}}>{{end}}
	//   {{define "attrs"}}href="{{.URL}}"{{end}}
	// Discussion:
	//   Package html/template looks through template calls to compute the
	//   context.
	//   Here the {{.URL}} in "attrs" must be treated as a URL when called
	//   from "main", but you will get this error if "attrs" is not defined
	//   when "main" is parsed.
	ErrNoSuchTemplate

// ErrOutputContext: "cannot compute output context for template ..."
	// Examples:
	//   {{define "t"}}{{if .T}}{{template "t" .T}}{{end}}{{.H}}",{{end}}
	// Discussion:
	//   A recursive template does not end in the same context in which it
	//   starts, and a reliable output context cannot be computed.
	//   Look for typos in the named template.
	//   If the template should not be called in the named start context,
	//   look for calls to that template in unexpected contexts.
	//   Maybe refactor recursive templates to not be recursive.
	ErrOutputContext

// ErrPartialCharset: "unfinished JS regexp charset in ..."
	// Example:
	//     <script>var pattern = /foo[{{.Chars}}]/</script>
	// Discussion:
	//   Package html/template does not support interpolation into regular
	//   expression literal character sets.
	ErrPartialCharset

// ErrPartialEscape: "unfinished escape sequence in ..."
	// Example:
	//   <script>alert("\{{.X}}")</script>
	// Discussion:
	//   Package html/template does not support actions following a
	//   backslash.
	//   This is usually an error and there are better solutions; for
	//   example
	//     <script>alert("{{.X}}")</script>
	//   should work, and if {{.X}} is a partial escape sequence such as
	//   "xA0", mark the whole sequence as safe content: JSStr(`\xA0`)
	ErrPartialEscape

// ErrRangeLoopReentry: "on range loop re-entry: ..."
	// Example:
	//   <script>var x = [{{range .}}'{{.}},{{end}}]</script>
	// Discussion:
	//   If an iteration through a range would cause it to end in a
	//   different context than an earlier pass, there is no single context.
	//   In the example, there is missing a quote, so it is not clear
	//   whether {{.}} is meant to be inside a JS string or in a JS value
	//   context. The second iteration would produce something like
	//
	//     <script>var x = ['firstValue,'secondValue]</script>
	ErrRangeLoopReentry

// ErrSlashAmbig: '/' could start a division or regexp.
	// Example:
	//   <script>
	//     {{if .C}}var x = 1{{end}}
	//     /-{{.N}}/i.test(x) ? doThis : doThat();
	//   </script>
	// Discussion:
	//   The example above could produce `var x = 1/-2/i.test(s)...`
	//   in which the first '/' is a mathematical division operator or it
	//   could produce `/-2/i.test(s)` in which the first '/' starts a
	//   regexp literal.
	//   Look for missing semicolons inside branches, and maybe add
	//   parentheses to make it clear which interpretation you intend.
	ErrSlashAmbig

// ErrPredefinedEscaper: "predefined escaper ... disallowed in template"
	// Example:
	//   <div class={{. | html}}>Hello<div>
	// Discussion:
	//   Package html/template already contextually escapes all pipelines to
	//   produce HTML output safe against code injection. Manually escaping
	//   pipeline output using the predefined escapers "html" or "urlquery" is
	//   unnecessary, and may affect the correctness or safety of the escaped
	//   pipeline output in Go 1.8 and earlier.
	//
	//   In most cases, such as the given example, this error can be resolved by
	//   simply removing the predefined escaper from the pipeline and letting the
	//   contextual autoescaper handle the escaping of the pipeline. In other
	//   instances, where the predefined escaper occurs in the middle of a
	//   pipeline where subsequent commands expect escaped input, e.g.
	//     {{.X | html | makeALink}}
	//   where makeALink does
	//     return `<a href="`+input+`">link</a>`
	//   consider refactoring the surrounding template to make use of the
	//   contextual autoescaper, i.e.
	//     <a href="{{.X}}">link</a>
	//
	//   To ease migration to Go 1.9 and beyond, "html" and "urlquery" will
	//   continue to be allowed as the last command in a pipeline. However, if the
	//   pipeline occurs in an unquoted attribute value context, "html" is
	//   disallowed. Avoid using "html" and "urlquery" entirely in new templates.
	ErrPredefinedEscaper

// ErrEscapeAction: "cannot escape action ..."
	// Discussion:
	//   Error returned while escaping an action using EscaperForContext.
	//   Refer to error message for more details.
	// TODO: remove this error type and replace it with more informative sanitization errors.
	ErrEscapeAction

// ErrCSPCompatibility: `"javascript:" URI disallowed for CSP compatibility`,
	//   "inline event handler ... is disallowed for CSP compatibility
	// Examples:
	//   <span onclick="doThings();">A thing.</span>
	//   <a href="javascript:linkClicked()">foo</a>
	// Discussion:
	//   Inline event handlers (onclick="...", onerror="...") and
	//   <a href="javascript:..."> links can be used to run scripts,
	//   so an attacker who finds an XSS bug could inject such HTML
	//   and execute malicious JavaScript. These patterns must be
	//   refactored into safer alternatives for compatibility with
	//   Content Security Policy (CSP).
	//
	//   For example, the following HTML that contains an inline event handler:
	//     <script> function doThings() { ... } </script>
	//     <span onclick="doThings();">A thing.</span>
	//   can be refactored into:
	//     <span id="things">A thing.</span>
	//     <script nonce="${nonce}">
	//     document.addEventListener('DOMContentLoaded', function () {
	//       document.getElementById('things')
	//               .addEventListener('click', function doThings() { ... });
	//     });
	//     </script>
	//
	//   Likewise, the following HTML containng a javascript: URI:
	//     <a href="javascript:linkClicked()">foo</a>
	//   can be refactored into:
	//     <a id="foo">foo</a>
	//     <script nonce="${nonce}">
	//     document.addEventListener('DOMContentLoaded', function () {
	//       document.getElementById('foo')
	//               .addEventListener('click', linkClicked);
	//     });
	//     </script>
	ErrCSPCompatibility
	// All JS templates inside script literals have to be balanced; otherwise a concatenation such as
	// <script>alert(`x{{.data}}`</script> can contain XSS if data contains user-controlled escaped strings (e.g. as JSON).
	ErrUnbalancedJsTemplate
)
```

We define codes for each error that manifests while escaping templates, but escaped templates may also fail at runtime.

Output: "ZgotmplZ" Example:

```go
<img src="{{.X}}">
where {{.X}} evaluates to `javascript:...`

```

Discussion:

```go
"ZgotmplZ" is a special value that indicates that unsafe content reached a
CSS or URL context at runtime. The output of the example will be
  <img src="#ZgotmplZ">
If the data comes from a trusted source, use content types to exempt it
from filtering: URL(`javascript:...`).

```

```go
type FuncMap map[string]interface{}
```

FuncMap is the type of the map defining the mapping from names to functions. Each function must have either a single return value, or two return values of which the second has type error. In that case, if the second (error) argument evaluates to non-nil during execution, execution terminates and Execute returns that error. FuncMap has the same base type as FuncMap in "text/template", copied here so clients need not import "text/template".

```go
type Template struct {

// The underlying template's parse tree, updated to be HTML-safe.
	Tree *parse.Tree
	// contains filtered or unexported fields
}
```

Template is a specialized Template from "text/template" that produces a safe HTML document fragment.

```go

package main

import (
	"log"
	"os"
	"strings"

"github.com/google/safehtml/template"
)

func main() {
	const (
		master  = `Names:{{block "list" .}}{{"\n"}}{{range .}}{{println "-" .}}{{end}}{{end}}`
		overlay = `{{define "list"}} {{join . ", "}}{{end}} `
	)
	var (
		funcs     = template.FuncMap{"join": strings.Join}
		guardians = []string{"Gamora", "Groot", "Nebula", "Rocket", "Star-Lord"}
	)
	masterTmpl, err := template.New("master").Funcs(funcs).Parse(master)
	if err != nil {
		log.Fatal(err)
	}
	overlayTmpl, err := template.Must(masterTmpl.Clone()).Parse(overlay)
	if err != nil {
		log.Fatal(err)
	}
	if err := masterTmpl.Execute(os.Stdout, guardians); err != nil {
		log.Fatal(err)
	}
	if err := overlayTmpl.Execute(os.Stdout, guardians); err != nil {
		log.Fatal(err)
	}
}

```

```go
Output:
Names:
- Gamora
- Groot
- Nebula
- Rocket
- Star-Lord
Names: Gamora, Groot, Nebula, Rocket, Star-Lord

```

Share Format Run

Here we demonstrate loading a set of templates from a directory.

```go

package main

import (
	"log"
	"os"

"github.com/google/safehtml/template"
)

func main() {
	// Here we load three template files with the following contents:
	// 		testdata/glob_t0.tmpl: `T0 invokes T1: ({{template "T1"}})`
	// 		testdata/glob_t1.tmpl: `{{define "T1"}}T1 invokes T2: ({{template "T2"}}){{end}}`
	// 		testdata/glob_t2.tmpl: `{{define "T2"}}This is T2{{end}}`
	// Note that ParseGlob only accepts an untyped string constant.
	// glob_t0.tmpl is the first name matched, so it becomes the starting template,
	// the value returned by ParseGlob.
	tmpl := template.Must(template.ParseGlob("testdata/glob_*.tmpl"))

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
	"log"
	"os"

"github.com/google/safehtml/template"
)
