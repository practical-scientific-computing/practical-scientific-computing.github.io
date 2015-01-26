---
title: Flow Control
ordering: 4
layout: default
group: Python
type: tutorial
---

# Flow Control and Logic

We've seen some basic math operations and data structures in Python, but to
really tie it altogether, we will need a few more things. The first is how to
make comparisons between two objects. The second is how to change the behavior
of our programs given certain conditions. And lastly, we often need to do
certain tasks repeatedly, so we'll need a way to repeating or looping some
instructions. We will now discuss how to make **comparison
tests**, **conditionals**, **branches**, and **loops** in Python.

## Comparison Testing

Generally, we can compare two objects using one of the **comparison operators**.

| **Operator** | &nbsp; | **Operation**               | &nbsp; | **Syntax** | &nbsp; | **Description**                                       |
|-------------:|--------|:----------------------------|--------|:-----------|--------|:------------------------------------------------------|
| `==`         | &nbsp; | Tests Equality              | &nbsp; | `a == b`   | &nbsp; | True if a is equivalent to b; False otherwise         |
| `!=`         | &nbsp; | Tests Inequality            | &nbsp; | `a != b`   | &nbsp; | True if a is inequivalent to b; False otherwise       |
| `<>`         | &nbsp; | Tests Inequality            | &nbsp; | `a <> b`   | &nbsp; | True if a is inequivalent to b; False otherwise       |
| `>`          | &nbsp; | Tests greater-than          | &nbsp; | `a > b`    | &nbsp; | True if a is strictly greater than b; False otherwise |
| `<`          | &nbsp; | Tests less-than             | &nbsp; | `a < b`    | &nbsp; | True if a is strictly less than b; False otherwise    |
| `>=`         | &nbsp; | Tests Greater-than-or-equal | &nbsp; | `a >= b`   | &nbsp; | True if a is not less than b; False otherwise         |
| `<=`         | &nbsp; | Tests Less-than-or-equal    | &nbsp; | `a <= b`   | &nbsp; | True if a is not greater than b; False otherwise      |

Comparisons are by definition binary operations meaning you need two objects two
compare. Usually, the objects need to be of the same (or logically similar) types.
The result of a comparison is a boolean, ie, true or false.  How this works is
pretty straight-forward for numeric objects.

```Python
5 < 2
5 == 5
2 != 5
```

Many objects **overload** these operators so that they can be used intuitively
with objects that are not numerics. With lists, for example:

```Python
# Lists are compared element-wise, item-by-item
[1, 2, 3] == [1, 2, 3] # Equal, element-by-element.
[1, 2, 3] == [1, 3, 2] # Same length, but 3 != 2. 
[1, 2, 3] == [1, 2]    # Unequal lengths, so not equal.
[1, 2, 3] > [1, 2]     # Excess elements only considered if sublist checks out.
[1, 1, 3] > [1, 2]     # 1 < 2 so False.
```

Python doesn't care if you mix floats and integers: they're both numerics and
Python knows how to handle that up to a certain exception:

```Python
0.2 = 2/5
1.0 == 1
0.999999999999999 == 1
0.99999999999999999 == 1 # Huh?
```
This last comparison is an example of floating-point representation error and
all computers and programming languages suffer from it. Most of the time, this
effect doesn't matter but when it does (as is sometimes the case in science)
there are ways around it. In Python, these issues can be skirted when necessary
by a 3rd party library called 'NumPy' (For **Num**eric **Py**thon). We'll talk
about NumPy in detail later.

Comparisons can apply to non-numeric objects as well, but things can get tricky.
Take strings for example:

```Python
# Strings are iterables and again, comparison between
#   iterables are character-by-character.
'Jake' == 'Jake'
'Finn' == 'Finns'

# Here's something neat:
'prismo' > 'Prismo'

# As seen below, Python gives priority to capital letters
# which means capitals are 'smaller' than lower case.
alpha = list('AaBbCc'); alpha.sort(); print(alpha)
numerics = list(range(5)); numerics.sort(); print(numerics)
```
So the message is this: many objects support comparison out-of-the-box, but you
need to be aware of the rules used to make the comparison.

### `is` vs `==`

When we saw the list of keywords, there was a comparison keyword `is` which can
be used to test object identity. It is easy to confuse this with object
equality.

```Python
1 == 1.0  # Literals that are equal...
1 is 1.0  # ... are not necessarily the same object.
```
The instruction `a is b` is shorthand for `id(a) == id(b)`. Remember how
assignment to a variable name is ordinarily just an alias? Here we see that
again:

```Python
a = 5
b = [1, a, 3] # Make a list with 'a' as an element.
b[1] is a     # True!

# This is a bad example because 'a' aliases an immutable object.
# Let's try it again with a mutable object:
c = [1, 2, 3]   # Here we make a list (a mutable object)
c is [1, 2, 3]  # False because the '[1, 2, 3]' is a NEW list.
c == [1, 2, 3]  # True
```

### Other Comparison Keywords

Between now and the last tutorial, we've seen all comparison keywords.  The
set of them consists of `is`, `not`, `and`, `or`, and `in`. We are now in a
position to understand more about how they work.

We glossed over `in` last time but now we can look at it more closely. Keyword
`in` tests for an object's membership in an iterable by comparing the object *by
value* to all the items in an iterable.

```Python
1.0 in [1, 2, 3]  # True, because:
1.0 == 1          # is true by value, even though:
1.0 is not 1      # by identity. 
```

As we see in the last line above, we can use the keyword `not` to negate keyword
comparisons. We talked about `and`, `not`, and `or` in regards to booleans.  We
can use these keywords with comparisons because comparisons are themselves
boolean statements,


```Python
1 in c               # Seen it. True!
c is [1, 2, 3]       # Seen it. False!
c is not [1, 2, 3]   # 'not' negates the statement. True! This is equivalent to
not (c is [1, 2, 3]) #   ie 'not (True)'
3 not in c           # False!
5 not in c           # True!
```

Comparisons can be chained together. Because comparison operators are binary,
the statement doesn't necessarily read like in pen-and-paper math:

```Python
4 < 7 == 7.0  # True, same as:
(4 < 7) and (7 == 7.0)

4 < 7 and 3 not in c # False!
4 < 7 or 3 not in c  # True!

(4 < 7) or (3 not in c)  # Same as above, but easier to read with parantheses.
((4 < 7) or 3) not in c  # Parentheses used to change order of comparison.
```

## Conditionals and Branching

Now we can use comparisons to alter program flow, also called **branching**.
Branching in Python is done with the **conditional** keywords `if`, `else`, and
`elif`.  There are **no unconditional branches** in Python (like the dreaded and
icky goto statement). For the record, there are also no case or switch branches
in Python. All branching starts with the basic conditional `if` with the
following syntax:

```Python
if boolean_statement:
    # This code is run if condition is True
    do_these_instructions
    until_the_indentation
    goes_back_to_normal

# This code is run after the branch.
outside_code
```

A few things to point out here are the colon `:` which marks the end of the
conditional line. Omitting the colon is a syntax error.  When
`boolean_statement` evaluates to `True`, the code in the body of the `if`
statement is executed. The body consists of all lines that are **indented
further than code outside the block**, ie, the conditional statement. The amount
of indentation is arbitrary, but common convention is four spaces. Using
indentation and whitespace is a key design philosophy of Python: it forces
programmers to write code blocks that are visually separated.

When Python reaches the end of the code block, execution continues with
`outside_code`. When `boolean_statment` evaluates to `False`, the conditional
body is skipped and execution immediately goes on to `outside_code`. Let's look
at some examples:

```Python
max_temperature = 2e-3 # Kelvin
min_temperature = 1e-3 # Kelvin
fridge_temperature = 273  # Kelvin

if fridge_temperature > max_temperature:
    # The fridge is too hot.
    print('The fridge is not cold enough!')

if fridge_temperature < min_temperature:
    # Oops, too cold.
    print('Turn on the heaters or abort the experiment.')
```

This example always makes two checks on a fridge's temperature. We can optimize
this a little bit and skip the second check when the first one is true by using
the `else` statement.

```Python
if (max_temperature >= fridge_temperature
        >= min_temperature):
    # Fridge temperature within allowed range.
    print('Temperature OK. Proceed with experiment.')
else:
    print('Temperature out-of-range!')
```

Branches must have one and only one `if` statement and can optionally have a
single `else` statement.  Notice how the conditional line is wrapped? It is good
practice to make the indentation of a wrapped line to be different than all
lines around it so we don't confuse it as being part of the branch body. PEP8
recommends indenting wrapped lines by two levels.

Suppose we want to do something specific depending on whether the out-of-range
condition is hot or cold. We can use the `elif` statement to make additional
comparisons when the preceeding ones are false. You can have as many additional
`elif` statements as you like.

```Python
if (max_temperature >= fridge_temperature
      >= min_temperature):
    # Fridge temperature within allowed range.
    print('Temperature OK. Proceed with experiment.')
elif fridge_temperature > max_temperature:
    # Only run when above conditionals are false.
    print('Temperature too high.')
elif False:
    # This block will never run.
    pass
else:
    # Only run when all above conditionals are false.
    print('Temperature too low.')
```

The above statement has a branch that will never run. However, an **empty block
is a syntax error**. Comments do not qualify as filling a block because the
interpereter ignores them. To fill a block but have it do nothing, we can use
the `pass` keyword. When Python sees `pass`, it acknowledges the author intended
the line to do nothing. Again, explicit is better than implicit.

### Inline if (Ternary Statements)
Often we want to conditionally run a single command or set a variable. Writing a full if-else branch to
do this is tiresome. So Python, and many other languages implement a so-called
**ternary operator** to do conditionals inline. The syntax for a ternary
statement in Python is:

```Python
a if conditional else b
```

Notice there are no `:` characters or blocks and everything is in a single line.
If the statement is so long and complicated that you need to break it up over
multiple lines, then you **shouldn't** be using a ternary statement. The output
is all inline so this can be used for assignment operations. It is also useful
in loops and some advanced topics like **comprehensions**.

```Python
adorables = ['bunny', 'puppy', 'kitty']
seen_object = 'bunny'
response = "d'awww" if seen_object in adorables else 'meh'
print(response)
```

## Loops
The last fundamental control flow in Python is repeating instructions in a loop.
Python is a popular language for many reasons, but the way it handles looping is
arguably one its best characteristics. There are two ways to loop in Python:
`for` and `while`. Loops have some additional flow control actions namely
`continue`, `break`, and `else`.

### For Loops
For loops repeat a block of code once for each item in a sequence. The syntax
of such a loop uses the `for` and `in` keywords:

```Python
for item in sequence:
    # Do this block of code for each 'item'.
    print(item)

# End of loop is the end of the block indentation.
```

What can be used as a sequence? Lots of things. First, iterables like lists,
strings, tuples, and sets are sequences. The output of the `range` built-in
function (technically called a **generator**) is iterable.  So are the keys of a
dictionary. Any object upon which we can use the `in` keyword can also be
for-looped over.

```Python
for i in (1, 2, 3):
    print(i**2)

for _ in range(10):
    # We don't need to use the iteration variable in the body.
    # A good practice is to use '_' as the iterator name
    # when the body doesn't make use of it.
    print('Print this statement 10 times.')

quarks = ['up', 'down', 'charm', 'strange', 'top', 'bottom']
for quark in quarks:
    # Variable 'quark' is assigned to current item in sequence.
    charge = '2/3e' if quark[0] in 'uct' else '-1/3e'
    print('Charge of ' + quark + ' is ' + charge)

for quark in quarks:
    # Because lists are mutable, we can modify them while
    # looping over them.
    index = quarks.index(quark)
    quarks[index].upper()
```

There are two things to learn from the last example.  First is that we can
modify a mutable sequence while looping over it.  This can be useful, but is
potentially dangerous! If we increase the length of the sequence each iteration,
we can run into this:

```Python
# DANGER! DO NOT RUN THIS CODE...
# or do: I'm a comment, not a cop.
# If you choose to run this, you will enter an infinte loop that
# will fill your computer's memory. Use Ctrl-C to exit the loop.
quarks = ['up', 'down', 'charm', 'strange', 'top', 'bottom']
for quark in quarks:
    # Appending to quarks while looping over it
    #   causes a runaway condition.
    # Even worse, the appended elements get bigger
    #   and bigger until  you run out of memory.
    quarks.append('anti-' + quark)
```

The safe way to do this is by looping over a copy of the object while modifying
the original:

```Python
# This won't enter a runaway loop or consume all your memory.
quarks = ['up', 'down', 'charm', 'strange', 'top', 'bottom']
for quark in list(quarks):
    # We used the list ctor to make a copy and 
    #   then we loop over the copy:
    quarks.append('anti-' + quark)
```

The second thing to learn from the upper-case example, is that we often want the
loop body to make use of both the item in a sequence and it's position in the
sequence. The best way to do this is by using the `enumerate` built-in function,
which returns an iterable of (index, item) pairs from an iterable argument:

```Python
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
   print(index, color)
   colors[index].upper()
```

So Python handles loops in a smart way. Compare the following simple example in
several other languages:

```CPP
// C/C++ needs very specifc iterator setup.
int a[] = { 1, 2, 3, 4, 5 };
for(int i = 0; i < (sizeof(a)/sizeof(*a)); i++)
{
  printf("%d\n", i*i);
}
```

```Mathematica
(* Mathematica can be hard to read for complex commands. *)
a = [1, 2, 3, 4, 5]
For[i = 0, i < Length[a], i++, Print[a[i]]]
```

```Python
# Python allows this, but considers it 'unpythonic':
a = [1, 2, 3, 4, 5]
for i in len(a):
    print(a[i])

# The pythonic way is to write:
for i in a:
    print(i)
```

The pythonic way is simple, clean, clear, and elegant with no need to check lengths
or array sizes. Of course these are trivial examples. The difference really
shines once your code starts to get complex.

### While Loops

While loops simply repeat until a test condition evaluates as `False`. The
syntax goes as:

```Python
while conditional:
    # Do the loop body if conditional is 'True'
    some_body_code

# Once conditional is 'False', resume execution here.
outside_the_loop_code
```

Here are some examples of `while` loops:

```Python
# Sit in this loop until interrupted.
while True:
    pass

# Compute the Fibonacci numbers less than 200
last, current = 0, 1
while current < 200:
    print(current)
    last, current = current, last + current
```

If the body of `while` loop doesn't alter the test condition into a false state,
the loop will continue until the the computation is interrupted either by the
user (Ctrl-C in a shell) or by the machine (program crash, low memory).

### Loop Flow Control
Loops execution can be modified by some additional keyword statements.
We can skip the remaining body of a loop for one iteration with the 
`continue` statement. This will advance the smallest enclosing loop
immediately to the next iteration.

```Python
superheroes = ['spider man', 'wolverine', 'professor x',
               'batman', 'jean grey', 'catwoman',
               'superman', 'green lantern']

# Print only names that do not have '-man' suffix.
for hero in superheroes:
    hero = hero.title()
    if 'man' in hero:
        continue
    print(hero)

numbers = [1, 2, 3, 4, 5, 6]
# Print the odd squares in the list.
for number in numbers:
    if not (number % 2):
       continue
    print(i, 'squared is', i**2)
```

We can use the `break` statement to skip all further iterations of the smallest
enclosing loop.

```Python
for i in range(10):
    if i == 5:
        # When i == 5, stop the loop
        break
    print(i)
print('Loop terminated')
```

Lastly, a loop can take an `else` clause which is called when a loop finishes
normally. If a loop ends due to `break`, the `else` clause is skipped.


```Python
primes_count = 0
prime_candidate = 2
# Find the first 10 prime numbers.
while primes_count < 10:
    for factor in range(2, prime_candidate):
        if prime_candidate % factor == 0:
            # Non-prime
            break
    else:
        # Loop didn't hit 'break'
        print(prime_candidate, 'is prime')
```

## Summary

We've seen how to do **comparisons**, **conditional branches**, and two types of
**loops**. Next we will learn how to write our own functions so we can organize
our code into reusable logical groups.

Now would also be a good time to take a look at data structure
[comprehensions](/python/adv-comprehensions.html).
