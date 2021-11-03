.. _lab-08:

Lab 8: Sprites
==============

.. image:: lab_8.gif

* Make sure you understand the code from :ref:`sprites`. The example code there
  is great to get started with.
* Create a player-character sprite. Pick your own image for the
  sprite, from the web or from Kenney.nl.
* Allow the user to move the player move by the keyboard, mouse, or game pad.
  Your choice. If you use the mouse, make sure you hide the cursor.
  The :ref:`sprites` chapter uses the mouse, you can also look at the examples on
  the Arcade website for
  `Sprite Player Movement <https://api.arcade.academy/en/latest/examples/index.html#sprite-player-movement>`_.
  These examples show mouse, keyboard, improved keyboard, and the game controller.
* Create "good" sprites. Pick your own image for the good sprite.
* For each good sprite collected, make the score go up. Play a 'good' sound when
  the user collects that item.
* Create "bad" sprites. Pick your own image for the bad sprite.
* For each bad sprite touched, have the score go down. Play a 'bad' sound when
  the user collects that item.

.. note:: A common mistake at this stage is to overwrite your list:

    .. code-block:: python

      hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
      hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
      for good_sprite in hit_list:
          # Process
      for bad_sprite in hit_list:
          # Process

    This would cause bad sprites to be processed twice, because the original `hit_list`
    is overwritten. Instead try:

    .. code-block:: python

      hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
      for good_sprite in hit_list:
          # Process
      hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
      for bad_sprite in hit_list:
          # Process

    or:

    .. code-block:: python

      good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)
      bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
      for good_sprite in good_hit_list:
          # Process
      for bad_sprite in bad_hit_list:
          # Process

* Animate/move the good sprites. Pick any of the motions we showed, such as move
  and reset, bounce, go in circles, or a pattern. You can even make your
  own. Try a sine-waves!
* Move the bad sprites. Move them differently than the good ones.
* If the length of the good sprite list is zero, then don't move any of the
  sprites or the character. "Freeze" the game.

  * Fine where in the the ``update`` method in the main window class causes the sprites to move.
  * Only run that line if you have good sprites. (Check the length of the sprite
    list. The logic is kind of opposite you you think. Instead of freezing at zero, you are
    not moving things if the length is bigger than zero.)
  * Remember, the ``len`` gets the length of the list. Compare the length of the list to 0, not
    the list itself.
  * If you get that to work, the do something similar ``on_mouse_motion``.

* If the length of the good sprite list is zero, draw "Game Over" on the screen.
* Add, commit, and push via ``git``.
* Turn in a URL to your project.
