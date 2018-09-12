# Algorithms

Literature:
* Course [Algorithms, Part I from Princeton University on Coursera](https://www.coursera.org/learn/algorithms-part1).

## Requirements
* Req.

## To Do
* For JAVA code, look into the structure at https://en.wikipedia.org/wiki/Apache_Maven
* Do general unit tests:
    * smoke test (add one connrction and test it)
    * create 2 connecting components and test it
* Translate the code to Python and C++? See [Support for other programming languages](https://github.com/kevin-wayne/algs4)

## Learning Notes

### Scientific Approach to Designing and Analyzing Algorithms
Steps to develop a usable algorithm:
1. Model the problem.
2. Find an algorithm to solve it.
3. Fast enough? Fits in memory?
4. If not, figure out why.
5. Find a way to address the problem.
6. Iterate until satisfied.

### Dynamic Connectivity (Union-Find) Problem

#### Model of the problem
* Objects: Given a set of objects _N_.
    * Convenient to name objects _0_ to _N-1_ when programming.
        * Use integers as array index. 
    * Suppress details not relevant to union-find.
* Connections: Connection between 2 objects.
    * Union command: connect 2 objects.
    * Connection is an equivalence relation:
        * Reflexive: _p_ is connected to _p_.
        * Symmetric: if _p_ is connected to _q_, then _q_ is connected to _p_.
        * Transitive: if _p_ is connected to _q_ and _q_ is connected to _r_, then _p_ is connected to _r_.
    * _Connected compontent_: a maximal set of objects that is a mutually connected.
        * A set of objects and connections divide into subsets called connected components. 
* Key part of the problem: Find or connected query.
    * Find/connected query: is there a path connecting 2 objects?

#### Applications
* Computers in network.
* Friends in a social network.
* Elements in a mathematical set.
* Pixels in a digital photo.
* Transistors in a computer chip.

#### Algorithms
* Algorithms gain efficiency by maintaining connected components and using that knowledge to efficiently answer the find/connected query.
* Operations:
    * Find query: check if two objects are in the same connected component.
    * Union command: replace connected components containing the two objects with their union.
* Goal: Design efficient data structure for union-find.
    * Number of objects _N_ can be huge.
    * Number of operations _M_ can be huge.
    * Find queries and union commands may be intermixed.

## Recommended Readings
* Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne, Addison-Wesley Professional, 2011.
    * Synopses of the textbook and Java code available [online](https://algs4.cs.princeton.edu/home/).