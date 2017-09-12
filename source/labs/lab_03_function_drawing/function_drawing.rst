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


Requirements for Animation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Animate an object. The movement does not need to be complex.

Tips to Make Things Easier
--------------------------

Putting Code In a Function
^^^^^^^^^^^^^^^^^^^^^^^^^^

Say I have a drawing with a tractor. See highlighted lines below:

.. literalinclude:: make_function_1.py
    :caption: make_function_1.py
    :language: python
    :linenos:
    :emphasize-lines: 67-86

I can easily move it to a function and call the function. See the highlighted lines below:

.. literalinclude:: make_function_2.py
    :caption: make_function_2.py
    :language: python
    :linenos:
    :emphasize-lines: 9-29, 90

But my function isn't very useful, because it always draws the tractor in the same spot. I can pass in parameters like:

.. literalinclude:: make_function_3.py
    :caption: make_function_3.py
    :language: python
    :linenos:
    :emphasize-lines: 9, 90

This is close, but not great. My function ignores the ``x`` and ``y`` that are passed in. So I need to use that x and y.

See below. I use x and y, and draw two tractors.

.. literalinclude:: make_function_4.py
    :caption: make_function_4.py
    :language: python
    :linenos:
    :emphasize-lines: 13-29, 90-91

Better. But when I tell the computer to draw the tractor at (0, 0), it doesn't draw it there. It draws it at the
original spot. Which makes sense when you look at the coordinates. Our original code does not center the tractor at (0, 0).

We can fix this by looking at the smallest x and smallest y of the drawing and subtract them out:

.. literalinclude:: make_function_5.py
    :caption: make_function_5.py
    :language: python
    :linenos:
    :emphasize-lines: 13-29, 90-91

Or more simply:

.. literalinclude:: make_function_6.py
    :caption: make_function_6.py
    :language: python
    :linenos:
    :emphasize-lines: 13-29, 90-91

Animation Tips
^^^^^^^^^^^^^^

Below are progressively more complex examples on how to do this.

Setup
'''''

First, make sure you've completed the steps above. Move your drawing items into functions. This next part will be
much easier if you've already done that.

Our next step to do animation is to move
all the drawing commands out of ``main`` and into a new function called ``on_draw``. Don't just move the item
you'll be animating here, move *everything*.

See the code example below. Note what the ``main`` function looks like. Note how the drawing is now in ``on_draw``.

.. literalinclude:: animate_example_00.py
    :caption: animate_example_01.py
    :language: python
    :linenos:

Example 1
'''''''''

Now for the animation.

In this example, we move the box to the left by changing ``center_x``. Also note that every time we use ``center_x``
we let the computer know it is a variable inside of ``on_draw`` that persists between calls. We do this by
calling it ``on_draw.center_x``.

.. literalinclude:: animate_example_01.py
    :caption: animate_example_01.py
    :language: python
    :linenos:

Example 2
'''''''''

This example moves the box up and to the left by changing both ``x`` and ``y``. We also move the code for drawing the
window into a ``main`` function.

.. literalinclude:: animate_example_02.py
    :caption: animate_example_02.py
    :language: python
    :linenos:

Example 3
'''''''''

This example uses new variables ``delta_x`` and ``delta_y`` to track the vector of the rectangle. It will multiply
either of these by -1 to reverse the direction when we hit the edge of the screen.

But it isn't perfect, because we are checking the center of the rectangle to hit the edge, rather than the
outside edge of the rectangle.

.. literalinclude:: animate_example_03.py
    :caption: animate_example_03.py
    :language: python
    :linenos:

Example 4
'''''''''

This adds the math to check the outside edge.

.. literalinclude:: animate_example_04.py
    :caption: animate_example_04.py
    :language: python
    :linenos:

Example 5
'''''''''

We get a variable called ``delta_time`` that holds how long it has been since the computer was last called. If the
computer is slowing down, we can keep the movement from slowing down by adjusting for the actual time between function
calls. The example below tracks how many pixels per second we should travel, then multiplies that by ``delta_time``.

Note that a video walkthrough of the code is at:
https://vimeo.com/168063840

.. literalinclude:: animate_example_full.py
    :language: python
    :caption: animate_example_full.py
    :linenos:



