---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## Mocking Frameworks

A _mocking framework_ is a  software  library that makes it easier to create test doubles within tests; it allows you to replace an object with a _mock_, which is a test double whose behavior is specified inline in a test. The use of mocking frameworks reduces boilerplate because you don’t need to define a new class each time you need a test double.

Mocking frameworks demonstrates the  use of Mockito <https://site.mockito.org>, a mocking framework for Java. Mockito creates a test double for `CreditCardService` and instructs it to return a specific value.
  Example 13-6. Mocking frameworks
```go

class PaymentProcessorTest {
  ...
  PaymentProcessor paymentProcessor;

  // Create a test double of CreditCardService with just one line of code.
  **@Mock CreditCardService mockCreditCardService**;
  @Before public void setUp() {
    // Pass in the test double to the system under test.
    paymentProcessor = new PaymentProcessor(**mockCreditCardService**);
  }
  @Test public void chargeCreditCardFails_returnFalse() {
    // Give some behavior to the test double: it will return false
    // anytime the chargeCreditCard() method is called. The usage of
    // “any()” for the method’s arguments tells the test double to
    // return false regardless of which arguments are passed.
    when(**mockCreditCardService.chargeCreditCard(**any(), any())
       .thenReturn(**false**);
    boolean success = paymentProcessor.makePayment(CREDIT_CARD, AMOUNT);
    assertThat(success).isFalse();
  }
}
```

Mocking frameworks  exist for most  major programming languages.  At Google, we use Mockito for Java, the googlemock component of Googletest <https://github.com/google/googletest> for C++, and unittest.mock <https://oreil.ly/clzvH> for Python. 

Although mocking frameworks facilitate easier usage of test doubles, they come with some significant caveats given that their overuse will often make a codebase more difficult to maintain. We cover some of these problems later in this chapter.

# Techniques for Using Test Doubles

There are three primary techniques for using test doubles.  This section presents a brief introduction to these techniques to give you a quick overview of what they are and how they differ. Later sections in this chapter go into more details on how to effectively apply them.

An engineer who is aware of the distinctions between these techniques is more likely to know the appropriate technique to use when faced with the need to use a test double.
