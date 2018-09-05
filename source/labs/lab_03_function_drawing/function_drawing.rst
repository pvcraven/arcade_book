.. _lab-03:

Lab 3: Drawing with Functions
=============================

Requirements
------------
Your goal: Draw and animate an image.

.. image:: lab_03_example_01.gif

Requirements for Drawing
^^^^^^^^^^^^^^^^^^^^^^^^

You can update your program from Lab 2, or create a new program. This lab is worth
20 points. See the point breakdown below.

Incorporate the following items:

* Find the folder for Lab 03 in PyCharm and start entering your code there.
  Feel free to use any code from Lab 02 you want, just copy it across.
* Make sure you are putting your program in the Lab 3 folder, and not just
  changing Lab 2 to have Lab 3 requirements.
* We are going to be following the instructions/example in :ref:`custom-drawing-function`.
* Put everything into a function as shown in :ref:`make_the_main_function`.
* Create three functions that draw something. (15 pts total, up to 5 pts
  per function)

  * Define the function and successfully call it. (1 pt)
  * Make your drawing function complex. 0 points for a one-line function that
    just draws a rectangle, 0 points for copying the example from the book,
    2 points for a cohesive multi-line function. (2 pts)
  * Pass in ``x`` and ``y`` parameters and successfully position the object
    as shown in :ref:`make_the_drawing_function`. (2 pts)

Drawing with functions is worth 16 points. You can get the final 4 points by animating your image.


Requirements for Animation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Animate an object. The movement does not need to be complex. See :ref:`animate-drawing` for
an example.

Double Check
^^^^^^^^^^^^

Make sure you don't put functions inside of functions. After the ``import`` statement, each function should
be listed out, one ``def`` after the other. But no ``def`` inside of another ``def``.

Also make sure you have *three* functions that take in an ``(x, y)`` position to draw an object,
not just one.