---
title: Remote Access
ordering: 2
layout: default
group: Shell
type: tutorial
---

# Remote Access

Using the shell, you can always access different computers/servers using the shell. In fact, that's what
you're doing to work on the computers at UC for this tutorial. There are several very useful commands:

| Command  | Mnemonic      |  Description  
|----------|---------------|----------------------------------------------------------------
| `ssh`    | Secure SHell  | log into remote machine and execute commands
| `scp`    | Secure Copy   | copy files between host on a network, using passwords
| `rsync`  | Remote Sync   | remote data copying tool that minimizes amount of copied data
| `screen` | Screen        | use multiple virtual terminals in the same window
{:.table}

While you can dive in to the man pages yourself to get the full usage of these commands, we'll go over a few
key examples here.

# ssh

This is how you connected to the UC machine that we used for the tutorials. Now, there are a bunch of options
that you can use with ssh to do fancy things. For a full list, see the man pages

```
man ssh
```

Some of the most useful options


| Command                           | Meaning
|-----------------------------------|---------------------------------------------------
| `ssh some_user@some_comp`         | Connect to some_comp as some_user
| `ssh -X some_user@some_comp`      | Connect to some_comp with X11 forwarding enabled
| `ssh -x some_user@some_comp`      | Connect to some_comp with X11 forwarding disabled
| `ssh -Y some_user@some_comp`      | Connect to some_comp with secure X11 forwarding 
| `ssh -p 000 some_user@some_comp`  | Connect to some_comp as some_user through port 000
{:.table}

## Uses

Why would you use any of these other flags? Let's say you have a graphic or something else
on some_comp which you'd like to look at on your current computer. An easy way to do this
is by connecting using `ssh -Y some_user@some_comp`, then running something like

```
firefox mydata.png
```

which will then pop up the firefox window.

## Caveats

Taken from the man pages of ssh:

X11 forwarding should be enabled with caution.  Users with the ability to bypass file permissions on the remote host (for the user's X authorization database) 
can access the local X11 display through the forwarded connection.  An attacker may then be able to perform activities such as keystroke monitoring.

For this reason, X11 forwarding is subjected to X11 SECURITY extension restrictions by default.  Please refer to the ssh -Y option and the
ForwardX11Trusted directive in ssh_config(5) for more information.

# scp

Using the same example as above, let's say you have some data, `data.txt`, on the computer some_comp in the folder `~/my_data/`, which you'd like to copy to your current computer. One way to do this
is by using `scp`

```
scp some_user@some_comp:~/mydata/data.txt ./
```

This will copy the data `data.txt` to your current directory.

Let's try this ourselves. [Here is a sample file TestData.txt](/shell/media/TestData.txt). Download this to your current computer.

Now, find where you downloaded the file on your computer, and go to that folder in the shell.

Next, type the following:

```
scp TestData.txt your_user@your_host:~/
```
(NB change `your_user` to your user name, and `your_host` to the host)

We are copying the file `TestData.txt` from your computer that you are currently working on to the Unix account you are working on.
This will prompt you for the password. Go ahead and enter it. Now, go to your home folder on your Unix account. Do you see the file?

If you have many files which you'd like to copy over, all with similar names, i.e. `data1.txt`,`data2.txt`, etc, then you can use the wildcard `*` to aid you.

```
scp some_user@some_comp:~/mydata/data*.txt ./
```

This copies all of the files which match the expression `data`something`.txt` to the current folder.
(NB: This doesn't work in tcsh.)

Would you prefer to copy it somewhere else? Give it a full path on your machine:

```
scp some_user@some_comp:~/mydata/data*.txt ~/some/other/path/
```

What if you just want the whole directory? Use the recursive command

```
scp -r some_user@some_comp:~/mydata/ ./
```

This has the general form

```
scp options source destination
```

# rsync

Similar to `scp` is `rsync`. The advantage to using `rsync` is that it is generally faster than `scp`, mainly because it only transfers the differences
from one file to another. As with `scp`, the syntax is:

```
rsync options source destination
```

So, in order to transfer the same file `data.txt` from the above source, you can say:

```
rsync some_user@some_comp:~/mydata/data.txt ./
```
Try copying the same data as above with `rsync` now.

There are a host of other options which you can use to help speed things up.

| Option           | Meaning
|------------------|---------------------------------------------------
|  `r`             | Copy data recursively
|  `a`             | Archive mode: Allows recursive copying, while preserve user ownership, sym links, permissions, ownership and timestamps
|  `z`             | Compress data
|  `h`             | Human readable numbers for messages
|  `v`             | Verbose output
{:.table}

So, in order to copy the whole `mydata` directory, as above, but have some more output, we can do

```
rsync -zvha some_user@some_comp:~/mydata/ ~/some/other/path/
```
# screen

Screen is probably the most useful command that you could possibly have with remote connections. Let's see why:

First, log onto your account on the UC box.

Next, type

```
screen
```

A new screen session just started.

Now, let's start some process, say python

```
python
```

Now, you'll see some text has popped up. Now, close your terminal. Yes, actually quit out of your terminal just the way it is. Open a new terminal and log back into the remote
computer. Looks like you've lost all that work that you were working on because your local computer crapped out/blew up/shut down unexpectedly huh? Type

```
screen -ls
```
You will see a dialogue like

```
There is a screen on:
      3591.pts-1.host	(Detached)
1 Socket in /var/run/screen/S-user.
```

Type:

```
screen -r
```

What happened? The task you were performing is still running on the remote host, but your computer detatched, and so did the screen session you had. See the usefulness?

Before we move forward, type `exit()` into the python window. This will exit.

Now there are some other options that you can add. Let's say you wanted to name your screen session. You can do


```
screen -S mySession
```

Now you're back in a screen session. To detatch your screen, say

```
Ctrl-a d
```

The dash means to hold them at the same time. Now, we have two active sessions running. To see them, type

```
screen -ls
```

This lists the active screen sessions. You should see something like:

```
There are screens on:
      3591.pts-1.host	(Detached)
      5315.mySession	(Detached)
2 Sockets in /var/run/screen/S-user.
```

If you wanted to name the screen session that doesn't have a name, you can reconnect it using

```
screen -r 3591
```
where 3591 corresponds to the number in the list `screen -ls`. Now, in this screen, say

```
Ctrl-a : sessionname session2
```

You'll see a box pop up at the bottom of the screen, which is your line. Now detach this screen

```
Ctrl-a d
```

and list your screen sessions

```
screen -ls
```

Now, you'll see

```
There are screens on:
      3591.session2	(Detached)
      5315.mySession	(Detached)
2 Sockets in /var/run/screen/S-user.
```

Now, you can re-attach the screen either by the name you gave it, or by the number
```
screen -r session2
```

Now let's exit out of this screen session. Do

```
Ctrl-d
```

And you will see that screen session has terminated.

To exit the other one, without reconnecting, you can type

```
screen -X -S 5315 kill
```

or

```
screen -X -S mySession kill
```

and the sessions will end.