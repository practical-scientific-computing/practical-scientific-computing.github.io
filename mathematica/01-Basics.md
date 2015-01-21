---
title: Basics
ordering: 1
layout: default
group: Mathematica
type: tutorial
---

# Basics of *Mathematica*

## Syntax

Evaluate input with "Shift-Enter".
Variable names cannot start with a number.

```
x = 1
x1234 = 2
2 x
```

You cannot change the value of predefined variables, like Pi or E.  
If Mathematica currently holds a value for a variable, it shows up in black; if it is undefined, then it shows up in blue.  
 If you want the decimal approximation of a number, use `N[number]`

```
{E, e, Pi, applesauce}
N[{E, e, Pi, applesauce}]
```

You can remove the value of a variable using Clear[...]

```
Clear[x, x1234]
```

**Square brackets** are used for function arguments;
**Parentheses** are used for order of operations;
**Curly brackets** denote lists

```
func = Sin[x]
poly = (x + y)^2
list = {w, x, y, z}
list2 = {a, b, c, d}
```

## Help Menus

The built-in Help in Mathematica is amazing.  If you don't know what something does or how it's used, either press F1 or use

```
?LegendreP
```

```
?? Plot
```

```
?*Bessel*
```

## List Manipulations

```
list = {w, x, y, z}
list2 = {a, b, c, d}
```

Take an *element* of the list

```
list[[2]]
```

Multiply a list by a constant

```
2 list
```

take the dot product of two lists

```
list.list2
```

remove a piece of the list with **Drop** or select a specific part of a list with **Take**

```
Drop[list, 1]
Drop[list, -1]
Take[list, 2]
```

```
list3 = Union[list, list2]
```

```
Partition[list3, 2]
```

```
listInt = Table[i, {i, 1, 12}]
listSq = Table[i^2, {i, 1, 12}]
Transpose[{listInt, listSq}]
```

```
MatrixForm[{listInt, listSq}]
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

(Semicolons suppress the output of a command)

```
func = Sin[x];
func2[x_] = Sin[x];

N[func /. x -> 1]
N[func2[1]]
```

## Basic Plotting

```
Plot[Sin[x]^2, {x, 0, 2 Pi}]
```

```
ListPlot[pairs, ImageSize -> Large]
```

## Integrals and Derivatives

```
D[Sin[w t], t]
D[BesselJ[n, x], x]
```

```
psi[x_] = A Sin[3 x];
Integrate[psi[x]^2, {x, -a, a}]
```

```
Integrate[(Sin[t^2]^4 - 10 Tan[2 t])/Csc[t], t]
N[% /. t -> 0]
```

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
