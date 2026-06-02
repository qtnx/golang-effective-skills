---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Seams

Code is said to be _testable_ <https://oreil.ly/yssV2> if it is written in a way that makes it possible to write unit tests for  the code.   A _seam_ <https://oreil.ly/pFSFf> is a way to make code testable by allowing for the use of test doubles—it makes it possible to use different dependencies for the system under test rather than the dependencies used in a production environment.

_Dependency injection_ <https://oreil.ly/og9p9> is a common technique for introducing seams.  In short, when a class utilizes dependency injection, any classes it needs to use (i.e., the class’s _dependencies_) are passed to it rather than instantiated directly, making it possible for these dependencies to be substituted in tests.

Dependency injection shows an example of dependency injection. Rather than the constructor creating an instance of `CreditCardService`, it accepts an instance as a parameter.
  Example 13-4. Dependency injection
```go

class PaymentProcessor {
  private CreditCardService creditCardService;

  PaymentProcessor(**CreditCardService creditCardService**) {
    this.creditCardService = creditCardService;
  }
  ...
}
```

The code that calls this constructor is responsible for creating an appropriate `CreditCardService` instance. Whereas the production code can pass in an implementation of `CreditCardService` that communicates with an external server, the test can pass in a test double, as demonstrated in Passing in a test double.
  Example 13-5. Passing in a test double
```go

PaymentProcessor paymentProcessor =
    new PaymentProcessor(new **TestDoubleCreditCardService**());
```

To reduce boilerplate associated with manually specifying constructors, automated dependency injection frameworks can be used for constructing object graphs automatically.  At Google, Guice <https://github.com/google/guice> and Dagger <https://google.github.io/dagger> are automated dependency injection frameworks that are commonly used for Java code.

With dynamically typed languages such as Python or JavaScript, it is possible to dynamically replace individual functions or object methods. Dependency injection is less important in these languages because this capability makes it possible to use real implementations of dependencies in tests while only overriding functions or methods of the dependency that are unsuitable for tests.

Writing testable code requires an upfront investment.  It is especially critical early in the lifetime of a codebase because the later testability is taken into account, the more difficult it is to apply to a codebase. Code written without testing in mind typically needs to be refactored or rewritten before you can add appropriate tests.
