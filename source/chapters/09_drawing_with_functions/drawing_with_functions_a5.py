import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT / 3, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(300 + x, 200 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 280 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300 + x, 340 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285 + x, 350 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315 + x, 350 + y, 5, arcade.color.BLACK)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    draw_snow_person(50, 50)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
