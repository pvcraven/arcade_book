.. _expressions:

Variables and Expressions
=========================

.. image:: expressions.svg
    :width: 30%
    :class: right-image

We've learned how to import a library and call functions.
The next step is to make our code more flexible.
What if we could take that drawing code we wrote and put it into
our own functions? Then we could just call a function anytime
we wanted a tree, house, or rainbow. Our code could look like this:

.. code-block:: python

    draw_tree(225, 35)
    draw_tree(420, 45)
    draw_house(720, 60)
    draw_snow_person(300, 20)

For this level of computer-programming power,
we need to learn three things:

* How to use variables (this chapter)
* How to write expressions (this chapter)
* How to create our own functions (next two chapters)

How to Use Variables
--------------------

A **variable** is a value the computer stores in memory that can change. That
is, it *varies*. Here is a quick example:

.. code-block:: python

    # What will this print?
    x = 5
    print(x)

What will the code above print? It will print ``5``.

``x`` is a variable. The ``=`` is called an **assignment operator**. It assigns the value on the
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

.. code-block:: text

    print(Have a great day!)

The code above will fail because the computer will think that it should evaluate
``Have a great day!`` as a mathematical expression. It isn't, so the computer
gets confused and generates a syntax error. That's why we need quotes:

.. code-block:: python

    print("Have a great day!")

Variable and Function Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Variable names and function names follow the same rules. There are
names you *should* use, names you *shouldn't* use, and
names you *can't* use.

Variable names *should* be descriptive, all lower case, and if you have
multiple words, separate the words by an underscore.
Variable names *can't* start with a number nor have a space or any symbol
other than an underscore.
Here are some examples:

Good variables:
    * ``temperature_in_celsius``
    * ``tree_position_1``
    * ``tree_position_2``
    * ``car_speed``
    * ``number_of_children``
    * ``simpson``

Bad variable names that still work:
    * ``temperatueInCelsius`` - Uses capital letters. Keep it lower case and use underscores.
    * ``x`` - Too short, and not descriptive.
    * ``Smith`` - Starts with a capital letter.

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

Good variable names help make code *readable*.

For example, what does this code do? It is hard to tell. (Furthermore, if I
have to update the numbers, I'm editing the equation which makes it more likely
I'll accidentally change the function.)

.. code-block:: python

    m = 294 / 10.5
    print(m)

Here we use variables. A bit easier to change the values, and a bit easier to understand.

.. code-block:: python

    m = 294
    g = 10.5
    m2 = m / g
    print(m2)

Instead of using short variable names, if we use use descriptive variable names
and comments the code is *very* easy to understand.

.. code-block:: python

    # Calculate mpg using good variable names
    miles_driven = 294
    gallons_used = 10.5
    mpg = miles_driven / gallons_used
    print(mpg)

Good variable names make code easier to understand, easier to code,
and easier to find errors.

How to Create Expressions
-------------------------

Great! We are part-way there. To manipulate data with a computer, we use
**expressions**. An expression is simply a mathematical equation, although
we aren't limited to numbers.

Using Operators in Expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Expressions use **operators**. That's just a fancy word for symbols like
addition (``+``) and subtraction(``-``).
Here's an example:

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

There are two things that **don't** work like mathematics. First, there is no
"juxtaposition" used to multiply items. Second, the ``=`` is not an algebraic
equality.

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
    # the = is a variable.
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

.. _incrementing_x:

Increasing a Variable
^^^^^^^^^^^^^^^^^^^^^

What if we want to change a value stored in a variable? We need to use
an assignment operator.

For example, take a look at this code. It prints the number ``4`` twice.
First, we assign ``3`` to ``x``.
Then, every time we print we add one to ``x``.
We *aren't* changing the original value of ``x``, so we don't print ``4`` and
then ``5``. The variable ``x`` only holds the number ``3``.

.. code-block:: python

    x = 3
    print(x + 1)
    print(x + 1)

Take a look at this example. This example prints ``3``. It *does* add ``1`` to ``x``.
But it does nothing with the result. We don't print it. Just like the prior example,
the number in ``x`` doesn't change.

.. code-block:: python

    x = 3
    x + 1
    print(x)

Now look at this example. We use the assignment operator. We store into ``x`` the result
of ``x + 1``. This *does* increase the value stored in ``x`` and therefore we print out
a ``4``.

.. code-block:: python

    x = 3
    x = x + 1
    print(x)

.. note::

   It can be confusing to learn when to use ``x + 1`` and when to use ``x = x + 1``. Remember,
   the former does *not* change the value of ``x``.

Increment/Decrement Operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``=`` symbol isn't the only assignment operator.
Here are the other assignment operators:

========== =====================================
Operator   Description
========== =====================================
``=``      Assignment
``+=``     Increment
``-=``     Decrement
``*=``     Multiply
``/=``     Divide
========== =====================================

Because statements like ``x = x + 1`` are so common, we can shorten this
using the ``+=`` assignment operator. Examine this code to see how it
works:

.. code-block:: python

    # This works, and prints "3"
    x = 3
    print(x)

    # Make x bigger by one using the regular
    # assignment operator.
    x = x + 1
    print(x)

    # Make x bigger by one, using the +=
    # assignment operator.
    x += 1
    print(x)

    # Make x smaller by five using the -=
    # operator.
    x -= 5
    print(x)


Remember, if you want to increase or decrease a variable, you need to use an assignment operator.

Oh, and a common mistake is to mix the ``+`` and ``+=`` operator.

.. code-block:: python

    # This doubles x, and then adds one.
    # Probably not what the programmer intended.
    x += x + 1



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

Printing Variables
------------------

How can you print variables and text together? Say you've got a variable ``result`` and
you want to nicely print it. Based on what we learned so far, you can do this:

.. code-block:: python

    answer = "bananas"
    print(answer)

But that just prints out ``bananas`` on a line by itself. Not very descriptive. What
if we wanted:

.. code-block:: text

    The answer is bananas

You can do this with:

.. code-block:: python

    answer = "bananas"
    print("The answer is", answer)

Better. But I want to add punctuation. If we do this:

.. code-block:: python

    answer = "bananas"
    print("The answer is", answer, ".")

We get an extra space before the period:

.. code-block:: text

    The answer is bananas .

The ``,`` adds a space when we use it in a ``print`` statement. We don't
always want that. We can instead use a ``+`` sign:

.. code-block:: python

    answer = "bananas"
    print("The answer is" + answer + ".")

Which gets rid of all the spaces:

.. code-block:: text

    The answer isbananas.

So we need to add a space INSIDE the quotes where we want it:

.. code-block:: python

    answer = "bananas"
    print("The answer is " + answer + ".")

Ok, so I think I know how to print variables. Until I try this:

.. code-block:: python

    answer = 42
    print("The answer is " + answer + ".")

The computer doesn't know how to put text and numbers together. If you add two
*numbers*
``20 + 20`` you get ``40``. If you add two *strings* ``"20" + "20"`` you
get ``2020``, but the
computer has no idea what to do with a combo of text and numbers. So the fix
is to use the ``str`` function which converts the number to a string (text):

.. code-block:: python

    answer = 42
    print("The answer is " + str(answer) + ".")

Yes, this is a bit complex. But wait! There's more! Another way to print
variables is to use a *formatted string*. Later we will spend a whole other
chapter on formatted strings, but they look like:

.. code-block:: python

    answer = 42
    print(f"The answer is {answer}.")

Note we start the string with an ``f`` before the quote, and the variable
we want to print goes in curly braces.

Review
------

Review Questions
^^^^^^^^^^^^^^^^

#. What do computer languages use to store changing data?
#. What do we call the ``=`` symbol in Python?
#. When we store text into a variable, what is another name for the text?


