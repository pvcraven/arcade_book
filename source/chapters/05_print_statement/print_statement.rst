.. _print-function:

The ``print`` Function
======================

In this chapter we'll write our first programs using the most fundamental of all
tools in the programmer's toolbox, the ``print`` function. As you can probably guess,
this function prints information to the screen.

While a lot of programs are graphics-based, text-only programs are still quite common
with people that manage computers, or who do data analytics. Even for the graphics-based
games we develop in this book, the ``print`` function will be a vital aid in understanding
and debugging our games.

We aren't limited to printing to the screen! The same techniques we learn here can
be used to print information to a file, so we can save our data. We can even print
over a over a network connection, which is the start of what's needed to learn how
to do web programming.

Prior to starting this chapter we got our computer ready to start coding in
:ref:`chapter-setup`. We did that by installing the Python programming language,
and an integrated development environment (IDE) called PyCharm. You can think
of Python as the engine, and PyCharm as the interface to the engine.

In :ref:`version-control` we began learning `git`, a version control system.
Version control systems allow us to share code, work on code in groups, and
track changes to the code.

.. _print-hello-world:

Printing "Hello World"
----------------------

We are going to use a **function** to output text to the screen.
Functions are a basic building block in any computer program.
If you've taken a geometry class, you've already used the sine (**sin**)
and cosine (**cos**) functions. In programming, we use functions *a lot*.
Just like in math, when we use functions in programming we start with a function
name and it by a pair of parentheses: ``( )``.
We put any function **parameter** inside the parenthesis.

In :ref:`sin-function` example below, we have a function,
parenthesis, and a parameter.

.. code-block:: text
    :caption: Functions in Math
    :name: sin-function

    sin(0)
    ^ Function name, sin
        ^ Parameter, 0

In the :ref:`print-function1` example below, we also have a function,
parenthesis, and a parameter.

.. code-block:: text
    :caption: Python Print Function
    :name: print-function1

    print("Hello there")
    ^ Function name, print
           ^ Parameter, "Hello there"

With a sine function, we put in an angle as our parameter.
With the ``print`` function, we put the text we want to print as a parameter.
Text *must* be enclosed in quotes, we'll explain why later in
the :ref:`expressions` chapter.

Running Our Program
-------------------

Great! Let's enter our program and run it.

Right-click on the program and select "Run 'lab_01.py'"

Before we go on, note how the PyCharm window is put together.
See the output of your program at the bottom of the screen.
Click the image below to make it bigger and note the:

* Right margin. You can write code past this point, but don’t.
* Where you can hover your mouse for "hints" on how to make your code better.
* Where you can quickly click to run your program again.

.. image:: pycharm_window.png

Ok, now it's time to update our program. Go back to our program and improve
it by printing multiple lines, while quoting Snoopy's famous story:

.. _print-multiple-lines:

Case matters when you type in code. The following will not work:

.. code-block:: text

    Print("Hello there")

Multiple Print Lines
--------------------

Let's add additional code:

.. code-block:: python

    print("It was a dark and stormy night.")
    print("Suddenly a shot rang out!")

Go ahead and run it to make sure it outputs as expected.

.. _escape-codes:

Escape Codes
------------

If quotes are used to tell the computer the start and end of the string of text you wish to print, how does a program
print out a set of double quotes? (This is a double quote ``"`` and this is a single quote ``'``.) For example:

.. code-block:: text

    print("I want to print a double quote " for some reason.")

This code doesn't work.
The computer looks at the quote in the middle of the string and thinks that is the end of the text.
Then it has no idea what to do with the commands for some reason and the quote and the end of the string confuses the
computer even further.

It is necessary to tell the computer that we want to treat that middle double quote as text, not as a quote ending the
string. This is easy, just prepend a backslash in front of quotes to tell the computer it is part of a string, not a
character that terminates a string. For example:

.. code-block:: python

    print("I want to print a double quote \" for some reason.")

This combination of the two characters ``\"`` is called an *escape code*. Almost every language has escape codes.
Here's another example:

.. code-block:: python

    print("Audrey Hepburn once said \"Nothing is impossible. The word itself says 'I'm Possible!'.\"")

This will print:

.. code-block:: text

    Audrey Hepburn once said "Nothing is impossible. The word itself says 'I'm Possible!'."

Because the backslash is used as part of an escape code, the backslash itself must be escaped if you want to use
one. For example, this code does not work correctly:

.. code-block:: python

    print("The file is stored in C:\new folder")

Why? Because ``\n`` is an escape code. To print the backslash it is necessary to escape it like so:

.. code-block:: python

    print("The file is stored in C:\\new folder")

There are a few other important escape codes to know. Here is a table of the important escape codes:

=========== =======================================
Escape code	Description
=========== =======================================
``\'``      Single Quote
``\"``	    Double Quote
``\t``	    Tab
``\r``	    CR: Carriage Return (move to the left)
``\n``	    LF: Linefeed (move down)
=========== =======================================

What is a "Carriage Return" and a "Linefeed"? Try this example:

.. code-block:: python

    print("This\nis\nmy\nsample.")

The output from this command is:

.. code-block:: text

    This
    is
    my
    sample.

The ``\n`` is a linefeed. It moves "cursor" where the computer will print text down one line. The computer stores all
text in one big long line. It knows to display the text on different lines because of the placement of ``\n`` characters.

To make matters more complex, different operating systems have different standards on what makes a line ending.

=========== =======================================
Escape code	Description
=========== =======================================
``\r\n``    CR+LF: Microsoft Windows
``\n``      LF: UNIX based systems, and newer Macs.
``\r``      CR: Older Mac based systems
=========== =======================================


Ok, now it is time to make this lab yours. Write program that consists of
several print statements. Here is my example:

.. code-block:: python

	print("You can print a statement surrounded by double quotes.")
	print('You can print a statement surrounded by single quotes.')

	print("If you want to print a double quote, you can by prepending it with")
	print("a slash. \"That's great!\" he said.")

	print("If you want to print a backslash, you can by prepending it with")
	print("a slash. So this \\ prints one backslash, and this \\\\ does two.")

	print("You can print a blank line with a empty print statement.")
	print()

	print("You can use a backlash n to print a new line. These\nare\non\nnew\nlines.")
	print("""You can print
	on multiple
	lines using
	triple
	quotes. Just in
	case you wanted to.""")

What We Learned
---------------

* function
* parameter

On-Line Practice
----------------

Where this is used
------------------

Possible Errors
---------------