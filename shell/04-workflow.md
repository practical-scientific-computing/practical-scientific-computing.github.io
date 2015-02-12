---
title: Redirection, pipes and job control
ordering: 5
layout: default
group: Shell
type: tutorial
---

Redirection, pipes and job control
====================

In Unix-like environments, programs are designed with specialized functions that can be stitched together to perform some meaningful task. This idea of carring-out complex tasks by combining simple components is pervasive in Unix. Doug McIlroy, the inventor of Unix pipelining, summed up this philosophy best: "Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface."[1]

To accomodate this building-block approach, each program in a Unix-like system has the following properties:

* A channel for receiving input, known as standard input (*stdin*)
* A channel for sending output, known as standard output (*stdout*)
* A channel for error messages and diagnostics, known as standard error (*stderr*)

Together, these are known as the *standard streams*. When you run a program on the shell, you can think of the standard input as being the keyboard, and the stdout and stderr as the terminal window.

Redirection
------------

What if you want to save the output of a program to a file instead of displaying it on the screen? This can be done simply by using *redirection*. The basic redirection operators are `>` for redirecting output, `>>` for appending to a file, and `<` for redirecting the input. More often than not, you will redirect output rather than input. For example, let us try taking the output of the `echo` command and saving it to a file.

```console
$ echo "Hello World"
Hello World
$ echo "Hello World" > hello
```

Notice that echo did not produce output the second time. Why? The standard output was _redirected_ to the file `hello`. We can use another command, `cat` (short for concatinate), to print the file onto the screen:

```console
$ cat hello
Hello world
```

Keep in mind that the `>` operator has a very particular behavior. If you run the first example again, you will see that your `hello` file only contains *one* instance of "Hello World". When you invoke `>`, it *will* overwrite whatever file already exists. Instead, you may want to *append* by using the `>>` operator. Try it:

```console
$ echo "Hello World" >> hello
$ cat hello
Hello World
Hello World
```

Similarly, we can redirect _stdin_ (standard input) by using the `<` operator. Suppose we want to filter out duplicated lines in our example file. A simple way to do this would be with the aptly named `uniq` utility:

```console
$ cat hello
Hello World
Hello World
$ uniq < hello
Hello World
```

Though it appears a bit convoluted, we could extend this example further by writing out filtered output to another new file:

```console
$ uniq < hello > hello_filtered
$ cat hello_filtered
Hello World
```

We should also briefly touch on the use of _stderr_. Standard error is often used to print out any diagnostic messages that your program may generate. When writing scientific applications, you should reserve _stderr_ for any noncritical warnings that you don`t want to later filter out of your results. In the core utilities suite, for example, _stderr_ is used to show the "usage page" when the program is incorrectly invoked.

```console
$ tr
tr: missing operand
Try 'tr --help' for more information.
```

If you try to redirect the output of cut, however, you will see that you get nothing:

```console
$ tr > tr_output
tr: missing operand
Try 'tr --help' for more information.
$ cat tr_output
$
```

It might be desirable to save the diagnostic output, which you can do by explicitly telling the shell that you want to redirect the _stderr_ using `2>`

```console
$ tr 2> tr_output
$ cat tr_output
tr: missing operand
Try 'tr --help' for more information.
```

Pipes
------

In a previous example, we used redirection to read _stdin_ from a file and write _stdout_ to a file. However, this approach has some limitations. For one, we have to write a new file every time we operate on our data, or overwrite our original data. Second, we can only run one program at a time. Unix has an elegant solution for both of these problems, known as _pipelining_. Separating a list of programs with the `|` (pipe) key connects the _stdout_ of one process to the _stdin_ of another.

You can think of it visually like this:

```console
    input  
      |
      |
 _____V_____
|           |
| program 1 |---> stderr 1
|___________|
      |
(pipe)| 
      | stdout 1
 _____V______
|           |
| program 2 |---> stderr 2
|___________|
      |
(pipe)| 
      | stdout 2
 _____V______
|           |
| program 3 |---> stderr 3
|___________|
      |
(pipe)|
      V
 final output
```

Suppose we take "Hello World" from before and we want to turn it into a comma separated list of values. We can use the `tr` (translate) program to do this:

```console
$ echo "Hello World" > hello
$ tr ' ' ',' hello
Hello,World
```

Or we can skip the intermediary file and use a pipe: 

```console
$ echo "Hello World" | tr ' ' ','
Hello,World
```

And, for purely pedagogical reasons, we also want to reverse the line:

```console
$ echo "Hello World" | tr ' ' ',' | rev
dlroW,olleH
```

You can also combine redirection and pipes. Try taking the previous example and redirecting the output to a file named `hello_reversed`.


Basic job control
-----------

Suppose you have a very long-running simulation or analysis, and you would like it to run for many hours or days. Using job control, you can ensure that your program stays running even if you get disconnected from the remote server. Our "simulation" will use the venerable `sleep` program.

The shell provides powerful shortcuts and utilities for canceling, suspending, and resuming processes. In Unix-like systems, all programs understand _signals_, which are a simple way to tell a process that it is supposed to do something. You can imagine them as being like traffic signals. For example, a 10000s run of our "simulation":

```console
$ sleep 10000
```

How would you exit early from this? An easy way is to simply use `CTRL-C`, which sends the _kill_ signal to the program. The kill signal tells the process to end immediately and return control of the shell back to the user. Similarly, you can pause a process with the `CTRL-Z` (suspend) signal. 

```console
$ sleep 10000
^Z
[1]+  Stopped                 sleep 10000
$
```

Once the process is stopped, you can resume it by simply typing `fg`, and it will pick up where it left off. 

You may find that you have started a long-running job in your terminal session, but have to disconnect from the shell for some reason (such as closing your laptop, leaving a shared computer, etc). Unfortunately, suspending the job (`CTRL-Z`) will not alone be effective here for reasons beyond this material. Happily, there`s a recipe to rescue such jobs:

* First, stop the job with `CTRL-Z` and get its job number ([1] in the previous example). 
* Next, send it to the "background" with the `bg` command.
* Finally, use the `disown` command with a percentage sign followed by the job number to disconnect the job from your shell.

```console
$ sleep 10000
^Z
[1]+  Stopped                 sleep 10000
$ bg 
[1]+ sleep 10000 &
$ disown %1
```


[1] Peter H. Salus. A Quarter-Century of Unix. Addison-Wesley. 1994. ISBN 0-201-54777-5
