# Advent of Code 2025

Advent of Code 2025 solutions, under the following restrictions:
- no imports of any Python libraries
- all solutions completed within 24 hours
- no custom class creation of any kind
- no `eval()` or `exec()` where they can be avoided
- no AI!

## Rationale

I've been working with Python as my language of choice for nearly 10 years, due to it being extremely popular on its own and being extremely easy to turn concepts into executable code. One of the main reasons it's so popular is that it lends itself to be a very "batteries-included" language - for a lot of different use-cases, there tends to be a library that abstracts a lot of the underlying mechanics. 

One notable example of this is `networkx` for anything involving graphs, and especially for pathfinding. It's an extremely powerful library for many AoC problems involving pathfinding (moreso in previous years), but if someone without the knowledge of general pathfinding algorithms looks at the docs for the library and sees `networkx.shortest_path` as a function to use, they can plug it right into their code solutions and arrive at the right answer without learning anything new (other than using that function to achieve a result). 

I view the yearly challenges as a way to improve learning of fundamental concepts, and trivializing those concepts to "just call this one function" does no good. It's one thing to rely on those packages to do all the heavy lifting (like the shortest path function), but it's another thing entirely to implement different pathfinding algorithms and understand not only *how* they work, but *why* one should be chosen over another. In addition, you can run solutions on one device with those libraries guaranteed to be installed, but you'd have to install those same libraries on every other device that needs to run the solutions (which, on a very extreme end, might be too much of a hassle for the end user).

As a result, I try to achieve a **complete self-ban** on all external Python libraries.

On its own, that would usually be enough. However, an  easy extrapolation to make off of this is by noticing what other functionality exists inside Python's standard library. Examples that come to mind include `heapq`, `bisect`, and `collections`. It's very handy to know that these libraries exist, especially when doing Leetcode problems or in Leetcode-style technical interviews, when *any* proper solution is acceptable. However, when looking across different languages, you cannot guarantee that libraries with similar functionality exist - C, for example, might not have an easily discoverable library that mimics `collections`, and especially not one that's built into the library itself. 

So, to make cross-language translation easy (and to allow other people proficient in *other* languages to understand how/why a solution works), I also self-ban **the entire Python standard library**. 

Batteries are no longer included.