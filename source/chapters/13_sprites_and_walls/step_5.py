""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

VIEWPORT_MARGIN = 40


class MyWindow(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.all_sprites_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Manage the view port
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Reset the view port
        self.view_left = 0
        self.view_bottom = 0

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.all_sprites_list.append(self.player_sprite)

        # --- Manually place walls

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)
        self.all_sprites_list.append(wall)

        # Manually create and position a box at 364, 200
        wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)
        self.all_sprites_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)
            self.all_sprites_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)
            self.all_sprites_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def update(self, delta_time):
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

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

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyWindow()
    window.setup()
    arcade.run()


main()