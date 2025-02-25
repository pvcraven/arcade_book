"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.WHITE)

# Get ready to draw
arcade.start_render()

# Draw an ellipse and rect with
# a center of (300, 300)
# width of 350
# height of 200
arcade.draw_rect_outline(arcade.XYWH(300, 300, 350, 200), arcade.csscolor.BLACK, 3)
arcade.draw_ellipse_outline(300, 300, 350, 200, arcade.csscolor.RED, 3)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
