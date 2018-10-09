
Using Sprites to Shoot
======================

How do we get sprites that we can shoot?

First, we need a 'shooting' image:

.. figure:: laserBlue01.png

    laserBlue01.png

.. figure:: sprites_bullet.gif

    Coins shooting

To start with, we need a sprite to represent the bullet. It will be a
moving sprite:

.. code-block:: Python

    class Bullet(arcade.Sprite):
        def update(self):
            self.center_y += BULLET_SPEED

This gets the bullets to move up. But we don't have any bullets. We need to
create bullets when the user presses the mouse button. We can add an
``on_mouse_press`` method to do something when the user presses the mouse button:

.. code-block:: Python

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = Bullet("laserBlue01.png", SPRITE_SCALING * 1.5)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

The two key points with the code above is that 1.) We position the bullet right
above the player that spawned it:

.. code-block:: Python

    bullet.center_x = self.player_sprite.center_x
    bullet.bottom = self.player_sprite.top

And two, we can rotate a sprite! Since the bullet image has the bullet going
sideways, that's no good. There is an attribute with any sprite  that you can
set called ``angle``. So we just set the angle to 90 to rotate it.

.. code-block:: Python

    bullet.angle = 90

Now that we have bullets, how do we get them to collide with the coins?
We add the following to our applications ``update`` method:

.. code-block:: Python

    # Loop through each bullet
    for bullet in self.bullet_list:

        # Check this bullet to see if it hit a coin
        hit_list = arcade.check_for_collision_with_list(bullet,
                                                        self.coin_list)

        # If it did, get rid of the bullet
        if len(hit_list) > 0:
            bullet.kill()

        # For every coin we hit, add to the score and remove the coin
        for coin in hit_list:
            coin.kill()
            self.score += 1

        # If the bullet flies off-screen, remove it.
        if bullet.bottom > SCREEN_HEIGHT:
            bullet.kill()

We loop through each bullet with a ``for`` loop. Then we check to see if the
bullet is hitting any of the coins. If it is, we get rid of the coin. We get
rid of the bullet.

We also check to see if the bullet flies off the top of the screen. If it does,
we get rid of the bullet. This is easy to forget, but if you do, it will cause
the computer to slow down because you are tracking thousands of bullets that
have long ago left the space we care about.

Here's the full example:

.. literalinclude:: sprites_bullet.py
    :caption: sprites_bullet.py
    :language: python
    :linenos: