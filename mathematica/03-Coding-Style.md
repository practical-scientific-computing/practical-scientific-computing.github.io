---
title: Loops and Modules
ordering: 3
layout: default
group: Mathematica
type: tutorial
---

# *Mathematica* Loops and Modules

## Overview


* Scope
* Loops
* Module

## Scope

**TO DO**

## Looping methods

There are many ways to impliment loops in *Mathematica*, here we will stick to the base 3 types:

* Table
* Do
* While

#### Table 

```
?Table
```

The **Table** function is used when you want to loop over a list and return a list as a result. An example is making a list of the squares

``` mma
Table[x^2,{x,1,10}]
```

#### Do 

```
?Do
```

The **Do** function is useful for looping over a set of instructions a fixed amount of times.
This function is analogous to the loops in *python*, *C* and *fortran*. 

``` mma
Do[Print[n^2], {n, 4}]
```

Note that this will not make a list like **Table** would have and also that any variables in the do loop have a global scope. 
This can be rectified by using a **Module** as will be seen later in this tuorial.

#### While

```
?While
```

The while loop is similar to a **Do** loop but rather than running a fixed amount of loops, it will continually test a Boolean expression until it returns false.

```
x = 1.;
While[x > 0.001,
 Print[x];
 x = x/2.;
]
```

## Modules


### Coding Paradigm

Creating a library of functions to perform many repetitive tasks can be performed in mathematica easily. 
When coding up this library of functions, you need to be careful about what variables are declared globally to avoid overwriting variables set in another part of the code.
This might seem like a complicated case but even a small number of functions can suffer from sharing global variables. 

As an example, consider writing two functions, `Ave` and `QuadVar`, which find the average and the quadratic variation of a list of numbers.
If both of these functions use a `temp` variable to store the sum you have a risk of overwriting the value of the temp variable. 

A module allows the use of variables local to the function itself that cannot be modified by any other function.
This takes the place of the scope of local variables in other languages like python or C.
Evaluating mutiple sets of the same module will not affect the local varibles to each call.

Lets look at the help for module

``` mma
?Module
```

``` mma
Module[{x}, Print[x]; Attributes[x]]
```

You will see from this code that x is not really x, it is `x$###` and it has attributes *Temporary* which means that it will be released from the memory after the module returns.

### Module of Riemann's Zeta function

$$ \zeta(x) = \sum_{n=1}^{\infty} \frac{1}{n^x} $$

``` mma
zetaModule[x_] := Module[{xLocal = x, sumLocal = 0.0},
  Do[sumLocal += 1/n^(xLocal);
   , {n, 1, 1000000}];
  sumLocal
  ]

zetaModule[2.]

Zeta[2.]
```

## Exercises

1. Write a module that will evaluate the Bessel function of the first kind ($J_{\alpha}$) to the m=1000 term.  Use the $\Gamma$-function (`Gamma`) defined in *Mathematica*.

$$ J_{\alpha }(x)=\sum _{m=0}^{\infty } \frac{(-1)^m}{m!(\Gamma  (a+m+1)}\left(\frac{x}{2}\right)^{\alpha +2 m} $$

