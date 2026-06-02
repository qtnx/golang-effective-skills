---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch13.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch13-html-8b9cefb288.html"
license_ref: ""
---

# Test Doubles

## How to Decide When to Use a Real Implementation

A real implementation is preferred if it is fast, deterministic, and has simple dependencies.   For example, a real implementation should be used for a _value object_ <https://oreil.ly/UZiXP>. Examples include an amount of money, a date, a geographical address, or a collection class such as a list or a map.

However, for more complex code, using a real implementation often isn’t feasible. There might not be an exact answer on when to use a real implementation or a test double given that there are trade-offs to be made, so you need to take the following considerations into account.

### Execution time

One of the most important qualities of unit tests is that they  should be fast—you want to  be able to continually  run them during development so that you can get quick feedback on whether your code is working (and you also want them to finish quickly when run in a CI system). As a result, a test double can be very useful when the real implementation is slow.

How slow is too slow for a unit test? If a real implementation added one millisecond to the running time of each individual test case, few people would classify it as slow. But what if it added 10 milliseconds, 100 milliseconds, 1 second, and so on?

There is no exact answer here—it can depend on whether engineers feel a loss in productivity, and how many tests are using the real implementation (one second extra per test case may be reasonable if there are five test cases, but not if there are 500). For borderline situations, it is often simpler to use a real implementation until it becomes too slow to use, at which point the tests can be updated to use a test double instead.

Parallelization of tests  can also help reduce execution time. At Google, our test infrastructure makes it trivial to split up tests in a test suite to be executed across multiple servers. This increases the cost of CPU time, but it can provide a large savings in developer time. We discuss this more in Build Systems and Build Philosophy.

Another trade-off to be aware of: using a real implementation can result in increased build times given that the tests need to build the real implementation as well as all of its dependencies. Using a highly scalable build system like Bazel <https://bazel.build> can help because it caches unchanged build artifacts.

### Determinism

A test is _deterministic_ <https://oreil.ly/brxJl> if, for a given version of the  system under test, running the test always results in the same outcome; that is, the test either always passes or always fails.  In contrast, a test is _nondeterministic_ <https://oreil.ly/5pG0f> if its outcome can change, even if the system under test remains unchanged.  

Nondeterminism in tests <https://oreil.ly/71OFU> can lead to flakiness—tests can occasionally fail even when there are no changes to the system under test.  As discussed in Testing Overview, flakiness harms the health of a test suite if developers start to distrust the results of the test and ignore failures. If use of a real implementation rarely causes flakiness, it might not warrant a response, because there is little disruption to engineers. But if flakiness happens often, it might be time to replace a real implementation with a test double because doing so will improve the fidelity of the test.

A real implementation can be much more complex compared to a test double, which increases the likelihood that it will be nondeterministic. For example, a real implementation that utilizes multithreading might occasionally cause a test to fail if the output of the system under test differs depending on the order in which the threads are executed.

A common cause of nondeterminism is code that is not hermetic <https://oreil.ly/aes__>; that is, it has dependencies  on external services that are outside the control of a test.  For example, a test that tries to read the contents of a web page from an HTTP server might fail if the server is overloaded or if the web page contents change. Instead, a test double should be used to prevent the test from depending on an external server. If using a test double is not feasible, another option is to use a hermetic instance of a server, which has its life cycle controlled by the test. Hermetic instances are discussed in more detail in the next chapter.

Another example of nondeterminism is code that relies on the system clock given that the output of the system under test can differ depending on the current time. Instead of relying on the system clock, a test can use a test double that hardcodes a specific time.

### Dependency construction

When using a real  implementation, you need to construct all of its dependencies.  For example, an object needs its entire dependency tree to be constructed: all objects that it depends on, all objects that these dependent objects depend on, and so on. A test double often has no dependencies, so constructing a test double can be much simpler compared to constructing a real implementation.

As an extreme example, imagine trying to create the object in the code snippet that follows in a test. It would be time consuming to determine how to construct each individual object. Tests will also require constant maintenance because they need to be updated when the signature of these objects’ constructors is modified:

```go

Foo foo = new Foo(new A(new B(new C()), new D()), new E(), ..., new Z());
```

It can be tempting to instead use a test double because constructing one can be trivial. For example, this is all it takes to construct a test double when using the Mockito mocking framework:

```go

@Mock Foo mockFoo;
```

Although creating this test double is much simpler, there are significant benefits to using the real implementation, as discussed earlier in this section. There are also often significant downsides to overusing test doubles in this way, which we look at later in this chapter. So, a trade-off needs to be made when considering whether to use a real implementation or a test double.

Rather than manually constructing the object in tests, the ideal solution is to use the same object construction code that is used in the production code, such as a factory method or automated dependency injection. To support the use case for tests, the object construction code needs to be flexible enough to be able to use test doubles rather than hardcoding the  implementations  that will be used  for production. 

# Faking

If using a real implementation is not feasible within a test, the best option is often to use a fake in its place.   A fake is preferred over other test double techniques because it behaves similarly to the real implementation: the system under test shouldn’t even be able to tell whether it is interacting with a real implementation or a fake. A fake file system illustrates a fake file system.
  Example 13-11. A fake file system
```go

// This fake implements the FileSystem interface. This interface is also
// used by the real implementation.
public class **FakeFileSystem** implements **FileSystem** {
  // Stores a map of file name to file contents. The files are stored in
  // memory instead of on disk since tests shouldn’t need to do disk I/O.
  private Map<String, String> **files** = new HashMap<>();
  @Override
  public void **writeFile**(String fileName, String contents) {
    // Add the file name and contents to the map.
    **files**.add(fileName, contents);
  }
  @Override
  public String **readFile**(String fileName) {
    String contents = **files**.get(fileName);
    // The real implementation will throw this exception if the
    // file isn’t found, so the fake must throw it too.
    if (contents == null) { throw new FileNotFoundException(fileName); }
    return contents;
  }
}
```
