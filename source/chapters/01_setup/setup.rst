.. sectnum::

Understanding and Setting Up Your System
========================================

Before you begin, you need to install a few things on the computer.
Using a school computer? You may have these already installed. Yay!
Still, read through this part. Make sure you know how the computer
is setup up.

When something goes wrong, you need to understand how your system is set up.
Avoid frustration later. Learn it now.

Your development computer will need:

* The Python_ programming language
* The Arcade_ code library
* An editor to type in your programs (IntelliJ_)
* A version control system to track and turn in your work (Git/SourceTree_/GitHub_)

.. _Python: https://www.python.org/
.. _Arcade: http://arcade.academy/
.. _IntelliJ: https://www.jetbrains.com/idea/
.. _SourceTree: https://www.sourcetreeapp.com/
.. _GitHub: https://github.com/

The Python programming language
-------------------------------

.. image:: python-logo.svg
    :width: 300px

We will be using the "Python_" computer programming language.
The creator of Python was a fan of `Monty Python`_, hence the name.

.. _Monty Python: https://en.wikipedia.org/wiki/Monty_Python

What is a
programming language? We could skip that explanation, and get to the fun
part, but this wouldn't be much of a programming course if you left without
even knowing what a programming language was. So let's get that out of the way.

What is a programming language?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Computers have a Central Processing Unit (CPU_) that are the main "brains" of the
computer. For example, you might have an Intel i7 or an AMD-FX in your computer.

The CPU gets its instructions by reading a set of numbers. For example
the number "04" might be an instruction to add two other numbers together.

Everything stored on the computer is in the form of numbers.
Some numbers computers store are for data (text, photos, movies),
and some are computer instructions.

.. _CPU: https://en.wikipedia.org/wiki/Central_processing_unit

Machine Code
^^^^^^^^^^^^

In the early days of computing, this is how people coded programs. Just punch
in numbers that represent computer instructions.

We call these numbers that are instructions **machine code**. Note that not
all numbers on the computer are machine code (might just be data),
but all machine code is made of numbers.
Machine code is also called a **First Generation Language** (1GL).

Computers still
run on machine code. You can still code this way if you want, although you'd
be crazy because hand-coding these numbers is tedious. There's something better:

Assembly Language
^^^^^^^^^^^^^^^^^

In order to make things
easier, computer scientists came up with something called **assembly language**.
Assembly language is a **Second Generation Language** (2GL). Assembly language
looks like this:

.. figure:: Motorola_6800_Assembly_Language.png
    :width: 400px

    Source: `Wikipedia <https://en.wikipedia.org/wiki/File:Motorola_6800_Assembly_Language.png>`_

Don't worry! We aren't coding in assembly language for this class.

Assembly language allows a programmer to edit a file and type in codes like
``LDA`` which
stands for "Load Accumulator Immediate." The programmer types these commands
into a **source file**. We call the commands **source code**. The computer
can't run the source code as-is. The programmer runs a **compiler** that
simply translates the computer commands like ``LDA`` into the number of the
machine language instruction.

Once I compile the code, I can run the compiled code. I can give the compiled
code to someone else and they can run it. They do not need the source code
or the compiler.

Assembly language is an improvement over machine language.
But it isn't *that* much of an improvement.
Why? Assembly language instructions are very low-level. There are no commands like
"draw a building here." There are commands that move bits from one spot
to another, add them, and shift them.

Third Generation Languages
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: Grace_Hopper_and_UNIVAC.jpg
    :width: 400px

    Source:
    `Wikipedia <https://en.wikipedia.org/wiki/Grace_Hopper#/media/File:Grace_Hopper_and_UNIVAC.jpg>`_

**Third Generation Languages** (3GL) started with `Grace Hopper`_ creating the
language COBOL. There are many, many different third generation languages now.
These languages often specialize at certain tasks. For example, the language
"C" is great at creating small, fast programs that can run on minimal hardware.
"PHP" is an easy-to-use language that can build websites.

.. _Grace Hopper: https://en.wikipedia.org/wiki/Grace_Hopper

Third generation languages usually fall into one of three categories.

* **Compiled:** The computer takes the original source code, and uses a
  *compiler* to translate it to machine code. The user then run the machine
  code. The original source code is not needed to run the program. "C" is an
  example of a language that works this way. So is the 2GL assembly language
  we just talked about.
* **Interpreted:** The computer looks at the source code and immediately
  translates it to machine code. The compile step is not needed, but the user
  needs both the source code and an interpreter to run the program. Python
  is an example of an interpreted language.
* **Runtime Environment:** Languages such as Java and C# take source code, and
  compile the source code to a machine language. But not the language of your
  actual machine, they compile to a *virtual* machine. This is a separate program
  that acts as a layer between the real machine and the compiled code. This
  allows for better security, portability, and memory management.

Working with a compiled language is like taking a book in Spanish and translating
it to English. You no longer need the Spanish book, and you don't need the
translator. However, if you want to edit or change the book you have to
re-translate everything.

Working with an interpreted language is like working with a interpreter. You can
communicate back and forth with a person that knows both English and Spanish.
You need the original Spanish, the English, and the interpreter. It is easier
to make ad-hoc changes and carry out a dialog. Interpreters often help prevent
computers from running commands that will cause major crashes or common security
issues. Kind of like having a human interpreter that says, "You don't *really*
want to say that."

Using a runtime environment is hard to explain in human terms. It is a hybrid
of the two system. You need source code. You need a compiler. Instead of the compiler
making machine code, it makes for for a **virtual machine**.

What is so great about Python?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python is a great language to start programming in.
Python is a Top-5 language in popularity according to the
`TIOBE Index <http://www.tiobe.com/tiobe-index/>`_.
While may be less popular
than Java, it is easier to read and learn. Less work is required to
do graphics. And everything you learn in Python you can also apply when you
learn `C#`_ or Java_.

.. _Java: https://en.wikipedia.org/wiki/Java_(programming_language)
.. _TIOBE Index: http://www.tiobe.com/tiobe-index/
.. _C#: https://en.wikipedia.org/wiki/C_Sharp_(programming_language)

Python a great language for people interested in doing data processing
and `automating boring things <https://automatetheboringstuff.com/>`_.

Python 2.7 vs. Python 3.6
^^^^^^^^^^^^^^^^^^^^^^^^^

There are two main versions of Python. When Python moved to version 3,
there were changes that didn't work with all the currently written Python 2
programs. So both Python 2 and Python 3 were being developed simultaneously.
Some people don't want to move to Python 3 at all.

We use Python 3. Why are you going to care?

* If you search up examples you will find both Python 2 and Python 3 examples.
* Systems such as the Mac and Linux have Python 2 installed by default.

If you see a Python example on the web that has a print statement that looks
like::

  print "Hi"

Instead of::

  print("Hi")

Then you have a Python 2 example and it won't run with what we install and use
in this class.

In the case of the Mac and Linux, it will be important to use Python 3 and
not Python 2.

Setup
-----

You can use a Windows computer, a Mac, or even a Linux computer for this course.
Installation instructions are available below:

* `Windows Installation <http://arcade.academy/installation_windows.html>`_
* `Mac Installation <http://arcade.academy/installation_mac.html>`_
* `Linux Installation <http://arcade.academy/installation_linux.html>`_

We also need an editor. We will use PyCharm_. You'll need a license to use
PyCharm. They are free for educational use. See your instructor for how to
get a PyCharm license. It can be used on a school computer, or on your own
computer.

.. _PyCharm: https://www.jetbrains.com/pycharm/

Version control
---------------

We will be using version control to manage your assignments. See the two
links below.

* `What is version control? <http://web-development-class.readthedocs.io/en/latest/theory/dvcs/dvcs.html>`_
* `Version control tutorial <http://web-development-class.readthedocs.io/en/latest/tutorials/dvcs/dvcs.html>`_

When going through the tutorial:

* For your "project name" use "CMSC_150".
* There won't be teams in this for this class, so each person needs to set up a repository.

First Program
-------------

