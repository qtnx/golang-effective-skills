---
source_name: "External Linked Documentation"
source_url: "https://dave.cheney.net/2014/10/17/functional-options-for-friendly-apis"
source_path: "sources/raw/external/dave-cheney-net-2014-10-17-functional-options-for-friendly-apis-fd693013a6.html"
license_ref: ""
---

I’m an amateur hardware hacker, and many of the devices I work with use a USB serial interface. A so a few months ago I wrote a terminal handling package <https://github.com/pkg/term>.
In the prior version of this package, to open a serial device, change the speed and set the terminal to raw mode, you’d have to do each of these steps individually, checking the error at every stage.
Even though this package is trying to provide a friendlier interface on an even lower level interface, it still left too many procedural warts for the user.
Let’s take a look at the package after applying the functional options pattern.
 <https://dave.cheney.net/wp-content/uploads/2014/10/Screenshot-from-2014-10-15-034321.png>
By converting the `Open` function to use a variadic parameter of function values, we get a much cleaner API.
In fact, it’s not just the `Open` API that improves, the grind of setting an option, checking an error, setting the next option, checking the error, that is gone as well.
The default case, still just takes one argument, the name of the device.
For more complicated use cases, configuration functions, defined in the `term` package, are passed to the `Open` function and are applied in order before returning.
This is the same pattern we saw in the previous example, the only thing that is different is rather than being anonymous, these are public functions. In all other respects their operation is identical.
We’ll take a look at how `Speed`, `RawMode`, and `Open`, are implemented on the next slide.
 <https://dave.cheney.net/wp-content/uploads/2014/10/Screenshot-from-2014-10-15-034413.png>
`RawMode` is the easiest to explain. It just a function whose signature is compatible with Open.
Because `RawMode` is declared in the same package as `Term`, it can access the private fields and call private methods declared on the `Term` type, in this case calling the private `setRawMode` helper.
`Speed` is also just a regular function, however it does not match the signature `Open` requires. This is because `Speed` itself requires an argument; the baud rate.
`Speed` returns an anonymous function which is compatible with the `Open` function’s signature, which closes over the baud rate parameter, capturing it for later when the function is applied.
Inside the call to `Open`, we first open the terminal device with the `openTerm` helper.
Next, just as before, we range over the slice of options functions, calling each one in turn passing in `t`, the pointer to our `term.Term` value.
If there is an error applying any function then we stop at that point, clean up and return the error to the caller.
Otherwise, returning from the function, we’ve now created and configured a Term value to the caller’s specifications.
 <https://dave.cheney.net/wp-content/uploads/2014/10/Screenshot-from-2014-10-15-034503.png>
In summary
- Functional options let you write APIs that can grow over time.
- They enable the default use case to be the simplest.
- They provide meaningful configuration parameters.
- Finally they give you access to the entire power of the language to initialize complex values.
In this talk, I have presented many of the existing configuration patterns, those considered idiomatic and commonly in use today, and at every stage asked questions like:
- Can this be made simpler ?
- Is that parameter necessary ?
- Does the signature of this function make it easy for it to be used safely ?
- Does the API contain traps or confusing misdirection that will frustrate ?
I hope I have inspired you to do the same. To revisit code that you have written in the past and pose yourself these same questions and thereby improve it.
 <https://dave.cheney.net/wp-content/uploads/2014/10/Screenshot-from-2014-10-15-034543.png>
Thank you.
