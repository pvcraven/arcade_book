.. sectnum::

Understanding and setting up your system
========================================

Before you begin, you need to install a few things on the computer.
Using a school computer? You may have these already installed. Yay!
Regardless, you still need to understand how the computer
is set up. Why? When something goes wrong, you'll be stuck without
that understanding. Frustrating. Let's avoid that.

You will need:

* The Python programming language
* The Arcade code library
* An editor to type in your programs
* A version control system to track and turn in your work

The Python programming language
-------------------------------

We will be using the "Python" computer programming language. What is a
programming language? We could skip that explanation, and get to the fun
part, but this wouldn't be much of a programming course if you left without
even knowing what a programming language was. So let's get that out of the way.

What is a programming language?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Computers have a Central Processing Unit (CPU) that are the main "brains" of the
computer.

The CPU gets its instructions by reading a set of numbers. For example
the number "04" might be an instruction to add two other numbers together.

In fact, everything stored on the computer is in the form of numbers.
Some numbers computers store are for data (text, photos, movies),
and some are computer instructions.

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
looks like this sample I got from Wikipedia:

.. image:: Motorola_6800_Assembly_Language.png
    :width: 400px
    :alt: Source: https://en.wikipedia.org/wiki/File:Motorola_6800_Assembly_Language.png

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

**Third Generation Languages** (3GL) started with Grace Hopper creating the
language COBOL. There are many, many different third generation languages now.
These languages often specialize at certain tasks. For example, the language
"C" is great at creating small, fast programs that can run on minimal hardware.
"PHP" is an easy-to-use language that can build websites.

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

Python is a great language to s

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
