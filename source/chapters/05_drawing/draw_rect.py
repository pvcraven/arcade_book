"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.BITTER_LIME)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
