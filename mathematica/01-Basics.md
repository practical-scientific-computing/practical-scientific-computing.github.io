---
title: Basics
ordering: 1
layout: default
group: Mathematica
type: tutorial
---

# Basics of *Mathematica*

## Syntax

Welcome to *Mathematica*!

First things are first: you evaluate input by selecting a cell and pressing "Shift-Enter".
You assign values to a variable using `=`; the names of a variables cannot start with a number.

```
x = 1
x1234 = 2
2 x
```

You cannot change the value of predefined variables, like `Pi` or `E`.  
If *Mathematica* currently holds a value for a variable, it shows up in **black**; if it is undefined, then it shows up in **blue**.  
 
*Mathematica* tries to be exact unless you specify otherwise; if you want the decimal approximation of a number, use `N[number]`

```
{E, e, Pi, applesauce}
N[{E, e, Pi, applesauce}]
```

You can remove the value of a variable using `Clear[x]`

```
Clear[x, x1234]
```

**Square brackets** are used for function arguments;
**Parentheses** are used for order of operations;
**Curly brackets** denote lists.

```
func = Sin[x]
poly = (x + y)^2
list = {w, x, y, z}
list2 = {a, b, c, d}
```

## Help Menus

The built-in Help in *Mathematica* is amazing.  If you don't know what something does or how it's used, either press F1 or use `?` with the function name:

```
?LegendreP
```

You can find more information by using `??` before the function:

```
?? Plot
```

`*` is a wildcard; `Plot*`, for example, will return every function which starts with the characters "Plot".  You can use two of them at once as well:

```
?*Bessel*
```

## List Manipulations

As we stated, curly brackets denote lists.

```
list = {w, x, y, z}
list2 = {a, b, c, d}
```

Two square brackets take only the specified element of the list:

```
list[[2]]
```

Lists in *Mathematica* are much like vectors; nested lists (i.e. lists of lists) represent matrices.

Multiplication by a constant is pretty straightforward:

```
2 list
```

You can take the dot product of two lists:

```
list.list2
```

It's sometimes useful to remove a piece of the list with `Drop` or select a specific part of a list with `Take`:

```
Drop[list, 1]
Drop[list, -1]
Take[list, 2]
```

To make two lists into one (`Union` also removes duplicated elements):

```
list3 = Union[list, list2]
```

To split a long list into a series of sublists:

```
Partition[list3, 2]
```

You can generate lists by hand using curly brackets, but `Table` does it automatically by evaluating an expression which runs over the index:

```
listInt = Table[i, {i, 1, 12}]
listSq = Table[i^2, {i, 1, 12}]
```

You can make two lists into a list of ordered pairs using `Transpose`:

```
Transpose[{listInt, listSq}]
```

## Replacement Rules vs Functions

```
list
```

You can temporarily set the value of a variable using the following commands:

```
list /. x -> 2
list /. {w -> 1, y -> 3}
```

(Semicolons suppress the output of a command, by the way.)

User-defined functions can take any number of arguments, but you have to specify them initially.

```
func2[x_] = Sin[x];
func3[a_,b_,c_] = a + b^2 + c^4;
```

(Note the necessary underscores!)

Evaluaion of functions is easy!
```
N[func2[1]]

N[func3[2,4,10]
```

If you don't define the argument of a function, then you can still work with it using replacement rules:

```
func = Sin[x];

N[func /. x -> 1]
```

## Basic Plotting

Visualization in *Mathematica* is an intricate subject; we will take it up in detail later.  For now, only the basics.

Continuous functions can be plotted using `Plot`:

```
Plot[Sin[x]^2, {x, 0, 2 Pi}, ImageSize -> Large]
```

For lists, you use `ListPlot`:

```
ListPlot[pairs, ImageSize -> Large]
```

## Integrals and Derivatives

Usually, functions in *Mathematica* are fully spelled out.  Not so for derivatives!  The function is just a capital `D`.

```
D[Sin[w t], t]
D[BesselJ[n, x], x]
```

*Mathematica* can do both definite and indefinite integrals:

```
psi[x_] = A Sin[3 x];
Integrate[psi[x]^2, {x, -a, a}]
```

```
int = Integrate[(Sin[t^2]^4 - 10 Tan[2 t])/Csc[t], t]
N[int /. t -> 0]
```

As we all know, some integrals don't have exact solutions (or they are really tough to find).  You can do a numerical integration using `NIntegrate`.

```
NIntegrate[x^2/(E^x - 1), {x, 0, Infinity}]
```

## A Bunch of Shortcuts

* To make a cell into a text cell, use Alt-7
  * (There are a bunch more formatting options with Alt-number)
* To make Greek letters, type Esc-letter-Esc (e.g. Esc-o-Esc gives \[Omega])
* Superscripts: Ctrl-6 (e.g. x^2)
* Subscripts: Ctrl - (Control-dash, e.g. Subscript[x, 2]) 
* To put comments into input cells, use `(* ... *)`
  * (You can also highlight the comment and type Alt-/ )
* To abort the evaluation of a cell, use Alt-. (use when things get stuck!)
