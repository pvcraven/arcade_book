""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5

class MyWindow(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")


    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()


def main():
    window = MyWindow()
    window.setup()
    arcade.run()


main()
