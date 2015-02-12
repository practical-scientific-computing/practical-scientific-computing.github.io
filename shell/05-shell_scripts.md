---
title: Shell Scripts
ordering: 5
layout: default
group: Shell
type: tutorial
---

# Why would I need a shell script?

There are instances when you need to do the same operation many times for slightly different
input parameters. Now, imagine you were changing one parameter in an input file many times,
and half way through, you made a mistake and spend another 5 hours tracking this down. Yes,
this happened to me. So, why not instead use computers to do this quickly and accurately?
There is no reason, and the way to accomplish this is through a shell script.

# Scripting Basics

Let's edit a file called `my_first_shell_script.sh`. The `.sh` extension generally indicates
that the file you are working with is a bash script. In this file, let's write two lines using
the editor of your choice:

```
#!/bin/bash 
echo Hello World
```

The first line is the so-called "shebang", or "hashbang" ( [or any other variety of variables](http://en.wikipedia.org/wiki/Shebang_%28Unix%29) ) and tells the kernel which program to use to run
the script. The second is a simple print statement.

Make sure to save the file, now change the file permissions to make this executable.

```
$ chmod +x my_first_shell_script.sh
```

Now, let's try running the script:

```
$ ./my_first_shell_script.sh
Hello World
```

You've written your first shell script.

# Setting Variables

Often times in a script you'd like to set a variable, be that a directory, a file name, or whatever. The 
way to do this in bash is by using the `=` sign. Let's copy `my_first_shell_script.sh` to `my_second_shell_script.sh`,
and do the same thing using variables. Modify the file to be the following:

```
#!/bin/bash
MYSTR="Hello World"
echo $MYSTR
```

Here, we've set the variable `MYSTR` in the second line, and asked for its value in the third, by putting `$` in front of the variable name.
Make sure the file permissions are correct and run the script. What happens if you forget the `$`?
(NB: There are no spaces between the variable name and the `=` sign!)

We can set variable to anything we want. Let's make a third script called `use_variables_script.sh`.

```
#!/bin/bash
mydir=$(pwd)
echo "You are in " $mydir
echo "Goodbye!"
```

Again, check the file permissions and run. What have we done? We've effectively redirected the output of `pwd` to mydir by creating a subshell with `$()`

# Loops.