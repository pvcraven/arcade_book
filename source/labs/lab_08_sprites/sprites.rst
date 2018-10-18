.. _lab-08:

Lab 8: Sprites
==============

.. image:: lab_8.gif

* Create a player-character sprite. Feel free to pick your own image for the
  sprite.
* Allow the user to move the player move by the keyboard, mouse, or game pad.
  Your choice. If you use the mouse, make sure you hide it.
* Create "good" sprites. Pick your own image for the sprite.
* Create "bad" sprites. Pick your own image for the sprite.
* For each good sprite collected, make the score go up. Play a 'good' sound when
  the user collects that item.
* For each bad sprite touched, have the score go down. Play a 'bad' sound when
  the user collects that item.
* Animate/move the good sprites. Pick any of the motions we showed, or make your
  one.
* Move the bad sprites. Move them differently than the good ones.
* If the length of the good sprite list is zero, then don't move any of the
  sprites or the character. "Freeze" the game. To do this, note what line of
  the ``update`` method in the main window class causes the sprites to move.
  Then only run that line if you have sprites. (Check the length of the sprite
  list.) If you get that to work, the do something similar ``on_mouse_motion``.
* If the length of the good sprite list is zero, draw "Game Over" on the screen.
* Add, commit, and push via ``git``.
* Turn in a URL to your project.
