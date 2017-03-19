.. sectnum::
    :start: 13

.. _sprites-and-walls:

Sprites and Walls
=================

The Simple Physics Engine
-------------------------

Many games with sprites often have "walls" that the character can't move
through. There are rather straight-forward to create.

To begin with, let's get a couple images. Our character, and a box that will
act as a blocking wall. Both images are from `kenney.nl`_.

.. _kenney.nl: http://kenney.nl/

.. figure:: images/character.png
    :width: 50px

    images/character.png

.. figure:: images/boxCrate_double.png
    :width: 50px

    images/boxCrate_double.png

In our ``setup`` method, we can create a row of box sprites using a ``for``
loop. In the code below, our y value is always 200, and we change the x value
from 173 to 650. We put a box every 64 pixels because each box happens to be
64 pixels wide.

.. code-block:: python

    for x in range(173, 650, 64):
        wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        self.all_sprites_list.append(wall)
        self.wall_list.append(wall)

The Arcade Library has a built in "physics engine." A physics engine handles
the interactions between the virtual physical objects in the game.
For example, a physics engine might be several balls running into each other,
a character sliding down a hill, or a car making a turn on the road.

Physics engines have made impressive gains on what they can simulate. For our
game, we'll just keep things simple and make sure our character can't walk
through walls.

We can create the physics engine in our ``setup`` method with the following
code:

.. code-block:: python

    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

This identifies the player character (``player_sprite``), and a list of sprites
(``wall_list``) that the player character isn't allowed to pass through.

.. code-block:: python

    self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

Before, we updated all the sprites with a ``self.all_sprites_list.update()``
command. With the physics engine, we will instead update the sprites by using
the physics engine's update::

    self.physics_engine.update()

The simple physics engine follows the following algorithm:

* Move the player in the x direction according to the player's ``change_x``
  value.
* Check the player against the wall list and see if there are any collisions.
* If the player is colliding:

    * If the player is moving right, set the player's right edge to the wall's
      left edge.
    * If the player is moving left, set the player's left edge to the wall's
      right edge.
    * If the player isn't moving left or right, print out a message that we
      are confused how we hit something when we aren't moving.

* Then we just do the same thing, except with the y coordinates.

You can see the `physics engine source code`_ on GitHub.

.. _physics engine source code: https://github.com/pvcraven/arcade/blob/master/arcade/physics_engines.py

Here's the full example:

.. literalinclude:: sprite_move_walls.py
    :caption: sprite_move_walls.py
    :language: python
    :linenos:

Using a View Port for Scrolling
-------------------------------

What if one screen isn't enough to hold your maze of walls? We can have a
world that is larger than just our window. We do this by adjusting the
*view port*. Normally coordinate (0, 0) is the lower left corner of our screen.
We can change that! We could have an entire world stretch from (0, 0) to
(3000, 3000), and have a smaller view port that was 800x640 that scrolled
around that.

The command for using the view port is ``set_viewport``. This command takes
four arguments. The first two are the left and bottom boundaries of the window.
By default these are zero. That is why (0, 0) is in the lower left of the
screen. The next two commands are the top and right coordinates of the screen.
By default these are the screen width and height, minus one. So an 800
pixel-wide window would have x-coordinates from 0 - 799.

A command like this would shift the whole "view" of the window 200 pixels to
the right:

.. code-block:: python

    arcade.set_viewport(200, 0, 200 + SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)

So with a 800 wide pixel window, we would show x-coordinates 200 - 999 instead
of 0 - 799.

Instead of hard-coding the shift at 200 pixels, we need to use a variable
and have rules around when to shift the view. In our next example, we will
create two new instance variables in our application class that hold the left
and bottom coordinates for our view port. We'll default to zero.

.. code-block:: python

    self.view_left = 0
    self.view_bottom = 0


We are also going to create two new constants. We don't want the player to
reach the edge of the screen before we start scrolling. Because then the player
would have no idea where she is going. In our example we will set a "margin" of
40 pixels. When the player is 40 pixels from the edge of the screen, we'll move
the view port so she can see at least 40 pixels around her.

.. code-block:: python

    VIEWPORT_MARGIN = 40

Next, in our update method, we need to see if the user has moved too close to
the edge of the screen and we need to update the boundaries.

.. code-block:: python

    # Keep track of if we changed the boundary. We don't want to call the
    # set_viewport command if we didn't change the view port.
    changed = False

    # Scroll left
    left_bndry = self.view_left + VIEWPORT_MARGIN
    if self.player_sprite.left < left_bndry:
        self.view_left -= left_bndry - self.player_sprite.left
        changed = True

    # Scroll right
    right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
    if self.player_sprite.right > right_bndry:
        self.view_left += self.player_sprite.right - right_bndry
        changed = True

    # Scroll up
    top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
    if self.player_sprite.top > top_bndry:
        self.view_bottom += self.player_sprite.top - top_bndry
        changed = True

    # Scroll down
    bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
    if self.player_sprite.bottom < bottom_bndry:
        self.view_bottom -= bottom_bndry - self.player_sprite.bottom
        changed = True

    # Make sure our boundaries are integer values. While the view port does
    # support floating point numbers, for this application we want every pixel
    # in the view port to map directly onto a pixel on the screen. We don't want
    # any rounding errors.
    self.view_left = int(self.view_left)
    self.view_bottom = int(self.view_bottom)

    # If we changed the boundary values, update the view port to match
    if changed:
        arcade.set_viewport(self.view_left,
                            SCREEN_WIDTH + self.view_left - 1,
                            self.view_bottom,
                            SCREEN_HEIGHT + self.view_bottom - 1)

The full example is below:

.. literalinclude:: sprite_move_scrolling.py
    :caption: sprite_move_scrolling.py
    :language: python
    :linenos:
