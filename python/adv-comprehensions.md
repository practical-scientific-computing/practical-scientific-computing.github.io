---
title: Comprehensions
layout: default
group: Python
type: advanced
---

# Comprehensions

Once you've mastered loops and conditionals, we can talk about
**comprehensions**. Comprehensions are clever short-hand statements used to
create sequence data structures. for instance, we can fill a list by
manipulating data from another list quickly using **list comprehension**:

```Python
a = [1, 2, 3]
b = [i**2 for i in a]
c = [i**2 for i in a if i % 2 == 0]
```

We can see that the syntax for a list comprehension uses the list literal
operators `[` and `]` to enclose a deconstructed `for` loop:

```Python
# Unconditional list comprehension
[loop_body for iterator_variable in sequence]

# An optional conditional can be included to modify
#   when a new item is added to the new list.
[loop_body for iterator_variable in sequence if conditional]
```

Tuples can be formed the same way using **tuple comprehension**. The only
syntax difference from list comprehensions is the use of the tuple literal
operators:

```Python
b = (i**2 for i in range(10))
c = (i**2 for i in range(10) if i % 2 == 0)
```
Likewise, **set comprehensions** are formed using the same syntax but with the
set literal operators `{` and `}`:

```Python
superheroes = ['spider man', 'wolverine', 'professor x',
               'batman', 'jean grey', 'catwoman',
               'superman', 'green lantern']
one_name_heroes = {name for name in superheroes if ' ' not in name}
```

Dictionaries also have a comprehension but it is slightly more complicated than
the others. It looks like this:

```Python
{key : value for item in sequence}
```

For instance, 

```Python
# Make a dictionary from a string:
simple_dict = {i : j for i, j in enumerate('abcd')}

# To swap keys and values:
swapped = {j : i for i, j in simple_dict.items()}
```

## When To Use Comprehensions?

Well, comprehensions are great. The real question is when not to use them? You
should avoid using a comprehension when the whole expression is much longer than
a single 80-character long line. When you try to pack so much code into a single
line, it makes the program hard to follow. Otherwise, use them whenever you can.

