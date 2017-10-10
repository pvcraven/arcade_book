.. _lab-07:

Lab 7: User Control
===================

This lab gives you a chance to practice drawing an object with a function
and allow the user to control it.

Create one program that does/implements the following:

* Create a ``Lab 07 - User Control`` folder for this lab, or use one that is already set up in your project.
* Begin your code with the template below:

.. literalinclude:: template.py
    :caption: Lab 7 Template
    :language: python
    :linenos:

* Create a background image of some sort in the ``on_draw`` method.
  (Feel free to use any of *your* code that *you* have written from
  prior labs that you have.)
* Create at least two different functions that draw an object
  to the screen given a particular x, y coordinate. Again, feel free to pull
  from prior labs.
* In :ref:`user-control`, we talked about moving graphics with the keyboard, a game
  controller, and the mouse. Pick two of those and use them to control two
  different items on the screen that are drawn by the functions you just made.
* In the case of the game controller and the keyboard, make sure to add checks
  so that your object does not move off-screen and get lost.
* Add a sound effect for when the user clicks the mouse button.
* Add a sound effect for when the user bumps into the edge of the screen.

.. _Arcade Starting Template: http://arcade.academy/examples/starting_template.html
