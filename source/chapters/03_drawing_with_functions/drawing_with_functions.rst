Creating Functions
==================

The goal of this chapter is to learn how to create our own functions to draw.
We don't want to be stuck with just ``draw_circle`` commands.
We want to be able to define create our own ``draw_tree`` or ``draw_house``
commands.

A **function** is a block of code that we can **call** with just one line.
Functions give us the ability to write:

* Clear, easy-to-read code.
* The ability to reuse code.

We have already *used* functions. Now we want *define* our own. Defining a
function is like giving a recipe to computer. Once we give the computer a
recipe for banana bread, we just have to tell the computer to "make banana
bread." There's no need to tell it the steps again.

To create our own drawing functions we need to learn three new skills:

* How to define a function
* How to use variables
* How to create simple mathematical expressions

How to Define a Function
------------------------

Defining a function is rather easy.

* Start with the keyword ``def``, which is short for "define."
* Next, give the function a name. There are rules for function names. They must:

  * Start with a lower case letter.
  * After the first letter, only use letters, numbers, and underscores.
  * Spaces are not allowed. Use underscores instead.
  * While upper-case letters can be used, function names are normally all
    lower-case.

* After that, we have a set of parenthesis. Inside the parenthesis will go
  **parameters**. We'll explain those in a bit.
* Next, a colon.
* Everything that is part of the function will be indented four spaces.
* Usually we start a function with a multi-line comment that explains what
  the function does.

Here is an example of a function:

.. code-block:: python

    def draw_grass():
        """
        This function draws the grass.
        """
        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

To call the function, all we need to do is:

.. code-block:: python

    draw_grass()

Below is a full program that defines and uses the function. Notice that
function definitions go *below* the ``import`` statements, and *above* the
rest of the program. While you can put them somewhere else, you shouldn't.

.. literalinclude:: drawing_with_functions_1.py
    :language: python
    :linenos:
    :emphasize-lines: 8-12, 20

Great! Let's make this scene a little better. I've created another function
called ``draw_pine_tree`` which will...you guessed it. Draw a pine tree.

Here's what it will look like:

.. image:: pine_tree.png

And here's the code:

.. literalinclude:: drawing_with_functions_2.py
    :language: python
    :linenos:
    :emphasize-lines: 15-26, 34

Great! But what if I want a forest? I want lots of trees? Do I create a function
for every tree? That's no fun. How can I create a function that allows me to say
where I want the tree? Like what if I wanted to draw three trees and specify
(x, y) coordinates of those trees::

    draw_pine_tree(45, 92)
    draw_pine_tree(220, 95)
    draw_pine_tree(250, 90)

To be able to do this, I need to learn about variables, expressions, and
function parameters.

How to Use Variables
--------------------

A **variable** is a value the computer stores in memory that can change. That
is, it *varies*.

You've used variables in mathematics before. With computer science, we use
them a lot. But in math class, you were given the equation and you had to
solve for the variable. In computer science class, *we* come up with the
equation and the *computer* solves the variable.

Here is a quick example:

.. code-block:: python

    # What will this print?
    x = 5
    print(x)

What will the code above print? It will print ``5``.

The ``=`` is called an **assignment operator**. It assigns the value on the
right side to the variable on the left.

Here's another example. Very similar, but something is different. What will
it print?

.. code-block:: python

    # What will this print?
    x = 5
    print("x")

The code above prints ``x``. Why not ``5``? Because:

* If there are no quotes, the computer evaluates code like a mathematical
  expression.
* If there are quotes, we treat what is between the quotes as a string of
  characters and don't change it.

In fact, that is what we call the characters between the quotes. A **string**,
which is short for "string of characters." We don't call it "text."

The following code won't print at all:

::

    print(Have a great day!)

The code above will fail because the computer will think that it should evaluate
``Have a great day!`` as a mathematical expression. It isn't, so the computer
gets confused and generates an error. That's why we need quotes:

.. code-block:: python

    print("Have a great day!")

Variable and Function Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variable names and function names follow the same rules. There are
names you *should* use, names you *shouldn't* use, and
names you *can't* use.

Good variable name examples:
    * temperature_in_celsius
    * tree_position
    * car_speed
    * number_of_children
    * simpson

Legal, but bad variable names:
    * temperatueInCelsius - Uses capital letters. Keep it lower case and use underscores.
    * x - Too short, and not descriptive.
    * Simpson - Starts with a capital letter.

Variable names that won't work:
    * tree position - Can't use spaces
    * 4runner - Can't start with a number

Sometimes we want to create a variable that won't change.
We call these variables **constants**.
By convention, these variable names are in all upper case. They are
the only variables that use upper-case. For example:

.. code-block:: python

    PI = 3.14159
    SCREEN_WIDTH = 600
    RED = (255, 0 ,0)

Good variable names help make code *readable*. Note the example below that
calculates miles-per-gallon. It isn't easy to understand.

.. code-block:: python

    # Calculate mpg using confusing variable names
    m = 294
    g = 10.5
    m2 = m / g
    print(m2)

But the code below that uses descriptive variable names *is* easy to understand.

.. code-block:: python

    # Calculate mpg using good variable names
    miles_driven = 294
    gallons_used = 10.5
    mpg = miles_driven / gallons_used
    print(mpg)

How to Create Expressions
-------------------------

Using Operators in Expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Great! We are part-way there. To really be powerful, variables need to be used
with **expressions**. An expression is simply a mathematical equation like what
you've used in math before. Here's an example:

.. code-block:: python

    # What will this print?
    x = 5 + 10
    print(x)

As you can probably guess, this will print out ``15``. We call the ``+`` sign
an **operator**. Here are some other operators:

========== =====================================
Operator   Description
========== =====================================
``+``      Addition
``-``      Subtraction
``*``      Multiplication
``**``     Exponentiation (raise to the power)
``/``      Division
``//``     Integer division (rounds down)
``%``      Modulus (gives remainder of division)
========== =====================================

There are two things that **don't** work like you'd expect. There is no
"juxtaposition" used to multiply items. And the ``=`` is not an algebraic
equality

Juxtaposition Doesn't Work
^^^^^^^^^^^^^^^^^^^^^^^^^^

Juxtaposition doesn't work for multiplication.
For example, the following will **not** work:

.. code-block:: python

    # The last two lines will error
    x = 3
    y = 2x
    z = 2(3 + x)

You can rewrite the code above to work by explicitly multiplying:

.. code-block:: python

    # This code works. Although it doesn't print anything.
    x = 3
    y = 2 * x
    z = 2 * (3 + x)

Easy enough, just remember to use ``*`` any time you want to multiply.

Assignment Operators
^^^^^^^^^^^^^^^^^^^^

The ``=`` doesn't work the same as in algebra. The ``=`` evaluates what is on
the right, and puts it in the variable on the left. For example:

.. code-block:: python

    # This works
    x = 3 + 4

    # This doesn't work because the only thing that can be on the left of
    # the = is one variable.
    3 + 4 = x

    # This works
    x = 5
    y = 6
    z = x + 2 * y

    # This doesn't
    x = 5
    y = 6
    2 * z = x + y

This allows us to do some strange things we can't do in algebra!

.. code-block:: python

    # This works, and prints "3"
    x = 3
    print(x)

    # This works too, even if it is invalid in algebra.
    # It takes the value of x (which is 3) and adds one. Then stores
    # the result (4) back in x. So we'll print "4".
    x = x + 1
    print(x)


The ``=`` sign is also considered an operator. Specifically an "assignment operator."
Here are some other "assignment" operators:

========== =====================================
Operator   Description
========== =====================================
``=``      Assignment
``+=``     Increment
``-=``     Decrement
``*=``     Multiply/Add
========== =====================================

.. code-block:: python

    # This works, and prints "3"
    x = 3
    print(x)

    # Make x bigger by one
    x = x + 1
    print(x)

    # Make x bigger by one, just like before
    x += 1
    print(x)

    # Make x smaller by five
    x += 5
    print(x)

Using Expressions In Function Calls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can use expressions even in the calls that we make. For example, what if we want
to draw a circle in the center of the screen?

We could do something like:

.. code-block:: python
    :linenos:
    :emphasize-lines: 12-15

    import arcade

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    # Instead of this:
    # arcade.draw_circle_filled(400, 300, 50, arcade.color.FOREST_GREEN)
    # do this:
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, arcade.color.FOREST_GREEN)

    arcade.finish_render()
    arcade.run()

Order of Operations
^^^^^^^^^^^^^^^^^^^

Python will evaluate expressions using the same order of operations that
are expected in standard mathematical expressions. For example this
equation does not correctly calculate the average:

.. code-block:: python

    average = 90 + 86 + 71 + 100 + 98 / 5

The first operation done is 98/5. The computer calculates:

.. math::

   90+86+71+100+\frac{98}{5}

rather than the desired:

.. math::

   \dfrac{90+86+71+100+98}{5}

By using parentheses this problem can be fixed:

.. code-block:: python

    average = (90 + 86 + 71 + 100 + 98) / 5

Returning and Capturing Values
------------------------------

Functions can not only take in values, functions can return values.

.. _returning-values:

Returning values
^^^^^^^^^^^^^^^^

For example:

Function that returns two numbers added together

.. code-block:: python

    # Add two numbers and return the results
    def sum_two_numbers(a, b):
        result = a + b
        return result

Note: Return is not a function, and does not use parentheses. Don't do
``return(result)``.

This only gets us half-way there. Because if we call the function now, not
much happens. The numbers get added. They get returned to us. But we do
nothing with the result.

.. code-block:: python

    # This doesn't do much, because we don't capture the result
    sum_two_numbers(22, 15)

Capturing Returned Values
^^^^^^^^^^^^^^^^^^^^^^^^^

We need to capture the result. We do that by setting a variable equal to
the value the function returned:

.. code-block:: python

    # Store the function's result into a variable
    my_result = sum_two_numbers(22, 15)
    print(my_result)

Now the result isn't lost. It is stored in my_result which we can print or use some other way.

Volume Cylinder Example
^^^^^^^^^^^^^^^^^^^^^^^

Function that returns the volume of a cylinder

.. code-block:: python

    def volume_cylinder(radius, height):
        pi = 3.141592653589
        volume = pi * radius ** 2 * height
        return volume

Because of the return, this function could be used later on as part of an
equation to calculate the volume of a six-pack like this:

.. code-block:: python

    six_pack_volume = volume_cylinder(2.5, 5) * 6

The value returned from volume_cylinder goes into the equation and is
multiplied by six.

There is a big difference between a function that prints a value and a
function that returns a value. Look at the code below and try it out.

.. code-block:: python

    # Function that prints the result
    def sum_print(a, b):
        result = a + b
        print(result)

    # Function that returns the results
    def sum_return(a, b):
        result = a + b
        return result

    # This prints the sum of 4+4
    sum_print(4, 4)

    # This does not
    sum_return(4, 4)

    # This will not set x1 to the sum
    # It actually gets a value of 'None'
    x1 = sum_print(4, 4)

    # This will
    x2 = sum_return(4, 4)


When first working with functions it is not unusual to get stuck looking at
code like this:

.. code-block:: python

    def calculate_average(a, b):
        """ Calculate an average of two numbers """
        result = (a + b) / 2
        return result

    # Pretend you have some code here
    x = 45
    y = 56

    # Wait, how do I print the result of this?
    calculate_average(x, y)

How do we print the result of calculate_average? The program can't print
result because that variable only exists inside the function. Instead, use
a variable to capture the result:

.. code-block:: python

    def calculate_average(a, b):
        """ Calculate an average of two numbers """
        result = (a + b) / 2
        return result

    # Pretend you have some code here
    x = 45
    y = 56

    average = calculate_average(x, y)
    print(average)

Documenting Functions
---------------------

Functions in Python typically have a comment as the first statement of the
function. This comment is delimited using three double quotes, and is called a
docstring. A function may look like:

.. code-block:: python

    def volume_cylinder(radius, height):
        """Returns volume of a cylinder given radius, height."""
        pi = 3.141592653589
        volume = pi * radius ** 2 * height
        return volume

The great thing about using docstrings in functions is that the comment can be
pulled out and put into a website documenting your code using a tool like
Sphinx. Most languages have similar tools that can help make documenting your
code a breeze. This can save a lot of time as you start working on larger
programs.

Variable Scope
--------------

The use of functions introduces the concept of scope. Scope is where in the
code a variable is "alive" and can be accessed. For example, look at the code
below:

.. code-block:: python

    # Define a simple function that sets
    # x equal to 22
    def f():
        x = 22

    # Call the function
    f()
    # This fails, x only exists in f()
    print(x)

The last line will generate an error because x only exists inside of the f()
function. The variable is created when ``f()`` is called and the memory it uses is
freed as soon as ``f()`` finishes.

Here's where it gets complicated.
A more confusing rule is accessing variables created outside of the ``f()``
function. In the following code, x is created before the ``f()`` function, and
thus can be read from inside the ``f()`` function.

.. code-block:: python

    # Create the x variable and set to 44
    x = 44

    # Define a simple function that prints x
    def f():
        print(x)

    # Call the function
    f()

Variables created ahead of a function may be read inside of the function only
if the function does not change the value. This code, very similar to the code
above, will fail. The computer will claim it doesn't know what x is.

.. code-block:: python

    # Create the x variable and set to 44
    x = 44

    # Define a simple function that prints x
    def f():
        x += 1
        print(x)

    # Call the function
    f()

Other languages have more complex rules around the creation of variables and
scope than Python does. Because Python is straight-forward it is a good
introductory language.

Pass-by-Copy
------------

Functions pass their values by creating a copy of the original. For example:

.. code-block:: python

    # Define a simple function that prints x
    def f(x):
        x += 1
        print(x)

    # Set y
    y = 10
    # Call the function
    f(y)
    # Print y to see if it changed
    print(y)

The value of y does not change, even though the f() function increases the
value passed to it. Each of the variables listed as a parameter in a function
is a brand new variable. The value of that variable is copied from where it is
called.

This is reasonably straight forward in the prior example. Where it gets
confusing is if both the code that calls the function and the function itself
have variables named the same. The code below is identical to the prior listing,
but rather than use y it uses x.

.. code-block:: python

    # Define a simple function that prints x
    def f(x):
        x += 1
        print(x)

    # Set x
    x = 10
    # Call the function
    f(x)
    # Print x to see if it changed
    print(x)

The output is the same as the program that uses y. Even though both the
function and the surrounding code use x for a variable name, there are
actually two different variables. There is the variable x that exists
inside of the function, and a different variable x that exists outside
the function.

Functions Calling Functions
---------------------------

For each of the examples below, think about what would print. Check to see
if you are right. If you didn't guess correctly, spend to the time to
understand why.

Example 1
^^^^^^^^^

In this example, note that if you don't use a function, it doesn't run.

.. code-block:: python

    # Example 1
    def a():
        print("A")

    def b():
        print("B")

    def c():
        print("C")

    a()

Example 2
^^^^^^^^^

.. code-block:: python

    # Example 2
    def a():
        b()
        print("A")

    def b():
        c()
        print("B")

    def c():
        print("C")

    a()


Example 3
^^^^^^^^^

.. code-block:: python

    # Example 3
    def a():
        print("A")
        b()

    def b():
        print("B")
        c()

    def c():
        print("C")

    a()

Example 4
^^^^^^^^^

.. code-block:: python

    # Example 4
    def a():
        print("A start")
        b()
        print("A end")

    def b():
        print("B start")
        c()
        print("B end")

    def c():
        print("C start and end")

    a()


Example 5
^^^^^^^^^

.. code-block:: python

    # Example 5
    def a(x):
        print("A start, x =",x)
        b(x + 1)
        print("A end, x =",x)

    def b(x):
        print("B start, x =",x)
        c(x + 1)
        print("B end, x =",x)

    def c(x):
        print("C start and end, x =",x)

    a(5)

Example 6
^^^^^^^^^

While line 3 of this example increases ``x``, the ``x`` variable in the function is a different variable than the
``x`` that is in the rest of the program. So that ``x`` never changes.

.. code-block:: python

    # Example 6
    def a(x):
        x = x + 1

    x = 3
    a(x)

    print(x)

Example 7
^^^^^^^^^

This example is similar to the prior example, but we ``return x`` at the end. Turns out, it doesn't matter. Because we
never do anything with the return value. So the global variable ``x`` still doesn't increase. See the next example.

.. code-block:: python

    # Example 7
    def a(x):
        x = x + 1
        return x

    x = 3
    a(x)

    print(x)

Example 8
^^^^^^^^^

This example take the value returned from ``a`` and stores it back into ``x``. How? By doing ``x = a(x)`` instead of
just ``a(x)``.

.. code-block:: python

    # Example 8
    def a(x):
        x = x + 1
        return x

    x = 3
    x = a(x)

    print(x)

Example 9
^^^^^^^^^

.. code-block:: python

    # Example 9
    def a(x, y):
        x = x + 1
        y = y + 1
        print(x, y)

    x = 10
    y = 20
    a(y, x)

Example 10
^^^^^^^^^^

While you can have two ``return`` statements in a function, once you hit the first ``return`` the function ends. In
this case, ``return y`` never runs, because we already returned from the function in the prior line.

.. code-block:: python

    # Example 10
    def a(x, y):
        x = x + 1
        y = y + 1
        return x
        return y

    x = 10
    y = 20
    z = a(x, y)

    print(z)

Example 11
^^^^^^^^^^

This is not something you can do in every programming language. You can return two values by using a comma and listing them.

.. code-block:: python

    # Example 11
    def a(x, y):
        x = x + 1
        y = y + 1
        return x, y

    x = 10
    y = 20
    z = a(x, y)

    print(z)

Example 12
^^^^^^^^^^

If you return two values out of a function, you can capture them this way.

.. code-block:: python

    # Example 12
    def a(x, y):
        x = x + 1
        y = y + 1
        return x, y

    x = 10
    y = 20
    x2, y2 = a(x, y) # Most computer languages don't support this

    print(x2)
    print(y2)

Example 13
^^^^^^^^^^

.. code-block:: python

    # Example 13
    def a(my_data):
        print("function a, my_data =  ", my_data)
        my_data = 20
        print("function a, my_data =  ", my_data)

    my_data = 10

    print("global scope, my_data =", my_data)
    a(my_data)
    print("global scope, my_data =", my_data)

Example 14
^^^^^^^^^^

We will talk more about these next two examples when we talk about "lists" and "classes" later. These examples don't
operate like you might expect at first. Take a look and see what is different. We'll explain why it works differently
later.

.. code-block:: python

    # Example 14
    def a(my_list):
        print("function a, list =  ", my_list)
        my_list = [10, 20, 30]
        print("function a, list =  ", my_list)

    my_list = [5, 2, 4]

    print("global scope, list =", my_list)
    a(my_list)
    print("global scope, list =", my_list)

Example 15
^^^^^^^^^^

.. code-block:: python

    # Example 15
    # New concept!
    # Covered in more detail in a later chapter
    def a(my_list):
        print("function a, list =  ", my_list)
        my_list[0] = 1000
        print("function a, list =  ", my_list)

    my_list = [5, 2, 4]

    print("global scope, list =", my_list)
    a(my_list)
    print("global scope, list =", my_list)

.. _custom-drawing-function:

How to Create a Custom Drawing Function
---------------------------------------

Here is a set of examples where we take a program that already exists and put
everything in functions.

First the original program:

.. image:: snowman1.png
    :width: 50%

.. literalinclude:: drawing_with_functions_a1.py
    :language: python
    :linenos:

.. _make_the_main_function:

Make The Main Function
^^^^^^^^^^^^^^^^^^^^^^

Next, create a ``main()`` function. Put everything in it, and call the main
function.

.. literalinclude:: drawing_with_functions_a2.py
    :language: python
    :linenos:

When you do this, run your program and make sure it still works before proceeding.

.. _make_the_drawing_function:

Make The Drawing Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, pick an item to move to a function. Start with an easy one if you have it.
I chose grass because it was only one line of code, and I wasn't going to ever try
to position it with x, y.

.. literalinclude:: drawing_with_functions_a3.py
    :language: python
    :linenos:
    :emphasize-lines: 7-9, 17

Then, I took a more complex shape and put it in a function.

.. literalinclude:: drawing_with_functions_a4.py
    :language: python
    :linenos:
    :emphasize-lines: 12-22, 31

But this draws the snowman only at one spot. I want to draw lots of snowmen,
anywhere I put them!

To do this, let's add an x and y:

.. image:: snowman2.png
    :width: 50%

.. literalinclude:: drawing_with_functions_a5.py
    :language: python
    :linenos:
    :emphasize-lines: 12, 19-21, 24-25, 34

But that's not perfect. If you'll note, I added a dot at the x and y. The
snowman draws way off from the dot, because originally I didn't try to draw
it at 0, 0. I need to recenter the snowman on the dot.

We need to re-center the shape onto the spot we are drawing. Typically you'll
need to subtract from all the x and y values the same amount.

.. image:: snowman3.png
    :width: 50%

.. literalinclude:: drawing_with_functions_a6.py
    :language: python
    :linenos:


.. _animate-drawing:

How To Animate A Drawing Function
---------------------------------

We can animate our drawing if we want. Here are the steps.

Create An ``on_draw`` Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Right now our program only draws our image once. We need to move all the drawing code
in our ``main`` to an ``on_draw`` function. Then we'll tell the computer to draw
that over and over.

Continuing from our last example, our program will look like:

.. literalinclude:: animate_1.py
    :language: python
    :linenos:
    :emphasize-lines: 28-34, 41-42

Do this with your own program. Nothing will move, but it should still run.

Add Variable To Control Where We Draw Our Item
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, we are going to create a variable inside of the ``on_draw`` function.
This variable will hold our *x* value.
Each time we call ``on_draw``, we'll change *x* so that it moves to the right.

.. literalinclude:: animate_2.py
    :language: python
    :linenos:
    :emphasize-lines: 33, 36-42

For more information, see the `Bouncing Rectangle Example`_.

.. _Bouncing Rectangle Example: http://arcade.academy/examples/bouncing_rectangle.html