---
title: First Python Experience
ordering: 1
layout: default
group: Python
type: tutorial
---

# My First Time Opening Python

In this interactive terminal, we'll walk through opening Python for the first
time. For simplicity, we'll do this on the command line. First, find your
respective terminal application. After opening, type on the command line

``` bash
$ python --version
Python 2.7.9
```

This command will let you know which version of python you are running, if any.
If the version number is less than 3.2, as above, you may need to use the
command

``` bash
$ python3 --version
Python 3.4.2
```

If you do not have python 3.2 or greater installed, take a look at the
introduction page.

Next, since python is installed, let's try to open it. Type

``` bash
$ python3
```
You should see something like the following

{% highlight pycon %}
Python 3.4.2 (default, Jan 12 2015, 11:38:40) 
[GCC 4.9.2 20141224 (prerelease)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
{% endhighlight %}

Great! You've opened python for the first time! Now how the heck do you get out
of it? You can either type `exit()` or use the key command `Ctrl-D` to exit.

Now let's try typing some things in the python command line. The `>>>` means the
interpreter is ready for the next command. How about some simple math? Try
typing the following, then pressing enter.

{% highlight pycon %}
>>> 1+1

>>> 300+1.

>>> 30/3

>>> 30./3.

>>> 2*3

>>> 2**3

>>> 20. % 3
{% endhighlight %}

You'll notice that without a decimal at the end of a number, python
automatically treats the number as an integer. We'll get to this in the next
tutorial. Also, the `%` sign means modulo, which is always a good tool for
counting.

Now, try the following:

{% highlight pycon %}
>>> print("hello world")

>>> print("SPAM")
{% endhighlight %}

I think you get the hang of it. Let's try something a bit different. Exit python
to the terminal, and open a new file called MyExample.py using your favorite
editor. In this file, write the following lines:

```python
#!/bin/python3
print('Green Eggs and Spam')
print(2**100)
```

Now, on the command line, type

``` bash
python3 MyExample.py
```

What happened? You just wrote your first script!
