.. sectnum::

Understanding and setting up your system
========================================

Before you begin, you need to install a few things on the computer that you
are working on. If you are using a school computer, you may have these already
installed, but you still need to understand what has been installed.

You need:

* The Python language
* The Arcade library
* An editor to type in your programs


What is a programming language?
-------------------------------

Computers have a Central Processing Unit (CPU) that are the main "brains" of the
computer.

The CPU gets its instructions by reading a set of numbers. For example
the number "04" might be an instruction to add two other numbers together.
So some numbers were data, and some were computer instructions.

In the early days of computing, this is how people coded programs.

Machine Code
^^^^^^^^^^^^

We call these numbers that are instructions **machine code**. Note that not
all numbers are machine code, but machine code is made of numbers.
Machine code is also called a **First Generation Language** (1GL).

Computers still
run on machine code. You can still code this way if you want, although you'd
be crazy because hand-coding these numbers is tedious.

Assembly Language
^^^^^^^^^^^^^^^^^

In order to make things
easier, computer scientists came up with something called **assembly language**.
Assembly language is a **second generation language** (2GL).

.. image:: Motorola_6800_Assembly_Language.png
    :width: 400px

# https://en.wikipedia.org/wiki/File:Motorola_6800_Assembly_Language.png

Assembly language allows a programmer to edit a file and type in ``LDA`` which
stands for "Load Accumulator Immediate." The programmer types these commands
into a **source file**. We call the commands **source code**. The computer
can't run the source code as-is. The programmer runs a **compiler** that
simply translates the computer commands like ``LDA`` into the number of the
machine language instruction.

Once I compile the code, I can run the compiled code. I can give the compiled
code to someone else,

Assembly language is an improvement. But it isn't *that* much of an improvement.
Why? Assembly language instructions are very low-level. There are no commands like
"draw a building here." There are commands that move bits from one spot
to another, add them, and shift them.

Third Generation Languages
^^^^^^^^^^^^^^^^^^^^^^^^^^

Third Generation Languages (3GL) started with Grace Hopper creating the
language COBOL. There are many, many different third generation languages now.
These languages often specialize at certain tasks. For example, the language
"C" is great at creating small, fast programs that can run on minimal hardware.
"PHP" is an easy-to-use language that can build websites.

What is so great about Python?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python 2.7 vs. Python 3.5
^^^^^^^^^^^^^^^^^^^^^^^^^

Windows setup
-------------

Install Python
^^^^^^^^^^^^^^

Installing the Arcade library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Linux setup
-----------

Install Python
^^^^^^^^^^^^^^

Installing the Arcade library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mac setup
---------

Install Python
^^^^^^^^^^^^^^

Installing the Arcade library
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the development environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Version control
---------------

First program
-------------
