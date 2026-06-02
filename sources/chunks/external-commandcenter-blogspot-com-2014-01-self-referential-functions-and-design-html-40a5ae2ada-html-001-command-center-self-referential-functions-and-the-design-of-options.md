---
source_name: "External Linked Documentation"
source_url: "http://commandcenter.blogspot.com/2014/01/self-referential-functions-and-design.html"
source_path: "sources/raw/external/commandcenter-blogspot-com-2014-01-self-referential-functions-and-design-html-40a5ae2ada.html"
license_ref: ""
---

command center: Self-referential functions and the design of options
###  Self-referential functions and the design of options
   I've been trying on and off to find a nice way to deal with setting options in a Go <http://golang.org/> package I am writing. Options on a type, that is. The package is intricate and there will probably end up being dozens of options. There are many ways to do this kind of thing, but I wanted one that felt nice to use, didn't require too much API (or at least not too much for the user to absorb), and could grow as needed without bloat.
 I've tried most of the obvious ways: option structs, lots of methods, variant constructors, and more, and found them all unsatisfactory. After a bunch of trial versions over the past year or so, and a lot of conversations with other Gophers making suggestions, I've finally found one I like. You might like it too. Or you might not, but either way it does show an interesting use of self-referential functions.
 I hope I have your attention now.
 Let's start with a simple version. We'll refine it to get to the final version.
 First, we define an option type. It is a function that takes one argument, the Foo we are operating on.
 type option func(*Foo)
 The idea is that an option is implemented as a function we call to set the state of that option. That may seem odd, but there's a method in the madness.
 Given the option type, we next define an Option method on *Foo that applies the options it's passed by calling them as functions. That method is defined in the same package, say pkg, in which Foo is defined.
 This is Go, so we can make the method variadic and set lots of options in a given call:
 // Option sets the options specified.
 func (f *Foo) Option(opts ...option) {
   for _, opt := range opts {
      opt(f)
   }
 }
 Now to provide an option, we define in pkg a function with the appropriate name and signature. Let's say we want to control verbosity by setting an integer value stored in a field of a Foo. We provide the verbosity option by writing a function with the obvious name and have it return an option, which means a closure; inside that closure we set the field:
 // Verbosity sets Foo's verbosity level to v.
 func Verbosity(v int) option {
   return func(f *Foo) {
      f.verbosity = v
   }
 }
 Why return a closure instead of just doing the setting? Because we don't want the user to have to write the closure and we want the Option method to be nice to use. (Plus there's more to come....)
 In the client of the package, we can set this option on a Foo object by writing:
 foo.Option(pkg.Verbosity(3))
 That's easy and probably good enough for most purposes, but for the package I'm writing, I want to be able to use the option mechanism to set temporary values, which means it would be nice if the Option method could return the previous state. That's easy: just save it in an empty interface value that is returned by the Option method and the underlying function type. That value flows through the code:
 type option func(*Foo) interface{}
 // Verbosity sets Foo's verbosity level to v.
 func Verbosity(v int) option {
   return func(f *Foo) interface{} {
      previous := f.verbosity
       f.verbosity = v
      return previous
   }
 }
 // Option sets the options specified.
 // It returns the previous value of the last argument.
 func (f *Foo) Option(opts ...option) (previous interface{}) {
   for _, opt := range opts {
      previous = opt(f)
   }
   return previous
 }
 The client can use this the same as before, but if the client also wants to restore a previous value, all that's needed is to save the return value from the first call, and then restore it.
 prevVerbosity := foo.Option(pkg.Verbosity(3))
 foo.DoSomeDebugging()
 foo.Option(pkg.Verbosity(prevVerbosity.(int)))
 The type assertion in the restoring call to Option is clumsy. We can do better if we push a little harder on our design.
 First, redefine an option to be a function that sets a value and returns _another option_ to restore the previous value.
 type option func(f *Foo) option
 This self-referential function definition is reminiscent of a state machine. Here we're using it a little differently: it's a function that returns its _inverse_.
 Then change the return type (and meaning) of the Option method of *Foo to option from interface{}:
 // Option sets the options specified.
 // It returns an option to restore the last arg's previous value.
 func (f *Foo) Option(opts ...option) (previous option) {
   for _, opt := range opts {
       previous = opt(f)
   }
   return previous
 }
 The final piece is the implementation of the actual option functions. Their inner closure must now return an option, not an interface value, and that means it must return a closure to undo itself. But that's easy: it can just recur to prepare the closure to undo the original! It looks like this:
 // Verbosity sets Foo's verbosity level to v.
 func Verbosity(v int) option {
   return func(f *Foo) option {
      previous := f.verbosity
      f.verbosity = v
      return Verbosity(previous)
   }
 }
 Note the last line of the inner closure changed from
      return previous
 to
      return Verbosity(previous)
 Instead of just returning the old value, it now calls the surrounding function (Verbosity) to create the undo closure, and returns that _closure_.
 Now from the client's view this is all very nice:
 prevVerbosity := foo.Option(pkg.Verbosity(3))
 foo.DoSomeDebugging()
 foo.Option(prevVerbosity)
 And finally we take it up one more level, using Go's defer <http://blog.golang.org/defer-panic-and-recover> mechanism to tidy it all up in the client:
 func DoSomethingVerbosely(foo *Foo, verbosity int) {
   // Could combine the next two lines,
   // with some loss of readability.
   prev := foo.Option(pkg.Verbosity(verbosity))
   defer foo.Option(prev)
   // ... do some stuff with foo under high verbosity.
 }
  It's worth noting that since the "verbosity" returned is now a closure, not a verbosity value, the actual previous value is hidden. If you want that value you need a little more magic, but there's enough magic for now.
 The implementation of all this may seem like overkill but it's actually just a few lines for each option, and has great generality. Most important, it's really nice to use from the point of view of the package's client. I'm finally happy with the design. I'm also happy at the way this uses Go's closures to achieve its goals with grace.
   Newer Post <https://commandcenter.blogspot.com/2014/08/prints.html>   Older Post <https://commandcenter.blogspot.com/2013/05/eisenbahnnet-bohrs-trip-about-spin.html>  Home <https://commandcenter.blogspot.com/>
### Implementing the transcendental functions in Ivy <https://commandcenter.blogspot.com/2026/01/implementing-transcendental-functions.html>
 Towards the end of 2014, in need of pleasant distraction, I began writing, in Go, my second pseudo-APL, called Ivy. Over the years, Ivy'...
-       <https://commandcenter.blogspot.com/2024/01/what-we-got-right-what-we-got-wrong.html>
 What We Got Right, What We Got Wrong <https://commandcenter.blogspot.com/2024/01/what-we-got-right-what-we-got-wrong.html>
   This is my closing talk ( video ) from the GopherConAU conference in Sydney, given November 10, 2023, the 14th anniversary of Go being lau...
-   Less is exponentially more <https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html>
  Here is the text of the talk I gave at the Go SF meeting in June, 2012. This is a personal talk. I do not speak for anyone else on the Go...
-   Self-referential functions and the design of options <https://commandcenter.blogspot.com/2014/01/self-referential-functions-and-design.html>
 I've been trying on and off to find a nice way to deal with setting options in a Go package I am writing. Options on a type, that is. T...
-  Home <https://commandcenter.blogspot.com/>
   Except as noted, the content of this page is licensed under the Creative Commons Attribution 3.0 License.
