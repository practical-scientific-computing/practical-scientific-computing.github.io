---
title: Introduction
ordering: 0
layout: default
group: Shell
type: index
---

# Unix Shells

![alt](/shell/media/dilbert_unix.png)

## What is the shell?

The shell is a program that serves as an interface between two very different parts of a computer, the *kernel* and the *user programs*.
The kernel  is the program which forms the communication link between the hardware of the computer and any of the other programs that you wish to use.
It is a very complex and highly optimized code that many users will never need to think about because the shell (and other programs) can talk to the kernel which will perform the action on the physical device.
The shell was developed specifically to make writing user programs that interface with the kernel easier to manage via a textual interface.

The *Unix shell* is a special type of shell that has been emulated by many operating systems.
The shell forms the core *Unix philosophy* of computing, where small programs are strung together using redirection (to be explained later) and conspire to solve a complex task.
All of the communication between these programs are handled by the operating system.
This make it a very powerful tool, one that is eye opening for many users which are used to having a single program for a single task and keep these tasks isolated.

## Brief History

Unix was originally made by a group of people at bell labs (Ken Thompson and Dennis Ritche et al) in the early 70's.
It was written in C and assembly and relied entirely on a textual interface, which was considered to be very sophisticated when first introduced.
It was very popular for development use as it had a nice sane file hierarchy and could handle multiple users by default.
The main problem with the Unix system was its closed source code. 
This made using the system only accessible to an elite, well connected few, and widespread adoption would not be possible.

By the late 70's, the Berkeley Software Distribution (BSD) was developed, but until the 90's, was a closed operating system (OS), used mainly by academics for research in computer science.

All of this change in the early 90's with the release of the GNU (GNU is not Unix) software and the Linux kernel.
These programs were made by Richard Stalman and Linus Torvalds and was released under the General Public License (GPL) which enforces the four fundamental software freedoms.
These two softwares made use of Unix like systems available to all for free and kick started the free software movement.

At this point, the Unix philosophy was widely accepted as a powerful OS design and many different versions were made to suit specific purposes, as you can see in the timeline below.

![alt](/shell/media/Unix_history-simple.svg)


The major 3 flavors of *nix that are available today are:

* GNU+Linux
* BSD
* Unix

There are many flavors of each of these Unix versions and many are free to use by anyone


## GNU+Linux or Unix

If you are using a Linux environment as your development computer, setup is essentially done before you even start. 
You simply need to launch a terminal emulator that is included with your environment and start going through the tutorials. 
The remote environment that is provided to you is a GNU+Linux distribution called Fedora which will provide these facilities.


## OSX 

OSX is actually a fully certified Unix environment that includes many of the tools used in this set of tutorials.
There is even a terminal emulator included with the OS, called `Terminal`, that you can use.
There is a much more useful terminal emulator available for OSX called `iterm2` that you can also install from [http://iterm2.com/].
If you are using OSX for development and are using the terminal often, it is highly recommended. 

## Windows

**Not supported for these tutorials**

The Windows operating system is much more difficult to translate these tutorials into.
Windows has an entirely separate history from the Unix side of computing, and all of the internals are incompatible with the Unix philosophy.
This can be remedied in a few ways but comes at the cost of maintaining a somewhat unsupported environment.


