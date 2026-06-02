---
source_name: "External Linked Documentation"
source_url: "https://go.dev/ref/spec"
source_path: "sources/raw/external/go-dev-ref-spec-3c5b020879.html"
license_ref: ""
---

## Lexical elements

### Identifiers

 Identifiers name program entities such as variables and types. An identifier is a sequence of one or more letters and digits. The first character in an identifier must be a letter.

```go

identifier = letter { letter | unicode_digit } .

```

```go

a
_x9
ThisVariableIsExported
αβ

```

 Some identifiers are predeclared.

## Lexical elements

### Keywords

 The following keywords are reserved and may not be used as identifiers.

```go

break        default      func         interface    select
case         defer        go           map          struct
chan         else         goto         package      switch
const        fallthrough  if           range        type
continue     for          import       return       var

```

## Lexical elements

### Operators and punctuation

 The following character sequences represent operators (including assignment operators) and punctuation [Go 1.18]:

```go

+    &     +=    &=     &&    ==    !=    (    )
-    |     -=    |=     ||    <     <=    [    ]
*    ^     *=    ^=     <-    >     >=    {    }
/    <<    /=    <<=    ++    =     :=    ,    ;
%    >>    %=    >>=    --    !     ...   .    :
     &^          &^=          ~

```
