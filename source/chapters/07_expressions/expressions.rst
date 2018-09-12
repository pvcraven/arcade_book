Variables and Expressions
=========================

We've learned how to call functions to draw shapes like circles,
but what if we could expand that?
What if we could create our own instructions for drawing trees, houses,
spaceships, and rainbows?
What if our program could look like:

.. code-block:: python

    draw_tree(225, 35)
    draw_tree(420, 45)
    draw_house(720, 60)
    draw_snow_person(300, 20)

For this level of computer-programming power,
we need to learn three things:

* How to use variables (this chapter)
* How to write expressions (this chapter)
* How to create out own functions (next two chapters)

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
    * ``temperature_in_celsius``
    * ``tree_position``
    * ``car_speed``
    * ``number_of_children``
    * ``simpson``

Legal, but bad variable names:
    * ``temperatueInCelsius`` - Uses capital letters. Keep it lower case and use underscores.
    * ``x`` - Too short, and not descriptive.
    * ``Simpson`` - Starts with a capital letter.

Variable names that won't work:
    * ``tree position`` - Can't use spaces
    * ``4runner`` - Can't start with a number

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
    x -= 5
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