---
title: Using curl to fetch a file
layout: default
group: Shell
type: example
---

# Downloading a file from the web

LibcURL is a library for copying and downloading a file from an external url.
This is very useful if you want to fetch a file from the web via a remote, text only system.

You can use curl to download a file from the web easily from the shell. 
Lets fetch a file from the matplotlib python examples

```
curl -o http://matplotlib.org/examples/animation/basic_example.py
```

Note that the option `-o` is needed to get this command to work correctly.
