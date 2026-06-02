command center: Regular expressions in lexing and parsing

###  Regular expressions in lexing and parsing
   Comments extracted from a code review. I've been asked to disseminate them more widely.

  I should say something about regular expressions in lexing and parsing. Regular expressions are hard to write, hard to write well, and can be expensive relative to other technologies. (Even when they are implemented correctly in N*M time, they have significant overheads, especially if they must capture the output.)  Lexers, on the other hand, are fairly easy to write correctly (if not as compactly), and very easy to test. Consider finding alphanumeric identifiers. It's not too hard to write the regexp (something like "[a-ZA-Z_][a-ZA-Z_0-9]*"), but really not much harder to write as a simple loop. The performance of the loop, though, will be much higher and will involve much less code under the covers. A regular expression library is a big thing. Using one to parse identifiers is like using a Mack truck to go to the store for milk. And when we want to adjust our lexer to admit other character types, such as Unicode identifiers, and handle normalization, and so on, the hand-written loop can cope easily but the regexp approach will break down.

 A similar argument applies to parsing. Using regular expressions to explore the parse state to find the way forward is expensive, overkill, and error-prone. Standard lexing and parsing techniques are so easy to write, so general, and so adaptable there's no reason to use regular expressions. They also result in much faster, safer, and compact implementations.

  Another way to look at it is that lexers and parsing are matching statically-defined patterns, but regular expressions' strength is that they provide a way to express patterns dynamically. They're great in text editors and search tools, but when you know at compile time what all the things are you're looking for, regular expressions bring far more generality and flexibility than you need.

  Finally, on the point about writing well. Regular expressions are, in my experience, widely misunderstood and abused. When I do code reviews involving regular expressions, I fix up a far higher fraction of the regular expressions in the code than I do regular statements. This is a sign of misuse: most programmers (no finger pointing here, just observing a generality) simply don't know what they are or how to use them correctly.  Encouraging regular expressions as a panacea for all text processing problems is not only lazy and poor engineering, it also reinforces their use by people who shouldn't be using them at all.

 So don't write lexers and parsers with regular expressions as the starting point. Your code will be faster, cleaner, and much easier to understand and to maintain.

   Newer Post <https://commandcenter.blogspot.com/2011/09/we-open-in-well-lit-corporate.html>   Older Post <https://commandcenter.blogspot.com/2010/08/know-your-science.html>  Home <https://commandcenter.blogspot.com/>

### Implementing the transcendental functions in Ivy <https://commandcenter.blogspot.com/2026/01/implementing-transcendental-functions.html>

 Towards the end of 2014, in need of pleasant distraction, I began writing, in Go, my second pseudo-APL, called Ivy. Over the years, Ivy'...

-       <https://commandcenter.blogspot.com/2024/01/what-we-got-right-what-we-got-wrong.html>
 What We Got Right, What We Got Wrong <https://commandcenter.blogspot.com/2024/01/what-we-got-right-what-we-got-wrong.html>
   This is my closing talk ( video ) from the GopherConAU conference in Sydney, given November 10, 2023, the 14th anniversary of Go being lau...

-   Less is exponentially more <https://commandcenter.blogspot.com/2012/06/less-is-exponentially-more.html>
  Here is the text of the talk I gave at the Go SF meeting in June, 2012. This is a personal talk. I do not speak for anyone else on the Go...

-   Self-referential functions and the design of options <https://commandcenter.blogspot.com/2014/01/self-referential-functions-and-design.html>
 I've been trying on and off to find a nice way to deal with setting options in a Go package I am writing. Options on a type, that is. T...

-  Home <https://commandcenter.blogspot.com/>

   Except as noted, the content of this page is licensed under the Creative Commons Attribution 3.0 License.

## About Me
     rob  <https://www.blogger.com/profile/18259238879445421354>   View my complete profile <https://www.blogger.com/profile/18259238879445421354>

## Blog Archive

-    ►     2026  <https://commandcenter.blogspot.com/2026/> (1)
-    ►     January  <https://commandcenter.blogspot.com/2026/01/> (1)

-    ►     2025  <https://commandcenter.blogspot.com/2025/> (1)
-    ►     February  <https://commandcenter.blogspot.com/2025/02/> (1)

-    ►     2024  <https://commandcenter.blogspot.com/2024/> (1)
-    ►     January  <https://commandcenter.blogspot.com/2024/01/> (1)

-    ►     2023  <https://commandcenter.blogspot.com/2023/> (1)
-    ►     December  <https://commandcenter.blogspot.com/2023/12/> (1)

-    ►     2022  <https://commandcenter.blogspot.com/2022/> (1)
-    ►     August  <https://commandcenter.blogspot.com/2022/08/> (1)

-    ►     2020  <https://commandcenter.blogspot.com/2020/> (6)
-    ►     September  <https://commandcenter.blogspot.com/2020/09/> (1)

-    ►     April  <https://commandcenter.blogspot.com/2020/04/> (1)

-    ►     January  <https://commandcenter.blogspot.com/2020/01/> (4)

-    ►     2019  <https://commandcenter.blogspot.com/2019/> (2)
-    ►     November  <https://commandcenter.blogspot.com/2019/11/> (1)

-    ►     January  <https://commandcenter.blogspot.com/2019/01/> (1)

-    ►     2018  <https://commandcenter.blogspot.com/2018/> (1)
-    ►     February  <https://commandcenter.blogspot.com/2018/02/> (1)

-    ►     2017  <https://commandcenter.blogspot.com/2017/> (4)
-    ►     December  <https://commandcenter.blogspot.com/2017/12/> (1)

-    ►     October  <https://commandcenter.blogspot.com/2017/10/> (1)

-    ►     September  <https://commandcenter.blogspot.com/2017/09/> (1)

-    ►     February  <https://commandcenter.blogspot.com/2017/02/> (1)

-    ►     2014  <https://commandcenter.blogspot.com/2014/> (2)
-    ►     August  <https://commandcenter.blogspot.com/2014/08/> (1)

-    ►     January  <https://commandcenter.blogspot.com/2014/01/> (1)

-    ►     2013  <https://commandcenter.blogspot.com/2013/> (1)
-    ►     May  <https://commandcenter.blogspot.com/2013/05/> (1)

-    ►     2012  <https://commandcenter.blogspot.com/2012/> (3)
-    ►     September  <https://commandcenter.blogspot.com/2012/09/> (1)

-    ►     June  <https://commandcenter.blogspot.com/2012/06/> (1)

-    ►     April  <https://commandcenter.blogspot.com/2012/04/> (1)

-    ▼     2011  <https://commandcenter.blogspot.com/2011/> (3)
-    ►     December  <https://commandcenter.blogspot.com/2011/12/> (1)

-    ►     September  <https://commandcenter.blogspot.com/2011/09/> (1)

-    ▼     August  <https://commandcenter.blogspot.com/2011/08/> (1)
- Regular expressions in lexing and parsing <https://commandcenter.blogspot.com/2011/08/regular-expressions-in-lexing-and.html>

-    ►     2010  <https://commandcenter.blogspot.com/2010/> (1)
-    ►     August  <https://commandcenter.blogspot.com/2010/08/> (1)

-    ►     2008  <https://commandcenter.blogspot.com/2008/> (2)
-    ►     April  <https://commandcenter.blogspot.com/2008/04/> (2)

-    ►     2006  <https://commandcenter.blogspot.com/2006/> (2)
-    ►     June  <https://commandcenter.blogspot.com/2006/06/> (1)

-    ►     April  <https://commandcenter.blogspot.com/2006/04/> (1)

-    ►     2004  <https://commandcenter.blogspot.com/2004/> (2)
-    ►     June  <https://commandcenter.blogspot.com/2004/06/> (1)

-    ►     May  <https://commandcenter.blogspot.com/2004/05/> (1)
