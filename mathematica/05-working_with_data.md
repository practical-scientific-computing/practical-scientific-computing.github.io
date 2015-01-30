---
title: Working with Data
ordering: 5
layout: default
group: Mathematica
type: tutorial
---

# Importing and Exporting data with *Mathematica*

Moving data from a save text (or other format) file using *Mathematica* is very simple once you get used to the operations involved.
As this is a programming language, importing data is performed with a function call (rather than clicking buttons as something like excel would have you do):

```
file=Import["path/to/file.txt"]
```

Often the file path is a very long and complicated text string ("path/to/file.txt"), so choosing the file graphically and having *Mathematica* insert this string is easier than typing it all out.
The path string can be inserted using `Insert -> File Path...` (Note: this is ** NOT file...**).
This will simply insert the string for your file path wherever your cursor is.
Now that we have the file imported, lets look at some of its properties

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
*Mathematica* will try to guess the file type from the extension, but often messes up and needs to be told the file format to be explicitly.


### Exporting

Exporting is just as easy as Importing.
Again, instead of clicking on buttons we will program this operation with a function call

```
Export["/path/to/file.xls",list]
```

Now you have saved this file and can use any other program to access it as you normally would. 
There are many file types you can export as shown here

```
$ExportFormats
```

# Making figures with numeric data

For many of us, numerical data sets are the focus of much of out research.
Visualizing a  function is nice, but real data is often much more messy and difficult to understand.
This is where graphics become essential, and after importing the data into *Mathematica*, there are many ways to make figures of data.
The most basic function to make a figure with data is a ListPlot

```
ListPlot[asdlkj
```

This function carries many of the same plot options as the regular `Plot` function has.

Another commonly used graphic is the histogram.
This was just recently added (version 7) and while they are very easy to make and look reasonably nice, the function does not have many options which other, more specialized software packages have.
To use a histogram simply use the function on a list of data

```
histogram[]
```

The same 3D plotting functions that were available for the symbolic side are available when using numerical data sets.
Many of these plots require the data to be in a specific list structure, which you will have to find from the help browser.
Here are a few examples:

```
ListPlot3D
ListContourPlot
ListStreamPlot
```
