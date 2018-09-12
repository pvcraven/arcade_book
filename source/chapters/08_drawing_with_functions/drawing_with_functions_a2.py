import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    # Draw a snow person

    # Snow
    arcade.draw_circle_filled(300, 200, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 280, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(300, 340, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(285, 350, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(315, 350, 5, arcade.color.BLACK)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
