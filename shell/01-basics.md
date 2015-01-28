---
title: Basic Shell Commands
ordering: 1
layout: default
group: Shell
type: tutorial
---

# The Prompt

Upon firing up a terminal emulator, it will start some flavor of textual
command-line-interface (**cli**) called a **shell**. There are many
different shells available including but not limited to:

  * bash (the **B**ourne-**a**gain **sh**ell)
  * zsh (**Z**hong **Sh**ao shell)
  * sh (the original Bourne **sh**ell)
  * csh (the **C**-**sh**ell)
  * tcsh (the **T**ENEX-**csh**)
  * ksh (the **K**orn **sh**ell)
  * fish (the **f**riendly **i**nteractive **sh**ell)
  * Ad nauseum....

On most systems, including Linux and modern MacOS, the default shell will be bash.
Some older Unix and Mac systems will use (t)csh by default. Unless specifically
stated we will assume the use of bash, although many shells are so similar that
there is little functional difference for the casual user. Bash is arguably the
best and certainly the most popular shell although some newer shells like zsh and
fish are making their way onto systems by default.

The shell presents itself as a **prompt**. The appearance of the prompt can be
customized and often is different from system to system even if they are running
the same shell. It is common, however, to have the last character in the prompt
be `$`. 

```console
$ 
```

From the prompt, we can issue **commands** to do virtually anything we wish a
computer to do. Every command is either a program, script or shell function.

We issue a command by typing it in at the prompt and press *ENTER*. Most
commands expect number of mandatory **positional arguments** which are typed
after the command name, in order, and each separated by spaces.

Most commands can also take a number of non-mandatory **optional arguments**
or **switches**. Switches can dramatically alter what a command does.  A switch
is invoked by preceding it's name by a number of hyphens `-`. One hyphen is used
if the switch has a single character name and two hyphens are used if the switch
name is more than one character. If a switch expects an argument, that is then
written following the switch name separated by a space. 

Commands and arguments are case-sensitive. You will find that most commands and
multi-character switches are all lowercase, while single character switches to be
of any case.

We'll look at some basic commands first.

## Who and Where am I?

The command `whoami` will return the username you are currently logged in as:

```console
$ whoami
user
```

The command will dump it's response below the prompt and issue a new one.
Once you know *who* you are, it helps to know *where* you are. The shell keeps
track of where you are in the filesystem (much like a file manager). Many
commands that you issue need the location of files relative to where you
currently are. To find out what directory you are currently in, issue the
command `pwd` (short for 'print working directory'):

```console
$ pwd
/home/user
```

If you are using a machine remotely through a terminal, it helps to know the
hostname of the machine you are using. We find this with the command `hostname`:

```console
$ hostname
laptop
```

Many folks will modify their prompt to include all this information in the
prompt so they don't lose track of who and where they are so some prompts may
look like:

```console
[username@laptop: /home/user] $
```

but for brevity, examples here will just use `$` and sometimes maybe `#` as the
shell prompt.

## Getting Help

We're going to learn a lot of commands. If you are new to this, relax: no one
expects you to remember everything about working in a shell. It takes years of
regular use to recall the syntax for all but the most used commands. The
developers of all this stuff know this and have provided some help that you can
access right from the prompt. This can be done two ways:

First, many commands take optional arguments. Options on a shell command are
denoted by one or two dashes followed by a keyword indicating the option to
invoke. Most commands have implemented an option named `--help` that will print a
summary of a command's use and syntax. It looks like this:

```console
$ whoami --help
Usage: whoami [OPTION]...
Print the user name associated with the current effective user ID.
Same as id -un.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
For complete documentation, run: info coreutils 'whoami invocation'
```

The other means of getting help in the terminal is by using the command `man`
which will bring up a command's manual page (if it exists, and it usually will)
in a text-viewing program called a **pager**. The command `man` takes the
name of the command you wish to see the manual for as an argument.

```console
$ man whoami
```

The manual pages tend to be complete and will tell you everything you could want
to know, but they can sometimes be daunting. So, as always, Google is your
friend.

## Getting Around

The most used commands are the ones for moving yourself and files
around the filesystem.

| Command &nbsp; | Mnemonic         | Description 
|---------|------------------|------------------------------------------------
| `ls`    | list             | Lists directory contents
| `cd`    | change directory &nbsp; | Change current working directory

### The UNIX Directory Tree

The UNIX standard outlines an order for where files should go. UNIX-like
operating systems like Linux and MacOS share much of this structure. The Windows
file structure however is very different. The UNIX directory tree starts at a
directory called 'the root directory' or 'root'. The root directory is located 
at `/` which is read as either 'root' or 'slash'.

Within the root directory are a number of subdirectories. As a user, all of your
personal files will reside in `/home/username` and this is where you'll spend
most of your time. 

| Path              | Read As           | Contains                                              | 
|:------------------|:------------------|:------------------------------------------------------|
| `/`               | root              | The root filesystem, highest directory in the system  |
| `/boot`           | ...               | bootloader                                            |
| `/dev`            | device            | system device files                                   |
| `/etc`            | et-cetera, etsy   | global system configuration files                     |
| `/home`           | ...               | user's personal directories                           |
| `/media`          | ...               | mountpoints removable media                           |
| `/mnt`            | mount             | abstract temporarily mounted filesystems              |
| `/opt`            | optional          | third-party software                                  |
| `/proc`           | process, prok     | process/kernel virtual fs                             |
| `/root`           | root-home         | root user's home directory                            |
| `/run`            | ...               | ramdisk tmpfs for temporary OS runtime files          |
| `/sys`            | system, sys       | system virtual fs                                     |
| `/tmp`            | temp, temporary &nbsp;  | ramdisk tmpfs for general temporary files             |
| `/usr`            | user              | userland applications                                 |
| `/usr/bin`        | user bin          | system commands, applications, and binaries           |
| `/usr/include` &nbsp; |user include           | system programming header files                       |
| `/usr/lib`        | user lib          | system shared libraries                               |
| `/usr/local`      | user local        | same as /usr but for host-specific files/commands     |
| `/usr/share`      | user share        | system shared resource files                          |
| `/var`            | variable, var     | runtime variable files                                |

## Manipulating Files

| Command &nbsp; | Mnemonic         | Description 
|---------|------------------|------------------------------------------------
| `mkdir` | make directory   | Makes a new directory
| `mv`    | move             | Moves a file in the filesystem
| `cp`    | copy             | Copies a file to a new location
| `rm`    | remove           | Deletes a file from the filesystem
| `touch` &nbsp; | ...              | Touches the filesystem, creating an empty file
| `rmdir` | remove directory &nbsp; | Removes an empty directory from the filesystem

