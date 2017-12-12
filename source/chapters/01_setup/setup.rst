.. _chapter-setup:

Setting Up Your System
======================

Before you begin, you need to install a few things on the computer.
Using a school computer? You may have these already installed. Yay!
Still, read through this part. Make sure you know how the computer
is setup up.

Getting a system set up and ready to program can be a bit frustrating. **Don't give up.** Once you've got a system
set up for programming you don't need to think about it again. You can concentrate on the programming part.
You may get stuck during the setup, so don't hesitate to reach out and get help.


Your development computer will need:

* The Python_ programming language and the Arcade_ code library.
* An editor to type in your programs. (We'll use a program called PyCharm_.
  You can use the community edition for free, or if you have an email
  address that ends in ``.edu`` get can get a free `student license`_ for
  the professional version.)
* A version control system to track and turn in your work. (Git/SourceTree_/BitBucket_)
* A minor configuration tweak so we can see file extensions.

.. _SourceTree: https://www.sourcetreeapp.com/


Let's go through these four items in detail.

.. _Python: https://www.python.org/
.. _Arcade: http://arcade.academy/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _GitHub: https://github.com/
.. _BitBucket: https://bitbucket.org/

The Python Programming Language
-------------------------------

.. image:: python-logo.svg
    :width: 300px

We will be using the "Python_" computer programming language.
The creator of Python was a fan of `Monty Python`_, hence the name.

.. _Monty Python: https://en.wikipedia.org/wiki/Monty_Python

Setup the Programming Environment
---------------------------------

To get your computer ready for programming, we need to install Python, some Python libraries, and an editor.

.. _installing-python:

Installing Python
^^^^^^^^^^^^^^^^^

In addition to the Python language, we are going to use a library of commands
for drawing on the screen. This is called the "Arcade" library.

Installation for installing Python and the Arcade library are available below:

* `Windows Installation <http://arcade.academy/installation_windows.html>`_
  (Make sure to read the instructions carefully. Do not skip the "Add Python
  to Path" step. This seems to be the most frequent issue.)
* `Mac Installation <http://arcade.academy/installation_mac.html>`_
* `Linux Installation <http://arcade.academy/installation_linux.html>`_

.. _installing-pycharm:

Installing an IDE
^^^^^^^^^^^^^^^^^

We also need an editor. Python comes with an editor called IDLE, but it is
awful and not worth using. We'll use an editor called PyCharm.

PyCharm is a powerful program that lets you do more than just edit the
program, it also includes a large set of tools that programmers need. This
type of environment is called an **Integrated Development Environment**, or **IDE**
for short.

Download and install PyCharm_.
You can use their community edition for free. We won't use the
features in the professional edition. If you decide to
pick the professional edition anyway,
you'll need a license to use it.
But licenses are free for educational use!
If you have an e-mail that ends in ``.edu`` you can
ask for a `student license`_. It can be used on a school computer, or on your own
computer.

What is a text editor? What is an IDE? Read more at
`Understanding and Choosing Text Editors`_.

.. _Understanding and Choosing Text Editors: http://web-development-class.readthedocs.io/en/latest/tutorials/text_editors/text_editors.html
.. _student license: https://www.jetbrains.com/student/

Opening in PyCharm
^^^^^^^^^^^^^^^^^^

1. Open PyCharm.
2. Select File...Open. Then select the directory that you cloned the repository.

Viewing File Extensions
-----------------------
It is a great idea to change your windows configuration to show file extensions.
A file usually has a name like Book ``report.docx`` where the ``.docx`` tells the
computer it is a Microsoft Word compatible document. By default Windows
hides the ``.docx`` extension if there is a program installed to handle it.
If you are programming, this hiding part of the file name can be annoying.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/LukHWurpjAc" frameborder="0" allowfullscreen></iframe>

For Windows 7, to show file extensions,
open up your computer's control panel. Find the selection for "Folder Options.""
Click the "View" tab, and then unselect the option for "Hide extensions for
known file types.""

For Windows 8 and 10, bring up a file explorer by hitting the Windows-E key.
Then click the "view" tab and make sure “File name extensions” has been checked.

Great! Now let's make our first program with.

.. _print-function:

The Print Function
------------------

.. _print-hello-world:

Printing Hello World
^^^^^^^^^^^^^^^^^^^^

We will use a function called ``print`` to print to the screen.
``print`` is called a *function*.

You've already used functions
in mathematics. For example, **sin** and **cos**.
Functions are followed by parentheses: ``( )``.
We put the
function *parameter(s)* inside the parenthesis.

With a sine function, we put in an angle. With
the ``print`` function, we are going to put the text we want to print. Text must be enclosed in quotes.

::

    print("Hello there")

Note that case matters. The following will not work:

::

    Print("Hello there")

Great! Time to run it.
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

Multiple Print Lines
^^^^^^^^^^^^^^^^^^^^

Let's add additional code:

::

	print("It was a dark and stormy night.")
	print("Suddenly a shot rang out!")

Go ahead and run it to make sure it outputs as expected.

.. _escape-codes:

Escape Codes
^^^^^^^^^^^^

If quotes are used to tell the computer the start and end of the string of text you wish to print, how does a program
print out a set of double quotes? For example:

::

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

::

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



