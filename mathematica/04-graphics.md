---
title: Graphics
ordering: 4
layout: default
group: Mathematica
type: tutorial
---

# Creating Graphics with Mathematica

The ability to graphically depict a complex problem and its solution is an essential skill to a scientist.
Often, other scientists will skip past all of the writing in a paper and attempt to understand your results from figures alone.
This requires generation of high quality figures that are clean, clear and well thought out.
Luckily, *Mathematica* has most, if not all, of the functionality that you might require to visualize and publish high quality figures and graphics.

Lets start with something familiar, the basic `Plot`:

```
Plot[Sin[x],{x,0,10}]
```

The syntax for most of the plotting functions in *Mathematica* will follow the same syntax.
For example, we can make a log plot using the same syntax

```
LogPlot[Abs[Sin[x]],{x,0,10}]
```

There are also other log based plotting functions available (see: `LogLinearPlot` and `LogLogPlot`), and other nice ways to plot functions (see: `ParametricPlot`).

### Changing the look of a Plot

Plots can be customized very easily by specifying options.
There are many options (too many to easily memorize) which are found in the help browser for `Plot`:

```
?Plot
```

Now click on the `>>` at the end of the help (or search for Plot in the help browser).
At the bottom of the help page you will find an arrow labeled "options".
Clicking this shows all of the plot options available to you for customizing your figure.
Options are included at the end of the `Plot` statement using an arrow (`->`).
Lets change a couple of things as a test:

{% raw %}
```
plot1 = Plot[{Sin[x], Cos[x]}, {x, 0, 10},
 Frame -> True,
 FrameLabel -> {"x", "", "Sin[x] (red), Cos[x] (green)", ""},
 PlotRange -> {{0, 3 Pi}, {-1, 1}},
 PlotStyle -> {Red, Green}]
```
{% endraw %}

### Graphics objects

All visual entities in the notebook are known to *Mathematica* as graphics objects.
These objects can be in the form of a plot, some text or a shape:

```
text1 = Graphics[Text["Some Text", {7, -.6}]];
circ1 = Graphics[Circle[{Pi, 0}, .3]];
```

These graphics can then be combined into a single image with show. 
This makes creating complex figures easy as you can work on single parts of the figure separately and combine them all at the end into the final figure.

```
Show[plot1, text1, circ1]
```

Note that the graphic will inherit the options from the first listed plot as the global options of the entire graphic, which means you can focus on plot options for a single plot and let the rest of the graphics inherit its options.
This takes care of most of the "two dimensional" plotting that you might need. 
But there is more...

### 3 Dimensional Plotting

Lets now visualize a function of two variables. 
This can be hard to do with a regular line on a figure, but becomes easy on a computer

{% raw %}
```
plot2 = Plot3D[Cos[x] + y^2/8, {x, -10, 10}, {y, -10, 10}, 
  PlotRange -> {-2, 18},
  AspectRatio -> 1]
```
{% endraw %}

You can move the viewing perspective of the graphic by clicking and dragging the image around.
Being able to move the viewpoint is very useful when trying to visualize a function that has a very complicated structure.
If you wish to then print these graphics out on a 2D piece of paper, the 3D plot might not be the best.
Lets instead use a contour plot:


{% raw %}
```
ContourPlot[Cos[x] + y^2/8, {x, -10, 10}, {y, -10, 10}]
```
{% endraw %}

There are many other useful 3D plots available (see `DensityPlot` and `StreamPlot`).

### 3D Graphics objects

The same rules apply when showing 3D graphics as in the 2D case, but you need to use a slightly different function

{% raw %}
```
sphere1 = Graphics3D[Sphere[{0, 0, 6}, 3]]
Show[plot2, sphere1]
```
{% endraw %}

