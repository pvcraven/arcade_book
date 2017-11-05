.. _lab-09:

Lab 9: Sprites and Walls
========================

Goal: Create a landscape of wall objects that the user must navigate around to
collect coins. This will help practice using ``for`` loops to create
and position multiple items.

.. image:: lab9.gif

* Step 1: Start with one of the move with walls examples.
  Use either the `Move with Walls`_ example or the `Move with a Scrolling Screen`_ example.
* Step 2: Create a more complex arrangement of walls. Make sure the walls don't
  allow the user to go off-screen. 6 points, based on how complex the
  arrangement.
* Step 3: Update the graphics. Use multiple types of blocks for the walls. Maybe
  change the character. 4 points, one point for each graphic used that wasn't
  part of the base example.
* Step 4: Add coins (or something) for the user to collect. 4 points, based on
  the complexity of the coin layout.
* Step 5: Keep score of how many coins were collected, and display on-screen.
  4 points.
* Step 6: Add a sound to play each time the user collects a coin. 2 points.

.. warning::
    Don't move the player twice!

    The command ``self.physics_engine.update()`` moves the player while checking
    for walls. The command ``self.all_sprites_list.update()`` will move the
    player WITHOUT checking for walls. Don't do both commands. You'll end up
    "walking through walls." If you have other
    sprites to update, update only those sprites. For example:
    ``self.coin_list.update()``.


.. _Move with Walls: http://arcade.academy/examples/sprite_move_walls.html
.. _Move with a Scrolling Screen: http://arcade.academy/examples/sprite_move_scrolling.html
