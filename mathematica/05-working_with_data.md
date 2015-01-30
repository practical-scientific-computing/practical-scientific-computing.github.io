---
title: Working with Data
ordering: 5
layout: default
group: Mathematica
type: tutorial
---

# Importing and Exporting data with *Mathematica*

Moving data from a saved text file (or other format) using *Mathematica* is very simple once you get used to the operations involved.
As this is a programming language, importing data is performed with a function call (rather than clicking buttons as something like Excel would have you do):

```
file=Import["path/to/file.txt","Table"]
```

There is a sample file [here](/mathematica/media/sample-data.txt)

Often the file path is a very long and complicated text string ("path/to/file.txt"), so choosing the file graphically and having *Mathematica* insert this string is easier than typing it all out.
The path string can be inserted using `Insert -> File Path...` (Note: this is ** NOT file...**).
This will simply insert the string for your file path wherever your cursor is.
The second argument specifies how *Mathematica* should interpret the file we have imported (in this case, as a `Table` or list).
Now that we have the file imported, lets look at some of its properties:

```
First[file]
Length[file]
Dimensions[file]
```

You can now manipulate this list as you would any other list (`Flatten`, `Partition`, `Drop`, `Take`,...)

### Import file types 

There are **MANY** types of files that *Mathematica* can import

```
$ImportFormats
```

Some commonly used extensions are "Table" (for columns of numbers), "CSV" (for comma separated values) and "JPEG".
If it is not specified, then *Mathematica* will try to guess the file type from the extension, but often messes up and needs to be told the file format to be explicitly.

### Exporting

Exporting is just as easy as Importing.
Again, instead of clicking on buttons we will program this operation with a function call:

```
Export["/path/to/file.xls",list]
```

Now you have saved this file and can use any other program to access it as you normally would. 
There are many file types you can export as shown here

```
$ExportFormats
```

# Making figures with numeric data

For many of us, numerical data sets are the focus of much of our research.
Visualizing a function is nice, but real data is often much more messy and difficult to understand.
This is where graphics become essential, and after importing the data into *Mathematica*, there are many ways to make figures of data.
The most basic function to make a figure with data is a `ListPlot`

{% raw %}
```
list1 = Table[Cos[n], {n, 0, 2 Pi, .1}];
ListPlot[list1]
```
{% endraw %}

Notice that the horizontal axis is not "n", as we might like; by default, the horizontal axis represents the number of the element of the list.  It is easy enough to fix this in the definition of the list:

{% raw %}
```
list2 = Table[{n, Cos[n]}, {n, 0, 2 Pi, .1}];
ListPlot[list2]
```
{% endraw %}

(That's better.)

This function carries many of the same plot options as the regular `Plot` function has.

Another commonly used graphic is the histogram.
This was added fairly recently (version 7), but while they are very easy to make and they look reasonably nice, the function does not have many options which other, more specialized software packages have.
To use a histogram simply use the function on a list of data

```
data = RandomVariate[NormalDistribution[-1, 1], 200]
Histogram[data]
```

The same 3D plotting functions that were available for the symbolic side are available when using numerical data sets.
Many of these plots require the data to be in a specific list structure, which you will have to find from the help browser.
Here are a few examples:

{% raw %}
```
matrix = {{1, 2, 3, 4}, {4, 3, 2, 2}, {1, 10, 1, 5}, {1, 1, 1, 0}, {-1, -5, 0, -1}}
ListPlot3D[matrix]
ListContourPlot[matrix]
```
{% endraw %}
