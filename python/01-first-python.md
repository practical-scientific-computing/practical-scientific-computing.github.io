---
title: First Python Experience
ordering: 1
layout: default
group: Python
type: tutorial
---

# My First time opening python

In this interactive terminal, we'll walk through opening Python for the
first time. For simplicity, we'll do this on the command line. First,
find your respective terminal application. After opening, type on the command
line

```
which python
```

This command will let you know which version of python you are running, if any.
If you do not have python installed, take a look at the introduction page.

Next, since python is installed, let's try to open it. Type

```
python
```
You should see something like the following

```
Python 2.7.8 (default, Oct 19 2014, 16:03:53) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.51)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Great! You've opened python for the first time! Now how the heck do you get out of it? You can either type "exit()" or use the key command "Ctrl-D" to exit.

Now let's try typing some things in the python command line. The ">>>" means the interpreter is ready for the next command. How about some simple math? Try typing the following, then pressing enter.

```
>>> 1+1

>>> 300+1.

>>> 30/3

>>> 30./3.

>>> 2*3

>>> 2**3

>>> 20. % 3
```

You'll notice that without a decimal at the end of a number, python automatically treats the number as an integer. We'll get to this in the next tutorial. Also, the % sign means modulo, which is always a good tool for counting.

Now, try the following:

```
>>> print ("hello world")

>>> print ("SPAM")
```

I think you get the hang of it. Let's try something a bit different. Exit python to the terminal, and open a new file called MyExample.py using your favorite editor. In this file, write the following lines:

```python
print ('Green Eggs and Spam')
print (2**100)
```

Now, on the command line, type

```
python MyExample.py
```

What happened? You just wrote your first script!
