---
source_name: "External Linked Documentation"
source_url: "https://abseil.io/resources/swe-book/html/ch12.html"
source_path: "sources/raw/external/abseil-io-resources-swe-book-html-ch12-html-f0fc7050d3.html"
license_ref: ""
---

# Unit Testing

Software Engineering at Google
# Unit Testing
Written by Erik Kuefler
Edited by Tom Manshreck
The previous chapter introduced two of the main axes along which Google classifies tests: _size_ and _scope_.  To recap, size refers to the resources consumed by a test and what it is allowed to do, and scope refers to how much code a test is intended to validate. Though Google has clear definitions for test size, scope tends to be a little fuzzier. We use the term _unit test_ to refer to tests of relatively narrow scope, such as of a single class or method. Unit tests are usually small in size, but this isn’t always the case.
After preventing bugs, the most important purpose of a test is to improve engineers’ productivity.  Compared to broader-scoped tests, unit tests have many properties that make them an excellent way to optimize productivity:
-
They tend to be small according to Google’s definitions of test size.  Small tests are fast and deterministic, allowing developers to run them frequently as part of their workflow and get immediate feedback. 
-
They tend to be easy to write at the same time as the code they’re testing, allowing engineers to focus their tests on the code they’re working on without having to set up and understand a larger system.
-
They promote high levels of test coverage because they are quick and easy to write. High test coverage allows engineers to make changes with confidence that they aren’t breaking anything.
-
They tend to make it easy to understand what’s wrong when they fail because each test is conceptually simple and focused on a particular part of the system.
-
They can serve as documentation and examples, showing engineers how to use the part of the system being tested and how that system is intended to work.
Due to their many advantages, most tests written at Google are unit tests, and as a rule of thumb, we encourage engineers to aim for a mix of about 80% unit tests and 20% broader-scoped tests. This advice, coupled with the ease of writing unit tests and the speed with which they run, means that engineers run a _lot_ of unit tests—it’s not at all unusual for an engineer to execute thousands of unit tests (directly or indirectly) during the average workday.
Because they make up such a big part of engineers’ lives, Google puts a lot of focus on _test maintainability_. Maintainable tests  are ones that "just work": after writing them, engineers don’t need to think about them again until they fail, and those failures indicate real bugs with clear causes. The bulk of this chapter focuses on exploring the idea of maintainability and techniques for achieving it.
# The Importance of Maintainability
Imagine this scenario: Mary wants to add a simple  new feature to the product and is able to implement it quickly, perhaps requiring only a couple dozen lines of code. But when she goes to check in her change, she gets a screen full of errors back from the automated testing system. She spends the rest of the day going through those failures one by one. In each case, the change introduced no actual bug, but broke some of the assumptions that the test made about the internal structure of the code, requiring those tests to be updated. Often, she has difficulty figuring out what the tests were trying to do in the first place, and the hacks she adds to fix them make those tests even more difficult to understand in the future. Ultimately, what should have been a quick job ends up taking hours or even days of busywork, killing Mary’s productivity and sapping her morale.
Here, testing had the opposite of its intended effect by draining productivity rather than improving it while not meaningfully increasing the quality of the code under test. This scenario is far too common, and Google engineers struggle with it every day. There’s no magic bullet, but many engineers at Google have been working to develop sets of patterns and practices to alleviate these problems, which we encourage the rest of the company to follow.
The problems Mary ran into weren’t her fault, and there was nothing she could have done to avoid them: bad tests must be fixed before they are checked in, lest they impose a drag on future engineers. Broadly speaking, the issues she encountered fall into two categories. First, the tests she was working with were _brittle_: they broke in response to a harmless and unrelated change that introduced no real bugs. Second, the tests were _unclear_: after they were failing, it was difficult to determine what was wrong, how to fix it, and what those tests were supposed to be doing in the first place.
# Preventing Brittle Tests
As just defined, a  brittle test  is one that fails in the face of an unrelated change to production code that does not introduce any real bugs.1 Such tests must be diagnosed and fixed by engineers as part of their work. In small codebases with only a few engineers, having to tweak a few tests for every change might not be a big problem. But if a team regularly writes brittle tests, test maintenance will inevitably consume a larger and larger proportion of the team’s time as they are forced to comb through an increasing number of failures in an ever-growing test suite. If a set of tests needs to be manually tweaked by engineers for each change, calling it an "automated test suite" is a bit of a stretch!
Brittle tests cause pain in codebases of any size, but they become particularly acute at Google’s scale. An individual engineer might easily run thousands of tests in a single day during the course of their work, and a single large-scale change (see Large-Scale Changes) can trigger hundreds of thousands of tests. At this scale, spurious breakages that affect even a small percentage of tests can waste huge amounts of engineering time. Teams at Google vary quite a bit in terms of how brittle their test suites are, but we’ve identified a few practices and patterns that tend to make tests more robust to change.
