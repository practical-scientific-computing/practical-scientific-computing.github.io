---
title: Graphics
ordering: 4
layout: default
group: Mathematica
type: tutorial
---

# Creating Graphics with Mathematica

The ability to graphically depict a complex problem and its solution is an essential skill to a scientist.
Often, other scientists will skip past all writing in a paper and attempt to understand your results from figures alone.
This requres generation of high quality figures that are clean, clear and well thought out.
Luckily, *Mathematica* has most, if not all, of the functionallity that you might require to visualize and publish high quality figures and graphis.

Lets start with something familiar, the basic Plot:

```
Plot[Sin[x],{x,0,10}]
```

The syntax for most of the plotting functions in *Mathematica* will follow the same syntax.
For example, we can make a log plot using the same syntax

```
Plot[Sin[x],{x,0,10}]
```

There are also other log based plotting functions available (see: `LogLinearPlot` and `LogLogPlot`), and other nice ways to plot funcitons (see: `ParametricPlot`).

### Changing the look of a Plot

Plots can be customized very easily by specifying options.
There are many options (too many to easily memorize) which are found in the help browser for Plot

```
?Plot
```

Now click on the `>>` at the end of the help (or search for Plot in the help browser).
At the bottom of the help page you will find an arrow labled "options".
Clicking this shows all of the plot options available to you for customizing your figure.
Lets change a couple of things as a test:

```
Plot[{Sin[x],Cos[x]},{x,0,10},PlotStyle->{Red,Green},Frame->True]
```

### Graphics objects

All visual entities in the notebook are known to *Mathematica* as a graphics object.
These objects can be a plot, some text or a shape

```
Graphics[Text...
Graphics[Circle
```


These graphics can then be combined into a single image with show. 
This makes creating complex figures easy as you can work on single parts of the figure seperately and combine them all at the end into the final figure.

```
plot
graphics
show...
```

Note that the graphic will inherit the options from a single plot as the global options of the entire graphic, which means you can focus on plot options for a single plot and let the rest of the graphics inherit it's options.
This takes care of most of the "two dimensional" plotting that you might need. 
But there is more...

### 3 Dimensional Plotting

Lets now visualize a funciton of two variables. 
This can be hard to do with a regular line on a figure, but becomes easy on a computer

```
Plot3D
```

You can move the viewing perspective of the graphic by clicking and dragging the image around.
Being able to move the viewpoint is very useful when trying to visualize a function that has a very complicated structure.
If you wish to then print these graphics out on a 2D piece of paper, the 3D plot might not be the best.
Lets instead use a contour plot

```
Contour Plot
```

There are many other useful 3D plots available (see `DensityPlot` and `StreamPlot`)

### 3D Graphics objects

The same rules apply when showing 3D graphics as the 2D case, but you need to use a slightly different function

```
Graphics3D[sphere]
Plot3D[]
Show[]
```

