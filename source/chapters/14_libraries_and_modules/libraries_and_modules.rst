.. sectnum::
    :start: 14

Libraries and Modules
=====================

.. image:: library.png
    :width: 400px

A *library* is a collection of code for functions and classes. Often, these
libraries are written by someone else and brought into the project so that
the programmer does not have to "reinvent the wheel." In Python the term used
to describe a library of code is module.

By using ``import pygame`` and ``import random``, the programs created so far have
already used modules. A library can be made up of multiple modules that can be
imported. Often a library only has one module, so these words can sometimes be
used interchangeably.

Modules are often organized into groups of similar functionality. In this class
programs have already used functions from the ``math`` module, the ``random`` module,
and the ``arcade`` library. Modules can be organized so that individual modules
contain other modules. For example, the ``arcade`` module contains submodules for
``arcade.key``, and ``arcade.color``.

Modules are not loaded unless the program asks them to. This saves time and
computer memory. This chapter shows how to create a module, and how to import
and use that module.

Why Create a Library?
---------------------

There are three major reasons for a programmer to create his or her own
libraries:

1. It breaks the code into smaller, easier to use parts.
2. It allows multiple people to work on a program at the same time.
3. The code written can be easily shared with other programmers.

Some of the programs already created in this book have started to get rather
long. By separating a large program into several smaller programs, it is
easier to manage the code. For example, in the prior chapter's sprite example,
a programmer could move the sprite class into a separate file. In a complex
program, each sprite might be contained in its own file.

If multiple programmers work on the same project, it is nearly impossible to
do so if all the code is in one file. However, by breaking the program into
multiple pieces, it becomes easier. One programmer could work on developing
an "Orc" sprite class. Another programmer could work on the "Goblin" sprite
class. Since the sprites are in separate files, the programmers do not run
into conflict.

Modern programmers rarely build programs from scratch. Often programs are
built from parts of other programs that share the same functionality. If
one programmer creates code that can handle a mortgage application form,
that code will ideally go into a library. Then any other program that needs
to manage a mortgage application form at that bank can call on that library.

Creating Your Own Module/Library File
-------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/3zSrkC6c1aU" frameborder="0" allowfullscreen></iframe>

Video: Libraries

In this example we will break apart a short program into multiple files. Here
we have a function in a file named ``test.py``, and a call to that function:

.. code-block:: python
    :linenos:
    :caption: test.py with everything in it

    # Foo function
    def foo():
        print("foo!")

    # Foo call
    foo()

Yes, this program is not too long to be in one file. But if both the function
and the main program code were long, it would be different. If we had several
functions, each 100 lines long, it would be time consuming to manage that
large of a file. But for this example we will keep the code short for clarity.

We can move the ``foo`` function out of this file. Then this file would be left
with only the main program code. (In this example there is no reason to
separate them, aside from learning how to do so.)

To do this, create a new file and copy the ``foo`` function into it. Save the
new file with the name ``my_functions.py``. The file must be saved to the same
directory as ``test.py``.

.. code-block:: python
    :linenos:
    :caption: my_functions.py

    # Foo function
    def foo():
        print("foo!")

.. code-block:: python
    :linenos:
    :caption: test.py that doesn't work

    # Foo call that doesn't work
    foo()

Unfortunately it isn't as simple as this. The file ``test.py`` does not know to
go and look at the ``my_functions.py`` file and import it. We have to add the
command to import it:

.. code-block:: python
    :linenos:
    :caption: test.py that imports but still doesn't work

    # Import the my_functions.py file
    import my_functions

    # Foo call that still doesn't work
    foo()

That still doesn't work. What are we missing? Just like when we import
pygame, we have to put the package name in front of the function. Like this:

.. code-block:: python
    :linenos:
    :caption: test.py that finally works

    # Import the my_functions.py file
    import my_functions

    # Foo call that does work
    my_functions.foo()

This works because ``my_functions.`` is prepended to the function call.

Namespace
---------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/vcYcFX9yqiY" frameborder="0" allowfullscreen></iframe>

Video: Namespace

A program might have two library files that need to be used. What if the
libraries had functions that were named the same? What if there were two
functions named print_report, one that printed grades, and one that printed
an account statement? For instance:

.. code-block:: python
    :linenos:
    :caption: student_functions.py

    def print_report():
        print("Student Grade Report:" )

.. code-block:: python
    :linenos:
    :caption: financial_functions.py

    def print_report():
        print("Financial Report:" )

How do you get a program to specify which function to call? Well, that is
pretty easy. You specify the *namespace*. The namespace is the work that
appears before the function name in the code below:

.. code-block:: python
    :linenos:
    :caption: test.py that calls different print_report functions

    import student_functions
    import financial_functions

    student_functions.print_report()
    financial_functions.print_report()

So now we can see why this might be needed. But what if you don't have name
collisions? Typing in a namespace each and every time can be tiresome. You
can get around this by importing the library into the *local namespace*. The
local namespace is a list of functions, variables, and classes that you
don't have to prepend with a namespace. Going back to the ``foo`` example,
let's remove the original import and replace it with a new type of import:

.. code-block:: python
    :linenos:
    :caption: test.py

    # import foo
    from my_functions import *

    foo()

This works even without ``my_functions.`` prepended to the function call. The
asterisk is a wildcard that will import all functions from ``my_functions``.
A programmer could import individual ones if desired by specifying the
function name.
