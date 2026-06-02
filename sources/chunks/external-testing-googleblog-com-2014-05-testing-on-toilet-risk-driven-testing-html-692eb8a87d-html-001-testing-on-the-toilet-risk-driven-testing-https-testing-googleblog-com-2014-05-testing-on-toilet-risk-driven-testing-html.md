---
source_name: "External Linked Documentation"
source_url: "https://testing.googleblog.com/2014/05/testing-on-toilet-risk-driven-testing.html"
source_path: "sources/raw/external/testing-googleblog-com-2014-05-testing-on-toilet-risk-driven-testing-html-692eb8a87d.html"
license_ref: ""
---

Google Testing Blog: Testing on the Toilet: Risk-Driven Testing
##   Testing on the Toilet: Risk-Driven Testing  <https://testing.googleblog.com/2014/05/testing-on-toilet-risk-driven-testing.html>
      _by Peter Arrenbrecht_

 _This article was adapted from a Google Testing on the Toilet <http://googletesting.blogspot.com/2007/01/introducing-testing-on-toilet.html> (TotT) episode. You can download a printer-friendly version <https://docs.google.com/document/d/1QfmhsvpiCx__rcU0sr03Lu1fM1yhE8P9atyTgeLbRAQ/edit?usp=sharing> of this TotT episode and post it in your office. _

 **We are all conditioned to write tests** as we code: unit, functional, UI—the whole shebang. We are professionals, after all. Many of us like how small tests let us work quickly, and how larger tests inspire safety and closure. Or we may just anticipate flak during review. We are so used to these tests that often **we no longer question why we write them**. This can be wasteful and dangerous.

 **Tests are a means to an end:** To **reduce the key risks** of a project, and to **get the biggest bang for the buck**. This bang may not always come from the tests that standard practice has you write, or not even from tests at all.

 Two examples:

  _“We built a new debugging aid. We wrote unit, integration, and UI tests. We were ready to launch.”_

 Outstanding practice. **Missing the mark.**

 Our key risks were that we'd corrupt our data or bring down our servers for the sake of a debugging aid. None of the tests addressed this, but they gave a false sense of safety and “being done”.
 **We stopped the launch.**

  _“We wanted to turn down a feature, so we needed to alert affected users. Again we had unit and integration tests, and even one expensive end-to-end test.”_

 Standard practice. **Wasted effort.**

 The alert was so critical it actually needed end-to-end coverage for all scenarios. But it would be live for only three releases. The cheapest effective test? Manual testing before each release.

 **A Better Approach: Risks First **

 For every project or feature, **think about testing**. Brainstorm your key risks and your best options to reduce them. **Do this at the start** so you don't waste effort and can adapt your design. **Write them down** as a QA design so you can point to it in reviews and discussions.

 To be sure, **standard practice remains a good idea in most cases** (hence it’s standard). Small tests are cheap and speed up coding and maintenance, and larger tests safeguard core use-cases and integration.

 **Just remember**: Your tests are a means. **The bang is what counts**. It’s your job to **maximize it**.

####  1 comment :

-

The term "cheapest effective test" is a great choice of words -- a great reminder for both manual and automation testers to communicate effectively especially in the test planning phase! Test planning should to take into account the for the "bang for the buck" and "return on investment" for manual and automated testing effort from the get go.
ReplyDelete <https://www.blogger.com/comment/delete/15045980/3751070536254843965>
Replies
Reply

Add comment

Load more...

   _  _  <https://testing.googleblog.com/>   _  _  <https://testing.googleblog.com/2014/06/gtac-2014-coming-to-seattlekirkland-in.html>    _  _  <https://testing.googleblog.com/2014/05/testing-on-toilet-effective-testing.html>

    _  _

## Feed
  <http://googletesting.blogspot.com/atom.xml>
