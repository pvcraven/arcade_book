Advanced Looping
================


.. image:: nested_loops.png
    :width: 200px

Games involve a lot of complex loops. This is a "challenge chapter" to learn
how to be an expert with loops. If you can understand the problems in this
chapter, by the end of it you can certify yourself as a loop expert.

If becoming a loop expert isn't your goal, at least make sure you can
write out the answers for the first eight problems. That will give you enough
knowledge to continue this book. (Besides, being a loop expert
never got anyone a date. Except for that guy in the
`Groundhog Day`_ movie.)

.. _Groundhog Day: http://www.imdb.com/title/tt0107048/

There are video explanations for the answers on-line.

Print Statement End Characters
------------------------------

By default, the "print" statement puts a <em>carriage return</em> at
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


Advanced Looping Problems
-------------------------

Problem 1
~~~~~~~~~

Write code that will print ten asterisks (*) like the following:

.. code:: text

    * * * * * * * * * *

Have this code print using a "for" loop, and print each
asterisk individually, rather than just printing ten asterisks with one "print" statement.
This can be done in two lines of code, a "for" loop and a "print" statement.
When you have figured it out, or given up, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/problem_1.php

Problem 2
~~~~~~~~~

Write code that will print the following:

.. code:: text

    * * * * * * * * * *
    * * * * *
    * * * * * * * * * * * * * * * * * * * *

This is just like the prior problem, but also printing five and twenty stars. Copy and paste
from the prior problem, adjusting the "for" loop as needed.

When you have figured it out, or given up, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/problem_2.php

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
It needs to be repeated ten times.
Work on this problem for at least ten minutes before looking at the answer.

When you have figured it out, or given up, here it is:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/10x10box.php

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
the numbers passed to the "range" function control.

When you have figured it out, or given up, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/problem_4.php

Problem 5
~~~~~~~~~

Use two "for" loops, one of them nested, to print the following 20x5
rectangle:

.. code:: text

    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * * * * * * *

Again, like Problem 3 and Problem 4, but with different range values.

When you have figured it out, or given up, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/problem_5.php

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

Use two nested loops. Print the first line with a loop, and not with:

.. code:: python

    print("0 1 2 3 4 5 6 7 8 9")

.. attention::

    First, create a loop that prints the first line. Then enclose it in another loop that repeats the line 10 times.
    Use either "i" or "j" variables for what the program prints.
    This example and the next one helps reinforce what those index
    variables are doing.

Work on this problem for at least ten minutes before looking at the answer.
The process of spending ten minutes working on the answer is far more important
than the answer itself.

http://ProgramArcadeGames.com/chapters/06_back_to_looping/number_square_answer.php

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


Answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/problem_7.php

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


After working at least ten minutes on the problem, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/top_right_triangle.php

Make sure you can write out the code for this and the prior problems. Yes, this
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

After working at least ten minutes on the problem, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/bottom_left_triangle.php

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

Finally, use an "if" to print spaces if the number
being printed is less than 10.

After working at least ten minutes on the problem, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/multiplication_table.php

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

After working at least ten minutes on the problem, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/top_triangle.php

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

After working at least ten minutes on the problem, here is the answer:

http://ProgramArcadeGames.com/chapters/06_back_to_looping/three_quarters.php

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




After working at least ten minutes on the problem, here is the answer:


http://ProgramArcadeGames.com/chapters/06_back_to_looping/full_diamond.php

