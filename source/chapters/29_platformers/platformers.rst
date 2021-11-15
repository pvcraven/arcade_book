.. _platformers:

Platformers
===========

Full tutorials:

* See the `Simple Platformer Tutorial <https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html>`_.
* For more advanced usage, see `Platformer with Physics <https://api.arcade.academy/en/latest/tutorials/pymunk_platformer/index.html>`_.

Short notes:

Download/install tiled from here:
https://www.mapeditor.org/

Use your own same-sized tiles, or download from resourced tab on class website.

Make sure tileset and map are stored in JSON format.

Simple terms, start with:

https://api.arcade.academy/en/latest/examples/sprite_move_scrolling.html

In your setup, you can load a map like this:

.. code-block:: python

    map_name = "level1.json"

    # Read in the tiled map
    self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALING)

    # Set wall and coin SpriteLists
    self.wall_list = self.tile_map.sprite_lists["Walls"]
    # self.coin_list = self.tile_map.sprite_lists["Coins"]

    # --- Other stuff
    # Set the background color
    if self.tile_map.background_color:
        arcade.set_background_color(self.tile_map.background_color)

    # Keep player from running through the wall_list layer
    self.physics_engine = arcade.PhysicsEnginePlatformer(
        self.player_sprite, self.wall_list, gravity_constant=GRAVITY
    )

    # Set the background color
    arcade.set_background_color(arcade.color.AMAZON)

Then

.. code-block:: python

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED


.. literalinclude:: main.py
    :caption: main.py
    :language: python
    :linenos:

.. literalinclude:: main_better.py
    :caption: main_better.py
    :language: python
    :linenos: