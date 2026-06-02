---
source_name: "External Linked Documentation"
source_url: "https://commandcenter.blogspot.com/2017/12/error-handling-in-upspin.html"
source_path: "sources/raw/external/commandcenter-blogspot-com-2017-12-error-handling-in-upspin-html-e227930291.html"
license_ref: ""
---

command center: Error handling in Upspin

###  Error handling in Upspin

   The Upspin <https://upspin.io/> project uses a custom package, upspin.io/errors <https://godoc.org/upspin.io/errors>, to represent error conditions that arise inside the system. These errors satisfy the standard Go error <https://golang.org/pkg/builtin/#error> interface, but are implemented using a custom type, upspin.io/errors.Error <https://godoc.org/upspin.io/errors#Error>, that has properties that have proven valuable to the project.

 Here we will demonstrate how the package works and how it is used. The story holds lessons for the larger discussion of error handling in Go.

 **Motivations**

 A few months into the project, it became clear we needed a consistent approach to error construction, presentation, and handling throughout the code. We decided to implement a custom errors package, and rolled one out in an afternoon. The details have changed a bit but the basic ideas behind the package have endured. These were:

- To make it easy to build informative error messages.

- To make errors easy to understand for users.

- To make errors helpful as diagnostics for programmers.

 As we developed experience with the package, some other motivations emerged. We'll talk about these below.

 **A tour of the package**

 The upspin.io/errors <https://godoc.org/upspin.io/errors> package is imported with the package name "errors", and so inside Upspin it takes over the role of Go's standard "errors" package.

 We noticed that the elements that go into an error message in Upspin are all of different types: user names, path names, the kind of error (I/O, permission, etc.) and so on. This provided the starting point for the package, which would build on these different types to construct, represent, and report the errors that arise.

 The center of the package is the Error <https://godoc.org/upspin.io/errors#Error> type, the concrete representation of an Upspin error. It has several fields, any of which may be left unset:

   type Error struct {

       Path upspin.PathName

       User upspin.UserName

       Op  Op

       Kind Kind

       Err error

   }

 The Path and User fields denote the path and user affected by the operation. Note that these are both strings, but have distinct types in Upspin to clarify their usage and to allow the type system to catch certain classes of programming errors.

 The Op field denotes the operation being performed. It is another string type and typically holds the name of the method or server function reporting the error: "client.Lookup", "dir/server.Glob", and so on.

 The Kind field classifies the error as one of a set of standard conditions (Permission, IO, NotExist, and so on <https://godoc.org/upspin.io/errors#Kind>). It makes it easy to see a concise description of what sort of error occurred, but also provides a hook for interfacing to other systems. For instance, upspinfs <https://godoc.org/upspin.io/cmd/upspinfs> uses the Kind field as the key to translation from Upspin errors to Unix error constants such as EPERM and EIO.

 The last field, Err, may hold another error value. Often this is an error from another system, such as a file system error from the os <https://golang.org/pkg/os/> package or a network error from the net <https://golang.org/pkg/net/> package. It may also be another upspin.io/errors.Error value, creating a kind of error trace that we will discuss later.

 **Constructing an Error**

 To facilitate error construction, the package provides a function named E <https://godoc.org/upspin.io/errors#E>, which is short and easy to type.

   func E(args ...interface{}) error

 As the doc comment <https://godoc.org/upspin.io/errors#E> for the function says, E builds an error value from its arguments. The type of each argument determines its meaning. The idea is to look at the types of the arguments and assign each argument to the field of the corresponding type in the constructed Error struct. There is an obvious correspondence: a PathName goes to Error.Path, a UserName to Error.User, and so on.

 Let's look at an example. In typical use, calls to errors.E will arise multiple times within a method, so we define a constant, conventionally called op, that will be passed to all E calls within the method:

   func (s *Server) Delete(ref upspin.Reference) error {

     const op errors.Op = "server.Delete"

      ...

 Then through the method we use the constant to prefix each call (although the actual ordering of arguments is irrelevant, by convention op goes first):

   if err := authorize(user); err != nil {

     return errors.E(op, user, errors.Permission, err)

   }

 The String method for E will format this neatly:

   server.Delete: user ann@example.com: permission denied: user not authorized

 If the errors nest to multiple levels, redundant fields are suppressed and the nesting is formatted with indentation:

   client.Lookup: ann@example.com/file: item does not exist:

           dir/remote("upspin.example.net:443").Lookup:

           dir/server.Lookup

 Notice that there are multiple operations mentioned in this error message (client.Lookup, dir/remote, dir/server). We'll discuss this multiplicity in a later section.

 As another example, sometimes the error is special and is most clearly described at the call site by a plain string. To make this work in the obvious way, the constructor promotes arguments of literal type string to a Go error type through a mechanism similar to the standard Go function errors.New <https://golang.org/pkg/errors/#New> <https://www.blogger.com/>. Thus one can write:

    errors.E(op, "unexpected failure")

 or

    errors.E(op, fmt.Sprintf("could not succeed after %d tries", nTries))

 and have the string be assigned to the Err field of the resulting Err type. This is a natural and easy way to build special-case errors.

 **Errors across the wire**

 Upspin is a distributed system and so it is critical that communications between Upspin servers preserve the structure of errors. To accomplish this we made Upspin's RPCs aware of these error types, using the errors package's MarshalError <https://godoc.org/upspin.io/errors#MarshalError> and UnmarshalError <https://godoc.org/upspin.io/errors#UnmarshalError> functions to transcode errors across a network connection. These functions make sure that a client will see all the details that the server provided when it constructed the error.

 Consider this error report:

   client.Lookup: ann@example.com/test/file: item does not exist:

          dir/remote("dir.example.com:443").Lookup:

          dir/server.Lookup:

          store/remote("store.example.com:443").Get:

          fetching https://storage.googleapis.com/bucket/C1AF...: 404 Not Found

 This is represented by four nested errors.E values.

 Reading from the bottom up, the innermost is from the package upspin.io/store/remote <http://upspin.io/store/remotehttps://godoc.org/upspin.io/store/remote> (responsible for taking to remote storage servers). The error indicates that there was a problem fetching an object from storage. That error is constructed with something like this, wrapping an underlying error from the cloud storage provider:

   const op errors.Op = `store/remote("store.example.com:443").Get`

   var resp *http.Response

   ...

   return errors.E(op, errors.Sprintf("fetching %s: %s", url, resp.Status))

 The next error is from the directory server (package upspin.io/dir/server <https://godoc.org/upspin.io/dir/server>, our directory server reference implementation), which indicates that the directory server was trying to perform a Lookup when the error occurred. That error is constructed like this:

   const op errors.Op = "dir/server.Lookup"

   ...

   return errors.E(op, pathName, errors.NotExist, err)

 This is the first layer at which a Kind (errors.NotExist) is added.

 The Lookup error value is passed across the network (marshaled and unmarshaled along the way), and then the upspin.io/dir/remote <https://godoc.org/upspin.io/dir/remote> package (responsible for talking to remote directory servers) wraps it with its own call to errors.E:

   const op errors.Op = "dir/remote.Lookup"

   ...

   return errors.E(op, pathName, err)

 There is no Kind set in this call, so the inner Kind (errors.NotExist) is lifted up during the construction of this Error struct.

 Finally, the upspin.io/client <https://godoc.org/upspin.io/client> package wraps the error once more:

   const op errors.Op = "client.Lookup"

   ...

   return errors.E(op, pathName, err)

 Preserving the structure of the server's error permits the client to know programmatically that this is a "not exist" error and that the item in question is "ann@example.com/file". The error's Error <https://godoc.org/upspin.io/errors#Error.Error> method can take advantage of this structure to suppress redundant fields. If the server error were merely an opaque string we would see the path name multiple times in the output.

 The critical details (the PathName and Kind) are pulled to the top of the error so they are more prominent in the display. The hope is that when seen by a user the first line of the error is usually all that's needed; the details below that are more useful when further diagnosis is required.

 Stepping back and looking at the error display as a unit, we can trace the path the error took from its creation back through various network-connected components to the client. The full picture might help the user but is sure to help the system implementer if the problem is unexpected or unusual.

 **Users and implementers**

 There is a tension between making errors helpful and concise for the end user versus making them expansive and analytic for the implementer. Too often the implementer wins and the errors are overly verbose, to the point of including stack traces or other overwhelming detail.

 Upspin's errors are an attempt to serve both the users and the implementers. The reported errors are reasonably concise, concentrating on information the user should find helpful. But they also contain internal details such as method names an implementer might find diagnostic but not in a way that overwhelms the user. In practice we find that the tradeoff has worked well.

 In contrast, a stack trace-like error is worse in both respects. The user does not have the context to understand the stack trace, and an implementer shown a stack trace is denied the information that could be presented if the server-side error was passed to the client. This is why Upspin error nesting behaves as an _operational_ trace, showing the path through the elements of the system, rather than as an _execution_ trace, showing the path through the code. The distinction is vital.

 For those cases where stack traces would be helpful, we allow the errors package to be built with the "debug" tag, which enables them. This works fine, but it's worth noting that we have almost never used this feature. Instead the default behavior of the package serves well enough that the overhead and ugliness of stack traces are obviated.

 **Matching errors**
