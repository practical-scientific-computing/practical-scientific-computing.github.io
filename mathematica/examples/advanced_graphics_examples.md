---
title: Advanced Drawing Options
layout: default
group: Mathematica
type: advanced
---

# Advanced Graphics Tutorial
## Visualizing a Probability Distribution Function
Building off of the lectures Patrick gave on graphics, let's
illustrate the concepts using some examples which came up in
research. Let's say that you want to model some histogram by
a Johnson SU PDF. Don't know what that is? Google it!

Now we want to know what the parameters of the Johnson function
do to its shape. How can we do that in real time? Let's use
Manipulate.

``` mma
Manipulate[
 Plot[E^(-(1/
    2) (\[Gamma] + \[Delta] ArcSinh[(x - \[Mu])/\[Sigma]])^2)/Sqrt[
  1 + (x - \[Mu])^2/\[Sigma]^2], {x, -10, 10}], {\[Gamma], 1, 
  10}, {\[Mu], 0, 20}, {\[Sigma], 1, 20}, {\[Delta], -3, 3}]
```

![Manipulate of Johnson](/mathematica/media/johnson_manipulate.png "Johnson Function using Manipulate")

Note, I've not included the normalization here, but you can certainly add it in.
What's the difference between an SU and SB Johnson?

##