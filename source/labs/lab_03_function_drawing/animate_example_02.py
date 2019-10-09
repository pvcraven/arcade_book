import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Size of the rectangle
RECT_WIDTH = 50
RECT_HEIGHT = 50


def on_draw(delta_time):
    """
    Use this function to draw everything to the screen.
    This function will be called over and over because of the "schedule"
    command below.
    """

    arcade.start_render()

    # Draw a rectangle.
    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y,
                                 RECT_WIDTH, RECT_HEIGHT,
                                 arcade.color.ALIZARIN_CRIMSON)

    # Modify rectangle's position
    on_draw.center_x += 1
    on_draw.center_y += 1


on_draw.center_x = 100      # Initial x position
on_draw.center_y = 50       # Initial y position


def main():
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncing Rectangle Example")
    arcade.set_background_color(arcade.color.WHITE)

    # The "schedule" command
    # Tell the computer to call the draw command 80 times per second
    arcade.schedule(on_draw, 1 / 80)

    # Run the program
    arcade.run()


main()
