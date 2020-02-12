.. _how-to-draw:

How to Draw with Your Computer
==============================

We've setup our system, learned to use git, and run our first program
using the ``print`` function. Now we are ready to start using
functions to make graphics!

In this chapter we will learn to import a graphics library and call its
functions. By the end of this chapter, you will be able to create your
own art like this:

.. image:: simpson_map.png

You can page through several other examples of student-created art
in :ref:`lab-02`.

We will concentrate on learning to call functions for graphics
in this chapter. Those same concepts apply if you want to call functions
for other activities
like robotics, data analytics, and web site programming.

Creating a New Program
----------------------

Open up PyCharm. It should start up with the same set of project files
we used last chapter. We'll use
this project for all our work in this book. Do **not** create new projects for each
lab or program.

We are going to create a lot of code samples as we learn new concepts.
You should already have a folder called ``Scratch Work``. We can put our code
samples there. Create a new sample by:

#. Right-click on ``Scratch Work``
#. Click ``New``
#. Click ``Python File``

.. image:: create_drawing_source_file.png

Name the file ``drawing_samples.py``. Make sure it is inside the ``Scratch Work``
folder. If it isn't, drag to move it. The file should appear like the
following:

.. image:: drawing_samples.png
    :width: 35%

Comments Your Code
------------------

Before we start writing long programs, we need to learn about **code comments**.
When typing in computer code, sometimes we want to be able to write things
for our own benefit, and for anyone else that reads the code. Since this won't be
computer code, we need to tell the computer to ignore it.

Below are two ways of adding comments to code in the Python computer language:

.. literalinclude:: comments.py
    :language: python
    :linenos:

The Python standard is to use multi-line comments with triple quotes
at the start of each source file to explain what the code does. For now,
just use single-line comments everywhere else.

Go ahead and try putting in your own comments.

Let's try running the program. But before we run the program, we need to make
sure we are running the *right* program. Look at the image below. If I select
"run" with the green arrow, I will run ``lab_01.py``, *not* the program I
want to run. You need to right-click on our program and select
"Run ``drawing_sample.py``" instead.

.. image:: running_the_right_program.png

Hey wait! When we finally run our program, nothing happens. That's because
the only code that we wrote were "comments." Comments are ignored.
Therefore, there was nothing for the computer to do. Read on.

Import the Arcade Library
-------------------------

.. image:: library.svg
    :width: 30%
    :class: right-image

Before we can draw anything, we need to import a "library" of code that has
commands for drawing.

Computer languages come with a set of built-in commands. Most programs will
require *more* commands than what the computer language loads by default. These
sets of commands are called **libraries**. Some languages have their own special
term for these libraries. In the case of Python, they are called **modules**.
In the Python world you can use the term library and module interchangeably.

Thankfully, it is easy to import a library of code.
If we want to use the Arcade library, all we need
to do is add ``import arcade`` at the top of our program.

.. attention::
    Libraries should always be imported at the **top** of your program.
    Only comments should appear ahead of an ``import`` statement.
    Technically, you *can* put the ``import`` statement somewhere else,
    just like technically you *can* wear a pair of shorts on your head. But
    don't. Trust me on this.

In the code below, we've imported the Arcade library. If you run the code,
yet again nothing will happen. We've loaded the arcade
library, but we haven't *done* anything with it yet. That's our next step.

.. literalinclude:: import_arcade.py
    :language: python
    :linenos:
    :emphasize-lines: 7

.. note::
   If you get an error that you can't import the arcade library, it hasn't been
   installed for your current Python environment. Go back
   and follow the directions in :ref:`installing-arcade`.

How to Open a Window for Drawing
--------------------------------

The first Arcade function we are going to learn is ``open_window``. This
command opens a window with a given size and title.
The code looks like the following:

.. code-block:: python

    arcade.open_window(600, 600, "Drawing Example")

What does each part mean?

.. image:: open_window.svg

To begin, we select the arcade library
with ``arcade``. Then we separate the library from the function name
with a period: ``.`` Next, we put in the name of the function, ``open_window``.

.. sidebar:: Vocabulary

    We give commands to the computer by using **functions**.
    The **function name**, such as ``print`` or ``open_window``
    is how we identify the function.

    We can import new functions
    by using a **library**. The **library name**, such as ``arcade``
    is how we identify the library.

    A **statement** is a line of code in Python. It includes the
    function name, parentheses, numbers, text and everything else
    required to call the function or perform some other operation.

Just like the ``print`` function, we surround the function
**parameters** with parentheses. For example:

.. code-block:: python

    my_function(parameters)

If we have more than one parameter, we can use commas to separate them.
PEP-8 asks that each comma is followed by a space. If we have a library,
then we specify that up front. For example:

.. code-block:: python

    my_library.my_function(parameter_1, parameter_2)


The ``open_window`` function requires at least three parameters:

* The window width in pixels.
* The window height in pixels.
* The text that will appear on the title bar.

In the case of width and height, the numbers specify the part of the window you
can draw on. The actual
window is larger to accommodate the title bar and borders. So a 600x600 window
is really 602x632 if you count the title bar and borders.

How do we know ``open_window`` is the name of the function to call? How did
we know what parameters to use? The names of the functions, the order of the
parameters, is the **Application Program Interface** or "API" for short. You can
click here for the `Arcade API`_. Any decent library will have API
documentation, and example code you can find on the web to learn how to use it.

.. _Arcade API: http://arcade.academy/quick_index.html

Below is an example program that will open up a window:

.. literalinclude:: open_window.py
    :language: python
    :linenos:
    :emphasize-lines: 13

Try running the code above. It kind-of works. If you have fast eyes, and a slow
computer you might see the window pop open, then immediately close.
If your computer is super-fast, you won't see anything at all because the
window opens and closes faster than your eye can process.
Why does it close? Because our program is done! We've ran out of code
to execute.

To keep the window open, we need to pause until the user hits the
close button. To do this, we'll use the ``run`` command in the Arcade library.
The ``run`` command takes no parameters, but still needs parentheses.

.. literalinclude:: open_window_and_pause.py
    :language: python
    :linenos:
    :emphasize-lines: 16

You should get a window that looks something like this:

.. image:: empty_window.png
    :width: 300px


Clearing the screen
-------------------

Right now we have default white as our background.
How do we get a different color? Use the ``set_background_color`` command.

Before we can see the color, we need two more commands. These
tell the Arcade library when you are about to start drawing (``start_render``),
and when you are done drawing (``finish_render``).

See below:

.. literalinclude:: open_window_and_clear_screen.py
    :language: python
    :linenos:
    :emphasize-lines: 16, 19, 24

.. image:: clear_screen.png
   :width: 35%

Specifying Colors
-----------------

Wait, where did ``arcade.csscolor.SKY_BLUE`` come from? How do I get to choose
the color I want? There are two ways to specify colors:

* Look at the `arcade.color API documentation`_ and specify by name.
* Look at the `arcade.csscolor API documentation`_ and specify by name.
* Specify the RGB or RGBA color.

To specify colors by name, you can look at the color API documentation and
use something like ``arcade.color.AQUAMARINE`` in your program. Those color
names come from the ColorPicker `color chart`_.

The colors in ``arcade.csscolor`` come from the standard color names used in
creating web pages. Therefore, getting used to these color names can help
with web development skills.

If the color you want isn't in the chart, or you just don't want to use
that chart, you can specify colors by "RGB" value. RGB stands for Red, Green, and
Blue.

Computers, TVs, color changing LEDs, all
work by having three small lights close together. A red light, a green light,
and a blue light. Turn all three lights off and you get black. Turn all three
lights on and you get white. Just turn on the red, and you get red. Turn on
both red and green to get yellow.

RGB based monitors work on an *additive* process. You start with black and
add light to get color.
This is different than
paint or ink, which works on a *subtractive* process. You start with white and
add to get darker colors.

Therefore, keep separate in your mind how light-based RGB color works from how
paint and ink works.

We specify how much red, green, and blue to use using numbers. No light is zero.
Turn the light on all the way and it is 255. So ``(0, 0, 0)`` means no red,
no green, no blue. Black. Here are some other examples:

===== ======= ====== ===========
Red   Green   Blue   Color
===== ======= ====== ===========
0     0       0      Black
255   255     255    White
127   127     127    Gray
255   0       0      Red
0     255     0      Green
0     0       255    Blue
255   255     0      Yellow
===== ======= ====== ===========

There are tools that let you easily find a color, and then get the RGB value for it.
If you go to the Google search engine and type in "`color picker`_" it shows a nice
tool for picking colors. At the bottom of the color picker, the color is shown
in hex, CMYK, and several other formats. Remember, we want the RGB
value.

.. _color picker: https://www.google.com/search?q=color+picker

.. image:: colorpicker.png

After getting the RBG value, specify the color as a set of three numbers surrounded
by parenthesis, like the following code:

.. code-block:: python

    arcade.set_background_color((189, 55, 180))

In addition to RGB, you can also specify the "Alpha" with an RGBA value.
The "Alpha Channel" controls
how transparent the color is. If you draw a square with an alpha of 255, it will
be solid and hide everything behind it. An alpha of 127 will be in the middle,
you will see some of the items behind the square. An alpha of 0 is completely
transparent and you'll see nothing of the square.

.. _color chart: http://www.colorpicker.com/color-chart/
.. _arcade.csscolor API documentation: http://arcade.academy/arcade.csscolor.html
.. _arcade.color API documentation: http://arcade.academy/arcade.color.html

Wait, What Is Up With 255?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice how the color values go between 0 and 255? That's strange. Why 255? Why
not 100? Why not 1000?
This requires an explanation of a very important concept of how computers
handle numbers.

You may have heard that computers think in 1's and 0's.
That's true.
Everything to the computer is a switch. If there is electricity, we have a 1. If
there is no electricity we have a 0. We can store those 1's and 0's in memory.
We call these 1's and 0's **binary numbers**.

How do we go from 1's and 0's to numbers we normally use? For example, a
number like 758? We do that with a combination of 1's and 0's. Like this:

================ ===========
Binary - Base 2  Base 10
================ ===========
0000             0
0001             1
0010             2
0011             3
0100             4
0101             5
0110             6
0111             7
1000             8
================ ===========

See the pattern? It is the same pattern we use when we count as a kid.
As a kid we learned to go 0 to 9,
then when we hit 9 we go back to 0 and add one to the ten's place. Here we only
have 0 to 1 instead of 0 to 9. And instead of a "ten's place" we have a "two's
place."

You might have used "bases" in math class long ago. Computers work in Base-2
because they only have two ways to count, on or off.
Humans think in Base-10 because we have 10 fingers.

Numbers are stored in **bytes**. A byte is a set of eight binary numbers.
If we were to follow the pattern we started above, the largest number we
could store with eight 1's and 0's is:

.. code-block:: text

    1111 1111

In Base-10 this is 255.

Let's use some math. We have 8 ones and zeros. That give us 2 :sup:`8` = 256
possible combinations. Each combination is a different number.
Since zero is a counts as a number, that makes the biggest number 255.

If we had 16 bits, then we'd have 2 :sup:`16` = 65,536 possible combinations. Or a
number from 0-65,535. A 32-bit computer can hold numbers up
to 2 :sup:`32` = 4,294,967,296. A 64-bit computer can hold really large numbers!

So because a computer holds colors with one byte for red, one for green, and one
for blue, each color has a value range from 0 - 255.

The Coordinate System
---------------------

In your math classes, you've learned about the Cartesian coordinate system,
which looks like this:

.. figure:: cartesian_coordinate_system.svg
    :width: 350px

    Source: `Wikipedia: Cartesian coordinate system <https://commons.wikimedia.org/wiki/File:Cartesian_coordinate_system_(comma).svg>`_

Our graphics will be drawn using this same system. But there are additional
things to keep in mind:

* We will only draw in the upper right quadrant. So 0,0 will be in the
  lower left of the screen, and all negative coordinates will be off-screen.
* Each "point" will be a pixel. So a window that is 800 pixels wide, will have
  x-coordinates that run from 0 to 799. (Zero is one of the pixels, so 0-799 is
  800 pixels. Off-by-one errors are *very* common in computing.)

Drawing a Rectangle
-------------------

Let's start drawing with a rectangle. The function
we will use is ``draw_lrtb_rectangle_filled``. It stands for "draw
left-right-top-bottom rectangle".

To make the bottom half of our screen green grass, we'll start
with a left of 0, a right of 599, a top of 300, and a bottom of zero.

.. literalinclude:: draw_rect.py
    :language: python
    :linenos:
    :emphasize-lines: 24

Sometimes we don't want to specify a rectangle by left-right-top-bottom.
There is also an option to specify it by center, width, and height using the
``draw_rectangle_filled`` function. For example
this displays a tree trunk:

.. code-block:: python

    # Tree trunk
    arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

We can draw an circle:

.. code-block:: python

    # Tree top
    arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

If you don't want a perfect ellipse, you can draw a circle:

.. code-block:: python

    # Another tree, with a trunk and ellipse for top
    arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

Triangles are a bit more difficult. You need to think about where each point
goes.

.. code-block:: python

    # Another tree, with a trunk and triangle for top
    arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(300, 400, 270, 320, 330, 320, arcade.csscolor.DARK_GREEN)


.. literalinclude:: draw_02.py
    :language: python
    :linenos:

Drawing Primitives
------------------

For a program showing all the drawing primitives, see the example
`Drawing Primitives`_. Also, see the API documentation's `Quick Index`_.

What's next? Try :ref:`lab-02`.

.. _Drawing Primitives: http://arcade.academy/examples/drawing_primitives.html
.. _Quick Index: http://arcade.academy/quick_index.html#id1
