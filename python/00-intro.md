---
title: Introduction
ordering: 0
layout: default
group: Python
type: index
---

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
having the following installed:

  * [Python v3.2](https://www.python.org/) or later.
  * [NumPy](http://www.numpy.org/), a linear algebra and numerical methods
      library for Python.
  * [matplotlib](http://matplotlib.org/), a Python plotting library based on
      MatLAB
  * [IPython](http://ipython.org/), and advanced Python shell with both terminal
      and notebook interfaces.

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
version 3.x and later as earlier versions will eventually lose support.
Python2.7 is now only recieving certain SSL-related security updates, all of
which are actually backports from Python3. We encourage you to embrace the
future. **In these tutorials, we will make use of Python3**.

### Installing

#### Unix-like Systems
We encourage the use of GNU/Linux for your development environment where Python
will likely be available in your distribution's core software repository. In
most cases, Python will be included by default on new GNU/Linux installs. 
If you are using one of the popular distributions RHEL/CentOS/SL/Fedora or
Debian/Ubuntu/Mint, then the required software for these tutorials will be
found in the distro's repository under the names:

  * python3
  * python3-matplotlib
  * python3-numpy
  * ipython3
  * ipython3-notebook

Please consult your OS's package management system documentation as required.

For special cases, see the official Python 
[download page](https://www.python.org/downloads/) for more information.

#### Caution:

On systems with both Python3 and Python2 installed, one will typically be called
'python' and the other will be called 'pythonN' where N is either 2 (Archlinux,
Gentoo) or 3 (RHEL/CentOS/SL/Fedora, Debian/Ubuntu/Mint). It's been 7 years
since Python3 came out, but switching names is a big task and it's still
ongoing. **Always be aware of your programming environment** and know which
version you are using when you call 'python'.

#### MacOS

Mac OS X 10.8 comes with the latest legacy version of python (version 2.7)
pre-installed. New Python users are encouraged to adopt non-legacy
versions 3.2 and higher. To install the latest Python3, see the official
Python [download page](https://www.python.org/downloads/) and the latest
Python3 [documentation](https://docs.python.org/3/using/mac.html).

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

