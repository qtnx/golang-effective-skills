---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html"
source_path: "sources/raw/external/testing-googleblog-com-2015-01-testing-on-toilet-change-detector-tests-html-10bff6cc6f.html"
license_ref: ""
---

Google Testing Blog: Testing on the Toilet: Change-Detector Tests Considered Harmful
##   Testing on the Toilet: Change-Detector Tests Considered Harmful  <https://testing.googleblog.com/2015/01/testing-on-toilet-change-detector-tests.html>
      _by Alex Eagle

 This article was adapted from a Google Testing on the Toilet <http://googletesting.blogspot.com/2007/01/introducing-testing-on-toilet.html> (TotT) episode. You can download a printer-friendly version <https://docs.google.com/document/d/13k8AsgYdF-2TJx9QIHHvPiuV3JMbsrMLkWmmjdYBLVg/edit?usp=sharing> of this TotT episode and post it in your office. _

 You have just finished refactoring some code without modifying its behavior. Then you run the tests before committing and… a bunch of unit tests are failing. **While fixing the tests, you get a sense that you are wasting time by mechanically applying the same transformation to many tests.** Maybe you introduced a parameter in a method, and now must update 100 callers of that method in tests to pass an empty string.

 **What does it look like to write tests mechanically?** Here is an absurd but obvious way:

```go
// Production code:
def abs(i: Int)
  return (i < 0) ? i * -1 : i

// Test code:
for (line: String in File(prod_source).read_lines())
  switch (line.number)
    1: assert line.content equals "def abs(i: Int)"
    2: assert line.content equals "  return (i < 0) ? i * -1 : i"
```

 **That test is clearly not useful**: it contains an exact copy of the code under test and acts like a checksum. **A correct or incorrect program is equally likely to pass** a test that is a derivative of the code under test. No one is really writing tests like that, but how different is it from this next example?

```go
// Production code:
def process(w: Work)
  firstPart.process(w)
  secondPart.process(w)

// Test code:
part1 = mock(FirstPart)
part2 = mock(SecondPart)
w = Work()
Processor(part1, part2).process(w)
verify_in_order
  was_called part1.process(w)
  was_called part2.process(w)
```

 It is tempting to write a test like this because it requires little thought and will run quickly. **This is a change-detector test**—it is a transformation of the same information in the code under test—and **it breaks in response to any change to the production code, without verifying correct behavior** of either the original or modified production code.

 **Change detectors provide negative value**, since the tests do not catch any defects, and the added maintenance cost slows down development. These tests should be re-written or deleted.

####  2 comments :

-

This topic is very much related to that of testing behavior versus implementation. In this case, the examples given are very simple. What if your process function looked more like this :

def process(w: Work)
 firstResult = firstPart.process(w)
 secondPart.process(w, firstResult)

In this case, would it not be acceptable for your unit test to validate that the secondPart's process method is being called with the result of the firstPart.process as parameter? Or perhaps a slightly more complex case, one where the Processor modifies the result from the firstPart's process and passes that to the secondPart.

Writing unit tests that are not change detectors sounds like a good objective. But, when coding in a system that is very service oriented, it is not always possible to write unit tests that are not change detectors and that test only behavior as opposed to implementation. In those cases, writing tests that validate function calls seems like the fastest way to achieve confidence that your code works.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/8028448860298130774>
Replies
-

There are also other aspects on testing than just running your code. Good written tests document your code and help others getting around. Tests provide a safety net for refactoring. Change-detector tests as described above do not add any clarity, and you cannot safely refactor stuff if you know for sure that you need to adapt the tests afterwards to get them passing again.

When you think about your example: can you really be "confident that your code works"? What if someone completely changes firstPart - your test would still pass, because you mock everything, even if the process function might not work anymore.
Delete <https://www.blogger.com/comment/delete/15045980/2563666534509864769>
Replies
Reply

Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2015/02/the-first-annual-testing-on-toilet.html>    _  _  <https://testing.googleblog.com/2015/01/testing-on-toilet-prefer-testing-public.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
