.. sectnum::
    :start: 4

Quiz Games and If Statements
============================

How do we tell if a player has beat the high score? How can we tell if he has
run out of lives? How can we tell if she has the key required to open the
locked door?


What we need is the ``if`` statement. The ``if`` statement is also known as a
*conditional statement*. (You can use the term "conditional statement" when you
want to impress everyone how smart you are.) The if statement allows a computer
to make a decision. Is it hot outside? Has the spaceship reached the edge of the
screen? Has too much money been withdrawn from the account? A program can test
for these conditions with the ``if`` statement.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/CBjtrmz7cXo" frameborder="0" allowfullscreen></iframe>

Basic Comparisons
-----------------

Here are a few examples of ``if`` statements. The first section sets up two
variables (a and b) for use in the ``if`` statements. Then two ``if`` statements
show how to compare the variables to see if one is greater than the other.

.. code-block:: python
    :linenos:
    :caption: Example ``if`` statements: less than, greater than

    # Variables used in the example ``if`` statements
    a = 4
    b = 5

    # Basic comparisons
    if a < b:
        print("a is less than b")

    if a > b:
        print("a is greater than b")

    print("Done")

.. code-block:: text
    :caption: Output

    a is less than b
    Done

Since ``a`` is less than ``b``, the first statement will print out if this code
is run. If the variables ``a`` and ``b`` were both equal to 4, then neither of
the two ``if`` statements above would print anything out. The number 4 is not
greater than 4, so the ``if`` statement would fail.

To show the flow of a program a *flowchart* may be used. Most people can follow a
flowchart even without an introduction to programming. See how well you can
understand the figure below.

.. figure:: flowchart1.png
    :width: 300px

    Flowchart

This book skips an in-depth look at flowcharting because it is boring. But if you
want to be a superstar programmer, please read more about it at:

http://en.wikipedia.org/wiki/Flowchart

The prior example checked for greater than or less than. Numbers that were equal
would not pass the test. To check for a values greater than or equal, the
following examples show how to do this:

.. code-block:: python
    :linenos:
    :caption: Example ``if`` statements: less than or equal, greater than or equal

    if a <= b:
        print("a is less than or equal to b")

    if a >= b:
        print("a is greater than or equal to b")

The ``<=`` and ``>=`` symbols must be used in order, and there may not be a
space between them. For example, ``=<`` will not work, nor will ``< =``.

When writing these statements out on a test, some students like to use the ``≤``
symbol. For example:

.. code-block:: text

    if a ≤ b:

This ``≤`` symbol doesn't actually work in a program. Plus most people don't
know how to easily type it on the keyboard. (Just in case you are curious,
to type it hold down the 'alt' key while typing 243 on the number pad.) So when
writing out code, remember that it is ``<=`` and not ``≤``. Many people lose
points on tests for this reason; don't be that person.

The next set of code checks to see if two items are equal or not. The operator
for equal is ``==`` and the operator for not equal is ``!=``. Here they are in
action.

.. code-block:: python
    :linenos:
    :caption: Example ``if`` statements: equal not equal

    # Equal
    if a == b:
        print("a is equal to b")

    # Not equal
    if a != b:
        print("a and b are not equal")

.. attention:: Learn when to use = and ==.

It is very easy to mix up when to use ``==`` and ``=``. Use ``==`` if you
are asking if they are equal, use ``=`` if you are assigning a value.

The two most common mistakes in mixing the ``=`` and ``==`` operators are
demonstrated below:

.. code-block:: python
    :linenos:

    # This is wrong
    a == 1

    # This is also wrong
    if a = 1:
        print("A is one")

Stop! Please take a moment to go back and carefully study the last two code
examples. Save time later by making sure you understand when to use ``=``
and ``==``. Don't guess.

Indentation
-----------

Indentation matters. Each line under the ``if`` statement that is indented will
only be executed ``if`` the statement is ``True``:

.. code-block:: python
    :linenos:

    if a == 1:
        print("If a is one, this will print.")
        print("So will this.")
        print("And this.")

    print("This will always print because it is not indented.")

Indentation must be the same. This code doesn't work.

.. code-block:: python
    :linenos:

    if a == 1:
      print("Indented two spaces.")
        print("Indented four. This will generate an error.")
       print("The computer will want you to make up your mind.")

Once an ``if`` statement has been finished, it is not possible to re-indent to
go back to it. The test has to be performed again.

.. code-block:: python
    :linenos:

    if a == 1:
        print("If a is one, this will print.")
        print("So will this.")

    print("This will always print because it is not indented.")
        print("This will generate an error. Why it is indented?")

Using And/Or
------------

An ``if`` statement can check multiple conditions by chaining together
comparisons with ``and`` and ``or``. These are also considered to be
*operators* just like ``+`` or ``-`` are.


.. code-block:: python
    :linenos:
    :caption: Example ``if`` statements, using "and" and "or"

    # And
    if a < b and a < c:
        print("a is less than b and c")

    # Non-exclusive or
    if a < b or a < c:
        print("a is less than either b or c (or both)")

.. hint:: Repeat yourself please.

A common mistake is to omit a variable when checking it against multiple
conditions. The code below does not work because the computer does not know
what to check against the variable ``c``. It will not assume to check it
against ``a``.

.. code-block:: python
    :linenos:

    # This is not correct
    if a < b or < c:
        print("a is less than b and c")

Boolean Variables
-----------------

Python supports Boolean variables. What are Boolean variables? Boolean variables
can store either a ``True`` or a value of ``False``. `Boolean algebra`_ was
developed by `George Boole`_ back in 1854. If only he knew how important his work
would become as the basis for modern computer logic!

.. _Boolean algebra: https://en.wikipedia.org/wiki/Boolean_algebra
.. _George Boole: https://en.wikipedia.org/wiki/George_Boole

An ``if`` statement needs an expression to evaluate to ``True`` or ``False``. What
may seem odd is that it does not actually need to do any comparisons if a
variable already evaluates to ``True`` or ``False``.

.. code-block:: python
    :linenos:
    :caption: If statements and Boolean data types

    # Boolean data type. This is legal!
    a = True
    if a:
        print("a is true")

Back when I was in school it was popular to say some false statement. Wait three
seconds, then shout "NOT!" Well, even your computer thinks that is lame. If you
are going to do that, you have to start with the not operator. The following code
uses the not to flip the value of a between true and false.

Because not is an operator and not a function, parentheses aren't
necessary.

.. code-block:: python
    :linenos:
    :caption: The not operator example 2

    # How to use the not function
    if not a:
        print("a is false")

It is also possible to use Boolean variables with and and or operators.

.. code-block:: python
    :linenos:
    :caption: Using "and" with Boolean variables

    a = True
    b = False

    if a and b:
        print("a and b are both true")

.. attention:: Who knew True/False could be hard?

It is also possible to assign a variable to the result of a comparison. In the
code below, the variables ``a`` and ``b`` are compared. If they are equal, ``c``
will be ``True``, otherwise ``c`` will be ``False``.

.. code-block:: python
    :linenos:
    :caption: Assigning values to Boolean data types

    a = 3
    b = 3

    # This next line is strange-looking, but legal.
    # c will be true or false, depending if
    # a and b are equal.
    c = a == b

    # Prints value of c, in this case True
    print(c)

.. hint:: Zero means False. Everything else is True.

It is possible to create an ``if`` statement with a condition that does not
evaluate to ``True`` or ``False``. This is not usually desired, but it is
important to understand how the computer handles these values when searching for
problems. The statement below is legal and will cause the text to be printed out
because the values in the ``if`` statement are non-zero:

.. code-block:: python
    :linenos:

    if 1:
        print("1")
    if "A":
        print("A")

The code below will not print out anything because the value in the ``if``
statement is zero which is treated as ``False``. Any value other than zero is
considered ``True``.

.. code-block:: python
    :linenos:

    if 0:
        print("Zero")

In the code below, the first ``if`` statement appears to work. The problem is
that it will always trigger as true even ``if`` the variable ``a`` is not equal
to ``b``. This is because ``b`` by itself is considered ``True``.

.. code-block:: python
    :linenos:

    a = "c"
    if a == "B" or "b":
        print("a is equal to b. Maybe.")

    # This is a better way to do the if statement.
    if a == "B" or a == "b":
        print("a is equal to b.")

Else and Else If
----------------

Below is code that will get the temperature from the user and print if it is hot.

.. code-block:: python
    :linenos:

    temperature = int(input("What is the temperature in Fahrenheit? "))
    if temperature > 90:
        print("It is hot outside")
    print("Done")

If the programmer wants code to be executed if it is not hot, she can use the
else statement. Notice how the else is lined up with the ``i`` in the ``if``
statement, and how it is followed by a colon just like the ``if`` statement.

In the case of an if...else statement, one block of code will always be
executed. The first block will be executed ``if`` the statement evaluates to
``True``, the second block if it evaluates to False.

.. code-block:: python
    :linenos:
    :caption: Example if/else statement

    temperature = int(input("What is the temperature in Fahrenheit? "))
    if temperature > 90:
        print("It is hot outside")
    else:
        print("It is not hot outside")
    print("Done")

It is possible to chain several ``if`` statements together using the else...if
statement. Python abbreviates this as ``elif``.

.. code-block:: python
    :linenos:
    :caption: Example if/elif/else statement

    temperature = int(input("What is the temperature in Fahrenheit? "))
    if temperature > 90:
        print("It is hot outside")
    elif temperature < 30:
        print("It is cold outside")
    else:
        print("It is not hot outside")
    print("Done")

In the code below, the program will output "It is hot outside" even if the user
types in 120 degrees. Why? How can the code be fixed?

If you can't figure it out, see the video.

.. code-block:: python
    :linenos:
    :caption: Example of improper ordering if/elif/else

    temperature = int(input("What is the temperature in Fahrenheit? "))
    if temperature > 90:
        print("It is hot outside")
    elif temperature > 110:
        print("Oh man, you could fry eggs on the pavement!")
    elif temperature < 30:
        print("It is cold outside")
    else:
        print("It is ok outside")
    print("Done")

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/uLJ7wxeaBbE" frameborder="0" allowfullscreen></iframe>

.. _text-comparisons:

Text Comparisons
----------------

It is possible to use an if statement to check text.

.. code-block:: python
    :linenos:
    :caption: Case sensitive text comparison

    user_name = input("What is your name? ")
    if user_name == "Paul":
        print("You have a nice name.")
    else:
        print("Your name is ok.")

The prior example will only match if the user enters "Paul". It will not work if the user enters "paul" or "PAUL".

A common mistake is to forget the quotes around the string being compared. In the example below, the computer will think that Paul is a variable that stores a value. It will flag an error because it has no idea what is stored in the variable Paul.

.. code-block:: python
    :linenos:
    :caption: Incorrect comparison

    user_name = input("What is your name? ")
    if user_name == Paul: # This does not work because quotes are missing
        print("You have a nice name.")
    else:
        print("Your name is ok.")

.. _multi-text-comparisons:

Multiple Text Possibilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When comparing a variable to multiple possible strings of text, it is important
to remember that the comparison must include the variable. For example:

.. code-block:: python
    :linenos:

    # This does not work! It will always be true
    if user_name == "Paul" or "Mary":
    Instead, the code should read:

    # This does work
    if user_name == "Paul" or user_name == "Mary":

This is because any value other than zero, the computer assumes to mean
``True``. So to the computer "Mary" is the same thing as ``True`` and so it
will run the code in the ``if`` statement.

Case Insensitive Comparisons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the program needs to match regardless as to the case of the text entered, the easiest way to do that is to convert everything to lower case. This can be done with the lower command.

.. attention:: Learn to be insensitive.

The example below will take whatever the user enters, convert it to lower case, and then do the comparison. Important: Don't compare it against a string that has uppercase. If the user input is converted to lowercase, then compared against uppercase letters, there is no way a match can occur.

.. code-block:: python
    :linenos:
    :caption: Case-insensitive text comparison

    user_name = input("What is your name? ")
    if user_name.lower() == "paul":
        print("You have a nice name.")
    else:
        print("Your name is ok.")

Example if Statements
---------------------

The next set of example code below runs through all the concepts talked about
earlier. The on-line video traces through each line of code and explains how it
works

In the video I use an integrated development editor (IDE) called Eclipse. The
default version of Eclipse doesn't work with Python, but the PyDev version does.
The PyDev editor is available for free from:

http://pydev.org/

The editor is complex, but it has many options and can be a powerful environment
to work in. Some programmers like using environments such as PyDev that can have
so many plug-ins that will do everything but bring you coffee. Some developers
prefer a minimalistic environment that doesn't "get in the way."

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/pDpNSck2aXQ" frameborder="0" allowfullscreen></iframe>

.. literalinclude:: if_statement_examples.py
    :language: python
    :linenos:
