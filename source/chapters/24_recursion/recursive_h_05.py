"""
Recursive H's
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

RECURSION_DEPTH = 0


def draw_h(x, y, width, height, count):
    """ Recursively draw an H, each one a half as big """

    # Draw the H
    # Draw cross-bar
    arcade.draw_line(x + width * .25, height / 2 + y,
                     x + width * .75, height / 2 + y, arcade.color.BLACK)
    # Draw left side
    arcade.draw_line(x + width * .25, height * .5 / 2 + y,
                     x + width * .25, height * 1.5 / 2 + y, arcade.color.BLACK)
    # Draw right side
    arcade.draw_line(x + width * .75, height * .5 / 2 + y,
                     x + width * .75, height * 1.5 / 2 + y, arcade.color.BLACK)

    # As long as we have a width bigger than 1, recursively call this function with a smaller rectangle
    if count > 0:
        count -= 1
        # Draw the rectangle 90% of our current size
        # Draw lower left
        draw_h(x, y, width / 2, height / 2, count)
        # Draw lower right
        draw_h(x + width / 2, y, width / 2, height / 2, count)
        # Draw upper left
        draw_h(x, y + height / 2, width / 2, height / 2, count)
        # Draw upper right
        draw_h(x + width / 2, y + height / 2, width / 2, height / 2, count)


class MyWindow(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Start our recursive calls
        draw_h(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, RECURSION_DEPTH)


def main():
    MyWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
