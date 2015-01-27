---
title: Functions
ordering: 5
layout: default
group: Python
type: tutorial
published: true
---

# Functions

Functions are constructs that encapsulate a set of instructions to be reused
throughout a program. Like mathematical functions, Python functions take any
number of input arguments and return a single ouput. Functions always return an
object, although in Python, that object is not always important. If a function
doesn't explicitly return an object, it will automatically return `None`.

To define a function, we use the `def` keyword followed by the name we wish to
give the function. The name must be unique else the new function will replace
any other object (functions, variables, etc) of the same name in the current
**namespace**. The name of the function is followed without a space by a tuple
of the argument names the function is to accept. Lastly, the tuple is followed
by a colon `:` and the body of the function begins on the next line. As with
conditionals, the body block is denoted by indentation. The `return` keyword may
be invoked at any time during a branch within the function. When Python reaches
a `return`, the function exits. If `return` is followed by an object, that
object is passed out of the function as output. Otherwise `None` is returned. If
Python reaches the end of the function body without encountering `return`, the
function exits and `None` is returned.

Let's look at some examples.

**In [1]:**

{% highlight python %}
# Take an iterable of arbitrary length as a vector
#   and return a list representing the normalized
#   input vector.
def verbose_normalize(vector):
    squared_elements = []
    for i in vector:
        squared_elements.append(i**2)
    magnitude = (sum(squared_elements))**(1/2)
    output = []
    for i in vector:
        output.append(i / magnitude)
    return output
    
# Same as above, but using comprehensions.
def normalize(vector):
    magnitude = (sum((i**2 for i in vector)))**(1/2)
    return [i/magnitude for i in vector]
{% endhighlight %}

**In [2]:**

{% highlight python %}
normalize([1, 2, 3]), normalize((1, 2, 3))
{% endhighlight %}




    ([0.2672612419124244, 0.5345224838248488, 0.8017837257372732],
     [0.2672612419124244, 0.5345224838248488, 0.8017837257372732])



There are a few of things to note here. First, Python knows how to do fractional
exponentiation. Second, unlike C/C++, we do not need to tell Python what type of
object the function is to return nor do we need to express the argument types.
You can pass anything into `normalize` and as long as that object supports the
operations done on it, the function will work. Python is what we call a **duck-
typed** language, from the expression "If it looks like a duck, swims like a
duck, and quacks like a duck, then it probably is a duck".

## Duck Typing

Python assumes that if it *can* operate on an object, then that object is in
fact what it was supposed to be operating on. This has it's ups and downs. On
the plus side, duck-typed code is:

 * shorter, easier to write and read
 * **polymorphic** by default - one function can handle multiple input types
without any more work on the author's part

The downsides to duck-typing are that Passing the wrong object can give two
kinds of runtime errors:

  * The function CAN process the input, but the output is meaningless
  * The function CANNOT process the input and the program crashes

Here's an example of the first type of error:

**In [3]:**

{% highlight python %}
normalize([1, 2, 3j])
{% endhighlight %}




    [(3.061616997868383e-17-0.5j),
     (6.123233995736766e-17-1j),
     (1.5+9.184850993605148e-17j)]



Above, we passed a list with an imaginary element to `normalize`. Our definition
for `normalize` doesn't compute the mathematically correct magnitude of a
complex vector. However, Python will give output because it knows how to do all
the operations asked on such a vector - it's just that they don't make sense in
this context. The second type of error is easier to catch at runtime:

**In [4]:**

{% highlight python %}
normalize('1, 2, 3')
{% endhighlight %}


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-b0b81ea61c1a> in <module>()
    ----> 1 normalize('1, 2, 3')
    

    <ipython-input-1-15ca5b16a0cf> in normalize(vector)
         14 # Same as above, but using comprehensions.
         15 def normalize(vector):
    ---> 16     magnitude = (sum((i**2 for i in vector)))**(1/2)
         17     return [i/magnitude for i in vector]


    /usr/lib/python3.4/site-packages/numpy/core/fromnumeric.py in sum(a, axis, dtype, out, keepdims)
       1699     """
       1700     if isinstance(a, _gentype):
    -> 1701         res = _sum_(a)
       1702         if out is not None:
       1703             out[...] = res


    <ipython-input-1-15ca5b16a0cf> in <genexpr>(.0)
         14 # Same as above, but using comprehensions.
         15 def normalize(vector):
    ---> 16     magnitude = (sum((i**2 for i in vector)))**(1/2)
         17     return [i/magnitude for i in vector]


    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


Trying to call `normalize` on a string leads to a `TypeError` because Python
doesn't know how to raise a string to a power. Both errors can be overcome by
writing clear, unambiguous code with focus on good documentation, unique
variable and function naming, vigilant namespace awareness, and unit-testing;
all of which you should be doing in any language.

## Avoiding Runtime Errors

To avoid runtime errors in a duck-typed language, we need to adhere to some
basic good practices when writing functions. Some key points to writing good
functions are:

  * Function naming
  * Code Documentation
  * Clear Exits
  * Code reuse (Use many small functions opposed to few large ones)

### Function Naming

We've mentioned that function names should be made of full words, separated if
necessary by underscores. Because functions DO something, the name should often
be a verb. Likewise, argument names should usually be clear nouns that express
what the argument should be. Let's see the normalize example again:

**In [5]:**

{% highlight python %}
def nml(v):
    se = []
    for i in v:
        se.append(i**2)
    m = (sum(se))**(1/2)
    o = []
    for i in v:
        o.append(i / m)
    return o
{% endhighlight %}

Using crummy names for things forces the author to read the code carefully to
make sure they understand what's happening. This is bad for duck typed languages
because it hides the intended purpose of the function. We need to know what a
function is *intended* to do in order to prevent passing bad arguments to it.

### Code Documentation

Another thing we can do to help document the code is to **add a docstring to
every function you write**. Docstrings, as we saw before are printed when the
`help` function is called on an object. To add a docstring to your function,
include a multiline string as the first line of the function's body. Python will
know that this string is intended to be the docstring.

**In [6]:**

{% highlight python %}
def normalize(vector):
    '''Takes an arbitrary length iterable of real 
    numbers "vector" and returns the normalized
    vector as a list.
    '''
    magnitude = (sum((i**2 for i in vector)))**(1/2)
    return [i/magnitude for i in vector]
  
help(normalize)
{% endhighlight %}

    Help on function normalize in module __main__:
    
    normalize(vector)
        Takes an arbitrary length iterable of real 
        numbers "vector" and returns the normalized
        vector as a list.
    


Now, with a docstring, normalize has a note in the code that explains what the
function does and how it should be used that helps both the author maintain
their code and users apply the function. Too often in science, you or a colleage
will write code that makes sense when you write it but doesn't make sense months
or years later when you look at it to answer a journal referree how the
calculation was done. Documenting all of your functions, especially large and
complicated ones, with docstrings will help you greatly.

### Code Reuse

It is a good idea to write many small functions as opposed to a single large
one. Take for example this function to rotate a vector using Tait-Bryan angles:

**In [7]:**

{% highlight python %}
import numpy as np

def normalize(vector):
  """Returns a normalized N-vector parallel to the given vector.
  """
  try:
    return vector.normalize()
  except AttributeError:
    return np.array(vector) / np.linalg.norm(np.array(vector))


def rotation_matrix_euler(theta, axis):
  """Applies the Euler-Rodrigues formula to return the rotation matrix
  for a rotation about 3-vector 'axis' by the angle theta.
  """
  axis = normalize(axis)
  a = np.cos(theta/2)
  b, c, d = axis * np.sin(theta/2)
  return np.array(
      [[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
       [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
       [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])

def rotate_vector(vector, theta, axis):
  """Rotates a given vector by the angle theta about a given 3D-axis.
  """
  return np.dot(rotation_matrix_euler(theta, axis), vector)

def rotate_yxz_tait_bryan(vector, angles):
  """Returns the 3-vector rotated under the yx'z'' Tait-Bryan convention Euler
  angles. Argument 'angles' must be an interable over (phi, theta, psi).
  """
  axes = [[0, 1, 0],
          [1, 0, 0],
          [0, 0, 1]]
  output = vector
  for axis, angle in enumerate(angles):
    output = rotate_vector(output, angle, axes[axis])
  return output

{% endhighlight %}

Chances are, even without reading the code in great detail, you can build a
sense of what each function does because of the adherence to good programming
practices. The above code is broken down into 4 separate functions instead of
putting all of it into one function. This makes each individual task easier to
follow and, if something is wrong, debug. More importantly, it let's us reuse
common tasks like normalizing vectors elsewhere in our code.

At least one of the functions is rather exotic in that it applies the Euler-
Rodriguez formula to produce a matrix. The pen-and-paper math for this formula
is just as complex as the code. Without the docstring telling us the name of the
algorithm, a reader might be totally lost. Likewise, the docstring on
`rotate_yxz_tait_bryan` makes it clear what 'angles' are expected as an argument
by specifically calling them "Tait-Bryan convention Euler angles" and using
their standard math textbook symbol names.

We also see an exception to the rule on full-word variable names in
`rotation_matrix_euler`. In the other functions, longer variable names are
preferable and easier to read. But for such a complex forumula, it is sometimes
better to use short names. Especially when the short names match conventional
equation variables as is the case if one were to look up the Euler-Rodriguez
formula.

### Clear Branching and Exits

The functions in the above case usually have only one exit point (one `return`
statement per function). The exception is `normalize` which attempts to
normalize a vector passed to it by calling it's `vector.normalize` method (duck-
typing). However, if the argument doesn't have a `vector.normalize` method
(which would ordinarily crash the program), it does something else. The try-
except pattern that does this is called **exception handling**. Exception
handling is an advanced topic that we won't discuss here: it is rarely used for
small programs.

It is best to keep the exit points for your functions to a minimum. The same is
true for branching: Rather than have deeply nested branches in your code, try
instead to solve the problem differently or use functions to reduce the apparent
branching depth.

## More About Arguments

You could stop here and start writing functions, however, there are some finer
details to functions that you should know about if you become very involved with
Python. Let's take a look at some additional things you can do with function
arguments first.

### Argument Mutation

Mutable arguments passed to a Python function can be altered by the function
with or without a `return` value. For those familiar with C/C++, this is similar
to passing-by-reference. The return value here is not strictly speaking needed
and serves only to return an alias to the original object.

**In [8]:**

{% highlight python %}
print?
{% endhighlight %}

**In [9]:**

{% highlight python %}
def mutate_input(argument):
    '''Attempts to mutate the input argument.'''
    argument += '2'
    return argument
    
a = [1,2,3]
b = mutate_input(a)
print('The input is:', a,
      '\nThe return value is:', b,
      '\nAre they the same object?', a is b)
{% endhighlight %}

    The input is: [1, 2, 3, '2'] 
    The return value is: [1, 2, 3, '2'] 
    Are they the same object? True


**In [10]:**

{% highlight python %}
def returnless_mutate_input(argument):
    '''Attempts to mutate the input argument without returning
    an alias for it.'''
    argument += '2'
    
a = [1,2,3]
b = returnless_mutate_input(a)
print('The input is:', a,
      '\nThe return value is:', b,
      '\nAre they the same object?', a is b)
{% endhighlight %}

    The input is: [1, 2, 3, '2'] 
    The return value is: None 
    Are they the same object? False


If you ever need to gaurantee that a mutable input argument is NOT mutated, you
must explicitly pass a clone or clone the object within the function.

**In [11]:**

{% highlight python %}
a = [1, 2, 3]
b = mutate_input(list(a)) # Use the list ctor to pass a copy of 'a'.
print('The input is:', a,
      '\nThe return value is:', b,
      '\nAre they the same object?', a is b)
{% endhighlight %}

    The input is: [1, 2, 3] 
    The return value is: [1, 2, 3, '2'] 
    Are they the same object? False


If the input argument is an immutable object, a new object is created within the
function and must be passed out of the function with a return value. An
immutable argument is never modified in place.

**In [12]:**

{% highlight python %}
a = 'abc' # Immutable
b = mutate_input(a) # Cleverly crafted to work with strings and lists (quack quack). Returns a new object.
print('The input is:', a,
      '\nThe return value is:', b,
      '\nAre they the same object?', a is b)
{% endhighlight %}

    The input is: abc 
    The return value is: abc2 
    Are they the same object? False


**In [13]:**

{% highlight python %}
a = 'abc' # Immutable
b = returnless_mutate_input(a)  # Returns nothing, new object created within is destroyed on exit.
print('The input is:', a,
      '\nThe return value is:', b,
      '\nAre they the same object?', a is b)
{% endhighlight %}

    The input is: abc 
    The return value is: None 
    Are they the same object? False


### Positional Arguments

The examples we've seen so far make use of **positional arguments** where the
order objects are passed to the function in the argument tuple determines what
variable they are assigned to:

**In [14]:**

{% highlight python %}
def print_positional_arguments(first, second, third):
    '''Prints the arguments passed to the function in order
    to demonstrate positional arguments.'''
    print(first)
    print(second)
    print(third)
    
print_positional_arguments('cat', [0, 1, 2], None)
{% endhighlight %}

    cat
    [0, 1, 2]
    None


A function requires all positional arguments to have an object passed to them:

**In [15]:**

{% highlight python %}
print_positional_arguments('cat', [1, 2, 3]) # missing the third argument
{% endhighlight %}


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-9ea1279c39b0> in <module>()
    ----> 1 print_positional_arguments('cat', [1, 2, 3]) # missing the third argument
    

    TypeError: print_positional_arguments() missing 1 required positional argument: 'third'


The stack trace tells us exactly what went wrong.

### Named Arguments

Arguments can be passed in any order if their name is supplied with the object.
The name used to pass the argument must exactly match the name used in the
function definition.

**In [16]:**

{% highlight python %}
print_positional_arguments(second='cat', third=[0, 1, 2], first=None)
{% endhighlight %}

    None
    cat
    [0, 1, 2]


### Default Arguments

When we define a function, we can make positional arguments optional by
supplying them with a default value in the form of `variable=default_value` in
the function definition.

**In [17]:**

{% highlight python %}
def demo_default_args(logic, bargument='fun', spouse=None):
    '''Demonstrates default arguments. Argument 'logic' needs
    to be supplied, 'bargument' defaults to 'fun', and the
    spouse argument defaults to 'None'
    '''
    print('logic argument is', logic)
    print('bargument is', bargument)
    print('spouse argument is', spouse)
    
demo_default_args('interesting')
{% endhighlight %}

    logic argument is interesting
    bargument is fun
    spouse argument is None


Incidentally, here is where the use of `None` as a default argument shines,
especially when we'd like a mutable default. Take for instance this:

**In [18]:**

{% highlight python %}
def demo_mutable_default(mutable=[1, 2, 3]):
    '''Demonstrates why you want to use None instead of
    a mutable default argument.'''
    return mutable
  
a = demo_mutable_default() # Returns the default [1, 2, 3]
b = list(a)                # Make a copy of the returned list.
a[0] = 3                   # We mutate the returned value
c = demo_mutable_default() # Returns the default [1, 2, 3], right?
print('a is ', a,
      '\nb is', b,
      '\nc is', c,
      "\nIs 'a' identically 'c'?", a is c)
{% endhighlight %}

    a is  [3, 2, 3] 
    b is [1, 2, 3] 
    c is [3, 2, 3] 
    Is 'a' identically 'c'? True


What happened here? Python evaluates the default value of `mutable` when it
creates the function. Since we used a mutable literal, it is that single
instance that is passed every time we call the function! How should we have done
this?

**In [19]:**

{% highlight python %}
def demo_safe_mutable_default(mutable=None):
    '''Safely returns a default value for mutable [1, 2, 3]
    by using 'None' as the argument default and providing
    the usable default within the function body.'''
    return mutable if mutable is not None else [1, 2, 3]
  
a = demo_safe_mutable_default() # Returns the default [1, 2, 3]
b = list(a)                     # Make a copy of the returned list.
a[0] = 3                        # We mutate the returned value
c = demo_safe_mutable_default() # Returns the default [1, 2, 3], right?
print('a is ', a,
      '\nb is', b,
      '\nc is', c,
      "\nIs 'a' identically 'c'?", a is c)
{% endhighlight %}

    a is  [3, 2, 3] 
    b is [1, 2, 3] 
    c is [1, 2, 3] 
    Is 'a' identically 'c'? False


### Keyword Arguments

Keyword arguments, usually written as 'kwargs', allow us to pass **any arbitrary
number** of arguments to a function. To do this, we need to tell the function to
look for and catch any unknown argument by writing:

**In [20]:**

{% highlight python %}
def demonstrate_kwargs(first, second, **kwargs):
    '''Demonstrates keyword arguments.'''
    print(first)
    print(second)
    print(kwargs)
{% endhighlight %}

To catch kwargs, all positional arguments must come first in the argument tuple.

**In [21]:**

{% highlight python %}
demonstrate_kwargs('first', 'second')
{% endhighlight %}

    first
    second
    {}


After all the positional arguments have been passed, kwargs can be supplied to
the function.

**In [22]:**

{% highlight python %}
demonstrate_kwargs('first', 'second', third='third', fourth=4)
{% endhighlight %}

    first
    second
    {'fourth': 4, 'third': 'third'}


All the kwargs caught by the function are put into the dictionary `kwargs` where
the key is the supplied name and the value is the object on the RHS of the
assignment in the arg list: just like the ctor for a dictionary. The kwarg names
cannot match any exisiting positional argument (else Python will think you are
passing named positional arguments out of order) nor can they be duplicated (a
dictionary must have unique keys).

**In [23]:**

{% highlight python %}
demonstrate_kwargs('first', 'second', third='third', first=4)
{% endhighlight %}


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-23-e453de9802ec> in <module>()
    ----> 1 demonstrate_kwargs('first', 'second', third='third', first=4)
    

    TypeError: demonstrate_kwargs() got multiple values for argument 'first'


**In [24]:**

{% highlight python %}
demonstrate_kwargs('first', 'second', third='third', third=4)
{% endhighlight %}


      File "<ipython-input-24-668f095ea2f7>", line 1
        demonstrate_kwargs('first', 'second', third='third', third=4)
                                                            ^
    SyntaxError: keyword argument repeated



As before, you can call the positional arguments in any order as named
arguments.

**In [25]:**

{% highlight python %}
demonstrate_kwargs(fourth=4, first='first', second='second', third='third')
{% endhighlight %}

    first
    second
    {'fourth': 4, 'third': 'third'}


Lastly, we don't need to call them `kwargs`, that's just common convention.
What's important in the function definition is the `**` part of the kwargs
argument. `**` in this context is the **dictionary unpack** operator and can be
used to collapse a tuple of `key=value` into a dictionary or expand a dictionary
into a tuple of `key=value` pairs.

**In [26]:**

{% highlight python %}
def more_kwargs(**whatever_you_want):
    '''Demonstrates that the unpacked dictionary can be named
    whatever you want.'''
    print(whatever_you_want)
    
more_kwargs(see='told you')
{% endhighlight %}

    {'see': 'told you'}


We can pass all the positional arguments as named arguments with a single
unpacked dictionary.

**In [27]:**

{% highlight python %}
packed_arguments = {'first':1, 'second':2}
demonstrate_kwargs(**packed_arguments)
{% endhighlight %}

    1
    2
    {}


## Variable Scope

When you access a variable name, Python searchs **up** through the heirarchy of
namespaces until it finds a defined instance of the name. If Python cannot find
an instance of the name, a `NameError` is raised complaining that the name is
undefined.

A function is one construct that separates a namespace. The others are class
definitions and modules which we will talk about later. A variable name defined
within a function replaces any names defined in a higher scope but only within
the function. Likewise, higher scopes cannot introspect within lower scopes.

**In [28]:**

{% highlight python %}
defined_without = '"defined outside"'

def demo_scope():
    '''Demonstrate scope resolution.'''
    defined_within = '"defined inside"'
    print('Inside sees', defined_within, 'and', defined_without)
    
demo_scope()

print('Outside sees', defined_without)
print('But not', defined_within)
{% endhighlight %}

    Inside sees "defined inside" and "defined outside"
    Outside sees "defined outside"



    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-28-a09936df80b3> in <module>()
          9 
         10 print('Outside sees', defined_without)
    ---> 11 print('But not', defined_within)
    

    NameError: name 'defined_within' is not defined


An interesting thing about scope in Python is that not all blocks change the
namespace; only those of functions, class definitions, and modules. For
instance, if statements in C change scope, but not in Python:

**In [29]:**

{% highlight python %}
if 4 < 5:
    this_is_a_new_name = "How'd this get here?"

print(this_is_a_new_name)
{% endhighlight %}

    How'd this get here?


## Recursive Functions

Python supports recursion. For instance we can implement a recursive function to
calculate the factorial of a natural number:

**In [30]:**

{% highlight python %}
def factorial(number):
    '''Recursively computes the factorial of a
    natural number "number"'''
    if number == 0:
        return 1
    elif number > 0:
        # Call factorial from within factorial.
        return number * factorial(number - 1)


factorial(5)
{% endhighlight %}




    120



## Functions Are Objects

As said before, *everything* in Python is an object. This includes functions!
Functions are only called when they are given an argument tuple after their
name. Otherwise, they can be manipulated like any other object. Take for example
the factorial function we just made. Without an argument tuple, python just
tells us we're looking at an object of type `function`:

**In [31]:**

{% highlight python %}
factorial
{% endhighlight %}




    <function __main__.factorial>



We can assign a new name to this object just like any other object:

**In [32]:**

{% highlight python %}
factorial_alias = factorial
factorial_alias(5)
{% endhighlight %}




    120



We can pass a function to another function if we like:

**In [33]:**

{% highlight python %}
def use_five_times(function):
    '''Calls a function that accepts a single
    number as it's argument on the first five
    integers and returns a list of the results.'''
    return [function(i) for i in range(1,6)]
  
use_five_times(factorial)
{% endhighlight %}




    [1, 2, 6, 24, 120]



We can even use functions as `return` values.

## Nested Functions

You can even define a function within a function. Because a function changes
scope, the nested function is not visible outside it's enclosing function. A
useless and trivial example looks like this:

**In [34]:**

{% highlight python %}
def outer(x, y):
    '''Weak example of nested functions.'''
    def nested_function():
        '''Multiplies two variables from a higher scope.'''
        return x * y
    return x + nested_function()
{% endhighlight %}

The function `outer` has defined within it another function which can be used
internally:

**In [35]:**

{% highlight python %}
outer(5, 2)
{% endhighlight %}




    15



but not externally:

**In [36]:**

{% highlight python %}
nested_function()
{% endhighlight %}


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-36-17987d3e845d> in <module>()
    ----> 1 nested_function()
    

    NameError: name 'nested_function' is not defined


But that's a weak demonstration. How nested functions are *really* useful is by
doing things like this:

**In [37]:**

{% highlight python %}
def functionception(function, text):
    '''Demonstrates a function defined within a function.'''
    def pretty_print(*args):
        text_args = ' and ' if len(args) == 2 else ', and '
        text_args = text_args.join((str(i) for i in args))
        response = 'The {} of {} is {}'
        result = function(*args)
        print(response.format(text, text_args, result))
        return result
        
    return pretty_print
    
{% endhighlight %}

**In [38]:**

{% highlight python %}
decorated_add = functionception(add, 'sum')
decorated_add(3, 5)
{% endhighlight %}

    The sum of 3 and 5 is 8





    8



Or instead of saving the output to a new name, we can overwrite the name of the
function we fed into `functionception`.

**In [39]:**

{% highlight python %}
factorial = functionception(factorial, 'factorial')
factorial(5)
{% endhighlight %}

    The factorial of 0 is 1
    The factorial of 1 is 1
    The factorial of 2 is 2
    The factorial of 3 is 6
    The factorial of 4 is 24
    The factorial of 5 is 120





    120



## Decorators

We've just created a function that can create functions from functions. This is
really powerful, although its utility may not be immediately apparent. The names
I used above are suggestive: we can wrap or **decorate** one function with
another function. There is a special syntax for doing this when you define a
function using so-called **decorators**.

Decorators give us a way of injecting common code into functions. Take for
instance this decorator that prints the execution time of any function it's
applied to:

**In [40]:**

{% highlight python %}
def time_this(function):
    '''A decorator to print the execution time
    of a function.'''
    def wrapper(*arg):
        '''Timed decorated version of {}
        '''.format(function.__name__)
        from time import clock
        start = clock()
        result = function(*arg)
        print(function.__name__, ':', clock() - start, 's')
        return result

    return wrapper

# The '@' line is where the magic happens
# and is analagous to the earlier:
# `factorial = functionception(factorial, 'factorial')`

# Equivalent to writing
# factorial = time_this(factorial)
@time_this  
def factorial(number):
    '''Recursively computes the factorial of a
    natural number "number"'''
    if number == 0:
        return 1
    elif number > 0:
        # Call factorial from within factorial.
        return number * factorial(number - 1)
      
factorial(5)
{% endhighlight %}

    factorial : 3.0000000001972893e-06 s
    factorial : 0.00010399999999988196 s
    factorial : 0.00016599999999988846 s
    factorial : 0.00022400000000000198 s
    factorial : 0.0002830000000000332 s
    factorial : 0.0003469999999998752 s





    120



Decorators are advanced and this is as far as we'll go with them in these
tutorials, but it's good to know about them now so you are not surprised when
you see them again later.

## Built-in Functions

We've seen lots of them already, and it's appropriate now to show you the [list
of built-in functions](https://docs.python.org/3/library/functions.html), which
can be seen in the official Python documentation. I recommend you be aware of at
least `abs`, the ctors, `eumerate`, `range`, `print`, `help`, `max`, `min`,
`range`, `round`, `filter`, and `zip`.
