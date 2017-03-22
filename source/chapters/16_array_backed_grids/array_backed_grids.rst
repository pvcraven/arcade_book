.. sectnum::
    :start: 16

Array-Backed Grids
==================

Introduction
------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/mdTeqiWyFnc" frameborder="0" allowfullscreen></iframe>

Games like minesweeper, tic-tac-toe, and many types of adventure games keep
data for the game in a grid of numbers. For example, a tic-tac-toe board:
 
+---+---+---+
|   | O | O |
+---+---+---+
|   | X |   |
+---+---+---+
| X |   |   |
+---+---+---+
 
. . . can use a grid of numbers to represent the empty spots, the O's and the
X's like this:

+---+---+---+
| 0 | 2 | 2 |
+---+---+---+
| 0 | 1 | 0 |
+---+---+---+
| 1 | 0 | 0 |
+---+---+---+

This grid of numbers can also be called a *two-dimensional* array or a *matrix*.
(Finally, we get to learn about The Matrix.) The values of the numbers in the
grid represent what should be displayed at each board location. In the prior
example, 0 represents a spot where no one has played, a 1 represents an X, and
a 2 represents an O.

.. figure:: minesweeper.png

    Figure 16.1: Minesweeper game, showing the backing grid of numbers

The figure above is an example from the classic minesweeper game. This example
has been modified to show both the classic display on the left, and the grid of
numbers used to display the board on the right.

The number ``10`` represents a mine, the number ``0`` represents a space that
has not been clicked, and the number 9 represents a cleared space. The numbers
``1`` to ``8`` represent how many mines are within the surrounding eight
squares, and is only filled in when the user clicks on the square.

Minesweeper can actually have two grids. One for the regular display, and a
completely separate grid of numbers that will track if the user has placed
"flags" on the board marking where she thinks the mines are.

Classic adventure game maps are created using a tiled map editor. These are
huge grids where each location is simply a number representing the type of
terrain that goes there. The terrain could be things like dirt, a road, a
path, green grass, brown grass, and so forth. Programs like Tiled_ shown in
the figure below allow a developer to easily make these maps and write the grid to
disk.

.. _Tiled: http://www.mapeditor.org/

.. figure:: qt_tiled.png

    Figure 16.2: Using Qt Tiles to create an adventure map

Adventure games also use multiple grids of numbers, just like minesweeper has
a grid for the mines, and a separate grid for the flags. One grid, or "layer,"
in the adventure game represents terrain you can walk on; another for things
you can't walk on like walls and trees; a layer for things that can instantly
kill you, like lava or bottomless pits; one for objects that can be picked up
and moved around; and yet another layer for initial placement of monsters.

Maps like these can be loaded in a Python program, but unfortunately a full
description of how to manage is beyond the scope of this book. Projects like
PyTMX_ that provide some of the code needed to load these maps.

.. _PyTMX: https://github.com/bitcraft/PyTMX

Application
-----------

Enough talk, let's write some code. This example will create a grid that will
trigger if we display a white or green block. We can change the grid value and
make it green by clicking on it. This is a first step to a grid-based game like minesweeper, battleship, connect four, etc. (One year I had a student call me over and she had modified a program like this to show my name in flashing lights. That was . . . disturbing. So please use this knowledge only for good!)

Go to the example code page and download the base template file:

http://ProgramArcadeGames.com/python_examples/f.php?file=pygame_base_template.py

Starting with the blank template file, attempt to recreate this program
following the instructions here. The final program is at the end of this
chapter but don't skip ahead and copy it! If you do that you'll have learned
nothing. Anyone can copy and paste the code, but if you can recreate this
program you have skills people are willing to pay for. If you can only copy
and paste, you've wasted your time here.

Drawing the Grid
^^^^^^^^^^^^^^^^

1. Adjust the program's window size to 255x255 pixels.
2. Create variables named ``width``, ``height``, and ``margin``. Set the width
   and height to 20. This will represent how large each grid location is. Set
   the margin to 5. This represents the margin between each grid location and
   the edges of the screen. Create these variables before the main program loop.
3. Draw a white box in the lower-left corner. Draw the box drawn using the
   height and width variables created earlier. (Feel free to adjust the colors.)
   Use the `draw_rectangle_filled`_ function. You will need to center the
   rectangle not at (0, 0) but at a coordinate that takes into account the
   height and width of the rectangle.
   When you get done your program's window should look like:

Figure 16.3: Step 3

4. Use a ``for`` loop to draw 10 boxes in a row. Use ``column`` for the variable name
   in the ``for`` loop. The output will look like one long box until we add in the
   margin between boxes. See Figure 16.4.

Figure 16.4: Step 4

5. Adjust the drawing of the rectangle to add in the ``margin`` variable. Now
   there should be gaps between the rectangles. See Figure 16.5.

Figure 16.5: Step 5

6. Add the margin before drawing the rectangles, in addition to between each
   rectangle. This should keep the box from appearing right next to the window
   edge. See Figure 16.6.

Figure 16.6: Step 6

7. Add another ``for`` loop that also will loop for each row. Call the variable in
   this ``for`` loop ``row``. Now we should have a full grid of boxes. See Figure 16.7.

Figure 16.7: Step 7

Populating the Grid
^^^^^^^^^^^^^^^^^^^

8. Now we need to create a two-dimensional array. Creating a two-dimensional array
   in Python is, unfortunately, not as easy as it is in some other computer
   languages. There are some libraries that can be downloaded for Python that make
   it easy, but for this example they will not be used. To create a two-dimensional
   array and set an example, use the code below:

.. code-block:: python
    :caption: Create a 10x10 array of numbers

    # --- Create grid of numbers
    # Create an empty list
    grid = []
    # Loop for each row
    for row in range(10):
        # For each row, create a list that will
        # represent an entire row
        grid.append([])
        # Loop for each column
        for column in range(10):
            # Add a the number zero to the current row
            grid[row].append(0)

A much shorter example is below, but this example uses some odd parts of
Python that I don't bother to explain in this book:

.. code-block:: python
    :caption: Create a 10x10 array of numbers

    grid = [[0 for x in range(10)] for y in range(10)]

Use one of these two examples and place the code to create our array ahead of
your main program loop.

9. Set an example location in the array to 1.

Two dimensional arrays are usually represented addressed by first their row,
and then the column. This is called a row-major storage. Most languages use
row-major storage, with the exception of Fortran and MATLAB. Fortran and
MATLAB use column-major storage.

.. code-block:: python

    # Set row 1, column 5 to one
    grid[1][5] = 1

Place this code somewhere ahead of your main program loop.

10. Select the color of the rectangle based on the value of a variable named
    ``color``. Do this by first finding the line of code where the rectangle is
    drawn. Ahead of it, create a variable named ``color`` and set it equal to white.
    Then replace the white color in the rectangle declaration with the ``color``
    variable.

11. Select the color based on the value in the grid. After setting color to
    white, place an if statement that looks at the value in
    ``grid[row][column]`` and changes the color to green if the grid value is
    equal to 1. There should now be one green square. See Figure 16.8.

Figure 16.8: Step 11

12. Print "click" to the screen if the user clicks the mouse button. See
    bitmapped_graphics.py for example code of how to detect a mouse click.
13. Print the mouse coordinates when the user clicks the mouse.
    See move_mouse.py for an example on getting the position of the mouse. See
    Figure 16.9.

Figure 16.9: Step 13

14. Convert the mouse coordinates into grid coordinates. Print those
    instead. Remember to use the width and height of each grid location
    combined with the margin. It will be necessary to convert the final
    value to an integer. This can be done by using int or by using the
    integer division operator ``//`` instead of the normal division operator
    ``/``. See Figure 16.10.

Figure 16.10: Step 14

15. Set the grid location at the row/column clicked to 1. See Figure 16.11.

Figure 16.11: Step 15

16.2.3 Final Program

.. _draw_rectangle_filled: http://pythonhosted.org/arcade/arcade.html#arcade.draw_commands.draw_rectangle_filled
