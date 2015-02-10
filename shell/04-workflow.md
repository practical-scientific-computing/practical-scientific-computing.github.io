---
title: Redirection, pipelining and job control
ordering: 5
layout: default
group: Shell
type: tutorial
---

In Unix-like environments, programs are designed with specialized functions that can be stitched together to perform some meaningful task. This idea of carring-out complex tasks by combining simple components is pervasive in Unix. Doug McIlroy, the inventor of Unix pipelining, summed up this philosophy best: "Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface."[1]

To accomodate this building-block approach, each program in a Unix-like system has the following properties:

* A channel for receiving input, known as standard input (*stdin*)
* A channel for sending output, known as standard output (*stdout*)
* A channel for error messages and diagnostics, known as standard error (*stderr*)

Together, these are known as the *standard streams*. When you run a program on the shell, you can think of the standard input as being the keyboard, and the stdout and stderr as the terminal window.

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

Keep in mind that the `>` operator has a very particular behavior. If you run the first example again, you will see that your `hello` file only contains *one* instance of "Hello World!". When you invoke `>`, it _will_ overwrite whatever file already exists. Instead, you may want to *append* by using the `>>` operator. Try it:

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

Obviously this all very pedagogical. In the "real world", ...




```console
                                                             ____________
                     ____________                           |            | --> ...
                    |            |  --> standard output --> | program #2 |
standard input -->  | program #1 |                          |____________| --> ...
                    |____________|  --> standard error
```



[1] Peter H. Salus. A Quarter-Century of Unix. Addison-Wesley. 1994. ISBN 0-201-54777-5
