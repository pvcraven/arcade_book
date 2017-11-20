"""
Recursive Rectangles
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


def draw_rectangle(x, y, width, height):
    """ Recursively draw a rectangle, each one a percentage smaller """

    # Draw it
    arcade.draw_rectangle_outline(x, y, width, height, arcade.color.BLACK)

    # As long as we have a width bigger than 1, recursively call this function with a smaller rectangle
    if width > 1:
        # Draw the rectangle 90% of our current size
        draw_rectangle(x, y, width * .9, height * .9)


class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Find the center of our screen
        center_x = SCREEN_WIDTH / 2
        center_y = SCREEN_HEIGHT / 2

        # Start our recursive calls
        draw_rectangle(center_x, center_y, SCREEN_WIDTH, SCREEN_HEIGHT)


def main():

    MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
