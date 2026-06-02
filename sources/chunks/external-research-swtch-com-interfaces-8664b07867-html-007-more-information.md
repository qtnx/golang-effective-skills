---
source_name: "External Linked Documentation"
source_url: "https://research.swtch.com/interfaces"
source_path: "sources/raw/external/research-swtch-com-interfaces-8664b07867.html"
license_ref: ""
---

### More Information

The interface runtime support is in `$GOROOT/src/pkg/runtime/iface.c <http://code.google.com/p/go/source/browse/src/pkg/runtime/iface.c>`. There's much more to say about interfaces (we haven't even seen an example of a pointer receiver yet) and the type descriptors (they power reflection in addition to the interface runtime) but those will have to wait for future posts.

### Code

Supporting code (`x.go`):

```go

package main

import (
 "fmt"
 "strconv"
)

type Stringer interface {
 String() string
}

type Binary uint64

func (i Binary) String() string {
 return strconv.Uitob64(i.Get(), 2)
}

func (i Binary) Get() uint64 {
 return uint64(i)
}

func main() {
 b := Binary(200)
 s := Stringer(b)
 fmt.Println(s.String())
}

```

Selected output of `8g -S x.go`:

```go

0045 (x.go:25) LEAL    s+-24(SP),BX
0046 (x.go:25) MOVL    4(BX),BP
0047 (x.go:25) MOVL    BP,(SP)
0048 (x.go:25) MOVL    (BX),BX
0049 (x.go:25) MOVL    20(BX),BX
0050 (x.go:25) CALL    ,BX

```

The `LEAL` loads the address of `s` into the register `BX`. (The notation `_n_(SP)` describes the word in memory at `SP+_n_`. `0(SP)` can be shortened to `(SP)`.) The next two `MOVL` instructions fetch the value from the second word in the interface and store it as the first function call argument, `0(SP)`. The final two `MOVL` instructions fetch the itable and then the function pointer from the itable, in preparation for calling that function.

-
rog peppe <http://www.blogger.com/profile/00839344798030831980> (December 2, 2009 2:42 AM) _Go's interfaces let you use duck typing like you would in a purely dynamic language like Python_

this has been said a lot, but i don't think it's quite true. duck typing goes deeper. for instance, if i've got an API for doing arithmetic:

**
type Foo struct { ... };

func (f0 *Foo)Add(f1 *Foo) *Foo;
func (f0 *Foo)Negate() *Foo;
**
etc

with duck typing, this is compatible with any other type that responds to the same methods, _including methods on objects that its methods return_. if interfaces were really like duck typing, then the above struct would be compatible with this interface:

**
type Arith interface {
    Add(f1 Arith) Arith;
    Negate() Arith;
}
**

but it's not.

-
Fred Blasdel <http://www.blogger.com/profile/08057528812732998703> (December 2, 2009 3:26 AM) It's kind of worse than that rog: the Go language doesn't itself use the polymorphism mechanism it provides to its users (Interfaces), and the ones it does use (the parametricity of Array and Map) are for its use only.

They're understandably afraid of overloading, and classicist counter-revolutionaries could perturb the public development of the language (see Prototype.js for a particularly ironic and depressing example). They have to be careful about what they add.

_I don't know whether Go is the first language to use this technique, but it's certainly not a common one._

I'm sure this is discussed in Cardelli and Abadi's "A Theory of Objects", but I don't have a copy of my own. I'd bet Rob has one you could borrow :)

-
Kalani <http://www.blogger.com/profile/01810792034258816216> (December 2, 2009 6:41 AM) Fred, I don't know why there should be any fear of overloading here (though you've put your finger on some major problems with this language). Especially with the poor String/toString example, somebody should have immediately seen a need to introduce overloading. Hopefully there's a better justification for accepting the unnecessary time/space overhead (and more importantly the logical/reasoning overhead) that goes along with runtime type-tag checking.

It's a shame -- the authors of Go should have read Mark Jones's dissertation on qualified types. Without polymorphic recursion, they could statically construct all necessary "interfaces" for primitive types and have a much nicer 'toString' function (not to mention a million other examples).

These guys missed a great chance to seriously advance the state of "system programming."

-
Evan Jones <http://www.blogger.com/profile/02694440592772191857> (December 10, 2009 4:31 PM) Re: Method lookup performance. It seems to me that the example shown for Method lookup performance is not quite "fair." The issue, I think, for Javascript and Python, is that the call to s.String() could call a different method on each loop iteration, if the code changes the type or the instance.

Go is a bit more static, and I don't think this is possible. If Python/Javascript forbid changing methods on an object, then the method lookup could be recognized by an optimizer as being constant, and hoisted out of the loop.

But I haven't thought about this too hard, so I could be wrong.

-
Tom <http://www.blogger.com/profile/13912039839233620950> (July 18, 2010 8:57 AM) _I don't know whether Go is the first language to use this technique, but it's certainly not a common one._

Haskell TypeClasses are implemented using a similar technique - each type (or set of types) implementing a typeclass is associated with a method table (called a **dictionary**) that is passed to functions requiring values of said typeclass.

-
Squire <http://www.blogger.com/profile/06702358341689436900> (October 14, 2010 9:45 AM) _
I don't know whether Go is the first language to use this technique, but it's certainly not a common one.
_

Emerald computed lookup tables dynamically; we called them "AbCon vectors", because they converted from the abstract type (aka interface), known at compile time, to the concrete type of the object (aka class), which was sometimes know only at runtime. We also cached the AbCons.

Emerald also did typechecking more or less as you have described it in Go, with interfaces being structural (programmers didn't have to _claim_ that they implemented an interface, they just had to do it), checking being static when possible but otherwise dynamic, and allowing run-time type interrogation and checked run-time conversions. Emerald also had methods with multiple return values and "comma assignments".

Are you sure that you didn't peek?

-
Russ Cox <http://swtch.com/~rsc/> (October 14, 2010 7:46 PM) @Squire:

Wow.

I'm about halfway through the 2007 retrospective paper about Emerald and my blog post pictures might as well have been lifted from Figure 3.

I'm sure we didn't peek, but I think it's interesting how similar the backgrounds of the team members are. In the case of Go, Rob brought the concurrency ideas via Hoare's CSP, Robert brought the object sensibilities of a Smalltalk programmer, and Ken brought the focus on C-quality performance that led to essentially the same data structures Emerald used 25 years ago. That characterization obviously oversimplifies, but you can see the same backgrounds coming together in the paper's description of the original Emerald team.

It's very cool to see not only that other people explored this space years ago but also that they arrived at essentially the same design. The fact that this design point has been discovered multiple times by independent groups makes it seem somehow more fundamental.

Thanks so much for pointing this out. Finding out about these kinds of connections is such a thrill.

-
Drew LeSueur <http://www.blogger.com/profile/05828569029365447689> (December 5, 2010 2:42 AM) Thanks so much for the tutorial. Your code at the end really helped me understand some Go basics

-
Anonymous (June 5, 2011 7:43 PM) "It's very cool " -- It's not cool at all; it indicates insufficient search of the literature, which one can see throughout the design of Go. Experienced language designers look at Go and just shake their heads. But it's Rob Pike and Ken Thompson! Yes, exactly -- a couple of clever strongly opinionated eccentrics, whose idiosyncratic ideas, not deep knowledge of language design, drive the design of Go. We can see the same thing in Perl and in Java -- idiosyncrasies in opposite directions. And then there's D, which is a trainwreck because its author treats it like a personal project. Google could have hired Walter Bright and turned D into the far better alternative to C++ that it had the potential to be in the beginning -- although they could have done better yet by hiring someone like Martin Odersky.

-
jam <http://www.blogger.com/profile/17344213294371886790> (July 31, 2011 7:33 AM) One trick I noticed was missing was:
 stringer = s.String
 for i ...
 print stringer()

Namely being able to pull out the attribute lookup outside the loop. I use that a lot, especially for comprehensions.

For go, it could still be helpful to avoid the extra indirections. But go doesn't seem to allow for bound functions and using:
 F = func() string { return s.String() }

Actually makes things a lot worse.

-
Consultoria RH <http://www.luizpaschoal.com.br> (December 11, 2011 9:56 AM) Este blog é uma representação exata de competências. Eu gosto da sua recomendação. Um grande conceito que reflete os pensamentos do escritor. Consultoria RH <http://www.luizpaschoal.com.br>
