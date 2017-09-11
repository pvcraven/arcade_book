.. _lab-03:

Lab 3: Drawing with Functions
=============================

Your goal: Draw and animate an image.

.. image:: lab_03_example_01.gif

You can update your program from Lab 2, or create a new program. This lab is worth
20 points. See the point breakdown below.

Incorporate the following items:

* Find the folder for Lab 03 in PyCharm. Feel free to use any code from Lab 02 you want, just
  copy it across.
* Create three functions that draw something. (15 pts total, up to 5 pts
  per function)

  * Define the function and successfully call it. (1 pt)
  * Make your drawing function complex. 0 points for a one-line function that
    just draws a rectangle, 0 points for copying the example from the book,
    2 points for a cohesive multi-line function. (2 pts)
  * Pass in ``x`` and ``y`` parameters and successfully position the object
    as shown in :ref:`custom-drawing-function`. (2 pts)

* Properly use the ``main`` function for your main program as shown
  in :ref:`make-everything-a-function`. (1 pt)

Drawing with functions is worth 16 points. You can get the final 4 points by animating your image.

Animation
---------
Try to animate the object. Below are progressively more complex examples on how to do this.

Example 1
^^^^^^^^^

In this example, we move the box to the left by changing ``x``.

.. literalinclude:: animate_example_01.py
    :caption: animate_example_01.py
    :language: python
    :linenos:

Example 2
^^^^^^^^^

This example moves the box up and to the left by changing both ``x`` and ``y``. We also move the code for drawing the
window into a ``main`` function.

.. literalinclude:: animate_example_02.py
    :caption: animate_example_02.py
    :language: python
    :linenos:

Example 3
^^^^^^^^^

This example uses new variables ``delta_x`` and ``delta_y`` to track the vector of the rectangle. It will multiply
either of these by -1 to reverse the direction when we hit the edge of the screen.

But it isn't perfect, because we are checking the center of the rectangle to hit the edge, rather than the
outside edge of the rectangle.

.. literalinclude:: animate_example_03.py
    :caption: animate_example_03.py
    :language: python
    :linenos:

Example 3
^^^^^^^^^

This adds the math to check the outside edge.

.. literalinclude:: animate_example_04.py
    :caption: animate_example_04.py
    :language: python
    :linenos:

Example 4
^^^^^^^^^

We get a variable called ``delta_time`` that holds how long it has been since the computer was last called. If the
computer is slowing down, we can keep the movement from slowing down by adjusting for the actual time between function
calls. The example below tracks how many pixels per second we should travel, then multiplies that by ``delta_time``.

Note that a video walkthrough of the code is at:
https://vimeo.com/168063840

.. literalinclude:: animate_example_full.py
    :language: python
    :caption: animate_example_full.py
    :linenos:




