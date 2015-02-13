---
title: Find Command
layout: default
group: Shell
type: advanced
---

### The Command `find`

The command `find` searches the filesystem for files based on their metadata.
The metadata that can be used to search for files includes, but is not limited
to a file's:

  * Filename
  * Filetype
  * Size
  * Creation Date
  * Access Date
  * Modification Date
  * Executables
  * Permission Mode

Unlike search mechanisms found outside a terminal (like Window Search or Apple's
Spotlight) which only list the files found, `find` can do things to the files it
finds. The tasks you can have `find` do are limited only by your imagination.
The syntax for `find` is:

``` nohighlight
find [-H] [-L] [-P] [-D debugopts] [-Olevel] [path...] [expression]
```

but the key to using find is in the path and expression arguments, which can be
complex. 

The optional `path` arguments tell `find` where to begin looking for files. If
not given, the current directory is used.`find` will ordinarily enter
subdirectories, but not parent directories of the given paths. 

A good practice is to explicitly enter the path `.` to search the current
directory, even though it is the default path.
{:.alert .alert-info}

The `expression` is made up of *option switches*, *tests*, and *actions*, each
separated by an *operator*. The format of these expression elements varies, and
are fully documented in the manual page `man find`. There are *too many*
expression elements to cover here, but below are listed the ones that we think are
the most useful or noteworthy.

* * *

#### Options
 
Options affect the behavior of `find` as a whole. Commonly used options include:

`-depth`
  : Process a directory's contents before the directory itself. Basically work
  from the bottom up.
{:.dl-horizontal}

  Deleting directories requires they be empty, so some actions like `-delete`
  will imply `-depth` automatically.
  {:.alert .alert-warning}

`-maxdepth LEVEL`
  : Descend only to at most a positive integer LEVEL below the given path.
{:.dl-horizontal}

  Do not confuse `-maxdepth` with `-depth`: they have completely different
  behaviours and uses.
  {:.alert .alert-warning}

`-mindepth LEVEL`
  : Do not apply tests or actions at levels above LEVEL.

`-help`
  : Print usage hints to the terminal.
{:.dl-horizontal}

* * *

#### Tests
 
Tests are used to compare a file against some reference. If the test comparison
yields true, the next test or action in the expression (read left to right) is
applied. If a test yields false, `find` moves on to the next file. Commonly used
tests include:

`-name PATTERN`
`-iname PATTERN`
  : Match parts of the filename (excluding parent directories). `-name` is
  case-sensitive, whereas `-iname` is case-insensitive. The `PATTERN` can
  include **wildcard characters**.
{:.dl-horizontal}
  
  Common wildcards include:\\
  `*` which matches any number of any characters,\\
  `?` which matches one position of any character, and\\
  `[ EXPR ]` will match a **POSIX bracket expression** in one position. 
  The syntax for bracket expressions is beyond the scope of this tutorial but
  we'll see some examples of what they look like.
  {:.alert .alert-info}

`-regex REGEXP`
  : Matches the whole path against a **regular expression** also referred to as
  a **regex** or **regexp**.
{:.dl-horizontal}

  Regular expressions are an extremely powerful means of matching patterns. They
  are used in many places and are worth learning, but deserve a treatment in
  their own right.
  {:.alert .alert-info}

`-size n[bcwkMG]`
  : Matches files greater than n units of space. The suffixes correspond to
  blocks, bytes, words, kilobytes, Megabytes, and Gigabytes respectively.

`-readable`
`-writeable`
`-executable`
  : Matches files to which you have these access permissions.

`-type c`
  : Matches files of type `c` where `c` is typically one of\\
  `d` for directory,\\
  `f` for regular file, or\\
  `l` for symbolic link. Other types also exits.\\
  See the manual page for more info.

`-mtime [+-]N`
`-ctime [+-]N`
`-atime [+-]N`
  : Matches against modification, creation, or access timestamps exactly N days
  ago. If N is preceded by `+` (`-`), times greater (less) than N days ago are
  matched.
{:.dl-horizontal}

* * *

#### Actions

Actions do something, either emit a response from `find` or run an arbitrary
command on a matched file. By default, `find` does the action `-print` when it
matches a file, which prints the full file name (with path starting from a
path argument) separated by a new line. Commonly used actions include:

`-exec CMD {};`
`-execdir CMD {};`
  : This option executes an arbitrary command `CMD`. The command can be
  anything.  All arguments following `-exec` are assumed to be part of the
  command until the first occurance of `;`. The (optional) characters `{}`, if
  encountered in the command expression, are replaced with the path to the
  currently examined file. If you used `-execdir`, find will run the command
  from the subdirectory containing the matched file.

`-ok CMD ;`
  : Like `-exec` but prompts the user before executing the command. Very useful
  if your expression may alter the file. It cannot take `{}` to represent the
  current matched file, so use it in conjunction with `-exec` as needed for
  safety.

`-print`
  : Prints the matched file's name.

`-printf FORMAT`
  : Prints the matched file's attributes according to FORMAT. See the man page
  for details.

`-quit`
  : Stop finding more files.

`-prune`
  : If the file is a directory, do not enter it. Used to eliminate
  subdirectories that you do not care to search.
{:.dl-horizontal}

* * *

#### Operators

Operators group expression elements together and allow for logic matching. The
operators, in decending order of precedence, are:

`( EXPR )`
  : Groups an expression together.

`! EXPR`
`-not EXPR`
  : Negates the expression.

`EXPR1 EXPR2`
`EXPR1 -a EXPR2`
`EXPR1 -and EXPR2`
  : Combines the two expressions with the logical conjunction "and".
{:.dl-horizontal}
  
By default, if two expressions are given without an operator joining them, the
operator `-and` is assumed.
{:.alert .alert-info}

`EXPR1 -o EXPR2`
`EXPR1 -or EXPR2`
  : Combines the two adjacent expressions with the logical disjunction "or".

`EXPR1 , EXPR2`
  : Processes both expressions, but discards the value of EXPR1 and uses the
  value of EXPR2. This is used in creative cases to search for multiple types of
  files in one traversal of the filesystem.
{:.dl-horizontal}

**Be mindful of the <kbd>Spaces</kbd> surrounding everything!** Each of the
expression elements is technically a command argument. As said earlier, all
arguments must be separated by a space. This includes `(` and `)`
{:.alert .alert-warning}

Many shells treat the characters `*[]{}()?$` amongst others as special
operators. To prevent your shell from altering any input to `find`, **wrap
expressions in quotations** as necessary. If in doubt, use quotes.
{:.alert .alert-warning}

* * *

#### Examples

Print all regular files named exactly ".bashrc" within and below `~`:

``` nohighlight
$ find ~ -type f -name bash.rc 
```

Print all regular files ending in "rc" within `~` and below:

``` nohighlight
$ find ~ -type f -name "*rc"
```

Print all files (regular and directories) ending in "rc" within `~`:

``` nohighlight
$ find ~ -name "*rc"
```

Print only directories one level into `/etc` that are 3 characters
long which end with "sh" or "sl"

``` nohighlight
$ find /etc -maxdepth 1 -type d -name "?s[hl]"
```

Find all files in `~` ending with ".jpg" or ".png" in any case that were created
within the last 2 days.

``` nohighlight
$ find ~ -type f \( -iname "*.jpg" -or -iname "*.png" \) -and -ctime -2
```

Find all the files strictly in `/tmp` named "data_NN.dat" where NN runs from
00-99 and run the command `ls -l FILE` on each of them: 

``` nohighlight
$ find /tmp -maxdepth 1 -type f -iname "data_[0-9][0-9].dat" -execdir ls -l {} \;
```

Have you ever needed to analyze hundreds of data files?  Imagine if instead of
calling `ls` on these files, you called a program that you wrote to analyze that
data. This is a quick way to generate those hundreds of plots you need to
process from your research data.
{:.alert .alert-info}
