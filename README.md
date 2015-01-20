# practical-scientific-computing.github.io
public website for the practical scientific computing workshop

https://practical-scientific-computing.github.io/

## Directory Structure

## Creating a Page

### YAML Front Matter

Each page written in markdown requires some Front Matter for the Jekyll
processing engine. The front matter is contained in a block delimited by
`---`.

```Markdown
---
title: Page title string
layout: default
group: Group Name
ordering: 1
---
```
The `title` variable is the name of the page as it would appear in a browser
window. The `title` is also used to populate navigation menu entries, so it is
**required** and best kept short in length.

The `layout` variable is a standard Jekyll variable naming the template used
to render the page. See the Jekyll documentation for more information and other
built-in variables. The `layout` is **required** to properly render a page.

The case-sensitive group string is used to sort pages in the main navigation bar.
Only groups that are hard-coded in `_include/bootstrap_navbar.html` are included 
in the navigation.

The `group` must be spelled as it would appear in a drop-down menu and all pages
in the group that are to be shown in the navigation require an appropriately
defined `group`. Initially, there are four groups included in the navbar:

 * Mathematica
 * Shell
 * Python
 * C/C++

The `ordering` variable is used to sort pages that appear in the navigation bar.
If `ordering` is omitted (ie, null) then those pages appear at the bottom of the
menu and are sorted alpha-numerically by filename.

