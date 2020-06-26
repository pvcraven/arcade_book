Advanced Looping
================


.. image:: nested_loops.png
    :width: 200px
    :class: right-image

Games involve a lot of complex loops. This is a "challenge chapter" to learn
how to be an expert with loops. If you can understand the problems in this
chapter, by the end of it you can certify yourself as a loop expert.

At the very least, make sure you can
write out the answers for the first eight problems. That will give you enough
knowledge to continue this book.

You can try solving these on your computer, or on-line with
`repl.it <https://repl.it/community/classrooms/174286>`_.
Scroll down to the "05" set of problems.

Print Statements and Line Endings
---------------------------------

By default, the ``print`` statement puts a *carriage return* at
the end of what is printed out. As we explained back in the first chapter,
the carriage return is a character that moves the next line of
output to be printed to the next line. Most of the time this is what we want.
Sometimes it isn't. If we want to continue printing on the same line, we can change
the default character printed at the end.
This is an example before we change the ending character:

.. code:: python

    print("Pink")
    print("Octopus")


...which will print out:

.. code:: text

    Pink
    Octopus


But if we wanted the code output to print on the same line,
it can be done by using a new option to set the "end" character.
For example:

.. code:: python

    print("Pink", end="")
    print("Octopus")

This will print:

.. code:: text

    PinkOctopus

We can also use a space instead of setting it to an empty string:

.. code:: python

    print("Pink", end=" ")
    print("Octopus")


This will print:

.. code:: text

    Pink Octopus


Here's another example, using a variable:

.. code:: python

    i = 0
    print(i, end=" ")
    i = 1
    print(i, end=" ")


This will print:

.. code:: text

    0 1

.. _move_to_the_next_line:

Moving to the Next Line
~~~~~~~~~~~~~~~~~~~~~~~

If you can get text to appear on the same line, how do you trigger text
to appear on the next line? An empty ``print`` statement will do the trick:

.. code:: python

    print()


The trick is to combine this statement with the ``for`` loops in the proper
location, and the proper indentation.

Advanced Looping Problems
-------------------------

Problem 1
~~~~~~~~~

Write code that will print ten asterisks (*) in a row:

.. code:: text

    * * * * * * * * * *

Write code to print the asterisks using a ``for`` loop. Print each
asterisk individually, don't just print all ten with one "print" statement.
This problem can be completed in two lines of code using one ``for`` loop and
one ``print`` statement.

Remember, **don't** look at the answer until you've figured it out yourself,
or you have been trying for 5-10 minutes. (I don't recommend waiting longer than
ten minutes.)

:ref:`answer-problem-01`

Problem 2
~~~~~~~~~

Write code that will print the following:

.. code:: text

    * * * * * * * * * *
    * * * * *
    * * * * * * * * * * * * * * * * * * * *

This is just like the prior problem, but also printing five and twenty stars. Copy and paste
from the prior problem, adjusting the ``for`` loop as needed.
Don't forget how :ref:`move_to_the_next_line`.

:ref:`answer-problem-02`

Problem 3
~~~~~~~~~

Use two "for" loops, one of them nested inside the other,
to print the following 10x10 rectangle:

.. code:: text

    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *


To start, take a look at Problem 1. The code in Problem 1 generates one line of asterisks.
It needs to be repeated ten times. You'll also need to move to the next line
after each row has printed.
Work on this problem for at least ten minutes before looking at the answer.

:ref:`answer-problem-03`

Problem 4
~~~~~~~~~

Use two "for" loops, one of them nested, to print the following 5x10
rectangle:

.. code:: text

    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *

This is a lot like the prior problem. Experiment with the ranges on the loops to find exactly what
the numbers passed to the ``range`` function control.

:ref:`answer-problem-04`

Problem 5
~~~~~~~~~

Use two ``for`` loops, one of them nested, to print the following 20x5
rectangle:

.. code:: text

    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *

Again, like Problem 3 and Problem 4, but with different range values.

:ref:`answer-problem-05`

Problem 6
~~~~~~~~~

Write code that will print the following:

.. code:: text

    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8 9

Use two nested loops. Print the first line with a loop. Don't use code like this:

.. code:: python

    print("0 1 2 3 4 5 6 7 8 9")

.. attention::

    First, create a loop that prints the first line. Then enclose it in another
    loop that repeats the line 10 times.
    Use either ``i`` or ``j`` variables for what the program prints.
    This example and the next one helps reinforce what those index
    variables are doing.

Work on this problem for at least ten minutes before looking at the answer.
The process of spending ten minutes working on the answer is far more important
than the answer itself.

:ref:`answer-problem-06`

Problem 7
~~~~~~~~~

Adjust the prior program to print:

.. code:: text

    0 0 0 0 0 0 0 0 0 0
    1 1 1 1 1 1 1 1 1 1
    2 2 2 2 2 2 2 2 2 2
    3 3 3 3 3 3 3 3 3 3
    4 4 4 4 4 4 4 4 4 4
    5 5 5 5 5 5 5 5 5 5
    6 6 6 6 6 6 6 6 6 6
    7 7 7 7 7 7 7 7 7 7
    8 8 8 8 8 8 8 8 8 8
    9 9 9 9 9 9 9 9 9 9

:ref:`answer-problem-07`

Problem 8
~~~~~~~~~

Write code that will print the following:

.. code:: text

    0
    0 1
    0 1 2
    0 1 2 3
    0 1 2 3 4
    0 1 2 3 4 5
    0 1 2 3 4 5 6
    0 1 2 3 4 5 6 7
    0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7 8 9


Tip: This is just problem 6, but the inside loop no longer loops a fixed number of times.
Don't use ``range(10)``, but adjust that range amount.

:ref:`answer-problem-08`

Make sure you can write out the code for this and the prior problems. Repeat
until you can get it without looking up the answer. Yes, this
practice is work, but it will pay off later and you'll save time in the long run.


Problem 9
~~~~~~~~~

Write code that will print the following:

.. code:: text

    0 1 2 3 4 5 6 7 8 9
      0 1 2 3 4 5 6 7 8
        0 1 2 3 4 5 6 7
          0 1 2 3 4 5 6
            0 1 2 3 4 5
              0 1 2 3 4
                0 1 2 3
                  0 1 2
                    0 1
                      0


This one is difficult. Tip: Two loops are needed inside the outer loop
that controls each row.
First, a loop prints spaces, then a loop prints the numbers. Loop both these
for each row.
To start with, try writing just one inside loop that prints:

.. code:: text

    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
    0 1 2 3 4 5 6
    0 1 2 3 4 5
    0 1 2 3 4
    0 1 2 3
    0 1 2
    0 1
    0

Then once that is working, add a loop after the outside loop starts
and before the already existing inside loop. Use this
new loop to print enough spaces to right justify the other loops.

:ref:`answer-problem-09`

Problem 10
~~~~~~~~~~

Write code that will print the following
(Getting the alignment is hard, at least get the numbers):

 .. code:: text

      1   2   3   4   5   6   7   8   9
      2   4   6   8  10  12  14  16  18
      3   6   9  12  15  18  21  24  27
      4   8  12  16  20  24  28  32  36
      5  10  15  20  25  30  35  40  45
      6  12  18  24  30  36  42  48  54
      7  14  21  28  35  42  49  56  63
      8  16  24  32  40  48  56  64  72
      9  18  27  36  45  54  63  72  81

Tip: Start by adjusting the code in problem 1 to print:

.. code:: text

     0  0  0  0  0  0  0  0  0  0
     0  1  2  3  4  5  6  7  8  9
     0  2  4  6  8  10  12  14  16  18
     0  3  6  9  12  15  18  21  24  27
     0  4  8  12  16  20  24  28  32  36
     0  5  10  15  20  25  30  35  40  45
     0  6  12  18  24  30  36  42  48  54
     0  7  14  21  28  35  42  49  56  63
     0  8  16  24  32  40  48  56  64  72
     0  9  18  27  36  45  54  63  72  81

Then adjust the code to print:

.. code:: text

     1  2  3  4  5  6  7  8  9
     2  4  6  8  10  12  14  16  18
     3  6  9  12  15  18  21  24  27
     4  8  12  16  20  24  28  32  36
     5  10  15  20  25  30  35  40  45
     6  12  18  24  30  36  42  48  54
     7  14  21  28  35  42  49  56  63
     8  16  24  32  40  48  56  64  72
     9  18  27  36  45  54  63  72  81

Finally, use an 11if`` to print spaces if the number
being printed is less than 10. (Or use string formatting if you are
already familar with that.)

:ref:`answer-problem-10`

Problem 11
~~~~~~~~~~

Write code that will print the following:

.. code:: text

                      1
                    1 2 1
                  1 2 3 2 1
                1 2 3 4 3 2 1
              1 2 3 4 5 4 3 2 1
            1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

Tip: first write code to print:

.. code:: text

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8
    1 2 3 4 5 6 7 8 9

Then write code to print:

.. code:: text

    1
    1 2 1
    1 2 3 2 1
    1 2 3 4 3 2 1
    1 2 3 4 5 4 3 2 1
    1 2 3 4 5 6 5 4 3 2 1
    1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

Then finish by adding spaces to print the final answer.

:ref:`answer-problem-11`

Problem 12
~~~~~~~~~~

Write code that will print the following:

.. code:: text

                      1
                    1 2 1
                  1 2 3 2 1
                1 2 3 4 3 2 1
              1 2 3 4 5 4 3 2 1
            1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
        1 2 3 4 5 6 7 8
          1 2 3 4 5 6 7
            1 2 3 4 5 6
              1 2 3 4 5
                1 2 3 4
                  1 2 3
                    1 2
                      1

This can be done by combining problems 11 and 9.

:ref:`answer-problem-12`

Problem 13
~~~~~~~~~~

Write code that will print the following:

.. code:: text

                      1
                    1 2 1
                  1 2 3 2 1
                1 2 3 4 3 2 1
              1 2 3 4 5 4 3 2 1
            1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
        1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
          1 2 3 4 5 6 7 6 5 4 3 2 1
            1 2 3 4 5 6 5 4 3 2 1
              1 2 3 4 5 4 3 2 1
                1 2 3 4 3 2 1
                  1 2 3 2 1
                    1 2 1
                      1


:ref:`answer-problem-13`


