---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

## Defining Test Infrastructure

The techniques we’ve discussed so far cover sharing code across  methods in a single test class or suite.  Sometimes, it can also be valuable to share code across multiple test suites.  We refer to this sort of code as _test infrastructure_. Though it is usually more valuable in integration or end-to-end tests, carefully designed test infrastructure can make unit tests much easier to write in some circumstances.

Custom test infrastructure must be approached more carefully than the code sharing that happens within a single test suite. In many ways, test infrastructure code is more similar to production code than it is to other test code given that it can have many callers that depend on it and can be difficult to change without introducing breakages. Most engineers aren’t expected to make changes to the common test infrastructure while testing their own features. Test infrastructure needs to be treated as its own separate product, and accordingly, _test infrastructure must always have its own tests_.

Of course, most of the test infrastructure that most engineers use comes in the form of well-known third-party libraries like JUnit <https://junit.org>. A huge number of such libraries are available, and standardizing on them within an organization should happen as early and universally as possible. For example, Google many years ago mandated Mockito as the only mocking framework that should be used in new Java tests and banned new tests from using other mocking frameworks. This edict produced some grumbling at the time from people comfortable with other frameworks, but today, it’s universally seen as a good move that made our tests easier to understand and work with.   

# Conclusion

Unit tests are one of the most powerful tools that we as software engineers have to make sure that our systems keep working over time in the face of unanticipated changes. But with great power comes great responsibility, and careless use of unit testing can result in a system that requires much more effort to maintain and takes much more effort to change without actually improving our confidence in said system.

Unit tests at Google are far from perfect, but we’ve found tests that follow the practices outlined in this chapter to be orders of magnitude more valuable than those that don’t. We hope they’ll help you to improve the quality of your own tests!

# TL;DRs

-
Strive for unchanging tests.

-
Test via public APIs.

-
Test state, not interactions.

-
Make your tests complete and concise.

-
Test behaviors, not methods.

-
Structure tests to emphasize behaviors.

-
Name tests after the behavior being tested.

-
Don’t put logic in tests.

-
Write clear failure messages.

-
Follow DAMP over DRY when sharing  code for tests.

1Note that this is slightly different from a _flaky test_, which fails nondeterministically without any change to production code.

2This is sometimes called the "Use the front door first principle <https://oreil.ly/8zSZg>."

3These are also the same two reasons that a test can be "flaky." Either the system under test has a nondeterministic fault, or the test is flawed such that it sometimes fails when it should pass.

4See _https://testing.googleblog.com/2014/04/testing-on-toilet-test-behaviors-not.html_ <https://testing.googleblog.com/2014/04/testing-on-toilet-test-behaviors-not.html> and _https://dannorth.net/introducing-bdd_ <https://dannorth.net/introducing-bdd>.

5Furthermore, a _feature_ (in the product sense of the word) can be expressed as a collection of behaviors.

6These components are sometimes referred to as "arrange," "act," and "assert."

7In many cases, it can even be useful to slightly randomize the default values returned for fields that aren’t explicitly set. This helps to ensure that two different instances won’t accidentally compare as equal, and makes it more difficult for engineers to hardcode dependencies on the defaults.

CC BY-NC-ND 4.0 <https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode>
