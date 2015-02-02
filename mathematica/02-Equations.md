---
title: Equations
ordering: 2
layout: default
group: Mathematica
type: tutorial
---

# Solving Equations in *Mathematica*

## Syntax

"=" is an *assignment* operator; it fixes the LHS to be equal to the RHS.  A variable can be assigned many types of values: Numbers, functions, lists, even whole equations.

```Mathematica
z = 1
p = a x^2 + b x + c
rep = {a -> 1, b -> 2, c -> 3}
```

"==" is a *comparison* operator; it compares the LHS to the RHS and returns "true" or "false".  == can be used in conjunction with = to assign an equation to a single variable.

```Mathematica
z == 1
z == 2
equation = x^2 == y
```

## Solving Equations Algebraically

`Solve[equation, x]` finds the solution to an equation, or a system of equations contained in a list:

```Mathematica
Solve[a x^2 + b x + c == 0, x]
Solve[{x^2 + x == 2 w, 3 x^2 - 2 == w}, {x, w}]
```

(Note that the output of `Solve` is a list of replacement rules, not an assignment.)

The number of equations must be equal to the number of variables.  To reduce the equations by removing one variable, use `Eliminate[{eq1, eq2}, x]`:

```Mathematica
Eliminate[{x^2 + x == 2 w, 3 x^2 - 2 == w}, x]
```

For differential equations, `DSolve[eq1, x[t], t]` finds the general solution x[t]
(You can use an apostrophe *in a differential equation* instead of the extraneous `D[x[t], t]`

```Mathematica
DSolve[x''[t] + \[Omega]^2 x[t] == 0, x[t], t]
```

It also works for a system of equations, just like `Solve`:

```Mathematica
DSolve[{x''[t] + \[Omega]1^2 x[t] == 0, 
  y'[t] + \[Omega]2^2 x[t] == 0}, {x[t], y[t]}, t]
```

The general solution contains arbitrary constants C[n].  For boundary value problems, include boundary conditions!

```Mathematica
DSolve[{x''[t] + \[Omega]^2 x[t] == 0, x[0] == 1, x'[1] == 2}, x[t], t]
```

## Solving Equations Numerically

If equations don't have an exact solution (or if it takes forever to find one), use `NSolve[func[x], x]`.  The argument must be fully numerical (have no arbitrary parameters), except for the variable x!

```Mathematica
NSolve[LegendreP[20, 2, x] == 0, x]
```

Similarly, with differential equations, but in this case you need to specify boundary conditions:

```Mathematica
sol = NDSolve[{6 y'[x] - 2 y[x] - x y[x]^4 == 0, y[0] == -2}, 
 y[x], {x, -10, 10}]
Plot[y[x] /.sol, {x, -10, 10}]
```
