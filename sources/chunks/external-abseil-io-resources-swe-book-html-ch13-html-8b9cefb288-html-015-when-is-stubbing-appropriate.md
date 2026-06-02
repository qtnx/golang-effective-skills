---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## When Is Stubbing Appropriate?

Rather than a catch-all replacement for a real implementation, stubbing is appropriate  when you need a function to return a specific value to get the system under test into a certain state, such as Using stubbing to simulate responses that requires the system under test to return a non-empty list of transactions. Because a function’s behavior is defined inline in the test, stubbing can simulate a wide variety of return values or errors that might not be possible to trigger from a real implementation or a fake.

To ensure its purpose is clear, each stubbed function should have a direct relationship with the test’s assertions.  As a result, a test typically should stub out a small number of functions because stubbing out many functions can lead to tests that are less clear. A test that requires many functions to be stubbed can be a sign that stubbing is being overused, or that the system under test is too complex and should be refactored.

Note that even when stubbing is appropriate, real implementations or fakes are still preferred because they don’t expose implementation details and they give you more guarantees about the correctness of the code compared to stubbing. But stubbing can be a reasonable technique to use, as long as its usage is constrained so that tests don’t become overly complex.  

# Interaction Testing

As discussed earlier in this chapter, interaction testing is a way to validate how a function  is called without  actually calling the implementation of the function.

Mocking frameworks make it easy to perform interaction testing. However, to keep tests useful, readable, and resilient to change, it’s important to perform interaction testing only when necessary.
