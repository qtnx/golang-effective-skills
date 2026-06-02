---
source_name: "External Linked Documentation"
source_url: "https://commandcenter.blogspot.com/2017/12/error-handling-in-upspin.html"
source_path: "sources/raw/external/commandcenter-blogspot-com-2017-12-error-handling-in-upspin-html-e227930291.html"
license_ref: ""
---

An unexpected benefit of Upspin's custom error handling was the ease with which we could write error-dependent tests, as well as write error-sensitive code outside of tests. Two functions in the errors package enable these uses.
 The first is a function, called errors.Is <https://godoc.org/upspin.io/errors#Is>, that returns a boolean reporting whether the argument is of type *errors.Error and, if so, that its Kind field has the specified value.
   func Is(kind Kind, err error) bool
 This function makes it straightforward for code to change behavior depending on the error condition, such as in the face of a permission error as opposed to a network error:
   if errors.Is(errors.Permission, err) { ... }
 The other function, Match <https://godoc.org/upspin.io/errors#Match>, is useful in tests. It was created after we had been using the errors package for a while and found too many of our tests were sensitive to irrelevant details of the errors. For instance, a test might only need to check that there was a permission error opening a particular file, but was sensitive to the exact formatting of the error message.
 After fixing a number of brittle tests like this, we responded by writing a function to report whether the received error, err, matches an error template:
   func Match(template, err error) bool
 The function checks whether the error is of type *errors.Error, and if so, whether the fields within equal those within the template. The key is that it checks _only_ those fields that are non-zero in the template, ignoring the rest.
 For our example described above, one can write:
   if errors.Match(errors.E(errors.Permission, pathName), err) { … }
 and be unaffected by whatever other properties the error has. We use Match countless times throughout our tests; it has been a boon.
 **Lessons**
 There is a lot of discussion in the Go community about how to handle errors and it's important to realize that there is no single answer. No one package or approach can do what's needed for every program. As was pointed out elsewhere <https://blog.golang.org/errors-are-values>, errors are just values and can be programmed in different ways to suit different situations.
 The Upspin errors package has worked out well for us. We do not advocate that it is the right answer for another system, or even that the approach is right for anyone else. But the package worked well within Upspin and taught us some general lessons worth recording.
 The Upspin errors package is modest in size and scope. The original implementation was built in a few hours and the basic design has endured, with a few refinements, since then. A custom error package for another project should be just as easy to create. The specific needs of any given environment should be easy to apply. Don't be afraid to try; just think a bit first and be willing to experiment. What's out there now can surely be improved upon when the details of your own project are considered.
 We made sure the error constructor was both easy to use and easy to read. If it were not, programmers would resist using it.
 The behavior of the errors package is built in part upon the types intrinsic to the underlying system. This is a small but important point: No general errors package could do what ours does. It truly is a custom package.
 Moreover, the use of types to discriminate arguments allowed error construction to be idiomatic and fluid. This was made possible by a combination of the existing types in the system (PathName, UserName) and new ones created for the purpose (Op, Kind). Helper types made error construction clean, safe, and easy. It took a little more work—we had to create the types and use them everywhere, such as through the "const op" idiom—but the payoff was worthwhile.
 Finally, we would like to stress the lack of stack traces as part of the error model in Upspin. Instead, the errors package reports the sequence of events, often across the network, that resulted in a problem being delivered to the client. Carefully constructed errors that thread through the operations in the system can be more concise, more descriptive, and more helpful than a simple stack trace.
 Errors are for users, not just for programmers.
 _by Rob Pike and Andrew Gerrand_
   Newer Post <https://commandcenter.blogspot.com/2018/02/cerns-ipod-like-control-devices-from.html>   Older Post <https://commandcenter.blogspot.com/2017/10/the-upspin-manifesto-on-ownership-and.html>  Home <https://commandcenter.blogspot.com/>
