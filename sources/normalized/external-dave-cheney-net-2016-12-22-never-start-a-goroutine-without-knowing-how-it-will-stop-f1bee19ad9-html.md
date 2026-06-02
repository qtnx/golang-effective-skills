Never start a goroutine without knowing how it will stop | Dave Cheney
In Go, goroutines are cheap to create and efficient to schedule. The Go runtime has been written for programs with tens of thousands of goroutines as the norm, hundreds of thousands are not unexpected. But goroutines do have a finite cost in terms of memory footprint; you cannot create an infinite number of them.

Every time you use the `go` keyword in your program to launch a goroutine, you must know how, and when, that goroutine will exit. If you don’t know the answer, that’s a potential memory leak.

Consider this trivial code snippet:

```go
ch := somefunction()
go func() {
        for range ch { }
}()
```

This code obtains a channel of `int` from `somefunction` and starts a goroutine to drain it. When will this goroutine exit? It will only exit when `ch` is closed. When will that occur? It’s hard to say, `ch` is returned by `somefunction.` So, depending on the state of `somefunction,` `ch` might never be closed, causing the goroutine to quietly leak.

In your design, some goroutines may run until the program exits, for example a background goroutine watching a configuration file, or the main `conn.Accept` loop in your server. However, these goroutines are rare enough I don’t consider them an exception to this rule.

Every time you write the statement `go` in a program, you should consider the question of how, and under what conditions, the goroutine you are about to start, will end.

### Related posts:

- Why is a Goroutine’s stack infinite ? <https://dave.cheney.net/2013/06/02/why-is-a-goroutines-stack-infinite>
- Curious Channels <https://dave.cheney.net/2013/04/30/curious-channels>
- Struct composition with Go <https://dave.cheney.net/2015/05/22/struct-composition-with-go>
- Threads are a strange abstraction <https://dave.cheney.net/2016/03/30/threads-are-a-strange-abstraction>

### Elsewhere

- LinkedIn <https://www.linkedin.com/in/davecheney>
- Serverfault <http://serverfault.com/users/301/dave-cheney>
- Stackoverflow <http://stackoverflow.com/users/6449/dave-cheney>

### Categories

- Economy <https://dave.cheney.net/category/economy>
- Go <https://dave.cheney.net/category/golang>
- Hardware Hacking <https://dave.cheney.net/category/hardware-hacking>
- History <https://dave.cheney.net/category/history>
- Internets of interest <https://dave.cheney.net/category/internets-of-interest>
- Photography <https://dave.cheney.net/category/photography>
- Programming <https://dave.cheney.net/category/programming-2>
- Retrochallenge <https://dave.cheney.net/category/retrochallenge>
- Small ideas <https://dave.cheney.net/category/small-ideas>
- Uncategorized <https://dave.cheney.net/category/uncategorized>
- Useless Trivia <https://dave.cheney.net/category/useless-trivia>

### Archives

- December 2025 <https://dave.cheney.net/2025/12>
- November 2025 <https://dave.cheney.net/2025/11>
- February 2024 <https://dave.cheney.net/2024/02>
- January 2021 <https://dave.cheney.net/2021/01>
- December 2020 <https://dave.cheney.net/2020/12>
- June 2020 <https://dave.cheney.net/2020/06>
- May 2020 <https://dave.cheney.net/2020/05>
- April 2020 <https://dave.cheney.net/2020/04>
- March 2020 <https://dave.cheney.net/2020/03>
- February 2020 <https://dave.cheney.net/2020/02>
- December 2019 <https://dave.cheney.net/2019/12>
- November 2019 <https://dave.cheney.net/2019/11>
- October 2019 <https://dave.cheney.net/2019/10>
- September 2019 <https://dave.cheney.net/2019/09>
- August 2019 <https://dave.cheney.net/2019/08>
- July 2019 <https://dave.cheney.net/2019/07>
- June 2019 <https://dave.cheney.net/2019/06>
- May 2019 <https://dave.cheney.net/2019/05>
- April 2019 <https://dave.cheney.net/2019/04>
- February 2019 <https://dave.cheney.net/2019/02>
- January 2019 <https://dave.cheney.net/2019/01>
- December 2018 <https://dave.cheney.net/2018/12>
- November 2018 <https://dave.cheney.net/2018/11>
- October 2018 <https://dave.cheney.net/2018/10>
- September 2018 <https://dave.cheney.net/2018/09>
- August 2018 <https://dave.cheney.net/2018/08>
- July 2018 <https://dave.cheney.net/2018/07>
- May 2018 <https://dave.cheney.net/2018/05>
- January 2018 <https://dave.cheney.net/2018/01>
- December 2017 <https://dave.cheney.net/2017/12>
- November 2017 <https://dave.cheney.net/2017/11>
- September 2017 <https://dave.cheney.net/2017/09>
- August 2017 <https://dave.cheney.net/2017/08>
- July 2017 <https://dave.cheney.net/2017/07>
- June 2017 <https://dave.cheney.net/2017/06>
- April 2017 <https://dave.cheney.net/2017/04>
- March 2017 <https://dave.cheney.net/2017/03>
- February 2017 <https://dave.cheney.net/2017/02>
- January 2017 <https://dave.cheney.net/2017/01>
- December 2016 <https://dave.cheney.net/2016/12>
- November 2016 <https://dave.cheney.net/2016/11>
- October 2016 <https://dave.cheney.net/2016/10>
- September 2016 <https://dave.cheney.net/2016/09>
- August 2016 <https://dave.cheney.net/2016/08>
- June 2016 <https://dave.cheney.net/2016/06>
- May 2016 <https://dave.cheney.net/2016/05>
- April 2016 <https://dave.cheney.net/2016/04>
- March 2016 <https://dave.cheney.net/2016/03>
- February 2016 <https://dave.cheney.net/2016/02>
- January 2016 <https://dave.cheney.net/2016/01>
- December 2015 <https://dave.cheney.net/2015/12>
- November 2015 <https://dave.cheney.net/2015/11>
- October 2015 <https://dave.cheney.net/2015/10>
- September 2015 <https://dave.cheney.net/2015/09>
- August 2015 <https://dave.cheney.net/2015/08>
- July 2015 <https://dave.cheney.net/2015/07>
- June 2015 <https://dave.cheney.net/2015/06>
- May 2015 <https://dave.cheney.net/2015/05>
- March 2015 <https://dave.cheney.net/2015/03>
- February 2015 <https://dave.cheney.net/2015/02>
- January 2015 <https://dave.cheney.net/2015/01>
- December 2014 <https://dave.cheney.net/2014/12>
- November 2014 <https://dave.cheney.net/2014/11>
- October 2014 <https://dave.cheney.net/2014/10>
- September 2014 <https://dave.cheney.net/2014/09>
- August 2014 <https://dave.cheney.net/2014/08>
- July 2014 <https://dave.cheney.net/2014/07>
- June 2014 <https://dave.cheney.net/2014/06>
- May 2014 <https://dave.cheney.net/2014/05>
- April 2014 <https://dave.cheney.net/2014/04>
- March 2014 <https://dave.cheney.net/2014/03>
- February 2014 <https://dave.cheney.net/2014/02>
- January 2014 <https://dave.cheney.net/2014/01>
- December 2013 <https://dave.cheney.net/2013/12>
- November 2013 <https://dave.cheney.net/2013/11>
- October 2013 <https://dave.cheney.net/2013/10>
- September 2013 <https://dave.cheney.net/2013/09>
- August 2013 <https://dave.cheney.net/2013/08>
- July 2013 <https://dave.cheney.net/2013/07>
- June 2013 <https://dave.cheney.net/2013/06>
- May 2013 <https://dave.cheney.net/2013/05>
- April 2013 <https://dave.cheney.net/2013/04>
- January 2013 <https://dave.cheney.net/2013/01>
- December 2012 <https://dave.cheney.net/2012/12>
- November 2012 <https://dave.cheney.net/2012/11>
- October 2012 <https://dave.cheney.net/2012/10>
- September 2012 <https://dave.cheney.net/2012/09>
- August 2012 <https://dave.cheney.net/2012/08>
- February 2012 <https://dave.cheney.net/2012/02>
- January 2012 <https://dave.cheney.net/2012/01>
- November 2011 <https://dave.cheney.net/2011/11>
- October 2011 <https://dave.cheney.net/2011/10>
- August 2011 <https://dave.cheney.net/2011/08>
- July 2011 <https://dave.cheney.net/2011/07>
- June 2011 <https://dave.cheney.net/2011/06>
- May 2011 <https://dave.cheney.net/2011/05>
- April 2011 <https://dave.cheney.net/2011/04>
- March 2011 <https://dave.cheney.net/2011/03>
- February 2011 <https://dave.cheney.net/2011/02>
- November 2010 <https://dave.cheney.net/2010/11>
- October 2010 <https://dave.cheney.net/2010/10>

### License
  <https://creativecommons.org/licenses/by-nc-sa/4.0/>
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
