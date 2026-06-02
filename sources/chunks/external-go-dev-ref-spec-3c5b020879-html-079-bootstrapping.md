---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Built-in functions

### Bootstrapping

 Current implementations provide several built-in functions useful during bootstrapping. These functions are documented for completeness but are not guaranteed to stay in the language. They do not return a result.

```go

Function   Behavior

print      prints all arguments; formatting of arguments is implementation-specific
println    like print but prints spaces between arguments and a newline at the end

```

 Implementation restriction: `print` and `println` need not accept arbitrary argument types, but printing of boolean, numeric, and string types must be supported.

# The Go Programming Language Specification

## Packages

 Go programs are constructed by linking together _packages_. A package in turn is constructed from one or more source files that together declare constants, types, variables and functions belonging to the package and which are accessible in all files of the same package. Those elements may be exported and used in another package.

### Source file organization

 Each source file consists of a package clause defining the package to which it belongs, followed by a possibly empty set of import declarations that declare packages whose contents it wishes to use, followed by a possibly empty set of declarations of functions, types, variables, and constants.

```go

SourceFile = PackageClause ";" { ImportDecl ";" } { TopLevelDecl ";" } .

```

### Package clause

 A package clause begins each source file and defines the package to which the file belongs.

```go

PackageClause = "package" PackageName .
PackageName   = identifier .

```

 The PackageName must not be the blank identifier.

```go

package math

```

 A set of files sharing the same PackageName form the implementation of a package. An implementation may require that all source files for a package inhabit the same directory.

### Import declarations

 An import declaration states that the source file containing the declaration depends on functionality of the _imported_ package (§Program initialization and execution) and enables access to exported identifiers of that package. The import names an identifier (PackageName) to be used for access and an ImportPath that specifies the package to be imported.

```go

ImportDecl = "import" ( ImportSpec | "(" { ImportSpec ";" } ")" ) .
ImportSpec = [ "." | PackageName ] ImportPath .
ImportPath = string_lit .

```

 The PackageName is used in qualified identifiers to access exported identifiers of the package within the importing source file. It is declared in the file block. If the PackageName is omitted, it defaults to the identifier specified in the package clause of the imported package. If an explicit period (`.`) appears instead of a name, all the package's exported identifiers declared in that package's package block will be declared in the importing source file's file block and must be accessed without a qualifier.

 The interpretation of the ImportPath is implementation-dependent but it is typically a substring of the full file name of the compiled package and may be relative to a repository of installed packages.

 Implementation restriction: A compiler may restrict ImportPaths to non-empty strings using only characters belonging to Unicode's <https://www.unicode.org/versions/Unicode6.3.0/> L, M, N, P, and S general categories (the Graphic characters without spaces) and may also exclude the characters `!"#$%&'()*,:;<=>?[\]^`{|}` and the Unicode replacement character U+FFFD.

 Consider a compiled a package containing the package clause `package math`, which exports function `Sin`, and installed the compiled package in the file identified by `"lib/math"`. This table illustrates how `Sin` is accessed in files that import the package after the various types of import declaration.

```go

Import declaration          Local name of Sin

import   "lib/math"         math.Sin
import m "lib/math"         m.Sin
import . "lib/math"         Sin

```

 An import declaration declares a dependency relation between the importing and imported package. It is illegal for a package to import itself, directly or indirectly, or to directly import a package without referring to any of its exported identifiers. To import a package solely for its side-effects (initialization), use the blank identifier as explicit package name:

```go

import _ "lib/math"

```

### An example package

 Here is a complete Go package that implements a concurrent prime sieve.

```go

package main

import "fmt"

// Send the sequence 2, 3, 4, … to channel 'ch'.
func generate(ch chan<- int) {
	for i := 2; ; i++ {
		ch <- i  // Send 'i' to channel 'ch'.
	}
}

// Copy the values from channel 'src' to channel 'dst',
// removing those divisible by 'prime'.
func filter(src <-chan int, dst chan<- int, prime int) {
	for i := range src {  // Loop over values received from 'src'.
		if i%prime != 0 {
			dst <- i  // Send 'i' to channel 'dst'.
		}
	}
}

// The prime sieve: Daisy-chain filter processes together.
func sieve() {
	ch := make(chan int)  // Create a new channel.
	go generate(ch)       // Start generate() as a subprocess.
	for {
		prime := <-ch
		fmt.Print(prime, "\n")
		ch1 := make(chan int)
		go filter(ch, ch1, prime)
		ch = ch1
	}
}

func main() {
	sieve()
}

```
