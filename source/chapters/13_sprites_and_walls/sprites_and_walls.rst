.. sectnum::
    :start: 13

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
