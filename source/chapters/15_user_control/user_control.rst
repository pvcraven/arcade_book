.. _user-control:

Using the Window Class
======================

We can use a class to represent our program.
The Arcade library has a built-in class that represents a window on the
screen. We can create our own child class and override functions to handle:

* Start-up and initialization
* Drawing the items on our screen
* Animating/Updating the positions of items on our screen
* Responding to the keyboard
* Responding to the mouse

One of the best ways of learning to program is to look at sample code. This
chapter has several examples designed to learn how to:

* Open a window using an object-oriented approach
* Animating objects
* Moving objects with the mouse
* Moving objects with the keyboard
* Moving objects with the joystick

Creating a Window with a Class
------------------------------

Up to now, we have used a function called ``open_window`` to open a window.
Here's the code:

.. literalinclude:: open_window_with_function.py
    :caption: open_window_with_function.py
    :language: python
    :emphasize-lines: 8
    :linenos:

We can also create an instance of a class called ``Window`` to open a window.
The code is rather straight-forward:

.. literalinclude:: open_window_with_object.py
    :caption: open_window_with_object.py
    :language: python
    :emphasize-lines: 8
    :linenos:

Function calls, and calls to create an instance of an object look very similar.
The tell-tale clue that we are creating an instance of an object in the second
example is the fact that ``Window`` is capitalized.

Extending the Window Class
--------------------------

Arcade's ``Window`` class has a lot of built-in methods that are automatically
called when needed. Methods for drawing, for responding to the keyboard, the
mouse, and more. You can see all the methods by looking at the
`Window Class Documentation`_.
But by default, these methods don't do anything. We need
to change that.

As we learned from the prior chapter, we can extend the functionality of a class
by creating a child class.
Therefore, we can extend the ``Window`` class by creating
a child class of it. I'm going to call my child class ``MyGame``.

.. _Window Class Documentation: http://arcade.academy/arcade.html#arcade.application.Window

.. literalinclude:: extending_window_class.py
    :caption: extending_window_class.py
    :language: python
    :linenos:
    :emphasize-lines: 4-9, 13

Drawing with the Window Class
-----------------------------

To draw with the ``Window`` class, we need to create our own method called
``on_draw``. This will override the default ``on_draw`` method built into the ``Window``
class. We will put our drawing code in there.

The ``on_draw`` method gets called about 60 times per second. We'll use this
fact when we do animation.

We also need to set the background color. Since we only need to do this once,
we will do that in the ``__init__`` method. No sense setting the background
60 times per second when it isn't changing.

.. literalinclude:: drawing.py
    :caption: drawing.py
    :language: python
    :linenos:
    :emphasize-lines: 11-12, 14-18

The result of this program just looks like:

.. image:: draw_example.png

Animating
---------

By overriding the ``update`` method, we can update our ball position and
animate our scene:

.. literalinclude:: simple_animation.py
    :caption: simple_animation.py
    :language: python
    :linenos:
    :emphasize-lines: 14-16, 22, 24-27

Encapsulating Our Animation Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It doesn't take much imagination to realize that adding more parameters to
the ball, getting it to bounce, or even having several balls on the screen would
make our ``MyApplication`` class very complex.

If only there was a way to encapsulate all that "ball" stuff together. Wait!
There is! Using classes!

Here is a more complex example, but all the logic for the ball has been moved
into a new ``Ball`` class.

.. literalinclude:: ball_class_example.py
    :caption: ball_class_example.py
    :language: python
    :linenos:

Here it is in action:

.. image:: ball_class_example.gif

Animating a List
^^^^^^^^^^^^^^^^

Wouldn't it be nice to animate multiple items? How do we track multiple items?
With a list! This takes our previous example and animates three balls at once.

.. literalinclude:: ball_list_example.py
    :caption: ball_list_example.py
    :language: python
    :linenos:
    :emphasize-lines: 54-65, 71-74, 81-82

.. image:: ball_list_example.gif

