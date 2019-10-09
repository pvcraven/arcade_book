
Using Sprites to Shoot
======================

How do we get sprites that we can shoot?

.. figure:: sprites_bullet.gif

    Coins shooting

Getting Started
---------------
First, let's go back to a program to start with.

.. literalinclude:: sprites_bullet_01.py
    :caption: Starting program for shooting sprites
    :language: python
    :linenos:

If you run this program, the player should move around the screen, and their
should be coins. But not much else is happening yet.

Next, we need a 'shooting' image:

.. figure:: laserBlue01.png

    laserBlue01.png

Download this image (originally from Kenney.nl) and make sure it is in the same
folder as your code.

Keeping The Player At The Bottom
--------------------------------

Right now the player can move anywhere on the screen. We want to keep that
sprite fixed to the bottom of the screen.

To do that, just remove the line of code for moving the player on the y-axis.
The player will keep the same y value that we set back in the ``setup`` method.

.. code-block:: Python
    :emphasize-lines: 6

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        # REMOVE THIS LINE: self.player_sprite.center_y = y

Moving The Coins Up
-------------------

We want all the coins above the player. So we can adjust the starting y locations
to have a starting point of 150 instead of 0. That will keep them above the player.

.. code-block:: Python
    :emphasize-lines: 10

    # Create the coins
    for i in range(COIN_COUNT):

        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(150, SCREEN_HEIGHT)

        # Add the coin to the lists
        self.coin_list.append(coin)

Set Up Bullet List
------------------

We need to create a list to manage the bullets. There are four places we need to
add this ``bullet_list`` code:

* Create the ``bullet_list`` variable (Line 26)
* Create an instance of ``SpriteList`` (Line 44)
* Draw the bullet list (Line 83)
* Update the bullet list (Line 105)

.. literalinclude:: sprites_bullet_02.py
    :caption: Set up bullet list
    :language: python
    :emphasize-lines: 26, 44, 83, 105
    :linenos:

Creating Bullets
----------------
We need to
create bullets when the user presses the mouse button. We can add an
``on_mouse_press`` method to do something when the user presses the mouse button:

.. code-block:: Python

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

This will create a bullet, but the bullet will default to the lower left corner.
You can just barely see it.

We can give the bullet a position:

.. code-block:: Python
    :emphasize-lines: 6-7

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.center_x = x
        bullet.center_y = y

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

But this isn't what we want either. The code above puts the laser where we click
the mouse. We want the laser to be where the player is. That's easy:

.. code-block:: Python
    :emphasize-lines: 6-7

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

We can even start the player a bit ABOVE the player:

.. code-block:: Python
    :emphasize-lines: 6-7

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y + 30

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

We can make the bullet move up using the constant ``BULLET_SPEED`` which
we set to 5 at the top of the program:

.. code-block:: Python
    :emphasize-lines: 8

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)

We can rotate the bullet so it isn't sideways using the ``angle`` attribute
built into the ``Sprite`` class:

.. code-block:: Python
    :emphasize-lines: 9

    def on_mouse_press(self, x, y, button, modifiers):

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)

        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y + 30
        bullet.change_y = BULLET_SPEED
        bullet.angle = 90

        # Add the bullet to the appropriate list
        self.bullet_list.append(bullet)


Bullet Collisions
-----------------

Now that we have bullets, how do we get them to collide with the coins?
We add the following to our applications ``update`` method:

.. code-block:: Python

    # Loop through each bullet
    for bullet in self.bullet_list:

        # Check this bullet to see if it hit a coin
        hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

        # If it did, get rid of the bullet
        if len(hit_list) > 0:
            bullet.remove_from_sprite_lists()

        # For every coin we hit, add to the score and remove the coin
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # If the bullet flies off-screen, remove it.
        if bullet.bottom > SCREEN_HEIGHT:
            bullet.remove_from_sprite_lists()

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

Other Examples
--------------

Here are some other examples from `Arcade Academy <http://arcade.academy>`_
and its `Example List <http://arcade.academy/examples/index.html>`_:

* `Aim bullets with mouse <http://arcade.academy/examples/sprite_bullets_aimed.html>`_
* `Enemies shoot periodically <http://arcade.academy/examples/sprite_bullets_periodic.html>`_
* `Enemies shoot at random times <http://arcade.academy/examples/sprite_bullets_random.html>`_
* `Enemies aim at player <http://arcade.academy/examples/sprite_bullets_enemy_aims.html>`_
* `Explosions <http://arcade.academy/examples/sprite_explosion.html>`_
