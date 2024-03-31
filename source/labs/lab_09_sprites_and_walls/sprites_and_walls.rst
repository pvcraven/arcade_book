.. _lab-09:

Lab 9: Sprites and Walls
========================

Goal: Create a landscape of wall objects that the user must navigate around to
collect coins. This will help practice using ``for`` loops to create
and position multiple items.

.. image:: lab9.gif

* Step 1: Start with one these examples:

  * `Move with Walls`_ (easiest, no scrolling)
  * `Move with a Scrolling Screen`_ (recommended)
  * `Move Between Different Rooms`_ (more complex)

* Step 2: If you start with the examples, delete the current wall
  placement code. You want to create your own.
* Step 3: Create a more complex arrangement of walls. Make sure the walls don't
  allow the user to go off-screen. This is worth 30 points, based on how complex the
  arrangement. See :ref:`individual_wall_placement`, :ref:`loop_wall_placement`,
  and :ref:`list_wall_placement` for ideas. Just DON'T do the same thing as
  examples. Make it your own. Specifically, do NOT just copy the random wall-gap
  algorithm in the scrolling screen example.
* Step 4: Update the graphics. Use multiple types of blocks for the walls.
  (See note below.)
  Change the character. This is worth 20 points, five points for each graphic used
  that wasn't
  part of the base example. Remember to put a quick citation in your program just
  before you load graphics or sounds.

.. note::
  If you have more than one type of wall block,
  that's great. But you don't need more than one wall list. The physics engine
  requires all walls be kept in the same list.


* Step 5: Add coins (or something) for the user to collect. 20 points, based on
  the complexity of the coin layout. Remember, you can place coins like we placed
  wall blocks. If you randomly place coins, you might end up with coins on
  top of walls. See the "Important Part" around line 83 or so of
  the example
  `sprite_no_coins_on_walls.py <https://api.arcade.academy/en/latest/examples/sprite_no_coins_on_walls.html>`_
  for how to avoid this.
* Step 6: Keep score of how many coins were collected, and display on-screen.
  20 points.
* Step 7: Add a sound to play each time the user collects a coin. 10 points.

.. warning::
    Don't move the player twice!

    The command ``self.physics_engine.update()`` moves the player while checking
    for walls. The command ``self.all_sprites_list.update()`` will move the
    player WITHOUT checking for walls. Don't do both commands. You'll end up
    "walking through walls." If you have other
    sprites to update, update only those sprites. For example:
    ``self.coin_list.update()``.

Additional Challenges
---------------------

These aren't required for the lab, but I've had students ask in prior
years how to do these:

* This is a *great* project to use the
  `Move Better <https://api.arcade.academy/en/latest/examples/sprite_move_keyboard_better.html>`_ example, as
  you'll find player movement is a lot more predictable.
* If you are interested in having the player be able to face left or right,
  see the
  `Sprite Face Left or Right <https://api.arcade.academy/en/latest/examples/sprite_face_left_or_right.html>`_
  example.
* Want to animate walking? Look at the
  `Animate your sprites <https://api.arcade.academy/en/latest/examples/sprite_move_animation.html>`_. example.


.. _Move with Walls: https://api.arcade.academy/en/latest/examples/sprite_move_walls.html
.. _Move with a Scrolling Screen: https://api.arcade.academy/en/latest/examples/sprite_move_scrolling.html
.. _Move Between Different Rooms: https://api.arcade.academy/en/latest/examples/sprite_rooms.html