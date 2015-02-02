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
| `screen` | Screen        | use multipla virtual terminals in the same window
{:.table}

While you can dive in to the man pages yourself to get the full usage of these commands, we'll go over a few
key examples here.

## ssh

