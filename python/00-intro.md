---
title: 00 - Introduction
layout: default
group: Python
---

# Python Workshop

This workshop aims to help get you started using Python in your research
projects.  We expect attendees of varied familiarity with Python and programming
in general. As such, we will start with the basics and work our way towards
practical examples and uses of Python in scientific research.

</p>
<hr>
<div class="row">
<div class="col-md-3">
#### Core Tutorials

 1. [Basic Syntax](01-syntax.html)
 1. [Core Data Structures](02-data_structures.html)
 1. [Flow Control](03-flow_control.html)
 1. [Functions](04-functions.html)
 1. [Classes (Part 1)](05-classes1.html)
 1. [Classes (Part 2)](06-classes2.html)
 1. [Modules](07-modules.html)
 1. [Packages](08-packages.html)
 1. [Numpy](09-numpy.html)
 1. [Matplotlib](10-matplotlib.html)

#### Advanced Topics

 * Lambdas
 * Comprehensions
 * Generators
 * String Formatting
 * Decorators
 * Exception Handling
 * Pickles
     
</div>
<div class="col-md-6">
## Introduction

Created in 1991 by "benevolent dictator-for-life" Guido van Rossum, Python is a
general-purpose dynamically-typed programming language. Python supports multiple
paradigms including object-oriented, imperative, and procedural styles. Its
hallmarks include great readability, simplicity, and a comprehensive standard
library. 

Python has found widespread use, especially in the scientific community.
Python code can be run as interpreted scripts or built into standalone
executables. As such, it is an invaluable tool for aspiring scientists to learn.

Before we can jump in, please ensure your development environment is in order by
having an appropriate version of Python installed on your development machine.
These tutorials will also make use of an interactive python shell and, later,
the IPython notebook interface.

### Python Version 3 vs. 2: Which to use?

In 2008, Python underwent a schism in response to the release of version 3 which
broke backwards-compatibility with earlier versions. For many years, migration
to v3.x was hampered by lack of support by major 3rd party packages such as
Numpy. Furthermore, many large-scale scientific experiments that depended on
RHEL4 supported only older versions of Python up to version 2.6. 

Today, most 3rd party packages have been updated to work with either the legacy
v2.x and currently maintained v3.x releases. However, if you are participating
in research that makes use of legacy Python code, you may need to install
version 2.7 or earlier to use your project's existing legacy software.

If your project has no legacy code restrictions, then it is encouraged to use
version 3.x and later as earlier versions will eventually lose support. *In these
tutorials, we will make use of Python 3*.

One word of caution when writing python scripts that will be run in mixed
environments: some systems (at the time of this writing: RHEL/CentOS, Debian,
Ubuntu) package Python version 2.x as the default 'python' and version 3.x as
'python3' whereas other systems (Archlinux, Gentoo, etc) package version 3.x as
'python' and legacy versions as 'python2'. Always be aware of your programming
environment. If you must develop a script to work in conflicting environments,
be sure to include version checks or overload conflicted elements using special
statements such as `from __future__ import x`.

### Installing

We encourage the use of GNU/Linux for your development environment where Python
will likely be available in your distribution's core software repository. In
most cases, Python will be included by default on new GNU/Linux installs. For
special cases, see the official Python 
[download page](https://www.python.org/downloads/) for more information.

#### Unix-like Systems
The installation procedure for Python is straight-forward on most \*nix
systems. Usually both Python version 2.x and version 3.x is available in the
standard distribution repositories, which are the preferred installation source.
Please consult your OS's package management system documentation as required.

#### MacOS

Mac OS X 10.8 comes with the latest legacy version of python (version 2.7)
pre-installed. New Python users are encouraged to adopt non-legacy
versions 3.x and higher. To install the latest Python 3.x, see the official
Python [download page](https://www.python.org/downloads/) and the latest
Python 3.x [documentation](https://docs.python.org/3/using/mac.html).

#### Windows

For these tutorials, Windows as a development environment will be unsupported.
However, an MSI-based Windows installer is available at the official Python
[download](https://www.python.org/downloads/) page. If you must use Windows as
development environment, consider using an all-in-one Python deployment such as
**Anaconda**.

### Interpereters

Python ships with its own interactive command line shell called **idle**. While
**idle** works well, other 3rd party interpereters provide significant
enhancements to workflow. We recommend and will make use of
[**IPython**](http://ipython.org) which supports:

 * Syntax highlighting,
 * Colorized output
 * Tab completion
 * GUI and data visualization support
 * A notebook interface that can be run in any web browser.
 * And more!

IPython is available in most GNU/Linux distribution repositories. 

</div>
<div class="col-md-3">

### Further Reading

 * [Python Documentation]()
 * [IPython Documentation]()
 * [PEP8 Style Guidelines]()
 * [Google Python Style]()
 * [Matplotlib Documentation]()

</div>
</div>
